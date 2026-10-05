# OpportunityScanner2 tier A: weekly RSI < 25 vs monthly RSI < 35

Generated 2026-09-29 from `OpportunityScanner2/output/yearly_backtest_weekly_rsi25_t20.*` and `output/yearly_backtest_t20_sector30.*`. Both runs: today's S&P 500 + 400 (899 tickers, survivorship bias), signals 2010 onwards, quality + cheap filters point in time from SEC filings, liquid names (average dollar volume ≥ $5M), top 20 buys per calendar year ranked by signal RSI, +20% target within 12 months on daily adjusted closes. Research tooling, not investment advice.

## Verdict

* **The monthly candle is the better signal on every measure.** Over complete 12-month windows the monthly list hit +20% 93% of the time with a +54% median return and 7% misses; the weekly list 83%, +40% and 17%. The weekly list beat SPY 60% of the time, the monthly 73%.
* **Weekly RSI < 25 is a shallower washout.** Its buys sit a median -44% below the all-time high, 10.0 months after the last overbought high; the monthly buys sit -50% below, 16.0 months after. A weekly RSI collapses in a few bad weeks; a monthly RSI under 35 needs a year or more of falling closes.
* **The lists overlap by about half.** 28 of the 57 monthly buys also appear on the weekly list, usually a median 2.9 weeks earlier at a median +6% vs the monthly entry price. On those shared names the weekly entry did better in 3 of 21 completed pairs; where the weekly fired months early in a sharp decline (META, CHTR, STT) it lost while the later monthly entry won.
* **Where both fire, the weekly entry is the weak one.** On the 21 shared names with complete windows the weekly entry hit 76% of the time with a +33% median and a -24% median drawdown; the same stocks bought at the monthly close hit 90% with +49% and -14%. Those are the long, deep declines, and the weekly print catches them on the way down. The 57 weekly-only buys did well on their own (86% hit, +48% median, -7% median drawdown): shorter, sharper sell-offs that never pushed the monthly RSI under 35. The 23 monthly-only buys hit 96% with a +55% median.
* **Practical reading.** Treat the weekly RSI < 25 print as a watchlist alert on a former leader, not as the buy. If the stock keeps falling until the monthly RSI closes under 35, that later entry was better in nearly every pair. A weekly-only list is a reasonable second scan for names the monthly rule never reaches, but on its own it carries about twice the monthly miss rate and a lower median.

## The two rules

| | Monthly | Weekly |
|---|---|---|
| Candle | calendar month | week ending Friday |
| Arming | new all-time high with monthly RSI(14) ≥ 70, ≥ 5 years of history | new all-time high with weekly RSI(14) ≥ 70, ≥ 5 years of history |
| Arming window | 36 months | 156 weeks (36 months) |
| Buy | first month closing with RSI < 35; Consumer Staples / Utilities / Materials only below 30 | first week closing with RSI < 25 (no sector rule needed at that level) |
| Entry price | the signal month's last close | the signal week's Friday close |
| Fundamentals | the signal month-end's point-in-time row | the last month-end on or before the signal week |
| Raw signals since 2010 (no fundamentals) | 259 | 494 |
| After quality + cheap | 58 | 94 |
| Buys after the top-20 cut | 57 (44 complete windows) | 88 (78 complete windows) |

## Results over complete 12-month windows (signals 2010 to Sep 2025)

| Metric | Monthly RSI < 35 | Weekly RSI < 25 |
|---|---|---|
| Buys (complete 12m windows) | 44 | 78 |
| Hit +20% within 12 months | 41/44 = 93% | 65/78 = 83% |
| Months to hit: median / mean / max | 1.9 / 2.5 / 10.7 | 1.8 / 2.8 / 9.6 |
| Hit within 3 / 6 months (share of buys) | 70% / 86% | 56% / 74% |
| 12-month return: median / mean | +54% / +54% | +40% / +53% |
| 12-month return positive | 95% | 81% |
| Best / worst 12-month return | +166% RCL / -8% FIS | +378% SGI / -55% TTD |
| Beat SPY over the same 12 months | 73% | 60% |
| SPY over the same 12 months (median) | +24% | +22% |
| Excess over SPY (median) | +21% | +13% |
| Max gain in the window (median / best) | +62% / +200% RCL | +51% / +378% SGI |
| Max drawdown from entry (median / worst) | -9% / -49% WAL | -10% / -63% TTD |
| Drawdown before the hit (median, hits only) | -6% | -5% |
| Buys that fell more than 10% / 20% below entry | 48% / 25% | 53% / 33% |
| RSI printed lower after the buy | 36% | 38% |
| Misses (no +20% close in 12 months) | 3/44 = 7% | 13/78 = 17% |
| Misses: 12m return median / max DD median | -2% / -19% | -6% / -25% |


