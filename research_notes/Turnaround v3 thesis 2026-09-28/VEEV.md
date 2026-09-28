# VEEV (Veeva Systems) — research notes for the turnaround v3 thesis, 2026-09-28

Working notes behind `turnaround_backtest_v3/thesis/VEEV.md`. Research tooling, not investment advice.
Primary sources first (SEC 8-K earnings releases, 10-Q/10-K, company prepared remarks), then news; consensus and analyst figures are third-party and labelled so. Price moves are close-to-close from the local cache `turnaround/cache/prices/VEEV.csv` unless a source is quoted.

Fiscal year ends January 31: FY2027 = Feb 2026 - Jan 2027. Latest quarter Q2 FY2027 ended 2026-07-31, reported 2026-08-26 (after the close), 10-Q filed 2026-08-27.

## Quarterly table (Q4 FY2024 - Q2 FY2027)

$ millions except per share. Growth y/y as reported. "Next-Q guide" and "FY guide" are the guidance given with that quarter's results.

| Quarter (end) | Reported | Total revenue | y/y | Subscription | y/y | GAAP diluted EPS | Non-GAAP EPS | Next-Q revenue guide | FY revenue guide at the time | FY non-GAAP EPS guide | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q4 FY24 (2024-01-31) | 2024-02-29 | 630.6 | +12% | 521.5 | +13% | 0.90 | 1.38 | 640-643 | FY25 2,725-2,740 | ~6.16 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305224000008/veev-2024131q424xex991.htm) |
| Q1 FY25 (2024-04-30) | 2024-05-30 | 650.3 | +24% | 534.0 | +29% | 0.98 | 1.50 | 666-669 | FY25 2,700-2,710 (cut) | ~6.16 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305224000019/veev-20240430q125xex991.htm) |
| Q2 FY25 (2024-07-31) | 2024-08-28 | 676.2 | +15% | 561.3 | +19% | 1.04 | 1.62 | 682-685 | FY25 2,704-2,710 | ~6.22 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305224000058/veev-20240731q225xex991.htm) |
| Q3 FY25 (2024-10-31) | 2024-12-05 | 699.2 | +13% | 580.9 | +17% | 1.13 | 1.75 | 696-699 | FY25 2,722-2,725 | ~6.44 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305224000071/veev-20241031q325xex991.htm) |
| Q4 FY25 (2025-01-31) | 2025-03-05 | 720.9 | +14% | 608.6 | +17% | 1.18 | 1.74 | 726-729 | FY26 3,040-3,055 | ~7.32 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305225000006/veev-20250131q425xex991.htm) |
| Q1 FY26 (2025-04-30) | 2025-05-28 | 759.0 | +17% | 634.8 | +19% | 1.37 | 1.97 | 766-769 | FY26 3,090-3,100 | ~7.63 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305225000037/veev-20250430q126xex991.htm) |
| Q2 FY26 (2025-07-31) | 2025-08-27 | 789.1 | +17% | 659.2 | +17% | 1.19 | 1.99 | 790-793 | FY26 3,134-3,140 | ~7.78 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305225000063/veev-20250731q226xex991.htm) |
| Q3 FY26 (2025-10-31) | 2025-11-20 | 811.2 | +16% | 682.5 | +17% | 1.40 | 2.04 | 807-810 | FY26 3,166-3,169 | ~7.93 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305225000074/veev-20251031q326xex991.htm) |
| Q4 FY26 (2026-01-31) | 2026-03-04 | 836.0 | +16% | 707.7 | +16% | 1.45 | 2.06 | 855-858 | FY27 3,585-3,600 | ~8.85 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000007/veev-20260131q426xex991.htm) |
| Q1 FY27 (2026-04-30) | 2026-06-03 | 882.9 | +16% | 730.2 | +15% | 1.57 | 2.24 | 902-905 | FY27 3,635-3,645 | ~9.05 | [8-K](https://www.sec.gov/Archives/edgar/data/0001393052/000139305226000022/veev-20260430xex991.htm) |
| Q2 FY27 (2026-07-31) | 2026-08-26 | 928.0 | +18% | 766.8 | +16% | 1.66 | 2.35 | 932-935 | FY27 3,682-3,687 | ~9.21 | [8-K](https://www.sec.gov/Archives/edgar/data/0001393052/000139305226000032/veev-20260731xex991.htm) |

Full years: FY2025 revenue $2,746.6M, GAAP EPS $4.32, non-GAAP EPS $6.60; FY2026 revenue $3,195.3M (+16%), subscription $2,684.2M (+17%), GAAP operating income $916.4M, GAAP EPS $5.44, non-GAAP EPS $8.10, operating cash flow $1,415.2M (Q4 FY26 8-K above). FY2026 finished $140-155M above its initial revenue guide ($3,040-3,055M) and $0.78 above its initial non-GAAP EPS guide ($7.32).

Checks against the local SEC cache (`turnaround/cache/edgar/VEEV.json`): quarterly revenue and GAAP EPS in the table match the XBRL company facts; TTM GAAP EPS path 4.71, 4.86, 5.13, 5.44, 5.64, 6.10 matches (the quarterly sum 1.40+1.45+1.57+1.66 = 6.08 is the fundamentals cache's figure; the EDGAR cache's 6.10 is TTM net income over diluted shares; both are fine). TTM revenue $3,458.1M, net income $1,014.8M, operating income $1,034.9M.

Q2 FY27 detail ([10-Q](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000036/veev-20260731.htm), [prepared remarks](https://s206.q4cdn.com/200001835/files/doc_financials/2027/q2/Veeva-Q2-27-Earnings-Prepared-Remarks.pdf)):

| $M | Q2 FY27 | Q2 FY26 | Change |
|---|---|---|---|
| Subscription, Commercial Solutions | 347.4 | 307.5 | +13.0% |
| Subscription, R&D and Quality Solutions | 419.4 | 351.7 | +19.3% |
| Services and other | 161.2 | 129.9 | +24% |
| GAAP operating income | 275.0 | 195.9 | +40% (year-ago G&A carried the $31M IQVIA success fee) |
| Other income, net (mostly interest) | 74.5 | 69.5 | +7% |
| Effective tax rate | 21.8% | 24.5% | OBBBA FDDEI deduction |
| Net income | 273.4 | 200.3 | +37% |
| Diluted shares (M) | 165.06 | 167.69 | -1.6% |
| Non-GAAP operating income | 415.9 (44.8%) | 352.6 (44.7%) | +18% |
| Normalized billings | 768 | — | +19% (prepared remarks) |

FY2027 guidance path: initial (Mar 4, 2026) $3,585-3,600M / ~$1,590M non-GAAP op income / ~$8.85; Jun 3 $3,635-3,645M / ~$1,610M / ~$9.05; Aug 26 $3,682-3,687M / ~$1,640M / ~$9.21. Aug 26 detail: subscription ~$3,080M (+15%): Commercial ~$1,405M, R&D and Quality ~$1,675M; services $602-607M; normalized billings ~$3,870M (+14%); non-GAAP cash flow from operations ~$1,600M; diluted shares ~165M; FX tailwind ~$20M to revenue ([Q2 remarks](https://s206.q4cdn.com/200001835/files/doc_financials/2027/q2/Veeva-Q2-27-Earnings-Prepared-Remarks.pdf)). The Jun 3 raise included ~$10M of Ostro revenue for the last three quarters ([Q1 remarks](https://s206.q4cdn.com/200001835/files/doc_earnings/2027/q1/supplemental-info/Veeva-Q1-27-Earnings-Prepared-Remarks.pdf); call per [Motley Fool / MarketBeat transcripts](https://www.fool.com/earnings/call-transcripts/2026/06/04/veeva-veev-q1-2027-earnings-call-transcript/)).

## Stock history, dated (price cache; causes sourced)

5-year high $325.25 close on 2021-10-21. Month-end close Oct 2021 $317.01.

| Date | Close / move | Event | Source |
|---|---|---|---|
| 2021-12-02 | $262.41, -3.6% | Q3 FY22 (Dec 1): first FY2023 outlook $2,150-2,170M revenue at a ~38% non-GAAP operating margin; FY2022 guide was ~$753M on ~$1,844M (~41%) | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305221000037/veev-20211031q322xex991.htm) |
| 2022-03-03 | $193.16, -16.2% | Q4 FY22 (Mar 2): FY2023 guide $2,160-2,170M, non-GAAP EPS ~$4.02, below consensus; BofA downgrade to neutral ($300 → $220) saying growth and margins may have peaked; Needham $327 → $270 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305222000011/veev-2022131q422xex991.htm); [Motley Fool](https://www.fool.com/investing/2022/03/04/why-veeva-systems-stock-was-plunging-this-week) |
| 2022-09-01 | $171.42, -14.0% | Q2 FY23 (Aug 31): FY2023 revenue cut to $2,140-2,145M from $2,165-2,175M; Q3 guide $545-547M vs ~$558M consensus; Piper, Barclays, UBS cut targets | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305222000033/veev-20220731q223xex991.htm); [Benzinga](https://www.benzinga.com/news/earnings/22/09/28722637/why-veeva-systems-stock-is-plunging-today) |
| 2022-10-14 | $151.10 | Low of the first leg (-54% from the high), amid the 2022 growth-stock de-rating | price cache |
| 2022-12-02 | $174.90, -8.6% | Q3 FY23 (Dec 1): Veeva said it would not renew the Salesforce platform agreement when it ends in Sept 2025 and would move CRM to Vault | [Motley Fool](https://www.fool.com/investing/2022/12/08/salesforce-and-veeva-systems-are-set-to-sever-ties/); [IntuitionLabs](https://intuitionlabs.ai/articles/veeva-salesforce-split-pharma-crm-shake-up) (date Dec 1, 2022, secondary) |
| FY2024 (Feb 2023 - Jan 2024) | — | Termination-for-convenience rights standardized in master subscription agreements from Feb 1, 2023; revenue on those orders recognized as invoiced, so reported growth dropped: Q1 FY24 revenue +4%, subscription +3% | [Q4 FY24 8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305224000008/veev-2024131q424xex991.htm); [Q1 FY24 8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305223000031/veev-20230430q124xex991.htm) |
| 2023-06-01 | $198.30, +19.7% | Q1 FY24 beat | price cache (cause not researched further) |
| 2023-11-09 | $166.60, -14.2% | Investor day: FY2025 revenue floor cut to ≥$2,750M from ≥$2,800M; FY2024 revenue cut to $2,353-2,355M (services -$17M); slide notes a "$90 million estimated TFC impact" to FY24 | [8-K exhibit](https://www.sec.gov/Archives/edgar/data/1393052/000139305223000057/investorday8-kexhibit.htm) |
| 2024-05-31 | $174.25, -10.3% | Q1 FY25 (May 30): FY2025 revenue guide cut to $2,700-2,710M from $2,725-2,740M (EPS guide unchanged) | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305224000019/veev-20240430q125xex991.htm); reason not verified from a primary text |
| 2024-12-24 | — | Bloomberg (via Yahoo): Salesforce has signed 40+ Life Sciences Cloud customers incl. a top-3 pharma; Veeva confirmed one top-20 customer left for Salesforce; GSK and Novo Nordisk pledged to stay | [Yahoo/Bloomberg](https://finance.yahoo.com/news/salesforce-stokes-veeva-fight-snagging-153210048.html) |
| 2025-05-29 | $279.04, +19.0% | Q1 FY26 beat-and-raise ($3,090-3,100M; $7.63); CFO: crossed the $3B revenue run-rate goal | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305225000037/veev-20250430q126xex991.htm) |
| 2025-08-13 / 08-18 | — | IQVIA settlement signed Aug 13, announced Aug 18: all suits since 2017 dismissed with prejudice, no damages either way; Veeva paid ~$31M success fees to law firms (charged to G&A in Q2 FY26); mutual third-party-access agreements (IQVIA data usable in Veeva Network, Nitro, Veeva AI; IQVIA joins Veeva's CRO clinical data, technology, AI and services partner programs, uses Veeva EDC) | [FY26 10-K note 13](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000014/veev-20260131.htm); [Veeva release](https://www.veeva.com/resources/iqvia-and-veeva-announce-long-term-clinical-and-commercial-partnerships-and-resolution-of-all-disputes/); [Investing.com](https://www.investing.com/news/sec-filings/veeva-systems-and-iqvia-settle-litigation-with-mutual-data-access-agreements-93CH-4197857); Q2 FY27 10-Q MD&A |
| 2025-08-28 | $272.33, -7.2% | Q2 FY26 beat-and-raise; muted "expectations" reaction | [Yahoo/StockStory](https://finance.yahoo.com/news/why-veeva-systems-veev-stock-184326076.html) — **conflict:** the article gives -3.8% (likely intraday); the cache close-to-close is -7.2%, preferred |
| 2025-10-07 | $306.22 | 2025 high (5-year high still Oct 2021) | price cache |
| 2025-11-21 | $244.06, -9.8% | Q3 FY26 (Nov 20) beat-and-raise, but Gassner on the call: "We used to have 18 out of the top 20. Now we're maybe going to have 14 or so" (Vault CRM); -16.8% over 5 days | [transcript, Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-veeva-systems-q3-2026-beats-expectations-stock-dips-93CH-4371867); [Trefis](https://www.trefis.com/stock/veev/articles2/583721/veeva-systems-stock-drop-looks-sharp-but-how-deep-can-it-go/2025-11-22) |
| 2026-01-30 / 02-03 | $203.92 month-end; Feb 3 $190.80, -6.2% | Software sell-off after Anthropic released Claude Cowork plugins (Jan 30), sharpest on Feb 3 | [CNN](https://www.cnn.com/2026/02/04/investing/us-stocks-anthropic-software); [CNBC](https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html). Feb 2026 = first oversold month for the screen |
| 2026-03-05 | $196.06, +4.0% | Q4 FY26 (Mar 4): FY2027 guide $3,585-3,600M, ~$8.85; 125+ Vault CRM live, 10 top-20 committed, ~14 expected by year-end | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000007/veev-20260131q426xex991.htm) |
| 2026-03-09 | — | Ostro (Rise Healthcare Tech) acquired for $90M ($70M net of cash): conversational AI for brands | Q2 FY27 10-Q note 2 |
| 2026-04-09 / 04-10 | $157.08 (-5.7%) / **$151.43 (-3.6%) low** | Second leg of the SaaS sell-off (a viral, later deleted Michael Burry post on SaaS vs AI agents is cited); VEEV -51% from Oct 7, 2025. April month-end P/E 28.7 = 5-year low (valuation cache) | [tech-insider.org](https://tech-insider.org/saas-stock-crash-ai-agents-2-trillion-2026/) (low-quality secondary); [CNBC on Burry buying the dip](https://www.cnbc.com/2026/04/16/burry-buys-the-dip-in-salesforce-and-other-software-stocks-after-sell-off.html); Seeking Alpha upgrade mid-April notes ~30% YTD fall ([SA](https://seekingalpha.com/article/4889896-veeva-systems-not-a-likely-victim-of-total-ai-disruption-buy-the-dip-upgrade)) |
| 2026-04-20 | — | GC Josh Faddis to retire Nov 1, 2026 | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000018/veev-20260420.htm) |
| 2026-06-03 / 06-04 | $178.72 / $178.60 | Q1 FY27 beat-and-raise; Piper Sandler $285 → $235 (AI revenue will take longer), Mizuho $295 → $270 (longer-term AI disruption risk, 27x P/E; caution on Development Cloud subscription uptake) on Jun 4 | [Piper, Investing.com](https://www.investing.com/news/analyst-ratings/piper-sandler-cuts-veeva-systems-stock-price-target-on-ai-timing-93CH-4726718); [Mizuho, Investing.com](https://www.investing.com/news/analyst-ratings/mizuho-cuts-veeva-systems-stock-price-target-on-ai-disruption-risk-93CH-4726451) |
| 2026-06-22 | $153.16 | Retest of the low | price cache |
| June 2026 | — | Copli acquired; Falcon MLR launched (H1 acquisitions $81.8M net cash, Ostro + Copli) | Q2 remarks; 10-Q cash flow |
| 2026-08-11 | — | Eli Lilly commits to Vault CRM globally | [Veeva](https://www.veeva.com/resources/veeva-vault-crm-selected-by-eli-lilly-and-company/) |
| 2026-08-20 | — | President and Chief Customer Officer Tom Schwenger resigns effective Oct 2, 2026 (CEO role at a Veeva partner); Dan Rizzo becomes EVP Sales, Consulting and Services | [8-K](https://www.sec.gov/Archives/edgar/data/1393052/000121390026092096/ea0302765-8k_veeva.htm) |
| 2026-08-25 | — | Biogen and Regeneron commit to Vault CRM | [Veeva (Biogen)](https://www.veeva.com/resources/veeva-vault-crm-selected-by-biogen/); [StockTitan (Regeneron)](https://www.stocktitan.net/news/VEEV/veeva-vault-crm-selected-by-qu0mjgsjlgml.html) |
| 2026-08-27 | $282.13, +15.2% | Q2 FY27 beat (EPS $2.35 vs $2.22 consensus, revenue $928M vs ~$905M, third-party) and raise; "best CRM quarter ever", 12 top-20 commitments | [8-K](https://www.sec.gov/Archives/edgar/data/0001393052/000139305226000032/veev-20260731xex991.htm); [Motley Fool](https://www.fool.com/investing/2026/08/27/why-veeva-systems-stock-skyrocketed-today/) |
| 2026-09-15 | — | Amgen announces a global Vault CRM deployment | [StockTitan](https://www.stocktitan.net/news/VEEV/leading-biotech-selects-veeva-vault-crm-uax8r7n6w16m.html) |
| 2026-09-23 | $270.75, +3.8% | Release: "global commitments from 14 of the top 20 biopharmas", a new unnamed top-20 commitment, 190+ live | [Veeva](https://www.veeva.com/resources/vault-crm-extends-market-leadership-as-another-top-20-biopharma-chooses-veeva/); [StockTitan](https://www.stocktitan.net/news/VEEV/vault-crm-extends-market-leadershipas-another-top-20-biopharma-rv4prz5u6smy.html) |
| 2026-09-25 | **$280.68** | Friday close; +85% from the April low, -13.7% from the 2021 high | price cache |

The July-August 2026 run from ~$180 to ~$248 before earnings came with no single dated company event found; it overlaps the sector rebound and the Lilly (Aug 11) win. Unverified what drove the Aug 7 (+5.8%) and Aug 13 (+4.6%) moves.

## Earnings peak or multiple?

- At the Oct 2021 high the public TTM GAAP EPS was $2.62 (quarter to 2021-07-31): trailing P/E ~124 on $325.25; P/S 30.9 at the Oct 2021 month-end (valuation cache). TTM GAAP operating margin then 27.2%, net margin 25.5% (EDGAR cache).
- Today: TTM GAAP EPS $6.10 (2.3x), operating margin 29.9%, net margin 29.3% (EDGAR cache). Non-GAAP operating margin: FY2022 guide ~41% vs FY2027 guide ~44%.
- EPS dips in the period were small: TTM EPS 2.66 (Oct 2021) → 2.42 (Jul 2022, -9%, investment year + margin guide to ~38%); 3.48 (Oct 2023) → 3.22 (Jan 2024, -7%, TFC timing). Neither approached the rule's 15% trigger.
- Conclusion: not an earnings peak; a peak multiple.

## Business facts used in the thesis

- **CRM migration:** Veeva CRM (on Salesforce) supported until Dec 31, 2029 ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000014/veev-20260131.htm)); the 2022-era "Sept 2030 wind-down" in secondary sources is superseded. Vault CRM live customers: 80+ (May 2025), 100+ (Aug 2025), 115 (Nov 2025), 125+ (Mar 2026), 150+ (Jun 2026, 27 added in Q1), 180+ incl. five top-20s in major markets (Aug 2026), 190+ (Sept 23, 2026). Top-20 commitments: 7th in Aug 2025 (Q2 FY26 8-K), 10 (Mar 2026), 12 (Aug 26, 2026), 14 (Sept 23, 2026) — the same "14 or so" management guided to in Nov 2025, when it said it used to have 18 of 20 on Veeva CRM. Company: "migrations to accelerate through 2027 and 2028" (Q1 remarks); focus now on "CRM win backs within the top 20 that did not select Vault CRM" (Q2 remarks).
- **Market share claims (management, Wells Fargo conference Sept 9, 2026, secondary summary):** win rate above 80% outside the top 20; expects >70% long-term share of life-sciences CRM; the $6B 2030 revenue run-rate goal covers existing life-sciences products only, excludes AI and Aspen CRM ([Investing.com](https://ng.investing.com/news/stock-market-news/veeva-at-wells-fargo-healthcare-conference-ai-and-crm-drive-growth-93CH-2690067)). The $6B run-rate goal itself is in the company's own Q3 FY26 release ("on track toward our 2030 $6 billion revenue run-rate goal").
- **Competitors (10-Q risk factors):** CRM mainly Salesforce (Life Sciences Cloud); "IQVIA ... has licensed its CRM software to Salesforce"; Data Cloud and Crossix compete with IQVIA, Ipsos, Definitive; Development/Quality compete with IQVIA, Dassault, OpenText, Oracle, Honeywell.
- **Veeva AI:** three layers. Vault AI (agents inside Vault apps; standard agents and custom-agent tools GA across Vault in August 2026). Veeva Falcon (agentic labor for clinical, regulatory, safety): five early adopters, first go-lives "this year", first top-20 go-live "first half of next year"; Falcon MLR (from the Copli deal) — management believes it can eliminate at least 70% of manual MLR review labor within five years. Ostro (conversational AI for brands). Pricing: "Some agents are charged by usage, while others are part of a fixed-price subscription license" (Q1 remarks); Vault AI consumption/token-based, Falcon possibly outcome-based or enterprise license (Wells Fargo summary). No AI revenue disclosed.
- **R&D and Quality:** Q2 FY27 clinical 30+ new customers (eTMF, EDC, CTMS strong); a large enterprise biopharma selected EDC; Safety >100 customers, second top-20 for Safety Workbench; Quality 30+ new customers (≥20 each in QualityDocs, QMS, Training); LIMS early adopters live. Q1: 18 QualityDocs, 23 QMS, 20 Training; 18 PromoMats. Nine of the top 20 use Veeva EDC (Q2 call, per [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/31/veeva-veev-q2-2027-earnings-call-transcript/) summary — not verified verbatim).
- **Data/Crossix:** Crossix growth in Measurement and Audiences; data network "well over 100 billion unique patient records, covering more than 300 million U.S. patients" (Q1 remarks); 14 new Data Cloud customers in Q2 incl. eight Compass brand wins.
- **Aspen CRM:** horizontal (all-industry) CRM announced early August 2026, broader early-customer availability "later this year" (Q2 remarks). Cost not disclosed.
- **Headcount:** 7,928 employees at Jan 31, 2026 (+637); +239 in Q1 FY27 (~25% Ostro), +298 in Q2 (graduate hiring).
- **Customers:** 1,552 at Jan 31, 2026 (10-K).
- **Pharma policy:** 10-K risk factors cite IRA negotiation, the administration's international reference pricing proposals and tariffs on life-sciences end products as risks to customer IT spending; commercial sales-rep reductions have "negatively impacted sales of our solutions, including Veeva CRM". Section 232 pharma tariffs: proclamation Apr 2, 2026, default 100% on patented drugs, 20% with approved onshoring plans, 0% for companies with MFN and onshoring agreements (0% expires Jan 20, 2029); effective July 31, 2026 for certain large companies and Sept 29, 2026 for all others ([White House](https://www.whitehouse.gov/presidential-actions/2026/04/adjusting-imports-of-pharmaceuticals-and-pharmaceutical-ingredients-into-the-united-states/); [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/04/president-trump-announces-section-232-tariffs-on-pharmaceuticals-and-active-pharmaceutical-ingredients/)). MFN: 17 agreements with large manufacturers, then nine mid-sized ones on Aug 31, 2026; 26 drugmakers covering 89% of the brand market ([Mintz, Sept 23, 2026](https://www.mintz.com/insights-center/viewpoints/2146/2026-09-23-pharmaceutical-policy-motion-continued-trump)). Management on the Q2 call: pharma marketing budgets strong; the industry has "gotten used to" the moving parts (Motley Fool transcript summary).
- **EU Data Act:** since Sept 12, 2025 EU customers may cancel subscriptions without cause after notice and a transition period (FY26 10-K). Master subscription agreements for multi-year orders generally carry termination-for-convenience rights anyway.

## Balance sheet, obligations (Q2 FY27 10-Q; FY26 10-K)

- Cash $1,812.0M + short-term investments $5,430.9M = $7,242.9M; $102M held outside the U.S.
- **No borrowings and no credit facility:** the FY26 10-K and Q2 FY27 10-Q contain no "credit facility", "revolving" or "line of credit" disclosure (text search). Liquidity is the cash pile and operating cash flow.
- Lease liabilities $151.7M ($14.6M current, $137.1M long-term); undiscounted payments: rest of FY27 $7.6M, FY28 $13.8M, FY29 $22.3M, FY30 $21.7M, FY31 $19.5M, thereafter $112.7M (total $197.5M); operating lease expense $11M in H1 FY27; weighted remaining term 9.5 years.
- Operating cash flow H1 FY27 $1,365.8M (H1 FY26 $1,115.6M; increase partly from lower tax payments under OBBBA). Capex small (long-term asset purchases $9.8M in H1).
- Buybacks: $2B program authorized Jan 2026, two-year term; $472.7M spent in H1 FY27 (2.66M shares at ~$175); ~$1.4B remaining at July 31, 2026.
- Hosting commitments to AWS and Salesforce: purchase-obligation amounts not found in the filings searched (open question).
- Other income TTM ≈ $292.5M (FY26 $278.1M − H1 FY26 $134.5M + H1 FY27 $148.9M); FY26 interest income, net $267.2M (10-K note 11). Stock-based compensation TTM ≈ $494.6M (FY26 $472.7M − H1 FY26 $234.2M + H1 FY27 $256.1M), ~14% of revenue. Options outstanding 14.9M (avg strike $181.57); unrecognized option cost $312M.

## Consensus (third-party)

| Source (date) | FY2027 (Jan 2027) | FY2028 | FY2029 |
|---|---|---|---|
| Zacks via Yahoo (Sept 17, 2026) — non-GAAP EPS / revenue | $9.22 / $3.69B (+15.3%) | $10.16 (+10.2%) / $4.13B (+12%) | — |
| MarketScreener (accessed 2026-09-28) — revenue / GAAP EPS / EBIT (≈ non-GAAP op income) | $3,690M / $6.53 / $1,643M | $4,142M / $7.31 / $1,852M | $4,647M / $8.42 / $2,101M |
| StockAnalysis (data Sept 24, 2026) | revenue $3.69B, EPS $9.24 | — | — |
| Yahoo forward EPS in the fundamentals cache | — | $10.25 (basis not labelled; consistent with FY2028 non-GAAP) | — |

Price targets (third-party): average $297.30, range $180-350, 29 analysts; 12 strong buy, 8 buy, 8 hold, 1 strong sell ([StockAnalysis](https://stockanalysis.com/stocks/veev/forecast/); [MarketScreener](https://www.marketscreener.com/quote/stock/VEEVA-SYSTEMS-INC-14551091/finances/)). Pre-Q2 consensus (Zacks, Aug 26): Q2 EPS $2.22, FY27 $9.05 / $3.64B ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/veeva-systems-veev-q2-earnings-212004513.html)). May 28, 2026 (Zacks): FY27 $8.86 / $3.59B, FY28 $9.81 / $4.01B ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/veeva-systems-inc-veev-trending-130006611.html)) — FY28 EPS estimate +3.6% since May.

Note: the fundamentals cache's "implied forward EPS growth +68.6%" compares a non-GAAP forward estimate ($10.25) with GAAP TTM EPS ($6.08); it is a basis mismatch, not a growth forecast.

## Valuation arithmetic (derived)

- Market cap $45.4B on 161.8M shares outstanding; $46.3B on 165.06M diluted. EV ≈ $39.2B (diluted cap − $7.24B cash + $0.15B leases).
- P/E: 46x TTM GAAP; 30.4x FY27 and 27.6x FY28 consensus non-GAAP; 38x FY28 and 33x FY29 consensus GAAP (MarketScreener). EV / FY27 revenue guide ≈ 10.6x.
- Cash is $43.9 a diluted share; after-tax interest ≈ $1.38 a share (22% tax) ≈ 23% of TTM GAAP EPS.
- Reverse DCF on OCF less stock comp ($1.666B − $0.495B = $1.17B), 10 years then 3% terminal: 8% discount → 9.2% a year implied growth; 9% → 11.7%; 10% → 14.1%.
- Scenario math (thesis section 5): EPS = (FY2030 revenue × GAAP operating margin + interest income) × (1 − tax) / diluted shares. Bear 4.64B × 27% + 0.29B, 23% tax, 158M → $7.52; base 5.18B × 32% + 0.32B, 22%, 160M → $9.64; bull 5.60B × 35% + 0.33B, 22%, 162M → $11.03.

## Conflicts between sources

- **Which August 2026 wins were top 20:** the company says two top-20s and "one just outside our top 20" selected Vault CRM in August (Q2 remarks). Named August wins: Lilly (Aug 11), Biogen and Regeneron (Aug 25). A Yahoo call summary names Lilly and Biogen as the top-20 wins; the Motley Fool transcript summary names Biogen and Regeneron. Which one is "just outside" is not resolved; company counts (12, then 14) are preferred over any name list.
- **Top-20 count:** a Motley Fool article (Aug 27) says 13 of the top 20 committed vs six for Salesforce; the company release the day before says 12. Company figure preferred. The 14 at Sept 23 is from the company.
- **Veeva CRM end of support:** secondary sources say the Salesforce-based product runs until Sept 2030; the FY26 10-K says supported until Dec 31, 2029. 10-K preferred.
- **Aug 28, 2025 move:** -7.2% close-to-close (cache) vs -3.8% (StockStory article, likely intraday). Cache preferred.
- **Aug 27, 2026 move:** +15.2% close-to-close (cache); articles cite "as much as 20.9%" and "+16.48%" (intraday/other basis). Cache preferred.

## Open questions no source closed

1. Salesforce's own top-20 count and the names of the six top-20 biopharmas not on Vault CRM (the "six for Salesforce" figure is a derivation: 20 − 14). Whether any of the six can be won back before the Dec 31, 2029 end of Veeva CRM support.
2. Price of Vault CRM vs legacy Veeva CRM at migration: revenue uplift, flat, or discounted to hold accounts. No disclosure found.
3. Veeva AI revenue: no figure disclosed for Vault AI, Falcon or Ostro (beyond ~$10M of FY27 Ostro revenue in guidance). Falcon pricing model not final.
4. Whether AI reduces seat counts in Development Cloud (clinical operations, regulatory, safety users) — Mizuho flagged Development Cloud subscription uptake; no company data on seat trends.
5. Cost and loss profile of Aspen CRM (horizontal CRM); excluded from the $6B 2030 goal.
6. Reason for the May 30, 2024 FY25 revenue-guide cut; not found in a primary text.
7. Q3 FY2027 report date (not announced by Sept 28; last year Nov 20) and whether a 2026 investor day is scheduled (2025's was Oct 16, 2025).
8. The 2030 goal's segment split and margin component (secondary sources cite $4B R&D / $2B Commercial; unverified).
9. Hosting purchase commitments to AWS and Salesforce, and how the Salesforce hosting cost falls as customers leave Veeva CRM (gross-margin tailwind size unknown).
10. Impact of the President/Chief Customer Officer's departure (Oct 2, 2026) on sales execution.
