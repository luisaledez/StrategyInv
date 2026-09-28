# APPF (AppFolio) — working notes for the turnaround v3 thesis, 2026-09-28

Research date 2026-09-28 (before the open). All returns are from the Friday 2026-09-25 close of $204.22 (last bar in `turnaround/cache/prices/APPF.csv`). Thesis file: `turnaround_backtest_v3/thesis/APPF.md`. Primary documents: the Q3 2024 to Q2 2026 earnings-release exhibits (8-K Ex. 99.1), the Q2 2026 10-Q, the FY2025 10-K (PDF from EDGAR, parsed locally), the 2025-09-30 credit-agreement 8-K and the 2025-11-18 investor-meeting 8-K. Consensus, price targets and ratings are third-party and labelled as such. Research tooling, not investment advice.

## 1. Local cache (point-in-time SEC data)

Source: `turnaround/cache/edgar/APPF.json` (fetched 2026-09-27), `fundamentals/APPF.json`, `valuation/APPF.json` (fetched 2026-09-14), `prices/APPF.csv`.

| Quarter end | TTM revenue $M | TTM net income $M | TTM operating income $M | TTM EPS (GAAP) | Cash $M | Diluted shares M | Available |
|---|---|---|---|---|---|---|---|
| 2024-06-30 | 722.1 | 125.0 | 98.3 | 3.45 | 59.6 | 36.24 | 2024-07-26 |
| 2024-09-30 | 762.4 | 131.6 | 140.9 | 3.61 | 62.4 | 36.45 | 2024-10-25 |
| 2024-12-31 | 794.2 | 204.1 | 135.6 | 5.55 | 42.5 | 36.77 | 2025-02-06 |
| 2025-03-31 | 824.5 | 196.8 | 135.3 | 5.36 | 56.9 | 36.71 | 2025-04-24 |
| 2025-06-30 | 862.7 | 203.1 | 139.8 | 5.54 | 73.5 | 36.66 | 2025-07-31 |
| 2025-09-30 | 906.3 | 203.7 | 132.3 | 5.57 | 76.1 | 36.58 | 2025-10-30 |
| 2025-12-31 | 950.8 | 140.9 | 152.9 | 3.88 | 107.0 | 36.32 | 2026-02-05 |
| 2026-03-31 | 995.3 | 152.0 | 169.9 | 4.20 | 147.4 | 36.18 | 2026-04-23 |
| 2026-06-30 | 1,040.9 | 157.5 | 182.3 | 4.39 | 217.4 | 35.88 | 2026-07-23 |

- No borrowings in any quarter (EDGAR debt 0). The fundamentals cache's "total debt $35.8M" is the operating-lease liability ($5.1M current, $30.7M non-current), not borrowings.
- TTM net income exceeded TTM operating income from 2024-12-31 to 2025-09-30 (the Q4 2024 tax benefit, below). It fell back below operating income at 2025-12-31 when that quarter left the trailing year. At 2026-06-30 the ratio is 0.86 (the v3 one-off guard passes).
- Fundamentals cache (balance sheet 2026-06-30): cash and current investments $221.7M; OCF TTM $272.9M, capex TTM $7.4M, FCF TTM $265.5M; buybacks TTM $125.0M; EBITDA TTM $205.2M, EBIT TTM $182.3M; EV $7.05B; market cap $7.23B at $204.22 (35.42M shares out).
- Fundamentals cache label: "EPS growth YoY (TTM) -30.1%" in thesis section 1 is on a fiscal-year basis (FY2025 $3.88 vs FY2024 $5.55), not TTM. The TTM-to-TTM figure is -21% (4.39 vs 5.54). Both are driven by the same tax item. Section 1 was left unchanged because the number is correct on its stated basis.

### Price legs (cache closes; SPY and XLK caches end 2026-09-14)

