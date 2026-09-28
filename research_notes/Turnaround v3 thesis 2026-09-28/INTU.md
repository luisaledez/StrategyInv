# INTU (Intuit) — working notes for the turnaround v3 thesis, 2026-09-28

Research pass for `turnaround_backtest_v3/thesis/INTU.md`. Research done 2026-09-28 (before the open). Price data: local Yahoo cache `turnaround/cache/prices/INTU.csv` through the 2026-09-25 close ($275.79); closes quoted below are from that cache unless a source is named. SEC figures: FY2026 10-K (fiscal year ended 2026-07-31) and 8-K earnings releases; point-in-time TTM from `turnaround/cache/edgar/INTU.json`. Consensus and analyst actions are third-party and labelled as such. Not investment advice.

## Primary documents used

- FY2026 10-K (filed 2026-09, EDGAR cache shows it available 2026-09-09): https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000037/intu-20260731.htm
- Q4 FY26 release (2026-08-25, 4:00pm EDT): https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000029/fy26q4earningspressrelease.htm ; IR copy: https://investors.intuit.com/news-events/press-releases/detail/1320/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance
- Q3 FY26 release (2026-05-20): https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000024/fy26q3earningspressrelease.htm
- Q2 FY26 release (2026-02-26): https://www.sec.gov/Archives/edgar/data/896878/000089687826000012/fy26q2earningspressrelease.htm
- Q1 FY26 release (2025-11-20): https://www.sec.gov/Archives/edgar/data/896878/000089687825000046/fy26q1earningspressrelease.htm
- Q4 FY25 release (2025-08-21): https://www.sec.gov/Archives/edgar/data/896878/000089687825000031/fy25q4earningspressrelease.htm
- Q3 FY25 release (2025-05-22): https://www.sec.gov/Archives/edgar/data/896878/000089687825000020/fy25q3earningspressrelease.htm
- Investor Day release (2026-09-17, reaffirms Q1 and FY27 guidance): https://investors.intuit.com/news-events/press-releases/detail/1323/intuit-hosts-investor-day-reaffirms-first-quarter-and-fiscal-2027-guidance
- Anthropic partnership release (2026-02-24): https://investors.intuit.com/news-events/press-releases/detail/1305/intuit-and-anthropic-partner-to-bring-trusted-financial-intelligence-and-custom-ai-agents-to-consumers-and-businesses
- OpenAI partnership release (2025-11-18): https://investors.intuit.com/news-events/press-releases/detail/1284/intuit-and-openai-join-forces-to-revolutionize-financial-intelligence-powering-every-person-business-and-dream-with-personalized-experiences
- Call transcripts (third-party transcription): Q4 FY26 https://www.fool.com/earnings/call-transcripts/2026/09/01/intuit-intu-q4-2026-earnings-call-transcript/ ; Q3 FY26 https://www.fool.com/earnings/call-transcripts/2026/05/20/intuit-intu-q3-2026-earnings-transcript/

## Quarterly table (revenue / EPS / guidance)

Revenue and EPS as reported in the releases above (GAAP diluted; non-GAAP on the old definition that excluded share-based comp). Q3 FY25 revenue $7,754M is derived from EDGAR TTM differences and matches the release's "$7.8 billion".

