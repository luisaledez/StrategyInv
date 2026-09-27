"""Run the strategy on synthetic lost-decade data for several random seeds.

For each seed: generate the data set (synthetic.py) into synthetic/data/, run
screen.py and backtest.py on it (TURNAROUND_BT_ROOT points the pipeline at that
folder), build the HTML report, and copy the outputs to synthetic/output/seed<k>/.
Then write synthetic/output/summary.md with every scenario per seed in nominal
and in real (CPI-deflated) terms, and the median across seeds.

    python synthetic_run.py --seeds 0,1,2,3,4
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import synthetic  # noqa: E402

SYN_OUT = HERE / "synthetic" / "output"


def cpi_index() -> pd.Series:
    """Cumulative price level, monthly, = 1.0 at the test start."""
    months = pd.date_range(synthetic.PRE_START, synthetic.TEST_END, freq="ME")
    lvl = [1.0]
    for m in months[1:]:
        lvl.append(lvl[-1] * (1 + synthetic.CPI[m.year] / 100.0) ** (1 / 12))
    s = pd.Series(lvl, index=months)
    return s / s.asof(pd.Timestamp(synthetic.TEST_START))


def deflate(amount: float, date: str, cpi: pd.Series) -> float:
    return amount / float(cpi.asof(pd.Timestamp(date)))


def run_seed(seed: int) -> dict:
    root = synthetic.DATA_ROOT
    import data as real_data
    synthetic.generate(seed, real_data.universe_tickers(), root)
    env = {**os.environ, "TURNAROUND_BT_ROOT": str(root)}
    for script in ("screen.py", "backtest.py", "report_html.py"):
        r = subprocess.run([sys.executable, str(HERE / script)], env=env, cwd=str(HERE),
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-3000:], file=sys.stderr)
            raise SystemExit(f"{script} failed for seed {seed}")
        tail = [ln for ln in r.stderr.strip().splitlines() if ln.strip()][-12:]
        print(f"  [{script}] " + " | ".join(t.strip() for t in tail[-1:]), file=sys.stderr)
    dest = SYN_OUT / f"seed{seed}"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(root / "output", dest)
    shutil.copy(root / "config.json", dest / "config.json")
    return json.loads((dest / "results.json").read_text(encoding="utf-8"))


def summarise(results: dict[int, dict]) -> Path:
    cpi = cpi_index()
    end_level = float(cpi.asof(pd.Timestamp(synthetic.TEST_END)))
    rows = []
    for seed, res in results.items():
        bench = res.pop("benchmarks")
        entries = list(res.items()) + [("index (buy & hold)", list(bench.values())[0])]
        for name, r in entries:
            s = r["summary"]
            wd_real = sum(deflate(w["amount"], w["date"], cpi) for w in r["withdrawals"])
            final_real = s["final_value"] / end_level
            rows.append({"seed": seed, "scenario": name, "final": s["final_value"], "withdrawn": s["total_withdrawn"],
                         "total": s["final_plus_withdrawn"], "irr": s["irr"], "cagr_index": s["cagr_tr_index"],
                         "max_dd": s["max_drawdown"], "final_real": final_real, "withdrawn_real": wd_real,
                         "total_real": final_real + wd_real, "trades": s.get("trades"),
                         "closed": s.get("closed_positions"), "win_rate": s.get("win_rate")})
        res["benchmarks"] = bench
    df = pd.DataFrame(rows)
    df.to_csv(SYN_OUT / "summary.csv", index=False)
    yrs = (pd.Timestamp(synthetic.TEST_END) - pd.Timestamp(synthetic.TEST_START)).days / 365.25

    def money(x):
        return f"${x:,.0f}"

    def pct(x):
        return "n/a" if x is None or x != x else f"{x * 100:+.1f}%"

    L = [f"# Synthetic lost decade — {synthetic.TEST_START} to {synthetic.TEST_END}, {len(results)} seeds", ""]
    L += ["Same rules and scenarios as the real backtest, run on synthetic data built on the real 1968–1982 S&P 500 path "
          "(see synthetic.py). $100,000 start. Real figures are deflated with BLS CPI-U: the price level at the end is "
          f"{end_level:.2f}× the start, so a nominal result has to reach {money(100000 * end_level)} just to preserve purchasing power. "
          f"Window length {yrs:.1f} years.", ""]
    L += ["## Median across seeds", ""]
    hdr = ["Scenario", "Final (nominal)", "Withdrawn (nominal)", "Final + withdrawn", "Final (real)", "Withdrawn (real)",
           "Final + withdrawn (real)", "IRR", "CAGR index", "Real CAGR index", "Max DD", "Closed trades", "Win rate"]
    L += ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
    order = [c for c in dict.fromkeys(df["scenario"])]
    infl_cagr = end_level ** (1 / yrs) - 1
    for sc in order:
        g = df[df["scenario"] == sc]
        med = g.median(numeric_only=True)
        L.append("| " + " | ".join([
            f"**{sc}**", money(med["final"]), money(med["withdrawn"]), money(med["total"]), money(med["final_real"]),
            money(med["withdrawn_real"]), money(med["total_real"]), pct(med["irr"]), pct(med["cagr_index"]),
            pct((1 + med["cagr_index"]) / (1 + infl_cagr) - 1), pct(med["max_dd"]),
            f"{med['closed']:.0f}" if med["closed"] == med["closed"] else "", pct(med["win_rate"]) if med["win_rate"] == med["win_rate"] else "",
        ]) + " |")
    L += ["", f"Inflation over the window: {pct(infl_cagr)} a year.", ""]
    L += ["## Every seed", ""]
    hdr2 = ["Seed", "Scenario", "Final (nominal)", "Withdrawn", "Final + withdrawn", "Final + withdrawn (real)", "IRR", "CAGR index", "Max DD"]
    L += ["| " + " | ".join(hdr2) + " |", "|" + "---|" * len(hdr2)]
    for _, r in df.iterrows():
        L.append("| " + " | ".join([str(r["seed"]), r["scenario"], money(r["final"]), money(r["withdrawn"]), money(r["total"]),
                                    money(r["total_real"]), pct(r["irr"]), pct(r["cagr_index"]), pct(r["max_dd"])]) + " |")
    L += ["", "## Seed-by-seed yearly detail", "",
          "Each seed's full report (yearly returns, withdrawals, trades, quarterly lists) is in `seed<k>/report.md` "
          "and `seed<k>/report.html`; `seed<k>/*_trades.csv` has every trade.", ""]
    # base vs index by year, median across seeds
    L += ["## Base vs index, year by year (median return across seeds)", ""]
    per_year = {}
    for seed, res in results.items():
        for y in res["base"]["years"]:
            per_year.setdefault(y["year"], {}).setdefault("base", []).append(y["return"])
        for y in list(res["benchmarks"].values())[0]["years"]:
            per_year.setdefault(y["year"], {}).setdefault("index", []).append(y["return"])
        for name in ("rotate", "no_trim"):
            for y in res[name]["years"]:
                per_year.setdefault(y["year"], {}).setdefault(name, []).append(y["return"])
    L += ["| Year | base | no_trim | rotate | index | CPI |", "|---|---|---|---|---|---|"]
    for yr in sorted(per_year):
        d = per_year[yr]
        L.append(f"| {yr} | {pct(np.median(d.get('base', [np.nan])))} | {pct(np.median(d.get('no_trim', [np.nan])))} | "
                 f"{pct(np.median(d.get('rotate', [np.nan])))} | {pct(np.median(d.get('index', [np.nan])))} | "
                 f"{synthetic.CPI.get(yr, float('nan')):+.1f}% |")
    p = SYN_OUT / "summary.md"
    p.write_text("\n".join(L), encoding="utf-8")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="0,1,2,3,4")
    ap.add_argument("--summary-only", action="store_true", help="re-read seed folders and rebuild summary.md")
    args = ap.parse_args()
    seeds = [int(s) for s in args.seeds.split(",")]
    SYN_OUT.mkdir(parents=True, exist_ok=True)
    results = {}
    for seed in seeds:
        if args.summary_only:
            results[seed] = json.loads((SYN_OUT / f"seed{seed}" / "results.json").read_text(encoding="utf-8"))
        else:
            print(f"seed {seed}", file=sys.stderr)
            results[seed] = run_seed(seed)
    print(f"wrote {summarise(results)}", file=sys.stderr)


if __name__ == "__main__":
    main()
