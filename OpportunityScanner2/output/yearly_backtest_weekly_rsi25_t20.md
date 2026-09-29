# Tier A yearly backtest on weekly candles: former overbought-ATH leader, weekly RSI < 25, +20% target

Generated 2026-09-29. Universe: today's S&P 500 + 400 (899 tickers, survivorship bias), weekly candles (weeks ending Friday) to 2026-09-25, fundamentals point in time from SEC filings. Weekly twin of `yearly_backtest.py --target 0.20 --sector-rsi 0` (output/yearly_backtest_t20_sector30.md).

**Trigger**: a new all-time high on a weekly candle with weekly RSI(14) ≥ 70 (≥ 5 years of history) arms the stock for 156 weeks (36 months); the first week whose weekly RSI closes below 25 is the buy, at that Friday's close. **Filters**: quality (profitable TTM and in 2 of the 3 past years, revenue growth ≥ 5%, EPS growing, no one-off gain, no acquisition-driven growth) and cheap (operating multiples in the bottom half of the company's own history), both read from the fundamentals row of the last month-end on or before the signal week (only filings public by then; the valuation is priced at that month-end). Liquid names only (63-day average dollar volume ≥ $5M at the signal). Signals are grouped by calendar year, ranked by signal RSI (lowest first) and cut to the top 20.

**What is measured** over the 12 months after the buy (daily adjusted closes): whether the stock closed ≥ 20% above the buy price ("hit") and how long that took; the highest close vs the buy ("max gain"); the lowest close vs the buy ("max DD", the drawdown from the entry price) and the same measured only up to the hit day ("DD before hit"); whether the weekly RSI printed below the signal RSI afterwards ("RSI went lower", ↓ in the tables, with the RSI low); and the plain 12-month return. Windows that run past 2026-09-25 are "open" and show what happened so far.

**SPY**: "SPY cal. year" is SPY's total return over the calendar year of the signals (2026 to the last completed week); "SPY same 12m" is SPY over each buy's own 12-month window, and "beat SPY" the share of buys that returned more than SPY over that window.

> Quality alone: 149 signals; quality + cheap: 94 (the cheap filter drops 55).


## Weekly vs monthly candles (quality + cheap, complete 12-month windows)

| List | Buys (complete 12m) | Hit target | Months to hit (median) | ≤3m / ≤6m | 12m median / mean | 12m positive | beat SPY | SPY same 12m (median) | Max gain (median) | Max DD (median / worst) | DD before hit (median) | DD worse than -20% | RSI went lower | Misses | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| weekly RSI (this run) | 78 | 65/78 = 83% | 1.8 | 56% / 74% | +40% / +53% | 81% | 60% | +22% | +51% | -10% / -63% TTD | -5% | 33% | 38% | 13/78 = 17% | -6% |
| monthly RSI (yearly_backtest_t20_sector30) | 44 | 41/44 = 93% | 1.9 | 70% / 86% | +54% / +54% | 95% | 73% | +24% | +62% | -9% / -49% WAL | -6% | 25% | 36% | 3/44 = 7% | -2% |


Signals before the cut: **94 weekly** vs **58 monthly** (the weekly RSI dips below 25 far more often, so the top-20 cap binds in 1 year on the weekly list and never on the monthly one). Of the 88 weekly buys, 28 have a monthly buy of the same stock within 3 months before or 6 months after (32%); of the 57 monthly buys, 28 have a weekly buy of the same stock in that range (49%). Where both fired, the weekly signal came a median 2.9 weeks before the monthly month-end (range -8 to 22), and the weekly entry price was a median +6% vs the monthly entry (negative = weekly bought lower).

**How far into the decline each candle buys**: the weekly buys sit a median -44% below the all-time high (quartiles -53% to -38%), a median 10.0 months after the last overbought high; the monthly buys sit -50% below it (quartiles -58% to -43%), 16.0 months after. A weekly RSI under 25 needs a fast, deep slide of a few months; a monthly RSI under 35 needs a year or more of falling closes, so the monthly signal is the deeper washout of the same idea.

Repeat names on the weekly list: 0 buys are a second signal of the same stock within 12 months of an earlier buy (overlapping windows, counted separately in every table).


Pairs (same stock, both candles): weekly signal, monthly signal, weeks the weekly came first, weekly entry vs monthly entry, 12m return weekly / monthly.

| Ticker | Weekly signal | Monthly signal | Weekly first by (weeks) | Weekly entry vs monthly | 12m weekly | 12m monthly | Hit weekly / monthly |
|---|---|---|---|---|---|---|---|
| GILD | 2010-06-04 | 2010-08 | 13 | +9% | +18% | +25% | yes / yes |
| DLB | 2011-08-05 | 2011-09 | 8 | +13% | -1% | +19% | yes / yes |
| ILMN | 2011-09-30 | 2011-10 | 4 | +34% | +18% | +55% | yes / yes |
| PII | 2015-12-04 | 2015-12 | 4 | +15% | -10% | -2% | no / no |
| CFR | 2016-01-22 | 2016-01 | 1 | -7% | +104% | +93% | yes / yes |
| PAG | 2016-01-15 | 2016-01 | 2 | +7% | +61% | +78% | yes / yes |
| ORLY | 2017-07-07 | 2017-08 | 8 | -12% | +64% | +71% | yes / yes |
| STT | 2018-10-26 | 2018-12 | 9 | +4% | +2% | +29% | no / yes |
| EPR | 2018-02-09 | 2018-03 | 7 | +1% | +40% | +48% | yes / yes |
| PVH | 2018-12-14 | 2018-12 | 2 | +0% | +12% | +13% | yes / yes |
| RGA | 2020-03-13 | 2020-03 | 3 | +14% | +38% | +54% | yes / yes |
| AFG | 2020-03-13 | 2020-03 | 3 | +9% | +62% | +71% | yes / yes |
| MOG-A | 2020-03-13 | 2020-03 | 3 | +2% | +70% | +66% | yes / yes |
| NFLX | 2022-04-22 | 2022-04 | 1 | +13% | +52% | +73% | yes / yes |
| CHTR | 2022-04-29 | 2022-09 | 22 | +41% | -14% | +45% | no / yes |
| ALGN | 2022-06-17 | 2022-06 | 2 | -1% | +41% | +49% | yes / yes |
| PNR | 2022-06-17 | 2022-09 | 15 | +8% | +41% | +62% | yes / yes |
| META | 2022-02-04 | 2022-06 | 21 | +47% | -21% | +78% | no / yes |
| SWKS | 2022-05-06 | 2022-06 | 8 | +13% | +1% | +22% | no / yes |
| CGNX | 2022-06-17 | 2022-06 | 2 | +1% | +30% | +32% | yes / yes |
| CCI | 2023-09-22 | 2023-07 | -8 | -14% | +33% | +8% | yes / no |
| FISV | 2025-10-31 | 2025-10 | 0 | +0% | open | open | no / no |
| TYL | 2026-01-30 | 2026-01 | 0 | +0% | open | open | no / no |
| NOW | 2026-02-06 | 2026-02 | 3 | -7% | open | open | yes / yes |
| INTU | 2026-02-13 | 2026-02 | 2 | -2% | open | open | yes / no |
| EXLS | 2026-02-13 | 2026-06 | 20 | +16% | open | open | yes / yes |
| ROL | 2026-06-26 | 2026-07 | 5 | +14% | open | open | no / no |
| BSX | 2026-04-03 | 2026-03 | -0 | +0% | open | open | no / no |


## Sensitivity: weekly RSI threshold and the yearly cap (quality + cheap, complete 12-month windows)

| List | Buys (complete 12m) | Hit target | Months to hit (median) | ≤3m / ≤6m | 12m median / mean | 12m positive | beat SPY | SPY same 12m (median) | Max gain (median) | Max DD (median / worst) | DD before hit (median) | DD worse than -20% | RSI went lower | Misses | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| weekly RSI < 25 (sector rule 0), top 20 / year (this run) | 78 | 65/78 = 83% | 1.8 | 56% / 74% | +40% / +53% | 81% | 60% | +22% | +51% | -10% / -63% TTD | -5% | 33% | 38% | 13/78 = 17% | -6% |
| weekly RSI < 25 (sector rule 0), no cap | 84 | 71/84 = 85% | 1.8 | 60% / 76% | +41% / +61% | 82% | 63% | +22% | +55% | -10% / -63% TTD | -5% | 32% | 38% | 13/84 = 15% | -6% |
| weekly RSI < 30, top 20 / year | 155 | 118/155 = 76% | 3.3 | 37% / 60% | +25% / +30% | 74% | 54% | +21% | +37% | -12% / -68% UAL | -7% | 34% | 60% | 37/155 = 24% | -13% |
| weekly RSI < 30, no cap | 171 | 129/171 = 75% | 3.2 | 37% / 60% | +25% / +30% | 74% | 55% | +21% | +36% | -12% / -68% UAL | -6% | 34% | 60% | 42/171 = 25% | -13% |
| weekly RSI < 25, no cap | 84 | 71/84 = 85% | 1.8 | 60% / 76% | +41% / +61% | 82% | 63% | +22% | +55% | -10% / -63% TTD | -5% | 32% | 38% | 13/84 = 15% | -6% |
| weekly RSI < 20, no cap | 26 | 25/26 = 96% | 0.8 | 69% / 85% | +68% / +91% | 88% | 81% | +33% | +71% | -6% / -66% RCL | -3% | 19% | 31% | 1/26 = 4% | -1% |


Each row is the same pipeline with a different signal threshold (the sector rule keeps the lower of the two levels) or without the top-20 cut per year. Lower thresholds fire later and less often.


## quality + cheap

94 signals since 2010, 88 after the top-20 cut per year (the cap bound in 2020).

### Summary by year

