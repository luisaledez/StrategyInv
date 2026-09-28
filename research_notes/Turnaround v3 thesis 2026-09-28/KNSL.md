# KNSL (Kinsale Capital Group) — working notes for the turnaround v3 thesis, 2026-09-28

*Research tooling, not investment advice. Companion to `turnaround_backtest_v3/thesis/KNSL.md`. Every fact carries its source. "Derived" = computed here from the cited figures or the local caches. Third-party estimates are labelled as such.*

Local caches used: `turnaround/cache/edgar/KNSL.json` (point-in-time SEC TTM data, fetched 2026-09-27), `turnaround/cache/prices/KNSL.csv` (Yahoo daily, through 2026-09-25), `turnaround/cache/valuation/KNSL.json`, `turnaround/cache/fundamentals/KNSL.json`.

## 1. Primary sources (SEC)

| Document | URL |
|---|---|
| Q2 2026 earnings release (8-K, 2026-07-23) | https://www.sec.gov/Archives/edgar/data/1669162/000166916226000039/earningsrelease2q2026.htm |
| Q2 2026 10-Q (filed 2026-07-23) | https://www.sec.gov/Archives/edgar/data/1669162/000166916226000040/knsl-20260630.htm |
| Q1 2026 release (2026-04-23) | https://www.sec.gov/Archives/edgar/data/1669162/000166916226000025/earningsrelease1q2026.htm |
| Q4 2025 release (2026-02-12) | https://www.sec.gov/Archives/edgar/data/1669162/000166916226000012/earningsrelease4q2025.htm |
| Q3 2025 release (2025-10-23) | https://www.sec.gov/Archives/edgar/data/1669162/000166916225000056/earningsrelease3q2025.htm |
| Q2 2025 release (2025-07-24) | https://www.sec.gov/Archives/edgar/data/1669162/000166916225000042/earningsrelease2q2025.htm |
| Q1 2025 release (2025-04-24) | https://www.sec.gov/Archives/edgar/data/1669162/000166916225000026/earningsrelease1q2025.htm |
| Q4 2024 release (2025-02-13) | https://www.sec.gov/Archives/edgar/data/1669162/000166916225000006/earningsrelease4q2024.htm |
| Q3 2024 release (2024-10-24) | https://www.sec.gov/Archives/edgar/data/1669162/000166916224000040/earningsrelease3q2024.htm |
| Q2 2024 release (2024-07-25) | https://www.sec.gov/Archives/edgar/data/1669162/000166916224000027/earningsrelease2q2024.htm |
| Q1 2024 release (2024-04-25) | https://www.sec.gov/Archives/edgar/data/1669162/000166916224000019/earningsrelease1q2024.htm |
| Q4 2023 release (2024-02-15) | https://www.sec.gov/Archives/edgar/data/1669162/000166916224000004/earningsrelease4q2023.htm |
| Q4 2022 release (2023-02-16) | https://www.sec.gov/Archives/edgar/data/1669162/000166916223000007/earningsrelease4q2022.htm |
| Q4 2021 release | https://www.sec.gov/Archives/edgar/data/1669162/000166916222000005/earningsrelease4q2021.htm |
| Q4 2020 release (search snippet only, 2020 combined ratio 86.7%) | https://www.sec.gov/Archives/edgar/data/1669162/000166916221000002/earningsrelease4q2020.htm |
| Q4 2019 release (search snippet only, 2019 combined ratio 84.7%, operating ROE 15.9%) | https://www.sec.gov/Archives/edgar/data/1669162/000166916220000003/earningsrelease4q2019.htm |
| 8-K index (dates of releases and 5.02 events) | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1669162&type=8-K |
| CIO retirement / analytics-technology realignment (8-K 2026-04-29) | https://www.sec.gov/Archives/edgar/data/1669162/000166916226000029/pressreleasedatedapril2920.htm |
| President/COO Haney board election and 2026-03-02 retirement (8-K 2025-10-23) | https://www.sec.gov/Archives/edgar/data/1669162/000166916225000057/pressreleaseoctober232025.htm |

