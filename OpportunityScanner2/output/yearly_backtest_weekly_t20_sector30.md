# Tier A yearly backtest on weekly candles: former overbought-ATH leader, weekly RSI < 35, +20% target, staples / utilities / materials only below RSI 30

Generated 2026-09-29. Universe: today's S&P 500 + 400 (899 tickers, survivorship bias), weekly candles (weeks ending Friday) to 2026-09-25, fundamentals point in time from SEC filings. Weekly twin of `yearly_backtest.py --target 0.20 --sector-rsi 30` (output/yearly_backtest_t20_sector30.md).

**Trigger**: a new all-time high on a weekly candle with weekly RSI(14) ≥ 70 (≥ 5 years of history) arms the stock for 156 weeks (36 months); the first week whose weekly RSI closes below 35 is the buy, at that Friday's close. **Filters**: quality (profitable TTM and in 2 of the 3 past years, revenue growth ≥ 5%, EPS growing, no one-off gain, no acquisition-driven growth) and cheap (operating multiples in the bottom half of the company's own history), both read from the fundamentals row of the last month-end on or before the signal week (only filings public by then; the valuation is priced at that month-end). Liquid names only (63-day average dollar volume ≥ $5M at the signal). Signals are grouped by calendar year, ranked by signal RSI (lowest first) and cut to the top 20.

**What is measured** over the 12 months after the buy (daily adjusted closes): whether the stock closed ≥ 20% above the buy price ("hit") and how long that took; the highest close vs the buy ("max gain"); the lowest close vs the buy ("max DD", the drawdown from the entry price) and the same measured only up to the hit day ("DD before hit"); whether the weekly RSI printed below the signal RSI afterwards ("RSI went lower", ↓ in the tables, with the RSI low); and the plain 12-month return. Windows that run past 2026-09-25 are "open" and show what happened so far.

**Sector rule**: Consumer Staples, Utilities and Materials are bought only when the signal RSI is below 30; other sectors keep RSI < 35. Full position at the signal close.

**SPY**: "SPY cal. year" is SPY's total return over the calendar year of the signals (2026 to the last completed week); "SPY same 12m" is SPY over each buy's own 12-month window, and "beat SPY" the share of buys that returned more than SPY over that window.

> Quality alone: 752 signals; quality + cheap: 237 (the cheap filter drops 515).


## Weekly vs monthly candles (quality + cheap, complete 12-month windows)

| List | Buys (complete 12m) | Hit target | Months to hit (median) | ≤3m / ≤6m | 12m median / mean | 12m positive | beat SPY | SPY same 12m (median) | Max gain (median) | Max DD (median / worst) | DD before hit (median) | DD worse than -20% | RSI went lower | Misses | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| weekly RSI (this run) | 171 | 123/171 = 72% | 3.6 | 34% / 53% | +22% / +28% | 74% | 56% | +19% | +35% | -13% / -73% UAL | -5% | 36% | 68% | 48/171 = 28% | -9% |
| monthly RSI (yearly_backtest_t20_sector30) | 44 | 41/44 = 93% | 1.9 | 70% / 86% | +54% / +54% | 95% | 73% | +24% | +62% | -9% / -49% WAL | -6% | 25% | 36% | 3/44 = 7% | -2% |


Signals before the cut: **237 weekly** vs **58 monthly** (the weekly RSI dips below 35 far more often, so the top-20 cap binds in 3 years on the weekly list and never on the monthly one). Of the 181 weekly buys, 6 have a monthly buy of the same stock within 3 months before or 6 months after (3%); of the 57 monthly buys, 6 have a weekly buy of the same stock in that range (11%). Where both fired, the weekly signal came a median 10.7 weeks before the monthly month-end (range 3 to 21), and the weekly entry price was a median +30% vs the monthly entry (negative = weekly bought lower).

**How far into the decline each candle buys**: the weekly buys sit a median -29% below the all-time high (quartiles -35% to -24%), a median 6.4 months after the last overbought high; the monthly buys sit -50% below it (quartiles -58% to -43%), 16.0 months after. A weekly RSI under 35 needs about a two-month slide; a monthly RSI under 35 needs a year or more of falling closes, so the monthly signal is a much deeper washout of the same idea.

Repeat names on the weekly list: 3 buys are a second signal of the same stock within 12 months of an earlier buy (overlapping windows, counted separately in every table).


Pairs (same stock, both candles): weekly signal, monthly signal, weeks the weekly came first, weekly entry vs monthly entry, 12m return weekly / monthly.

| Ticker | Weekly signal | Monthly signal | Weekly first by (weeks) | Weekly entry vs monthly | 12m weekly | 12m monthly | Hit weekly / monthly |
|---|---|---|---|---|---|---|---|
| ILMN | 2011-08-05 | 2011-10 | 12 | +75% | -21% | +55% | no / yes |
| PAG | 2015-12-18 | 2016-01 | 6 | +34% | +30% | +78% | yes / yes |
| MOG-A | 2020-03-13 | 2020-03 | 3 | +2% | +70% | +66% | yes / yes |
| META | 2022-02-04 | 2022-06 | 21 | +47% | -21% | +78% | no / yes |
| EXLS | 2026-02-06 | 2026-06 | 21 | +23% | open | open | yes / yes |
| ROL | 2026-05-29 | 2026-07 | 9 | +25% | open | open | no / no |


## Sensitivity: weekly RSI threshold and the yearly cap (quality + cheap, complete 12-month windows)

| List | Buys (complete 12m) | Hit target | Months to hit (median) | ≤3m / ≤6m | 12m median / mean | 12m positive | beat SPY | SPY same 12m (median) | Max gain (median) | Max DD (median / worst) | DD before hit (median) | DD worse than -20% | RSI went lower | Misses | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| weekly RSI < 35 (sector rule 30), top 20 / year (this run) | 171 | 123/171 = 72% | 3.6 | 34% / 53% | +22% / +28% | 74% | 56% | +19% | +35% | -13% / -73% UAL | -5% | 36% | 68% | 48/171 = 28% | -9% |
| weekly RSI < 35 (sector rule 30), no cap | 209 | 152/209 = 73% | 3.0 | 36% / 53% | +23% / +28% | 76% | 57% | +19% | +36% | -13% / -73% UAL | -5% | 33% | 67% | 57/209 = 27% | -8% |
| weekly RSI < 30, top 20 / year | 155 | 118/155 = 76% | 3.3 | 37% / 60% | +25% / +30% | 74% | 54% | +21% | +37% | -12% / -68% UAL | -7% | 34% | 60% | 37/155 = 24% | -13% |
| weekly RSI < 30, no cap | 171 | 129/171 = 75% | 3.2 | 37% / 60% | +25% / +30% | 74% | 55% | +21% | +36% | -12% / -68% UAL | -6% | 34% | 60% | 42/171 = 25% | -13% |
| weekly RSI < 25, no cap | 84 | 71/84 = 85% | 1.8 | 60% / 76% | +41% / +61% | 82% | 63% | +22% | +55% | -10% / -63% TTD | -5% | 32% | 38% | 13/84 = 15% | -6% |


Each row is the same pipeline with a different signal threshold (the sector rule keeps the lower of the two levels) or without the top-20 cut per year. Lower thresholds fire later and less often.


## quality + cheap

237 signals since 2010, 194 after the top-20 cut per year (the cap bound in 2011, 2022, 2025), 13 dropped by the sector rule.

Dropped by the sector rule: ALB 2011-08-19, EXP 2015-10-23, SAM 2015-07-17, DG 2016-09-02, TAP 2017-06-09, EXP 2018-08-31, EXP 2022-04-01, PKG 2022-09-16, AVNT 2022-09-23, CF 2023-03-17, DUK 2026-09-25, VMC 2026-09-18, POST 2026-06-05.

### Summary by year

| Year | SPY cal. year | Buys | Hit +20% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | 12m return: median / mean | 12m best | 12m worst | beat SPY (same 12m) | SPY same 12m (median) | Max gain (median / best) | Max DD (median / worst) | RSI went lower | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | +15% | 1 | 1/1 = 100% | 2.1 / 2.1 / 2.1 | 100% / 100% | +71% / +71% | +71% ISRG | +71% ISRG | 100% | +3% | +81% / +81% ISRG | +2% / +2% ISRG | 0% | 0/1 = 0% | – / – | – |
| 2011 | +2% | 19 | 15/19 = 79% | 2.7 / 3.5 / 9.0 | 47% / 68% | +27% / +26% | +87% MMS | -21% ILMN | 68% | +19% | +41% / +99% FFIV | -10% / -52% ILMN | 53% | 4/19 = 21% | -22% / -52% | -8% |
| 2012 | +16% | 9 | 5/9 = 56% | 3.1 / 4.5 / 10.3 | 22% / 44% | +2% / +9% | +42% BWA | -12% DECK | 22% | +23% | +22% / +42% BWA | -14% / -60% SGI | 56% | 4/9 = 44% | -42% / -60% | -4% |
| 2013 | +32% | 4 | 3/4 = 75% | 5.7 / 6.1 / 8.7 | 0% / 50% | +8% / +6% | +37% NVR | -29% CVLT | 50% | +20% | +26% / +43% NVR | -11% / -36% CVLT | 100% | 1/4 = 25% | -36% / -36% | -29% |
| 2014 | +13% | 14 | 9/14 = 64% | 4.9 / 5.1 / 11.6 | 29% / 43% | +2% / +4% | +55% ULTA | -60% WYNN | 43% | +10% | +24% / +58% ULTA | -7% / -68% WYNN | 64% | 5/14 = 36% | -28% / -68% | -21% |
| 2015 | +1% | 17 | 12/17 = 71% | 5.1 / 5.2 / 8.9 | 24% / 47% | +17% / +16% | +61% THO | -33% URI | 53% | +11% | +33% / +64% THO | -13% / -36% JLL | 71% | 5/17 = 29% | -14% / -36% | +6% |
| 2016 | +12% | 10 | 7/10 = 70% | 2.7 / 3.8 / 11.9 | 60% / 60% | +24% / +28% | +113% NVR | -18% REGN | 50% | +21% | +29% / +113% NVR | -9% / -21% REGN | 70% | 3/10 = 30% | -18% / -21% | +3% |
| 2017 | +22% | 7 | 6/7 = 86% | 5.2 / 5.5 / 10.0 | 29% / 57% | +37% / +31% | +44% FFIV | +4% EXPE | 71% | +17% | +43% / +52% FFIV | -3% / -17% EXPE | 86% | 1/7 = 14% | -17% / -17% | +4% |
| 2018 | -5% | 16 | 12/16 = 75% | 5.7 / 6.0 / 11.2 | 6% / 50% | +29% / +22% | +65% CPAY | -30% IPGP | 69% | +10% | +33% / +75% CPAY | -16% / -38% IPGP | 81% | 4/16 = 25% | -30% / -38% | -13% |
| 2019 | +31% | 2 | 2/2 = 100% | 3.5 / 3.5 / 6.2 | 50% / 50% | +100% / +100% | +139% COHR | +61% ROL | 100% | +15% | +100% / +139% COHR | -13% / -22% COHR | 50% | 0/2 = 0% | – / – | – |
| 2020 | +18% | 19 | 15/19 = 79% | 3.1 / 4.0 / 9.9 | 37% / 63% | +67% / +70% | +283% RH | -47% UAL | 68% | +31% | +71% / +319% RH | -31% / -73% UAL | 95% | 4/19 = 21% | -59% / -73% | +9% |
| 2021 | +29% | 6 | 3/6 = 50% | 6.1 / 7.0 / 10.8 | 0% / 17% | -27% / -20% | +15% CMI | -41% OLED | 33% | -15% | +19% / +26% UHS | -31% / -50% CHTR | 83% | 3/6 = 50% | -44% / -50% | -38% |
| 2022 | -18% | 17 | 8/17 = 47% | 4.0 / 4.6 / 11.2 | 24% / 24% | +5% / +13% | +108% LRCX | -32% AMZN | 47% | +2% | +19% / +131% LRCX | -21% / -62% META | 76% | 9/17 = 53% | -30% / -62% | -10% |
| 2023 | +26% | 6 | 5/6 = 83% | 7.1 / 5.4 / 8.1 | 33% / 33% | +21% / +32% | +98% AXP | -9% ULTA | 50% | +33% | +38% / +104% AXP | -13% / -21% TPL | 83% | 1/6 = 17% | -19% / -19% | +5% |
| 2024 | +25% | 6 | 2/6 = 33% | 4.2 / 4.2 / 5.7 | 17% / 33% | -7% / +4% | +75% HII | -29% WEX | 33% | +13% | +17% / +75% HII | -24% / -39% WEX | 83% | 4/6 = 67% | -29% / -39% | -20% |
| 2025 | +18% | 20 (2 open) | 19/20 = 95% | 1.3 / 2.4 / 8.9 | 70% / 85% | +43% / +64% | +340% VRT | -22% CRM | 61% | +31% | +65% / +365% VRT | -3% / -26% CRM | 30% | 0/18 = 0% | – / – | – |
| 2026 | +14% | 8 (8 open) | 3/8 = 38% | 6.0 / 4.7 / 6.6 | 12% / 25% | – / – | – | – | – | – | +17% / +24% ULTA | -13% / -37% ROL | 88% | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-09-25)** |  | 171 | 123/171 = 72% | 3.6 / 4.4 / 11.9 | 34% / 53% | +22% / +28% | +340% VRT | -60% WYNN | 56% | +19% | +35% / +365% VRT | -13% / -73% UAL | 68% | 48/171 = 28% | -30% / -73% | -9% |
| **All incl. open** |  | 181 (10 open) | 127/181 = 70% | 3.6 / 4.4 / 11.9 | 33% / 51% | +22% / +28% | +340% VRT | -60% WYNN | 56% | +19% | +33% / +365% VRT | -13% / -73% UAL | 70% | 48/171 = 28% | -30% / -73% | -9% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months (30.44 days) from the signal week's Friday. "RSI went lower" = share of buys whose weekly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 1 buys, 1 hit +20%, SPY +15% that year, 12m median +71%, best +71%, worst +71%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ISRG | Intuitive Surgical | Health Care | 2010-11-19 | 34 | -37% | 31 | 15% | +40% | +67% | yes | 2.1 | +81% (11.9) | +2% (0.1) | +2% | 37 | +71% | +3% |


#### 2011: 19 buys, 15 hit +20%, SPY +2% that year, 12m median +27%, best +87%, worst -21%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | LII | Lennox International | Industrials | 2011-07-29 | 26 | -32% | 66 | 48% | +9% | +119% | yes | 9.0 | +33% (11.2) | -32% (1.8) | -32% | 17 ↓ | +23% | +10% |
| 2 | CTSH | Cognizant | Information Technology | 2011-08-19 | 28 | -34% | 20 | 43% | +43% | +35% | yes | 1.3 | +41% (7.2) | +1% (10.8) | +3% | 32 | +17% | +29% |
| 3 | PH | Parker Hannifin | Industrials | 2011-08-05 | 29 | -32% | 25 | 49% | +24% | +152% | yes | 2.7 | +36% (7.3) | -10% (1.9) | -10% | 28 ↓ | +21% | +19% |
| 4 | APH | Amphenol | Information Technology | 2011-08-05 | 30 | -27% | 22 | 28% | +27% | +52% | yes | 5.5 | +42% (7.9) | -8% (1.9) | -8% | 33 | +38% | +19% |
| 5 | ALV | Autoliv | Consumer Discretionary | 2011-08-05 | 30 | -33% | 29 | 38% | +40% | +5675% | yes | 6.0 | +27% (7.3) | -17% (1.9) | -17% | 25 ↓ | +5% | +19% |
| 6 | BIO | Bio-Rad Laboratories | Health Care | 2011-08-05 | 30 | -21% | 11 | 37% | +8% | +25% | **no** | – | +13% (8.0) | -13% (1.6) | -13% | 26 ↓ | -4% | +19% |
| 7 | GGG | Graco Inc. | Industrials | 2011-08-19 | 30 | -37% | 6 | 45% | +29% | +168% | yes | 2.3 | +66% (8.0) | -5% (1.5) | -5% | 35 | +50% | +29% |
| 8 | EMR | Emerson Electric | Industrials | 2011-08-05 | 30 | -27% | 24 | 36% | +10% | +37% | **no** | – | +19% (6.1) | -10% (1.9) | -10% | 28 ↓ | +10% | +19% |
| 9 | FFIV | F5, Inc. | Information Technology | 2011-08-19 | 31 | -52% | 31 | 31% | +35% | +115% | yes | 0.9 | +99% (7.5) | -0% (0.1) | -0% | 34 | +49% | +29% |
| 10 | MMS | Maximus Inc. | Industrials | 2011-09-23 | 31 | -25% | 19 | 33% | +16% | +61% | yes | 1.0 | +87% (12.0) | +2% (0.1) | +2% | 43 | +87% | +31% |
| 11 | SNX | TD Synnex | Information Technology | 2011-08-05 | 31 | -30% | 22 | 44% | +12% | +36% | yes | 5.0 | +70% (7.7) | -10% (0.5) | -10% | 25 ↓ | +30% | +19% |
| 12 | MSM | MSC Industrial Direct | Industrials | 2011-08-05 | 31 | -30% | 17 | 19% | +14% | +47% | yes | 2.5 | +54% (7.8) | -9% (0.1) | -9% | 34 | +27% | +19% |
| 13 | UTHR | United Therapeutics | Health Care | 2011-06-17 | 31 | -23% | 15 | 2% | +63% | +409% | **no** | – | +5% (1.4) | -32% (3.5) | -32% | 20 ↓ | -12% | +8% |
| 14 | LFUS | Littelfuse | Information Technology | 2011-08-05 | 31 | -36% | 13 | 6% | +41% | +719% | yes | 2.7 | +53% (7.9) | -10% (1.6) | -10% | 31 ↓ | +30% | +19% |
| 15 | ILMN | Illumina, Inc. | Health Care | 2011-08-05 | 31 | -33% | 24 | 20% | +35% | +64% | **no** | – | +3% (5.7) | -52% (4.3) | -52% | 18 ↓ | -21% | +19% |
| 16 | JBHT | J.B. Hunt | Industrials | 2011-08-19 | 32 | -25% | 16 | 48% | +19% | +72% | yes | 3.4 | +66% (10.0) | -4% (1.1) | -4% | 36 | +52% | +29% |
| 17 | JKHY | Jack Henry & Associates | Financials | 2011-08-05 | 32 | -23% | 17 | 35% | +12% | +25% | yes | 2.5 | +36% (11.0) | -7% (0.1) | -7% | 32 | +35% | +19% |
| 18 | RRX | Regal Rexnord | Industrials | 2011-08-05 | 32 | -28% | 67 | 46% | +23% | +46% | yes | 6.1 | +28% (6.6) | -22% (1.9) | -22% | 27 ↓ | +20% | +19% |
| 19 | WSM | Williams-Sonoma, Inc. | Consumer Discretionary | 2011-08-19 | 32 | -36% | 14 | 46% | +13% | +169% | yes | 1.8 | +41% (8.4) | +1% (1.5) | +1% | 40 | +33% | +29% |