| Quarter (end) | Released | Revenue $M | y/y | GAAP EPS | Non-GAAP EPS | Guidance given at this print | Source |
|---|---|---|---|---|---|---|---|
| Q4 FY24 (2024-07-31) | 2024-08 | 3,184 | | (0.07) | 1.99 | — | FY25 Q4 release comparatives |
| Q1 FY25 (2024-10-31) | 2024-11 | 3,283 | | 0.70 | 2.50 | — | FY26 Q1 release comparatives |
| Q2 FY25 (2025-01-31) | 2025-02 | 3,963 | | 1.67 | 3.32 | — | FY26 Q2 release comparatives |
| Q3 FY25 (2025-04-30) | 2025-05-22 | 7,754 | +15% | 10.02 | 11.65 | raised all FY25 company metrics | FY25 Q3 release |
| Q4 FY25 (2025-07-31) | 2025-08-21 | 3,831 | +20% | 1.35 | 2.75 | FY26: revenue $20.997-21.186B (+12-13%), GAAP EPS $15.49-15.69, non-GAAP $22.98-23.18; GBS +14-15%, Consumer +8-9% (TurboTax +8%, Credit Karma +10-13%, ProTax +2-3%); Q1: revenue +14-15%, GAAP EPS $1.19-1.26, non-GAAP $3.05-3.12 | FY25 Q4 release |
| Q1 FY26 (2025-10-31) | 2025-11-20 | 3,885 | +18% | 1.59 | 3.34 | FY26 reiterated; Q2: revenue +14-15%, GAAP $1.76-1.81, non-GAAP $3.63-3.68 | FY26 Q1 release |
| Q2 FY26 (2026-01-31) | 2026-02-26 | 4,651 | +17% | 2.48 | 4.15 | FY26 reiterated; Q3: revenue ~+10%, GAAP $10.56-10.62, non-GAAP $12.45-12.51 | FY26 Q2 release |
| Q3 FY26 (2026-04-30) | 2026-05-20 | 8,558 | +10% | 11.09 | 12.80 | FY26 revenue raised to $21.341-21.374B (+13-14%), non-GAAP EPS $23.80-23.85; TurboTax cut to $5.277-5.282B (from $5.305-5.330B, per investinglive); Q4: revenue +11-12%, non-GAAP $3.56-3.62; 17% workforce cut, $300-340M charge | FY26 Q3 release |
| Q4 FY26 (2026-07-31) | 2026-08-25 | 4,354 | +14% | 1.34 | 4.03 | FY27: revenue $23.279-23.512B (+9-10%), GAAP op income $7.408-7.490B, GAAP EPS $20.12-20.36 (+22-24%), non-GAAP (now incl. SBC) $22.88-23.12 (+23-24%); GBS $13.068-13.158B (+13-14%), Consumer $8.955-9.088B (+4-6%), TurboTax $5.377-5.453B (+2-3%), Credit Karma $2.919-2.973B (+11-13%), ProTax $659-662M (+2%), Mailchimp $1.256-1.266B (flat to -1%); Q1 FY27: revenue $4.294-4.313B (+11%), GAAP EPS $1.71-1.75, non-GAAP $2.44-2.48 | FY26 Q4 release |

FY totals: FY25 revenue $18,831M, GAAP EPS $13.67, non-GAAP $20.15 (FY25 Q4 release). FY26 revenue $21,448M (+14%), GAAP operating income $5,884M (+20%), GAAP EPS $16.46 (+20%), non-GAAP operating income $8,935M (+18%), non-GAAP EPS $24.27 (+20%) (FY26 Q4 release; 10-K income statement).

Actual vs guidance through FY26: every quarter beat the non-GAAP EPS guide (Q1 3.34 vs 3.05-3.12; Q2 4.15 vs 3.63-3.68; Q3 12.80 vs 12.45-12.51; Q4 4.03 vs 3.56-3.62); FY26 revenue $21.448B beat even the raised $21.341-21.374B. The misses were in units and customers, not in revenue or EPS.

## FY2026 10-K facts (all from the 10-K linked above)

