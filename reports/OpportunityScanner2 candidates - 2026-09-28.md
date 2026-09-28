# OpportunityScanner2 candidates on September 28, 2026

*Research tooling output, not investment advice. Scanner and study: `OpportunityScanner2/` (see its README for the full results). Prices: Yahoo through the Friday, September 25 close. Tiers use the last completed monthly candle (August 2026); the "Sep, prov." column treats the September 25 close as if September had ended (three trading days left, so it can still change). Fundamentals: SEC EDGAR point-in-time tables (latest quarter up to August 31, 2026). Row-level data: `OpportunityScanner2/output/live_2026-09-28.csv` / `.json`.*

## The rule and what the study found

Arming: a monthly candle makes a **new all-time high with monthly RSI(14) ≥ 70** (≥ 5 years of history, $5M+ daily dollar volume).

| Tier | Trigger | Since 2009: 12m median / beat SPY / beat own-stock average | With the quality filter |
|---|---|---|---|
| **A ★** | former leader (armed in the last 36 months), monthly RSI < 35 | +43% / 65% / 80% (276 signals) | +49% / 70% / 89% (46) |
| **A** | ... monthly RSI < 40 | +29% / 55% / 65% (562) | +34% / 57% / 64% (149) |
| **B** | RSI ≤ 68% of the 24-month peak (the −32% rule) **and** price ≥ 40% below ATH | +28% / 55% / 58% (513) | +29% / 54% / 56% (190); with cheap too: +33% / 55% / 60% (152) |
| **C** | RSI ≤ 68% of the 24-month peak (the −32% rule alone) | +17% / 51% / 47% (1,486) | +17% / 52% / 46% (560) |

Tier C, the −32% rule as first stated, has done no better than buying the same stock in a random month. It fires early: the median stock fell another 14.5% afterwards. The rule is worth acting on once the damage is deeper (tier B), or when the former leader's RSI reaches the old oversold zone (tier A). **Quality** means profitable in the latest year and in two of the three before it, revenue growth ≥ 5%, EPS growing, no one-off gain in earnings and no acquisition-driven growth. **Cheap** means operating multiples (P/S, EV/EBITDA, EV/EBIT) sit in the bottom half of the company's own history ("Val. pct", 0 = cheapest ever).

Hindsight check: signals whose revenue kept growing ≥ 10% over the next year beat the universe by ~6 points; those whose revenue shrank lagged by ~16. The filters raise the share that kept growing from 77% to 85%. Each name below still needs its forward story (guidance, estimates, what broke the chart) checked by hand.

## 1. Tier A/B, quality and cheap: the buy-zone list

| Ticker | Name | Tier (Aug) | Tier (Sep, prov.) | RSI Aug / Sep | Peak RSI (month) | vs ATH | Rev TTM y/y | EPS TTM y/y | Val. pct | Fwd EPS (Yahoo) |
|---|---|---|---|---|---|---|---|---|---|---|
| **BSX** | Boston Scientific | A+B ★ | A+B ★ | 29.9 / 28.0 | 87 (2025-02) | -56% | +14% | +47% | 0.21 | +38% |
| **TTD** | Trade Desk (The) | A+B ★ | A+B ★ | 30.9 / 30.6 | 72 (2024-11) | -90% | +12% | +1% | 0.05 | +20% |
| **ROL** | Rollins, Inc. | A+B ★ | A+B ★ | 32.5 / 28.2 | 70 (2026-01) | -45% | +10% | +9% | 0.09 | +18% |
| **OLLI** | Ollie's Bargain Outlet | A+B | B | 37.5 / 43.6 | 71 (2025-07) | -47% | +14% | +30% | 0.10 | +10% |
| **INTU** | Intuit | A+B | A+B ★ | 37.5 / 33.0 | 72 (2025-06) | -56% | +14% | +20% | 0.11 | +64% |
| **GDDY** | GoDaddy | B | B | 40.4 / 40.1 | 86 (2025-01) | -55% | +7% | +20% | 0.07 | +64% |
| **TYL** | Tyler Technologies | B | A+B | 41.3 / 36.4 | 78 (2024-11) | -44% | +8% | +9% | 0.18 | +104% |
| **DECK** | Deckers Brands | B | A+B | 41.9 / 39.6 | 77 (2024-12) | -61% | +8% | +8% | 0.21 | +18% |
| **FICO** | Fair Isaac | B | A+B | 42.9 / 36.6 | 91 (2024-11) | -52% | +24% | +35% | 0.45 | +53% |
| **SFM** | Sprouts Farmers Market | B | A+B | 44.2 / 37.2 | 97 (2024-11) | -55% | +7% | +8% | 0.26 | +14% |