## 2. Quarterly table (all from the SEC releases above; stock reaction from the local price cache)

GWP = gross written premiums. CP = Commercial Property Division. PYD = favourable prior-year reserve development (points of net earned premium). Op EPS = diluted net operating EPS (excludes equity fair-value changes and realized gains, after tax). Reaction = close of the day after the after-market release vs the release-day close.

| Quarter | GWP $M | GWP y/y | CP y/y | Ex-CP y/y | NEP $M | NII $M | Combined ratio | Cat pts | PYD pts | GAAP EPS | Op EPS | Op EPS y/y | BVPS (end) | Reaction next day |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q4 2023 | 395.2 | +33.8% | n/d | n/d | 296.8 | 30.4 | 72.1% | 0.1 | 2.3 | 4.43 | 3.87 | n/d | 46.88 | +15.4% (2024-02-16) |
| Q1 2024 | 448.6 | +25.5% | n/d | n/d | 309.5 | 32.9 | 79.5% | 0.2 | 2.7 | 4.24 | 3.50 | +43.4% | 50.31 | **-17.3%** (2024-04-26) |
| Q2 2024 | 529.8 | +20.9% | n/d | n/d | 332.5 | 35.8 | 77.7% | 1.0 | 2.8 | 3.97 | 3.75 | +30.2% | 53.99 | +17.5% (2024-07-26) |
| Q3 2024 | 448.6 | +18.8% | n/d | n/d | 348.8 | 39.6 | 75.7% | 3.8 | 2.8 | 4.90 | 4.20 | +26.9% | 61.62 | -5.3% (2024-10-25) |
| Q4 2024 | 443.3 | +12.2% | n/d | n/d | 359.7 | 41.9 | 73.4% | 2.2 | 2.6 | 4.68 | 4.62 | +19.4% | 63.75 | -7.8% (2025-02-14) |
| Q1 2025 | 484.3 | +7.9% | -18.4% | +16.7% | 365.8 | 43.8 | 82.1% | 6.0 | 3.9 | 3.83 | 3.71 | +6.0% | 67.92 | **-16.3%** (2025-04-25) |
| Q2 2025 | 555.5 | +4.9% | -16.8% | +14.3% | 383.6 | 46.5 | 75.8% | 0.9 | 3.9 | 5.76 | 4.78 | +27.5% | 73.93 | +0.2% (5-day -7.5%) |
| Q3 2025 | 486.3 | +8.4% | -7.9% | +12.3% | 411.0 | 49.6 | 74.9% | 0.3 | 3.7 | 6.09 | 5.21 | +24.0% | 80.19 | -6.8% (2025-10-24) |
| Q4 2025 | 451.1 | +1.8% | -28.3% | +10.2% | 415.5 | 52.3 | 71.7% | 0.7 | 4.0 | 5.99 | 5.81 | +25.8% | 84.66 | -7.4% (2026-02-13) |
| Q1 2026 | 482.0 | -0.5% | -28.3% | +6.0% | 406.9 | 55.4 | 77.4% | 0.4 | 4.5 | 4.88 | 5.11 | +37.7% | 85.31 | -0.8% (5-day -7.0%) |
| Q2 2026 | 527.6 | **-5.0%** | -32.7% | +3.7% | 417.6 | 55.7 | 75.5% | 1.3 | 4.5 | 7.72 | 5.54 | +15.9% | 89.34 | +5.1% (2026-07-24) |

