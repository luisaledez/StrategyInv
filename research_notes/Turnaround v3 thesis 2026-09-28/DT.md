# DT (Dynatrace) — working notes for the turnaround v3 thesis, 2026-09-28

Research date 2026-09-28 (before the open; all returns from the Friday 2026-09-25 close of $57.95, the last bar in the price cache). Thesis file: `turnaround_backtest_v3/thesis/DT.md`. Primary documents were downloaded from EDGAR for this pass (FY2026 10-K, Q1 FY2027 and Q3 FY2026 10-Qs) and parsed locally; earnings-release exhibits (8-K Ex. 99) were read on sec.gov. Consensus, ratings, price targets and news-reported price moves are third-party and labelled as such. Fiscal year ends March 31 (FY2027 = April 2026 to March 2027). Research tooling, not investment advice.

## 1. Local cache (primary, point-in-time SEC data)

Source: `turnaround/cache/edgar/DT.json`, `fundamentals/DT.json`, `valuation/DT.json`, `prices/DT.csv`.

| Quarter end | TTM revenue $M | TTM net income $M | TTM operating income $M | TTM EBITDA $M | TTM EPS (GAAP) | Cash $M | Available |
|---|---|---|---|---|---|---|---|
| 2021-09-30 | 816 | 82 | 87 | 98 | 0.28 | 370 | 2021-12-29 |
| 2024-09-30 | 1,563 | 163 | 148 | 164 | 0.54 | 1,005 | 2024-11-07 |
| 2024-12-31 | 1,634 | 482 | 160 | 177 | 1.60 | 1,008 | 2025-01-30 |
| 2025-03-31 | 1,699 | 484 | 179 | 199 | 1.59 | 1,113 | 2025-05-22 |
| 2025-06-30 | 1,777 | 493 | 200 | 220 | 1.62 | 1,346 | 2025-08-06 |
| 2025-09-30 | 1,853 | 506 | 226 | 246 | 1.67 | 1,315 | 2025-11-05 |
| 2025-12-31 | 1,932 | 185 | 251 | 270 | 0.60 | 1,188 | 2026-02-09 |
| 2026-03-31 | 2,018 | 163 | 245 | 264 | 0.54 | 1,172 | 2026-05-20 |
| 2026-06-30 | 2,096 | 152 | 255 | 273 | 0.50 | 1,109 | 2026-08-05 |

- The cache builds TTM EPS as last fiscal year + current YTD − prior YTD (checks: 0.54 − 0.16 + 0.12 = 0.50). So the next prints are: after Q2 FY27, TTM = 0.31 + Q2 EPS; after Q3 FY27, TTM = 0.18 + Q2 + Q3; after Q4 FY27, TTM = FY27 EPS; after Q1 FY28, TTM = Q2 + Q3 + Q4 FY27 + Q1 FY28.
- Fundamentals cache (2026-06-30 balance sheet): cash $1,108.9M (the 10-Q shows cash and equivalents $1,057.8M plus $94.8M of unrestricted marketable securities; the cache figure apparently includes the short-term part — not an error worth changing); "total debt" $159.3M is operating-lease liabilities only (current $23.1M) — there is no financial debt. OCF TTM $598.4M, capex $27.8M, FCF $570.6M; buybacks TTM $709.2M; EBITDA $298.3M (fundamentals) vs $273M (EDGAR rebuild); EV $15.80B.
- Valuation cache: P/S 29.0 (Oct 2021) → 11.8 (May 2022) → 10.7 (Jan 2025) → 6.2 (Jan 2026) → 5.8 (Apr 2026, the low) → 6.6 (Jun) → 7.9 (Aug) → 8.4 (Sep 2026). EV/EBITDA 221.8 → 117.3 → 92.6 → 41.6 → 36.8 → 45.7 → 56.7 → 60.4 at the same months. P/E (trailing GAAP) 288.5 (Oct 2021), 22.8 (Jan 2026, still carrying the tax benefit), 115.9 now.
- Prices (closes): 5-year high $78.76 on 2021-10-22 (month close Oct 2021 $75.00); 2022 low $30.11 on 2022-05-11; post-2021 high $62.42 on 2025-02-12; low $32.36 on 2026-04-10; $57.95 on 2026-09-25 (+79% from the April low, +19% over 12 months).
- Large daily moves (cache): 2021-10-27 −9.9% (Q2 FY22 release day); 2021-11-15 −4.7% (CEO transition announced); 2022-02-02 −18.0% (Q3 FY22 release); 2025-03-10 −6.7%; 2025-04-04 −8.0%; 2025-08-07 −7.2% (the 2025-08-06 bar is flat at 50.53, likely stale; Q1 FY26 was released 08-06); 2025-11-05/06 −4.5%/−2.8% (Q2 FY26); 2026-01-29 −6.9%; 2026-02-03 −9.1%; 2026-02-09 +7.3% (Q3 FY26); 2026-04-09 −8.1%; 2026-05-13 −11.4% (Q4 FY26); 2026-08-05 +11.3% (Q1 FY27).

