# Turnaround candidates, top 20 as of September 27, 2026

*Research tooling output, not investment advice. Screen run on 2026-09-28 with the rules of the second backtest's "re-screen + guide-cut proxy" scenario (`turnaround_backtest/backtest_v2.py`, scenario `rescreen_only`, snapshots from `screen.py --organic`). Prices: Yahoo cache through the Friday, September 25 close. Fundamentals: SEC EDGAR point-in-time tables, latest quarter June 30, 2026 (July quarter for VEEV, ADSK, DKS, GEN). The row-level data is in `turnaround_backtest/output_v2/current_top20_2026-09-27.csv`.*

## Rules applied

The screen is the quarterly snapshot of the backtest, evaluated today instead of on October 1:

1. **Price screen** (scanner defaults): monthly Wilder RSI(14) below 42 in any of the last 6 monthly candles, at least 5 years of history, 3-month average dollar volume of $5M or more, market cap of $1B or more. Universe: today's S&P 500 + S&P 400 (898 tickers with filings).
2. **Profitable now and in the past**: trailing-twelve-month (TTM) EPS and net income above zero, and at most one losing year among the TTM readings one, two and three years back.
3. **Organic growth only**: TTM revenue growth positive and under 100%, no quarter-to-quarter jump of the TTM figure above 60% in the last eight quarters, latest quarter not below its year-ago quarter.
4. **Top 20 by TTM revenue growth**, then **top 10 by valuation versus the company's own history**: mean percentile of today's trailing P/E, P/S and EV/EBITDA within the monthly series rebuilt from filings (0 = cheapest ever, 1 = most expensive ever).

Portfolio rules of the scenario, for reference: at most 10% of the portfolio per stock, bought on the first trading day after the snapshot; names that drop off the list are kept; trim half at +50%; sell all at a month-end with monthly RSI at or above 90; a winner above +100% is sold to fund a new top-10 name when cash is short; a holding whose filings re-base by 30% or more is sold unless it is still on the list; **guidance-cut proxy: sold at the month-end when TTM EPS is 15% or more below its level at entry within the first 12 months**; yearly withdrawals of 5 to 10%. No position cap, no S&P correction parking.

## Funnel today

| Step | Names |
|---|---|
| RSI(14, monthly) < 42 within the last 6 months | 239 |
| ... liquid and with 5 years of history | 233 |
| ... market cap ≥ $1B | 230 |
| ... profitable now and in the past | 193 |
| ... organic growth (positive, < 100%, no jumps, latest quarter not fading) | 139 |
| Top 20 by revenue growth → top 10 by valuation percentile | 20 → 10 |

The monthly candle for September is two trading days from complete. The official October 1 snapshot will use the September 30 close. Run on the completed August candle instead, the top 10 has three different names (CPT, DKS and DT in place of VEEV, PINS and GEN), so the boundary is live; see the last section.

## The top 20

Growth = TTM revenue growth year over year. Val = valuation percentile versus own history (lower is cheaper). RSI = monthly RSI(14) on the current candle; min = lowest monthly RSI in the 6-month window. From 5y high = distance of the month-end close from the 5-year high. EPS Δ = TTM EPS versus 12 months earlier. ND/EBITDA = net debt over TTM EBITDA.

