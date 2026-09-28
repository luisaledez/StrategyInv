# BSX — Boston Scientific

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #10 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-02-28 |
| Monthly RSI, last completed candle | 29.9 |
| Episode months / min RSI | 7 / 24.0 |
| Drawdown from trailing 5-year high | -59.4% (high 108.14 on 2025-09-08) |
| Market cap / avg daily $ volume (3m) | $63.65B / $944M |
| Sector / industry | Health Care / Health Care Equipment |
| Survival gate (proxy) | REVIEW — cash $539M, debt due <1y $1.71B, FCF TTM $1.81B, 24m gap $1.17B |
| Net debt / EBITDA, interest coverage | 2.1 / 11.6 |
| Valuation | P/E trailing 17.8, P/E forward 12.9, PEG 0.62, P/S 3.03, EV/Sales 3.6, EV/EBITDA 13.4, P/FCF 35.2 |
| EPS | TTM 2.47, forward est. 3.41; growth YoY (TTM) +55.2%, last quarter +15.1%, implied forward +38.2% |
| Revenue YoY (last quarter) | +7.5% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 10 of 10 / 20 of 20 |
| TTM revenue growth | +14% (latest quarter 2026-06-30) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.21** — P/S 0.41, EV/EBITDA 0.12, EV/EBIT 0.10 (P/E pct 0.14, not used) |
| Multiples today | P/S 3.1, EV/EBITDA 13.9, EV/EBIT 18.6, P/E 17.8 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 28.0 / 24.0 |
| From 5-year high | -59% |
| TTM EPS path, 6 quarters (oldest first) | 1.37, 1.68, 1.87, 1.94, 2.39, 2.47 |
| TTM EPS vs 12 months earlier | +47% |
| One-off EPS guard | passed — TTM net income / operating income 0.88 |
| Acquisition guard | passed — diluted shares -0.1% y/y |
| Net debt / EBITDA | 2.2 |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 227 shares per $100k at Friday's $43.92).
Entry TTM EPS **$2.47** → guide-cut trigger **$2.10** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$66** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val 0.10-0.25: n 222, mean +17%, median +16%, 66% winners, 52% beat SPY; 40-60% below: n 250, mean +24%, median +19%, 68% winners. All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Fair; boundary case on growth rank.

- Reward case: Most oversold name on the list (monthly RSI 28, min 24), 59% below the 5-year high; EV/EBITDA and EV/EBIT at the 10-12th percentile; TTM EPS up 47% and rising every quarter.
- Main risks under these rules: Net debt 2.2x EBITDA, the highest of the ten; the P/S percentile (0.41) is not cheap, and growth (13.5%) is exactly rank 20, so this is the seat most exposed to the October 1 re-run (below). Trigger $2.10.

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression** — earnings kept rising (adj. EPS $0.75 → $0.86 per quarter, GAAP TTM +47%), but the growth that justified ~30x forward earnings reset from 15.8% organic (2025) to a 5-6% guide (2026) in three cuts, because the two premium franchises (Farapulse EP and Watchman) slowed at once; the slowdown has a structural part (U.S. PFA share loss to new entrants, weaker LAAC evidence), so a return to the 2025 multiple is not the base case.

No split or spin-off affects the comparison: the EDGAR cache shows splits only in 1998 and 2003, close equals adjusted close (no dividend), and the $108.14 high and $43.92 close are on the same basis.

Narrative (cache closes; numbers from the 8-K releases and 10-Qs; sources in the [research notes](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/BSX.md)):

