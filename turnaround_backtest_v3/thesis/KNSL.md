# KNSL — Kinsale Capital Group

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #2 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-03-31 |
| Monthly RSI, last completed candle | 48.4 |
| Episode months / min RSI | 4 / 38.0 |
| Drawdown from trailing 5-year high | -39.7% (high 547.98 on 2024-03-06) |
| Market cap / avg daily $ volume (3m) | $7.53B / $89M |
| Sector / industry | Financials / Property & Casualty Insurance |
| Survival gate (proxy) | PASS — cash $2.89B, debt due <1y $51M, FCF TTM $1.00B, 24m gap -$2.84B |
| Net debt / EBITDA, interest coverage | n/a / 60.2 |
| Valuation | P/E trailing 13.4, P/E forward 15.3, PEG 0.98, P/S 3.77, EV/Sales 2.4, EV/EBITDA n/a, P/FCF 7.5 |
| EPS | TTM 24.68, forward est. 21.65; growth YoY (TTM) +21.8%, last quarter +34.0%, implied forward -12.3% |
| Revenue YoY (last quarter) | +16.8% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 2 of 10 / 14 of 20 |
| TTM revenue growth | +16% (latest quarter 2026-06-30) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.01** — P/S 0.01, EV/EBITDA n/a, EV/EBIT n/a (P/E pct 0.00, not used) |
| Multiples today | P/S 3.8, EV/EBITDA n/a, EV/EBIT n/a, P/E 13.4 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 43.1 / 38.0 |
| From 5-year high | -40% |
| TTM EPS path, 6 quarters (oldest first) | 17.37, 19.16, 20.35, 21.65, 22.70, 24.64 |
| TTM EPS vs 12 months earlier | +29% |
| One-off EPS guard | passed — TTM net income / operating income n/a (no operating-income tag) |
| Acquisition guard | passed — diluted shares -1.0% y/y |
| Net debt / EBITDA | n/a |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 30 shares per $100k at Friday's $330.49).
Entry TTM EPS **$24.64** → guide-cut trigger **$20.94** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$496** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val ≤ 0.10: n 218, mean +38%, median +23%, 80% winners, 58% beat SPY; less than 40% below: n 306, mean +14%, median +13%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Solid; single-multiple valuation is the caveat.

- Reward case: P/S at the cheapest 1% of its history, P/E 13.4, TTM EPS up every quarter for six (+29%), 40% below the 5-year high. Held in the running v3 portfolio since April 2026 (+8%).
- Main risks under these rules: The valuation percentile rests on one multiple: the filings carry no EBITDA or operating-income tag for an insurer, so EV/EBITDA and EV/EBIT are missing and the one-off guard could only test the EPS jump. Specialty-insurance pricing is cyclical and the growth (16%) is the slowest of its own history.

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression, triggered by excess industry capacity** (the E&S soft market). Operating EPS rose 73% from FY2023 ($12.50) to TTM $21.67 while the P/E on it fell from ~44x to ~15x. What set the multiple off was new capacity, including standard carriers, cutting Commercial Property rates, which took premium growth from +34% to -5%.  <!-- inventory cycle | financing-sensitive demand | temporary execution | excess industry capacity | valuation compression | structural deterioration -->

Narrative (what actually happened, with dates and numbers from the filings; prices from the local cache, sources in the [research notes](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/KNSL.md)):

