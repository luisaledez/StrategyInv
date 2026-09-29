"""Tier A yearly backtest, version 2: sector-aware trigger and a two-tranche entry.

Same trigger and yearly top-20 lists as yearly_backtest.py (former overbought-ATH leader of the last 36
months, first monthly RSI(14) close below 35, 2010+, ranked by signal RSI), with two changes learned from
the losers of the unfiltered run:

  sector rule   Consumer Staples, Utilities and Materials are only bought when the signal RSI is below 30
                (the RSI 30-35 signals in those sectors hit the +25% target only about two thirds of the
                time). Other sectors keep RSI < 35.
  two tranches  half the position at the signal month's close; the other half at the first month-end
                within the next 4 months whose close is a new low for the move (below every month-end
                close since the signal) while the monthly RSI is higher than the signal RSI (a bullish
                divergence: lower price, higher RSI). If that never happens the second half stays in cash.

Metrics over the 12 months after the signal month (daily adjusted closes):
  deployed   the value of the capital actually invested: tranche 1 alone until tranche 2 fills, then
             both halves at their own cost. Hit (+25%), months to hit, max gain and max drawdown are on
             this path, measured from the signal month-end.
  with cash  the 12-month return counting an unfilled second half as cash at 0%.
  tranche 1 / tranche 2 the plain 12-month return of each half from its own buy to the common exit.
Both filter sets of v1 are run ("quality + cheap" and "no fundamentals filter"), and each summary carries
the v1 single-entry result of the same signals (before the sector rule) for comparison.

    python yearly_backtest_v2.py                  # ~2 min; output/yearly_backtest_v2.{md,json}, _events.csv
    python yearly_backtest_v2.py --target 0.30 --window 6 --sector-rsi 30
    python yearly_backtest_v2.py --t2-rule lower   # second half on a new low with the RSI at or below the signal RSI
                                                   # -> output/yearly_backtest_v2_lower.{md,json}, _events.csv
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common  # noqa: E402
import signals as sig  # noqa: E402
import study  # noqa: E402
import yearly_backtest as v1  # noqa: E402

OUT = common.OUT
LAST = common.LAST_MONTH
STRICT_SECTORS = ("Consumer Staples", "Utilities", "Materials")
pct, num = v1.pct, v1.num


# ------------------------------------------------------------------ second tranche
RULES = {"higher": "the monthly RSI is higher than the signal RSI (bullish divergence)",
         "lower": "the monthly RSI is at or below the signal RSI (price and momentum both at new lows)",
         "any": "regardless of the RSI"}


def second_tranche(m: pd.DataFrame, month: pd.Timestamp, window: int, rule: str = "higher") -> dict:
    """First month-end within `window` months after the signal whose close is below every close since
    the signal month while the RSI meets `rule` (see RULES) against the signal RSI."""
    idx = m.index
    i0 = idx.get_loc(month)
    r0 = float(m["rsi"].iloc[i0]); low = float(m["Close"].iloc[i0])
    for k in range(1, window + 1):
        i = i0 + k
        if i >= len(m):
            break
        c = float(m["Close"].iloc[i]); r = float(m["rsi"].iloc[i])
        ok = r > r0 if rule == "higher" else (r <= r0 if rule == "lower" else True)
        if c < low and ok:
            return {"t2_month": idx[i], "t2_offset": k, "t2_rsi": r, "t2_close": c, "t2_vs_t1": c / float(m["Close"].iloc[i0]) - 1.0}
        low = min(low, c)
    return {"t2_month": None, "t2_offset": None, "t2_rsi": None, "t2_close": None, "t2_vs_t1": None}


def position_metrics(daily: pd.DataFrame, m: pd.DataFrame, month: pd.Timestamp, t2_month, target: float,
                     horizon_m: int = v1.HORIZON_M) -> dict:
    adj = daily["AdjClose"]
    p1 = float(adj.loc[:month].iloc[-1])
    end = (month + pd.offsets.MonthEnd(horizon_m)).normalize()
    complete = end <= LAST
    win = adj.loc[month + pd.Timedelta(days=1): end]
    out = {"complete": complete, "window_end": end.date().isoformat(), "entry_adj": p1}
    if not len(win):
        return out
    if t2_month is not None:
        p2 = float(adj.loc[:t2_month].iloc[-1])
        out["entry2_adj"] = p2
        after2 = (win.index > t2_month)
        deployed = np.where(after2, 0.5 * win / p1 + 0.5 * win / p2, win / p1)
        cash = np.where(after2, 0.5 * win / p1 + 0.5 * win / p2, 0.5 * win / p1 + 0.5)
        out["avg_cost_vs_t1"] = (p1 + p2) / 2 / p1 - 1.0
    else:
        p2 = None
        deployed = (win / p1).to_numpy()
        cash = (0.5 * win / p1 + 0.5).to_numpy()
        out["avg_cost_vs_t1"] = 0.0
    rel = pd.Series(deployed - 1.0, index=win.index)
    hit = rel[rel >= target]
    out["hit"] = bool(len(hit))
    if len(hit):
        d = hit.index[0]
        out["hit_date"] = d.date().isoformat(); out["months_to_hit"] = float((d - month).days / 30.44)
        out["dd_before_hit"] = float(rel.loc[:d].min())
    else:
        out["hit_date"] = None; out["months_to_hit"] = None; out["dd_before_hit"] = float(rel.min())
    out["max_gain"] = float(rel.max()); out["max_gain_month"] = float((rel.idxmax() - month).days / 30.44)
    out["max_dd"] = float(rel.min()); out["max_dd_month"] = float((rel.idxmin() - month).days / 30.44)
    rsi = m["rsi"]; after = rsi.loc[month + pd.Timedelta(days=1): min(end, LAST)]
    r0 = float(rsi.loc[month])
    out["min_rsi_after"] = float(after.min()) if len(after) else None
    out["rsi_lower"] = bool(after.min() < r0) if len(after) else None
    out["r12"] = float(rel.iloc[-1]) if complete else None
    out["ret_so_far"] = float(rel.iloc[-1])
    out["r12_cash"] = float(cash[-1] - 1.0) if complete else None
    out["r12_t1"] = float(win.iloc[-1] / p1 - 1.0) if complete else None
    out["r12_t2"] = float(win.iloc[-1] / p2 - 1.0) if (complete and p2) else None
    return out


# ------------------------------------------------------------------ summaries
def summarize(df: pd.DataFrame) -> dict:
    s = v1.summarize(df)
    if not s.get("n"):
        return s
    done = df[df["complete"]]
    s["t2_filled"] = int(df["t2_month"].notna().sum()); s["t2_fill_rate"] = float(df["t2_month"].notna().mean())
    f = df[df["t2_month"].notna()]
    s["t2_offset_median"] = v1._med(f["t2_offset"]); s["t2_vs_t1_median"] = v1._med(f["t2_vs_t1"])
    s["r12_cash_median"] = v1._med(done["r12_cash"]); s["r12_t1_median"] = v1._med(done["r12_t1"])
    s["r12_t2_median"] = v1._med(done["r12_t2"])
    fd = done[done["t2_month"].notna()]
    s["filled_n"] = int(len(fd))
    s["filled_hit_rate"] = float((fd["hit"] == True).mean()) if len(fd) else None  # noqa: E712
    s["filled_r12_median"] = v1._med(fd["r12"]); s["filled_r12_t1_median"] = v1._med(fd["r12_t1"])
    nd = done[done["t2_month"].isna()]
    s["unfilled_n"] = int(len(nd))
    s["unfilled_hit_rate"] = float((nd["hit"] == True).mean()) if len(nd) else None  # noqa: E712
    s["unfilled_r12_median"] = v1._med(nd["r12"])
    return s


# ------------------------------------------------------------------ report
def summary_table(rows: list[tuple[str, dict, dict | None]]) -> str:
    head = ("| Year | Buys | 2nd half filled | Hit +25% (deployed) | v1 single entry hit | Months to hit (median / mean) "
            "| Max gain (median) | Max DD (median / worst) | RSI went lower | 12m deployed (median) | 12m with cash | 12m v1 single entry "
            "| Misses | Miss DD (median / worst) | Miss 12m (median) |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    out = []
    for label, s, b in rows:
        if not s.get("n"):
            out.append(f"| {label} | 0 | | | | | | | | | | | | | |")
            continue
        open_note = f" ({s['n_open']} open)" if s.get("n_open") else ""
        hit = f"{s['hits']}/{s['n']} = {pct(s['hit_rate'], 0, False)}"
        bhit = f"{b['hits']}/{b['n']} = {pct(b['hit_rate'], 0, False)}" if b and b.get("n") else "–"
        br12 = pct(b["r12_median"]) if b and b.get("n") else "–"
        out.append(f"| {label} | {s['n']}{open_note} | {s['t2_filled']}/{s['n']} = {pct(s['t2_fill_rate'], 0, False)} | {hit} | {bhit} "
                   f"| {num(s['months_to_hit_median'])} / {num(s['months_to_hit_mean'])} | {pct(s['max_gain_median'])} "
                   f"| {pct(s['max_dd_median'])} / {pct(s['max_dd_worst'])} | {pct(s['rsi_lower_share'], 0, False)} "
                   f"| {pct(s['r12_median'])} | {pct(s['r12_cash_median'])} | {br12} "
                   f"| {s['miss_n']}/{s['n_complete']}" + (f" = {pct(s['miss_share'], 0, False)}" if s["n_complete"] else "")
                   + f" | {pct(s['miss_max_dd_median'])} / {pct(s['miss_max_dd_worst'])} | {pct(s['miss_r12_median'])} |")
    return head + "\n".join(out) + "\n"


def year_table(df: pd.DataFrame) -> str:
    head = ("| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) "
            "| Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    rows = []
    for i, r in enumerate(df.itertuples(index=False), 1):
        hit = "yes" if r.hit is True else ("**no**" if r.complete else "open")
        t2 = (f"{r.t2_month.date().isoformat()[:7]} ({pct(r.t2_vs_t1)}, RSI {num(r.t2_rsi, 0)})" if pd.notna(r.t2_month) else "not filled")
        rsi_low = f"{num(r.min_rsi_after, 0)}{' ↓' if r.rsi_lower else ''}" if r.min_rsi_after is not None else "–"
        r12 = pct(r.r12) if r.complete else f"{pct(r.ret_so_far)} (so far)"
        halves = f"{pct(r.r12_t1)} / {pct(r.r12_t2)}" if r.complete else "–"
        rows.append(f"| {i} | {r.ticker} | {r.name} | {r.sector} | {r.signal_month.date().isoformat()[:7]} | {num(r.rsi, 0)} | {pct(r.dd_ath)} "
                    f"| {pct(r.val_pct_op, 0, False)} | {pct(r.rev_yoy)} | {t2} | {hit} | {num(r.months_to_hit)} "
                    f"| {pct(r.max_gain)} ({num(r.max_gain_month)}) | {pct(r.max_dd)} ({num(r.max_dd_month)}) | {rsi_low} "
                    f"| {r12} | {pct(r.r12_cash) if r.complete else '–'} | {halves} |")
    return head + "\n".join(rows) + "\n"


def write_report(res: dict, events: dict[str, pd.DataFrame], dropped: dict[str, pd.DataFrame], a) -> str:
    L = [f"# Tier A yearly backtest v2: sector rule (staples / utilities / materials need RSI < {a.sector_rsi:.0f}) and a two-tranche entry\n",
         f"Generated {res['generated']}. Universe: today's S&P 500 + 400 ({res['n_tickers']} tickers, survivorship bias), monthly candles to "
         f"{res['last_month']}, fundamentals point in time from SEC filings. Same trigger, yearly top-{v1.TOP_N} lists (ranked by signal RSI) "
         "and filters as `yearly_backtest.md`.\n",
         f"**Changes**: (1) Consumer Staples, Utilities and Materials are bought only when the signal RSI is below {a.sector_rsi:.0f}; other sectors "
         f"keep RSI < 35. (2) Half the position is bought at the signal month's close, the other half at the first month-end within the next "
         f"{a.window} months whose close is a new low for the move (below every month-end close since the signal) while the monthly RSI is "
         "higher than the signal RSI. If that never happens the second half stays in cash.\n",
         f"**Metrics** over the 12 months after the signal month (daily adjusted closes). \"Deployed\" = the value of the capital actually invested "
         "(tranche 1 alone until tranche 2 fills, then both halves at their own cost); hit (+{:.0f}%), months to hit, max gain and max DD are on that "
         "path, measured from the signal month-end. \"With cash\" counts an unfilled second half as cash at 0%. \"v1 single entry\" is the "
         "yearly_backtest.py result for the same signals before the sector rule (all-in at the signal close). A positive max DD means the position "
         "never traded below cost.\n".format(a.target * 100)]
    for set_name, df in events.items():
        blk = res["sets"][set_name]
        L.append(f"\n## {set_name}\n")
        L.append(f"{blk['n_signals_v1']} signals in the v1 lists, {blk['n_dropped_sector']} dropped by the sector rule, {blk['n_buys']} buys; "
                 f"second half filled in {blk['all']['t2_filled']} ({pct(blk['all']['t2_fill_rate'], 0, False)}), median {num(blk['all']['t2_offset_median'], 0)} months "
                 f"after the signal at {pct(blk['all']['t2_vs_t1_median'])} vs the first buy.\n")
        L.append("### Summary by year\n")
        rows = [(str(y), blk["by_year"][y], blk["by_year_v1"].get(y)) for y in blk["by_year"]]
        rows.append((f"**All complete 12m windows (signals 2010–{res['last_complete_signal']})**", blk["all_complete"], blk["all_complete_v1"]))
        rows.append(("**All incl. open**", blk["all"], blk["all_v1"]))
        L.append(summary_table(rows))
        ac = blk["all_complete"]
        L.append(f"\n**Two-tranche detail (complete windows)**: when the second half filled ({ac['filled_n']} buys) the deployed hit rate was "
                 f"{pct(ac['filled_hit_rate'], 0, False)} and the median 12m return {pct(ac['filled_r12_median'])} (first half alone {pct(ac['filled_r12_t1_median'])}, "
                 f"second half {pct(ac['r12_t2_median'])}); when it did not fill ({ac['unfilled_n']} buys) the hit rate was {pct(ac['unfilled_hit_rate'], 0, False)} "
                 f"and the median 12m return {pct(ac['unfilled_r12_median'])}.\n")
        dr = dropped[set_name]
        if len(dr):
            dd = dr[dr["complete"]]
            L.append(f"\n**Dropped by the sector rule** ({len(dr)} signals, {len(dd)} complete): single-entry hit rate {pct((dd['hit'] == True).mean(), 0, False) if len(dd) else '–'}, "  # noqa: E712
                     f"median 12m return {pct(dd['r12'].median()) if len(dd) else '–'}, median max DD {pct(dd['max_dd'].median()) if len(dd) else '–'}: "
                     + ", ".join(f"{r.ticker} {r.signal_month.date().isoformat()[:7]} ({pct(r.r12) if r.complete else 'open'})" for r in dr.itertuples()) + ".\n")
        L.append("### Buys by year\n")
        for y, g in df.groupby("year"):
            s = blk["by_year"][int(y)]
            L.append(f"\n#### {y}: {s['n']} buys, {s['t2_filled']} second halves filled, {s['hits']} hit +{a.target * 100:.0f}%"
                     + (f", median max gain {pct(s['max_gain_median'])}, median max DD {pct(s['max_dd_median'])}" if s["n"] else "") + "\n")
            L.append(year_table(g))
    return "\n".join(L)


# ------------------------------------------------------------------ main
def main(a) -> None:
    u = study.Universe()
    ev = study.liquid(study.collect(u, sig.detect, p=v1.TRIGGER))
    ev = ev[ev["signal_month"] >= pd.Timestamp(f"{v1.START_YEAR}-01-01")].copy()
    ev["year"] = ev["signal_month"].dt.year
    res = {"generated": pd.Timestamp.today().date().isoformat(), "last_month": LAST.date().isoformat(), "n_tickers": len(u.daily),
           "trigger": v1.TRIGGER.as_dict(), "target": a.target, "window": a.window, "sector_rsi": a.sector_rsi, "t2_rule": a.t2_rule,
           "strict_sectors": list(STRICT_SECTORS), "top_n": v1.TOP_N,
           "last_complete_signal": (LAST - pd.DateOffset(months=v1.HORIZON_M)).strftime("%Y-%m"), "sets": {}}
    events_out, dropped_out = {}, {}
    all_years = range(v1.START_YEAR, int(LAST.year) + 1)
    for set_name, fn in v1.SETS.items():
        e = fn(ev).copy().sort_values(["year", "rsi", "ticker"])
        e = e.groupby("year", group_keys=False).head(v1.TOP_N)          # the v1 yearly lists
        strict = e["sector"].isin(STRICT_SECTORS) & (e["rsi"] >= a.sector_rsi)
        # v1 single-entry metrics for every listed signal (comparison + the dropped ones)
        base_rows = [{**r, **v1.path_metrics(u.daily[r["ticker"]], u.monthly[r["ticker"]], r["signal_month"], a.target)} for r in e.to_dict("records")]
        base = pd.DataFrame(base_rows)
        dropped = base[strict.to_numpy()].copy()
        kept = e[~strict]
        rows = []
        for r in kept.to_dict("records"):
            t = r["ticker"]
            t2 = second_tranche(u.monthly[t], r["signal_month"], a.window, a.t2_rule)
            pm = position_metrics(u.daily[t], u.monthly[t], r["signal_month"], t2["t2_month"], a.target)
            rows.append({**r, **t2, **pm})
        df = pd.DataFrame(rows); df["set"] = set_name
        events_out[set_name], dropped_out[set_name] = df, dropped
        by_year = {y: summarize(g) for y, g in df.groupby("year")}
        by_year_v1 = {y: v1.summarize(g) for y, g in base.groupby("year")}
        res["sets"][set_name] = {
            "n_signals_v1": int(len(e)), "n_dropped_sector": int(strict.sum()), "n_buys": int(len(df)),
            "by_year": {y: by_year.get(y, {"n": 0}) for y in all_years},
            "by_year_v1": {y: by_year_v1.get(y, {"n": 0}) for y in all_years},
            "all_complete": summarize(df[df["complete"]]), "all": summarize(df),
            "all_complete_v1": v1.summarize(base[base["complete"]]), "all_v1": v1.summarize(base),
            "dropped": v1.summarize(dropped) if len(dropped) else {"n": 0},
        }
        s = res["sets"][set_name]["all_complete"]
        print(f"{set_name}: {len(e)} listed, {strict.sum()} dropped, {len(df)} buys, 2nd half filled {s['t2_fill_rate']:.0%}, "
              f"hit {s['hit_rate']:.0%} (v1 {res['sets'][set_name]['all_complete_v1']['hit_rate']:.0%}), median 12m {s['r12_median']:+.0%} "
              f"(v1 {res['sets'][set_name]['all_complete_v1']['r12_median']:+.0%})", file=sys.stderr, flush=True)
    allev = pd.concat(events_out.values(), ignore_index=True)
    cols = ["set", "year", "ticker", "name", "sector", "signal_month", "rsi", "peak_rsi", "dd_ath", "months_from_ath", "adv", "mcap", "val_pct_op",
            "rev_yoy", "eps_yoy", "oneoff", "acq", "entry_adj", "t2_month", "t2_offset", "t2_rsi", "t2_vs_t1", "entry2_adj", "avg_cost_vs_t1",
            "complete", "hit", "hit_date", "months_to_hit", "max_gain", "max_gain_month", "max_dd", "max_dd_month", "dd_before_hit",
            "min_rsi_after", "rsi_lower", "r12", "r12_cash", "r12_t1", "r12_t2", "ret_so_far"]
    stem = "yearly_backtest_v2" + ("" if a.t2_rule == "higher" else f"_{a.t2_rule}")
    allev[[c for c in cols if c in allev.columns]].to_csv(OUT / f"{stem}_events.csv", index=False)
    (OUT / f"{stem}.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    (OUT / f"{stem}.md").write_text(write_report(res, events_out, dropped_out, a), encoding="utf-8")
    print(f"wrote {OUT / (stem + '.md')}", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=float, default=0.25)
    ap.add_argument("--window", type=int, default=4, help="months after the signal in which the second half can fill")
    ap.add_argument("--sector-rsi", type=float, default=30.0, help="RSI needed for staples / utilities / materials")
    ap.add_argument("--t2-rule", choices=list(RULES), default="higher",
                    help="RSI condition on the second half's new-low month: higher than the signal RSI (default), lower, or any")
    main(ap.parse_args())
