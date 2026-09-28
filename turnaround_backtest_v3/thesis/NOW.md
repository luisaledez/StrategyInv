# NOW — ServiceNow

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #7 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-06-30 |
| Monthly RSI, last completed candle | 51.2 |
| Episode months / min RSI | 2 / 37.8 |
| Drawdown from trailing 5-year high | -42.1% (high 234.08 on 2025-01-28) |
| Market cap / avg daily $ volume (3m) | $140.21B / $2.27B |
| Sector / industry | Information Technology / Systems Software |
| Survival gate (proxy) | PASS — cash $4.66B, debt due <1y $2.20B, FCF TTM $4.57B, 24m gap -$2.47B |
| Net debt / EBITDA, interest coverage | 1.1 / 29.3 |
| Valuation | P/E trailing 84.8, P/E forward 27.1, PEG 0.98, P/S 9.52, EV/Sales 9.8, EV/EBITDA 41.1, P/FCF 30.7 |
| EPS | TTM 1.60, forward est. 5.01; growth YoY (TTM) +22.1%, last quarter -21.2%, implied forward +212.8% |
| Revenue YoY (last quarter) | +24.0% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 7 of 10 / 5 of 20 |
| TTM revenue growth | +22% (latest quarter 2026-06-30) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.15** — P/S 0.16, EV/EBITDA 0.16, EV/EBIT 0.12 (P/E pct 0.16, not used) |
| Multiples today | P/S 9.6, EV/EBITDA 63.9, EV/EBIT 86.0, P/E 84.8 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 48.3 / 29.8 |
| From 5-year high | -42% |
| TTM EPS path, 6 quarters (oldest first) | 1.47, 1.59, 1.65, 1.67, 1.68, 1.60 |
| TTM EPS vs 12 months earlier | +1% |
| One-off EPS guard | passed — TTM net income / operating income 0.99 |
| Acquisition guard | passed — diluted shares -0.1% y/y |
| Net debt / EBITDA | 1.3 |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 73 shares per $100k at Friday's $135.62).
Entry TTM EPS **$1.60** → guide-cut trigger **$1.36** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$203** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val 0.10-0.25: n 222, mean +17%, median +16%, 66% winners, 52% beat SPY; 40-60% below: n 250, mean +24%, median +19%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Fair; watch the EPS base.

- Reward case: 22% growth at the 12-16th percentile; 42% below the high. New to the v3 portfolio (the v2 portfolio holds it from April 2026).
- Main risks under these rules: TTM EPS slipped 1.68 to 1.60 last quarter; the trigger ($1.36) is one and a half more such quarters away. P/S 9.6 and EV/EBITDA 64 are cheap only against its own past; seat-based software under AI pressure.

## 2. Why did the stock fall?  (diagnosis)

Cause category: valuation compression — subscription revenue grew 19-24.5% in every quarter of the fall and non-GAAP margins and FCF rose; the price fell because the multiple halved in the sector-wide AI-agent de-rating, sharpened by a below-consensus 2025 guide, the $7.75B Armis purchase and a Middle East deal slip. GAAP EPS stalled on acquisition accounting, not demand.  <!-- inventory cycle | financing-sensitive demand | temporary execution | excess industry capacity | valuation compression | structural deterioration -->

Narrative (what actually happened, with dates and numbers from the filings; all prices split-adjusted for the 5-for-1 split effective 2025-12-17, so the high is about $1,170 pre-split):

