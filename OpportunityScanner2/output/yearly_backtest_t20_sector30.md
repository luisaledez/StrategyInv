# Tier A yearly backtest: former overbought-ATH leader, monthly RSI < 35, +20% target, staples / utilities / materials only below RSI 30

Generated 2026-09-29. Universe: today's S&P 500 + 400 (899 tickers, survivorship bias), monthly candles to 2026-08-31, fundamentals point in time from SEC filings.

**Trigger**: a new all-time high on a monthly candle with monthly RSI(14) ≥ 70 (≥ 5 years of history) arms the stock for 36 months; the first month whose RSI closes below 35 is the buy, at that month's close. **Filters**: quality (profitable TTM and in 2 of the 3 past years, revenue growth ≥ 5%, EPS growing, no one-off gain, no acquisition-driven growth) and cheap (operating multiples in the bottom half of the company's own history). Liquid names only (3-month average dollar volume ≥ $5M). Signals are grouped by calendar year, ranked by signal RSI (lowest first) and cut to the top 20.

**What is measured** over the 12 months after the buy (daily adjusted closes): whether the stock closed ≥ 20% above the buy price ("hit") and how long that took; the highest close vs the buy ("max gain"); the lowest close vs the buy ("max DD", the drawdown from the entry price) and the same measured only up to the hit day ("DD before hit"); whether the monthly RSI printed below the signal RSI afterwards ("RSI went lower", ↓ in the tables, with the RSI low); and the plain 12-month return. Windows that run past Aug 2026 are "open" and show what happened so far.

**Sector rule**: Consumer Staples, Utilities and Materials are bought only when the signal RSI is below 30; other sectors keep RSI < 35. Full position at the signal close.

**SPY**: "SPY cal. year" is SPY's total return over the calendar year of the signals (2026 to Aug); "SPY same 12m" is SPY over each buy's own 12-month window, and "beat SPY" the share of buys that returned more than SPY over that window.

> Since 2010 every leader + RSI<35 signal that passes the quality filter also passes the cheap filter (valuation percentile ≤ 50%), so "quality" and "quality + cheap" are the same list.


## quality + cheap

58 signals since 2010, 58 after the top-20 cut per year (the cap never bound), 1 dropped by the sector rule.

Dropped by the sector rule: ALB 2019-05.

### Summary by year

| Year | SPY cal. year | Buys | Hit +20% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | 12m return: median / mean | 12m best | 12m worst | beat SPY (same 12m) | SPY same 12m (median) | Max gain (median / best) | Max DD (median / worst) | RSI went lower | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | +15% | 1 | 1/1 = 100% | 1.6 / 1.6 / 1.6 | 100% / 100% | +25% / +25% | +25% GILD | +25% GILD | 100% | +18% | +36% / +36% GILD | +4% / +4% GILD | 0% | 0/1 = 0% | – / – | – |
| 2011 | +2% | 2 | 2/2 = 100% | 2.3 / 2.3 / 2.6 | 100% / 100% | +37% / +37% | +55% ILMN | +19% DLB | 50% | +23% | +72% / +80% ILMN | -10% / -15% ILMN | 50% | 0/2 = 0% | – / – | – |
| 2012 | +16% | 1 | 1/1 = 100% | 4.6 / 4.6 / 4.6 | 0% / 100% | +16% / +16% | +16% CHRW | +16% CHRW | 0% | +25% | +30% / +30% CHRW | +0% / +0% CHRW | 0% | 0/1 = 0% | – / – | – |
| 2013 | +32% | 0 | | | | | | | | | | | | | | |
| 2014 | +13% | 0 | | | | | | | | | | | | | | |
| 2015 | +1% | 1 | 0/1 = 0% | – / – / – | 0% / 0% | -2% / -2% | -2% PII | -2% PII | 0% | +12% | +18% / +18% PII | -19% / -19% PII | 100% | 1/1 = 100% | -19% / -19% | -2% |
| 2016 | +12% | 2 | 2/2 = 100% | 1.0 / 1.0 / 1.1 | 100% / 100% | +86% / +86% | +93% CFR | +78% PAG | 100% | +20% | +93% / +103% CFR | -5% / -5% CFR | 0% | 0/2 = 0% | – / – | – |
| 2017 | +22% | 2 | 2/2 = 100% | 4.3 / 4.3 / 5.7 | 50% / 100% | +54% / +54% | +71% ORLY | +37% TSCO | 100% | +17% | +61% / +71% ORLY | -5% / -9% TSCO | 50% | 0/2 = 0% | – / – | – |
| 2018 | -5% | 4 | 4/4 = 100% | 2.5 / 4.2 / 10.7 | 75% / 75% | +39% / +36% | +54% SNX | +13% PVH | 50% | +23% | +46% / +57% SNX | -13% / -26% PVH | 50% | 0/4 = 0% | – / – | – |
| 2019 | +31% | 0 | | | | | | | | | | | | | | |
| 2020 | +18% | 12 | 12/12 = 100% | 1.6 / 1.8 / 7.3 | 92% / 92% | +69% / +82% | +166% RCL | +41% GD | 75% | +56% | +76% / +200% RCL | -11% / -24% RCL | 33% | 0/12 = 0% | – / – | – |
| 2021 | +29% | 0 | | | | | | | | | | | | | | |
| 2022 | -18% | 11 | 10/11 = 91% | 1.5 / 2.5 / 8.4 | 55% / 82% | +55% / +48% | +78% META | -8% FIS | 91% | +19% | +60% / +93% NFLX | -4% / -45% META | 36% | 1/11 = 9% | -29% / -29% | -8% |
| 2023 | +26% | 5 | 4/5 = 80% | 2.0 / 2.3 / 3.6 | 60% / 80% | +38% / +40% | +87% WAL | +8% CCI | 60% | +36% | +50% / +103% WAL | -19% / -49% WAL | 60% | 1/5 = 20% | -19% / -19% | +8% |
| 2024 | +25% | 1 | 1/1 = 100% | 1.4 / 1.4 / 1.4 | 100% / 100% | +88% / +88% | +88% FIVE | +88% FIVE | 100% | +16% | +96% / +96% FIVE | -23% / -23% FIVE | 0% | 0/1 = 0% | – / – | – |
| 2025 | +18% | 5 (3 open) | 3/5 = 60% | 2.2 / 2.5 / 3.6 | 40% / 60% | +19% / +19% | +24% MOH | +14% REXR | 50% | +25% | +29% / +54% MOH | -22% / -31% FISV | 40% | 0/2 = 0% | – / – | – |
| 2026 | +13% | 10 (10 open) | 5/10 = 50% | 1.9 / 2.1 / 4.5 | 30% / 50% | – / – | – | – | – | – | +21% / +123% QLYS | -22% / -47% TTD | 90% | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-08)** |  | 44 | 41/44 = 93% | 1.9 / 2.5 / 10.7 | 70% / 86% | +54% / +54% | +166% RCL | -8% FIS | 73% | +24% | +62% / +200% RCL | -9% / -49% WAL | 36% | 3/44 = 7% | -19% / -29% | -2% |
| **All incl. open** |  | 57 (13 open) | 47/57 = 82% | 1.9 / 2.4 / 10.7 | 61% / 77% | +54% / +54% | +166% RCL | -8% FIS | 73% | +24% | +51% / +200% RCL | -13% / -49% WAL | 47% | 3/44 = 7% | -19% / -29% | -2% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months from the signal month-end. "RSI went lower" = share of buys whose monthly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 1 buys, 1 hit +20%, SPY +15% that year, 12m median +25%, best +25%, worst +25%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GILD | Gilead Sciences | Health Care | 2010-08 | 35 | -45% | 0% | +23% | +60% | yes | 1.6 | +36% (10.7) | +4% (0.0) | +4% | 41 | +25% | +18% |


#### 2011: 2 buys, 2 hit +20%, SPY +2% that year, 12m median +37%, best +55%, worst +19%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLB | Dolby | Information Technology | 2011-09 | 31 | -61% | 0% | +9% | +15% | yes | 2.1 | +64% (7.5) | -4% (0.1) | -4% | 33 | +19% | +30% |
| 2 | ILMN | Illumina, Inc. | Health Care | 2011-10 | 35 | -61% | 0% | +44% | +50% | yes | 2.6 | +80% (2.8) | -15% (1.4) | -15% | 33 ↓ | +55% | +15% |