| Leg | Dates | Move | Cause |
|---|---|---|---|
| Drift from the high | 2025-09-08 → 2025-12-31 | $108.14 → $95.35, -12% | No single dated cause. Q3 2025 was strong (organic +15.3%, FY raised to ~15.5%; +4.0% on Oct 22), but U.S. EP had stopped growing sequentially ($607M Q3 → $605M Q4). CLOSURE-AF (LAAC failed non-inferiority vs medical therapy) and OCEAN (low stroke risk after ablation) were presented at AHA on Nov 8, 2025 with no visible reaction at the time. Abbott's Volt PFA won FDA approval Dec 22, 2025. |
| Penumbra deal | 2026-01-15 | -4.0% | $14.5B EV agreement, ~73% cash (~$11B, cash plus new debt) / 27% stock. |
| FY2026 guide | 2026-02-04 | **-17.6%** to $75.50 | Q4 beat (adj. $0.80), but FY2026 organic 10-11% vs 15.8% in 2025 and adj. EPS $3.43-3.49 vs $3.47 consensus (third-party); EP $890M flat quarter on quarter and ~$33M below consensus. A securities class action (class period Jul 23, 2025 – Feb 3, 2026) alleges U.S. EP weakness was concealed. |
| Drift | 02-04 → 03-27 | -8% to $69.17 | FTC Second Request on Penumbra (Mar 16). |
| CHAMPION-AF | 2026-03-30 | **-9.0%** to $62.93 | Watchman FLX vs NOACs (ACC, Mar 28; NEJM): non-inferior on the primary endpoint (5.7% vs 4.8%), bleeding 10.9% vs 19.0%, but ischemic stroke 3.2% vs 2.0% (not significant). Read as "not a home run". |
| Q1 2026 | 2026-04-22 | **+9.0%** to $64.87 | Organic +9.4% beat, but FY cut to 6.5-8.0% organic and adj. EPS $3.34-3.41; Watchman volumes declined from February for the first time; EP +24% with more share loss than expected. Relief that the cut was out. |
| Drift | 04-22 → 05-26 | -11% to $57.64 | May 18 $2B ASR and $1.5B MiRus (TAVR option) stake: +6.2% that day. |
| Bernstein conference | 2026-05-27 | **-12.5%** to $50.46 | U.S. Watchman guided flat sequentially for Q2 and Q3, standalone procedures falling; EP share loss, leadless CRM and urology soft. Stifel target $85 → $75 (third-party). |
| Drift to the low | 05-27 → 07-28 | -9% to $46.06 | Low close $42.63 on Jul 14. |
| Q2 2026 | 2026-07-29 | 0.0% (premarket -6.6%) | Beat (organic +7.0%, adj. $0.86), but FY cut again to 5-6% organic, adj. EPS $3.28-3.32; Q3 organic 3-5%; 2027 revenue growth "below our WAMGR" with "limited adjusted EPS growth"; Penumbra "slightly dilutive" at first; restructuring plan ($700-800M charges, ~$500M savings by 2029). |
| Cyberattack | 08-25 → 09-25 | -12% to $43.92 | Network outage from Aug 25 stopped manufacturing, order processing and shipping; Sept 7 8-K: "unlikely to meet" Q3 and FY2026 sales and adj. EPS guidance (-5.9% on Sept 8). |