| Year | SPY cal. year | Buys | Hit +20% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | 12m return: median / mean | 12m best | 12m worst | beat SPY (same 12m) | SPY same 12m (median) | Max gain (median / best) | Max DD (median / worst) | RSI went lower | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | +15% | 1 | 1/1 = 100% | 9.6 / 9.6 / 9.6 | 0% / 0% | +18% / +18% | +18% GILD | +18% GILD | 0% | +25% | +23% / +23% GILD | -8% / -8% GILD | 100% | 0/1 = 0% | – / – | – |
| 2011 | +2% | 6 | 6/6 = 100% | 4.1 / 4.2 / 6.0 | 33% / 100% | +27% / +24% | +68% TTC | -17% NFLX | 50% | +21% | +47% / +71% TTC | -20% / -37% ILMN | 50% | 0/6 = 0% | – / – | – |
| 2012 | +16% | 1 | 1/1 = 100% | 1.6 / 1.6 / 1.6 | 100% / 100% | +73% / +73% | +73% SGI | +73% SGI | 100% | +27% | +96% / +96% SGI | -18% / -18% SGI | 100% | 0/1 = 0% | – / – | – |
| 2013 | +32% | 0 | | | | | | | | | | | | | | |
| 2014 | +13% | 1 | 0/1 = 0% | – / – / – | 0% / 0% | -6% / -6% | -6% HAL | -6% HAL | 0% | +3% | +18% / +18% HAL | -20% / -20% HAL | 100% | 1/1 = 100% | -20% / -20% | -6% |
| 2015 | +1% | 2 | 1/2 = 50% | 2.3 / 2.3 / 2.3 | 50% / 50% | +26% / +26% | +62% DKS | -10% PII | 50% | +11% | +40% / +77% DKS | -17% / -30% PII | 50% | 1/2 = 50% | -30% / -30% | -10% |
| 2016 | +12% | 8 | 6/8 = 75% | 1.5 / 1.6 / 2.7 | 75% / 75% | +29% / +41% | +104% EXP | -8% WSM | 50% | +23% | +40% / +107% EXP | -7% / -20% JLL | 38% | 2/8 = 25% | -17% / -20% | -6% |
| 2017 | +22% | 2 | 2/2 = 100% | 4.8 / 4.8 / 8.7 | 50% / 50% | +39% / +39% | +64% ORLY | +14% ULTA | 50% | +18% | +44% / +66% ORLY | -5% / -10% ULTA | 0% | 0/2 = 0% | – / – | – |
| 2018 | -5% | 14 | 10/14 = 71% | 3.5 / 3.1 / 5.9 | 36% / 71% | +26% / +34% | +128% FN | -21% LEA | 57% | +16% | +41% / +131% FN | -12% / -35% THO | 36% | 4/14 = 29% | -27% / -35% | +3% |
| 2019 | +31% | 1 | 1/1 = 100% | 4.0 / 4.0 / 4.0 | 0% / 100% | +1% / +1% | +1% ULTA | +1% ULTA | 0% | +13% | +33% / +33% ULTA | -43% / -43% ULTA | 0% | 0/1 = 0% | – / – | – |
| 2020 | +18% | 20 | 20/20 = 100% | 0.6 / 2.0 / 9.4 | 80% / 85% | +100% / +123% | +378% SGI | +38% RGA | 85% | +73% | +118% / +378% SGI | -6% / -51% STWD | 30% | 0/20 = 0% | – / – | – |
| 2021 | +29% | 0 | | | | | | | | | | | | | | |
| 2022 | -18% | 13 | 8/13 = 62% | 1.9 / 3.2 / 7.5 | 38% / 54% | +30% / +29% | +152% WING | -21% META | 69% | +3% | +33% / +161% WING | -23% / -62% META | 46% | 5/13 = 38% | -29% / -62% | -14% |
| 2023 | +26% | 3 | 3/3 = 100% | 2.2 / 3.7 / 7.5 | 67% / 67% | +36% / +46% | +70% VMI | +33% CCI | 33% | +43% | +46% / +74% VMI | -0% / -7% CCI | 33% | 0/3 = 0% | – / – | – |
| 2024 | +25% | 2 | 2/2 = 100% | 1.9 / 1.9 / 3.1 | 50% / 100% | +13% / +13% | +39% DXCM | -13% LULU | 50% | +18% | +54% / +66% LULU | -10% / -14% LULU | 50% | 0/2 = 0% | – / – | – |
| 2025 | +18% | 6 (2 open) | 4/6 = 67% | 2.2 / 2.0 / 2.5 | 67% / 67% | -2% / -9% | +24% TTEK | -55% TTD | 25% | +17% | +30% / +83% ANF | -25% / -63% TTD | 50% | 0/4 = 0% | – / – | – |
| 2026 | +14% | 8 (8 open) | 5/8 = 62% | 0.9 / 1.8 / 6.1 | 50% / 50% | – / – | – | – | – | – | +24% / +47% NOW | -22% / -36% INTU | 50% | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-09-25)** |  | 78 | 65/78 = 83% | 1.8 / 2.8 / 9.6 | 56% / 74% | +40% / +53% | +378% SGI | -55% TTD | 60% | +22% | +51% / +378% SGI | -10% / -63% TTD | 38% | 13/78 = 17% | -25% / -62% | -6% |
| **All incl. open** |  | 88 (10 open) | 70/88 = 80% | 1.7 / 2.7 / 9.6 | 55% / 70% | +40% / +53% | +378% SGI | -55% TTD | 60% | +22% | +47% / +378% SGI | -12% / -63% TTD | 41% | 13/78 = 17% | -25% / -62% | -6% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months (30.44 days) from the signal week's Friday. "RSI went lower" = share of buys whose weekly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 1 buys, 1 hit +20%, SPY +15% that year, 12m median +18%, best +18%, worst +18%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GILD | Gilead Sciences | Health Care | 2010-06-04 | 23 | -40% | 135 | 0% | +27% | +51% | yes | 9.6 | +23% (10.0) | -8% (2.9) | -8% | 23 ↓ | +18% | +25% |


#### 2011: 6 buys, 6 hit +20%, SPY +2% that year, 12m median +27%, best +68%, worst -17%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UTHR | United Therapeutics | Health Care | 2011-08-26 | 20 | -43% | 25 | 7% | +63% | +391% | yes | 4.3 | +42% (11.7) | -7% (1.2) | -7% | 23 | +38% | +23% |
| 2 | LII | Lennox International | Industrials | 2011-08-05 | 22 | -38% | 67 | 38% | +7% | +117% | yes | 6.0 | +47% (11.0) | -24% (1.6) | -24% | 17 ↓ | +36% | +19% |
| 3 | DLB | Dolby | Information Technology | 2011-08-05 | 24 | -56% | 65 | 4% | +28% | +23% | yes | 5.6 | +46% (9.4) | -15% (1.9) | -15% | 25 | -1% | +19% |
| 4 | NFLX | Netflix | Communication Services | 2011-10-28 | 24 | -72% | 21 | 19% | +41% | +60% | yes | 2.7 | +54% (3.3) | -36% (10.9) | -24% | 22 ↓ | -17% | +12% |
| 5 | TTC | Toro | Industrials | 2011-08-19 | 25 | -31% | 37 | 40% | +11% | +105% | yes | 2.5 | +71% (11.0) | -3% (1.5) | -3% | 37 | +68% | +29% |
| 6 | ILMN | Illumina, Inc. | Health Care | 2011-09-30 | 25 | -48% | 32 | 0% | +44% | +64% | yes | 3.8 | +35% (3.8) | -37% (2.4) | -37% | 18 ↓ | +18% | +30% |


#### 2012: 1 buys, 1 hit +20%, SPY +16% that year, 12m median +73%, best +73%, worst +73%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SGI | Somnigroup International | Consumer Discretionary | 2012-06-08 | 23 | -71% | 9 | 23% | +28% | +47% | yes | 1.6 | +96% (9.6) | -18% (0.6) | -18% | 22 ↓ | +73% | +27% |


#### 2014: 1 buys, 0 hit +20%, SPY +13% that year, 12m median -6%, best -6%, worst -6%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HAL | Halliburton | Energy | 2014-11-28 | 23 | -43% | 18 | 47% | +9% | +82% | **no** | – | +18% (5.0) | -20% (8.9) | -20% | 20 ↓ | -6% | +3% |


#### 2015: 2 buys, 1 hit +20%, SPY +1% that year, 12m median +26%, best +62%, worst -10%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PII | Polaris | Consumer Discretionary | 2015-12-04 | 23 | -38% | 99 | 22% | +14% | +13% | **no** | – | +3% (4.7) | -30% (1.8) | -30% | 17 ↓ | -10% | +7% |
| 2 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2015-12-18 | 24 | -41% | 39 | 3% | +9% | +13% | yes | 2.3 | +77% (11.7) | -4% (0.9) | -4% | 25 | +62% | +15% |


#### 2016: 8 buys, 6 hit +20%, SPY +12% that year, 12m median +29%, best +104%, worst -8%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MCK | McKesson Corporation | Health Care | 2016-10-28 | 19 | -49% | 126 | 46% | +5% | +38% | yes | 2.7 | +36% (8.6) | +2% (0.1) | +2% | 26 | +10% | +24% |
| 2 | WSM | Williams-Sonoma, Inc. | Consumer Discretionary | 2016-01-08 | 23 | -39% | 47 | 26% | +7% | +10% | **no** | – | +14% (3.6) | -13% (9.8) | -13% | 20 ↓ | -8% | +21% |
| 3 | SEIC | SEI Investments Company | Financials | 2016-02-05 | 24 | -35% | 25 | 49% | +6% | +9% | yes | 1.8 | +45% (11.3) | -6% (0.2) | -6% | 25 | +37% | +25% |
| 4 | CFR | Frost Bank | Financials | 2016-01-22 | 24 | -46% | 126 | 14% | +8% | +8% | yes | 1.3 | +106% (11.7) | -5% (0.1) | -5% | 30 | +104% | +22% |
| 5 | JLL | Jones Lang LaSalle | Real Estate | 2016-02-05 | 24 | -38% | 46 | 33% | +12% | +28% | **no** | – | +12% (2.7) | -20% (8.9) | -20% | 21 ↓ | -4% | +25% |
| 6 | PAG | Penske Automotive Group | Consumer Discretionary | 2016-01-15 | 24 | -38% | 119 | 21% | +8% | +20% | yes | 1.7 | +72% (10.8) | -11% (0.6) | -11% | 22 ↓ | +61% | +23% |
| 7 | AN | AutoNation | Consumer Discretionary | 2016-01-29 | 25 | -36% | 81 | 10% | +11% | +18% | yes | 0.9 | +23% (6.0) | -7% (9.3) | +0% | 31 | +21% | +21% |
| 8 | EXP | Eagle Materials | Materials | 2016-01-22 | 25 | -53% | 70 | 21% | +16% | +16% | yes | 1.1 | +107% (10.6) | -5% (0.2) | -5% | 33 | +104% | +22% |


#### 2017: 2 buys, 2 hit +20%, SPY +22% that year, 12m median +39%, best +64%, worst +14%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2017-07-07 | 17 | -41% | 88 | 37% | +6% | +13% | yes | 0.8 | +66% (11.5) | +0% (0.1) | +0% | 24 | +64% | +16% |
| 2 | ULTA | Ulta Beauty | Consumer Discretionary | 2017-08-25 | 24 | -33% | 12 | 41% | +23% | +32% | yes | 8.7 | +22% (10.6) | -10% (1.6) | -10% | 27 | +14% | +20% |


#### 2018: 14 buys, 10 hit +20%, SPY -5% that year, 12m median +26%, best +128%, worst -21%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FBIN | Fortune Brands Innovations | Industrials | 2018-10-26 | 21 | -44% | 67 | 12% | +5% | +8% | yes | 5.3 | +49% (11.9) | -13% (1.9) | -13% | 25 | +48% | +16% |
| 2 | EVR | Evercore | Financials | 2018-12-21 | 22 | -44% | 46 | 32% | +14% | +1% | yes | 0.7 | +49% (4.2) | -2% (0.1) | -2% | 30 | +19% | +36% |
| 3 | STT | State Street Corporation | Financials | 2018-10-26 | 23 | -42% | 39 | 50% | +10% | +12% | **no** | – | +12% (1.1) | -25% (9.6) | -25% | 25 | +2% | +16% |
| 4 | EPR | EPR Properties | Real Estate | 2018-02-09 | 24 | -33% | 80 | 21% | +18% | +8% | yes | 4.3 | +40% (12.0) | -5% (0.7) | -5% | 25 | +40% | +5% |
| 5 | IBKR | Interactive Brokers | Financials | 2018-10-26 | 24 | -41% | 24 | 48% | +47% | +58% | yes | 0.4 | +23% (6.3) | -6% (10.0) | -1% | 35 | -2% | +16% |
| 6 | UFPI | UFP Industries | Industrials | 2018-10-26 | 24 | -30% | 46 | 42% | +22% | +36% | yes | 5.9 | +83% (11.9) | -12% (1.9) | -12% | 25 | +83% | +16% |
| 7 | THO | Thor Industries | Consumer Discretionary | 2018-10-26 | 25 | -58% | 41 | 3% | +15% | +27% | **no** | – | +11% (0.3) | -35% (9.6) | -35% | 22 ↓ | +3% | +16% |
| 8 | MAS | Masco | Industrials | 2018-10-12 | 25 | -30% | 38 | 38% | +7% | +16% | yes | 4.6 | +35% (11.0) | -15% (0.6) | -15% | 17 ↓ | +34% | +10% |
| 9 | DHI | D. R. Horton | Consumer Discretionary | 2018-11-09 | 25 | -35% | 44 | 5% | +15% | +28% | yes | 4.0 | +59% (11.5) | -4% (1.5) | -4% | 27 | +51% | +13% |
| 10 | PVH | PVH Corp. | Consumer Discretionary | 2018-12-14 | 25 | -45% | 27 | 23% | +13% | +69% | yes | 1.8 | +42% (4.3) | -26% (8.3) | -7% | 23 ↓ | +12% | +24% |
| 11 | FN | Fabrinet | Information Technology | 2018-02-02 | 25 | -50% | 69 | 19% | +32% | +12% | yes | 0.8 | +131% (11.7) | -4% (0.1) | -4% | 40 | +128% | -0% |
| 12 | LEA | Lear | Consumer Discretionary | 2018-10-05 | 25 | -31% | 36 | 38% | +12% | +31% | **no** | – | +12% (3.7) | -25% (10.3) | -25% | 22 ↓ | -21% | +4% |
| 13 | AMAT | Applied Materials | Information Technology | 2018-10-26 | 25 | -48% | 49 | 28% | +27% | +6% | yes | 3.0 | +76% (12.0) | -10% (1.9) | -10% | 31 | +76% | +16% |
| 14 | EXP | Eagle Materials | Materials | 2018-10-05 | 25 | -33% | 43 | 17% | +10% | +29% | **no** | – | +13% (8.7) | -30% (2.6) | -30% | 17 ↓ | +9% | +4% |


