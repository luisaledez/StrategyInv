import json, datetime as dt

r3 = json.load(open("round3.json"))
NEW = ["xom", "nvo", "intc", "qcom", "amkr", "aehr", "baba"]
VARIANTS = ["bh", "combo", "combo_puts"]
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

out = {"tickers": {}, "basket": {}}

for t in NEW:
    e = {"summary": {}}
    by_date = {}
    for v in VARIANTS:
        r = r3[t][v]
        e["summary"][v] = {k: r[k] for k in ("final", "total_return", "cagr", "max_drawdown", "avg_invested")}
        e["summary"][v]["stats"] = r["stats"]
        for d, val, inv in r["curve"]:
            by_date.setdefault(d, {})[v] = val
    rows = [[d, m.get("bh"), m.get("combo"), m.get("combo_puts")]
            for d, m in sorted(by_date.items()) if len(m) == 3]
    e["curve"] = weekly(rows)
    out["tickers"][t] = e

# basket
by_date = {}
for v in VARIANTS:
    for t in NEW:
        for d, val, inv in r3[t][v]["curve"]:
            by_date.setdefault(d, {}).setdefault(v, []).append(val)
rows = [[d] + [sum(m[v]) / 7 for v in VARIANTS]
        for d, m in sorted(by_date.items()) if all(len(m.get(v, [])) == 7 for v in VARIANTS)]

def stats(vals):
    peak, mdd = vals[0], 0.0
    for x in vals:
        peak = max(peak, x)
        mdd = min(mdd, x / peak - 1)
    return {"final": vals[-1], "cagr": (vals[-1] / 100000) ** (1 / YEARS) - 1, "max_drawdown": mdd}

for i, v in enumerate(VARIANTS):
    out["basket"][v] = stats([r[i + 1] for r in rows])
out["basket"]["curve"] = [[r[0], round(r[1]), round(r[2]), round(r[3])] for r in weekly(rows)]

ratios = sorted(r3[t]["combo_puts"]["final"] / r3[t]["bh"]["final"] for t in NEW)
out["median_ratio"] = ratios[3]
out["old_puts_basket"] = r3["_old_combo_puts_basket_final"]
ex = [t for t in NEW if t != "aehr"]
out["ex_aehr"] = {"bh": sum(r3[t]["bh"]["final"] for t in ex) / 6,
                  "combo_puts": sum(r3[t]["combo_puts"]["final"] for t in ex) / 6}

json.dump(out, open("round3_report.json", "w"))
b = out["basket"]
print("basket:", {v: {k: round(x, 3) for k, x in b[v].items()} for v in VARIANTS})
print("median ratio:", round(out["median_ratio"], 2), "| ex-AEHR:", {k: round(v) for k, v in out["ex_aehr"].items()})
print("size:", len(json.dumps(out)) // 1024, "KB")
