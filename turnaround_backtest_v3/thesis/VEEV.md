# VEEV — Veeva Systems

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #9 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-02-28 |
| Monthly RSI, last completed candle | 61.7 |
| Episode months / min RSI | 5 / 35.4 |
| Drawdown from trailing 5-year high | -13.7% (high 325.25 on 2021-10-21) |
| Market cap / avg daily $ volume (3m) | $45.44B / $423M |
| Sector / industry | Health Care / Health Care Technology |
| Survival gate (proxy) | PASS — cash $7.24B, debt due <1y $15M, FCF TTM $1.67B, 24m gap -$7.23B |
| Net debt / EBITDA, interest coverage | -6.6 / n/a |
| Valuation | P/E trailing 46.1, P/E forward 27.4, PEG 1.25, P/S 13.14, EV/Sales 11.1, EV/EBITDA 35.7, P/FCF 27.3 |
| EPS | TTM 6.08, forward est. 10.25; growth YoY (TTM) +25.9%, last quarter +39.5%, implied forward +68.6% |
| Revenue YoY (last quarter) | +17.6% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 9 of 10 / 11 of 20 |
| TTM revenue growth | +17% (latest quarter 2026-07-31) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.17** — P/S 0.28, EV/EBITDA n/a, EV/EBIT 0.06 (P/E pct 0.05, not used) |
| Multiples today | P/S 13.5, EV/EBITDA n/a, EV/EBIT 38.1, P/E 46.0 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 60.6 / 35.4 |
| From 5-year high | -14% |
| TTM EPS path, 6 quarters (oldest first) | 4.71, 4.86, 5.13, 5.44, 5.64, 6.10 |
| TTM EPS vs 12 months earlier | +26% |
| One-off EPS guard | passed — TTM net income / operating income 0.98 |
| Acquisition guard | passed — diluted shares -0.2% y/y |
| Net debt / EBITDA | n/a |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 35 shares per $100k at Friday's $280.68).
Entry TTM EPS **$6.10** → guide-cut trigger **$5.19** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$421** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val 0.10-0.25: n 222, mean +17%, median +16%, 66% winners, 52% beat SPY; less than 40% below: n 306, mean +14%, median +13%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Low risk, smallest valuation edge; already a winner in the backtest.

- Reward case: EPS up every quarter (+26%), net cash, 17% growth, EV/EBIT at the 6th percentile. In the running portfolio since April 2026 at $172.74 (+65%, trimmed).
- Main risks under these rules: Least distressed name after DT: 14% below its 5-year high, monthly RSI 61; the P/S percentile (0.28) is the honest one and the 0.17 mean is pulled down by EV/EBIT. No EBITDA tag, so two multiples only. Trigger $5.19.

## 2. Why did the stock fall?  (diagnosis)

Cause category: valuation compression — revenue grew year over year in every quarter (+13% to +24% since FY2025) and TTM GAAP EPS went from $2.62 at the 2021 high to $6.10; both big drawdowns (-54% to Oct 2022, -51% from Oct 2025 to Apr 2026) were multiple de-ratings. The second was sharpened by a real but bounded competitive loss (Vault CRM top-20 accounts from 18 to about 14) and the sector-wide AI-agent sell-off.  <!-- inventory cycle | financing-sensitive demand | temporary execution | excess industry capacity | valuation compression | structural deterioration -->

Narrative (what actually happened, with dates and numbers from the filings; full dated table and sources in the research notes):