BSX, INTU and OLLI are also in the turnaround v3 (`both_opval`) top 10 from this morning. Two scanners built on different logic agree on them. INTU moves to A ★ if September closes near here.

TTD is 90% below its ATH: the filings still show growth, but a fall that deep needs its own diagnosis before it counts as a "reset".

## 2. Tier A/B, quality but still expensive vs own history

| Ticker | Name | Tier (Aug) | Tier (Sep, prov.) | RSI Aug / Sep | Peak RSI (month) | vs ATH | Rev TTM y/y | EPS TTM y/y | Val. pct | Fwd EPS (Yahoo) |
|---|---|---|---|---|---|---|---|---|---|---|
| **NRG** | NRG Energy | B | B | 45.4 / 42.9 | 83 (2025-07) | -42% | +12% | +66% | 0.61 | +286% |
| **ORCL** | Oracle Corporation | B | B | 47.3 / 45.7 | 77 (2024-11) | -57% | +22% | +48% | 0.69 | +72% |
| **DY** | Dycom Industries | B | B | 49.5 / 47.8 | 79 (2026-02) | -49% | +38% | +23% | 0.80 | +89% |
| **AMKR** | Amkor Technology | B | B | 53.4 / 56.4 | 85 (2026-06) | -51% | +13% | +43% | 0.97 | +26% |
| **KLAC** | KLA Corporation | B | C | 58.1 / 59.8 | 93 (2026-06) | -43% | +12% | +21% | 0.98 | +83% |
| **TTMI** | TTM Technologies | B | – | 61.0 / 63.1 | 93 (2026-06) | -47% | +28% | +149% | 0.94 | +210% |

These fell hard from blow-off tops (KLAC, TTMI, AMKR: RSI 85–93 in June 2026, then a 40–50% slide in July–August). The businesses still grow, but their multiples remain near the top of their own history. That is the profile the study rates weakest within tier B, so these are watchlist names.

## 3. Moving into A/B on the provisional September candle (quality names)

| Ticker | Name | Tier (Aug) | Tier (Sep, prov.) | RSI Aug / Sep | Peak RSI (month) | vs ATH | Rev TTM y/y | EPS TTM y/y | Val. pct | Fwd EPS (Yahoo) |
|---|---|---|---|---|---|---|---|---|---|---|
| **SYK** | Stryker Corporation | C | A | 45.3 / 35.8 | 70 (2024-11) | -20% | +8% | +28% | 0.35 | +73% |
| **NFLX** | Netflix | C | B | 46.9 / 42.3 | 85 (2025-06) | -40% | +16% | +35% | 0.30 | +20% |
| **NOW** | ServiceNow | C | B | 51.2 / 48.3 | 80 (2024-12) | -38% | +22% | +1% | 0.15 | +213% |
| **PEG** | Public Service Enterprise Group | C | A | 43.4 / 37.8 | 77 (2024-11) | -23% | +13% | +2% | 0.62 | +16% |
| **BWXT** | BWX Technologies | C | B | 49.0 / 45.3 | 84 (2025-10) | -37% | +23% | +20% | 0.84 | +36% |
| **HII** | Huntington Ingalls Industries | C | B | 49.6 / 46.3 | 77 (2026-02) | -37% | +14% | +26% | 0.62 | +24% |
| **TPL** | Texas Pacific Land Corporation | C | B | 51.5 / 48.5 | 86 (2024-11) | -37% | +21% | +17% | 0.57 | +832% |
| **BX** | Blackstone Inc. | – | B | 52.8 / 44.6 | 76 (2024-11) | -29% | +17% | +21% | 0.62 | +67% |

