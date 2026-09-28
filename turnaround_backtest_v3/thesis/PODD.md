# PODD — Insulet Corporation

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #1 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-03-31 |
| Monthly RSI, last completed candle | 36.1 |
| Episode months / min RSI | 6 / 34.0 |
| Drawdown from trailing 5-year high | -61.4% (high 352.82 on 2025-09-09) |
| Market cap / avg daily $ volume (3m) | $9.44B / $238M |
| Sector / industry | Health Care / Health Care Equipment |
| Survival gate (proxy) | PASS — cash $535M, debt due <1y $19M, FCF TTM $266M, 24m gap -$516M |
| Net debt / EBITDA, interest coverage | 0.6 / 9.4 |
| Valuation | P/E trailing 25.5, P/E forward 17.7, PEG 1.07, P/S 3.09, EV/Sales 3.2, EV/EBITDA 15.1, P/FCF 35.5 |
| EPS | TTM 5.35, forward est. 7.71; growth YoY (TTM) -39.8%, last quarter +328.1%, implied forward +44.0% |
| Revenue YoY (last quarter) | +23.5% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 1 of 10 / 2 of 20 |
| TTM revenue growth | +29% (latest quarter 2026-06-30) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.00** — P/S 0.00, EV/EBITDA 0.00, EV/EBIT 0.00 (P/E pct 0.00, not used) |
| Multiples today | P/S 3.1, EV/EBITDA 16.3, EV/EBIT 19.4, P/E 25.5 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 34.6 / 34.0 |
| From 5-year high | -61% |
| TTM EPS path, 6 quarters (oldest first) | 5.55, 3.28, 3.43, 3.48, 4.28, 5.33 |
| TTM EPS vs 12 months earlier | +62% |
| One-off EPS guard | passed — TTM net income / operating income 0.73 |
| Acquisition guard | passed — diluted shares -2.2% y/y |
| Net debt / EBITDA | 0.7 |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 73 shares per $100k at Friday's $136.13).
Entry TTM EPS **$5.33** → guide-cut trigger **$4.53** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$204** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val ≤ 0.10: n 218, mean +38%, median +23%, 80% winners, 58% beat SPY; 60%+ below 5y high: n 64, mean +56%, median +24%, 73% winners (regime-heavy: 2009, 2020). All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Cleanest fit; deepest-and-cheapest bucket.

- Reward case: Cheapest ever on all three operating multiples after a 61% fall; TTM EPS up 62% and rising four quarters running; net debt 0.7x EBITDA. The repository's Sept 27 Dexcom-versus-Insulet comparison weights a $90-260 scenario range at 30/50/20.
- Main risks under these rules: Late-October print is the first test of the mid-teens US guide; consensus still falling, short interest rising; two Class I pod corrections in 2026; three tubeless competitors entering over the next nine months. Guide-cut trigger $4.53 is 15% below a still-rising figure, so the proxy needs a real miss.

Repository research: [Dexcom vs Insulet comparison](../../reports/Dexcom%20vs%20Insulet%20comparison.md), [research notes](../../research_notes/Dexcom%20vs%20Insulet%20comparison/)

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression + temporary execution** (structural deterioration not yet ruled out). Trailing EPS rose while the price fell 61%, so the loss is almost all multiple; what knocked the multiple off were execution events (two Class I pod corrections, a Type 2 onboarding/retention miss that cut the US guide), and the part that could still prove structural is Type 2 churn plus three tubeless competitors arriving between late 2026 and mid-2027.

Narrative (closes from the price cache; figures from the 8-K exhibits and 10-Q; sources in the [research notes](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/PODD.md)):