| Leg | APPF | SPY | XLK | INTU | NOW | Company event in window |
|---|---|---|---|---|---|---|
| 2025-08-04 high $321.25 → 2025-09-26 $278.53 | -13.3% | +4.9% | +6.3% | -11.0% | +1.4% | High came one day after the Q2 2025 report (+19.4% on 2025-08-01). Gave back most of the gap by 2025-08-15 ($265.3). No company news found |
| 2025-09-26 → 2025-10-10 $224.87 | -19.3% | -1.3% | -0.2% | -8.1% | -5.1% | 2025-10-01 -6.9%, then down every day to 10-10. The only filing in the window is the 2025-09-30 credit-facility 8-K. **No source found for the cause** |
| 2025-10-10 → 2025-11-03 $262.26 | +16.6% | +4.6% | +8.4% | +5.4% | +2.8% | Q3 2025 report 2025-10-30: revenue guide raised, margin guide cut; +7.9% on 10-31 |
| 2025-11-03 → 2025-12-31 $232.65 | -11.3% | -0.2% | -4.6% | -2.0% | -16.2% | Investor meeting 2025-11-18. Stock fell 11-17 (-3.9%), 11-18 (-4.3%) and 11-19 (-2.8%). No reaction coverage found, so the causal link is unverified |
| 2025-12-31 → 2026-01-28 $218.00 | -6.3% | +2.0% | +3.7% | -18.7% | -15.4% | Software sell-off after Anthropic's Claude Cowork launch (2026-01-12, per DeepLearning.AI) |
| 2026-01-28 → 2026-02-05 $177.36 | -18.6% | -2.6% | -9.1% | -19.3% | -20.8% | 01-29 -5.0% (before the release, sector day). Q4 2025 report after the close on 01-29, with FY2026 guide $1.10-1.12B vs $1.13B consensus: 01-30 -8.3%. 02-03 -5.7% (Claude Cowork plugins "SaaSpocalypse" day) |
| 2026-02-05 → 2026-04-10 $143.34 (low close; intraday low $142.73) | -19.2% | +0.3% | +5.2% | -19.3% | -19.1% | No company event. Sector de-rating: IGV down 23-24% year to date |
| **Peak → 2026-04-10** | **-55.4%** | +7.7% | +8.7% | -55.3% | -55.0% | APPF, INTU and NOW fell almost exactly the same amount |
| 2026-04-10 → 2026-07-31 $180.19 | +25.7% | +9.9% | +22.9% | -9.9% | +34.0% | Q1 2026 beat and raise 04-23: 04-24 +11.2%. Q2 2026 07-23: 07-24 +0.7% |
| 2026-07-31 → 2026-08-31 $234.21 | +30.0% | +2.7% | +6.4% | +13.7% | +33.0% | Software rebound (NOW +33% in the same month). No APPF-specific catalyst found |
| 2026-08-31 → 2026-09-25 $204.22 | -12.8% | -0.8%* | -1.2%* | -23.2% | -8.4% | KeyBanc PT $255 → $280 on 09-17. Zacks Strong Buy → Hold on 09-23 (MarketBeat). *SPY/XLK to 09-14 only |
| Peak → 2026-09-25 | -36.4% | +20.5%* | +40.5%* | -64.9% | -26.5% | |

## 2. Quarterly revenue, EPS, guidance (8-K Ex. 99.1 unless noted)

Revenue in $M; "Sub" = Core Solutions (renamed Subscription Services in the FY2025 10-K); VAS = Value Added Services; units in millions. GAAP EPS is diluted. The day-after move is from the price cache (every release was after the close).

| Quarter (release date) | Revenue (y/y) | Sub / VAS | Units | GAAP op inc (margin) | GAAP EPS | Non-GAAP EPS (consensus, 3rd party) | FY guidance after the release: revenue / non-GAAP op margin | Next-day move |
|---|---|---|---|---|---|---|---|---|
| Q3 2024 (2024-10-24) | 205.7 (+24%) | 46.0 / 157.7 | 8.5 | 42.6 (20.7%) | 0.90 | 1.29 | FY24 $786-790M / 24.5-25.5% | +10.6% |
| Q4 2024 (2025-01-30) | 203.7 (+19%) | n/c | 8.7 | 23.0 (11.3%) | **2.79** (tax benefit $75.6M) | 0.92 | FY25 $920-940M / 24.5-26.5% | -7.8% |
| Q1 2025 (2025-04-24) | 217.7 (+16%) | 49.5 / 164.7 | 8.8 | 33.8 (15.5%) | 0.86 | 1.21 (1.23) | unchanged $920-940M / 24.5-26.5%; $300M buyback; $75M Second Nature stake | -18.2% |
| Q2 2025 (2025-07-31) | 235.6 (+19%) | 52.5 / 180.1 | 8.9 | 40.5 (17.2%) | 0.99 | 1.38 | raised to $935-945M / 24.5-26.5% | +19.4% |
| Q3 2025 (2025-10-30) | 249.4 (+21%) | 53.8 / 192.1 | 9.1 | 35.0 (14.1%) | 0.93 | 1.31 (1.46) | raised to $945-950M / **cut to 23.5-24.5%** | +7.9% |
| Q4 2025 (2026-01-29) | 248.2 (+22%) | 55.7 / 184.6 | 9.4 | 43.6 (17.6%) | 1.10 | 1.39 (1.25) | FY26 $1,100-1,120M (consensus $1.13B) / 25.5-27.5% | -8.3% |
| Q1 2026 (2026-04-23) | 262.2 (+20%) | 58.2 / 201.4 | 9.5 | 50.7 (19.4%) | 1.18 | 1.61 (1.44-1.50) | raised to $1,110-1,125M / 26.0-28.0% | +11.2% |
| Q2 2026 (2026-07-23) | 281.1 (+19%) | 59.8 / 219.5 | 9.6 | 52.9 (18.8%) | 1.17 | 1.71 (n/f) | raised to $1,117-1,127M / 26.5-28.0% | +0.7% |

