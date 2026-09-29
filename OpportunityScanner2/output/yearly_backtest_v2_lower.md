# Tier A yearly backtest v2: sector rule (staples / utilities / materials need RSI < 30) and a two-tranche entry

Generated 2026-09-29. Universe: today's S&P 500 + 400 (899 tickers, survivorship bias), monthly candles to 2026-08-31, fundamentals point in time from SEC filings. Same trigger, yearly top-20 lists (ranked by signal RSI) and filters as `yearly_backtest.md`.

**Changes**: (1) Consumer Staples, Utilities and Materials are bought only when the signal RSI is below 30; other sectors keep RSI < 35. (2) Half the position is bought at the signal month's close, the other half at the first month-end within the next 4 months whose close is a new low for the move (below every month-end close since the signal) while the monthly RSI is higher than the signal RSI. If that never happens the second half stays in cash.

**Metrics** over the 12 months after the signal month (daily adjusted closes). "Deployed" = the value of the capital actually invested (tranche 1 alone until tranche 2 fills, then both halves at their own cost); hit (+25%), months to hit, max gain and max DD are on that path, measured from the signal month-end. "With cash" counts an unfilled second half as cash at 0%. "v1 single entry" is the yearly_backtest.py result for the same signals before the sector rule (all-in at the signal close). A positive max DD means the position never traded below cost.


## quality + cheap

58 signals in the v1 lists, 1 dropped by the sector rule, 57 buys; second half filled in 26 (46%), median 1 months after the signal at -5% vs the first buy.

### Summary by year

| Year | Buys | 2nd half filled | Hit +25% (deployed) | v1 single entry hit | Months to hit (median / mean) | Max gain (median) | Max DD (median / worst) | RSI went lower | 12m deployed (median) | 12m with cash | 12m v1 single entry | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | 1 | 0/1 = 0% | 1/1 = 100% | 1/1 = 100% | 1.9 / 1.9 | +36% | +4% / +4% | 0% | +25% | +13% | +25% | 0/1 = 0% | – / – | – |
| 2011 | 2 | 1/2 = 50% | 2/2 = 100% | 2/2 = 100% | 3.1 / 3.1 | +77% | -8% / -12% | 50% | +41% | +36% | +37% | 0/2 = 0% | – / – | – |
| 2012 | 1 | 0/1 = 0% | 1/1 = 100% | 1/1 = 100% | 5.5 / 5.5 | +30% | +0% / +0% | 0% | +16% | +8% | +16% | 0/1 = 0% | – / – | – |
| 2013 | 0 | | | | | | | | | | | | | |
| 2014 | 0 | | | | | | | | | | | | | |
| 2015 | 1 | 1/1 = 100% | 1/1 = 100% | 0/1 = 0% | 2.6 / 2.6 | +28% | -19% / -19% | 100% | +6% | +6% | -2% | 0/1 = 0% | – / – | – |
| 2016 | 2 | 0/2 = 0% | 2/2 = 100% | 2/2 = 100% | 1.8 / 1.8 | +93% | -5% / -5% | 0% | +86% | +43% | +86% | 0/2 = 0% | – / – | – |
| 2017 | 2 | 1/2 = 50% | 2/2 = 100% | 2/2 = 100% | 4.5 / 4.5 | +62% | -4% / -9% | 50% | +55% | +37% | +54% | 0/2 = 0% | – / – | – |
| 2018 | 4 | 1/4 = 25% | 4/4 = 100% | 4/4 = 100% | 3.2 / 4.8 | +46% | -13% / -26% | 50% | +39% | +21% | +39% | 0/4 = 0% | – / – | – |
| 2019 | 0 | | | | | | | | | | | | | |
| 2020 | 12 | 4/12 = 33% | 12/12 = 100% | 12/12 = 100% | 1.7 / 2.0 | +78% | -11% / -24% | 33% | +70% | +50% | +69% | 0/12 = 0% | – / – | – |
| 2021 | 0 | | | | | | | | | | | | | |
| 2022 | 11 | 4/11 = 36% | 10/11 = 91% | 10/11 = 91% | 3.4 / 4.1 | +64% | -4% / -44% | 36% | +56% | +28% | +55% | 1/11 = 9% | -26% / -26% | +3% |
| 2023 | 5 | 3/5 = 60% | 4/5 = 80% | 4/5 = 80% | 2.8 / 3.4 | +53% | -16% / -49% | 60% | +38% | +19% | +38% | 1/5 = 20% | -16% / -16% | +12% |
| 2024 | 1 | 0/1 = 0% | 1/1 = 100% | 1/1 = 100% | 1.4 / 1.4 | +96% | -23% / -23% | 0% | +88% | +44% | +88% | 0/1 = 0% | – / – | – |
| 2025 | 5 (3 open) | 2/5 = 40% | 3/5 = 60% | 3/5 = 60% | 2.3 / 2.8 | +29% | -22% / -28% | 40% | +19% | +9% | +19% | 0/2 = 0% | – / – | – |
| 2026 | 10 (10 open) | 9/10 = 90% | 5/10 = 50% | 5/10 = 50% | 1.9 / 2.2 | +22% | -20% / -46% | 90% | – | – | – | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-08)** | 44 | 15/44 = 34% | 42/44 = 95% | 42/45 = 93% | 2.3 / 3.2 | +64% | -8% / -49% | 36% | +56% | +32% | +54% | 2/44 = 5% | -21% / -26% | +7% |
| **All incl. open** | 57 (13 open) | 26/57 = 46% | 48/57 = 84% | 48/58 = 83% | 2.3 / 3.1 | +53% | -12% / -49% | 47% | +56% | +32% | +54% | 2/44 = 5% | -21% / -26% | +7% |


**Two-tranche detail (complete windows)**: when the second half filled (15 buys) the deployed hit rate was 87% and the median 12m return +63% (first half alone +49%, second half +71%); when it did not fill (29 buys) the hit rate was 100% and the median 12m return +54%.


**Dropped by the sector rule** (1 signals, 1 complete): single-entry hit rate 100%, median 12m return +24%, median max DD -18%: ALB 2019-05 (+24%).

### Buys by year


#### 2010: 1 buys, 0 second halves filled, 1 hit +25%, median max gain +36%, median max DD +4%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GILD | Gilead Sciences | Health Care | 2010-08 | 35 | -45% | 0% | +23% | not filled | yes | 1.9 | +36% (10.7) | +4% (0.0) | 41 | +25% | +13% | +25% / – |


#### 2011: 2 buys, 1 second halves filled, 2 hit +25%, median max gain +77%, median max DD -8%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLB | Dolby | Information Technology | 2011-09 | 31 | -61% | 0% | +9% | not filled | yes | 3.6 | +64% (7.5) | -4% (0.1) | 33 | +19% | +10% | +19% / – |
| 2 | ILMN | Illumina, Inc. | Health Care | 2011-10 | 35 | -61% | 0% | +44% | 2011-11 (-9%, RSI 33) | yes | 2.6 | +89% (2.8) | -12% (1.0) | 33 ↓ | +63% | +63% | +55% / +71% |


#### 2012: 1 buys, 0 second halves filled, 1 hit +25%, median max gain +30%, median max DD +0%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CHRW | C.H. Robinson | Industrials | 2012-07 | 33 | -36% | 0% | +10% | not filled | yes | 5.5 | +30% (6.0) | +0% (0.0) | 40 | +16% | +8% | +16% / – |


#### 2015: 1 buys, 1 second halves filled, 1 hit +25%, median max gain +28%, median max DD -19%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PII | Polaris | Consumer Discretionary | 2015-12 | 31 | -46% | 14% | +14% | 2016-01 (-14%, RSI 28) | yes | 2.6 | +28% (3.8) | -19% (0.9) | 28 ↓ | +6% | +6% | -2% / +14% |


#### 2016: 2 buys, 0 second halves filled, 2 hit +25%, median max gain +93%, median max DD -5%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CFR | Frost Bank | Financials | 2016-01 | 33 | -42% | 14% | +8% | not filled | yes | 2.6 | +103% (11.9) | -5% (0.1) | 33 | +93% | +47% | +93% / – |
| 2 | PAG | Penske Automotive Group | Consumer Discretionary | 2016-01 | 33 | -42% | 10% | +8% | not filled | yes | 1.1 | +84% (10.2) | -4% (0.1) | 37 | +78% | +39% | +78% / – |


#### 2017: 2 buys, 1 second halves filled, 2 hit +25%, median max gain +62%, median max DD -4%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TSCO | Tractor Supply | Consumer Discretionary | 2017-05 | 34 | -43% | 19% | +8% | 2017-06 (-2%, RSI 33) | yes | 5.9 | +52% (7.7) | -9% (1.4) | 33 ↓ | +38% | +38% | +37% / +40% |
| 2 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2017-08 | 34 | -33% | 22% | +6% | not filled | yes | 3.1 | +71% (12.0) | +0% (0.4) | 41 | +71% | +36% | +71% / – |


