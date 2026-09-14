"""
Round 3: the Growth Combo (30% never-sold core + trend-filtered sells +
SPY-parked cash + %-of-sleeve tiers) with cash-secured puts (no covered
calls), tested out-of-sample on XOM, NVO, INTC, QCOM, AMKR, AEHR, BABA.
"""
import json
import backtest as bt
import improved as im

NEW = ["xom", "nvo", "intc", "qcom", "amkr", "aehr", "baba"]
OLD = ["nflx", "msft", "enph", "nvda", "cvx"]

COMBO = dict(core_frac=0.30, core_never_sell=True, trend_filter=True,
             park_spy=True, pct_budgets=True)
COMBO_PUTS = dict(**COMBO, use_options=True, no_calls=True)

def strip(r):
    return {k: v for k, v in r.items() if k != "trades"}

out = {}
for t in NEW:
    out[t] = {
        "bh": strip(bt.buy_hold(t)),
        "combo": strip(im.run2(t, **COMBO)),
        "combo_puts": strip(im.run2(t, **COMBO_PUTS)),
    }

# puts-only combo on the original five, for the cross-check
old_puts = {t: strip(im.run2(t, **COMBO_PUTS)) for t in OLD}
out["_old_combo_puts_basket_final"] = sum(old_puts[t]["final"] for t in OLD) / 5
out["_old_puts"] = {t: {k: old_puts[t][k] for k in ("final", "cagr", "max_drawdown")} for t in OLD}

hdr = f"{'ticker':6} {'variant':11} {'final $':>12} {'CAGR':>7} {'maxDD':>6} {'exp':>5} {'buys':>5} {'sells':>5} {'assign':>6} {'prem':>9} {'divs':>8}"
print(hdr)
for t in NEW:
    for v in ("bh", "combo", "combo_puts"):
        r = out[t][v]
        s = r["stats"]
        print(f"{t.upper():6} {v:11} {r['final']:>12,.0f} {r['cagr']:>7.1%} {r['max_drawdown']:>6.0%} {r['avg_invested']:>5.0%} "
              f"{s.get('buys',0):>5.0f} {s.get('sells',0):>5.0f} {s.get('put_assignments',0):>6.0f} {s.get('put_premium',0):>9,.0f} {s.get('dividends',0):>8,.0f}")
print(f"\nold-5 basket, combo+puts: {out['_old_combo_puts_basket_final']:,.0f}")
for t in OLD:
    r = out["_old_puts"][t]
    print(f"  {t.upper():5} {r['final']:>12,.0f} {r['cagr']:>6.1%} {r['max_drawdown']:>5.0%}")

json.dump(out, open("round3.json", "w"))
print("wrote round3.json")
