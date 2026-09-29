# Tier A yearly backtest: former overbought-ATH leader, monthly RSI < 35, quality + cheap

Generated 2026-09-29. Universe: today's S&P 500 + 400 (899 tickers, survivorship bias), monthly candles to 2026-08-31, fundamentals point in time from SEC filings.

**Trigger**: a new all-time high on a monthly candle with monthly RSI(14) ≥ 70 (≥ 5 years of history) arms the stock for 36 months; the first month whose RSI closes below 35 is the buy, at that month's close. **Filters**: quality (profitable TTM and in 2 of the 3 past years, revenue growth ≥ 5%, EPS growing, no one-off gain, no acquisition-driven growth) and cheap (operating multiples in the bottom half of the company's own history). Liquid names only (3-month average dollar volume ≥ $5M). Signals are grouped by calendar year, ranked by signal RSI (lowest first) and cut to the top 20.

**What is measured** over the 12 months after the buy (daily adjusted closes): whether the stock closed ≥ 25% above the buy price ("hit") and how long that took; the highest close vs the buy ("max gain"); the lowest close vs the buy ("max DD", the drawdown from the entry price) and the same measured only up to the hit day ("DD before hit"); whether the monthly RSI printed below the signal RSI afterwards ("RSI went lower", ↓ in the tables, with the RSI low); and the plain 12-month return. Windows that run past Aug 2026 are "open" and show what happened so far.

> Since 2010 every leader + RSI<35 signal that passes the quality filter also passes the cheap filter (valuation percentile ≤ 50%), so "quality" and "quality + cheap" are the same list.


## quality + cheap

57 signals since 2010, 57 after the top-20 cut per year (the cap never bound).

### Summary by year

| Year | Buys | Hit +25% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | Max gain (median) | Max DD (median / worst) | DD before hit (median) | RSI went lower | 12m return (median) | Misses | Miss DD (median / worst) | Miss 12m return (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | 1 | 1/1 = 100% | 1.9 / 1.9 / 1.9 | 100% / 100% | +36% | +4% / +4% | +4% | 0% | +25% | 0/1 = 0% | – / – | – |
| 2011 | 2 | 2/2 = 100% | 3.2 / 3.2 / 3.6 | 50% / 100% | +72% | -10% / -15% | -10% | 50% | +37% | 0/2 = 0% | – / – | – |
| 2012 | 1 | 1/1 = 100% | 5.5 / 5.5 / 5.5 | 0% / 100% | +30% | +0% / +0% | +0% | 0% | +16% | 0/1 = 0% | – / – | – |
| 2013 | 0 | | | | | | | | | | | |
| 2014 | 0 | | | | | | | | | | | |
| 2015 | 1 | 0/1 = 0% | – / – / – | 0% / 0% | +18% | -19% / -19% | – | 100% | -2% | 1/1 = 100% | -19% / -19% | -2% |
| 2016 | 2 | 2/2 = 100% | 1.8 / 1.8 / 2.6 | 100% / 100% | +93% | -5% / -5% | -5% | 0% | +86% | 0/2 = 0% | – / – | – |
| 2017 | 2 | 2/2 = 100% | 4.5 / 4.5 / 6.0 | 0% / 100% | +61% | -5% / -9% | -5% | 50% | +54% | 0/2 = 0% | – / – | – |
| 2018 | 4 | 4/4 = 100% | 3.2 / 4.8 / 11.2 | 50% / 75% | +46% | -13% / -26% | -5% | 50% | +39% | 0/4 = 0% | – / – | – |
| 2019 | 1 | 1/1 = 100% | 7.5 / 7.5 / 7.5 | 0% / 0% | +51% | -18% / -18% | -6% | 0% | +24% | 0/1 = 0% | – / – | – |
| 2020 | 11 | 11/11 = 100% | 1.9 / 1.5 / 2.3 | 100% / 100% | +76% | -11% / -24% | -8% | 27% | +68% | 0/11 = 0% | – / – | – |
| 2021 | 0 | | | | | | | | | | | |
| 2022 | 11 | 10/11 = 91% | 3.5 / 4.2 / 8.5 | 36% / 55% | +60% | -4% / -45% | -4% | 36% | +55% | 1/11 = 9% | -29% / -29% | -8% |
| 2023 | 5 | 4/5 = 80% | 3.0 / 3.6 / 6.2 | 40% / 60% | +50% | -19% / -49% | -13% | 60% | +38% | 1/5 = 20% | -19% / -19% | +8% |
| 2024 | 1 | 1/1 = 100% | 1.4 / 1.4 / 1.4 | 100% / 100% | +96% | -23% / -23% | -11% | 0% | +88% | 0/1 = 0% | – / – | – |
| 2025 | 5 (3 open) | 3/5 = 60% | 2.3 / 2.8 / 3.9 | 40% / 60% | +29% | -22% / -31% | -4% | 40% | +19% | 0/2 = 0% | – / – | – |
| 2026 | 10 (10 open) | 5/10 = 50% | 2.0 / 2.2 / 4.9 | 30% / 50% | +21% | -22% / -47% | -11% | 90% | – | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-08)** | 44 | 41/44 = 93% | 2.3 / 3.3 / 11.2 | 57% / 77% | +59% | -9% / -49% | -7% | 34% | +52% | 3/44 = 7% | -19% / -29% | -2% |
| **All incl. open** | 57 (13 open) | 47/57 = 82% | 2.3 / 3.1 / 11.2 | 51% / 70% | +51% | -13% / -49% | -7% | 46% | +52% | 3/44 = 7% | -19% / -29% | -2% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months from the signal month-end. "RSI went lower" = share of buys whose monthly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 1 buys, 1 hit +25%, median max gain +36%, median max DD +4%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GILD | Gilead Sciences | 2010-08 | 35 | -45% | 0% | +23% | +60% | yes | 1.9 | +36% (10.7) | +4% (0.0) | +4% | 41 | +25% |


#### 2011: 2 buys, 2 hit +25%, median max gain +72%, median max DD -10%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLB | Dolby | 2011-09 | 31 | -61% | 0% | +9% | +15% | yes | 3.6 | +64% (7.5) | -4% (0.1) | -4% | 33 | +19% |
| 2 | ILMN | Illumina, Inc. | 2011-10 | 35 | -61% | 0% | +44% | +50% | yes | 2.8 | +80% (2.8) | -15% (1.4) | -15% | 33 ↓ | +55% |


#### 2012: 1 buys, 1 hit +25%, median max gain +30%, median max DD +0%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CHRW | C.H. Robinson | 2012-07 | 33 | -36% | 0% | +10% | +11% | yes | 5.5 | +30% (6.0) | +0% (0.0) | +0% | 40 | +16% |


#### 2015: 1 buys, 0 hit +25%, median max gain +18%, median max DD -19%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PII | Polaris | 2015-12 | 31 | -46% | 14% | +14% | +13% | **no** | – | +18% (3.8) | -19% (0.9) | -19% | 28 ↓ | -2% |


#### 2016: 2 buys, 2 hit +25%, median max gain +93%, median max DD -5%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CFR | Frost Bank | 2016-01 | 33 | -42% | 14% | +8% | +8% | yes | 2.6 | +103% (11.9) | -5% (0.1) | -5% | 33 | +93% |
| 2 | PAG | Penske Automotive Group | 2016-01 | 33 | -42% | 10% | +8% | +20% | yes | 1.1 | +84% (10.2) | -4% (0.1) | -4% | 37 | +78% |


#### 2017: 2 buys, 2 hit +25%, median max gain +61%, median max DD -5%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TSCO | Tractor Supply | 2017-05 | 34 | -43% | 19% | +8% | +5% | yes | 6.0 | +51% (7.7) | -9% (1.4) | -9% | 33 ↓ | +37% |
| 2 | ORLY | O'Reilly Automotive | 2017-08 | 34 | -33% | 22% | +6% | +14% | yes | 3.1 | +71% (12.0) | +0% (0.4) | +0% | 41 | +71% |