#### 2012: 1 buys, 1 hit +20%, SPY +16% that year, 12m median +16%, best +16%, worst +16%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CHRW | C.H. Robinson | Industrials | 2012-07 | 33 | -36% | 0% | +10% | +11% | yes | 4.6 | +30% (6.0) | +0% (0.0) | +0% | 40 | +16% | +25% |


#### 2015: 1 buys, 0 hit +20%, SPY +1% that year, 12m median -2%, best -2%, worst -2%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PII | Polaris | Consumer Discretionary | 2015-12 | 31 | -46% | 14% | +14% | +13% | **no** | – | +18% (3.8) | -19% (0.9) | -19% | 28 ↓ | -2% | +12% |


#### 2016: 2 buys, 2 hit +20%, SPY +12% that year, 12m median +86%, best +93%, worst +78%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CFR | Frost Bank | Financials | 2016-01 | 33 | -42% | 14% | +8% | +8% | yes | 1.1 | +103% (11.9) | -5% (0.1) | -5% | 33 | +93% | +20% |
| 2 | PAG | Penske Automotive Group | Consumer Discretionary | 2016-01 | 33 | -42% | 10% | +8% | +20% | yes | 0.8 | +84% (10.2) | -4% (0.1) | -4% | 37 | +78% | +20% |


#### 2017: 2 buys, 2 hit +20%, SPY +22% that year, 12m median +54%, best +71%, worst +37%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TSCO | Tractor Supply | Consumer Discretionary | 2017-05 | 34 | -43% | 19% | +8% | +5% | yes | 5.7 | +51% (7.7) | -9% (1.4) | -9% | 33 ↓ | +37% | +14% |
| 2 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2017-08 | 34 | -33% | 22% | +6% | +14% | yes | 3.0 | +71% (12.0) | +0% (0.4) | +0% | 41 | +71% | +19% |


#### 2018: 4 buys, 4 hit +20%, SPY -5% that year, 12m median +39%, best +54%, worst +13%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SNX | TD Synnex | Information Technology | 2018-10 | 33 | -45% | 38% | +27% | +2% | yes | 2.4 | +57% (11.9) | -6% (0.9) | -6% | 35 | +54% | +14% |
| 2 | EPR | EPR Properties | Real Estate | 2018-03 | 33 | -35% | 18% | +17% | +4% | yes | 2.7 | +49% (11.9) | -4% (0.8) | -4% | 33 ↓ | +48% | +9% |
| 3 | STT | State Street Corporation | Financials | 2018-12 | 34 | -45% | 21% | +9% | +8% | yes | 10.7 | +31% (11.4) | -21% (7.5) | -21% | 32 ↓ | +29% | +31% |
| 4 | PVH | PVH Corp. | Consumer Discretionary | 2018-12 | 35 | -45% | 5% | +13% | +32% | yes | 1.2 | +43% (3.7) | -26% (7.7) | -2% | 36 | +13% | +31% |


#### 2020: 12 buys, 12 hit +20%, SPY +18% that year, 12m median +69%, best +166%, worst +41%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RGA | Reinsurance Group of America | Financials | 2020-03 | 25 | -50% | 15% | +11% | +24% | yes | 0.3 | +64% (11.5) | -19% (3.3) | -7% | 30 | +54% | +56% |
| 2 | WTFC | Wintrust Financial | Financials | 2020-03 | 27 | -67% | 5% | +6% | +3% | yes | 0.3 | +162% (11.5) | -11% (0.5) | -7% | 35 | +136% | +56% |
| 3 | RCL | Royal Caribbean Group | Consumer Discretionary | 2020-03 | 28 | -76% | 7% | +15% | +5% | yes | 0.3 | +200% (10.8) | -24% (0.1) | -24% | 34 | +166% | +56% |
| 4 | AFG | American Financial Group | Financials | 2020-03 | 30 | -42% | 19% | +15% | +68% | yes | 7.3 | +78% (11.6) | -22% (1.5) | -22% | 26 ↓ | +71% | +56% |
| 5 | UDR | UDR, Inc. | Real Estate | 2020-09 | 32 | -36% | 19% | +13% | +9% | yes | 1.3 | +77% (9.9) | -8% (0.9) | -8% | 30 ↓ | +68% | +30% |
| 6 | WWD | Woodward, Inc. | Industrials | 2020-03 | 33 | -54% | 17% | +18% | +24% | yes | 2.1 | +115% (9.2) | -14% (0.1) | -14% | 33 | +104% | +56% |
| 7 | ACGL | Arch Capital Group | Financials | 2020-04 | 33 | -50% | 12% | +27% | +124% | yes | 0.9 | +68% (11.9) | -7% (0.4) | -7% | 41 | +65% | +46% |
| 8 | THG | Hanover Insurance | Financials | 2020-03 | 33 | -37% | 40% | +9% | +15% | yes | 2.2 | +51% (11.6) | -7% (0.1) | -7% | 37 | +46% | +56% |
| 9 | GD | General Dynamics | Industrials | 2020-03 | 34 | -42% | 41% | +9% | +7% | yes | 2.2 | +43% (11.9) | -7% (1.2) | -7% | 33 ↓ | +41% | +56% |
| 10 | FNF | Fidelity National Financial | Financials | 2020-03 | 34 | -50% | 18% | +12% | +69% | yes | 1.9 | +76% (11.5) | -7% (0.1) | -7% | 37 | +70% | +56% |
| 11 | MTN | Vail Resorts | Consumer Discretionary | 2020-03 | 34 | -51% | 27% | +13% | +13% | yes | 1.2 | +116% (10.8) | -11% (0.1) | -11% | 40 | +97% | +56% |
| 12 | MOG-A | Moog Inc. | Industrials | 2020-03 | 34 | -49% | 13% | +8% | +37% | yes | 2.1 | +73% (11.4) | -21% (1.4) | -21% | 34 ↓ | +66% | +56% |


#### 2022: 11 buys, 10 hit +20%, SPY -18% that year, 12m median +55%, best +78%, worst -8%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | Communication Services | 2022-04 | 29 | -73% | 15% | +15% | +33% | yes | 3.2 | +93% (8.9) | -13% (0.4) | -13% | 29 ↓ | +73% | +3% |
| 2 | CMCSA | Comcast | Communication Services | 2022-09 | 30 | -53% | 9% | +12% | +15% | yes | 1.7 | +66% (11.0) | -1% (0.4) | -1% | 34 | +56% | +22% |
| 3 | CHTR | Charter Communications | Communication Services | 2022-09 | 31 | -63% | 5% | +6% | +59% | yes | 0.9 | +50% (11.6) | +1% (2.5) | +1% | 36 | +45% | +22% |
| 4 | SWKS | Skyworks Solutions | Information Technology | 2022-06 | 32 | -55% | 14% | +21% | +14% | yes | 1.1 | +34% (7.3) | -14% (3.4) | -2% | 33 | +22% | +19% |
| 5 | META | Meta Platforms | Communication Services | 2022-06 | 33 | -58% | 2% | +27% | +13% | yes | 8.4 | +79% (11.8) | -45% (4.1) | -45% | 26 ↓ | +78% | +19% |
| 6 | ALGN | Align Technology | Health Care | 2022-06 | 33 | -68% | 13% | +43% | +56% | yes | 0.7 | +53% (9.8) | -26% (4.3) | +4% | 33 ↓ | +49% | +19% |
| 7 | RH | RH | Consumer Discretionary | 2022-06 | 34 | -71% | 16% | +19% | +110% | yes | 0.2 | +64% (7.1) | +4% (0.0) | +4% | 38 | +55% | +19% |
| 8 | FIS | Fidelity National Information Services | Financials | 2022-12 | 35 | -57% | 34% | +7% | +325% | **no** | – | +15% (1.1) | -29% (9.9) | -29% | 32 ↓ | -8% | +26% |
| 9 | PNR | Pentair | Industrials | 2022-09 | 35 | -49% | 21% | +18% | +19% | yes | 3.4 | +80% (10.2) | -3% (0.7) | -3% | 38 | +62% | +22% |
| 10 | CGNX | Cognex | Information Technology | 2022-06 | 35 | -58% | 33% | +22% | +22% | yes | 4.4 | +35% (7.1) | -4% (3.5) | -4% | 37 | +32% | +19% |
| 11 | LII | Lennox International | Industrials | 2022-06 | 35 | -42% | 38% | +11% | +12% | yes | 1.3 | +60% (12.0) | +3% (0.0) | +3% | 41 | +60% | +19% |