- 5-year high 325.25 on 2021-10-21; price now -14%. From that month's close (317.01) P/S went from 30.9 to 13.5 (-56%) while TTM revenue per share changed +102%: the fall is all multiple (price and valuation caches, derived).
- 12-month price return +0%; TTM EPS +26% over the same span; revenue +17%.
- **Leg 1, Oct 2021 - Oct 2022, 325.25 → 151.10 (-54%).** Growth normalised from the mid-20s and the margin guide stepped down. Dec 1, 2021: the first FY2023 outlook ($2,150-2,170M) came with a ~38% non-GAAP operating margin versus ~41% for FY2022. Mar 3, 2022, -16.2%: FY2023 guide below consensus and a BofA downgrade on peaking growth and margins. Sept 1, 2022, -14.0%: FY2023 revenue cut to $2,140-2,145M from $2,165-2,175M ([8-K](https://www.sec.gov/Archives/edgar/data/1393052/000139305222000033/veev-20220731q223xex991.htm)). TTM EPS dipped only 2.66 → 2.42 (-9%) while TTM revenue rose 25%.
- **Dec 2, 2022, -8.6%: the CRM decision.** Veeva said it would not renew the Salesforce platform agreement (ends Sept 2025) and would rebuild CRM on Vault. Salesforce then built its own Life Sciences Cloud, and by Dec 2024 Veeva had confirmed that one top-20 customer had left ([Bloomberg via Yahoo](https://finance.yahoo.com/news/salesforce-stokes-veeva-fight-snagging-153210048.html)).
- **2023-2024, range 158-250.** Standardised termination-for-convenience rights (from Feb 1, 2023) pushed revenue timing and cut reported growth: Q1 FY24 revenue +4%, subscription +3%. On Nov 9, 2023, -14.2%, the investor day cut the FY2025 revenue floor to ≥$2,750M from ≥$2,800M ([8-K exhibit](https://www.sec.gov/Archives/edgar/data/1393052/000139305223000057/investorday8-kexhibit.htm)). On May 31, 2024, -10.3%, the FY2025 revenue guide was cut to $2,700-2,710M. FY2025 still closed at $2,746.6M.
- **Recovery to 306.22 on Oct 7, 2025 (-6% from the high).** FY2026 was beat-and-raise every quarter; the May 29, 2025 print gave +19.0%. The IQVIA litigation dating from 2017 was settled on Aug 13, 2025 (announced Aug 18): no damages either way, a ~$31M success fee to Veeva's law firms, and mutual data-access agreements ([FY26 10-K note 13](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000014/veev-20260131.htm)).
- **Leg 2, Oct 2025 - Apr 2026, 306.22 → 151.43 on Apr 10 (-51%); this is the dip that qualified.** Nov 21, 2025, -9.8% (-16.8% in 5 days): the Q3 FY26 print beat and raised, but the CEO said of Vault CRM, "We used to have 18 out of the top 20. Now we're maybe going to have 14 or so" ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-veeva-systems-q3-2026-beats-expectations-stock-dips-93CH-4371867)). Jan-Feb 2026 brought the software AI-agent sell-off (Feb 3, -6.2%, after the Claude Cowork plugins; February was the first oversold month). The Mar 4 print guided FY2027 to $3,585-3,600M (+12-13%) and the stock rose 4%. Apr 9-10 (-5.7%, -3.6%) was the second leg of the SaaS sell-off, leaving the April month-end at a trailing P/E of 28.7, the 5-year low. TTM GAAP EPS rose 4.86 → 5.44 (+12%) over the leg.
- **Retest and rebound, 153.16 on Jun 22 → 280.68 (+83%).** After the Jun 3 beat-and-raise, Piper ($285 → $235) and Mizuho ($295 → $270) cut targets on AI timing and disruption risk. Then came Vault CRM wins at Lilly (Aug 11), Biogen and Regeneron (Aug 25) and Amgen (Sept 15). The Q2 FY27 print on Aug 26 gave +15.2% (revenue +18%, guide raised to $3,682-3,687M), and by Sept 23 the count was **14 of the top 20 committed** ([Veeva](https://www.veeva.com/resources/vault-crm-extends-market-leadership-as-another-top-20-biopharma-chooses-veeva/)).

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **No earnings peak; the multiple.** At the high the stock was ~124x TTM GAAP EPS ($2.62) and 30.9x sales on a 27.2% TTM GAAP operating margin. Today TTM GAAP EPS is $6.10, the operating margin is 29.9% and the non-GAAP margin guide is ~44% (FY2022 guide ~41%). The two EPS dips in between (-9% in 2022, -7% in late 2023 on termination-for-convenience timing) never came near a 15% cut. What did change is growth: 26% in FY2022, mid-teens now, with consensus at ~12% for FY2028.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $7.24B ($1.81B cash + $5.43B short-term investments; $102M outside the U.S.); no borrowings; total "debt" $152M is all lease liabilities; net cash $7.09B | fundamentals cache, balance sheet 2026-07-31; [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1393052/000139305226000036/veev-20260731.htm) |
| Realistically available credit (undrawn revolver, covenants) | none: no credit facility, revolver or line of credit is disclosed in the FY2026 10-K or the Q2 FY27 10-Q, so there are no covenants. Liquidity is the cash pile | FY2026 10-K; Q2 FY27 10-Q |
| Debt maturities next 24 months | no debt. Lease payments only: $7.6M rest of FY2027, $13.8M FY2028, $22.3M FY2029 ($197.5M undiscounted in total, 9.5-year average term) | Q2 FY27 10-Q note 9 |
| Cash consumption if weak conditions persist 24 months | none: operating cash flow TTM $1.67B, H1 FY2027 $1.37B; FY2027 non-GAAP operating cash flow guide ~$1.60B; capex ~$10M a half-year | fundamentals cache; Q2 FY27 10-Q; [Q2 remarks](https://s206.q4cdn.com/200001835/files/doc_financials/2027/q2/Veeva-Q2-27-Earnings-Prepared-Remarks.pdf) |
| Interest, maintenance capex, leases, other fixed obligations | no interest expense; operating lease expense $11M in H1 FY2027; AWS and Salesforce hosting costs sit in cost of revenue (commitment amounts not disclosed in the filings read). Buybacks are discretionary: $2B program to Jan 2028, $1.4B left | Q2 FY27 10-Q |
| Can recovery happen without a large equity raise? | yes | positive FCF, net cash |

Gate verdict: PASS — reasoning:

- $7.24B of cash and investments, no debt, no covenants and ~$1.6B a year of operating cash flow against ~$20M a year of leases. The only material uses of cash are optional (buybacks, small AI acquisitions such as Ostro at $90M and Copli). Survival is not the question for this name.

## 4. Recovery thesis  (testable statement)

> The business weakened because of **nothing in the numbers. The multiple fell from ~31x to ~13x sales as growth normalised from the mid-20s to the mid-teens, and in Nov 2025 - Apr 2026 it was hit twice more: by the Vault CRM top-20 reset (18 accounts on Veeva CRM, about 14 committed to Vault CRM) and by the market's fear that AI agents shrink seat-based software**. Recovery requires **subscription growth to hold at 14%+ with GAAP EPS compounding in the mid-teens while the CRM migration completes without further top-20 losses, and Veeva AI (Vault AI, Falcon, Ostro) to show up as added revenue rather than lost seats in Development and Commercial Cloud**.
> We expect to observe **Q3 and Q4 FY2027 results at or above the $932-935M and $3,682-3,687M guides, a FY2028 guide in March 2027 of about 12%+ revenue growth (consensus $4.13B) at a ~44% non-GAAP margin, and the first Falcon early-adopter go-lives in 2026 as promised** within the next 2–4 quarters.

Much of the price recovery has already happened (+85% from the April low). The thesis now has to hold the multiple through the next two reports; it does not rest on a re-rating.

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| Vault CRM: top-20 commitments, go-lives, Commercial subscription growth | leading (company-specific) | 14 of top 20 committed (Sept 23, 2026), 190+ live, five top-20s live in major markets; Commercial subscription +13.0% in Q2 FY27, FY2027 guide ~$1,405M | no reversal among the 14; more top-20 go-lives and 200+ live in the Q3/Q4 reports; FY2028 Commercial growth guided ≥ ~11% | a committed top-20 goes to Salesforce, migrations slip past 2028, or Commercial subscription growth guided below ~9% |
| Veeva AI and R&D / Quality growth | leading | Falcon: five early adopters, first go-lives "this year", first top-20 in H1 2027; Vault AI agents GA since Aug 2026; R&D and Quality subscription +19.3% in Q2, FY2027 guide ~$1,675M | Falcon go-lives on schedule and priced as new revenue; R&D and Quality subscription growth ≥ 15% in the FY2028 guide | Falcon slips to H2 2027, R&D and Quality growth guided below ~12%, or customers cut seats citing AI |
| TTM EPS vs entry $6.10 / trigger $5.19 | financial confirmation | $6.10 (+26% y/y). Q3 FY26's $1.40 leaves the TTM next; Q3 FY27 GAAP EPS would have to fall below $0.49 to reach the trigger (the $2.33-2.34 non-GAAP guide implies ~$1.64 GAAP at the recent 0.70 ratio, derived) | flat or rising at each month-end | prints at or below $5.19 at a month-end before 2027-09-28 (rule exit) |
| TTM revenue growth (entry +17%) | screen (organic test) | +17%; latest quarter +18% (subscription +16%, services +24%) | holds double digits; latest quarter ≥ year-ago quarter | latest quarter below its year-ago quarter (fails the organic screen) |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **Interest income on the cash pile:** other income TTM ≈ $293M, almost all interest (FY2026 interest income $267M). That is ~$1.38 a share after tax, ~23% of the $6.10 TTM GAAP EPS. It falls if rates fall or the cash is spent on acquisitions; ex-cash and ex-interest, the stock is at ~50x TTM GAAP EPS ($236.80 / $4.72, derived) and 38x EV/EBIT.
- **IQVIA success fee in the base year:** the $31M charge sat in Q2 FY26 G&A, so Q2 FY27 GAAP EPS growth (+39.5%) and the +26% TTM EPS growth are flattered. Ex-charge TTM growth is about +22% (derived). The $6.10 entry base no longer contains it: it is clean.
- **Tax:** the Q2 FY27 effective rate was 21.8% vs 24.5%, from the FDDEI deduction under the One Big Beautiful Bill Act. Lower cash taxes also lifted H1 operating cash flow. Non-GAAP EPS uses a fixed 21%.
- **Stock comp:** ~$495M TTM (~14% of revenue); non-GAAP EPS TTM $8.69 vs GAAP $6.10. Buybacks ($473M in H1 FY2027) more than offset dilution: diluted shares 165.1M, -1.6% y/y. 14.9M options are outstanding (average strike $182), so dilution rises with the price.
- **Mix and timing:** services (+24%) is growing faster than subscription (+16%) at lower margins, so total revenue growth overstates the recurring base. FY2027 revenue guidance includes a ~$20M FX tailwind and ~$10M from Ostro. Normalized billings are guided $38M below calculated billings (customer term changes).
- **Basis mismatch in section 1:** the "implied forward +68.6%" compares a non-GAAP forward EPS ($10.25) with GAAP TTM ($6.08); it is not a growth forecast. No EBITDA tag: the valuation mean uses P/S (0.28) and EV/EBIT (0.06); the P/S percentile is the honest one.

## 5. Valuation — three scenarios, 3-year horizon

Year 3 = FY2030 (Feb 2029 - Jan 2030), valued in about September 2029. Revenue paths start from the FY2027 guide midpoint ($3,685M). EPS = (revenue × GAAP operating margin + interest income) × (1 − tax) / diluted shares. The multiple is applied to GAAP EPS including interest, so net cash is inside the price, not added on top.

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $4.64B (8% a year: CRM pricing pressure, AI shrinks seats, pharma budgets tighten under MFN and tariffs) | $5.18B (+13%, +12%, +11%; FY2028 at consensus $4.13B) | $5.60B (15% a year: Falcon, Ostro and CRM win-backs on top of the $6B 2030 plan) |
| Sustainable margin | 27% GAAP operating (~40% non-GAAP) | 32% GAAP (~45% non-GAAP) | 35% GAAP (~47% non-GAAP) |
| Net debt / cash (yr 3) | ~$8.0B net cash (interest ~$0.29B) | ~$9.2B (~$0.32B) | ~$9.5B (~$0.33B; more spent on buybacks at higher prices) |
| Diluted shares (yr 3) | 158M | 160M | 162M |
| Multiple applied | 25x GAAP EPS of $7.52 (P/S 6.4) | 32x EPS of $9.64 (P/S 9.5) | 40x EPS of $11.03 (P/S 12.8) |
| Implied price | $188 | $308 | $441 |
| Total return / annualised | -33% / -12.5% | +10% / +3.2% | +57% / +16.3% |
| Probability weight | 25% | 50% | 25% |

Probability-weighted value **$312 (+11%, about 3.5% a year)** from Friday's $280.68 (no dividend).

Key assumptions:
- Tax is 22% (23% in bear).
- Buybacks of about $1B a year retire 1-1.5% of the shares net of option issuance.
- Bear's 25x is below the April 2026 trough (28.7x trailing, the 5-year low). Base's 32x is roughly today's multiple of FY2029 consensus GAAP EPS (33x), i.e. no re-rating. Bull's 40x is still below the 5-year median of 61x.
- The base case lands well under the $421 trim within three years; only the bull path reaches it.

What does today's price already require the business to deliver?

- **Consensus (third-party).** Zacks via [Yahoo](https://finance.yahoo.com/markets/stocks/articles/investors-heavily-search-veeva-systems-130004429.html), Sept 17, 2026, non-GAAP: FY2027 revenue $3.69B (+15.3%), EPS $9.22 (+13.8%); FY2028 $4.13B (+12%), $10.16 (+10.2%). [MarketScreener](https://www.marketscreener.com/quote/stock/VEEVA-SYSTEMS-INC-14551091/finances/) GAAP EPS: FY2027 $6.53, FY2028 $7.31, FY2029 $8.42; revenue FY2029 $4.65B. Average target $297 (29 analysts).
- **Multiples today:** 30x FY2027 and 27.6x FY2028 non-GAAP EPS; 38x FY2028 and 33x FY2029 GAAP EPS; EV ≈ $39.2B = 10.6x FY2027 revenue guide, 23.5x TTM operating cash flow, 33.5x operating cash flow less stock comp.
- **Reverse-implied growth:** a 10-year reverse DCF on operating cash flow less stock comp ($1.17B), with a 9% discount rate and 3% terminal growth, needs ~12% a year (9% at an 8% discount rate, 14% at 10%). That is the company's own $6B-by-2030 path (~13% a year), which management says excludes AI and Aspen. The price therefore assumes the plan is met and needs AI or margin upside for more than a mid-single-digit return. It does not require a turnaround; it requires no slowdown.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 13.5 | 14.0 | 8.2 | 30.9 | 0.28 | 30.9 | 2013-10-31 |
| EV/EBITDA (cache; not used by v3) | 32.9 | 65.2 | 48.6 | 106.4 | 0.00 | 106.4 | 2013-10-31 |
| P/E (trailing) | 46.0 | 60.8 | 28.7 | 121.0 | 0.05 | 121.0 | 2013-10-31 |

At the 5-year median P/S (14.0) on today's TTM revenue the price would be about $292 (+4%); at the 5-year low (8.2), about $170 (-40%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.17, growth +17%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$5.19** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (n/a today)
- **Price target where recovery is fully reflected:** trim half at **$421** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** de-rated software (APPF, INTU, DT, NOW, VEEV): half the basket, one shared driver (AI-disruption / seat-pricing narrative and sector multiple); same-driver holdings: APPF, INTU, DT, NOW
- **Research overlay (not part of the rule):**
  - *More confident if:* the 14 top-20 commitments hold and turn into go-lives; the first Falcon go-lives land in 2026; R&D and Quality subscription growth stays at 15%+; and the FY2028 guide (early March 2027) is about 12%+ revenue growth at a ~44% non-GAAP margin.
  - *Less confident if:* a committed top-20 reverses; the FY2028 guide comes in near 10% or below; Commercial subscription growth falls toward high single digits (rep cuts under MFN pricing pressure, Section 232 tariffs); services keep outgrowing subscription; AI arrives as seat cuts rather than add-ons; or the Oct 2 departure of the President and Chief Customer Officer shows up in bookings. Aspen CRM (horizontal CRM) spending is an unquantified drag.
  - *Trigger risk:* remote, under 5%. Q3 FY27 GAAP EPS would have to fall below $0.49 against ~$1.64 implied by guidance.
  - *Catalysts:*
    - Section 232 pharma tariffs apply to all remaining companies from Sept 29, 2026.
    - Oct 2, 2026: Schwenger leaves; Dan Rizzo becomes EVP Sales, Consulting and Services.
    - Nov 1, 2026: the General Counsel retires.
    - Q3 FY2027 results, date not announced (last year Nov 20), with the Nov 30 month-end rule check.
    - Falcon early-adopter go-lives and Aspen early availability, both promised for "later this year".
    - Q4 FY2027 results and the FY2028 guide in early March 2027 (last year Mar 4).
    - First top-20 Falcon go-live in H1 2027.
    - Q1 FY2028 results in about early June 2027.

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #9: val 0.17, growth +17%, entry TTM EPS $6.10, trigger $5.19, trim $421 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/VEEV.md) | Diagnosis confirmed as valuation compression, survival PASS (no debt, no credit line needed), weighted 3-year value ~$312 (+11%): high quality, thin price edge. The CRM top-20 question is largely settled (14 of 20 committed on Sept 23); trigger risk remote. Sections 1/1b unchanged; review_deadline unchanged (2027-03-27 falls after the expected early-March Q4 FY2027 report, the second after today) |

## 8. Research conclusion

VEEV passes as a quality compounder bought after a multiple reset, not as a turnaround. Revenue and EPS rose through both drawdowns, and the one real competitive loss is now bounded: 14 of the top 20 committed to Vault CRM, versus 18 of 20 on the old product. The probability-weighted 3-year value is about $312 (+11%, ~3.5% a year) against $280.68. After the +85% rebound from April the price already discounts the company's own ~13%-a-year plan, so the edge is small and depends on AI adding revenue. The single thing to watch is the FY2028 guide in early March 2027: about 12%+ revenue growth with steady R&D and Quality subscription growth keeps the base case; near 10% would point to the bear case. In the basket it is the fifth dose of the de-rated software factor (APPF, INTU, DT, NOW) but the least exposed to the rule's mechanical exits. Its customer risk is pharma drug pricing and tariffs, which no other holding shares (PODD, DXCM and BSX are device makers; KNSL and OLLI are unrelated). Its net cash makes it the lowest-risk seat in the book. In the running v3 backtest book it is already held from April 2026 at $172.74 (+65%, trimmed), so the signal is a new buy only for a fresh account.
