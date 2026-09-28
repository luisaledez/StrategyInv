# NOW (ServiceNow) — research notes for the turnaround v3 thesis, 2026-09-28

Working notes behind `turnaround_backtest_v3/thesis/NOW.md`. Research tooling, not investment advice.
Primary sources first (SEC 8-K earnings releases, 10-Q), then news; consensus figures are third-party.

## Split and data conventions

- **5-for-1 stock split**: approved by the board 2025-12-05, record date 2025-12-16, effective 2025-12-17 (Q2 2026 10-Q, stock split paragraph: https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm). Split authorisation was first announced with Q3 2025 results on 2025-10-29 (https://www.sec.gov/Archives/edgar/data/1373715/000137371525000305/erq3fy25.htm).
- Local EDGAR cache (`turnaround/cache/edgar/NOW.json`) records the split as `2025-12-18, 5.0` (first split-adjusted trading day); price cache is split-adjusted throughout. The 5-year high 234.08 (2025-01-28 close) is about $1,170 pre-split.
- All per-share figures below are **split-adjusted** (pre-2025-Q4 releases reported pre-split EPS; divided by 5 here; the as-reported value is shown in brackets where useful). The cache's TTM EPS path (1.47, 1.59, 1.65, 1.67, 1.68, 1.60) matches the sum of the split-adjusted quarterly GAAP EPS below.

## Quarterly table (Q3 2024 - Q2 2026)

$ millions except per share. Growth y/y; cc = constant currency. Guidance = the next quarter's guide given with that quarter's results, and the full-year subscription guide at that date.

| Quarter | Total rev | Subscription rev | Sub growth (cc) | cRPO $B | cRPO growth (cc) | GAAP op margin | Non-GAAP op margin | GAAP EPS | Non-GAAP EPS | FCF | Next-quarter guide (sub rev; cRPO) | FY sub-rev guide at the time | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q3 2024 | 2,797 | 2,715 | 23% (22.5%) | 9.36 | 26% (23.5%) | 15% | 31% | 0.414 [2.07] | 0.744 [3.72] | 471 | Q4: 2,875-2,880; cRPO 21.5% cc | FY24 10,655-10,660 | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371524000342/erq3fy24.htm) |
| Q4 2024 | 2,957 | 2,866 | 21% (21%) | 10.27 | 19% (22%) | 13% | 29.5% | 0.366 [1.83] | 0.734 [3.67] | 1,400 | Q1: 2,995-3,000; cRPO 19.5-20.5% cc | FY25 12,635-12,675 (18.5-19%) | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000007/erq4fy24.htm) |
| Q1 2025 | 3,088 | 3,005 | 19% (20%) | 10.31 | 22% (22%) | 14.5% | 31% | 0.44 [2.20] | 0.808 [4.04] | 1,477 | Q2: 3,030-3,035; cRPO 19.5% cc | FY25 12,640-12,680 | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000124/erq1fy25.htm) |
| Q2 2025 | 3,215 | 3,113 | 22.5% (21.5%) | 10.92 | 24.5% (21.5%) | 11% | 29.5% | 0.368 [1.84] | 0.818 [4.09] | 535 | Q3: 3,260-3,265; cRPO 18.5% (18% cc) | FY25 12,775-12,795 | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000274/erq2fy25.htm) |
| Q3 2025 | 3,407 | 3,299 | 21.5% (20.5%) | 11.35 | 21% (20.5%) | 17% | 33.5% | 0.48 [2.40] | 0.964 [4.82] | 592 | Q4: 3,420-3,430; cRPO 23% (19% cc) | FY25 12,835-12,845 | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000305/erq3fy25.htm) |
| Q4 2025 | 3,568 | 3,466 | 20.5% (19.5%) | 12.85 | 25% (21%) | 12.5% | 31% | 0.38 | 0.92 | 2,032 | Q1: 3,650-3,655; cRPO 22.5% (20% cc) | FY26 15,530-15,570 (20.5-21%) | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000005/erq4fy25.htm) |
| Q1 2026 | 3,770 | 3,671 | 22% (19%) | 12.64 | 22.5% (21%) | 13.5% | 32% | 0.45 | 0.97 | 1,665 | Q2: 3,815-3,820; cRPO 19-19.5%; GAAP op margin 3.5%, non-GAAP 26.5% | FY26 15,735-15,775 | [8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000054/erq1fy26.htm) |
| Q2 2026 | 3,987 | 3,877 | 24.5% (23%) | 13.20 | 21% (21.5%) | 4% | 29.5% | 0.29 | 0.90 | 634 | Q3: 3,975-3,980 (20.5%, 20% cc); cRPO 19.5% (20% cc); GAAP op margin 8%, non-GAAP 31%; diluted shares 1.05B | FY26 15,760-15,780 (22.5%, 21% cc) | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000072/erq2fy26.htm) |