| # | Ticker | Company | Sector | Growth | Val pct | P/E | P/S | EV/EBITDA | RSI (min) | From 5y high | Mkt cap $B | EPS Δ 1y | ND/EBITDA | Top 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CELH | Celsius Holdings | Cons. Staples | +83% | 0.34 | 117 | 4.9 | 87 | 42 (42) | -71% | 15.1 | -37% | 0.3 | |
| 2 | AMCR | Amcor | Materials | +57% | 0.20 | 17.9 | 0.8 | 9.6 | 46 (39) | -37% | 19.8 | +49% | 3.8 | **7** |
| 3 | DKS | Dick's Sporting Goods | Cons. Disc. | +54% | 0.32 | 15.1 | 0.6 | 6.6 | 35 (35) | -45% | 12.6 | -35% | net cash | |
| 4 | BRO | Brown & Brown | Financials | +34% | 0.33 | 19.4 | 3.4 | 15.0 | 38 (31) | -51% | 23.4 | -10% | 3.4 | |
| 5 | ELF | e.l.f. Beauty | Cons. Staples | +31% | 0.57 | 102 | 3.4 | 30 | 51 (40) | -54% | 6.1 | -42% | 2.2 | |
| 6 | PODD | Insulet | Health Care | +29% | **0.00** | 25.5 | 3.1 | 16.3 | 35 (34) | -61% | 9.6 | +62% | 0.7 | **1** |
| 7 | DUOL | Duolingo | Cons. Disc. | +29% | 0.17 | 17.0 | 6.1 | 36 | 43 (38) | -73% | 7.0 | +247% | net cash | **6** |
| 8 | AJG | Arthur J. Gallagher | Financials | +26% | 0.74 | 38 | 3.8 | 25 | 45 (37) | -34% | 60.1 | -9% | 4.2 | |
| 9 | FICO | Fair Isaac | Info. Tech. | +24% | 0.44 | 25.0 | 8.5 | 21 | 37 (37) | -64% | 20.4 | +35% | 4.3 | |
| 10 | NOW | ServiceNow | Info. Tech. | +22% | 0.16 | 85 | 9.6 | 64 | 48 (30) | -42% | 141.6 | +1% | 1.3 | **3** |
| 11 | CSGP | CoStar Group | Real Estate | +22% | 0.25 | 156 | 3.2 | 28 | 28 (26) | -72% | 11.5 | -31% | net cash | **9** |
| 12 | ISRG | Intuitive Surgical | Health Care | +21% | 0.48 | 46 | 13.2 | n/a | 45 (37) | -34% | 145.8 | +22% | n/a | |
| 13 | APPF | AppFolio | Info. Tech. | +21% | 0.17 | 47 | 7.0 | 35 | 50 (39) | -36% | 7.3 | -21% | net cash | **5** |
| 14 | GEN | Gen Digital | Info. Tech. | +20% | 0.26 | 12.6 | 2.6 | 8.0 | 44 (36) | -33% | 13.3 | +78% | 2.9 | **10** |
| 15 | FIS | Fidelity National Info. | Financials | +18% | 0.03 | 5.4 | 1.5 | 8.3 | 29 (27) | -72% | 18.3 | +33x | 3.9 | **2** |
| 16 | ADSK | Autodesk | Info. Tech. | +18% | 0.27 | 27 | 5.7 | 19.6 | 41 (33) | -37% | 44.5 | +61% | net cash | |
| 17 | DT | Dynatrace | Info. Tech. | +18% | 0.27 | 116 | 8.4 | 60 | 63 (36) | -26% | 17.6 | -69% | net cash | |
| 18 | CXT | Crane NXT | Info. Tech. | +17% | 0.57 | 19.7 | 1.5 | 10.5 | 47 (39) | -31% | 2.8 | -7% | 3.2 | |
| 19 | PINS | Pinterest | Comm. Services | +17% | 0.24 | 56 | 3.0 | 49 | 40 (39) | -70% | 13.8 | -88% | net cash | **8** |
| 20 | VEEV | Veeva Systems | Health Care | +17% | 0.16 | 46 | 13.5 | n/a | 61 (35) | -14% | 46.7 | +25% | net cash | **4** |

The top 10 in the scenario's buy order (valuation rank): PODD, FIS, NOW, VEEV, APPF, DUOL, AMCR, PINS, CSGP, GEN.

## What the backtest says about a basket like this

Scenario `rescreen_only`, 2004 to August 2026 (first buy April 2008), $100,000 start, withdrawals included:

| Measure | Strategy | SPY, same withdrawals |
|---|---|---|
| IRR | 14.0% | 9.1% |
| Max drawdown (no-withdrawal index) | -38% | -55% |
| Closed positions | 118 | |
| Win rate | 71% | |
| Average / median closed return | +39% / +40% | |
| Average winner / average loser | +61% / -13% | |
| 10th percentile closed return | -12% | |
| Worst closed | FANG -69% (Oct 2019 to Mar 2020), META -59% (2022) | |
| Median hold | 8.9 months | |

Half of all entries (70 of 141) were sold by the guidance-cut proxy inside year one. Those exits averaged +10% (median +3%), so the rule mostly cuts flat positions early rather than catching disasters; the two worst losses above were both guide-cut exits that came too late. The other exits: 39 positions sold as >100% winners to fund new names, 9 re-screen sales averaging +47%, 71 trims at +50%.

**Forward returns of the picks themselves**, every organic snapshot from 2009 to September 2025, buy-and-hold from the snapshot date, no portfolio rules (634 top-10 picks, 491 bench picks):

| Group | 12-month mean | Median | Win rate | Beat SPY | 10th pct | 90th pct | Median worst drawdown in year 1 |
|---|---|---|---|---|---|---|---|
| Top 10 (bought) | +24% | +19% | 72% | 54% | -20% | +64% | -12% |
| Ranks 11-20 (bench) | +20% | +16% | 69% | 48% | -22% | +63% | -12% |
| Top 10 with val pct ≤ 0.10 | +36% | +25% | 81% | 58% | -15% | +89% | -10% |
| Top 10 with val pct 0.10 to 0.25 | +23% | +17% | 70% | 52% | -28% | +65% | -13% |
| Top 10 more than 60% below 5y high | +50% | +25% | 76% | 50% | -26% | +163% | -13% |
| Top 10, 24 months | +46% | +34% | 79% | 53% | -19% | +113% | |