#### 2019: 1 buys, 1 hit +20%, SPY +31% that year, 12m median +1%, best +1%, worst +1%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ULTA | Ulta Beauty | Consumer Discretionary | 2019-09-13 | 24 | -38% | 43 | 4% | +12% | +23% | yes | 4.0 | +33% (5.3) | -43% (6.1) | -1% | 25 | +1% | +13% |


#### 2020: 20 buys, 20 hit +20%, SPY +18% that year, 12m median +100%, best +378%, worst +38%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DAL | Delta Air Lines | Industrials | 2020-03-20 | 16 | -66% | 113 | 18% | +5% | +25% | yes | 0.1 | +139% (11.8) | -10% (1.8) | +4% | 25 | +130% | +73% |
| 2 | UHS | Universal Health Services | Health Care | 2020-03-20 | 18 | -52% | 34 | 46% | +6% | +10% | yes | 0.2 | +89% (9.6) | -5% (0.1) | -5% | 28 | +83% | +73% |
| 3 | EME | Emcor | Industrials | 2020-03-20 | 19 | -47% | 37 | 43% | +13% | +19% | yes | 0.2 | +134% (11.7) | +3% (0.1) | +3% | 30 | +129% | +73% |
| 4 | RGA | Reinsurance Group of America | Financials | 2020-03-13 | 19 | -43% | 119 | 36% | +11% | +24% | yes | 7.9 | +39% (11.9) | -40% (0.3) | -40% | 14 ↓ | +38% | +49% |
| 5 | SGI | Somnigroup International | Consumer Discretionary | 2020-03-20 | 20 | -67% | 5 | 45% | +15% | +88% | yes | 0.1 | +378% (12.0) | +3% (0.5) | +9% | 28 | +378% | +73% |
| 6 | CBRE | CBRE Group | Real Estate | 2020-03-20 | 20 | -47% | 5 | 46% | +12% | +27% | yes | 0.6 | +135% (11.8) | -13% (0.1) | -13% | 27 | +124% | +73% |
| 7 | STWD | Starwood Property Trust | Financials | 2020-03-13 | 20 | -32% | 25 | 1% | +8% | +26% | yes | 9.4 | +54% (12.0) | -51% (0.4) | -51% | 11 ↓ | +54% | +49% |
| 8 | TKR | Timken | Industrials | 2020-03-20 | 20 | -55% | 9 | 28% | +10% | +4% | yes | 0.2 | +229% (11.9) | -5% (0.1) | -5% | 29 | +222% | +73% |
| 9 | JPM | JPMorgan Chase | Financials | 2020-03-20 | 20 | -41% | 11 | 48% | +6% | +19% | yes | 0.7 | +96% (11.9) | -5% (0.1) | -5% | 26 | +93% | +73% |
| 10 | FIVE | Five Below | Consumer Discretionary | 2020-03-13 | 20 | -48% | 79 | 44% | +21% | +20% | yes | 1.5 | +156% (11.2) | -32% (0.2) | -32% | 15 ↓ | +149% | +49% |
| 11 | EXPE | Expedia Group | Consumer Discretionary | 2020-03-20 | 21 | -70% | 138 | 15% | +8% | +30% | yes | 0.1 | +280% (11.9) | -2% (0.4) | +4% | 26 | +269% | +73% |
| 12 | MLM | Martin Marietta Materials | Materials | 2020-03-20 | 21 | -45% | 14 | 34% | +12% | +31% | yes | 0.2 | +128% (11.4) | -6% (0.1) | -6% | 31 | +118% | +73% |
| 13 | PCAR | Paccar | Industrials | 2020-03-20 | 21 | -37% | 14 | 19% | +9% | +10% | yes | 0.6 | +95% (10.7) | -5% (0.1) | -5% | 35 | +86% | +73% |
| 14 | VMC | Vulcan Materials Company | Materials | 2020-03-20 | 21 | -44% | 25 | 30% | +12% | +20% | yes | 0.2 | +107% (11.2) | -3% (0.1) | -3% | 33 | +97% | +73% |
| 15 | AFG | American Financial Group | Financials | 2020-03-13 | 21 | -37% | 110 | 47% | +15% | +68% | yes | 8.3 | +62% (12.0) | -38% (0.2) | -38% | 14 ↓ | +62% | +49% |
| 16 | RBA | RB Global | Industrials | 2020-03-20 | 22 | -37% | 9 | 36% | +13% | +23% | yes | 0.4 | +168% (7.6) | -2% (0.1) | -2% | 36 | +104% | +73% |
| 17 | CPAY | Corpay | Financials | 2020-03-20 | 22 | -43% | 28 | 43% | +8% | +25% | yes | 0.7 | +55% (11.2) | -8% (0.1) | -8% | 24 | +50% | +73% |
| 18 | ALLY | Ally Financial | Financials | 2020-03-13 | 22 | -42% | 33 | 2% | +10% | +63% | yes | 5.7 | +129% (11.9) | -43% (0.2) | -43% | 14 ↓ | +129% | +49% |
| 19 | MOG-A | Moog Inc. | Industrials | 2020-03-13 | 22 | -48% | 126 | 37% | +8% | +37% | yes | 2.7 | +70% (12.0) | -32% (0.2) | -32% | 19 ↓ | +70% | +49% |
| 20 | MMS | Maximus Inc. | Industrials | 2020-03-20 | 23 | -37% | 114 | 15% | +25% | +13% | yes | 0.7 | +71% (11.7) | +5% (0.1) | +5% | 29 | +69% | +73% |


#### 2022: 13 buys, 8 hit +20%, SPY -18% that year, 12m median +30%, best +152%, worst -21%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | Communication Services | 2022-04-22 | 20 | -69% | 25 | 34% | +19% | +85% | yes | 5.9 | +71% (9.1) | -23% (0.6) | -23% | 19 ↓ | +52% | -2% |
| 2 | CHTR | Charter Communications | Communication Services | 2022-04-29 | 22 | -48% | 34 | 26% | +7% | +59% | **no** | – | +19% (0.9) | -29% (5.1) | -29% | 25 | -14% | +3% |
| 3 | WING | Wingstop | Consumer Discretionary | 2022-05-06 | 23 | -55% | 88 | 29% | +14% | +49% | yes | 2.4 | +161% (11.9) | -18% (0.6) | -18% | 21 ↓ | +152% | +2% |
| 4 | ALGN | Align Technology | Health Care | 2022-06-17 | 23 | -68% | 38 | 22% | +43% | +56% | yes | 1.1 | +55% (10.2) | -26% (4.8) | -2% | 28 | +41% | +22% |
| 5 | PNR | Pentair | Industrials | 2022-06-17 | 24 | -45% | 43 | 34% | +23% | +30% | yes | 7.5 | +42% (11.9) | -10% (4.1) | -10% | 31 | +41% | +22% |
| 6 | META | Meta Platforms | Communication Services | 2022-02-04 | 24 | -38% | 28 | 7% | +42% | +39% | **no** | – | -1% (1.9) | -62% (8.9) | -62% | 19 ↓ | -21% | -7% |
| 7 | FBIN | Fortune Brands Innovations | Industrials | 2022-04-15 | 24 | -39% | 49 | 9% | +26% | +41% | **no** | – | +14% (9.6) | -23% (6.2) | -23% | 23 ↓ | +0% | -4% |
| 8 | LAD | Lithia Motors | Consumer Discretionary | 2022-10-21 | 24 | -56% | 83 | 11% | +48% | +39% | yes | 0.7 | +76% (8.6) | +4% (2.0) | +4% | 32 | +40% | +14% |
| 9 | SWKS | Skyworks Solutions | Information Technology | 2022-05-06 | 25 | -48% | 63 | 30% | +29% | +15% | **no** | – | +18% (9.1) | -24% (5.2) | -24% | 23 ↓ | +1% | +2% |
| 10 | SGI | Somnigroup International | Consumer Discretionary | 2022-06-17 | 25 | -58% | 38 | 9% | +32% | +58% | yes | 1.3 | +110% (7.6) | -0% (0.1) | -0% | 30 | +83% | +22% |
| 11 | VEEV | Veeva Systems | Health Care | 2022-03-11 | 25 | -49% | 72 | 47% | +28% | +24% | yes | 0.6 | +33% (4.8) | -13% (7.1) | -2% | 30 | -6% | -7% |
| 12 | CGNX | Cognex | Information Technology | 2022-06-17 | 25 | -58% | 70 | 38% | +22% | +22% | yes | 5.9 | +33% (7.6) | -5% (3.9) | -5% | 28 | +30% | +22% |
| 13 | SMTC | Semtech | Information Technology | 2022-09-16 | 25 | -67% | 45 | 20% | +18% | +119% | **no** | – | +10% (4.6) | -43% (7.6) | -43% | 22 ↓ | -21% | +17% |


#### 2023: 3 buys, 3 hit +20%, SPY +26% that year, 12m median +36%, best +70%, worst +33%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | VMI | Valmont Industries | Industrials | 2023-10-27 | 21 | -47% | 47 | 48% | +10% | +28% | yes | 1.6 | +74% (11.9) | +2% (0.1) | +2% | 29 | +70% | +43% |
| 2 | CCI | Crown Castle | Real Estate | 2023-09-22 | 23 | -56% | 114 | 7% | +6% | +8% | yes | 2.2 | +38% (11.8) | -7% (0.9) | -7% | 22 ↓ | +33% | +34% |
| 3 | MAA | Mid-America Apartment Communities | Real Estate | 2023-10-27 | 24 | -49% | 95 | 34% | +12% | +1% | yes | 7.5 | +46% (10.7) | -0% (0.1) | -0% | 32 | +36% | +43% |


#### 2024: 2 buys, 2 hit +20%, SPY +25% that year, 12m median +13%, best +39%, worst -13%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DXCM | Dexcom | Health Care | 2024-07-26 | 19 | -61% | 140 | 19% | +26% | +117% | yes | 0.8 | +42% (7.0) | -7% (8.3) | +5% | 25 | +39% | +18% |
| 2 | LULU | Lululemon Athletica | Consumer Discretionary | 2024-07-26 | 23 | -51% | 30 | 9% | +16% | +67% | yes | 3.1 | +66% (6.2) | -14% (11.9) | -8% | 21 ↓ | -13% | +18% |


#### 2025: 6 buys, 4 hit +20%, SPY +18% that year, 12m median -2%, best +24%, worst -55%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FISV | Fiserv | Financials | 2025-10-31 | 15 | -72% | 36 | 6% | +5% | +25% | open | – | +5% (2.3) | -31% (10.7) | -31% | 14 ↓ | -30% (so far) | +14% (so far) |
| 2 | SFM | Sprouts Farmers Market | Consumer Staples | 2025-10-31 | 23 | -57% | 37 | 44% | +17% | +49% | open | – | +14% (6.6) | -21% (10.8) | -21% | 23 ↓ | -21% (so far) | +14% (so far) |
| 3 | TTEK | Tetra Tech | Industrials | 2025-02-28 | 24 | -43% | 20 | 44% | +11% | +10% | yes | 2.3 | +47% (11.4) | -4% (1.3) | -4% | 26 | +24% | +17% |
| 4 | BAH | Booz Allen Hamilton | Industrials | 2025-02-28 | 25 | -44% | 16 | 24% | +14% | +115% | yes | 2.5 | +22% (2.7) | -28% (11.8) | -3% | 27 | -24% | +17% |
| 5 | ANF | Abercrombie & Fitch | Consumer Discretionary | 2025-05-02 | 25 | -64% | 48 | 27% | +16% | +167% | yes | 0.9 | +83% (8.2) | -7% (6.8) | -2% | 27 | +19% | +29% |
| 6 | TTD | Trade Desk (The) | Communication Services | 2025-03-07 | 25 | -54% | 13 | 20% | +26% | +152% | yes | 2.2 | +38% (4.9) | -63% (11.7) | -30% | 21 ↓ | -55% | +18% |