## 2. Filings: survival data (FY2026 10-K, Q1 FY2027 10-Q)

Sources: [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000050/dt-20260630.htm); [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000019/dt-20260331.htm).

- Revolver: $400.0M senior secured revolving credit facility (Credit Agreement Dec 2022, as amended), sublimits $30M swing line / $45M letters of credit; matures **December 2, 2027**; nothing drawn at June 30, 2026 or March 31, 2026; $1.1M of letters of credit; $398.9M available. Interest at Term SOFR + 0.10% (or alternatives) plus a margin; commitment fee 0.175-0.35% by leverage ratio. — 10-Q Note 8, 10-K Note 11.
- Covenants: "customary affirmative and negative covenants (including a financial covenant requiring compliance with a maximum leverage ratio)"; in compliance at June 30, 2026. The numeric maximum is not stated in the 10-K/10-Q text (it would be in the credit agreement exhibit, not read) — unverified. With no borrowings and ~$270-300M EBITDA, it is not binding.
- Debt maturities next 24 months: none (no borrowings). The only "maturity" is the undrawn revolver itself (Dec 2, 2027), which will need renewing; not a funding need.
- Leases (10-K Note 12): operating lease liabilities $164.3M at March 31, 2026; payments FY27 $28.4M, FY28 $25.4M, FY29 $23.8M, FY30 $22.6M, FY31 $20.1M, thereafter $71.5M; weighted term 8.0 years, discount rate 4.0%; a further $4.1M lease not yet commenced. At June 30, 2026: $23.1M current, $136.2M non-current (10-Q).
- Purchase obligations (10-K Note 13), "primarily related to cloud-based hosting costs, business technology software and support, and sales and marketing": FY27 $152.5M, FY28 $164.8M, FY29 $103.8M, FY30 $104.3M, total $525.3M. MD&A: total contractual commitments $721.2M, $180.8M within 12 months.
- Liquidity (10-Q): cash and equivalents $1,057.8M plus $94.8M unrestricted marketable securities at June 30, 2026; Q1 FY27 OCF $306.2M, adjusted FCF $309.2M.
- Buybacks: $500M program (May 2024) completed Feb 2026 (10.6M shares at $46.79 average, per Q3 FY26 release); new $1B program announced Feb 9, 2026; Q1 FY27 7.1M shares for $275.5M ($38.88 average); $573.1M remaining at June 30, 2026. — 10-Q, [Q1 FY27 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000049/q1fy27-earningsreleaseex99.htm), [Q3 FY26 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000006/q3fy26-earningsreleaseex99.htm).
- Acquisitions: Bindplane (observIQ) April 14, 2026, $99.7M cash in the 10-Q ($100.2M in the 10-K subsequent-event note; the 10-Q figure is the later allocation), goodwill $61.4M, intangibles $44.9M; DevCycle (Taplytics assets) Jan 13, 2026; Metis earlier. — 10-Q, 10-K.
- Litigation: none material disclosed. — 10-Q.

## 3. Filings: the EPS base and the tax question

### 3a. What left the TTM in the Dec 2025 quarter

