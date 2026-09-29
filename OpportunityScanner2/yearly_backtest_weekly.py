"""Weekly-RSI twin of yearly_backtest.py: tier A ("former overbought-ATH leader") read on weekly candles.

Everything follows yearly_backtest.py (--target 0.20 --sector-rsi 30 by default) except the candle:

  arming   a completed *week* (Mon-Fri) whose high is a new all-time high with weekly RSI(14) >= 70,
           >= 5 years of history; arms the stock for 156 weeks (= 36 months)
  signal   the first week whose weekly RSI closes below 35 (Consumer Staples / Utilities / Materials:
           below 30); after a signal the next one needs a new arming week
  filter   quality + cheap (study.py), point in time: the fundamentals row of the last month-end on or
           before the signal week, so only filings public by then are used (and the valuation percentile
           is priced at that month-end, a little conservative when the price fell during the month)
  entry    the signal week's Friday close (adjusted); liquid names only (63-day average dollar volume
           >= $5M at the signal week)
  list     signals grouped by calendar year, ranked by signal RSI (lowest first), top 20 per year

Measured over the 12 months after the buy (daily adjusted closes): +20% target hit / time to hit, max
gain, max drawdown from entry (and before the hit), whether the *weekly* RSI printed lower afterwards,
the 12-month return and SPY over the same window. Windows past the last completed week are "open".

The report also compares the weekly list with the monthly one
(output/yearly_backtest_t20_sector30_events.csv) and shows a threshold / cap sensitivity.

    python yearly_backtest_weekly.py                       # ~2 min
        -> output/yearly_backtest_weekly_t20_sector30.{md,json}, _events.csv
    python yearly_backtest_weekly.py --max-rsi 30 --sector-rsi 0 --target 0.25
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
import signals as sig  # noqa: E402,F401  (also puts ../turnaround on the path)
import study  # noqa: E402
import yearly_backtest as yb  # noqa: E402
import indicators as ind  # noqa: E402

OUT = common.OUT
START_YEAR = yb.START_YEAR
TOP_N = yb.TOP_N
HORIZON_M = yb.HORIZON_M
STRICT_SECTORS = yb.STRICT_SECTORS
OB = 70.0
WINDOW_W = 156          # 36 months of weeks
MIN_YEARS = 5.0
pct, num = yb.pct, yb.num


# ------------------------------------------------------------------ weekly bars and the signal
def last_completed_week(daily: pd.DataFrame) -> pd.Timestamp:
    """The last Friday-ending week that is fully in the data (the data's last day if it is a Friday,
    otherwise the Friday before it)."""
    end = daily.index[-1]
    if end.weekday() == 4:
        return end
    return end - pd.offsets.Week(weekday=4)


def weekly(daily: pd.DataFrame, last_week: pd.Timestamp) -> pd.DataFrame:
    """Completed weekly bars (weeks ending Friday) with Wilder RSI(14), running all-time high and
    the length of history behind each bar."""
    w = pd.DataFrame({
        "Open": daily["Open"].resample("W-FRI").first(),
        "High": daily["High"].resample("W-FRI").max(),
        "Low": daily["Low"].resample("W-FRI").min(),
        "Close": daily["Close"].resample("W-FRI").last(),
        "AdjClose": daily["AdjClose"].resample("W-FRI").last(),
        "Volume": daily["Volume"].resample("W-FRI").sum(),
        "Days": daily["Close"].resample("W-FRI").count(),
    }).dropna(subset=["Close"]).loc[:last_week].copy()
    w["rsi"] = ind.wilder_rsi(w["Close"], 14).to_numpy()
    w["ath_prev"] = w["High"].cummax().shift(1)
    w["ath"] = w["High"].cummax()
    w["years"] = (w.index - daily.index[0]).days / 365.25
    return w


def detect(w: pd.DataFrame, max_rsi: float = 35.0, ob: float = OB, window: int = WINDOW_W,
           min_years: float = MIN_YEARS) -> list[dict]:
    """Leader + RSI<max_rsi on weekly bars (signals._scan with drop=0 and max_rsi set, in weeks)."""
    rsi = w["rsi"].to_numpy(); high = w["High"].to_numpy(); close = w["Close"].to_numpy()
    ath_prev = w["ath_prev"].to_numpy(); ath = w["ath"].to_numpy(); years = w["years"].to_numpy()
    idx = w.index
    arms: list[tuple[int, float]] = []
    out = []
    for i in range(len(w)):
        r = rsi[i]
        if np.isnan(r):
            continue
        is_ath = not np.isnan(ath_prev[i]) and high[i] >= ath_prev[i]
        if is_ath and r >= ob and years[i] >= min_years:
            arms.append((i, r))
            continue
        arms = [a for a in arms if i - a[0] <= window]
        if not arms:
            continue
        if r < max_rsi:
            j, pk = max(arms, key=lambda a: a[1])
            last_arm = arms[-1][0]
            out.append({
                "signal_date": idx[i], "peak_date": idx[j], "last_ath_date": idx[last_arm],
                "peak_rsi": float(pk), "rsi": float(r), "rsi_chg": float(r / pk - 1.0),
                "weeks_from_peak": int(i - j), "weeks_from_ath": int(i - last_arm),
                "close": float(close[i]), "ath": float(ath[i]), "dd_ath": float(close[i] / ath[i] - 1.0),
            })
            arms = []
    return out


def month_end_before(d: pd.Timestamp) -> pd.Timestamp:
    """Last month-end on or before `d` (the fundamentals row that was public at the signal)."""
    return pd.offsets.MonthEnd().rollback(d).normalize()


def collect(u: study.Universe, W: dict[str, pd.DataFrame], adv: dict[str, pd.Series], **kw) -> pd.DataFrame:
    rows = []
    for t, w in W.items():
        for e in detect(w, **kw):
            d = e["signal_date"]
            r = {"ticker": t, "name": u.meta["name"].get(t, ""), "sector": u.meta["sector"].get(t, ""), **e}
            a = adv[t].asof(d)
            r["adv"] = float(a) if pd.notna(a) else None
            me = month_end_before(d)
            r["fund_month"] = me
            r.update(study.fund_row(u, t, me))
            rows.append(r)
    df = pd.DataFrame(rows)
    if len(df):
        df = df.sort_values(["signal_date", "ticker"]).reset_index(drop=True)
    return df


# ------------------------------------------------------------------ path metrics (from the signal week's close)
def path_metrics(daily: pd.DataFrame, w: pd.DataFrame, date: pd.Timestamp, target: float, last_week: pd.Timestamp,
                 horizon_m: int = HORIZON_M, spy: pd.Series | None = None) -> dict:
    adj = daily["AdjClose"]
    entry = float(adj.loc[:date].iloc[-1])
    end = (date + pd.DateOffset(months=horizon_m)).normalize()
    complete = end <= last_week
    win = adj.loc[date + pd.Timedelta(days=1): end]
    out = {"entry_adj": entry, "window_end": end.date().isoformat(), "complete": complete, "days_observed": int(len(win))}
    if not len(win):
        return out
    rel = win / entry - 1.0
    hit = rel[rel >= target]
    out["hit"] = bool(len(hit))
    if len(hit):
        d = hit.index[0]
        out["hit_date"] = d.date().isoformat()
        out["days_to_hit"] = int((d - date).days)
        out["months_to_hit"] = float((d - date).days / 30.44)
        out["dd_before_hit"] = float(rel.loc[:d].min())
    else:
        out["hit_date"] = None; out["days_to_hit"] = None; out["months_to_hit"] = None
        out["dd_before_hit"] = float(rel.min())
    out["max_gain"] = float(rel.max()); out["max_gain_month"] = float((rel.idxmax() - date).days / 30.44)
    out["max_dd"] = float(rel.min()); out["max_dd_month"] = float((rel.idxmin() - date).days / 30.44)
    eq = win / entry
    out["peak_to_trough"] = float((eq / eq.cummax() - 1.0).min())
    rsi = w["rsi"]
    after = rsi.loc[date + pd.Timedelta(days=1): min(end, last_week)]
    r0 = float(rsi.loc[date])
    if len(after):
        out["min_rsi_after"] = float(after.min()); out["rsi_lower"] = bool(after.min() < r0)
        out["min_rsi_month"] = int(round((after.idxmin() - date).days / 30.44))
    else:
        out["min_rsi_after"] = None; out["rsi_lower"] = None; out["min_rsi_month"] = None
    out["r12"] = float(rel.iloc[-1]) if complete else None
    out["ret_so_far"] = float(rel.iloc[-1])
    if spy is not None:
        s0 = float(spy.loc[:date].iloc[-1]); s1 = float(spy.loc[:min(end, win.index[-1])].iloc[-1])
        out["spy12"] = s1 / s0 - 1.0 if complete else None
        out["spy_so_far"] = s1 / s0 - 1.0
        out["x12_spy"] = out["r12"] - out["spy12"] if complete else None
    return out


# ------------------------------------------------------------------ list building
def build_list(ev: pd.DataFrame, sector_rsi: float, top_n: int | None = TOP_N):
    """Rank by RSI within each year, cut to top_n, apply the sector rule. Returns (kept, dropped, capped_years)."""
    e = ev.sort_values(["year", "rsi", "ticker"]).copy()
    capped = [int(y) for y, g in e.groupby("year") if top_n and len(g) > top_n]
    if top_n:
        e = e.groupby("year", group_keys=False).head(top_n)
    dropped = []
    if sector_rsi:
        strict = e["sector"].isin(STRICT_SECTORS) & (e["rsi"] >= sector_rsi)
        dropped = [f"{r.ticker} {r.signal_date.date().isoformat()}" for r in e[strict].itertuples()]
        e = e[~strict]
    return e, dropped, capped


def run_paths(u, W, e: pd.DataFrame, target: float, last_week: pd.Timestamp, spy: pd.Series) -> pd.DataFrame:
    rows = []
    for r in e.to_dict("records"):
        t = r["ticker"]
        rows.append({**r, **path_metrics(u.daily[t], W[t], r["signal_date"], target, last_week, spy=spy)})
    return pd.DataFrame(rows)


# ------------------------------------------------------------------ report
def year_table(df: pd.DataFrame) -> str:
    head = ("| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? "
            "| Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    rows = []
    for i, r in enumerate(df.itertuples(index=False), 1):
        hit = "yes" if r.hit is True else ("**no**" if r.complete else "open")
        r12 = pct(r.r12) if r.complete else f"{pct(r.ret_so_far)} (so far)"
        spy = pct(r.spy12) if r.complete else f"{pct(r.spy_so_far)} (so far)"
        rsi_low = f"{num(r.min_rsi_after, 0)}{' ↓' if r.rsi_lower else ''}" if r.min_rsi_after is not None else "–"
        rows.append(f"| {i} | {r.ticker} | {r.name} | {r.sector} | {r.signal_date.date().isoformat()} | {num(r.rsi, 0)} | {pct(r.dd_ath)} "
                    f"| {r.weeks_from_ath} | {pct(r.val_pct_op, 0, False)} | {pct(r.rev_yoy)} | {pct(r.eps_yoy)} | {hit} | {num(r.months_to_hit)} "
                    f"| {pct(r.max_gain)} ({num(r.max_gain_month)}) | {pct(r.max_dd)} ({num(r.max_dd_month)}) | {pct(r.dd_before_hit)} "
                    f"| {rsi_low} | {r12} | {spy} |")
    return head + "\n".join(rows) + "\n"


def compare_table(rows: list[tuple[str, dict]]) -> str:
    head = ("| List | Buys (complete 12m) | Hit target | Months to hit (median) | ≤3m / ≤6m | 12m median / mean | 12m positive | beat SPY "
            "| SPY same 12m (median) | Max gain (median) | Max DD (median / worst) | DD before hit (median) | DD worse than -20% | RSI went lower | Misses | Miss 12m (median) |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    out = []
    for label, s in rows:
        if not s.get("n"):
            out.append(f"| {label} | 0 | | | | | | | | | | | | | | |")
            continue
        out.append(f"| {label} | {s['n']} | {s['hits']}/{s['n']} = {pct(s['hit_rate'], 0, False)} | {num(s['months_to_hit_median'])} "
                   f"| {pct(s['hit_within_3m'], 0, False)} / {pct(s['hit_within_6m'], 0, False)} | {pct(s['r12_median'])} / {pct(s['r12_mean'])} "
                   f"| {pct(s.get('r12_positive'), 0, False)} | {pct(s.get('beat_spy'), 0, False)} | {pct(s.get('spy12_median'))} | {pct(s['max_gain_median'])} "
                   f"| {pct(s['max_dd_median'])} / {pct(s['max_dd_worst'])} {s['max_dd_worst_ticker']} | {pct(s['dd_before_hit_median'])} "
                   f"| {pct(s['share_dd_worse_20'], 0, False)} | {pct(s['rsi_lower_share'], 0, False)} | {s['miss_n']}/{s['n_complete']}"
                   + (f" = {pct(s['miss_share'], 0, False)}" if s['n_complete'] else "") + f" | {pct(s['miss_r12_median'])} |")
    return head + "\n".join(out) + "\n"


def write_report(res: dict, events: dict[str, pd.DataFrame], target: float, max_rsi: float, sector_rsi: float) -> str:
    L = []
    L.append(f"# Tier A yearly backtest on weekly candles: former overbought-ATH leader, weekly RSI < {max_rsi:.0f}, +{target * 100:.0f}% target"
             + (f", staples / utilities / materials only below RSI {sector_rsi:.0f}" if sector_rsi else "") + "\n")
    L.append(f"Generated {res['generated']}. Universe: today's S&P 500 + 400 ({res['n_tickers']} tickers, survivorship bias), "
             f"weekly candles (weeks ending Friday) to {res['last_week']}, fundamentals point in time from SEC filings. "
             f"Weekly twin of `yearly_backtest.py --target {target:.2f} --sector-rsi {sector_rsi:.0f}` (output/yearly_backtest_t20_sector30.md).\n")
    L.append(f"**Trigger**: a new all-time high on a weekly candle with weekly RSI(14) ≥ {OB:.0f} (≥ {MIN_YEARS:.0f} years of history) arms the stock "
             f"for {WINDOW_W} weeks (36 months); the first week whose weekly RSI closes below {max_rsi:.0f} is the buy, at that Friday's close. "
             "**Filters**: quality (profitable TTM and in 2 of the 3 past years, revenue growth ≥ 5%, EPS growing, no one-off gain, no "
             "acquisition-driven growth) and cheap (operating multiples in the bottom half of the company's own history), both read from the "
             "fundamentals row of the last month-end on or before the signal week (only filings public by then; the valuation is priced at that "
             "month-end). Liquid names only (63-day average dollar volume ≥ $5M at the signal). Signals are grouped by calendar year, ranked by "
             f"signal RSI (lowest first) and cut to the top {TOP_N}.\n")
    L.append(f"**What is measured** over the 12 months after the buy (daily adjusted closes): whether the stock closed ≥ {target * 100:.0f}% above the "
             "buy price (\"hit\") and how long that took; the highest close vs the buy (\"max gain\"); the lowest close vs the buy "
             "(\"max DD\", the drawdown from the entry price) and the same measured only up to the hit day (\"DD before hit\"); "
             "whether the weekly RSI printed below the signal RSI afterwards (\"RSI went lower\", ↓ in the tables, with the RSI low); "
             f"and the plain 12-month return. Windows that run past {res['last_week']} are \"open\" and show what happened so far.\n")
    if sector_rsi:
        L.append(f"**Sector rule**: Consumer Staples, Utilities and Materials are bought only when the signal RSI is below {sector_rsi:.0f}; "
                 f"other sectors keep RSI < {max_rsi:.0f}. Full position at the signal close.\n")
    L.append("**SPY**: \"SPY cal. year\" is SPY's total return over the calendar year of the signals (2026 to the last completed week); "
             "\"SPY same 12m\" is SPY over each buy's own 12-month window, and \"beat SPY\" the share of buys that returned more than SPY over that window.\n")
    if res.get("filter_note"):
        L.append(f"> {res['filter_note']}\n")

    cmp = res.get("compare")
    if cmp:
        L.append("\n## Weekly vs monthly candles (quality + cheap, complete 12-month windows)\n")
        L.append(compare_table([(k, v) for k, v in cmp["summary"].items()]))
        ov = cmp["overlap"]
        n_capped = len(res['sets']['quality + cheap']['capped_years'])
        L.append(f"\nSignals before the cut: **{ov['weekly_signals']} weekly** vs **{ov['monthly_signals']} monthly** (the weekly RSI dips below "
                 f"{max_rsi:.0f} far more often, so the top-{TOP_N} cap binds in {n_capped} year{'s' if n_capped != 1 else ''} on the weekly list and never on the monthly one). "
                 f"Of the {ov['weekly_buys']} weekly buys, {ov['weekly_with_monthly_twin']} have a monthly buy of the same stock within 3 months "
                 f"before or 6 months after ({pct(ov['weekly_with_monthly_twin'] / ov['weekly_buys'], 0, False) if ov['weekly_buys'] else '–'}); "
                 f"of the {ov['monthly_buys']} monthly buys, {ov['monthly_with_weekly_twin']} have a weekly buy of the same stock in that range "
                 f"({pct(ov['monthly_with_weekly_twin'] / ov['monthly_buys'], 0, False) if ov['monthly_buys'] else '–'}). "
                 f"Where both fired, the weekly signal came a median {num(ov['lead_weeks_median'], 1)} weeks before the monthly month-end "
                 f"(range {num(ov['lead_weeks_min'], 0)} to {num(ov['lead_weeks_max'], 0)}), and the weekly entry price was a median "
                 f"{pct(ov['entry_vs_monthly_median'])} vs the monthly entry (negative = weekly bought lower).\n")
        dp = cmp["depth"]
        L.append(f"**How far into the decline each candle buys**: the weekly buys sit a median {pct(dp['weekly_dd_ath_median'])} below the all-time high "
                 f"(quartiles {pct(dp['weekly_dd_ath_q1'])} to {pct(dp['weekly_dd_ath_q3'])}), a median {num(dp['weekly_months_from_ath_median'])} months after "
                 f"the last overbought high; the monthly buys sit {pct(dp['monthly_dd_ath_median'])} below it (quartiles {pct(dp['monthly_dd_ath_q1'])} to "
                 f"{pct(dp['monthly_dd_ath_q3'])}), {num(dp['monthly_months_from_ath_median'])} months after. A weekly RSI under {max_rsi:.0f} needs "
                 f"{'about a two-month slide' if max_rsi >= 30 else 'a fast, deep slide of a few months'}; a monthly RSI under 35 needs a year or more of "
                 "falling closes, so the monthly signal is the deeper washout of the same idea.\n")
        L.append(f"Repeat names on the weekly list: {ov['weekly_repeat_within_12m']} buys are a second signal of the same stock within 12 months of an "
                 "earlier buy (overlapping windows, counted separately in every table).\n")
        if ov.get("twins"):
            L.append("\nPairs (same stock, both candles): weekly signal, monthly signal, weeks the weekly came first, weekly entry vs monthly entry, 12m return weekly / monthly.\n")
            L.append("| Ticker | Weekly signal | Monthly signal | Weekly first by (weeks) | Weekly entry vs monthly | 12m weekly | 12m monthly | Hit weekly / monthly |\n|---|---|---|---|---|---|---|---|")
            for p in ov["twins"]:
                L.append(f"| {p['ticker']} | {p['weekly']} | {p['monthly']} | {num(p['lead_weeks'], 0)} | {pct(p['entry_vs_monthly'])} "
                         f"| {pct(p['r12_w']) if p['r12_w'] is not None else 'open'} | {pct(p['r12_m']) if p['r12_m'] is not None else 'open'} "
                         f"| {'yes' if p['hit_w'] else 'no'} / {'yes' if p['hit_m'] else 'no'} |")
            L.append("")

    sens = res.get("sensitivity")
    if sens:
        L.append("\n## Sensitivity: weekly RSI threshold and the yearly cap (quality + cheap, complete 12-month windows)\n")
        L.append(compare_table([(k, v) for k, v in sens.items()]))
        L.append("\nEach row is the same pipeline with a different signal threshold (the sector rule keeps the lower of the two levels) or "
                 "without the top-20 cut per year. Lower thresholds fire later and less often.\n")

    for set_name, df in events.items():
        blk = res["sets"][set_name]
        L.append(f"\n## {set_name}\n")
        L.append(f"{blk['n_signals_total']} signals since {START_YEAR}, {blk['n_after_cap']} after the top-{TOP_N} cut per year"
                 + (f" (the cap bound in {', '.join(str(y) for y in blk['capped_years'])})" if blk["capped_years"] else " (the cap never bound)")
                 + (f", {blk['n_dropped_sector']} dropped by the sector rule" if sector_rsi else "") + ".\n")
        if sector_rsi and blk.get("dropped"):
            L.append("Dropped by the sector rule: " + ", ".join(blk["dropped"]) + ".\n")
        L.append("### Summary by year\n")
        spy_y = res["spy_year"]
        rows = [(str(y), blk["by_year"][y], pct(spy_y.get(str(y)))) for y in blk["by_year"]]
        rows.append((f"**All complete 12m windows (signals {START_YEAR}–{res['last_complete_signal']})**", blk["all_complete"], ""))
        rows.append(("**All incl. open**", blk["all"], ""))
        L.append(yb.summary_table(rows, target))
        L.append(f"\n\"Buys\" = signals kept after the top-{TOP_N} cut. \"Hit\" counts open windows that already reached the target; \"Misses\" are "
                 "complete windows only. Months are calendar months (30.44 days) from the signal week's Friday. \"RSI went lower\" = share of buys whose "
                 "weekly RSI printed below the signal RSI within the next 12 months.\n")
        L.append("### Buys by year\n")
        for y, g in df.groupby("year"):
            s = blk["by_year"][int(y)]
            L.append(f"\n#### {y}: {s['n']} buys, {s['hits']} hit +{target * 100:.0f}%, SPY {pct(res['spy_year'].get(str(y)))} that year"
                     + (f", 12m median {pct(s['r12_median'])}, best {pct(s['r12_best'])}, worst {pct(s['r12_worst'])}" if s.get("r12_median") is not None else "") + "\n")
            L.append(year_table(g))
    return "\n".join(L)


# ------------------------------------------------------------------ comparison with the monthly list
def compare_with_monthly(dfw: pd.DataFrame, monthly_csv: Path, n_weekly_signals: int, sw: dict) -> dict | None:
    if not monthly_csv.exists():
        return None
    m = pd.read_csv(monthly_csv, parse_dates=["signal_month"])
    m = m[m["set"] == "quality + cheap"].copy()
    n_monthly_signals = int(json.loads(monthly_csv.with_name(monthly_csv.name.replace("_events.csv", ".json")).read_text(encoding="utf-8"))
                            ["sets"]["quality + cheap"]["n_signals_total"])
    for c in ("hit", "complete"):
        m[c] = m[c].astype(str).str.lower().eq("true")
    sm = yb.summarize(m[m["complete"]])
    twins, w_twin, m_twin = [], set(), set()
    for r in dfw.itertuples(index=False):
        cand = m[(m["ticker"] == r.ticker) & (m["signal_month"] >= r.signal_date - pd.DateOffset(months=3))
                 & (m["signal_month"] <= r.signal_date + pd.DateOffset(months=6))]
        if not len(cand):
            continue
        c = cand.iloc[int((cand["signal_month"] - r.signal_date).abs().argsort().iloc[0])]
        w_twin.add((r.ticker, r.signal_date)); m_twin.add((c["ticker"], c["signal_month"]))
        twins.append({"ticker": r.ticker, "weekly": r.signal_date.date().isoformat(), "monthly": c["signal_month"].date().isoformat()[:7],
                      "lead_weeks": float((c["signal_month"] - r.signal_date).days / 7),
                      "entry_vs_monthly": float(r.entry_adj / c["entry_adj"] - 1.0),
                      "r12_w": None if pd.isna(r.r12) else float(r.r12), "r12_m": None if pd.isna(c["r12"]) else float(c["r12"]),
                      "hit_w": bool(r.hit), "hit_m": bool(c["hit"])})
    rep = 0
    for _, g in dfw.sort_values("signal_date").groupby("ticker"):
        d = g["signal_date"].to_list()
        rep += sum(1 for i in range(1, len(d)) if (d[i] - d[i - 1]).days <= 366)
    lead = pd.Series([p["lead_weeks"] for p in twins], dtype=float); evm = pd.Series([p["entry_vs_monthly"] for p in twins], dtype=float)
    return {"summary": {"weekly RSI (this run)": sw, "monthly RSI (yearly_backtest_t20_sector30)": sm},
            "depth": {"weekly_dd_ath_median": float(dfw["dd_ath"].median()), "monthly_dd_ath_median": float(m["dd_ath"].median()),
                      "weekly_months_from_ath_median": float(dfw["weeks_from_ath"].median() / 4.345),
                      "monthly_months_from_ath_median": float(m["months_from_ath"].median()),
                      "weekly_dd_ath_q1": float(dfw["dd_ath"].quantile(0.25)), "weekly_dd_ath_q3": float(dfw["dd_ath"].quantile(0.75)),
                      "monthly_dd_ath_q1": float(m["dd_ath"].quantile(0.25)), "monthly_dd_ath_q3": float(m["dd_ath"].quantile(0.75))},
            "overlap": {"weekly_signals": n_weekly_signals, "monthly_signals": n_monthly_signals,
                        "weekly_buys": int(len(dfw)), "monthly_buys": int(len(m)),
                        "weekly_with_monthly_twin": len(w_twin), "monthly_with_weekly_twin": len(m_twin),
                        "lead_weeks_median": float(lead.median()) if len(lead) else None,
                        "lead_weeks_min": float(lead.min()) if len(lead) else None, "lead_weeks_max": float(lead.max()) if len(lead) else None,
                        "entry_vs_monthly_median": float(evm.median()) if len(evm) else None,
                        "weekly_repeat_within_12m": rep, "twins": twins}}


# ------------------------------------------------------------------ main
def main(target: float = 0.20, max_rsi: float = 35.0, sector_rsi: float = 30.0) -> None:
    u = study.Universe()
    spy = u.spy["AdjClose"]
    last_week = last_completed_week(u.spy)
    W = {t: weekly(d, last_week) for t, d in u.daily.items()}
    adv = {t: (d["Close"] * d["Volume"]).rolling(63, min_periods=20).mean() for t, d in u.daily.items()}
    print(f"weekly bars built for {len(W)} tickers, last completed week {last_week.date()}", file=sys.stderr, flush=True)

    ev_all = study.liquid(collect(u, W, adv, max_rsi=max_rsi))
    ev_all = ev_all[ev_all["signal_date"] >= pd.Timestamp(f"{START_YEAR}-01-01")].copy()
    ev_all["year"] = ev_all["signal_date"].dt.year
    print(f"leader + weekly RSI<{max_rsi:.0f} signals since {START_YEAR}: {len(ev_all)}", file=sys.stderr, flush=True)

    res = {"generated": pd.Timestamp.today().date().isoformat(), "last_week": last_week.date().isoformat(),
           "n_tickers": len(u.daily), "trigger": {"ob": OB, "max_rsi": max_rsi, "window_weeks": WINDOW_W, "min_years": MIN_YEARS},
           "target": target, "top_n": TOP_N, "sector_rsi": sector_rsi, "strict_sectors": list(STRICT_SECTORS) if sector_rsi else [],
           "last_complete_signal": (last_week - pd.DateOffset(months=HORIZON_M)).strftime("%Y-%m-%d"), "sets": {}}
    q_only, qc = study.f_quality(ev_all), study.f_quality_val(ev_all)
    res["filter_note"] = (f"Since {START_YEAR} every weekly leader + RSI<{max_rsi:.0f} signal that passes the quality filter also passes the cheap filter, "
                          "so \"quality\" and \"quality + cheap\" are the same list." if len(q_only) == len(qc)
                          else f"Quality alone: {len(q_only)} signals; quality + cheap: {len(qc)} (the cheap filter drops {len(q_only) - len(qc)}).")

    spy_y = spy.resample("YE").last()
    res["spy_year"] = {str(y): float(spy_y.loc[str(y)].iloc[-1] / spy_y.loc[str(y - 1)].iloc[-1] - 1.0) for y in range(START_YEAR, int(last_week.year))}
    res["spy_year"][str(last_week.year)] = float(spy.loc[:last_week].iloc[-1] / spy_y.loc[str(last_week.year - 1)].iloc[-1] - 1.0)

    events_out: dict[str, pd.DataFrame] = {}
    for set_name, fn in yb.SETS.items():
        ev = fn(ev_all).copy()
        e, dropped, capped = build_list(ev, sector_rsi)
        df = run_paths(u, W, e, target, last_week, spy)
        df["set"] = set_name
        events_out[set_name] = df
        by_year = {int(y): yb.summarize(g) for y, g in df.groupby("year")}
        by_year = {y: by_year.get(y, {"n": 0}) for y in range(START_YEAR, int(last_week.year) + 1)}
        res["sets"][set_name] = {"n_signals_total": int(len(ev)), "n_after_cap": int(len(df) + len(dropped)), "capped_years": capped,
                                 "n_dropped_sector": len(dropped), "dropped": dropped, "by_year": by_year,
                                 "all_complete": yb.summarize(df[df["complete"]]), "all": yb.summarize(df)}
        print(f"{set_name}: {len(ev)} signals, {len(df)} after cap, hit rate {res['sets'][set_name]['all']['hit_rate']:.0%}", file=sys.stderr, flush=True)

    # sensitivity on the quality + cheap list: thresholds and the cap
    sens = {}
    lower = (lambda lvl: min(sector_rsi, lvl)) if sector_rsi else (lambda lvl: 0.0)
    for mr, sr, cap, label in ((max_rsi, sector_rsi, TOP_N, f"weekly RSI < {max_rsi:.0f} (sector rule {sector_rsi:.0f}), top {TOP_N} / year (this run)"),
                               (max_rsi, sector_rsi, None, f"weekly RSI < {max_rsi:.0f} (sector rule {sector_rsi:.0f}), no cap"),
                               (30.0, lower(30.0), TOP_N, f"weekly RSI < 30, top {TOP_N} / year"),
                               (30.0, lower(30.0), None, "weekly RSI < 30, no cap"),
                               (25.0, lower(25.0), None, "weekly RSI < 25, no cap"),
                               (20.0, lower(20.0), None, "weekly RSI < 20, no cap")):
        if mr == max_rsi and cap == TOP_N:
            sens[label] = res["sets"]["quality + cheap"]["all_complete"]
            continue
        e_s = study.liquid(collect(u, W, adv, max_rsi=mr)) if mr != max_rsi else ev_all
        e_s = e_s[e_s["signal_date"] >= pd.Timestamp(f"{START_YEAR}-01-01")].copy()
        e_s["year"] = e_s["signal_date"].dt.year
        e_s, _, _ = build_list(study.f_quality_val(e_s), sr, cap)
        d_s = run_paths(u, W, e_s, target, last_week, spy)
        sens[label] = yb.summarize(d_s[d_s["complete"]])
        print(f"sensitivity {label}: {len(d_s)} buys", file=sys.stderr, flush=True)
    res["sensitivity"] = sens

    dfq = events_out["quality + cheap"]
    # the monthly reference list is always the +20% / sector-30 run unless the target differs
    stem_m = "yearly_backtest_t20_sector30" if target == 0.20 else "yearly_backtest" + (f"_t{target * 100:.0f}" if target != 0.25 else "")
    res["compare"] = compare_with_monthly(dfq, OUT / f"{stem_m}_events.csv", res["sets"]["quality + cheap"]["n_signals_total"],
                                          res["sets"]["quality + cheap"]["all_complete"])

    allev = pd.concat(events_out.values(), ignore_index=True)
    cols = ["set", "year", "ticker", "name", "sector", "signal_date", "fund_month", "rsi", "peak_rsi", "peak_date", "last_ath_date",
            "weeks_from_ath", "close", "ath", "dd_ath", "adv", "mcap", "val_pct_op", "rev_yoy", "eps_yoy", "pe", "ps", "ev_ebitda",
            "q_end", "oneoff", "acq", "entry_adj", "window_end", "complete", "hit", "hit_date", "days_to_hit", "months_to_hit",
            "max_gain", "max_gain_month", "max_dd", "max_dd_month", "dd_before_hit", "peak_to_trough", "min_rsi_after", "rsi_lower",
            "min_rsi_month", "r12", "spy12", "x12_spy", "ret_so_far", "spy_so_far"]
    stem = ("yearly_backtest_weekly" + (f"_rsi{max_rsi:.0f}" if max_rsi != 35 else "") + (f"_t{target * 100:.0f}" if target != 0.25 else "")
            + (f"_sector{sector_rsi:.0f}" if sector_rsi else ""))
    allev[[c for c in cols if c in allev.columns]].to_csv(OUT / f"{stem}_events.csv", index=False)
    (OUT / f"{stem}.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    (OUT / f"{stem}.md").write_text(write_report(res, events_out, target, max_rsi, sector_rsi), encoding="utf-8")
    print(f"wrote {OUT / (stem + '.md')}", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=float, default=0.20)
    ap.add_argument("--max-rsi", type=float, default=35.0, help="weekly RSI level that triggers the buy")
    ap.add_argument("--sector-rsi", type=float, default=30.0,
                    help="Consumer Staples / Utilities / Materials are bought only below this weekly RSI (0 = off)")
    a = ap.parse_args()
    main(a.target, a.max_rsi, a.sector_rsi)