#### 2018: 4 buys, 4 hit +25%, median max gain +46%, median max DD -13%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SNX | TD Synnex | 2018-10 | 33 | -45% | 38% | +27% | +2% | yes | 2.4 | +57% (11.9) | -6% (0.9) | -6% | 35 | +54% |
| 2 | EPR | EPR Properties | 2018-03 | 33 | -35% | 18% | +17% | +4% | yes | 4.1 | +49% (11.9) | -4% (0.8) | -4% | 33 ↓ | +48% |
| 3 | STT | State Street Corporation | 2018-12 | 34 | -45% | 21% | +9% | +8% | yes | 11.2 | +31% (11.4) | -21% (7.5) | -21% | 32 ↓ | +29% |
| 4 | PVH | PVH Corp. | 2018-12 | 35 | -45% | 5% | +13% | +32% | yes | 1.7 | +43% (3.7) | -26% (7.7) | -2% | 36 | +13% |


#### 2019: 1 buys, 1 hit +25%, median max gain +51%, median max DD -18%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ALB | Albemarle Corporation | 2019-05 | 34 | -56% | 19% | +7% | +1210% | yes | 7.5 | +51% (8.7) | -18% (9.8) | -6% | 36 | +24% |


#### 2020: 11 buys, 11 hit +25%, median max gain +76%, median max DD -11%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RGA | Reinsurance Group of America | 2020-03 | 25 | -50% | 15% | +11% | +24% | yes | 0.3 | +64% (11.5) | -19% (3.3) | -7% | 30 | +54% |
| 2 | WTFC | Wintrust Financial | 2020-03 | 27 | -67% | 5% | +6% | +3% | yes | 1.0 | +162% (11.5) | -11% (0.5) | -11% | 35 | +136% |
| 3 | RCL | Royal Caribbean Group | 2020-03 | 28 | -76% | 7% | +15% | +5% | yes | 0.3 | +200% (10.8) | -24% (0.1) | -24% | 34 | +166% |
| 4 | UDR | UDR, Inc. | 2020-09 | 32 | -36% | 19% | +13% | +9% | yes | 2.1 | +77% (9.9) | -8% (0.9) | -8% | 30 ↓ | +68% |
| 5 | WWD | Woodward, Inc. | 2020-03 | 33 | -54% | 17% | +18% | +24% | yes | 2.1 | +115% (9.2) | -14% (0.1) | -14% | 33 | +104% |
| 6 | ACGL | Arch Capital Group | 2020-04 | 33 | -50% | 12% | +27% | +124% | yes | 1.1 | +68% (11.9) | -7% (0.4) | -7% | 41 | +65% |
| 7 | THG | Hanover Insurance | 2020-03 | 33 | -37% | 40% | +9% | +15% | yes | 2.3 | +51% (11.6) | -7% (0.1) | -7% | 37 | +46% |
| 8 | GD | General Dynamics | 2020-03 | 34 | -42% | 41% | +9% | +7% | yes | 2.3 | +43% (11.9) | -7% (1.2) | -7% | 33 ↓ | +41% |
| 9 | FNF | Fidelity National Financial | 2020-03 | 34 | -50% | 18% | +12% | +69% | yes | 1.9 | +76% (11.5) | -7% (0.1) | -7% | 37 | +70% |
| 10 | MTN | Vail Resorts | 2020-03 | 34 | -51% | 27% | +13% | +13% | yes | 1.6 | +116% (10.8) | -11% (0.1) | -11% | 40 | +97% |
| 11 | MOG-A | Moog Inc. | 2020-03 | 34 | -49% | 13% | +8% | +37% | yes | 2.2 | +73% (11.4) | -21% (1.4) | -21% | 34 ↓ | +66% |


#### 2022: 11 buys, 10 hit +25%, median max gain +60%, median max DD -4%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | 2022-04 | 29 | -73% | 15% | +15% | +33% | yes | 3.4 | +93% (8.9) | -13% (0.4) | -13% | 29 ↓ | +73% |
| 2 | CMCSA | Comcast | 2022-09 | 30 | -53% | 9% | +12% | +15% | yes | 2.0 | +66% (11.0) | -1% (0.4) | -1% | 34 | +56% |
| 3 | CHTR | Charter Communications | 2022-09 | 31 | -63% | 5% | +6% | +59% | yes | 1.4 | +50% (11.6) | +1% (2.5) | +1% | 36 | +45% |
| 4 | SWKS | Skyworks Solutions | 2022-06 | 32 | -55% | 14% | +21% | +14% | yes | 7.3 | +34% (7.3) | -14% (3.4) | -14% | 33 | +22% |
| 5 | META | Meta Platforms | 2022-06 | 33 | -58% | 2% | +27% | +13% | yes | 8.5 | +79% (11.8) | -45% (4.1) | -45% | 26 ↓ | +78% |
| 6 | ALGN | Align Technology | 2022-06 | 33 | -68% | 13% | +43% | +56% | yes | 7.1 | +53% (9.8) | -26% (4.3) | -26% | 33 ↓ | +49% |
| 7 | RH | RH | 2022-06 | 34 | -71% | 16% | +19% | +110% | yes | 0.5 | +64% (7.1) | +4% (0.0) | +4% | 38 | +55% |
| 8 | FIS | Fidelity National Information Services | 2022-12 | 35 | -57% | 34% | +7% | +325% | **no** | – | +15% (1.1) | -29% (9.9) | -29% | 32 ↓ | -8% |
| 9 | PNR | Pentair | 2022-09 | 35 | -49% | 21% | +18% | +19% | yes | 3.6 | +80% (10.2) | -3% (0.7) | -3% | 38 | +62% |
| 10 | CGNX | Cognex | 2022-06 | 35 | -58% | 33% | +22% | +22% | yes | 6.5 | +35% (7.1) | -4% (3.5) | -4% | 37 | +32% |
| 11 | LII | Lennox International | 2022-06 | 35 | -42% | 38% | +11% | +12% | yes | 1.4 | +60% (12.0) | +3% (0.0) | +3% | 41 | +60% |


#### 2023: 5 buys, 4 hit +25%, median max gain +50%, median max DD -19%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UDR | UDR, Inc. | 2023-10 | 33 | -48% | 9% | +10% | +176% | yes | 6.2 | +53% (10.4) | -1% (0.0) | -1% | 36 | +38% |
| 2 | WAL | Western Alliance Bancorporation | 2023-03 | 34 | -72% | 17% | +17% | +12% | yes | 3.6 | +103% (10.0) | -49% (1.1) | -49% | 33 ↓ | +87% |
| 3 | CCI | Crown Castle | 2023-07 | 35 | -48% | 10% | +6% | +15% | **no** | – | +11% (4.0) | -19% (2.6) | -19% | 31 ↓ | +8% |
| 4 | SBAC | SBA Communications | 2023-09 | 35 | -49% | 8% | +11% | +44% | yes | 2.0 | +28% (3.1) | -6% (7.0) | -5% | 37 | +22% |
| 5 | PODD | Insulet Corporation | 2023-09 | 35 | -53% | 16% | +24% | +73% | yes | 2.4 | +50% (11.8) | -20% (0.4) | -20% | 32 ↓ | +46% |


#### 2024: 1 buys, 1 hit +25%, median max gain +96%, median max DD -23%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FIVE | Five Below | 2024-07 | 33 | -69% | 0% | +15% | +11% | yes | 1.4 | +96% (11.9) | -23% (8.2) | -11% | 33 | +88% |


