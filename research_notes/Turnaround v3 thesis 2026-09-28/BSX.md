# BSX (Boston Scientific) — working notes for the turnaround v3 thesis, 2026-09-28

Research date 2026-09-28 (before the open; last bar in the price cache is Friday 2026-09-25, close $43.92). Thesis file: `turnaround_backtest_v3/thesis/BSX.md`. Primary documents were downloaded from EDGAR for this pass and parsed locally: Q2 2026 10-Q, Q1 2026 10-Q, FY2025 10-K, Q3 2025 10-Q, the ten 8-K earnings releases Q1 2024 to Q2 2026, and the 2026 8-Ks (Feb 2, Feb 18, Feb 26, Mar 28, May 18 x2, Jul 21, Jul 29, Aug 26, Sep 7, Sep 21). Consensus, ratings and price targets are third-party and labelled as such. Research tooling, not investment advice.

## 1. Local cache (primary, point-in-time SEC data)

Source: `turnaround/cache/edgar/BSX.json` (fetched 2026-09-27), `fundamentals/BSX.json`, `valuation/BSX.json`, `prices/BSX.csv`.

| Quarter end | TTM revenue $M | TTM net income $M | TTM operating income $M | TTM EPS (GAAP) | Cash $M | Debt $M | Diluted shares M | Available |
|---|---|---|---|---|---|---|---|---|
| 2024-12-31 | 16,747 | 1,846 | 2,603 | 1.25 | 414 | 10,746 | 1,476.8 | 2025-02-18 |
| 2025-03-31 | 17,554 | 2,025 | 2,849 | 1.37 | 725 | 11,309 | 1,478.1 | 2025-05-01 |
| 2025-06-30 | 18,494 | 2,498 | 3,148 | 1.68 | 534 | 11,587 | 1,486.9 | 2025-08-01 |
| 2025-09-30 | 19,349 | 2,784 | 3,463 | 1.87 | 1,275 | 11,600 | 1,488.8 | 2025-11-03 |
| 2025-12-31 | 20,074 | 2,892 | 3,613 | 1.94 | 1,965 | 11,436 | 1,490.7 | 2026-02-17 |
| 2026-03-31 | 20,614 | 3,559 | 3,793 | 2.39 | 1,453 | 11,029 | 1,489.1 | 2026-05-01 |
| 2026-06-30 | 20,996 | 3,668 | 4,152 | 2.47 | 539 | 12,624 | 1,485.0 | 2026-08-03 |

- Stock splits in the EDGAR cache: 2-for-1 on 1998-12-01 and 2003-11-06 only. Close equals adjusted close throughout (no dividend). The 5-year high ($108.14 close, 2025-09-08) and today's $43.92 are on the same share basis; no split or spin-off distorts the -59.4%.
- **Data-quality flag (EV/EBITDA):** `da_ttm` is $412-471M for 2024-2025 and jumps to $1,394M at 2026-03-31. The FY2025 10-K cash-flow statement shows D&A of $1,368M (2024 $1,269M), so the pre-2026 rows carry depreciation only and understate EBITDA by roughly $0.9B (about a quarter). Historical EV/EBITDA in the rebuild is therefore inflated relative to today's reading, and the v3 EV/EBITDA percentile (0.12) is biased toward "cheap". Not recomputed; P/S (0.41) and EV/EBIT (0.10) are unaffected. The v3 rebuild gives EV/EBITDA 43.5 at the Sept 2025 high month from the Q2 2025 row; `valuation/BSX.json` shows 35.1 for the same month (different source/fetch — unresolved).
- **Data-quality flag (FCF):** `fundamentals/BSX.json` capex_ttm -$2,723M includes "payments for investments and acquisitions of certain technologies" (H1 2026 $1,730M, mainly the $1.5B MiRus stake). 10-K/10-Q: OCF TTM $4,529M (2025 $4,534M + H1'26 $1,822M − H1'25 $1,827M); PP&E TTM $904M ($876M + $372M − $344M); **FCF TTM ≈ $3,625M**, not $1,806M; P/FCF ≈ 17.6, not 35.2.
- Price legs (cache closes): see thesis section 2. Peer returns 2025-09-08 → 2026-09-25 from the same cache: MDT -4.7%, ABT -23.4%, SYK -30.7%, ISRG -13.8%, EW +7.6%, JNJ +52.3%, PEN +11.7%; XLV +21.3% and SPY +17.3% to 2026-09-14 (last bars). Large-cap medtech was weak, but BSX's -59% is mostly company-specific.
- Penumbra deal spread: PEN closed $318.89 on 2026-09-25. Blended consideration at BSX $43.92 = 0.73 × $374 + 0.27 × 3.8721 × $43.92 = **$318.94**. The market is pricing the deal as near-certain to close (my calculation; assumes the 73/27 proration holds).