#### 2023: 5 buys, 4 hit +20%, SPY +26% that year, 12m median +38%, best +87%, worst +8%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UDR | UDR, Inc. | Real Estate | 2023-10 | 33 | -48% | 9% | +10% | +176% | yes | 1.4 | +53% (10.4) | -1% (0.0) | -1% | 36 | +38% | +38% |
| 2 | WAL | Western Alliance Bancorporation | Financials | 2023-03 | 34 | -72% | 17% | +17% | +12% | yes | 3.6 | +103% (10.0) | -49% (1.1) | -49% | 33 ↓ | +87% | +30% |
| 3 | CCI | Crown Castle | Real Estate | 2023-07 | 35 | -48% | 10% | +6% | +15% | **no** | – | +11% (4.0) | -19% (2.6) | -19% | 31 ↓ | +8% | +22% |
| 4 | SBAC | SBA Communications | Real Estate | 2023-09 | 35 | -49% | 8% | +11% | +44% | yes | 1.9 | +28% (3.1) | -6% (7.0) | -5% | 37 | +22% | +36% |
| 5 | PODD | Insulet Corporation | Health Care | 2023-09 | 35 | -53% | 16% | +24% | +73% | yes | 2.0 | +50% (11.8) | -20% (0.4) | -20% | 32 ↓ | +46% | +36% |


#### 2024: 1 buys, 1 hit +20%, SPY +25% that year, 12m median +88%, best +88%, worst +88%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FIVE | Five Below | Consumer Discretionary | 2024-07 | 33 | -69% | 0% | +15% | +11% | yes | 1.4 | +96% (11.9) | -23% (8.2) | -11% | 33 | +88% | +16% |


#### 2025: 5 buys, 3 hit +20%, SPY +18% that year, 12m median +19%, best +24%, worst +14%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MOH | Molina Healthcare | Health Care | 2025-07 | 29 | -63% | 14% | +16% | +10% | yes | 1.8 | +54% (11.4) | -22% (6.4) | -4% | 31 | +24% | +19% |
| 2 | FISV | Fiserv | Financials | 2025-10 | 30 | -72% | 6% | +5% | +25% | open | – | +5% (2.3) | -31% (10.7) | -31% | 29 ↓ | -30% (so far) | +14% (so far) |
| 3 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2025-10 | 34 | -54% | 12% | +7% | +5% | yes | 2.2 | +29% (2.8) | -11% (7.1) | -6% | 37 | -1% (so far) | +14% (so far) |
| 4 | REXR | Rexford Industrial Realty | Real Estate | 2025-04 | 34 | -61% | 5% | +18% | +13% | yes | 3.6 | +37% (5.7) | +0% (0.0) | +0% | 36 | +14% | +31% |
| 5 | KBR | KBR, Inc. | Industrials | 2025-12 | 34 | -45% | 50% | +9% | +23% | open | – | +12% (0.5) | -25% (4.4) | -25% | 31 ↓ | -13% (so far) | +14% (so far) |


#### 2026: 10 buys, 5 hit +20%, SPY +13% that year

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BR | Broadridge Financial Solutions | Industrials | 2026-03 | 32 | -40% | 38% | +7% | +41% | open | – | +15% (4.8) | -16% (3.0) | -16% | 26 ↓ | +2% (so far) | +19% (so far) |
| 2 | TYL | Tyler Technologies | Information Technology | 2026-01 | 32 | -44% | 26% | +11% | +31% | open | – | +3% (7.1) | -25% (4.7) | -25% | 26 ↓ | -12% (so far) | +12% (so far) |
| 3 | BSX | Boston Scientific | Health Care | 2026-03 | 32 | -43% | 30% | +20% | +55% | open | – | +5% (0.8) | -32% (3.4) | -32% | 24 ↓ | -30% (so far) | +19% (so far) |
| 4 | EXLS | EXL Service | Industrials | 2026-06 | 33 | -51% | 9% | +13% | +19% | yes | 1.0 | +48% (1.9) | +4% (0.0) | +4% | 47 | +34% (so far) | +4% (so far) |
| 5 | INTU | Intuit | Information Technology | 2026-02 | 33 | -50% | 37% | +17% | +44% | open | – | +18% (0.2) | -37% (3.8) | -37% | 27 ↓ | -32% (so far) | +13% (so far) |
| 6 | NOW | ServiceNow | Information Technology | 2026-02 | 34 | -55% | 7% | +21% | +21% | yes | 3.1 | +37% (6.0) | -23% (1.3) | -23% | 30 ↓ | +26% (so far) | +13% (so far) |
| 7 | TTD | Trade Desk (The) | Communication Services | 2026-02 | 34 | -83% | 10% | +18% | +15% | yes | 0.2 | +25% (0.2) | -47% (6.9) | +2% | 31 ↓ | -47% (so far) | +13% (so far) |
| 8 | ADP | Automatic Data Processing | Industrials | 2026-02 | 34 | -35% | 41% | +7% | +11% | yes | 4.5 | +36% (5.9) | -11% (1.3) | -11% | 32 ↓ | +26% (so far) | +13% (so far) |
| 9 | ROL | Rollins, Inc. | Industrials | 2026-07 | 34 | -43% | 14% | +10% | +9% | open | – | +1% (0.1) | -21% (1.8) | -21% | 32 ↓ | -21% (so far) | +4% (so far) |
| 10 | QLYS | Qualys | Information Technology | 2026-03 | 34 | -57% | 2% | +10% | +17% | yes | 1.9 | +123% (4.4) | -13% (0.3) | -13% | 34 ↓ | +96% (so far) | +19% (so far) |


## no fundamentals filter

259 signals since 2010, 182 after the top-20 cut per year (the cap bound in 2015, 2018, 2020, 2022, 2026), 29 dropped by the sector rule.

Dropped by the sector rule: LIN 2015-09, CBT 2015-09, OGE 2015-11, CF 2016-01, PCG 2017-12, KR 2017-06, TGT 2017-06, SAM 2017-06, GIS 2018-03, PM 2018-04, SLGN 2018-10, COKE 2018-05, INGR 2019-05, ALB 2019-05, LYB 2020-03, UGI 2020-02, CLX 2022-09, BALL 2022-08, SAM 2022-06, DG 2023-08, EL 2023-09, DLTR 2024-09, GPK 2025-10, HSY 2025-01, GIS 2025-05, OLN 2025-02, ADM 2025-02, INGR 2026-06, PPC 2026-07.

### Summary by year

