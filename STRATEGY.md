# The Dip Ladder — strategy playbook

A lot-based strategy for owning quality companies: buy deep corrections in size
(more shares the lower it goes), recycle expensive lots on bounces, get paid to
wait with cash-secured puts. Two configurations of the same rules — pick by the
drawdown you can live with.

Everything here was backtested on real daily data, Jan 2015 – Aug 2026, on 12
stocks including deliberate losers. Full results with charts:
https://claude.ai/code/artifact/152b871b-c680-4fc4-8167-bec9b5bd475b

> **This is a backtested rule set, not investment advice.** Option premiums are
> modeled (Black–Scholes), taxes and commissions are excluded, and the past does
> not predict the future.

---

## 0 · Before any rule fires: the fundamentals gate

The backtest's clearest lesson: **no price rule can tell a dip from a dying
business.** ENPH (−95%) and NVO (−70%) lost money under every variant tested,
because averaging down into a structural decline compounds the damage. The
price rules below assume the gate has been passed, and it is re-checked on
every buy:

- Durable business with a reason to exist in 10 years; revenue and margins that
  recover after downturns (cyclical is fine, broken is not).
- Valuation sane vs its own history and peers (P/E, EV/EBITDA vs 10-yr range) —
  a −40% price does not make an overvalued stock cheap.
- **Stop the ladder** (no new tier buys, no new puts) whenever the *reason* the
  stock is falling is a deterioration of the thesis — collapsing earnings power,
  losing its market, balance-sheet stress — and not general market fear.

## 1 · Capital allocation (per stock "sleeve")

Give each stock its own sleeve of capital (the backtests used $100k each; any
size works — the rules are all percentages).

| Bucket | Growth Combo (tested best) | Defensive version |
|---|---|---|
| **Core position**, bought day 1, **never sold** | 30% | 20% (sellable) |
| **Reserve**, waiting for corrections | 70% — held in **SPY** (or a broad index fund), sold down to fund buys | 80% — held in T-bills / money market |
| Idle cash | ~0% — everything is invested | ~80% earns the cash rate |

- The Growth Combo compounded at **38–40% CAGR** on the round-1 basket and beat
  buy-and-hold on **6 of 7** out-of-sample stocks — but its drawdowns are
  buy-and-hold-sized (−60%). The Defensive version made 9.6–10.7% with only a
  **−19%** max drawdown. That is the trade; there is no configuration that got
  both.
- Diversify sleeves: 8–12 names across sectors. Cyclicals and boom-bust names
  (energy, semis) suit these rules far better than steady compounders — on
  MSFT-like stocks the rules mostly lag buy-and-hold.

## 2 · When to BUY

Track the **trailing 2-year high** of the closing price. Buy when the close
falls to a tier below it — deeper tiers commit more capital at cheaper prices,
which is what makes the average-down work:

| Drawdown from 2-yr high | Buy this % of current sleeve value |
|---|---|
| −20% | 15% |
| −30% | 20% |
| −40% | 25% |
| −50% | 40% |

- **"Current sleeve value"** = stock + reserve + cash today (not the original
  amount) — so buys stay meaningful as the sleeve compounds. (The defensive
  version sizes off original capital instead.)
- One buy per tier per correction. Tiers **re-arm** once price recovers to
  within 10% of its high — a new correction starts a new ladder.
- Each buy is funded by selling reserve (SPY). If the reserve is exhausted
  (below the −50% tier), you simply hold — the ladder is out of ammunition by
  design. Do not raid other sleeves.
- Every tier buy re-checks the fundamentals gate (§0) first.

## 3 · When to HOLD vs SELL

- **The core is never sold.** That 30% is the "own solid companies" anchor and
  is exempt from every rule below.
- **Tier lots** (everything bought on the ladder) are sold one lot at a time,
  highest cost first, when **both** conditions hold:
  1. Price ≥ **1.20 ×** that lot's cost (the +20% rule), **and**
  2. Price is **below its 200-day moving average** (the trend filter).
