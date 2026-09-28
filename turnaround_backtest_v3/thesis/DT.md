# DT — Dynatrace

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #6 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-01-31 |
| Monthly RSI, last completed candle | 59.7 |
| Episode months / min RSI | 4 / 35.3 |
| Drawdown from trailing 5-year high | -26.4% (high 78.76 on 2021-10-22) |
| Market cap / avg daily $ volume (3m) | $16.75B / $311M |
| Sector / industry | Information Technology / Application Software |
| Survival gate (proxy) | PASS — cash $1.11B, debt due <1y $23M, FCF TTM $571M, 24m gap -$1.09B |
| Net debt / EBITDA, interest coverage | -3.2 / n/a |
| Valuation | P/E trailing 115.9, P/E forward 25.2, PEG 1.18, P/S 8.03, EV/Sales 7.5, EV/EBITDA 53.0, P/FCF 29.4 |
| EPS | TTM 0.50, forward est. 2.30; growth YoY (TTM) -66.0%, last quarter -25.0%, implied forward +359.3% |
| Revenue YoY (last quarter) | +16.2% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 6 of 10 / 9 of 20 |
| TTM revenue growth | +18% (latest quarter 2026-06-30) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.14** — P/S 0.13, EV/EBITDA 0.14, EV/EBIT 0.14 (P/E pct 0.54, not used) |
| Multiples today | P/S 8.4, EV/EBITDA 60.4, EV/EBIT 64.7, P/E 115.9 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 62.7 / 36.2 |
| From 5-year high | -26% |
| TTM EPS path, 6 quarters (oldest first) | 1.59, 1.62, 1.67, 0.60, 0.54, 0.50 |
| TTM EPS vs 12 months earlier | -69% |
| One-off EPS guard | passed — TTM net income / operating income 0.60 |
| Acquisition guard | passed — diluted shares -0.3% y/y |
| Net debt / EBITDA | net cash |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 172 shares per $100k at Friday's $57.95).
Entry TTM EPS **$0.50** → guide-cut trigger **$0.43** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$87** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val 0.10-0.25: n 222, mean +17%, median +16%, 66% winners, 52% beat SPY; less than 40% below: n 306, mean +14%, median +13%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Bought by the rule; likeliest mechanical exit of the ten.

- Reward case: 18% growth at the 13-14th percentile of all three multiples; net cash of about 4x EBITDA. Bought by v3 in the backtest's last window (+48%).
- Main risks under these rules: **Least distressed and highest proxy-exit risk.** Monthly RSI 63 and only 26% below the high (qualified on the March-April dip). The drop from 1.67 to 0.60 four quarters ago is a non-operating item leaving the trailing year, so the $0.50 base is clean, but TTM EPS has drifted down 10% and 7% in the last two quarters; two more such quarters reach the $0.43 trigger without any operating miss. P/E 116, P/S 8.4.

Repository research: [working notes and sources](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/DT.md)

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression** — revenue per share is up 167% since the 2021 peak and non-GAAP earnings roughly 2.5x, while P/S fell from 29.0 to 5.8 at the April 2026 low (8.4 now); the 2026 dip was the sector-wide AI-disruption de-rating of software plus a decelerating FY27 guide, and the GAAP EPS drop is tax accounting, not operations  <!-- inventory cycle | financing-sensitive demand | temporary execution | excess industry capacity | valuation compression | structural deterioration -->

Narrative (what actually happened, with dates and numbers from the filings):

