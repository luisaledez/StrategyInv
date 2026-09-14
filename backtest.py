"""
Lot-based dip-buying backtest.

Strategy per user's spec:
  - Own quality names; buy on deep corrections, buying MORE shares the lower it goes.
  - Sell the highest-cost lot whenever price exceeds that lot's cost by 20%+.
  - Options variant: sell cash-secured puts at the next lower buy tier; sell
    covered calls at 1.2x the highest-cost lot's basis.

Data: Yahoo chart API JSON (split-adjusted closes, dividend events).
"""

import json, math, datetime as dt
from collections import defaultdict

DATA_DIR = "data"
START = dt.date(2015, 1, 2)
CAPITAL = 100_000.0
INITIAL_FRACTION = 0.20          # starter position on day 1
TIERS = [(0.20, 0.15), (0.30, 0.20), (0.40, 0.25), (0.50, 0.40)]  # (drawdown, weight of capital)
REARM_DD = -0.10                 # tiers re-arm when drawdown recovers above -10%
SELL_GAIN = 0.20                 # sell highest-cost lot when price >= (1+SELL_GAIN)*cost
HIGH_WINDOW = 504                # trailing 2-year high
CASH_RATE = 0.025                # interest on idle cash
RF = 0.03                        # risk-free for BS
VOL_WINDOW = 63
VOL_MULT = 1.10                  # implied-vol premium over realized
OPT_CYCLE = 21                   # trading days per option cycle
MIN_PREM_FRAC = 0.002            # skip options with premium < 0.2% of strike

N = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))

def bs(S, K, T, r, sig, kind):
    if T <= 0 or sig <= 0 or S <= 0 or K <= 0:
        return 0.0
    d1 = (math.log(S / K) + (r + sig * sig / 2) * T) / (sig * math.sqrt(T))
    d2 = d1 - sig * math.sqrt(T)
    if kind == "put":
        return K * math.exp(-r * T) * N(-d2) - S * N(-d1)
    return S * N(d1) - K * math.exp(-r * T) * N(d2)

def load(t):
    d = json.load(open(f"{DATA_DIR}/{t}.json"))["chart"]["result"][0]
    ts = d["timestamp"]
    close = d["indicators"]["quote"][0]["close"]
    divs = {}
    for v in d.get("events", {}).get("dividends", {}).values():
        divs[dt.date.fromtimestamp(v["date"])] = v["amount"]
    dates, px = [], []
    for i, t_ in enumerate(ts):
        if close[i] is None:
            continue
        dates.append(dt.date.fromtimestamp(t_))
        px.append(close[i])
    return dates, px, divs

def realized_vol(px, i, window=VOL_WINDOW):
    lo = max(1, i - window)
    rets = [math.log(px[j] / px[j - 1]) for j in range(lo, i + 1)]
    if len(rets) < 20:
        return 0.40
    m = sum(rets) / len(rets)
    var = sum((r - m) ** 2 for r in rets) / (len(rets) - 1)
    return math.sqrt(var * 252)

def run(ticker, use_options):
    dates, px, divs = load(ticker)
    i0 = next(i for i, d in enumerate(dates) if d >= START)

    cash = CAPITAL
    lots = []                    # list of dicts {shares, cost}
    tier_filled = {t: False for t, _ in TIERS}
    open_put = None              # {strike, shares, expiry_idx, tier}
    open_call = None             # {strike, lot, expiry_idx}
    stats = defaultdict(float)
    trades = []
    curve = []                   # (date, value, invested_frac)

    # day-1 starter position
    if INITIAL_FRACTION > 0:
        sh = CAPITAL * INITIAL_FRACTION / px[i0]
        lots.append({"shares": sh, "cost": px[i0]})
        cash -= CAPITAL * INITIAL_FRACTION
        stats["buys"] += 1
        trades.append((dates[i0], "BUY-init", px[i0], sh))

    next_opt = i0 + OPT_CYCLE

    for i in range(i0, len(px)):
        d, S = dates[i], px[i]
        cash *= 1 + CASH_RATE / 252
        held = sum(l["shares"] for l in lots)
        if d in divs and held > 0:
            cash += divs[d] * held
            stats["dividends"] += divs[d] * held

        hi = max(px[max(0, i - HIGH_WINDOW):i + 1])
        dd = S / hi - 1

        # settle expiring options
        if use_options and open_put and i >= open_put["expiry_idx"]:
            K = open_put["strike"]
            if S < K:
                sh = open_put["shares"]
                cost_ = sh * K
                if cost_ <= cash + 1:
                    cash -= cost_
                    lots.append({"shares": sh, "cost": K})
                    tier_filled[open_put["tier"]] = True
                    stats["put_assignments"] += 1
                    stats["buys"] += 1
                    trades.append((d, "PUT-assigned", K, sh))
            open_put = None
        if use_options and open_call and i >= open_call["expiry_idx"]:
            K = open_call["strike"]
            lot = open_call["lot"]
            if S > K and lot in lots:
                cash += lot["shares"] * K
                lots.remove(lot)
                stats["calls_assigned"] += 1
                stats["sells"] += 1
                stats["call_upside_forgone"] += lot["shares"] * (S - K)
                trades.append((d, "CALL-assigned", K, lot["shares"]))
            open_call = None

        # re-arm tiers on recovery
        if dd > REARM_DD:
            tier_filled = {t: False for t, _ in TIERS}

        # mechanical sells: highest-cost lot up 20%+ (skip lot under an open call)
        while lots:
            lot = max(lots, key=lambda l: l["cost"])
            if open_call and lot is open_call["lot"]:
                break
            if S >= (1 + SELL_GAIN) * lot["cost"]:
                cash += lot["shares"] * S
                lots.remove(lot)
                stats["sells"] += 1
                stats["realized_gain"] += lot["shares"] * (S - lot["cost"])
                trades.append((d, "SELL", S, lot["shares"]))
            else:
                break

        # tier buys (suppressed for the tier reserved by an open put)
        for t, w in TIERS:
            if dd <= -t and not tier_filled[t]:
                if use_options and open_put and open_put["tier"] == t:
                    continue
                budget = min(CAPITAL * w, cash)
                if budget > 500:
                    sh = budget / S
                    lots.append({"shares": sh, "cost": S})
                    cash -= budget
                    tier_filled[t] = True
                    stats["buys"] += 1
                    trades.append((d, f"BUY-{int(t*100)}", S, sh))

        # monthly option writing
        if use_options and i >= next_opt:
            next_opt = i + OPT_CYCLE
            sig = realized_vol(px, i) * VOL_MULT
            T = OPT_CYCLE / 252
            if open_put is None:
                for t, w in TIERS:
                    if tier_filled[t]:
                        continue
                    K = (1 - t) * hi
                    if K >= S * 0.995:
                        continue
                    budget = min(CAPITAL * w, cash)
                    if budget < 500:
                        continue
                    prem = bs(S, K, T, RF, sig, "put")
                    if prem < MIN_PREM_FRAC * K:
                        break  # deeper tiers are even further OTM
                    sh = budget / K
                    cash += prem * sh
                    stats["put_premium"] += prem * sh
                    stats["puts_sold"] += 1
                    open_put = {"strike": K, "shares": sh, "expiry_idx": i + OPT_CYCLE, "tier": t}
                    break
            if open_call is None and lots:
                lot = max(lots, key=lambda l: l["cost"])
                K = (1 + SELL_GAIN) * lot["cost"]
                if K > S * 1.005 and K < S * 1.8:
                    prem = bs(S, K, T, RF, sig, "call")
                    if prem >= MIN_PREM_FRAC * S:
                        cash += prem * lot["shares"]
                        stats["call_premium"] += prem * lot["shares"]
                        stats["calls_sold"] += 1
                        open_call = {"strike": K, "lot": lot, "expiry_idx": i + OPT_CYCLE}

        held = sum(l["shares"] for l in lots)
        value = cash + held * S
        stats["invested_sum"] += (held * S) / value if value > 0 else 0
        stats["days"] += 1
        curve.append((d.isoformat(), round(value, 2), round(held * S / value, 4) if value > 0 else 0))

    return finish(curve, stats, trades)