#### 2018: 4 buys, 1 second halves filled, 4 hit +25%, median max gain +46%, median max DD -13%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SNX | TD Synnex | Information Technology | 2018-10 | 33 | -45% | 38% | +27% | not filled | yes | 2.4 | +57% (11.9) | -6% (0.9) | 35 | +54% | +27% | +54% / – |
| 2 | EPR | EPR Properties | Real Estate | 2018-03 | 33 | -35% | 18% | +17% | 2018-04 (-1%, RSI 33) | yes | 4.1 | +49% (11.9) | -4% (0.8) | 33 ↓ | +48% | +48% | +48% / +48% |
| 3 | STT | State Street Corporation | Financials | 2018-12 | 34 | -45% | 21% | +9% | not filled | yes | 11.2 | +31% (11.4) | -21% (7.5) | 32 ↓ | +29% | +15% | +29% / – |
| 4 | PVH | PVH Corp. | Consumer Discretionary | 2018-12 | 35 | -45% | 5% | +13% | not filled | yes | 1.7 | +43% (3.7) | -26% (7.7) | 36 | +13% | +7% | +13% / – |


#### 2020: 12 buys, 4 second halves filled, 12 hit +25%, median max gain +78%, median max DD -11%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RGA | Reinsurance Group of America | Financials | 2020-03 | 25 | -50% | 15% | +11% | not filled | yes | 0.3 | +64% (11.5) | -19% (3.3) | 30 | +54% | +27% | +54% / – |
| 2 | WTFC | Wintrust Financial | Financials | 2020-03 | 27 | -67% | 5% | +6% | not filled | yes | 1.0 | +162% (11.5) | -11% (0.5) | 35 | +136% | +68% | +136% / – |
| 3 | RCL | Royal Caribbean Group | Consumer Discretionary | 2020-03 | 28 | -76% | 7% | +15% | not filled | yes | 0.3 | +200% (10.8) | -24% (0.1) | 34 | +166% | +83% | +166% / – |
| 4 | AFG | American Financial Group | Financials | 2020-03 | 30 | -42% | 19% | +15% | 2020-04 (-5%, RSI 29) | yes | 7.3 | +82% (11.6) | -20% (1.5) | 26 ↓ | +75% | +75% | +71% / +80% |
| 5 | UDR | UDR, Inc. | Real Estate | 2020-09 | 32 | -36% | 19% | +13% | 2020-10 (-4%, RSI 30) | yes | 1.3 | +80% (9.9) | -8% (0.9) | 30 ↓ | +71% | +71% | +68% / +74% |
| 6 | WWD | Woodward, Inc. | Industrials | 2020-03 | 33 | -54% | 17% | +18% | not filled | yes | 2.1 | +115% (9.2) | -14% (0.1) | 33 | +104% | +52% | +104% / – |
| 7 | ACGL | Arch Capital Group | Financials | 2020-04 | 33 | -50% | 12% | +27% | not filled | yes | 1.1 | +68% (11.9) | -7% (0.4) | 41 | +65% | +33% | +65% / – |
| 8 | THG | Hanover Insurance | Financials | 2020-03 | 33 | -37% | 40% | +9% | not filled | yes | 2.3 | +51% (11.6) | -7% (0.1) | 37 | +46% | +23% | +46% / – |
| 9 | GD | General Dynamics | Industrials | 2020-03 | 34 | -42% | 41% | +9% | 2020-04 (-1%, RSI 33) | yes | 2.3 | +43% (11.9) | -7% (1.2) | 33 ↓ | +42% | +42% | +41% / +42% |
| 10 | FNF | Fidelity National Financial | Financials | 2020-03 | 34 | -50% | 18% | +12% | not filled | yes | 1.9 | +76% (11.5) | -7% (0.1) | 37 | +70% | +35% | +70% / – |
| 11 | MTN | Vail Resorts | Consumer Discretionary | 2020-03 | 34 | -51% | 27% | +13% | not filled | yes | 1.6 | +116% (10.8) | -11% (0.1) | 40 | +97% | +49% | +97% / – |
| 12 | MOG-A | Moog Inc. | Industrials | 2020-03 | 34 | -49% | 13% | +8% | 2020-04 (-2%, RSI 34) | yes | 2.1 | +75% (11.4) | -20% (1.4) | 34 ↓ | +68% | +68% | +66% / +70% |


#### 2022: 11 buys, 4 second halves filled, 10 hit +25%, median max gain +64%, median max DD -4%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | Communication Services | 2022-04 | 29 | -73% | 15% | +15% | 2022-06 (-8%, RSI 29) | yes | 3.2 | +102% (8.9) | -13% (0.4) | 29 ↓ | +81% | +81% | +73% / +89% |
| 2 | CMCSA | Comcast | Communication Services | 2022-09 | 30 | -53% | 9% | +12% | not filled | yes | 2.0 | +66% (11.0) | -1% (0.4) | 34 | +56% | +28% | +56% / – |
| 3 | CHTR | Charter Communications | Communication Services | 2022-09 | 31 | -63% | 5% | +6% | not filled | yes | 1.4 | +50% (11.6) | +1% (2.5) | 36 | +45% | +22% | +45% / – |
| 4 | SWKS | Skyworks Solutions | Information Technology | 2022-06 | 32 | -55% | 14% | +21% | not filled | yes | 7.3 | +34% (7.3) | -14% (3.4) | 33 | +22% | +11% | +22% / – |
| 5 | META | Meta Platforms | Communication Services | 2022-06 | 33 | -58% | 2% | +27% | 2022-07 (-1%, RSI 33) | yes | 8.5 | +80% (11.8) | -44% (4.1) | 26 ↓ | +79% | +79% | +78% / +80% |
| 6 | ALGN | Align Technology | Health Care | 2022-06 | 33 | -68% | 13% | +43% | 2022-10 (-18%, RSI 33) | yes | 6.9 | +70% (9.8) | -23% (3.9) | 33 ↓ | +66% | +66% | +49% / +82% |
| 7 | RH | RH | Consumer Discretionary | 2022-06 | 34 | -71% | 16% | +19% | not filled | yes | 0.5 | +64% (7.1) | +4% (0.0) | 38 | +55% | +28% | +55% / – |
| 8 | FIS | Fidelity National Information Services | Financials | 2022-12 | 35 | -57% | 34% | +7% | 2023-03 (-20%, RSI 32) | **no** | – | +15% (1.1) | -26% (2.7) | 32 ↓ | +3% | +3% | -8% / +14% |
| 9 | PNR | Pentair | Industrials | 2022-09 | 35 | -49% | 21% | +18% | not filled | yes | 3.6 | +80% (10.2) | -3% (0.7) | 38 | +62% | +31% | +62% / – |
| 10 | CGNX | Cognex | Information Technology | 2022-06 | 35 | -58% | 33% | +22% | not filled | yes | 6.5 | +35% (7.1) | -4% (3.5) | 37 | +32% | +16% | +32% / – |
| 11 | LII | Lennox International | Industrials | 2022-06 | 35 | -42% | 38% | +11% | not filled | yes | 1.4 | +60% (12.0) | +3% (0.0) | 41 | +60% | +30% | +60% / – |


#### 2023: 5 buys, 3 second halves filled, 4 hit +25%, median max gain +53%, median max DD -16%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UDR | UDR, Inc. | Real Estate | 2023-10 | 33 | -48% | 9% | +10% | not filled | yes | 6.2 | +53% (10.4) | -1% (0.0) | 36 | +38% | +19% | +38% / – |
| 2 | WAL | Western Alliance Bancorporation | Financials | 2023-03 | 34 | -72% | 17% | +17% | 2023-05 (-5%, RSI 33) | yes | 3.6 | +106% (10.0) | -49% (1.1) | 33 ↓ | +90% | +90% | +87% / +93% |
| 3 | CCI | Crown Castle | Real Estate | 2023-07 | 35 | -48% | 10% | +6% | 2023-08 (-7%, RSI 33) | **no** | – | +16% (4.0) | -16% (2.6) | 31 ↓ | +12% | +12% | +8% / +16% |
| 4 | SBAC | SBA Communications | Real Estate | 2023-09 | 35 | -49% | 8% | +11% | not filled | yes | 2.0 | +28% (3.1) | -6% (7.0) | 37 | +22% | +11% | +22% / – |
| 5 | PODD | Insulet Corporation | Health Care | 2023-09 | 35 | -53% | 16% | +24% | 2023-10 (-17%, RSI 32) | yes | 1.7 | +65% (11.8) | -20% (0.4) | 32 ↓ | +61% | +61% | +46% / +76% |