#### 2012: 9 buys, 5 hit +20%, SPY +16% that year, 12m median +2%, best +42%, worst -12%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLR | Digital Realty | Real Estate | 2012-10-26 | 30 | -24% | 26 | 4% | +14% | +34% | yes | 3.1 | +23% (5.7) | -14% (9.8) | -3% | 29 ↓ | -0% | +27% |
| 2 | CLH | Clean Harbors | Industrials | 2012-09-21 | 33 | -33% | 33 | 42% | +23% | +15% | yes | 1.3 | +24% (1.5) | -2% (0.4) | -2% | 33 | +19% | +20% |
| 3 | MCD | McDonald's | Consumer Discretionary | 2012-06-01 | 33 | -15% | 19 | 35% | +12% | +13% | yes | 10.3 | +22% (10.3) | -2% (5.5) | -2% | 35 | +15% | +30% |
| 4 | GNTX | Gentex | Consumer Discretionary | 2012-04-20 | 34 | -40% | 64 | 16% | +25% | +16% | **no** | – | +10% (0.6) | -29% (3.2) | -29% | 28 ↓ | -0% | +15% |
| 5 | SGI | Somnigroup International | Consumer Discretionary | 2012-05-11 | 34 | -40% | 5 | 39% | +28% | +47% | **no** | – | -2% (0.1) | -60% (1.5) | -60% | 22 ↓ | -7% | +23% |
| 6 | BWA | BorgWarner | Consumer Discretionary | 2012-07-20 | 34 | -27% | 68 | 28% | +20% | +38% | yes | 1.8 | +42% (12.0) | -5% (0.1) | -5% | 40 | +42% | +27% |
| 7 | AAPL | Apple Inc. | Information Technology | 2012-11-16 | 34 | -25% | 8 | 18% | +48% | +68% | **no** | – | +12% (0.3) | -26% (5.1) | -26% | 30 ↓ | +2% | +35% |
| 8 | DECK | Deckers Brands | Consumer Discretionary | 2012-03-30 | 35 | -47% | 58 | 40% | +38% | +46% | **no** | – | +10% (0.9) | -55% (7.1) | -55% | 29 ↓ | -12% | +14% |
| 9 | MSM | MSC Industrial Direct | Industrials | 2012-07-06 | 35 | -25% | 16 | 2% | +16% | +35% | yes | 5.9 | +39% (8.5) | -3% (0.1) | -3% | 38 | +24% | +23% |


#### 2013: 4 buys, 3 hit +20%, SPY +32% that year, 12m median +8%, best +37%, worst -29%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | EW | Edwards Lifesciences | Health Care | 2013-04-26 | 26 | -42% | 39 | 34% | +13% | +25% | yes | 5.7 | +27% (11.7) | -4% (7.6) | -3% | 26 ↓ | +25% | +20% |
| 2 | CVLT | CommVault Systems | Information Technology | 2013-12-13 | 33 | -25% | 39 | 39% | +21% | +42% | **no** | – | +13% (1.5) | -36% (10.5) | -36% | 29 ↓ | -29% | +15% |
| 3 | ISRG | Intuitive Surgical | Health Care | 2013-07-12 | 34 | -28% | 64 | 21% | +23% | +29% | yes | 8.7 | +26% (8.7) | -18% (9.9) | -17% | 28 ↓ | -9% | +20% |
| 4 | NVR | NVR, Inc. | Consumer Discretionary | 2013-08-30 | 34 | -22% | 22 | 0% | +28% | +45% | yes | 3.9 | +43% (6.1) | -2% (0.2) | -2% | 34 ↓ | +37% | +25% |


#### 2014: 14 buys, 9 hit +20%, SPY +13% that year, 12m median +2%, best +55%, worst -60%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2014-05-23 | 26 | -27% | 108 | 33% | +6% | +25% | yes | 7.5 | +38% (10.4) | -2% (2.5) | -2% | 31 | +27% | +14% |
| 2 | WRB | W. R. Berkley Corporation | Financials | 2014-01-31 | 30 | -15% | 42 | 3% | +13% | +16% | yes | 4.9 | +41% (10.2) | -2% (0.1) | -2% | 32 | +30% | +14% |
| 3 | FCFS | FirstCash | Financials | 2014-01-31 | 32 | -23% | 10 | 17% | +16% | +19% | yes | 5.0 | +21% (9.8) | -3% (2.6) | -3% | 32 | +1% | +14% |
| 4 | ECHO | EchoStar | Communication Services | 2014-10-10 | 32 | -18% | 47 | 50% | +6% | +25% | yes | 1.5 | +25% (4.4) | -5% (11.6) | -1% | 28 ↓ | +3% | +8% |
| 5 | BWA | BorgWarner | Consumer Discretionary | 2014-10-03 | 33 | -20% | 26 | 48% | +11% | +24% | **no** | – | +17% (4.9) | -28% (11.7) | -28% | 18 ↓ | -21% | +1% |
| 6 | ULTA | Ulta Beauty | Consumer Discretionary | 2014-01-17 | 33 | -37% | 9 | 16% | +25% | +27% | yes | 2.0 | +58% (11.7) | -3% (0.1) | -3% | 34 | +55% | +12% |
| 7 | PEGA | Pegasystems | Information Technology | 2014-03-28 | 34 | -33% | 17 | 18% | +15% | +96% | yes | 2.0 | +35% (11.0) | -8% (1.0) | -8% | 32 ↓ | +26% | +13% |
| 8 | EOG | EOG Resources | Energy | 2014-10-10 | 34 | -24% | 15 | 36% | +18% | +139% | **no** | – | +13% (1.4) | -23% (10.5) | -23% | 28 ↓ | -2% | +8% |
| 9 | WYNN | Wynn Resorts | Consumer Discretionary | 2014-12-05 | 34 | -34% | 39 | 44% | +8% | +33% | **no** | – | -2% (2.3) | -68% (9.9) | -68% | 19 ↓ | -60% | +3% |
| 10 | TRMB | Trimble Inc. | Information Technology | 2014-10-03 | 34 | -27% | 30 | 26% | +12% | +35% | **no** | – | +5% (0.8) | -45% (11.8) | -45% | 19 ↓ | -44% | +1% |
| 11 | PCAR | Paccar | Industrials | 2014-10-10 | 34 | -18% | 29 | 42% | +11% | +22% | yes | 1.5 | +26% (1.8) | -6% (11.7) | -2% | 25 ↓ | +1% | +8% |
| 12 | G | Genpact | Industrials | 2014-01-24 | 34 | -22% | 27 | 16% | +13% | +22% | yes | 11.6 | +24% (11.9) | -14% (0.5) | -14% | 25 ↓ | +23% | +17% |
| 13 | BKNG | Booking Holdings | Consumer Discretionary | 2014-10-10 | 34 | -23% | 31 | 42% | +29% | +32% | yes | 9.8 | +27% (9.9) | -6% (3.2) | -6% | 37 | +23% | +8% |
| 14 | FAST | Fastenal | Industrials | 2014-08-01 | 35 | -20% | 122 | 21% | +9% | +8% | **no** | – | +10% (4.9) | -9% (7.1) | -9% | 32 ↓ | -3% | +12% |


#### 2015: 17 buys, 12 hit +20%, SPY +1% that year, 12m median +17%, best +61%, worst -33%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2015-10-23 | 26 | -30% | 31 | 10% | +9% | +13% | yes | 8.7 | +49% (11.0) | -18% (2.7) | -18% | 24 ↓ | +37% | +5% |
| 2 | CFR | Frost Bank | Financials | 2015-01-09 | 27 | -22% | 72 | 26% | +7% | +10% | yes | 4.8 | +28% (5.5) | -11% (12.0) | -3% | 27 ↓ | -11% | -4% |
| 3 | TROW | T. Rowe Price | Financials | 2015-08-21 | 29 | -19% | 127 | 3% | +10% | +9% | **no** | – | +11% (8.0) | -9% (4.8) | -9% | 26 ↓ | -1% | +13% |
| 4 | THO | Thor Industries | Consumer Discretionary | 2015-09-25 | 30 | -20% | 100 | 31% | +18% | +15% | yes | 5.7 | +64% (11.4) | -6% (4.6) | -6% | 35 | +61% | +14% |
| 5 | JLL | Jones Lang LaSalle | Real Estate | 2015-09-04 | 31 | -20% | 24 | 41% | +15% | +44% | **no** | – | +17% (2.9) | -36% (10.1) | -36% | 21 ↓ | -17% | +16% |
| 6 | AAPL | Apple Inc. | Information Technology | 2015-08-21 | 32 | -21% | 26 | 28% | +26% | +39% | **no** | – | +16% (2.4) | -13% (8.7) | -13% | 34 | +6% | +13% |
| 7 | LRCX | Lam Research | Information Technology | 2015-09-25 | 32 | -26% | 42 | 50% | +16% | +17% | yes | 1.1 | +52% (11.2) | -2% (0.1) | -2% | 37 | +48% | +14% |
| 8 | URI | United Rentals | Industrials | 2015-01-16 | 32 | -31% | 19 | 45% | +12% | +67% | yes | 2.9 | +28% (4.1) | -33% (12.0) | +1% | 26 ↓ | -33% | -5% |
| 9 | JBHT | J.B. Hunt | Industrials | 2015-08-28 | 33 | -21% | 126 | 46% | +6% | +20% | yes | 7.7 | +22% (7.8) | -11% (4.6) | -11% | 33 | +10% | +11% |
| 10 | ILMN | Illumina, Inc. | Health Care | 2015-10-02 | 33 | -32% | 11 | 43% | +28% | +117% | **no** | – | +19% (2.9) | -18% (7.0) | -18% | 28 ↓ | +11% | +13% |
| 11 | TREX | Trex | Industrials | 2015-08-07 | 33 | -31% | 17 | 28% | +23% | +93% | yes | 8.0 | +48% (12.0) | -20% (1.7) | -20% | 27 ↓ | +48% | +7% |
| 12 | SMCI | Supermicro | Information Technology | 2015-07-10 | 34 | -38% | 19 | 39% | +36% | +79% | yes | 2.9 | +33% (8.7) | -17% (6.1) | -6% | 32 ↓ | -2% | +5% |
| 13 | COLM | Columbia Sportswear | Consumer Discretionary | 2015-12-04 | 35 | -38% | 18 | 39% | +18% | +40% | yes | 2.3 | +36% (4.7) | -5% (0.4) | -5% | 33 ↓ | +28% | +7% |
| 14 | RMD | ResMed| | Health Care | 2015-09-25 | 35 | -33% | 24 | 45% | +8% | +3% | yes | 5.5 | +42% (10.5) | -2% (0.1) | -2% | 38 | +28% | +14% |
| 15 | PAG | Penske Automotive Group | Consumer Discretionary | 2015-12-18 | 35 | -23% | 115 | 26% | +8% | +20% | yes | 8.9 | +37% (11.7) | -29% (1.5) | -29% | 22 ↓ | +30% | +15% |
| 16 | LUV | Southwest Airlines | Industrials | 2015-06-19 | 35 | -27% | 20 | 46% | +6% | +75% | yes | 3.8 | +45% (5.6) | -5% (0.6) | -5% | 32 ↓ | +17% | +0% |
| 17 | GNTX | Gentex | Consumer Discretionary | 2015-08-14 | 35 | -18% | 36 | 22% | +14% | +19% | **no** | – | +19% (11.4) | -14% (5.8) | -14% | 30 ↓ | +18% | +7% |


#### 2016: 10 buys, 7 hit +20%, SPY +12% that year, 12m median +24%, best +113%, worst -18%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GILD | Gilead Sciences | Health Care | 2016-01-29 | 30 | -33% | 32 | 13% | +52% | +93% | yes | 2.6 | +24% (2.9) | -13% (11.9) | -0% | 33 | -12% | +21% |
| 2 | AN | AutoNation | Consumer Discretionary | 2016-01-08 | 30 | -28% | 78 | 10% | +11% | +18% | **no** | – | +9% (6.7) | -18% (10.0) | -18% | 25 ↓ | +3% | +21% |
| 3 | NVR | NVR, Inc. | Consumer Discretionary | 2016-10-28 | 30 | -17% | 47 | 3% | +16% | +30% | yes | 2.9 | +113% (12.0) | -2% (0.2) | -2% | 29 ↓ | +113% | +24% |
| 4 | MDT | Medtronic | Health Care | 2016-11-25 | 31 | -15% | 19 | 48% | +23% | +22% | **no** | – | +20% (7.3) | -6% (1.3) | -6% | 26 ↓ | +13% | +20% |
| 5 | TDG | TransDigm Group | Industrials | 2016-02-12 | 33 | -20% | 34 | 48% | +14% | +134% | yes | 2.9 | +53% (8.9) | +5% (0.1) | +5% | 31 ↓ | +42% | +27% |
| 6 | MOH | Molina Healthcare | Health Care | 2016-05-06 | 33 | -45% | 49 | 5% | +47% | +100% | yes | 2.7 | +46% (12.0) | -6% (10.5) | -0% | 34 | +46% | +19% |
| 7 | LAD | Lithia Motors | Consumer Discretionary | 2016-01-08 | 34 | -32% | 25 | 47% | +66% | +40% | yes | 11.9 | +21% (11.9) | -19% (5.6) | -19% | 29 ↓ | +17% | +21% |
| 8 | SWKS | Skyworks Solutions | Information Technology | 2016-01-15 | 34 | -46% | 30 | 38% | +42% | +72% | yes | 1.6 | +34% (8.8) | -8% (0.9) | -8% | 35 | +31% | +23% |
| 9 | BKNG | Booking Holdings | Consumer Discretionary | 2016-01-15 | 34 | -26% | 10 | 47% | +11% | +8% | yes | 1.8 | +45% (9.8) | -10% (0.8) | -10% | 31 ↓ | +42% | +23% |
| 10 | REGN | Regeneron Pharmaceuticals | Health Care | 2016-01-29 | 35 | -31% | 34 | 46% | +45% | +68% | **no** | – | +6% (9.5) | -21% (4.9) | -21% | 30 ↓ | -18% | +21% |


#### 2017: 7 buys, 6 hit +20%, SPY +22% that year, 12m median +37%, best +44%, worst +4%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TJX | TJX Companies | Consumer Discretionary | 2017-06-23 | 31 | -17% | 129 | 41% | +6% | +4% | yes | 8.2 | +42% (11.9) | -3% (1.0) | -3% | 34 | +40% | +15% |
| 2 | FFIV | F5, Inc. | Information Technology | 2017-08-04 | 33 | -20% | 32 | 7% | +5% | +14% | yes | 5.9 | +52% (10.3) | -4% (1.1) | -4% | 30 ↓ | +44% | +17% |
| 3 | TDG | TransDigm Group | Industrials | 2017-01-20 | 34 | -23% | 19 | 34% | +17% | +33% | yes | 4.6 | +43% (12.0) | -7% (2.1) | -7% | 31 ↓ | +43% | +26% |
| 4 | GNTX | Gentex | Consumer Discretionary | 2017-07-21 | 34 | -22% | 18 | 18% | +9% | +13% | yes | 3.0 | +48% (10.8) | -2% (0.4) | -2% | 33 ↓ | +31% | +15% |
| 5 | IDCC | InterDigital | Information Technology | 2017-08-11 | 34 | -32% | 25 | 17% | +49% | +172% | yes | 10.0 | +24% (10.9) | -3% (0.3) | -3% | 33 ↓ | +18% | +18% |
| 6 | EXPE | Expedia Group | Consumer Discretionary | 2017-11-10 | 34 | -25% | 15 | 45% | +17% | +123% | **no** | – | +15% (8.5) | -17% (3.2) | -17% | 33 ↓ | +4% | +10% |
| 7 | UFPI | UFP Industries | Industrials | 2017-08-11 | 35 | -27% | 50 | 39% | +16% | +5% | yes | 1.6 | +46% (10.0) | -3% (0.2) | -3% | 32 ↓ | +37% | +18% |


