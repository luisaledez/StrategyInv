# OLLI — Ollie's Bargain Outlet

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #4 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-04-30 |
| Monthly RSI, last completed candle | 37.5 |
| Episode months / min RSI | 5 / 36.1 |
| Drawdown from trailing 5-year high | -40.2% (high 140.80 on 2025-08-06) |
| Market cap / avg daily $ volume (3m) | $5.00B / $137M |
| Sector / industry | Consumer Discretionary / Broadline Retail |
| Survival gate (proxy) | PASS — cash $188M, debt due <1y $100M, FCF TTM $223M, 24m gap -$88M |
| Net debt / EBITDA, interest coverage | 1.3 / n/a |
| Valuation | P/E trailing 18.8, P/E forward 17.0, PEG n/a, P/S 1.79, EV/Sales 2.0, EV/EBITDA 13.1, P/FCF 22.4 |
| EPS | TTM 4.48, forward est. 4.94; growth YoY (TTM) +20.4%, last quarter +43.4%, implied forward +10.3% |
| Revenue YoY (last quarter) | +9.1% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 4 of 10 / 17 of 20 |
| TTM revenue growth | +14% (latest quarter 2026-08-01) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.10** — P/S 0.15, EV/EBITDA 0.08, EV/EBIT 0.09 (P/E pct 0.04, not used) |
| Multiples today | P/S 1.8, EV/EBITDA 13.0, EV/EBIT 14.7, P/E 18.8 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 43.6 / 36.1 |
| From 5-year high | -40% |
| TTM EPS path, 6 quarters (oldest first) | 3.25, 3.45, 3.61, 3.89, 4.04, 4.47 |
| TTM EPS vs 12 months earlier | +30% |
| One-off EPS guard | passed — TTM net income / operating income 0.80 |
| Acquisition guard | passed — diluted shares -1.0% y/y |
| Net debt / EBITDA | net cash |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 118 shares per $100k at Friday's $84.25).
Entry TTM EPS **$4.47** → guide-cut trigger **$3.80** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$126** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val 0.10-0.25: n 222, mean +17%, median +16%, 66% winners, 52% beat SPY; 40-60% below: n 250, mean +24%, median +19%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Clean; low variance.

- Reward case: Steadiest fundamentals on the list: TTM EPS up every quarter (+30%), net cash, 14% growth, 18.8x earnings at the 10th percentile of its history, 40% below the high.
- Main risks under these rules: One of the slowest growers in the top 20 (growth rank 17); a consumer slowdown would show in comparable sales before EPS. Trigger $3.80.

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression, set off by a cyclical comp slowdown** (fuel-price squeeze on the low-income customer, bad seasonal weather, heavy industry clearance) — EPS rose every quarter and margins are higher than at the peak, so this is a growth-premium multiple (39-43x) meeting a demand air pocket, not structural deterioration (so far).  <!-- inventory cycle | financing-sensitive demand | temporary execution | excess industry capacity | valuation compression | structural deterioration -->

Narrative (what actually happened, with dates and numbers from the filings; closes from the price cache, full sources in the [research notes](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/OLLI.md)):