#### 2024: 1 buys, 0 second halves filled, 1 hit +25%, median max gain +96%, median max DD -23%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FIVE | Five Below | Consumer Discretionary | 2024-07 | 33 | -69% | 0% | +15% | not filled | yes | 1.4 | +96% (11.9) | -23% (8.2) | 33 | +88% | +44% | +88% / – |


#### 2025: 5 buys, 2 second halves filled, 3 hit +25%, median max gain +29%, median max DD -22%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MOH | Molina Healthcare | Health Care | 2025-07 | 29 | -63% | 14% | +16% | not filled | yes | 2.1 | +54% (11.4) | -22% (6.4) | 31 | +24% | +12% | +24% / – |
| 2 | FISV | Fiserv | Financials | 2025-10 | 30 | -72% | 6% | +5% | 2025-11 (-8%, RSI 29) | open | – | +9% (2.3) | -28% (10.7) | 29 ↓ | -27% (so far) | – | – |
| 3 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2025-10 | 34 | -54% | 12% | +7% | not filled | yes | 2.3 | +29% (2.8) | -11% (7.1) | 37 | -1% (so far) | – | – |
| 4 | REXR | Rexford Industrial Realty | Real Estate | 2025-04 | 34 | -61% | 5% | +18% | not filled | yes | 3.9 | +37% (5.7) | +0% (0.0) | 36 | +14% | +7% | +14% / – |
| 5 | KBR | KBR, Inc. | Industrials | 2025-12 | 34 | -45% | 50% | +9% | 2026-03 (-8%, RSI 33) | open | – | +12% (0.5) | -22% (4.4) | 31 ↓ | -9% (so far) | – | – |


#### 2026: 10 buys, 9 second halves filled, 5 hit +25%, median max gain +22%, median max DD -20%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BR | Broadridge Financial Solutions | Industrials | 2026-03 | 32 | -40% | 38% | +7% | 2026-04 (-5%, RSI 30) | open | – | +18% (4.8) | -14% (3.0) | 26 ↓ | +5% (so far) | – | – |
| 2 | TYL | Tyler Technologies | Information Technology | 2026-01 | 32 | -44% | 26% | +11% | 2026-02 (-4%, RSI 31) | open | – | +5% (7.1) | -24% (4.7) | 26 ↓ | -10% (so far) | – | – |
| 3 | BSX | Boston Scientific | Health Care | 2026-03 | 32 | -43% | 30% | +20% | 2026-04 (-8%, RSI 30) | open | – | +5% (0.8) | -29% (3.4) | 24 ↓ | -27% (so far) | – | – |
| 4 | EXLS | EXL Service | Industrials | 2026-06 | 33 | -51% | 9% | +13% | not filled | yes | 1.0 | +48% (1.9) | +4% (0.0) | 47 | +34% (so far) | – | – |
| 5 | INTU | Intuit | Information Technology | 2026-02 | 33 | -50% | 37% | +17% | 2026-04 (-5%, RSI 33) | open | – | +18% (0.2) | -36% (3.8) | 27 ↓ | -30% (so far) | – | – |
| 6 | NOW | ServiceNow | Information Technology | 2026-02 | 34 | -55% | 7% | +21% | 2026-03 (-3%, RSI 33) | yes | 3.1 | +39% (6.0) | -22% (1.3) | 30 ↓ | +28% (so far) | – | – |
| 7 | TTD | Trade Desk (The) | Communication Services | 2026-02 | 34 | -83% | 10% | +18% | 2026-03 (-5%, RSI 34) | yes | 0.2 | +25% (0.2) | -46% (6.9) | 31 ↓ | -46% (so far) | – | – |
| 8 | ADP | Automatic Data Processing | Industrials | 2026-02 | 34 | -35% | 41% | +7% | 2026-03 (-5%, RSI 32) | yes | 4.9 | +39% (5.9) | -9% (1.3) | 32 ↓ | +29% (so far) | – | – |
| 9 | ROL | Rollins, Inc. | Industrials | 2026-07 | 34 | -43% | 14% | +10% | 2026-08 (-5%, RSI 32) | open | – | +1% (0.1) | -19% (1.8) | 32 ↓ | -19% (so far) | – | – |
| 10 | QLYS | Qualys | Information Technology | 2026-03 | 34 | -57% | 2% | +10% | 2026-04 (-1%, RSI 34) | yes | 1.9 | +124% (4.4) | -13% (0.3) | 34 ↓ | +97% (so far) | – | – |


## no fundamentals filter

182 signals in the v1 lists, 29 dropped by the sector rule, 153 buys; second half filled in 65 (42%), median 1 months after the signal at -7% vs the first buy.

### Summary by year

| Year | Buys | 2nd half filled | Hit +25% (deployed) | v1 single entry hit | Months to hit (median / mean) | Max gain (median) | Max DD (median / worst) | RSI went lower | 12m deployed (median) | 12m with cash | 12m v1 single entry | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | 4 | 1/4 = 25% | 3/4 = 75% | 3/4 = 75% | 4.3 / 3.8 | +42% | -2% / -12% | 50% | +36% | +18% | +35% | 1/4 = 25% | -12% / -12% | +8% |
| 2011 | 2 | 1/2 = 50% | 2/2 = 100% | 2/2 = 100% | 3.1 / 3.1 | +77% | -8% / -12% | 50% | +41% | +36% | +37% | 0/2 = 0% | – / – | – |
| 2012 | 1 | 0/1 = 0% | 1/1 = 100% | 1/1 = 100% | 5.5 / 5.5 | +30% | +0% / +0% | 0% | +16% | +8% | +16% | 0/1 = 0% | – / – | – |
| 2013 | 1 | 1/1 = 100% | 1/1 = 100% | 1/1 = 100% | 6.2 / 6.2 | +54% | -6% / -6% | 100% | +54% | +54% | +54% | 0/1 = 0% | – / – | – |
| 2014 | 2 | 0/2 = 0% | 2/2 = 100% | 2/2 = 100% | 6.9 / 6.9 | +40% | -0% / -3% | 0% | +19% | +10% | +19% | 0/2 = 0% | – / – | – |
| 2015 | 17 | 12/17 = 71% | 15/17 = 88% | 13/20 = 65% | 7.1 / 6.4 | +34% | -16% / -51% | 71% | +23% | +19% | +23% | 2/17 = 12% | -37% / -51% | -3% |
| 2016 | 15 | 2/15 = 13% | 14/15 = 93% | 15/16 = 94% | 3.5 / 4.9 | +48% | -4% / -24% | 13% | +46% | +23% | +43% | 1/15 = 7% | -5% / -5% | +15% |
| 2017 | 8 | 4/8 = 50% | 8/8 = 100% | 10/12 = 83% | 5.6 / 5.2 | +48% | -11% / -25% | 62% | +30% | +26% | +31% | 0/8 = 0% | – / – | – |
| 2018 | 16 | 7/16 = 44% | 15/16 = 94% | 16/20 = 80% | 3.8 / 5.1 | +38% | -10% / -33% | 50% | +34% | +23% | +30% | 1/16 = 6% | -20% / -20% | -4% |
| 2019 | 2 | 0/2 = 0% | 1/2 = 50% | 3/4 = 75% | 5.7 / 5.7 | +28% | -43% / -55% | 50% | +4% | +2% | +19% | 1/2 = 50% | -55% / -55% | -20% |
| 2020 | 18 | 5/18 = 28% | 18/18 = 100% | 19/20 = 95% | 1.3 / 2.4 | +111% | -16% / -40% | 28% | +94% | +69% | +91% | 0/18 = 0% | – / – | – |
| 2021 | 1 | 0/1 = 0% | 1/1 = 100% | 1/1 = 100% | 4.0 / 4.0 | +32% | -22% / -22% | 0% | +12% | +6% | +12% | 0/1 = 0% | – / – | – |
| 2022 | 17 | 8/17 = 47% | 14/17 = 82% | 16/20 = 80% | 2.6 / 3.3 | +50% | -13% / -44% | 47% | +45% | +25% | +22% | 3/17 = 18% | -31% / -37% | -0% |
| 2023 | 16 | 6/16 = 38% | 13/16 = 81% | 13/18 = 72% | 3.6 / 4.0 | +54% | -5% / -49% | 38% | +37% | +19% | +35% | 3/16 = 19% | -15% / -16% | +10% |
| 2024 | 2 | 0/2 = 0% | 1/2 = 50% | 2/3 = 67% | 1.4 / 1.4 | +60% | -24% / -25% | 50% | +42% | +21% | +34% | 1/2 = 50% | -25% / -25% | -3% |
| 2025 | 13 (4 open) | 6/13 = 46% | 9/13 = 69% | 11/18 = 61% | 2.9 / 4.2 | +37% | -14% / -48% | 54% | +26% | +13% | +26% | 1/9 = 11% | -48% / -48% | -18% |
| 2026 | 18 (18 open) | 12/18 = 67% | 10/18 = 56% | 9/20 = 45% | 1.6 / 2.0 | +27% | -13% / -46% | 71% | – | – | – | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-08)** | 131 | 50/131 = 38% | 117/131 = 89% | 127/157 = 81% | 3.8 / 4.4 | +52% | -11% / -55% | 43% | +38% | +23% | +32% | 14/131 = 11% | -21% / -55% | -1% |
| **All incl. open** | 153 (22 open) | 65/153 = 42% | 128/153 = 84% | 137/182 = 75% | 3.6 / 4.2 | +48% | -12% / -55% | 47% | +38% | +23% | +32% | 14/131 = 11% | -21% / -55% | -1% |