## Year by year

Per list: buys, hit rate, 12-month return median, max drawdown median, misses over complete windows.

| Year | SPY cal. year | Monthly: buys | hit | 12m median | max DD median | misses | Weekly: buys | hit | 12m median | max DD median | misses |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | +15% | 1 | 1/1 = 100% | +25% | +4% | 0/1 | 1 | 1/1 = 100% | +18% | -8% | 0/1 |
| 2011 | +2% | 2 | 2/2 = 100% | +37% | -10% | 0/2 | 6 | 6/6 = 100% | +27% | -20% | 0/6 |
| 2012 | +16% | 1 | 1/1 = 100% | +16% | +0% | 0/1 | 1 | 1/1 = 100% | +73% | -18% | 0/1 |
| 2013 | +32% | 0 | | | | | 0 | | | | |
| 2014 | +13% | 0 | | | | | 1 | 0/1 = 0% | -6% | -20% | 1/1 |
| 2015 | +1% | 1 | 0/1 = 0% | -2% | -19% | 1/1 | 2 | 1/2 = 50% | +26% | -17% | 1/2 |
| 2016 | +12% | 2 | 2/2 = 100% | +86% | -5% | 0/2 | 8 | 6/8 = 75% | +29% | -7% | 2/8 |
| 2017 | +22% | 2 | 2/2 = 100% | +54% | -5% | 0/2 | 2 | 2/2 = 100% | +39% | -5% | 0/2 |
| 2018 | -5% | 4 | 4/4 = 100% | +39% | -13% | 0/4 | 14 | 10/14 = 71% | +26% | -12% | 4/14 |
| 2019 | +31% | 0 | | | | | 1 | 1/1 = 100% | +1% | -43% | 0/1 |
| 2020 | +18% | 12 | 12/12 = 100% | +69% | -11% | 0/12 | 20 | 20/20 = 100% | +100% | -6% | 0/20 |
| 2021 | +29% | 0 | | | | | 0 | | | | |
| 2022 | -18% | 11 | 10/11 = 91% | +55% | -4% | 1/11 | 13 | 8/13 = 62% | +30% | -23% | 5/13 |
| 2023 | +26% | 5 | 4/5 = 80% | +38% | -19% | 1/5 | 3 | 3/3 = 100% | +36% | -0% | 0/3 |
| 2024 | +25% | 1 | 1/1 = 100% | +88% | -23% | 0/1 | 2 | 2/2 = 100% | +13% | -10% | 0/2 |
| 2025 | +18% | 5 (3 open) | 3/5 = 60% | +19% | -22% | 0/2 | 6 (2 open) | 4/6 = 67% | -2% | -25% | 0/4 |
| 2026 | +13% | 10 (10 open) | 5/10 = 50% | – | -22% | 0/0 | 8 (8 open) | 5/8 = 62% | – | -22% | 0/0 |

In the 12 years where both lists have complete windows, the weekly median was lower in 9 (2010, 2011, 2016, 2017, 2018, 2022, 2023, 2024, 2025). The weekly list fills the years the monthly list skips (2013, 2014, 2019) with small, mixed batches, and it is much bigger in 2018 and 2022, the two years where it also misses most.

## How deep into the decline each list buys

| | Monthly | Weekly |
|---|---|---|
| Signal RSI: median (quartiles) | 33 (32 to 34) | 23 (21 to 25) |
| Price vs all-time high: median (quartiles) | -50% (-58% to -43%) | -44% (-53% to -38%) |
| Months since the last overbought high: median (quartiles) | 16 (10 to 22) | 10 (6 to 16) |
| Buys less than 30% below the ATH | 0% | 1% |
| Buys more than 50% below the ATH | 49% | 30% |

Weekly buys by distance below the all-time high (complete windows):

| Distance | Buys | Hit +20% | 12m median | Max DD median | Misses |
|---|---|---|---|---|---|
| more than 50% below ATH | 22 | 91% | +41% | -9% | 2 |
| 40 to 50% | 32 | 88% | +44% | -9% | 4 |
| 30 to 40% | 23 | 70% | +34% | -13% | 7 |
| less than 30% | 1 | 100% | +83% | -12% | 0 |

## Overlap: the same stocks on both lists

A weekly buy is paired with a monthly buy of the same stock dated from 3 months before to 6 months after it. 28 pairs (28 of 88 weekly buys, 28 of 57 monthly buys).

