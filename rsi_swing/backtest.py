"""Weekly-RSI oversold swing-trade backtester.

Strategy under test
-------------------
1. Build weekly candles (Friday close) from daily prices.
2. Compute 14-period Wilder RSI on the weekly closes.
3. A *signal* fires on the first week whose RSI closes at or below the
   threshold (default 32). Consecutive oversold weeks belong to the same
   episode; the strategy re-arms only after RSI has closed back above the
   `rearm` level (default: the threshold itself). `--every-week` instead
   treats every oversold week as its own trade (overlapping positions).
4. Enter at the next week's open (default) or the signal week's close.
5. Measure the return N months after entry for N in [min_hold, max_hold]
   (default 4..10 months), plus the best / worst exit available inside that
   window and the max drawdown suffered before the window opens.

Returns use dividend-adjusted prices (total return) unless --price-only.
The RSI is always computed on split-adjusted (not dividend-adjusted) closes,
which is what a chart would have shown at the time.

Usage
-----
    python backtest.py QCOM                      # default: threshold 32, 4-10 months
    python backtest.py QCOM --threshold 30 --min-hold 3 --max-hold 12
    python backtest.py QCOM AAPL INTC --sweep 25,28,30,32,35,38,40
    python backtest.py QCOM --start 1996-01-01   # limit history
    python backtest.py QCOM --every-week          # every oversold week = a trade

Outputs (rsi_swing/output/):
    <TICKER>_t<threshold>_trades.csv    one row per trade with every horizon
    <TICKER>_t<threshold>_summary.md    summary tables
    <TICKER>_sweep.csv                  when --sweep is used
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from prices import load_daily  # noqa: E402

OUT = HERE / "output"


# ------------------------------------------------------------------ indicators
def wilder_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    """Textbook Wilder RSI (SMA seed, then alpha=1/period smoothing)."""
    c = close.to_numpy(dtype=float)
    n = len(c)
    out = np.full(n, np.nan)
    if n <= period:
        return pd.Series(out, index=close.index, name="rsi")
    d = np.diff(c)
    gains = np.where(d > 0, d, 0.0)
    losses = np.where(d < 0, -d, 0.0)
    ag = gains[:period].mean()
    al = losses[:period].mean()
    out[period] = 100.0 if al == 0 else 100.0 - 100.0 / (1.0 + ag / al)
    for i in range(period, n - 1):
        ag = (ag * (period - 1) + gains[i]) / period
        al = (al * (period - 1) + losses[i]) / period
        out[i + 1] = 100.0 if al == 0 else 100.0 - 100.0 / (1.0 + ag / al)
    return pd.Series(out, index=close.index, name="rsi")


def weekly_bars(daily: pd.DataFrame) -> pd.DataFrame:
    """Calendar-week candles (label = the Friday of that week)."""
    w = pd.DataFrame({
        "Open": daily["Open"].resample("W-FRI").first(),
        "High": daily["High"].resample("W-FRI").max(),
        "Low": daily["Low"].resample("W-FRI").min(),
        "Close": daily["Close"].resample("W-FRI").last(),
        "AdjClose": daily["AdjClose"].resample("W-FRI").last(),
        "AdjOpen": (daily["Open"] * daily["AdjClose"] / daily["Close"]).resample("W-FRI").first(),
        "Volume": daily["Volume"].resample("W-FRI").sum(),
    }).dropna(subset=["Close"])
    return w


def daily_bars(daily: pd.DataFrame) -> pd.DataFrame:
    """Daily candles in the same layout as weekly_bars (for --timeframe daily)."""
    d = daily.copy()
    d["AdjOpen"] = d["Open"] * d["AdjClose"] / d["Close"]
    return d


def make_bars(daily: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    return daily_bars(daily) if timeframe == "daily" else weekly_bars(daily)


# --------------------------------------------------------------------- signals
def find_signals(rsi: pd.Series, threshold: float, rearm: float | None = None,
                 every_week: bool = False) -> list[pd.Timestamp]:
    """Weeks on which a trade is triggered.

    Default: the first week RSI <= threshold, then nothing until RSI has
    closed above `rearm` (>= threshold) again. every_week: all oversold weeks.
    """
    rearm = threshold if rearm is None else rearm
    signals: list[pd.Timestamp] = []
    armed = True
    for dt, v in rsi.items():
        if np.isnan(v):
            continue
        if v <= threshold:
            if every_week or armed:
                signals.append(dt)
            armed = False
        elif v > rearm:
            armed = True
    return signals


# ---------------------------------------------------------------------- trades
def _price_on_or_after(series: pd.Series, when: pd.Timestamp):
    """(date, value) of the first bar on/after `when`, or (None, nan)."""
    pos = series.index.searchsorted(when)
    if pos >= len(series):
        return None, np.nan
    return series.index[pos], float(series.iloc[pos])


def build_trades(daily: pd.DataFrame, weekly: pd.DataFrame, rsi: pd.Series,
                 signals: list[pd.Timestamp], min_hold: int, max_hold: int,
                 entry: str = "next_open", price_only: bool = False) -> pd.DataFrame:
    """One row per signal with the forward return at every monthly horizon."""
    px_col = "Close" if price_only else "AdjClose"
    d_px = daily[px_col]
    w_px = weekly[px_col]
    rows = []
    last_date = daily.index[-1]
    horizons = list(range(min_hold, max_hold + 1))

    for sig in signals:
        w_pos = weekly.index.get_loc(sig)
        if entry == "next_open":
            if w_pos + 1 >= len(weekly):
                continue
            nxt = weekly.index[w_pos + 1]
            # first daily bar of the following week
            e_date, _ = _price_on_or_after(daily["Open"], sig + pd.Timedelta(days=1))
            if e_date is None or e_date > nxt:
                continue
            e_px = float(daily.loc[e_date, "Open"] * (1 if price_only else daily.loc[e_date, "AdjClose"] / daily.loc[e_date, "Close"]))
        else:  # signal week close
            e_date = daily.loc[:sig].index[-1]
            e_px = float(d_px.loc[e_date])

        row = {
            "signal_week": sig.date(),
            "rsi": round(float(rsi.loc[sig]), 2),
            "entry_date": e_date.date(),
            "entry_px": round(e_px, 4),
        }
        complete = True
        for n in horizons:
            target = e_date + pd.DateOffset(months=n)
            x_date, x_px = _price_on_or_after(d_px, target)
            if x_date is None or target > last_date:
                row[f"ret_{n}m"] = np.nan
                complete = False
            else:
                row[f"ret_{n}m"] = x_px / e_px - 1.0
        # window statistics (weekly closes between min_hold and max_hold months)
        w_start = e_date + pd.DateOffset(months=min_hold)
        w_end = e_date + pd.DateOffset(months=max_hold)
        window = w_px.loc[w_start:w_end]
        pre = w_px.loc[e_date:w_start]
        if len(window) and w_end <= last_date:
            row["best_in_window"] = float(window.max() / e_px - 1.0)
            row["best_date"] = window.idxmax().date()
            row["worst_in_window"] = float(window.min() / e_px - 1.0)
            row["worst_date"] = window.idxmin().date()
            row["mean_in_window"] = float((window / e_px - 1.0).mean())
        else:
            row["best_in_window"] = row["worst_in_window"] = row["mean_in_window"] = np.nan
            row["best_date"] = row["worst_date"] = None
        # pain before the exit window opens
        row["max_dd_pre_window"] = float(pre.min() / e_px - 1.0) if len(pre) else np.nan
        full = w_px.loc[e_date:w_end]
        row["max_dd_to_10m"] = float(full.min() / e_px - 1.0) if len(full) else np.nan
        row["complete"] = complete
        rows.append(row)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- target study
def target_trades(daily: pd.DataFrame, trades: pd.DataFrame, target: float,
                  price_only: bool = False) -> pd.DataFrame:
    """For every signal: hold until the first daily close >= entry*(1+target).
    No time limit. Reports months to target, the worst close on the way, and
    for signals that never got there, where they stand now."""
    px = daily["Close" if price_only else "AdjClose"]
    last = daily.index[-1]
    rows = []
    for t in trades.itertuples():
        e = pd.Timestamp(t.entry_date)
        path = px.loc[e:] / t.entry_px - 1.0
        hit = path[path >= target]
        row = {"signal_week": t.signal_week, "rsi": t.rsi, "entry_date": t.entry_date, "entry_px": t.entry_px}
        if len(hit):
            x = hit.index[0]
            pre = path.loc[:x]
            row.update(hit=True, exit_date=x.date(), months=(x - e).days / 30.4375,
                       exit_return=float(hit.iloc[0]), worst_before=float(pre.min()),
                       worst_date=pre.idxmin().date())
        else:
            row.update(hit=False, exit_date=None, months=(last - e).days / 30.4375,
                       exit_return=float(path.iloc[-1]), worst_before=float(path.min()),
                       worst_date=path.idxmin().date())
        rows.append(row)
    return pd.DataFrame(rows)


def target_summary(tt: pd.DataFrame) -> dict:
    if tt.empty:
        return {}
    h = tt[tt["hit"]]
    return {
        "signals": int(len(tt)), "hit": int(len(h)), "open": int((~tt["hit"]).sum()),
        "avg_months": float(h["months"].mean()) if len(h) else float("nan"),
        "median_months": float(h["months"].median()) if len(h) else float("nan"),
        "max_months": float(h["months"].max()) if len(h) else float("nan"),
        "within_4m": int((h["months"] <= 4).sum()), "within_10m": int((h["months"] <= 10).sum()),
        "within_12m": int((h["months"] <= 12).sum()), "within_24m": int((h["months"] <= 24).sum()),
        "avg_worst": float(tt["worst_before"].mean()), "min_worst": float(tt["worst_before"].min()),
        "n_worse_20": int((tt["worst_before"] <= -0.20).sum()),
    }


def target_table(tt: pd.DataFrame) -> str:
    lines = ["| Signal | RSI | Entry | Entry px | Reached | Months | Return | Worst on the way | Worst date |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in tt.itertuples():
        lines.append(f"| {r.signal_week} | {r.rsi} | {r.entry_date} | {r.entry_px} | "
                     f"{r.exit_date if r.hit else '**not yet**'} | {r.months:.1f} | {pct(r.exit_return)} | "
                     f"{pct(r.worst_before)} | {r.worst_date} |")
    return "\n".join(lines)


# ------------------------------------------------------------------- summaries
def summarise(trades: pd.DataFrame, min_hold: int, max_hold: int) -> pd.DataFrame:
    """Per-horizon statistics over completed trades."""
    if trades.empty or "complete" not in trades:
        return pd.DataFrame()
    t = trades[trades["complete"]]
    recs = []
    for n in range(min_hold, max_hold + 1):
        r = t[f"ret_{n}m"].dropna()
        if r.empty:
            continue
        recs.append({
            "horizon_m": n,
            "trades": int(len(r)),
            "win_rate": float((r > 0).mean()),
            "avg": float(r.mean()),
            "median": float(r.median()),
            "min": float(r.min()),
            "max": float(r.max()),
            "losses": int((r <= 0).sum()),
            "avg_loss": float(r[r <= 0].mean()) if (r <= 0).any() else 0.0,
            "avg_win": float(r[r > 0].mean()) if (r > 0).any() else 0.0,
        })
    return pd.DataFrame(recs)


def window_summary(trades: pd.DataFrame, min_hold: int, max_hold: int) -> dict:
    if trades.empty or "complete" not in trades:
        return {}
    t = trades[trades["complete"]]
    if t.empty:
        return {}
    ret_cols = [f"ret_{n}m" for n in range(min_hold, max_hold + 1)]
    any_loss = (t[ret_cols] <= 0).any(axis=1)
    all_loss = (t[ret_cols] <= 0).all(axis=1)
    return {
        "trades": int(len(t)),
        "avg_of_window_mean": float(t["mean_in_window"].mean()),
        "avg_best_exit": float(t["best_in_window"].mean()),
        "avg_worst_exit": float(t["worst_in_window"].mean()),
        "worst_single_exit": float(t["worst_in_window"].min()),
        "trades_with_any_loss_point": int(any_loss.sum()),
        "trades_negative_all_horizons": int(all_loss.sum()),
        "trades_never_below_entry_in_window": int((t["worst_in_window"] > 0).sum()),
        "avg_max_dd_pre_window": float(t["max_dd_pre_window"].mean()),
        "worst_max_dd_pre_window": float(t["max_dd_pre_window"].min()),
        "avg_max_dd_to_end": float(t["max_dd_to_10m"].mean()),
        "worst_max_dd_to_end": float(t["max_dd_to_10m"].min()),
    }


def baseline(daily: pd.DataFrame, weekly: pd.DataFrame, min_hold: int, max_hold: int,
             price_only: bool = False) -> pd.DataFrame:
    """Unconditional forward returns from *every* week — the base rate to beat."""
    px_col = "Close" if price_only else "AdjClose"
    d_px = daily[px_col]
    last = daily.index[-1]
    recs = []
    for n in range(min_hold, max_hold + 1):
        rets = []
        for dt, p in weekly[px_col].items():
            target = dt + pd.DateOffset(months=n)
            if target > last:
                break
            _, x = _price_on_or_after(d_px, target)
            rets.append(x / p - 1.0)
        r = pd.Series(rets)
        recs.append({"horizon_m": n, "weeks": len(r), "win_rate": float((r > 0).mean()),
                     "avg": float(r.mean()), "median": float(r.median()), "min": float(r.min())})
    return pd.DataFrame(recs)


# ------------------------------------------------------------------ formatting
def pct(x) -> str:
    return "n/a" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x * 100:+.1f}%"


def md_table(df: pd.DataFrame, pct_cols: set[str]) -> str:
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if c in pct_cols:
                cells.append(pct(v))
            elif isinstance(v, float) and float(v).is_integer():
                cells.append(str(int(v)))
            elif isinstance(v, float):
                cells.append(f"{v:.2f}")
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def trades_table(trades: pd.DataFrame, min_hold: int, max_hold: int) -> str:
    cols = ["signal_week", "rsi", "entry_date", "entry_px"] + \
           [f"ret_{n}m" for n in range(min_hold, max_hold + 1)] + \
           ["best_in_window", "worst_in_window", "max_dd_pre_window"]
    pct_cols = {c for c in cols if c.startswith("ret_") or c.endswith("window")}
    return md_table(trades[cols], pct_cols)


def run_one(ticker: str, args) -> tuple[pd.DataFrame, pd.DataFrame, dict, pd.DataFrame]:
    daily = load_daily(ticker, refresh=args.refresh)
    if daily is None:
        raise SystemExit(f"{ticker}: no price data")
    if args.start:
        daily = daily.loc[args.start:]
    if args.end:
        daily = daily.loc[:args.end]
    weekly = make_bars(daily, args.timeframe)
    rsi = wilder_rsi(weekly["Close"], args.rsi_period)
    signals = find_signals(rsi, args.threshold, args.rearm, args.every_week)
    trades = build_trades(daily, weekly, rsi, signals, args.min_hold, args.max_hold,
                          entry=args.entry, price_only=args.price_only)
    summ = summarise(trades, args.min_hold, args.max_hold)
    win = window_summary(trades, args.min_hold, args.max_hold)
    base = baseline(daily, weekly, args.min_hold, args.max_hold, args.price_only)
    if getattr(args, "target", None):
        trades.attrs["target"] = target_trades(daily, trades, args.target, args.price_only)
    return trades, summ, win, base, daily, weekly, rsi


def write_report(ticker: str, args, trades, summ, win, base, daily, weekly, rsi) -> Path:
    OUT.mkdir(exist_ok=True)
    tag = f"{ticker}_{'d' if args.timeframe == 'daily' else 'w'}_t{args.threshold:g}"
    trades.to_csv(OUT / f"{tag}_trades.csv", index=False)
    lines = [
        f"# {ticker} — {args.timeframe} RSI({args.rsi_period}) ≤ {args.threshold:g} swing study",
        "",
        f"- Data: {daily.index[0].date()} → {daily.index[-1].date()} "
        f"({len(weekly)} {args.timeframe} bars, {'price only' if args.price_only else 'total return'})",
        f"- Entry: {'next bar open' if args.entry == 'next_open' else 'signal bar close'}; "
        f"re-arm when RSI closes above {args.rearm if args.rearm is not None else args.threshold:g}"
        + ("; every oversold bar is a trade" if args.every_week else "; first bar of each episode only"),
        f"- Exit window: {args.min_hold}–{args.max_hold} months after entry",
        f"- Signals: {len(trades)} (completed: {int(trades['complete'].sum()) if len(trades) else 0})",
        "",
        "## Return by fixed exit horizon (completed trades)",
        "",
        md_table(summ, {"win_rate", "avg", "median", "min", "max", "avg_loss", "avg_win"}) if len(summ) else "_no completed trades_",
        "",
        f"## Whole-window view ({args.min_hold}–{args.max_hold} month exit range)",
        "",
    ]
    if win:
        lines += [
            f"- Trades: {win['trades']}",
            f"- Average return across the window: {pct(win['avg_of_window_mean'])}",
            f"- Average best exit inside the window: {pct(win['avg_best_exit'])}",
            f"- Average worst exit inside the window: {pct(win['avg_worst_exit'])}; "
            f"single worst: {pct(win['worst_single_exit'])}",
            f"- Trades that stayed above entry at every weekly close in the window: "
            f"{win['trades_never_below_entry_in_window']} / {win['trades']}",
            f"- Trades with at least one losing month-end horizon: {win['trades_with_any_loss_point']} / {win['trades']}",
            f"- Trades negative at every horizon: {win['trades_negative_all_horizons']} / {win['trades']}",
            f"- Drawdown before the window opens (entry → month {args.min_hold}): "
            f"avg {pct(win['avg_max_dd_pre_window'])}, worst {pct(win['worst_max_dd_pre_window'])}",
            f"- Max drawdown entry → month {args.max_hold}: avg {pct(win['avg_max_dd_to_end'])}, "
            f"worst {pct(win['worst_max_dd_to_end'])}",
        ]
    tt = trades.attrs.get("target")
    if tt is not None and len(tt):
        ts = target_summary(tt)
        lines += [
            "",
            f"## Hold until +{args.target * 100:g}% (no time limit)",
            "",
            f"- Reached the target: {ts['hit']} of {ts['signals']} signals; still waiting: {ts['open']}",
            f"- Months to target: median {ts['median_months']:.1f}, average {ts['avg_months']:.1f}, longest {ts['max_months']:.1f}",
            f"- Reached within 4 / 10 / 12 / 24 months: {ts['within_4m']} / {ts['within_10m']} / {ts['within_12m']} / {ts['within_24m']}",
            f"- Worst close before the target: average {pct(ts['avg_worst'])}, single worst {pct(ts['min_worst'])}; "
            f"{ts['n_worse_20']} signals fell 20% or more first",
            "",
            target_table(tt),
        ]
    lines += [
        "",
        "## Base rate: forward return from *any* week (no signal)",
        "",
        md_table(base, {"win_rate", "avg", "median", "min"}),
        "",
        "## Trades",
        "",
        trades_table(trades, args.min_hold, args.max_hold) if len(trades) else "_none_",
        "",
    ]
    p = OUT / f"{tag}_summary.md"
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


def sweep(ticker: str, args, thresholds: list[float]) -> pd.DataFrame:
    recs = []
    for th in thresholds:
        a = argparse.Namespace(**vars(args))
        a.threshold = th
        trades, summ, win, base, *_ = run_one(ticker, a)
        if not win:
            recs.append({"ticker": ticker, "threshold": th, "trades": len(trades)})
            continue
        t = trades[trades["complete"]]
        ret_cols = [f"ret_{n}m" for n in range(args.min_hold, args.max_hold + 1)]
        recs.append({
            "ticker": ticker, "threshold": th, "signals": len(trades), "trades": win["trades"],
            "avg_window": win["avg_of_window_mean"],
            "median_window": float(t["mean_in_window"].median()),
            "win_rate_window_mean": float((t["mean_in_window"] > 0).mean()),
            "avg_best": win["avg_best_exit"], "avg_worst": win["avg_worst_exit"],
            "worst_single": win["worst_single_exit"],
            "any_loss_pt": win["trades_with_any_loss_point"],
            "all_neg": win["trades_negative_all_horizons"],
            "worst_dd_to_end": win["worst_max_dd_to_end"],
            **{f"avg_{n}m": float(t[f"ret_{n}m"].mean()) for n in range(args.min_hold, args.max_hold + 1)},
        })
    return pd.DataFrame(recs)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--threshold", type=float, default=32.0, help="weekly RSI trigger (<=)")
    ap.add_argument("--rearm", type=float, default=None,
                    help="RSI must close above this to allow a new signal (default: threshold)")
    ap.add_argument("--rsi-period", type=int, default=14)
    ap.add_argument("--timeframe", choices=["weekly", "daily"], default="weekly",
                    help="bar size for the RSI (default weekly)")
    ap.add_argument("--min-hold", type=int, default=4, help="months")
    ap.add_argument("--max-hold", type=int, default=10, help="months")
    ap.add_argument("--entry", choices=["next_open", "close"], default="next_open")
    ap.add_argument("--every-week", action="store_true", help="every oversold week is a trade")
    ap.add_argument("--price-only", action="store_true", help="ignore dividends")
    ap.add_argument("--start", default=None, help="YYYY-MM-DD")
    ap.add_argument("--end", default=None, help="YYYY-MM-DD")
    ap.add_argument("--sweep", default=None, help="comma list of thresholds to compare")
    ap.add_argument("--target", type=float, default=None,
                    help="also study holding each signal until this return, e.g. 0.30, no time limit")
    ap.add_argument("--refresh", action="store_true", help="re-download prices")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    pd.set_option("display.width", 200)
    for ticker in [t.upper() for t in args.tickers]:
        if args.sweep:
            ths = [float(x) for x in args.sweep.split(",")]
            df = sweep(ticker, args, ths)
            OUT.mkdir(exist_ok=True)
            df.to_csv(OUT / f"{ticker}_{'d' if args.timeframe == 'daily' else 'w'}_sweep.csv", index=False)
            if not args.quiet:
                show = df.copy()
                for c in show.columns:
                    if c.startswith(("avg", "median", "win_rate", "worst")):
                        show[c] = show[c].map(lambda v: f"{v*100:+.1f}%" if pd.notna(v) else "")
                print(f"\n=== {ticker} threshold sweep ({args.min_hold}-{args.max_hold}m) ===")
                print(show.to_string(index=False))
            continue
        trades, summ, win, base, daily, weekly, rsi = run_one(ticker, args)
        p = write_report(ticker, args, trades, summ, win, base, daily, weekly, rsi)
        if not args.quiet:
            print(f"\n=== {ticker}  {args.timeframe} RSI<={args.threshold:g}  {daily.index[0].date()} → {daily.index[-1].date()}  "
                  f"signals={len(trades)} ===")
            if len(summ):
                s = summ.copy()
                for c in ["win_rate", "avg", "median", "min", "max", "avg_loss", "avg_win"]:
                    s[c] = s[c].map(lambda v: f"{v*100:+.1f}%")
                print(s.to_string(index=False))
            if win:
                print(f"window mean {pct(win['avg_of_window_mean'])} | best {pct(win['avg_best_exit'])} | "
                      f"worst {pct(win['avg_worst_exit'])} (min {pct(win['worst_single_exit'])}) | "
                      f"never-below-entry {win['trades_never_below_entry_in_window']}/{win['trades']} | "
                      f"all-horizons-negative {win['trades_negative_all_horizons']}/{win['trades']}")
            tt = trades.attrs.get("target")
            if tt is not None and len(tt):
                ts = target_summary(tt)
                print(f"hold to +{args.target * 100:g}%: {ts['hit']}/{ts['signals']} reached, median {ts['median_months']:.1f} mo, "
                      f"longest {ts['max_months']:.1f} mo, within 10 mo {ts['within_10m']}, worst on the way {pct(ts['min_worst'])}")
                show = tt.copy(); show["exit_return"] = show["exit_return"].map(pct); show["worst_before"] = show["worst_before"].map(pct)
                show["months"] = show["months"].round(1)
                print(show.to_string(index=False))
            print(f"report: {p}")


if __name__ == "__main__":
    main()