## 2. Quarterly results and guidance (8-K earnings releases)

Releases: [Q1'24](https://www.sec.gov/Archives/edgar/data/885725/000088572524000040/q12024earningsrelease.htm), [Q2'24](https://www.sec.gov/Archives/edgar/data/885725/000088572524000060/q22024earningsrelease.htm), [Q3'24](https://www.sec.gov/Archives/edgar/data/885725/000088572524000070/q32024earningsrelease.htm), [Q4'24](https://www.sec.gov/Archives/edgar/data/885725/000088572525000007/q42024earningsrelease.htm), [Q1'25](https://www.sec.gov/Archives/edgar/data/885725/000088572525000023/q12025earningsrelease.htm), [Q2'25](https://www.sec.gov/Archives/edgar/data/885725/000088572525000039/q22025earningsrelease.htm), [Q3'25](https://www.sec.gov/Archives/edgar/data/885725/000088572525000046/q32025earningsrelease.htm), [Q4'25](https://www.sec.gov/Archives/edgar/data/885725/000088572526000006/q42025earningsrelease.htm), [Q1'26](https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000031/q12026earningsrelease.htm), [Q2'26](https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000051/q22026earningsrelease.htm).

| Quarter | Revenue $M | Reported growth | Organic growth | GAAP EPS | Adj. EPS | FY guidance given at this report (organic / adj. EPS) | Next-quarter adj. EPS guide |
|---|---|---|---|---|---|---|---|
| Q1 2024 | 3,856 | +13.8% | +13.1% | 0.33 | 0.56 | FY24 10-12% / $2.29-2.34 | $0.57-0.59 |
| Q2 2024 | 4,120 | +14.5% | +14.7% | 0.22 | 0.62 | FY24 13-14% / $2.38-2.42 | $0.57-0.59 |
| Q3 2024 | 4,209 | +19.4% | +18.2% | 0.32 | 0.63 | FY24 ~15% / $2.45-2.47 | $0.64-0.66 |
| Q4 2024 | 4,561 | +22.4% | +19.5% | 0.38 | 0.70 | FY25 10-12% / $2.80-2.87 | $0.66-0.68 |
| Q1 2025 | 4,663 | +20.9% | +18.2% | 0.45 | 0.75 | FY25 12-14% / $2.87-2.94 | $0.71-0.73 |
| Q2 2025 | 5,061 | +22.8% | +17.4% | 0.53 | 0.75 | FY25 14-15% / $2.95-2.99 | $0.70-0.72 |
| Q3 2025 | 5,065 | +20.3% | +15.3% | 0.51 | 0.75 | FY25 ~15.5% / $3.02-3.04 | $0.77-0.79 |
| Q4 2025 | 5,286 | +15.9% | +12.7% | 0.45 | 0.80 | **FY26 10-11% / $3.43-3.49** (reported 10.5-11.5%) | $0.78-0.80 |
| Q1 2026 | 5,203 | +11.6% | +9.4% | 0.90 | 0.80 | **FY26 6.5-8.0% / $3.34-3.41** (reported 7.0-8.5%) | $0.82-0.84 |
| Q2 2026 | 5,442 | +7.5% | +7.0% | 0.61 | 0.86 | **FY26 5-6% / $3.28-3.32** (reported 5.5-6.5%) | $0.80-0.82 (Q3 organic 3-5%) |

- FY2025: revenue $20.074B, +19.9% reported, +15.8% organic; GAAP EPS $1.94; adj. EPS $3.06 (2024 $2.51). — Q4'25 release.
- 2026 guidance no longer includes a GAAP EPS range (adjusted only) — Q4'25, Q1'26, Q2'26 releases.
- Sept 7, 2026 8-K (filed Sept 8): "unlikely to meet" Q3 and FY2026 net sales growth and adjusted EPS guidance because of the Aug 25 cyber incident; Q3 call on **Wednesday Oct 28, 2026**. — [8-K](https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000059/bsx-20260907.htm), [Aug 26 8-K](https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000056/bsx-20260826.htm).
- Adj. operating margin Q2 2026 28.4% (+70 bp), adj. gross margin 70.3%; FCF Q2 $1.29B — [Investing.com slides summary](https://www.investing.com/news/company-news/boston-scientific-q2-2026-slides-strong-quarter-softer-outlook-93CH-4820451) (third-party read of company slides).

### Franchise detail (10-Q/10-K revenue notes; $M)

| | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|
| Electrophysiology, total | 730 | 840 | 865 | 890 | 905 | 916 |
| EP, U.S. | 511 | 587 | 607 | 605 | 603 | 606 |
| Watchman, total | 425 | 486 | 512 | 535 | 506 | 507 |
| Watchman, U.S. | 390 | 446 | 470 | 485 | 462 | 459 |
| CRM | 578 | 590 | 578 | — | 578 | 585 |
| Urology | 633 | 676 | 682 | — | 646 | 684 |

Q4'25 = FY2025 10-K minus nine months from the Q3 2025 10-Q (my subtraction; the Q3 10-Q is on the pre-reorganisation segment layout, EP and Watchman lines unchanged). FY: EP $800M (2023) → $1,904M (2024) → $3,325M (2025); Watchman $1,274M → $1,516M → $1,958M. — [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/885725/000088572526000010/bsx-20251231.htm), [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/885725/000088572526000033/bsx-20260331.htm), [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000053/bsx-20260630.htm), [Q3 2025 10-Q](https://www.sec.gov/Archives/edgar/data/885725/000088572525000050/bsx-20250930.htm).

- U.S. EP has been flat at ~$605M a quarter for four quarters (Q3'25-Q2'26); Q2'26 U.S. EP +3.2% y/y, international EP +23% ($310M vs $252M).
- Watchman Q2'26 +4.3% y/y (U.S. +2.9%); 2025 growth was ~29%.

## 3. Dated events behind the fall

| Date | Close / move (cache) | Event | Source |
|---|---|---|---|
| 2025-09-08 | $108.14 (5-yr high) | — | cache |
| 2025-10-22 | $103.85, +4.0% | Q3'25: organic +15.3%, FY25 raised to ~15.5% organic, adj. EPS $3.02-3.04 | Q3'25 release |
| 2025-11-08 | no reaction (stock rose to $104.98 by 11-13) | AHA 2025: CLOSURE-AF (912 pts, Germany; LAAC failed non-inferiority vs physician-directed medical therapy, HR 1.28) and OCEAN (post-ablation rivaroxaban vs aspirin, stroke <1%/yr both arms) | [ACC CLOSURE-AF](https://www.acc.org/latest-in-cardiology/clinical-trials/2026/03/03/18/35/closure-af), [ACC OCEAN](https://www.acc.org/latest-in-cardiology/clinical-trials/2026/03/03/18/35/ocean) |
| 2025-12-22 | — | Abbott Volt PFA FDA approval (U.S. competitor) | [Abbott release](https://abbott.mediaroom.com/2025-12-22-Abbotts-Volt-TM-Pulsed-Field-Ablation-System-Receives-FDA-Approval-to-Treat-Patients-with-Atrial-Fibrillation) |
| 2026-01-15 | $90.03, -4.0% (vol 27.9M) | Penumbra agreement: $374/sh, EV ~$14.5B, ~73% cash / 27% stock (3.8721 BSX shares), cash ~$11B from cash + new debt | [BSX release](https://news.bostonscientific.com/2026-01-15-Boston-Scientific-announces-agreement-to-acquire-Penumbra,-Inc), [MedTech Dive](https://www.medtechdive.com/news/boston-scientific-penumbra-deal-takeaways/809988/) |
| 2026-02-04 | $75.50, **-17.6%** (vol 78.2M) | Q4'25 beat (adj. $0.80 vs $0.78 est.), but FY26 organic 10-11% vs 15.8% in 2025, adj. EPS $3.43-3.49 vs $3.47 consensus; Q1 guide $0.78-0.80 vs $0.79; EP $890M flat q/q, ~$33M below consensus | Q4'25 release; [Yahoo/Reuters](https://finance.yahoo.com/news/boston-scientific-shares-slide-cautious-130211137.html); [MassDevice](https://www.massdevice.com/boston-scientific-q4-2025-beats/) (third-party consensus) |
| 2026-02-26 | — | New $3.0B revolver (2031), $2.0B 364-day revolver, $6.0B 364-day delayed-draw term loan for Penumbra | [8-K](https://www.sec.gov/Archives/edgar/data/885725/000088572526000017/bsx-20260226.htm), Q2'26 10-Q |
| 2026-03-05 | — | Securities class action filed (D. Mass.), class period 2025-07-23 to 2026-02-03, alleges U.S. EP growth was misrepresented; lead plaintiff Indiana PRS appointed 2026-05-20 | [Kessler Topaz](https://www.ktmc.com/bsx-boston-scientific-corporation-class-action-lawsuit/), Q2'26 10-Q |
| 2026-03-16 | — | FTC Second Request on Penumbra | Q2'26 10-Q |
| 2026-03-30 | $62.93, **-9.0%** (vol 43.5M) | CHAMPION-AF (ACC, Mar 28; NEJM): non-inferior on CV death/stroke/SE (5.7% vs 4.8%), ischemic stroke 3.2% vs 2.0% (n.s.), non-procedural bleeding 10.9% vs 19.0%; read as "not a home run"; Raymond James cut target $97 → $88 | [BSX 8-K ex. 99.2](https://www.sec.gov/Archives/edgar/data/885725/000088572526000029/ex992-pressrelease.htm), [ACC "uneasy win"](https://www.acc.org/latest-in-cardiology/articles/2026/04/21/15/23/champion-af), [Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/03/30/stock-market-today-march-30-boston-scientific-falls-after-delivering-underwhelming-trial-results/) (third-party) |
| 2026-04-22 | $64.87, **+9.0%** | Q1'26: organic +9.4% (above 8.5-10% guide), adj. $0.80; FY cut to 6.5-8.0% organic / $3.34-3.41; Watchman volumes declined from February; EP +24% but more share loss than expected; CEO: a guide-down "we... are not proud of" | Q1'26 release; [MedTech Dive](https://www.medtechdive.com/news/boston-scientific-slashes-2026-guidance/818196/) |
| 2026-05-06 | — | Penumbra holders approve the merger | Q2'26 10-Q |
| 2026-05-18 | $55.92, +6.2% | $2B ASR (JPMorgan; ~40M shares final) and $1.5B for ~34% of MiRus LLC with an option on its SIEGEL TAVR | [ASR 8-K](https://www.sec.gov/Archives/edgar/data/885725/000088572526000042/exhibit991-pressrelease_fi.htm), [MiRus 8-K](https://www.sec.gov/Archives/edgar/data/885725/000088572526000041/exhibit991-pressrelease_fi.htm) |
| 2026-05-27 | $50.46, **-12.5%** (vol 52.7M) | Bernstein conference: U.S. Watchman revenue guided flat sequentially in Q2 and Q3, standalone procedures declining; EP share loss, leadless CRM and urology weakness; Stifel target $85 → $75; JPM "raises concerns over trend visibility" | [Investing.com](https://www.investing.com/news/stock-market-news/boston-scientific-stock-tumbles-6-after-guidance-cut-4712376), [Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/05/27/stock-market-today-may-27-boston-scientific-plunges-after-reiterating-underwhelming-full-year-growth-guidance/) (third-party) |
| 2026-07-14 | $42.63 (low close) | — | cache |
| 2026-07-21 | — | Board approves 2026 Restructuring Plan: $700-800M pre-tax charges ($600-700M cash) to end-2029, ~$500M gross annual savings | [8-K](https://www.sec.gov/Archives/edgar/data/885725/000088572526000049/bsx-20260721.htm), Q2'26 10-Q Note M |
| 2026-07-29 | $46.04, 0.0% (premarket -6.6%) | Q2'26 beat (organic 7.0%, adj. $0.86) but FY cut to 5-6% organic / $3.28-3.32; Q3 organic 3-5%; 2027 revenue growth "below our WAMGR" and "limited adjusted EPS growth"; Penumbra "slightly dilutive" initially | Q2'26 release; [MedTech Dive](https://www.medtechdive.com/news/boston-scientific-again-cuts-2026-guidance/826473/); [call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/08/07/boston-scientific-bsx-q2-2026-earnings-call-transcript/) |
| 2026-08-25/26 | $48.17 (-3.4%) on 08-26, $46.67 (-3.1%) on 08-27 | Cyber incident identified Aug 25: network outage hit manufacturing, order processing and shipping globally | Aug 26 8-K; [TechCrunch](https://techcrunch.com/2026/08/26/medical-device-maker-boston-scientific-says-a-cyberattack-is-causing-a-global-disruption-to-its-operations/) |
| 2026-09-08 | $44.98, -5.9% | 8-K: unlikely to meet Q3/FY26 sales and adj. EPS guidance; distribution centres "at or above normal" | Sept 7 8-K |
| 2026-09-21 | — | Arthur Butcher (EVP, Group President MedSurg and APAC) to retire Jan 1, 2027 | [8-K](https://www.sec.gov/Archives/edgar/data/885725/000088572526000061/bsx-20260921.htm) |

- Guidance conflict: the Motley Fool May 27 piece says management reiterated FY organic 5.5-7% and Q2 6-8%; Investing.com says 6.5-8% and 5-7%; a Seeking Alpha headline for July calls the prior range 5-7%. The Q1'26 release says FY 6.5-8.0% and Q2 5.0-7.0%. **Prefer the company release**; no filing shows a formal change between April 22 and July 29.
- Raymond James on Mar 30: the Fool summary says both "maintained outperform" (Wells Fargo, Leerink, Raymond James) and that Raymond James "downgraded"; unresolved, only the target cut is used.

## 4. Competition and clinical evidence

- Medtronic FQ1 FY27 (quarter to July 31, 2026): Cardiac Ablation Solutions +88%, over $2B TTM revenue; Sphere-9 "added nine points" of U.S. PFA share — [MD+DI](https://www.mddionline.com/business/medtronic-s-cardiac-ablation-juggernaut-hits-2b-milestone) (third-party read of Medtronic's call). Sphere-360: CE mark Jan 2026, U.S. IDE ongoing, not FDA-approved — [Medtronic release](https://news.medtronic.com/2026-01-23-Affera-TM-momentum-continues-as-Medtronic-announces-CE-Mark-in-Europe-and-U-S-IDE-first-cases-for-Sphere-360-TM-PFA-catheter-to-treat-paroxysmal-atrial-fibrillation).
- J&J: Varipulse U.S. cases resumed after a 2025 pause; Varipulse Pro CE-marked, not U.S.-approved — [J&J](https://www.jnj.com/media-center/press-releases/johnson-johnson-to-resume-u-s-varipulse-cases).
- Abbott Volt FDA approval 2025-12-22 (above). Kardium also cited as a U.S. entrant (MassDevice).
- BSX on the Q2 call: PFA is ~80-85% of U.S. AF ablation, so conversion no longer offsets share loss; U.S. EP "flat to low-single digits" for 2026 with a mid-single-digit sequential decline in Q3; international EP ~20%. Pipeline: FARAPOINT launched; FARAWAVE Ultra (mapping + ablation) "at scale" ~mid-2027; FARAFLEX 2028 (FARADIGM pivotal started); ICE entry 2027; AVANT GUARD (persistent AF, first-line vs drugs) met endpoints at HRS 2026. CEO: "we did undercall the competitive pressures in the U.S." — transcript / MedTech Dive.
- Watchman: concomitant (ablation + LAAC, supported by OPTION) is ~one-third of U.S. procedures and grew >60% in Q2; standalone procedures down mid-teens; FY26 Watchman flat to low-single-digit, H2 down mid- to high-single-digit; no recovery assumed for 2027 — transcript. Market share 91% (Investing.com, third-party). CHAMPION-AF label expansion and CMS NCD revision are planned — [MD+DI](https://www.mddionline.com/cardiovascular/boston-scientific-eyes-market-expansion-with-watchman-flx-after-champion-af-success); **filing and decision dates: no source found**.

## 5. Survival data (Q2 2026 10-Q, FY2025 10-K)

- Debt at 2026-06-30: current $1,709M (commercial paper $1,689M at par, 41-day weighted maturity, 4.06% yield) + long-term $10,915M = $12,624M. Senior notes $10.859B. Cash $539M.
- 2026 Revolving Credit Agreement $3.000B to 2031-02-26, undrawn; CP capacity $2.750B, **$1.061B available**. 364-Day Revolving Credit Agreement $2.000B, undrawn (term runs 364 days from first availability or Penumbra close). Term Loan Credit Agreement $6.000B (Tranche A $1.0B, Tranche B $5.0B), drawable only at Penumbra closing, each maturing 364 days after drawing; Tranche B cut by, and after closing prepaid from, any bond/equity proceeds.
- Covenant: max debt / deemed EBITDA 3.75x, **4.00x at June 30, 2026**, stepping up to **4.75x** for four quarters after a >$1B qualified acquisition; actual **2.02x**; cash litigation exclusion capacity $1.115B left of $1.160B.
- Note ladder (10-Q table): Dec 2027 €900M 0.625% ($1,026M); Mar 2028 euro notes 1.375% ($855M) and $344M 4.000%; Mar 2029 $272M + $855M; Jun 2030 $1,200M; 2031 $855M + $969M; 2032 $1,424M; 2034 $570M + $741M; 2035 $350M; 2039 $450M; 2040 $300M; 2049 $650M; finance lease $124M. **Due by 2028-09-30: $2.225B of notes + $1.689B CP** (my sum).
- Leases and commitments (FY2025 10-K): operating lease liabilities $536M ($90M current); unrecorded purchase obligations $1,830M ($1,051M in 2026, $268M 2027, $186M 2028). Interest expense H1 2026 $186M.
- Capital use H1 2026: acquisitions $718M; investments/technologies $1,730M (MiRus $1.5B + $100M earlier); buybacks $2,000M (treasury shares 263.3M → 303.2M); no bond issuance; CP +$1,675M.
- Penumbra: 2025 revenue ~$1.4B (BSX release); Q2 2026 revenue $390.0M (+14.9%), operating income $41.0M, cash + investments $658.8M — [PEN Q2 8-K](https://www.sec.gov/Archives/edgar/data/0001321732/000132173226000036/pen-63026xexhibit991.htm). 39.3M PEN shares (DEFM14A vote count) → ~$11B cash and ~41M new BSX shares (my estimate from the 73/27 split). Close expected "second half of 2026" (Q2'26 10-Q). FTC status after the Second Request: no source found.
- Pro forma (my estimate, not disclosed): net debt at closing ≈ $12.1B + ~$11.0B − ~$0.7B Penumbra cash ≈ $22-23B; on TTM EBITDA $5.6B plus Penumbra's (unknown, likely a few hundred $M) ≈ 3.8-4.0x net debt/EBITDA. Management on the call: capital allocation "strategic tuck-in M&A and opportunistic share repurchases", no deleveraging timeline stated. Credit ratings: not checked (unverified).

## 6. EPS base and headline adjustments (release reconciliations, per share after tax)

| Item | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---|---|---|---|
| GAAP EPS | 0.51 | 0.45 | 0.90 | 0.61 |
| Amortization | +0.13 | +0.13 | +0.14 | +0.14 |
| Acquisition/divestiture | +0.06 | +0.02 | +0.02 | +0.05 |
| Restructuring | +0.02 | +0.06 | +0.02 | +0.02 |
| Litigation | — | +0.10 ($194M pre-tax) | — | +0.04 ($76M) |
| Investment gains/losses | (0.00) | +0.02 | **(0.07)** ($137M pre-tax gain) | (0.00) |
| EU MDR | +0.01 | +0.01 | 0.00 | 0.00 |
| IEEPA tariff refund | — | — | — | **(0.05)** ($83M pre-tax) |
| Deferred tax / discrete tax | +0.03 | +0.02 | **(0.21)** ($320M benefit) | +0.05 |
| Adjusted EPS | 0.75 | 0.80 | 0.80 | 0.86 |

- TTM GAAP EPS $2.47 contains ~$0.28 of Q1 2026 non-operating/tax gains ($424M after tax). Ex those, ~$2.19, 4% above the $2.10 trigger.
- Rough TTM GAAP EPS path (my estimate, not a forecast from any source): Q3'26 GAAP perhaps $0.45-0.58 (consensus adj. $0.77, third-party; cyber impact unknown) → TTM ~$2.41-2.54 after the Oct 28 report; Q4'26 replaces $0.45 (Penumbra closing costs, step-up and interest if it closes in Q4); **Q1'27 replaces $0.90** → with GAAP ~$0.45-0.60 the TTM falls by $0.30-0.45, to about $2.0-2.3 at the May 2027 month-end (after the Q1 2027 10-Q, likely early May). The guide-cut proxy (sell at or below $2.10 before 2027-09-28) is at real risk from accounting roll-off plus purchase accounting, not only from operations.

## 7. Consensus (third-party)

- Yahoo Finance analysis page, fetched 2026-09-28: Q3'26 EPS $0.77 (22 analysts; low $0.58), revenue $5.15B (+1.7%; low $4.70B); Q4'26 EPS $0.84, revenue $5.41B; **FY2026 EPS $3.27 (25), revenue $21.27B (+5.95%); FY2027 EPS $3.41 (26; range $3.19-3.90), revenue $22.25B (+4.6%)**; FY27 EPS was $3.72 90 days ago. — [Yahoo](https://finance.yahoo.com/quote/BSX/analysis/). Matches the cache's forward EPS $3.41.
- Note: FY26 revenue consensus (+5.95%) sits inside the pre-cyber guide the company says it will likely miss — estimates look partly stale. Whether FY27 revenue includes Penumbra is unclear (likely mixed across analysts).
- Price targets: stockanalysis.com (updated Sept 23-24) average $61.07, low $44, high $94, "Buy", 31 analysts — [stockanalysis](https://stockanalysis.com/stocks/bsx/forecast/); another aggregator cites an average $72.43 (older). Prefer the newer one.

## 8. Open questions no source could close

1. Size of the cyber hit to Q3/Q4 2026 revenue and EPS, whether it is excluded from adjusted EPS, insurance recovery, and any data-exfiltration or regulatory follow-up (answer due Oct 28, 2026).
2. FTC outcome on Penumbra (clearance, consent decree with divestitures, or challenge) and the closing date; the permanent financing mix (bond sizes and coupons) to take out the $6B 364-day term loans.
3. Penumbra's EBITDA and the pro forma leverage and covenant ratio after closing; whether buybacks pause.
4. Timing of the CHAMPION-AF label expansion filing/approval and any CMS NCD reconsideration.
5. Whether U.S. EP share loss has stabilised by product (Farawave vs Sphere-9 vs Volt), and U.S. PFA market growth in 2026 (BSX called ~15% in February).
6. The corrected EV/EBITDA percentile with full D&A for pre-2026 rows (see data flag).
7. Date of the Q4 2026 report (early February 2027 by pattern; unconfirmed).
8. Cause of the 2025-12-08 (-3.8%), 2026-08-20 (-5.1%) and 2026-09-10 (-4.1%) moves: no specific source found.