**Two-tranche detail (complete windows)**: when the second half filled (50 buys) the deployed hit rate was 82% and the median 12m return +39% (first half alone +29%, second half +42%); when it did not fill (81 buys) the hit rate was 94% and the median 12m return +38%.


**Dropped by the sector rule** (29 signals, 26 complete): single-entry hit rate 62%, median 12m return +22%, median max DD -13%: LIN 2015-09 (+22%), CBT 2015-09 (+70%), OGE 2015-11 (+26%), CF 2016-01 (+23%), PCG 2017-12 (-47%), KR 2017-06 (+25%), TGT 2017-06 (+51%), SAM 2017-06 (+127%), GIS 2018-03 (+20%), PM 2018-04 (+12%), SLGN 2018-10 (+30%), COKE 2018-05 (+138%), INGR 2019-05 (+14%), ALB 2019-05 (+24%), LYB 2020-03 (+121%), UGI 2020-02 (+11%), CLX 2022-09 (+5%), BALL 2022-08 (-1%), SAM 2022-06 (+2%), DG 2023-08 (-39%), EL 2023-09 (-29%), DLTR 2024-09 (+34%), GPK 2025-10 (open), HSY 2025-01 (+35%), GIS 2025-05 (-34%), OLN 2025-02 (+4%), ADM 2025-02 (+51%), INGR 2026-06 (open), PPC 2026-07 (open).

### Buys by year


#### 2010: 4 buys, 1 second halves filled, 3 hit +25%, median max gain +42%, median max DD -2%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | XOM | ExxonMobil | Energy | 2010-06 | 33 | -41% | – | – | not filled | yes | 4.3 | +57% (10.0) | -1% (0.1) | 37 | +46% | +23% | +46% / – |
| 2 | BAX | Baxter International | Health Care | 2010-05 | 35 | -41% | 2% | +2% | 2010-06 (-4%, RSI 33) | yes | 5.2 | +49% (11.6) | -3% (0.3) | 33 ↓ | +47% | +47% | +45% / +49% |
| 3 | OVV | Ovintiv | Energy | 2010-01 | 35 | -69% | – | – | not filled | **no** | – | +15% (4.5) | -12% (6.8) | 34 ↓ | +8% | +4% | +8% / – |
| 4 | GILD | Gilead Sciences | Health Care | 2010-08 | 35 | -45% | 0% | +23% | not filled | yes | 1.9 | +36% (10.7) | +4% (0.0) | 41 | +25% | +13% | +25% / – |


#### 2011: 2 buys, 1 second halves filled, 2 hit +25%, median max gain +77%, median max DD -8%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLB | Dolby | Information Technology | 2011-09 | 31 | -61% | 0% | +9% | not filled | yes | 3.6 | +64% (7.5) | -4% (0.1) | 33 | +19% | +10% | +19% / – |
| 2 | ILMN | Illumina, Inc. | Health Care | 2011-10 | 35 | -61% | 0% | +44% | 2011-11 (-9%, RSI 33) | yes | 2.6 | +89% (2.8) | -12% (1.0) | 33 ↓ | +63% | +63% | +55% / +71% |


#### 2012: 1 buys, 0 second halves filled, 1 hit +25%, median max gain +30%, median max DD +0%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CHRW | C.H. Robinson | Industrials | 2012-07 | 33 | -36% | 0% | +10% | not filled | yes | 5.5 | +30% (6.0) | +0% (0.0) | 40 | +16% | +8% | +16% / – |


#### 2013: 1 buys, 1 second halves filled, 1 hit +25%, median max gain +54%, median max DD -6%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLR | Digital Realty | Real Estate | 2013-10 | 33 | -41% | 0% | +25% | 2013-11 (-1%, RSI 33) | yes | 6.2 | +54% (12.0) | -6% (1.1) | 33 ↓ | +54% | +54% | +54% / +55% |


#### 2014: 2 buys, 0 second halves filled, 2 hit +25%, median max gain +40%, median max DD -0%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TPR | Tapestry, Inc. | Consumer Discretionary | 2014-06 | 33 | -57% | 7% | -2% | not filled | yes | 7.9 | +30% (8.0) | -3% (4.2) | 34 | +5% | +2% | +5% / – |
| 2 | HAE | Haemonetics | Health Care | 2014-04 | 34 | -34% | 46% | +14% | not filled | yes | 6.0 | +49% (10.4) | +2% (0.0) | 44 | +33% | +17% | +33% / – |


#### 2015: 17 buys, 12 second halves filled, 15 hit +25%, median max gain +34%, median max DD -16%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | WMT | Walmart | Consumer Staples | 2015-10 | 30 | -37% | 0% | +1% | not filled | yes | 6.8 | +34% (9.6) | -1% (0.4) | 33 | +26% | +13% | +26% / – |
| 2 | M | Macy's | Consumer Discretionary | 2015-11 | 31 | -47% | 27% | -0% | 2015-12 (-10%, RSI 28) | yes | 11.8 | +26% (11.8) | -18% (5.6) | 28 ↓ | +18% | +18% | +12% / +24% |
| 3 | PII | Polaris | Consumer Discretionary | 2015-12 | 31 | -46% | 14% | +14% | 2016-01 (-14%, RSI 28) | yes | 2.6 | +28% (3.8) | -19% (0.9) | 28 ↓ | +6% | +6% | -2% / +14% |
| 4 | HUBB | Hubbell Incorporated | Industrials | 2015-09 | 31 | -33% | 33% | +5% | not filled | yes | 6.0 | +31% (11.1) | +0% (0.0) | 40 | +30% | +15% | +30% / – |
| 5 | MAT | Mattel | Consumer Discretionary | 2015-01 | 32 | -45% | 52% | -7% | 2015-02 (-2%, RSI 31) | **no** | – | +14% (2.7) | -23% (8.0) | 27 ↓ | +9% | +9% | +9% / +10% |
| 6 | PVH | PVH Corp. | Consumer Discretionary | 2015-12 | 32 | -47% | 17% | -3% | 2016-01 (-0%, RSI 32) | yes | 2.8 | +55% (9.2) | -10% (0.6) | 32 ↓ | +23% | +23% | +23% / +23% |
| 7 | OKE | Oneok | Energy | 2015-09 | 32 | -55% | 65% | – | 2015-11 (-8%, RSI 31) | yes | 7.1 | +78% (12.0) | -38% (2.6) | 28 ↓ | +78% | +78% | +72% / +85% |
| 8 | EMR | Emerson Electric | Industrials | 2015-08 | 32 | -32% | 14% | -5% | 2015-09 (-7%, RSI 29) | yes | 7.9 | +26% (10.6) | -10% (0.9) | 29 ↓ | +19% | +19% | +15% / +24% |
| 9 | KEX | Kirby Corporation | Industrials | 2015-09 | 33 | -50% | 17% | +6% | 2015-12 (-15%, RSI 30) | yes | 8.2 | +28% (8.3) | -20% (3.4) | 29 ↓ | +9% | +9% | +0% / +18% |
| 10 | WMB | Williams Companies | Energy | 2015-12 | 33 | -58% | 59% | +5% | 2016-01 (-25%, RSI 29) | yes | 7.3 | +56% (11.9) | -49% (1.3) | 28 ↓ | +53% | +53% | +31% / +75% |
| 11 | R | Ryder | Industrials | 2015-12 | 33 | -44% | 51% | -1% | 2016-01 (-6%, RSI 31) | yes | 3.8 | +58% (11.3) | -16% (0.6) | 31 ↓ | +39% | +39% | +34% / +44% |
| 12 | FLS | Flowserve | Industrials | 2015-09 | 33 | -50% | 31% | -3% | not filled | yes | 8.2 | +28% (8.3) | -14% (3.6) | 34 | +19% | +10% | +19% / – |
| 13 | VMI | Valmont Industries | Industrials | 2015-07 | 34 | -33% | 51% | -10% | 2015-08 (-4%, RSI 31) | yes | 8.7 | +34% (8.9) | -13% (2.0) | 26 ↓ | +22% | +22% | +19% / +25% |
| 14 | CXT | Crane NXT | Information Technology | 2015-09 | 34 | -39% | 36% | +2% | not filled | yes | 7.9 | +44% (11.0) | -7% (3.7) | 38 | +38% | +19% | +38% / – |
| 15 | EQT | EQT Corporation | Energy | 2015-11 | 34 | -49% | 88% | – | 2015-12 (-9%, RSI 32) | yes | 4.4 | +46% (7.0) | -17% (0.6) | 32 ↓ | +29% | +29% | +23% / +35% |
| 16 | WYNN | Wynn Resorts | Consumer Discretionary | 2015-04 | 34 | -55% | 10% | -3% | 2015-05 (-9%, RSI 32) | **no** | – | +7% (0.3) | -51% (5.1) | 25 ↓ | -15% | -15% | -19% / -11% |
| 17 | CVLT | CommVault Systems | Information Technology | 2015-09 | 34 | -62% | 64% | -2% | not filled | yes | 2.1 | +58% (11.9) | -10% (3.8) | 40 | +56% | +28% | +56% / – |


