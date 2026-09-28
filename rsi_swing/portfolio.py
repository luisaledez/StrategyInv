"""Compounding portfolio simulation for the weekly-RSI swing strategy.

Rules
-----
* Start with `--capital` on `--start` (default $10,000 on 1995-01-01).
* When flat and the weekly RSI closes <= threshold, buy with ALL capital at
  the next Monday's open.
* Sell at the first daily close >= entry * (1 + target)  (default +30%).
* Optional `--max-hold N` months: if the target is not reached by then, sell
  at that day's close. Optional `--stop` (e.g. 0.25) sells at a -25% close.
* While in a position, new signals are ignored. Cash earns nothing.
* Prices are dividend-adjusted (total return) unless --price-only.

Usage
-----
    python portfolio.py QCOM                          # 30% target, no time cap
    python portfolio.py QCOM --max-hold 10            # give up after 10 months
    python portfolio.py QCOM --target 0.2 --stop 0.2
    python portfolio.py QCOM AAPL --targets 0.15,0.2,0.3,0.4,0.5   # compare targets
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from prices import load_daily            # noqa: E402
from backtest import make_bars, wilder_rsi, find_signals, pct  # noqa: E402

OUT = HERE / "output"


def simulate(daily: pd.DataFrame, weekly: pd.DataFrame, rsi: pd.Series, *,
             threshold: float, target: float, start: str, capital: float,
             max_hold: int | None = None, stop: float | None = None,
             price_only: bool = False, rearm: float | None = None):
    px_col = "Close" if price_only else "AdjClose"
    d_px = daily[px_col]
    d_open = daily["Open"] * (1.0 if price_only else daily["AdjClose"] / daily["Close"])
    signals = [s for s in find_signals(rsi, threshold, rearm) if s >= pd.Timestamp(start)]
    sig_set = set(signals)

    cash = capital
    pos = None            # dict(entry_date, entry_px, shares)
    trades = []
    equity = []           # (date, value)
    dates = daily.loc[start:].index
    # a signal on a weekly close -> buy at the next trading day's open
    pending_entry: pd.Timestamp | None = None

    for dt in dates:
        # 1) execute a pending entry at today's open
        if pos is None and pending_entry is not None and dt > pending_entry:
            e_px = float(d_open.loc[dt])
            pos = {"entry_date": dt, "entry_px": e_px, "shares": cash / e_px,
                   "capital_in": cash, "signal": pending_entry}
            cash = 0.0
            pending_entry = None
        # 2) check exit at today's close
        if pos is not None:
            px = float(d_px.loc[dt])
            r = px / pos["entry_px"] - 1.0
            months = (dt - pos["entry_date"]).days / 30.4375
            reason = None
            if r >= target:
                reason = "target"
            elif stop is not None and r <= -stop:
                reason = "stop"
            elif max_hold is not None and dt >= pos["entry_date"] + pd.DateOffset(months=max_hold):
                reason = "time"
            if reason:
                cash = pos["shares"] * px
                trades.append({
                    "signal_week": pos["signal"].date(), "entry_date": pos["entry_date"].date(),
                    "entry_px": round(pos["entry_px"], 3), "exit_date": dt.date(), "exit_px": round(px, 3),
                    "months_held": round(months, 1), "return": r, "reason": reason,
                    "capital_in": pos["capital_in"], "capital_out": cash,
                })
                pos = None
        # 3) new signal on a Friday weekly close -> enter next trading day
        if pos is None and pending_entry is None:
            # the weekly bar labelled by the Friday on/after dt
            wpos = weekly.index.searchsorted(dt)
            if wpos < len(weekly) and weekly.index[wpos] in sig_set and dt == daily.loc[:weekly.index[wpos]].index[-1]:
                pending_entry = weekly.index[wpos]
        value = cash if pos is None else pos["shares"] * float(d_px.loc[dt])
        equity.append((dt, value))

    eq = pd.Series(dict(equity), name="equity")
    open_pos = None
    if pos is not None:
        last = float(d_px.iloc[-1])
        open_pos = {"entry_date": pos["entry_date"].date(), "entry_px": round(pos["entry_px"], 3),
                    "months_held": round((daily.index[-1] - pos["entry_date"]).days / 30.4375, 1),
                    "return": last / pos["entry_px"] - 1.0, "value": pos["shares"] * last}
    return pd.DataFrame(trades), eq, open_pos, signals


def stats(trades: pd.DataFrame, eq: pd.Series, capital: float, daily: pd.DataFrame,
          price_only: bool) -> dict:
    years = (eq.index[-1] - eq.index[0]).days / 365.25
    final = float(eq.iloc[-1])
    px = daily["Close" if price_only else "AdjClose"].loc[eq.index[0]:]
    bh = capital * float(px.iloc[-1] / px.iloc[0])
    dd = float((eq / eq.cummax() - 1.0).min())
    in_mkt = None
    if len(trades):
        held = sum((pd.Timestamp(r.exit_date) - pd.Timestamp(r.entry_date)).days for r in trades.itertuples())
        in_mkt = held / (eq.index[-1] - eq.index[0]).days
    return {
        "start": eq.index[0].date(), "end": eq.index[-1].date(), "years": years,
        "final": final, "multiple": final / capital, "cagr": (final / capital) ** (1 / years) - 1,
        "max_dd": dd, "trades": int(len(trades)),
        "wins": int((trades["return"] > 0).sum()) if len(trades) else 0,
        "avg_months": float(trades["months_held"].mean()) if len(trades) else float("nan"),
        "max_months": float(trades["months_held"].max()) if len(trades) else float("nan"),
        "time_in_market": in_mkt,
        "buy_hold_final": bh, "buy_hold_cagr": (bh / capital) ** (1 / years) - 1,
    }


def money(x: float) -> str:
    return f"${x:,.0f}"


def run(ticker: str, args, target: float, max_hold, stop, quiet=False):
    daily = load_daily(ticker, refresh=args.refresh)
    if daily is None:
        raise SystemExit(f"{ticker}: no data")
    weekly = make_bars(daily, args.timeframe)
    rsi = wilder_rsi(weekly["Close"], args.rsi_period)
    trades, eq, open_pos, signals = simulate(
        daily, weekly, rsi, threshold=args.threshold, target=target, start=args.start,
        capital=args.capital, max_hold=max_hold, stop=stop, price_only=args.price_only,
        rearm=args.rearm)
    st = stats(trades, eq, args.capital, daily, args.price_only)
    return trades, eq, open_pos, signals, st


def write_report(ticker, args, target, max_hold, stop, trades, eq, open_pos, signals, st) -> Path:
    OUT.mkdir(exist_ok=True)
    tag = f"{ticker}_{'d' if args.timeframe == 'daily' else 'w'}_t{args.threshold:g}_tp{int(round(target * 100))}" + \
          (f"_mh{max_hold}" if max_hold else "") + (f"_sl{int(round(stop * 100))}" if stop else "")
    trades.to_csv(OUT / f"{tag}_portfolio_trades.csv", index=False)
    eq.to_csv(OUT / f"{tag}_equity.csv", header=True)
    lines = [
        f"# {ticker} — compounding {args.timeframe} RSI ≤ {args.threshold:g} swing, sell at +{target * 100:g}%",
        "",
        f"- {money(args.capital)} on {st['start']}, all-in on each signal, next Monday open; "
        f"sell at first daily close ≥ +{target * 100:g}%"
        + (f"; or after {max_hold} months" if max_hold else "")
        + (f"; or at −{stop * 100:g}%" if stop else "")
        + f"; cash idle between trades; {'price only' if args.price_only else 'dividends included'}",
        f"- Signals in period: {len(signals)}; trades taken: {st['trades']} "
        f"(others arrived while a position was open)",
        "",
        "## Result",
        "",
        f"| | Strategy | Buy & hold {ticker} |",
        "|---|---|---|",
        f"| Final value {st['end']} | **{money(st['final'])}** | {money(st['buy_hold_final'])} |",
        f"| Multiple | {st['multiple']:.1f}× | {st['buy_hold_final'] / args.capital:.1f}× |",
        f"| CAGR over {st['years']:.1f} years | {pct(st['cagr'])} | {pct(st['buy_hold_cagr'])} |",
        f"| Max drawdown of equity | {pct(st['max_dd'])} | |",
        f"| Trades / wins | {st['trades']} / {st['wins']} | |",
        f"| Avg / longest hold (months) | {st['avg_months']:.1f} / {st['max_months']:.1f} | |",
        f"| Time invested | {pct(st['time_in_market']) if st['time_in_market'] is not None else 'n/a'} | 100% |",
        "",
    ]
    if open_pos:
        lines += [f"Open position: entered {open_pos['entry_date']} at {open_pos['entry_px']}, "
                  f"{open_pos['months_held']} months, {pct(open_pos['return'])}, worth {money(open_pos['value'])}.", ""]
    lines += ["## Trades", "", "| # | Signal | Entry | Entry px | Exit | Exit px | Months | Return | Why | Capital in | Capital out |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, (_, r) in enumerate(trades.iterrows(), 1):
        lines.append(f"| {i} | {r['signal_week']} | {r['entry_date']} | {r['entry_px']} | {r['exit_date']} | {r['exit_px']} | "
                     f"{r['months_held']} | {pct(r['return'])} | {r['reason']} | {money(r['capital_in'])} | {money(r['capital_out'])} |")
    p = OUT / f"{tag}_portfolio.md"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--threshold", type=float, default=32.0)
    ap.add_argument("--rearm", type=float, default=None)
    ap.add_argument("--rsi-period", type=int, default=14)
    ap.add_argument("--timeframe", choices=["weekly", "daily"], default="weekly")
    ap.add_argument("--target", type=float, default=0.30, help="take-profit, e.g. 0.30")
    ap.add_argument("--targets", default=None, help="comma list of targets to compare")
    ap.add_argument("--max-hold", type=int, default=None, help="months; sell at close if target not hit")
    ap.add_argument("--stop", type=float, default=None, help="stop-loss, e.g. 0.25")
    ap.add_argument("--start", default="1995-01-01")
    ap.add_argument("--capital", type=float, default=10_000)
    ap.add_argument("--price-only", action="store_true")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args(argv)

    for ticker in [t.upper() for t in args.tickers]:
        if args.targets:
            rows = []
            for tg in [float(x) for x in args.targets.split(",")]:
                trades, eq, open_pos, signals, st = run(ticker, args, tg, args.max_hold, args.stop)
                rows.append({"target": f"+{tg * 100:g}%", "trades": st["trades"], "wins": st["wins"],
                             "final": money(st["final"]), "cagr": pct(st["cagr"]), "max_dd": pct(st["max_dd"]),
                             "avg_mo": f"{st['avg_months']:.1f}", "max_mo": f"{st['max_months']:.1f}",
                             "invested": pct(st["time_in_market"]) if st["time_in_market"] is not None else "n/a",
                             "open": f"{pct(open_pos['return'])} ({open_pos['months_held']}mo)" if open_pos else ""})
            print(f"\n=== {ticker}  {args.timeframe} RSI<={args.threshold:g}  from {args.start}  {money(args.capital)}  "
                  f"buy&hold {money(st['buy_hold_final'])} ===")
            print(pd.DataFrame(rows).to_string(index=False))
            continue
        trades, eq, open_pos, signals, st = run(ticker, args, args.target, args.max_hold, args.stop)
        p = write_report(ticker, args, args.target, args.max_hold, args.stop, trades, eq, open_pos, signals, st)
        print(f"\n=== {ticker}  {args.timeframe} RSI<={args.threshold:g}  target +{args.target * 100:g}%"
              f"{'  max-hold ' + str(args.max_hold) + 'mo' if args.max_hold else ''}"
              f"{'  stop -' + str(int(args.stop * 100)) + '%' if args.stop else ''} ===")
        print(f"{money(args.capital)} on {st['start']} -> {money(st['final'])} on {st['end']}  "
              f"({st['multiple']:.1f}x, CAGR {pct(st['cagr'])}, max DD {pct(st['max_dd'])})")
        print(f"buy & hold: {money(st['buy_hold_final'])} (CAGR {pct(st['buy_hold_cagr'])})")
        print(f"trades {st['trades']}, wins {st['wins']}, avg hold {st['avg_months']:.1f} mo, "
              f"longest {st['max_months']:.1f} mo, invested {pct(st['time_in_market'])} of the time")
        if open_pos:
            print(f"open: {open_pos['entry_date']} {pct(open_pos['return'])} after {open_pos['months_held']} mo, "
                  f"worth {money(open_pos['value'])}")
        show = trades.copy()
        if len(show):
            show["return"] = show["return"].map(pct)
            show["capital_in"] = show["capital_in"].map(money)
            show["capital_out"] = show["capital_out"].map(money)
            print(show.to_string(index=False))
        print(f"report: {p}")


if __name__ == "__main__":
    main()