- Segments FY26: GBS revenue $12,864M (FY25 $11,077M), segment operating income $9,887M; Consumer revenue $8,584M (FY25 $7,754M), segment operating income $6,308M. Unallocated: SBC $2,056M, other corporate $7,303M, amortization of acquired technology $174M, other acquired intangibles $485M, restructuring $293M.
- Product lines FY26: QuickBooks Online Accounting $5,051M (+23%); Online Services $4,867M (+16%); Online Ecosystem $9,918M (+19%); QuickBooks Desktop Accounting $1,801M; Desktop Services and Supplies $1,145M; TurboTax $5,296M (+7%); Credit Karma $2,641M (+20%); ProTax $647M (+4%).
- Online Ecosystem paying customers +3% at 2026-07-31; Online Ecosystem ARPC +15% for FY26. QBO growth attributed to "higher effective prices, customer growth, and mix shift". Desktop Ecosystem +6% on higher effective prices.
- TurboTax revenue increase "due to growth in assisted tax and our consumer money offerings, partially offset by ... fewer TurboTax federal units".
- Mailchimp becomes a separate reportable segment from FY27 (managed separately from 2026-08-01).
- Income statement FY26: interest expense $256M; interest and other income $389M (includes $174M net gains on long-term investments per the Q4 release); tax provision $1,451M on pre-tax $6,017M (24.1%; FY25 20.0%). Diluted shares 277M (FY25 283M). Shares outstanding 267,236K at 2026-08-31 (cover page).
- Cash flow FY26: operating cash flow $8,838M "including the impact of lower cash tax payments" (OBBBA R&D expensing); capex $221M; cash taxes paid $281M (FY25 $1,408M, FY24 $1,881M); company expects ~$2B of income tax payments in FY27, mostly in H2. Repurchases $5.5B (13.4M shares); remaining authorization $7.9B (Board added $8.0B on 2026-05-07). Dividends paid $1.3B.
- SBC $2,056M in FY26 (9.6% of revenue).
- Restructuring (2026 Plan, approved May 2026): total cost ~$315M; $293M recorded in FY26 (severance); substantially complete by Q1 FY27. Employees ~18,600 at 2026-07-31. The ~3,000 jobs figure is from press (investinglive, Bloomberg/Reuters), not the 10-K.
- Liquidity: cash, cash equivalents and investments $7.2B (none restricted; ~93% in the U.S.). Short-term debt $1,249M, long-term debt $6,420M; total principal $7,720M = senior notes $6,750M + secured (non-recourse SPV) revolving facilities $970M.
- Senior notes: 5.250% Sep-2026 $750M (repaid August 2026 from the June 2026 issue plus cash); 1.350% Jul-2027 $500M; 5.125% Sep-2028 $750M; 1.650% Jul-2030 $500M; 4.950% Jun-2031 $750M (new); 5.200% Sep-2033 $1,250M; 5.500% Jun-2036 $1,000M (new); 5.500% Sep-2053 $1,250M.
- Principal by fiscal year: FY27 $1,250M; FY28 $400M; FY29 $1,100M; FY30 $720M; FY31 $750M; thereafter $3,500M.
- Unsecured revolver: $2.2B, entered 2026-01-09, expires 2031-01-09, undrawn at 2026-07-31; accordion up to $4B; covenant total gross debt / EBITDA ≤ 4.00x (compliant). Commercial paper program $2.2B, nothing outstanding (temporarily $3.2B during the season, reduced March 2026). A $5.8B short-term facility for the early-refund offering existed 2026-01-30 to 2026-02-26.
- Secured SPV facilities: $1.2B committed, $970M drawn, SOFR+1.10-1.35%, commitment terms April 2027-November 2028, final maturities May 2028-November 2029; non-recourse to Intuit Inc.
- Contractual obligations (<1y / 1-3y / 3-5y / >5y / total, $M): senior notes 1,250 / 750 / 1,250 / 3,500 / 6,750; secured facilities 0 / 750 / 220 / 0 / 970; interest and fees 351 / 590 / 465 / 1,984 / 3,390; operating leases 112 / 264 / 233 / 285 / 894; purchase obligations (mainly cloud) 1,160 / 2,079 / 927 / 768 / 4,934; deferred comp 308 (<1y).
- Legal (Note 13): FTC free-filing matter — Fifth Circuit vacated the FTC order on 2026-03-20 and remanded; FTC did not appeal; Intuit moved on 2026-08-31 to dismiss the remaining FTC suit in N.D. Cal. as moot, FTC not opposing, decision pending. Ontario class action (filed 2022-08-25) certified 2026-07-24; Intuit expects to appeal. Two securities class actions (N.D. Cal., filed 2026-07-10 and 2026-08-17; Sections 10(b)/20(a)); no lead plaintiff appointed at filing; no loss estimate.
- Direct File: 10-K risk factor says "the IRS free direct filing system was suspended" but proponents continue to advocate; IRS Free File continues.