#### 2016: 15 buys, 2 second halves filled, 14 hit +25%, median max gain +48%, median max DD -4%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AXP | American Express | Financials | 2016-01 | 26 | -44% | 13% | – | not filled | yes | 7.3 | +48% (11.6) | -4% (0.4) | 29 | +46% | +23% | +46% / – |
| 2 | BWA | BorgWarner | Consumer Discretionary | 2016-01 | 27 | -56% | 8% | -4% | not filled | yes | 1.5 | +45% (10.3) | -5% (4.9) | 32 | +41% | +21% | +41% / – |
| 3 | AMG | Affiliated Managers Group | Financials | 2016-01 | 32 | -42% | 16% | – | not filled | yes | 2.4 | +33% (2.9) | -12% (0.4) | 34 | +14% | +7% | +14% / – |
| 4 | HRB | H&R Block | Consumer Discretionary | 2016-04 | 32 | -46% | 64% | -9% | not filled | yes | 10.5 | +27% (11.9) | -4% (0.4) | 34 | +27% | +14% | +27% / – |
| 5 | AMP | Ameriprise Financial | Financials | 2016-02 | 32 | -39% | 35% | -1% | not filled | yes | 8.4 | +62% (12.0) | +3% (3.9) | 40 | +62% | +31% | +62% / – |
| 6 | CFR | Frost Bank | Financials | 2016-01 | 33 | -42% | 14% | +8% | not filled | yes | 2.6 | +103% (11.9) | -5% (0.1) | 33 | +93% | +47% | +93% / – |
| 7 | UNP | Union Pacific Corporation | Industrials | 2016-01 | 33 | -42% | 22% | -3% | not filled | yes | 2.7 | +57% (11.8) | -0% (0.1) | 40 | +52% | +26% | +52% / – |
| 8 | WDC | Western Digital | Information Technology | 2016-01 | 33 | -58% | 38% | -8% | 2016-02 (-9%, RSI 31) | yes | 7.7 | +82% (11.8) | -22% (3.4) | 31 ↓ | +81% | +81% | +73% / +90% |
| 9 | DOC | Healthpeak Properties | Real Estate | 2016-02 | 33 | -47% | 53% | +12% | not filled | yes | 4.4 | +41% (6.3) | +4% (0.0) | 40 | +29% | +14% | +29% / – |
| 10 | PAG | Penske Automotive Group | Consumer Discretionary | 2016-01 | 33 | -42% | 10% | +8% | not filled | yes | 1.1 | +84% (10.2) | -4% (0.1) | 37 | +78% | +39% | +78% / – |
| 11 | WEX | WEX Inc. | Financials | 2016-02 | 34 | -45% | 66% | +5% | not filled | yes | 0.7 | +83% (11.4) | +4% (0.0) | 46 | +70% | +35% | +70% / – |
| 12 | MCK | McKesson Corporation | Health Care | 2016-10 | 34 | -48% | 16% | +3% | not filled | yes | 6.7 | +33% (8.5) | +2% (0.0) | 39 | +9% | +5% | +9% / – |
| 13 | GWW | W. W. Grainger | Industrials | 2016-01 | 34 | -29% | 29% | +2% | not filled | yes | 11.6 | +33% (11.9) | -2% (0.1) | 42 | +31% | +16% | +31% / – |
| 14 | STX | Seagate Technology | Information Technology | 2016-01 | 34 | -58% | 67% | -14% | 2016-04 (-25%, RSI 33) | yes | 1.3 | +95% (12.0) | -24% (2.9) | 33 ↓ | +95% | +95% | +69% / +121% |
| 15 | WSM | Williams-Sonoma, Inc. | Consumer Discretionary | 2016-10 | 35 | -48% | 5% | +5% | not filled | **no** | – | +23% (1.2) | -5% (9.7) | 39 | +15% | +8% | +15% / – |


#### 2017: 8 buys, 4 second halves filled, 8 hit +25%, median max gain +48%, median max DD -11%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BBWI | Bath & Body Works, Inc. | Consumer Discretionary | 2017-02 | 32 | -48% | 48% | +6% | 2017-03 (-10%, RSI 30) | yes | 9.6 | +32% (9.9) | -25% (6.0) | 28 ↓ | +5% | +5% | -1% / +10% |
| 2 | VFC | VF Corporation | Consumer Discretionary | 2017-01 | 33 | -34% | 49% | -1% | not filled | yes | 6.4 | +65% (11.9) | -6% (0.2) | 35 | +62% | +31% | +62% / – |
| 3 | TSCO | Tractor Supply | Consumer Discretionary | 2017-05 | 34 | -43% | 19% | +8% | 2017-06 (-2%, RSI 33) | yes | 5.9 | +52% (7.7) | -9% (1.4) | 33 ↓ | +38% | +38% | +37% / +40% |
| 4 | GILD | Gilead Sciences | Health Care | 2017-05 | 34 | -47% | 1% | -11% | not filled | yes | 3.0 | +40% (8.0) | -1% (0.3) | 41 | +7% | +3% | +7% / – |
| 5 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2017-08 | 34 | -33% | 22% | +6% | not filled | yes | 3.1 | +71% (12.0) | +0% (0.4) | 41 | +71% | +36% | +71% / – |
| 6 | AZO | AutoZone | Consumer Discretionary | 2017-06 | 34 | -30% | 17% | +2% | 2017-07 (-5%, RSI 32) | yes | 5.2 | +44% (6.9) | -14% (0.4) | 31 ↓ | +21% | +21% | +18% / +24% |
| 7 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2017-09 | 35 | -59% | 67% | – | 2017-10 (-12%, RSI 32) | yes | 6.8 | +82% (10.5) | -13% (4.5) | 32 ↓ | +57% | +57% | +48% / +67% |
| 8 | CAH | Cardinal Health | Health Care | 2017-11 | 35 | -36% | – | – | not filled | yes | 1.7 | +28% (2.0) | -16% (8.3) | 33 ↓ | -4% | -2% | -4% / – |