- **Leg 1, Oct 22, 2021 → May 11, 2022: $78.76 → $30.11 (-62%).** The peak came with ARR growing 35% and P/S 29.0, EV/EBITDA 222, trailing P/E 288 (valuation cache). Oct 27, 2021 -9.9% on a beat-and-raise Q2 FY22 print (ARR $864M, +35%; cause of the reaction: no source found). Nov 15, 2021: CEO John Van Siclen's retirement and Rick McConnell's appointment (-4.7%). Feb 2, 2022 -18.0% on Q3 FY22: ARR growth slowed to 29% reported (32% cc) from 35%, non-GAAP operating margin 25% vs 29% a year earlier, and a plan to step up investment ([Q3 FY22 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338322000019/fy22q3-earningsreleaseex991.htm)). The rest was the 2022 rate-driven software de-rating.
- **Recovery to $62.42 (Feb 12, 2025)**, the post-2021 high, on 20%+ ARR growth and margin expansion; P/S about 10.7.
- **Leg 2, Feb 12, 2025 → Apr 10, 2026: $62.42 → $32.36 (-48%).** Operations held up throughout: ARR growth at 16-17% cc in each of the last five quarters, FY26 revenue +19%, non-GAAP EPS $1.70 vs a $1.56-1.59 initial guide, FCF $529M. The fall came in steps without an earnings miss: -7.2% on Aug 7, 2025 after a Q1 FY26 beat-and-raise (cause: no reliable source), -7% over Nov 5-6, 2025 after Q2 FY26, then **-6.9% on Jan 29 and -9.1% on Feb 3, 2026** in the software sell-off triggered by AI-agent disruption fears ([Axios](https://www.axios.com/2026/02/03/ai-software-anthropic-stock-market)). This was the first oversold monthly candle (January 2026, RSI episode min 35.3). Q3 FY26 (Feb 9) beat, raised and added a $1B buyback (+7.3%); Apr 9-10, 2026 -12% over two days (cause: no source found) set the $32.36 low at P/S 5.8 and EV/EBITDA 36.8.
- **May 13, 2026, -11.4%**: Q4 FY26 beat, but the FY27 guide showed deceleration (ARR 15.5-16.5% cc, revenue 14-15% cc) and a Q1 non-GAAP EPS guide of $0.44-0.45, slightly below consensus ([Motley Fool](https://www.fool.com/investing/2026/05/13/why-dynatrace-stock-plummeted-today/), third-party). In the same month Datadog printed +32% growth, which sharpened the share-loss narrative.
- **Rebound, Apr 10 → Sep 25, 2026: +79% to $57.95.** Aug 5, 2026 +11.3% on Q1 FY27: net new ARR +66% (+41% organic), ARR $2,136M (+17%), non-GAAP EPS $0.48 vs a $0.44-0.45 guide, FY27 EPS guide raised to $1.97-1.99 ([Q1 FY27 release](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000049/q1fy27-earningsreleaseex99.htm)). On Sep 18 Needham upgraded to Buy with a $68 target. P/S is back at 8.4, still the 13th percentile of its own history.
- **GAAP EPS (the rule's figure) tells a different story, and it is tax-driven.** The 1.67 → 0.60 drop in the Dec 2025 quarter was Q3 FY25's **$320.9M ($1.06/share) deferred-tax benefit from the intra-group transfer of Dynatrace IP to Switzerland** leaving the TTM. This was a deferred-tax-asset recognition, not a valuation-allowance release. Since that transfer the GAAP tax rate has run 45-55% (FY26 45.7%: GILTI, foreign-branch and US royalty tax on the transferred IP, nondeductible compensation). As a result, GAAP EPS was $0.54 in both FY25 (ex-IP benefit) and FY26 while revenue grew 19% ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000019/dt-20260331.htm) Note 9).
- 5-year high 78.76 on 2021-10-22; price now -26%. From that month's close (75.00) P/S went from 29.0 to 8.4 (-71%) while TTM revenue per share changed +167%: the fall is all multiple (price and valuation caches, derived).
- 12-month price return +19%; TTM EPS -69% over the same span; revenue +18%.

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **Unsustainable multiple — not an earnings peak.** At the Oct 2021 high, TTM revenue was $816M, GAAP operating income $87M, and quarterly non-GAAP operating margins ran 25-29% (Q3 FY21 29%, Q3 FY22 25%). Now revenue is $2,096M, GAAP operating income $255M (EDGAR cache) and the non-GAAP margin 29-30%, so margins and earnings are higher today. The high priced 29x sales and 222x EBITDA for a company whose ARR growth then halved (35% → 16-17%). What has changed for the worse is the growth rate, not profitability.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $1.11B (cache); 10-Q: cash $1,057.8M + $94.8M marketable securities. No financial debt: the cache's "total debt" $159M is operating-lease liabilities | fundamentals cache; [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1773383/000177338326000050/dt-20260630.htm) |
| Realistically available credit (undrawn revolver, covenants) | $400M secured revolver, undrawn, $398.9M available ($1.1M letters of credit); one financial covenant, a maximum leverage ratio (level not in the filing text; not binding with zero debt); in compliance | 10-Q Note 8, 10-K Note 11 |
| Debt maturities next 24 months | none: no borrowings. The revolver itself matures Dec 2, 2027 and will need renewal, but it is not funding anything | 10-Q Note 8 |
| Cash consumption if weak conditions persist 24 months | none: FCF TTM $571M (Q1 FY27 adjusted FCF $309M; FY27 guide $610-615M). Buybacks ($573M left on the $1B program) are discretionary | fundamentals cache, Q1 FY27 release |
| Interest, maintenance capex, leases, other fixed obligations | no interest expense beyond revolver fees; net interest income $47.7M in FY26. Capex ~$28-32M a year. Lease payments FY27 $28.4M, FY28 $25.4M ($164.3M liability). Purchase obligations (mostly cloud hosting) FY27 $152.5M, FY28 $164.8M ($525.3M total); all contractual commitments $721.2M, $180.8M within 12 months | 10-K Notes 12-13, MD&A |
| Can recovery happen without a large equity raise? | yes | net cash, FCF ~26% of revenue |

Gate verdict: PASS — reasoning:

- There is no debt, net cash is about $1.15B, and FCF of about $600M a year covers two years of all fixed commitments (~$370M of leases and purchase obligations in FY27-28) several times over. The only things to track are the revolver renewal before Dec 2027 (routine) and whether buybacks run down cash (Q1 FY27 $275M against $309M FCF). Survival is not the question for this name.

## 4. Recovery thesis  (testable statement)

> The business weakened because of a de-rating of software multiples on AI-disruption and share-loss-to-Datadog fears, plus growth slowing from 35% to 16% ARR growth, while earnings and margins kept rising (the GAAP EPS fall is tax, not operations). Recovery requires ARR growth to hold or reaccelerate at 16%+ cc on DPS consumption, logs and AI-workload monitoring, with net new ARR growth in double digits, so the market treats Dynatrace as an AI beneficiary rather than a seat-based victim.
> We expect to observe FY27 ARR at or above the $2,359-2,379M guide with net new ARR up 16-23% (FY27 guide $320-340M), net retention at 110% or better, and GAAP EPS stabilising at $0.14-0.19 a quarter as SBC shortfalls fade within the next 2–4 quarters (Q2 FY27 in early November 2026, Q3 FY27 in early February 2027).

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| Net new ARR growth and cc ARR growth (with dollar-based net retention) | leading | Q1 FY27 net new ARR $85M, +66% (+41% organic, ex-Bindplane $13M); ARR +17% cc; NRR 110%; FY27 guide 15.5-16.5% cc, net new ARR $320-340M | ARR growth ≥ 16% cc in Q2 and Q3; FY27 guide held or raised in cc terms; NRR ≥ 110%; logs keep doubling (now ~$200M annualized) | cc ARR guide cut, or ARR growth < 15% cc; NRR < 109%; net new ARR growth turning negative y/y |
| TTM EPS vs entry $0.50 / trigger $0.43 | financial confirmation | $0.50 (-69% y/y); quarterly GAAP EPS $0.19, $0.13, $0.06, $0.12; ETR 54.6% in Q1 FY27 | Q2 FY27 GAAP EPS ≥ $0.14 (TTM ≥ $0.45 in November) and Q2+Q3 ≥ $0.30 (TTM ≥ $0.48 in February); ETR back below ~50% | prints at or below $0.43 at a month-end before 2027-09-28 (rule exit): Q2 ≤ $0.12 in November, or Q2+Q3 ≤ $0.25 in February |
| Non-GAAP operating margin and adjusted FCF vs guide (cross-check that the GAAP drift is tax only) | operating | Q1 FY27 29% margin, adjusted FCF $309M; FY27 guide 29.5-29.75%, $610-615M | margin ≥ 29.5% for FY27 and GAAP operating income still growing ≥ 15% y/y | margin guide cut, or a new impairment/restructuring charge (FY26 had $28.1M incl. an $18.5M impairment) |
| TTM revenue growth (entry +18%) |  | +18% | holds double digits; latest quarter ≥ year-ago quarter | latest quarter below its year-ago quarter (fails the organic screen) |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **IP transfer tax benefit:** $320.9M ($1.06/share) in Q3 FY25 (Dec 2024). It left the TTM in the Dec 2025 quarter, so the $0.50 base is clean of it. There is a mirror effect: the resulting deferred tax asset (intangible-asset DTA $270.5M at March 31, 2026) is consumed through 2035, and the US side of the transfer is taxable through 2044. That keeps the GAAP rate structurally high at about 45% (FY26), versus about 27% in FY25 before the transfer. The company says OBBBA will have no material impact. No further rate normalisation downward is signalled.
- **SBC shortfalls:** the Q1 FY27 ETR of 54.6% (vs 41.1%) is mostly shortfalls on RSUs vesting below their grant price, when the stock was in the high $30s (Q1 buybacks averaged $38.88). The effect is roughly $7M, or about $0.02-0.03 a quarter, and it shrinks at today's ~$55-58 price. SBC runs ~$74-78M a quarter (FY26 $299.6M, 14.8% of revenue vs 16.0% in FY25).
- **Q4 FY26 charges:** $28.1M of transaction, restructuring and other items, including an $18.5M long-lived-asset impairment; all of it fell in Q4 FY26, which is why that quarter's EPS was $0.06. It leaves the TTM in May 2027.
- **Other:** interest income is falling as cash goes to buybacks ($8.9M in Q1 FY27 vs $12.3M), and FX sits in other income ($0.4M vs $6.8M). Bindplane (Apr 2026, $99.7M) adds ~$3M a quarter of amortization and brought $7.7M of Q1 acquisition costs. Diluted shares are down 3.4% y/y (293.7M), which supports EPS.
- **Trigger arithmetic:** after the November print TTM = $0.31 + Q2 EPS; after the February print TTM = $0.18 + Q2 + Q3. My estimate is Q2 FY27 GAAP EPS of $0.14-0.19, putting TTM at about $0.45-0.50 in November. That is close to the trigger but likely above it; details are in the research notes §3d.

## 5. Valuation — three scenarios, 3-year horizon

Year 3 = the 12 months to September 2029, from TTM revenue of about $2.17B at September 2026. Valued on EV / adjusted FCF, because GAAP EPS is distorted by the post-transfer tax rate and SBC. Implied EV/Sales is shown as a cross-check against the own-history table below.

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $2.81B (9% a year: ARR growth slides to high single digits as Datadog and cheaper OpenTelemetry-based tools take share and AI agents compress seat-like spend) | $3.13B (13% a year: FY27 guide 14.5-15% cc fading to ~12%; consensus FY28 $2.66B, +14.7%) | $3.39B (16% a year: DPS consumption, logs and AI-workload monitoring hold net new ARR growth at the 16-23% guide) |
| Sustainable margin | adj. FCF 25% (non-GAAP op margin ~28%) | adj. FCF 27% (op margin ~31%) | adj. FCF 30% (op margin ~33%) |
| Net debt / cash (yr 3) | net cash $1.2B | net cash $1.2B | net cash $1.5B |
| Diluted shares (yr 3) | 278M (buybacks at ~$45, ~2%/yr SBC dilution) | 282M (buybacks at ~$65) | 283M (buybacks at ~$80) |
| Multiple applied | 15x EV/FCF (EV/Sales 3.8) | 22x EV/FCF (EV/Sales 5.9, the 5-year P/S low) | 28x EV/FCF (EV/Sales 8.4, today's level) |
| Implied price | $42 | $70 | $106 |
| Total return / annualised | -27% / -10% | +21% / +7% | +83% / +22% |
| Probability weight | 30% | 50% | 20% |

Key assumptions: FCF is returned mainly through buybacks, so net cash stays at about $1.2-1.5B. SBC of ~$300M a year (~14% of revenue) is not deducted from FCF, which matches the company's and consensus definition. On SBC-adjusted FCF the same prices imply multiples about twice as high. The bear weight of 30% reflects that the multiple has already recovered 45% from the April low, and that Datadog is growing twice as fast (Q2 2026 revenue +36%). Probability-weighted value **≈ $69 (+19%, ~6% a year)**. The rule's trim price ($87) sits between the base and bull values.

What does today's price already require the business to deliver?

- At $57.95 (EV ≈ $15.8B) the stock trades at ~26x FY27 guided adjusted FCF ($610-615M) and 25x FY28 consensus non-GAAP EPS. Consensus is third-party (Yahoo, read 2026-09-28): FY27 (Mar 2027) revenue $2.32B / non-GAAP EPS $1.98; FY28 $2.66B / $2.30. Q2 FY27 consensus is $568M / $0.49 against a $565-570M / $0.48-0.49 guide. The average target is about $59.7 (36 analysts, range $42-71), so the price is already at the street's target.
- Reverse DCF (my arithmetic: 10% discount rate, 10 years then 3% terminal): adjusted FCF must compound about **10-11% a year for ten years**, or about 20% a year if SBC is treated as a cash cost. At a 22x exit multiple and 27% FCF margin, today's EV needs about $2.65B of revenue in three years (~7% a year) just to hold the price. The market is therefore pricing a mid-teens grower that slows gradually — roughly the base case — and not a share-loss story. Upside needs growth to stay near 16% and the multiple to hold. The downside case needs growth to fall below ~10%.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 8.4 | 10.7 | 5.7 | 29.0 | 0.13 | 29.0 | 2020-06-30 |
| EV/EBITDA | 60.4 | 98.9 | 36.5 | 221.8 | 0.14 | 221.8 | 2020-12-31 |
| P/E (trailing) | 115.9 | 100.6 | 22.8 | 509.9 | 0.54 | 288.5 | 2020-12-31 |

At the 5-year median P/S (10.7) on today's TTM revenue the price would be about $74 (+27%); at the 5-year low (5.7), about $40 (-32%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.14, growth +18%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$0.43** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (net cash today)
- **Price target where recovery is fully reflected:** trim half at **$87** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** de-rated software (APPF, INTU, DT, NOW, VEEV): half the basket, one shared driver (AI-disruption / seat-pricing narrative and sector multiple); same-driver holdings: APPF, INTU, NOW, VEEV
- **Research overlay (not part of the rule):** **Trigger risk.** I estimate about a **15-20%** chance that the guide-cut proxy fires in the next 12 months, with no operating miss needed. Roughly 5% of that is at the November print (it needs Q2 FY27 GAAP EPS ≤ $0.12, i.e. an ETR of ~60%+ or a ~$15M charge). About 10% is at the February 2027 print (Q2 + Q3 ≤ $0.25), and a few percent later only with a large charge. The TTM will probably dip to about $0.45-0.50 in November as the $0.19 windfall quarter leaves. Higher-confidence signals: the stock staying above ~$50 (shortfalls shrink), a Q2 ETR below 50%, cc ARR growth ≥ 16%, NRR ≥ 110%, logs and AI-workload counts still compounding, and a clean CFO succession. Lower-confidence signals: a return to the high $30s (shortfalls return), any impairment/restructuring or larger acquisition, a cut to the cc ARR guide, and Datadog widening its growth gap. The Sep 1-2, 2026 platform incident is a minor reputational flag unless it shows up in NRR. **Dated catalysts:** Q2 FY27 print, early November 2026 (date not yet announced; Q2 FY26 was Nov 5, 2025) — first trigger test and first check of the tax rate; month-end Nov 30, 2026 is the first rule check on the new TTM. Q3 FY27, early February 2027 (Q3 FY26 was Feb 9) — the main trigger test. New CFO named by March 31, 2027 (Jim Benson leaves by then). Q4 FY27 and the FY28 guide, mid-May 2027 — the low $0.06 quarter leaves the TTM. The revolver (Dec 2, 2027) should be renewed during 2027.

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #6: val 0.14, growth +18%, entry TTM EPS $0.50, trigger $0.43, trim $87 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/DT.md) | Business intact (ARR +17%, NRR 110%, net cash, FCF ~26%); the EPS fall is IP-transfer tax accounting; probability-weighted value ~$69 (+19%); trigger risk ~15-20%, mostly at the Feb 2027 print; review_deadline 2027-03-27 kept (it already follows the second report after today, early Feb 2027) |

## 8. Research conclusion

Dynatrace passes the rule's intent on the business, but only partly on the price. Earnings, margins and FCF are higher than at the 2021 peak, net cash is about $1.15B, and ARR growth has held at 16-17% cc with net new ARR reaccelerating. The fall was multiple, and the GAAP EPS collapse is the $320.9M IP-transfer tax benefit leaving the trailing year, followed by a structurally higher tax rate. The stock has already rebounded 79% from its April low, however, and sits on the street's average target. The probability-weighted 3-year value is about $69 (+19%, ~6% a year), with a $42 bear against a $106 bull: a modest edge for a name that is only 26% below its high. The single most important thing to watch is the Q2 and Q3 FY27 GAAP tax rate against the $0.43 trigger; there is about a 15-20% chance the proxy sells a healthy business for accounting reasons. The operating tell is cc ARR growth and net new ARR against the 15.5-16.5% guide. In the basket, DT is one of five software names sharing the AI-disruption multiple driver with APPF, INTU, NOW and VEEV. Its consumption-based DPS model and AI-workload monitoring make it more of an AI beneficiary than the seat-priced names, but it still trades with the software index. Its drivers are unrelated to PODD, DXCM and BSX (medtech), KNSL and OLLI, and with NOW it is one of the two likeliest early mechanical exits.