| Year | SPY cal. year | Buys | Hit +20% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | 12m return: median / mean | 12m best | 12m worst | beat SPY (same 12m) | SPY same 12m (median) | Max gain (median / best) | Max DD (median / worst) | RSI went lower | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | +15% | 4 | 3/4 = 75% | 4.2 / 3.5 / 4.7 | 25% / 75% | +35% / +31% | +46% XOM | +8% OVV | 75% | +24% | +41% / +57% XOM | -2% / -12% OVV | 50% | 1/4 = 25% | -12% / -12% | +8% |
| 2011 | +2% | 2 | 2/2 = 100% | 2.3 / 2.3 / 2.6 | 100% / 100% | +37% / +37% | +55% ILMN | +19% DLB | 50% | +23% | +72% / +80% ILMN | -10% / -15% ILMN | 50% | 0/2 = 0% | – / – | – |
| 2012 | +16% | 1 | 1/1 = 100% | 4.6 / 4.6 / 4.6 | 0% / 100% | +16% / +16% | +16% CHRW | +16% CHRW | 0% | +25% | +30% / +30% CHRW | +0% / +0% CHRW | 0% | 0/1 = 0% | – / – | – |
| 2013 | +32% | 1 | 1/1 = 100% | 6.2 / 6.2 / 6.2 | 0% / 0% | +54% / +54% | +54% DLR | +54% DLR | 100% | +17% | +54% / +54% DLR | -7% / -7% DLR | 100% | 0/1 = 0% | – / – | – |
| 2014 | +13% | 2 | 2/2 = 100% | 5.7 / 5.7 / 7.7 | 0% / 50% | +19% / +19% | +33% HAE | +5% TPR | 50% | +10% | +40% / +49% HAE | -0% / -3% TPR | 0% | 0/2 = 0% | – / – | – |
| 2015 | +1% | 17 | 12/17 = 71% | 4.4 / 4.8 / 8.7 | 24% / 41% | +23% / +23% | +72% OKE | -19% WYNN | 82% | +12% | +31% / +72% OKE | -16% / -57% WMB | 71% | 5/17 = 29% | -23% / -53% | +0% |
| 2016 | +12% | 15 | 15/15 = 100% | 1.9 / 2.2 / 7.9 | 87% / 93% | +46% / +47% | +93% CFR | +9% MCK | 80% | +20% | +48% / +103% CFR | -4% / -32% STX | 13% | 0/15 = 0% | – / – | – |
| 2017 | +22% | 8 | 8/8 = 100% | 5.3 / 5.0 / 9.6 | 38% / 75% | +27% / +30% | +71% ORLY | -4% CAH | 62% | +16% | +45% / +71% ORLY | -11% / -30% BBWI | 62% | 0/8 = 0% | – / – | – |
| 2018 | -5% | 16 | 15/16 = 94% | 3.2 / 4.3 / 10.7 | 44% / 69% | +31% / +31% | +64% BWXT | -13% DY | 75% | +14% | +37% / +69% BWXT | -10% / -40% VC | 50% | 1/16 = 6% | -25% / -25% | -13% |
| 2019 | +31% | 2 | 1/2 = 50% | 2.0 / 2.0 / 2.0 | 50% / 50% | +4% / +4% | +28% IDCC | -20% DD | 50% | +17% | +28% / +37% IDCC | -43% / -55% DD | 50% | 1/2 = 50% | -55% / -55% | -20% |
| 2020 | +18% | 18 | 18/18 = 100% | 0.9 / 1.9 / 7.3 | 83% / 89% | +91% / +106% | +195% EWBC | +48% L | 72% | +56% | +108% / +213% EWBC | -16% / -40% PBF | 28% | 0/18 = 0% | – / – | – |
| 2021 | +29% | 1 | 1/1 = 100% | 0.9 / 0.9 / 0.9 | 100% / 100% | +12% / +12% | +12% HAE | +12% HAE | 100% | -0% | +32% / +32% HAE | -22% / -22% HAE | 0% | 0/1 = 0% | – / – | – |
| 2022 | -18% | 17 | 14/17 = 82% | 1.2 / 2.1 / 8.4 | 59% / 76% | +45% / +33% | +81% AMZN | -34% PYPL | 59% | +19% | +50% / +93% NFLX | -14% / -45% META | 47% | 3/17 = 18% | -39% / -40% | -2% |
| 2023 | +26% | 16 | 13/16 = 81% | 1.9 / 2.4 / 7.5 | 62% / 75% | +37% / +36% | +87% WAL | -2% PFE | 50% | +38% | +51% / +103% WAL | -5% / -49% WAL | 38% | 3/16 = 19% | -19% / -20% | +4% |
| 2024 | +25% | 2 | 2/2 = 100% | 2.2 / 2.2 / 3.1 | 50% / 100% | +42% / +42% | +88% FIVE | -3% ELV | 50% | +17% | +60% / +96% FIVE | -24% / -25% ELV | 50% | 0/2 = 0% | – / – | – |
| 2025 | +18% | 13 (4 open) | 9/13 = 69% | 2.2 / 3.5 / 11.4 | 46% / 54% | +26% / +40% | +163% PBF | -21% IT | 56% | +30% | +37% / +210% PBF | -14% / -50% IT | 54% | 1/9 = 11% | -50% / -50% | -21% |
| 2026 | +13% | 18 (18 open) | 10/18 = 56% | 1.5 / 1.8 / 4.5 | 44% / 56% | – / – | – | – | – | – | +25% / +123% QLYS | -15% / -47% TTD | 71% | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-08)** |  | 131 | 116/131 = 89% | 2.3 / 3.2 / 11.4 | 56% / 73% | +36% / +43% | +195% EWBC | -34% PYPL | 67% | +20% | +50% / +213% EWBC | -11% / -57% WMB | 43% | 15/131 = 11% | -23% / -55% | -2% |
| **All incl. open** |  | 153 (22 open) | 127/153 = 83% | 2.2 / 3.0 / 11.4 | 54% / 70% | +36% / +43% | +195% EWBC | -34% PYPL | 67% | +20% | +46% / +213% EWBC | -12% / -57% WMB | 47% | 15/131 = 11% | -23% / -55% | -2% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months from the signal month-end. "RSI went lower" = share of buys whose monthly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 4 buys, 3 hit +20%, SPY +15% that year, 12m median +35%, best +46%, worst +8%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | XOM | ExxonMobil | Energy | 2010-06 | 33 | -41% | – | – | – | yes | 4.2 | +57% (10.0) | -1% (0.1) | -1% | 37 | +46% | +30% |
| 2 | BAX | Baxter International | Health Care | 2010-05 | 35 | -41% | 2% | +2% | -16% | yes | 4.7 | +47% (11.6) | -3% (0.3) | -3% | 33 ↓ | +45% | +26% |
| 3 | OVV | Ovintiv | Energy | 2010-01 | 35 | -69% | – | – | – | **no** | – | +15% (4.5) | -12% (6.8) | -12% | 34 ↓ | +8% | +22% |
| 4 | GILD | Gilead Sciences | Health Care | 2010-08 | 35 | -45% | 0% | +23% | +60% | yes | 1.6 | +36% (10.7) | +4% (0.0) | +4% | 41 | +25% | +18% |


#### 2011: 2 buys, 2 hit +20%, SPY +2% that year, 12m median +37%, best +55%, worst +19%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLB | Dolby | Information Technology | 2011-09 | 31 | -61% | 0% | +9% | +15% | yes | 2.1 | +64% (7.5) | -4% (0.1) | -4% | 33 | +19% | +30% |
| 2 | ILMN | Illumina, Inc. | Health Care | 2011-10 | 35 | -61% | 0% | +44% | +50% | yes | 2.6 | +80% (2.8) | -15% (1.4) | -15% | 33 ↓ | +55% | +15% |


#### 2012: 1 buys, 1 hit +20%, SPY +16% that year, 12m median +16%, best +16%, worst +16%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CHRW | C.H. Robinson | Industrials | 2012-07 | 33 | -36% | 0% | +10% | +11% | yes | 4.6 | +30% (6.0) | +0% (0.0) | +0% | 40 | +16% | +25% |


#### 2013: 1 buys, 1 hit +20%, SPY +32% that year, 12m median +54%, best +54%, worst +54%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLR | Digital Realty | Real Estate | 2013-10 | 33 | -41% | 0% | +25% | +1% | yes | 6.2 | +54% (12.0) | -7% (1.1) | -7% | 33 ↓ | +54% | +17% |


#### 2014: 2 buys, 2 hit +20%, SPY +13% that year, 12m median +19%, best +33%, worst +5%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TPR | Tapestry, Inc. | Consumer Discretionary | 2014-06 | 33 | -57% | 7% | -2% | -11% | yes | 7.7 | +30% (8.0) | -3% (4.2) | -3% | 34 | +5% | +7% |
| 2 | HAE | Haemonetics | Health Care | 2014-04 | 34 | -34% | 46% | +14% | -15% | yes | 3.6 | +49% (10.4) | +2% (0.0) | +2% | 44 | +33% | +13% |