## Guidance changes, FY27 and medium term

- FY27 guidance (2026-08-25, reaffirmed 2026-09-17): see quarterly table. SBC is included in non-GAAP from 2026-08-01; FY27 SBC guided at $2,020M, Q1 FY27 $521M (Investor Day release).
- FY26 non-GAAP EPS on the new (SBC-inclusive) basis: implied ≈ $18.6 by the +23-24% growth on $22.88-23.12 (22.88/1.23 = 18.60; 23.12/1.24 = 18.65), and consistent with $24.27 less ~$5.6 of after-tax SBC per share. A WebFetch summary of the IR release gave $17.05; that does not reconcile and is rejected.
- Medium-term targets (from the Q4 call as transcribed by Motley Fool, not verified against company slides): GBS 10-15% revenue CAGR over three years; Consumer 4-8%; SBC down to 8% of revenue by FY2030; "high-teens" annual non-GAAP EPS growth.
- Q4 call (transcript): "Price is now the #1 reason customers leave TurboTax"; management is "deliberately accepting lower initial DIY tax ARPC"; online paying customers 8.9M, +3% (from +5% a year earlier); QuickBooks Free and Lite launched, >20,000 customers active or converted in the first month; mid-market customers +28% to >145,000; Intuit Enterprise Suite annualized revenue >$145M; desktop ecosystem to decline low single digits in FY27. https://www.fool.com/earnings/call-transcripts/2026/09/01/intuit-intu-q4-2026-earnings-call-transcript/
- Investor Day 2026-09-17 (Yahoo Finance): Intuit missed FY26 new-customer targets in DIY tax and QuickBooks Online; "The number one reason why customers left us was price"; lost share in DIY tax, gained in assisted; lower-cost entry points (QuickBooks Free, Credit Karma Tax, local and partner channels); 70% of code pull requests delivered by AI. https://finance.yahoo.com/technology/ai/articles/intuit-investor-day-puts-ai-210208852.html
- Q3 call (transcript, 2026-05-20): "We lost on price" among filers under $50k; TurboTax Live expected at 53% of TurboTax revenue (+11 pts); assisted customers +38%, revenue +36%; online paying units +2%; ARPU +11%; ~35% of TurboTax customers use money offerings; management said the DIY shortfall "has nothing to do with AI". https://www.fool.com/earnings/call-transcripts/2026/05/20/intuit-intu-q3-2026-earnings-transcript/

## TurboTax units

- FY26 (Q4 FY26 release): desktop 4.1M (-7% from 4.4M), online 34.9M (-2% from 35.5M), total 39.0M (-2% from 39.9M).
- FY25 (Q4 FY25 release, as extracted): desktop 4.3M (-4%), online 34.9M (-1%), total 39.2M (-2%). **Conflict:** the FY26 release shows FY25 at 39.9M / 35.5M / 4.4M. Not reconciled (possible later restatement of season units, or an extraction error in the tool summary). I use the FY26 release comparatives for the y/y read.

## Stock-decline timeline (closes from local cache)