- Q3 FY25 (quarter to Dec 31, 2024): intra-entity transfer of the global economic rights of Dynatrace IP from a US subsidiary to a Swiss subsidiary; Swiss tax-basis step-up created a deferred tax asset and a discrete **income tax benefit of $320.9M, or $1.06 per diluted share**. Q3 FY25 GAAP net income $362M, EPS $1.19, income tax benefit $305M; ETR −533.3%. — [Q3 FY25 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338325000008/fy25q3-earningsreleaseex991.htm), Q3 FY26 10-Q Note 6, FY26 10-K Note 9.
- It is a deferred-tax-asset recognition, not a valuation-allowance release. The rule's "one-off EPS guard" did not fire at entry because it left the TTM in the Dec 2025 quarter (1.67 → 0.60).
- FY25 ex-IP benefit: (483.7 − 320.9) / 303.6M diluted = **$0.54**, the same as FY26 GAAP EPS $0.54 — GAAP EPS has been flat for two years while revenue grew 19% a year.

### 3b. Why the GAAP tax rate is now ~45-55%

- FY26 ETR **45.7%** (tax $137.1M on pre-tax $299.8M); FY25 ex-IP about 27% ((−260.3 + 320.9) / 223.4); FY24 0.2%. — 10-K Note 9 (my arithmetic for FY25 ex-IP).
- FY26 rate reconciliation (10-K, ASU 2023-09 table, % of pre-tax): statutory 21.0; state 1.4; Switzerland rate difference −7.8, cantonal/communal +2.3; other foreign +6.3; **GILTI net of credits +8.8; foreign branches net of credits +6.5; US tax on foreign IP royalties +2.1**; nondeductible employee compensation +4.3; unrecognized tax benefits +1.1; Brazil withholding +1.5; Israel IP transfer +1.1; Poland R&D credits −1.6; other small items. Total 45.7%.
- MD&A: rate differs from 21% mainly due to "(1) the net global intangible low-taxed income ("GILTI") inclusion, (2) foreign withholding taxes, (3) nondeductible executive compensation, and (4) the recognition of royalty income in the U.S. as a result of the IP Transfer ... partially offset by the generation of U.S. foreign tax credits. We expect these items to continue to affect our income tax rate". The transfer "is taxable in the U.S. through 2044"; Swiss tax amortization runs "through 2035". — 10-K.
- Q3 FY26 10-Q: the IP Transfer "also impacted fiscal 2026 resulting in an increase to the GILTI inclusion, primarily due to an increase in capitalized foreign research and development expenses within GILTI and a decrease to the foreign-derived intangible income" deduction. — [Q3 FY26 10-Q](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000008/dt-20251231.htm).
- OBBBA: "did not have a material impact on fiscal 2026. We do not anticipate the provisions effective in future years will have a material impact." Pillar Two: not material in FY26; Jan 5, 2026 OECD side-by-side guidance may exempt US-parented groups. — 10-K risk factors / MD&A.
- Quarterly ETR: Q1 FY26 41.1%; Q2 FY26 ~34% ($30M on $87M); Q3 FY26 52.6%; Q4 FY26 62.8% ($29.4M on $46.8M, pre-tax depressed by an $18.5M long-lived-asset impairment and other items); Q1 FY27 **54.6%** ($44.2M on $80.8M). Q1 FY27 driver per 10-Q: "the tax impact of share-based compensation shortfalls recognized in the current fiscal year as compared to share-based compensation windfalls recognized in the prior fiscal year." Interim method: estimated annual ETR applied to income, plus discrete items in the period.
- Cash taxes paid FY26 $117.6M (US federal $70.8M). Non-GAAP uses an "effective cash tax" ($30.7M in Q1 FY27 on ~$170M non-GAAP pre-tax).

### 3c. Why TTM EPS drifted 0.60 → 0.54 → 0.50