n/c = not collected; n/f = no source found. Q4 2025 GAAP operating income is derived: FY2025 $152.9M less Q1-Q3.

Sources:
- Q3 2024: https://www.sec.gov/Archives/edgar/data/1433195/000143319524000125/appfq32024exhibit991.htm
- Q4 2024: https://www.sec.gov/Archives/edgar/data/1433195/000143319525000005/appfq42024exhibit991.htm (Q4 2024 tax provision -$75.6M; net income $102.7M; the company cites a valuation-allowance release of about $76.9M of deferred tax benefit)
- Q1 2025: https://www.sec.gov/Archives/edgar/data/1433195/000143319525000053/appfq12025exhibit991.htm. Consensus and reaction from https://in.investing.com/news/transcripts/earnings-call-transcript-appfolio-q1-2025-earnings-miss-stock-falls-93CH-4791397. Cost of revenue rose to 36% of revenue from 34% (payment-processing fee changes and mix).
- Q2 2025: https://www.sec.gov/Archives/edgar/data/1433195/000143319525000103/appfq22025exhibit991.htm ("96% of customers having used one or more AI-powered solutions")
- Q3 2025: https://www.sec.gov/Archives/edgar/data/1433195/000143319525000140/appfq32025exhibit991.htm. Consensus from https://www.investing.com/news/transcripts/earnings-call-transcript-appfolio-q3-2025-revenue-rises-eps-falls-short-93CH-4322104. Margin drivers named in the call coverage: bonus-plan over-attainment, AI data-center expense, sales capacity, new products, revenue mix. Conflict: Investing.com says the stock "closed down 1.2% at $238.67". In the cache $238.67 is the 10-29 close and 10-30 closed at $235.71 (-1.2%); the post-release session (10-31) was +7.9%. I use the cache.
- Q4 2025: https://www.sec.gov/Archives/edgar/data/1433195/000143319526000006/appfq42025exhibit991.htm (8-K filed 2026-01-29, per the EDGAR index). Consensus from https://www.investing.com/news/earnings/appfolio-shares-slip-over-4-as-2026-revenue-guidance-disappoints-despite-strong-q4-results-93CH-4474642. Call: https://www.investing.com/news/transcripts/earnings-call-transcript-appfolio-q4-2025-beats-forecasts-stock-dips-93CH-4474883 ($15M of 2025 bonus over-attainment = 1.6% of revenue; premium tiers above 25%; data-center spend up for AI). Conflict: that transcript article puts the after-hours price at $217.50, which does not fit the $207.10 close on 01-29 in the cache. The cache is preferred.
- Q1 2026: https://www.sec.gov/Archives/edgar/data/0001433195/000143319526000021/appfq12026exhibit991.htm. Consensus range from search snippets (Investing.com / Quiver): $1.44 / $1.47 / $1.50 EPS, $258.08M revenue.
- Q2 2026: https://www.sec.gov/Archives/edgar/data/0001433195/000143319526000056/appfq22026exhibit991.htm. Revenue consensus $277.26M from https://www.investing.com/news/transcripts/earnings-call-transcript-appfolio-tops-revenue-view-in-q2-2026-shares-flat-93CH-4810150. Call highlights: https://finance.yahoo.com/markets/stocks/articles/appfolio-q2-earnings-call-highlights-220616842.html ("nearly 1 in 3" units on a premium tier; 22,751 customers +6%; Leasing Performer in about half of completed showings where deployed).

## 3. EPS base and headline adjustments