- Total 2025-09-08 → 2026-09-25: -59.4%. Over the same span MDT -5%, ABT -23%, SYK -31%, ISRG -14%, while XLV rose 21% (to Sept 14): large-cap medtech was weak, but most of BSX's fall is its own.
- 12-month price return -55%; TTM EPS +47% over the same span; revenue +14%. From the high month's close (97.63) P/S went from 7.9 to 3.1 (-61%) while TTM revenue per share rose 14% (price and valuation caches).
- Franchise evidence (10-Q revenue notes): U.S. EP $511M, $587M, $607M, $605M, $603M, $606M (Q1 2025 → Q2 2026), flat for four quarters; Q2 2026 U.S. EP +3% y/y against international +23%. Watchman $425M → $535M (Q4 2025) → $507M (Q2 2026), +4% y/y after ~29% growth in 2025. Management: PFA is already 80-85% of U.S. AF ablation, so conversion no longer hides the share loss to Medtronic (Sphere-9/Affera; Medtronic's ablation business +88% in its July quarter), Abbott (Volt) and J&J (Varipulse); standalone Watchman procedures fell mid-teens while concomitant cases (OPTION-supported, a third of U.S. volume) grew >60%.

Was the prior high an exceptional earnings peak or an unsustainable multiple? **Unsustainable multiple — not an earnings peak.**

- At the high month: trailing GAAP P/E 58, forward P/E ~29 (Yahoo snapshot Sept 30, 2025), P/S 7.9, EV/EBITDA 35. Today: 17.8, 12.9, 3.1 and 13.9.
- Earnings and margins did not peak: adj. EPS rose every quarter ($0.75 in Q3 2025 → $0.86 in Q2 2026); adj. operating margin was 28.4% in Q2 2026, up 70 bp y/y; adj. gross margin 70.3%.
- What peaked was the growth rate: EP went from $1.9B (2024) to $3.3B (2025, +75%) on the one-time conversion of the U.S. ablation market to PFA. The 2025 multiple capitalised that conversion wave as if it were durable.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $539M (total debt $12.62B, net debt $12.09B) | fundamentals cache, balance sheet 2026-06-30 |
| Realistically available credit (undrawn revolver, covenants) | $3.0B revolver (to Feb 2031) undrawn but backs commercial paper: $1.689B CP out, **$1.061B CP capacity left**; $2.0B 364-day revolver undrawn; $6.0B 364-day term loans committed, drawable only at the Penumbra closing. Covenant: debt / deemed EBITDA **2.02x vs 4.00x max** (3.75x base; 4.75x for four quarters after a >$1B acquisition) | [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000053/bsx-20260630.htm), Note E |
| Debt maturities next 24 months | CP $1.689B (rolling, 41-day average); **€900M 0.625% notes Dec 2027 ($1,026M)**; **Mar 2028 notes $855M + $344M**; nothing else before Mar 2029 ($1.13B). Notes due by Sept 2028: $2.23B. Plus, at the Penumbra closing, ~$11B of cash consideration funded mostly by 364-day loans that must be termed out within a year | 10-Q debt table |
| Cash consumption if weak conditions persist 24 months | none: TTM OCF $4.53B, PP&E capex $0.90B, **FCF ≈ $3.63B**. The cache's FCF of $1.81B (and P/FCF 35) deducts $1.73B of investment payments, mainly the $1.5B MiRus stake — not capex | 10-K / 10-Q cash-flow statements |
| Interest, maintenance capex, leases, other fixed obligations | interest $186M in H1 2026 (coverage 12x); operating leases $536M, finance lease $124M; purchase obligations $1.83B ($1.05B in 2026); restructuring cash $600-700M through 2029 | FY2025 10-K, 10-Q |
| Can recovery happen without a large equity raise? | yes | FCF covers the notes due in the window; the stock portion of the Penumbra deal adds ~41M shares (~3%, my estimate) |

Gate verdict: REVIEW (proxy) → **PASS** on the filings — reasoning:

- Liquidity is ample and covenant headroom large today; FCF of ~$3.6B a year covers the $2.2B of notes due by March 2028 with room to spare, and funding is commercial paper, bank lines and unsecured notes (no secured debt; credit ratings not checked).
- The real balance-sheet risk is after Penumbra: net debt rises to roughly $22-23B, about 3.8-4.0x EBITDA (my pro forma estimate; Penumbra's EBITDA is not disclosed), inside the 4.75x step-up but with little room if EBITDA falls, and with ~$6B of 364-day loans to refinance in the bond market. Buybacks likely pause. This is a leverage watch, not a survival question.

## 4. Recovery thesis  (testable statement)

> The business weakened because the two franchises that carried 2025 growth slowed together: U.S. Farapulse lost share once Medtronic, Abbott and J&J had competitive PFA systems (U.S. EP flat at ~$605M a quarter since Q3 2025), and standalone Watchman referrals fell after CLOSURE-AF, OCEAN and a mixed CHAMPION-AF read — on top of a $14.5B debt-funded Penumbra deal and the August 2026 cyberattack. Recovery requires U.S. EP to stop shrinking once the Q3 dip passes (FARAPOINT, FARAWAVE Ultra, persistent-AF data), Watchman to stabilise with concomitant growth and a CHAMPION-AF label, and Penumbra to close without a further guide cut or leverage above ~4x.
> We expect to observe a cyber hit sized as a one-off at the Oct 28, 2026 report, then U.S. EP back at ≥ $600M and U.S. Watchman ≥ $450M a quarter, with 2027 guidance no worse than "below-WAMGR growth, limited EPS growth", within the next 2–4 quarters (Q4 2026 and Q1 2027 reports).

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| U.S. EP and U.S. Watchman quarterly sales (10-Q revenue note) | leading | Q2 2026: U.S. EP $606M (+3% y/y, flat for 4 quarters); U.S. Watchman $459M (+3% y/y, down from $485M in Q4 2025) | Q4 2026 / Q1 2027 U.S. EP back to ≥ $600M after the guided Q3 dip, and U.S. Watchman ≥ $450M; 2027 guide at or above consensus ($22.25B revenue, $3.41 adj. EPS, third-party) | U.S. EP below ~$570M in two consecutive quarters after Q3, or U.S. Watchman below ~$420M; another 2027 guide cut |
| TTM EPS vs entry $2.47 / trigger $2.10 | financial confirmation | $2.47 (+47% y/y); ~$2.19 without Q1 2026's $0.21 deferred-tax benefit and $0.07 investment gain | flat or rising at each month-end | prints at or below $2.10 at a month-end before 2027-09-28 (rule exit). Real risk at the May 2027 month-end, when Q1 2026's $0.90 rolls off and Penumbra purchase accounting and interest are in the base (my estimate: TTM about $2.0-2.3) |
| TTM revenue growth (entry +14%) |  | +14%; Q2 2026 quarter +7.5% | holds positive; Q3 2026 revenue ≥ Q3 2025's $5,065M despite the cyber outage (consensus $5.15B, low $4.70B, third-party) | latest quarter below its year-ago quarter (fails the organic screen); a sub-$5,065M Q3 is possible from the outage alone |
| Net debt / EBITDA after the Penumbra closing | balance sheet | 2.2x (covenant 2.02x vs 4.00x) | below ~3.5x within four quarters of closing, 364-day loans termed out | above ~4x a year after closing, or buybacks resumed while leverage rises |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **Q1 2026 GAAP EPS $0.90 vs adj. $0.80:** $320M deferred-tax benefit ($0.21) and $137M pre-tax investment gain ($0.07). Passed the one-off guard (TTM net income / operating income 0.88) but is ~11% of TTM GAAP EPS.
- **Q2 2026:** IEEPA tariff refund +$83M pre-tax (+$0.05), offset by $0.05 of deferred tax expense; litigation charge $76M (-$0.04).
- **Amortization:** ~$230M a quarter (-$0.14), set to rise with Penumbra intangibles.
- **Litigation:** Q4 2025 $194M (-$0.10); securities class action on U.S. EP disclosure pending (lead plaintiff appointed May 20, 2026).
- **Restructuring:** 2026 plan $700-800M pre-tax through 2029 (Q4 2025 -$0.06; ~$0.02 a quarter in 2026 so far), more to come.
- **Acquisition charges and Penumbra:** deal costs ran $0.02-0.06 a quarter; at closing expect inventory step-up, integration costs, higher amortization and interest on ~$11B of new debt — all in GAAP, mostly excluded from adjusted.
- **Cyber incident (Q3 2026):** size, insurance recovery and adjusted-EPS treatment unknown until Oct 28.
- Organic vs reported: 2025 +19.9% reported vs +15.8% organic (Axonics, Silk Road and smaller deals, FX); 2026 so far FX only (Q2 +7.5% vs +7.0%). After closing, Penumbra (~$1.5B revenue, +15%) will lift reported growth by roughly 7 points for four quarters.

## 5. Valuation — three scenarios, 3-year horizon

Price $43.92 (Friday 2026-09-25 close). Year 3 = FY2029 (value at ~Sept 2029). EPS on the adjusted basis the market prices; the rule's GAAP TTM EPS is lower by amortization, restructuring and deal costs. Penumbra assumed closed in late 2026. No dividend.

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $24.5B (organic 2-3% a year; Penumbra slows) | $27.0B (organic ~4.5% in 2027, 7-7.5% in 2028-29; Penumbra ~$2.2B) | $29.0B (organic 6% in 2027, 9-10% in 2028-29 on the new launches) |
| Sustainable margin | 18.5% adj. net (EP/Watchman price and mix pressure, deal interest) | 21.5% adj. net (2025: ~22.8%; Penumbra interest offset by $500M savings) | 23.0% adj. net |
| Net debt / cash (yr 3) | ~$18B net debt (weaker FCF, tuck-ins, MiRus option) | ~$14B (≈$3.5-4B FCF a year to debt paydown; ~1.7x EBITDA) | ~$13B (paydown plus some buybacks) |
| Diluted shares (yr 3) | 1.50B (Penumbra shares, no buybacks) | 1.48B | 1.45B (buybacks resume in 2028) |
| Multiple applied | 11x adj. EPS $3.02 | 18x adj. EPS $3.92 | 22x adj. EPS $4.60 |
| Implied price | $33 | $71 | $101 |
| Total return / annualised | -24% / -8.9% | +61% / +17.1% | +130% / +32.1% |
| Probability weight | 30% | 50% | 20% |

Probability-weighted value **≈ $65.5** (+49%, ~14% a year). Key assumptions: Penumbra closes without a material divestiture; the cyber hit is a 2026 timing loss; the 2028 launch slate (FARAWAVE Ultra, FARAFLEX, ICE, PRECEDENT ICD, coronary IVL) lifts organic growth back to high single digits in the base; Watchman stays flat to low growth until a CHAMPION-AF label. Multiples: bear is today's ~13x less a leverage discount; base is below the 5-year forward-P/E median (28.5, Yahoo snapshots) and in line with a mid-growth large-cap device maker; bull needs growth back near 10%.

What does today's price already require the business to deliver?

- At $43.92 the stock trades at 12.9x consensus 2027 adj. EPS ($3.41) and 13.4x 2026 ($3.27) (third-party consensus: 2026 revenue $21.27B, +6.0%; 2027 revenue $22.25B, +4.6%, EPS +4.4%; 2027 EPS was $3.72 ninety days ago).
- Reverse-implied (my arithmetic): for an 8-10% annual return to 2029, adj. EPS must reach $4.26-4.50 if the multiple stays at 13x (9-11% a year from $3.27), $3.69-3.90 at 15x (4-6% a year), or only $3.07-3.25 at 18x (flat). FCF yield on the market cap is 5.7% (true FCF $3.63B), which at a 9% cost of equity implies ~3% perpetual growth before Penumbra.
- So the price already assumes BSX stays a low-growth device maker with a permanently low multiple. It does not require the 2025 growth rate back; it requires the growth reset to stop getting worse.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 3.1 | 5.8 | 3.1 | 9.5 | 0.41 | 7.9 | 2008-03-31 |
| EV/EBITDA | 13.9 | 29.8 | 14.1 | 43.2 | 0.12 | 35.1 | 2008-03-31 |
| P/E (trailing) | 17.8 | 68.3 | 17.9 | 117.3 | 0.14 | 58.1 | 2011-06-30 |

At the 5-year median P/S (5.8) on today's TTM revenue the price would be about $82 (+86%); at the 5-year low (3.1), about $44 (-1%). Mechanical, not a forecast.

Data caveat: the EDGAR rebuild's D&A for 2024-2025 is depreciation only (~$470M TTM vs $1,368M in the FY2025 10-K; full D&A from Q1 2026), so historical EV/EBITDA is overstated by roughly a quarter and the 0.12 percentile flatters today's reading. P/S and EV/EBIT are unaffected. Not recomputed.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.21, growth +14%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$2.10** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (2.2 today)
- **Price target where recovery is fully reflected:** trim half at **$66** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** medical devices (PODD, DXCM, BSX): a third of the basket; PODD and DXCM also share the diabetes / GLP-1 / competition narrative; same-driver holdings: PODD, DXCM
- **Research overlay (not part of the rule):** More confident if the Oct 28, 2026 report sizes the cyber loss as a one-quarter timing item with Q4 recapture, U.S. EP returns to ≥ $600M a quarter by Q1 2027, the FTC clears Penumbra without a large divestiture and the 364-day loans are termed out at reasonable coupons, and a CHAMPION-AF label filing is dated. Less confident on a fourth 2026/2027 guide cut, an FTC challenge, Watchman's H2 decline running past high single digits, or pro forma leverage above ~4x. Rule-specific: the $2.10 trigger is closer than the +47% suggests (~$2.19 ex Q1 2026 tax and investment gains), and the Q1 2027 10-Q (~early May 2027) is the most likely month for a mechanical exit even if adjusted EPS holds; growth rank 20 also means the name may not survive the October 1 re-run (positions report) and will likely leave the top 20 after Q3 (TTM growth falls to ~9% on consensus). Dated catalysts: Oct 28, 2026 Q3 results and revised 2026 outlook; Penumbra FTC decision and closing (company: second half of 2026); Arthur Butcher (MedSurg/APAC) retires Jan 1, 2027; Q4 2026 results and 2027 guidance (early February 2027 by pattern, date unconfirmed); Q1 2027 results (late April 2027, the TTM EPS roll-off); FARAWAVE Ultra launch "at scale" around mid-2027; CHAMPION-AF label and CMS coverage timing — no source found.

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #10: val 0.21, growth +14%, entry TTM EPS $2.47, trigger $2.10, trim $66 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/BSX.md) | Cause: valuation compression from a growth reset (EP share loss, Watchman slowdown, three 2026 guide cuts, cyberattack), not an earnings peak; survival PASS with a post-Penumbra leverage watch; probability-weighted ~$65.5 vs $43.92; main rule risk is the TTM GAAP EPS roll-off toward $2.10 in May 2027. Sections 1/1b unchanged; note their FCF $1.81B / P/FCF 35.2 deduct the $1.5B MiRus investment (true FCF ≈ $3.63B, P/FCF ≈ 17.6). Review deadline left at 2027-03-27 (after the Q4 2026 report) |

## 8. Research conclusion

Research view: the rule's buy is defensible — at 12.9x consensus 2027 adjusted EPS the price already discounts a low-growth device maker, earnings and margins have not peaked, and survival is not in question — but this is a slower, more levered recovery than the 47% TTM EPS gain suggests. The probability-weighted value is about $65.5 (+49%, ~14% a year over three years), close to the $66 trim level, with a real bear case near $33 if EP share loss and the Watchman slowdown persist into a 4x-levered Penumbra integration. The single most important thing to watch is U.S. EP and U.S. Watchman sales in the Q3 and Q4 2026 reports (Oct 28 and early February): if both stabilise the growth reset is over; for the rule itself, watch the TTM GAAP EPS path into the Q1 2027 10-Q, where the Q1 2026 tax gain rolls off and the $2.10 trigger could fire for accounting reasons. In the basket, BSX is the third medtech name with PODD and DXCM but its drivers (PFA competition, LAAC evidence, M&A leverage) differ from their diabetes/GLP-1 story; the shared risk is the 2026 large-cap medtech de-rating (ABT -23%, SYK -31% over the same year). It is the only name with a large pending acquisition, the most levered of the ten, and the seat most exposed to the October 1 re-run.
