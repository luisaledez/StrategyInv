import json, datetime as dt

res = json.load(open("results.json"))
sens = json.load(open("sensitivity.json"))
TICKERS = ["nflx", "msft", "enph", "nvda", "cvx"]
VARIANTS = ["bh", "dip", "dip_opt"]

def weekly(curve):
    """keep last point of each ISO week + final point"""
    out, last_key = [], None
    for i, (d, v, inv) in enumerate(curve):
        key = dt.date.fromisoformat(d).isocalendar()[:2]
        if key != last_key and out is not None and i > 0:
            out.append(prev)
        last_key = key
        prev = (d, v)
    out.append(prev)
    return out

def summarize(r):
    return {
        "final": r["final"],
        "total_return": r["total_return"],
        "cagr": r["cagr"],
        "max_drawdown": r["max_drawdown"],
        "avg_invested": r["avg_invested"],
        "stats": r.get("stats", {}),
    }

report = {"tickers": {}, "portfolio": {}, "sensitivity": {}, "spy": {}}

# per-ticker
for t in TICKERS:
    entry = {"summary": {v: summarize(res[t][v]) for v in VARIANTS}}
    # align three curves by date
    by_date = {}
    for v in VARIANTS:
        for d, val in weekly(res[t][v]["curve"]):
            by_date.setdefault(d, {})[v] = val
    rows = [[d, m.get("bh"), m.get("dip"), m.get("dip_opt")]
            for d, m in sorted(by_date.items()) if len(m) == 3]
    entry["curve"] = rows
    report["tickers"][t] = entry

# equal-weight portfolio (per-$100k basis: average of the 5 sleeves)
port_by_date = {}
for v in VARIANTS:
    for t in TICKERS:
        for d, val, inv in res[t][v]["curve"]:
            port_by_date.setdefault(d, {}).setdefault(v, []).append(val)
rows = []
for d, m in sorted(port_by_date.items()):
    if all(len(m.get(v, [])) == 5 for v in VARIANTS):
        rows.append([d] + [sum(m[v]) / 5 for v in VARIANTS])
# weekly downsample
wrows, last_key = [], None
for i, r in enumerate(rows):
    key = dt.date.fromisoformat(r[0]).isocalendar()[:2]
    if key != last_key and i > 0:
        wrows.append(prev)
    last_key = key
    prev = r
wrows.append(prev)

spy_map = {d: v for d, v, inv in res["spy"]["bh"]["curve"]}
port_curve = [[d, round(a, 0), round(b, 0), round(c, 0), spy_map.get(d)] for d, a, b, c in wrows]
report["portfolio"]["curve"] = port_curve

def curve_stats(vals):
    peak, mdd = vals[0], 0.0
    for v in vals:
        peak = max(peak, v)
        mdd = min(mdd, v / peak - 1)
    years = 11.62
    return {"final": vals[-1], "total_return": vals[-1] / 100000 - 1,
            "cagr": (vals[-1] / 100000) ** (1 / years) - 1, "max_drawdown": mdd}

for i, v in enumerate(VARIANTS):
    report["portfolio"][v] = curve_stats([r[i + 1] for r in rows])
report["spy"] = summarize(res["spy"]["bh"])

# sensitivity
for label, byticker in sens.items():
    report["sensitivity"][label] = {
        t: {k: r[k] for k in ("final", "total_return", "cagr", "max_drawdown", "avg_invested")}
        for t, r in byticker.items()
    }
    report["sensitivity"][label]["portfolio_final"] = sum(r["final"] for r in byticker.values()) / 5

json.dump(report, open("report_data.json", "w"))
sz = len(json.dumps(report))
print("report_data.json:", f"{sz/1024:.0f} KB")
print("portfolio:", {v: {k: round(x, 3) for k, x in report["portfolio"][v].items()} for v in VARIANTS})