#### 2015: 17 buys, 12 hit +20%, SPY +1% that year, 12m median +23%, best +72%, worst -19%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | WMT | Walmart | Consumer Staples | 2015-10 | 30 | -37% | 0% | +1% | -2% | yes | 4.5 | +34% (9.6) | -1% (0.4) | -1% | 33 | +26% | +4% |
| 2 | M | Macy's | Consumer Discretionary | 2015-11 | 31 | -47% | 27% | -0% | +1% | **no** | – | +20% (11.8) | -22% (5.6) | -22% | 28 ↓ | +12% | +8% |
| 3 | PII | Polaris | Consumer Discretionary | 2015-12 | 31 | -46% | 14% | +14% | +13% | **no** | – | +18% (3.8) | -19% (0.9) | -19% | 28 ↓ | -2% | +12% |
| 4 | HUBB | Hubbell Incorporated | Industrials | 2015-09 | 31 | -33% | 33% | +5% | -5% | yes | 2.8 | +31% (11.1) | +0% (0.0) | +0% | 40 | +30% | +15% |
| 5 | MAT | Mattel | Consumer Discretionary | 2015-01 | 32 | -45% | 52% | -7% | -13% | **no** | – | +14% (2.7) | -23% (8.0) | -23% | 27 ↓ | +9% | -1% |
| 6 | PVH | PVH Corp. | Consumer Discretionary | 2015-12 | 32 | -47% | 17% | -3% | +39% | yes | 2.5 | +55% (9.2) | -10% (0.6) | -10% | 32 ↓ | +23% | +12% |
| 7 | OKE | Oneok | Energy | 2015-09 | 32 | -55% | 65% | – | -5% | yes | 0.2 | +72% (12.0) | -40% (2.6) | +2% | 28 ↓ | +72% | +15% |
| 8 | EMR | Emerson Electric | Industrials | 2015-08 | 32 | -32% | 14% | -5% | +1% | yes | 7.9 | +22% (10.6) | -10% (4.8) | -10% | 29 ↓ | +15% | +12% |
| 9 | KEX | Kirby Corporation | Industrials | 2015-09 | 33 | -50% | 17% | +6% | -2% | **no** | – | +17% (8.3) | -26% (3.4) | -26% | 29 ↓ | +0% | +15% |
| 10 | WMB | Williams Companies | Energy | 2015-12 | 33 | -58% | 59% | +5% | -84% | yes | 8.2 | +34% (11.9) | -57% (1.3) | -57% | 28 ↓ | +31% | +12% |
| 11 | R | Ryder | Industrials | 2015-12 | 33 | -44% | 51% | -1% | -11% | yes | 3.6 | +53% (11.3) | -16% (0.6) | -16% | 31 ↓ | +34% | +12% |
| 12 | FLS | Flowserve | Industrials | 2015-09 | 33 | -50% | 31% | -3% | -20% | yes | 7.1 | +28% (8.3) | -14% (3.6) | -14% | 34 | +19% | +15% |
| 13 | VMI | Valmont Industries | Industrials | 2015-07 | 34 | -33% | 51% | -10% | -41% | yes | 8.7 | +31% (8.9) | -15% (2.0) | -15% | 26 ↓ | +19% | +5% |
| 14 | CXT | Crane NXT | Information Technology | 2015-09 | 34 | -39% | 36% | +2% | -11% | yes | 6.5 | +44% (11.0) | -7% (3.7) | -7% | 38 | +38% | +15% |
| 15 | EQT | EQT Corporation | Energy | 2015-11 | 34 | -49% | 88% | – | -60% | yes | 4.4 | +39% (7.0) | -17% (0.6) | -17% | 32 ↓ | +23% | +8% |
| 16 | WYNN | Wynn Resorts | Consumer Discretionary | 2015-04 | 34 | -55% | 10% | -3% | +0% | **no** | – | +7% (0.3) | -53% (5.1) | -53% | 25 ↓ | -19% | +1% |
| 17 | CVLT | CommVault Systems | Information Technology | 2015-09 | 34 | -62% | 64% | -2% | -81% | yes | 1.0 | +58% (11.9) | -10% (3.8) | +2% | 40 | +56% | +15% |


#### 2016: 15 buys, 15 hit +20%, SPY +12% that year, 12m median +46%, best +93%, worst +9%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AXP | American Express | Financials | 2016-01 | 26 | -44% | 13% | – | +0% | yes | 2.6 | +48% (11.6) | -4% (0.4) | -4% | 29 | +46% | +20% |
| 2 | BWA | BorgWarner | Consumer Discretionary | 2016-01 | 27 | -56% | 8% | -4% | -4% | yes | 1.2 | +45% (10.3) | -5% (4.9) | -3% | 32 | +41% | +20% |
| 3 | AMG | Affiliated Managers Group | Financials | 2016-01 | 32 | -42% | 16% | – | +22% | yes | 1.6 | +33% (2.9) | -12% (0.4) | -12% | 34 | +14% | +20% |
| 4 | HRB | H&R Block | Consumer Discretionary | 2016-04 | 32 | -46% | 64% | -9% | -40% | yes | 2.5 | +27% (11.9) | -4% (0.4) | -4% | 34 | +27% | +18% |
| 5 | AMP | Ameriprise Financial | Financials | 2016-02 | 32 | -39% | 35% | -1% | +2% | yes | 1.9 | +62% (12.0) | +3% (3.9) | +5% | 40 | +62% | +25% |
| 6 | CFR | Frost Bank | Financials | 2016-01 | 33 | -42% | 14% | +8% | +8% | yes | 1.1 | +103% (11.9) | -5% (0.1) | -5% | 33 | +93% | +20% |
| 7 | UNP | Union Pacific Corporation | Industrials | 2016-01 | 33 | -42% | 22% | -3% | +7% | yes | 2.7 | +57% (11.8) | -0% (0.1) | -0% | 40 | +52% | +20% |
| 8 | WDC | Western Digital | Information Technology | 2016-01 | 33 | -58% | 38% | -8% | -12% | yes | 7.9 | +73% (11.8) | -25% (3.4) | -25% | 31 ↓ | +73% | +20% |
| 9 | DOC | Healthpeak Properties | Real Estate | 2016-02 | 33 | -47% | 53% | +12% | -160% | yes | 2.3 | +41% (6.3) | +4% (0.0) | +4% | 40 | +29% | +25% |
| 10 | PAG | Penske Automotive Group | Consumer Discretionary | 2016-01 | 33 | -42% | 10% | +8% | +20% | yes | 0.8 | +84% (10.2) | -4% (0.1) | -4% | 37 | +78% | +20% |
| 11 | WEX | WEX Inc. | Financials | 2016-02 | 34 | -45% | 66% | +5% | -49% | yes | 0.4 | +83% (11.4) | +4% (0.0) | +4% | 46 | +70% | +25% |
| 12 | MCK | McKesson Corporation | Health Care | 2016-10 | 34 | -48% | 16% | +3% | +9% | yes | 4.0 | +33% (8.5) | +2% (0.0) | +2% | 39 | +9% | +23% |
| 13 | GWW | W. W. Grainger | Industrials | 2016-01 | 34 | -29% | 29% | +2% | -1% | yes | 2.5 | +33% (11.9) | -2% (0.1) | -2% | 42 | +31% | +20% |
| 14 | STX | Seagate Technology | Information Technology | 2016-01 | 34 | -58% | 67% | -14% | -67% | yes | 1.1 | +69% (12.0) | -32% (3.3) | -2% | 33 ↓ | +69% | +20% |
| 15 | WSM | Williams-Sonoma, Inc. | Consumer Discretionary | 2016-10 | 35 | -48% | 5% | +5% | +1% | yes | 1.2 | +23% (1.2) | -5% (9.7) | +1% | 39 | +15% | +23% |


#### 2017: 8 buys, 8 hit +20%, SPY +22% that year, 12m median +27%, best +71%, worst -4%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BBWI | Bath & Body Works, Inc. | Consumer Discretionary | 2017-02 | 32 | -48% | 48% | +6% | – | yes | 9.6 | +24% (9.9) | -30% (6.0) | -30% | 28 ↓ | -1% | +17% |
| 2 | VFC | VF Corporation | Consumer Discretionary | 2017-01 | 33 | -34% | 49% | -1% | +9% | yes | 5.7 | +65% (11.9) | -6% (0.2) | -6% | 35 | +62% | +26% |
| 3 | TSCO | Tractor Supply | Consumer Discretionary | 2017-05 | 34 | -43% | 19% | +8% | +5% | yes | 5.7 | +51% (7.7) | -9% (1.4) | -9% | 33 ↓ | +37% | +14% |
| 4 | GILD | Gilead Sciences | Health Care | 2017-05 | 34 | -47% | 1% | -11% | -19% | yes | 3.0 | +40% (8.0) | -1% (0.3) | -1% | 41 | +7% | +14% |
| 5 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2017-08 | 34 | -33% | 22% | +6% | +14% | yes | 3.0 | +71% (12.0) | +0% (0.4) | +0% | 41 | +71% | +19% |
| 6 | AZO | AutoZone | Consumer Discretionary | 2017-06 | 34 | -30% | 17% | +2% | +10% | yes | 5.0 | +40% (6.9) | -14% (0.4) | -14% | 31 ↓ | +18% | +14% |
| 7 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2017-09 | 35 | -59% | 67% | – | -30% | yes | 6.8 | +71% (10.5) | -18% (4.5) | -18% | 32 ↓ | +48% | +18% |
| 8 | CAH | Cardinal Health | Health Care | 2017-11 | 35 | -36% | – | – | – | yes | 1.4 | +28% (2.0) | -16% (8.3) | -1% | 33 ↓ | -4% | +6% |