- **Peak, 2025-09-09, $352.82.** About 83x trailing adjusted EPS ($4.24) and 94x trailing GAAP EPS at the 5-year-high month, after fourteen straight quarters of beating and raising; FY2025 guidance had gone from 16-20% to 28-29%.
- **Leg 1, 2025-11-19 → 2026-02-18: $346.36 → $258.07 (-25.5%; peak to Feb 18 -26.9% while XLV rose 13.8%).** Nov 20 Investor Day set a ~20% cc revenue CAGR to 2028 with ~100 bp a year of margin expansion; the market read Omnipod 6 as a software upgrade against competitor patch pumps due by 2027 (-9.7% that day). Dec 1: CMS finalised DMEPOS competitive bidding for pumps and CGMs (-5.0%, link inferred). Jan 12: Barclays Underweight on competition (-3.6%). Feb 18: Q4 2025 beat (revenue $783.8M, +31.2%; adj EPS $1.55), FY2026 guided 20-22% cc, $300M ASR.
- **Leg 2, 2026-02-18 → 2026-05-28: $258.07 → $142.65 (-44.7%; XLV -4.3%).** Mar 12 first Omnipod 5 pod correction (cannula tear, silent under-delivery; -6.9% next day). Apr 24 Rothschild to Neutral ($380 → $220). Apr 29 FDA Class I classification (-12.5%, attribution inferred from the date match). May 6 Q1: revenue $761.7M (+33.9%), adj EPS $1.42, total guide raised to 21-23% but US held at 20-22%, US new starts down sequentially and "modest retention deterioration" as Type 2 reached ~40% of starts (-9.7%). May 26 second correction (~7M pods, -5.1% next day); May 28 the Federal Circuit reversed the EOFlow trade-secret verdict. H1 correction costs: $36.7M pre-tax, $0.42 a share.
- **Relief, 2026-05-28 → 2026-08-04: +16.9% to $166.82.** Director buy at $143.51 (Jun 3); STRIVE (Omnipod 6) data at ADA (Jun 6). Securities class action filed Jul 2 (class period to May 26, no accrual).
- **Leg 3, 2026-08-05: -20.1% to $133.26.** Q2 beat on every line (revenue $801.7M, +23.5%; US Omnipod +20.1%; adj EPS $1.66 vs ~$1.46; adj operating margin 19.3%) and the 8-K raised FY2026 adj EPS growth to >30% (from >25%), but cut FY2026 US Omnipod to 17-19% from 20-22% and guided Q3 US to 14-16% on "lower rates of utilization and retention among type 2 customers" in their first 90 days. At least six downgrades, targets cut to $144-152.
- **Since, 2026-08-05 → 2026-09-25: +2.2% to $136.13** (low close $131.96 on Sep 11). Sep 9 Wells Fargo conference framed a Q4 exit of 12-17% cc (US 9-14%); two long-serving directors left in September (no disagreement); Sep 21 term loan repriced and revolver raised to $750M; Beta Bionics' Mint patch pump cleared Sep 14.
- Over the whole fall TTM revenue rose from $2,360M to $3,053M (+29%), TTM adjusted EPS from $4.24 to $5.87 (+38%) and GAAP TTM EPS from $3.28 to $5.33 (+62%, flattered by the 2025 debt-extinguishment loss leaving the window). P/S went from 9.4 at the peak month to 3.1. Over roughly the same span XLV rose ~21% (to Sep 14, last cached bar) and DXCM ~10%, so this is company-specific.

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **Unsustainable multiple, not an earnings peak.** Earnings, margins and revenue are all higher today than at the peak (adjusted operating margin 17.8% in Q2 2025, 19.3% in Q2 2026); only the multiple collapsed (~83x → ~23x trailing adjusted, P/S 9.4 → 3.1). At 80x-plus the stock was priced for 20%-plus growth for years; a guide implying mid-teens removed the whole premium.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $534.9M at 2026-06-30 ($346.3M in money-market funds); total debt $948.4M, net debt $413.5M | fundamentals cache; Q2 2026 10-Q |
| Realistically available credit (undrawn revolver, covenants) | **$750M revolver, undrawn** (raised from $500M on 2026-09-21, matures 2030, SOFR + 1.25-1.75%). Only maintenance covenant: a leverage ratio that applies when ≥35% of the revolver is drawn; the term loan and 6.5% notes have incurrence-only leverage and fixed-charge tests. Liquidity ≈ $1.28B | [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000169/podd-20260630.htm); [8-K, Sep 21, 2026](https://www.sec.gov/Archives/edgar/data/1145197/000119312526396779/d71204d8k.htm) |
| Debt maturities next 24 months | About $35-40M, all amortization: 10-K ladder 2026 $18.4M, 2027 $19.4M, 2028 $12.1M (equipment financings, $5M a year of term-loan amortization) plus $7.4M Costa Rica financing (2028). First bullets: $475M term loan Aug 2031, $450M notes April 2033 | [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1145197/000114519726000028/podd-20251231.htm) Note 13; 10-Q Note 8 |
| Cash consumption if weak conditions persist 24 months | None: FCF TTM $266M; H1 2026 FCF $145.4M after ~$37M of correction costs and capex up to $56.8M; FY2026 FCF guided "down modestly" from $377.7M. Even the bear case stays FCF-positive | fundamentals cache; Q2 2026 8-K; Q2 call |
| Interest, maintenance capex, leases, other fixed obligations | Net interest expense guided "$40M or more" for 2026 (coverage 9x; $460M of the term loan swapped to 3.47%); operating leases $51.9M (payments $6.6M 2026, $8.0M 2027); purchase obligations $353M due within a year at Dec 31, 2025; remaining correction cost ~$23-33M of the $60-70M estimate; contingent guarantee of up to $97M of the Costa Rica plant seller's loan | 10-K; 10-Q |
| Can recovery happen without a large equity raise? | yes | positive FCF, 0.6-0.7x net debt/EBITDA, $750M undrawn, no maturity before 2031 |

Gate verdict: PASS — reasoning:

- Profitable in 4 of 4 reported years, FCF-positive through two recalls, ~$1.28B of liquidity against ~$40M of maturities in 24 months, and no maintenance covenant unless the revolver is more than a third drawn. Ratings Ba3 / BB (March 2025 upgrades; current outlooks unverified). The open-ended items are the class action (no accrual) and a third correction, neither of which threatens solvency at this balance sheet.

## 4. Recovery thesis  (testable statement)

> The business weakened because of a US Type 2 onboarding and first-90-day retention problem, two Class I pod corrections that hit the same onboarding window, and the fear that three tubeless competitors (Tandem Mobi tubeless, Beta Bionics Mint, MiniMed Fit) will take new-start share in 2027; the multiple fell to the lowest of its history while earnings kept rising. Recovery requires US Omnipod growth to land inside the guided 14-16% (Q3) and 9-14% (Q4 exit) without another cut, a FY2027 guide at or above the 12% low end of the exit range with stable pod pricing, and no new quality event.
> We expect to observe a Q3 2026 print (early November, date not yet announced) with US Omnipod ≥14% and the exit range kept, followed by a FY2027 guide of 12%+ cc in mid-to-late February 2027, within the next 2–4 quarters.

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| US Omnipod revenue growth vs guide (plus any new-start or retention disclosure) | leading | Q2 2026 +20.1%; Q3 guide 14-16% (≈$567-577M on $497.1M); Q4 exit US 9-14%; retention and Type 2 users undisclosed | Q3 US ≥14% and Q4 guide inside 9-14%; new starts stable; any retention KPI disclosed and flat or better | Q3 US <14%, Q4 guide below 9%, or the 12-17% total exit range lowered |
| TTM EPS vs entry $5.33 / trigger $4.53 | financial confirmation | $5.33 GAAP (adjusted TTM $5.87); rising four quarters running | Keeps rising (Q3 2026 GAAP above the $1.24 it replaces); FY2027 consensus EPS ($7.63-7.71) stops falling | Prints at or below $4.53 at a month-end before 2027-09-28 (rule exit). Needs ~$0.80 of cumulative GAAP shortfall vs year-ago quarters, i.e. a large charge or a sustained miss |
| Competitive entry and pod pricing (Tandem tubeless clearance, Mint launch Q1 2027, MiniMed Fit summer 2027; short interest 7.4% of float) | competitive / sentiment | Mint cleared Sep 14, 2026; Tandem tubeless not yet cleared (targeted H2 2026); management says pricing "stable to slightly up" | Launches slip or reimburse slowly; FY2027 guide assumes stable price and holds; short interest falls | PBM formulary exclusion or net-price concession on pods; Mint/Tandem uptake visible in Insulet's new starts; FY2027 guide below 12% |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **Correction costs inside GAAP EPS:** H1 2026 GAAP includes $36.7M pre-tax of pod-correction warranty cost ($0.42 a share: Q1 $0.13, Q2 $0.29). $23-33M of the $60-70M estimate is still to come, mostly in H2 2026, so GAAP Q3-Q4 EPS will again sit below adjusted.
- **The +62% TTM EPS change is mostly base effect:** Q2 2025 GAAP EPS of $0.32 carried an $84.4M loss on repurchasing the 2026 converts ($1.16 a share; $123.9M for FY2025). On adjusted EPS the trailing change is +38%.
- **Adjusted EPS is not flattered by stock comp:** Insulet's non-GAAP adjustments remove only corrections, executive transitions, debt extinguishment, investment losses and tax matters; stock comp ($40.9M in H1 2026, up from $25.7M which included a $10.8M CEO-forfeiture reversal) and amortization stay in both measures.
- **Tax:** H1 2026 effective rate 19.7% (R&D credits, mix) vs 27.2% in FY2025; FY2024 GAAP EPS ($5.78) contained ~$191M of valuation-allowance releases. A 5-point swing in the rate is ~$0.35 a share.
- **Working capital / distributor timing:** three distributors took 27%, 26% and 25% of 2025 revenue; H1 2026 receivables rose $76.9M on "timing of distributor orders in the United States", and the Q1 guide flagged a 200 bp Q2 inventory headwind. A US quarter can swing a few points on stocking.
- **Buyback and interest:** the $300M ASR at ~$240 cut diluted shares to 69.4M (about +2% to EPS); interest income is falling with the lower cash balance (net interest ≥$40M in 2026). No acquisitions.

## 5. Valuation — three scenarios, 3-year horizon

Year 3 = FY2029, valued in September 2029 on FY2029 adjusted EPS. Start: FY2026 revenue $3.25-3.31B (guide and consensus), FY2025 adjusted operating margin 17.6%, net debt $414M, 69.35M shares. Net income = adjusted EBIT × 0.76-0.77 (≈20% tax and small net interest; FY2028 consensus implies ~0.75). Net cash is not added to the implied price (worth ~$7-15 a share).

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $3.87B (FY27-29 +7%, +6%, +5%: US new starts fall, blended attrition drifts to 17-20%, tubeless rivals take share) | $4.62B (+13%, +12%, +11%: management's exit framework with no retention benefit; ≈ consensus FY27-28) | $5.03B (+16%, +15%, +14%: 45-day retention fix works, Omnipod 6 in 2027, rival launches slow) |
| Sustainable margin | Adj. operating 16.5% (pod price concessions, retention spend) | Adj. operating 21.5% (~100 bp a year as guided) | Adj. operating 23% |
| Net debt / cash (yr 3) | ~$0.5B net cash (FCF ~$300M/yr, no buyback) | ~$1.0B net cash (FCF $0.5-0.7B/yr, ~$150M/yr buyback) | ~$0.9B net cash (~$300M/yr buyback) |
| Diluted shares (yr 3) | 70.0M (stock-comp dilution) | 68.5M | 67.0M |
| Multiple applied | 13x FY2029 EPS $6.93 (ex-growth medtech / Tandem-like) | 18x FY2029 EPS $11.02 (below medtech average for a ~11% grower facing new competition) | 24x FY2029 EPS $13.31 (partial growth multiple, still below DXCM's 28x today) |
| Implied price | **$90** | **$198** | **$319** |
| Total return / annualised | -34% / -12.8% | +46% / +13.4% | +135% / +32.9% |
| Probability weight | 30% | 50% | 20% |

Probability-weighted value **~$190, +40% from $136.13 (~11.8% a year)**. Key assumptions: FY2026 lands inside the guide (Q3-Q4 are guided and pre-funded by the H1 beat); no further quality event of the March-May size; pod pricing holds in the base case; no large M&A. The weights keep the repository comparison's 30/50/20 because revision momentum is still negative and all three competitor launches fall inside the window. The comparison report's 12-24 month scenarios ($90-120 / $155-185 / $215-260, weighted ~$164, +20%) are the same view at a shorter horizon.

What does today's price already require the business to deliver?

- At $136.13 the stock trades at 20.9x FY2026 consensus adjusted EPS ($6.50 on revenue $3.29B, +21%) and 17.7x FY2027 ($7.63-7.71 on ~$3.74B, +13.8%), EV/sales 2.6x FY2027 (consensus third-party: StockAnalysis, MarketScreener; FY2027 still drifting down since the Q2 print).
- Reverse-implied: to earn 10% a year to September 2029 the stock needs ~$181. At an 18x exit that requires FY2029 EPS of ~$10.07, i.e. ~9% annual revenue growth on the guided margin plan (EPS +16% a year) — below consensus and below the 12-17% exit range. At a 15x exit it requires ~$12.08, i.e. ~16% revenue growth. So the price does not require the growth story to hold; it requires the multiple not to fall further from the mid-to-high teens. The market is pricing a permanently lower multiple more than lower earnings.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 3.1 | 9.5 | 3.1 | 20.2 | 0.00 | 9.4 | 2010-03-31 |
| EV/EBITDA | 16.3 | 56.4 | 15.9 | 215.0 | 0.00 | 45.5 | 2014-12-31 |
| P/E (trailing) | 25.5 | 82.9 | 24.9 | 28,834.0 | 0.00 | 94.1 | 2019-03-31 |

At the 5-year median P/S (9.5) on today's TTM revenue the price would be about $412 (+203%); at the 5-year low (3.1), about $133 (-3%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.00, growth +29%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$4.53** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (0.7 today)
- **Price target where recovery is fully reflected:** trim half at **$204** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** medical devices (PODD, DXCM, BSX): a third of the basket; PODD and DXCM also share the diabetes / GLP-1 / competition narrative; same-driver holdings: DXCM, BSX
- **Research overlay (not part of the rule):** More confident on a Q3 print with US Omnipod ≥14%, the exit range kept, any disclosed retention or new-start metric that is stable, a new buyback commitment at these prices (only ~$115M is left on the authorization), or a slip in Tandem's tubeless clearance. Less confident on US growth below 14% or a lower exit range, any pod net-price concession or PBM exclusion, a third correction, or FY2027 consensus EPS falling below ~$7.3. Note the proxy is slow for this name: a $4.53 print needs roughly $0.80 of cumulative GAAP EPS shortfall, so an operating disappointment would show up in price long before the rule fires. Dated catalysts: Q3 2026 results, early November (not yet announced; third-party estimates Oct 29 or Nov 5; last year Nov 6); Tandem Mobi tubeless FDA decision (company target H2 2026); CMS competitive-bidding window for pumps and CGMs (late 2026, effective by Jan 1, 2028); EOFlow rehearing petition (filed Jul 29, 2026, pending); Hu v. Insulet lead-plaintiff appointment and amended complaint (dates unknown); Q4 2026 results and FY2027 guide, mid-to-late February 2027; Beta Bionics Mint full US launch, Q1 2027; Omnipod 6 clearance and launch, 2027 (filing status unverified); Q1 2027 results, early May 2027; ADA Scientific Sessions, June 2027; MiniMed Fit US launch, summer 2027; buyback authorization expires Dec 31, 2027.

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #1: val 0.00, growth +29%, entry TTM EPS $5.33, trigger $4.53, trim $204 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/PODD.md) | Supports the rule buy: cause = valuation compression + temporary execution; survival PASS ($750M undrawn revolver, ~$40M due in 24 months); 3-year probability-weighted value ~$190 (+40%); the $4.53 trigger needs ~$0.80 of cumulative EPS shortfall. Corrects the comparison report: the Q2 8-K guides FY2026 adj EPS >30%, not >25%. review_deadline kept at 2027-03-27 (after the second report from today, the Q4 2026 print in Feb 2027) |

## 8. Research conclusion

Insulet fits the rule's intent cleanly: a profitable, FCF-positive grower whose multiple fell from ~83x to ~23x trailing adjusted earnings while earnings rose 38%, with a balance sheet that removes survival from the question. The research supports the buy, with a 3-year probability-weighted value of about $190 (+40%, ~12% a year) against a bear case of about $90. The skew is wide, and the 30% bear weight is real because revision momentum is still negative and three tubeless rivals launch inside the window. The single most important thing to watch is US Omnipod growth in the early-November Q3 print against the 14-16% guide, together with whether the 12-17% exit range survives; that print decides which tail applies well before the EPS proxy can. In the basket, PODD adds to a one-third medtech weight and shares its diabetes, GLP-1, CMS and competition risk with DXCM (most Omnipod users wear a Dexcom or Abbott sensor). The pair is partly self-hedging, though: if Insulet's Type 2 churn proves structural, those patients mostly keep their sensor. PODD's drivers are unrelated to the five software names (APPF, INTU, DT, NOW, VEEV), KNSL and OLLI. Unlike DT or NOW, it is one of the names least likely to be sold early by the mechanical proxy.