#### 2025: 5 buys, 3 hit +25%, median max gain +29%, median max DD -22%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MOH | Molina Healthcare | 2025-07 | 29 | -63% | 14% | +16% | +10% | yes | 2.1 | +54% (11.4) | -22% (6.4) | -4% | 31 | +24% |
| 2 | FISV | Fiserv | 2025-10 | 30 | -72% | 6% | +5% | +25% | open | – | +5% (2.3) | -31% (10.7) | -31% | 29 ↓ | -30% (so far) |
| 3 | CMG | Chipotle Mexican Grill | 2025-10 | 34 | -54% | 12% | +7% | +5% | yes | 2.3 | +29% (2.8) | -11% (7.1) | -6% | 37 | -1% (so far) |
| 4 | REXR | Rexford Industrial Realty | 2025-04 | 34 | -61% | 5% | +18% | +13% | yes | 3.9 | +37% (5.7) | +0% (0.0) | +0% | 36 | +14% |
| 5 | KBR | KBR, Inc. | 2025-12 | 34 | -45% | 50% | +9% | +23% | open | – | +12% (0.5) | -25% (4.4) | -25% | 31 ↓ | -13% (so far) |


#### 2026: 10 buys, 5 hit +25%, median max gain +21%, median max DD -22%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BR | Broadridge Financial Solutions | 2026-03 | 32 | -40% | 38% | +7% | +41% | open | – | +15% (4.8) | -16% (3.0) | -16% | 26 ↓ | +2% (so far) |
| 2 | TYL | Tyler Technologies | 2026-01 | 32 | -44% | 26% | +11% | +31% | open | – | +3% (7.1) | -25% (4.7) | -25% | 26 ↓ | -12% (so far) |
| 3 | BSX | Boston Scientific | 2026-03 | 32 | -43% | 30% | +20% | +55% | open | – | +5% (0.8) | -32% (3.4) | -32% | 24 ↓ | -30% (so far) |
| 4 | EXLS | EXL Service | 2026-06 | 33 | -51% | 9% | +13% | +19% | yes | 1.0 | +48% (1.9) | +4% (0.0) | +4% | 47 | +34% (so far) |
| 5 | INTU | Intuit | 2026-02 | 33 | -50% | 37% | +17% | +44% | open | – | +18% (0.2) | -37% (3.8) | -37% | 27 ↓ | -32% (so far) |
| 6 | NOW | ServiceNow | 2026-02 | 34 | -55% | 7% | +21% | +21% | yes | 3.1 | +37% (6.0) | -23% (1.3) | -23% | 30 ↓ | +26% (so far) |
| 7 | TTD | Trade Desk (The) | 2026-02 | 34 | -83% | 10% | +18% | +15% | yes | 0.2 | +25% (0.2) | -47% (6.9) | +2% | 31 ↓ | -47% (so far) |
| 8 | ADP | Automatic Data Processing | 2026-02 | 34 | -35% | 41% | +7% | +11% | yes | 4.9 | +36% (5.9) | -11% (1.3) | -11% | 32 ↓ | +26% (so far) |
| 9 | ROL | Rollins, Inc. | 2026-07 | 34 | -43% | 14% | +10% | +9% | open | – | +1% (0.1) | -21% (1.8) | -21% | 32 ↓ | -21% (so far) |
| 10 | QLYS | Qualys | 2026-03 | 34 | -57% | 2% | +10% | +17% | yes | 2.0 | +123% (4.4) | -13% (0.3) | -13% | 34 ↓ | +96% (so far) |


## no fundamentals filter

259 signals since 2010, 182 after the top-20 cut per year (the cap bound in 2015, 2018, 2020, 2022, 2026).

### Summary by year

| Year | Buys | Hit +25% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | Max gain (median) | Max DD (median / worst) | DD before hit (median) | RSI went lower | 12m return (median) | Misses | Miss DD (median / worst) | Miss 12m return (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | 4 | 3/4 = 75% | 4.3 / 4.2 / 6.5 | 25% / 50% | +41% | -2% / -12% | -1% | 50% | +35% | 1/4 = 25% | -12% / -12% | +8% |
| 2011 | 2 | 2/2 = 100% | 3.2 / 3.2 / 3.6 | 50% / 100% | +72% | -10% / -15% | -10% | 50% | +37% | 0/2 = 0% | – / – | – |
| 2012 | 1 | 1/1 = 100% | 5.5 / 5.5 / 5.5 | 0% / 100% | +30% | +0% / +0% | +0% | 0% | +16% | 0/1 = 0% | – / – | – |
| 2013 | 1 | 1/1 = 100% | 6.2 / 6.2 / 6.2 | 0% / 0% | +54% | -7% / -7% | -7% | 100% | +54% | 0/1 = 0% | – / – | – |
| 2014 | 2 | 2/2 = 100% | 6.9 / 6.9 / 7.9 | 0% / 0% | +40% | -0% / -3% | -0% | 0% | +19% | 0/2 = 0% | – / – | – |
| 2015 | 20 | 13/20 = 65% | 6.8 / 5.7 / 8.7 | 15% / 30% | +31% | -14% / -57% | -10% | 65% | +23% | 7/20 = 35% | -22% / -53% | +9% |
| 2016 | 16 | 15/16 = 94% | 4.4 / 5.4 / 11.8 | 44% / 50% | +46% | -4% / -32% | -3% | 12% | +43% | 1/16 = 6% | -5% / -5% | +15% |
| 2017 | 12 | 10/12 = 83% | 5.5 / 4.8 / 6.8 | 17% / 58% | +45% | -11% / -60% | -5% | 58% | +31% | 2/12 = 17% | -45% / -60% | -24% |
| 2018 | 20 | 16/20 = 80% | 4.0 / 5.1 / 11.2 | 25% / 50% | +35% | -10% / -40% | -6% | 50% | +30% | 4/20 = 20% | -16% / -25% | +15% |
| 2019 | 4 | 3/4 = 75% | 6.9 / 6.7 / 7.5 | 0% / 25% | +35% | -25% / -55% | -3% | 25% | +19% | 1/4 = 25% | -55% / -55% | -20% |
| 2020 | 20 | 19/20 = 95% | 1.6 / 2.3 / 7.6 | 75% / 80% | +108% | -16% / -40% | -14% | 30% | +91% | 1/20 = 5% | -36% / -36% | +11% |
| 2021 | 1 | 1/1 = 100% | 4.0 / 4.0 / 4.0 | 0% / 100% | +32% | -22% / -22% | -2% | 0% | +12% | 0/1 = 0% | – / – | – |
| 2022 | 20 | 16/20 = 80% | 2.7 / 3.4 / 8.5 | 40% / 65% | +48% | -13% / -45% | -2% | 45% | +22% | 4/20 = 20% | -27% / -40% | -2% |
| 2023 | 18 | 13/18 = 72% | 3.6 / 4.1 / 10.2 | 33% / 50% | +48% | -6% / -49% | -1% | 44% | +35% | 5/18 = 28% | -20% / -40% | -2% |
| 2024 | 3 | 2/3 = 67% | 4.4 / 4.4 / 7.4 | 33% / 33% | +67% | -23% / -25% | -12% | 67% | +34% | 1/3 = 33% | -25% / -25% | -3% |
| 2025 | 18 (5 open) | 11/18 = 61% | 2.9 / 4.0 / 11.6 | 33% / 50% | +34% | -17% / -50% | -3% | 56% | +26% | 3/13 = 23% | -36% / -50% | -21% |
| 2026 | 20 (20 open) | 9/20 = 45% | 1.2 / 1.9 / 4.9 | 35% / 45% | +22% | -13% / -47% | -0% | 63% | – | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-08)** | 157 | 127/157 = 81% | 3.9 / 4.4 / 11.8 | 34% / 54% | +48% | -11% / -60% | -5% | 43% | +32% | 30/157 = 19% | -24% / -60% | -0% |
| **All incl. open** | 182 (25 open) | 137/182 = 75% | 3.7 / 4.2 / 11.8 | 34% / 52% | +40% | -12% / -60% | -5% | 46% | +32% | 30/157 = 19% | -24% / -60% | -0% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months from the signal month-end. "RSI went lower" = share of buys whose monthly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 4 buys, 3 hit +25%, median max gain +41%, median max DD -2%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | XOM | ExxonMobil | 2010-06 | 33 | -41% | – | – | – | yes | 4.3 | +57% (10.0) | -1% (0.1) | -1% | 37 | +46% |
| 2 | BAX | Baxter International | 2010-05 | 35 | -41% | 2% | +2% | -16% | yes | 6.5 | +47% (11.6) | -3% (0.3) | -3% | 33 ↓ | +45% |
| 3 | OVV | Ovintiv | 2010-01 | 35 | -69% | – | – | – | **no** | – | +15% (4.5) | -12% (6.8) | -12% | 34 ↓ | +8% |
| 4 | GILD | Gilead Sciences | 2010-08 | 35 | -45% | 0% | +23% | +60% | yes | 1.9 | +36% (10.7) | +4% (0.0) | +4% | 41 | +25% |


