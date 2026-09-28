# PODD (Insulet) — working notes for the turnaround v3 thesis, 2026-09-28

Research date 2026-09-28 (before the open; the price cache has a partial 2026-09-28 bar at $132.57 on 0.53M shares, not used; all returns are from the Friday 2026-09-25 close of $136.13). Thesis file: `turnaround_backtest_v3/thesis/PODD.md`. Base research reused and re-checked: `reports/Dexcom vs Insulet comparison.md` and `research_notes/Dexcom vs Insulet comparison/` (cited below as "comparison notes"). Primary documents were re-downloaded from EDGAR for this pass (Q2 2026 10-Q, FY2025 10-K, Q1/Q2 2026 and Q3/Q4 2025 8-K exhibits, the September 2026 8-Ks) and parsed locally. Consensus, ratings and short-interest figures are third-party and labelled as such. Research tooling, not investment advice.

## 1. Local cache (primary, point-in-time SEC data)

Source: `turnaround/cache/edgar/PODD.json`, `fundamentals/PODD.json`, `valuation/PODD.json`, `prices/PODD.csv`.

| Quarter end | TTM revenue $M | TTM net income $M | TTM operating income $M | TTM EPS (GAAP) | Cash $M | Debt $M | Available |
|---|---|---|---|---|---|---|---|
| 2024-12-31 | 2,071.6 | 418.3 | 308.9 | 5.78 | 953 | 1,380 | 2025-02-21 |
| 2025-03-31 | 2,198.9 | 402.2 | 340.8 | 5.55 | 1,283 | 1,695 | 2025-05-09 |
| 2025-06-30 | 2,359.5 | 236.1 | 407.3 | 3.28 | 1,122 | 1,400 | 2025-08-07 |
| 2025-09-30 | 2,521.8 | 246.2 | 436.8 | 3.43 | 757 | 1,015 | 2025-11-06 |
| 2025-12-31 | 2,708.1 | 247.1 | 473.8 | 3.48 | 716 | 949 | 2026-02-18 |
| 2026-03-31 | 2,900.8 | 302.8 | 507.1 | 4.28 | 480 | 948 | 2026-05-06 |
| 2026-06-30 | 3,053.4 | 375.3 | 515.7 | 5.33 | 535 | 948 | 2026-08-05 |

- TTM net income / operating income 0.73 (one-off guard passed); TTM OCF $511.2M, capex $245.6M, FCF $265.6M; EBITDA TTM $652.7M (fundamentals) vs $615.0M (EDGAR rebuild), hence net debt/EBITDA 0.6 vs 0.7 in the thesis rows; interest TTM $58.7M, coverage 9.4x.
- Price legs (cache closes): peak $352.82 2025-09-09; $346.36 2025-11-19; Investor Day 2025-11-20 $312.89 (-9.7%); $258.07 2026-02-18; $142.65 2026-05-28; $166.82 2026-08-04; $133.26 2026-08-05 (-20.1%); low close since the peak $131.96 on 2026-09-11; $136.13 2026-09-25.
- Leg returns: 2025-09-09 → 2026-02-18 -26.9% (XLV +13.8%, SPY +5.5%, DXCM -7.1% over the same dates); 2026-02-18 → 05-28 -44.7% (XLV -4.3%, SPY +10.0%, DXCM -0.6%); 05-28 → 08-04 +16.9%; 08-04 → 08-05 -20.1% (XLV +1.3%, DXCM -4.9%); 08-05 → 09-25 +2.2%. Peak to 2026-09-14: XLV +20.6%, SPY +17.0% (last bars in those caches); DXCM +10.5% to 09-25. The fall is company-specific, not sector.

## 2. Filings: survival data (Q2 2026 10-Q, FY2025 10-K, 8-Ks)