#### 2018: 16 buys, 12 hit +20%, SPY -5% that year, 12m median +29%, best +65%, worst -30%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UFPI | UFP Industries | Industrials | 2018-10-19 | 26 | -27% | 45 | 42% | +22% | +36% | yes | 6.2 | +46% (10.8) | -15% (2.2) | -15% | 24 ↓ | +45% | +10% |
| 2 | CBRE | CBRE Group | Real Estate | 2018-10-12 | 29 | -23% | 37 | 21% | +45% | +4% | yes | 4.0 | +43% (10.9) | -3% (2.4) | -3% | 30 | +33% | +10% |
| 3 | DHI | D. R. Horton | Consumer Discretionary | 2018-10-12 | 31 | -29% | 40 | 24% | +15% | +28% | yes | 5.9 | +43% (11.9) | -12% (2.4) | -12% | 25 ↓ | +40% | +10% |
| 4 | META | Meta Platforms | Communication Services | 2018-10-26 | 31 | -34% | 48 | 3% | +46% | +45% | yes | 5.3 | +41% (8.5) | -15% (1.9) | -15% | 28 ↓ | +29% | +16% |
| 5 | IPGP | IPG Photonics | Information Technology | 2018-08-03 | 31 | -35% | 28 | 45% | +37% | +30% | **no** | – | +7% (8.7) | -38% (4.7) | -38% | 28 ↓ | -30% | +5% |
| 6 | TKR | Timken | Industrials | 2018-10-26 | 32 | -33% | 40 | 50% | +21% | +59% | yes | 4.8 | +41% (6.2) | -8% (1.9) | -8% | 33 | +31% | +16% |
| 7 | AMAT | Applied Materials | Information Technology | 2018-09-07 | 32 | -36% | 42 | 35% | +27% | +6% | yes | 10.3 | +33% (10.5) | -27% (3.5) | -27% | 25 ↓ | +28% | +6% |
| 8 | LEN | Lennar | Consumer Discretionary | 2018-10-05 | 33 | -38% | 37 | 5% | +31% | +14% | yes | 7.3 | +33% (12.0) | -15% (2.6) | -15% | 28 ↓ | +33% | +4% |
| 9 | LRCX | Lam Research | Information Technology | 2018-10-05 | 34 | -37% | 45 | 22% | +38% | +43% | yes | 4.1 | +67% (11.7) | -16% (2.6) | -16% | 31 ↓ | +62% | +4% |
| 10 | EVR | Evercore | Financials | 2018-10-19 | 34 | -25% | 37 | 50% | +17% | +7% | **no** | – | +12% (6.3) | -26% (2.2) | -26% | 22 ↓ | -11% | +10% |
| 11 | FBIN | Fortune Brands Innovations | Industrials | 2018-05-04 | 34 | -25% | 42 | 11% | +6% | +16% | **no** | – | +6% (1.1) | -34% (7.7) | -34% | 21 ↓ | +2% | +13% |
| 12 | SF | Stifel | Financials | 2018-10-12 | 34 | -31% | 39 | 37% | +12% | +47% | yes | 5.7 | +30% (9.6) | -18% (2.3) | -18% | 28 ↓ | +14% | +10% |
| 13 | ARW | Arrow Electronics | Information Technology | 2018-10-12 | 34 | -22% | 64 | 41% | +17% | +2% | yes | 5.7 | +26% (6.4) | -8% (7.6) | -8% | 30 ↓ | +8% | +10% |
| 14 | MAS | Masco | Industrials | 2018-10-05 | 34 | -23% | 37 | 38% | +7% | +16% | yes | 11.2 | +22% (11.3) | -23% (0.8) | -23% | 17 ↓ | +20% | +4% |
| 15 | CCL | Carnival Corporation | Consumer Discretionary | 2018-10-26 | 34 | -25% | 60 | 44% | +9% | +21% | **no** | – | +15% (1.1) | -23% (11.4) | -23% | 29 ↓ | -15% | +16% |
| 16 | CPAY | Corpay | Financials | 2018-12-21 | 35 | -23% | 47 | 30% | +14% | +53% | yes | 1.6 | +75% (11.4) | -1% (0.1) | -1% | 40 | +65% | +36% |


#### 2019: 2 buys, 2 hit +20%, SPY +31% that year, 12m median +100%, best +139%, worst +61%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ROL | Rollins, Inc. | Industrials | 2019-08-02 | 34 | -25% | 45 | 46% | +8% | +21% | yes | 6.2 | +61% (12.0) | -4% (0.8) | -4% | 31 ↓ | +61% | +14% |
| 2 | COHR | Coherent Corp. | Information Technology | 2019-11-22 | 34 | -49% | 104 | 29% | +18% | +21% | yes | 0.8 | +139% (12.0) | -22% (3.6) | +1% | 34 | +139% | +16% |


#### 2020: 19 buys, 15 hit +20%, SPY +18% that year, 12m median +67%, best +283%, worst -47%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MOG-A | Moog Inc. | Industrials | 2020-03-13 | 22 | -48% | 126 | 37% | +8% | +37% | yes | 2.7 | +70% (12.0) | -32% (0.2) | -32% | 19 ↓ | +70% | +49% |
| 2 | EME | Emcor | Industrials | 2020-03-13 | 25 | -33% | 36 | 43% | +13% | +19% | yes | 4.9 | +84% (12.0) | -23% (0.1) | -23% | 19 ↓ | +84% | +49% |
| 3 | SGI | Somnigroup International | Consumer Discretionary | 2020-03-13 | 27 | -45% | 4 | 45% | +15% | +88% | yes | 2.5 | +176% (12.0) | -56% (0.2) | -56% | 20 ↓ | +176% | +49% |
| 4 | DHI | D. R. Horton | Consumer Discretionary | 2020-03-13 | 29 | -37% | 3 | 43% | +11% | +15% | yes | 1.5 | +114% (11.9) | -27% (0.2) | -27% | 24 ↓ | +108% | +49% |
| 5 | CBRE | CBRE Group | Real Estate | 2020-03-13 | 29 | -28% | 4 | 46% | +12% | +27% | yes | 7.9 | +71% (12.0) | -36% (0.3) | -36% | 20 ↓ | +71% | +49% |
| 6 | ALLY | Ally Financial | Financials | 2020-02-28 | 30 | -29% | 31 | 27% | +6% | +52% | yes | 8.4 | +76% (11.7) | -53% (0.7) | -53% | 14 ↓ | +71% | +31% |
| 7 | MMS | Maximus Inc. | Industrials | 2020-02-28 | 30 | -23% | 111 | 48% | +21% | +11% | yes | 5.2 | +35% (11.5) | -22% (0.6) | -22% | 23 ↓ | +31% | +31% |
| 8 | TSCO | Tractor Supply | Consumer Discretionary | 2020-03-13 | 31 | -33% | 70 | 30% | +6% | +14% | yes | 1.1 | +128% (11.2) | -12% (0.1) | -12% | 31 ↓ | +127% | +49% |
| 9 | RBA | RB Global | Industrials | 2020-03-13 | 31 | -23% | 8 | 36% | +13% | +23% | yes | 1.3 | +117% (7.8) | -22% (0.2) | -22% | 22 ↓ | +67% | +49% |
| 10 | JPM | JPMorgan Chase | Financials | 2020-03-06 | 31 | -23% | 9 | 48% | +6% | +19% | yes | 9.9 | +47% (11.7) | -27% (0.6) | -27% | 20 ↓ | +45% | +31% |
| 11 | UAL | United Airlines Holdings | Industrials | 2020-01-31 | 31 | -24% | 71 | 34% | +6% | +36% | **no** | – | +10% (0.4) | -73% (3.4) | -73% | 13 ↓ | -47% | +17% |
| 12 | STWD | Starwood Property Trust | Financials | 2020-02-28 | 32 | -16% | 23 | 16% | +14% | +6% | **no** | – | +19% (11.9) | -60% (0.8) | -60% | 11 ↓ | +17% | +31% |
| 13 | DAL | Delta Air Lines | Industrials | 2020-02-28 | 32 | -27% | 110 | 29% | +5% | +39% | **no** | – | +8% (11.9) | -58% (2.5) | -58% | 16 ↓ | +4% | +31% |
| 14 | TKR | Timken | Industrials | 2020-03-06 | 32 | -30% | 7 | 28% | +10% | +4% | yes | 3.1 | +111% (10.3) | -41% (0.4) | -41% | 20 ↓ | +100% | +31% |
| 15 | RH | RH | Consumer Discretionary | 2020-03-13 | 33 | -52% | 14 | 46% | +6% | +87% | yes | 1.5 | +319% (10.1) | -35% (0.3) | -35% | 27 ↓ | +283% | +49% |
| 16 | QLYS | Qualys | Information Technology | 2020-03-13 | 33 | -27% | 91 | 42% | +16% | +41% | yes | 0.4 | +104% (10.5) | -3% (0.1) | -3% | 40 | +41% | +49% |
| 17 | CPAY | Corpay | Financials | 2020-03-06 | 33 | -24% | 26 | 43% | +8% | +25% | **no** | – | +16% (11.7) | -31% (0.6) | -31% | 22 ↓ | +13% | +31% |
| 18 | PCAR | Paccar | Industrials | 2020-02-28 | 34 | -20% | 11 | 29% | +14% | +12% | yes | 4.7 | +52% (11.4) | -25% (0.8) | -25% | 21 ↓ | +39% | +31% |
| 19 | OLED | Universal Display | Information Technology | 2020-03-06 | 34 | -32% | 26 | 37% | +64% | +92% | yes | 5.0 | +68% (10.5) | -31% (0.4) | -31% | 23 ↓ | +22% | +31% |


#### 2021: 6 buys, 3 hit +20%, SPY +29% that year, 12m median -27%, best +15%, worst -41%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FDX | FedEx | Industrials | 2021-09-24 | 28 | -29% | 20 | 50% | +21% | +297% | **no** | – | +17% (3.4) | -33% (12.0) | -33% | 27 ↓ | -33% | -16% |
| 2 | CHTR | Charter Communications | Communication Services | 2021-12-10 | 32 | -26% | 14 | 49% | +8% | +74% | **no** | – | +8% (0.7) | -50% (9.7) | -50% | 22 ↓ | -38% | -15% |
| 3 | CMI | Cummins | Industrials | 2021-12-17 | 32 | -24% | 40 | 49% | +23% | +43% | yes | 10.8 | +22% (11.4) | -11% (6.2) | -11% | 32 | +15% | -15% |
| 4 | BAX | Baxter International | Health Care | 2021-08-06 | 34 | -21% | 100 | 41% | +7% | +22% | yes | 6.1 | +20% (6.1) | -21% (11.9) | -1% | 29 ↓ | -21% | -5% |
| 5 | UHS | Universal Health Services | Health Care | 2021-10-29 | 34 | -25% | 22 | 27% | +8% | +49% | yes | 4.1 | +26% (5.7) | -29% (10.9) | -6% | 30 ↓ | -5% | -14% |
| 6 | OLED | Universal Display | Information Technology | 2021-10-08 | 35 | -36% | 38 | 24% | +41% | +81% | **no** | – | +11% (0.8) | -44% (11.7) | -44% | 30 ↓ | -41% | -16% |


#### 2022: 17 buys, 8 hit +20%, SPY -18% that year, 12m median +5%, best +108%, worst -32%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | META | Meta Platforms | Communication Services | 2022-02-04 | 24 | -38% | 28 | 7% | +42% | +39% | **no** | – | -1% (1.9) | -62% (8.9) | -62% | 19 ↓ | -21% | -7% |
| 2 | MMS | Maximus Inc. | Industrials | 2022-05-06 | 30 | -30% | 54 | 27% | +24% | +28% | yes | 9.2 | +27% (9.4) | -17% (5.2) | -17% | 23 ↓ | +21% | +2% |
| 3 | BBY | Best Buy | Consumer Discretionary | 2022-05-20 | 30 | -49% | 26 | 43% | +10% | +44% | yes | 6.4 | +31% (8.5) | -11% (5.0) | -11% | 34 | +2% | +9% |
| 4 | APO | Apollo Global Management | Financials | 2022-04-22 | 30 | -33% | 25 | 0% | +153% | +1564% | yes | 6.6 | +40% (9.6) | -13% (1.8) | -13% | 26 ↓ | +21% | -2% |
| 5 | FAF | First American Financial Corporation | Financials | 2022-04-08 | 31 | -27% | 20 | 26% | +30% | +81% | **no** | – | +11% (9.9) | -24% (6.4) | -24% | 27 ↓ | -3% | -7% |
| 6 | TRU | TransUnion | Industrials | 2022-02-25 | 31 | -27% | 24 | 46% | +11% | +45% | **no** | – | +14% (1.1) | -44% (8.2) | -44% | 26 ↓ | -28% | -8% |
| 7 | AMZN | Amazon | Consumer Discretionary | 2022-01-21 | 31 | -24% | 72 | 39% | +32% | +50% | **no** | – | +19% (2.2) | -43% (11.2) | -43% | 25 ↓ | -32% | -8% |
| 8 | MIDD | Middleby | Industrials | 2022-04-08 | 32 | -27% | 35 | 49% | +29% | +129% | **no** | – | +10% (0.9) | -16% (3.2) | -16% | 29 ↓ | -8% | -7% |
| 9 | SSD | Simpson Manufacturing | Industrials | 2022-06-17 | 32 | -37% | 24 | 24% | +29% | +67% | yes | 1.1 | +51% (11.7) | -13% (4.1) | +2% | 29 ↓ | +48% | +22% |
| 10 | LRCX | Lam Research | Information Technology | 2022-10-14 | 32 | -57% | 79 | 31% | +18% | +22% | yes | 0.4 | +131% (9.4) | +0% (0.1) | +0% | 40 | +108% | +23% |
| 11 | TSLA | Tesla, Inc. | Consumer Discretionary | 2022-12-16 | 32 | -64% | 58 | 25% | +60% | +215% | yes | 1.5 | +95% (7.0) | -28% (0.6) | -28% | 27 ↓ | +69% | +24% |
| 12 | ALLY | Ally Financial | Financials | 2022-06-17 | 32 | -42% | 54 | 28% | +17% | +36% | **no** | – | +13% (2.0) | -30% (9.0) | -30% | 30 ↓ | -10% | +22% |
| 13 | SGI | Somnigroup International | Consumer Discretionary | 2022-02-25 | 32 | -33% | 22 | 34% | +33% | +142% | yes | 11.2 | +33% (11.2) | -39% (3.6) | -39% | 25 ↓ | +28% | -8% |
| 14 | CHH | Choice Hotels | Consumer Discretionary | 2022-07-01 | 33 | -28% | 26 | 41% | +55% | +683% | **no** | – | +16% (10.2) | -8% (2.9) | -8% | 32 ↓ | +5% | +18% |
| 15 | WSM | Williams-Sonoma, Inc. | Consumer Discretionary | 2022-05-20 | 33 | -52% | 58 | 21% | +22% | +117% | yes | 0.2 | +57% (2.9) | -2% (0.1) | -2% | 39 | +9% | +9% |
| 16 | FBIN | Fortune Brands Innovations | Industrials | 2022-03-04 | 33 | -26% | 43 | 16% | +26% | +41% | **no** | – | +3% (0.5) | -36% (7.6) | -36% | 23 ↓ | -12% | -5% |
| 17 | NOW | ServiceNow | Information Technology | 2022-05-20 | 33 | -39% | 37 | 32% | +29% | +43% | **no** | – | +19% (2.7) | -21% (4.8) | -21% | 35 | +18% | +9% |


#### 2023: 6 buys, 5 hit +20%, SPY +26% that year, 12m median +21%, best +98%, worst -9%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CFR | Frost Bank | Financials | 2023-03-17 | 29 | -35% | 71 | 37% | +24% | +33% | **no** | – | +13% (11.6) | -19% (7.3) | -19% | 27 ↓ | +5% | +33% |
| 2 | WTFC | Wintrust Financial | Financials | 2023-03-17 | 32 | -32% | 61 | 47% | +5% | +6% | yes | 8.0 | +41% (11.6) | -15% (1.8) | -15% | 25 ↓ | +37% | +33% |
| 3 | ULTA | Ulta Beauty | Consumer Discretionary | 2023-05-26 | 35 | -24% | 8 | 37% | +18% | +34% | yes | 8.1 | +35% (9.6) | -12% (4.8) | -12% | 29 ↓ | -9% | +28% |
| 4 | FTNT | Fortinet | Information Technology | 2023-11-03 | 35 | -38% | 16 | 29% | +31% | +63% | yes | 2.2 | +64% (11.3) | -2% (0.1) | -2% | 35 | +56% | +33% |
| 5 | AXP | American Express | Financials | 2023-10-20 | 35 | -29% | 117 | 14% | +18% | +1% | yes | 1.3 | +104% (11.9) | -0% (0.2) | -0% | 35 ↓ | +98% | +41% |
| 6 | TPL | Texas Pacific Land Corporation | Energy | 2023-03-17 | 35 | -40% | 18 | 39% | +48% | +66% | yes | 7.1 | +22% (7.1) | -21% (3.2) | -21% | 27 ↓ | +3% | +33% |


#### 2024: 6 buys, 2 hit +20%, SPY +25% that year, 12m median -7%, best +75%, worst -29%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HII | Huntington Ingalls Industries | Industrials | 2024-11-01 | 26 | -37% | 34 | 38% | +6% | +36% | yes | 5.7 | +75% (12.0) | -15% (3.2) | -15% | 27 | +75% | +21% |
| 2 | LULU | Lululemon Athletica | Consumer Discretionary | 2024-04-05 | 31 | -31% | 14 | 25% | +19% | +83% | **no** | – | +18% (9.9) | -35% (4.0) | -35% | 21 ↓ | -26% | -1% |
| 3 | QLYS | Qualys | Information Technology | 2024-05-31 | 32 | -32% | 23 | 16% | +12% | +50% | **no** | – | +13% (5.2) | -18% (10.2) | -18% | 29 ↓ | -1% | +13% |
| 4 | NBIX | Neurocrine Biosciences | Health Care | 2024-10-04 | 35 | -28% | 35 | 8% | +27% | +87% | yes | 2.6 | +34% (3.9) | -23% (6.1) | -2% | 29 ↓ | +20% | +18% |
| 5 | WEX | WEX Inc. | Financials | 2024-05-31 | 35 | -23% | 8 | 26% | +6% | +84% | **no** | – | +16% (4.6) | -39% (10.2) | -39% | 27 ↓ | -29% | +13% |
| 6 | ULTA | Ulta Beauty | Consumer Discretionary | 2024-04-19 | 35 | -28% | 7 | 19% | +10% | +8% | **no** | – | +8% (8.2) | -24% (10.8) | -24% | 28 ↓ | -13% | +8% |


