"""Third turnaround backtest: the second backtest's "re-screen + guide-cut
proxy" rule set (`rescreen_only` in ../turnaround_backtest/backtest_v2.py)
run on snapshots with the entry-data guards of screen_v3.py.

Portfolio rules (unchanged): $100,000, at most 10% per stock, names that leave
the list are kept, trim half at +50%, sell all at monthly RSI(14) >= 90, a
>100% winner is sold to fund a new top-10 name, spin-off / divestiture
re-screen (filings re-based by >= 30% -> sold unless still on the list),
guidance-cut proxy (TTM EPS >= 15% below its entry level within 12 months ->
sold), yearly withdrawals (10% / 7.5% / 5%). No position cap, no S&P parking.

Scenarios: one per screen variant (ref, oneoff, acq, both, both_opval) from
2004-01-01, and the same from 2009-01-01.

    python screen_v3.py        # first
    python backtest_v3.py      # -> output/results.json, report.md, <scenario>_trades.csv, *_equity.csv
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
BT = HERE.parent / "turnaround_backtest"
sys.path.insert(0, str(BT))
sys.path.insert(0, str(HERE))
import engine  # noqa: E402
import backtest  # noqa: E402
from engine import Scenario  # noqa: E402
import screen_v3  # noqa: E402

OUT = HERE / "output"
S0 = engine.data.START.date().isoformat()
RULES = dict(rebase_exit=True, rebase_min_drop=0.30, guide_cut_exit=0.15, guide_cut_months=12)
LABELS = {
    "ref": "Reference: organic screen only (= backtest v2 `rescreen_only`)",
    "oneoff": "+ one-off EPS guard (net income > operating income, or a one-quarter jump in TTM net income)",
    "acq": "+ acquisition guard (shares +15% y/y, or growth >= 15% that is 3x and 10 points above a year earlier)",
    "both": "+ both guards",
    "both_opval": "+ both guards, valuation ranked on P/S, EV/EBITDA and EV/EBIT (no P/E)",
}

INTRO = [
    "**Third backtest.** The second backtest's re-screen + guide-cut proxy rule set (`rescreen_only`), with entry "
    "guards that the organic filter did not provide: a **one-off EPS guard** (trailing net income above trailing "
    "operating income, or one quarter lifting TTM net income by more than 50% while operating income rose less "
    "than 25%: a non-operating gain or a tax benefit is inflating the P/E) and an **acquisition guard** (diluted "
    "shares up more than 15% year over year, or trailing revenue growth of 15%+ that is at least three times and "
    "ten points above the growth reported a year earlier while that earlier growth was not negative: a deal that "
    "closed during the year, whether it stepped up in one quarter or over four). A variant also ranks valuation "
    "on P/S, EV/EBITDA and EV/EBIT instead of P/E. See `screen_v3.py` for the exact tests and "
    "`README.md` for why they were tried.",
]


def load_snaps(variant: str) -> list[dict]:
    return json.loads((OUT / f"snapshots_{variant}.json").read_text(encoding="utf-8"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    snaps = {v: load_snaps(v) for v in screen_v3.VARIANTS}
    tickers = sorted({r["ticker"] for v in snaps.values() for s in v for r in s["top10"]})
    print(f"backtest v3: {len(snaps['ref'])} snapshots per variant, {len(tickers)} distinct top-10 tickers", file=sys.stderr)
    mkt = engine.Market(tickers, engine.data.START, fundamentals=True, rebase=True)
    scenarios = []
    for v in screen_v3.VARIANTS:
        scenarios.append((Scenario(v, LABELS[v], start=S0, **RULES), v))
    for v in screen_v3.VARIANTS:
        scenarios.append((Scenario(f"{v}_2009", LABELS[v] + ", started 2009-01-01", start="2009-01-01", **RULES), v))
    results, benches = {}, {}
    for sc, v in scenarios:
        r = engine.simulate(sc, snaps[v], mkt)
        results[sc.name] = r
        s = r["summary"]
        print(f"  {sc.name:16s} final {s['final_value']:>12,.0f}  withdrawn {s['total_withdrawn']:>10,.0f}  "
              f"IRR {s['irr'] * 100:5.1f}%  maxDD {s['max_drawdown'] * 100:5.1f}%  closed {s['closed_positions']:3d}  "
              f"win {s['win_rate'] * 100:4.0f}%  avg {s['avg_closed_return_pct']:5.1f}%", file=sys.stderr)
        pd.DataFrame(r["trades"]).to_csv(OUT / f"{sc.name}_trades.csv", index=False)
        r["equity"].to_csv(OUT / f"{sc.name}_equity.csv")
        if sc.start[:4] not in benches:
            benches[sc.start[:4]] = engine.benchmark(sc, mkt)
    for key, b in benches.items():
        b["equity"].to_csv(OUT / f"spy_{key}_equity.csv")
    out = {name: {k: v for k, v in r.items() if k != "equity"} for name, r in results.items()}
    out["benchmarks"] = {k: {kk: vv for kk, vv in b.items() if kk != "equity"} for k, b in benches.items()}
    (OUT / "results.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    p = backtest.write_report(results, benches, snaps["both"], out=OUT, title="Turnaround candidates backtest v3", intro=INTRO)
    append_guard_sections(p, snaps)
    print(f"wrote {p}", file=sys.stderr)


def append_guard_sections(p: Path, snaps: dict[str, list[dict]]) -> None:
    L = ["", "## What the guards changed, snapshot by snapshot", "",
         "Organic-eligible names removed by each guard, and the top-10 list of the reference screen with the names "
         "that the `both` variant dropped struck out and its replacements in bold.", "",
         "| Snapshot | Organic eligible | Removed: one-off | Removed: acq | Top 10 (ref → both) |", "|---|---|---|---|---|"]
    for s_ref, s_both in zip(snaps["ref"], snaps["both"]):
        ref = [r["ticker"] for r in s_ref["top10"]]
        both = [r["ticker"] for r in s_both["top10"]]
        if not ref and not both:
            continue
        cells = [f"~~{t}~~" if t not in both else t for t in ref] + [f"**{t}**" for t in both if t not in ref]
        L.append(f"| {s_ref['date']} | {s_ref['n_organic']} | {s_ref['n_flag_oneoff']} | {s_ref['n_flag_acq']} | {', '.join(cells)} |")
    L += ["", "## Names the guards removed from the reference top 10 (with the reason)", "",
          "| Snapshot | Ticker | Growth | Val pct | One-off reason | Acquisition reason |", "|---|---|---|---|---|---|"]
    for s_ref in snaps["ref"]:
        for r in s_ref["top10"]:
            if r["oneoff"] or r["acq"]:
                L.append(f"| {s_ref['date']} | {r['ticker']} | {r['rev_yoy'] * 100:+.0f}% | {r['val_pct']:.2f} | "
                         f"{r['oneoff'] or ''} | {r['acq'] or ''} |")
    L += ["", "## Today's lists", ""]
    for v in screen_v3.VARIANTS:
        cur = json.loads((OUT / f"current_{v}.json").read_text(encoding="utf-8"))
        L.append(f"* **{v}** (as of {cur['as_of']}): top 10 {', '.join(r['ticker'] for r in cur['top10'])}; "
                 f"top 20 {', '.join(r['ticker'] for r in cur['top20'])}")
    with p.open("a", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
