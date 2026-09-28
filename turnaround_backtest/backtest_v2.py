"""Second turnaround backtest (2026-09-27 request), kept apart from the first
one: everything is written to output_v2/, output/ is untouched.

Rules on top of the base scenario (trim half at +50%, RSI(m) 90 exit, replace
>100% winners for new names, yearly withdrawals, max 10% per stock):

  * organic growth only (screen.py --organic): trailing revenue growth must be
    positive and under 100%, the trailing figure must not have jumped more than
    60% quarter to quarter in the last eight quarters (acquisition), and the
    latest quarter must not be below its year-ago quarter while the trailing
    year is up (a spike already fading). Applied before the top-20 growth rank.
  * never more than MAX_POSITIONS stocks: when the book is full a new name only
    gets in if a >100% winner that left the list can be sold to make room
  * S&P 500 correction rule: when SPY closes 10% or more below its running high,
    no new stocks are bought and all idle cash (trim and sale proceeds,
    dividends) is parked in SPY; once the drawdown is back within 5% the
    correction is over and SPY is sold only as needed to fund the next new names
  * spin-off / major divestiture re-screen: when a holding's filings re-base its
    history by 30% or more (a year-ago comparative restated to <= 0.70x, or a
    reported annual revenue <= 0.70x the trailing reading, both from the EDGAR
    loader's warnings), it is treated as a new position: kept only if it is on
    the current top-10 list, otherwise sold at that month-end
  * guidance-cut proxy: the data set has no guidance history, so "a full-year
    guidance cut within 12 months of purchase" is approximated by the
    point-in-time TTM EPS falling 15% or more below its level at entry within
    the first 12 months; the position is sold at that month-end

    python screen.py --organic --out output_v2     # organic-growth snapshots
    python backtest_v2.py                           # -> output_v2/report.md, results.json, *_trades.csv
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine  # noqa: E402
import backtest  # noqa: E402
from engine import Scenario  # noqa: E402

OUT = HERE / "output_v2"
S0 = engine.data.START.date().isoformat()
MAX_POSITIONS = 14   # "stay under 15 stocks at all times"

PARK = dict(spy_park=0.10, spy_resume=0.05, spy_high_window=252)   # 10% below the 1-year high opens, within 5% closes
V2 = dict(start=S0, max_positions=MAX_POSITIONS, rebase_exit=True, rebase_min_drop=0.30,
          guide_cut_exit=0.15, guide_cut_months=12, **PARK)
SCENARIOS = [
    Scenario("v2", "All new rules: organic entries, <15 stocks, S&P correction parking, spin-off re-screen, guide-cut proxy", **V2),
    Scenario("v2_no_park", "v2 without the S&P correction parking", **{**V2, "spy_park": None}),
    Scenario("v2_eps30", "v2 plus the loss-control exit: sell when TTM EPS is 30% below entry", **{**V2, "eps_exit": 0.30}),
    Scenario("organic_only", "Base rules with only the organic-growth entry filter (isolates the filter)", start=S0),
    Scenario("cap14_only", "Base rules with only the <15 stocks cap (organic entries)", start=S0, max_positions=MAX_POSITIONS),
    Scenario("park_only", "Base rules with only the S&P correction parking (organic entries)", start=S0, **PARK),
    Scenario("rescreen_only", "Base rules with only the spin-off re-screen and the guide-cut proxy (organic entries)",
             start=S0, rebase_exit=True, rebase_min_drop=0.30, guide_cut_exit=0.15, guide_cut_months=12),
    Scenario("v2_2009", "v2 started 2009-01-01 (no idle pre-2008 cash to park)", **{**V2, "start": "2009-01-01"}),
    Scenario("v2_no_park_2009", "v2 without parking, started 2009-01-01", **{**V2, "start": "2009-01-01", "spy_park": None}),
]

INTRO = [
    "**Second backtest.** Same engine and data as the first backtest (`output/`), with the organic-growth "
    "entry filter, a cap of fewer than 15 stocks, S&P 500 correction parking (SPY drawdown >= 10% from its "
    "running high: no new stocks, idle cash into SPY until the drawdown is back within 5%), a spin-off / "
    "divestiture re-screen (a holding whose filings re-base by >= 30% is sold unless it is on the current "
    "top-10 list) and a guidance-cut proxy (no guidance data exists here, so: TTM EPS >= 15% below its entry "
    "level within the first 12 months → sell). See `backtest_v2.py` for the exact rules and "
    "`../research_notes/turnaround_worst_open.md` for why they were tried.",
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    snaps_path = OUT / "snapshots.json"
    if not snaps_path.exists():
        print("run `python screen.py --organic --out output_v2` first", file=sys.stderr)
        sys.exit(1)
    snaps = json.loads(snaps_path.read_text(encoding="utf-8"))
    tickers = sorted({r["ticker"] for s in snaps for r in s["top10"]})
    print(f"backtest v2: {len(snaps)} snapshots, {len(tickers)} distinct top-10 tickers", file=sys.stderr)
    mkt = engine.Market(tickers, engine.data.START, fundamentals=True, rebase=True)
    n_events = sum(len(v) for v in mkt.rebase.values())
    print(f"  re-basing events (spin-offs / divestitures / discontinued ops) on candidate tickers: {n_events}", file=sys.stderr)
    results, benches = {}, {}
    for sc in SCENARIOS:
        r = engine.simulate(sc, snaps, mkt)
        results[sc.name] = r
        s = r["summary"]
        print(f"  {sc.name:13s} final {s['final_value']:>12,.0f}  withdrawn {s['total_withdrawn']:>10,.0f}  "
              f"IRR {s['irr'] * 100:5.1f}%  maxDD {s['max_drawdown'] * 100:5.1f}%  trades {s['trades']}", file=sys.stderr)
        pd.DataFrame(r["trades"]).to_csv(OUT / f"{sc.name}_trades.csv", index=False)
        r["equity"].to_csv(OUT / f"{sc.name}_equity.csv")
        if sc.start[:4] not in benches:
            benches[sc.start[:4]] = engine.benchmark(sc, mkt)
    for key, b in benches.items():
        b["equity"].to_csv(OUT / f"spy_{key}_equity.csv")
    out = {name: {k: v for k, v in r.items() if k != "equity"} for name, r in results.items()}
    out["benchmarks"] = {k: {kk: vv for kk, vv in b.items() if kk != "equity"} for k, b in benches.items()}
    out["rebase_events"] = {t: [(d.date().isoformat(), r) for d, r in ev] for t, ev in mkt.rebase.items() if ev}
    (OUT / "results.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    p = backtest.write_report(results, benches, snaps, out=OUT, title="Turnaround candidates backtest v2", intro=INTRO)
    print(f"wrote {p}", file=sys.stderr)


if __name__ == "__main__":
    main()