#### 2018: 16 buys, 15 hit +20%, SPY -5% that year, 12m median +31%, best +64%, worst -13%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KDP | Keurig Dr Pepper | Consumer Staples | 2018-07 | 24 | -81% | 0% | +5% | +39% | yes | 8.8 | +31% (10.6) | -7% (2.2) | -7% | 24 ↓ | +20% | +8% |
| 2 | OZK | Bank OZK | Financials | 2018-10 | 28 | -52% | – | – | – | yes | 3.5 | +27% (6.1) | -23% (1.6) | -23% | 25 ↓ | +6% | +14% |
| 3 | THO | Thor Industries | Consumer Discretionary | 2018-12 | 31 | -68% | 0% | +1% | -26% | yes | 0.5 | +50% (11.7) | -17% (7.5) | -2% | 34 | +46% | +31% |
| 4 | TCBI | Texas Capital Bancshares | Financials | 2018-12 | 32 | -50% | 7% | – | +36% | yes | 1.7 | +30% (4.1) | -0% (9.2) | +1% | 37 | +11% | +31% |
| 5 | SNX | TD Synnex | Information Technology | 2018-10 | 33 | -45% | 38% | +27% | +2% | yes | 2.4 | +57% (11.9) | -6% (0.9) | -6% | 35 | +54% | +14% |
| 6 | DY | Dycom Industries | Industrials | 2018-12 | 33 | -56% | 8% | – | -3% | **no** | – | +18% (1.7) | -25% (7.7) | -25% | 31 ↓ | -13% | +31% |
| 7 | EPR | EPR Properties | Real Estate | 2018-03 | 33 | -35% | 18% | +17% | +4% | yes | 2.7 | +49% (11.9) | -4% (0.8) | -4% | 33 ↓ | +48% | +9% |
| 8 | LEN | Lennar | Consumer Discretionary | 2018-12 | 33 | -46% | 4% | +46% | +24% | yes | 1.0 | +59% (9.8) | +1% (0.1) | +1% | 47 | +43% | +31% |
| 9 | BWXT | BWX Technologies | Industrials | 2018-12 | 33 | -47% | 57% | +5% | -5% | yes | 1.0 | +69% (11.6) | -0% (0.1) | -0% | 44 | +64% | +31% |
| 10 | AYI | Acuity Brands | Industrials | 2018-04 | 34 | -57% | 11% | +3% | – | yes | 3.6 | +38% (4.7) | -11% (7.8) | -8% | 33 ↓ | +23% | +13% |
| 11 | NXPI | NXP Semiconductors | Information Technology | 2018-10 | 34 | -40% | 15% | -3% | +1005% | yes | 3.2 | +55% (12.0) | -9% (1.8) | -9% | 36 | +53% | +14% |
| 12 | STT | State Street Corporation | Financials | 2018-12 | 34 | -45% | 21% | +9% | +8% | yes | 10.7 | +31% (11.4) | -21% (7.5) | -21% | 32 ↓ | +29% | +31% |
| 13 | VMRK | Vivmark Residential | Real Estate | 2018-02 | 34 | -32% | 74% | +2% | -86% | yes | 5.1 | +37% (11.8) | -0% (0.1) | -0% | 44 | +36% | +5% |
| 14 | OC | Owens Corning | Industrials | 2018-10 | 34 | -51% | 20% | +13% | -1% | yes | 7.9 | +37% (11.7) | -13% (1.8) | -13% | 34 | +32% | +14% |
| 15 | ECHO | EchoStar | Communication Services | 2018-10 | 35 | -35% | 50% | – | +230% | yes | 10.4 | +23% (10.8) | -17% (1.8) | -17% | 32 ↓ | +19% | +14% |
| 16 | VC | Visteon | Consumer Discretionary | 2018-11 | 35 | -48% | 55% | -1% | +14% | yes | 2.7 | +30% (11.2) | -40% (6.0) | -22% | 30 ↓ | +27% | +16% |


#### 2019: 2 buys, 1 hit +20%, SPY +31% that year, 12m median +4%, best +28%, worst -20%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IDCC | InterDigital | Information Technology | 2019-08 | 31 | -52% | 89% | -36% | -78% | yes | 2.0 | +37% (11.3) | -31% (6.6) | -1% | 32 | +28% | +22% |
| 2 | DD | DuPont | Industrials | 2019-05 | 35 | -41% | 67% | +19% | – | **no** | – | +18% (0.1) | -55% (9.8) | -55% | 24 ↓ | -20% | +13% |


#### 2020: 18 buys, 18 hit +20%, SPY +18% that year, 12m median +91%, best +195%, worst +48%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RGA | Reinsurance Group of America | Financials | 2020-03 | 25 | -50% | 15% | +11% | +24% | yes | 0.3 | +64% (11.5) | -19% (3.3) | -7% | 30 | +54% | +56% |
| 2 | GHC | Graham Holdings | Consumer Discretionary | 2020-03 | 25 | -55% | 37% | +9% | +22% | yes | 3.7 | +84% (10.8) | -7% (1.4) | -7% | 29 | +67% | +56% |
| 3 | OKE | Oneok | Energy | 2020-03 | 26 | -72% | 38% | -19% | +10% | yes | 0.3 | +166% (11.4) | -12% (0.0) | -12% | 32 | +162% | +56% |
| 4 | WTFC | Wintrust Financial | Financials | 2020-03 | 27 | -67% | 5% | +6% | +3% | yes | 0.3 | +162% (11.5) | -11% (0.5) | -7% | 35 | +136% | +56% |
| 5 | RCL | Royal Caribbean Group | Consumer Discretionary | 2020-03 | 28 | -76% | 7% | +15% | +5% | yes | 0.3 | +200% (10.8) | -24% (0.1) | -24% | 34 | +166% | +56% |
| 6 | UAL | United Airlines Holdings | Industrials | 2020-03 | 29 | -68% | 5% | +5% | +50% | yes | 2.1 | +98% (11.5) | -37% (1.5) | -37% | 28 ↓ | +82% | +56% |
| 7 | DRI | Darden Restaurants | Consumer Discretionary | 2020-03 | 29 | -58% | 9% | +4% | -4% | yes | 0.7 | +175% (11.8) | -19% (0.1) | -19% | 39 | +162% | +56% |
| 8 | HXL | Hexcel | Industrials | 2020-03 | 30 | -57% | 9% | +8% | – | yes | 2.1 | +73% (11.5) | -28% (1.4) | -28% | 29 ↓ | +51% | +56% |
| 9 | AFG | American Financial Group | Financials | 2020-03 | 30 | -42% | 19% | +15% | +68% | yes | 7.3 | +78% (11.6) | -22% (1.5) | -22% | 26 ↓ | +71% | +56% |
| 10 | MPC | Marathon Petroleum | Energy | 2020-03 | 30 | -73% | 22% | +29% | -25% | yes | 0.9 | +161% (11.3) | -15% (0.1) | -15% | 37 | +140% | +56% |
| 11 | CFR | Frost Bank | Financials | 2020-03 | 31 | -54% | 0% | +4% | -1% | yes | 0.3 | +117% (11.6) | -4% (0.0) | -4% | 38 | +102% | +56% |
| 12 | PBF | PBF Energy | Energy | 2020-03 | 31 | -87% | 18% | -10% | +140% | yes | 0.9 | +160% (11.4) | -40% (6.9) | -19% | 31 | +100% | +56% |
| 13 | BA | Boeing | Industrials | 2020-03 | 31 | -67% | 80% | -24% | -106% | yes | 2.1 | +80% (11.4) | -20% (1.5) | -20% | 30 ↓ | +71% | +56% |
| 14 | AFL | Aflac | Financials | 2020-03 | 31 | -40% | 18% | +3% | +18% | yes | 2.3 | +57% (11.5) | -7% (0.1) | -7% | 33 | +54% | +56% |
| 15 | L | Loews Corporation | Financials | 2020-03 | 31 | -39% | 0% | +6% | +54% | yes | 7.3 | +53% (11.6) | -17% (1.4) | -17% | 30 ↓ | +48% | +56% |
| 16 | TNL | Travel + Leisure Co. | Consumer Discretionary | 2020-03 | 31 | -62% | 26% | +3% | -19% | yes | 1.0 | +212% (11.5) | -14% (0.1) | -14% | 36 | +193% | +56% |
| 17 | TRV | Travelers Companies (The) | Financials | 2020-03 | 32 | -36% | 0% | +4% | +7% | yes | 2.2 | +63% (11.5) | -10% (1.4) | -10% | 33 | +55% | +56% |
| 18 | EWBC | East West Bancorp | Financials | 2020-03 | 32 | -65% | 0% | +3% | -4% | yes | 0.3 | +213% (11.6) | -11% (0.1) | -11% | 40 | +195% | +56% |