#### 2018: 16 buys, 7 second halves filled, 15 hit +25%, median max gain +38%, median max DD -10%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KDP | Keurig Dr Pepper | Consumer Staples | 2018-07 | 24 | -81% | 0% | +5% | 2018-08 (-5%, RSI 24) | yes | 9.0 | +35% (10.6) | -5% (1.0) | 24 ↓ | +23% | +23% | +20% / +26% |
| 2 | OZK | Bank OZK | Financials | 2018-10 | 28 | -52% | – | – | 2018-11 (-1%, RSI 28) | yes | 6.0 | +27% (6.1) | -22% (1.6) | 25 ↓ | +7% | +7% | +6% / +7% |
| 3 | THO | Thor Industries | Consumer Discretionary | 2018-12 | 31 | -68% | 0% | +1% | not filled | yes | 0.6 | +50% (11.7) | -17% (7.5) | 34 | +46% | +23% | +46% / – |
| 4 | TCBI | Texas Capital Bancshares | Financials | 2018-12 | 32 | -50% | 7% | – | not filled | yes | 3.7 | +30% (4.1) | -0% (9.2) | 37 | +11% | +6% | +11% / – |
| 5 | SNX | TD Synnex | Information Technology | 2018-10 | 33 | -45% | 38% | +27% | not filled | yes | 2.4 | +57% (11.9) | -6% (0.9) | 35 | +54% | +27% | +54% / – |
| 6 | DY | Dycom Industries | Industrials | 2018-12 | 33 | -56% | 8% | – | 2019-02 (-17%, RSI 31) | **no** | – | +22% (6.0) | -20% (1.9) | 31 ↓ | -4% | -4% | -13% / +5% |
| 7 | EPR | EPR Properties | Real Estate | 2018-03 | 33 | -35% | 18% | +17% | 2018-04 (-1%, RSI 33) | yes | 4.1 | +49% (11.9) | -4% (0.8) | 33 ↓ | +48% | +48% | +48% / +48% |
| 8 | LEN | Lennar | Consumer Discretionary | 2018-12 | 33 | -46% | 4% | +46% | not filled | yes | 1.5 | +59% (9.8) | +1% (0.1) | 47 | +43% | +21% | +43% / – |
| 9 | BWXT | BWX Technologies | Industrials | 2018-12 | 33 | -47% | 57% | +5% | not filled | yes | 1.1 | +69% (11.6) | -0% (0.1) | 44 | +64% | +32% | +64% / – |
| 10 | AYI | Acuity Brands | Industrials | 2018-04 | 34 | -57% | 11% | +3% | 2018-05 (-1%, RSI 33) | yes | 3.8 | +39% (4.7) | -11% (7.8) | 33 ↓ | +23% | +23% | +23% / +24% |
| 11 | NXPI | NXP Semiconductors | Information Technology | 2018-10 | 34 | -40% | 15% | -3% | not filled | yes | 3.7 | +55% (12.0) | -9% (1.8) | 36 | +53% | +27% | +53% / – |
| 12 | STT | State Street Corporation | Financials | 2018-12 | 34 | -45% | 21% | +9% | not filled | yes | 11.2 | +31% (11.4) | -21% (7.5) | 32 ↓ | +29% | +15% | +29% / – |
| 13 | VMRK | Vivmark Residential | Real Estate | 2018-02 | 34 | -32% | 74% | +2% | not filled | yes | 8.5 | +37% (11.8) | -0% (0.1) | 44 | +36% | +18% | +36% / – |
| 14 | OC | Owens Corning | Industrials | 2018-10 | 34 | -51% | 20% | +13% | not filled | yes | 8.0 | +37% (11.7) | -13% (1.8) | 34 | +32% | +16% | +32% / – |
| 15 | ECHO | EchoStar | Communication Services | 2018-10 | 35 | -35% | 50% | – | 2018-12 (-9%, RSI 32) | yes | 10.4 | +29% (10.8) | -17% (1.8) | 32 ↓ | +25% | +25% | +19% / +31% |
| 16 | VC | Visteon | Consumer Discretionary | 2018-11 | 35 | -48% | 55% | -1% | 2018-12 (-18%, RSI 30) | yes | 2.7 | +44% (11.2) | -33% (6.0) | 30 ↓ | +41% | +41% | +27% / +55% |


#### 2019: 2 buys, 0 second halves filled, 1 hit +25%, median max gain +28%, median max DD -43%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IDCC | InterDigital | Information Technology | 2019-08 | 31 | -52% | 89% | -36% | not filled | yes | 5.7 | +37% (11.3) | -31% (6.6) | 32 | +28% | +14% | +28% / – |
| 2 | DD | DuPont | Industrials | 2019-05 | 35 | -41% | 67% | +19% | not filled | **no** | – | +18% (0.1) | -55% (9.8) | 24 ↓ | -20% | -10% | -20% / – |


#### 2020: 18 buys, 5 second halves filled, 18 hit +25%, median max gain +111%, median max DD -16%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RGA | Reinsurance Group of America | Financials | 2020-03 | 25 | -50% | 15% | +11% | not filled | yes | 0.3 | +64% (11.5) | -19% (3.3) | 30 | +54% | +27% | +54% / – |
| 2 | GHC | Graham Holdings | Consumer Discretionary | 2020-03 | 25 | -55% | 37% | +9% | not filled | yes | 4.4 | +84% (10.8) | -7% (1.4) | 29 | +67% | +34% | +67% / – |
| 3 | OKE | Oneok | Energy | 2020-03 | 26 | -72% | 38% | -19% | not filled | yes | 0.3 | +166% (11.4) | -12% (0.0) | 32 | +162% | +81% | +162% / – |
| 4 | WTFC | Wintrust Financial | Financials | 2020-03 | 27 | -67% | 5% | +6% | not filled | yes | 1.0 | +162% (11.5) | -11% (0.5) | 35 | +136% | +68% | +136% / – |
| 5 | RCL | Royal Caribbean Group | Consumer Discretionary | 2020-03 | 28 | -76% | 7% | +15% | not filled | yes | 0.3 | +200% (10.8) | -24% (0.1) | 34 | +166% | +83% | +166% / – |
| 6 | UAL | United Airlines Holdings | Industrials | 2020-03 | 29 | -68% | 5% | +5% | 2020-04 (-6%, RSI 28) | yes | 2.1 | +105% (11.5) | -35% (1.5) | 28 ↓ | +88% | +88% | +82% / +95% |
| 7 | DRI | Darden Restaurants | Consumer Discretionary | 2020-03 | 29 | -58% | 9% | +4% | not filled | yes | 0.7 | +175% (11.8) | -19% (0.1) | 39 | +162% | +81% | +162% / – |
| 8 | HXL | Hexcel | Industrials | 2020-03 | 30 | -57% | 9% | +8% | 2020-04 (-7%, RSI 29) | yes | 2.2 | +79% (11.5) | -26% (0.7) | 29 ↓ | +56% | +56% | +51% / +62% |
| 9 | AFG | American Financial Group | Financials | 2020-03 | 30 | -42% | 19% | +15% | 2020-04 (-5%, RSI 29) | yes | 7.3 | +82% (11.6) | -20% (1.5) | 26 ↓ | +75% | +75% | +71% / +80% |
| 10 | MPC | Marathon Petroleum | Energy | 2020-03 | 30 | -73% | 22% | +29% | not filled | yes | 1.0 | +161% (11.3) | -15% (0.1) | 37 | +140% | +70% | +140% / – |
| 11 | CFR | Frost Bank | Financials | 2020-03 | 31 | -54% | 0% | +4% | not filled | yes | 0.3 | +117% (11.6) | -4% (0.0) | 38 | +102% | +51% | +102% / – |
| 12 | PBF | PBF Energy | Energy | 2020-03 | 31 | -87% | 18% | -10% | not filled | yes | 0.9 | +160% (11.4) | -40% (6.9) | 31 | +100% | +50% | +100% / – |
| 13 | BA | Boeing | Industrials | 2020-03 | 31 | -67% | 80% | -24% | 2020-04 (-5%, RSI 30) | yes | 2.1 | +86% (11.4) | -17% (0.1) | 30 ↓ | +76% | +76% | +71% / +81% |
| 14 | AFL | Aflac | Financials | 2020-03 | 31 | -40% | 18% | +3% | not filled | yes | 7.6 | +57% (11.5) | -7% (0.1) | 33 | +54% | +27% | +54% / – |
| 15 | L | Loews Corporation | Financials | 2020-03 | 31 | -39% | 0% | +6% | 2020-04 (-0%, RSI 31) | yes | 7.6 | +53% (11.6) | -17% (1.4) | 30 ↓ | +49% | +49% | +48% / +49% |
| 16 | TNL | Travel + Leisure Co. | Consumer Discretionary | 2020-03 | 31 | -62% | 26% | +3% | not filled | yes | 1.6 | +212% (11.5) | -14% (0.1) | 36 | +193% | +96% | +193% / – |
| 17 | TRV | Travelers Companies (The) | Financials | 2020-03 | 32 | -36% | 0% | +4% | not filled | yes | 2.2 | +63% (11.5) | -10% (1.4) | 33 | +55% | +28% | +55% / – |
| 18 | EWBC | East West Bancorp | Financials | 2020-03 | 32 | -65% | 0% | +3% | not filled | yes | 0.9 | +213% (11.6) | -11% (0.1) | 40 | +195% | +98% | +195% / – |


#### 2021: 1 buys, 0 second halves filled, 1 hit +25%, median max gain +32%, median max DD -22%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HAE | Haemonetics | Health Care | 2021-05 | 35 | -60% | 53% | -12% | not filled | yes | 4.0 | +32% (5.2) | -22% (7.9) | 36 | +12% | +6% | +12% / – |