- 5-year high 140.80 on 2025-08-06; price now -40%. From that month's close (126.84) P/S went from 3.4 to 1.8 (-45%) while TTM revenue per share changed +21%: the fall is all multiple (price and valuation caches, derived).
- 12-month price return -37%; TTM EPS +30% over the same span; revenue +14%.
- **Aug 2025, 140.80 → 126.84 (-10%).** The peak came after four beat-and-raise prints and the Big Lots lease grab (63 former Big Lots leases acquired by Feb 2025). Q2 FY25 on 2025-08-28 was another beat-and-raise (comps +5.0%, FY25 comp guide 3.0-3.5%, adj. EPS $3.76-3.84), but the guide implied H2 comps of roughly 2-3% after 3.9% in H1 (derived); -3.5% the next day. No dated news cause found for the rest of the drift.
- **Dec 2025, 123.11 → 109.61 (-11% in the month).** Q3 FY25 on 2025-12-09: comps +3.3%, EPS +29%, guide raised again (adj. EPS $3.81-3.87), gross margin -10 bp on tariff costs; stock -4.0% on the day. No source found for the reaction; the guide implied Q4 comps of about 2-3% (derived).
- **Mar 2026, 109.25 (Mar 13) → 89.24 (Mar 27), -18%.** The US-Iran conflict began Feb 28; OLLI fell 5.3% on Mar 2, the first session after, as oil jumped. Q4 FY25 on 2026-03-12 was fine (comps +3.6%, FY25 EPS $3.89, FY26 guide 75 stores, comps ~2%, adj. EPS $4.40-4.50) and Wells Fargo upgraded to Overweight, but the stock then lost 18% in two weeks as Brent peaked near $118 and US gasoline passed $4. Only the low-income names followed: Mar 13-27 DG -11%, SPY -4%, while TJX, ROST, BURL and FIVE were flat to up.
- **May 11, 2026: -7.9%** in a sector move (DG -7.6%, FIVE -6.9%) on gasoline at its highest since 2022 and a record-low Michigan sentiment reading (47.6 in April).
- **June 3-4, 2026, Q1 FY26:** comps +1.7% (transactions nearly flat, per Gordon Haskett ~0.2% vs 4-6% before), EPS $0.92 (+19%); FY26 sales guide trimmed to $2.980-3.000B, EPS guide raised to $4.45-4.55; management said Q2 comps would look like Q1. Flat on the day, then -6.6% on June 4 with a Gordon Haskett downgrade (to Accumulate, $90), UBS cut to $87 (Neutral), Goldman $151 → $129, and Five Below's ~13% post-earnings drop the same day.
- **July 6-8, 2026: -6.8% and -9.0% to the low of 61.88 (-56% from the high).** July 8: JPMorgan downgraded to Neutral ($70), expecting negative-to-low-single-digit Q2 comps and a lower gross margin. No source found for July 6.
- **Sept 2, 2026, Q2 FY26 ([8-K](https://www.sec.gov/Archives/edgar/data/0001639300/000114036126035406/ef20081496_ex99-1.htm), [10-Q](https://www.sec.gov/Archives/edgar/data/0001639300/000110465926104755/olli-20260801x10q.htm)):** comps **-1.8%** (basket down, transactions flat; about 3.5 points below management's own June outlook), sales +9.1% on 11.9% more stores, average sales per store -4%. EPS $1.42 (+43%) against ~$1.12 consensus, but **$28.3M of IEEPA tariff refunds in cost of sales (380 bp of gross margin, ~$0.35 a share per management)** did the beating; ex-refund EPS ≈ $1.07, slightly below consensus. FY26 sales guide cut to $2.928-2.941B and comps to 0-0.5%; EPS guide raised to $4.57-4.65 (refund included); buyback raised to ~$175M. Close-to-close +2.1% (third-party reports of a 6% intraday fall conflict; the cache is used). September rally to 84.25 (+36% from the July low).
- Relative: from 2025-08-06 to 2026-09-25 OLLI -40% vs DG +10%, DLTR -2%, TJX -2%, BURL -10%, ROST +61%, FIVE +64%, SPY +20% (price caches). The de-rating is OLLI-specific: drive-to destination for a rural, lower-income shopper (management: longer drive times made the fuel headwind worse; Midwest and Texas weakest) and a seasonal/home mix hit by weather.

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **Multiple, not an earnings peak.** At the high, TTM EPS was $3.25 (P/E ~43x on the close, 39x at the month-end in the valuation cache; EV/EBITDA 25.9). TTM EPS is now $4.47 (+38%), $4.12 ex-refund (+27%). TTM operating margin was 10.7% then and is 12.3% now (11.2% ex-refund). What has faded is the comp: +5.0% in the quarter reported just after the peak versus -1.8% now. The high priced in a 10%-unit-growth story plus 3-5% comps; the market now doubts the comp half.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $188M cash + short-term investments, plus $320M long-term investments = **$507M**; borrowings $2.2M (finance leases only). The screen's "total debt $726M / net debt $538M" is the operating-lease liability ($723M) and leaves out the long-term investments | 10-Q balance sheet 2026-08-01; fundamentals cache |
| Realistically available credit (undrawn revolver, covenants) | $100M ABL revolver (borrowing base 90% of appraised inventory), **undrawn**; $88.4M available after $11.3M letters of credit; matures 2029-01-09; one springing covenant (fixed-charge coverage ≥ 1.0x only in a low-availability period), in compliance; accordion up to $150M | 10-Q note 7 |
| Debt maturities next 24 months | none: no borrowings; finance leases $0.8M current. Revolver maturity (Jan 2029) is outside the window | 10-Q note 7 |
| Cash consumption if weak conditions persist 24 months | none: FCF TTM $223M after $118M capex (proxy 24m gap -$88M). H1 FY26 operating cash flow $154M vs $109M a year ago | fundamentals cache; 10-Q cash flow |
| Interest, maintenance capex, leases, other fixed obligations | interest paid $0.2M in H1 (net interest income $11M). Operating lease payments ≈ **$274M over the next 24 months** ($53M rest of FY26, $151M FY27, half of $137M FY28), plus $36M signed not commenced; operating lease cost $73M per half. Capex guide $103-113M, mostly new stores (maintenance split not disclosed). Buyback ~$175M in FY26 is discretionary. Lease-adjusted net debt ≈ $216M, ~0.6x TTM EBITDA | 10-Q note 4, MD&A |
| Can recovery happen without a large equity raise? | yes | net cash of ~$505M before leases, positive FCF, undrawn revolver |

Gate verdict: **PASS** — reasoning:

- Profitable in 4 of 4 reported years (net margin 5.6% even in the FY22 freight-and-inflation year), no borrowings, $507M of cash and investments against ~$274M of lease payments over two years, and FCF covers leases, capex and more. The only fixed-charge risk is rent, and new-store commitments can be slowed. Survival is not the question.

## 4. Recovery thesis  (testable statement)

> The business weakened because of **a comp slowdown (from +5.0% to -1.8%) as fuel prices, bad seasonal weather and aggressive industry clearance hit a lower-income, drive-to customer, while the growth-premium multiple (39-43x) had no room for it**. Recovery requires **comps back to at least flat-to-+2% with positive transactions, and gross margin holding near the 40.5% target without tariff refunds while ~75 stores a year keep coming**.
> We expect to observe **Q3 FY26 comps at or above flat (guide implies ~0%) and Q4 at or above +1%, with transactions positive and ex-refund gross margin ≥ 40%, and a FY27 guide in March 2027 of ~75 stores and ~2% comps** within the next 2–4 quarters.

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| Comparable-store sales and transactions vs management's implied guide (Q3 ~0%, Q4 ~+1%) | leading | Q2 -1.8% (basket down, transactions flat; transactions positive and basket flat by quarter-end per the call); guide 0-0.5% for FY26 | Q3 ≥ 0% and Q4 ≥ +1% with positive transactions; FY27 comp guide ~2% | Q3 negative again or FY guide cut a second time; transactions turning down |
| TTM EPS vs entry $4.47 / trigger $3.80 | financial confirmation | $4.47 (+30% y/y); ~$4.12 ex-refund | flat or rising at each month-end (guide implies ~$4.57-4.65 by the March 2027 print) | prints at or below $3.80 at a month-end before 2027-09-28 (rule exit) — needs H2 FY26 EPS about 30% below last year's $2.14, or Q3 FY26 to Q1 FY27 about 22% below |
| Gross margin ex-refunds vs 40.5% long-term target | third (margin quality) | Q2 43.5% reported, ~40.3-40.4% ex-refund and price investment (management); FY26 guide ~41.3% incl. refund | H2 at or above last year (41.3% Q3, 39.9% Q4) while funding the ~$15M price investment | price investment beyond plan plus fuel costs push ex-refund margin below ~39.5% (FY22-type squeeze) |

Organic-screen check: TTM revenue +14%, latest quarter +9.1% over its year-ago quarter; with ~11% more stores the quarter-versus-year-ago test fails only if comps fall about 10%.

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **IEEPA tariff refunds, Q2 FY26: $29.4M received, $28.3M in cost of sales and $1.1M in interest income** (10-Q note 5). About $0.35 of the $1.42 Q2 EPS and of the $4.47 TTM; company "adjusted" EPS does **not** remove it. Management calls it finite and plans to reinvest part in price. It leaves the TTM with the Q2 FY27 report (early Sept 2027), just after the rule's window if the timing holds.
- Big Lots dark rent (~$5M in FY25, in pre-opening) does not recur: pre-opening fell 42% in Q2 FY26. A real but one-time tailwind to FY26 growth.
- Stock comp ~$14M a year (~$0.18/share after tax) is in GAAP and adjusted EPS; adjusted EPS only strips excess tax benefits from stock options ($0.5M in H1 FY26). Effective tax ~25%.
- Buybacks: diluted shares 60.2M in Q2 vs 61.8M a year ago (-2.5%); FY26 guide ~60.0M on ~$175M of repurchases. Part of EPS growth is buyback.
- Calendar: FY23 (ended Feb 3, 2024) had 53 weeks; **FY28 (ending Feb 3, 2029) will too** (derived from the "Saturday nearer January 31" convention).
- Working capital: inventory +10.5% y/y vs stores +11.9%, so no release or build flattering cash flow.

## 5. Valuation — three scenarios, 3-year horizon

Year 3 = fiscal 2028 (ending Feb 3, 2029, 53 weeks), the last full year reported before September 2029. P/E is applied to EPS that already includes interest income on the cash pile, so net cash is not added again. Starting points: FY26 guide $2.93B revenue; underlying FY26 EPS ≈ $4.26 ($4.61 guide midpoint less ~$0.35 refund); ~59.5M shares outstanding; net margin 8.6-9.1% in FY23-FY25, 5.6% in FY22.

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $3.30B (~6%/yr: comps -1% to 0, ~50 openings a year) | $3.60B (~10%/yr: ~75 stores, ~2% comps, plus 53rd week) | $3.75B (~13%/yr: 75-80 stores, ~3% comps, plus 53rd week) |
| Sustainable margin | net 7.5% (gross margin ~39.5%, SG&A deleverage) | net 8.8% (gross ~40.5%, modest leverage) | net 9.8% (gross ~41%, SG&A leverage on +3% comps) |
| Net debt / cash (yr 3) | net cash ~$0.6B (before $0.7-0.8B of lease liabilities) | net cash ~$0.7B | net cash ~$0.75B |
| Diluted shares (yr 3) | 56.0M | 55.5M | 55.5M |
| Multiple applied | 14x P/E (below the 5y low of 16.1) | 20x (5y median 30.8; today 18.8 reported, ~20 ex-refund) | 25x |
| Implied price | $62 (EPS $4.42) | $114 (EPS $5.71) | $166 (EPS $6.62) |
| Total return / annualised | -27% / -9.8% | +36% / +10.7% | +96% / +25.3% |
| Probability weight | 25% | 50% | 25% |

Probability-weighted value **≈ $114 (+35%, ~10.6% a year)** from $84.25. Key assumptions: unit growth near the ~10% management talks about; new stores keep dilution of average sales per store to low single digits (it was -4% in Q2); no further tariff refunds in the numbers; buybacks of ~$100-175M a year. The bear case is a two-year low-income recession with a margin squeeze like FY22's, but it does not go that far (FY22 net margin was 5.6%).

What does today's price already require the business to deliver?

- **Consensus (third-party):** FY26 (Jan 2027) revenue ~$2.93B, EPS ~$4.61, i.e., the company guide ([stockanalysis.com](https://stockanalysis.com/stocks/olli/forecast/), 15 analysts, average target $99.93); FY27 (Jan 2028) EPS ~$4.94 (Yahoo forward EPS in the fundamentals cache; the year it refers to is inferred, not confirmed; no FY27 revenue consensus found).
- $84.25 is 19.8x underlying FY26 EPS ($4.26) and 17.1x the FY27 estimate. At a multiple of 20x, the price needs only ~$4.2 of EPS in yr 3, **no growth from the ex-refund base**; at 16x (the 5-year low) it needs ~$5.27, about 11% a year for two years, which is below the company's own "mid-teens" algorithm. Put another way, the price assumes the store growth adds little value (or that comps stay negative long enough to offset it), not that the business shrinks.
- On P/S the mechanical anchors below give $72-107; the scenario table is lower in the bear case because it cuts margin and multiple together.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 1.8 | 2.3 | 1.6 | 3.6 | 0.15 | 3.4 | 2015-07-31 |
| EV/EBITDA | 13.0 | 20.3 | 10.2 | 28.0 | 0.08 | 25.9 | 2015-10-31 |
| P/E (trailing) | 18.8 | 30.8 | 16.1 | 42.0 | 0.04 | 39.0 | 2015-07-31 |

At the 5-year median P/S (2.3) on today's TTM revenue the price would be about $107 (+27%); at the 5-year low (1.6), about $72 (-14%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.10, growth +14%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$3.80** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (net cash today)
- **Price target where recovery is fully reflected:** trim half at **$126** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** none in the basket (OLLI is the only consumer name); exposed to US low-income consumer spending
- **Research overlay (not part of the rule):** More confident if Q3 comps land at or above flat with positive transactions, ex-refund gross margin stays near 40.5% while the price investment is funded, and the March 2027 guide keeps ~75 openings and ~2% comps. Less confident if comps go negative a second quarter, price investment grows well past the ~$15M plan, gasoline rises again into winter, or average sales per store keeps falling faster than ~4% (new stores, many of them ex-Big Lots boxes, diluting productivity). The guide-cut proxy is unlikely to fire (it needs a ~30% H2 EPS drop), so the risk under the rules is a slow, flat position rather than a forced exit. Dated catalysts: Q3 FY26 report around early-to-mid December 2026 (last year Dec 9; December 8 is a third-party estimate, not confirmed); holiday season Nov 2026-Jan 30, 2027 (Q4 is ~29% of sales); Q4 FY26 results and FY27 guidance around mid-March 2027 (last year Mar 12); Q1 FY27 early June 2027. No investor day found. Litigation: nothing material per the 10-Q. Macro: gasoline prices (Iran conflict), any further IEEPA refunds (not guided).

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #4: val 0.10, growth +14%, entry TTM EPS $4.47, trigger $3.80, trim $126 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/OLLI.md) | Fall explained: 39-43x multiple meeting a comp slowdown (+5.0% to -1.8%) from fuel prices, weather and clearance; ~$0.35 of the $4.47 TTM EPS is a one-off tariff refund (ex-refund ~$4.12, still 8% above the trigger). Survival PASS confirmed (no borrowings, $507M cash and investments; the screen's "debt" is operating leases — section 1 left unchanged). Weighted value ~$114. Review deadline kept at 2027-03-27: the second report after today (Q4 FY26) is expected around mid-March 2027 |

## 8. Research conclusion

OLLI fits the rule's pattern cleanly: the 40% fall is a de-rating from 39-43x earnings, not an earnings collapse, and the balance sheet ($507M of cash and investments, no borrowings) removes survival risk. The earnings base is less clean than the screen shows: about $0.35 of the $4.47 TTM EPS is a tariff refund, so the price is ~20x underlying earnings, not 18.8x, still at the bottom of its own range. Probability-weighted value is about $114 (+35%, ~11% a year) with a -27% bear case, fairly symmetric for a name that needs only its store growth to be worth something. The single thing to watch is the Q3 comp in December: at or above flat with positive transactions supports the "weird year" reading, while a second negative quarter would point to new-store productivity or customer loss rather than weather. In the v3 basket OLLI is the only consumer and retail exposure and has little in common with the five de-rated software names (APPF, INTU, DT, NOW, VEEV), the three medtech names (PODD, DXCM, BSX) or KNSL, so it diversifies the basket; its own driver is gasoline prices and the US lower-income consumer.