- 5-year high 234.08 on 2025-01-28; price now -42%. From that month's close (203.68) P/S went from 19.3 to 9.6 (-50%) while TTM revenue per share changed +34%: the fall is all multiple (price and valuation caches, derived).
- 12-month price return -26%; TTM EPS +1% over the same span; revenue +22%.
- **Leg 1, 2025-01-30, -11.4% (202.55, -13.5% from the high).** Q4 2024 report on Jan 29: FY2025 subscription guide $12,635-12,675M (18.5-19%), below a consensus of about $12.83B (third-party), with a ~$175M FX headwind and federal business weighted to H2 after the change of administration ([8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000007/erq4fy24.htm)).
- **Leg 2, Feb-Apr 2025, to 144.33 on 2025-04-04 (-38%), then fully recovered.** Market-wide tariff sell-off, no company event; the Q1 2025 beat (subscription $3,005M, cRPO +22%) gave +15.5% on Apr 24 and the stock was back to 208.94 on Jul 3. Not part of the lasting damage.
- **Leg 3, Jul-Dec 2025, 208.94 → 153.04 (-27%).** Beats every quarter but federal budget headwinds flagged in Q2 and Q3 2025 and the Oct-Nov shutdown; November -11.6% with no company event found; **Dec 15 -11.5%** on the Bloomberg report of talks to buy Armis (announced Dec 23 at $7.75B cash), days after Moveworks closed (Dec 15, $2.4B).
- **Leg 4, Jan-Feb 2026, 153.19 (Dec 31) → 102.63 on Feb 5 (-33%).** Q4 2025 (Jan 28) beat and guided FY2026 subscription +20.5-21% with a $5B buyback and $2B ASR, yet fell 9.9% on Jan 29 into the AI-agent software sell-off; Anthropic's Claude Cowork plugins (Jan 30) set off the Feb 3-5 software rout (-7.0%, -7.6%) ([8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000005/erq4fy25.htm), [Axios](https://www.axios.com/2026/02/03/ai-software-anthropic-stock-market)).
- **Leg 5, April 2026, to the low of 83.00 on Apr 10 (-64.5%).** Apr 9 -7.9%: ServiceNow replaced its five packages with three AI-native tiers (AI no longer an add-on) in the same week as Anthropic's "Mythos" news; Apr 10 -7.6%: UBS downgrade to Neutral, target $170 → $100, citing AI agents and app-budget pressure ([CNBC](https://www.cnbc.com/2026/04/10/ubs-downgrades-servicenow-saying-ai-is-a-bigger-threat-than-first-believed.html)). Q1 2026 on Apr 22: ~75 bp subscription headwind from delayed Middle East on-prem deals and a Q2 guide of 3.5% GAAP / 26.5% non-GAAP operating margin with Armis → -17.7% on Apr 23 ([8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000054/erq1fy26.htm)).
- **Since the low, +63% to 135.62.** Enterprise-AI rotation (May 29 +14.4%, Jun 1 +9.2%), the Q2 2026 beat-and-raise on Jul 22 (subscription +24.5%, cRPO +21%, AI ACV above $1B; [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000072/erq2fy26.htm)), Salesforce read-across on Aug 27 (+10%) and target raises on Sep 14 (+7.4%).

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **No earnings peak, the multiple.** At the high the stock was 84x FY2024 non-GAAP EPS ($2.78) and 19.3x sales on a 29.5% non-GAAP operating margin. Today TTM revenue is 34% higher, the FY2026 non-GAAP margin guide is 31.5% and FY2026 consensus non-GAAP EPS is $4.07 (33x). GAAP TTM operating margin is lower (12.4% → 11.4%) only because of acquisition amortization, deal costs and stock comp.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $4.66B (total debt $8.45B, net debt $3.79B), plus $2.04B long-term marketable securities and $2.07B strategic investments not counted; debt ex leases less all marketable securities ≈ $0.8B net debt | fundamentals cache, balance sheet 2026-06-30; [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm) |
| Realistically available credit (undrawn revolver, covenants) | $3.0B unsecured revolver, undrawn, matures 2031-04-01 (+$2.0B accordion); "customary affirmative and negative covenants", no financial-ratio covenant in the 10-Q text; $3.0B commercial-paper programme with $2.1B out | Q2 2026 10-Q debt note |
| Debt maturities next 24 months | commercial paper $2.1B (up to 397 days, rolled) + $750M 4.25% notes due May 2028 = ~$2.85B; next is $1.5B in Sept 2030. The $4.0B Armis term loan (Apr 2026) was repaid from $4.0B of notes issued May 2026 | Q2 2026 10-Q |
| Cash consumption if weak conditions persist 24 months | none: FCF TTM $4.57B is positive (proxy 24m gap -$2.47B); FY2026 FCF margin guide 35% (~$5.7B) | fundamentals cache; Q2 2026 8-K |
| Interest, maintenance capex, leases, other fixed obligations | interest expense $66M in Q2 2026, ~$82M a quarter at the June debt stack (derived); operating leases $936M ($114M current); capex $0.74B TTM; interest coverage 29x. Buybacks ($2.2B in H1 2026) are discretionary | Q2 2026 10-Q; fundamentals cache |
| Can recovery happen without a large equity raise? | yes | positive FCF, ~$6.7B cash and securities, undrawn revolver |

Gate verdict: PASS — reasoning:

- Liquidity of about $6.7B in cash and securities plus a $3.0B undrawn revolver against ~$2.85B due within 24 months, and FCF of $4.6-5.7B a year. Gross debt went from $1.5B to $7.5B to pay for Armis, but net of securities it is under $1B. Survival is not the question for this name.

## 4. Recovery thesis  (testable statement)