#### 2022: 17 buys, 8 second halves filled, 14 hit +25%, median max gain +50%, median max DD -13%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NFLX | Netflix | Communication Services | 2022-04 | 29 | -73% | 15% | +15% | 2022-06 (-8%, RSI 29) | yes | 3.2 | +102% (8.9) | -13% (0.4) | 29 ↓ | +81% | +81% | +73% / +89% |
| 2 | CMCSA | Comcast | Communication Services | 2022-09 | 30 | -53% | 9% | +12% | not filled | yes | 2.0 | +66% (11.0) | -1% (0.4) | 34 | +56% | +28% | +56% / – |
| 3 | PEGA | Pegasystems | Information Technology | 2022-05 | 30 | -67% | 47% | +20% | 2022-06 (-3%, RSI 30) | **no** | – | +10% (0.1) | -37% (4.4) | 26 ↓ | -0% | -0% | -2% / +1% |
| 4 | CHTR | Charter Communications | Communication Services | 2022-09 | 31 | -63% | 5% | +6% | not filled | yes | 1.4 | +50% (11.6) | +1% (2.5) | 36 | +45% | +22% | +45% / – |
| 5 | SWKS | Skyworks Solutions | Information Technology | 2022-06 | 32 | -55% | 14% | +21% | not filled | yes | 7.3 | +34% (7.3) | -14% (3.4) | 33 | +22% | +11% | +22% / – |
| 6 | DIS | Walt Disney Company (The) | Communication Services | 2022-06 | 33 | -54% | 34% | +31% | not filled | yes | 1.4 | +32% (1.5) | -11% (5.9) | 36 | -5% | -3% | -5% / – |
| 7 | XYZ | Block, Inc. | Financials | 2022-06 | 33 | -79% | 33% | +26% | not filled | yes | 1.1 | +46% (1.1) | -16% (3.5) | 34 | +8% | +4% | +8% / – |
| 8 | META | Meta Platforms | Communication Services | 2022-06 | 33 | -58% | 2% | +27% | 2022-07 (-1%, RSI 33) | yes | 8.5 | +80% (11.8) | -44% (4.1) | 26 ↓ | +79% | +79% | +78% / +80% |
| 9 | BURL | Burlington Stores | Consumer Discretionary | 2022-06 | 33 | -62% | 31% | +27% | 2022-09 (-18%, RSI 31) | yes | 4.5 | +91% (7.1) | -19% (3.0) | 31 ↓ | +28% | +28% | +16% / +41% |
| 10 | ALGN | Align Technology | Health Care | 2022-06 | 33 | -68% | 13% | +43% | 2022-10 (-18%, RSI 33) | yes | 6.9 | +70% (9.8) | -23% (3.9) | 33 ↓ | +66% | +66% | +49% / +82% |
| 11 | RH | RH | Consumer Discretionary | 2022-06 | 34 | -71% | 16% | +19% | not filled | yes | 0.5 | +64% (7.1) | +4% (0.0) | 38 | +55% | +28% | +55% / – |
| 12 | MDT | Medtronic | Health Care | 2022-09 | 34 | -41% | 12% | -2% | not filled | **no** | – | +15% (6.9) | -6% (1.9) | 35 | +0% | +0% | +0% / – |
| 13 | GWRE | Guidewire Software | Information Technology | 2022-09 | 34 | -54% | 2% | +9% | 2022-10 (-4%, RSI 33) | yes | 4.1 | +56% (11.3) | -13% (1.3) | 33 ↓ | +49% | +49% | +46% / +51% |
| 14 | ALLY | Ally Financial | Financials | 2022-12 | 34 | -57% | 8% | +5% | not filled | yes | 0.7 | +50% (11.9) | -8% (2.5) | 39 | +49% | +25% | +49% / – |
| 15 | TRU | TransUnion | Industrials | 2022-09 | 34 | -53% | 8% | +17% | 2022-10 (-0%, RSI 34) | yes | 4.1 | +39% (11.0) | -14% (1.1) | 34 ↓ | +22% | +22% | +21% / +22% |
| 16 | PYPL | PayPal | Financials | 2022-02 | 34 | -64% | 25% | +18% | 2022-04 (-21%, RSI 32) | **no** | – | +9% (1.1) | -31% (10.0) | 29 ↓ | -25% | -25% | -34% / -16% |
| 17 | AMZN | Amazon | Consumer Discretionary | 2022-12 | 34 | -55% | 14% | +10% | not filled | yes | 1.1 | +83% (11.6) | -1% (0.2) | 40 | +81% | +40% | +81% / – |


#### 2023: 16 buys, 6 second halves filled, 13 hit +25%, median max gain +54%, median max DD -5%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RVTY | Revvity | Health Care | 2023-10 | 32 | -59% | 49% | – | not filled | yes | 1.6 | +55% (11.0) | -0% (0.0) | 35 | +44% | +22% | +44% / – |
| 2 | UMBF | UMB Financial Corp. | Financials | 2023-03 | 32 | -49% | 18% | – | not filled | yes | 3.8 | +54% (11.9) | -6% (1.1) | 34 | +54% | +27% | +54% / – |
| 3 | CPT | Camden Property Trust | Real Estate | 2023-10 | 33 | -53% | 58% | -53% | not filled | yes | 6.1 | +54% (10.8) | -0% (0.0) | 36 | +42% | +21% | +42% / – |
| 4 | MAA | Mid-America Apartment Communities | Real Estate | 2023-10 | 33 | -49% | 23% | +9% | not filled | yes | 8.5 | +46% (10.5) | -0% (0.0) | 36 | +34% | +17% | +34% / – |
| 5 | UDR | UDR, Inc. | Real Estate | 2023-10 | 33 | -48% | 9% | +10% | not filled | yes | 6.2 | +53% (10.4) | -1% (0.0) | 36 | +38% | +19% | +38% / – |
| 6 | BIO | Bio-Rad Laboratories | Health Care | 2023-10 | 33 | -67% | 44% | -3% | not filled | yes | 4.3 | +30% (12.0) | -4% (8.0) | 36 | +30% | +15% | +30% / – |
| 7 | EXR | Extra Space Storage | Real Estate | 2023-10 | 33 | -55% | 7% | +15% | not filled | yes | 0.5 | +84% (10.8) | -0% (0.0) | 44 | +64% | +32% | +64% / – |
| 8 | SUI | Sun Communities | Real Estate | 2023-10 | 33 | -47% | 21% | +21% | not filled | yes | 10.2 | +36% (10.4) | +2% (6.0) | 38 | +23% | +11% | +23% / – |
| 9 | WAL | Western Alliance Bancorporation | Financials | 2023-03 | 34 | -72% | 17% | +17% | 2023-05 (-5%, RSI 33) | yes | 3.6 | +106% (10.0) | -49% (1.1) | 33 ↓ | +90% | +90% | +87% / +93% |
| 10 | PFE | Pfizer | Health Care | 2023-10 | 34 | -50% | 12% | -23% | 2023-11 (-0%, RSI 33) | **no** | – | +8% (9.0) | -15% (5.8) | 29 ↓ | -2% | -2% | -2% / -3% |
| 11 | FFIN | First Financial Bankshares | Financials | 2023-04 | 34 | -47% | 28% | – | 2023-05 (-11%, RSI 31) | **no** | – | +23% (9.0) | -15% (5.7) | 31 ↓ | +10% | +10% | +4% / +17% |
| 12 | CCI | Crown Castle | Real Estate | 2023-07 | 35 | -48% | 10% | +6% | 2023-08 (-7%, RSI 33) | **no** | – | +16% (4.0) | -16% (2.6) | 31 ↓ | +12% | +12% | +8% / +16% |
| 13 | TECH | Bio-Techne | Health Care | 2023-10 | 35 | -60% | 34% | +3% | not filled | yes | 1.2 | +55% (6.4) | -3% (0.0) | 40 | +36% | +18% | +36% / – |
| 14 | PNFP | Pinnacle Financial Partners | Financials | 2023-04 | 35 | -51% | – | – | 2023-05 (-10%, RSI 32) | yes | 2.6 | +81% (9.0) | -14% (0.1) | 32 ↓ | +51% | +51% | +43% / +59% |
| 15 | SBAC | SBA Communications | Real Estate | 2023-09 | 35 | -49% | 8% | +11% | not filled | yes | 2.0 | +28% (3.1) | -6% (7.0) | 37 | +22% | +11% | +22% / – |
| 16 | PODD | Insulet Corporation | Health Care | 2023-09 | 35 | -53% | 16% | +24% | 2023-10 (-17%, RSI 32) | yes | 1.7 | +65% (11.8) | -20% (0.4) | 32 ↓ | +61% | +61% | +46% / +76% |