- **Tax item (verified).** Q4 2024 had an income-tax benefit of $75.6M on about $27M of pre-tax income, so Q4 2024 EPS was $2.79 against non-GAAP $0.92. FY2024 tax was a $53.7M benefit, "primarily due to the release of our valuation allowance" at 2024-12-31 (FY2025 10-K; FY2024 effective tax rate -35.8%). That quarter sat in TTM EPS from 2024-12-31 to 2025-09-30 (5.55 / 5.36 / 5.54 / 5.57) and left at 2025-12-31 (3.88). The screen report's reading is correct.
- **Clean comparison (my arithmetic).** Taxing Q4 2024 at about 21% gives roughly $0.58 instead of $2.79. That puts tax-adjusted TTM EPS at about $3.33 at 2025-06-30 and $3.36 at 2025-09-30. On that basis the $4.39 entry base is about +32% y/y, not -21%. TTM GAAP operating income is +30% y/y ($182.3M vs $139.8M).
- **Tax-rate normalization is a headwind still inside the base.** FY2025 effective tax rate was 12.5% (lower excess stock-comp benefits and R&D credits than 2024, but still low). Q3 2025 tax was $3.1M on about $36.7M pre-tax, roughly 8%. H1 2026 ETR was 21.9% and Q2 2026 23.7% (10-Q). The low-tax Q3 and Q4 2025 quarters ($0.93 and $1.10) roll out of the TTM in the next two reports. A 23% ETR quarter needs about $51M of pre-tax income to match Q4 2025's $1.10; Q2 2026 pre-tax was $54.4M. So TTM EPS should rise at the Q3 report and be roughly flat at the Q4 report (my estimate, not guidance).
- **Stock comp.** $70.8M in FY2025 (7.4% of revenue; 7.6% in 2024) and $38.5M in H1 2026. Net-share-settlement tax withholding was $43.2M in 2025. Unrecognized RSU expense is $143.3M over 2.5 years (10-Q). The gap between non-GAAP and GAAP operating margin is about 8 points.
- **Working capital.** Accrued bonuses were $43.3M at 2025-12-31 vs $17.1M a year earlier, after a switch from semi-annual to annual payment (10-K). That flattered 2025 OCF and was paid in Q1 2026 (Q1 2026 OCF $34.3M, 13.1% of revenue). TTM FCF at 2026-06-30 ($265.5M) contains both effects. FY2025 FCF = OCF $242.1M − capex $3.2M − capitalized software $3.4M = $235.5M (10-K cash-flow statement; Motley Fool cites $236M).
- **Acquisitions and investments.** LiveEasy (Move EZ) was bought 2024-10-22 for $78.5M cash. It is small against about $1B revenue, and the acquisition guard passes (shares -2.1% y/y). In April 2025 AppFolio paid $75.0M cash for a minority stake in Second Nature Holdings (resident-benefits provider). It is carried at cost under the measurement alternative with no gains or losses through 2025 (10-K Note 4). Long-term investments were $77.7M at 2026-03-31 and $87.7M at 2026-06-30. **The +$10M in Q2 2026 is not explained in the sources read (open question).** An impairment would be a GAAP charge below operating income and would hit the TTM EPS the rule tracks.
- **Interest income.** Net interest income was $8.2M in 2025 vs $14.0M in 2024 (sale of AFS securities, lower rates). Six-month 2026 interest income was $3.2M (-27%). Customer funds do not appear as a float line; no source quantifies float income (open question).

## 4. Survival data

