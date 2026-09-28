# DXCM — Dexcom

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #8 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-03-31 |
| Monthly RSI, last completed candle | 55.5 |
| Episode months / min RSI | 2 / 39.8 |
| Drawdown from trailing 5-year high | -46.8% (high 162.82 on 2021-11-17) |
| Market cap / avg daily $ volume (3m) | $32.69B / $383M |
| Sector / industry | Health Care / Health Care Equipment |
| Survival gate (proxy) | PASS — cash $1.95B, debt due <1y $21M, FCF TTM $1.41B, 24m gap -$1.93B |
| Net debt / EBITDA, interest coverage | -0.4 / 86.3 |
| Valuation | P/E trailing 34.2, P/E forward 27.7, PEG 1.33, P/S 6.58, EV/Sales 6.5, EV/EBITDA 20.6, P/FCF 23.3 |
| EPS | TTM 2.53, forward est. 3.12; growth YoY (TTM) +47.2%, last quarter +42.2%, implied forward +23.5% |
| Revenue YoY (last quarter) | +13.1% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 8 of 10 / 15 of 20 |
| TTM revenue growth | +16% (latest quarter 2026-06-30) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.15** — P/S 0.22, EV/EBITDA 0.12, EV/EBIT 0.11 (P/E pct 0.08, not used) |
| Multiples today | P/S 6.9, EV/EBITDA 23.6, EV/EBIT 29.1, P/E 34.2 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 53.3 / 39.8 |
| From 5-year high | -47% |
| TTM EPS path, 6 quarters (oldest first) | 1.33, 1.42, 1.80, 2.09, 2.33, 2.53 |
| TTM EPS vs 12 months earlier | +78% |
| One-off EPS guard | passed — TTM net income / operating income 0.88 |
| Acquisition guard | passed — diluted shares -1.8% y/y |
| Net debt / EBITDA | net cash |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 115 shares per $100k at Friday's $86.62).
Entry TTM EPS **$2.53** → guide-cut trigger **$2.15** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$130** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val 0.10-0.25: n 222, mean +17%, median +16%, 66% winners, 52% beat SPY; 40-60% below: n 250, mean +24%, median +19%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Good; the higher-confidence half of the PODD/DXCM pair.

- Reward case: TTM EPS up 78% and rising every quarter, net cash, 16% growth, 47% below the high at the 11-22nd percentile. In the running portfolio since October 2025 at $66.08 (+38%). The repository's Sept 27 deep dive weights a $55-135 scenario range at 25/50/25 and finds execution risk down after three beat-and-raise quarters.
- Main risks under these rules: Management-flagged H2 headwinds (FX, Ireland start-up), Abbott competition, pleading-stage litigation. Monthly RSI 53 already, so the entry is not at the low. Trigger $2.15.

Repository research: [Dexcom DXCM deep dive](../../reports/Dexcom%20DXCM%20deep%20dive.md), [Dexcom vs Insulet comparison](../../reports/Dexcom%20vs%20Insulet%20comparison.md), [research notes](../../research_notes/Dexcom%20DXCM%20deep%20dive/)

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression**, triggered by temporary execution. TTM revenue is up 114% and TTM operating income 3.1x since the November 2021 high while the price is down 47%; the only fundamental setback (TTM GAAP EPS -19% from September 2024 to March 2025, on a 2024 sales mistake and 2025 margin and quality problems) has been repaired, but the multiple it knocked off has not come back.

Narrative (closes from the price cache; figures from the 8-K exhibits, 10-Q and 10-K; sources in the [research notes](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/DXCM.md)):