#### 2024: 2 buys, 0 second halves filled, 1 hit +25%, median max gain +60%, median max DD -24%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FIVE | Five Below | Consumer Discretionary | 2024-07 | 33 | -69% | 0% | +15% | not filled | yes | 1.4 | +96% (11.9) | -23% (8.2) | 33 | +88% | +44% | +88% / – |
| 2 | ELV | Elevance Health | Health Care | 2024-12 | 34 | -35% | 49% | +3% | not filled | **no** | – | +23% (3.1) | -25% (7.0) | 30 ↓ | -3% | -2% | -3% / – |


#### 2025: 13 buys, 6 second halves filled, 9 hit +25%, median max gain +37%, median max DD -14%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MOH | Molina Healthcare | Health Care | 2025-07 | 29 | -63% | 14% | +16% | not filled | yes | 2.1 | +54% (11.4) | -22% (6.4) | 31 | +24% | +12% | +24% / – |
| 2 | WLK | Westlake Corporation | Materials | 2025-05 | 30 | -56% | 41% | -1% | not filled | yes | 2.7 | +77% (10.2) | -20% (5.7) | 32 | +25% | +13% | +25% / – |
| 3 | FISV | Fiserv | Financials | 2025-10 | 30 | -72% | 6% | +5% | 2025-11 (-8%, RSI 29) | open | – | +9% (2.3) | -28% (10.7) | 29 ↓ | -27% (so far) | – | – |
| 4 | CHRD | Chord Energy | Energy | 2025-04 | 31 | -53% | 13% | +35% | 2025-05 (-0%, RSI 31) | yes | 2.9 | +70% (11.0) | -4% (6.2) | 31 ↓ | +69% | +69% | +70% / +68% |
| 5 | IT | Gartner | Information Technology | 2025-08 | 32 | -57% | 14% | +6% | 2025-11 (-7%, RSI 31) | **no** | – | +5% (4.0) | -48% (9.7) | 27 ↓ | -18% | -18% | -21% / -15% |
| 6 | REGN | Regeneron Pharmaceuticals | Health Care | 2025-05 | 32 | -60% | 7% | +8% | not filled | yes | 4.9 | +66% (7.3) | -1% (0.2) | 35 | +26% | +13% | +26% / – |
| 7 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2025-10 | 34 | -54% | 12% | +7% | not filled | yes | 2.3 | +29% (2.8) | -11% (7.1) | 37 | -1% (so far) | – | – |
| 8 | REXR | Rexford Industrial Realty | Real Estate | 2025-04 | 34 | -61% | 5% | +18% | not filled | yes | 3.9 | +37% (5.7) | +0% (0.0) | 36 | +14% | +7% | +14% / – |
| 9 | PBF | PBF Energy | Energy | 2025-04 | 34 | -73% | 27% | -14% | not filled | yes | 0.4 | +210% (10.9) | -3% (0.0) | 36 | +163% | +81% | +163% / – |
| 10 | CDW | CDW Corporation | Information Technology | 2025-12 | 34 | -48% | 31% | +6% | 2026-01 (-7%, RSI 32) | open | – | +19% (8.1) | -24% (4.3) | 30 ↓ | +5% (so far) | – | – |
| 11 | MRK | Merck & Co. | Health Care | 2025-04 | 34 | -37% | 28% | +7% | 2025-05 (-10%, RSI 30) | yes | 6.8 | +58% (11.3) | -14% (0.5) | 30 ↓ | +40% | +40% | +33% / +47% |
| 12 | KBR | KBR, Inc. | Industrials | 2025-12 | 34 | -45% | 50% | +9% | 2026-03 (-8%, RSI 33) | open | – | +12% (0.5) | -22% (4.4) | 31 ↓ | -9% (so far) | – | – |
| 13 | CHE | Chemed Corp. | Health Care | 2025-07 | 35 | -37% | 49% | +8% | not filled | yes | 11.6 | +32% (11.9) | -10% (7.9) | 33 ↓ | +30% | +15% | +30% / – |


#### 2026: 18 buys, 12 second halves filled, 10 hit +25%, median max gain +27%, median max DD -13%

| # | Ticker | Name | Sector | Signal | RSI | vs ATH | Val pct | Rev y/y | 2nd half (month, vs 1st, RSI) | Hit +25%? | Months to hit | Max gain (month) | Max DD (month) | RSI low after | 12m deployed | 12m with cash | 12m 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HRB | H&R Block | Consumer Discretionary | 2026-02 | 30 | -55% | 15% | +5% | not filled | yes | 2.6 | +81% (5.4) | -3% (2.2) | 31 | +42% (so far) | – | – |
| 2 | BR | Broadridge Financial Solutions | Industrials | 2026-03 | 32 | -40% | 38% | +7% | 2026-04 (-5%, RSI 30) | open | – | +18% (4.8) | -14% (3.0) | 26 ↓ | +5% (so far) | – | – |
| 3 | TYL | Tyler Technologies | Information Technology | 2026-01 | 32 | -44% | 26% | +11% | 2026-02 (-4%, RSI 31) | open | – | +5% (7.1) | -24% (4.7) | 26 ↓ | -10% (so far) | – | – |
| 4 | BSX | Boston Scientific | Health Care | 2026-03 | 32 | -43% | 30% | +20% | 2026-04 (-8%, RSI 30) | open | – | +5% (0.8) | -29% (3.4) | 24 ↓ | -27% (so far) | – | – |
| 5 | PTC | PTC Inc. | Information Technology | 2026-06 | 32 | -48% | 19% | +28% | not filled | yes | 1.2 | +40% (1.9) | -0% (0.8) | 42 | +22% (so far) | – | – |
| 6 | PNR | Pentair | Industrials | 2026-08 | 33 | -47% | 29% | +3% | not filled | open | – | -0% (0.0) | -12% (0.8) | – | -11% (so far) | – | – |
| 7 | BRO | Brown & Brown | Financials | 2026-04 | 33 | -52% | 46% | +29% | 2026-05 (-6%, RSI 31) | yes | 2.9 | +29% (3.0) | -9% (0.4) | 31 ↓ | +5% (so far) | – | – |
| 8 | EXLS | EXL Service | Industrials | 2026-06 | 33 | -51% | 9% | +13% | not filled | yes | 1.0 | +48% (1.9) | +4% (0.0) | 47 | +34% (so far) | – | – |
| 9 | TSCO | Tractor Supply | Consumer Discretionary | 2026-04 | 33 | -45% | 16% | +4% | 2026-05 (-10%, RSI 31) | open | – | +10% (3.4) | -15% (0.9) | 30 ↓ | -2% (so far) | – | – |
| 10 | INTU | Intuit | Information Technology | 2026-02 | 33 | -50% | 37% | +17% | 2026-04 (-5%, RSI 33) | open | – | +18% (0.2) | -36% (3.8) | 27 ↓ | -30% (so far) | – | – |
| 11 | LDOS | Leidos | Industrials | 2026-06 | 33 | -50% | 29% | +2% | not filled | yes | 1.1 | +42% (1.6) | +0% (0.0) | 39 | +20% (so far) | – | – |
| 12 | NOW | ServiceNow | Information Technology | 2026-02 | 34 | -55% | 7% | +21% | 2026-03 (-3%, RSI 33) | yes | 3.1 | +39% (6.0) | -22% (1.3) | 30 ↓ | +28% (so far) | – | – |
| 13 | TTD | Trade Desk (The) | Communication Services | 2026-02 | 34 | -83% | 10% | +18% | 2026-03 (-5%, RSI 34) | yes | 0.2 | +25% (0.2) | -46% (6.9) | 31 ↓ | -46% (so far) | – | – |
| 14 | ADP | Automatic Data Processing | Industrials | 2026-02 | 34 | -35% | 41% | +7% | 2026-03 (-5%, RSI 32) | yes | 4.9 | +39% (5.9) | -9% (1.3) | 32 ↓ | +29% (so far) | – | – |
| 15 | CVLT | CommVault Systems | Information Technology | 2026-03 | 34 | -61% | 9% | +22% | not filled | yes | 0.9 | +97% (3.2) | +1% (0.0) | 42 | +87% (so far) | – | – |
| 16 | ROL | Rollins, Inc. | Industrials | 2026-07 | 34 | -43% | 14% | +10% | 2026-08 (-5%, RSI 32) | open | – | +1% (0.1) | -19% (1.8) | 32 ↓ | -19% (so far) | – | – |
| 17 | QLYS | Qualys | Information Technology | 2026-03 | 34 | -57% | 2% | +10% | 2026-04 (-1%, RSI 34) | yes | 1.9 | +124% (4.4) | -13% (0.3) | 34 ↓ | +97% (so far) | – | – |
| 18 | ERIE | Erie Indemnity | Financials | 2026-03 | 35 | -54% | 10% | +7% | 2026-04 (-13%, RSI 31) | open | – | +16% (4.8) | -12% (1.0) | 30 ↓ | -4% (so far) | – | – |