| Date | Close | Day move | Event | Source |
|---|---|---|---|---|
| 2025-07-30 | 807.39 | | 5-year high (intraday high 813.70) | cache |
| 2025-08-11 | 706.09 | -5.7% | no company-specific cause found (MarketBeat notes a 5.1% intraday drop without a cause) | https://www.marketbeat.com/instant-alerts/intuit-nasdaqintu-shares-down-51-heres-why-2025-08-11 |
| 2025-08-22 | 662.66 | -5.0% | Q4 FY25 beat (revenue +20%, non-GAAP EPS $2.75 vs ~$2.66 est.) but FY26 revenue guide +12-13% vs 16% in FY25; Q1 guide +14-15% | https://finance.yahoo.com/news/intuit-stock-tumbles-q4-beat-123704981.html ; FY25 Q4 release |
| 2025-11 | | | IRS tells 25 partner states Direct File "will not be available in Filing Season 2026" | https://www.nextgov.com/digital-government/2025/11/direct-file-wont-happen-2026-irs-tells-states/409309/ ; https://federalnewsnetwork.com/it-modernization/2025/11/irs-direct-file-will-not-be-available-in-2026-agency-tells-states/ |
| 2025-11-18 | | | OpenAI deal, $100M+ for model access; Intuit apps in ChatGPT | https://www.cnbc.com/2025/11/18/intuit-pays-openai-100-million-turbotax-integrates-chatgpt.html |
| 2025-11-21 | 663.15 | +4.0% | Q1 FY26 beat (revenue +18%, non-GAAP $3.34 vs $3.05-3.12 guide), FY reiterated | FY26 Q1 release |
| 2026-01-13/14 | 605.28 / 566.60 | -4.7% / -6.4% | Anthropic Claude Cowork fears; Wells Fargo cut to Equal Weight ($840 to $700); Goldman initiated Neutral $720 | https://www.tikr.com/blog/intuit-stock-drops-6-after-sharp-downgrades-are-we-looking-at-a-difficult-2026 ; https://ts2.tech/en/intuit-stock-slips-again-as-ai-agent-jitters-rattle-turbotax-maker-ahead-of-tax-season/ |
| 2026-01-29 | 502.98 | -6.6% | software rout after Microsoft, ServiceNow and SAP results (press: INTU -7.8% intraday) | https://www.sahmcapital.com/news/content/update-1-us-software-stocks-slump-as-ai-disruption-fears-take-over-2026-01-29 ; https://finance.yahoo.com/news/stock-market-today-jan-29-151254174.html |
| 2026-02-03 | 434.09 | -10.9% | Anthropic Cowork industry plugins trigger ~$285B sector selloff; MarketBeat also flags an analyst downgrade (firm not identified) | https://www.cnn.com/2026/02/04/investing/us-stocks-anthropic-software ; https://www.marketbeat.com/instant-alerts/intuit-nasdaqintu-shares-down-73-on-analyst-downgrade-2026-02-03/ |
| 2026-02-17 | 379.17 | -5.1% | software falls on Anthropic's latest Claude model | https://www.forbes.com/sites/tylerroush/2026/02/17/software-stocks-oracle-intuit-more-fall-as-anthropics-latest-claude-model-fuels-ai-concerns/ |
| 2026-02-24 | 358.71 | | low of the winter leg; Anthropic partnership announced that day | Anthropic partnership release; https://www.cnbc.com/2026/02/24/software-stocks-anthropic-ai.html |
| 2026-02-25 / 26 / 27 | 381.23 / 394.42 / 409.03 | +6.3% / +3.5% / +3.7% | partnership, then Q2 FY26 beat (non-GAAP $4.15 vs $3.63-3.68), FY reiterated | FY26 Q2 release |
| 2026-03-20 | | | Fifth Circuit vacates FTC order | 10-K Note 13 |
| 2026-04-08 / 09 | 389.51 / 361.69 | -5.1% / -7.1% | Anthropic launches: "Managed Agents" (Yahoo/TIKR say -8.3% to -8.5%) and "Claude Mythos" (Reuters, 2026-04-09: INTU among names down 3.7-6.8%). **Sources differ on which launch drove which day.** | https://finance.yahoo.com/markets/stocks/articles/intuit-intu-down-8-5-161621368.html ; https://www.investing.com/news/stock-market-news/us-software-stocks-fall-as-anthropics-new-ai-model-revives-disruption-fears-4606149 |
| 2026-04-23 | 383.30 | -6.2% | software plunges on ServiceNow and IBM results | https://www.cnbc.com/2026/04/23/software-stocks-plunge-on-servicenow-ibm-results-ai-fears-escalate.html |
| 2026-05-21 | 307.07 | -20.0% | Q3 FY26: revenue +10%, TurboTax guide cut, 17% workforce reduction; press: worst decline in more than two decades | FY26 Q3 release; https://investinglive.com/stocks/why-is-intuit-stock-crashing-also-after-its-earnings-last-night-20260521/ ; https://www.benzinga.com/markets/earnings/26/05/52724838/intuit-stock-cracks-after-layoffs-turbotax-warning |
| 2026-06-02 | 322.14 | -8.9% | Goldman Sachs downgrade Neutral to Sell (GenAI-powered lower-priced tax competition; "fundamentals may get worse before they get better"); price target not found | https://www.gurufocus.com/news/8896109/intuit-intu-faces-downgrade-from-goldman-sachs-shares-drop-686?mobile=true ; https://seekingalpha.com/news/4599702-intuit-stock-down-after-goldman-sachs-lowers-recommendation-to-sell-from-neutral |
| 2026-06-25 | 255.07 | | low close of the episode (-68.4% from the high) | cache |
| 2026-07-10 | | | first securities class action filed (N.D. Cal.) | 10-K Note 13 |
| 2026-07-13 | 289.76 | +5.4% | Stifel cut to Hold, target $375 to $275; Redburn target $600 to $540 (Buy kept) — the stock rose with the sector that day | https://stockstotrade.com/news/intuit-inc-intu-news-2026_07_13-2/ |
| July 2026 | 316.07 (Jul 31) | +21.1% for the month | sector rotation into software (WDAY +31%, ADBE +22%, ADSK +20%, CRM +18% in July per Stocktwits) | https://www.gurufocus.com/news/8951715/intuit-intu-rebounds-in-july-after-significant-firsthalf-decline ; https://stocktwits.com/news-articles/markets/equity/wday-adbe-intu-adsk-crm-software-stocks-stage-sharp-rebound-in-july/cZoT3QfRJ5C |
| 2026-08-24 | 369.92 | | top of the rebound (+45% from the June low) | cache |
| 2026-08-26 | 345.88 | -3.2% (opened 323.47, -9.5%) | FY27 guide: revenue +9-10% (midpoint $23.40B) vs ~$23.74B consensus; TurboTax +2-3%, Mailchimp flat to -1%; Q4 non-GAAP $4.03 vs ~$3.59 est. Piper Sandler Underweight, target $250 to $290; Mizuho Outperform, $500 to $430 | https://finance.yahoo.com/markets/stocks/articles/intuit-shares-plunge-cautious-fiscal-104320782.html ; https://www.investing.com/news/earnings/intuit-issues-conservative-fullyear-guidance-amid-strategy-shift-4875875 ; https://finance.yahoo.com/markets/stocks/articles/intuit-crashed-over-agentic-ai-132427512.html |
| 2026-09-17 | 313.13 | | Investor Day: FY27 reaffirmed, no upside surprise | Investor Day release; https://www.quiverquant.com/news/Intuit+Falls+as+Investor+Day+Reaffirmed+a+Slower+Growth+Outlook |
| 2026-09-22 / 24 | 292.35 / 277.13 | -3.9% / -3.4% | no company-specific news found; Goldman reiterated Sell, $304 target (date not verified); sector weak | https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-falls-3-37-percent-ahead-of-the-open/70180700 |
| 2026-09-25 | 275.79 | | screen close | cache |