- Q4 FY26 EPS $0.06 vs $0.13 a year earlier: $28.1M of transaction, restructuring and other items in FY26, all in Q4 (the Q3 FY26 10-Q shows none for the nine months), including an **$18.5M impairment of long-lived assets** (right-of-use assets and related property; 10-K); plus a 62.8% ETR. GAAP operating income $37M vs non-GAAP $143M.
- Q1 FY27 EPS $0.12 vs $0.16: pre-tax flat ($80.8M vs $81.4M) because interest income fell ($8.9M vs $12.3M, cash spent on buybacks) and other income fell ($0.4M vs $6.8M, FX), while GAAP operating income rose 15% ($71.5M vs $62.3M) despite $7.7M of Bindplane acquisition costs; ETR 54.6% vs 41.1%. Diluted shares 293.7M vs 304.2M (−3.4%) partly offset. — Q1 FY27 10-Q.

### 3d. GAAP EPS path to the trigger (my estimates; not company guidance — Dynatrace guides non-GAAP only)

Quarters leaving the TTM: Q2 FY26 $0.19 (Nov 2026 print), Q3 FY26 $0.13 (Feb 2027), Q4 FY26 $0.06 (May 2027), Q1 FY27 $0.12 (Aug 2027).

- Q2 FY27 estimate: non-GAAP operating income guide $166-170M (Q1 came in $8-12M above its $150-154M guide) less SBC ~$74-78M (Q1 $73.6M), employer payroll taxes ~$4-6M (Q1 $6.5M), amortization ~$3M (remaining FY27 $9.4M over three quarters), acquisition costs $0-5M → GAAP operating income ~$80-95M; plus ~$8-9M interest/other → pre-tax ~$88-104M. At 45-55% ETR → net income ~$40-57M → **EPS ~$0.14-0.19** on 293-294M diluted shares. TTM after the November print ~$0.45-0.50.
- Trigger at the November print needs Q2 EPS ≤ $0.12, i.e. an ETR of ~60%+ on ~$95M pre-tax, or a ~$15M+ discrete charge. Probability ~5% (judgement).
- Trigger at the February 2027 print needs Q2 + Q3 ≤ $0.25 (9-month FY27 EPS ≤ $0.37). Q3 non-GAAP operating income, implied by the $682-690M FY guide less Q1 actual and Q2 guide, is ~$175-185M → GAAP pre-tax ~$100-110M → Q3 EPS ~$0.16-0.20 at 45-55%. Sum ~$0.30-0.39; failing needs both quarters near Q1's $0.12 (ETR ~55-60% plus shortfalls) or a charge of ~$25-35M after tax. Additional probability ~10% (judgement).
- May and August 2027 prints: TTM replaces $0.06 and $0.12 quarters; trigger needs FY27 ≤ $0.43 (i.e. Q2-Q4 ≤ $0.31) — only with a large charge. ~3-5%.
- **Total trigger risk over the 12-month window: about 15-20%**, concentrated in the Feb 2027 print. It falls if the share price stays above the ~$45-55 level at which recent RSUs were granted (shortfalls shrink or turn to windfalls; Q2 FY26 had a ~34% ETR with windfalls at ~$50 stock), and rises with a return to the high $30s (Q1 FY27 buybacks averaged $38.88) or any impairment/restructuring (e.g. around the CFO change) or a larger acquisition.
- Unverified inputs: RSU vesting calendar and grant-date prices (not disclosed in the text read); the estimated annual ETR used in Q1 FY27 (not disclosed).

## 4. Quarterly table (earnings releases, Ex. 99.1 on EDGAR)

$M except per share. NG = non-GAAP. Guide = the next-quarter revenue / NG EPS guide and the full-year guide issued with that print.