#### 2026: 8 buys, 5 hit +20%, SPY +14% that year

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TYL | Tyler Technologies | Information Technology | 2026-01-30 | 20 | -44% | 61 | 45% | +11% | +31% | open | – | +3% (7.1) | -25% (4.7) | -25% | 14 ↓ | -12% (so far) | +12% (so far) |
| 2 | NOW | ServiceNow | Information Technology | 2026-02-06 | 22 | -58% | 60 | 8% | +21% | +21% | yes | 0.9 | +47% (6.8) | -18% (2.1) | -0% | 26 | +35% (so far) | +13% (so far) |
| 3 | INTU | Intuit | Information Technology | 2026-02-13 | 23 | -51% | 32 | 48% | +17% | +42% | yes | 0.7 | +20% (0.7) | -36% (4.3) | -10% | 22 ↓ | -30% (so far) | +14% (so far) |
| 4 | EXLS | EXL Service | Industrials | 2026-02-13 | 24 | -43% | 53 | 50% | +14% | +30% | yes | 6.1 | +28% (6.4) | -16% (4.3) | -16% | 24 | +16% (so far) | +14% (so far) |
| 5 | NFLX | Netflix | Communication Services | 2026-02-13 | 24 | -43% | 32 | 39% | +16% | +28% | yes | 0.5 | +40% (2.0) | -12% (5.2) | -1% | 27 | -7% (so far) | +14% (so far) |
| 6 | ROL | Rollins, Inc. | Industrials | 2026-06-26 | 24 | -35% | 55 | 19% | +11% | +10% | open | – | +5% (0.7) | -30% (3.0) | -30% | 16 ↓ | -30% (so far) | +6% (so far) |
| 7 | ICE | Intercontinental Exchange | Financials | 2026-06-26 | 25 | -35% | 87 | 25% | +7% | +42% | yes | 1.0 | +33% (2.3) | -1% (0.1) | -1% | 35 | +25% (so far) | +6% (so far) |
| 8 | BSX | Boston Scientific | Health Care | 2026-04-03 | 25 | -43% | 60 | 30% | +20% | +55% | open | – | +5% (0.7) | -32% (3.4) | -32% | 22 ↓ | -30% (so far) | +18% (so far) |


## no fundamentals filter

494 signals since 2010, 207 after the top-20 cut per year (the cap bound in 2015, 2016, 2018, 2020, 2022, 2023, 2025, 2026).

### Summary by year

| Year | SPY cal. year | Buys | Hit +20% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | 12m return: median / mean | 12m best | 12m worst | beat SPY (same 12m) | SPY same 12m (median) | Max gain (median / best) | Max DD (median / worst) | RSI went lower | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | +15% | 2 | 2/2 = 100% | 7.1 / 7.1 / 9.6 | 0% / 50% | +35% / +35% | +52% BAX | +18% GILD | 50% | +25% | +38% / +52% BAX | -4% / -8% GILD | 50% | 0/2 = 0% | – / – | – |
| 2011 | +2% | 10 | 10/10 = 100% | 3.3 / 4.3 / 11.7 | 50% / 90% | +37% / +30% | +68% TTC | -17% NFLX | 60% | +26% | +47% / +71% TTC | -9% / -37% ILMN | 40% | 0/10 = 0% | – / – | – |
| 2012 | +16% | 2 | 2/2 = 100% | 1.9 / 1.9 / 2.3 | 100% / 100% | +71% / +71% | +73% SGI | +69% KEX | 100% | +24% | +86% / +96% SGI | -10% / -18% SGI | 100% | 0/2 = 0% | – / – | – |
| 2013 | +32% | 1 | 1/1 = 100% | 4.1 / 4.1 / 4.1 | 0% / 100% | +24% / +24% | +24% RGLD | +24% RGLD | 100% | +22% | +37% / +37% RGLD | -26% / -26% RGLD | 100% | 0/1 = 0% | – / – | – |
| 2014 | +13% | 7 | 3/7 = 43% | 4.0 / 4.7 / 8.8 | 14% / 29% | -9% / -6% | +45% OC | -51% RRC | 29% | +3% | +18% / +64% OC | -20% / -53% RRC | 57% | 4/7 = 57% | -32% / -53% | -30% |
| 2015 | +1% | 20 | 13/20 = 65% | 6.4 / 6.3 / 11.8 | 15% / 30% | +22% / +29% | +201% OKE | -23% CMG | 65% | +13% | +26% / +206% OKE | -16% / -44% DAR | 65% | 7/20 = 35% | -32% / -44% | -10% |
| 2016 | +12% | 20 | 16/20 = 80% | 2.6 / 2.9 / 8.6 | 60% / 70% | +39% / +39% | +104% EXP | -10% TSCO | 65% | +24% | +44% / +107% EXP | -7% / -26% TSCO | 50% | 4/20 = 20% | -17% / -26% | -6% |
| 2017 | +22% | 12 | 9/12 = 75% | 4.8 / 4.3 / 9.1 | 33% / 58% | +18% / +31% | +188% DXCM | -55% PCG | 67% | +16% | +43% / +228% DXCM | -10% / -67% PCG | 50% | 3/12 = 25% | -25% / -67% | -11% |
| 2018 | -5% | 20 | 15/20 = 75% | 2.0 / 2.9 / 9.5 | 50% / 65% | +20% / +36% | +197% COKE | -18% WLK | 55% | +16% | +34% / +197% COKE | -11% / -46% VC | 40% | 5/20 = 25% | -25% / -46% | +2% |
| 2019 | +31% | 3 | 3/3 = 100% | 4.0 / 4.4 / 7.1 | 33% / 67% | +5% / +14% | +37% IDCC | +1% ULTA | 33% | +13% | +33% / +43% IDCC | -28% / -43% ULTA | 33% | 0/3 = 0% | – / – | – |
| 2020 | +18% | 20 | 19/20 = 95% | 0.2 / 1.1 / 10.3 | 90% / 90% | +90% / +103% | +223% APTV | +11% UGI | 85% | +73% | +92% / +248% APTV | -10% / -50% OKE | 30% | 1/20 = 5% | -36% / -36% | +11% |
| 2021 | +29% | 3 | 2/3 = 67% | 2.7 / 2.7 / 3.9 | 33% / 67% | -3% / -13% | +0% HAE | -37% SAM | 67% | -7% | +23% / +33% HAE | -22% / -47% SAM | 67% | 1/3 = 33% | -47% / -47% | -37% |
| 2022 | -18% | 20 | 12/20 = 60% | 2.5 / 3.8 / 10.8 | 35% / 50% | +18% / +19% | +152% WING | -52% PYPL | 65% | +0% | +35% / +161% WING | -17% / -62% META | 50% | 8/20 = 40% | -34% / -62% | -20% |
| 2023 | +26% | 20 | 15/20 = 75% | 1.6 / 3.0 / 7.8 | 50% / 60% | +29% / +34% | +139% TRU | -28% EL | 45% | +35% | +43% / +151% TRU | -7% / -38% DG | 50% | 5/20 = 25% | -12% / -38% | +2% |
| 2024 | +25% | 7 | 5/7 = 71% | 2.9 / 2.4 / 3.4 | 43% / 71% | -5% / -1% | +39% DXCM | -18% HUM | 14% | +16% | +28% / +66% LULU | -22% / -36% REGN | 71% | 2/7 = 29% | -29% / -36% | -4% |
| 2025 | +18% | 20 (8 open) | 9/20 = 45% | 2.3 / 3.2 / 10.7 | 25% / 40% | +10% / +26% | +215% PBF | -19% IT | 33% | +27% | +16% / +255% PBF | -19% / -45% IT | 65% | 4/12 = 33% | -23% / -45% | -15% |
| 2026 | +14% | 20 (20 open) | 12/20 = 60% | 1.3 / 2.3 / 6.1 | 35% / 55% | – / – | – | – | – | – | +33% / +79% CVLT | -16% / -45% PLNT | 58% | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-09-25)** |  | 179 | 135/179 = 75% | 2.3 / 3.4 / 11.8 | 46% / 62% | +25% / +36% | +223% APTV | -55% PCG | 58% | +21% | +42% / +255% PBF | -11% / -67% PCG | 50% | 44/179 = 25% | -26% / -67% | -9% |
| **All incl. open** |  | 207 (28 open) | 148/207 = 71% | 2.3 / 3.3 / 11.8 | 43% / 59% | +25% / +36% | +223% APTV | -55% PCG | 58% | +21% | +39% / +255% PBF | -12% / -67% PCG | 52% | 44/179 = 25% | -26% / -67% | -9% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months (30.44 days) from the signal week's Friday. "RSI went lower" = share of buys whose weekly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 2 buys, 2 hit +20%, SPY +15% that year, 12m median +35%, best +52%, worst +18%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GILD | Gilead Sciences | Health Care | 2010-06-04 | 23 | -40% | 135 | 0% | +27% | +51% | yes | 9.6 | +23% (10.0) | -8% (2.9) | -8% | 23 ↓ | +18% | +25% |
| 2 | BAX | Baxter International | Health Care | 2010-05-21 | 24 | -43% | 92 | 0% | +2% | +14% | yes | 4.5 | +52% (12.0) | +0% (0.6) | +0% | 27 | +52% | +25% |


#### 2011: 10 buys, 10 hit +20%, SPY +2% that year, 12m median +37%, best +68%, worst -17%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UTHR | United Therapeutics | Health Care | 2011-08-26 | 20 | -43% | 25 | 7% | +63% | +391% | yes | 4.3 | +42% (11.7) | -7% (1.2) | -7% | 23 | +38% | +23% |
| 2 | LII | Lennox International | Industrials | 2011-08-05 | 22 | -38% | 67 | 38% | +7% | +117% | yes | 6.0 | +47% (11.0) | -24% (1.6) | -24% | 17 ↓ | +36% | +19% |
| 3 | PNC | PNC Financial Services | Financials | 2011-08-19 | 23 | -51% | 152 | 27% | -8% | +67% | yes | 1.8 | +59% (8.4) | -0% (0.1) | -0% | 32 | +48% | +29% |
| 4 | GBCI | Glacier Bancorp | Financials | 2011-08-19 | 23 | -63% | 152 | – | – | +5% | yes | 2.3 | +62% (11.0) | -12% (1.5) | -12% | 27 | +56% | +29% |
| 5 | DLB | Dolby | Information Technology | 2011-08-05 | 24 | -56% | 65 | 4% | +28% | +23% | yes | 5.6 | +46% (9.4) | -15% (1.9) | -15% | 25 | -1% | +19% |
| 6 | NFLX | Netflix | Communication Services | 2011-10-28 | 24 | -72% | 21 | 19% | +41% | +60% | yes | 2.7 | +54% (3.3) | -36% (10.9) | -24% | 22 ↓ | -17% | +12% |
| 7 | HAS | Hasbro | Consumer Discretionary | 2011-09-23 | 25 | -31% | 41 | 44% | +3% | +4% | yes | 11.7 | +20% (11.7) | -7% (3.2) | -7% | 21 ↓ | +14% | +31% |
| 8 | TRV | Travelers Companies (The) | Financials | 2011-08-26 | 25 | -25% | 16 | 10% | +1% | +13% | yes | 1.9 | +40% (11.8) | -2% (1.2) | -2% | 26 | +40% | +23% |
| 9 | TTC | Toro | Industrials | 2011-08-19 | 25 | -31% | 37 | 40% | +11% | +105% | yes | 2.5 | +71% (11.0) | -3% (1.5) | -3% | 37 | +68% | +29% |
| 10 | ILMN | Illumina, Inc. | Health Care | 2011-09-30 | 25 | -48% | 32 | 0% | +44% | +64% | yes | 3.8 | +35% (3.8) | -37% (2.4) | -37% | 18 ↓ | +18% | +30% |


#### 2012: 2 buys, 2 hit +20%, SPY +16% that year, 12m median +71%, best +73%, worst +69%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SGI | Somnigroup International | Consumer Discretionary | 2012-06-08 | 23 | -71% | 9 | 23% | +28% | +47% | yes | 1.6 | +96% (9.6) | -18% (0.6) | -18% | 22 ↓ | +73% | +27% |
| 2 | KEX | Kirby Corporation | Industrials | 2012-06-29 | 24 | -33% | 23 | 38% | +86% | +59% | yes | 2.3 | +75% (10.7) | -2% (0.4) | -2% | 24 ↓ | +69% | +21% |


#### 2013: 1 buys, 1 hit +20%, SPY +32% that year, 12m median +24%, best +24%, worst +24%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RGLD | Royal Gold | Materials | 2013-04-19 | 25 | -47% | 28 | 2% | – | +4% | yes | 4.1 | +37% (10.8) | -26% (2.2) | -26% | 24 ↓ | +24% | +22% |