Peer check from local caches, INTU's high (2025-07-30) to 2026-09-25: INTU -65.8%, ADBE -35.3%, ADSK -32.0%, NOW -30.6%, HRB -23.0%, WDAY -20.3%, CRM -11.6%, SPY +19.9%. From 2026-08-31 to 2026-09-25: INTU -23.2%, ADBE -19.6%, ADSK -19.0%, HRB -18.3%, CRM -9.1%, NOW -8.4%, WDAY -4.1%, SPY -0.8%. June 25 to Aug 31: INTU +40.9%, CRM +71.5%, WDAY +73.6%, NOW +65.3%. Reading: roughly half of INTU's fall is the sector de-rating; the other ~30-45 points of underperformance are company-specific (tax-season and new-customer misses, the FY27 step-down).

## Valuation cache anchors (`turnaround/cache/valuation/INTU.json`, fetched 2026-09-14)

Trailing GAAP P/E snapshots: 64.1 (2025-07-31), 49.9 (2025-10-02), 34.3 (2026-01-31), 25.3 (2026-04-30), 19.3 (2026-07-31), 19.5 (2026-09-11). Full-history (from 2008-10) low 15.7, 5-year median 58.9. Today 16.8 (screen).

## Consensus and analyst views (third-party)

- Yahoo Finance analysis page, viewed 2026-09-28: FY27 (Jul-2027) revenue $23.41B avg (28 analysts, range $23.28-23.54B, +9.1%); FY28 $25.57B (29 analysts, range $24.28-26.64B, +9.2%). EPS ("normalized") FY27 $23.77 (31 analysts, range $21.83-28.88), FY28 $27.08 (range $21.32-32.92); FY27 was $27.25 thirty days earlier; Q1 FY27 $2.64 (was $4.01 30 days ago); 20 down vs 1 up revisions in 7 days for the quarter. https://finance.yahoo.com/quote/INTU/analysis/
  - Basis caveat: the drop from $27.25 to $23.77 and the $28.88 high point to a mix of old (ex-SBC) and new (SBC-inclusive) definitions. Company guide on the new basis is $22.88-23.12.
  - The screen's "forward EPS $27.08" (fundamentals cache) equals Yahoo's FY28 average, so the screen's forward P/E 10.2 is on FY28, mixed basis.