The valuation ranking is what carries the edge: names bought in the cheapest tenth of their own history returned about twice the bench, and the bench's excess return over SPY is close to zero. Every name in today's top 10 sits at or below the 26th percentile, and five (PODD, FIS, DUOL, CSGP, PINS) are 60% or more below their 5-year high, the bucket with the best average and the widest spread. Small-sample warning: the "cheapest and deepest" cell has 28 observations and most come from 2009 and 2020, so its +95% mean is a regime statement, not a forecast.

## Name by name: risk and reward

Reward figures are the 12-month base rates from the buckets above, applied by valuation percentile and drawdown; the risk column is what the rule set would actually do to the position and what is specific to the company.

| Rank | Ticker | Base-rate 12m (median / 10th pct) | Reward case | Main risks under these rules | Verdict |
|---|---|---|---|---|---|
| 1 | PODD | +25% / -15% | Cheapest ever on all three multiples after a 61% fall; TTM EPS +62% and rising every quarter; the repository's Sept 27 comparison put a probability-weighted 12 to 24-month value near $164 (+20%) with a $90-120 bear case. | The Aug 5 guidance cut is already in the price; the late-October print either confirms the mid-teens exit rate or cuts again. Three tubeless competitors launch into its pharmacy channel over the next nine months; two Class I pod corrections in 2026; net debt 0.7x EBITDA. Guide-cut proxy risk is low because TTM EPS is still climbing. | Cleanest fit of the ten. |
| 2 | FIS | +25% / -15% | P/S 1.5 (cheapest 1% of its history) and EV/EBITDA 8.3 (9th pct) are genuine; -72% from the 5-year high. | **The 5.4 P/E is an artefact.** TTM EPS went from $0.19 to $6.51 in two quarters because of a one-off gain (the Worldpay stake disposal in the Issuer Solutions swap), and the +18% revenue growth includes the acquired business. When the gain leaves the trailing four quarters, around the Q1 2027 filing, TTM EPS falls far more than 15% and the guide-cut proxy sells the position mechanically inside year one. Net debt 3.9x EBITDA. | Bought by the rule, but expect a forced exit within about 6 to 9 months. |
| 3 | NOW | +17% / -28% | 22% growth at the 16th percentile of its own valuation; -42% from the high in the software de-rating. The backtest already holds NOW from the April 2026 snapshot at +42%. | P/E 85 and P/S 9.6 are only cheap relative to its own past; TTM EPS dipped 1.68 to 1.60 in the last quarter, so one more soft quarter puts the proxy within reach (-15% from $1.60 = $1.36). AI-disruption narrative on seat-based software. | Fair; already owned in the running portfolio, so only a new account buys it. |
| 4 | VEEV | +17% / -28% | The steadiest earner on the list: TTM EPS up every quarter for six quarters (+25%), net cash, growth 17%, 16th percentile valuation. | Least distressed name: only 14% below its 5-year high, and the monthly RSI has already rebounded to 61 (it qualified on the March-April dip). Valuation edge is smaller than the percentile suggests; P/E 46. Two more September trading days could lift it off the list, or keep it. | Low risk, modest upside. |
| 5 | APPF | +17% / -28% | Growth 21%, net cash, 17th percentile; TTM EPS has been rising again for two quarters. | TTM EPS is 21% below a year ago because a tax item fell out of the trailing figure in Q4 2025; the entry base ($4.39) is now clean, so the proxy needs an operating miss to fire. P/E 47, P/S 7 in a sector being re-rated. | Fair. |
| 6 | DUOL | +25% / -26% | Fastest organic grower left in the top 10 (29%), net cash, -73% from the high, 17th percentile valuation. | **The 17x P/E is an artefact**: TTM EPS jumped from $2.44 to $7.94 in Q3 2025 on a deferred-tax-asset release. The Q3 2026 filing (early November) laps it and TTM EPS should drop well past -15%, so the proxy would sell within two months of buying. On operating multiples (P/S 6, EV/EBITDA 36) it is cheap only versus its own history. | Bought by the rule; a near-certain mechanical exit in November unless the tax item is smaller than it looks. |
| 7 | AMCR | +17% / -28% | 18x earnings, 9.6x EBITDA, 20th percentile, TTM EPS +49%. | **Growth is the Berry Global merger (April 2025), not organic**: revenue went from $10B to $23.5B TTM. It passed the organic filter only because the step-up was spread over four quarters (largest single jump 16%). Net debt 3.8x EBITDA is the highest on the list. The worst-open study found acquisition-driven entries were the loser pattern. | Weakest thesis of the ten. |
| 8 | PINS | +25% / -26% | P/S 3.0 is the cheapest 2% of its history, net cash of about five times EBITDA, -70% from the high, growth 17%. | TTM EPS -88% is the 2024 tax-asset release rolling out, so the $0.34 entry base is washed out and P/E 56 overstates the price; a further -15% would be a real operating decline, which is possible in an ad-spend slowdown. Highest-variance bucket (10th pct -54%, 90th pct +163% for names this far below their high). | Asymmetric; size for the variance. |
| 9 | CSGP | +25% / -26% | Most oversold name (monthly RSI 28), P/S at the cheapest 0.5% and EV/EBITDA at the 3rd percentile of its history, net cash, 22% growth, activists involved. | GAAP EPS is near zero (Homes.com spend) and swung from $0.02 to $0.18 over three quarters, so a 15% TTM move is noise; the proxy is likely to fire on noise either way. P/E 156 keeps the mean percentile at 0.25 despite the two cheap multiples. | High-noise position; the exit rule, not the thesis, will decide it. |
| 10 | GEN | +17% / -13% | 12.6x earnings, 8x EBITDA, TTM EPS +78%; the backtest owned it once before (July 2012, sold +53% via the proxy). | Part of the 20% growth is the MoneyLion acquisition (April 2025); net debt 2.9x EBITDA. Last name in, 0.256 versus CSGP 0.252 and ADSK 0.271, so two trading days can swap it for ADSK or DT. | Solid value, boundary case. |