#### 2014: 7 buys, 3 hit +20%, SPY +13% that year, 12m median -9%, best +45%, worst -51%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HAL | Halliburton | Energy | 2014-11-28 | 23 | -43% | 18 | 47% | +9% | +82% | **no** | – | +18% (5.0) | -20% (8.9) | -20% | 20 ↓ | -6% | +3% |
| 2 | MAT | Mattel | Consumer Discretionary | 2014-09-26 | 24 | -36% | 71 | 57% | -1% | +9% | **no** | – | +4% (2.1) | -26% (10.9) | -26% | 23 ↓ | -22% | -1% |
| 3 | KEX | Kirby Corporation | Industrials | 2014-12-19 | 24 | -35% | 21 | 50% | +13% | +12% | **no** | – | +4% (4.1) | -37% (12.0) | -37% | 22 ↓ | -37% | -1% |
| 4 | HAE | Haemonetics | Health Care | 2014-03-28 | 24 | -30% | 61 | 51% | +14% | -15% | yes | 8.8 | +41% (11.5) | -5% (1.1) | -5% | 26 | +38% | +13% |
| 5 | OC | Owens Corning | Industrials | 2014-10-10 | 24 | -37% | 86 | 35% | +2% | +371% | yes | 1.3 | +64% (10.2) | -2% (0.1) | -2% | 26 | +45% | +8% |
| 6 | RRC | Range Resources | Energy | 2014-10-03 | 25 | -30% | 24 | 9% | +20% | +271% | **no** | – | +11% (1.3) | -53% (11.9) | -53% | 22 ↓ | -51% | +1% |
| 7 | CXT | Crane NXT | Information Technology | 2014-10-10 | 25 | -25% | 31 | 71% | +9% | -2% | yes | 4.0 | +21% (4.4) | -19% (11.6) | -7% | 25 | -9% | +8% |


#### 2015: 20 buys, 13 hit +20%, SPY +1% that year, 12m median +22%, best +201%, worst -23%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | XPO | XPO, Inc. | Industrials | 2015-09-25 | 20 | -54% | 27 | 61% | +160% | – | yes | 0.4 | +58% (10.9) | -17% (3.8) | -8% | 30 | +50% | +14% |
| 2 | BDC | Belden Inc. | Information Technology | 2015-07-31 | 21 | -38% | 16 | 80% | +16% | -72% | yes | 11.6 | +28% (11.7) | -37% (6.3) | -37% | 15 ↓ | +24% | +5% |
| 3 | PSKY | Paramount Skydance Corporation | Communication Services | 2015-08-21 | 21 | -34% | 76 | – | – | – | yes | 6.8 | +30% (10.7) | -14% (1.2) | -14% | 20 ↓ | +16% | +13% |
| 4 | TKR | Timken | Industrials | 2015-07-24 | 22 | -36% | 55 | 76% | -29% | -9% | **no** | – | +18% (9.0) | -25% (5.9) | -25% | 19 ↓ | +1% | +7% |
| 5 | LIN | Linde plc | Materials | 2015-09-04 | 22 | -25% | 85 | – | – | – | yes | 11.4 | +24% (12.0) | -5% (4.7) | -5% | 27 | +24% | +16% |
| 6 | NDSN | Nordson Corporation | Industrials | 2015-08-21 | 22 | -26% | 131 | 59% | +7% | +11% | yes | 6.4 | +50% (12.0) | -14% (5.0) | -14% | 31 | +50% | +13% |
| 7 | OKE | Oneok | Energy | 2015-12-11 | 22 | -71% | 66 | 66% | -32% | +1% | yes | 0.7 | +206% (11.9) | -7% (0.2) | -7% | 21 ↓ | +201% | +15% |
| 8 | WCC | WESCO International | Industrials | 2015-08-21 | 23 | -44% | 83 | 26% | +2% | +4% | **no** | – | +16% (9.6) | -32% (5.0) | -32% | 22 ↓ | +11% | +13% |
| 9 | RTX | RTX Corporation | Industrials | 2015-08-21 | 23 | -25% | 107 | 52% | +3% | +12% | yes | 11.8 | +21% (11.9) | -8% (5.7) | -8% | 21 ↓ | +20% | +13% |
| 10 | R | Ryder | Industrials | 2015-12-11 | 23 | -44% | 72 | 68% | -1% | -11% | yes | 4.3 | +55% (11.9) | -15% (1.3) | -15% | 21 ↓ | +50% | +15% |
| 11 | DAR | Darling Ingredients | Consumer Staples | 2015-03-13 | 23 | -41% | 72 | 58% | +93% | -85% | **no** | – | +14% (2.7) | -44% (11.0) | -44% | 23 ↓ | -13% | +1% |
| 12 | CBT | Cabot Corp | Materials | 2015-07-24 | 23 | -43% | 68 | 32% | -7% | -31% | yes | 3.8 | +47% (9.1) | -11% (2.2) | -11% | 23 ↓ | +45% | +7% |
| 13 | PII | Polaris | Consumer Discretionary | 2015-12-04 | 23 | -38% | 99 | 22% | +14% | +13% | **no** | – | +3% (4.7) | -30% (1.8) | -30% | 17 ↓ | -10% | +7% |
| 14 | WYNN | Wynn Resorts | Consumer Discretionary | 2015-09-04 | 23 | -71% | 78 | 22% | -20% | -62% | yes | 5.9 | +46% (10.8) | -29% (0.9) | -29% | 19 ↓ | +29% | +16% |
| 15 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2015-11-20 | 23 | -29% | 15 | 36% | – | +31% | **no** | – | +8% (0.2) | -33% (11.4) | -33% | 19 ↓ | -23% | +7% |
| 16 | AMG | Affiliated Managers Group | Financials | 2015-09-04 | 24 | -25% | 86 | 42% | – | +39% | **no** | – | +9% (2.1) | -32% (5.3) | -32% | 24 | -19% | +16% |
| 17 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2015-12-18 | 24 | -41% | 39 | 3% | +9% | +13% | yes | 2.3 | +77% (11.7) | -4% (0.9) | -4% | 25 | +62% | +15% |
| 18 | VTR | Ventas | Real Estate | 2015-08-28 | 24 | -41% | 119 | 36% | +14% | -2% | yes | 8.2 | +42% (11.1) | -12% (5.5) | -12% | 21 ↓ | +34% | +11% |
| 19 | AVNT | Avient | Materials | 2015-09-04 | 24 | -28% | 65 | 75% | -7% | -21% | yes | 7.8 | +25% (10.3) | -21% (5.2) | -21% | 24 | +14% | +16% |
| 20 | WMT | Walmart | Consumer Staples | 2015-09-04 | 24 | -30% | 40 | 6% | +2% | +2% | **no** | – | +20% (11.5) | -12% (2.3) | -12% | 24 | +17% | +16% |


#### 2016: 20 buys, 16 hit +20%, SPY +12% that year, 12m median +39%, best +104%, worst -10%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MCK | McKesson Corporation | Health Care | 2016-10-28 | 19 | -49% | 126 | 46% | +5% | +38% | yes | 2.7 | +36% (8.6) | +2% (0.1) | +2% | 26 | +10% | +24% |
| 2 | VC | Visteon | Consumer Discretionary | 2016-01-29 | 20 | -45% | 10 | 90% | -61% | +619% | yes | 2.0 | +37% (11.9) | -10% (0.4) | -10% | 18 ↓ | +33% | +21% |
| 3 | AXP | American Express | Financials | 2016-01-22 | 21 | -43% | 105 | 14% | – | +0% | yes | 3.0 | +43% (11.9) | -7% (0.7) | -7% | 20 ↓ | +41% | +22% |
| 4 | TSCO | Tractor Supply | Consumer Discretionary | 2016-09-09 | 22 | -30% | 80 | 54% | +7% | +8% | **no** | – | +15% (3.4) | -26% (10.1) | -26% | 19 ↓ | -10% | +18% |
| 5 | WSM | Williams-Sonoma, Inc. | Consumer Discretionary | 2016-01-08 | 23 | -39% | 47 | 26% | +7% | +10% | **no** | – | +14% (3.6) | -13% (9.8) | -13% | 20 ↓ | -8% | +21% |
| 6 | CVS | CVS Health | Health Care | 2016-11-11 | 23 | -34% | 67 | 35% | +15% | -2% | **no** | – | +13% (10.2) | -9% (11.8) | -9% | 22 ↓ | -3% | +22% |
| 7 | CAR | Avis Budget Group | Industrials | 2016-01-15 | 23 | -64% | 73 | – | – | +83% | yes | 4.5 | +63% (10.7) | -13% (1.3) | -13% | 25 | +45% | +23% |
| 8 | CAH | Cardinal Health | Health Care | 2016-11-04 | 23 | -29% | 85 | – | – | – | yes | 3.1 | +29% (4.3) | -4% (11.9) | +0% | 31 | -3% | +26% |
| 9 | EL | Estée Lauder Companies (The) | Consumer Staples | 2016-11-04 | 24 | -19% | 76 | 80% | +4% | +5% | yes | 6.1 | +57% (11.9) | -4% (0.9) | -4% | 22 ↓ | +56% | +26% |
| 10 | MORN | Morningstar, Inc. | Financials | 2016-11-04 | 24 | -24% | 65 | 7% | +1% | +3% | yes | 8.6 | +31% (11.7) | -0% (0.1) | -0% | 33 | +29% | +26% |
| 11 | WEX | WEX Inc. | Financials | 2016-02-12 | 24 | -50% | 77 | 25% | +8% | -32% | yes | 0.7 | +100% (12.0) | +4% (0.1) | +4% | 28 | +100% | +27% |
| 12 | LYV | Live Nation Entertainment | Communication Services | 2016-02-12 | 24 | -35% | 36 | 70% | +2% | -2100% | yes | 2.8 | +49% (12.0) | +1% (0.2) | +1% | 29 | +49% | +27% |
| 13 | AMP | Ameriprise Financial | Financials | 2016-02-05 | 24 | -40% | 108 | 45% | +0% | +15% | yes | 2.5 | +51% (12.0) | -7% (0.2) | -7% | 22 ↓ | +51% | +25% |
| 14 | SEIC | SEI Investments Company | Financials | 2016-02-05 | 24 | -35% | 25 | 49% | +6% | +9% | yes | 1.8 | +45% (11.3) | -6% (0.2) | -6% | 25 | +37% | +25% |
| 15 | CFR | Frost Bank | Financials | 2016-01-22 | 24 | -46% | 126 | 14% | +8% | +8% | yes | 1.3 | +106% (11.7) | -5% (0.1) | -5% | 30 | +104% | +22% |
| 16 | JLL | Jones Lang LaSalle | Real Estate | 2016-02-05 | 24 | -38% | 46 | 33% | +12% | +28% | **no** | – | +12% (2.7) | -20% (8.9) | -20% | 21 ↓ | -4% | +25% |
| 17 | PAG | Penske Automotive Group | Consumer Discretionary | 2016-01-15 | 24 | -38% | 119 | 21% | +8% | +20% | yes | 1.7 | +72% (10.8) | -11% (0.6) | -11% | 22 ↓ | +61% | +23% |
| 18 | AN | AutoNation | Consumer Discretionary | 2016-01-29 | 25 | -36% | 81 | 10% | +11% | +18% | yes | 0.9 | +23% (6.0) | -7% (9.3) | +0% | 31 | +21% | +21% |
| 19 | MOG-A | Moog Inc. | Industrials | 2016-02-05 | 25 | -49% | 87 | 42% | -5% | -5% | yes | 2.8 | +78% (9.6) | -3% (0.2) | -3% | 24 ↓ | +68% | +25% |
| 20 | EXP | Eagle Materials | Materials | 2016-01-22 | 25 | -53% | 70 | 21% | +16% | +16% | yes | 1.1 | +107% (10.6) | -5% (0.2) | -5% | 33 | +104% | +22% |