> The business weakened because of **nothing in the revenue line: the stock de-rated on the fear that AI agents shrink seat-based workflow software, and GAAP earnings stalled under ~$11B of acquisitions (Moveworks, Veza, Armis) that brought amortization, deal costs, higher stock comp and interest expense**. Recovery requires **organic subscription growth to hold around 20% in constant currency through the switch to AI-native tiers, with no seat shrinkage showing in cRPO, and Armis absorbed with the non-GAAP operating margin back at 31-32% and GAAP margins rising as deal costs roll off**.
> We expect to observe **cRPO growth of at least 19.5-20% in constant currency in the Q3 and Q4 2026 reports, ServiceNow AI ACV of $1.5B or more at end-2026, and a FY2027 guide of about 18% subscription growth or better at a non-GAAP operating margin of 32% or more** within the next 2–4 quarters.

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| cRPO growth, constant currency (includes ~1-1.5 pts from Armis) | leading | Q2 2026 $13.20B, +21% (+21.5% cc); Q3 guide +19.5% (+20% cc) | ≥ 20% cc in Q3 2026 and ≥ 19% cc in Q4 2026 | below 18% cc (organic ~16-17%) or a FY2027 subscription guide below 17% |
| ServiceNow AI ACV and new-tier pricing | leading (company-specific) | > $1B ACV in Q2 2026; target $1.5B end-2026; AI-native SKUs priced 20-30% above legacy; half of new business not seat-based (management) | ≥ $1.5B at Q4 2026 and uplift holding at renewals of the legacy SKUs (end of sale 2026-07-01) | target missed, or renewals showing seat cuts or discounted migrations |
| TTM EPS vs entry $1.60 / trigger $1.36 | financial confirmation | $1.60 (+1% y/y); Q3 2025's $0.48 leaves the TTM next quarter, so Q3 2026 GAAP EPS must exceed $0.24 | flat or rising at each month-end | prints at or below $1.36 at a month-end before 2027-09-28 (rule exit) |
| TTM revenue growth (entry +22%) | screen (organic test) | +22%; latest quarter +24% | holds double digits; latest quarter ≥ year-ago quarter | latest quarter below its year-ago quarter (fails the organic screen) |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **Why TTM EPS slipped 1.68 → 1.60:** Q2 2026 GAAP EPS $0.29 vs $0.37. Amortization of intangibles $219M vs $25M, stock comp $655M vs $499M, deal and severance costs $137M vs $43M, interest income down $46M and $66M of new interest expense, partly offset by a larger unrealised investment gain. Non-GAAP EPS rose ($0.90 vs $0.81).
- **The $1.60 base is flattered:** Q2 2026 includes $273M of unrealised gains on strategic investments and a $51M tax valuation-allowance release; Q1 2026 had $87M of gains. Without them TTM GAAP EPS is about $1.28 (derived), already below the trigger. The v3 one-off guard passed (0.99) only because a 30%+ GAAP tax rate offset the gains.
- **Acquired growth:** Armis adds ~125 bp to 2026 subscription growth, Moveworks about 1 point (sources conflict, see notes); organic growth is roughly 20-21%. Amortization still to come: $391M in H2 2026, $776M in 2027, $726M in 2028.
- **Timing:** about half of Q2 2026's subscription beat was U.S. federal on-prem revenue pulled from Q3 into Q2; the Q3 guide (+20.5%) already reflects it. One federal channel partner is 13% of revenue (10-Q).

## 5. Valuation — three scenarios, 3-year horizon

Year 3 = FY2029, valued in about September 2029. Revenue paths start from the FY2026 consensus of $16.22B; EPS = revenue × non-GAAP operating margin × 0.79 (21% tax, ~zero net interest) / shares.

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $22.6B (+15%, +11%, +9%) | $25.5B (+18.8% = FY2027 consensus, then +16%, +14%) | $27.3B (+20%, +19%, +18%) |
| Sustainable margin | 31% non-GAAP operating (AI compute costs, seat pressure) | 34.5% | 36% |
| Net debt / cash (yr 3) | ~$5B net cash | ~$8B net cash | ~$10B net cash |
| Diluted shares (yr 3) | 1.02B | 1.00B | 0.99B |
| Multiple applied | 16x non-GAAP EPS of $5.42 (P/S 3.9) | 25x EPS of $6.95 (P/S 6.8) | 32x EPS of $7.85 (P/S 9.1) |
| Implied price | $87 | $174 | $251 |
| Total return / annualised | -36% / -14% | +28% / +8.6% | +85% / +23% |
| Probability weight | 25% | 50% | 25% |

Probability-weighted value **$171 (+26%, about 8% a year)** from Friday's $135.62. Key assumptions: non-GAAP earnings exclude stock comp of ~16% of revenue, so the GAAP multiples are about 1.6x the ones shown; net cash is not added to the price and is a cushion of $5-10 a share; buybacks offset dilution plus about 1% a year; no further large acquisition. The base case lands below the $203 trim price in three years; reaching the trim needs the bull path or a faster re-rating. Bear is the AI-agent seat-compression case, with growth near 10% by 2029 and a multiple like today's INTU (16.8x).

What does today's price already require the business to deliver?

