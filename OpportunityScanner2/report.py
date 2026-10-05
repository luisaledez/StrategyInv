"""Write the candidates report for the newest live list:
reports/OpportunityScanner2 candidates - <date>.md (the web app's /os2 page renders the newest one).

Reads output/live_<date>.json (live.py), output/web_summary.json (export_web.py) and, for the overlap
note, the newest ../turnaround_backtest_v3/output/live_both_opval_<date>.json.

    python report.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "output"
REPORTS = ROOT / "reports"
V3_OUT = ROOT / "turnaround_backtest_v3" / "output"


def p(v) -> str:
    return "–" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v * 100:+.0f}%"


def n(v, d=1) -> str:
    return "–" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v:.{d}f}"


def tier(t, rsi) -> str:
    if not isinstance(t, str) or t in ("", "-"):
        return "–"
    s = "A+B" if ("A" in t and "B" in t) else "A" if "A" in t else "B" if "B" in t else "C"
    return s + (" ★" if "A" in t and rsi is not None and not math.isnan(rsi) and rsi < 35 else "")


def table(df: pd.DataFrame, m_done: str, m_prov: str) -> str:
    head = (f"| Ticker | Name | Tier ({m_done}) | Tier ({m_prov}, prov.) | RSI {m_done} / {m_prov} | Peak RSI (month) | vs ATH "
            "| Rev TTM y/y | EPS TTM y/y | Val. pct | Fwd EPS (Yahoo) |\n|---|---|---|---|---|---|---|---|---|---|---|\n")
    rows = "".join(
        f"| **{r.ticker}** | {r['name']} | {tier(r.tier, r.rsi)} | {tier(r.tier_prov, r.rsi_prov)} | "
        f"{n(r.rsi)} / {n(r.rsi_prov)} | {n(r.peak_rsi, 0)} ({str(r.peak_month)[:7]}) | {p(r.dd_ath)} | "
        f"{p(r.rev_yoy)} | {p(r.eps_yoy)} | {n(r.val_pct_op, 2)} | {p(r.eps_fwd_growth)} |\n"
        for _, r in df.iterrows())
    return head + rows if len(df) else "*None today.*\n"


def why_not(r) -> str:
    w = []
    if isinstance(r.acq, str):
        w.append(r.acq)
    if isinstance(r.oneoff, str):
        w.append(r.oneoff)
    if pd.isna(r.rev_yoy):
        w.append("no revenue growth figure")
    elif r.rev_yoy < 0.05:
        w.append(f"revenue {r.rev_yoy * 100:+.0f}%")
    if pd.isna(r.eps_yoy):
        w.append("EPS growth n/a")
    elif r.eps_yoy <= 0:
        w.append(f"EPS {r.eps_yoy * 100:+.0f}%")
    if r.prof_past != 1.0:
        w.append("loss years")
    return "; ".join(w) or "profitability history"


def main() -> None:
    live = sorted(OUT.glob("live_*.json"))[-1]
    date = live.stem.replace("live_", "")
    df = pd.DataFrame(json.loads(live.read_text(encoding="utf-8")))
    S = json.loads((OUT / "web_summary.json").read_text(encoding="utf-8"))
    if "tier_sep_prov" in df.columns:  # lists written before the keys lost their month name
        df = df.rename(columns={"tier_sep_prov": "tier_prov", "rsi_sep_prov": "rsi_prov"})
    last_month = pd.Timestamp(df["last_month"].iloc[0] if "last_month" in df.columns else S["last_month"])
    m_done = last_month.strftime("%b")
    m_prov = (last_month + pd.offsets.MonthEnd(1)).strftime("%b")
    m_prov_full = (last_month + pd.offsets.MonthEnd(1)).strftime("%B")
    v3f = sorted(V3_OUT.glob("live_both_opval_*.json"))
    v3_top = []
    if v3f:
        v3 = json.loads(v3f[-1].read_text(encoding="utf-8"))
        v3_top = [r["ticker"] for r in sorted([r for r in v3["top20"] if r.get("value_rank")], key=lambda r: r["value_rank"])]

    ab = df[df.tier.str.contains("A|B")]
    qc = ab[ab.quality & ab.cheap]
    qe = ab[ab.quality & ~ab.cheap]
    sep = df[~df.tier.str.contains("A|B") & df.tier_prov.str.contains("A|B") & df.quality]
    nq = ab[~ab.quality]
    c_only = int((df.tier == "C").sum())

    def st(key, flt):
        s = next(t for t in S["tiers"] if t["key"] == key)["stats"][f"2009+|{flt}|12m"]
        return f"{p(s['median'])} / {s['beat_spy'] * 100:.0f}% / {s['beat_own'] * 100:.0f}% ({s['n']:,})"

    both = [t for t in qc.ticker if t in v3_top]
    deep = [f"{r.ticker} ({r.dd_ath * 100:.0f}%)" for _, r in qc.iterrows() if r.dd_ath <= -0.8]
    to_star = [r.ticker for _, r in qc.iterrows() if "★" not in tier(r.tier, r.rsi) and "★" in tier(r.tier_prov, r.rsi_prov)]
    notes1 = []
    if both:
        notes1.append(f"{', '.join(both)} {'is' if len(both) == 1 else 'are'} also in the turnaround v3 (`both_opval`) top 10 "
                      f"({v3f[-1].stem.replace('live_both_opval_', '')}): two scanners built on different logic agree.")
    if to_star:
        notes1.append(f"{', '.join(to_star)} move{'s' if len(to_star) == 1 else ''} to A ★ if {m_prov_full} closes near the latest price.")
    if deep:
        notes1.append(f"{', '.join(deep)}: a fall that deep needs its own diagnosis before it counts as a reset.")

    # growth that jumped against the year before without new goodwill or new shares: organic acceleration
    jumped = [r.ticker for _, r in ab[ab.quality].iterrows()
              if "prior_yoy" in r and pd.notna(r.prior_yoy) and pd.notna(r.rev_yoy) and r.prior_yoy >= 0
              and r.rev_yoy >= 0.15 and r.rev_yoy >= 3 * r.prior_yoy and r.rev_yoy - r.prior_yoy >= 0.10]
    acq_bits = [f"**{r.ticker}**" for _, r in nq.iterrows() if isinstance(r.acq, str)]
    one_bits = [f"**{r.ticker}**" for _, r in nq.iterrows() if isinstance(r.oneoff, str) and not isinstance(r.acq, str)]
    guard_note = []
    if acq_bits:
        guard_note.append(f"- {', '.join(acq_bits)}: growth bought through an acquisition (new shares, or a jump in growth "
                          "backed by new goodwill). Judge the business on its organic growth.")
    if one_bits:
        guard_note.append(f"- {', '.join(one_bits)}: one-off gains in net income; the earnings growth is not clean.")

    ts = pd.Timestamp(date)
    md = f"""# OpportunityScanner2 candidates on {ts.strftime('%B')} {ts.day}, {ts.year}