#### 2017: 12 buys, 9 hit +20%, SPY +22% that year, 12m median +18%, best +188%, worst -55%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2017-07-07 | 17 | -41% | 88 | 37% | +6% | +13% | yes | 0.8 | +66% (11.5) | +0% (0.1) | +0% | 24 | +64% | +16% |
| 2 | EFX | Equifax | Industrials | 2017-09-15 | 20 | -37% | 60 | 86% | – | +23% | yes | 0.6 | +49% (12.0) | +2% (0.1) | +2% | 32 | +49% | +18% |
| 3 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2017-08-18 | 20 | -57% | 47 | 3% | +10% | -8% | yes | 4.8 | +45% (9.4) | -9% (2.5) | -9% | 20 ↓ | +41% | +20% |
| 4 | EIX | Edison International | Utilities | 2017-12-22 | 22 | -22% | 39 | 86% | +7% | +56% | **no** | – | +12% (10.1) | -25% (10.8) | -25% | 19 ↓ | -11% | -8% |
| 5 | PCG | PG&E Corporation | Utilities | 2017-11-17 | 23 | -25% | 34 | 61% | +7% | +168% | **no** | – | +2% (0.4) | -67% (11.9) | -67% | 12 ↓ | -55% | +8% |
| 6 | KR | Kroger | Consumer Staples | 2017-06-16 | 23 | -48% | 116 | 56% | +5% | -0% | yes | 5.6 | +42% (7.5) | -10% (3.3) | -10% | 25 | +19% | +16% |
| 7 | ULTA | Ulta Beauty | Consumer Discretionary | 2017-08-25 | 24 | -33% | 12 | 41% | +23% | +32% | yes | 8.7 | +22% (10.6) | -10% (1.6) | -10% | 27 | +14% | +20% |
| 8 | AZO | AutoZone | Consumer Discretionary | 2017-06-16 | 24 | -28% | 84 | 26% | +3% | +12% | yes | 5.7 | +34% (7.4) | -17% (0.9) | -17% | 16 ↓ | +17% | +16% |
| 9 | BBWI | Bath & Body Works, Inc. | Consumer Discretionary | 2017-08-18 | 24 | -64% | 123 | 39% | +1% | – | yes | 2.1 | +76% (4.3) | -11% (11.3) | -0% | 25 | -6% | +20% |
| 10 | DXCM | Dexcom | Health Care | 2017-10-20 | 25 | -57% | 109 | 30% | +30% | – | yes | 0.9 | +228% (10.7) | -1% (0.2) | -1% | 25 ↓ | +188% | +9% |
| 11 | BKH | Black Hills Corporation | Utilities | 2017-11-10 | 25 | -20% | 23 | 81% | +24% | +852% | **no** | – | +14% (7.8) | -11% (3.0) | -11% | 27 | +13% | +10% |
| 12 | TGT | Target Corporation | Consumer Staples | 2017-03-17 | 25 | -37% | 101 | 7% | -5% | – | yes | 9.1 | +49% (10.2) | -7% (3.8) | -7% | 24 ↓ | +36% | +18% |


#### 2018: 20 buys, 15 hit +20%, SPY -5% that year, 12m median +20%, best +197%, worst -18%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KDP | Keurig Dr Pepper | Consumer Staples | 2018-07-13 | 10 | -81% | 23 | 96% | +5% | +28% | yes | 9.5 | +30% (11.2) | -8% (2.8) | -8% | 10 | +21% | +10% |
| 2 | OZK | Bank OZK | Financials | 2018-10-19 | 16 | -55% | 85 | – | – | – | yes | 3.0 | +36% (6.5) | -17% (2.0) | -17% | 16 ↓ | +17% | +10% |
| 3 | SEIC | SEI Investments Company | Financials | 2018-12-21 | 20 | -44% | 47 | 48% | +10% | +31% | yes | 1.8 | +56% (11.9) | -2% (0.1) | -2% | 27 | +54% | +36% |
| 4 | FBIN | Fortune Brands Innovations | Industrials | 2018-10-26 | 21 | -44% | 67 | 12% | +5% | +8% | yes | 5.3 | +49% (11.9) | -13% (1.9) | -13% | 25 | +48% | +16% |
| 5 | XPO | XPO, Inc. | Industrials | 2018-12-14 | 22 | -56% | 39 | 44% | +15% | +205% | yes | 0.9 | +66% (10.9) | -10% (2.8) | -1% | 22 | +62% | +24% |
| 6 | STZ | Constellation Brands | Consumer Staples | 2018-12-21 | 22 | -31% | 51 | – | +6% | – | yes | 3.9 | +32% (4.2) | -7% (0.6) | -7% | 23 | +18% | +36% |
| 7 | SSB | South State Bank | Financials | 2018-10-26 | 22 | -33% | 98 | 86% | – | -11% | yes | 6.1 | +28% (9.1) | -10% (1.9) | -10% | 27 | +25% | +16% |
| 8 | WLK | Westlake Corporation | Materials | 2018-10-19 | 22 | -38% | 32 | 28% | +23% | +245% | **no** | – | +6% (3.9) | -26% (10.2) | -26% | 19 ↓ | -18% | +10% |
| 9 | MLM | Martin Marietta Materials | Materials | 2018-10-19 | 22 | -34% | 101 | 38% | +3% | +65% | yes | 1.3 | +71% (11.4) | -5% (0.3) | -5% | 21 ↓ | +66% | +10% |
| 10 | EVR | Evercore | Financials | 2018-12-21 | 22 | -44% | 46 | 32% | +14% | +1% | yes | 0.7 | +49% (4.2) | -2% (0.1) | -2% | 30 | +19% | +36% |
| 11 | COKE | Coca-Cola Consolidated | Consumer Staples | 2018-05-11 | 23 | -48% | 41 | 52% | +37% | +92% | yes | 3.0 | +197% (12.0) | -3% (0.2) | -3% | 22 ↓ | +197% | +8% |
| 12 | VC | Visteon | Consumer Discretionary | 2018-10-12 | 23 | -42% | 39 | 64% | -1% | +30% | **no** | – | +10% (4.3) | -46% (7.6) | -46% | 19 ↓ | +1% | +10% |
| 13 | STT | State Street Corporation | Financials | 2018-10-26 | 23 | -42% | 39 | 50% | +10% | +12% | **no** | – | +12% (1.1) | -25% (9.6) | -25% | 25 | +2% | +16% |
| 14 | BLDR | Builders FirstSource | Industrials | 2018-10-19 | 23 | -48% | 38 | 8% | +12% | -57% | yes | 0.5 | +89% (12.0) | -16% (2.2) | -2% | 23 ↓ | +89% | +10% |
| 15 | AVNT | Avient | Materials | 2018-10-26 | 23 | -35% | 47 | 78% | -1% | – | **no** | – | +16% (10.6) | -18% (7.0) | -18% | 24 | +7% | +16% |
| 16 | FDX | FedEx | Industrials | 2018-12-21 | 23 | -42% | 48 | 58% | +10% | +67% | yes | 3.4 | +26% (3.9) | -11% (9.6) | -3% | 24 | -5% | +36% |
| 17 | MCHP | Microchip Technology | Information Technology | 2018-10-26 | 23 | -40% | 40 | 63% | +18% | -76% | yes | 0.7 | +63% (6.2) | -0% (0.1) | -0% | 35 | +53% | +16% |
| 18 | STLD | Steel Dynamics | Materials | 2018-12-21 | 23 | -42% | 44 | 28% | +23% | +151% | yes | 1.3 | +31% (2.1) | -15% (5.3) | -4% | 23 ↓ | +19% | +36% |
| 19 | AOS | A. O. Smith | Industrials | 2018-10-12 | 23 | -30% | 37 | 59% | +10% | -4% | **no** | – | +19% (6.2) | -14% (7.6) | -14% | 19 ↓ | +2% | +10% |
| 20 | BC | Brunswick | Consumer Discretionary | 2018-12-21 | 24 | -38% | 27 | 76% | +1% | -61% | yes | 2.0 | +45% (12.0) | -3% (5.3) | -1% | 31 | +45% | +36% |


#### 2019: 3 buys, 3 hit +20%, SPY +31% that year, 12m median +5%, best +37%, worst +1%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ULTA | Ulta Beauty | Consumer Discretionary | 2019-09-13 | 24 | -38% | 43 | 4% | +12% | +23% | yes | 4.0 | +33% (5.3) | -43% (6.1) | -1% | 25 | +1% | +13% |
| 2 | IDCC | InterDigital | Information Technology | 2019-08-23 | 25 | -54% | 131 | 98% | -45% | -82% | yes | 2.0 | +43% (11.6) | -28% (6.8) | +1% | 28 | +37% | +22% |
| 3 | INGR | Ingredion | Consumer Staples | 2019-05-24 | 25 | -46% | 69 | 60% | +0% | -13% | yes | 7.1 | +29% (8.6) | -21% (9.8) | -6% | 23 ↓ | +5% | +7% |


#### 2020: 20 buys, 19 hit +20%, SPY +18% that year, 12m median +90%, best +223%, worst +11%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | OKE | Oneok | Energy | 2020-03-13 | 14 | -61% | 87 | 91% | -19% | +10% | yes | 2.2 | +89% (12.0) | -50% (0.2) | -50% | 12 ↓ | +89% | +49% |
| 2 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2020-03-20 | 15 | -42% | 79 | 63% | +6% | +8% | yes | 0.2 | +88% (9.8) | -1% (0.1) | -1% | 31 | +85% | +73% |
| 3 | LAMR | Lamar Advertising Company | Real Estate | 2020-03-20 | 16 | -59% | 5 | 57% | +8% | +20% | yes | 0.2 | +154% (11.9) | -19% (0.1) | -19% | 22 | +140% | +73% |
| 4 | SYY | Sysco | Consumer Staples | 2020-03-13 | 16 | -45% | 11 | 70% | +1% | +24% | yes | 1.5 | +83% (12.0) | -34% (0.2) | -34% | 12 ↓ | +83% | +49% |
| 5 | PAYX | Paychex | Industrials | 2020-03-20 | 16 | -43% | 40 | 85% | +15% | +7% | yes | 0.2 | +95% (11.9) | -3% (0.1) | -3% | 29 | +91% | +73% |
| 6 | DAL | Delta Air Lines | Industrials | 2020-03-20 | 16 | -66% | 113 | 18% | +5% | +25% | yes | 0.1 | +139% (11.8) | -10% (1.8) | +4% | 25 | +130% | +73% |
| 7 | BA | Boeing | Industrials | 2020-03-13 | 17 | -62% | 54 | 91% | -24% | -107% | yes | 2.8 | +58% (12.0) | -44% (0.2) | -44% | 12 ↓ | +58% | +49% |
| 8 | UHS | Universal Health Services | Health Care | 2020-03-20 | 18 | -52% | 34 | 46% | +6% | +10% | yes | 0.2 | +89% (9.6) | -5% (0.1) | -5% | 28 | +83% | +73% |
| 9 | PRU | Prudential Financial | Financials | 2020-03-13 | 18 | -58% | 111 | 7% | +3% | +6% | yes | 1.5 | +89% (12.0) | -26% (0.3) | -26% | 15 ↓ | +89% | +49% |
| 10 | SNA | Snap-on | Industrials | 2020-03-20 | 18 | -47% | 78 | 30% | -9% | +5% | yes | 0.7 | +132% (11.9) | -4% (0.5) | -4% | 22 | +132% | +73% |
| 11 | BCO | Brink's | Industrials | 2020-03-20 | 18 | -54% | 34 | 82% | +6% | – | yes | 0.2 | +87% (11.8) | -23% (1.8) | -7% | 23 | +86% | +73% |
| 12 | SWK | Stanley Black & Decker | Industrials | 2020-03-20 | 18 | -55% | 113 | 70% | +3% | +59% | yes | 0.2 | +153% (11.9) | -9% (0.1) | -9% | 30 | +152% | +73% |
| 13 | ALV | Autoliv | Consumer Discretionary | 2020-03-20 | 19 | -65% | 111 | 27% | -2% | +143% | yes | 0.2 | +147% (11.9) | +1% (0.1) | +1% | 25 | +133% | +73% |
| 14 | CBT | Cabot Corp | Materials | 2020-03-20 | 19 | -69% | 112 | 21% | -3% | +72% | yes | 0.2 | +165% (11.9) | +4% (0.1) | +4% | 28 | +158% | +73% |
| 15 | G | Genpact | Industrials | 2020-03-20 | 19 | -44% | 7 | 57% | +18% | +12% | yes | 0.7 | +75% (10.7) | -6% (0.1) | -6% | 27 | +72% | +73% |
| 16 | THG | Hanover Insurance | Financials | 2020-03-13 | 19 | -29% | 31 | 65% | +9% | +15% | yes | 10.3 | +28% (12.0) | -19% (0.3) | -19% | 13 ↓ | +28% | +49% |
| 17 | APTV | Aptiv | Consumer Discretionary | 2020-03-20 | 19 | -56% | 111 | 74% | -1% | -4% | yes | 0.2 | +248% (11.1) | -4% (0.5) | +3% | 23 | +223% | +73% |
| 18 | EME | Emcor | Industrials | 2020-03-20 | 19 | -47% | 37 | 43% | +13% | +19% | yes | 0.2 | +134% (11.7) | +3% (0.1) | +3% | 30 | +129% | +73% |
| 19 | UGI | UGI Corp | Utilities | 2020-02-28 | 19 | -39% | 80 | 87% | -4% | -65% | **no** | – | +16% (11.7) | -36% (0.8) | -36% | 12 ↓ | +11% | +31% |
| 20 | LUV | Southwest Airlines | Industrials | 2020-03-20 | 19 | -52% | 141 | 27% | +2% | -0% | yes | 0.2 | +94% (11.8) | -25% (1.8) | +6% | 25 | +91% | +73% |


