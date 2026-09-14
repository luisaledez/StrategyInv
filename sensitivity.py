"""Round-1 sensitivity scenarios (used by the report): 50% starter position,
never-sell accumulation, and both combined. Writes sensitivity.json."""
import json
import backtest as bt

TICKERS = ["nflx", "msft", "enph", "nvda", "cvx"]

def sweep(label, scen, **over):
    saved = {k: getattr(bt, k) for k in over}
    for k, v in over.items():
        setattr(bt, k, v)
    scen[label] = {}
    for t in TICKERS:
        r = bt.run(t, use_options=False)
        scen[label][t] = {k: r[k] for k in ("final", "total_return", "cagr", "max_drawdown", "avg_invested")}
        scen[label][t]["curve"] = r["curve"]
    for k, v in saved.items():
        setattr(bt, k, v)

if __name__ == "__main__":
    scen = {}
    sweep("start50", scen, INITIAL_FRACTION=0.50)
    sweep("nosell", scen, SELL_GAIN=1e9)
    sweep("nosell_start50", scen, SELL_GAIN=1e9, INITIAL_FRACTION=0.50)
    for label, rows in scen.items():
        avg = sum(r["final"] for r in rows.values()) / len(rows)
        print(f"{label:16} basket avg {avg:>12,.0f}")
    json.dump(scen, open("sensitivity.json", "w"))
    print("wrote sensitivity.json")
