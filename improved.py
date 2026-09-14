"""
Round 2: improvement variants on the dip-ladder strategy.

Levers tested (each isolates one weakness found in round 1):
  core50     - 50% bought day 1 and NEVER sold (rotation only touches tier lots)
  trend      - sell rule active only when price < 200-day MA (let uptrends run)
  spy_park   - idle cash held in SPY instead of cash at 2.5% (kills cash drag)
  gain50     - sell trigger raised from +20% to +50%
  combo      - 30% never-sold core + SPY parking + trend-filtered sells
               + options overlay + tier budgets as % of current sleeve value
"""
import json, math
from collections import defaultdict
import backtest as bt

CAPITAL = bt.CAPITAL
TIERS = bt.TIERS

def run2(ticker, core_frac=0.20, core_never_sell=False, sell_gain=0.20,
         trend_filter=False, park_spy=False, use_options=False, pct_budgets=False,
         no_calls=False):
    dates, px, divs = bt.load(ticker)
    sdates, spx, sdivs = bt.load("spy")
    spy_by_date = dict(zip(sdates, spx))
    sdiv_by_date = sdivs
    i0 = next(i for i, d in enumerate(dates) if d >= bt.START)

    cash = CAPITAL
    spy_sh = 0.0
    last_spy = spy_by_date.get(dates[i0]) or spx[0]
    lots = []
    tier_filled = {t: False for t, _ in TIERS}
    open_put = None
    open_call = None
    stats = defaultdict(float)
    curve = []

    # rolling 200dma
    def ma200(i):
        if i < 199:
            return None
        return sum(px[i - 199:i + 1]) / 200

    if core_frac > 0:
        sh = CAPITAL * core_frac / px[i0]
        lots.append({"shares": sh, "cost": px[i0], "core": core_never_sell})
        cash -= CAPITAL * core_frac
        stats["buys"] += 1

    next_opt = i0 + bt.OPT_CYCLE

    for i in range(i0, len(px)):
        d, S = dates[i], px[i]
        sp = spy_by_date.get(d)
        if sp:
            last_spy = sp
        sp = last_spy

        if not park_spy:
            cash *= 1 + bt.CASH_RATE / 252
        held = sum(l["shares"] for l in lots)
        if d in divs and held > 0:
            cash += divs[d] * held
            stats["dividends"] += divs[d] * held
        if d in sdiv_by_date and spy_sh > 0:
            cash += sdiv_by_date[d] * spy_sh

        def total_value():
            return cash + spy_sh * sp + sum(l["shares"] for l in lots) * S

        def ensure_cash(amount):
            """pull funds out of SPY if needed; returns cash actually available"""
            nonlocal cash, spy_sh
            if cash >= amount or spy_sh <= 0:
                return min(cash, amount) if cash < amount else amount
            need = amount - cash
            sell_sh = min(spy_sh, need / sp)
            cash += sell_sh * sp
            spy_sh -= sell_sh
            return min(cash, amount)

        hi = max(px[max(0, i - bt.HIGH_WINDOW):i + 1])
        dd = S / hi - 1
        ma = ma200(i)
        sell_ok = (not trend_filter) or (ma is not None and S < ma)

        # settle options
        if use_options and open_put and i >= open_put["expiry_idx"]:
            K = open_put["strike"]
            if S < K:
                sh = open_put["shares"]
                avail = ensure_cash(sh * K)
                sh = avail / K
                if sh > 0:
                    cash -= sh * K
                    lots.append({"shares": sh, "cost": K, "core": False})
                    tier_filled[open_put["tier"]] = True
                    stats["put_assignments"] += 1
                    stats["buys"] += 1
            open_put = None
        if use_options and open_call and i >= open_call["expiry_idx"]:
            K = open_call["strike"]
            lot = open_call["lot"]
            if S > K and lot in lots:
                cash += lot["shares"] * K
                lots.remove(lot)
                stats["calls_assigned"] += 1
                stats["sells"] += 1
            open_call = None

        if dd > bt.REARM_DD:
            tier_filled = {t: False for t, _ in TIERS}

        # rotation sells (non-core lots only, optional trend filter)
        while lots and sell_ok:
            cand = [l for l in lots if not l.get("core")]
            if not cand:
                break
            lot = max(cand, key=lambda l: l["cost"])
            if open_call and lot is open_call["lot"]:
                break
            if S >= (1 + sell_gain) * lot["cost"]:
                cash += lot["shares"] * S
                lots.remove(lot)
                stats["sells"] += 1
                stats["realized_gain"] += lot["shares"] * (S - lot["cost"])
            else:
                break

        # tier buys
        for t, w in TIERS:
            if dd <= -t and not tier_filled[t]:
                if use_options and open_put and open_put["tier"] == t:
                    continue
                base = total_value() if pct_budgets else CAPITAL
                want = w * base
                avail = ensure_cash(want)
                if avail > 500:
                    sh = avail / S
                    lots.append({"shares": sh, "cost": S, "core": False})
                    cash -= avail
                    tier_filled[t] = True
                    stats["buys"] += 1

        # monthly options
        if use_options and i >= next_opt:
            next_opt = i + bt.OPT_CYCLE
            sig = bt.realized_vol(px, i) * bt.VOL_MULT
            T = bt.OPT_CYCLE / 252
            if open_put is None:
                for t, w in TIERS:
                    if tier_filled[t]:
                        continue
                    K = (1 - t) * hi
                    if K >= S * 0.995:
                        continue
                    base = total_value() if pct_budgets else CAPITAL
                    budget = min(w * base, cash + spy_sh * sp)
                    if budget < 500:
                        continue
                    prem = bt.bs(S, K, T, bt.RF, sig, "put")
                    if prem < bt.MIN_PREM_FRAC * K:
                        break
                    sh = budget / K
                    cash += prem * sh
                    stats["put_premium"] += prem * sh
                    stats["puts_sold"] += 1
                    open_put = {"strike": K, "shares": sh, "expiry_idx": i + bt.OPT_CYCLE, "tier": t}
                    break
            if open_call is None and not no_calls:
                cand = [l for l in lots if not l.get("core")]
                if cand and ((not trend_filter) or (ma is not None and S < ma)):
                    lot = max(cand, key=lambda l: l["cost"])
                    K = (1 + sell_gain) * lot["cost"]
                    if S * 1.005 < K < S * 1.8:
                        prem = bt.bs(S, K, T, bt.RF, sig, "call")
                        if prem >= bt.MIN_PREM_FRAC * S:
                            cash += prem * lot["shares"]
                            stats["call_premium"] += prem * lot["shares"]
                            stats["calls_sold"] += 1
                            open_call = {"strike": K, "lot": lot, "expiry_idx": i + bt.OPT_CYCLE}

        # sweep idle cash into SPY
        if park_spy and cash > 0:
            spy_sh += cash / sp
            cash = 0.0

        held = sum(l["shares"] for l in lots)
        v = cash + spy_sh * sp + held * S
        stats["invested_sum"] += held * S / v if v > 0 else 0
        stats["days"] += 1
        curve.append((d.isoformat(), round(v, 2), round(held * S / v, 4) if v > 0 else 0))

    return bt.finish(curve, stats, [])