- StockAnalysis, data as of 2026-09-24: 34 analysts, consensus Buy (15 Strong Buy, 5 Buy, 12 Hold, 2 negative), average target $405.6, range $290-732; FY27 revenue $23.41B, EPS $23.94. https://stockanalysis.com/stocks/intu/forecast/
- Yahoo/Barchart piece (September 2026): median target $405.60; 5 Strong Buy, 16 Buy, 12 Hold, 1 Sell, 1 Strong Sell; consensus EPS $23.94 with 24 cuts vs 5 raises in 30 days. https://finance.yahoo.com/markets/stocks/articles/intuit-crashed-over-agentic-ai-132427512.html

## Legal and regulatory

- Securities class actions: class period 2025-08-22 to 2026-05-20; alleges overstated TurboTax growth, competitive strength and FY26 guidance; lead-plaintiff deadline 2026-09-08. https://www.newsfilecorp.com/release/311867/INTU-CLASS-ACTION-NOTICE-Faruqi-Faruqi-LLP-Reminds-Intuit-INTU-Investors-of-Securities-Class-Action-Lawsuit-Deadline-on-September-8-2026 ; https://www.rgrdlaw.com/cases-intuit-inc-class-action-lawsuit-intu.html ; 10-K Note 13.
- A 2026-09-01 press item describes a class action on generative-AI disclosures and Mailchimp performance; it may be the same N.D. Cal. cases described differently. Not confirmed. https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-steadies-near-358-as-fy27-outlook-reset-and-ai-lawsuit-shape/70035530
- Direct File: less than 0.5% of ~146M individual returns for tax year 2024; not available in 2026; "no launch date has been set for the future". https://www.mondaq.com/unitedstates/tax-authorities/1730108/irs-ends-direct-file-what-us-taxpayers-need-to-know-for-the-2026-filing-season ; https://www.nstp.org/article/direct-file-not-available-2026-tax-filing-season