- If price is above the 200-day average: **hold everything and do nothing.**
  This single filter was the most valuable rule in the whole study — it means
  you harvest 20% bounces inside downtrends (dead-cat bounces, bear rallies)
  but never sell into a confirmed recovery. Without it, the +20% rule sold
  NVDA's 2022 bottom lots into the 2023 run and forfeited a 10× continuation.
- Sells cascade: after selling the highest-cost lot, check the next one the
  same day. Proceeds go back into the reserve (SPY), rebuilding ammunition.

## 4 · Selling puts — how much and when

Cash-secured puts replace limit orders at the tiers: you are paid to promise a
buy you already wanted to make.

- **When:** once a month, on one name at a time per sleeve, only while at least
  one tier is un-triggered and funded.
- **Strike:** the next unfilled tier's price = (1 − tier%) × trailing 2-yr high,
  and it must be below the current price. ~1 month to expiry.
- **How much:** size the contracts so assignment equals that tier's budget —
  `contracts = tier budget ÷ (strike × 100)`.
  Example: $150k sleeve, −30% tier next → budget 20% = $30k; 2-yr high $200 →
  strike $140; sell **2 contracts** ($28k collateral). The collateral stays in
  the reserve (SPY/T-bills) until assignment.
  At most **one put series open per sleeve** at a time, so put collateral at
  risk is at most the next tier's budget (15–40% of the sleeve, typically ~20%).
- **Skip the trade** if the premium is under ~0.2% of the strike for the month
  (deep-OTM strikes on calm stocks aren't worth the pin risk).
- **Outcomes:** assigned → that *is* your tier buy, at a better effective price
  (strike minus premium); expires worthless → keep the premium, the tier stays
  armed for a direct buy.
- **Where puts pay:** volatile cyclicals (AMKR +$430k, INTC +$160k in the
  backtest). Where they don't: relentless compounders (waiting a month for
  assignment costs more than premium earns) and structural decliners (NVO —
  paid pennies to catch a falling business). The fundamentals gate applies to
  every put sold: never write a put you wouldn't buy the shares at.
- **Covered calls: not part of the Growth Combo.** They cap exactly the
  recoveries the trend filter is built to ride (tested worse with them).
  Optional exception: write a call at 1.2× cost on a tier lot only when price
  is below the 200-day MA and you'd be content to lose the lot at that strike.

## 5 · Known failure modes (from the backtest, not theory)

1. **Structural decline** — the strategy's only real enemy. ENPH −95% and NVO
   −70% hurt every variant. The only defense is §0. A mechanical tripwire worth
   considering: if price sits below the −50% tier for 6+ months, stop all
   averaging and re-underwrite the thesis from scratch.
2. **Relentless compounders** — the rules lag buy-and-hold badly on stocks that
   never correct 20% (MSFT sleeve was 5% invested in the defensive version).
   The 30% core is the mitigation; accept that these names are core-only.
3. **Correlated crashes** — the SPY reserve falls with your buy opportunities
   (2020, 2022). The Growth Combo's basket drawdown equaled buy-and-hold's.
   If that is unacceptable, hold the reserve in T-bills and accept lower returns
   (the round-2 ladder in the report prices each step).
4. **Taxes** — constant short-term gains from rotation and premiums. This
   strategy strongly prefers a tax-advantaged account.

## 6 · Backtested reference numbers (equal-weight baskets, per $100k)

| Rule set | Final | CAGR | Max DD |
|---|---|---|---|
| Defensive ladder (fixed tiers, +20% sell, options) | $327k | 10.7% | −19% |
| Trend + SPY-parked + puts ("2.0") | $1.75M | 27.9% | −42% |
| **Growth Combo + puts** (round-1 five) | $4.35M | 38.3% | −65% worst name |
| Growth Combo + puts (out-of-sample seven) | $1.70M | 27.6% | −60% |
| Buy & hold (round-1 five / out-of-sample seven) | $9.61M / $991k | 48.1% / 21.8% | −53% / −60% |
| SPY | $415k | 13.1% | −31% |

The round-1 buy-and-hold column is inflated by hindsight (NVDA 448×); the
out-of-sample row is the fairer picture: **+71% over buy-and-hold at the basket
level, median stock +75%, winning on 6 of 7 names.**
