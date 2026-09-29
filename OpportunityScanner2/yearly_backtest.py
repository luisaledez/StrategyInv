"""Year-by-year backtest of tier A ("former overbought-ATH leader, monthly RSI < 35")
with the quality + cheap filters, 2010 onwards, one calendar year of signals at a time.

Trigger (signals.py, the "leader + RSI<35" variant of variants.py / tier A of live.py):
  arming   a monthly candle makes a new all-time high with monthly RSI(14) >= 70, >= 5 years of history
  signal   within the next 36 months, the first month whose RSI closes below 35
           (after a signal the next one needs a new arming month)
  filter   quality (profitable TTM and 2 of 3 past years, revenue growth >= 5%, EPS growing, no one-off
           gain, no acquisition-driven growth) and cheap (operating multiples in the bottom half of the
           company's own history), both point in time at the signal month
  entry    the signal month's last close (adjusted, dividends included); liquid names only (ADV >= $5M)
  list     signals are grouped by calendar year and cut to the top 20 per year, ranked by the signal
           RSI (lowest first, the order of the live list); --rank val ranks by the valuation percentile

For every buy the following 12 months of daily closes are read:
  target     first close >= 25% above entry: hit / miss, days and months to get there
  max gain   highest close in the window vs entry (and when)
  drawdown   lowest close in the window vs entry ("max drawdown" from the buy price), and the same
             measured only up to the day the target was hit ("pain before the payoff")
  RSI lower  did the monthly RSI print below the signal RSI in the following 12 months, and its low
  r12        the plain 12-month return
Windows that run past the last completed month (Aug 2026) are reported as "open" with what happened so far.

    python yearly_backtest.py                 # ~2 min; writes output/yearly_backtest.{json,md} and
                                              # output/yearly_backtest_events.csv
    python yearly_backtest.py --rank val      # rank the yearly list by valuation percentile instead of RSI
    python yearly_backtest.py --target 0.30   # a different recovery target
    python yearly_backtest.py --target 0.20 --sector-rsi 30
        # +20% target; Consumer Staples, Utilities and Materials are only bought when the signal RSI is below 30
        # -> output/yearly_backtest_t20_sector30.{md,json}, _events.csv
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common  # noqa: E402
import signals as sig  # noqa: E402
import study  # noqa: E402

OUT = common.OUT
LAST = common.LAST_MONTH
TRIGGER = sig.Params(drop=0.0, max_rsi=35.0, window=36)   # tier A: leader (36 months) + RSI < 35
START_YEAR = 2010
TOP_N = 20
HORIZON_M = 12
STRICT_SECTORS = ("Consumer Staples", "Utilities", "Materials")

SETS = {
    "quality + cheap": study.f_quality_val,
    "no fundamentals filter": lambda d: d,
}


# ------------------------------------------------------------------ path metrics
def path_metrics(daily: pd.DataFrame, m: pd.DataFrame, month: pd.Timestamp, target: float,
                 horizon_m: int = HORIZON_M, spy: pd.Series | None = None) -> dict:
    """Read the `horizon_m` months after the signal month from daily adjusted closes."""
    adj = daily["AdjClose"]
    upto = adj.loc[:month]
    entry = float(upto.iloc[-1])
    end = (month + pd.offsets.MonthEnd(horizon_m)).normalize()
    complete = end <= LAST
    win = adj.loc[month + pd.Timedelta(days=1): end]
    out = {"entry_adj": entry, "window_end": end.date().isoformat(), "complete": complete,
           "days_observed": int(len(win))}
    if not len(win):
        return out
    rel = win / entry - 1.0
    hit = rel[rel >= target]
    out["hit"] = bool(len(hit))
    if len(hit):
        d = hit.index[0]
        out["hit_date"] = d.date().isoformat()
        out["days_to_hit"] = int((d - month).days)
        out["months_to_hit"] = float((d - month).days / 30.44)
        before = rel.loc[:d]
        out["dd_before_hit"] = float(before.min())
    else:
        out["hit_date"] = None; out["days_to_hit"] = None; out["months_to_hit"] = None
        out["dd_before_hit"] = float(rel.min())
    out["max_gain"] = float(rel.max())
    out["max_gain_month"] = float((rel.idxmax() - month).days / 30.44)
    out["max_dd"] = float(rel.min())
    out["max_dd_month"] = float((rel.idxmin() - month).days / 30.44)
    # peak-to-trough drawdown inside the window (a second reading of "drawdown during the period")
    eq = win / entry
    out["peak_to_trough"] = float((eq / eq.cummax() - 1.0).min())
    # monthly RSI after the signal
    rsi = m["rsi"]
    after = rsi.loc[month + pd.Timedelta(days=1): min(end, LAST)]
    r0 = float(rsi.loc[month])
    if len(after):
        out["min_rsi_after"] = float(after.min())
        out["rsi_lower"] = bool(after.min() < r0)
        out["min_rsi_month"] = int(round((after.idxmin() - month).days / 30.44))
    else:
        out["min_rsi_after"] = None; out["rsi_lower"] = None; out["min_rsi_month"] = None
    # end-of-window return (only when the window is complete)
    out["r12"] = float(rel.iloc[-1]) if complete else None
    out["ret_so_far"] = float(rel.iloc[-1])
    if spy is not None:
        s0 = float(spy.loc[:month].iloc[-1]); s1 = float(spy.loc[:min(end, win.index[-1])].iloc[-1])
        out["spy12"] = s1 / s0 - 1.0 if complete else None
        out["spy_so_far"] = s1 / s0 - 1.0
        out["x12_spy"] = out["r12"] - out["spy12"] if complete else None
    return out


# ------------------------------------------------------------------ summaries
def _med(s):
    s = pd.Series(s).dropna()
    return float(s.median()) if len(s) else None


def _mean(s):
    s = pd.Series(s).dropna()
    return float(s.mean()) if len(s) else None


def summarize(df: pd.DataFrame) -> dict:
    """Per-year (or overall) statistics of the buys in `df`."""
    n = int(len(df))
    if not n:
        return {"n": 0}
    done = df[df["complete"]]
    hits = df[df["hit"] == True]  # noqa: E712
    miss_done = done[done["hit"] == False]  # noqa: E712
    out = {
        "n": n, "n_complete": int(len(done)), "n_open": int(n - len(done)),
        "hits": int(len(hits)), "hit_rate": float(len(hits) / n),
        "hit_rate_complete": float((done["hit"] == True).mean()) if len(done) else None,  # noqa: E712
        "months_to_hit_median": _med(hits["months_to_hit"]), "months_to_hit_mean": _mean(hits["months_to_hit"]),
        "months_to_hit_max": float(hits["months_to_hit"].max()) if len(hits) else None,
        "hit_within_3m": float((hits["months_to_hit"] <= 3).sum() / n), "hit_within_6m": float((hits["months_to_hit"] <= 6).sum() / n),
        "max_gain_median": _med(df["max_gain"]), "max_gain_mean": _mean(df["max_gain"]),
        "max_gain_best": float(df["max_gain"].max()),
        "max_dd_median": _med(df["max_dd"]), "max_dd_worst": float(df["max_dd"].min()),
        "dd_before_hit_median": _med(hits["dd_before_hit"]),
        "share_dd_worse_10": float((df["max_dd"] < -0.10).mean()), "share_dd_worse_20": float((df["max_dd"] < -0.20).mean()),
        "rsi_lower_share": float(df["rsi_lower"].dropna().mean()) if df["rsi_lower"].notna().any() else None,
        "min_rsi_median": _med(df["min_rsi_after"]),
        "r12_median": _med(done["r12"]), "r12_mean": _mean(done["r12"]),
        "r12_best": float(done["r12"].max()) if len(done) else None, "r12_worst": float(done["r12"].min()) if len(done) else None,
        "r12_best_ticker": str(done.loc[done["r12"].idxmax(), "ticker"]) if len(done) else None,
        "r12_worst_ticker": str(done.loc[done["r12"].idxmin(), "ticker"]) if len(done) else None,
        "r12_positive": float((done["r12"] > 0).mean()) if len(done) else None,
        "spy12_median": _med(done["spy12"]) if "spy12" in done else None,
        "beat_spy": float((done["x12_spy"] > 0).mean()) if "x12_spy" in done and len(done) else None,
        "x12_spy_median": _med(done["x12_spy"]) if "x12_spy" in done else None,
        "max_gain_best_ticker": str(df.loc[df["max_gain"].idxmax(), "ticker"]),
        "max_dd_worst_ticker": str(df.loc[df["max_dd"].idxmin(), "ticker"]),
        "miss_n": int(len(miss_done)), "miss_share": float(len(miss_done) / len(done)) if len(done) else None,
        "miss_max_dd_median": _med(miss_done["max_dd"]), "miss_max_dd_worst": float(miss_done["max_dd"].min()) if len(miss_done) else None,
        "miss_r12_median": _med(miss_done["r12"]), "miss_max_gain_median": _med(miss_done["max_gain"]),
        "miss_r12_positive": float((miss_done["r12"] > 0).mean()) if len(miss_done) else None,
        "miss_rsi_lower_share": float(miss_done["rsi_lower"].dropna().mean()) if miss_done["rsi_lower"].notna().any() else None,
    }
    return out


# ------------------------------------------------------------------ report
def pct(v, d=0, sign=True):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "–"
    return f"{v * 100:{'+' if sign else ''}.{d}f}%"


def num(v, d=1):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "–"
    return f"{v:.{d}f}"


def year_table(df: pd.DataFrame) -> str:
    head = ("| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit "
            "| Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    rows = []
    for i, r in enumerate(df.itertuples(index=False), 1):
        if r.hit is True:
            hit = "yes"
        elif r.complete:
            hit = "**no**"
        else:
            hit = "open"
        r12 = pct(r.r12) if r.complete else f"{pct(r.ret_so_far)} (so far)"
        spy = pct(r.spy12) if r.complete else f"{pct(r.spy_so_far)} (so far)"
        rsi_low = f"{num(r.min_rsi_after, 0)}{' ↓' if r.rsi_lower else ''}" if r.min_rsi_after is not None else "–"
        rows.append(f"| {i} | {r.ticker} | {r.name} | {r.sector} | {r.signal_month.date().isoformat()[:7]} | {num(r.rsi, 0)} | {pct(r.dd_ath)} "
                    f"| {pct(r.val_pct_op, 0, False)} | {pct(r.rev_yoy)} | {pct(r.eps_yoy)} | {hit} | {num(r.months_to_hit)} "
                    f"| {pct(r.max_gain)} ({num(r.max_gain_month)}) | {pct(r.max_dd)} ({num(r.max_dd_month)}) | {pct(r.dd_before_hit)} "
                    f"| {rsi_low} | {r12} | {spy} |")
    return head + "\n".join(rows) + "\n"


def summary_table(rows: list[tuple[str, dict, str]], target: float) -> str:
    head = (f"| Year | SPY cal. year | Buys | Hit +{target * 100:.0f}% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m "
            "| 12m return: median / mean | 12m best | 12m worst | beat SPY (same 12m) | SPY same 12m (median) | Max gain (median / best) "
            "| Max DD (median / worst) | RSI went lower | Misses | Miss DD (median / worst) | Miss 12m (median) |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    out = []
    for label, s, spy_y in rows:
        if not s.get("n"):
            out.append(f"| {label} | {spy_y} | 0 | | | | | | | | | | | | | | |")
            continue
        open_note = f" ({s['n_open']} open)" if s.get("n_open") else ""
        hit = f"{s['hits']}/{s['n']} = {pct(s['hit_rate'], 0, False)}"
        best = f"{pct(s['r12_best'])} {s['r12_best_ticker']}" if s.get("r12_best") is not None else "–"
        worst = f"{pct(s['r12_worst'])} {s['r12_worst_ticker']}" if s.get("r12_worst") is not None else "–"
        out.append(f"| {label} | {spy_y} | {s['n']}{open_note} | {hit} | {num(s['months_to_hit_median'])} / {num(s['months_to_hit_mean'])} / {num(s['months_to_hit_max'])} "
                   f"| {pct(s['hit_within_3m'], 0, False)} / {pct(s['hit_within_6m'], 0, False)} | {pct(s['r12_median'])} / {pct(s['r12_mean'])} | {best} | {worst} "
                   f"| {pct(s.get('beat_spy'), 0, False)} | {pct(s.get('spy12_median'))} | {pct(s['max_gain_median'])} / {pct(s['max_gain_best'])} {s['max_gain_best_ticker']} "
                   f"| {pct(s['max_dd_median'])} / {pct(s['max_dd_worst'])} {s['max_dd_worst_ticker']} | {pct(s['rsi_lower_share'], 0, False)} "
                   f"| {s['miss_n']}/{s['n_complete']}" + (f" = {pct(s['miss_share'], 0, False)}" if s['n_complete'] else "")
                   + f" | {pct(s['miss_max_dd_median'])} / {pct(s['miss_max_dd_worst'])} | {pct(s['miss_r12_median'])} |")
    return head + "\n".join(out) + "\n"


def write_report(res: dict, events: dict[str, pd.DataFrame], target: float, rank: str) -> str:
    L = []
    sr = res.get("sector_rsi") or 0
    L.append(f"# Tier A yearly backtest: former overbought-ATH leader, monthly RSI < 35, +{target * 100:.0f}% target"
             + (f", staples / utilities / materials only below RSI {sr:.0f}" if sr else "") + "\n")
    L.append(f"Generated {res['generated']}. Universe: today's S&P 500 + 400 ({res['n_tickers']} tickers, survivorship bias), "
             f"monthly candles to {res['last_month']}, fundamentals point in time from SEC filings.\n")
    L.append("**Trigger**: a new all-time high on a monthly candle with monthly RSI(14) ≥ 70 (≥ 5 years of history) arms the stock "
             "for 36 months; the first month whose RSI closes below 35 is the buy, at that month's close. **Filters**: quality "
             "(profitable TTM and in 2 of the 3 past years, revenue growth ≥ 5%, EPS growing, no one-off gain, no acquisition-driven "
             "growth) and cheap (operating multiples in the bottom half of the company's own history). Liquid names only "
             f"(3-month average dollar volume ≥ $5M). Signals are grouped by calendar year, ranked by {'signal RSI (lowest first)' if rank == 'rsi' else 'valuation percentile (cheapest first)'} "
             f"and cut to the top {TOP_N}.\n")
    L.append(f"**What is measured** over the 12 months after the buy (daily adjusted closes): whether the stock closed ≥ {target * 100:.0f}% above the "
             "buy price (\"hit\") and how long that took; the highest close vs the buy (\"max gain\"); the lowest close vs the buy "
             "(\"max DD\", the drawdown from the entry price) and the same measured only up to the hit day (\"DD before hit\"); "
             "whether the monthly RSI printed below the signal RSI afterwards (\"RSI went lower\", ↓ in the tables, with the RSI low); "
             "and the plain 12-month return. Windows that run past Aug 2026 are \"open\" and show what happened so far.\n")
    if sr:
        L.append(f"**Sector rule**: Consumer Staples, Utilities and Materials are bought only when the signal RSI is below {sr:.0f}; "
                 "other sectors keep RSI < 35. Full position at the signal close.\n")
    L.append("**SPY**: \"SPY cal. year\" is SPY's total return over the calendar year of the signals (2026 to Aug); \"SPY same 12m\" is SPY over "
             "each buy's own 12-month window, and \"beat SPY\" the share of buys that returned more than SPY over that window.\n")
    note = res.get("filter_note")
    if note:
        L.append(f"> {note}\n")

    for set_name, df in events.items():
        blk = res["sets"][set_name]
        L.append(f"\n## {set_name}\n")
        L.append(f"{blk['n_signals_total']} signals since {START_YEAR}, {blk['n_after_cap']} after the top-{TOP_N} cut per year"
                 + (f" (the cap bound in {', '.join(str(y) for y in blk['capped_years'])})" if blk["capped_years"] else " (the cap never bound)")
                 + (f", {blk['n_dropped_sector']} dropped by the sector rule" if sr else "") + ".\n")
        if sr and blk.get("dropped"):
            L.append("Dropped by the sector rule: " + ", ".join(blk["dropped"]) + ".\n")
        L.append("### Summary by year\n")
        spy_y = res["spy_year"]
        rows = [(str(y), blk["by_year"][y], pct(spy_y.get(str(y)))) for y in blk["by_year"]]
        rows.append((f"**All complete 12m windows (signals {START_YEAR}–{res['last_complete_signal']})**", blk["all_complete"], ""))
        rows.append(("**All incl. open**", blk["all"], ""))
        L.append(summary_table(rows, target))
        L.append("\n\"Buys\" = signals kept after the top-20 cut. \"Hit\" counts open windows that already reached the target; \"Misses\" are "
                 "complete windows only. Months are calendar months from the signal month-end. \"RSI went lower\" = share of buys whose "
                 "monthly RSI printed below the signal RSI within the next 12 months.\n")
        L.append("### Buys by year\n")
        for y, g in df.groupby("year"):
            s = blk["by_year"][int(y)]
            L.append(f"\n#### {y}: {s['n']} buys, {s['hits']} hit +{target * 100:.0f}%, SPY {pct(res['spy_year'].get(str(y)))} that year"
                     + (f", 12m median {pct(s['r12_median'])}, best {pct(s['r12_best'])}, worst {pct(s['r12_worst'])}" if s.get("r12_median") is not None else "") + "\n")
            L.append(year_table(g))
    return "\n".join(L)


# ------------------------------------------------------------------ main
def main(target: float = 0.25, rank: str = "rsi", sector_rsi: float = 0.0) -> None:
    u = study.Universe()
    spy = u.spy["AdjClose"]
    ev = study.liquid(study.collect(u, sig.detect, p=TRIGGER))
    ev = ev[ev["signal_month"] >= pd.Timestamp(f"{START_YEAR}-01-01")].copy()
    ev["year"] = ev["signal_month"].dt.year
    print(f"leader + RSI<35 signals since {START_YEAR}: {len(ev)}", file=sys.stderr, flush=True)

    res = {"generated": pd.Timestamp.today().date().isoformat(), "last_month": LAST.date().isoformat(),
           "n_tickers": len(u.daily), "trigger": TRIGGER.as_dict(), "target": target, "rank": rank, "top_n": TOP_N,
           "sector_rsi": sector_rsi, "strict_sectors": list(STRICT_SECTORS) if sector_rsi else [],
           "last_complete_signal": (LAST - pd.DateOffset(months=HORIZON_M)).strftime("%Y-%m"),
           "sets": {}}
    q_only = study.f_quality(ev)
    qc = study.f_quality_val(ev)
    if len(q_only) == len(qc):
        res["filter_note"] = (f"Since {START_YEAR} every leader + RSI<35 signal that passes the quality filter also passes the cheap "
                              "filter (valuation percentile ≤ 50%), so \"quality\" and \"quality + cheap\" are the same list.")
    else:
        res["filter_note"] = f"Quality alone: {len(q_only)} signals; quality + cheap: {len(qc)}."

    # SPY calendar-year total returns (the current year to the last completed month)
    spy_y = spy.resample("YE").last()
    res["spy_year"] = {str(y): float(spy_y.loc[str(y)].iloc[-1] / spy_y.loc[str(y - 1)].iloc[-1] - 1.0) for y in range(START_YEAR, int(LAST.year))}
    res["spy_year"][str(LAST.year)] = float(spy.loc[:LAST].iloc[-1] / spy_y.loc[str(LAST.year - 1)].iloc[-1] - 1.0)

    events_out: dict[str, pd.DataFrame] = {}
    for set_name, fn in SETS.items():
        e = fn(ev).copy()
        n_total = len(e)
        key = "rsi" if rank == "rsi" else "val_pct_op"
        e = e.sort_values(["year", key, "ticker"], ascending=[True, True, True])
        capped_years = [int(y) for y, g in e.groupby("year") if len(g) > TOP_N]
        e = e.groupby("year", group_keys=False).head(TOP_N)
        dropped = []
        if sector_rsi:
            strict = e["sector"].isin(STRICT_SECTORS) & (e["rsi"] >= sector_rsi)
            dropped = [f"{r.ticker} {r.signal_month.date().isoformat()[:7]}" for r in e[strict].itertuples()]
            e = e[~strict]
        rows = []
        for r in e.to_dict("records"):
            t = r["ticker"]
            pm = path_metrics(u.daily[t], u.monthly[t], r["signal_month"], target, spy=spy)
            rows.append({**r, **pm})
        df = pd.DataFrame(rows)
        df["set"] = set_name
        events_out[set_name] = df
        by_year = {int(y): summarize(g) for y, g in df.groupby("year")}
        all_years = range(START_YEAR, int(LAST.year) + 1)
        by_year = {y: by_year.get(y, {"n": 0}) for y in all_years}
        res["sets"][set_name] = {
            "n_signals_total": int(n_total), "n_after_cap": int(len(df) + len(dropped)), "capped_years": capped_years,
            "n_dropped_sector": len(dropped), "dropped": dropped,
            "by_year": by_year,
            "all_complete": summarize(df[df["complete"]]),
            "all": summarize(df),
        }
        print(f"{set_name}: {n_total} signals, {len(df)} after cap, hit rate {res['sets'][set_name]['all']['hit_rate']:.0%}",
              file=sys.stderr, flush=True)

    allev = pd.concat(events_out.values(), ignore_index=True)
    cols = ["set", "year", "ticker", "name", "sector", "signal_month", "rsi", "peak_rsi", "peak_month", "last_ath_month",
            "months_from_ath", "close", "ath", "dd_ath", "adv", "mcap", "val_pct_op", "rev_yoy", "eps_yoy", "pe", "ps", "ev_ebitda",
            "q_end", "oneoff", "acq", "entry_adj", "window_end", "complete", "hit", "hit_date", "days_to_hit", "months_to_hit",
            "max_gain", "max_gain_month", "max_dd", "max_dd_month", "dd_before_hit", "peak_to_trough", "min_rsi_after", "rsi_lower",
            "min_rsi_month", "r12", "spy12", "x12_spy", "ret_so_far", "spy_so_far", "r24", "r36"]
    stem = "yearly_backtest" + (f"_t{target * 100:.0f}" if target != 0.25 else "") + (f"_sector{sector_rsi:.0f}" if sector_rsi else "")
    allev[[c for c in cols if c in allev.columns]].to_csv(OUT / f"{stem}_events.csv", index=False)
    (OUT / f"{stem}.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    md = write_report(res, events_out, target, rank)
    (OUT / f"{stem}.md").write_text(md, encoding="utf-8")
    print(f"wrote {OUT / (stem + '.md')}", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=float, default=0.25)
    ap.add_argument("--rank", choices=["rsi", "val"], default="rsi")
    ap.add_argument("--sector-rsi", type=float, default=0.0,
                    help="if set, Consumer Staples / Utilities / Materials are bought only when the signal RSI is below this")
    a = ap.parse_args()
    main(a.target, a.rank, a.sector_rsi)
