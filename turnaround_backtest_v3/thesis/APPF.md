# APPF — AppFolio

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #3 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-02-28 |
| Monthly RSI, last completed candle | 56.6 |
| Episode months / min RSI | 5 / 37.4 |
| Drawdown from trailing 5-year high | -36.4% (high 321.25 on 2025-08-04) |
| Market cap / avg daily $ volume (3m) | $7.23B / $72M |
| Sector / industry | Information Technology / Application Software |
| Survival gate (proxy) | PASS — cash $222M, debt due <1y $5M, FCF TTM $266M, 24m gap -$217M |
| Net debt / EBITDA, interest coverage | -0.9 / n/a |
| Valuation | P/E trailing 46.5, P/E forward 24.2, PEG 7.45, P/S 6.95, EV/Sales 6.8, EV/EBITDA 34.3, P/FCF 27.2 |
| EPS | TTM 4.38, forward est. 8.43; growth YoY (TTM) -30.1%, last quarter +18.2%, implied forward +92.5% |
| Revenue YoY (last quarter) | +19.3% |
| Profitable years (of reported) | 3 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 3 of 10 / 7 of 20 |
| TTM revenue growth | +21% (latest quarter 2026-06-30) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.09** — P/S 0.14, EV/EBITDA 0.05, EV/EBIT 0.06 (P/E pct 0.31, not used) |
| Multiples today | P/S 7.0, EV/EBITDA 35.0, EV/EBIT 39.0, P/E 46.5 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 50.1 / 38.7 |
| From 5-year high | -36% |
| TTM EPS path, 6 quarters (oldest first) | 5.36, 5.54, 5.57, 3.88, 4.20, 4.39 |
| TTM EPS vs 12 months earlier | -21% |
| One-off EPS guard | passed — TTM net income / operating income 0.86 |
| Acquisition guard | passed — diluted shares -2.1% y/y |
| Net debt / EBITDA | net cash |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 48 shares per $100k at Friday's $204.22).
Entry TTM EPS **$4.39** → guide-cut trigger **$3.73** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$306** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val ≤ 0.10: n 218, mean +38%, median +23%, 80% winners, 58% beat SPY; less than 40% below: n 306, mean +14%, median +13%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Fair.

- Reward case: EV/EBITDA and EV/EBIT at the cheapest 5-6% of its history, net cash, 21% growth; TTM EPS rising again for two quarters. In the running portfolio since July 2026 at $164.82 (+42% to August).
- Main risks under these rules: The -21% EPS change is the tax item that left the trailing year in Q4 2025; the $4.39 entry base is clean, so the trigger ($3.73) needs an operating miss. Monthly RSI already back at 50; P/S 7 in a sector being re-rated.

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression**. The multiple fell with the software sector's AI-disruption de-rating and with guidance that implied slower growth (20% in 2025 to about 17% in 2026). Operations did not weaken: revenue, GAAP operating income and margins are all higher than at the high, and the EPS drop is a tax item leaving the trailing year.  <!-- inventory cycle | financing-sensitive demand | temporary execution | excess industry capacity | valuation compression | structural deterioration -->

Narrative (price legs are cache closes; figures are from the 8-K earnings exhibits and 10-K/10-Q; details and URLs in the [research notes](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/APPF.md)):