Full-year: FY2025 subscription revenue $12,883M (+21%), GAAP EPS $1.67 (FY24 $1.37), non-GAAP EPS $3.51 (FY24 $2.78), FCF margin 35% (Q4 2025 8-K). FY2026 guide (Q2 2026 8-K): non-GAAP subscription gross margin 81%, non-GAAP operating margin 31.5%, FCF margin 35%, GAAP operating margin 10%, GAAP subscription gross margin 75%, diluted shares 1.04B. The FY2025 non-GAAP subscription gross margin guide was 83.5% (Q3 2025 8-K), so the 2026 guide is about 2.5 points lower (Armis, AI compute/hyperscaler costs).

Guidance history for FY2026 non-GAAP operating margin: 32% (Jan 2026) → 31.5% (Apr 2026, after Armis; Armis ~75 bp operating-margin, ~200 bp FCF-margin headwind per Q1 2026 8-K) → 31.5% (Jul 2026). FCF margin: 36% → 35% → 35%.

**Conflict flagged:** the FY2026 subscription guide after Q2 2026 is $15,760-15,780M in the SEC 8-K; an Investing.com call summary gives $15.755-15.770B. The 8-K is preferred.

## Why TTM GAAP EPS slipped 1.68 → 1.60 (Q2 2026 vs Q2 2025)