def buy_hold(ticker):
    dates, px, divs = load(ticker)
    i0 = next(i for i, d in enumerate(dates) if d >= START)
    sh = CAPITAL / px[i0]
    cash = 0.0
    curve = []
    stats = defaultdict(float)
    for i in range(i0, len(px)):
        d, S = dates[i], px[i]
        cash *= 1 + CASH_RATE / 252
        if d in divs:
            cash += divs[d] * sh
        curve.append((d.isoformat(), round(cash + sh * S, 2), 1.0))
    stats["days"] = len(curve)
    stats["invested_sum"] = len(curve)
    return finish(curve, stats, [])

def finish(curve, stats, trades):
    vals = [v for _, v, _ in curve]
    peak, mdd = vals[0], 0.0
    for v in vals:
        peak = max(peak, v)
        mdd = min(mdd, v / peak - 1)
    years = stats["days"] / 252 if stats["days"] else len(vals) / 252
    final = vals[-1]
    cagr = (final / CAPITAL) ** (1 / years) - 1
    return {
        "final": final,
        "total_return": final / CAPITAL - 1,
        "cagr": cagr,
        "max_drawdown": mdd,
        "avg_invested": stats["invested_sum"] / max(stats["days"], 1),
        "stats": {k: round(v, 2) for k, v in stats.items() if k not in ("invested_sum", "days")},
        "curve": curve,
        "trades": [(d.isoformat(), a, round(p, 2), round(s, 2)) for d, a, p, s in trades],
    }

if __name__ == "__main__":
    tickers = ["nflx", "msft", "enph", "nvda", "cvx"]
    out = {}
    for t in tickers:
        out[t] = {
            "dip": run(t, use_options=False),
            "dip_opt": run(t, use_options=True),
            "bh": buy_hold(t),
        }
    out["spy"] = {"bh": buy_hold("spy")}

    hdr = f"{'ticker':6} {'variant':8} {'final $':>12} {'totret':>8} {'CAGR':>7} {'maxDD':>7} {'inv%':>6} {'buys':>5} {'sells':>5} {'putPrem':>9} {'callPrem':>9}"
    print(hdr)
    for t in tickers:
        for v in ("bh", "dip", "dip_opt"):
            r = out[t][v]
            s = r["stats"]
            print(f"{t.upper():6} {v:8} {r['final']:>12,.0f} {r['total_return']:>7.0%} {r['cagr']:>7.1%} {r['max_drawdown']:>7.0%} {r['avg_invested']:>6.0%} "
                  f"{s.get('buys',0):>5.0f} {s.get('sells',0):>5.0f} {s.get('put_premium',0):>9,.0f} {s.get('call_premium',0):>9,.0f}")
    r = out["spy"]["bh"]
    print(f"{'SPY':6} {'bh':8} {r['final']:>12,.0f} {r['total_return']:>7.0%} {r['cagr']:>7.1%} {r['max_drawdown']:>7.0%}")

    json.dump(out, open("results.json", "w"))
    print("\nwrote results.json")