- **2025-07-31, Q2 2025 report: +19.4% to the high.** Revenue $235.6M (+19%); FY2025 guide raised to $935-945M from $920-940M. The 5-year high close of $321.25 came on 2025-08-04. The TTM GAAP EPS at the time ($5.54) contained the Q4 2024 tax benefit.
- **2025-08-04 → 09-26: -13%** (SPY +5%). The stock gave back the post-report gap by mid-August ($265) and held $275-285 through September. No company news found.
- **2025-09-26 → 10-10: -19%** ($278.53 → $224.87; 10-01 -6.9%). SPY -1%, INTU -8%. **No source found for the cause.** The only filing in the window is the 2025-09-30 $150M revolver 8-K.
- **2025-10-30, Q3 2025 report: +7.9% the next day.** Revenue $249.4M (+21%), FY revenue guide raised to $945-950M. The non-GAAP operating margin guide was cut to 23.5-24.5% from 24.5-26.5%: bonus over-attainment, AI data-center cost, sales capacity, product investment, mix. Non-GAAP EPS was $1.31 against a $1.46 consensus (third party).
- **2025-11-03 → 12-31: -11%.** Most of it came 11-17 to 11-19 (-10.6%) around the 2025-11-18 investor meeting, which gave no multi-year revenue or margin targets. No reaction coverage found, so the link is unverified. NOW fell 16% over the same weeks.
- **2026-01-12 → 01-28: -6% to $218.** The software sell-off started when Anthropic launched Claude Cowork (01-12). INTU fell 19% and NOW 15% from 12-31 to 01-28.
- **2026-01-29, Q4 2025 report: -8.3% the next day; -18.6% from 01-28 to 02-05 ($177.36).** Q4 beat: revenue $248.2M (+22%), non-GAAP EPS $1.39 against $1.25 consensus. But the FY2026 guide of $1.10-1.12B (+16.7% at the midpoint) was below the $1.13B consensus. 02-03 (-5.7%) was the "SaaSpocalypse" day after the Claude Cowork plugins. Five brokers cut targets on 01-30, e.g. DA Davidson $325 → $275 on "weaker than expected value-added services revenue and conservative 2026 guidance". VAS fell sequentially to $184.6M from $192.1M in Q3.
- **2026-02-05 → 04-10: -19% to the low close of $143.34 (-55.4% from the high).** No company event; IGV was down 23-24% year to date. From the high to that low, APPF, INTU and NOW each fell 55%, the clearest sign this was a sector multiple, not an APPF problem.
- **Recovery.** 2026-04-23, Q1 2026: revenue +20%, GAAP operating income +50%, FY guide raised to $1.110-1.125B and 26-28% margin; +11.2% the next day. 2026-07-23, Q2 2026: revenue $281.1M (+19%), guide raised again to $1.117-1.127B and 26.5-28.0%; +0.7%. August +30% (NOW +33%, a sector rebound). September -13% to $204.22 (INTU -23% in the same weeks).
- Net: 12-month price -26% and TTM GAAP EPS -21% (5.54 → 4.39). Over the same year, revenue was +21% and TTM GAAP operating income +30% ($139.8M → $182.3M). Excluding the Q4 2024 tax benefit, TTM EPS is about +32% (≈$3.33 → $4.39).

Was the prior high an exceptional earnings peak or an unsustainable multiple? **Multiple, not an earnings peak.**