*Research tooling output, not investment advice. Scanner and study: `OpportunityScanner2/` (see its README). Prices: Yahoo through {df.last_date.max()}. Tiers use the last completed monthly candle ({last_month.strftime('%B %Y')}); the "{m_prov}, prov." column treats the latest close as if {m_prov_full} had ended, so it can still change. Fundamentals: SEC EDGAR point-in-time tables. Row-level data: `OpportunityScanner2/output/{live.stem}.csv` / `.json`. Generated by `OpportunityScanner2/report.py`.*

## The rule and what the study found

Arming: a monthly candle makes a **new all-time high with monthly RSI(14) ≥ 70** (≥ 5 years of history, $5M+ daily dollar volume).

| Tier | Trigger | Since 2009: 12m median / beat SPY / beat own-stock average (signals) | With the quality filter |
|---|---|---|---|
| **A ★** | former leader (armed in the last 36 months), monthly RSI < 35 | {st('leader + RSI<35', 'none')} | {st('leader + RSI<35', 'quality')} |
| **A** | ... monthly RSI < 40 | {st('leader + RSI<40', 'none')} | {st('leader + RSI<40', 'quality')} |
| **B** | RSI ≤ 68% of the 24-month peak (the −32% rule) **and** price ≥ 40% below ATH | {st('rsi-32% + price-40%', 'none')} | {st('rsi-32% + price-40%', 'quality')}; with cheap too: {st('rsi-32% + price-40%', 'quality + cheap')} |
| **C** | RSI ≤ 68% of the 24-month peak (the −32% rule alone) | {st('rsi-32%', 'none')} | {st('rsi-32%', 'quality')} |

Tier C, the −32% rule as first stated, has done no better than buying the same stock in a random month: it fires early (the median stock falls another {-S['default_2009']['med_mae12'] * 100:.1f}% afterwards). The rule is worth acting on once the damage is deeper (tier B) or the former leader's RSI reaches the old oversold zone (tier A). **Quality** = profitable in the latest year and in two of the three before it, revenue growth ≥ 5%, EPS growing, no one-off gain in earnings, no acquisition-driven growth (new shares, or a jump in growth backed by new goodwill). **Cheap** = operating multiples (P/S, EV/EBITDA, EV/EBIT) in the bottom half of the company's own history ("Val. pct", 0 = cheapest ever).

Each name below still needs its forward story (guidance, estimates, what broke the chart) checked by hand.

## 1. Tier A/B, quality and cheap: the buy-zone list

{table(qc, m_done, m_prov)}
{chr(10).join(notes1)}

## 2. Tier A/B, quality but still expensive vs own history

{table(qe, m_done, m_prov)}
Multiples still in the upper half of their own history: the profile the study rates weakest within tier B. Watchlist names.
{(chr(10) + ', '.join(jumped) + ": revenue growth jumped against the year before with no new goodwill or shares behind it, so the acquisition guard treats it as organic acceleration (before 2026-09-29 the jump alone was flagged).") if jumped else ''}

## 3. Moving into A/B on the provisional {m_prov_full} candle (quality names)

{table(sep, m_done, m_prov)}
Recheck these after the {m_prov_full} close.

## 4. Tier A/B names that fail the quality filter

| Ticker | Tier ({m_done}) | vs ATH | Why not quality |
|---|---|---|---|
{''.join(f"| {r.ticker} | {tier(r.tier, r.rsi)} | {p(r.dd_ath)} | {why_not(r)} |{chr(10)}" for _, r in nq.iterrows())}
Most of these are shrinking or losing earnings: the hindsight split says those are the losing signals.
{chr(10).join(guard_note)}

{c_only} other names are in tier C only (the −32% rule without deeper damage) and are left out here; they are in the CSV and in the web page's grid.

## Notes on the columns

* *Fwd EPS (Yahoo)* is analyst next-year EPS (usually adjusted, non-GAAP) over trailing GAAP EPS: it runs high and is sometimes nonsense, so use it only as a direction check.
* *Peak RSI (month)* is the highest monthly RSI on an all-time-high candle in the last 24 months (36 for tier A).
* Survivorship: the study universe is today's index members. Blow-off-top stocks that later collapsed out of the index are missing, which flatters the history of every tier, the deeper tiers most.
"""
    path = REPORTS / f"OpportunityScanner2 candidates - {date}.md"
    path.write_text(md, encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