n/d = not disclosed in the fetched release (the CP split first appears in the Q1 2025 release in what I read). Q1 2024 GWP growth of 25.5% was down from 33.8% in Q4 2023 ([Q1 2024 call summary, investing.com](https://in.investing.com/news/earnings-call-kinsale-capitalizes-on-strong-q1-2024-performance-93CH-4154676)).

Annual context: FY2019 combined ratio 84.7%, op ROE 15.9% (Q4 2019 release, search snippet); FY2020 86.7% (Q4 2020 release, snippet; 5.6 cat pts per Q4 2021 release); FY2021 77.1%, GWP +38.3% to $764.4M, op ROE 20.8%; FY2022 77.9% (Q4 2022 release) **or 78.5%** (as shown in the Q4 2023 release — conflict, see open questions), GWP +44.2%, op EPS $7.80, op ROE 25.0%; FY2023 75.4%, GWP +42.3%, op EPS $12.50, op ROE 31.8%, BVPS $46.88 (Dec 2022 BVPS $32.28 per the Q4 2023 release); FY2024 76.4%, GWP +19.2%, op EPS $16.06, op ROE 29.2%; FY2025 75.9%, GWP +5.7% ($2.0B), CP -17.9%, ex-CP +13.3%, op EPS $19.51, GAAP EPS $21.65, op ROE 26.4%, PYD 3.9 pts ($62.8M).

Guidance: Kinsale gives no numeric guidance. Management targets 20%+ ROE on every product line and says it will not trade margin for growth (Q2 2026 call, [investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-kinsale-capital-tops-q2-2026-forecasts-as-shares-rise-93CH-4811975)).

### Derived from the table

- TTM operating EPS to Q2 2026: 5.21 + 5.81 + 5.11 + 5.54 = **$21.67**; TTM GAAP EPS 6.09 + 5.99 + 4.88 + 7.72 = $24.68 (cache point-in-time TTM $24.64, rounding). Non-operating items in TTM GAAP EPS ≈ **+$3.0/share** (Q3'25 +0.88, Q4'25 +0.18, Q1'26 -0.23, Q2'26 +2.18).
- TTM NEP $1,651M; TTM NII $213.0M; TTM PYD $70.9M pre-tax (15.8 + 17.0 + 18.7 + 19.4) ≈ $2.46/share after 20% tax.
- P/B at Friday's $330.49: 330.49 / 89.34 = **3.70x**. P/E on TTM operating EPS: **15.25x**. At the 2024-03-06 high ($547.98) on the then-latest reported figures (FY2023): P/B 11.7x (BVPS $46.88), P/E 41.4x GAAP / 43.8x operating. Other P/B points: Dec 2024 close $465.1 / $63.75 = 7.3x; Dec 2025 $391.1 / $84.66 = 4.6x; 2026-06-03 low $290.20 / $85.31 = 3.4x.
- Operating EPS from FY2023 ($12.50) to TTM Q2 2026 ($21.67): +73%.

## 3. Balance sheet, liquidity and debt (Q2 2026 10-Q, text downloaded from the 10-Q URL above)

- Cash and cash equivalents **$210.5M** (Dec 2025 $163.4M). Total investments $5,298M: fixed maturities $4,470.5M AFS (gross unrealized losses $110.4M), equity securities $773.1M at fair value (cost $581.8M, so ~$191M unrealized gain in income-statement exposure), real estate $54.7M. Release: cash and invested assets $5.5B, average credit quality AA-, duration 4.3 years, H1 2026 annualized gross investment return 4.5%.
- The fundamentals cache shows "cash $2.89B"; that is **not** a 10-Q line (10-Q: $210.5M cash + $5.3B investments). The origin of the $2.89B figure is unverified (probably a data vendor's cash-and-investments aggregation).
- Debt table (10-Q Note 13): Credit Facility $51.0M drawn, maturity **2027-07-22**; 5.15% Series A Notes $125.0M due 2034-07-22; 6.21% Series B Note $50.0M due 2034-07-22; less $1.465M issuance costs = total $224.5M. Series A amortizes $25M a year and Series B $10M a year from 2030-07-22.
- Credit Facility: $100.0M senior unsecured revolver (JPMorgan Chase agent, Truist syndication agent), option to increase by $30.0M, commitment fee 0.25%, Adjusted Term SOFR + 1.625%; H1 2026 weighted rate 5.42%. Undrawn: **$49M**. $30M drawn and repaid in H1 2026 around share-repurchase timing.
- Covenants: "financial covenants customary for agreements of this type"; in compliance at 2026-06-30. December 2025 amendment loosened the restricted-payments covenant (8-K 2025-12-11, items 1.01/8.01). Specific covenant tests not stated in the 10-Q.
- Note Purchase Agreement (PGIM) shelf capacity up to $200M through 2026-09-18 (now expired or expiring; $175M issued).
- Leases: no lease note or lease liability found in the 10-Q text; the company owns real estate ($54.7M). Interest expense $6.5M in H1 2026.
- Holding company funded by service fees, tax-sharing payments and dividends from Kinsale Insurance Company (Arkansas domicile). Statutory dividend capacity: not in the 10-Q text I searched.
- Gross loss reserves $2,890.9M at 2025-12-31 and **$3,192.6M at 2026-06-30** (10-Q reserve roll-forward); net $2,509.5M at 2025-12-31. Reinsurance recoverables, net $415.1M at 2026-06-30.
- H1 2026 reserve development: favourable $38.1M net = $43.1M favourable on accident years 2020-2025 ("lower emergence of reported losses than expected ... particularly in the shorter-tail lines") less adverse development "primarily in the construction liability business in the 2017 through 2019 accident years". H1 2025 showed the same pattern ($35.8M favourable on 2020-2024 AYs, construction adverse on older years).
- Operating cash flow $490.8M in H1 2026; share repurchases $163.1M in H1 2026; dividends $11.5M in H1 2026. Buyback authorization: $87.5M left at 2026-06-30, +$250M in July 2026 → $337.5M.
- Effective tax rate 19.8% H1 2026 (stock-comp benefits and tax-exempt income). Stock comp $11.4M in H1 2026.
- H1 2026 GWP mix: 74.1% casualty, 25.9% property; personal lines (homeowners) 2.5%.
- Average premium per policy ~$12,300 in Q2 2026 vs ~$14,300 in Q2 2025 ("heightened competition").

## 4. Stock timeline (prices: local cache; causes: sources as cited)

| Date | Close | Move | Cause | Source |
|---|---|---|---|---|
| 2023-10-27 | 342.87 | -19.6% | Q3 2023 results; management's growth outlook unsettled investors (before the 5-year high; context only) | [investing.com](https://www.investing.com/news/stock-market-news/kinsale-capital-stock-drops-20-despite-strong-quarterly-results-93CH-3218643) |
| 2024-02-16 | 505.03 | +15.4% | Q4 2023: GWP +33.8%, CR 72.1%, op EPS $3.87 | Q4 2023 release |
| 2024-03-06 | **547.98** | 5-year high | P/B 11.7x, P/E 41x GAAP (derived) | price cache |
| 2024-04-26 | 374.64 | -17.3% | Q1 2024: GWP growth slowed to +25.5% from +33.8%; CR 79.5% vs 72.1% in Q4. Management: property returning to "a normal level of competition". No news article giving the market's reason was found | Q1 2024 release; call summary above |
| 2024-07-26 | 443.29 | +17.5% | Q2 2024: GWP +20.9%, op EPS +30.2% | Q2 2024 release |
| 2024-12-06 | 524.22 | local high | Recovery to within 4% of the March 2024 high | price cache |
| 2025-02-14 | 449.34 | -7.8% | Q4 2024: GWP +12.2%, "increasingly competitive" pricing | Q4 2024 release |
| 2025-04-25 | 419.99 | -16.3% | Q1 2025: GWP +7.9% vs J.P. Morgan's expected 15%; NWP +8.7%, lowest since 2017 (Oppenheimer); CP -18.4%; Palisades Fire cat 6.0 pts | [itiger / Dow Jones summary](https://www.itiger.com/hans/news/2530168290) (search snippet), Q1 2025 release |
| 2025-07-25 | 477.35 | +0.2% (5-day -7.5%) | Q2 2025: GWP +4.9%, CP -16.8% | Q2 2025 release |
| 2025-10-08 | 478.99 | 12-month high | | price cache |
| 2025-10-24 | 422.38 | -6.8% | Q3 2025: GWP +8.4%, CP -7.9%; same day, President/COO Haney's 2026 retirement announced | Q3 2025 release; 8-K 2025-10-23 |
| 2026-02-13 | 371.32 | -7.4% | Q4 2025: GWP +1.8%, CP -28.3%; op EPS +25.8% | Q4 2025 release |
| 2026-02-25 | 373.16 | -2.0% | BMO downgrade Market Perform → Underperform, PT $418 → $348 | [MarketScreener](https://www.marketscreener.com/news/bmo-capital-downgrades-kinsale-capital-group-to-underperform-from-market-perform-cuts-price-target-ce7e5cdbdf8ef72d) |
| 2026-03-19 | 326.72 | -6.2% | Jefferies downgrade Hold → Underperform, PT $392 → $312: E&S market grew ~8% in 2025 and ~3% in H2 2025; after E&S growth falls to single digits the industry historically averaged 1-2% CAGR over three years | [investing.com](https://www.investing.com/news/analyst-ratings/jefferies-downgrades-kinsale-capital-stock-rating-on-slowing-growth-93CH-4569848), [Yahoo/Simply Wall St](https://finance.yahoo.com/markets/stocks/articles/look-kinsale-capital-group-knsl-170357858.html) |
| 2026-04-06 | 345.79 | +0.3% | Morgan Stanley Overweight → Equal-weight, PT $450 → $350 (E&S property pricing, softening P&C cycle; valuation "full on a growth-adjusted basis") | [investing.com](https://www.investing.com/news/analyst-ratings/morgan-stanley-cuts-kinsale-capital-stock-rating-on-pricing-pressures-93CH-4597811) |
| 2026-04-09 | 361.77 | +1.5% | Cantor Fitzgerald Neutral, PT $360 → $280; expects the most margin pressure in its group in 2026 (commercial-property mix, conservative reserving), ~3-pt loss-ratio deterioration, 2026 GWP growth ~5%; values at 2.8x book | [investing.com](https://www.investing.com/news/analyst-ratings/cantor-fitzgerald-cuts-kinsale-capital-stock-price-target-on-margin-concerns-93CH-4605507) |
| 2026-04-24 | 345.08 | -0.8% (5-day -7.0%) | Q1 2026: GWP -0.5%, CP -28.3% ("including from standard carriers"); op EPS +37.7% | Q1 2026 release |
| 2026-04-29 | — | — | EVP & CIO Diane Schnupp retired; analytics/technology realignment | 8-K 2026-04-29 |
| 2026-06-03 | **290.20** | cycle low | -47% from the high | price cache |
| 2026-06-26 | 328.43 | +6.5% | no source found | price cache |
| 2026-07-24 | 349.10 | +5.1% | Q2 2026: op EPS $5.54 vs consensus ~$5.10-5.11 (third-party); GWP -5.0%, CP -32.7% | Q2 2026 release; investing.com transcript |
| 2026-08-24 | 395.51 | post-Q2 high | | price cache |
| 2026-08-31 → 09-25 | 373.90 → 330.49 | -11.6% | No company-specific news found. Specialty/broker peers fell alike over the same dates (local price cache): RLI -12.3%, AJG -11.8%, BRO -15.7%, RYAN -10.2%, WRB -1.1%, SPY -0.8%. Public brokers reported roughly flat organic growth in Q2 2026 ([Business Insurance](https://www.businessinsurance.com/slow-organic-growth-soft-market-hit-public-brokers-consultant/), search snippet) | price cache; [GuruFocus 2026-09-23](https://www.gurufocus.com/news/9094316/kinsale-capital-group-inc-knsl-stock-down-35-now-undervalued-gf-score-84100) (no cause given) |

Peer context since the 2024-03-06 high (local price cache, to 2026-09-25): KNSL -40%, RLI -25%, RYAN -30%, BRO -29%, WRB +18%, CINF +38%, TRV +65%, SPY +49%. The E&S specialists and brokers fell; the diversified standard carriers did not.

## 5. Q2 2026 call (2026-07-24), [investing.com transcript summary](https://www.investing.com/news/transcripts/earnings-call-transcript-kinsale-capital-tops-q2-2026-forecasts-as-shares-rise-93CH-4811975)

- E&S market "competitive and largely consistent" with Q1. Pricing cited as down 5.9% vs down 3.3% in Q1, "in line with" a market index (the summary attributes it to an MS Amlin index; whether this is Kinsale's own renewal rate change or the index is unclear — open question).
- Commercial Property: material rate declines with broader coverage terms; Kinsale shrinking; no stabilization signal; ~60% of the prior year's CP premium was written in H1, so the y/y comparison eases in Q3-Q4.
- Growing lines: excess casualty, commercial auto, entertainment, environmental, energy. New-business submissions +6% (ex-CP +8%); over half of divisions with double-digit submission growth; most growth in accounts under $25,000 premium.
- Expense ratio 21.7% vs 20.7% (higher net commission from reinsurance retention changes); CFO expects Q2 level to continue with a possible "slight uptick". Other underwriting expense ratio 10.3% vs 10.6%.
- Float $3.4B vs $3.1B at end of 2025.
- Product launches: 9 YTD, 5 imminent, 10 in pipeline; 24 new wholesale and 176 retail broker appointments (Aspera).
- Buybacks the main capital tool given "moderate growth"; CEO Kehoe: shares "a very good value" at the current price.
- The investing.com summary compares "revenue $527.61M vs $451.75M forecast" — this mixes GWP with a revenue consensus; ignored.

## 6. Industry data (third-party)

- WSIA: 15 stamping-office states' surplus-lines premium +8% in 2025 to $90.3B ([The Insurer, 2026-01-30](https://www.theinsurer.com/e-and-s/news/wsia-stamping-office-surplus-lines-premium-up-8-in-2025-to-903-billion-2026-01-30/), search snippet).
- WSIA H1 2026: premium +2.8% to $47.6B; item filings +16.9% to 4.3M; property premium -13.7% while property transactions +15.2%; liability still hardening ([The Insurer, 2026-08-05](https://www.theinsurer.com/e-and-s/news/surplus-lines-stamping-office-premium-volume-up-28-to-476-billion-in-h1-2026-2026-08-05/), [Insurance Business](https://www.insurancebusinessmag.com/us/news/excess-surplus/property-softens-liability-hardens-what-eands-midyear-data-means-for-brokers-585004.aspx), search snippets).
- Brokers: Q2 2026 organic growth roughly flat for public brokers; BRO -0.7%, RYAN 6.7% vs 11.8% in Q1 (Business Insurance, search snippet).

## 7. Consensus and ratings (third-party, not verified against a primary data vendor)

| Item | Value | Source |
|---|---|---|
| FY2026 EPS (operating basis) | $21.13 (+8.3%), 12 analysts | [stockanalysis.com](https://stockanalysis.com/stocks/knsl/forecast/) |
| FY2026 EPS, alt. | consensus $21.12; Zacks Research $20.93 (Aug 2026) | [Daily Political 2026-08-06](https://www.dailypolitical.com/2026/08/06/what-is-zacks-researchs-estimate-for-knsl-fy2026-earnings.html) (search snippet) |
| FY2027 EPS | $21.65 (+2.4%) | stockanalysis.com |
| FY2027 EPS, alt. | consensus $21.10; Zacks Research $21.41 | Daily Political 2026-08-06 / 2026-08-11 (they conflict; see open questions) |
| FY2026 revenue | $1.96B (+4.7%); range $1.91-1.98B across nine analysts | stockanalysis.com; search snippet |
| FY2027 revenue | ~+0.8-0.9% vs 2026 (Zacks consensus) — exact figure not seen | search snippet (Zacks via Yahoo) |
| Q2 2026 consensus op EPS | $5.10-5.11 | investing.com; Daily Political 2026-08-11 |
| Ratings | 1 Buy / 6 Hold / 3 Sell, "Reduce", avg PT $362.11 (MarketBeat count); stockanalysis: 12 analysts, "Hold", avg PT $354.78, range $259-$405 | [Daily Political 2026-08-11](https://www.dailypolitical.com/2026/08/11/equities-analysts-offer-predictions-for-knsl-q3-earnings.html); stockanalysis.com |
| Other PT moves | Wells Fargo to $377 (2026-07-27); RBC to $375 and Truist to $405 (2026-04-27) | Daily Political 2026-08-11 |
| Insider selling | $10.7M over the last 12 months | GuruFocus 2026-09-23 |

Consensus EPS is on the operating basis (FY2026 $21.13 = FY2025 op EPS $19.51 × 1.083). The Yahoo "forward EPS 21.65" in the fundamentals cache equals the FY2027 figure, so the cache's "implied forward -12.3%" compares operating consensus with GAAP TTM and overstates the expected decline.

## 8. Rule-exit arithmetic (derived)

The v3 trigger reads point-in-time **GAAP** TTM EPS (entry $24.64, trigger $20.94, window to 2027-09-28). Quarters that roll off: Q3'25 $6.09 (in the Q3 2026 print), Q4'25 $5.99, Q1'26 $4.88, Q2'26 $7.72 (in the Q2 2027 print, late July 2027). The four replacement quarters must sum to more than $20.94, i.e. average above $5.24 GAAP.

- Consensus path, no investment gains or losses: Q3+Q4 2026 ≈ $10.49 (FY2026 $21.13 less H1 op $10.64) and H1 2027 ≈ $10.8 (half of FY2027 $21.65) → TTM after the Q2 2027 report ≈ **$21.3, about 2% above the trigger**.
- Each $1/share of after-tax equity mark-to-market ≈ $29M pre-tax at a 20% tax rate and 23.1M shares, i.e. a ~3.8% move in the $773M equity portfolio. A ~10% equity-market decline in the window, a heavy cat quarter or a reserve charge would likely trip the trigger even if the underwriting business is unchanged.
- Quarter-by-quarter at $5.30 GAAP per quarter: 23.85 (Oct 2026), 23.16 (Feb 2027), 23.58 (Apr 2027), 21.16 (Jul 2027).

## 9. Open questions no source closed

1. Cause of the -11.6% move from 2026-08-31 to 2026-09-25: no company-specific news found; peers fell alike. Was there a conference remark, a peer pre-announcement or a rate-index release?
2. The market's stated reason for the 2024-04-26 -17.3% move: only the filing numbers (growth slowdown to 25.5%, CR 79.5%) were found, no contemporaneous analyst or news explanation.
3. Is the "-5.9% pricing" in Q2 2026 Kinsale's own rate change or an external index? The transcript summary is ambiguous.
4. Specific financial covenants (minimum net worth, leverage) in the credit agreement and note purchase agreement; plan for the revolver maturing 2027-07-22.
5. Statutory surplus, ordinary-dividend capacity of Kinsale Insurance Company, and the current A.M. Best rating: not verified in this pass.
6. FY2022 combined ratio: 77.9% in the FY2022 release vs 78.5% in the FY2023 release comparative. I use 77.9% for 2022 as reported at the time; the difference may be a reclassification (not verified).
7. Q3 2026 release date: not announced in anything found (pattern: fourth Thursday of October, 2024-10-24 and 2025-10-23 → probably ~2026-10-22).
8. FY2027 consensus EPS differs by source ($21.65 stockanalysis vs $21.10 MarketBeat-type consensus); FY2027 revenue consensus not seen directly.
9. Origin of the fundamentals cache's "cash $2.89B" (10-Q: cash $210.5M, investments $5.3B).
10. Reserve adequacy on 2022-2024 casualty accident years (industry-wide adverse development in those years at other carriers?): Kinsale keeps posting favourable development (4.5 pts), but no independent reserve study was found.
11. Cause of the +6.5% day on 2026-06-26.