Sources: [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000169/podd-20260630.htm); [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000028/podd-20251231.htm); [Sept 21, 2026 8-K (Ninth Amendment)](https://www.sec.gov/Archives/edgar/data/1145197/000119312526396779/d71204d8k.htm).

- Debt at 2026-06-30 (10-Q Note 8): equipment financings $28.3M (2028); Costa Rica plant financing $7.4M (2028); revolver (2030) undrawn; Term Loan B $475.0M (2031; $477.5M at Dec 31, 2025, so ~$1.25M a quarter amortization); 6.5% senior unsecured notes $450.0M (due April 2033); less $3.4M discount and $8.9M costs = $948.4M ($18.9M current, $929.5M long-term). Swaps fix $460M notional at a weighted 3.47%. — 10-Q.
- Covenants (10-Q liquidity section, same wording in the 10-K): the revolver "contains a covenant to maintain a specified leverage ratio when there are amounts of at least 35% of the aggregate Revolving Credit Facility outstanding"; other covenants "none of which are considered restrictive"; Term Loan B covenants restrict debt, liens, asset sales, acquisitions; the senior notes carry leverage and fixed-charge-coverage covenants "measured upon the incurrence of future debt". So there is no maintenance covenant while the revolver is less than 35% drawn. The numeric ratio is not in the filings text I parsed (it is in the credit agreement exhibit; not read). Whether the 35% trigger is unchanged after the Ninth Amendment is not stated in the 8-K (it says "substantially similar terms" for the term loans) — unverified.
- Ninth Amendment, 2026-09-21: $475M term loans replaced at par with new term loans at SOFR + 1.75% (base + 0.75%), 25 bp lower, SOFR floor 0%; revolver commitments +$250M to **$750M**, undrawn at closing, margin cut to SOFR + 1.25-1.75% (from 1.50-2.00%) by adjusted total leverage ratio; agent Morgan Stanley Senior Funding. — 8-K.
- Debt maturity ladder at Dec 31, 2025 (10-K Note 13): 2026 $18.4M; 2027 $19.4M; 2028 $12.1M; 2029 $5.0M; 2030 $5.0M; remainder 2031 (TLB) and 2033 (notes). Add the $7.4M Costa Rica financing (2028) booked in 2026. Next 24 months (Oct 2026-Sep 2028): roughly $35-40M, all amortization (my sum from the ladder; exact quarter split not disclosed).
- Contractual obligations at Dec 31, 2025 (10-K): debt $18.4M short / $944.0M long; interest payments $59.6M / $317.3M (before swaps); purchase obligations $353.1M / $114.1M; lease obligations $5.8M / $67.4M; total $436.9M / $1,442.8M.
- Operating leases (10-K Note 12): liabilities $51.9M ($3.0M current); payments 2026 $6.6M, 2027 $8.0M, 2028 $7.9M, 2029 $8.1M, 2030 $12.4M, thereafter $39.3M; lease cost $10.6M in 2025; 10.0-year weighted term, 7.9% discount rate.
- Costa Rica: build-to-suit plant, Insulet is accounting owner; April 2026 guarantee of up to $97M of the seller's construction loan (contingent). — 10-Q.
- Liquidity statement: current liquidity "sufficient to meet our projected operating, investing and debt service requirements for at least the next twelve months". — 10-Q.
- Cash flow H1 2026: OCF $202.2M (vs $260.3M), capex $56.8M (vs $30.9M), FCF $145.4M (vs $229.4M); working-capital outflow $94.5M (AR +$76.9M "primarily driven by the timing of distributor orders in the United States", inventory +$34.9M planned build, prepaid +$28.1M; AP +$39.9M); financing -$315.9M incl. $300M ASR. — 10-Q and [Q2 2026 8-K exhibit](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000167/podd2026-06x30ex991.htm).
- FY2026 net interest expense guided to "$40 million or more, primarily due to lower interest income". — FY2025 10-K MD&A.
- Capital return: $475M authorization to Dec 31, 2027; $300M ASR completed by Mar 31, 2026; 1,251K shares bought in H1 2026 for $302.6M; ~$115M left (comparison notes); 69,354,199 shares at 2026-07-29. — 10-Q.
- Ratings: Moody's Ba3 / S&P BB (March 2025 upgrades; comparison notes, [Investing.com Moody's](https://www.investing.com/news/stock-market-news/insulets-corporate-family-rating-upgraded-by-moodys-ratings-93CH-3935535)). Current outlooks unverified.

## 3. Filings: EPS base and headline adjustments

- Q2 2026 GAAP → non-GAAP (8-K exhibit): GAAP net income $95.0M / EPS $1.37; + voluntary MDC costs $25.0M pre-tax ($20.0M after tax, $0.29); CFO transition -$0.2M; tax matters +$0.2M → non-GAAP $115.0M / $1.66; GAAP gross margin 70.2% vs 72.9% adjusted (MDC $21.9M in COGS); GAAP operating margin 16.2% vs 19.3%.
- H1 2026: MDC costs $36.7M pre-tax ($29.3M after tax, $0.42/share) — Q1 $11.7M ($0.13), Q2 $25.0M ($0.29). GAAP H1 EPS $2.67 vs adjusted $3.08. — Q1 and Q2 2026 8-K exhibits ([Q1](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000100/podd2026-03x31ex991.htm)).
- MDC total cost estimate $60-70M, most in 2026, remainder 2027; 10-Q says net six-month charge $41.0M (the 10-Q figure is net warranty-related; the 8-K adjustment is $36.7M — the two bases differ and I did not reconcile the $4.3M gap); warranty liability $33.4M at June 30, 2026 (MDC warranty expense $37.0M in H1, change in estimate -$3.6M). — 10-Q.
- Insulet's non-GAAP adjustments do **not** remove stock comp or amortization (Q2 2026 reconciliation items are MDCs, CFO transition, tax only; FY2025 items: CEO/CFO transition, $123.9M debt extinguishment, $12.5M derivative gain, $7.5M investment losses, tax matters). So adjusted EPS is close to "GAAP ex one-offs". The comparison notes' statement that the FY2025 GAAP-to-adjusted gap was "mostly stock comp, amortization ..." is incorrect; it was mostly the debt-extinguishment loss ($1.71/share of the $1.49 gap, partly offset by the derivative gain and tax matters). — [Q4 2025 8-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000026/podd202512-31ex991.htm).
- Stock comp: Q2 2026 $19.7M, H1 2026 $40.9M vs $25.7M in H1 2025 (which included a $10.8M reversal on the former CEO's forfeiture); FY2025 $62.7M incl. $11.7M reversal. — 10-Q, 10-K.
- Debt extinguishment 2025: $123.9M total, $84.4M in Q2 2025 ($1.16/share in the Q2 2025 reconciliation) and $39.5M in Q1 2025 (derived: 123.9 - 84.4). This is why the rule's TTM EPS change is +62% (5.33 vs 3.28): Q2 2025 GAAP EPS $0.32 left the window. On adjusted EPS the TTM change is +38% ($5.87 vs $4.24, comparison report).
- Tax: ETR 20.0% Q2 2026, 19.7% H1 2026 (R&D credits, mix, foreign tax credits) vs 27.2% FY2025 (non-deductible convert premiums) and a 39.3% benefit in FY2024 (valuation-allowance releases $146.9M Q2 2024 + $14.8M Q3 2024; FY total $190.8M + $8.3M R&D credits). Q4 2025 GAAP ETR 27.5% with a $7.7M "tax matters" adjustment. — 10-Q, 10-K, 8-Ks.
- Distributor concentration: three distributors were 27%, 26% and 25% of 2025 revenue. — FY2025 10-K. US quarterly growth can swing with distributor order timing (H1 2026 AR build above).
- Diluted shares 69.403M in Q2 2026 vs 70.652M a year earlier (-1.8%); the rule row's -2.2% uses the EDGAR weighted series (70.41M vs 71.98M). ASR effect on EPS ~2%.

## 4. Quarterly table, Q3 2023 - Q2 2026 (12 quarters)

Sources: Insulet 8-K Exhibit 99.1 per quarter (links in the comparison notes' `insulet_earnings_and_stock_timeline.md`, Table A; Q3 2025, Q4 2025, Q1 2026 and Q2 2026 re-read for this pass). Consensus is third-party (Zacks for 2023-Q1 2024, MarketBeat / Investing.com later). Move = close-to-close from the price cache on the reaction day.

| Quarter (released) | Revenue $M (YoY rep / cc) | US Omnipod $M (YoY) | GAAP EPS | Adj EPS | Consensus adj EPS | Guidance action (FY, cc) | Move |
|---|---|---|---|---|---|---|---|
| Q3 2023 (2023-11-02) | 432.7 (+27.0% / +25.1%) | 320.6 (+34.6%) | 0.74 | 0.71 | ~0.40 (Zacks) | FY23 raised to 26-27% | +15.8% |
| Q4 2023 (2024-02-22) | 509.8 (+37.9% / +36.6%) | 394.6 (+42.9%) | 1.44 | 1.40 | 0.67 (Zacks) | FY24 initiated 12-17% | -6.6%, -8.3% |
| Q1 2024 (2024-05-09) | 441.7 (+23.3% / +22.8%) | 317.7 (+22.7%) | 0.73 | 0.73 (unverified as distinct) | ~0.39 (Zacks) | FY24 raised to 14-18% | -6.6% |
| Q2 2024 (2024-08-08) | 488.5 (+23.2% / +23.4%) | 352.3 (+27.3%) | 2.59 (incl. $146.9M VA release) | 0.55 | 0.56 | FY24 raised to 16-19% | -8.8% |
| Q3 2024 (2024-11-07) | 543.9 (+25.7% / +25.4%) | 395.6 (+23.4%) | 1.08 (incl. $14.8M VA release) | 0.90 | 0.77-0.78 | FY24 raised to 20-21% | +9.4% |
| Q4 2024 (2025-02-20) | 597.5 (+17.2% / +17.1%) | 443.7 (+12.4%) | 1.39 | 1.15 | 1.00-1.03 | FY25 initiated 16-20% | -1.9% |
| Q1 2025 (2025-05-08) | 569.0 (+28.8% / +29.8%) | 401.7 (+26.4%) | 0.50 (incl. ~$39.5M debt loss) | 1.02 | 0.79-0.81 | FY25 raised to 19-22% | +20.9% |
| Q2 2025 (2025-08-07) | 649.1 (+32.9% / +31.3%) | 453.2 (+28.7%) | 0.32 (incl. $84.4M debt loss) | 1.17 | 0.92 | FY25 raised to 24-27% | +9.5% |
| Q3 2025 (2025-11-06) | 706.3 (+29.9% / +28.2%) | 497.1 (+25.6%) | 1.24 | 1.24 | 1.13-1.14 | FY25 raised to 28-29% | +2.9% |
| Q4 2025 (2026-02-18) | 783.8 (+31.2% / +29.0%) | 567.8 (+28.0%) | 1.44 | 1.55 | 1.46-1.48 | FY26 initiated 20-22% (US 20-22%), adj EPS >25% | +4.8%, -3.5% |
| Q1 2026 (2026-05-06) | 761.7 (+33.9% / +30.1%) | 515.6 (+28.3%) | 1.30 (MDC $0.13) | 1.42 | 1.19-1.20 | FY26 raised to 21-23%; US held 20-22% | -9.7% |
| Q2 2026 (2026-08-05) | 801.7 (+23.5% / +22.7%) | 544.1 (+20.1%) | 1.37 (MDC $0.29) | 1.66 | 1.45-1.47 | FY26 cut to 20-22%; US 17-19% (from 20-22%); Intl 30-32%; adj EPS growth **>30% (from >25%)**; Q3 17.5-19.5% (US 14-16%) | -20.1% |

- Correction to the comparison notes: the Q2 2026 8-K guidance table, parsed cell by cell, shows "Adjusted EPS Growth: >30%" in the FY 2026 (as of 8/5/2026) column and ">25%" in the prior-guidance column. The comparison report's "conflict flag" (8-K says >25%, calls say at least 30%) came from misreading the table; the written guide is >30%. — [Q2 2026 8-K exhibit](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000167/podd2026-06x30ex991.htm).
- Q3 2026 guide in reported currency: total 17-19%, US 14-16%, Intl 26-28% (FX -2 pt); FY2026 reported 21-23%. Dollarised: Q3 ≈ $826-840M reported on $706.3M; FY ≈ $3.28-3.33B reported.
- Exit framework (Wells Fargo conference, 2026-09-09): Q4 2026 exit 12-17% cc (US 9-14%, Intl 19-24%); US new starts flat to slightly down at the low end; T2 attrition "more than double" the ~10% T1 rate; blended US attrition "mid-teens". — [Investing.com](https://ng.investing.com/news/stock-market-news/insulet-at-wells-fargo-conference-guidance-cut-meets-longterm-optimism-93CH-2690101) (third-party summary of a webcast; no transcript read).

## 5. Why the stock fell — dated facts

| Date | Close / move | Fact | Source |
|---|---|---|---|
| 2025-09-09 | $352.82 peak | ~83x trailing adjusted EPS ($4.24), 94x trailing GAAP at the 5y-high month (valuation cache) | comparison report; valuation cache |
| 2025-09-16/17 | -2.4% / -3.0% | CFO transition (Pease replaces Chadwick) | [Insulet release](https://investors.insulet.com/news/news-details/2025/Insulet-Announces-CFO-Transition/default.aspx) |
| 2025-11-06 | +2.9% | Q3 2025 beat; FY25 raised to 28-29% | [Q3 2025 8-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519725000067/podd2025-09x30ex991.htm) |
| 2025-11-20 | -9.7% ($312.89) | Investor Day: ~20% cc revenue CAGR 2025-28, ~100 bp/yr margin, 25%+ EPS CAGR; Omnipod 6 judged software-led; competitor patch pumps by 2027 | [Insulet release](https://investors.insulet.com/news/news-details/2025/Insulet-Outlines-Long-Term-Strategy-to-Drive-Growth-and-Value-Creation-at-2025-Investor-Day/default.aspx); [MedTech Dive](https://www.medtechdive.com/news/insulet-patch-pump-plans/806292/) |
| 2025-12-01 | -5.0% | CMS final DMEPOS competitive-bidding rule incl. pumps (link inferred) | [MedTech Dive](https://www.medtechdive.com/news/cms-final-rule-diabetes-competitive-bidding/806719/) |
| 2026-01-12 | -3.6% | Barclays Underweight on PODD and DXCM (competition) | [Investing.com](https://www.investing.com/news/stock-market-news/barclays-downgrades-dexcom-insulet-as-diabetes-competition-seen-intensifying-in-2-4442462) |
| 2026-02-18 | +4.8% then -3.5% | Q4 2025 beat; FY26 20-22%; $350M buyback increase, $300M ASR | [Q4 2025 8-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000026/podd202512-31ex991.htm) |
| 2026-03-13 | -6.9% | First Omnipod 5 pod correction (cannula/tubing tear, under-delivery) | [FDA](https://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/insulin-pump-recall-insulet-removes-certain-omnipod-5-pods) |
| 2026-04-24 | n/a | Rothschild Redburn to Neutral, $220 from $380 | [Investing.com](https://www.investing.com/news/analyst-ratings/rothschild-downgrades-insulet-stock-rating-on-competition-concerns-93CH-4634808) |
| 2026-04-29 | -12.5% | FDA Class I classification; 8-K on MDR counts (attribution inferred, date match) | [Insulet 8-K](https://www.sec.gov/Archives/edgar/data/0001145197/000114519726000095/podd-20260429.htm) |
| 2026-05-06 | -9.7% | Q1 beat, total raised to 21-23% but US held; new starts down sequentially; "modest retention deterioration" | [Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000100/podd2026-03x31ex991.htm); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/05/06/insulet-podd-q1-2026-earnings-transcript/) |
| 2026-05-26/27 | -0.7% / -5.1% | Second correction, ~7M pods | [Insulet 8-K](https://www.sec.gov/Archives/edgar/data/0001145197/000114519726000132/podd-20260526.htm) |
| 2026-05-28 | -2.3% ($142.65) | Federal Circuit reverses EOFlow verdict (time-barred) | [CAFC opinion](https://www.cafc.uscourts.gov/opinions-orders/25-1807.OPINION.5-28-2026_2700697.pdf) |
| 2026-06-03 | n/a | Director Stonesifer buys $400K at $143.51 | comparison notes ([MarketBeat insider](https://www.marketbeat.com/stocks/NASDAQ/PODD/insider-trades/)) |
| 2026-06-06 | n/a | STRIVE (Omnipod 6) data at ADA: T1 TIR 77% vs 73%, time in tight range 54% vs 47%; no FDA filing date given | [StockTitan copy of Insulet release](https://www.stocktitan.net/news/PODD/insulet-reveals-new-data-supporting-breakthrough-omnipod-6-and-fully-ppr56gfvrlme.html); [Drug Delivery Business](https://www.drugdeliverybusiness.com/insulet-investor-day-omnipod-6-2027/) (2026 filing, 2027 launch plan) |
| 2026-07-02 | n/a | Hu v. Insulet (D. Mass. 1:26-cv-13062), class period 2025-02-21 to 2026-05-26; no accrual; lead-plaintiff deadline Aug 31, 2026 | 10-Q; [Robbins Geller notice](https://www.globenewswire.com/news-release/2026/08/28/3352605/0/en/monday-podd-investor-deadline-insulet-corporation-investors-with-substantial-losses-have-opportunity-to-lead-class-action-lawsuit-robbins-geller-rudman-dowd-llp-announces.html) |
| 2026-08-05 | -20.1% ($133.26) | Q2 beat (rev $801.7M, adj EPS $1.66 vs ~$1.46) but US FY cut to 17-19%, Q3 US 14-16%; "lower rates of utilization and retention among type 2 customers"; at least six downgrades, target cuts to $144-152 (JPM, TD Cowen, Wells Fargo, Leerink) | [Q2 8-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000167/podd2026-06x30ex991.htm); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/12/insulet-podd-q2-2026-earnings-call-transcript/); [Investing.com JPM](https://www.investing.com/news/stock-market-news/jpmorgan-cuts-insulet-to-neutral-on-slowing-us-growth-trims-target-by-45-4841939) |
| 2026-08-21 | n/a | CEO McEvoy buys 1,100 shares at ~$147.47 | [Benzinga](https://www.benzinga.com/news/26/08/61385697/president-and-ceo-insulet-purchased-162k-stock) |
| 2026-09-03 / 09-08 | n/a | Directors Scannell (health; 12 years, 7 as chair) and Minogue (running for MA governor; left Sept 15) step down; "not due to any disagreement" | [8-K Sept 10, 2026](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000175/podd-20260903.htm) |
| 2026-09-04 | n/a | Zacks: estimates "broadly trending downward"; Zacks Rank #3; FY26 adj EPS consensus $6.51 | [Yahoo/Zacks](https://finance.yahoo.com/markets/stocks/articles/why-insulet-podd-8-1-153013441.html) |
| 2026-09-09 | -3.1% | Wells Fargo conference: exit 12-17% cc, US 9-14% | Investing.com (above) |
| 2026-09-11 | $131.96 | Lowest close since the peak | price cache |
| 2026-09-14 | n/a | Beta Bionics Mint patch pump cleared; full US launch Q1 2027, pharmacy only, ≥1.5M disposables in 2027 | [MedTech Dive](https://www.medtechdive.com/news/beta-bionics-insulin-patch-pump-gets-fda-nod/830332/) |
| 2026-09-16 | n/a | Nonqualified deferred comp plan adopted (effective 2027-01-01) | [8-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000177/podd-20260914.htm) |
| 2026-09-21 | n/a | Term loan repriced -25 bp; revolver to $750M | 8-K (above) |

## 6. Consensus and sell side (third-party)

- StockAnalysis (fetched 2026-09-28): 25 analysts, consensus "Buy", average target $171.91, range $144-275; FY2026 revenue $3.29B (+21.4%), EPS $6.50 (+30.8%); FY2027/28 behind paywall. Latest listed actions: Citi Hold $150 (Aug 13), UBS Hold $150 (Aug 12), Baird Buy $175, Deutsche Bank Buy $180, StoneX Buy $185 (Aug 6). — [StockAnalysis forecast](https://stockanalysis.com/stocks/podd/forecast/)
- FY2027: EPS $7.71 (StockAnalysis via local cache `eps_forward` 7.7065; comparison notes) / $7.63 (MarketScreener); revenue ~$3.74B (+13.8%) MarketScreener; FY2028 $4.25B / $9.14 (MarketScreener, vintage unclear). — [MarketScreener](https://www.marketscreener.com/quote/stock/INSULET-CORPORATION-50468/finances/)
- Zacks FY2026 $6.51 on $3.28B; the Zacks FY2027 figure seen ($7.99, +23.9%) is the pre-Q2 vintage and is stale. — [Yahoo/Zacks](https://finance.yahoo.com/healthcare/articles/podds-q2-earnings-top-estimates-132200272.html)
- Q3 2026 consensus: MarketBeat EPS $1.79 / revenue $846.3M (fetched 2026-09-28) versus pre-Q2 Zacks $1.61 / $842.9M. Conflict: MarketBeat's figure is newer but its history table contains at least one error (Q3 2025 revenue shown as $521.7M vs $706.3M filed); treat Q3 EPS consensus as "$1.6-1.8, unverified". Revenue consensus ($843-846M) sits at or just above the top of the dollarised guide. — [MarketBeat earnings](https://www.marketbeat.com/stocks/NASDAQ/PODD/earnings/)
- Short interest 5.08M shares / 7.4% of float at the Sept 15 settlement (tripled in 12 months). — comparison notes, [MarketBeat short interest](https://www.marketbeat.com/stocks/NASDAQ/PODD/short-interest/); not re-checked today.

## 7. Competition and catalysts (dated)

- Tandem Mobi tubeless: 510(k) filing planned Q2 2026, clearance targeted H2 2026, phased launch. No clearance announcement found as of 2026-09-28. — [MedTech Dive](https://www.medtechdive.com/news/tandem-to-file-tubeless-insulin-pump-with-fda-this-quarter/819722/); [Drug Delivery Business](https://www.drugdeliverybusiness.com/tandem-q1-2026-beats-reaffirms-guidance/)
- Beta Bionics Mint: cleared 2026-09-14; full launch Q1 2027. — MedTech Dive (above)
- MiniMed Fit: submitted to FDA Sept 2026, US launch expected summer 2027. — [MedTech Dive](https://www.medtechdive.com/news/minimed-submits-new-patch-pump-for-fda-clearance/829313/) (comparison notes; not re-fetched)
- Omnipod 6: 2026 filing / 2027 launch plan; filing status not confirmed. Type 2 fully closed loop: EVOLVE pivotal enrolling, 510(k) 2027, launch 2028.
- CMS DMEPOS competitive bidding incl. pumps and CGMs: bid window late 2026, contracts 2027, effective no later than 2028-01-01; Insulet says Omnipod "may not qualify" (pharmacy channel). — [MedTech Dive](https://www.medtechdive.com/news/cms-final-rule-diabetes-competitive-bidding/806719/)
- Q3 2026 report: date not announced by Insulet as of 2026-09-28 (no release found). Third-party estimates Oct 29 (Investing.com) or Nov 5 (MarketBeat, "estimated"); prior Q3 reports Nov 2, 2023, Nov 7, 2024, Nov 6, 2025; 2026's Q1/Q2 came 2 days earlier than 2025's. Q4 2026 / FY2027 guide expected mid-to-late February 2027 (Feb 18 in 2026).
- EOFlow: Insulet's petition for rehearing (filed 2026-07-29) pending; partial stay keeps the injunction in Korea/EU/Gulf. — comparison notes ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/06/divided-federal-circuit-panel-nixes-452-million-trade-secret-judgment))

## 8. Guide-cut proxy arithmetic (rule mechanics, derived)

- Entry TTM EPS $5.33, trigger $4.53: the trailing four quarters are Q3'25 $1.24, Q4'25 $1.44, Q1'26 $1.30, Q2'26 $1.37 (GAAP). To print ≤ $4.53, the replacing quarters must fall a cumulative ~$0.80 below their year-ago GAAP EPS before 2027-09-28 (the last filing inside the window is Q2 2027, due ~early Aug 2027).
- Q3 2026 GAAP EPS would have to be ≤ ~$0.44 (vs consensus adjusted $1.6-1.8) to trip it alone. Realistic paths are a large one-off (third correction, litigation settlement, impairment) or a sustained operating miss across three quarters; an ordinary mid-teens-growth year keeps TTM EPS rising.
- Remaining MDC cost ($23-33M, mostly 2026) depresses GAAP by roughly $0.25-0.40/share in total — not enough on its own.

## 9. Scenario inputs (thesis section 5, derived)

- FY2026 base revenue $3.25-3.31B (guide/consensus). Growth paths FY27-29: bear 7/6/5%, base 13/12/11%, bull 16/15/14%. Adjusted operating margin FY2029: 16.5% / 21.5% / 23%. Net income = EBIT x 0.76-0.77 (≈20% tax plus small net interest; consensus FY2028 implies 0.75). Diluted shares 70.0M / 68.5M / 67.0M (bear: SBC dilution, no buyback; base: ~$150M/yr buyback; bull: ~$300M/yr). Multiples on FY2029 EPS: 13x / 18x / 24x.
- Results: bear FY29 revenue $3.87B, EPS $6.93, $90; base $4.62B, $11.02, $198; bull $5.03B, $13.31, $319. Weights 30/50/20 → $190 (+40%, 11.8%/yr). Net cash per share not added (base ~$1.0B ≈ $15/share).
- Reverse: with a 10%/yr hurdle ($181 in Sept 2029), FY2029 EPS needed = $12.08 at 15x, $10.07 at 18x, $8.63 at 21x → revenue CAGR FY26-29 of 15.6% / 8.7% / 3.3% on the ~100 bp/yr margin plan (EPS CAGR from $6.50: 22.9% / 15.7% / 9.9%).
- FCF path used for net cash: FY26 $340-370M (guided "down modestly" from $377.7M), FY27 ~$494M and FY28 ~$615M (MarketScreener consensus), FY29 ~$700M (my assumption).

## 10. Open questions no source closed

1. Type 2 retention and active-user numbers: Insulet discloses neither; sell-side attrition estimates (17.5% blended US, Wells Fargo; 20-50% Type 2) are unverified models.
2. Q3 2026 report date (not announced) and a clean post-Q2 Q3 EPS consensus (MarketBeat $1.79 vs older Zacks $1.61).
3. FY2027 consensus EPS vintage: $7.71 vs $7.63; FY2028/29 consensus not available free (MarketScreener FY2028 vintage unclear); no FY2029 consensus found.
4. The numeric leverage ratio in the springing revolver covenant, and whether the 35% utilisation trigger was changed by the Ninth Amendment (Exhibit 10.1 not read).
5. Gap between the 10-Q "net charge $41.0M" and the 8-K MDC adjustment of $36.7M for H1 2026.
6. Omnipod 6 FDA submission status; Tandem Mobi tubeless clearance date.
7. Whether a lead plaintiff has been appointed in Hu v. Insulet and whether a second suit covering the Aug 5, 2026 drop exists (none found).
8. Current S&P/Moody's outlooks after the guide cut.
9. Dexcom vs Abbott sensor split on Omnipod 5 (undisclosed; matters for the DXCM interaction).
10. How much of the Type 2 churn is recall-related (onboarding window overlapped the March-May corrections); management did not attribute it.