#### 2011: 2 buys, 2 hit +25%, median max gain +72%, median max DD -10%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLB | Dolby | 2011-09 | 31 | -61% | 0% | +9% | +15% | yes | 3.6 | +64% (7.5) | -4% (0.1) | -4% | 33 | +19% |
| 2 | ILMN | Illumina, Inc. | 2011-10 | 35 | -61% | 0% | +44% | +50% | yes | 2.8 | +80% (2.8) | -15% (1.4) | -15% | 33 ↓ | +55% |


#### 2012: 1 buys, 1 hit +25%, median max gain +30%, median max DD +0%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CHRW | C.H. Robinson | 2012-07 | 33 | -36% | 0% | +10% | +11% | yes | 5.5 | +30% (6.0) | +0% (0.0) | +0% | 40 | +16% |


#### 2013: 1 buys, 1 hit +25%, median max gain +54%, median max DD -7%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLR | Digital Realty | 2013-10 | 33 | -41% | 0% | +25% | +1% | yes | 6.2 | +54% (12.0) | -7% (1.1) | -7% | 33 ↓ | +54% |


#### 2014: 2 buys, 2 hit +25%, median max gain +40%, median max DD -0%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TPR | Tapestry, Inc. | 2014-06 | 33 | -57% | 7% | -2% | -11% | yes | 7.9 | +30% (8.0) | -3% (4.2) | -3% | 34 | +5% |
| 2 | HAE | Haemonetics | 2014-04 | 34 | -34% | 46% | +14% | -15% | yes | 6.0 | +49% (10.4) | +2% (0.0) | +2% | 44 | +33% |


#### 2015: 20 buys, 13 hit +25%, median max gain +31%, median max DD -14%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | WMT | Walmart | 2015-10 | 30 | -37% | 0% | +1% | -2% | yes | 6.8 | +34% (9.6) | -1% (0.4) | -1% | 33 | +26% |
| 2 | M | Macy's | 2015-11 | 31 | -47% | 27% | -0% | +1% | **no** | – | +20% (11.8) | -22% (5.6) | -22% | 28 ↓ | +12% |
| 3 | PII | Polaris | 2015-12 | 31 | -46% | 14% | +14% | +13% | **no** | – | +18% (3.8) | -19% (0.9) | -19% | 28 ↓ | -2% |
| 4 | HUBB | Hubbell Incorporated | 2015-09 | 31 | -33% | 33% | +5% | -5% | yes | 6.0 | +31% (11.1) | +0% (0.0) | +0% | 40 | +30% |
| 5 | MAT | Mattel | 2015-01 | 32 | -45% | 52% | -7% | -13% | **no** | – | +14% (2.7) | -23% (8.0) | -23% | 27 ↓ | +9% |
| 6 | PVH | PVH Corp. | 2015-12 | 32 | -47% | 17% | -3% | +39% | yes | 2.8 | +55% (9.2) | -10% (0.6) | -10% | 32 ↓ | +23% |
| 7 | OKE | Oneok | 2015-09 | 32 | -55% | 65% | – | -5% | yes | 7.1 | +72% (12.0) | -40% (2.6) | -40% | 28 ↓ | +72% |
| 8 | EMR | Emerson Electric | 2015-08 | 32 | -32% | 14% | -5% | +1% | **no** | – | +22% (10.6) | -10% (4.8) | -10% | 29 ↓ | +15% |
| 9 | LIN | Linde plc | 2015-09 | 33 | -25% | – | – | – | **no** | – | +24% (11.1) | -5% (3.8) | -5% | 36 | +22% |
| 10 | CBT | Cabot Corp | 2015-09 | 33 | -49% | 23% | -15% | -265% | yes | 1.1 | +73% (12.0) | +1% (0.0) | +1% | 41 | +70% |
| 11 | KEX | Kirby Corporation | 2015-09 | 33 | -50% | 17% | +6% | -2% | **no** | – | +17% (8.3) | -26% (3.4) | -26% | 29 ↓ | +0% |
| 12 | WMB | Williams Companies | 2015-12 | 33 | -58% | 59% | +5% | -84% | yes | 8.2 | +34% (11.9) | -57% (1.3) | -57% | 28 ↓ | +31% |
| 13 | R | Ryder | 2015-12 | 33 | -44% | 51% | -1% | -11% | yes | 3.9 | +53% (11.3) | -16% (0.6) | -16% | 31 ↓ | +34% |
| 14 | FLS | Flowserve | 2015-09 | 33 | -50% | 31% | -3% | -20% | yes | 8.2 | +28% (8.3) | -14% (3.6) | -14% | 34 | +19% |
| 15 | VMI | Valmont Industries | 2015-07 | 34 | -33% | 51% | -10% | -41% | yes | 8.7 | +31% (8.9) | -15% (2.0) | -15% | 26 ↓ | +19% |
| 16 | CXT | Crane NXT | 2015-09 | 34 | -39% | 36% | +2% | -11% | yes | 7.9 | +44% (11.0) | -7% (3.7) | -7% | 38 | +38% |
| 17 | EQT | EQT Corporation | 2015-11 | 34 | -49% | 88% | – | -60% | yes | 4.9 | +39% (7.0) | -17% (0.6) | -17% | 32 ↓ | +23% |
| 18 | WYNN | Wynn Resorts | 2015-04 | 34 | -55% | 10% | -3% | +0% | **no** | – | +7% (0.3) | -53% (5.1) | -53% | 25 ↓ | -19% |
| 19 | CVLT | CommVault Systems | 2015-09 | 34 | -62% | 64% | -2% | -81% | yes | 2.1 | +58% (11.9) | -10% (3.8) | +2% | 40 | +56% |
| 20 | OGE | OGE Energy | 2015-11 | 34 | -35% | 65% | -7% | -24% | yes | 7.0 | +30% (9.8) | -8% (1.7) | -8% | 32 ↓ | +26% |