- 5-year high 547.98 on 2024-03-06; price now -40%. From that month's close (524.74) P/S went from 10.0 to 3.8 (-62%) while TTM revenue per share changed +65%: the fall is all multiple (price and valuation caches, derived).
- 12-month price return -20%; TTM EPS +29% over the same span; revenue +16%.
- **High, 2024-03-06, $547.98.** It came after Q4 2023: GWP +33.8%, combined ratio 72.1%. At the high the stock traded at P/B 11.7x and P/E 41x GAAP (44x operating) on FY2023 figures.
- **2024-04-26, -17.3% ($453.09 → $374.64).** Q1 2024 GWP growth slowed to +25.5% from +33.8%, and the combined ratio rose to 79.5% from 72.1% in Q4. Management said property was returning to "a normal level of competition". The April low was $358.00. I found no news story giving the market's reason for the drop. This leg was fully retraced: +17.5% on 2024-07-26 (Q2 GWP +20.9%, op EPS +30%) and back to $524.22 on 2024-12-06.
- **2025-02-14, -7.8%, and 2025-04-25, -16.3% ($501.97 → $419.99).** Q4 2024 GWP growth was +12.2% in an "increasingly competitive" market. Q1 2025 GWP grew +7.9% against J.P. Morgan's expected 15%. Commercial Property fell 18.4%, the Palisades Fire cost 6.0 points of cat losses, and op EPS rose only 6%.
- **H2 2025 grind, $478.99 (2025-10-08) → $354.60 (2025-12-08).** GWP grew +4.9% in Q2 and +8.4% in Q3 (-6.8% on 2025-10-24, the same day President/COO Haney's March 2026 retirement was announced). Commercial Property was -8% to -17% while the rest grew +12% to +14%. Op EPS was still up 24-28%.
- **Feb-Apr 2026, results plus downgrades, $414 → $327.** Q4 2025 GWP +1.8% with Commercial Property -28.3% (-7.4% on 2026-02-13). BMO cut to Underperform on 2026-02-25 (PT $348). Jefferies cut to Underperform on 2026-03-19, sending the stock -6.2% to $326.72 (PT $312). Its argument: E&S market growth fell to ~8% in 2025 and ~3% in H2 2025, and after single-digit growth the industry has historically compounded 1-2% a year for three years. Morgan Stanley cut to Equal-weight on 2026-04-06 (PT $350). Cantor cut its PT to $280 on 2026-04-09, expecting ~3 points of loss-ratio deterioration.
- **Q1 2026 and the low.** GWP fell 0.5% (Commercial Property -28.3%, "including from standard carriers") while op EPS rose 37.7%; the stock lost 7.0% over the next 5 days. Low **$290.20 on 2026-06-03 (-47%)**, P/B 3.4x.
- **Q2 2026 bounce.** Op EPS $5.54 vs ~$5.10 consensus and combined ratio 75.5%, but GWP -5.0% (Commercial Property -32.7%, ex-property +3.7%). +5.1% on 2026-07-24 and up to $395.51 by 2026-08-24.
- **September 2026, -11.6% ($373.90 → $330.49).** I found no company-specific news. Specialty and broker peers fell by similar amounts over the same dates (RLI -12.3%, AJG -11.8%, BRO -15.7%, RYAN -10.2%; SPY -0.8%), so this looks like a sector de-rating on softening pricing. Public brokers reported roughly flat organic growth in Q2.

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **An unsustainable multiple, not an earnings peak.** Op EPS rose from $12.50 (FY2023) to $21.67 TTM (+73%) and BVPS from $46.88 to $89.34. The combined ratio was 75.4% in FY2023 and is ~75% TTM. The multiple at the high (P/B 11.7x, ~44x op EPS) assumed premium growth would stay at 34-42% (FY2022-23 GWP +44%/+42%). Growth is now -5%.
- Caveat pointing the other way: today's earnings sit on the best underwriting margins of the cycle. The combined ratio of ~75% includes 4.5 points of reserve releases, against 84.7% in 2019 and 86.7% in 2020. Operating ROE has already slipped from 31.8% (FY2023) to 24.4% (H1 2026) as equity grew. The bear question is margin, not the multiple.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | **$210.5M** cash and equivalents; $5.5B cash and invested assets (fixed maturities $4.47B, avg AA-, duration 4.3y; equities $773M; real estate $55M). The invested assets back $3.19B of gross loss reserves, so they are not free cash. (The $2.89B in section 1 / the fundamentals cache is not a 10-Q line — see log) | [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1669162/000166916226000040/knsl-20260630.htm), balance sheet 2026-06-30 |
| Realistically available credit (undrawn revolver, covenants) | $100M senior unsecured revolver (+$30M accordion), $51M drawn → **$49M undrawn**; SOFR + 1.625%. Covenants: "financial covenants customary for agreements of this type", in compliance at 2026-06-30 (specific tests not disclosed); restricted-payments covenant loosened in Dec 2025 | 10-Q Note 13 |
| Debt maturities next 24 months | **Revolver $51M due 2027-07-22** (only item). Senior notes $175M (5.15% $125M, 6.21% $50M) due 2034-07-22, amortizing $35M a year from July 2030. Total debt $224.5M | 10-Q Note 13 |
| Cash consumption if weak conditions persist 24 months | none on operations: operating cash flow $490.8M in H1 2026 (includes float growth; FCF TTM $1.00B in the cache is float-inflated, not distributable). The real stress case is reserves or a catastrophe: a 10% deficiency on $3.19B gross reserves (~$320M pre-tax) would be ~12% of $2.04B equity | 10-Q; derived |
| Interest, maintenance capex, leases, other fixed obligations | interest $6.5M in H1 2026 (~$13M/yr, coverage 60x); dividends $0.25/qtr (~$23M/yr); capex $10.3M in H1 2026; no lease liability disclosed (owns its real estate) | 10-Q |
| Can recovery happen without a large equity raise? | yes — equity $2.04B, debt/equity 11%, $337.5M buyback authorization outstanding | 10-Q; Q2 2026 release |

Gate verdict: PASS — reasoning:

- Profitable in 4 of 4 reported years (TTM net income positive in every reading of the SEC cache back to 2014), holding-company debt of $224.5M against $2.04B equity, and ~$13M of annual interest against ~$0.6B TTM pre-tax operating income. The only maturity before 2030 is the $51M revolver in July 2027, which is small next to annual earnings. The subsidiary's statutory dividend capacity was not verified.
- For an insurer the survival risks are reserve adequacy and catastrophes, not liquidity. Reserves have developed favorably in every quarter since Q4 2023 (2.3-4.5 points). Property is down to 25.9% of GWP, which reduces cat exposure. The item to watch is adverse development in construction liability on the 2017-2019 accident years, which recent releases on 2020-2025 have offset so far.

## 4. Recovery thesis  (testable statement)

> The business weakened because of **a softening E&S market: new capacity, including standard carriers, cut Commercial Property rates and volume (division premiums -28% to -33% y/y from Q4 2025 to Q2 2026), taking total GWP growth from +34% (Q4 2023) to -5% (Q2 2026) while underwriting margins held (combined ratio 75.5%)**. Recovery requires **total premiums to grow again as the property decline laps, with casualty and small-account growth continuing, while the combined ratio stays at or below ~80% and prior-year reserves keep developing favorably**.
> We expect to observe **total GWP back to flat-or-positive y/y, ex-Commercial-Property GWP growth of at least +5%, and a combined ratio under 80%** in the Q3 2026 to Q2 2027 reports (the next 2–4 quarters).

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| GWP growth, total and ex-Commercial Property, with new-business submissions | leading | Q2 2026: total -5.0%, ex-CP +3.7% (H1 +4.8%), CP -32.7%; submissions +6% (ex-CP +8%); avg premium per policy $12,300 vs $14,300 a year earlier | total GWP y/y ≥ 0% by the Q4 2026 or Q1 2027 report (60% of last year's CP premium was written in H1, so the comparison eases), ex-CP ≥ +5% | ex-CP GWP turns negative, or submissions flat/down (demand leaving, not just price) |
| TTM EPS vs entry $24.64 / trigger $20.94 | financial confirmation | $24.64 (+29% y/y) | flat or rising at each month-end | prints at or below $20.94 at a month-end before 2027-09-28 (rule exit) |
| Combined ratio and prior-year reserve development | margin / quality | Q2 2026 CR 75.5% (H1 76.4%), favorable PYD 4.5 pts, cat 1.3 pts; operating ROE 24.4% (H1) | CR ≤ 80% with PYD still favorable; operating ROE ≥ 20% | CR above ~82% for two quarters, or net adverse prior-year development |
| TTM revenue growth (entry +16%) | rule screen | +16% | holds double digits; latest quarter ≥ year-ago quarter | latest quarter below its year-ago quarter (fails the organic screen) |

Rule-level note on the EPS row: the trigger reads **GAAP** TTM EPS, which includes equity mark-to-market. Operating TTM EPS is $21.67, only 3.5% above $20.94. On consensus with no investment gains, TTM EPS falls to ~$21.3 after the Q2 2027 report (late July 2027), when Q2 2026's $7.72 (with $2.18 of gains) drops out. A ~10% equity-market decline in the window, a heavy cat quarter or a reserve charge could therefore trip the exit without the thesis breaking. Arithmetic in the research notes, section 8.

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- No EBITDA or operating-income tag in the filings: EV/EBITDA and EV/EBIT are missing, so the valuation percentile is P/S only and the one-off guard could only test the EPS jump.
- **Investment gains:** TTM GAAP EPS of $24.64 includes ~$3.0/share of equity fair-value changes and realized gains (Q2 2026 alone +$2.18: $56.2M fair-value change and $6.7M realized gains, pre-tax). Use operating EPS ($21.67 TTM) as the base. Consensus is on the operating basis (FY2026 ~$21.13, FY2027 ~$21.65). The cache's "forward EPS 21.65 / implied forward -12.3%" compares that operating consensus with GAAP TTM and overstates the expected decline.
- **Reserve releases:** TTM favorable development of $70.9M pre-tax (≈ $2.46/share after tax, ~11% of op EPS), up from 2.6-2.8 points in 2024 to 4.5 points in 2026. It has recurred so far, but it is the first thing to fade in a soft market.
- **Light catastrophe year:** quarterly cat losses were 0.3-1.3 points over the last four quarters, against 6.0 in Q1 2025 and 3.8 in Q3 2024. Each point of TTM NEP ($1,651M) is ~$0.57/share after tax.
- **Tax:** effective rate 19.8% in H1 2026 (stock-comp benefits, tax-exempt income); no one-off tax items found.
- **Stock comp and buybacks:** stock comp $11.4M in H1 2026, included in op EPS. Buybacks were $163M in H1 2026 and diluted shares are -1.0% y/y. The $337.5M authorization is worth ~3-4% a year of EPS accretion at current prices if used.
- **No acquisitions.** Expense ratio +1.0 pt y/y (21.7%) from reinsurance commission changes; the CFO expects that level or a "slight uptick".
- **Cash flow:** operating cash flow includes float growth (unearned premiums, reserves), so P/FCF 7.5 in section 1 overstates distributable cash. Net income is the better proxy.

## 5. Valuation — three scenarios, 3-year horizon

Insurer version of the template. "Sustainable margin" is replaced by **combined ratio / operating ROE**, and the multiple is **P/E on operating EPS, cross-checked with P/B**; EBITDA/EV multiples do not apply. Year 3 = TTM to 2029-06-30, the last report before the September 2029 horizon. Total return includes ~$3 of dividends ($0.25 a quarter).

| | Bear | Base | Bull |
|---|---|---|---|
| GWP growth path (assumption) | flat to -2% a year (Jefferies' 1-2% industry CAGR after a slowdown, with Kinsale losing share) | ~0% in 2026, then +4-6% a year | +8-10% a year from 2027 (casualty hardens, property stabilizes) |
| Revenue (yr 3; NEP + net investment income + fees, excl. investment gains) | $1.89B (NEP $1.60B) | $2.14B (NEP $1.83B) | $2.48B (NEP $2.15B) |
| Sustainable margin → **combined ratio / operating ROE** | 85% / ~17% | 79% / ~22% | 76% / ~25% |
| Net operating income (yr 3) | $370M | $499M | $621M |
| Net debt / cash (yr 3) | debt ~$175-225M; cash & invested assets ~$5.9B (backs reserves, not net cash) | ~$175-225M; ~$6.3B | ~$175-225M; ~$6.9B |
| Diluted shares (yr 3) | 21.8M | 21.3M | 21.6M |
| Operating EPS (yr 3) | $16.99 | $23.45 | $28.74 |
| Multiple applied (P/E on op EPS; P/B cross-check) | 13x (today's trough) / 2.0x book | 17x / 3.3x book | 22x (below the 5y median 29x) / 4.6x book |
| Implied price | $221 | $399 | $632 |
| Total return / annualised | -32% / -12.2% | +22% / +6.7% | +92% / +24.3% |
| Probability weight | 30% | 50% | 20% |

Probability-weighted value **~$392**: +20% including dividends over three years, ~6.1% a year from $330.49.

Key assumptions:

- Underwriting income = NEP × (1 − combined ratio); Kinsale's ratio is net of fee income. Pre-tax operating income = underwriting income + net investment income − interest ($13-15M) − other ($2M), taxed at 20%. On TTM inputs (NEP $1,651M, NII $213M, CR ~75%) this gives $493M against $500M reported.
- Net investment income grows with float and retained equity to $240M / $255M / $275M (TTM $213M), at a ~4.5% portfolio return (lower in the bear).
- Bear combined ratio of 85% means a return to the 2019-2020 levels (84.7% / 86.7%) as reserve releases fade and loss trend outruns falling rates. Base 79% assumes 3-4 points of deterioration (Cantor expects ~3 points). Bull 76% is roughly today.
- Buybacks $250-300M a year, dividend $1/share, no acquisitions, no equity raise.
- Multiples: the base 17x sits between today's 15x and the ~3.7x book justified by 20% ROE, 5% growth and a 9% cost of equity ((0.20 − 0.05) / (0.09 − 0.05)). The bear 13x is the lowest P/E in the cache history (today's 13.4x). The bull 22x is still below the 5-year median P/E of 29.3x.
- Not modelled: a large reserve charge (tail risk beyond the bear case) and a hard-market snap-back after a major catastrophe year (tail beyond the bull case).

What does today's price already require the business to deliver?

- At $330.49 the stock trades at 15.25x TTM operating EPS ($21.67), 15.6x FY2026 consensus and 15.3x FY2027 consensus, and at **3.70x book** ($89.34).
- Consensus (third-party, [stockanalysis.com](https://stockanalysis.com/stocks/knsl/forecast/), MarketBeat/Zacks via news items): FY2026 revenue ~$1.96B (+4.7%), op EPS ~$21.13 (+8.3%); FY2027 op EPS ~$21.65 (+2.4%; another source shows $21.10), revenue ~+1%. Ratings Hold/Reduce, average PT $355-362.
- Reverse-implied: P/B = (ROE − g) / (r − g). At 3.70x book and a 9-10% cost of equity, 22% ROE implies 4.2-5.6% perpetual growth, 20% ROE implies 4.9-6.3%, and 24% ROE implies 3.4-4.8%. The price therefore needs ROE held in the low 20s (a combined ratio near 80%, not the mid-80s of 2019-2020) and book growth of ~4-6% a year after buybacks. It does not need premium growth to return to 20%+. In EPS terms, consensus's roughly flat 2026-2027 earnings at today's 15x is today's price: no recovery is priced in, but no margin reversion is either.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 3.8 | 7.4 | 3.7 | 10.9 | 0.01 | 10.0 | 2018-03-31 |
| EV/EBITDA (cache; not used by v3) | 12.3 | 27.0 | 12.3 | 34.5 | 0.00 | 30.9 | 2018-03-31 |
| P/E (trailing) | 13.4 | 29.3 | 13.4 | 52.5 | 0.00 | 39.7 | 2018-03-31 |

At the 5-year median P/S (7.4) on today's TTM revenue the price would be about $639 (+93%); at the 5-year low (3.7), about $319 (-3%). Mechanical, not a forecast.

P/B, the insurer anchor (derived from reported BVPS, not in the cache): 3.70x today; 11.7x at the 2024-03-06 high; 7.3x at end-2024; 4.6x at end-2025; 3.4x at the 2026-06-03 low. Cantor's $280 target used 2.8x book.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.01, growth +16%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$20.94** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (n/a today)
- **Price target where recovery is fully reflected:** trim half at **$496** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** none in the basket (KNSL is the only financial); exposed to the specialty P&C pricing cycle
- **Research overlay (not part of the rule):** More confident if total GWP turns flat-or-positive y/y by the Q4 2026 or Q1 2027 report, with ex-Commercial-Property growth of +5% or more and a combined ratio under 80%, if WSIA's full-year 2026 data show casualty premium still growing, and if buybacks keep running at around $100M a quarter near today's price. Less confident if ex-property GWP turns negative, the combined ratio goes above ~82% or prior-year development turns adverse (watch construction liability, 2017-2019 accident years), casualty rate changes turn negative, or standard carriers take share beyond property. Rule-level caution: on consensus, GAAP TTM EPS lands only ~2% above the $20.94 trigger after the Q2 2027 report, so an equity-market drop or a heavy cat quarter could force an exit without a thesis break. Dated catalysts: Q3 2026 results ~2026-10-22 (not yet announced; the pattern is the fourth Thursday of October); Atlantic hurricane season to 2026-11-30; WSIA full-year 2026 surplus-lines data ~late January 2027; Q4 2026 results ~mid-February 2027 (2025-02-13 and 2026-02-12 pattern) and the 10-K; Q1 2027 results ~late April 2027; annual meeting ~late May 2027; revolver maturity 2027-07-22; Q2 2027 results ~late July 2027 (the trigger-risk print). No investor day, pending regulatory decision or material litigation was found.

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #2: val 0.01, growth +16%, entry TTM EPS $24.64, trigger $20.94, trim $496 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/KNSL.md) | Cause set to valuation compression triggered by E&S soft-market capacity; survival PASS confirmed; probability-weighted value ~$392 (+20% over 3 years); main rule risk is GAAP TTM EPS landing ~2% above the trigger after the July 2027 report. Review deadline kept: 2027-03-27 already follows the second report after today (Q4 2026, ~mid-February 2027) |
| 2026-09-28 | Data fix in section 3 only | Cash and equivalents are $210.5M per the Q2 2026 10-Q, not $2.89B (fundamentals-cache figure of unverified origin; left unchanged in section 1 as the screen proxy). FCF $1.00B and P/FCF 7.5 in section 1 include float growth; the survival verdict is unaffected |

## 8. Research conclusion

The research supports the rule's buy. The fall is multiple compression, triggered by the E&S soft market, not a broken business: operating EPS is up 73% since the high, the combined ratio is ~75%, the balance sheet is conservative, and survival is not in question. The probability-weighted value is **~$392** (bear $221 at 30%, base $399 at 50%, bull $632 at 20%), about +20% including dividends over three years (~6% a year) from $330.49. That is a modest edge, because today's earnings sit on cycle-best margins. The single thing to watch is total GWP growth against the combined ratio: premiums growing again with the combined ratio under 80% is the recovery, while flat premiums with the combined ratio drifting to the mid-80s is the bear case. In the v3 basket KNSL is the only financial. Its drivers (the P&C pricing cycle, bond yields) are largely separate from the de-ratings in software (APPF, INTU, DT, NOW, VEEV) and medtech (PODD, DXCM, BSX), and higher rates help it while hurting long-duration growth names. The shared exposure is the equity market: the $773M equity portfolio runs through GAAP EPS, so a broad sell-off would raise the chance of a guide-cut exit here at the same time as it hits prices elsewhere (OLLI is the other name with no software or medtech link).
