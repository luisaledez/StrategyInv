"""Build round2.json (basket stats + curves for the improvement variants)
from improved.json. Run from the repo root: python report/prep_round2.py"""
import json, datetime as dt

imp = json.load(open("improved.json"))
TICKERS = ["nflx", "msft", "enph", "nvda", "cvx"]
YEARS = 11.62

def weekly(rows):
    wk, lk = [], None
    for i, r in enumerate(rows):
        key = dt.date.fromisoformat(r[0]).isocalendar()[:2]
        if key != lk and i > 0:
            wk.append(prev)
        lk = key
        prev = r
    wk.append(prev)
    return wk

def basket(name):
    by_date = {}
    for t in TICKERS:
        for d, v, inv in imp[name][t]["curve"]:
            by_date.setdefault(d, []).append((v, inv))
    rows = [(d, sum(x[0] for x in m) / 5, sum(x[1] for x in m) / 5)
            for d, m in sorted(by_date.items()) if len(m) == 5]
    vals = [v for _, v, _ in rows]
    peak, mdd = vals[0], 0.0
    for v in vals:
        peak = max(peak, v)
        mdd = min(mdd, v / peak - 1)
    return rows, {"final": vals[-1], "cagr": (vals[-1] / 100000) ** (1 / YEARS) - 1,
                  "max_drawdown": mdd, "avg_exposure": sum(i for _, _, i in rows) / len(rows)}

out = {"summary": {}, "curves": {}}
for name in ["gain50", "spy_park", "trend", "trend_park", "trend_park_opt", "combo_noopt", "combo", "core50"]:
    rows, s = basket(name)
    out["summary"][name] = s
    print(f"{name:15} final {s['final']:>12,.0f} cagr {s['cagr']:>6.1%} mdd {s['max_drawdown']:>5.0%}")
    if name in ("trend_park_opt", "combo_noopt"):
        out["curves"][name] = [[d, round(v)] for d, v, i in weekly(rows)]

out["per_ticker"] = {name: {t: {k: imp[name][t][k] for k in ("final", "cagr", "max_drawdown", "avg_invested")}
                            for t in TICKERS} for name in imp}
json.dump(out, open("round2.json", "w"))
print("wrote round2.json")