#### 2016: 16 buys, 15 hit +25%, median max gain +46%, median max DD -4%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AXP | American Express | 2016-01 | 26 | -44% | 13% | – | +0% | yes | 7.3 | +48% (11.6) | -4% (0.4) | -4% | 29 | +46% |
| 2 | BWA | BorgWarner | 2016-01 | 27 | -56% | 8% | -4% | -4% | yes | 1.5 | +45% (10.3) | -5% (4.9) | -3% | 32 | +41% |
| 3 | AMG | Affiliated Managers Group | 2016-01 | 32 | -42% | 16% | – | +22% | yes | 2.4 | +33% (2.9) | -12% (0.4) | -12% | 34 | +14% |
| 4 | HRB | H&R Block | 2016-04 | 32 | -46% | 64% | -9% | -40% | yes | 10.5 | +27% (11.9) | -4% (0.4) | -4% | 34 | +27% |
| 5 | AMP | Ameriprise Financial | 2016-02 | 32 | -39% | 35% | -1% | +2% | yes | 8.4 | +62% (12.0) | +3% (3.9) | +3% | 40 | +62% |
| 6 | CFR | Frost Bank | 2016-01 | 33 | -42% | 14% | +8% | +8% | yes | 2.6 | +103% (11.9) | -5% (0.1) | -5% | 33 | +93% |
| 7 | UNP | Union Pacific Corporation | 2016-01 | 33 | -42% | 22% | -3% | +7% | yes | 2.7 | +57% (11.8) | -0% (0.1) | -0% | 40 | +52% |
| 8 | WDC | Western Digital | 2016-01 | 33 | -58% | 38% | -8% | -12% | yes | 7.9 | +73% (11.8) | -25% (3.4) | -25% | 31 ↓ | +73% |
| 9 | CF | CF Industries | 2016-01 | 33 | -57% | 52% | -9% | -31% | yes | 11.8 | +29% (11.8) | -27% (6.1) | -27% | 33 | +23% |
| 10 | DOC | Healthpeak Properties | 2016-02 | 33 | -47% | 53% | +12% | -160% | yes | 4.4 | +41% (6.3) | +4% (0.0) | +4% | 40 | +29% |
| 11 | PAG | Penske Automotive Group | 2016-01 | 33 | -42% | 10% | +8% | +20% | yes | 1.1 | +84% (10.2) | -4% (0.1) | -4% | 37 | +78% |
| 12 | WEX | WEX Inc. | 2016-02 | 34 | -45% | 66% | +5% | -49% | yes | 0.7 | +83% (11.4) | +4% (0.0) | +4% | 46 | +70% |
| 13 | MCK | McKesson Corporation | 2016-10 | 34 | -48% | 16% | +3% | +9% | yes | 6.7 | +33% (8.5) | +2% (0.0) | +2% | 39 | +9% |
| 14 | GWW | W. W. Grainger | 2016-01 | 34 | -29% | 29% | +2% | -1% | yes | 11.6 | +33% (11.9) | -2% (0.1) | -2% | 42 | +31% |
| 15 | STX | Seagate Technology | 2016-01 | 34 | -58% | 67% | -14% | -67% | yes | 1.3 | +69% (12.0) | -32% (3.3) | -2% | 33 ↓ | +69% |
| 16 | WSM | Williams-Sonoma, Inc. | 2016-10 | 35 | -48% | 5% | +5% | +1% | **no** | – | +23% (1.2) | -5% (9.7) | -5% | 39 | +15% |


#### 2017: 12 buys, 10 hit +25%, median max gain +45%, median max DD -11%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PCG | PG&E Corporation | 2017-12 | 31 | -37% | 36% | +4% | +163% | **no** | – | +9% (9.5) | -60% (10.5) | -60% | 23 ↓ | -47% |
| 2 | BBWI | Bath & Body Works, Inc. | 2017-02 | 32 | -48% | 48% | +6% | – | **no** | – | +24% (9.9) | -30% (6.0) | -30% | 28 ↓ | -1% |
| 3 | VFC | VF Corporation | 2017-01 | 33 | -34% | 49% | -1% | +9% | yes | 6.4 | +65% (11.9) | -6% (0.2) | -6% | 35 | +62% |
| 4 | KR | Kroger | 2017-06 | 33 | -45% | 46% | +5% | -22% | yes | 6.6 | +36% (7.0) | -14% (2.9) | -14% | 31 ↓ | +25% |
| 5 | TSCO | Tractor Supply | 2017-05 | 34 | -43% | 19% | +8% | +5% | yes | 6.0 | +51% (7.7) | -9% (1.4) | -9% | 33 ↓ | +37% |
| 6 | TGT | Target Corporation | 2017-06 | 34 | -39% | 32% | -5% | -13% | yes | 5.6 | +57% (11.4) | -4% (0.3) | -4% | 38 | +51% |
| 7 | GILD | Gilead Sciences | 2017-05 | 34 | -47% | 1% | -11% | -19% | yes | 3.0 | +40% (8.0) | -1% (0.3) | -1% | 41 | +7% |
| 8 | ORLY | O'Reilly Automotive | 2017-08 | 34 | -33% | 22% | +6% | +14% | yes | 3.1 | +71% (12.0) | +0% (0.4) | +0% | 41 | +71% |
| 9 | AZO | AutoZone | 2017-06 | 34 | -30% | 17% | +2% | +10% | yes | 5.3 | +40% (6.9) | -14% (0.4) | -14% | 31 ↓ | +18% |
| 10 | CMG | Chipotle Mexican Grill | 2017-09 | 35 | -59% | 67% | – | -30% | yes | 6.8 | +71% (10.5) | -18% (4.5) | -18% | 32 ↓ | +48% |
| 11 | CAH | Cardinal Health | 2017-11 | 35 | -36% | – | – | – | yes | 1.7 | +28% (2.0) | -16% (8.3) | -1% | 33 ↓ | -4% |
| 12 | SAM | Boston Beer Company | 2017-06 | 35 | -59% | 2% | -7% | -1% | yes | 3.2 | +129% (11.9) | -1% (0.8) | -1% | 42 | +127% |


#### 2018: 20 buys, 16 hit +25%, median max gain +35%, median max DD -10%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KDP | Keurig Dr Pepper | 2018-07 | 24 | -81% | 0% | +5% | +39% | yes | 9.4 | +31% (10.6) | -7% (2.2) | -7% | 24 ↓ | +20% |
| 2 | OZK | Bank OZK | 2018-10 | 28 | -52% | – | – | – | yes | 6.0 | +27% (6.1) | -23% (1.6) | -23% | 25 ↓ | +6% |
| 3 | THO | Thor Industries | 2018-12 | 31 | -68% | 0% | +1% | -26% | yes | 0.6 | +50% (11.7) | -17% (7.5) | -2% | 34 | +46% |
| 4 | TCBI | Texas Capital Bancshares | 2018-12 | 32 | -50% | 7% | – | +36% | yes | 3.7 | +30% (4.1) | -0% (9.2) | +1% | 37 | +11% |
| 5 | GIS | General Mills | 2018-03 | 33 | -38% | 43% | -1% | +39% | **no** | – | +20% (11.8) | -16% (8.6) | -16% | 30 ↓ | +20% |
| 6 | SNX | TD Synnex | 2018-10 | 33 | -45% | 38% | +27% | +2% | yes | 2.4 | +57% (11.9) | -6% (0.9) | -6% | 35 | +54% |
| 7 | DY | Dycom Industries | 2018-12 | 33 | -56% | 8% | – | -3% | **no** | – | +18% (1.7) | -25% (7.7) | -25% | 31 ↓ | -13% |
| 8 | EPR | EPR Properties | 2018-03 | 33 | -35% | 18% | +17% | +4% | yes | 4.1 | +49% (11.9) | -4% (0.8) | -4% | 33 ↓ | +48% |
| 9 | LEN | Lennar | 2018-12 | 33 | -46% | 4% | +46% | +24% | yes | 1.5 | +59% (9.8) | +1% (0.1) | +1% | 47 | +43% |
| 10 | BWXT | BWX Technologies | 2018-12 | 33 | -47% | 57% | +5% | -5% | yes | 1.1 | +69% (11.6) | -0% (0.1) | -0% | 44 | +64% |
| 11 | AYI | Acuity Brands | 2018-04 | 34 | -57% | 11% | +3% | – | yes | 3.9 | +38% (4.7) | -11% (7.8) | -8% | 33 ↓ | +23% |
| 12 | NXPI | NXP Semiconductors | 2018-10 | 34 | -40% | 15% | -3% | +1005% | yes | 3.7 | +55% (12.0) | -9% (1.8) | -9% | 36 | +53% |
| 13 | STT | State Street Corporation | 2018-12 | 34 | -45% | 21% | +9% | +8% | yes | 11.2 | +31% (11.4) | -21% (7.5) | -21% | 32 ↓ | +29% |
| 14 | VMRK | Vivmark Residential | 2018-02 | 34 | -32% | 74% | +2% | -86% | yes | 8.5 | +37% (11.8) | -0% (0.1) | -0% | 44 | +36% |
| 15 | PM | Philip Morris International | 2018-04 | 34 | -34% | 56% | +4% | -14% | **no** | – | +17% (10.7) | -16% (7.8) | -16% | 33 ↓ | +12% |
| 16 | OC | Owens Corning | 2018-10 | 34 | -51% | 20% | +13% | -1% | yes | 8.0 | +37% (11.7) | -13% (1.8) | -13% | 34 | +32% |
| 17 | SLGN | Silgan Holdings | 2018-10 | 34 | -26% | 19% | +15% | +131% | yes | 5.0 | +33% (8.0) | -6% (1.8) | -6% | 37 | +30% |
| 18 | COKE | Coca-Cola Consolidated | 2018-05 | 35 | -49% | 38% | +37% | +75% | yes | 2.3 | +215% (11.4) | -1% (0.0) | -1% | 37 | +138% |
| 19 | ECHO | EchoStar | 2018-10 | 35 | -35% | 50% | – | +230% | **no** | – | +23% (10.8) | -17% (1.8) | -17% | 32 ↓ | +19% |
| 20 | VC | Visteon | 2018-11 | 35 | -48% | 55% | -1% | +14% | yes | 10.8 | +30% (11.2) | -40% (6.0) | -40% | 30 ↓ | +27% |