#### 2021: 1 buys, 1 hit +20%, SPY +29% that year, 12m median +12%, best +12%, worst +12%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HAE | Haemonetics | Health Care | 2021-05 | 35 | -60% | 53% | -12% | +5% | yes | 0.9 | +32% (5.2) | -22% (7.9) | -2% | 36 | +12% | -0% |


#### 2022: 17 buys, 14 hit +20%, SPY -18% that year, 12m median +45%, best +81%, worst -34%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | Communication Services | 2022-04 | 29 | -73% | 15% | +15% | +33% | yes | 3.2 | +93% (8.9) | -13% (0.4) | -13% | 29 ↓ | +73% | +3% |
| 2 | CMCSA | Comcast | Communication Services | 2022-09 | 30 | -53% | 9% | +12% | +15% | yes | 1.7 | +66% (11.0) | -1% (0.4) | -1% | 34 | +56% | +22% |
| 3 | PEGA | Pegasystems | Information Technology | 2022-05 | 30 | -67% | 47% | +20% | – | **no** | – | +10% (0.1) | -39% (4.4) | -39% | 26 ↓ | -2% | +3% |
| 4 | CHTR | Charter Communications | Communication Services | 2022-09 | 31 | -63% | 5% | +6% | +59% | yes | 0.9 | +50% (11.6) | +1% (2.5) | +1% | 36 | +45% | +22% |
| 5 | SWKS | Skyworks Solutions | Information Technology | 2022-06 | 32 | -55% | 14% | +21% | +14% | yes | 1.1 | +34% (7.3) | -14% (3.4) | -2% | 33 | +22% | +19% |
| 6 | DIS | Walt Disney Company (The) | Communication Services | 2022-06 | 33 | -54% | 34% | +31% | – | yes | 1.4 | +32% (1.5) | -11% (5.9) | -3% | 36 | -5% | +19% |
| 7 | XYZ | Block, Inc. | Financials | 2022-06 | 33 | -79% | 33% | +26% | -117% | yes | 0.7 | +46% (1.1) | -16% (3.5) | +2% | 34 | +8% | +19% |
| 8 | META | Meta Platforms | Communication Services | 2022-06 | 33 | -58% | 2% | +27% | +13% | yes | 8.4 | +79% (11.8) | -45% (4.1) | -45% | 26 ↓ | +78% | +19% |
| 9 | BURL | Burlington Stores | Consumer Discretionary | 2022-06 | 33 | -62% | 31% | +27% | -14% | yes | 1.4 | +72% (7.1) | -19% (3.0) | +1% | 31 ↓ | +16% | +19% |
| 10 | ALGN | Align Technology | Health Care | 2022-06 | 33 | -68% | 13% | +43% | +56% | yes | 0.7 | +53% (9.8) | -26% (4.3) | +4% | 33 ↓ | +49% | +19% |
| 11 | RH | RH | Consumer Discretionary | 2022-06 | 34 | -71% | 16% | +19% | +110% | yes | 0.2 | +64% (7.1) | +4% (0.0) | +4% | 38 | +55% | +19% |
| 12 | MDT | Medtronic | Health Care | 2022-09 | 34 | -41% | 12% | -2% | +35% | **no** | – | +15% (6.9) | -6% (1.9) | -6% | 35 | +0% | +22% |
| 13 | GWRE | Guidewire Software | Information Technology | 2022-09 | 34 | -54% | 2% | +9% | – | yes | 4.1 | +53% (11.3) | -15% (1.3) | -15% | 33 ↓ | +46% | +22% |
| 14 | ALLY | Ally Financial | Financials | 2022-12 | 34 | -57% | 8% | +5% | -27% | yes | 0.7 | +50% (11.9) | -8% (2.5) | -0% | 39 | +49% | +26% |
| 15 | TRU | TransUnion | Industrials | 2022-09 | 34 | -53% | 8% | +17% | +175% | yes | 3.9 | +39% (11.0) | -14% (1.1) | -14% | 34 ↓ | +21% | +22% |
| 16 | PYPL | PayPal | Financials | 2022-02 | 34 | -64% | 25% | +18% | -1% | **no** | – | +9% (1.1) | -40% (10.0) | -40% | 29 ↓ | -34% | -8% |
| 17 | AMZN | Amazon | Consumer Discretionary | 2022-12 | 34 | -55% | 14% | +10% | -57% | yes | 0.9 | +83% (11.6) | -1% (0.2) | -1% | 40 | +81% | +26% |


#### 2023: 16 buys, 13 hit +20%, SPY +26% that year, 12m median +37%, best +87%, worst -2%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RVTY | Revvity | Health Care | 2023-10 | 32 | -59% | 49% | – | +22% | yes | 1.4 | +55% (11.0) | -0% (0.0) | -0% | 35 | +44% | +38% |
| 2 | UMBF | UMB Financial Corp. | Financials | 2023-03 | 32 | -49% | 18% | – | +22% | yes | 3.6 | +54% (11.9) | -6% (1.1) | -6% | 34 | +54% | +30% |
| 3 | CPT | Camden Property Trust | Real Estate | 2023-10 | 33 | -53% | 58% | -53% | -73% | yes | 1.4 | +54% (10.8) | -0% (0.0) | -0% | 36 | +42% | +38% |
| 4 | MAA | Mid-America Apartment Communities | Real Estate | 2023-10 | 33 | -49% | 23% | +9% | -8% | yes | 7.5 | +46% (10.5) | -0% (0.0) | -0% | 36 | +34% | +38% |
| 5 | UDR | UDR, Inc. | Real Estate | 2023-10 | 33 | -48% | 9% | +10% | +176% | yes | 1.4 | +53% (10.4) | -1% (0.0) | -1% | 36 | +38% | +38% |
| 6 | BIO | Bio-Rad Laboratories | Health Care | 2023-10 | 33 | -67% | 44% | -3% | – | yes | 3.0 | +30% (12.0) | -4% (8.0) | +1% | 36 | +30% | +38% |
| 7 | EXR | Extra Space Storage | Real Estate | 2023-10 | 33 | -55% | 7% | +15% | -8% | yes | 0.5 | +84% (10.8) | -0% (0.0) | -0% | 44 | +64% | +38% |
| 8 | SUI | Sun Communities | Real Estate | 2023-10 | 33 | -47% | 21% | +21% | -33% | yes | 1.4 | +36% (10.4) | +2% (6.0) | +2% | 38 | +23% | +38% |
| 9 | WAL | Western Alliance Bancorporation | Financials | 2023-03 | 34 | -72% | 17% | +17% | +12% | yes | 3.6 | +103% (10.0) | -49% (1.1) | -49% | 33 ↓ | +87% | +30% |
| 10 | PFE | Pfizer | Health Care | 2023-10 | 34 | -50% | 12% | -23% | -27% | **no** | – | +9% (9.0) | -15% (5.8) | -15% | 29 ↓ | -2% | +38% |
| 11 | FFIN | First Financial Bankshares | Financials | 2023-04 | 34 | -47% | 28% | – | +3% | **no** | – | +15% (9.0) | -20% (5.7) | -20% | 31 ↓ | +4% | +22% |
| 12 | CCI | Crown Castle | Real Estate | 2023-07 | 35 | -48% | 10% | +6% | +15% | **no** | – | +11% (4.0) | -19% (2.6) | -19% | 31 ↓ | +8% | +22% |
| 13 | TECH | Bio-Techne | Health Care | 2023-10 | 35 | -60% | 34% | +3% | +6% | yes | 1.2 | +55% (6.4) | -3% (0.0) | -3% | 40 | +36% | +38% |
| 14 | PNFP | Pinnacle Financial Partners | Financials | 2023-04 | 35 | -51% | – | – | – | yes | 2.6 | +71% (9.0) | -14% (0.1) | -14% | 32 ↓ | +43% | +22% |
| 15 | SBAC | SBA Communications | Real Estate | 2023-09 | 35 | -49% | 8% | +11% | +44% | yes | 1.9 | +28% (3.1) | -6% (7.0) | -5% | 37 | +22% | +36% |
| 16 | PODD | Insulet Corporation | Health Care | 2023-09 | 35 | -53% | 16% | +24% | +73% | yes | 2.0 | +50% (11.8) | -20% (0.4) | -20% | 32 ↓ | +46% | +36% |