#### 2025: 20 buys, 19 hit +20%, SPY +18% that year, 12m median +43%, best +340%, worst -22%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | QCOM | Qualcomm | Information Technology | 2025-04-04 | 28 | -45% | 41 | 37% | +12% | +35% | yes | 1.3 | +49% (6.8) | -2% (0.1) | -2% | 31 | +2% | +31% |
| 2 | CRM | Salesforce | Information Technology | 2025-04-04 | 30 | -35% | 17 | 7% | +9% | +142% | yes | 1.2 | +21% (1.4) | -26% (10.7) | -2% | 30 ↓ | -22% | +31% |
| 3 | AMZN | Amazon | Consumer Discretionary | 2025-04-04 | 30 | -29% | 9 | 22% | +11% | +91% | yes | 1.2 | +49% (7.0) | -2% (0.6) | -2% | 35 | +23% | +31% |
| 4 | WTFC | Wintrust Financial | Financials | 2025-04-04 | 31 | -32% | 18 | 49% | +14% | +8% | yes | 0.9 | +70% (10.1) | -1% (0.1) | -1% | 33 | +47% | +31% |
| 5 | DELL | Dell Technologies | Information Technology | 2025-04-04 | 31 | -60% | 45 | 47% | +8% | +77% | yes | 0.6 | +162% (11.7) | +1% (0.1) | +1% | 38 | +148% | +31% |
| 6 | UAL | United Airlines Holdings | Industrials | 2025-04-04 | 31 | -50% | 10 | 32% | +6% | +20% | yes | 0.2 | +104% (9.1) | -3% (0.1) | -3% | 38 | +60% | +31% |
| 7 | GOOGL | Alphabet Inc. (Class A) | Communication Services | 2025-04-04 | 31 | -30% | 9 | 14% | +14% | +39% | yes | 2.2 | +137% (10.0) | -1% (0.1) | -1% | 38 | +104% | +31% |
| 8 | GOOG | Alphabet Inc. (Class C) | Communication Services | 2025-04-04 | 31 | -29% | 9 | 15% | +14% | +39% | yes | 2.2 | +134% (10.0) | -1% (0.1) | -1% | 38 | +100% | +31% |
| 9 | VRT | Vertiv | Industrials | 2025-04-04 | 31 | -62% | 19 | 30% | +17% | +8% | yes | 0.2 | +365% (11.7) | +6% (0.1) | +6% | 37 | +340% | +31% |
| 10 | ALSN | Allison Transmission | Industrials | 2025-04-04 | 33 | -30% | 18 | 46% | +6% | +12% | yes | 1.2 | +49% (11.0) | -7% (7.5) | -2% | 34 | +38% | +31% |
| 11 | PHM | PulteGroup | Consumer Discretionary | 2025-04-11 | 33 | -37% | 54 | 44% | +12% | +25% | yes | 2.9 | +52% (10.1) | -2% (0.2) | -2% | 33 | +28% | +29% |
| 12 | ACM | AECOM | Industrials | 2025-04-04 | 33 | -25% | 18 | 43% | +9% | +680% | yes | 1.3 | +51% (6.9) | -6% (11.8) | -2% | 30 ↓ | -4% | +31% |
| 13 | CPAY | Corpay | Financials | 2025-04-04 | 33 | -28% | 18 | 37% | +6% | +6% | yes | 1.2 | +23% (10.2) | -12% (6.9) | -2% | 32 ↓ | +2% | +31% |
| 14 | TOL | Toll Brothers | Consumer Discretionary | 2025-03-14 | 33 | -38% | 43 | 38% | +6% | +17% | yes | 4.3 | +60% (11.0) | -14% (0.8) | -14% | 29 ↓ | +31% | +19% |
| 15 | MEDP | Medpace | Health Care | 2025-04-04 | 33 | -38% | 38 | 19% | +12% | +42% | yes | 3.6 | +116% (9.6) | -3% (0.1) | -3% | 35 | +74% | +31% |
| 16 | FTNT | Fortinet | Information Technology | 2025-08-08 | 34 | -35% | 24 | 40% | +14% | +58% | yes | 8.9 | +126% (11.9) | +0% (0.1) | +0% | 38 | +115% | +23% |
| 17 | UHS | Universal Health Services | Health Care | 2025-03-14 | 34 | -31% | 27 | 18% | +11% | +64% | yes | 6.4 | +46% (8.4) | -7% (4.5) | -7% | 36 | +15% | +19% |
| 18 | JLL | Jones Lang LaSalle | Real Estate | 2025-04-11 | 34 | -27% | 24 | 48% | +13% | +142% | yes | 2.5 | +70% (9.6) | -3% (0.3) | -3% | 34 | +51% | +29% |
| 19 | KNSL | Kinsale Capital Group | Financials | 2025-11-21 | 34 | -30% | 89 | 6% | +18% | +16% | open | – | +8% (2.5) | -24% (6.4) | -24% | 29 ↓ | -14% (so far) | +18% (so far) |
| 20 | DVA | DaVita | Health Care | 2025-10-31 | 34 | -34% | 58 | 12% | +5% | +4% | yes | 3.2 | +102% (8.9) | -13% (2.5) | -13% | 28 ↓ | +50% (so far) | +14% (so far) |


#### 2026: 8 buys, 3 hit +20%, SPY +14% that year

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | EXLS | EXL Service | Industrials | 2026-02-06 | 26 | -40% | 52 | 50% | +14% | +30% | yes | 6.6 | +21% (6.7) | -20% (4.6) | -20% | 24 ↓ | +10% (so far) | +13% (so far) |
| 2 | ROL | Rollins, Inc. | Industrials | 2026-05-29 | 30 | -28% | 51 | 49% | +11% | +10% | open | – | +0% (0.4) | -37% (3.9) | -37% | 16 ↓ | -37% (so far) | +2% (so far) |
| 3 | UHS | Universal Health Services | Health Care | 2026-05-22 | 32 | -36% | 25 | 6% | +10% | +37% | open | – | +15% (4.1) | -10% (0.9) | -10% | 28 ↓ | +14% (so far) | +4% (so far) |
| 4 | ADC | Agree Realty | Real Estate | 2026-09-18 | 33 | -17% | 28 | 30% | +18% | +11% | open | – | -1% (0.1) | -1% (0.2) | -1% | 32 ↓ | -1% (so far) | +1% (so far) |
| 5 | BKNG | Booking Holdings | Consumer Discretionary | 2026-02-06 | 34 | -24% | 60 | 28% | +13% | +4% | yes | 6.0 | +21% (6.0) | -13% (3.2) | -13% | 29 ↓ | -7% (so far) | +13% (so far) |
| 6 | PTC | PTC Inc. | Information Technology | 2026-01-23 | 34 | -26% | 25 | 40% | +19% | +95% | open | – | +2% (0.1) | -31% (5.0) | -31% | 26 ↓ | -15% (so far) | +13% (so far) |
| 7 | ULTA | Ulta Beauty | Consumer Discretionary | 2026-06-19 | 34 | -36% | 17 | 16% | +10% | +1% | yes | 1.6 | +24% (1.6) | -1% (0.4) | -1% | 38 | +20% (so far) | +4% (so far) |
| 8 | ALLE | Allegion | Industrials | 2026-03-20 | 35 | -22% | 26 | 38% | +8% | +9% | open | – | +19% (4.6) | -12% (1.8) | -12% | 28 ↓ | +9% (so far) | +20% (so far) |


## no fundamentals filter

1913 signals since 2010, 324 after the top-20 cut per year (the cap bound in 2011, 2012, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026), 35 dropped by the sector rule.

Dropped by the sector rule: MZTI 2010-08-20, IFF 2011-08-19, BALL 2011-09-23, UGI 2011-08-05, ED 2012-11-09, ATR 2012-11-16, NJR 2012-04-13, D 2012-11-09, MNST 2012-10-26, SO 2012-11-16, TGT 2013-08-30, RGLD 2013-02-15, HSY 2014-08-01, SJM 2014-02-07, KDP 2016-11-11, KMB 2016-10-28, BKH 2017-11-03, EIX 2017-12-08, EVRG 2017-04-21, PM 2017-11-03, CASY 2017-07-07, UGI 2019-08-09, MZTI 2019-10-04, PNW 2019-11-08, NJR 2019-08-23, SAM 2021-07-23, SMG 2021-08-06, ATR 2021-09-17, HRL 2021-09-03, CHD 2021-02-26, DAR 2023-03-17, MDLZ 2023-10-06, WLK 2024-12-13, NUE 2024-06-14, NEE 2026-09-25.

### Summary by year

