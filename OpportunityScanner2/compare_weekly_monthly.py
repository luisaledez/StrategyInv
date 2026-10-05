"""Side-by-side report of the two tier A yearly backtests:

  monthly   output/yearly_backtest_t20_sector30.*        (yearly_backtest.py --target 0.20 --sector-rsi 30)
  weekly    output/yearly_backtest_weekly_rsi25_t20.*    (yearly_backtest_weekly.py --max-rsi 25 --sector-rsi 0)

Both: former overbought-ATH leader, quality + cheap, top 20 per year, +20% target within 12 months.
Writes ../reports/OpportunityScanner2 tier A weekly vs monthly - <date>.md (the web app lists every reports/*.md).

    python compare_weekly_monthly.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import yearly_backtest as yb  # noqa: E402  (summarize, pct, num)

OUT = HERE / "output"
REPORTS = HERE.parent / "reports"
M_STEM, W_STEM = "yearly_backtest_t20_sector30", "yearly_backtest_weekly_rsi25_t20"
pct, num = yb.pct, yb.num


def load(stem: str, date_col: str) -> tuple[dict, pd.DataFrame]:
    res = json.loads((OUT / f"{stem}.json").read_text(encoding="utf-8"))
    ev = pd.read_csv(OUT / f"{stem}_events.csv", parse_dates=[date_col])
    ev = ev[ev["set"] == "quality + cheap"].copy()
    for c in ("hit", "complete", "rsi_lower"):
        ev[c] = ev[c].astype(str).str.lower().eq("true")
    ev["date"] = ev[date_col]
    return res, ev


def stat_rows(pairs: list[tuple[str, dict]]) -> str:
    """One metric per row, one column per list."""
    metrics = [
        ("Buys (complete 12m windows)", lambda s: str(s["n"])),
        ("Hit +20% within 12 months", lambda s: f"{s['hits']}/{s['n']} = {pct(s['hit_rate'], 0, False)}"),
        ("Months to hit: median / mean / max", lambda s: f"{num(s['months_to_hit_median'])} / {num(s['months_to_hit_mean'])} / {num(s['months_to_hit_max'])}"),
        ("Hit within 3 / 6 months (share of buys)", lambda s: f"{pct(s['hit_within_3m'], 0, False)} / {pct(s['hit_within_6m'], 0, False)}"),
        ("12-month return: median / mean", lambda s: f"{pct(s['r12_median'])} / {pct(s['r12_mean'])}"),
        ("12-month return positive", lambda s: pct(s["r12_positive"], 0, False)),
        ("Best / worst 12-month return", lambda s: f"{pct(s['r12_best'])} {s['r12_best_ticker']} / {pct(s['r12_worst'])} {s['r12_worst_ticker']}"),
        ("Beat SPY over the same 12 months", lambda s: pct(s["beat_spy"], 0, False)),
        ("SPY over the same 12 months (median)", lambda s: pct(s["spy12_median"])),
        ("Excess over SPY (median)", lambda s: pct(s["x12_spy_median"])),
        ("Max gain in the window (median / best)", lambda s: f"{pct(s['max_gain_median'])} / {pct(s['max_gain_best'])} {s['max_gain_best_ticker']}"),
        ("Max drawdown from entry (median / worst)", lambda s: f"{pct(s['max_dd_median'])} / {pct(s['max_dd_worst'])} {s['max_dd_worst_ticker']}"),
        ("Drawdown before the hit (median, hits only)", lambda s: pct(s["dd_before_hit_median"])),
        ("Buys that fell more than 10% / 20% below entry", lambda s: f"{pct(s['share_dd_worse_10'], 0, False)} / {pct(s['share_dd_worse_20'], 0, False)}"),
        ("RSI printed lower after the buy", lambda s: pct(s["rsi_lower_share"], 0, False)),
        ("Misses (no +20% close in 12 months)", lambda s: f"{s['miss_n']}/{s['n_complete']} = {pct(s['miss_share'], 0, False)}"),
        ("Misses: 12m return median / max DD median", lambda s: f"{pct(s['miss_r12_median'])} / {pct(s['miss_max_dd_median'])}"),
    ]
    head = "| Metric | " + " | ".join(k for k, _ in pairs) + " |\n|---|" + "---|" * len(pairs) + "\n"
    body = "".join(f"| {name} | " + " | ".join(fn(s) if s.get("n") else "–" for _, s in pairs) + " |\n" for name, fn in metrics)
    return head + body


def q(s: pd.Series, p: float) -> float:
    return float(s.quantile(p))


def miss_table(df: pd.DataFrame, date_fmt) -> str:
    m = df[df["complete"] & ~df["hit"]].sort_values("date")
    if not len(m):
        return "None.\n"
    out = "| Ticker | Sector | Signal | RSI | vs ATH | Max gain | Max DD | 12m return | SPY same 12m |\n|---|---|---|---|---|---|---|---|---|\n"
    for r in m.itertuples(index=False):
        out += (f"| {r.ticker} | {r.sector} | {date_fmt(r.date)} | {num(r.rsi, 0)} | {pct(r.dd_ath)} | {pct(r.max_gain)} | {pct(r.max_dd)} "
                f"| {pct(r.r12)} | {pct(r.spy12)} |\n")
    return out


def main() -> None:
    rm, m = load(M_STEM, "signal_month")
    rw, w = load(W_STEM, "signal_date")
    sm, sw = yb.summarize(m[m["complete"]]), yb.summarize(w[w["complete"]])
    fm = lambda d: d.date().isoformat()[:7]  # noqa: E731
    fw = lambda d: d.date().isoformat()  # noqa: E731

    # ---- pairs and the three groups
    pairs, w_shared, m_shared = [], set(), set()
    for r in w.itertuples(index=False):
        cand = m[(m["ticker"] == r.ticker) & (m["date"] >= r.date - pd.DateOffset(months=3)) & (m["date"] <= r.date + pd.DateOffset(months=6))]
        if not len(cand):
            continue
        c = cand.iloc[int((cand["date"] - r.date).abs().argsort().iloc[0])]
        w_shared.add((r.ticker, r.date)); m_shared.add((c["ticker"], c["date"]))
        pairs.append((r, c))
    w["shared"] = [(t, d) in w_shared for t, d in zip(w["ticker"], w["date"])]
    m["shared"] = [(t, d) in m_shared for t, d in zip(m["ticker"], m["date"])]
    groups = [
        ("Weekly buys also on the monthly list (weekly entry)", yb.summarize(w[w["complete"] & w["shared"]])),
        ("Weekly-only buys", yb.summarize(w[w["complete"] & ~w["shared"]])),
        ("Monthly buys also on the weekly list (monthly entry)", yb.summarize(m[m["complete"] & m["shared"]])),
        ("Monthly-only buys", yb.summarize(m[m["complete"] & ~m["shared"]])),
    ]
    done_pairs = [(a, b) for a, b in pairs if a.complete and b.complete]
    lead = pd.Series([(b["date"] - a.date).days / 7 for a, b in pairs])
    entry = pd.Series([a.entry_adj / b["entry_adj"] - 1 for a, b in pairs])
    diff = pd.Series([a.r12 - b["r12"] for a, b in done_pairs])
    w_better = int((diff > 0).sum())

    # ---- by year
    years = sorted(set(int(y) for y in rm["sets"]["quality + cheap"]["by_year"]) | set(int(y) for y in rw["sets"]["quality + cheap"]["by_year"]))
    bym, byw = rm["sets"]["quality + cheap"]["by_year"], rw["sets"]["quality + cheap"]["by_year"]

    def yrow(s):
        if not s.get("n"):
            return "0 | | | |"
        o = f" ({s['n_open']} open)" if s.get("n_open") else ""
        return (f"{s['n']}{o} | {s['hits']}/{s['n']} = {pct(s['hit_rate'], 0, False)} | {pct(s['r12_median'])} | "
                f"{pct(s['max_dd_median'])} | {s['miss_n']}/{s['n_complete']}")

    # ---- cadence
    raw_m, raw_w = rm["sets"]["quality + cheap"]["n_signals_total"], rw["sets"]["quality + cheap"]["n_signals_total"]
    unf_m, unf_w = rm["sets"]["no fundamentals filter"]["n_signals_total"], rw["sets"]["no fundamentals filter"]["n_signals_total"]
    clusters = w.groupby("date").size().sort_values(ascending=False).head(5)
    sec = pd.concat([m["sector"].value_counts().rename("monthly"), w["sector"].value_counts().rename("weekly")], axis=1).fillna(0).astype(int)

    today = pd.Timestamp.today().date().isoformat()
    L = []
    L.append(f"# OpportunityScanner2 tier A: weekly RSI < 25 vs monthly RSI < 35\n")
    L.append(f"Generated {today} from `OpportunityScanner2/output/{W_STEM}.*` and `output/{M_STEM}.*`. Both runs: today's S&P 500 + 400 "
             f"({rm['n_tickers']} tickers, survivorship bias), signals 2010 onwards, quality + cheap filters point in time from SEC filings, liquid names "
             "(average dollar volume ≥ $5M), top 20 buys per calendar year ranked by signal RSI, +20% target within 12 months on daily adjusted closes. "
             "Research tooling, not investment advice.\n")

    L.append("## Verdict\n")
    L.append(f"* **The monthly candle is the better signal on every measure.** Over complete 12-month windows the monthly list hit +20% "
             f"{pct(sm['hit_rate'], 0, False)} of the time with a {pct(sm['r12_median'])} median return and {pct(sm['miss_share'], 0, False)} misses; the weekly list "
             f"{pct(sw['hit_rate'], 0, False)}, {pct(sw['r12_median'])} and {pct(sw['miss_share'], 0, False)}. The weekly list beat SPY {pct(sw['beat_spy'], 0, False)} of the time, "
             f"the monthly {pct(sm['beat_spy'], 0, False)}.")
    L.append(f"* **Weekly RSI < 25 is a shallower washout.** Its buys sit a median {pct(w['dd_ath'].median())} below the all-time high, "
             f"{num(w['weeks_from_ath'].median() / 4.345)} months after the last overbought high; the monthly buys sit {pct(m['dd_ath'].median())} below, "
             f"{num(m['months_from_ath'].median())} months after. A weekly RSI collapses in a few bad weeks; a monthly RSI under 35 needs a year or more of falling closes.")
    L.append(f"* **The lists overlap by about half.** {len(m_shared)} of the {len(m)} monthly buys also appear on the weekly list, usually a median {num(lead.median())} weeks "
             f"earlier at a median {pct(entry.median())} vs the monthly entry price. On those shared names the weekly entry did better in {w_better} of {len(done_pairs)} "
             f"completed pairs; where the weekly fired months early in a sharp decline (META, CHTR, STT) it lost while the later monthly entry won.")
    gs, go, ms, mo = groups[0][1], groups[1][1], groups[2][1], groups[3][1]
    L.append(f"* **Where both fire, the weekly entry is the weak one.** On the {gs['n']} shared names with complete windows the weekly entry hit "
             f"{pct(gs['hit_rate'], 0, False)} of the time with a {pct(gs['r12_median'])} median and a {pct(gs['max_dd_median'])} median drawdown; the same stocks bought at "
             f"the monthly close hit {pct(ms['hit_rate'], 0, False)} with {pct(ms['r12_median'])} and {pct(ms['max_dd_median'])}. Those are the long, deep declines, and the "
             f"weekly print catches them on the way down. The {go['n']} weekly-only buys did well on their own ({pct(go['hit_rate'], 0, False)} hit, {pct(go['r12_median'])} median, "
             f"{pct(go['max_dd_median'])} median drawdown): shorter, sharper sell-offs that never pushed the monthly RSI under 35. The {mo['n']} monthly-only buys hit "
             f"{pct(mo['hit_rate'], 0, False)} with a {pct(mo['r12_median'])} median.")
    L.append("* **Practical reading.** Treat the weekly RSI < 25 print as a watchlist alert on a former leader, not as the buy. If the stock keeps falling until the monthly "
             "RSI closes under 35, that later entry was better in nearly every pair. A weekly-only list is a reasonable second scan for names the monthly rule never "
             "reaches, but on its own it carries about twice the monthly miss rate and a lower median.\n")

    L.append("## The two rules\n")
    L.append("| | Monthly | Weekly |\n|---|---|---|\n"
             "| Candle | calendar month | week ending Friday |\n"
             "| Arming | new all-time high with monthly RSI(14) ≥ 70, ≥ 5 years of history | new all-time high with weekly RSI(14) ≥ 70, ≥ 5 years of history |\n"
             "| Arming window | 36 months | 156 weeks (36 months) |\n"
             "| Buy | first month closing with RSI < 35; Consumer Staples / Utilities / Materials only below 30 | first week closing with RSI < 25 (no sector rule needed at that level) |\n"
             "| Entry price | the signal month's last close | the signal week's Friday close |\n"
             "| Fundamentals | the signal month-end's point-in-time row | the last month-end on or before the signal week |\n"
             f"| Raw signals since 2010 (no fundamentals) | {unf_m} | {unf_w} |\n"
             f"| After quality + cheap | {raw_m} | {raw_w} |\n"
             f"| Buys after the top-20 cut | {len(m)} ({int(m['complete'].sum())} complete windows) | {len(w)} ({int(w['complete'].sum())} complete windows) |\n")

    L.append("## Results over complete 12-month windows (signals 2010 to Sep 2025)\n")
    L.append(stat_rows([("Monthly RSI < 35", sm), ("Weekly RSI < 25", sw)]))

    L.append("\n## Year by year\n")
    L.append("Per list: buys, hit rate, 12-month return median, max drawdown median, misses over complete windows.\n")
    L.append("| Year | SPY cal. year | Monthly: buys | hit | 12m median | max DD median | misses | Weekly: buys | hit | 12m median | max DD median | misses |\n"
             "|---|---|---|---|---|---|---|---|---|---|---|---|")
    for y in years:
        L.append(f"| {y} | {pct(rm['spy_year'].get(str(y)))} | {yrow(bym[str(y)])} | {yrow(byw[str(y)])} |")
    L.append("")
    worse_w = [y for y in years if bym[str(y)].get("n") and byw[str(y)].get("n") and bym[str(y)].get("r12_median") is not None
               and byw[str(y)].get("r12_median") is not None and byw[str(y)]["r12_median"] < bym[str(y)]["r12_median"]]
    L.append(f"In the {len([y for y in years if bym[str(y)].get('r12_median') is not None and byw[str(y)].get('r12_median') is not None])} years where both lists have "
             f"complete windows, the weekly median was lower in {len(worse_w)} ({', '.join(str(y) for y in worse_w)}). The weekly list fills the years the monthly list "
             f"skips (2013, 2014, 2019) with small, mixed batches, and it is much bigger in 2018 and 2022, the two years where it also misses most.\n")

    L.append("## How deep into the decline each list buys\n")
    L.append("| | Monthly | Weekly |\n|---|---|---|\n"
             f"| Signal RSI: median (quartiles) | {num(m['rsi'].median(), 0)} ({num(q(m['rsi'], .25), 0)} to {num(q(m['rsi'], .75), 0)}) | {num(w['rsi'].median(), 0)} ({num(q(w['rsi'], .25), 0)} to {num(q(w['rsi'], .75), 0)}) |\n"
             f"| Price vs all-time high: median (quartiles) | {pct(m['dd_ath'].median())} ({pct(q(m['dd_ath'], .25))} to {pct(q(m['dd_ath'], .75))}) | {pct(w['dd_ath'].median())} ({pct(q(w['dd_ath'], .25))} to {pct(q(w['dd_ath'], .75))}) |\n"
             f"| Months since the last overbought high: median (quartiles) | {num(m['months_from_ath'].median(), 0)} ({num(q(m['months_from_ath'], .25), 0)} to {num(q(m['months_from_ath'], .75), 0)}) "
             f"| {num(w['weeks_from_ath'].median() / 4.345, 0)} ({num(q(w['weeks_from_ath'], .25) / 4.345, 0)} to {num(q(w['weeks_from_ath'], .75) / 4.345, 0)}) |\n"
             f"| Buys less than 30% below the ATH | {pct((m['dd_ath'] > -0.30).mean(), 0, False)} | {pct((w['dd_ath'] > -0.30).mean(), 0, False)} |\n"
             f"| Buys more than 50% below the ATH | {pct((m['dd_ath'] < -0.50).mean(), 0, False)} | {pct((w['dd_ath'] < -0.50).mean(), 0, False)} |\n")
    # outcome by depth on the weekly list
    wd = w[w["complete"]].copy()
    wd["bucket"] = pd.cut(wd["dd_ath"], [-1, -0.5, -0.4, -0.3, 0], labels=["more than 50% below ATH", "40 to 50%", "30 to 40%", "less than 30%"])
    L.append("Weekly buys by distance below the all-time high (complete windows):\n")
    L.append("| Distance | Buys | Hit +20% | 12m median | Max DD median | Misses |\n|---|---|---|---|---|---|")
    for k, g in wd.groupby("bucket", observed=True):
        s = yb.summarize(g)
        L.append(f"| {k} | {s['n']} | {pct(s['hit_rate'], 0, False)} | {pct(s['r12_median'])} | {pct(s['max_dd_median'])} | {s['miss_n']} |")
    L.append("")

    L.append("## Overlap: the same stocks on both lists\n")
    L.append(f"A weekly buy is paired with a monthly buy of the same stock dated from 3 months before to 6 months after it. {len(pairs)} pairs "
             f"({len(w_shared)} of {len(w)} weekly buys, {len(m_shared)} of {len(m)} monthly buys).\n")
    L.append(stat_rows([(k, v) for k, v in groups]))
    L.append("\n| Ticker | Weekly signal | Monthly signal | Weekly first by (weeks) | Weekly entry vs monthly | 12m weekly | 12m monthly | Max DD weekly / monthly | Hit weekly / monthly |\n"
             "|---|---|---|---|---|---|---|---|---|")
    for a, b in sorted(pairs, key=lambda p: p[0].date):
        r12w = pct(a.r12) if a.complete else f"{pct(a.ret_so_far)} (open)"
        r12m = pct(b["r12"]) if b["complete"] else f"{pct(b['ret_so_far'])} (open)"
        L.append(f"| {a.ticker} | {fw(a.date)} | {fm(b['date'])} | {num((b['date'] - a.date).days / 7, 0)} | {pct(a.entry_adj / b['entry_adj'] - 1)} "
                 f"| {r12w} | {r12m} | {pct(a.max_dd)} / {pct(b['max_dd'])} | {'yes' if a.hit else 'no'} / {'yes' if b['hit'] else 'no'} |")
    L.append(f"\nOver the {len(done_pairs)} pairs with complete windows the weekly entry's 12-month return was a median {pct(diff.median())} vs the monthly entry's "
             f"(better in {w_better}, worse in {len(done_pairs) - w_better}).\n")

    L.append("## Misses\n")
    L.append("### Monthly\n")
    L.append(miss_table(m, fm))
    L.append("### Weekly\n")
    L.append(miss_table(w, fw))

    L.append("\n## Sector mix and cadence\n")
    L.append("| Sector | Monthly buys | Weekly buys |\n|---|---|---|")
    for s_, r in sec.sort_values("weekly", ascending=False).iterrows():
        L.append(f"| {s_} | {r['monthly']} | {r['weekly']} |")
    L.append("")
    L.append(f"The weekly signal fires {unf_w / unf_m:.1f}x as often before fundamentals and {raw_w / raw_m:.1f}x after. It bunches into crash weeks: "
             + ", ".join(f"{d.date().isoformat()} ({n} buys)" for d, n in clusters.items() if n >= 3)
             + f". The top-20 cap bound in {', '.join(str(y) for y in rw['sets']['quality + cheap']['capped_years']) or 'no year'} on the weekly list and never on the monthly one.\n")

    L.append("## Caveats\n")
    L.append("* Same universe for both: today's index members, so stocks that never recovered are missing and every drawdown rule is flattered.\n"
             "* Small yearly samples on both lists; the totals are the honest comparison, and 2020 dominates both (12 of 44 monthly windows, 20 of 78 weekly).\n"
             "* The weekly fundamentals row is the prior month-end, so its valuation percentile is priced slightly before the signal; that makes the weekly "
             "cheap filter a little stricter, not looser.\n"
             "* No costs, taxes or position sizing; each buy is scored on its own 12-month window.\n")
    L.append(f"Sources: `OpportunityScanner2/output/{M_STEM}.md`, `OpportunityScanner2/output/{W_STEM}.md`; scripts `yearly_backtest.py`, `yearly_backtest_weekly.py`.\n")

    REPORTS.mkdir(exist_ok=True)
    p = REPORTS / f"OpportunityScanner2 tier A weekly vs monthly - {today}.md"
    p.write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {p}", file=sys.stderr)


if __name__ == "__main__":
    main()