VARIANTS = {
    "core50":   dict(core_frac=0.50, core_never_sell=True),
    "trend":    dict(trend_filter=True),
    "spy_park": dict(park_spy=True),
    "gain50":   dict(sell_gain=0.50),
    "trend_park": dict(trend_filter=True, park_spy=True),
    "trend_park_opt": dict(trend_filter=True, park_spy=True, use_options=True),
    "combo_noopt": dict(core_frac=0.30, core_never_sell=True, trend_filter=True,
                        park_spy=True, pct_budgets=True),
    "combo":    dict(core_frac=0.30, core_never_sell=True, trend_filter=True,
                     park_spy=True, use_options=True, pct_budgets=True),
}

if __name__ == "__main__":
    tickers = ["nflx", "msft", "enph", "nvda", "cvx"]
    out = {}
    for name, kw in VARIANTS.items():
        out[name] = {}
        for t in tickers:
            r = run2(t, **kw)
            out[name][t] = r
        avg = sum(out[name][t]["final"] for t in tickers) / 5
        print(f"--- {name}  (basket avg {avg:,.0f})")
        for t in tickers:
            r = out[name][t]
            s = r["stats"]
            print(f"{t.upper():5} final {r['final']:>12,.0f} cagr {r['cagr']:>6.1%} mdd {r['max_drawdown']:>5.0%} "
                  f"stock-exp {r['avg_invested']:>4.0%} buys {s.get('buys',0):>3.0f} sells {s.get('sells',0):>3.0f} "
                  f"prem {s.get('put_premium',0)+s.get('call_premium',0):>8,.0f}")
    json.dump({n: {t: {k: v for k, v in r.items() if k != "trades"} for t, r in byt.items()}
               for n, byt in out.items()}, open("improved.json", "w"))
    print("wrote improved.json")