- Consensus (third-party, [Yahoo Finance](https://finance.yahoo.com/quote/NOW/analysis/) on 2026-09-28, non-GAAP EPS): FY2026 revenue $16.22B (+22%), EPS $4.07; FY2027 revenue $19.26B (+18.8%), EPS $5.01 (+23%). Today is 33x FY2026 and 27x FY2027 non-GAAP EPS, 9.8x EV/sales and 31.5x EV/FCF.
- Reverse-implied: an 8% annual return to 2029 at a 25x exit multiple needs FY2029 non-GAAP EPS of $6.83, about 19% a year from $4.07. That is roughly the consensus path, so the price assumes consensus holds and no more than that. At a 20x exit even a 0% return needs $6.78. A 10-year reverse DCF (9% discount, 3% terminal) needs ~8% a year FCF growth on reported FCF, or ~16% if stock comp is counted as a cash cost. Undemanding on reported FCF, about fair on SBC-adjusted FCF.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 9.6 | 15.3 | 6.6 | 27.1 | 0.16 | 19.3 | 2012-06-30 |
| EV/EBITDA | 63.9 | 108.8 | 32.1 | 219.3 | 0.16 | 106.9 | 2012-06-30 |
| P/E (trailing) | 84.8 | 137.0 | 52.6 | 820.9 | 0.16 | 148.7 | 2019-09-30 |

At the 5-year median P/S (15.3) on today's TTM revenue the price would be about $215 (+59%); at the 5-year low (6.6), about $93 (-31%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.15, growth +22%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$1.36** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (1.3 today)
- **Price target where recovery is fully reflected:** trim half at **$203** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** de-rated software (APPF, INTU, DT, NOW, VEEV): half the basket, one shared driver (AI-disruption / seat-pricing narrative and sector multiple); same-driver holdings: APPF, INTU, DT, VEEV
- **Research overlay (not part of the rule):** *More confident* if Q3 2026 cRPO grows 20%+ in constant currency, AI ACV is on track for $1.5B, the FY2027 guide (late January) is about 18%+ subscription growth at a non-GAAP margin of 32%+, and no further large deal is announced. *Less confident* if cRPO drops below 18% cc, renewals of the retired SKUs show seat cuts, gross margin keeps sliding (FY2026 non-GAAP subscription gross margin guide 81% vs 83.5% for FY2025), or federal or Middle East deals slip again. **Trigger risk: about 55% (range 40-70%) that the proxy sells at the Oct 30 (or Nov 30) 2026 month-end.** Q3 2025's $0.48 leaves the TTM, and Q3 2026 GAAP EPS must beat $0.24. The company guides an 8% GAAP operating margin, which works out to roughly $0.21-0.23 without investment gains. Each point of GAAP margin beat is worth about $0.027, and a $100M investment gain about $0.07. Such an exit would come from accounting, not a broken thesis; if Q3 passes, the ~14% GAAP margin implied for Q4 2026 should lift the TTM. Catalysts: Q3 2026 results on about Oct 28, 2026 (third-party date, not confirmed by the company); the Oct 30 month-end proxy check; federal funding deadline Dec 11, 2026 (secondary sources); Q4 2026 results with the FY2027 guide in late January 2027 (date not announced); Q1 2027 in late April 2027; Knowledge 2027 in about May (date not verified).

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #7: val 0.15, growth +22%, entry TTM EPS $1.60, trigger $1.36, trim $203 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/NOW.md) | Diagnosis is valuation compression, survival PASS, weighted value ~$171 (+26% over 3 years). High mechanical exit risk: the $1.60 base holds ~$0.32 of investment gains and a tax release, and Q3 2026 GAAP EPS must beat $0.24 against an 8% GAAP-margin guide. Sections 1/1b unchanged; review_deadline unchanged (the second report after today, Q4 2026, is expected in late January with no date set) |

## 8. Research conclusion

The operating turnaround case is fair: 20%+ subscription growth, non-GAAP margins and FCF held through a 64% peak-to-trough fall that was all multiple. The recovery rests on showing that AI agents add revenue per customer rather than cut seats, and the Q2 2026 cRPO and AI ACV readings lean that way. The probability-weighted 3-year value is about $171 (+26%, ~8% a year) against $135.62, a modest edge that assumes consensus holds and that sits below the $203 trim. The single thing to watch is the Q3 2026 GAAP EPS print against $0.24, expected around Oct 28. There is roughly an even-to-better chance that the guide-cut proxy sells the position at the Oct 30 month-end, driven by Armis amortization, interest expense and a gain-inflated base rather than by the business. Within the v3 basket NOW adds a fifth dose of the de-rated software factor (APPF, INTU, DT, VEEV) and, like DT, is a likely early mechanical exit on GAAP accounting items. Its federal and security exposure is unique in the basket; the medtech names (PODD, DXCM, BSX), KNSL and OLLI carry unrelated drivers.