#### 2019: 4 buys, 3 hit +25%, median max gain +35%, median max DD -25%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | INGR | Ingredion | 2019-05 | 31 | -48% | 44% | -1% | -19% | yes | 6.9 | +32% (8.4) | -18% (9.6) | -3% | 34 | +14% |
| 2 | IDCC | InterDigital | 2019-08 | 31 | -52% | 89% | -36% | -78% | yes | 5.7 | +37% (11.3) | -31% (6.6) | -1% | 32 | +28% |
| 3 | ALB | Albemarle Corporation | 2019-05 | 34 | -56% | 19% | +7% | +1210% | yes | 7.5 | +51% (8.7) | -18% (9.8) | -6% | 36 | +24% |
| 4 | DD | DuPont | 2019-05 | 35 | -41% | 67% | +19% | – | **no** | – | +18% (0.1) | -55% (9.8) | -55% | 24 ↓ | -20% |


#### 2020: 20 buys, 19 hit +25%, median max gain +108%, median max DD -16%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RGA | Reinsurance Group of America | 2020-03 | 25 | -50% | 15% | +11% | +24% | yes | 0.3 | +64% (11.5) | -19% (3.3) | -7% | 30 | +54% |
| 2 | GHC | Graham Holdings | 2020-03 | 25 | -55% | 37% | +9% | +22% | yes | 4.4 | +84% (10.8) | -7% (1.4) | -7% | 29 | +67% |
| 3 | OKE | Oneok | 2020-03 | 26 | -72% | 38% | -19% | +10% | yes | 0.3 | +166% (11.4) | -12% (0.0) | -12% | 32 | +162% |
| 4 | WTFC | Wintrust Financial | 2020-03 | 27 | -67% | 5% | +6% | +3% | yes | 1.0 | +162% (11.5) | -11% (0.5) | -11% | 35 | +136% |
| 5 | RCL | Royal Caribbean Group | 2020-03 | 28 | -76% | 7% | +15% | +5% | yes | 0.3 | +200% (10.8) | -24% (0.1) | -24% | 34 | +166% |
| 6 | UAL | United Airlines Holdings | 2020-03 | 29 | -68% | 5% | +5% | +50% | yes | 2.2 | +98% (11.5) | -37% (1.5) | -37% | 28 ↓ | +82% |
| 7 | DRI | Darden Restaurants | 2020-03 | 29 | -58% | 9% | +4% | -4% | yes | 0.7 | +175% (11.8) | -19% (0.1) | -19% | 39 | +162% |
| 8 | HXL | Hexcel | 2020-03 | 30 | -57% | 9% | +8% | – | yes | 2.2 | +73% (11.5) | -28% (1.4) | -28% | 29 ↓ | +51% |
| 9 | AFG | American Financial Group | 2020-03 | 30 | -42% | 19% | +15% | +68% | yes | 7.4 | +78% (11.6) | -22% (1.5) | -22% | 26 ↓ | +71% |
| 10 | MPC | Marathon Petroleum | 2020-03 | 30 | -73% | 22% | +29% | -25% | yes | 1.0 | +161% (11.3) | -15% (0.1) | -15% | 37 | +140% |
| 11 | LYB | LyondellBasell | 2020-03 | 31 | -59% | 4% | -11% | -20% | yes | 1.8 | +132% (11.3) | -9% (0.0) | -9% | 36 | +121% |
| 12 | CFR | Frost Bank | 2020-03 | 31 | -54% | 0% | +4% | -1% | yes | 0.3 | +117% (11.6) | -4% (0.0) | -4% | 38 | +102% |
| 13 | PBF | PBF Energy | 2020-03 | 31 | -87% | 18% | -10% | +140% | yes | 0.9 | +160% (11.4) | -40% (6.9) | -19% | 31 | +100% |
| 14 | BA | Boeing | 2020-03 | 31 | -67% | 80% | -24% | -106% | yes | 2.2 | +80% (11.4) | -20% (1.5) | -20% | 30 ↓ | +71% |
| 15 | AFL | Aflac | 2020-03 | 31 | -40% | 18% | +3% | +18% | yes | 7.6 | +57% (11.5) | -7% (0.1) | -7% | 33 | +54% |
| 16 | UGI | UGI Corp | 2020-02 | 31 | -39% | 82% | -8% | -50% | **no** | – | +16% (11.7) | -36% (0.8) | -36% | 24 ↓ | +11% |
| 17 | L | Loews Corporation | 2020-03 | 31 | -39% | 0% | +6% | +54% | yes | 7.6 | +53% (11.6) | -17% (1.4) | -17% | 30 ↓ | +48% |
| 18 | TNL | Travel + Leisure Co. | 2020-03 | 31 | -62% | 26% | +3% | -19% | yes | 1.6 | +212% (11.5) | -14% (0.1) | -14% | 36 | +193% |
| 19 | TRV | Travelers Companies (The) | 2020-03 | 32 | -36% | 0% | +4% | +7% | yes | 2.2 | +63% (11.5) | -10% (1.4) | -10% | 33 | +55% |
| 20 | EWBC | East West Bancorp | 2020-03 | 32 | -65% | 0% | +3% | -4% | yes | 0.9 | +213% (11.6) | -11% (0.1) | -11% | 40 | +195% |


#### 2021: 1 buys, 1 hit +25%, median max gain +32%, median max DD -22%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HAE | Haemonetics | 2021-05 | 35 | -60% | 53% | -12% | +5% | yes | 4.0 | +32% (5.2) | -22% (7.9) | -2% | 36 | +12% |