#### 2024: 2 buys, 2 hit +20%, SPY +25% that year, 12m median +42%, best +88%, worst -3%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FIVE | Five Below | Consumer Discretionary | 2024-07 | 33 | -69% | 0% | +15% | +11% | yes | 1.4 | +96% (11.9) | -23% (8.2) | -11% | 33 | +88% | +16% |
| 2 | ELV | Elevance Health | Health Care | 2024-12 | 34 | -35% | 49% | +3% | +9% | yes | 3.1 | +23% (3.1) | -25% (7.0) | -1% | 30 ↓ | -3% | +18% |


#### 2025: 13 buys, 9 hit +20%, SPY +18% that year, 12m median +26%, best +163%, worst -21%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MOH | Molina Healthcare | Health Care | 2025-07 | 29 | -63% | 14% | +16% | +10% | yes | 1.8 | +54% (11.4) | -22% (6.4) | -4% | 31 | +24% | +19% |
| 2 | WLK | Westlake Corporation | Materials | 2025-05 | 30 | -56% | 41% | -1% | +50% | yes | 1.3 | +77% (10.2) | -20% (5.7) | -2% | 32 | +25% | +30% |
| 3 | FISV | Fiserv | Financials | 2025-10 | 30 | -72% | 6% | +5% | +25% | open | – | +5% (2.3) | -31% (10.7) | -31% | 29 ↓ | -30% (so far) | +14% (so far) |
| 4 | CHRD | Chord Energy | Energy | 2025-04 | 31 | -53% | 13% | +35% | -32% | yes | 1.6 | +71% (11.0) | -3% (6.2) | -0% | 31 ↓ | +70% | +31% |
| 5 | IT | Gartner | Information Technology | 2025-08 | 32 | -57% | 14% | +6% | +61% | **no** | – | +5% (0.9) | -50% (9.7) | -50% | 27 ↓ | -21% | +20% |
| 6 | REGN | Regeneron Pharmaceuticals | Health Care | 2025-05 | 32 | -60% | 7% | +8% | +16% | yes | 2.7 | +66% (7.3) | -1% (0.2) | -1% | 35 | +26% | +30% |
| 7 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2025-10 | 34 | -54% | 12% | +7% | +5% | yes | 2.2 | +29% (2.8) | -11% (7.1) | -6% | 37 | -1% (so far) | +14% (so far) |
| 8 | REXR | Rexford Industrial Realty | Real Estate | 2025-04 | 34 | -61% | 5% | +18% | +13% | yes | 3.6 | +37% (5.7) | +0% (0.0) | +0% | 36 | +14% | +31% |
| 9 | PBF | PBF Energy | Energy | 2025-04 | 34 | -73% | 27% | -14% | -128% | yes | 0.4 | +210% (10.9) | -3% (0.0) | -3% | 36 | +163% | +31% |
| 10 | CDW | CDW Corporation | Information Technology | 2025-12 | 34 | -48% | 31% | +6% | -3% | open | – | +15% (8.1) | -27% (4.3) | -27% | 30 ↓ | +1% (so far) | +14% (so far) |
| 11 | MRK | Merck & Co. | Health Care | 2025-04 | 34 | -37% | 28% | +7% | +4714% | yes | 6.8 | +50% (11.3) | -14% (0.5) | -14% | 30 ↓ | +33% | +31% |
| 12 | KBR | KBR, Inc. | Industrials | 2025-12 | 34 | -45% | 50% | +9% | +23% | open | – | +12% (0.5) | -25% (4.4) | -25% | 31 ↓ | -13% (so far) | +14% (so far) |
| 13 | CHE | Chemed Corp. | Health Care | 2025-07 | 35 | -37% | 49% | +8% | -2% | yes | 11.4 | +32% (11.9) | -10% (7.9) | -10% | 33 ↓ | +30% | +19% |


#### 2026: 18 buys, 10 hit +20%, SPY +13% that year

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HRB | H&R Block | Consumer Discretionary | 2026-02 | 30 | -55% | 15% | +5% | +20% | yes | 2.2 | +81% (5.4) | -3% (2.2) | -3% | 31 | +42% (so far) | +13% (so far) |
| 2 | BR | Broadridge Financial Solutions | Industrials | 2026-03 | 32 | -40% | 38% | +7% | +41% | open | – | +15% (4.8) | -16% (3.0) | -16% | 26 ↓ | +2% (so far) | +19% (so far) |
| 3 | TYL | Tyler Technologies | Information Technology | 2026-01 | 32 | -44% | 26% | +11% | +31% | open | – | +3% (7.1) | -25% (4.7) | -25% | 26 ↓ | -12% (so far) | +12% (so far) |
| 4 | BSX | Boston Scientific | Health Care | 2026-03 | 32 | -43% | 30% | +20% | +55% | open | – | +5% (0.8) | -32% (3.4) | -32% | 24 ↓ | -30% (so far) | +19% (so far) |
| 5 | PTC | PTC Inc. | Information Technology | 2026-06 | 32 | -48% | 19% | +28% | +186% | yes | 1.0 | +40% (1.9) | -0% (0.8) | -0% | 42 | +22% (so far) | +4% (so far) |
| 6 | PNR | Pentair | Industrials | 2026-08 | 33 | -47% | 29% | +3% | +11% | open | – | -0% (0.0) | -12% (0.8) | -12% | – | -11% (so far) | +1% (so far) |
| 7 | BRO | Brown & Brown | Financials | 2026-04 | 33 | -52% | 46% | +29% | -14% | yes | 2.9 | +25% (3.0) | -9% (0.4) | -9% | 31 ↓ | +2% (so far) | +8% (so far) |
| 8 | EXLS | EXL Service | Industrials | 2026-06 | 33 | -51% | 9% | +13% | +19% | yes | 1.0 | +48% (1.9) | +4% (0.0) | +4% | 47 | +34% (so far) | +4% (so far) |
| 9 | TSCO | Tractor Supply | Consumer Discretionary | 2026-04 | 33 | -45% | 16% | +4% | +1% | open | – | +5% (3.4) | -16% (1.1) | -16% | 30 ↓ | -7% (so far) | +8% (so far) |
| 10 | INTU | Intuit | Information Technology | 2026-02 | 33 | -50% | 37% | +17% | +44% | open | – | +18% (0.2) | -37% (3.8) | -37% | 27 ↓ | -32% (so far) | +13% (so far) |
| 11 | LDOS | Leidos | Industrials | 2026-06 | 33 | -50% | 29% | +2% | +10% | yes | 1.1 | +42% (1.6) | +0% (0.0) | +0% | 39 | +20% (so far) | +4% (so far) |
| 12 | NOW | ServiceNow | Information Technology | 2026-02 | 34 | -55% | 7% | +21% | +21% | yes | 3.1 | +37% (6.0) | -23% (1.3) | -23% | 30 ↓ | +26% (so far) | +13% (so far) |
| 13 | TTD | Trade Desk (The) | Communication Services | 2026-02 | 34 | -83% | 10% | +18% | +15% | yes | 0.2 | +25% (0.2) | -47% (6.9) | +2% | 31 ↓ | -47% (so far) | +13% (so far) |
| 14 | ADP | Automatic Data Processing | Industrials | 2026-02 | 34 | -35% | 41% | +7% | +11% | yes | 4.5 | +36% (5.9) | -11% (1.3) | -11% | 32 ↓ | +26% (so far) | +13% (so far) |
| 15 | CVLT | CommVault Systems | Information Technology | 2026-03 | 34 | -61% | 9% | +22% | -49% | yes | 0.5 | +97% (3.2) | +1% (0.0) | +1% | 42 | +87% (so far) | +19% (so far) |
| 16 | ROL | Rollins, Inc. | Industrials | 2026-07 | 34 | -43% | 14% | +10% | +9% | open | – | +1% (0.1) | -21% (1.8) | -21% | 32 ↓ | -21% (so far) | +4% (so far) |
| 17 | QLYS | Qualys | Information Technology | 2026-03 | 34 | -57% | 2% | +10% | +17% | yes | 1.9 | +123% (4.4) | -13% (0.3) | -13% | 34 ↓ | +96% (so far) | +19% (so far) |
| 18 | ERIE | Erie Indemnity | Financials | 2026-03 | 35 | -54% | 10% | +7% | – | open | – | +8% (4.8) | -17% (2.1) | -17% | 30 ↓ | -10% (so far) | +19% (so far) |