- Revolver: $150M senior secured revolving facility with PNC Bank, N.A. (agent), signed 2025-09-30. Sublimits: $25M letters of credit, $25M swingline. Matures 2030-09-30. **Undrawn** at 2025-12-31 and 2026-06-30 (10-K; 10-Q). Pricing: SOFR + 125-200 bp or base + 25-100 bp by net leverage; commitment fee 15-30 bp. Accordion up to the greater of $225M and 100% of consolidated EBITDA, plus more at pro-forma net leverage ≤ 3.25x. Sources: https://www.sec.gov/Archives/edgar/data/1433195/000143319525000134/appf-20250930.htm (8-K) and the credit agreement https://www.sec.gov/Archives/edgar/data/1433195/000143319525000134/pnc-appfolioxcreditagree.htm (not read in full).
- Covenant: maximum Consolidated Net Leverage Ratio of **3.75x** (4.25x during an acquisition step-up period), per the 8-K. With no debt and $222M cash the ratio is below zero. The company was in compliance at 2025-12-31 (10-K). Negative covenants restrict debt, liens, investments, dividends and buybacks, "subject to certain exceptions" (baskets not read).
- Debt maturities next 24 months: none; there are no borrowings.
- Operating leases (10-K Note 9): payments 2026 $6.7M, 2027 $6.8M, 2028 $7.0M, 2029 $6.9M, 2030 $7.1M, thereafter $10.4M; total $44.8M, less $6.7M imputed interest = $38.2M. At 2026-06-30 the liability is $35.8M ($5.1M current).
- Purchase commitments: $31.3M non-cancelable at 2025-12-31, "due primarily over the next three years" (10-K). In January 2026 a cloud-computing commitment of at least $219.3M through 2031, of which $36.2M is short-term (Q2 2026 10-Q). No year-by-year split was found beyond the short-term portion.
- Other: Terra Mar Insurance (captive reinsurer of landlord-liability policies) carried a $6.6M claims reserve and $7.8M collateral deposits at 2025-12-31 (10-K).
- Capital return: 2025 program of $300M authorized 2025-04-23; $125M remaining at 2026-06-30. Q1 2026 bought 702,502 shares at $177.95 average ($125M) (10-Q).
- 10-Q: https://www.sec.gov/Archives/edgar/data/0001433195/000143319526000058/appf-20260630.htm. 10-K (HTML): https://www.sec.gov/Archives/edgar/data/1433195/000143319526000011/appf-20251231.htm; PDF parsed locally: https://www.sec.gov/Archives/edgar/data/1433195/000143319526000032/appf12312510-k.pdf

## 5. Business facts used in the thesis

- FY2025 revenue $950.8M: Subscription Services $211.5M (+17%), Value Added Services $721.5M (+19%), Other $17.8M (+108%). VAS growth came from "electronic payment, tenant screening, and risk mitigation services". Units under management +8%. Customers 22,096; employees 1,702. RPO $93.9M, which "grew significantly during 2025 as we began selling more multi-year revenue contracts". Class A 24.33M and Class B 11.66M shares at 2026-01-29 (dual class; voting terms not read). — FY2025 10-K.
- Pricing is per unit and per transaction (payments, screening, insurance), not per seat. VAS was 78% of Q2 2026 revenue ($219.5M of $281.1M; 8-K). VAS per unit rose about 13% y/y in Q2 2026 (VAS +21.8%, units +8%; my arithmetic).
- Investor meeting 2025-11-18 (8-K): premium tiers (Plus/Max) 25% of units YTD 2025 vs 10% in 2022; ARPU $103 YTD 2025 (+12%); 15M+ automated actions in 2025; no multi-year revenue or margin target was given. https://www.sec.gov/Archives/edgar/data/1433195/000143319525000145/appfolioinvestormeeting2.htm
- Premium tiers reached "nearly 1 in 3" units at Q2 2026 (Yahoo call highlights, above; Investing.com says "from 25% to nearly 33%").
- Competition (10-K): vertical real-estate software providers, horizontal business-software providers and point solutions. No competitor is named in the text read; Yardi, RealPage, Entrata and others are industry knowledge, not from a source read here.
- Legal and regulatory: the 2020/2021 FTC FCRA settlement ($4.25M; ongoing compliance and reporting obligations), https://www.ftc.gov/news-events/news/press-releases/2020/12/tenant-background-report-provider-settles-ftc-allegations-it-failed-follow-accuracy-requirements. The 10-K risk factor notes algorithmic pricing tools "have been subject to antitrust challenges" and that AppFolio "may face similar challenges". No pending material case is named; the 10-Q says no proceeding would be material.

## 6. Sector and analyst context (third party)