#### 2022: 20 buys, 16 hit +25%, median max gain +48%, median max DD -13%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | 2022-04 | 29 | -73% | 15% | +15% | +33% | yes | 3.4 | +93% (8.9) | -13% (0.4) | -13% | 29 ↓ | +73% |
| 2 | CMCSA | Comcast | 2022-09 | 30 | -53% | 9% | +12% | +15% | yes | 2.0 | +66% (11.0) | -1% (0.4) | -1% | 34 | +56% |
| 3 | PEGA | Pegasystems | 2022-05 | 30 | -67% | 47% | +20% | – | **no** | – | +10% (0.1) | -39% (4.4) | -39% | 26 ↓ | -2% |
| 4 | CHTR | Charter Communications | 2022-09 | 31 | -63% | 5% | +6% | +59% | yes | 1.4 | +50% (11.6) | +1% (2.5) | +1% | 36 | +45% |
| 5 | SWKS | Skyworks Solutions | 2022-06 | 32 | -55% | 14% | +21% | +14% | yes | 7.3 | +34% (7.3) | -14% (3.4) | -14% | 33 | +22% |
| 6 | DIS | Walt Disney Company (The) | 2022-06 | 33 | -54% | 34% | +31% | – | yes | 1.4 | +32% (1.5) | -11% (5.9) | -3% | 36 | -5% |
| 7 | XYZ | Block, Inc. | 2022-06 | 33 | -79% | 33% | +26% | -117% | yes | 1.1 | +46% (1.1) | -16% (3.5) | +2% | 34 | +8% |
| 8 | META | Meta Platforms | 2022-06 | 33 | -58% | 2% | +27% | +13% | yes | 8.5 | +79% (11.8) | -45% (4.1) | -45% | 26 ↓ | +78% |
| 9 | CLX | Clorox | 2022-09 | 33 | -46% | 63% | -3% | -33% | yes | 6.0 | +40% (7.1) | -2% (0.2) | -2% | 39 | +5% |
| 10 | BURL | Burlington Stores | 2022-06 | 33 | -62% | 31% | +27% | -14% | yes | 4.8 | +72% (7.1) | -19% (3.0) | -19% | 31 ↓ | +16% |
| 11 | ALGN | Align Technology | 2022-06 | 33 | -68% | 13% | +43% | +56% | yes | 7.1 | +53% (9.8) | -26% (4.3) | -26% | 33 ↓ | +49% |
| 12 | RH | RH | 2022-06 | 34 | -71% | 16% | +19% | +110% | yes | 0.5 | +64% (7.1) | +4% (0.0) | +4% | 38 | +55% |
| 13 | MDT | Medtronic | 2022-09 | 34 | -41% | 12% | -2% | +35% | **no** | – | +15% (6.9) | -6% (1.9) | -6% | 35 | +0% |
| 14 | BALL | Ball Corporation | 2022-08 | 34 | -46% | 56% | +18% | -12% | **no** | – | +10% (5.1) | -15% (1.4) | -15% | 31 ↓ | -1% |
| 15 | GWRE | Guidewire Software | 2022-09 | 34 | -54% | 2% | +9% | – | yes | 4.1 | +53% (11.3) | -15% (1.3) | -15% | 33 ↓ | +46% |
| 16 | ALLY | Ally Financial | 2022-12 | 34 | -57% | 8% | +5% | -27% | yes | 0.7 | +50% (11.9) | -8% (2.5) | -0% | 39 | +49% |
| 17 | TRU | TransUnion | 2022-09 | 34 | -53% | 8% | +17% | +175% | yes | 4.1 | +39% (11.0) | -14% (1.1) | -14% | 34 ↓ | +21% |
| 18 | PYPL | PayPal | 2022-02 | 34 | -64% | 25% | +18% | -1% | **no** | – | +9% (1.1) | -40% (10.0) | -40% | 29 ↓ | -34% |
| 19 | AMZN | Amazon | 2022-12 | 34 | -55% | 14% | +10% | -57% | yes | 1.1 | +83% (11.6) | -1% (0.2) | -1% | 40 | +81% |
| 20 | SAM | Boston Beer Company | 2022-06 | 34 | -78% | 50% | -0% | -122% | yes | 1.0 | +38% (7.1) | +0% (10.3) | +1% | 37 | +2% |


#### 2023: 18 buys, 13 hit +25%, median max gain +48%, median max DD -6%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DG | Dollar General | 2023-08 | 30 | -47% | 14% | +10% | -3% | **no** | – | +18% (6.4) | -39% (12.0) | -39% | 26 ↓ | -39% |
| 2 | RVTY | Revvity | 2023-10 | 32 | -59% | 49% | – | +22% | yes | 1.6 | +55% (11.0) | -0% (0.0) | -0% | 35 | +44% |
| 3 | UMBF | UMB Financial Corp. | 2023-03 | 32 | -49% | 18% | – | +22% | yes | 3.8 | +54% (11.9) | -6% (1.1) | -6% | 34 | +54% |
| 4 | CPT | Camden Property Trust | 2023-10 | 33 | -53% | 58% | -53% | -73% | yes | 6.1 | +54% (10.8) | -0% (0.0) | -0% | 36 | +42% |
| 5 | MAA | Mid-America Apartment Communities | 2023-10 | 33 | -49% | 23% | +9% | -8% | yes | 8.5 | +46% (10.5) | -0% (0.0) | -0% | 36 | +34% |
| 6 | UDR | UDR, Inc. | 2023-10 | 33 | -48% | 9% | +10% | +176% | yes | 6.2 | +53% (10.4) | -1% (0.0) | -1% | 36 | +38% |
| 7 | BIO | Bio-Rad Laboratories | 2023-10 | 33 | -67% | 44% | -3% | – | yes | 4.3 | +30% (12.0) | -4% (8.0) | +1% | 36 | +30% |
| 8 | EXR | Extra Space Storage | 2023-10 | 33 | -55% | 7% | +15% | -8% | yes | 0.5 | +84% (10.8) | -0% (0.0) | -0% | 44 | +64% |
| 9 | SUI | Sun Communities | 2023-10 | 33 | -47% | 21% | +21% | -33% | yes | 10.2 | +36% (10.4) | +2% (6.0) | +2% | 38 | +23% |
| 10 | WAL | Western Alliance Bancorporation | 2023-03 | 34 | -72% | 17% | +17% | +12% | yes | 3.6 | +103% (10.0) | -49% (1.1) | -49% | 33 ↓ | +87% |
| 11 | PFE | Pfizer | 2023-10 | 34 | -50% | 12% | -23% | -27% | **no** | – | +9% (9.0) | -15% (5.8) | -15% | 29 ↓ | -2% |
| 12 | EL | Estée Lauder Companies (The) | 2023-09 | 34 | -61% | 72% | -10% | -57% | **no** | – | +10% (5.4) | -40% (11.4) | -40% | 31 ↓ | -29% |
| 13 | FFIN | First Financial Bankshares | 2023-04 | 34 | -47% | 28% | – | +3% | **no** | – | +15% (9.0) | -20% (5.7) | -20% | 31 ↓ | +4% |
| 14 | CCI | Crown Castle | 2023-07 | 35 | -48% | 10% | +6% | +15% | **no** | – | +11% (4.0) | -19% (2.6) | -19% | 31 ↓ | +8% |
| 15 | TECH | Bio-Techne | 2023-10 | 35 | -60% | 34% | +3% | +6% | yes | 1.2 | +55% (6.4) | -3% (0.0) | -3% | 40 | +36% |
| 16 | PNFP | Pinnacle Financial Partners | 2023-04 | 35 | -51% | – | – | – | yes | 2.6 | +71% (9.0) | -14% (0.1) | -14% | 32 ↓ | +43% |
| 17 | SBAC | SBA Communications | 2023-09 | 35 | -49% | 8% | +11% | +44% | yes | 2.0 | +28% (3.1) | -6% (7.0) | -5% | 37 | +22% |
| 18 | PODD | Insulet Corporation | 2023-09 | 35 | -53% | 16% | +24% | +73% | yes | 2.4 | +50% (11.8) | -20% (0.4) | -20% | 32 ↓ | +46% |


#### 2024: 3 buys, 2 hit +25%, median max gain +67%, median max DD -23%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FIVE | Five Below | 2024-07 | 33 | -69% | 0% | +15% | +11% | yes | 1.4 | +96% (11.9) | -23% (8.2) | -11% | 33 | +88% |
| 2 | DLTR | Dollar Tree | 2024-09 | 33 | -60% | 0% | +6% | -178% | yes | 7.4 | +67% (10.2) | -13% (1.4) | -13% | 32 ↓ | +34% |
| 3 | ELV | Elevance Health | 2024-12 | 34 | -35% | 49% | +3% | +9% | **no** | – | +23% (3.1) | -25% (7.0) | -25% | 30 ↓ | -3% |