| Metric | Weekly buys also on the monthly list (weekly entry) | Weekly-only buys | Monthly buys also on the weekly list (monthly entry) | Monthly-only buys |
|---|---|---|---|---|
| Buys (complete 12m windows) | 21 | 57 | 21 | 23 |
| Hit +20% within 12 months | 16/21 = 76% | 49/57 = 86% | 19/21 = 90% | 22/23 = 96% |
| Months to hit: median / mean / max | 4.1 / 4.4 / 9.6 | 1.5 / 2.3 / 9.4 | 2.1 / 3.0 / 10.7 | 1.8 / 2.0 / 5.7 |
| Hit within 3 / 6 months (share of buys) | 33% / 57% | 65% / 81% | 62% / 76% | 78% / 96% |
| 12-month return: median / mean | +33% / +31% | +48% / +61% | +49% / +47% | +55% / +60% |
| 12-month return positive | 81% | 81% | 95% | 96% |
| Best / worst 12-month return | +104% CFR / -21% META | +378% SGI / -55% TTD | +93% CFR / -2% PII | +166% RCL / -8% FIS |
| Beat SPY over the same 12 months | 48% | 65% | 71% | 74% |
| SPY over the same 12 months (median) | +22% | +22% | +20% | +31% |
| Excess over SPY (median) | -1% | +16% | +15% | +23% |
| Max gain in the window (median / best) | +40% / +106% CFR | +59% / +378% SGI | +64% / +103% CFR | +60% / +200% RCL |
| Max drawdown from entry (median / worst) | -24% / -62% META | -7% / -63% TTD | -14% / -45% META | -7% / -49% WAL |
| Drawdown before the hit (median, hits only) | -9% | -4% | -4% | -7% |
| Buys that fell more than 10% / 20% below entry | 71% / 57% | 46% / 25% | 57% / 29% | 39% / 22% |
| RSI printed lower after the buy | 57% | 32% | 48% | 26% |
| Misses (no +20% close in 12 months) | 5/21 = 24% | 8/57 = 14% | 2/21 = 10% | 1/23 = 4% |
| Misses: 12m return median / max DD median | -10% / -29% | -5% / -24% | +3% / -19% | -8% / -29% |


| Ticker | Weekly signal | Monthly signal | Weekly first by (weeks) | Weekly entry vs monthly | 12m weekly | 12m monthly | Max DD weekly / monthly | Hit weekly / monthly |
|---|---|---|---|---|---|---|---|---|
| GILD | 2010-06-04 | 2010-08 | 13 | +9% | +18% | +25% | -8% / +4% | yes / yes |
| DLB | 2011-08-05 | 2011-09 | 8 | +13% | -1% | +19% | -15% / -4% | yes / yes |
| ILMN | 2011-09-30 | 2011-10 | 4 | +34% | +18% | +55% | -37% / -15% | yes / yes |
| PII | 2015-12-04 | 2015-12 | 4 | +15% | -10% | -2% | -30% / -19% | no / no |
| PAG | 2016-01-15 | 2016-01 | 2 | +7% | +61% | +78% | -11% / -4% | yes / yes |
| CFR | 2016-01-22 | 2016-01 | 1 | -7% | +104% | +93% | -5% / -5% | yes / yes |
| ORLY | 2017-07-07 | 2017-08 | 8 | -12% | +64% | +71% | +0% / +0% | yes / yes |
| EPR | 2018-02-09 | 2018-03 | 7 | +1% | +40% | +48% | -5% / -4% | yes / yes |
| STT | 2018-10-26 | 2018-12 | 9 | +4% | +2% | +29% | -25% / -21% | no / yes |
| PVH | 2018-12-14 | 2018-12 | 2 | +0% | +12% | +13% | -26% / -26% | yes / yes |
| RGA | 2020-03-13 | 2020-03 | 3 | +14% | +38% | +54% | -40% / -19% | yes / yes |
| AFG | 2020-03-13 | 2020-03 | 3 | +9% | +62% | +71% | -38% / -22% | yes / yes |
| MOG-A | 2020-03-13 | 2020-03 | 3 | +2% | +70% | +66% | -32% / -21% | yes / yes |
| META | 2022-02-04 | 2022-06 | 21 | +47% | -21% | +78% | -62% / -45% | no / yes |
| NFLX | 2022-04-22 | 2022-04 | 1 | +13% | +52% | +73% | -23% / -13% | yes / yes |
| CHTR | 2022-04-29 | 2022-09 | 22 | +41% | -14% | +45% | -29% / +1% | no / yes |
| SWKS | 2022-05-06 | 2022-06 | 8 | +13% | +1% | +22% | -24% / -14% | no / yes |
| ALGN | 2022-06-17 | 2022-06 | 2 | -1% | +41% | +49% | -26% / -26% | yes / yes |
| PNR | 2022-06-17 | 2022-09 | 15 | +8% | +41% | +62% | -10% / -3% | yes / yes |
| CGNX | 2022-06-17 | 2022-06 | 2 | +1% | +30% | +32% | -5% / -4% | yes / yes |
| CCI | 2023-09-22 | 2023-07 | -8 | -14% | +33% | +8% | -7% / -19% | yes / no |
| FISV | 2025-10-31 | 2025-10 | 0 | +0% | -30% (open) | -30% (open) | -31% / -31% | no / no |
| TYL | 2026-01-30 | 2026-01 | 0 | +0% | -12% (open) | -12% (open) | -25% / -25% | no / no |
| NOW | 2026-02-06 | 2026-02 | 3 | -7% | +35% (open) | +26% (open) | -18% / -23% | yes / yes |
| INTU | 2026-02-13 | 2026-02 | 2 | -2% | -30% (open) | -32% (open) | -36% / -37% | yes / no |
| EXLS | 2026-02-13 | 2026-06 | 20 | +16% | +16% (open) | +34% (open) | -16% / +4% | yes / yes |
| BSX | 2026-04-03 | 2026-03 | -0 | +0% | -30% (open) | -30% (open) | -32% / -32% | no / no |
| ROL | 2026-06-26 | 2026-07 | 5 | +14% | -30% (open) | -21% (open) | -30% / -21% | no / no |