Recheck these after the September 30 close. SYK and PEG would qualify for tier A with only a 20–23% price drop, because their prior peaks were mild (RSI 70–77).

## 4. Tier A/B names that fail the quality filter

| Ticker | Tier (Aug) | vs ATH | Why not quality |
|---|---|---|---|
| GPK | A ★ | -64% | revenue +0%; EPS -63% |
| FISV | A+B ★ | -78% | revenue -1%; EPS -13% |
| PNR | A+B ★ | -47% | revenue +3% |
| DKS | A+B ★ | -47% | growth 54% vs 3% a year earlier; EPS -35% |
| ACM | A+B ★ | -50% | revenue -4%; EPS -52% |
| WING | A+B | -75% | EPS -30% |
| TSCO | A | -45% | revenue +4%; EPS -5% |
| POST | A | -34% | EPS -6% |
| LEN | A | -55% | revenue -7%; EPS -47% |
| CPRT | A+B | -49% | revenue +1% |
| BAH | A+B | -60% | revenue -7%; EPS -22% |
| IT | A+B | -66% | revenue +1%; EPS -31% |
| BLDR | A | -69% | revenue -9%; EPS -86% |
| LII | B | -44% | revenue -2%; EPS -4% |
| PSN | B | -58% | revenue -7%; EPS growth n/a |
| ERIE | B | -53% | revenue +4%; EPS growth n/a |
| PPC | B | -45% | revenue +1%; EPS -56% |
| AVAV | B | -64% | shares +78% y/y; EPS -362%; loss years |
| BRO | B | -43% | shares +33% y/y; EPS -10% |
| HLNE | B | -47% | EPS growth n/a |
| HIMS | B | -59% | EPS -181% |
| WSO | B | -46% | revenue -3%; EPS -11% |
| AAON | B | -50% | growth 54% vs 5% a year earlier |
| KBH | B | -41% | revenue -18%; EPS -45% |
| ALGM | B | -49% | EPS growth n/a |
| MTZ | B | -46% | growth 23% vs 7% a year earlier |
| FN | B | -45% | net income 1.02x operating income |
| VICR | B | -51% | net income 1.38x operating income |
| STRL | B | -53% | growth 61% vs 3% a year earlier |
| MKSI | B | -43% | growth 16% vs 4% a year earlier |
| ECHO | B | -41% | revenue -5%; EPS growth n/a |
| GLW | B | -45% | TTM net income jumped 1.67x in one quarter |

Most of these are shrinking or losing earnings: the hindsight split says those are the losing signals. Seven others fail only on the data checks:

- **AAON, STRL, MTZ, MKSI**: growth that jumped against the year before, the pattern of an acquisition. Check it before trusting the growth.
- **FN, VICR, GLW**: one-off gains in net income.

105 other names are in tier C only (the −32% rule without deeper damage) and are left out here. They are in the CSV.

## Notes on the columns

* *Fwd EPS (Yahoo)* is analyst next-year EPS (usually adjusted, non-GAAP) over trailing GAAP EPS. It runs high and is sometimes nonsense (TPL +832%); use it only as a direction check.
* *Peak RSI (month)* is the highest monthly RSI on an all-time-high candle in the last 24 months (36 for tier A).
* Survivorship: the study universe is today's index members. Blow-off-top stocks that later collapsed out of the index are missing, which flatters the history of every tier, and the deeper tiers most.