## Calculations used in the thesis

- Market cap $73.7B = 267.24M shares (2026-08-31) × $275.79. Net debt ≈ $0.5B = $7.72B principal − $7.2B cash and investments (excludes $0.75B lease liabilities; the fundamentals cache's $1.22B includes leases).
- FY27 GAAP operating margin at guidance midpoint: $7.449B / $23.396B = 31.8%. FY27 new-basis non-GAAP operating margin: $8.104B / $23.396B = 34.6%. FY26 on the new basis: $8.935B − $2.056B = $6.879B, 32.1% of revenue.
- P/E at $275.79: 13.6x FY27 GAAP guide midpoint ($20.24); 12.0x new-basis non-GAAP midpoint ($23.00).
- Normalized FCF: FY26 FCF $8.62B minus the extra cash tax expected in FY27 (≈$2.0B − $0.28B) ≈ $6.9B (9.4% of market cap); less FY27 SBC $2.02B ≈ $4.9B (6.6%).
- Restructuring after tax: $293M × (1 − 24%) / 277M ≈ $0.80 per share. Investment gains: $174M × 0.76 / 277M ≈ $0.48. Amortization of acquired intangibles $659M × 0.76 / 277M ≈ $1.81.
- Reverse DCF (10% discount, dividends $5.52 growing 10%, 5-year hold, EPS base $23.00): exit forward P/E 10x needs 11.9% EPS CAGR; 12x needs 7.9%; 15x needs 3.2%. Perpetuity: $6.2B FY27 SBC-inclusive earnings / ~$74.2B EV = 8.4% yield, implying ~0.6% (9% cost of equity) to ~1.6% (10%) perpetual growth.
- Scenario EPS = revenue × operating margin × (1 − 24%) / diluted shares (net interest ignored: FY26 interest expense $256M vs other income $389M, of which $174M one-off gains). Bear $24.5B × 31% → $23.1 on 250M; base $27.8B × 36% → $31.0 on 245M; bull $29.5B × 38% → $34.1 on 250M. Dividends over three years ≈ $17 per share ($1.38 quarterly now, +10%/yr assumed).

## Open questions no source closed

1. Q1 FY27 earnings date: not announced as of 2026-09-28 (Q1 FY26 was 2025-11-20). Q2 and Q3 dates likewise unannounced (last year 2026-02-26 and 2026-05-20).
2. Cause of the 2025-08-11 drop (-5.7%): no source found.
3. Which analyst downgraded INTU on 2026-02-03 (MarketBeat headline): firm not identified.
4. April 8-9, 2026: whether "Managed Agents" or "Claude Mythos" drove each day; sources conflict.
5. FY25 TurboTax units: 39.2M in the FY25 release vs 39.9M as the FY26 release comparative; not reconciled.
6. Size of the 2026 IRS filing contraction cited on the Q3 call (transcript summary says "30 basis points" and "roughly 2 million units", which do not match each other).
7. Which lower-priced or AI-native tax products took DIY share in 2026: no source quantifies it by name. Goldman's June 2 note names "GenAI-powered" competition generically.
8. Mailchimp FY26 revenue: not disclosed separately; ≈$1.26-1.27B implied by the FY27 guide of $1.256-1.266B at flat to -1%.
9. Medium-term targets (GBS 10-15%, Consumer 4-8% three-year CAGR; SBC 8% of revenue by FY2030): only in a third-party transcript summary; not checked against company slides.
10. Goldman's Sell price target at the June downgrade: not found; $304 cited in September (third-party, date unverified).
11. Lead-plaintiff appointment in the securities cases after the 2026-09-08 deadline: no update found.
12. How much of FY27's GAAP operating income growth (+26-27%) is the drop-out of FY26 restructuring ($293M to ~$22M) vs run-rate savings from the 17% cut: the company does not split it.