#### 2021: 3 buys, 2 hit +20%, SPY +29% that year, 12m median -3%, best +0%, worst -37%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NEU | NewMarket Corporation | Materials | 2021-06-18 | 25 | -39% | 83 | 42% | -9% | -6% | yes | 3.9 | +23% (4.2) | -3% (11.9) | -2% | 31 | -3% | -11% |
| 2 | SAM | Boston Beer Company | Consumer Staples | 2021-09-10 | 25 | -60% | 20 | 53% | +44% | +72% | **no** | – | +0% (0.9) | -47% (9.2) | -47% | 24 ↓ | -37% | -7% |
| 3 | HAE | Haemonetics | Health Care | 2021-05-14 | 25 | -61% | 91 | 46% | -12% | +39% | yes | 1.5 | +33% (5.7) | -22% (8.5) | -2% | 25 ↓ | +0% | -2% |


#### 2022: 20 buys, 12 hit +20%, SPY -18% that year, 12m median +18%, best +152%, worst -52%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | Communication Services | 2022-04-22 | 20 | -69% | 25 | 34% | +19% | +85% | yes | 5.9 | +71% (9.1) | -23% (0.6) | -23% | 19 ↓ | +52% | -2% |
| 2 | CHTR | Charter Communications | Communication Services | 2022-04-29 | 22 | -48% | 34 | 26% | +7% | +59% | **no** | – | +19% (0.9) | -29% (5.1) | -29% | 25 | -14% | +3% |
| 3 | DOV | Dover Corporation | Industrials | 2022-06-17 | 22 | -36% | 40 | 77% | +17% | +64% | yes | 2.0 | +37% (7.6) | -0% (3.4) | +1% | 28 | +28% | +22% |
| 4 | RH | RH | Consumer Discretionary | 2022-03-11 | 23 | -56% | 45 | 45% | +36% | +170% | **no** | – | +19% (0.6) | -35% (3.6) | -35% | 27 | -20% | -7% |
| 5 | SWK | Stanley Black & Decker | Industrials | 2022-04-29 | 23 | -47% | 50 | 67% | +7% | +31% | **no** | – | +9% (0.2) | -39% (6.2) | -39% | 21 ↓ | -26% | +3% |
| 6 | ROK | Rockwell Automation | Industrials | 2022-05-13 | 23 | -43% | 25 | 92% | +17% | -37% | yes | 2.5 | +52% (9.8) | -6% (1.1) | -6% | 23 ↓ | +36% | +4% |
| 7 | DECK | Deckers Brands | Consumer Discretionary | 2022-03-04 | 23 | -46% | 30 | 64% | +26% | +16% | yes | 4.5 | +74% (12.0) | -8% (2.5) | -8% | 28 | +74% | -5% |
| 8 | WING | Wingstop | Consumer Discretionary | 2022-05-06 | 23 | -55% | 88 | 29% | +14% | +49% | yes | 2.4 | +161% (11.9) | -18% (0.6) | -18% | 21 ↓ | +152% | +2% |
| 9 | ALGN | Align Technology | Health Care | 2022-06-17 | 23 | -68% | 38 | 22% | +43% | +56% | yes | 1.1 | +55% (10.2) | -26% (4.8) | -2% | 28 | +41% | +22% |
| 10 | ECL | Ecolab | Materials | 2022-03-11 | 23 | -34% | 143 | 89% | +8% | – | **no** | – | +16% (0.9) | -16% (7.8) | -16% | 30 | +1% | -7% |
| 11 | TROW | T. Rowe Price | Financials | 2022-01-28 | 24 | -33% | 21 | 59% | +25% | +49% | **no** | – | +5% (2.2) | -33% (8.4) | -33% | 21 ↓ | -19% | -7% |
| 12 | PNR | Pentair | Industrials | 2022-06-17 | 24 | -45% | 43 | 34% | +23% | +30% | yes | 7.5 | +42% (11.9) | -10% (4.1) | -10% | 31 | +41% | +22% |
| 13 | CSGP | CoStar Group | Real Estate | 2022-03-11 | 24 | -45% | 84 | 32% | +17% | -1% | yes | 0.4 | +52% (8.0) | -2% (2.0) | +1% | 35 | +21% | -7% |
| 14 | PYPL | PayPal | Financials | 2022-01-21 | 24 | -47% | 48 | 70% | +21% | +57% | **no** | – | +7% (0.4) | -59% (11.2) | -59% | 15 ↓ | -52% | -8% |
| 15 | META | Meta Platforms | Communication Services | 2022-02-04 | 24 | -38% | 28 | 7% | +42% | +39% | **no** | – | -1% (1.9) | -62% (8.9) | -62% | 19 ↓ | -21% | -7% |
| 16 | WELL | Welltower | Real Estate | 2022-10-07 | 24 | -41% | 26 | 39% | +24% | -37% | yes | 1.1 | +50% (11.4) | -2% (0.1) | -2% | 23 ↓ | +44% | +20% |
| 17 | DLB | Dolby | Information Technology | 2022-03-11 | 24 | -33% | 48 | 82% | -1% | -21% | yes | 10.8 | +24% (10.8) | -10% (7.0) | -10% | 33 | +15% | -7% |
| 18 | ARE | Alexandria Real Estate Equities | Real Estate | 2022-06-17 | 24 | -41% | 24 | 19% | +17% | -52% | yes | 1.3 | +33% (7.6) | -13% (11.2) | -0% | 31 | -9% | +22% |
| 19 | MMS | Maximus Inc. | Industrials | 2022-06-10 | 24 | -38% | 59 | 27% | +25% | -9% | yes | 5.7 | +43% (11.9) | -7% (4.1) | -7% | 23 ↓ | +43% | +12% |
| 20 | FBIN | Fortune Brands Innovations | Industrials | 2022-04-15 | 24 | -39% | 49 | 9% | +26% | +41% | **no** | – | +14% (9.6) | -23% (6.2) | -23% | 23 ↓ | +0% | -4% |


#### 2023: 20 buys, 15 hit +20%, SPY +26% that year, 12m median +29%, best +139%, worst -28%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TRU | TransUnion | Industrials | 2023-10-27 | 20 | -65% | 111 | 21% | +10% | -82% | yes | 0.4 | +151% (11.9) | -1% (0.1) | -1% | 30 | +139% | +43% |
| 2 | BMY | Bristol Myers Squibb | Health Care | 2023-10-27 | 21 | -37% | 70 | 35% | -4% | +25% | **no** | – | +11% (11.3) | -20% (8.2) | -20% | 24 | +7% | +43% |
| 3 | VMI | Valmont Industries | Industrials | 2023-10-27 | 21 | -47% | 47 | 48% | +10% | +28% | yes | 1.6 | +74% (11.9) | +2% (0.1) | +2% | 29 | +70% | +43% |
| 4 | DG | Dollar General | Consumer Staples | 2023-06-02 | 21 | -37% | 137 | 63% | +11% | +9% | **no** | – | +4% (0.7) | -38% (4.3) | -38% | 16 ↓ | -16% | +25% |
| 5 | IRT | Independence Realty Trust | Real Estate | 2023-10-27 | 22 | -57% | 95 | 52% | +46% | -52% | yes | 1.5 | +78% (10.9) | -1% (0.1) | -1% | 34 | +68% | +43% |
| 6 | CCI | Crown Castle | Real Estate | 2023-09-22 | 23 | -56% | 114 | 7% | +6% | +8% | yes | 2.2 | +38% (11.8) | -7% (0.9) | -7% | 22 ↓ | +33% | +34% |
| 7 | SJM | J.M. Smucker Company (The) | Consumer Staples | 2023-09-29 | 23 | -25% | 38 | 99% | +6% | -102% | **no** | – | +10% (4.1) | -12% (1.5) | -12% | 17 ↓ | +2% | +35% |
| 8 | EL | Estée Lauder Companies (The) | Consumer Staples | 2023-10-27 | 24 | -67% | 112 | 72% | -10% | -57% | yes | 1.7 | +28% (4.5) | -31% (10.5) | -16% | 20 ↓ | -28% | +43% |
| 9 | UMBF | UMB Financial Corp. | Financials | 2023-03-17 | 24 | -48% | 96 | 40% | – | +22% | yes | 4.1 | +48% (9.4) | -7% (1.6) | -7% | 24 | +39% | +33% |
| 10 | NEE | NextEra Energy | Utilities | 2023-09-29 | 24 | -39% | 91 | 56% | +14% | +212% | yes | 7.1 | +53% (11.6) | -14% (0.3) | -14% | 19 ↓ | +52% | +35% |
| 11 | CPT | Camden Property Trust | Real Estate | 2023-10-27 | 24 | -53% | 95 | 63% | -71% | -76% | yes | 1.6 | +56% (10.9) | -0% (0.1) | -0% | 33 | +46% | +43% |
| 12 | TGT | Target Corporation | Consumer Staples | 2023-10-06 | 24 | -61% | 112 | 47% | +0% | -40% | yes | 1.3 | +72% (5.8) | +1% (0.1) | +1% | 30 | +50% | +35% |
| 13 | HSY | Hershey Company (The) | Consumer Staples | 2023-10-13 | 24 | -31% | 23 | 54% | +12% | – | **no** | – | +11% (7.1) | -5% (2.2) | -5% | 22 ↓ | +0% | +36% |
| 14 | CBSH | Commerce Bancshares | Financials | 2023-05-12 | 24 | -38% | 112 | 52% | – | -11% | yes | 7.1 | +26% (11.9) | -10% (5.7) | -10% | 24 ↓ | +25% | +28% |
| 15 | UPS | United Parcel Service | Industrials | 2023-10-27 | 24 | -42% | 128 | 18% | -4% | -7% | yes | 1.6 | +22% (1.6) | -5% (9.4) | +3% | 31 | +7% | +43% |
| 16 | RMD | ResMed| | Health Care | 2023-09-08 | 24 | -51% | 104 | 51% | +18% | +15% | yes | 4.0 | +67% (11.7) | -9% (1.6) | -9% | 21 ↓ | +67% | +23% |
| 17 | COLB | Columbia Banking System | Financials | 2023-05-12 | 24 | -64% | 113 | 13% | +3% | +15% | yes | 0.7 | +59% (7.1) | +1% (11.2) | +7% | 34 | +18% | +28% |
| 18 | AIZ | Assurant | Financials | 2023-03-17 | 24 | -46% | 47 | 61% | +0% | -78% | yes | 1.5 | +77% (11.4) | +6% (0.1) | +6% | 34 | +76% | +33% |
| 19 | ORA | Ormat Technologies | Utilities | 2023-10-20 | 24 | -48% | 140 | 71% | +8% | +36% | **no** | – | +19% (11.9) | -11% (0.8) | -11% | 19 ↓ | +19% | +41% |
| 20 | GBCI | Glacier Bancorp | Financials | 2023-04-21 | 24 | -47% | 110 | 48% | +27% | -4% | yes | 7.8 | +26% (7.8) | -23% (0.7) | -23% | 17 ↓ | +8% | +22% |