- **5-year high, 2021-11-17, $162.82.** About 28x TTM revenue ($2,319M) and ~174x TTM operating income ($369M) on a ~$64B market cap; month-end P/S 25.4, EV/EBITDA 122.7, P/E 93.0. Even the P/E flattered it: TTM net income ($529M) exceeded operating income because a ~$260M non-operating or tax item landed in Q4 2020 (TTM net income jumped $231M → $494M in one quarter with operating income flat; nature not verified).
- **Leg 1, 2021-11-17 → 2022-06-16: $162.82 → $67.99 (-58%; SPY -22%).** No guidance cut: revenue grew 27% in 2021 and 19% in 2022. This was the 2022 de-rating of high-multiple growth stocks, plus two company items: -11.0% on 2022-05-24 after Bloomberg reported Dexcom was in talks to buy Insulet (denied May 31) and a G7 FDA delay to late 2022 (announced July 28). The stock recovered to $137.93 by 2023-07-18 on the G7 launch and a 2023 beat-and-raise year, fell to $93.30 on the summer-2023 GLP-1 scare, and made a cycle high of **$140.45 on 2024-04-09** at 108x point-in-time trailing EPS ($1.30, itself lifted by a Q4 2023 tax benefit; 91x on the Q1 2024 TTM of $1.54 released April 25).
- **Leg 2, 2024-07-26: -40.7% ($107.85 → $64.00).** Q2 2024 revenue of $1,004M missed (~$1.04B expected) and FY2024 guidance was cut from $4.20-4.35B to $4.00-4.05B ([Q2 2024 8-K](https://www.sec.gov/Archives/edgar/data/1093557/000109355724000143/dxcmq2202499-1_6302024.htm)). Causes were self-inflicted and US-centric: a sales-force realignment, G7 rebate eligibility arriving faster than planned, DME share loss. A ~6% guidance cut took 41% off because the stock sat at ~70x TTM EPS and had raised guidance three months earlier.
- **Leg 3, 2024-07-26 → 2025-11-10: $64.00 → $54.84 (-14%).** Revenue never fell year over year (worst: +2% in Q3 2024), but TTM GAAP EPS fell from $1.65 (Sept 2024) to $1.33 (March 2025). Non-GAAP gross margin fell to 59.4% (Q4 2024) and 57.5% (Q1 2025). The FDA warning letter of March 4, 2025 (-9.1% on March 10) cited an uncleared sensor-material change. The FY2025 GM guide went 64-65% → 62% → 61% (actual 60.8%). Class I recalls followed, then the CEO's medical leave (Sept 14, 2025) and the Hunterbrook short report (Sept 18). Q3 2025 was a beat with a second GM cut and 2026 framed "below the Street": -14.6% to $58.22 on Oct 31. The November 28 CMS rule put CGMs into competitive bidding from 2028.
- **Recovery, 2025-11-10 → 2026-09-25: $54.84 → $86.62 (+58%).** TTM EPS $1.80 → $2.53 (+41%), so most of the rebound is earnings, not re-rating (trailing P/E ~30x → 34x). Q4 2025 non-GAAP GM 63.5%, then FY2026 guidance raised twice. May 14 Investor Day: 2030 targets, $1B buyback, Elliott settlement. Q2 2026: revenue $1,308M (+13%, organic +12%), non-GAAP GM 64.1%, all guidance raised, +12.0% next day ([Q2 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001093557/000109355726000142/dxcm06302026-exhibit991.htm)). 52-week high $92.34 on Aug 21.
- Net over three years (deep dive decomposition): TTM EPS +178%, trailing P/E ~95x → 34x (-64%), price +0.7%. From the 5-year-high month, P/S 25.4 → 6.9 (-73%) while TTM revenue per share rose 127%.

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **Unsustainable multiple, not an earnings peak.** Revenue, operating income and EPS are all well above their levels at both highs (TTM operating income $369M in Sept 2021, $598-652M around the April 2024 peak, $1,139M now). At 25x sales and ~120x EBITDA in November 2021, and ~16x sales and ~108x trailing EPS in April 2024, the price assumed 20%-plus growth for years; growth is now 11-13% with a 2030 target of 10%-plus. The historical P/E averages are a poor anchor because GAAP earnings were thin (and in 2020-2021 one-off-inflated) when they were set.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $1,947M at 2026-06-30: $1,105.0M cash + $842.0M short-term securities. Debt: $1,250M converts (carrying $1,242.8M) + $155.6M lease obligations = $1,398M; net cash $549M | [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001093557/000109355726000143/dxcm-20260630.htm); fundamentals cache |
| Realistically available credit (undrawn revolver, covenants) | $200M revolver (accordion to $500M), undrawn; $8.7M letters of credit → **$191.3M available**. Covenants: maximum leverage and minimum fixed-charge coverage (thresholds not in the filing text), in compliance at 2026-06-30. **Matures Oct 13, 2026**; no renewal 8-K through the last filing (Sept 16) | 10-Q Note 4 |
| Debt maturities next 24 months | **$1,250M 0.375% notes due May 15, 2028** (inside the window). Conversion price $162.41 (87% above $86.62), capped call to $212.62; settlement in cash, stock or both at Dexcom's option; freely convertible from Feb 15, 2028. Expect cash repayment, as with the $1.21B 2025 notes (Nov 2025). The screen's "debt due <1y $21M" is the current operating-lease liability, not borrowings | 10-Q; [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1093557/000109355726000027/dxcm-20251231.htm) |
| Cash consumption if weak conditions persist 24 months | None: TTM operating cash flow $1,749M, capex $344M, FCF $1,405M ($1.24B after stock comp). Today's cash alone covers the 2028 principal 1.6x | fundamentals cache |
| Interest, maintenance capex, leases, other fixed obligations | Coupon ~$4.7M a year (H1 2026 interest expense $6.1M vs interest income $36.4M). Capex $161.3M in H1 2026 (Ireland build-out; construction in progress $614.4M). Operating leases $20.7M current + $82.6M long-term; finance lease $52.3M. Open purchase orders and obligations ~$1.25B at Dec 31, 2025, mostly within a year (normal course) | 10-Q; 10-K Note 5 |
| Can recovery happen without a large equity raise? | yes | net cash, ~$1.4B FCF a year, buyback running ($600M in Q2 2026; ~$400M left to June 30, 2027) |

Gate verdict: PASS — reasoning:

- Profitable in 4 of 4 reported years and FCF-positive through the 2025 margin trough. The one maturity in the window ($1.25B, May 2028) is covered by current cash before any FCF. The revolver is small, undrawn and not needed. Its October 2026 maturity is a disclosure item to check in the Q3 10-Q, not a funding risk. Litigation is at the pleading stage with no accrual (section 4).

## 4. Recovery thesis  (testable statement)

> The business weakened because a self-inflicted 2024 US sales and channel mistake cut growth from ~25% to 2-8% for two quarters. Then 2025 manufacturing and quality problems (scrap, air freight, an FDA warning letter, Class I recalls) took non-GAAP gross margin from ~64% to 57.5-61% during a CEO transition, and the market removed the growth premium. Recovery requires organic growth of 10% or more with non-GAAP gross margin at or above ~64% through the Ireland ramp, no new FDA enforcement, and the expanding type 2 coverage (four largest PBMs now, Medicare pending) turning into new starts.
> We expect to observe Q3 2026 (late October) and Q4 2026 (~mid-February 2027) prints that deliver the FY2026 guide (revenue $5.18-5.25B, GM ~64%, OM 23.5-24%) and a FY2027 guide of 10%-plus growth. We also expect a Medicare non-insulin type 2 coverage proposal within the next 2–4 quarters.

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| Organic revenue growth and non-GAAP gross margin | leading | Q2 2026 organic +12% ($1,298M), non-GAAP GM 64.1%, OM 25.1%; H2 guide implies +8.5% to +11.4%; CFO flagged a Q3 GM peak then an Ireland step-down and ~$15M FX headwind | Q3 organic ≥10%, FY2026 GM ~64% and OM 23.5-24% delivered, FY2027 guide ≥10% growth with GM ≥64% | Q3 or Q4 organic below ~9%, a GM guide cut, or a FY2027 guide below 10% |
| TTM EPS vs entry $2.53 / trigger $2.15 | financial confirmation | $2.53, up six quarters running (+78% y/y). The Q3 2026 print replaces Q3 2025's $0.70 (which held an $82.7M equity-investment gain), so TTM likely prints ~$2.45-2.50 in late October | Back above $2.53 by the Q4 2026 print and rising; FY2027 consensus EPS ($3.12) holds | ≤ $2.15 at a month-end before 2027-09-28 (rule exit): needs Q3 2026 GAAP EPS ≤ $0.32 vs ~$0.66 non-GAAP consensus |
| Medicare type 2 coverage, FDA status, Abbott growth | external | No Medicare proposal public (management: decision by year-end 2026, effective mid-2027). Warning letter open (no close-out found). Abbott CGM +9.5% comparable in Q2 2026 vs Dexcom organic +12% | Proposed coverage (most likely a DME MAC LCD revision) by early 2027 with broad non-insulin scope; Abbott growth stays below Dexcom's | No proposal by Q1 2027 or narrow scope; a new 483, recall or FDA action on sensor accuracy; Abbott back above Dexcom on growth as its tender delay laps |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **Equity-investment swings inside GAAP EPS:** Q3 2025 GAAP EPS $0.70 vs non-GAAP $0.61 because of $82.7M of income from equity investments (less $22.7M business-transition costs). The deep dive attributed the gap to tax; the release shows otherwise. Q2 2026 carried a $10.0M loss the other way. Together that is ~$73M of net pre-tax gain in today's $2.53 TTM (Q4 2025 not checked), and the Q3 2025 part leaves with the Q3 2026 print.
- **Shrinking interest income:** other income was $176.6M in 2025 (16% of pretax) on ~$3B of cash; after repaying $1.21B of notes and buying back stock, interest income fell to $16.9M a quarter (from $28.0M). This is why net income is 0.88x operating income. Net interest fell from $47.1M in H1 2025 to $30.3M in H1 2026, about $0.07 a share a year (derived); this is already in the 2026 guide.
- **Tax:** 2025 GAAP rate 23.2%; 2026 estimated 21.8% (Malaysia tax holiday started), H1 2026 actual 23.6% on stock-comp shortfalls. The non-GAAP rate derived from H1 2026 is ~22%, not the 17-18% the deep dive assumed; the scenarios below use 21.5%.
- **Convertible dilution:** GAAP diluted shares include 7.7M if-converted note shares (Q2 2026 diluted 390.1M vs basic 382.2M); non-GAAP EPS excludes them (~384M implied). Cash settlement in May 2028 removes them from GAAP (~2% accretion) and uses $1.25B of cash.
- **Stock comp stays in non-GAAP EPS** (only adjusted EBITDA adds it back): $159.6M in 2025, $82.3M in H1 2026. Non-GAAP EPS is close to clean; FCF is not (it adds stock comp back).
- **Litigation:** two securities class actions, one pending motion to dismiss each (S.D. Cal. filed Feb 20, 2026; S.D.N.Y. filed Jun 9, 2026), stayed derivative suits and consolidated consumer G6/G7 actions; no accrual, "unable to reasonably estimate". The deep dive attached the 2026 S.D.N.Y. dates to the 2024 guidance-cut case; corrected in the notes.
- **Buyback-driven EPS:** diluted shares -1.8% y/y (screen). The Q2 2026 purchase of 8.6M shares ($600M) cuts the share count by another ~2% from Q3.

## 5. Valuation — three scenarios, 3-year horizon

Year 3 = FY2029, valued in September 2029 on FY2029 non-GAAP EPS. Start: FY2026 revenue $5.18-5.25B (guide), non-GAAP OM 23.5-24%, net cash $549M, basic shares 377.4M. Non-GAAP net income = (revenue × OM + ~$50-60M net interest) × (1 − 21.5%). This calibrates to $2.63 for FY2026 (consensus $2.66). FY2027-28 follow the deep dive's scenario table: base FY2027 $3.06 vs its $3.10-3.15, FY2028 $3.72 vs its $3.60-3.80. **FY2029 and the multiples are this pass's extension.** Shares fall a net ~7M a year (buybacks at 50-60% of FCF less plan issuance), and the 2028 notes are repaid in cash. Net cash is not added to the price (its interest is already in EPS).

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $6.36B (FY27 +7-8% to ~$5.6B, FY28 +7% to ~$6.0B, FY29 +6%: Abbott share and Libre Duo, ASP erosion, 2028 competitive bidding, Medicare coverage delayed or narrow) | $6.98B (FY27 +10-11% to $5.78B, FY28 +10% to $6.35B, FY29 +10%: the 2030 plan's floor; ≈ consensus through FY2027) | $7.70B (FY27 +13-14% to $5.95B, FY28 +14% to $6.8B, FY29 +13%: Medicare non-insulin type 2 from mid-2027, international >15%) |
| Sustainable margin | Non-GAAP OM 24% (GM 62-63%; stuck at the 2026 level) | Non-GAAP OM 28% (GM ~66-67%; ~100-150 bp a year, short of the 29-30% 2030 target) | Non-GAAP OM 30% (2030 target a year early) |
| Net debt / cash (yr 3) | ~$2.5B net cash after repaying the notes (FCF ~$1.3B a year) | ~$2.9B net cash (FCF $1.5-1.9B a year, ~60% bought back) | ~$2.6B net cash (heavier buyback at higher prices) |
| Diluted shares (yr 3) | 362M | 358M | 355M |
| Multiple applied | 18x FY2029 EPS $3.42 (large-cap medtech: Abbott ~17.5x forward) | 25x FY2029 EPS $4.40 (≈ 22x FY2030; down from 32.6x FY2026 / 27.8x FY2027 today as growth settles at ~10%) | 30x FY2029 EPS $5.24 (about today's multiple held on a faster grower) |
| Implied price | **$62** | **$110** | **$157** |
| Total return / annualised | -29% / -10.8% | +27% / +8.3% | +82% / +22.0% |
| Probability weight | 25% | 50% | 25% |

Probability-weighted value **~$110, +27% from $86.62 (~8.2% a year)**; no dividend. The weights keep the deep dive's 25/50/25. Execution risk is down after three beat-and-raise quarters, but the multiple has already re-rated from the trough and two external items (Medicare coverage, 2028 bidding) can move the outcome either way. The path is consistent with the deep dive's 12-24 month base ($90-105, weighted ~$95): the base case at September 2027 is FY2028 $3.72 × 26-29x ≈ $97-108. Sensitivities in the base: ±1x on the FY2029 multiple = ±$4.40; ±1 point of operating margin = ±$0.15 of EPS (±$3.8 at 25x). The bear value is close to where the stock actually traded in November 2025 and April 2026 ($55-60).

What does today's price already require the business to deliver?

- At $86.62 the stock trades at 32.6x FY2026 consensus EPS ($2.66 on $5.23B, +12%) and 27.8x FY2027 ($3.12 on $5.80B, +11%), ~24x a February-vintage FY2028 ($3.60), and 22.9x EV/TTM FCF (4.4% FCF yield on EV). Consensus is third-party: S&P Global via [StockAnalysis](https://stockanalysis.com/stocks/dxcm/forecast/) and Yahoo, with 28 analysts, "Strong Buy" and an average target of $94.48 (range $79-115). MarketBeat shows a lower $2.46 for FY2026; S&P/Yahoo is preferred because it reconciles with the guide.
- Reverse-implied, two lenses. (1) Reverse DCF on EV $32.1B and TTM FCF $1.405B, with 3% terminal growth and a 9% discount rate: ~6.8% a year of FCF growth for ten years (8.4% if stock comp is treated as cash; 4.3-5.9% at 8%). That is below management's 10%-plus revenue plan with margin expansion. (2) Exit multiple: earning 9% a year to September 2029 at 25x needs FY2029 EPS of ~$4.49, about 19% a year from $2.66. That is essentially the base case.
- So the price already discounts the base case at a high-single-digit return and does not require the bull case. What it does require is that the multiple settle no lower than ~25x current-year earnings. Returns above ~8% a year need Medicare coverage or margins running ahead of the 2030 plan.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 6.9 | 12.1 | 4.9 | 28.1 | 0.22 | 25.4 | 2010-03-31 |
| EV/EBITDA | 23.6 | 57.7 | 17.5 | 136.5 | 0.12 | 122.7 | 2018-12-31 |
| P/E (trailing) | 34.2 | 82.7 | 25.6 | 241.3 | 0.08 | 93.0 | 2013-05-31 |

At the 5-year median P/S (12.1) on today's TTM revenue the price would be about $153 (+76%); at the 5-year low (4.9), about $62 (-28%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.15, growth +16%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$2.15** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (net cash today)
- **Price target where recovery is fully reflected:** trim half at **$130** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** medical devices (PODD, DXCM, BSX): a third of the basket; PODD and DXCM also share the diabetes / GLP-1 / competition narrative; same-driver holdings: PODD, BSX
- **Research overlay (not part of the rule):** More confident on:
  - a Q3 print with organic growth ≥10% and the FY2026 GM/OM guide delivered through the Ireland step-down;
  - a Medicare non-insulin type 2 coverage proposal before early 2027 with broad scope;
  - Abbott's comparable CGM growth staying below Dexcom's organic growth;
  - an FDA close-out of the March 2025 warning letter;
  - dismissal of either securities case.

  Less confident on:
  - Q3 or Q4 organic growth below ~9%, or any GM guide cut;
  - a FY2027 guide below 10% growth;
  - no Medicare proposal by Q1 2027, or a narrow one;
  - a new 483, recall or FDA action on sensor accuracy;
  - Libre Duo taking type 1 / pump share faster than G8 (late 2027 to early 2028) can answer;
  - FY2027 consensus EPS falling below ~$3.00.

  The proxy is slow for this name. The Q3 2026 print will likely leave TTM EPS flat (~$2.45-2.50) because Q3 2025's $82.7M investment gain rolls off; that is not an operating stall. A $2.15 print needs Q3 GAAP EPS of $0.32 or less, so a disappointment would show in price long before the rule fires.

  Dated catalysts:
  - revolver maturity: Oct 13, 2026 (renewal not yet disclosed);
  - Q3 2026 results: late October, not yet announced (third-party estimate Oct 29; last year Oct 30), with the first TTM EPS update at the Oct 31 month-end;
  - Medicare non-insulin type 2 coverage decision: by year-end 2026 per management, effective mid-2027;
  - DMEPOS competitive-bidding window: late 2026, contracts in 2027, in effect by Jan 1, 2028;
  - Abbott Libre Duo US rollout: late 2026;
  - rulings on the motions to dismiss (S.D. Cal., filed Feb 20, 2026; S.D.N.Y., filed Jun 9, 2026): no dates set;
  - preliminary Q4 at the J.P. Morgan conference: ~mid-January 2027;
  - Q4 2026 results and FY2027 guide: ~mid-February 2027;
  - Q1 2027 results: ~late April 2027;
  - buyback authorization expires: Jun 30, 2027;
  - 2028 notes: freely convertible from Feb 15, 2028, due May 15, 2028.

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #8: val 0.15, growth +16%, entry TTM EPS $2.53, trigger $2.15, trim $130 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/DXCM.md) | Supports the rule buy. Cause = valuation compression triggered by temporary execution; survival PASS ($1.95B cash vs the $1.25B May 2028 notes; small undrawn revolver maturing Oct 13, 2026); 3-year probability-weighted value ~$110 (+27%, ~8% a year); the $2.15 trigger needs Q3 2026 GAAP EPS ≤ $0.32. Corrects the deep dive: the Q3 2025 GAAP > non-GAAP gap was an $82.7M equity-investment gain, not tax; the Apr 10 / Jun 9, 2026 filings belong to the S.D.N.Y. G7 case, not the 2024 guidance-cut case; the non-GAAP tax rate is ~22%, not 17-18%. review_deadline kept at 2027-03-27 (after the second report from today, the Q4 2026 print in ~mid-February 2027) |

## 8. Research conclusion

Dexcom fits the rule's intent. Earnings roughly tripled over three years while the multiple fell from ~95x to 34x trailing, the one real setback (2024-25 execution and quality) has been repaired for three quarters running, and the balance sheet takes survival off the table. The research supports the buy, but as a moderate-return, lower-variance holding, not a deep-value one: the 3-year probability-weighted value is about $110 (+27%, ~8% a year) against a bear case of about $62. Today's price already discounts roughly the base case, and the 2026 re-rating from $54.84 has happened.

The single most important thing to watch is the Medicare non-insulin type 2 coverage decision (management expects it by year-end, effective mid-2027). It is the main route to the bull case, and a delay or narrow scope is the shortest route to the bear. The late-October Q3 print (organic growth ≥10% through the flagged gross-margin step-down) is the nearer test.

In the basket, DXCM and PODD are the same diabetes-technology trade at different stages. Both carry CMS, competitive-bidding, GLP-1 and Abbott risk, so together they are 20% of the book on one theme (30% of medtech with BSX). They are partly self-hedging, though: Insulet's type 2 churn mostly leaves patients on a sensor, and Omnipod 5 works with both Dexcom and Libre. DXCM is the lower-beta, higher-confidence half, while PODD offers the larger expected return with a wider range. DXCM is also one of the names least likely to be sold early by the EPS proxy, unlike DT or NOW. Its drivers are unrelated to the five software names (APPF, INTU, DT, NOW, VEEV), KNSL and OLLI.