- Margins are higher now than at the high. TTM GAAP operating margin was 16.2% at 2025-06-30 and is 17.5% at 2026-06-30 (19.1% in H1 2026). The non-GAAP margin guide went from 24.5-26.5% (Aug 2025) to 26.5-28.0% (Jul 2026). Revenue per share is +23%.
- The headline P/E at the high (50x on $5.54) understated the multiple. On tax-normalized TTM EPS of about $3.33, the August 2025 month-end price of $277 was about 83x, with P/S 11.8 and EV/EBITDA 62.5. Today: P/S 7.0, EV/EBITDA 35, EV/EBIT 39, all at the 5-14th percentile of the company's own history.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $217.4M cash + $4.3M current investments = $221.7M; no borrowings (the $35.8M "total debt" in section 1 is the operating-lease liability) | 10-Q 2026-06-30; fundamentals cache |
| Realistically available credit (undrawn revolver, covenants) | $150M senior secured revolver (PNC, signed 2025-09-30, matures 2030-09-30), **fully undrawn**. One maintenance covenant: consolidated net leverage ≤ 3.75x (4.25x after an acquisition); today below zero. Accordion to the greater of $225M or 100% of EBITDA | [8-K 2025-09-30](https://www.sec.gov/Archives/edgar/data/1433195/000143319525000134/appf-20250930.htm); FY2025 10-K; Q2 2026 10-Q |
| Debt maturities next 24 months | **none** (no borrowings). Lease payments $6.7M (2026) and $6.8M (2027) | FY2025 10-K lease note |
| Cash consumption if weak conditions persist 24 months | none: FCF TTM $266M (FY2025 $236M after capitalized software); proxy 24m gap -$217M | fundamentals cache; 10-K cash-flow statement |
| Interest, maintenance capex, leases, other fixed obligations | Interest: none (net interest income $8.2M in 2025). Capex + capitalized software $6.6M in 2025. Leases $44.8M undiscounted to 2030+. Purchase commitments $31.3M (mostly over 3 years). Cloud commitment ≥ $219.3M through 2031 ($36.2M within 12 months, signed Jan 2026) | FY2025 10-K; Q2 2026 10-Q |
| Can recovery happen without a large equity raise? | yes | net cash, FCF about 25% of revenue, $125M of buyback authorization left |

Gate verdict: **PASS** — reasoning:

- There is no debt and the revolver is undrawn. Fixed obligations over the next 24 months (leases about $14M, about $36M of the cloud commitment in the first year, part of the $31.3M purchase commitments) are small against $266M of TTM FCF and $222M of cash. Survival is not a question for this name. The capital decisions that matter are discretionary: $125M bought back in Q1 2026 at $177.95 average, and the $75M Second Nature stake in 2025.

## 4. Recovery thesis  (testable statement)

> The business weakened because of **nothing operating. The stock de-rated with software (AI-disruption fear) while FY2026 guidance implied growth slowing from 20% to about 17%, and reported TTM EPS fell only because a $75.6M Q4 2024 tax benefit left the trailing year.** Recovery requires **revenue growth holding in the high teens (units +7-8%, premium-tier and VAS-per-unit gains), GAAP operating margin continuing to widen, and evidence that agentic AI is a product AppFolio sells (Realm-X Performers on per-unit, per-transaction pricing) rather than a substitute for it.**
> We expect to observe **FY2026 revenue at or above the $1.117-1.127B guide, a FY2027 revenue guide at or above about $1.30B (consensus $1.32B) with the non-GAAP margin at 27% or higher, and TTM GAAP EPS above $4.39 at the Q3 2026 report and not below it after Q4** within the next 2–4 quarters.

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| Units under management and VAS revenue per unit (premium-tier share as colour) | leading | Q2 2026: 9.6M units (+8%); VAS $219.5M (+22%), so VAS per unit about +13%; premium tiers "nearly 1 in 3" units (25% in 2025) | units growth ≥ 7% and VAS growth ≥ 18% in Q3/Q4 2026; premium share still rising in the Q4 call | units growth below 6% or VAS growth below 15% for a quarter, or a second sequential VAS miss like Q4 2025 |
| TTM EPS vs entry $4.39 / trigger $3.73 | financial confirmation | $4.39 (-21% y/y; about +32% excluding the Q4 2024 tax benefit) | flat or rising at each month-end | prints at or below $3.73 at a month-end before 2027-09-28 (rule exit) |
| TTM revenue growth (entry +21%) and FY guidance | organic growth / guidance | +21% TTM; Q2 2026 +19%; FY2026 guide $1.117-1.127B (+18% at the midpoint), raised twice | holds double digits; latest quarter ≥ year-ago quarter; FY2027 guide ≥ +15% | latest quarter below its year-ago quarter (fails the organic screen), or a FY2026 guide cut / FY2027 guide under +13% |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **Tax (verified).** Q4 2024 carried a $75.6M tax benefit from the valuation-allowance release (Q4 2024 GAAP EPS $2.79 vs non-GAAP $0.92). It sat in TTM EPS through 2025-09-30 and left at 2025-12-31 (5.57 → 3.88). The $4.39 base is clean of it.
- **Tax-rate drift inside the base.** FY2025 effective tax rate was 12.5% (Q3 2025 about 8%) vs 21.9% in H1 2026. The low-tax Q3 and Q4 2025 quarters ($0.93, $1.10) roll off next. At about 23% ETR, Q4 2026 needs about $51M of pre-tax income to match $1.10 (Q2 2026: $54.4M). So expect TTM EPS up at the Q3 report and roughly flat at the Q4 report.
- **Second Nature stake.** $75M, April 2025, carried at cost; long-term investments were $87.7M at 2026-06-30. Any impairment is a GAAP charge below operating income. A full write-off would be roughly $1.6-2.1 per share depending on tax treatment (my estimate), and a write-down of about $25-30M would already take TTM EPS to the trigger. Either is enough to reach the $3.73 trigger without an operating miss. This is the main non-operating route to a mechanical exit.
- **Stock comp.** $70.8M in 2025 (7.4% of revenue), plus $43.2M of withholding tax on net-settled shares. The non-GAAP margin is about 8 points above GAAP. Consensus EPS ($6.90 FY2026, $8.43 FY2027) is non-GAAP.
- **Working capital.** Bonus accrual moved to annual payment: accrued bonuses rose to $43.3M at 2025-12-31 from $17.1M, which flattered 2025 OCF and was paid in Q1 2026 (OCF 13% of revenue). VAS is seasonal, peaking in Q2-Q3, so Q4 VAS dips sequentially.
- **Acquisitions.** LiveEasy ($78.5M, Oct 2024) is small; diluted shares -2.1% y/y from buybacks.

## 5. Valuation — three scenarios, 3-year horizon

Yr 3 = trailing year to 2029-09-30, grown from the FY2026 guide midpoint ($1.122B). Value = EV/EBIT on GAAP EBIT (after stock comp) plus net cash. EV/EBIT is today 39x (6th percentile of its own history); every multiple below is under the company's historical range, reflecting the sector de-rating.

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $1.48B (growth 14% / 10% / 7% in 2027-29) | $1.69B (17.5% / 16% / 14%; 2027 = consensus $1.32B) | $1.77B (19% / 18% / 17%) |
| Sustainable margin | GAAP EBIT 18% (flat vs today's 17.5%: AI and data-center cost absorb leverage) | GAAP EBIT 23% (non-GAAP about 30% less about 7% stock comp) | GAAP EBIT 28% |
| Net debt / cash (yr 3) | net cash $0.50B | net cash $0.45B | net cash $0.40B |
| Diluted shares (yr 3) | 35.5M | 34.5M | 33.5M |
| Multiple applied | 18x EV/EBIT (≈3.2x EV/S, ≈25x GAAP P/E) | 26x EV/EBIT (≈6.0x EV/S, ≈34x GAAP P/E) | 30x EV/EBIT (≈8.4x EV/S, ≈39x GAAP P/E) |
| Implied price | $149 | $305 | $456 |
| Total return / annualised | -27% / -10% | +50% / +14% | +123% / +31% |
| Probability weight | 30% | 50% | 20% |

**Probability-weighted value ≈ $289 (+41% over 3 years, about 12% a year).**

Key assumptions:
- Bear: agentic AI and platform consolidation compress what property managers pay per unit. VAS per-unit growth stalls, unit growth slows to about 5%, and the market prices APPF as a no-growth payments processor.
- Base: consensus for 2027, then a gentle fade. Margin expansion continues at about the 2025-26 pace (non-GAAP margin from 24.7% in 2025 to a 26.5-28.0% guide for 2026).
- Bull: resident services (Second Nature, LiveEasy, Resident Onboarding Lift) and premium tiers keep VAS per unit growing double digits while units grow 8%.
- In all three, net cash assumes most FCF goes to buybacks (no company target).
- Weights lean bearish because the sector de-rating has not reversed (INTU -23% in September) and half the v3 basket shares that driver.

What does today's price already require the business to deliver?

- Consensus (stockanalysis.com, 2026-09-28, third party): FY2026 revenue $1.12B (+18%), non-GAAP EPS $6.90; FY2027 revenue $1.32B (+17.5%), non-GAAP EPS $8.43. At $204.22 that is 29.6x FY2026 and 24.2x FY2027 non-GAAP EPS; GAAP trailing P/E 46.5. Average target $234 (range $200-280, 10 analysts).
- Reverse test (23% GAAP EBIT margin in 2029, $0.45B net cash, 34.5M shares). A 10% a year return needs revenue to compound about **13% a year** from the $1.04B TTM if the exit multiple is 26x EV/EBIT, or about **19%** at 22x. A flat price in 3 years needs only about 8% growth at 22x.
- So today's price requires roughly the guided/consensus path only if the multiple keeps compressing. If the multiple holds in the mid-20s, the price discounts growth well below the 17-18% being guided.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 7.0 | 10.3 | 5.8 | 15.4 | 0.14 | 11.8 | 2015-06-30 |
| EV/EBITDA | 35.0 | 59.8 | 29.6 | 392.6 | 0.05 | 62.5 | 2017-03-31 |
| P/E (trailing) | 46.5 | 50.1 | 30.8 | 3,773.7 | 0.31 | 50.1 | 2017-09-30 |

At the 5-year median P/S (10.3) on today's TTM revenue the price would be about $297 (+46%); at the 5-year low (5.8), about $169 (-17%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.09, growth +21%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$3.73** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (net cash today)
- **Price target where recovery is fully reflected:** trim half at **$306** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** de-rated software (APPF, INTU, DT, NOW, VEEV): half the basket, one shared driver (AI-disruption / seat-pricing narrative and sector multiple); same-driver holdings: INTU, DT, NOW, VEEV
- **Research overlay (not part of the rule):**
  - More confident if: Q3 2026 units growth holds ≥ 8% and VAS ≥ 20%; the FY2027 guide (late January 2027) starts at or above consensus ($1.32B) rather than about 2% below it as in January 2026; premium tiers move past one-third of units; buybacks continue near current prices.
  - Less confident if: VAS misses again in the seasonally weak Q4; unit growth drops below 7%; the non-GAAP margin guide is cut a second time (as in Oct 2025); any impairment or write-up/down of the Second Nature stake appears; or agentic tools from horizontal vendors show up in customer-count losses (22,751 customers, +6%).
  - Dated catalysts: Q3 2026 results expected late October 2026 (not yet announced; 2024-10-24 and 2025-10-30 precedents). Q4 2026 results and FY2027 guidance expected late January 2027 (2025-01-30, 2026-01-29 precedents). 2026 investor meeting: no date found (2025's was 2025-11-18). No scheduled regulatory decision or litigation milestone found; standing exposures are FCRA tenant-screening obligations (2020 FTC settlement) and the algorithmic-pricing antitrust risk the 10-K flags without a named case.

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #3: val 0.09, growth +21%, entry TTM EPS $4.39, trigger $3.73, trim $306 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/APPF.md) | Supports the entry: valuation compression with improving operations, tax item verified, weighted value ≈ $289 vs $204.22; main exit risk is a GAAP one-off (Second Nature stake). review_deadline kept (falls after the expected late-January Q4 report) |

## 8. Research conclusion

The research supports the rule's buy. The 36% fall from the August 2025 high is a multiple story: APPF tracked INTU and NOW almost exactly to a -55% low in April 2026, while revenue grew 21%, GAAP operating income 30%, and 2026 guidance was raised twice; the -21% EPS change is only the Q4 2024 tax benefit leaving the trailing year. Scenario value weighted 30/50/20 is about $289 (+41% over three years), with a bear case near $149 if agentic AI compresses what property managers pay per unit. The single most important thing to watch is the FY2027 guide in late January 2027 against the $1.32B consensus, together with unit and VAS-per-unit growth; the $3.73 trigger is realistically reachable only through a GAAP one-off such as a Second Nature write-down. In the basket, APPF adds to the software cluster (INTU, DT, NOW, VEEV), so a sector leg down hits half the book together, though its per-unit and payments revenue ties it more to US rental housing than to seat counts and it has no fundamental overlap with PODD, DXCM, BSX, KNSL or OLLI.