| Year | SPY cal. year | Buys | Hit +20% in 12m | Months to hit (median / mean / max) | ≤3m / ≤6m | 12m return: median / mean | 12m best | 12m worst | beat SPY (same 12m) | SPY same 12m (median) | Max gain (median / best) | Max DD (median / worst) | RSI went lower | Misses | Miss DD (median / worst) | Miss 12m (median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | +15% | 4 | 4/4 = 100% | 4.5 / 4.1 / 5.3 | 25% / 100% | +26% / +35% | +71% ISRG | +19% SF | 75% | +7% | +57% / +81% ISRG | -5% / -9% PB | 75% | 0/4 = 0% | – / – | – |
| 2011 | +2% | 17 | 13/17 = 76% | 2.7 / 3.4 / 9.0 | 47% / 71% | +23% / +26% | +87% MMS | -9% CHRW | 47% | +22% | +41% / +99% FFIV | -10% / -32% LII | 47% | 4/17 = 24% | -12% / -16% | +8% |
| 2012 | +16% | 14 | 12/14 = 86% | 3.8 / 4.8 / 11.4 | 36% / 57% | +36% / +32% | +79% CNC | -7% SGI | 57% | +26% | +37% / +88% HALO | -5% / -60% SGI | 64% | 2/14 = 14% | -44% / -60% | -4% |
| 2013 | +32% | 17 | 11/17 = 65% | 7.5 / 6.6 / 9.3 | 6% / 24% | +19% / +21% | +99% OKE | -29% CVLT | 47% | +20% | +27% / +101% OKE | -2% / -36% CVLT | 53% | 6/17 = 35% | -11% / -36% | +4% |
| 2014 | +13% | 18 | 10/18 = 56% | 3.3 / 3.4 / 7.5 | 28% / 44% | -7% / -3% | +30% WRB | -44% NOV | 33% | +8% | +21% / +49% ALV | -19% / -44% NOV | 50% | 8/18 = 44% | -32% / -44% | -26% |
| 2015 | +1% | 20 | 13/20 = 65% | 5.8 / 5.9 / 10.1 | 20% / 35% | +16% / +13% | +61% THO | -26% AMG | 60% | +13% | +28% / +64% THO | -10% / -38% AMG | 60% | 7/20 = 35% | -33% / -38% | -16% |
| 2016 | +12% | 18 | 13/18 = 72% | 2.7 / 2.8 / 5.6 | 50% / 72% | +25% / +27% | +113% NVR | -24% BBWI | 50% | +22% | +31% / +113% NVR | -6% / -36% BBWI | 67% | 5/18 = 28% | -18% / -36% | +3% |
| 2017 | +22% | 15 | 8/15 = 53% | 5.0 / 6.3 / 11.9 | 0% / 33% | +13% / +10% | +54% ROST | -29% XRAY | 33% | +16% | +22% / +55% ROST | -11% / -40% DKS | 87% | 7/15 = 47% | -23% / -40% | -12% |
| 2018 | -5% | 20 | 15/20 = 75% | 4.0 / 5.1 / 10.9 | 20% / 50% | +27% / +28% | +79% CLH | -22% EWBC | 75% | +12% | +33% / +79% CLH | -10% / -35% NXPI | 65% | 5/20 = 25% | -17% / -35% | -4% |
| 2019 | +31% | 16 | 11/16 = 69% | 5.3 / 4.5 / 7.9 | 25% / 44% | +34% / +43% | +279% TSLA | -34% TKO | 56% | +16% | +42% / +335% TSLA | -24% / -46% ULTA | 75% | 5/16 = 31% | -36% / -45% | -2% |
| 2020 | +18% | 20 | 19/20 = 95% | 0.6 / 1.5 / 7.9 | 85% / 90% | +49% / +56% | +124% LH | +15% AFL | 45% | +73% | +53% / +130% LH | -8% / -51% LAMR | 30% | 1/20 = 5% | -41% / -41% | +15% |
| 2021 | +29% | 15 | 7/15 = 47% | 5.0 / 6.7 / 11.5 | 7% / 27% | -25% / -13% | +21% AMT | -62% XYZ | 47% | -14% | +17% / +53% AMT | -33% / -72% XYZ | 80% | 8/15 = 53% | -45% / -72% | -38% |
| 2022 | -18% | 20 | 12/20 = 60% | 5.7 / 5.2 / 9.2 | 25% / 30% | +8% / +16% | +129% AXON | -28% TRU | 65% | +2% | +28% / +137% AXON | -12% / -62% META | 70% | 8/20 = 40% | -29% / -62% | -16% |
| 2023 | +26% | 18 | 13/18 = 72% | 3.5 / 3.9 / 8.7 | 22% / 61% | +25% / +17% | +43% OMC | -22% VC | 33% | +33% | +34% / +50% DHR | -10% / -28% LSCC | 67% | 5/18 = 28% | -19% / -27% | -1% |
| 2024 | +25% | 18 | 11/18 = 61% | 2.8 / 3.6 / 7.8 | 33% / 50% | +8% / +16% | +99% SMCI | -29% HUM | 50% | +16% | +28% / +133% SMCI | -19% / -43% BRKR | 78% | 7/18 = 39% | -35% / -43% | -19% |
| 2025 | +18% | 20 (3 open) | 14/20 = 70% | 1.3 / 2.2 / 6.0 | 50% / 70% | +17% / +21% | +102% CMI | -32% GDDY | 41% | +31% | +51% / +121% CMI | -5% / -44% GDDY | 35% | 4/17 = 24% | -33% / -44% | -12% |
| 2026 | +14% | 19 (19 open) | 9/19 = 47% | 3.2 / 4.0 / 7.2 | 21% / 32% | – / – | – | – | – | – | +20% / +38% NWS | -10% / -50% PLNT | 72% | 0/0 | – / – | – |
| **All complete 12m windows (signals 2010–2025-09-25)** |  | 267 | 185/267 = 69% | 3.6 / 4.2 / 11.9 | 31% / 52% | +20% / +21% | +279% TSLA | -62% XYZ | 50% | +18% | +31% / +335% TSLA | -10% / -72% XYZ | 61% | 82/267 = 31% | -29% / -72% | -12% |
| **All incl. open** |  | 289 (22 open) | 195/289 = 67% | 3.6 / 4.1 / 11.9 | 30% / 51% | +20% / +21% | +279% TSLA | -62% XYZ | 50% | +18% | +30% / +335% TSLA | -11% / -72% XYZ | 62% | 82/267 = 31% | -29% / -72% | -12% |


"Buys" = signals kept after the top-20 cut. "Hit" counts open windows that already reached the target; "Misses" are complete windows only. Months are calendar months (30.44 days) from the signal week's Friday. "RSI went lower" = share of buys whose weekly RSI printed below the signal RSI within the next 12 months.

### Buys by year


#### 2010: 4 buys, 4 hit +20%, SPY +15% that year, 12m median +26%, best +71%, worst +19%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PB | Prosperity Bancshares | Financials | 2010-08-13 | 33 | -33% | 99 | 24% | – | +30% | yes | 4.0 | +52% (11.2) | -9% (0.6) | -9% | 30 ↓ | +20% | +11% |
| 2 | DLR | Digital Realty | Real Estate | 2010-11-19 | 34 | -20% | 30 | – | – | – | yes | 5.3 | +33% (12.0) | -4% (0.9) | -4% | 33 ↓ | +33% | +3% |
| 3 | ISRG | Intuitive Surgical | Health Care | 2010-11-19 | 34 | -37% | 31 | 15% | +40% | +67% | yes | 2.1 | +81% (11.9) | +2% (0.1) | +2% | 37 | +71% | +3% |
| 4 | SF | Stifel | Financials | 2010-06-11 | 35 | -25% | 90 | 30% | +24% | +19% | yes | 5.0 | +63% (8.9) | -5% (0.7) | -5% | 31 ↓ | +19% | +19% |


#### 2011: 17 buys, 13 hit +20%, SPY +2% that year, 12m median +23%, best +87%, worst -9%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | LII | Lennox International | Industrials | 2011-07-29 | 26 | -32% | 66 | 48% | +9% | +119% | yes | 9.0 | +33% (11.2) | -32% (1.8) | -32% | 17 ↓ | +23% | +10% |
| 2 | CTSH | Cognizant | Information Technology | 2011-08-19 | 28 | -34% | 20 | 43% | +43% | +35% | yes | 1.3 | +41% (7.2) | +1% (10.8) | +3% | 32 | +17% | +29% |
| 3 | CHE | Chemed Corp. | Health Care | 2011-08-05 | 28 | -24% | 12 | 62% | +8% | +10% | **no** | – | +18% (11.7) | -12% (4.3) | -12% | 28 | +12% | +19% |
| 4 | ROP | Roper Technologies | Information Technology | 2011-08-19 | 29 | -26% | 20 | 72% | +20% | +38% | yes | 2.2 | +62% (12.0) | -0% (0.1) | -0% | 40 | +62% | +29% |
| 5 | PH | Parker Hannifin | Industrials | 2011-08-05 | 29 | -32% | 25 | 49% | +24% | +152% | yes | 2.7 | +36% (7.3) | -10% (1.9) | -10% | 28 ↓ | +21% | +19% |
| 6 | SWK | Stanley Black & Decker | Industrials | 2011-08-19 | 30 | -28% | 20 | 55% | +125% | +20% | yes | 2.7 | +48% (6.9) | -14% (1.1) | -14% | 29 ↓ | +25% | +29% |
| 7 | APH | Amphenol | Information Technology | 2011-08-05 | 30 | -27% | 22 | 28% | +27% | +52% | yes | 5.5 | +42% (7.9) | -8% (1.9) | -8% | 33 | +38% | +19% |
| 8 | PB | Prosperity Bancshares | Financials | 2011-08-19 | 30 | -28% | 16 | 83% | – | +16% | yes | 4.1 | +41% (7.0) | -6% (1.5) | -6% | 33 | +25% | +29% |
| 9 | ALV | Autoliv | Consumer Discretionary | 2011-08-05 | 30 | -33% | 29 | 38% | +40% | +5675% | yes | 6.0 | +27% (7.3) | -17% (1.9) | -17% | 25 ↓ | +5% | +19% |
| 10 | BIO | Bio-Rad Laboratories | Health Care | 2011-08-05 | 30 | -21% | 11 | 37% | +8% | +25% | **no** | – | +13% (8.0) | -13% (1.6) | -13% | 26 ↓ | -4% | +19% |
| 11 | GGG | Graco Inc. | Industrials | 2011-08-19 | 30 | -37% | 6 | 45% | +29% | +168% | yes | 2.3 | +66% (8.0) | -5% (1.5) | -5% | 35 | +50% | +29% |
| 12 | EMR | Emerson Electric | Industrials | 2011-08-05 | 30 | -27% | 24 | 36% | +10% | +37% | **no** | – | +19% (6.1) | -10% (1.9) | -10% | 28 ↓ | +10% | +19% |
| 13 | FFIV | F5, Inc. | Information Technology | 2011-08-19 | 31 | -52% | 31 | 31% | +35% | +115% | yes | 0.9 | +99% (7.5) | -0% (0.1) | -0% | 34 | +49% | +29% |
| 14 | CHRW | C.H. Robinson | Industrials | 2011-08-19 | 31 | -23% | 32 | 57% | +20% | +14% | yes | 2.2 | +20% (2.2) | -16% (11.2) | +1% | 33 | -9% | +29% |
| 15 | MMS | Maximus Inc. | Industrials | 2011-09-23 | 31 | -25% | 19 | 33% | +16% | +61% | yes | 1.0 | +87% (12.0) | +2% (0.1) | +2% | 43 | +87% | +31% |
| 16 | UHS | Universal Health Services | Health Care | 2011-08-12 | 31 | -33% | 13 | 83% | – | +5% | **no** | – | +18% (6.6) | -16% (1.7) | -16% | 29 ↓ | +5% | +22% |
| 17 | SNX | TD Synnex | Information Technology | 2011-08-05 | 31 | -30% | 22 | 44% | +12% | +36% | yes | 5.0 | +70% (7.7) | -10% (0.5) | -10% | 25 ↓ | +30% | +19% |


#### 2012: 14 buys, 12 hit +20%, SPY +16% that year, 12m median +36%, best +79%, worst -7%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DLTR | Dollar Tree | Consumer Staples | 2012-10-12 | 29 | -28% | 16 | 75% | +12% | +25% | yes | 6.8 | +44% (11.7) | -8% (1.1) | -8% | 26 ↓ | +43% | +22% |
| 2 | DLR | Digital Realty | Real Estate | 2012-10-26 | 30 | -24% | 26 | 4% | +14% | +34% | yes | 3.1 | +23% (5.7) | -14% (9.8) | -3% | 29 ↓ | -0% | +27% |
| 3 | HALO | Halozyme | Health Care | 2012-08-03 | 31 | -66% | 18 | 13% | +312% | – | yes | 0.1 | +88% (11.4) | +5% (0.1) | +5% | 36 | +53% | +25% |
| 4 | NSC | Norfolk Southern | Industrials | 2012-11-09 | 32 | -26% | 71 | 24% | +4% | +7% | yes | 2.5 | +55% (11.6) | -3% (0.2) | -3% | 30 ↓ | +52% | +31% |
| 5 | NKE | Nike, Inc. | Consumer Discretionary | 2012-06-29 | 32 | -24% | 15 | 86% | +16% | +14% | yes | 5.7 | +52% (10.5) | +1% (0.1) | +1% | 38 | +47% | +21% |
| 6 | KEX | Kirby Corporation | Industrials | 2012-05-18 | 32 | -22% | 17 | 62% | +67% | +55% | yes | 8.3 | +48% (12.0) | -18% (1.3) | -18% | 24 ↓ | +48% | +32% |
| 7 | DRI | Darden Restaurants | Consumer Discretionary | 2012-12-21 | 33 | -22% | 139 | 63% | +6% | +8% | yes | 4.5 | +25% (11.0) | -2% (0.2) | -2% | 31 ↓ | +18% | +30% |
| 8 | CNC | Centene Corporation | Health Care | 2012-06-15 | 33 | -45% | 10 | 68% | +27% | +14% | yes | 0.8 | +85% (11.0) | +1% (0.1) | +1% | 35 | +79% | +24% |
| 9 | CMG | Chipotle Mexican Grill | Consumer Discretionary | 2012-07-20 | 33 | -28% | 14 | 76% | – | +23% | yes | 11.4 | +29% (12.0) | -25% (3.1) | -25% | 29 ↓ | +29% | +27% |
| 10 | CLH | Clean Harbors | Industrials | 2012-09-21 | 33 | -33% | 33 | 42% | +23% | +15% | yes | 1.3 | +24% (1.5) | -2% (0.4) | -2% | 33 | +19% | +20% |
| 11 | MCD | McDonald's | Consumer Discretionary | 2012-06-01 | 33 | -15% | 19 | 35% | +12% | +13% | yes | 10.3 | +22% (10.3) | -2% (5.5) | -2% | 35 | +15% | +30% |
| 12 | GNTX | Gentex | Consumer Discretionary | 2012-04-20 | 34 | -40% | 64 | 16% | +25% | +16% | **no** | – | +10% (0.6) | -29% (3.2) | -29% | 28 ↓ | -0% | +15% |
| 13 | OLED | Universal Display | Information Technology | 2012-11-09 | 34 | -62% | 83 | 3% | +115% | – | yes | 2.8 | +55% (9.1) | -8% (0.2) | -8% | 32 ↓ | +50% | +31% |
| 14 | SGI | Somnigroup International | Consumer Discretionary | 2012-05-11 | 34 | -40% | 5 | 39% | +28% | +47% | **no** | – | -2% (0.1) | -60% (1.5) | -60% | 22 ↓ | -7% | +23% |


#### 2013: 17 buys, 11 hit +20%, SPY +32% that year, 12m median +19%, best +99%, worst -29%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | EW | Edwards Lifesciences | Health Care | 2013-04-26 | 26 | -42% | 39 | 34% | +13% | +25% | yes | 5.7 | +27% (11.7) | -4% (7.6) | -3% | 26 ↓ | +25% | +20% |
| 2 | FRT | Federal Realty Investment Trust | Real Estate | 2013-06-21 | 31 | -18% | 6 | 75% | +10% | -10% | yes | 9.3 | +29% (11.5) | -1% (0.1) | -1% | 35 | +28% | +26% |
| 3 | IRM | Iron Mountain | Real Estate | 2013-06-07 | 31 | -27% | 4 | 79% | – | -61% | **no** | – | +13% (12.0) | -11% (4.1) | -11% | 27 ↓ | +13% | +21% |
| 4 | SPG | Simon Property Group | Real Estate | 2013-08-16 | 31 | -20% | 14 | 77% | +13% | -32% | yes | 8.4 | +28% (11.2) | -2% (0.7) | -2% | 33 | +27% | +20% |
| 5 | RYN | Rayonier | Real Estate | 2013-10-25 | 32 | -23% | 23 | 76% | +13% | +34% | **no** | – | +7% (8.0) | -11% (3.0) | -11% | 27 ↓ | -1% | +14% |
| 6 | LH | Labcorp | Health Care | 2013-12-13 | 32 | -17% | 4 | 76% | +3% | +0% | yes | 8.5 | +23% (10.6) | -1% (1.7) | -1% | 34 | +14% | +15% |
| 7 | CHE | Chemed Corp. | Health Care | 2013-05-10 | 32 | -22% | 11 | 76% | +5% | +9% | yes | 6.3 | +45% (10.8) | +2% (0.1) | +2% | 41 | +36% | +17% |
| 8 | OKE | Oneok | Energy | 2013-07-05 | 33 | -24% | 39 | 90% | -12% | +0% | yes | 0.7 | +101% (11.9) | +4% (0.1) | +4% | 44 | +99% | +24% |
| 9 | CVLT | CommVault Systems | Information Technology | 2013-12-13 | 33 | -25% | 39 | 39% | +21% | +42% | **no** | – | +13% (1.5) | -36% (10.5) | -36% | 29 ↓ | -29% | +15% |
| 10 | VTR | Ventas | Real Estate | 2013-08-16 | 33 | -29% | 13 | 53% | +15% | -17% | **no** | – | +19% (8.7) | -5% (3.6) | -5% | 33 ↓ | +14% | +20% |
| 11 | IBM | IBM | Information Technology | 2013-10-18 | 34 | -20% | 117 | 54% | -4% | +2% | **no** | – | +15% (5.8) | -1% (0.1) | -1% | 36 | +7% | +10% |
| 12 | ISRG | Intuitive Surgical | Health Care | 2013-07-12 | 34 | -28% | 64 | 21% | +23% | +29% | yes | 8.7 | +26% (8.7) | -18% (9.9) | -17% | 28 ↓ | -9% | +20% |
| 13 | DOC | Healthpeak Properties | Real Estate | 2013-06-21 | 34 | -23% | 5 | 81% | +6% | +28% | **no** | – | +9% (0.9) | -15% (5.7) | -15% | 31 ↓ | +0% | +26% |
| 14 | NVR | NVR, Inc. | Consumer Discretionary | 2013-08-30 | 34 | -22% | 22 | 0% | +28% | +45% | yes | 3.9 | +43% (6.1) | -2% (0.2) | -2% | 34 ↓ | +37% | +25% |
| 15 | WELL | Welltower | Real Estate | 2013-11-29 | 35 | -30% | 28 | 46% | +38% | -11% | yes | 8.4 | +38% (12.0) | -6% (0.7) | -6% | 31 ↓ | +38% | +17% |
| 16 | VMRK | Vivmark Residential | Real Estate | 2013-08-16 | 35 | -23% | 108 | – | – | +75% | yes | 7.5 | +36% (11.4) | -0% (0.1) | -0% | 39 | +34% | +20% |
| 17 | DINO | HF Sinclair | Energy | 2013-07-05 | 35 | -33% | 17 | – | – | – | yes | 4.7 | +39% (9.8) | +1% (0.2) | +1% | 40 | +19% | +24% |


#### 2014: 18 buys, 10 hit +20%, SPY +13% that year, 12m median -7%, best +30%, worst -44%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2014-05-23 | 26 | -27% | 108 | 33% | +6% | +25% | yes | 7.5 | +38% (10.4) | -2% (2.5) | -2% | 31 | +27% | +14% |
| 2 | EQT | EQT Corporation | Energy | 2014-10-10 | 28 | -26% | 29 | – | – | +88% | yes | 0.9 | +22% (0.9) | -21% (11.7) | -5% | 31 | -9% | +8% |
| 3 | ARW | Arrow Electronics | Information Technology | 2014-10-10 | 28 | -25% | 47 | 66% | +7% | +12% | yes | 0.9 | +35% (5.4) | -3% (0.1) | -3% | 33 | +22% | +8% |
| 4 | DAR | Darling Ingredients | Consumer Staples | 2014-10-10 | 28 | -29% | 50 | 64% | +60% | -73% | **no** | – | +13% (1.5) | -36% (11.7) | -36% | 23 ↓ | -32% | +8% |
| 5 | TKR | Timken | Industrials | 2014-10-10 | 28 | -23% | 14 | 81% | -6% | -12% | **no** | – | +15% (1.5) | -29% (11.6) | -29% | 19 ↓ | -17% | +8% |
| 6 | ROK | Rockwell Automation | Industrials | 2014-10-10 | 29 | -22% | 31 | 68% | +4% | +9% | yes | 6.7 | +28% (8.0) | -2% (0.1) | -2% | 30 | +7% | +8% |
| 7 | NOV | NOV Inc. | Energy | 2014-12-12 | 29 | -29% | 20 | 30% | -6% | +21% | **no** | – | +9% (0.2) | -44% (12.0) | -44% | 18 ↓ | -44% | +3% |
| 8 | HAL | Halliburton | Energy | 2014-10-10 | 29 | -27% | 11 | 68% | +6% | +63% | **no** | – | +3% (0.4) | -38% (10.5) | -38% | 20 ↓ | -26% | +8% |
| 9 | WCC | WESCO International | Industrials | 2014-10-10 | 29 | -23% | 38 | 62% | +9% | +1% | **no** | – | +19% (1.1) | -37% (11.7) | -37% | 22 ↓ | -30% | +8% |
| 10 | BIO | Bio-Rad Laboratories | Health Care | 2014-10-10 | 30 | -19% | 79 | 75% | +3% | -56% | yes | 4.7 | +40% (9.1) | -2% (0.1) | -2% | 34 | +28% | +8% |
| 11 | IEX | IDEX Corporation | Industrials | 2014-10-10 | 30 | -17% | 14 | 67% | +6% | +406% | **no** | – | +19% (8.4) | -2% (0.1) | -2% | 34 | +17% | +8% |
| 12 | PSKY | Paramount Skydance Corporation | Communication Services | 2014-10-10 | 30 | -27% | 31 | – | – | – | yes | 4.1 | +28% (5.3) | -22% (11.6) | -2% | 20 ↓ | -13% | +8% |
| 13 | PH | Parker Hannifin | Industrials | 2014-10-17 | 30 | -20% | 41 | 64% | +2% | +10% | yes | 0.5 | +28% (1.3) | -7% (11.4) | +2% | 28 ↓ | -2% | +10% |
| 14 | WRB | W. R. Berkley Corporation | Financials | 2014-01-31 | 30 | -15% | 42 | 3% | +13% | +16% | yes | 4.9 | +41% (10.2) | -2% (0.1) | -2% | 32 | +30% | +14% |
| 15 | MAT | Mattel | Consumer Discretionary | 2014-01-31 | 31 | -22% | 37 | 79% | +5% | -1% | **no** | – | +8% (2.0) | -27% (11.9) | -27% | 23 ↓ | -26% | +14% |
| 16 | ALV | Autoliv | Consumer Discretionary | 2014-10-10 | 31 | -18% | 18 | 77% | +10% | -15% | yes | 2.4 | +49% (7.3) | -1% (0.1) | -1% | 31 | +30% | +8% |
| 17 | GATX | GATX | Industrials | 2014-10-10 | 31 | -22% | 28 | 64% | +7% | +42% | yes | 0.9 | +21% (1.5) | -18% (11.7) | -2% | 31 | -6% | +8% |
| 18 | DOV | Dover Corporation | Industrials | 2014-10-10 | 31 | -18% | 14 | 21% | +7% | – | **no** | – | +10% (1.5) | -25% (10.5) | -25% | 25 ↓ | -17% | +8% |


#### 2015: 20 buys, 13 hit +20%, SPY +1% that year, 12m median +16%, best +61%, worst -26%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2015-10-23 | 26 | -30% | 31 | 10% | +9% | +13% | yes | 8.7 | +49% (11.0) | -18% (2.7) | -18% | 24 ↓ | +37% | +5% |
| 2 | CFR | Frost Bank | Financials | 2015-01-09 | 27 | -22% | 72 | 26% | +7% | +10% | yes | 4.8 | +28% (5.5) | -11% (12.0) | -3% | 27 ↓ | -11% | -4% |
| 3 | SHW | Sherwin-Williams | Materials | 2015-09-25 | 28 | -23% | 24 | 75% | +8% | +24% | yes | 1.8 | +38% (9.8) | -4% (0.1) | -4% | 35 | +26% | +14% |
| 4 | JAZZ | Jazz Pharmaceuticals | Health Care | 2015-09-25 | 28 | -31% | 82 | 59% | +27% | +232% | **no** | – | +17% (6.9) | -16% (4.6) | -16% | 29 | -6% | +14% |
| 5 | NEU | NewMarket Corporation | Materials | 2015-07-31 | 29 | -18% | 22 | 80% | -3% | -4% | **no** | – | +13% (11.9) | -18% (6.3) | -18% | 26 ↓ | +9% | +5% |
| 6 | COO | Cooper Companies (The) | Health Care | 2015-09-04 | 29 | -21% | 22 | 89% | +8% | -19% | yes | 10.1 | +24% (11.8) | -20% (4.5) | -20% | 24 ↓ | +23% | +16% |
| 7 | JNJ | Johnson & Johnson | Health Care | 2015-09-04 | 29 | -17% | 50 | 62% | -2% | +5% | yes | 6.6 | +40% (10.9) | -0% (0.7) | -0% | 32 | +34% | +16% |
| 8 | TROW | T. Rowe Price | Financials | 2015-08-21 | 29 | -19% | 127 | 3% | +10% | +9% | **no** | – | +11% (8.0) | -9% (4.8) | -9% | 26 ↓ | -1% | +13% |
| 9 | BLK | BlackRock | Financials | 2015-08-21 | 30 | -20% | 117 | – | – | – | yes | 8.0 | +25% (11.5) | -4% (5.2) | -4% | 28 ↓ | +24% | +13% |
| 10 | CSL | Carlisle Companies | Industrials | 2015-10-23 | 30 | -18% | 68 | 77% | – | +6% | yes | 5.8 | +28% (8.6) | -9% (2.9) | -9% | 28 ↓ | +23% | +5% |
| 11 | THO | Thor Industries | Consumer Discretionary | 2015-09-25 | 30 | -20% | 100 | 31% | +18% | +15% | yes | 5.7 | +64% (11.4) | -6% (4.6) | -6% | 35 | +61% | +14% |
| 12 | MMM | 3M | Industrials | 2015-08-21 | 30 | -17% | 34 | 83% | -1% | +8% | yes | 7.8 | +30% (11.0) | -3% (1.1) | -3% | 30 | +30% | +13% |
| 13 | GBCI | Glacier Bancorp | Financials | 2015-01-30 | 30 | -28% | 57 | – | – | +21% | yes | 2.9 | +36% (9.2) | +3% (0.1) | +3% | 36 | +10% | -1% |
| 14 | CGNX | Cognex | Information Technology | 2015-08-07 | 30 | -29% | 17 | 71% | +40% | +44% | yes | 10.0 | +34% (12.0) | -23% (5.1) | -23% | 27 ↓ | +34% | +7% |
| 15 | RBC | RBC Bearings | Industrials | 2015-09-04 | 31 | -25% | 20 | 87% | +11% | -10% | yes | 2.0 | +36% (12.0) | -5% (4.7) | -1% | 32 | +36% | +16% |
| 16 | ST | Sensata Technologies | Industrials | 2015-08-21 | 31 | -21% | 19 | 60% | +32% | -11% | **no** | – | +7% (2.2) | -35% (5.7) | -35% | 27 ↓ | -16% | +13% |
| 17 | BEN | Franklin Resources | Financials | 2015-07-24 | 31 | -22% | 114 | 19% | +1% | +9% | **no** | – | +0% (0.1) | -33% (11.1) | -33% | 18 ↓ | -23% | +7% |
| 18 | AMG | Affiliated Managers Group | Financials | 2015-08-21 | 31 | -17% | 84 | 52% | – | +31% | **no** | – | -1% (0.2) | -38% (5.7) | -38% | 24 ↓ | -26% | +13% |
| 19 | ALV | Autoliv | Consumer Discretionary | 2015-08-21 | 31 | -26% | 13 | 84% | -1% | +3% | yes | 2.1 | +32% (3.4) | -1% (0.1) | -1% | 36 | +10% | +13% |
| 20 | JLL | Jones Lang LaSalle | Real Estate | 2015-09-04 | 31 | -20% | 24 | 41% | +15% | +44% | **no** | – | +17% (2.9) | -36% (10.1) | -36% | 21 ↓ | -17% | +16% |


#### 2016: 18 buys, 13 hit +20%, SPY +12% that year, 12m median +25%, best +113%, worst -24%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | VC | Visteon | Consumer Discretionary | 2016-01-29 | 20 | -45% | 10 | 90% | -61% | +619% | yes | 2.0 | +37% (11.9) | -10% (0.4) | -10% | 18 ↓ | +33% | +21% |
| 2 | TSCO | Tractor Supply | Consumer Discretionary | 2016-09-09 | 22 | -30% | 80 | 54% | +7% | +8% | **no** | – | +15% (3.4) | -26% (10.1) | -26% | 19 ↓ | -10% | +18% |
| 3 | CAH | Cardinal Health | Health Care | 2016-10-28 | 26 | -27% | 84 | – | – | – | yes | 3.7 | +25% (4.5) | -6% (12.0) | -3% | 23 ↓ | -6% | +24% |
| 4 | SEIC | SEI Investments Company | Financials | 2016-01-29 | 27 | -29% | 24 | 94% | +6% | +9% | yes | 2.7 | +33% (11.5) | -14% (0.4) | -14% | 24 ↓ | +26% | +21% |
| 5 | TYL | Tyler Technologies | Information Technology | 2016-02-19 | 29 | -34% | 11 | 90% | +17% | +30% | yes | 2.3 | +44% (7.1) | -2% (0.1) | -2% | 29 ↓ | +27% | +25% |
| 6 | CTSH | Cognizant | Information Technology | 2016-09-30 | 29 | -32% | 80 | 1% | +15% | -0% | yes | 3.2 | +53% (11.4) | +4% (0.7) | +4% | 35 | +53% | +18% |
| 7 | GILD | Gilead Sciences | Health Care | 2016-01-29 | 30 | -33% | 32 | 13% | +52% | +93% | yes | 2.6 | +24% (2.9) | -13% (11.9) | -0% | 33 | -12% | +21% |
| 8 | CNC | Centene Corporation | Health Care | 2016-11-11 | 30 | -39% | 72 | 43% | +65% | -4% | yes | 1.8 | +94% (10.1) | +2% (0.1) | +2% | 41 | +85% | +22% |
| 9 | CRM | Salesforce | Information Technology | 2016-02-05 | 30 | -29% | 102 | 55% | – | – | yes | 0.9 | +43% (3.7) | -8% (0.1) | -8% | 32 | +37% | +25% |
| 10 | AN | AutoNation | Consumer Discretionary | 2016-01-08 | 30 | -28% | 78 | 10% | +11% | +18% | **no** | – | +9% (6.7) | -18% (10.0) | -18% | 25 ↓ | +3% | +21% |
| 11 | ZBH | Zimmer Biomet | Health Care | 2016-11-04 | 30 | -23% | 12 | 67% | +63% | – | yes | 5.6 | +30% (8.4) | -5% (0.3) | -5% | 27 ↓ | +7% | +26% |
| 12 | LOW | Lowe's | Consumer Discretionary | 2016-10-28 | 30 | -20% | 83 | 77% | +6% | +5% | yes | 4.1 | +30% (6.4) | -2% (0.1) | -2% | 29 ↓ | +23% | +24% |
| 13 | BC | Brunswick | Consumer Discretionary | 2016-01-15 | 30 | -33% | 53 | 52% | +1% | -71% | yes | 2.0 | +51% (11.7) | +0% (0.1) | +0% | 36 | +49% | +23% |
| 14 | BBWI | Bath & Body Works, Inc. | Consumer Discretionary | 2016-05-06 | 30 | -31% | 56 | 86% | +6% | -100% | **no** | – | +14% (3.5) | -36% (11.0) | -36% | 25 ↓ | -24% | +19% |
| 15 | RLI | RLI Corp. | Financials | 2016-10-21 | 30 | -19% | 31 | 97% | +2% | -7% | **no** | – | +15% (2.1) | -7% (10.5) | -7% | 27 ↓ | +6% | +23% |
| 16 | NVR | NVR, Inc. | Consumer Discretionary | 2016-10-28 | 30 | -17% | 47 | 3% | +16% | +30% | yes | 2.9 | +113% (12.0) | -2% (0.2) | -2% | 29 ↓ | +113% | +24% |
| 17 | CRL | Charles River Laboratories | Health Care | 2016-11-04 | 31 | -24% | 85 | 73% | +13% | +1% | yes | 2.9 | +73% (11.7) | +3% (0.9) | +3% | 39 | +73% | +26% |
| 18 | MDT | Medtronic | Health Care | 2016-11-25 | 31 | -15% | 19 | 48% | +23% | +22% | **no** | – | +20% (7.3) | -6% (1.3) | -6% | 26 ↓ | +13% | +20% |


#### 2017: 15 buys, 8 hit +20%, SPY +22% that year, 12m median +13%, best +54%, worst -29%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PCG | PG&E Corporation | Utilities | 2017-10-13 | 27 | -19% | 29 | 73% | +7% | +168% | **no** | – | +0% (0.2) | -34% (3.9) | -34% | 12 ↓ | -18% | +10% |
| 2 | ROST | Ross Stores | Consumer Discretionary | 2017-06-23 | 29 | -19% | 30 | 80% | +8% | +13% | yes | 4.8 | +55% (11.9) | -6% (1.7) | -6% | 28 ↓ | +54% | +15% |
| 3 | MSM | MSC Industrial Direct | Industrials | 2017-07-14 | 29 | -30% | 20 | 55% | -0% | +7% | yes | 4.6 | +36% (6.4) | -11% (1.2) | -11% | 26 ↓ | +14% | +16% |
| 4 | DGX | Quest Diagnostics | Health Care | 2017-09-29 | 30 | -17% | 12 | 99% | +1% | -4% | yes | 8.4 | +25% (9.6) | -3% (0.4) | -3% | 28 ↓ | +17% | +18% |
| 5 | ENS | EnerSys | Industrials | 2017-08-11 | 31 | -25% | 35 | 74% | +2% | +22% | yes | 5.2 | +31% (11.6) | -3% (0.3) | -3% | 29 ↓ | +20% | +18% |
| 6 | XRAY | Dentsply Sirona | Health Care | 2017-08-11 | 31 | -16% | 140 | 97% | +39% | -25% | yes | 3.2 | +24% (3.6) | -29% (12.0) | -5% | 23 ↓ | -29% | +18% |
| 7 | TJX | TJX Companies | Consumer Discretionary | 2017-06-23 | 31 | -17% | 129 | 41% | +6% | +4% | yes | 8.2 | +42% (11.9) | -3% (1.0) | -3% | 34 | +40% | +15% |
| 8 | UAL | United Airlines Holdings | Industrials | 2017-09-08 | 31 | -30% | 14 | 41% | +1% | -59% | yes | 4.1 | +51% (11.9) | -2% (2.2) | -2% | 33 | +50% | +19% |
| 9 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2017-05-19 | 31 | -35% | 34 | 31% | +9% | -10% | **no** | – | +3% (0.4) | -40% (5.5) | -40% | 20 ↓ | -22% | +16% |
| 10 | ORLY | O'Reilly Automotive | Consumer Discretionary | 2017-06-09 | 32 | -20% | 84 | 55% | +6% | +13% | yes | 11.9 | +22% (12.0) | -26% (0.9) | -26% | 17 ↓ | +22% | +16% |
| 11 | ALK | Alaska Air Group | Industrials | 2017-08-25 | 32 | -26% | 25 | 84% | +12% | -15% | **no** | – | +8% (1.5) | -23% (7.2) | -23% | 26 ↓ | -12% | +20% |
| 12 | UBSI | United Bankshares | Financials | 2017-07-28 | 33 | -30% | 33 | – | – | -1% | **no** | – | +15% (10.8) | -7% (0.5) | -7% | 28 ↓ | +13% | +16% |
| 13 | AZO | AutoZone | Consumer Discretionary | 2017-04-14 | 33 | -16% | 75 | 66% | +3% | +12% | **no** | – | +16% (9.4) | -28% (2.9) | -28% | 16 ↓ | -12% | +16% |
| 14 | RNR | RenaissanceRe | Financials | 2017-09-08 | 33 | -15% | 27 | 55% | +6% | +19% | **no** | – | +9% (1.9) | -9% (4.1) | -9% | 28 ↓ | -1% | +19% |
| 15 | HSIC | Henry Schein | Health Care | 2017-09-22 | 33 | -15% | 15 | 79% | +8% | +16% | **no** | – | +8% (11.9) | -20% (5.3) | -20% | 27 ↓ | +8% | +19% |


#### 2018: 20 buys, 15 hit +20%, SPY -5% that year, 12m median +27%, best +79%, worst -22%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KDP | Keurig Dr Pepper | Consumer Staples | 2018-07-13 | 10 | -81% | 23 | 96% | +5% | +28% | yes | 9.5 | +30% (11.2) | -8% (2.8) | -8% | 10 | +21% | +10% |
| 2 | PKG | Packaging Corporation of America | Materials | 2018-10-12 | 26 | -33% | 39 | 58% | +12% | +50% | yes | 10.9 | +28% (12.0) | -11% (2.4) | -11% | 26 ↓ | +28% | +10% |
| 3 | UFPI | UFP Industries | Industrials | 2018-10-19 | 26 | -27% | 45 | 42% | +22% | +36% | yes | 6.2 | +46% (10.8) | -15% (2.2) | -15% | 24 ↓ | +45% | +10% |
| 4 | RTX | RTX Corporation | Industrials | 2018-12-21 | 27 | -26% | 47 | 56% | +8% | -2% | yes | 1.8 | +44% (12.0) | -4% (0.1) | -4% | 27 ↓ | +44% | +36% |
| 5 | MCHP | Microchip Technology | Information Technology | 2018-10-05 | 28 | -34% | 37 | 63% | +18% | -76% | yes | 4.0 | +47% (6.9) | -12% (0.6) | -12% | 23 ↓ | +38% | +4% |
| 6 | BC | Brunswick | Consumer Discretionary | 2018-10-26 | 28 | -27% | 19 | 94% | -2% | -59% | **no** | – | +18% (12.0) | -17% (7.1) | -17% | 24 ↓ | +18% | +16% |
| 7 | RJF | Raymond James Financial | Financials | 2018-10-26 | 29 | -29% | 39 | 74% | +15% | +26% | yes | 5.5 | +27% (6.1) | -5% (1.9) | -5% | 32 | +18% | +16% |
| 8 | BLK | BlackRock | Financials | 2018-10-12 | 29 | -28% | 37 | – | – | – | **no** | – | +15% (9.0) | -15% (2.4) | -15% | 22 ↓ | +5% | +10% |
| 9 | FAF | First American Financial Corporation | Financials | 2018-10-12 | 29 | -26% | 37 | 88% | +0% | +27% | yes | 6.0 | +35% (10.9) | -7% (2.4) | -7% | 25 ↓ | +32% | +10% |
| 10 | CBRE | CBRE Group | Real Estate | 2018-10-12 | 29 | -23% | 37 | 21% | +45% | +4% | yes | 4.0 | +43% (10.9) | -3% (2.4) | -3% | 30 | +33% | +10% |
| 11 | URI | United Rentals | Industrials | 2018-10-19 | 29 | -39% | 32 | 56% | +22% | +165% | yes | 6.3 | +20% (6.3) | -18% (2.2) | -18% | 27 ↓ | +10% | +10% |
| 12 | LMT | Lockheed Martin | Industrials | 2018-12-21 | 29 | -29% | 44 | 84% | +4% | -28% | yes | 2.3 | +58% (8.9) | -4% (0.1) | -4% | 32 | +55% | +36% |
| 13 | CACI | CACI International | Industrials | 2018-12-21 | 29 | -29% | 15 | 88% | +3% | +77% | yes | 1.5 | +77% (12.0) | -2% (0.1) | -2% | 31 | +77% | +36% |
| 14 | HUBB | Hubbell Incorporated | Industrials | 2018-04-27 | 29 | -30% | 15 | 80% | +5% | -16% | yes | 3.8 | +32% (4.8) | -10% (7.9) | -2% | 29 ↓ | +21% | +12% |
| 15 | BAX | Baxter International | Health Care | 2018-11-02 | 29 | -21% | 40 | 48% | +7% | -1% | yes | 3.7 | +46% (10.1) | -1% (0.3) | -1% | 33 | +27% | +15% |
| 16 | WTFC | Wintrust Financial | Financials | 2018-10-26 | 29 | -27% | 87 | 69% | – | +31% | **no** | – | +7% (0.4) | -17% (9.6) | -17% | 27 ↓ | -9% | +16% |
| 17 | NXPI | NXP Semiconductors | Information Technology | 2018-04-20 | 30 | -17% | 8 | 44% | -3% | +1005% | **no** | – | +14% (1.6) | -35% (8.1) | -35% | 21 ↓ | -4% | +11% |
| 18 | CLH | Clean Harbors | Industrials | 2018-12-21 | 30 | -34% | 14 | 60% | +10% | +3243% | yes | 1.1 | +79% (12.0) | -3% (0.1) | -3% | 30 | +79% | +36% |
| 19 | EWBC | East West Bancorp | Financials | 2018-10-12 | 30 | -24% | 37 | 62% | – | +13% | **no** | – | +0% (4.3) | -31% (10.5) | -31% | 22 ↓ | -22% | +10% |
| 20 | PSX | Phillips 66 | Energy | 2018-11-23 | 30 | -28% | 27 | 62% | +17% | +233% | yes | 9.8 | +38% (11.5) | -12% (1.0) | -12% | 29 ↓ | +36% | +20% |


#### 2019: 16 buys, 11 hit +20%, SPY +31% that year, 12m median +34%, best +279%, worst -34%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ULTA | Ulta Beauty | Consumer Discretionary | 2019-08-30 | 26 | -36% | 41 | 55% | +13% | +28% | yes | 5.3 | +27% (5.7) | -46% (6.6) | -5% | 24 ↓ | -0% | +22% |
| 2 | TKO | TKO Group Holdings | Communication Services | 2019-11-01 | 30 | -44% | 57 | – | – | – | **no** | – | +19% (2.2) | -45% (4.5) | -45% | 25 ↓ | -34% | +9% |
| 3 | FCFS | FirstCash | Financials | 2019-11-08 | 31 | -25% | 74 | 34% | +4% | +1% | **no** | – | +9% (2.7) | -34% (11.7) | -34% | 29 ↓ | -29% | +16% |
| 4 | TTWO | Take-Two Interactive | Communication Services | 2019-02-22 | 32 | -38% | 55 | 74% | -5% | +45% | yes | 2.7 | +54% (5.9) | -3% (0.2) | -3% | 32 | +33% | +22% |
| 5 | AVAV | AeroVironment | Industrials | 2019-06-28 | 32 | -53% | 40 | 86% | +12% | – | yes | 6.3 | +39% (11.9) | -18% (8.5) | -13% | 26 ↓ | +36% | +4% |
| 6 | ENSG | Ensign Group | Health Care | 2019-10-04 | 32 | -33% | 32 | 71% | – | +41% | yes | 3.3 | +53% (11.0) | -37% (5.4) | -1% | 31 ↓ | +44% | +16% |
| 7 | SIGI | Selective Insurance Group | Financials | 2019-11-22 | 32 | -21% | 15 | 67% | +7% | +52% | **no** | – | +9% (2.8) | -36% (3.8) | -36% | 21 ↓ | -2% | +16% |
| 8 | CNC | Centene Corporation | Health Care | 2019-04-19 | 33 | -35% | 32 | 75% | +24% | -4% | yes | 7.0 | +51% (11.9) | -11% (5.5) | -11% | 34 | +48% | +1% |
| 9 | TRV | Travelers Companies (The) | Financials | 2019-10-25 | 33 | -16% | 15 | 62% | +5% | +35% | **no** | – | +9% (2.9) | -37% (4.8) | -37% | 21 ↓ | -1% | +17% |
| 10 | ERIE | Erie Indemnity | Financials | 2019-11-22 | 33 | -36% | 18 | – | +11% | – | yes | 7.9 | +46% (11.7) | -21% (3.6) | -21% | 21 ↓ | +42% | +16% |
| 11 | TSLA | Tesla, Inc. | Consumer Discretionary | 2019-05-17 | 33 | -46% | 99 | 32% | +81% | – | yes | 1.9 | +335% (9.1) | -15% (0.6) | -15% | 30 ↓ | +279% | +2% |
| 12 | FFIV | F5, Inc. | Information Technology | 2019-05-17 | 34 | -30% | 33 | 22% | +4% | +25% | **no** | – | +10% (2.3) | -35% (10.1) | -35% | 27 ↓ | -1% | +2% |
| 13 | CSX | CSX Corporation | Industrials | 2019-08-16 | 34 | -19% | 15 | 81% | +7% | -35% | yes | 5.5 | +24% (6.2) | -26% (7.2) | -1% | 22 ↓ | +16% | +19% |
| 14 | HUM | Humana | Health Care | 2019-04-19 | 34 | -32% | 29 | 89% | +6% | -28% | yes | 2.8 | +59% (9.9) | -10% (11.1) | -2% | 34 | +56% | +1% |
| 15 | ROL | Rollins, Inc. | Industrials | 2019-08-02 | 34 | -25% | 45 | 46% | +8% | +21% | yes | 6.2 | +61% (12.0) | -4% (0.8) | -4% | 31 ↓ | +61% | +14% |
| 16 | COHR | Coherent Corp. | Information Technology | 2019-11-22 | 34 | -49% | 104 | 29% | +18% | +21% | yes | 0.8 | +139% (12.0) | -22% (3.6) | +1% | 34 | +139% | +16% |


#### 2020: 20 buys, 19 hit +20%, SPY +18% that year, 12m median +49%, best +124%, worst +15%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NNN | NNN Reit | Real Estate | 2020-03-20 | 20 | -49% | 51 | 82% | +8% | -5% | yes | 2.5 | +62% (11.8) | -12% (0.5) | -12% | 23 | +50% | +73% |
| 2 | AZO | AutoZone | Consumer Discretionary | 2020-03-20 | 20 | -43% | 35 | 74% | +7% | +23% | yes | 0.2 | +82% (12.0) | -1% (0.1) | -1% | 31 | +82% | +73% |
| 3 | ESS | Essex Property Trust | Real Estate | 2020-03-20 | 21 | -41% | 25 | 56% | +4% | +17% | yes | 0.6 | +55% (11.8) | -7% (0.1) | -7% | 28 | +46% | +73% |
| 4 | WELL | Welltower | Real Estate | 2020-03-13 | 22 | -45% | 27 | 47% | +9% | +51% | yes | 2.8 | +51% (12.0) | -35% (0.2) | -35% | 19 ↓ | +51% | +49% |
| 5 | MOG-A | Moog Inc. | Industrials | 2020-03-13 | 22 | -48% | 126 | 37% | +8% | +37% | yes | 2.7 | +70% (12.0) | -32% (0.2) | -32% | 19 ↓ | +70% | +49% |
| 6 | WPC | W. P. Carey | Real Estate | 2020-03-20 | 23 | -47% | 39 | 79% | +39% | – | yes | 0.2 | +55% (11.2) | -11% (0.1) | -11% | 30 | +48% | +73% |
| 7 | FISV | Fiserv | Financials | 2020-03-20 | 23 | -35% | 6 | 96% | +33% | -39% | yes | 0.3 | +52% (11.7) | -6% (0.1) | -6% | 33 | +49% | +73% |
| 8 | LH | Labcorp | Health Care | 2020-03-20 | 24 | -45% | 5 | 62% | +2% | -3% | yes | 0.2 | +130% (11.2) | -3% (0.1) | -3% | 32 | +124% | +73% |
| 9 | SRE | Sempra | Utilities | 2020-03-13 | 24 | -34% | 6 | 95% | -8% | +113% | yes | 0.9 | +31% (8.0) | -17% (0.1) | -17% | 22 ↓ | +25% | +49% |
| 10 | O | Realty Income | Real Estate | 2020-03-20 | 24 | -44% | 20 | 86% | +11% | +8% | yes | 0.2 | +42% (5.9) | -9% (0.1) | -9% | 29 | +37% | +73% |
| 11 | GPN | Global Payments | Financials | 2020-03-20 | 24 | -43% | 4 | 98% | +46% | -24% | yes | 0.2 | +82% (11.8) | -2% (0.1) | -2% | 34 | +73% | +73% |
| 12 | AFL | Aflac | Financials | 2020-02-28 | 24 | -25% | 33 | 86% | -1% | -36% | **no** | – | +20% (11.9) | -41% (0.6) | -41% | 12 ↓ | +15% | +31% |
| 13 | CTAS | Cintas | Industrials | 2020-03-20 | 24 | -43% | 5 | 91% | +7% | +1% | yes | 1.2 | +113% (7.9) | -10% (0.1) | -10% | 25 | +93% | +73% |
| 14 | MRSH | Marsh McLennan | Financials | 2020-03-20 | 25 | -33% | 5 | 78% | +11% | +14% | yes | 0.7 | +52% (11.9) | -4% (0.1) | -4% | 29 | +49% | +73% |
| 15 | EME | Emcor | Industrials | 2020-03-13 | 25 | -33% | 36 | 43% | +13% | +19% | yes | 4.9 | +84% (12.0) | -23% (0.1) | -23% | 19 ↓ | +84% | +49% |
| 16 | ITW | Illinois Tool Works | Industrials | 2020-03-20 | 25 | -34% | 4 | 92% | -4% | +2% | yes | 0.6 | +81% (11.9) | -6% (0.1) | -6% | 37 | +78% | +73% |
| 17 | UDR | UDR, Inc. | Real Estate | 2020-03-20 | 26 | -38% | 28 | 66% | +10% | -15% | yes | 0.6 | +48% (11.8) | -6% (0.1) | -6% | 32 | +41% | +73% |
| 18 | LAMR | Lamar Advertising Company | Real Estate | 2020-03-13 | 26 | -32% | 4 | 57% | +8% | +20% | yes | 7.9 | +49% (12.0) | -51% (0.3) | -51% | 16 ↓ | +49% | +49% |
| 19 | COKE | Coca-Cola Consolidated | Consumer Staples | 2020-02-28 | 26 | -52% | 42 | 58% | +4% | -107% | yes | 1.3 | +45% (11.4) | -2% (0.7) | -2% | 30 | +31% | +31% |
| 20 | ETR | Entergy | Utilities | 2020-03-20 | 26 | -41% | 5 | 85% | -1% | +36% | yes | 0.2 | +45% (7.9) | -2% (0.1) | -2% | 34 | +28% | +73% |


#### 2021: 15 buys, 7 hit +20%, SPY +29% that year, 12m median -25%, best +21%, worst -62%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FDX | FedEx | Industrials | 2021-09-24 | 28 | -29% | 20 | 50% | +21% | +297% | **no** | – | +17% (3.4) | -33% (12.0) | -33% | 27 ↓ | -33% | -16% |
| 2 | AMT | American Tower | Real Estate | 2021-03-05 | 31 | -27% | 55 | 79% | +6% | -11% | yes | 0.8 | +53% (6.1) | -1% (0.1) | -1% | 33 | +21% | +14% |
| 3 | ENSG | Ensign Group | Health Care | 2021-10-08 | 31 | -27% | 28 | 68% | +11% | +37% | yes | 5.0 | +30% (5.7) | -4% (0.6) | -4% | 31 ↓ | +14% | -16% |
| 4 | XRAY | Dentsply Sirona | Health Care | 2021-11-19 | 31 | -24% | 27 | 72% | +18% | – | **no** | – | +12% (3.2) | -48% (11.5) | -48% | 26 ↓ | -40% | -14% |
| 5 | PTC | PTC Inc. | Information Technology | 2021-11-26 | 32 | -31% | 40 | 68% | +22% | +164% | yes | 11.5 | +25% (11.6) | -8% (5.0) | -8% | 34 | +18% | -11% |
| 6 | TMUS | T-Mobile US | Communication Services | 2021-10-08 | 32 | -19% | 12 | 84% | +53% | +10% | yes | 10.0 | +21% (10.5) | -16% (3.4) | -16% | 27 ↓ | +14% | -16% |
| 7 | XYZ | Block, Inc. | Financials | 2021-12-03 | 32 | -37% | 41 | 12% | +119% | +64% | **no** | – | +7% (0.2) | -72% (10.3) | -72% | 18 ↓ | -62% | -9% |
| 8 | CHTR | Charter Communications | Communication Services | 2021-12-10 | 32 | -26% | 14 | 49% | +8% | +74% | **no** | – | +8% (0.7) | -50% (9.7) | -50% | 22 ↓ | -38% | -15% |
| 9 | CMI | Cummins | Industrials | 2021-12-17 | 32 | -24% | 40 | 49% | +23% | +43% | yes | 10.8 | +22% (11.4) | -11% (6.2) | -11% | 32 | +15% | -15% |
| 10 | DIS | Walt Disney Company (The) | Communication Services | 2021-11-19 | 32 | -24% | 36 | 83% | -9% | – | **no** | – | +3% (1.7) | -44% (11.7) | -44% | 23 ↓ | -40% | -14% |
| 11 | VEEV | Veeva Systems | Health Care | 2021-12-03 | 33 | -27% | 58 | 71% | +30% | +27% | **no** | – | +9% (0.2) | -39% (10.3) | -39% | 25 ↓ | -30% | -9% |
| 12 | ALL | Allstate | Financials | 2021-11-12 | 33 | -18% | 24 | 58% | +13% | -6% | yes | 4.3 | +27% (5.2) | -6% (0.6) | -6% | 30 ↓ | +18% | -13% |
| 13 | CMCSA | Comcast | Communication Services | 2021-12-10 | 33 | -22% | 14 | 82% | +9% | +39% | **no** | – | +7% (1.1) | -39% (10.0) | -39% | 24 ↓ | -25% | -15% |
| 14 | GMED | Globus Medical | Health Care | 2021-11-26 | 33 | -24% | 17 | 89% | +24% | +94% | yes | 4.5 | +27% (4.8) | -17% (6.6) | -2% | 32 ↓ | +12% | -11% |
| 15 | SWKS | Skyworks Solutions | Information Technology | 2021-11-26 | 34 | -25% | 40 | 67% | +47% | +87% | **no** | – | +7% (0.5) | -47% (10.5) | -47% | 23 ↓ | -38% | -11% |


#### 2022: 20 buys, 12 hit +20%, SPY -18% that year, 12m median +8%, best +129%, worst -28%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | META | Meta Platforms | Communication Services | 2022-02-04 | 24 | -38% | 28 | 7% | +42% | +39% | **no** | – | -1% (1.9) | -62% (8.9) | -62% | 19 ↓ | -21% | -7% |
| 2 | NWS | News Corp (Class B) | Communication Services | 2022-05-06 | 26 | -35% | 49 | 56% | +15% | – | yes | 8.7 | +29% (8.9) | -9% (4.7) | -9% | 26 ↓ | +3% | +2% |
| 3 | NWSA | News Corp (Class A) | Communication Services | 2022-05-06 | 27 | -39% | 52 | 55% | +15% | – | yes | 8.7 | +26% (8.9) | -12% (4.7) | -12% | 25 ↓ | +1% | +2% |
| 4 | NFLX | Netflix | Communication Services | 2022-01-21 | 27 | -43% | 12 | 52% | +20% | +79% | **no** | – | +15% (0.4) | -58% (3.6) | -58% | 19 ↓ | -14% | -8% |
| 5 | BALL | Ball Corporation | Materials | 2022-05-06 | 29 | -30% | 78 | 69% | +17% | +51% | **no** | – | +3% (1.1) | -34% (5.3) | -34% | 27 ↓ | -17% | +2% |
| 6 | MMS | Maximus Inc. | Industrials | 2022-05-06 | 30 | -30% | 54 | 27% | +24% | +28% | yes | 9.2 | +27% (9.4) | -17% (5.2) | -17% | 23 ↓ | +21% | +2% |
| 7 | WMT | Walmart | Consumer Staples | 2022-05-20 | 30 | -26% | 89 | 93% | +2% | +3% | yes | 5.3 | +31% (11.7) | -1% (0.9) | -1% | 33 | +28% | +9% |
| 8 | DKS | Dick's Sporting Goods | Consumer Discretionary | 2022-05-20 | 30 | -47% | 37 | 19% | +28% | +142% | yes | 2.0 | +97% (11.1) | -8% (0.1) | -8% | 31 | +67% | +9% |
| 9 | BBY | Best Buy | Consumer Discretionary | 2022-05-20 | 30 | -49% | 26 | 43% | +10% | +44% | yes | 6.4 | +31% (8.5) | -11% (5.0) | -11% | 34 | +2% | +9% |
| 10 | CINF | Cincinnati Financial | Financials | 2022-07-29 | 30 | -32% | 15 | 51% | -13% | -33% | yes | 6.2 | +33% (6.4) | -7% (2.1) | -7% | 30 ↓ | +16% | +13% |
| 11 | AXON | Axon Enterprise | Industrials | 2022-05-06 | 30 | -55% | 64 | 69% | +27% | – | yes | 2.9 | +137% (11.4) | -12% (0.2) | -12% | 29 ↓ | +129% | +2% |
| 12 | FIVE | Five Below | Consumer Discretionary | 2022-05-20 | 30 | -51% | 65 | 23% | +45% | +125% | yes | 2.6 | +85% (10.7) | -4% (1.4) | -4% | 34 | +62% | +9% |
| 13 | ICE | Intercontinental Exchange | Financials | 2022-05-06 | 30 | -29% | 27 | 59% | +11% | +92% | **no** | – | +13% (3.4) | -9% (1.4) | -9% | 28 ↓ | +10% | +2% |
| 14 | FFIV | F5, Inc. | Information Technology | 2022-04-29 | 30 | -33% | 17 | 75% | +11% | +13% | **no** | – | +6% (0.2) | -22% (11.9) | -22% | 28 ↓ | -20% | +3% |
| 15 | APO | Apollo Global Management | Financials | 2022-04-22 | 30 | -33% | 25 | 0% | +153% | +1564% | yes | 6.6 | +40% (9.6) | -13% (1.8) | -13% | 26 ↓ | +21% | -2% |
| 16 | FAF | First American Financial Corporation | Financials | 2022-04-08 | 31 | -27% | 20 | 26% | +30% | +81% | **no** | – | +11% (9.9) | -24% (6.4) | -24% | 27 ↓ | -3% | -7% |
| 17 | TRU | TransUnion | Industrials | 2022-02-25 | 31 | -27% | 24 | 46% | +11% | +45% | **no** | – | +14% (1.1) | -44% (8.2) | -44% | 26 ↓ | -28% | -8% |
| 18 | RBA | RB Global | Industrials | 2022-02-18 | 31 | -35% | 67 | 69% | +9% | -3% | yes | 2.8 | +42% (5.5) | -2% (0.2) | -2% | 33 | +24% | -5% |
| 19 | ALLE | Allegion | Industrials | 2022-02-18 | 31 | -23% | 43 | 71% | +6% | +57% | **no** | – | +9% (11.5) | -21% (7.3) | -21% | 29 ↓ | +6% | -5% |
| 20 | APH | Amphenol | Information Technology | 2022-06-17 | 31 | -29% | 30 | 81% | +26% | +29% | yes | 1.3 | +32% (12.0) | +1% (0.2) | +1% | 35 | +32% | +22% |


#### 2023: 18 buys, 13 hit +20%, SPY +26% that year, 12m median +25%, best +43%, worst -22%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SJM | J.M. Smucker Company (The) | Consumer Staples | 2023-09-15 | 25 | -22% | 36 | 99% | +6% | -102% | **no** | – | +6% (4.6) | -15% (1.9) | -15% | 17 ↓ | -1% | +28% |
| 2 | MET | MetLife | Financials | 2023-03-17 | 28 | -29% | 96 | 78% | +5% | -63% | yes | 5.9 | +37% (11.9) | -10% (2.0) | -10% | 28 ↓ | +37% | +33% |
| 3 | HALO | Halozyme | Health Care | 2023-03-17 | 29 | -44% | 15 | 41% | +49% | -47% | yes | 4.0 | +33% (4.8) | -8% (1.7) | -8% | 31 | +24% | +33% |
| 4 | CFR | Frost Bank | Financials | 2023-03-17 | 29 | -35% | 71 | 37% | +24% | +33% | **no** | – | +13% (11.6) | -19% (7.3) | -19% | 27 ↓ | +5% | +33% |
| 5 | PEP | PepsiCo | Consumer Staples | 2023-10-06 | 29 | -19% | 21 | 85% | +10% | -14% | **no** | – | +16% (7.3) | -1% (0.2) | -1% | 29 ↓ | +8% | +35% |
| 6 | LSCC | Lattice Semiconductor | Information Technology | 2023-11-03 | 30 | -41% | 32 | 56% | +19% | +60% | yes | 1.3 | +45% (4.1) | -28% (10.1) | -6% | 29 ↓ | -9% | +33% |
| 7 | RJF | Raymond James Financial | Financials | 2023-03-17 | 31 | -30% | 61 | 70% | +7% | -1% | yes | 3.8 | +40% (11.6) | -5% (1.6) | -5% | 32 | +40% | +33% |
| 8 | OMC | Omnicom Group | Communication Services | 2023-09-22 | 31 | -26% | 32 | 33% | +1% | +11% | yes | 3.5 | +44% (11.9) | -2% (0.4) | -2% | 32 | +43% | +34% |
| 9 | ON | ON Semiconductor | Information Technology | 2023-11-03 | 31 | -39% | 14 | 36% | +3% | +29% | yes | 1.3 | +26% (1.3) | -11% (5.6) | -6% | 30 ↓ | +4% | +33% |
| 10 | KBR | KBR, Inc. | Industrials | 2023-11-03 | 31 | -23% | 20 | 78% | -13% | – | yes | 4.0 | +41% (11.6) | -2% (0.1) | -2% | 36 | +34% | +33% |
| 11 | PEN | Penumbra, Inc. | Health Care | 2023-10-13 | 31 | -44% | 15 | 21% | +16% | – | yes | 2.0 | +39% (4.1) | -17% (9.8) | -8% | 31 ↓ | +3% | +36% |
| 12 | WTFC | Wintrust Financial | Financials | 2023-03-17 | 32 | -32% | 61 | 47% | +5% | +6% | yes | 8.0 | +41% (11.6) | -15% (1.8) | -15% | 25 ↓ | +37% | +33% |
| 13 | TMO | Thermo Fisher Scientific | Health Care | 2023-10-20 | 32 | -31% | 94 | 81% | +2% | -22% | yes | 3.3 | +35% (10.7) | -7% (0.2) | -7% | 27 ↓ | +30% | +41% |
| 14 | CBSH | Commerce Bancshares | Financials | 2023-03-17 | 32 | -27% | 104 | 75% | – | -11% | **no** | – | +4% (0.1) | -24% (7.5) | -24% | 24 ↓ | -6% | +33% |
| 15 | RMD | ResMed| | Health Care | 2023-08-04 | 32 | -41% | 99 | 74% | +13% | +11% | yes | 8.7 | +26% (12.0) | -25% (2.8) | -25% | 21 ↓ | +26% | +21% |
| 16 | VC | Visteon | Consumer Discretionary | 2023-10-27 | 32 | -30% | 145 | 61% | +31% | +61% | **no** | – | +9% (1.6) | -27% (11.9) | -27% | 29 ↓ | -22% | +43% |
| 17 | BYD | Boyd Gaming | Consumer Discretionary | 2023-10-27 | 32 | -25% | 130 | 29% | – | +39% | yes | 3.4 | +29% (12.0) | -7% (7.0) | +0% | 33 | +29% | +43% |
| 18 | DHR | Danaher Corporation | Health Care | 2023-10-27 | 32 | -37% | 111 | 75% | -1% | +0% | yes | 1.5 | +50% (9.2) | -1% (0.1) | -1% | 39 | +31% | +43% |


#### 2024: 18 buys, 11 hit +20%, SPY +25% that year, 12m median +8%, best +99%, worst -29%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HII | Huntington Ingalls Industries | Industrials | 2024-11-01 | 26 | -37% | 34 | 38% | +6% | +36% | yes | 5.7 | +75% (12.0) | -15% (3.2) | -15% | 27 | +75% | +21% |
| 2 | APD | Air Products | Materials | 2024-02-09 | 26 | -33% | 60 | 60% | -1% | +2% | yes | 3.2 | +58% (11.8) | -1% (0.2) | -1% | 31 | +45% | +21% |
| 3 | REGN | Regeneron Pharmaceuticals | Health Care | 2024-11-01 | 29 | -30% | 9 | 42% | +6% | -0% | **no** | – | -2% (0.1) | -43% (7.1) | -43% | 23 ↓ | -22% | +21% |
| 4 | CHRD | Chord Energy | Energy | 2024-09-06 | 30 | -29% | 135 | 26% | +5% | -48% | **no** | – | +3% (1.0) | -37% (7.0) | -37% | 29 ↓ | -19% | +21% |
| 5 | ELV | Elevance Health | Health Care | 2024-10-18 | 30 | -24% | 132 | 73% | +4% | +6% | **no** | – | +6% (5.5) | -35% (9.4) | -35% | 21 ↓ | -18% | +15% |
| 6 | LULU | Lululemon Athletica | Consumer Discretionary | 2024-04-05 | 31 | -31% | 14 | 25% | +19% | +83% | **no** | – | +18% (9.9) | -35% (4.0) | -35% | 21 ↓ | -26% | -1% |
| 7 | MPWR | Monolithic Power Systems | Information Technology | 2024-11-15 | 31 | -40% | 11 | 86% | +3% | -10% | yes | 2.2 | +94% (11.4) | -20% (4.7) | -2% | 31 | +62% | +16% |
| 8 | HUM | Humana | Health Care | 2024-01-19 | 32 | -30% | 63 | 55% | +12% | +10% | **no** | – | +2% (0.1) | -41% (10.9) | -41% | 24 ↓ | -29% | +25% |
| 9 | WMS | Advanced Drainage Systems | Industrials | 2024-12-20 | 32 | -38% | 39 | 49% | +3% | +6% | yes | 7.8 | +34% (11.2) | -16% (3.6) | -16% | 31 ↓ | +30% | +16% |
| 10 | CI | Cigna | Health Care | 2024-12-13 | 32 | -24% | 37 | 27% | +22% | -40% | yes | 3.6 | +21% (4.5) | -12% (10.6) | -6% | 28 ↓ | -1% | +14% |
| 11 | BRKR | Bruker | Health Care | 2024-11-15 | 32 | -46% | 34 | 70% | +15% | +11% | yes | 1.9 | +23% (1.9) | -43% (9.6) | -6% | 24 ↓ | -18% | +16% |
| 12 | QLYS | Qualys | Information Technology | 2024-05-31 | 32 | -32% | 23 | 16% | +12% | +50% | **no** | – | +13% (5.2) | -18% (10.2) | -18% | 29 ↓ | -1% | +13% |
| 13 | CDW | CDW Corporation | Information Technology | 2024-11-01 | 33 | -28% | 30 | 67% | -4% | +4% | **no** | – | +10% (3.2) | -23% (5.1) | -23% | 25 ↓ | -14% | +21% |
| 14 | SMCI | Supermicro | Information Technology | 2024-11-01 | 33 | -79% | 34 | 69% | +110% | +68% | yes | 0.7 | +133% (8.9) | -31% (0.4) | -31% | 30 ↓ | +99% | +21% |
| 15 | WDAY | Workday, Inc. | Information Technology | 2024-05-31 | 33 | -32% | 14 | 2% | +17% | – | yes | 2.8 | +32% (6.3) | -2% (0.4) | -2% | 33 | +17% | +13% |
| 16 | VLO | Valero Energy | Energy | 2024-12-20 | 33 | -36% | 37 | 63% | -11% | -61% | yes | 1.5 | +60% (10.9) | -11% (3.4) | +0% | 30 ↓ | +42% | +16% |
| 17 | AMGN | Amgen | Health Care | 2024-12-20 | 33 | -24% | 46 | 76% | +21% | -44% | yes | 2.2 | +35% (11.3) | -2% (0.6) | -2% | 32 ↓ | +28% | +16% |
| 18 | MPC | Marathon Petroleum | Energy | 2024-11-01 | 33 | -35% | 30 | 44% | -6% | -28% | yes | 7.5 | +42% (10.8) | -16% (5.2) | -16% | 32 ↓ | +39% | +21% |


#### 2025: 20 buys, 14 hit +20%, SPY +18% that year, 12m median +17%, best +102%, worst -32%

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FCN | FTI Consulting | Industrials | 2025-02-21 | 25 | -32% | 97 | 61% | +12% | +29% | **no** | – | +11% (11.1) | -8% (7.8) | -8% | 26 | -2% | +16% |
| 2 | DOV | Dover Corporation | Industrials | 2025-04-04 | 26 | -31% | 44 | 88% | -8% | +159% | yes | 1.3 | +53% (10.6) | -2% (0.1) | -2% | 33 | +35% | +31% |
| 3 | ADP | Automatic Data Processing | Industrials | 2025-10-31 | 27 | -21% | 48 | 55% | +7% | +11% | open | – | +13% (9.9) | -26% (5.3) | -26% | 22 ↓ | +4% (so far) | +14% (so far) |
| 4 | WM | Waste Management | Industrials | 2025-10-31 | 27 | -18% | 83 | 74% | +16% | -3% | yes | 3.9 | +24% (4.2) | -2% (0.1) | -2% | 30 | +5% (so far) | +14% (so far) |
| 5 | ITT | ITT Inc. | Industrials | 2025-04-04 | 27 | -30% | 53 | 80% | +11% | +27% | yes | 0.7 | +86% (10.7) | -0% (0.1) | -0% | 40 | +73% | +31% |
| 6 | EIX | Edison International | Utilities | 2025-01-10 | 27 | -27% | 18 | 64% | +4% | +7% | **no** | – | -0% (12.0) | -25% (5.1) | -25% | 18 ↓ | -0% | +21% |
| 7 | ARES | Ares Management | Financials | 2025-04-04 | 27 | -41% | 9 | 91% | +7% | – | yes | 0.2 | +64% (4.3) | -17% (11.2) | +4% | 27 ↓ | -10% | +31% |
| 8 | GDDY | GoDaddy | Information Technology | 2025-08-08 | 27 | -38% | 27 | 34% | +8% | – | **no** | – | +12% (1.1) | -44% (10.4) | -44% | 16 ↓ | -32% | +23% |
| 9 | GMED | Globus Medical | Health Care | 2025-05-09 | 28 | -41% | 14 | 52% | +61% | -30% | yes | 6.0 | +73% (11.4) | -7% (2.4) | -7% | 29 | +40% | +32% |
| 10 | AJG | Arthur J. Gallagher & Co. | Financials | 2025-10-31 | 28 | -29% | 35 | 68% | +14% | +26% | open | – | +10% (9.8) | -23% (6.4) | -23% | 26 ↓ | -6% (so far) | +14% (so far) |
| 11 | BRO | Brown & Brown | Financials | 2025-08-01 | 28 | -27% | 18 | 68% | +12% | +0% | **no** | – | +5% (0.9) | -41% (9.4) | -41% | 24 ↓ | -23% | +21% |
| 12 | CXT | Crane NXT | Information Technology | 2025-04-04 | 28 | -33% | 86 | 63% | +7% | -3% | yes | 1.2 | +54% (6.1) | -11% (11.8) | -6% | 28 | -10% | +31% |
| 13 | QCOM | Qualcomm | Information Technology | 2025-04-04 | 28 | -45% | 41 | 37% | +12% | +35% | yes | 1.3 | +49% (6.8) | -2% (0.1) | -2% | 31 | +2% | +31% |
| 14 | CMI | Cummins | Industrials | 2025-04-04 | 28 | -28% | 16 | 58% | +0% | +451% | yes | 1.3 | +121% (10.1) | -4% (0.1) | -4% | 31 | +102% | +31% |
| 15 | SYF | Synchrony Financial | Financials | 2025-04-04 | 28 | -38% | 10 | 57% | – | +65% | yes | 0.9 | +105% (9.1) | +0% (0.1) | +0% | 33 | +59% | +31% |
| 16 | BDC | Belden Inc. | Information Technology | 2025-04-04 | 29 | -32% | 21 | 55% | -2% | -15% | yes | 1.1 | +70% (10.3) | -2% (0.1) | -2% | 35 | +29% | +31% |
| 17 | J | Jacobs Solutions | Industrials | 2025-04-04 | 29 | -26% | 21 | 84% | -30% | +35% | yes | 2.9 | +50% (6.6) | -1% (0.1) | -1% | 37 | +17% | +31% |
| 18 | DCI | Donaldson Company | Industrials | 2025-04-04 | 29 | -23% | 47 | 25% | +4% | +12% | yes | 4.3 | +84% (10.3) | -3% (0.1) | -3% | 35 | +42% | +31% |
| 19 | EMR | Emerson Electric | Industrials | 2025-04-04 | 29 | -30% | 18 | 92% | +10% | -78% | yes | 1.2 | +73% (10.2) | -0% (0.1) | -0% | 35 | +42% | +31% |
| 20 | MAS | Masco | Industrials | 2025-04-04 | 29 | -27% | 53 | 60% | -2% | -6% | yes | 4.6 | +25% (10.2) | -7% (0.1) | -7% | 26 ↓ | -4% | +31% |


#### 2026: 19 buys, 9 hit +20%, SPY +14% that year

| # | Ticker | Name | Sector | Signal week | RSI(w) | vs ATH | Weeks from ATH | Val pct | Rev y/y | EPS y/y | Hit target? | Months to hit | Max gain (month) | Max DD (month) | DD before hit | RSI(w) low after | 12m return | SPY same 12m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | EXLS | EXL Service | Industrials | 2026-02-06 | 26 | -40% | 52 | 50% | +14% | +30% | yes | 6.6 | +21% (6.7) | -20% (4.6) | -20% | 24 ↓ | +10% (so far) | +13% (so far) |
| 2 | COR | Cencora | Health Care | 2026-05-08 | 27 | -31% | 23 | 86% | +7% | +18% | yes | 2.7 | +30% (3.9) | -2% (0.2) | -2% | 27 ↓ | +18% (so far) | +5% (so far) |
| 3 | NWS | News Corp (Class B) | Communication Services | 2026-02-06 | 28 | -28% | 52 | – | – | +232% | yes | 2.5 | +38% (6.6) | +0% (0.2) | +0% | 31 | +25% (so far) | +13% (so far) |
| 4 | GWRE | Guidewire Software | Information Technology | 2026-01-16 | 29 | -42% | 32 | 61% | +23% | +186% | yes | 7.2 | +29% (7.4) | -35% (5.2) | -35% | 23 ↓ | -8% (so far) | +12% (so far) |
| 5 | EQH | Equitable Holdings | Financials | 2026-02-27 | 29 | -29% | 54 | 33% | +9% | – | yes | 4.5 | +37% (6.6) | -12% (0.9) | -12% | 23 ↓ | +37% (so far) | +13% (so far) |
| 6 | PLNT | Planet Fitness | Consumer Discretionary | 2026-02-27 | 30 | -28% | 56 | 24% | +14% | – | open | – | +1% (0.1) | -50% (6.9) | -50% | 15 ↓ | -48% (so far) | +13% (so far) |
| 7 | ROL | Rollins, Inc. | Industrials | 2026-05-29 | 30 | -28% | 51 | 49% | +11% | +10% | open | – | +0% (0.4) | -37% (3.9) | -37% | 16 ↓ | -37% (so far) | +2% (so far) |
| 8 | CME | CME Group | Financials | 2026-06-26 | 31 | -33% | 17 | 70% | +8% | +18% | yes | 1.1 | +30% (2.2) | -1% (0.1) | -1% | 37 | +20% (so far) | +6% (so far) |
| 9 | SYK | Stryker Corporation | Health Care | 2026-05-01 | 31 | -27% | 111 | 53% | +11% | +8% | open | – | +20% (2.9) | -8% (4.8) | -8% | 29 ↓ | -7% (so far) | +8% (so far) |
| 10 | MCD | McDonald's | Consumer Discretionary | 2026-05-08 | 31 | -19% | 10 | 66% | +4% | +5% | open | – | +5% (1.3) | -13% (4.6) | -13% | 25 ↓ | -13% (so far) | +5% (so far) |
| 11 | RBA | RB Global | Industrials | 2026-08-14 | 31 | -30% | 47 | 74% | +9% | +6% | open | – | +4% (0.2) | -4% (0.9) | -4% | 31 | -2% (so far) | -0% (so far) |
| 12 | BSX | Boston Scientific | Health Care | 2026-02-06 | 31 | -30% | 52 | 56% | +22% | +55% | open | – | +1% (0.7) | -44% (5.2) | -44% | 22 ↓ | -42% (so far) | +13% (so far) |
| 13 | TTWO | Take-Two Interactive | Communication Services | 2026-02-06 | 32 | -26% | 18 | 86% | +14% | – | yes | 3.2 | +32% (4.9) | -3% (1.6) | -3% | 31 ↓ | +3% (so far) | +13% (so far) |
| 14 | ENSG | Ensign Group | Health Care | 2026-06-12 | 32 | -31% | 17 | 76% | +19% | +16% | yes | 1.5 | +23% (1.9) | +1% (0.1) | +1% | 35 | +17% (so far) | +5% (so far) |
| 15 | APPF | AppFolio | Information Technology | 2026-01-30 | 32 | -42% | 26 | 15% | +19% | +54% | yes | 6.9 | +23% (6.9) | -25% (2.3) | -25% | 27 ↓ | +8% (so far) | +12% (so far) |
| 16 | SPXC | SPX Technologies | Industrials | 2026-09-25 | 32 | -31% | 47 | 75% | +21% | +25% | open | – | – (–) | – (–) | – | – ↓ | – (so far) | – (so far) |
| 17 | CG | Carlyle Group (The) | Financials | 2026-03-13 | 32 | -35% | 25 | 83% | -12% | -21% | open | – | +15% (1.1) | -12% (6.4) | -12% | 34 | -11% (so far) | +17% (so far) |
| 18 | HCA | HCA Healthcare | Health Care | 2026-05-22 | 32 | -29% | 10 | 75% | +7% | +32% | open | – | +12% (4.0) | -8% (0.6) | -8% | 29 ↓ | +11% (so far) | +4% (so far) |
| 19 | MTZ | MasTec | Industrials | 2026-09-18 | 32 | -51% | 19 | 87% | +23% | +87% | open | – | +4% (0.1) | -1% (0.2) | -1% | 32 ↓ | -1% (so far) | +1% (so far) |