#### 2025: 18 buys, 11 hit +25%, median max gain +34%, median max DD -17%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MOH | Molina Healthcare | 2025-07 | 29 | -63% | 14% | +16% | +10% | yes | 2.1 | +54% (11.4) | -22% (6.4) | -4% | 31 | +24% |
| 2 | WLK | Westlake Corporation | 2025-05 | 30 | -56% | 41% | -1% | +50% | yes | 2.7 | +77% (10.2) | -20% (5.7) | -2% | 32 | +25% |
| 3 | FISV | Fiserv | 2025-10 | 30 | -72% | 6% | +5% | +25% | open | – | +5% (2.3) | -31% (10.7) | -31% | 29 ↓ | -30% (so far) |
| 4 | GPK | Graphic Packaging | 2025-10 | 31 | -48% | 14% | -5% | -24% | open | – | +7% (0.1) | -43% (4.6) | -43% | 22 ↓ | -39% (so far) |
| 5 | CHRD | Chord Energy | 2025-04 | 31 | -53% | 13% | +35% | -32% | yes | 2.9 | +71% (11.0) | -3% (6.2) | -0% | 31 ↓ | +70% |
| 6 | HSY | Hershey Company (The) | 2025-01 | 31 | -46% | 21% | -2% | – | yes | 1.1 | +39% (11.5) | -3% (0.1) | -3% | 39 | +35% |
| 7 | IT | Gartner | 2025-08 | 32 | -57% | 14% | +6% | +61% | **no** | – | +5% (0.9) | -50% (9.7) | -50% | 27 ↓ | -21% |
| 8 | REGN | Regeneron Pharmaceuticals | 2025-05 | 32 | -60% | 7% | +8% | +16% | yes | 4.9 | +66% (7.3) | -1% (0.2) | -1% | 35 | +26% |
| 9 | CMG | Chipotle Mexican Grill | 2025-10 | 34 | -54% | 12% | +7% | +5% | yes | 2.3 | +29% (2.8) | -11% (7.1) | -6% | 37 | -1% (so far) |
| 10 | GIS | General Mills | 2025-05 | 34 | -40% | 18% | -3% | +4% | **no** | – | +1% (0.3) | -36% (11.5) | -36% | 20 ↓ | -34% |
| 11 | OLN | Olin Corporation | 2025-02 | 34 | -62% | 44% | -4% | -75% | **no** | – | +9% (6.4) | -29% (1.3) | -29% | 31 ↓ | +4% |
| 12 | REXR | Rexford Industrial Realty | 2025-04 | 34 | -61% | 5% | +18% | +13% | yes | 3.9 | +37% (5.7) | +0% (0.0) | +0% | 36 | +14% |
| 13 | PBF | PBF Energy | 2025-04 | 34 | -73% | 27% | -14% | -128% | yes | 0.4 | +210% (10.9) | -3% (0.0) | -3% | 36 | +163% |
| 14 | CDW | CDW Corporation | 2025-12 | 34 | -48% | 31% | +6% | -3% | open | – | +15% (8.1) | -27% (4.3) | -27% | 30 ↓ | +1% (so far) |
| 15 | MRK | Merck & Co. | 2025-04 | 34 | -37% | 28% | +7% | +4714% | yes | 6.9 | +50% (11.3) | -14% (0.5) | -14% | 30 ↓ | +33% |
| 16 | ADM | Archer Daniels Midland | 2025-02 | 34 | -52% | 22% | -9% | -49% | yes | 5.4 | +51% (12.0) | -11% (1.3) | -11% | 35 | +51% |
| 17 | KBR | KBR, Inc. | 2025-12 | 34 | -45% | 50% | +9% | +23% | open | – | +12% (0.5) | -25% (4.4) | -25% | 31 ↓ | -13% (so far) |
| 18 | CHE | Chemed Corp. | 2025-07 | 35 | -37% | 49% | +8% | -2% | yes | 11.6 | +32% (11.9) | -10% (7.9) | -10% | 33 ↓ | +30% |


#### 2026: 20 buys, 9 hit +25%, median max gain +22%, median max DD -13%

| # | Ticker | Name | Signal | RSI | vs ATH | Val pct | Rev y/y | EPS y/y | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI low after | 12m return |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HRB | H&R Block | 2026-02 | 30 | -55% | 15% | +5% | +20% | yes | 2.6 | +81% (5.4) | -3% (2.2) | -3% | 31 | +42% (so far) |
| 2 | BR | Broadridge Financial Solutions | 2026-03 | 32 | -40% | 38% | +7% | +41% | open | – | +15% (4.8) | -16% (3.0) | -16% | 26 ↓ | +2% (so far) |
| 3 | TYL | Tyler Technologies | 2026-01 | 32 | -44% | 26% | +11% | +31% | open | – | +3% (7.1) | -25% (4.7) | -25% | 26 ↓ | -12% (so far) |
| 4 | BSX | Boston Scientific | 2026-03 | 32 | -43% | 30% | +20% | +55% | open | – | +5% (0.8) | -32% (3.4) | -32% | 24 ↓ | -30% (so far) |
| 5 | PTC | PTC Inc. | 2026-06 | 32 | -48% | 19% | +28% | +186% | yes | 1.2 | +40% (1.9) | -0% (0.8) | -0% | 42 | +22% (so far) |
| 6 | PNR | Pentair | 2026-08 | 33 | -47% | 29% | +3% | +11% | open | – | -0% (0.0) | -12% (0.8) | -12% | – | -11% (so far) |
| 7 | BRO | Brown & Brown | 2026-04 | 33 | -52% | 46% | +29% | -14% | open | – | +25% (3.0) | -9% (0.4) | -9% | 31 ↓ | +2% (so far) |
| 8 | EXLS | EXL Service | 2026-06 | 33 | -51% | 9% | +13% | +19% | yes | 1.0 | +48% (1.9) | +4% (0.0) | +4% | 47 | +34% (so far) |
| 9 | TSCO | Tractor Supply | 2026-04 | 33 | -45% | 16% | +4% | +1% | open | – | +5% (3.4) | -16% (1.1) | -16% | 30 ↓ | -7% (so far) |
| 10 | INTU | Intuit | 2026-02 | 33 | -50% | 37% | +17% | +44% | open | – | +18% (0.2) | -37% (3.8) | -37% | 27 ↓ | -32% (so far) |
| 11 | LDOS | Leidos | 2026-06 | 33 | -50% | 29% | +2% | +10% | yes | 1.1 | +42% (1.6) | +0% (0.0) | +0% | 39 | +20% (so far) |
| 12 | NOW | ServiceNow | 2026-02 | 34 | -55% | 7% | +21% | +21% | yes | 3.1 | +37% (6.0) | -23% (1.3) | -23% | 30 ↓ | +26% (so far) |
| 13 | TTD | Trade Desk (The) | 2026-02 | 34 | -83% | 10% | +18% | +15% | yes | 0.2 | +25% (0.2) | -47% (6.9) | +2% | 31 ↓ | -47% (so far) |
| 14 | ADP | Automatic Data Processing | 2026-02 | 34 | -35% | 41% | +7% | +11% | yes | 4.9 | +36% (5.9) | -11% (1.3) | -11% | 32 ↓ | +26% (so far) |
| 15 | CVLT | CommVault Systems | 2026-03 | 34 | -61% | 9% | +22% | -49% | yes | 0.9 | +97% (3.2) | +1% (0.0) | +1% | 42 | +87% (so far) |
| 16 | ROL | Rollins, Inc. | 2026-07 | 34 | -43% | 14% | +10% | +9% | open | – | +1% (0.1) | -21% (1.8) | -21% | 32 ↓ | -21% (so far) |
| 17 | INGR | Ingredion | 2026-06 | 34 | -39% | 15% | -2% | +10% | open | – | +14% (1.6) | +2% (0.0) | +2% | 38 | +3% (so far) |
| 18 | PPC | Pilgrim's Pride | 2026-07 | 34 | -52% | 41% | +1% | -56% | open | – | +19% (0.8) | -3% (0.3) | -3% | 41 | +2% (so far) |
| 19 | QLYS | Qualys | 2026-03 | 34 | -57% | 2% | +10% | +17% | yes | 2.0 | +123% (4.4) | -13% (0.3) | -13% | 34 ↓ | +96% (so far) |
| 20 | ERIE | Erie Indemnity | 2026-03 | 35 | -54% | 10% | +7% | – | open | – | +8% (4.8) | -17% (2.1) | -17% | 30 ↓ | -10% (so far) |