- Software AI de-rating: Claude Cowork (2026-01-12) and plugins (2026-01-30; 2026-02-03 sell-off) — https://www.deeplearning.ai/the-batch/claude-cowork-plugins-trigger-a-saas-stock-selloff-but-partnerships-lead-to-slight-rebound, https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html. S&P Software & Services -25% between 2026-01-12 and 02-23 (DeepLearning.AI).
- Motley Fool 2026-03-03: -18.5% after the Q4 report; IGV down more than 24% in early 2026; about 24x trailing FCF and 5.3x forward sales at $199.43. https://www.fool.com/investing/2026/03/03/appfolio-grew-free-cash-flow-30-in-2025/
- 2026-01-30 target cuts (Investing.com; MarketBeat): DA Davidson $325 → $275 ("weaker than expected value-added services revenue and conservative 2026 guidance"); Piper Sandler $350 → $245; KeyBanc $270 → $255; JPMorgan $330 → $300; KBW $311 → $290. https://www.investing.com/news/analyst-ratings/da-davidson-lowers-appfolio-stock-price-target-on-weaker-services-revenue-93CH-4476548, https://www.marketbeat.com/stocks/NASDAQ/APPF/forecast/
- 2026-04-24: Piper $245 → $210, UBS $210, Benchmark $222 → $226. 2026-07-22 Guggenheim initiates Buy at $232. 2026-09-17 KeyBanc $255 → $280 (Overweight; resident services "could become a meaningful driver of average revenue per user"; valued at 7.5x 2027 EV/sales and 27x EV/FCF). https://finance.yahoo.com/markets/stocks/articles/keybanc-raises-appfolio-appf-price-213318180.html
- Conflict: one search summary put a Piper Sandler upgrade to Overweight ($240 → $350) and a DA Davidson $350 target in "early August 2026". The $350 levels match mid-2025 targets (Piper cut from $350 in January 2026), so this is most likely a misdated 2025 action. Not used.
- Consensus (stockanalysis.com, 2026-09-28; third party): FY2026 revenue $1.12B (+18.2%), EPS $6.90 (+30.4%, non-GAAP basis); FY2027 revenue $1.32B (+17.5%), EPS $8.43 (+22.2%). 10 analysts; average PT $234.16 (low $200, high $280). The fundamentals cache's forward EPS $8.43 is this FY2027 non-GAAP figure, so the "P/E forward 24.2" in thesis section 1 is on non-GAAP FY2027. https://stockanalysis.com/stocks/appf/forecast/
- MarketBeat consensus PT $246.63, 1 Strong Buy / 9 Buy / 2 Hold (different panel; third party).

## 7. Scenario arithmetic (thesis section 5)

Yr 3 = trailing year to 2029-09-30 = FY2028 × (1 + FY2029 growth)^0.75. Start from the FY2026 guide midpoint of $1.122B.

| | Growth 2027/28/29 | Rev TTM Sep-2029 | GAAP EBIT margin | EBIT $M | EV/EBIT | Net cash | Shares | Price | Implied EV/S | Implied GAAP P/E |
|---|---|---|---|---|---|---|---|---|---|---|
| Bear | 14% / 10% / 7% | $1.48B | 18% | 266 | 18x | $0.50B | 35.5M | $149 | 3.2 | 25 |
| Base | 17.5% / 16% / 14% | $1.69B | 23% | 388 | 26x | $0.45B | 34.5M | $305 | 6.0 | 34 |
| Bull | 19% / 18% / 17% | $1.77B | 28% | 496 | 30x | $0.40B | 33.5M | $456 | 8.4 | 39 |

- Weights 30/50/20 give $289 (+41% over 3 years, about 12.2% a year).
- Reverse test (23% GAAP EBIT margin, $0.45B net cash, 34.5M shares, from TTM revenue of $1.041B). A 10% a year return needs a revenue CAGR of about 12.8% at a 26x exit or 19.2% at 22x. A flat price needs about 7.8% at 22x.
- Net cash in yr 3 assumes most FCF goes to buybacks. This is an assumption, not a company target.

## 8. Catalysts and dates

- Q3 2026 results: date not announced in any source found (2026-09-28). Precedent is late October: Q3 2024 on 2024-10-24 and Q3 2025 on 2025-10-30.
- Q4 2026 results and FY2027 guidance: expected late January 2027 (precedents 2025-01-30 and 2026-01-29). Unconfirmed.
- Investor meeting: 2025 was 2025-11-18; no 2026 date found.
- No scheduled regulatory decision or litigation milestone found.

## 9. Open questions no source could close

1. Cause of the -19% leg from 2025-09-26 to 2025-10-10 (2025-10-01 -6.9%): no downgrade, news or filing found beyond the credit-facility 8-K.
2. Whether the 2025-11-18 investor meeting caused the 11-17 to 11-19 decline (-10.6%): no reaction coverage found.
3. What drove the August 2026 rally (+30%) beyond the software rebound: no company catalyst found.
4. The +$10M rise in long-term investments in Q2 2026 (new strategic investment?) and the current carrying value and health of the Second Nature stake.
5. Premium-tier share of units as an exact number for Q1 and Q2 2026 (only "nearly 1 in 3"); ARPU for 2026.
6. Size of interest or float income on customer payment flows, if any.
7. The Q3 2026 earnings date.
8. Year-by-year split of the $219.3M cloud commitment beyond the $36.2M short-term portion.
9. Class B voting rights and insider ownership (not read).
10. Q2 2026 non-GAAP EPS consensus (only the revenue consensus was found).