| Quarter (end) | Released | Revenue | ARR | ARR growth rep / cc | GAAP EPS | NG EPS | NG op margin | ETR | Guide issued with the print |
|---|---|---|---|---|---|---|---|---|---|
| Q1 FY25 (Jun 2024) | Aug 2024 | 399 | 1,541 | n/a | 0.13 | 0.33 | 29% | n/a | not collected |
| Q2 FY25 (Sep 2024) | Nov 2024 | 418 | 1,617 | n/a | 0.15 | 0.37 | 31% | ~24% | not collected |
| Q3 FY25 (Dec 2024) | Jan 30, 2025 | 436 | 1,647 | n/a | **1.19** (incl. $1.06 IP benefit) | 0.37 | 30% | −533% | not collected |
| Q4 FY25 (Mar 2025) | May 2025 | 445 | 1,734 | 15% / 17% | 0.13 | 0.33 | 26% | 29% | Q1: rev 465-470, NG EPS 0.37-0.38; FY26: ARR 1,975-1,990 (13-14% cc), rev 1,950-1,965, NG EPS 1.56-1.59, FCF 505-515 |
| Q1 FY26 (Jun 2025) | Aug 6, 2025 | 477 | 1,822 | 18% / 16% | 0.16 | 0.42 | 30% | 41.1% | Q2: rev 484-489, EPS 0.40-0.41; FY26: ARR 1,988-2,003, rev 1,970-1,985, EPS 1.58-1.61 |
| Q2 FY26 (Sep 2025) | Nov 5, 2025 | 494 | 1,899 | 17% / 16% | 0.19 | 0.44 | 31% | ~34% | Q3: rev 503-508, EPS 0.40-0.42; FY26: ARR 2,010-2,025, rev 1,985-1,995, EPS 1.62-1.64 |
| Q3 FY26 (Dec 2025) | Feb 9, 2026 | 515 | 1,972 | 20% / 16% | 0.13 | 0.44 | 30% | 52.6% | Q4: rev 518-523, EPS 0.38-0.39; FY26: ARR 2,053-2,061, rev 2,005-2,010, EPS 1.67-1.69; new $1B buyback |
| Q4 FY26 (Mar 2026) | May 13, 2026 | 532 | 2,054 | 18% / 16% | 0.06 | 0.41 | 27% | 62.8% | Q1: rev 547-551, EPS 0.44-0.45; FY27: ARR 2,382-2,402 (15.5-16.5% cc), rev 2,317-2,335 (14-15% cc), NG op margin 29.5%, EPS 1.93-1.95, FCF 613-620, shares 302-304M |
| Q1 FY27 (Jun 2026) | Aug 5, 2026 | 555 | 2,136 | 17% / 17% | 0.12 | 0.48 | 29% | 54.6% | Q2: rev 565-570 (15-16% cc), NG op inc 166-170, EPS 0.48-0.49, shares 293-294M; FY27: ARR 2,359-2,379 (cc 15.5-16.5% unchanged; FX −$23M), rev 2,306-2,320 (14.5-15% cc, +25 bp), NG op margin 29.5-29.75%, EPS 1.97-1.99, adj. FCF 610-615 |