Over the 21 pairs with complete windows the weekly entry's 12-month return was a median -9% vs the monthly entry's (better in 3, worse in 18).

## Misses

### Monthly

| Ticker | Sector | Signal | RSI | vs ATH | Max gain | Max DD | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|
| PII | Consumer Discretionary | 2015-12 | 31 | -46% | +18% | -19% | -2% | +12% |
| FIS | Financials | 2022-12 | 35 | -57% | +15% | -29% | -8% | +26% |
| CCI | Real Estate | 2023-07 | 35 | -48% | +11% | -19% | +8% | +22% |

### Weekly

| Ticker | Sector | Signal | RSI | vs ATH | Max gain | Max DD | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|
| HAL | Energy | 2014-11-28 | 23 | -43% | +18% | -20% | -6% | +3% |
| PII | Consumer Discretionary | 2015-12-04 | 23 | -38% | +3% | -30% | -10% | +7% |
| WSM | Consumer Discretionary | 2016-01-08 | 23 | -39% | +14% | -13% | -8% | +21% |
| JLL | Real Estate | 2016-02-05 | 24 | -38% | +12% | -20% | -4% | +25% |
| LEA | Consumer Discretionary | 2018-10-05 | 25 | -31% | +12% | -25% | -21% | +4% |
| EXP | Materials | 2018-10-05 | 25 | -33% | +13% | -30% | +9% | +4% |
| STT | Financials | 2018-10-26 | 23 | -42% | +12% | -25% | +2% | +16% |
| THO | Consumer Discretionary | 2018-10-26 | 25 | -58% | +11% | -35% | +3% | +16% |
| META | Communication Services | 2022-02-04 | 24 | -38% | -1% | -62% | -21% | -7% |
| FBIN | Industrials | 2022-04-15 | 24 | -39% | +14% | -23% | +0% | -4% |
| CHTR | Communication Services | 2022-04-29 | 22 | -48% | +19% | -29% | -14% | +3% |
| SWKS | Information Technology | 2022-05-06 | 25 | -48% | +18% | -24% | +1% | +2% |
| SMTC | Information Technology | 2022-09-16 | 25 | -67% | +10% | -43% | -21% | +17% |


## Sector mix and cadence

| Sector | Monthly buys | Weekly buys |
|---|---|---|
| Consumer Discretionary | 10 | 21 |
| Industrials | 11 | 19 |
| Financials | 11 | 13 |
| Information Technology | 8 | 9 |
| Health Care | 6 | 9 |
| Communication Services | 5 | 6 |
| Real Estate | 6 | 5 |
| Materials | 0 | 4 |
| Energy | 0 | 1 |
| Consumer Staples | 0 | 1 |

The weekly signal fires 1.9x as often before fundamentals and 1.6x after. It bunches into crash weeks: 2020-03-20 (14 buys), 2018-10-26 (6 buys), 2020-03-13 (6 buys), 2022-06-17 (4 buys), 2026-02-13 (3 buys). The top-20 cap bound in 2020 on the weekly list and never on the monthly one.

## Caveats

* Same universe for both: today's index members, so stocks that never recovered are missing and every drawdown rule is flattered.
* Small yearly samples on both lists; the totals are the honest comparison, and 2020 dominates both (12 of 44 monthly windows, 20 of 78 weekly).
* The weekly fundamentals row is the prior month-end, so its valuation percentile is priced slightly before the signal; that makes the weekly cheap filter a little stricter, not looser.
* No costs, taxes or position sizing; each buy is scored on its own 12-month window.

Sources: `OpportunityScanner2/output/yearly_backtest_t20_sector30.md`, `OpportunityScanner2/output/yearly_backtest_weekly_rsi25_t20.md`; scripts `yearly_backtest.py`, `yearly_backtest_weekly.py`.