#### 2024: 7 buys, 5 hit +20%, SPY +25% that year, 12m median -5%, best +39%, worst -18%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DXCM | Dexcom | Health Care | 2024-07-26 | 19 | -61% | 140 | 19% | +26% | +117% | yes | 0.8 | +42% (7.0) | -7% (8.3) | +5% | 25 | +39% | +18% |
| 2 | ADM | Archer Daniels Midland | Consumer Staples | 2024-01-26 | 20 | -47% | 92 | 42% | -2% | -1% | yes | 1.8 | +28% (5.7) | -2% (10.8) | +2% | 26 | +1% | +26% |
| 3 | LULU | Lululemon Athletica | Consumer Discretionary | 2024-07-26 | 23 | -51% | 30 | 9% | +16% | +67% | yes | 3.1 | +66% (6.2) | -14% (11.9) | -8% | 21 ↓ | -13% | +18% |
| 4 | ELV | Elevance Health | Health Care | 2024-12-20 | 24 | -35% | 141 | 55% | +3% | +9% | yes | 3.4 | +24% (3.4) | -24% (7.4) | -0% | 21 ↓ | -5% | +16% |
| 5 | REGN | Regeneron Pharmaceuticals | Health Care | 2024-11-15 | 24 | -38% | 11 | 42% | +6% | -0% | **no** | – | +4% (0.8) | -36% (6.6) | -36% | 23 ↓ | -8% | +16% |
| 6 | HUM | Humana | Health Care | 2024-04-05 | 24 | -45% | 74 | 46% | +15% | -9% | yes | 2.9 | +30% (3.8) | -25% (8.4) | -4% | 24 ↓ | -18% | -1% |
| 7 | MRK | Merck & Co. | Health Care | 2024-11-15 | 25 | -28% | 33 | 66% | +7% | +343% | **no** | – | +8% (0.8) | -22% (5.9) | -22% | 25 ↓ | +0% | +16% |


#### 2025: 20 buys, 9 hit +20%, SPY +18% that year, 12m median +10%, best +215%, worst -19%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FISV | Fiserv | Financials | 2025-10-31 | 15 | -72% | 36 | 6% | +5% | +25% | open | – | +5% (2.3) | -31% (10.7) | -31% | 14 ↓ | -30% (so far) | +14% (so far) |
| 2 | IT | Gartner | Information Technology | 2025-08-08 | 16 | -61% | 42 | 42% | +6% | +59% | **no** | – | +15% (1.6) | -45% (10.4) | -45% | 19 | -19% | +23% |
| 3 | STZ | Constellation Brands | Consumer Staples | 2025-01-10 | 19 | -34% | 76 | – | +4% | – | **no** | – | +9% (4.1) | -28% (9.9) | -28% | 17 ↓ | -17% | +21% |
| 4 | PBF | PBF Energy | Energy | 2025-04-04 | 21 | -76% | 52 | 29% | -14% | -128% | yes | 1.0 | +255% (11.7) | -4% (0.1) | -4% | 23 | +215% | +31% |
| 5 | CHDN | Churchill Downs Inc. | Consumer Discretionary | 2025-04-04 | 22 | -32% | 100 | 36% | +11% | – | **no** | – | +15% (8.4) | -18% (11.2) | -18% | 15 ↓ | -13% | +31% |
| 6 | EIX | Edison International | Utilities | 2025-01-24 | 23 | -34% | 20 | 64% | +4% | +7% | **no** | – | +13% (11.7) | -17% (4.6) | -17% | 18 ↓ | +10% | +15% |
| 7 | INGR | Ingredion | Consumer Staples | 2025-11-07 | 23 | -30% | 52 | 28% | -5% | +5% | open | – | +12% (2.9) | -11% (7.7) | -11% | 22 ↓ | -9% (so far) | +16% (so far) |
| 8 | SFM | Sprouts Farmers Market | Consumer Staples | 2025-10-31 | 23 | -57% | 37 | 44% | +17% | +49% | open | – | +14% (6.6) | -21% (10.8) | -21% | 23 ↓ | -21% (so far) | +14% (so far) |
| 9 | PSN | Parsons Corporation | Industrials | 2025-02-21 | 23 | -48% | 15 | 57% | +29% | -45% | yes | 4.2 | +50% (7.5) | -7% (0.3) | -7% | 23 ↓ | +10% | +16% |
| 10 | VRSK | Verisk Analytics | Industrials | 2025-10-31 | 23 | -32% | 48 | 52% | +7% | +2% | open | – | +3% (2.3) | -28% (6.4) | -28% | 19 ↓ | -22% (so far) | +14% (so far) |
| 11 | TXT | Textron | Industrials | 2025-04-04 | 23 | -38% | 53 | 71% | +0% | -5% | yes | 1.2 | +66% (10.6) | +0% (0.1) | +0% | 34 | +45% | +31% |
| 12 | WLK | Westlake Corporation | Materials | 2025-04-04 | 23 | -46% | 52 | 52% | -3% | +25% | yes | 10.7 | +39% (11.9) | -35% (7.6) | -35% | 22 ↓ | +39% | +31% |
| 13 | ATR | AptarGroup | Materials | 2025-10-31 | 23 | -35% | 51 | 44% | +2% | +31% | yes | 3.4 | +26% (3.8) | -3% (7.2) | -2% | 24 | +8% (so far) | +14% (so far) |
| 14 | ROP | Roper Technologies | Information Technology | 2025-10-31 | 23 | -25% | 98 | 59% | +14% | +7% | open | – | +2% (0.4) | -29% (3.6) | -29% | 11 ↓ | -19% (so far) | +14% (so far) |
| 15 | BRKR | Bruker | Health Care | 2025-04-04 | 24 | -62% | 54 | 53% | +14% | -74% | yes | 3.2 | +50% (9.2) | -19% (5.0) | -3% | 27 | +1% | +31% |
| 16 | GPK | Graphic Packaging | Materials | 2025-10-31 | 24 | -48% | 83 | 14% | -5% | -24% | open | – | +7% (0.1) | -43% (4.6) | -43% | 15 ↓ | -39% (so far) | +14% (so far) |
| 17 | PAYX | Paychex | Industrials | 2025-11-07 | 24 | -31% | 35 | 69% | +5% | -2% | open | – | +18% (9.8) | -23% (5.1) | -23% | 22 ↓ | -6% (so far) | +16% (so far) |
| 18 | ELF | e.l.f. Beauty | Consumer Staples | 2025-04-04 | 24 | -75% | 56 | 24% | +46% | -26% | yes | 0.9 | +167% (5.5) | -9% (0.4) | -9% | 24 ↓ | +11% | +31% |
| 19 | MDLZ | Mondelez International | Consumer Staples | 2025-01-10 | 24 | -28% | 89 | 43% | +2% | -16% | yes | 1.8 | +28% (6.3) | -6% (11.9) | -0% | 29 | +1% | +21% |
| 20 | TTEK | Tetra Tech | Industrials | 2025-02-28 | 24 | -43% | 20 | 44% | +11% | +10% | yes | 2.3 | +47% (11.4) | -4% (1.3) | -4% | 26 | +24% | +17% |


#### 2026: 20 buys, 12 hit +20%, SPY +14% that year

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TYL | Tyler Technologies | Information Technology | 2026-01-30 | 20 | -44% | 61 | 45% | +11% | +31% | open | – | +3% (7.1) | -25% (4.7) | -25% | 14 ↓ | -12% (so far) | +12% (so far) |
| 2 | NOW | ServiceNow | Information Technology | 2026-02-06 | 22 | -58% | 60 | 8% | +21% | +21% | yes | 0.9 | +47% (6.8) | -18% (2.1) | -0% | 26 | +35% (so far) | +13% (so far) |
| 3 | HRB | H&R Block | Consumer Discretionary | 2026-02-06 | 22 | -52% | 77 | 26% | +4% | +9% | yes | 3.4 | +69% (6.1) | -14% (0.2) | -14% | 20 ↓ | +33% (so far) | +13% (so far) |
| 4 | WDAY | Workday, Inc. | Information Technology | 2026-02-13 | 23 | -54% | 103 | 0% | +13% | -61% | yes | 5.7 | +43% (6.6) | -22% (1.8) | -22% | 21 ↓ | +31% (so far) | +14% (so far) |
| 5 | CVLT | CommVault Systems | Information Technology | 2026-01-30 | 23 | -57% | 68 | 56% | +22% | -55% | yes | 3.2 | +79% (5.2) | -12% (1.9) | -12% | 23 | +70% (so far) | +12% (so far) |
| 6 | GWRE | Guidewire Software | Information Technology | 2026-02-06 | 23 | -53% | 35 | 26% | +23% | +186% | yes | 0.9 | +61% (6.7) | -20% (4.5) | -5% | 23 ↓ | +14% (so far) | +13% (so far) |
| 7 | BR | Broadridge Financial Solutions | Industrials | 2026-02-06 | 23 | -33% | 110 | 51% | +9% | +22% | open | – | +8% (0.9) | -25% (4.7) | -25% | 21 ↓ | -8% (so far) | +13% (so far) |
| 8 | INTU | Intuit | Information Technology | 2026-02-13 | 23 | -51% | 32 | 48% | +17% | +42% | yes | 0.7 | +20% (0.7) | -36% (4.3) | -10% | 22 ↓ | -30% (so far) | +14% (so far) |
| 9 | EXLS | EXL Service | Industrials | 2026-02-13 | 24 | -43% | 53 | 50% | +14% | +30% | yes | 6.1 | +28% (6.4) | -16% (4.3) | -16% | 24 | +16% (so far) | +14% (so far) |
| 10 | NFLX | Netflix | Communication Services | 2026-02-13 | 24 | -43% | 32 | 39% | +16% | +28% | yes | 0.5 | +40% (2.0) | -12% (5.2) | -1% | 27 | -7% (so far) | +14% (so far) |
| 11 | PPC | Pilgrim's Pride | Consumer Staples | 2026-05-15 | 24 | -52% | 79 | 31% | +3% | -18% | open | – | +18% (3.4) | -4% (2.9) | -4% | 27 | +1% (so far) | +5% (so far) |
| 12 | ERIE | Erie Indemnity | Financials | 2026-03-20 | 24 | -56% | 77 | 11% | +7% | – | open | – | +13% (5.2) | -13% (2.5) | -13% | 23 ↓ | -6% (so far) | +20% (so far) |
| 13 | SLM | SLM Corp | Financials | 2026-02-27 | 24 | -46% | 57 | 82% | – | -2% | yes | 1.6 | +51% (5.5) | +1% (0.1) | +1% | 26 | +28% (so far) | +13% (so far) |
| 14 | JEF | Jefferies | Financials | 2026-03-13 | 24 | -56% | 65 | 51% | +3% | -5% | yes | 0.9 | +74% (3.3) | +1% (0.1) | +1% | 28 | +33% (so far) | +17% (so far) |
| 15 | ROL | Rollins, Inc. | Industrials | 2026-06-26 | 24 | -35% | 55 | 19% | +11% | +10% | open | – | +5% (0.7) | -30% (3.0) | -30% | 16 ↓ | -30% (so far) | +6% (so far) |
| 16 | ICE | Intercontinental Exchange | Financials | 2026-06-26 | 25 | -35% | 87 | 25% | +7% | +42% | yes | 1.0 | +33% (2.3) | -1% (0.1) | -1% | 35 | +25% (so far) | +6% (so far) |
| 17 | MCD | McDonald's | Consumer Discretionary | 2026-09-25 | 25 | -31% | 30 | 53% | +6% | +5% | open | – | – (–) | – (–) | – | – ↓ | – (so far) | – (so far) |
| 18 | PLNT | Planet Fitness | Consumer Discretionary | 2026-03-13 | 25 | -36% | 58 | 34% | +12% | – | open | – | +3% (0.2) | -45% (6.4) | -45% | 15 ↓ | -42% (so far) | +17% (so far) |
| 19 | TSCO | Tractor Supply | Consumer Discretionary | 2026-04-24 | 25 | -43% | 100 | 41% | +4% | +1% | open | – | -0% (3.6) | -20% (1.3) | -20% | 20 ↓ | -11% (so far) | +9% (so far) |
| 20 | EQH | Equitable Holdings | Financials | 2026-03-13 | 25 | -34% | 56 | 34% | -6% | -228% | yes | 3.1 | +47% (6.2) | -5% (0.5) | -5% | 23 ↓ | +47% (so far) | +17% (so far) |