Bench notes (ranks 11 to 20, not bought): CELH (+83%) and DKS (+54%) owe their growth to the Alani Nu and Foot Locker acquisitions and both have falling EPS; DKS was in the August-close top 10 at rank 9. BRO, AJG, ISRG, FICO and ELF are quality names whose valuation percentiles (0.33 to 0.74) keep them off the buy list. ADSK and DT sit just outside on valuation (0.27).

## Allocation

**By the rule** ($100,000 fresh account, first trading day after the snapshot, 10% each, fully invested):

| Ticker | Weight | Dollars | Expected path under the rules |
|---|---|---|---|
| PODD | 10% | $10,000 | Hold; trim half at +50% (about $204) |
| FIS | 10% | $10,000 | Likely proxy exit around the Q1 2027 filing |
| NOW | 10% | $10,000 | Hold (already held in the running backtest portfolio, so 9 buys there) |
| VEEV | 10% | $10,000 | Hold |
| APPF | 10% | $10,000 | Hold |
| DUOL | 10% | $10,000 | Likely proxy exit at the November filing |
| AMCR | 10% | $10,000 | Hold unless EPS falls 15% |
| PINS | 10% | $10,000 | Hold; high variance |
| CSGP | 10% | $10,000 | Coin-flip proxy exit on EPS noise |
| GEN | 10% | $10,000 | Hold; trim at about $32 |

Basket expectation, taking the 12-month base rates of the buckets each name sits in: median return in the high teens to low twenties, roughly 7 of 10 positive, 1 or 2 names down 25% or more at some point in the year, and by the backtest's own history about half the names sold by the proxy before their first anniversary at a small gain. Portfolio drawdowns of 30 to 40% happened twice in 18 years of this rule set (2008 to 2009 and 2020) and the current basket is more concentrated in de-rated software (NOW, VEEV, APPF, DUOL, CSGP, half the book) than any past snapshot, so correlation is higher than the base rates assume.

**Risk-tiered variant** (departs from the backtest; not what the scenario did): keep 10% in the six names whose numbers are what they appear to be (PODD, VEEV, NOW, APPF, PINS, GEN), 5% in the four whose entry data has a known flaw (FIS and DUOL one-off EPS, AMCR acquisition growth, CSGP noise-level EPS), and hold the remaining 20% as cash for the January snapshot. The backtest had idle cash earn nothing and full investment was part of its return, so this trades expected return for less mechanical churn.

## Sensitivity to the October 1 snapshot

The official snapshot uses the September 30 close. On the completed August candle the top 10 was PODD, FIS, DUOL, APPF, NOW, AMCR, DT, CSGP, DKS, CPT. Since then, DKS fell to valuation 0.32 as its P/E percentile rose, CPT dropped out of the top 20 altogether, and DT's valuation percentile rose above GEN's; VEEV, PINS and GEN entered. Seven names (PODD, FIS, NOW, APPF, DUOL, AMCR, CSGP) are stable across both views; the three seats now held by VEEV, PINS and GEN are the ones two more trading days can change. Re-run on October 1:

```bash
cd turnaround_backtest && python screen.py --organic --out output_v2
```