From the Q2 2026 10-Q income statement (https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm) and the 8-K reconciliation (https://www.sec.gov/Archives/edgar/data/1373715/000137371526000072/erq2fy26.htm):

| $M | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | 3,987 | 3,215 | +772 |
| Gross profit | 2,818 (70.7%) | 2,491 (77.5%) | +327 |
| Income from operations | 162 | 358 | -196 |
| Interest income | 70 | 116 | -46 (cash spent on Veza/Armis: $8.8B cash paid for acquisitions in H1 2026) |
| Other income (expense), net | 206 | (3) | +209 (includes $273M unrealised gains on strategic investments and $66M interest expense on the new debt) |
| Pre-tax income | 438 | 471 | -33 |
| Tax provision | 140 | 86 | +54 (includes a $51M discrete benefit from a valuation-allowance release) |
| Net income | 298 | 385 | -87 |
| Diluted EPS | 0.29 | 0.37 | -0.08 |
| Non-GAAP operating income | 1,173 (29.5%) | ~948 (29.5%, derived) | +~225 |
| Non-GAAP diluted EPS | 0.90 | 0.81 | +0.09 |

Reconciling items (Q2 2026 vs Q2 2025): stock-based compensation 655 vs 499; amortization of purchased intangibles 219 vs 25; business-combination costs 75 vs 14; severance 62 vs 29; impairment 0 vs 30; gains on strategic investments -273 vs -5; valuation-allowance release -51 vs 0.

So the slip is **acquisition accounting and financing, not operations**: amortization +$194M, SBC +$156M, deal and severance costs +$94M, lost interest income -$46M and new interest expense ~$66M, partly offset by a $268M larger unrealised investment gain. Non-GAAP operating income grew ~24%.

Q1 2026 also carried $87M of gains on strategic investments (Q1 2026 8-K). Q3 2025 and Q4 2025 reconciliations list no investment-gain line (8-Ks above). Which investee drove the Q2 2026 $273M unrealised gain: **not identified** (a Substack recap calls it unrealised valuation gains: https://ashtoninvests.substack.com/p/servicenow-q2-2026-earnings-recap).

Rough non-operating share of TTM EPS (derived): ($87M + $273M) gains × (1 - 21%) + $51M VA release ≈ $335M ≈ $0.32 per share → TTM GAAP EPS ex these items ≈ **$1.28**, already below the $1.36 trigger. The v3 one-off guard passed (TTM net income / operating income 0.99) because the gains were offset by the high GAAP tax charge and lower interest income; the guard's test cannot see this.

## Trigger arithmetic (guide-cut proxy $1.36)

- TTM at entry = Q3'25 0.48 + Q4'25 0.38 + Q1'26 0.45 + Q2'26 0.29 = 1.60.
- After the Q3 2026 print, Q3 2025's $0.48 drops out. The TTM stays above $1.36 only if **Q3 2026 GAAP EPS > $0.24**, i.e. net income > ~$252M on ~1.05B diluted shares.
- Company guide for Q3 2026: GAAP operating margin 8% (non-GAAP 31%; SBC 16% of revenue, amortization 5%, other ~2%) on ~$4.09B revenue (subscription guide midpoint $3,977.5M + ~$110M services; consensus revenue $4.1B) → GAAP operating income ≈ $327M.
- Below the line (derived): interest income ~$65M (Q2 $70M on a smaller cash pile); interest expense ~$82M/quarter at the June 30 debt stack ($5.5B notes at 1.53-6.57% effective ≈ $61M, $2.1B commercial paper at 3.98% ≈ $21M; Q2 actual $66M with notes outstanding for part of the quarter).
- Sensitivity (derived, no investment gains): GAAP op margin 8% / tax 30% → EPS ~$0.21 → TTM ~$1.33 (trigger); 9% / 30% → $0.23 → $1.35 (trigger); 10% / 30% → $0.26 → $1.38 (no trigger); 10% / 40% → $0.22 → $1.34 (trigger). A $100M pre-tax investment gain adds ~$0.06-0.07.
- GAAP effective tax rate: 30.3% in Q1 2026 (204/673), 32% in Q2 2026 (140/438) and ~44% in Q2 excluding the VA release; H1 2026 30.9% vs 17.6% in H1 2025 (10-Q). No company explanation of the 2026 rate found.
- Beat history on the GAAP guide: Q2 2026 guided 3.5%, delivered 4% (+0.5 pt) while the non-GAAP margin beat by 3 pts (26.5% → 29.5%); the gap went into severance and deal costs. One data point only.
- Timing: Q3 2026 report expected **Oct 28, 2026 after close** (TipRanks/MarketBeat listings via search, https://www.tipranks.com/stocks/now/earnings, https://www.marketbeat.com/stocks/NYSE/NOW/earnings/; **not confirmed by a company announcement found**). The Q2 10-Q reached the cache the day after the release (available 2026-07-23), so the Q3 figure should be in the point-in-time data by the **Oct 30, 2026** month-end check (last trading day of October).
- Q4 2026 (implied by the FY GAAP 10% margin guide: ~$0.62-0.63B GAAP operating income, ~14% margin) should print above Q4 2025's $0.38, so the risk is concentrated in the Q3 print. Q1 2027 and Q2 2027 compare against quarters that contained $87M and $273M gains.
- **Estimate: roughly 55% probability (range 40-70%) that the proxy fires at the Oct 30 or Nov 30, 2026 month-end.** Low confidence: it hinges on the GAAP margin beat, the tax line and any mark-to-market on $2.07B of strategic investments.

## Acquisitions (10-Q Q2 2026 business-combination note)

| Deal | Closed | Consideration | Notes |
|---|---|---|---|
| Logik.io | 2025-05-30 | $506M (~$434M stock + $62M cash, per fetch summary; components do not sum, unverified) | CPQ |
| Moveworks | 2025-12-15 | $2.407B (stock $1,467M, cash $905M, other $35M) | AI assistant layer; goodwill $1,748M non-deductible |
| Veza | 2026-03-02 | ~$1.2B cash | identity security |
| Armis | 2026-04-20 | ~$7.6B cash (announced $7.75B, 2025-12-23: https://www.cnbc.com/2025/12/23/servicenow-armis-cybersecurity-acquisition.html) | intangibles $2,530M (developed tech $1,950M, customer relationships $473M, 5-6 yr lives); goodwill $5,323M |

- Inorganic contribution: Armis ~125 bp to Q2 and FY2026 subscription growth; ~25 bp subscription gross-margin, ~75 bp operating-margin and ~200 bp FCF-margin headwind for FY2026 (Q1 2026 8-K). Moveworks: the Q4 2025 8-K summary says about 100 bp; a Motley Fool transcript summary rendered it as "1 bp" (https://www.fool.com/earnings/call-transcripts/2026/01/28/servicenow-now-q4-2025-earnings-call-transcript/). **Conflict; about 1 point is the more plausible reading, unverified against the transcript text.**
- Organic subscription growth in Q2 2026 is therefore roughly 21-22% reported (~20-21% cc) after ~2-2.5 pts of acquired revenue — derived, not a company figure.
- Future amortization of intangibles at 2026-06-30: remainder of 2026 $391M, 2027 $776M, 2028 $726M, 2029 $700M, 2030 $648M, thereafter $540M (10-Q).
- M&A stance: CEO on the Q4 2025 call: "We do not have a large-scale M&A on the roadmap" (Fool transcript above).
- The v3 acquisition guard passed: diluted shares -0.1% y/y (Moveworks stock offset by buybacks) and growth did not jump by the guard's 3x/10 pp test.

## Balance sheet, debt and obligations (Q2 2026 10-Q and 8-K)

- Cash and equivalents $2,503M; current marketable securities $2,161M (these two = the cache's $4.66B "cash"); long-term marketable securities $2,043M; strategic investments $2,073M.
- Debt: senior notes $5.5B — 1.40% due Sept 2030 $1,500M (issued Aug 2020); issued May 2026: 4.25% due May 2028 $750M, 4.70% due Aug 2031 $600M, 5.05% due May 2033 $650M, 5.40% due May 2036 $1,250M, 6.30% due May 2056 $750M. Commercial paper $2.1B outstanding (program up to $3.0B, maturities up to 397 days, weighted rate 3.98%). Balance-sheet short-term debt $2,082M, long-term $5,435M.
- $4.0B term loan (credit agreement 2026-04-17, maturity Oct 16, 2026) was drawn for Armis and repaid from the May 2026 notes.
- Revolver: $3.0B unsecured, matures 2031-04-01, undrawn at 2026-06-30, accordion up to +$2.0B, SOFR/base + 0.60-1.00%; "customary affirmative and negative covenants"; **no financial-ratio covenant found in the 10-Q text read** (unverified against the credit agreement exhibit).
- Maturities within 24 months of 2026-09-28: commercial paper ~$2.1B (rolling) and the $750M 4.25% notes due May 2028 → ~$2.85B.
- Interest expense on debt: $66M in Q2 2026 (10-Q); run-rate ~$82M/quarter derived.
- Operating lease liabilities $936M ($114M current, $822M non-current). Purchase obligations by year not in the 10-Q text read.
- Buybacks: $2,233M (20.2M shares, ~$110.58 average) in H1 2026 (10-Q); $5B additional authorisation and a $2B ASR announced 2026-01-28 (Q4 2025 8-K). Remaining authorisation not found.
- Customer concentration / federal: one U.S. federal channel partner and systems integrator = 13% of total revenue in Q2 and H1 2026 and 12% of receivables at 2026-06-30 (10-Q). Not named in the text read (commonly assumed to be Carahsoft; unverified).

## Price history and dated events (price cache, split-adjusted closes)

| Date | Close / move | Event | Source |
|---|---|---|---|
| 2025-01-28 | 234.08 (5-yr high) | — | price cache |
| 2025-01-30 | 202.55 (-11.4%) | Q4 2024 on 01-29: FY25 subscription guide $12,635-12,675M (18.5-19%) vs a consensus of about $12.83B; Q1 guide $2,995-3,000M vs ~$3.04B; ~$175M FX headwind; federal H2-weighted after the change of administration | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000007/erq4fy24.htm); consensus per [Yahoo/Jefferies](https://finance.yahoo.com/news/servicenow-falls-despite-q4-earnings-221503686.html) (third-party) |
| 2025-03-10 / 04-03 / 04-04 | -7.9% / -6.1% / -6.8%; low 144.33 on 04-04 (-38% from high) | Market-wide tariff sell-off; no company-specific event found | price cache |
| 2025-04-24 | 187.71 (+15.5%) | Q1 2025 beat: subscription $3,005M, cRPO +22% | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000124/erq1fy25.htm) |
| 2025-07-03 | 208.94 (2025 H2 high) | Q2 2025 on 07-23: +4.2% next day; federal headwinds flagged | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000274/erq2fy25.htm) |
| 2025-10-29/30 | -2.8% / +2.5% | Q3 2025: beat, split announced, shutdown may affect deal timing | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000305/erq3fy25.htm) |
| Nov 2025 | 183.86 → 162.48 (-11.6% month) | No company-specific event found (broad tech/AI sell-off, unverified) | price cache |
| 2025-12-15 | 153.04 (-11.5%) | Bloomberg report (weekend of 12-13/14) of talks to buy Armis for up to $7B; deal announced 12-23 at $7.75B cash | [Yahoo](https://finance.yahoo.com/news/servicenow-shares-plunge-armis-deal-152751931.html), [CNBC](https://www.cnbc.com/2025/12/23/servicenow-armis-cybersecurity-acquisition.html) |
| 2026-01-29 | 116.73 (-9.9%) | Q4 2025 on 01-28: beat; FY26 subscription guide 20.5-21% (third-party says above consensus); $5B buyback + $2B ASR; stock pulled into the AI-agent software sell-off | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000005/erq4fy25.htm), [TIKR](https://www.tikr.com/blog/servicenow-stock-is-down-33-in-2026-could-q1-earnings-be-the-turning-point) |
| 2026-02-03 / 02-05 | -7.0% / -7.6% (102.63) | "SaaSpocalypse": Anthropic's Claude Cowork plugins (01-30) triggered a ~$1T software sell-off on Feb 3-5 | [Axios](https://www.axios.com/2026/02/03/ai-software-anthropic-stock-market), [Morningstar](https://www.morningstar.com/markets/what-know-about-software-stock-selloff) |
| 2026-04-09 | -7.9% | ServiceNow replaced its five package tiers with three AI-native tiers (Foundation/Advanced/Prime), AI no longer sold as an add-on, legacy SKUs end of sale 2026-07-01; same week Anthropic's "Mythos" model news hit software/security stocks | [ServiceNow newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-moves-beyond-the-sidecar-AI-era-giving-customers-a-complete-AI-native-experience-across-all-products-and-packages/default.aspx), [Motley Fool](https://www.fool.com/investing/2026/05/03/why-servicenow-stock-fell-16-in-april/) |
| 2026-04-10 | 83.00 (-7.6%), all-time 5-yr low, -64.5% from high | UBS downgrade Buy → Neutral, PT $170 → $100: AI agents a bigger threat, non-AI app budget pressure | [CNBC](https://www.cnbc.com/2026/04/10/ubs-downgrades-servicenow-saying-ai-is-a-bigger-threat-than-first-believed.html) |
| 2026-04-23 | 84.78 (-17.7%, worst day on record per CNBC) | Q1 2026 on 04-22: ~75 bp subscription headwind from delayed large on-prem Middle East deals; Q2 guide GAAP op margin 3.5% / non-GAAP 26.5%; Armis dilution; gross margin 79% → 75% | [8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000054/erq1fy26.htm), [CNBC](https://www.cnbc.com/2026/04/22/servicenow-now-earnings-q1-2026.html), [CNBC sector](https://www.cnbc.com/2026/04/23/software-stocks-plunge-on-servicenow-ibm-results-ai-fears-escalate.html) |
| 2026-05-29 / 06-01 | +14.4% / +9.2% (135.86) | Enterprise-AI rotation after Dell results; Experian agent partnership | [24/7 Wall St](https://247wallst.com/investing/2026/05/29/servicenow-soars-14-on-enterprise-ai-rotation-as-dells-blowout-earnings-lift-software-sector/) |
| 2026-06-30 | 99.28 | Monthly RSI qualification month (cache: first oversold month 2026-06-30) | price cache |
| 2026-07-22/23 | -6.5% in session, +4.75% after hours, -3.7% next day | Q2 2026 beat and raise; about half the subscription beat was U.S. federal on-prem revenue pulled from Q3 into Q2 | [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000072/erq2fy26.htm), [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-beats-q2-2026-forecasts-shares-rebound-after-hours-93CH-4807190) |
| 2026-07-24 / 07-27 | +7.4% / +6.9% | Software rebound on AI rotation | [24/7 Wall St](https://247wallst.com/investing/2026/07/27/salesforce-surges-7-servicenow-jumps-8-workday-jumps-10-as-software-rebounds-on-ai-rotation/) |
| 2026-08-27 | 138.43 (+10.0%) | Salesforce Q2 beat and Anthropic partnership lifted workflow software | [Benzinga](https://www.benzinga.com/markets/tech/26/08/61473602/servicenow-stock-jumps-on-enterprise-ai-momentum) |
| 2026-09-14 | 142.35 (+7.4%) | PT raises: Needham $115 → $155, BTIG $150 → $170, BMO $118 → $150; rotation out of AI infrastructure | [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-heads-into-the-open-after-a-7-4-percent-jump/70108715), [24/7 Wall St](https://247wallst.com/investing/2026/09/14/servicenow-climbs-5-as-software-sidesteps-ai-selloff-adobe-gains-4-salesforce-ticks-up/) |
| 2026-09-25 | 135.62 | Friday close; -42.1% from high, +63% from the April low | price cache |

## AI, pricing and seat exposure

- Now Assist net new ACV more than doubled y/y in Q4 2025; Now Assist ACV $600M+ at Q4 2025 with a $1B+ 2026 target (Q4 2025 8-K; Fool transcript).
- "ServiceNow AI" crossed $1B ACV in Q2 2026; management says it is tracking ahead of a $1.5B end-2026 target and a 30%-of-ACV-by-2030 goal (Q2 2026 8-K; Investing.com transcript).
- Pricing: hybrid seat + consumption ("assists"); AI-native SKUs 20-30% price uplift, Pro Plus >30%; "50% of new business already non-seat based"; McDermott on seat compression: "Not at all," with active seats rising (Investing.com Q2 2026 transcript — management claims, not independently verified).
- April 9, 2026 repackaging to Foundation / Advanced / Prime with AI bundled; legacy SKUs end of sale July 1, 2026 (ServiceNow newsroom link above; practitioner guides e.g. https://www.servicenow.com/community/itsm-articles/itsm-licensing-in-april-2026-foundation-advanced-and-prime-in/ta-p/3544380).
- Q2 2026 deals: 123 transactions >$1M net new ACV (+~40%), 658 customers >$5M ACV (+23%); security and risk in 16 of the top 20 deals (8-K; transcript).
- Gross-margin pressure from hyperscaler partnerships and AI consumption was acknowledged on the Q2 2026 call (transcript summary).

## Federal

- 2025: budget constraints at U.S. agencies flagged in Q2 and Q3 2025 releases; Q3 2025 release warned the shutdown could affect deal timing. Q4 2025 call: global government up 80% y/y despite the shutdown (Fool transcript).
- Q2 2026: "strong U.S. Federal demand" pulled on-prem revenue into Q2 from Q3 (8-K), roughly half the Q2 beat (transcript).
- One federal channel partner = 13% of revenue (10-Q).
- A continuing resolution signed 2026-09-02 funds the government to Dec 11, 2026 (secondary sources: https://www.nbcnews.com/politics/congress/senate-leaders-reach-deal-avert-shutdown-2026-elections-rcna590564, https://govtschemes.org/government-shutdown-october-2026/); verify before relying on it.

## Consensus and targets (third-party)

- Yahoo Finance analysis page, read 2026-09-28 (https://finance.yahoo.com/quote/NOW/analysis/): Q3 2026 revenue $4.1B / EPS $1.03 (39 analysts); Q4 2026 $4.36B / $1.17; FY2026 revenue $16.22B / EPS $4.07 (44); FY2027 revenue $19.26B (+18.8%) / EPS $5.01 (+23%). EPS is the adjusted (non-GAAP) basis (stockanalysis.com says so explicitly: https://stockanalysis.com/stocks/now/forecast/). The page showed 34 down vs 3 up revisions to the current-quarter EPS in the last 7 days: **cause unverified**, could be a data artefact.
- Price targets: average ~$145 (stockanalysis, 49 analysts, range $72-248); ~$146 average per ad-hoc-news on 2026-09-14.
- A Simply Wall St snippet (search result only, page returned 403) says the 2026 EPS estimate fell from $2.01 to $1.55 — likely the statutory (GAAP) estimate; **unverified**. If right, it implies ~$0.81 GAAP EPS in H2 2026, higher than the derived Q3 estimate above.

## Valuation working

- Market cap $140.2B (fundamentals cache), EV $144.0B; net debt $3.79B in the cache counts leases ($0.94B) and excludes $2.04B long-term securities; debt ex leases minus all marketable securities ≈ $0.8B net debt.
- Non-GAAP P/E: 33x FY2026 consensus, 27x FY2027; at the Jan 2025 high 84x FY2024 non-GAAP EPS ($234.08 / $2.78).
- Reverse DCF (derived; 9% discount, 3% terminal growth, 10 years): EV $144B needs ~8%/yr FCF growth on 2026 FCF of ~$5.7B (35% × $16.22B); ~16%/yr if SBC (~$2.6B annualised from Q2) is treated as a cash cost.
- Scenario inputs: see thesis section 5 (revenue paths from the FY2026 consensus $16.22B; non-GAAP net margin = non-GAAP operating margin × 0.79 for a 21% tax rate and ~zero net interest).

## Open questions no source closed

1. Which strategic investment produced the $273M Q2 2026 unrealised gain, and whether further marks (up or down) are likely in Q3 2026.
2. Why the 2026 GAAP effective tax rate is ~30-44% versus 17.6% in H1 2025 (non-deductible Armis items? GILTI? SBC shortfalls?). No company explanation found.
3. Confirmed Q3 2026 report date (third-party listings say Oct 28; no company press release found) and 10-Q filing date relative to the Oct 30 month-end.
4. Organic cRPO growth excluding Armis/Veza/Moveworks; the company gives subscription contributions, not cRPO contributions.
5. Moveworks' contribution to 2026 growth (~100 bp vs "1 bp" in two summaries).
6. Whether the revolver has any financial-ratio covenant (credit agreement exhibit not read).
7. Renewal rate and seat counts at renewal: management asserts active seats are rising; no disclosed metric found for 2026.
8. Consensus GAAP EPS for Q3 2026 (only the non-GAAP $1.03 was found).
9. Remaining buyback authorisation after the H1 2026 $2.2B repurchases.