Sources: [Q1 FY27](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000049/q1fy27-earningsreleaseex99.htm); [Q4 FY26](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000011/fy26q4-earningsreleaseex99.htm); [Q3 FY26](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000006/q3fy26-earningsreleaseex99.htm); [Q2 FY26](https://www.sec.gov/Archives/edgar/data/1773383/000162828025049224/q2fy26-earningsreleaseex991.htm); [Q1 FY26](https://www.sec.gov/Archives/edgar/data/1773383/000177338325000153/fy26q1-earningsreleaseex991.htm); [Q4 FY25](https://www.sec.gov/Archives/edgar/data/1773383/000177338325000047/fy25q4-earningsreleaseex991.htm); [Q3 FY25](https://www.sec.gov/Archives/edgar/data/1773383/000177338325000008/fy25q3-earningsreleaseex991.htm). FY25 quarters' ARR/revenue/EPS taken from the year-ago columns of the FY26 releases; Q2 FY25 ETR (~24%, $14M on $58M) from the Q2 FY26 release. Q4 FY25 ETR 29% ($16.4M on $55.7M) from the Q4 FY26 release. Q4 FY25 release date: May 2025 (exact day not checked).

- FY26 actuals: revenue $2,018M (+19%, +17% cc), ARR $2,054M, GAAP op margin 12%, NG op margin 29%, GAAP EPS $0.54, NG EPS $1.70 (vs initial guide 1.56-1.59), FCF $529M, SBC $299.6M, buybacks $478.7M. Net new ARR FY26 $277M (+12%), first double-digit net-new-ARR growth in three years; FY27 net new ARR guide $320-340M (+16-23%). — Q4 FY26 release; call coverage: [Yahoo Q4 FY26 call highlights](https://finance.yahoo.com/markets/stocks/articles/dynatrace-inc-dt-q4-2026-230250207.html).
- Guidance pattern: beat-and-raise every quarter in FY26 (NG EPS guide 1.56-1.59 → actual 1.70; ARR guide 1,975-1,990 → actual 2,054, helped by FX). FY27 raised once (NG EPS +$0.04; ARR in dollars −$23M on FX, cc unchanged).

## 5. KPIs: retention, DPS, logs, AI

- Dollar-based net retention (cc, ARR cohort): 111% (Mar 2024), 110% (Mar 2025), 110% (Mar 2026), 111% (Jun 2025), **110% (Jun 2026)**. — 10-K, 10-Q. Gross retention "mid-90% range" (Q1 FY27 call, [Yahoo call highlights](https://finance.yahoo.com/markets/stocks/articles/dynatrace-q1-earnings-call-highlights-050348489.html), third-party summary). In Q3 FY22 the release cited net expansion "above 120%" ([Q3 FY22 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338322000019/fy22q3-earningsreleaseex991.htm)) — the metric definition may differ; not reconciled.
- DPS (Dynatrace Platform Subscription: minimum annual platform commit consumed on a rate card, on-demand usage beyond commit at the same rate, no penalty overage — 10-K): >40% of customers / >60% of ARR (Q4 FY25 release); >45% / >65% (Q1 FY26 release); ~50% / ~70% (Q2 FY26, per search summary of the call; not checked in a transcript); **~60% of customers / >75% of ARR (Q4 FY26 call**, per [search summary citing Yahoo/Motley Fool transcripts](https://www.fool.com/earnings/call-transcripts/2026/05/13/dynatrace-dt-q4-2026-earnings-transcript/); not verified line by line). Company says DPS customers consume at about twice the rate of SKU customers. Q1 FY27 figure: not found. Needham (Sep 18, 2026 upgrade) cites the growing DPS renewal cohort as the driver ([Investing.com](https://www.investing.com/news/analyst-ratings/needham-upgrades-dynatrace-stock-rating-on-platform-momentum-93CH-4907068), third-party).
- ARR excludes on-demand usage beyond commit ("product usage overage billings") — 10-K definition. So DPS over-consumption shows in revenue before ARR; a revenue/ARR gap is a leading sign of commit expansion at renewal.
- Logs: annualized consumption >$100M (Q3 FY26 release); "well over $100M", >100% growth (Q4 FY26 call); **nearly $200M annualized, >100% y/y, nearly doubled in two quarters** (Q1 FY27 release). 50% of Q1 FY26's twelve >$1M expansion deals had significant log deployments (Q1 FY26 release).
- AI: 1,000+ customers monitoring AI workloads (up from ~850), 800+ using agentic capabilities (up from ~500), AI-cohort consumption growth 1.5x that of others; management sizes AI observability at >$10B by 2030 growing 50%+ a year (Q1 FY27 call, third-party summary). Products: "Dynatrace Intelligence" agentic system (Q3 FY26 release); Dynatrace Bluebox private preview (Q1 FY27 release). Gartner MQ Leader for observability platforms, 16th consecutive year (Q1 FY27 release).
- New logos: 126 in Q4 FY26, record 22 deals > $1M ACV, new-logo ARR +43% (Q4 FY26 call, third-party summary); 122 in Q1 FY27, new-logo ARR >160%, average land ~$285K (Q1 FY27 call/release). Net new ARR Q1 FY27 $85M (+66%), organic $73M (+41%) excluding Bindplane's $13M ARR.
- CFO: Jim Benson to resign by March 31, 2027; search under way (Q1 FY27 release).

## 6. Price history causes (news, third-party unless noted)

- Oct 27, 2021 −9.9%: Q2 FY22 beat and raise (ARR $864M +35%, FY22 ARR guide raised to $986-996M, NG EPS $0.63-0.65) ([Q2 FY22 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338321000113/fy22q2-earningsreleaseex991.htm)). No source found for the reason for the drop; read as a multiple event at P/S 29.
- Nov 15, 2021: CEO John Van Siclen to retire Dec 13, 2021; Rick McConnell (ex-Akamai) named CEO ([8-K press release](https://www.sec.gov/Archives/edgar/data/1773383/000177338321000118/exh991pressrelease11-15x21.htm)). Stock −4.7% that day (cache).
- Feb 2, 2022 −18.0%: Q3 FY22: ARR $930M +29% reported (+32% cc) vs +35% the prior quarter; NG op margin 25% vs 29% a year earlier; plan to step up investment; FY22 guide nudged up ([Q3 FY22 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338322000019/fy22q3-earningsreleaseex991.htm)). Cause of the reaction inferred (growth deceleration + margin reset at a very high multiple); no news source read.
- 2022: software de-rating with rates; low close $30.11 May 11, 2022 (cache). No company-specific source.
- Mar-Apr 2025 (−6.7% Mar 10, −8.0% Apr 4): market/tariff sell-off period; no DT-specific source found.
- Aug 7, 2025 −7.2% after Q1 FY26 beat-and-raise: no reliable source for the cause found (search summaries conflated it with the May 2026 print).
- Jan 29 − Feb 5, 2026 (−6.9% Jan 29, −9.1% Feb 3): sector-wide AI-disruption sell-off in software after Anthropic's Claude Cowork plugins (Jan 30); ~$1T of software market value lost Feb 3-5 ([Axios, Feb 3, 2026](https://www.axios.com/2026/02/03/ai-software-anthropic-stock-market); [Morningstar](https://www.morningstar.com/markets/what-know-about-software-stock-selloff)).
- Feb 9, 2026 +7.3%: Q3 FY26 beat, ARR guide +125 bp, $1B buyback ([Q3 FY26 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000006/q3fy26-earningsreleaseex99.htm)). Macquarie initiated Neutral, $36 target, Feb 27, 2026 (search summary; third-party).
- Apr 9-10, 2026 (−8.1%, −4.3%; low $32.36): cause not found ([GuruFocus](https://www.gurufocus.com/news/8785472/dynatrace-inc-dt-shares-down-579-on-apr-9) reports the move without a cause).
- May 13, 2026 −11.4% (down as much as 16.4% intraday): Q4 FY26 beat, but FY27 guide implied deceleration (ARR 15.5-16.5% cc; revenue 14-15% cc) and Q1 NG EPS guide $0.44-0.45 vs consensus ~$0.45 ([Motley Fool](https://www.fool.com/investing/2026/05/13/why-dynatrace-stock-plummeted-today/); [Investing.com](https://www.investing.com/news/earnings/dynatrace-shares-tumble-despite-earnings-beat-4683867)). The Fool's "roughly 14% ARR growth" conflicts with the release's 16-17% reported / 15.5-16.5% cc; I prefer the release. Datadog reported +32% revenue growth the same month and rose 31% in a day ([Yahoo, May 18, 2026](https://finance.yahoo.com/markets/stocks/articles/datadog-soars-dynatrace-slumps-gap-114500255.html)).
- Aug 5, 2026 +11.3%: Q1 FY27 (net new ARR +66%, NG EPS $0.48 vs $0.44-0.45 guide, FY EPS raised).
- Sep 1-2, 2026: platform incident ("Issue with Authentication Services" Sep 1; partial disruption across AWS/Azure/GCP into Sep 2); stock −3.8% Sep 2 ([Quiver Quantitative](https://www.quiverquant.com/news/Dynatrace+Shares+Fall+as+Platform+Disruption+Clouds+Sentiment); status aggregators). Customer impact/credits: no source found.
- Sep 18, 2026: Needham upgrade Hold → Buy, $68 target ([MarketBeat](https://www.marketbeat.com/instant-alerts/analyst-dynatrace-nyse-dt-raised-to-buy-at-needham-company-llc-2026-09-18/)).

## 7. Consensus and competition (third-party)

- Yahoo Finance (read 2026-09-28; normalized = non-GAAP): Q2 FY27 (Sep 2026) EPS $0.49 (0.47-0.51), revenue $567.9M; Q3 FY27 EPS $0.51, revenue $588.1M; FY27 EPS $1.98 (1.85-2.02), revenue $2.32B; **FY28 EPS $2.30 (2.18-2.44), revenue $2.66B (2.61-2.74)**; 30-day EPS revisions: FY27 25 up / 1 down, FY28 18 up / 8 down ([Yahoo analysis](https://finance.yahoo.com/quote/DT/analysis/)).
- StockAnalysis (S&P Global / TipRanks, updated Sep 24, 2026): 36 analysts, "Buy", average target $59.71 (range $42-71); FY27 revenue $2.32B (+14.9%), EPS $1.98 ([stockanalysis.com](https://stockanalysis.com/stocks/dt/forecast/)). Other aggregators show $59.12 and $63.10 averages — sources differ; I use $59.7 as a mid value.
- Fundamentals cache forward EPS $2.30 (= FY28 non-GAAP consensus) → forward P/E 25.2.
- Datadog Q2 2026 (Aug 6, 2026): revenue $1.12B, +36% y/y; NG op margin 23%; FY26 guide $4.45-4.47B ([Datadog 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001561550/000162828026053829/ex-991x20260630x8k.htm)). Datadog is growing about twice as fast as Dynatrace on ~2x the revenue.
- Market sizing: observability tools ~$11.9B in 2026, ~14% CAGR to 2031 (Mordor Intelligence, third-party, low confidence). Cost is repeatedly cited as the top selection criterion; OpenTelemetry lowers switching costs (vendor blogs, low confidence).

## 8. Scenario arithmetic (thesis section 5)

- Starting TTM revenue at Sep 2026 ≈ $2,096M + Q2 FY27 guide mid $567M − Q2 FY26 $494M ≈ $2.17B.
- Year-3 (12 months to Sep 2029) revenue = 2.17 × (1+g)^3: bear g 9% → $2.81B; base 13% → $3.13B; bull 16% → $3.39B.
- Adjusted FCF margin: bear 25%, base 27%, bull 30% (FY27 guide 26.5%; FY26 26%).
- EV/FCF: bear 15x, base 22x, bull 28x (today ~26x FY27 guided adjusted FCF, 27.7x TTM FCF).
- Net cash yr 3: $1.2B / $1.2B / $1.5B (FCF mostly returned via buybacks). Diluted shares yr 3: 278M / 282M / 283M (buybacks at $45 / $65 / $80 average net of ~2%/yr SBC dilution).
- Implied prices: $42.2 / $70.2 / $105.8; EV/Sales implied 3.8x / 5.9x / 8.4x. Weights 30/50/20 → **$68.9 (+19%)**.
- Reverse DCF (10% discount, 10 years then 3% terminal, EV $15.8B): FY27 adjusted FCF $612M must grow ~10.6% a year for ten years; treating SBC (~$300M/yr) as a cash cost, ~19.7% a year. My calculation.

## 9. Open questions no source closed

1. RSU vesting calendar and grant-date prices (determines the size and quarter of SBC shortfalls) — not in the text read.
2. The estimated annual ETR embedded in Q1 FY27 (how much of 54.6% is discrete) — not disclosed.
3. Maximum leverage ratio covenant level — in the credit agreement exhibit, not read.
4. DPS share of ARR at June 30, 2026 — not found; the Q4 FY26 ">75% of ARR / 60% of customers" is from call summaries, not verified against a transcript.
5. Cause of the Oct 27, 2021, Aug 7, 2025 and Apr 9-10, 2026 drops — no reliable source.
6. Q2 FY27 earnings date — not yet announced as of the searches (Q2 FY26 was Nov 5, 2025; Q3 FY26 Feb 9, 2026).
7. Customer impact of the Sep 1-2, 2026 platform incident (credits, churn) — no source.
8. How much of the FY26 $18.5M impairment and $28.1M "transaction, restructuring and other" relates to office consolidation vs other items — quarter placement inferred (Q4) from the Q3 10-Q showing none for nine months.
9. FY28 consensus revenue/EPS are from one aggregator (Yahoo); StockAnalysis FY28 figures are paywalled.
