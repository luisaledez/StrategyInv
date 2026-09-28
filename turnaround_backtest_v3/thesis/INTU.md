# INTU — Intuit

status: watchlist            <!-- watchlist | starter | add | exit | rejected -->  set to starter once the v3 buy is filled
review_deadline: 2027-03-27   <!-- date by which the expected evidence must have appeared -->
last_updated: 2026-09-28
strategy: turnaround v3 `both_opval` — buy #5 of 10 on the 2026-09-28 screen ([positions report](../../reports/Turnaround%20v3%20positions%20-%202026-09-28.md), [rules](../STRATEGY_both_opval.md))

## 1. Screen facts (auto-filled on 2026-09-28)

| Field | Value |
|---|---|
| RSI qualification date (first oversold month) | 2026-01-31 |
| Monthly RSI, last completed candle | 37.5 |
| Episode months / min RSI | 8 / 27.1 |
| Drawdown from trailing 5-year high | -65.8% (high 807.39 on 2025-07-30) |
| Market cap / avg daily $ volume (3m) | $73.70B / $1.27B |
| Sector / industry | Information Technology / Application Software |
| Survival gate (proxy) | PASS — cash $7.20B, debt due <1y $1.33B, FCF TTM $8.62B, 24m gap -$5.87B |
| Net debt / EBITDA, interest coverage | 0.2 / 24.5 |
| Valuation | P/E trailing 16.8, P/E forward 10.2, PEG 0.88, P/S 3.44, EV/Sales 3.5, EV/EBITDA 10.5, P/FCF 8.6 |
| EPS | TTM 16.50, forward est. 27.08; growth YoY (TTM) +20.4%, last quarter -0.7%, implied forward +64.1% |
| Revenue YoY (last quarter) | +13.7% |
| Profitable years (of reported) | 4 / 4 |

## 1b. Turnaround v3 (`both_opval`) rule data (2026-09-28 screen)

| Field | Value |
|---|---|
| Buy order / growth rank | 5 of 10 / 18 of 20 |
| TTM revenue growth | +14% (latest quarter 2026-07-31) |
| Valuation (operating multiples, 0 = cheapest ever) | **0.11** — P/S 0.08, EV/EBITDA 0.18, EV/EBIT 0.06 (P/E pct 0.02, not used) |
| Multiples today | P/S 3.6, EV/EBITDA 13.1, EV/EBIT 13.5, P/E 16.8 |
| Monthly RSI (Sept candle, incomplete) / 6-month min | 33.0 / 27.1 |
| From 5-year high | -66% |
| TTM EPS path, 6 quarters (oldest first) | 12.25, 13.67, 14.56, 15.37, 16.39, 16.46 |
| TTM EPS vs 12 months earlier | +20% |
| One-off EPS guard | passed — TTM net income / operating income 0.78 |
| Acquisition guard | passed — diluted shares -2.0% y/y |
| Net debt / EBITDA | 0.5 |

**Entry plan (rule):** 10% of the account at the 2026-09-28 close (sizing guide: 36 shares per $100k at Friday's $275.79).
Entry TTM EPS **$16.46** → guide-cut trigger **$13.99** (sold at the first month-end the point-in-time TTM EPS prints at or below it, until 2027-09-28).
Trim half at **$414** (+50%). Sell all at a month-end with monthly RSI ≥ 90. Not added to if already held.

**Base rates** (12-month forward returns of past `both_opval` top-10 picks, 2009-2025): val 0.10-0.25: n 222, mean +17%, median +16%, 66% winners, 52% beat SPY; 60%+ below 5y high: n 64, mean +56%, median +24%, 73% winners (regime-heavy: 2009, 2020). All top-10 picks: median +16%, 69% winners, 10th percentile -21%, median worst drawdown in year 1 -24%.

**Screen report's read:** Good fit; deepest-drawdown bucket has the widest spread.

- Reward case: 66% below the 5-year high, the deepest drawdown after PODD, monthly RSI 33 (min 27); 16.8x earnings at the 6-18th percentile on the three multiples; EPS up 20% and rising every quarter; net debt 0.5x EBITDA.
- Main risks under these rules: The de-rating is the AI-disruption narrative on tax and small-business software, not an earnings problem; the last quarter's EPS was flat (16.39 to 16.46), and a 15% TTM decline would need a large miss. Trigger $13.99.

## 2. Why did the stock fall?  (diagnosis)

Cause category: **valuation compression + structural deterioration (partial, unproven: DIY tax)** — the multiple fell about 70% while revenue and GAAP EPS each grew 20%, so most of the fall is the de-rating of software on AI-agent fears; but INTU fell 30-55 points more than its software and tax peers because its own outlook stepped down (FY27 revenue guide +9-10% after +14%, TurboTax +2-3% after losing price-sensitive DIY filers, customer growth 3%), and that part may be permanent.  <!-- inventory cycle | financing-sensitive demand | temporary execution | excess industry capacity | valuation compression | structural deterioration -->

Narrative (what actually happened, with dates and numbers from the filings):

- 5-year high 807.39 on 2025-07-30; price now -66%. From that month's close (785.13) P/S went from 12.2 to 3.6 (-71%) while TTM revenue per share changed +20%: the fall is all multiple (price and valuation caches, derived).
- 12-month price return -60%; TTM EPS +20% over the same span; revenue +14%.
- Revenue and EPS never missed: every FY26 quarter beat its non-GAAP EPS guide, and FY26 revenue ($21.45B, +14%) beat even the May raise. The misses were in customers and units, and in the FY27 outlook. Sources for each line are in the [research notes](../../research_notes/Turnaround%20v3%20thesis%202026-09-28/INTU.md).

| Leg | Close to close | Move | What happened |
|---|---|---|---|
| 1 | 2025-07-30 → 2025-12-31 | 807.39 → 662.42, **-18%** | Aug 22 -5.0%: Q4 FY25 beat (revenue +20%), but the [FY26 guide](https://www.sec.gov/Archives/edgar/data/896878/000089687825000031/fy25q4earningspressrelease.htm) was +12-13% revenue after +16% (Aug 11 -5.7%: no cause found). Sept-Dec range-bound; Nov 21 +4.0% on a Q1 beat. In November the IRS told states Direct File would not run in 2026, and Intuit signed a $100M+ OpenAI deal (Nov 18). |
| 2 | 2025-12-31 → 2026-02-24 | 662.42 → 358.71, **-46%** | Sector AI-agent selloff: Jan 13-14 -4.7%/-6.4% (Anthropic Claude Cowork; Wells Fargo cut to Equal Weight, $840 → $700); Jan 29 -6.6% (Microsoft/ServiceNow/SAP results); Feb 3 -10.9% (Anthropic Cowork industry plugins, a ~$285B software sell-off); Feb 17 -5.1% (new Claude model). No Intuit fundamental news. |
| 3 | 2026-02-24 → 2026-03-05 | 358.71 → 466.79, **+30%** | [Anthropic partnership](https://investors.intuit.com/news-events/press-releases/detail/1305/intuit-and-anthropic-partner-to-bring-trusted-financial-intelligence-and-custom-ai-agents-to-consumers-and-businesses) (Feb 24; +6.3% next day) and a Q2 FY26 beat (non-GAAP EPS $4.15 vs $3.63-3.68 guide, Feb 26). |
| 4 | 2026-03-05 → 2026-05-20 | 466.79 → 383.93, **-18%** | Apr 8-9 -5.1%/-7.1% on Anthropic launches (Managed Agents / Claude Mythos; sources differ on which drove which day); Apr 23 -6.2% on ServiceNow/IBM results. Mar 20: the Fifth Circuit vacated the FTC's free-filing order (a positive). |
| 5 | 2026-05-20 → 2026-06-25 | 383.93 → 255.07, **-34%** | **May 21 -20.0%**, the company-specific break: [Q3 FY26](https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000024/fy26q3earningspressrelease.htm) revenue +10%, TurboTax guide cut to $5.277-5.282B (from $5.305-5.330B), a 17% workforce reduction, and management saying it "lost on price" with DIY filers under $50k. Jun 2 -8.9%: Goldman Sachs downgraded to Sell (lower-priced GenAI tax competition). Episode low close $255.07. |
| 6 | 2026-06-25 → 2026-08-24 | 255.07 → 369.92, **+45%** | Sector rotation back into software (CRM +72%, WDAY +74%, NOW +65% from Jun 25 to Aug 31). A securities class action was filed Jul 10; Stifel cut to Hold ($275) on Jul 13. |
| 7 | 2026-08-24 → 2026-09-25 | 369.92 → 275.79, **-25%** | [FY27 guide](https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000029/fy26q4earningspressrelease.htm) (Aug 25): revenue +9-10% (midpoint $23.40B vs ~$23.74B consensus), TurboTax +2-3%, Mailchimp flat to -1%, SBC now inside non-GAAP. The stock opened -9.5% on Aug 26 and closed -3.2%. The Sept 17 Investor Day reaffirmed the guide with no upside. In September software sold off again (ADBE -20%, ADSK -19%, HRB -18%, INTU -23%, Aug 31 to Sep 25). |

- Relative to peers from INTU's high to Friday (local caches): INTU -66%, ADBE -35%, ADSK -32%, NOW -31%, HRB -23%, WDAY -20%, CRM -12%, SPY +20%. Roughly half of the fall is the sector; the rest is Intuit-specific.

Was the prior high an exceptional earnings peak or an unsustainable multiple? (yes/no, evidence)

- **Not an earnings peak; the multiple was unsustainable.** Margins and EPS have kept rising since the high: GAAP operating margin 26.1% in FY25, 27.4% in FY26, and about 31.8% at the FY27 guide midpoint; GAAP EPS $13.67 → $16.46 → guide $20.12-20.36. At the July 2025 high the stock traded at 64x trailing GAAP EPS, 12.2x sales and 39x FY25 non-GAAP EPS ($20.15). Those prices assumed mid-teens growth for years, and the guide is now 9-10%.
- Caveat: 64x was close to INTU's own 5-year median (58.9x). The 2021-2025 multiple regime as a whole is what re-based, not a one-off spike, so a return to the 5-year median is not a sensible anchor.

## 3. Survival assessment  (gate — must pass before any upside is assigned)

| Item | Amount | Source |
|---|---|---|
| Cash and equivalents | $7.20B cash, equivalents and investments, unrestricted, ~93% in the U.S. Debt principal $7.72B (senior notes $6.75B + $0.97B non-recourse secured facilities that fund small-business loans), so net debt is ≈ $0.5B excluding $0.75B of leases (the fundamentals cache's $1.22B includes leases) | [FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000037/intu-20260731.htm), liquidity and Note 7 |
| Realistically available credit (undrawn revolver, covenants) | $2.2B unsecured revolver (signed 2026-01-09, expires 2031-01-09), undrawn, with a $4B accordion; one covenant, gross debt / EBITDA ≤ 4.0x (about 1.1x today on $7.1B TTM EBITDA; compliant). $2.2B commercial paper program, nothing outstanding. Secured SPV facilities: $1.2B committed, $0.97B drawn | 10-K |
| Debt maturities next 24 months | $1.25B in FY27: $750M 5.25% notes due Sep 2026, **already repaid in August 2026** from the June 2026 $1.75B issue, and $500M 1.35% notes due Jul 2027 (the company intends to use the rest of the June proceeds). Plus $400M in FY28, secured SPV facilities that are non-recourse. The next unsecured maturity after that is $750M in Sep 2028 | 10-K, Note 7 |
| Cash consumption if weak conditions persist 24 months | none. FCF TTM $8.62B is flattered by only $281M of cash taxes (OBBBA R&D expensing; FY25 $1.41B). The company expects about $2B of cash taxes in FY27, so normalised FCF is ≈ $6.9B, far above ~$1.5B a year of dividends and the $500M of unsecured maturities left in the next 12 months | 10-K cash flow and liquidity |
| Interest, maintenance capex, leases, other fixed obligations | Next 12 months: interest and fees $351M, operating leases $112M, purchase obligations $1.16B (mainly cloud), deferred comp $308M; capex $221M in FY26; dividend $1.38/quarter (≈ $1.5B a year). Interest coverage 25x | 10-K contractual obligations table |
| Can recovery happen without a large equity raise? | yes | net debt ≈ 0.1x EBITDA, $7.9B of buyback authorization left, investment-grade notes issued at 4.95-5.50% in June 2026 |

Gate verdict: PASS — reasoning:

- Profitable in 4 of 4 reported years and FCF-positive; normalised FCF of ~$6.9B covers every fixed claim several times over. The only near-term maturity is $500M in July 2027, and there is $2.2B of undrawn revolver. Survival is not the question for this name.
- Watch items that are not survival issues: buybacks ($5.5B in FY26) now run above normalised FCF after dividends; the two securities class actions and the Ontario class action have no loss estimate.

## 4. Recovery thesis  (testable statement)

> The business weakened because of a growth step-down among price-sensitive customers: TurboTax lost DIY filers under $50k on price in the 2026 season (federal units -2% to 39.0M, TurboTax guided +2-3% for FY27), new-customer growth in QuickBooks/Online Ecosystem slowed to 3%, and Mailchimp is shrinking. At the same time the whole software group de-rated on AI-agent disruption fears. Recovery requires evidence that the lower entry prices (QuickBooks Free/Lite, Credit Karma Tax, lower DIY ARPC) win back units and customers without breaking the FY27 guide (revenue +9-10%, GAAP EPS $20.12-20.36), and that AI assistants (Intuit's own agents and the ChatGPT/Claude integrations) are channels to Intuit rather than substitutes for paid filing.
> We expect to observe Q1 and Q2 FY27 revenue at or above guidance (Q1 $4.294-4.313B, +11%), GBS growth of at least 13%, Online Ecosystem customer growth above 3%, and FY27 guidance held or raised at the February 2027 print, all within the next 2–4 quarters. The decisive read on TurboTax units and share for the 2027 season comes with Q3 FY27 (about late May 2027, after the review deadline).

Indicators (one leading, one financial confirmation, optionally one more):

| Indicator | Type | Current reading | What "confirmed" looks like | What "broken" looks like |
|---|---|---|---|---|
| New-customer growth: Online Ecosystem paying customers y/y (reported with Q4 each year; management comments quarterly) and QuickBooks Free/Lite conversion | leading | +3% at 2026-07-31 (about +5% a year earlier per the call); ARPC +15%; Free/Lite >20,000 customers in its first month | customer growth back to 4-5% while Online Ecosystem ARPC still grows ≥10%; GBS at or above the +13-14% guide | customer count flat or falling, or ARPC growth fading below ~10% as the price cuts spread; GBS below 13% |
| TurboTax federal units and TurboTax revenue, 2027 season (IRS weekly filing statistics Feb-Apr 2027; Intuit units with Q3 FY27, ~late May 2027) | leading (tax) | FY26: 39.0M units (-2%; online 34.9M -2%, desktop 4.1M -7%); TurboTax revenue $5.30B (+7%); TurboTax Live 53% of TurboTax revenue | units flat or up, with TurboTax revenue at or above the $5.377-5.453B guide | units down again **and** TurboTax revenue below guide: the price cuts bought nothing |
| TTM EPS vs entry $16.46 / trigger $13.99 | financial confirmation | $16.46 (+20% y/y); includes ~$0.80 of restructuring drag. The Q1 FY27 GAAP guide of $1.71-1.75 (vs $1.59) implies ~$16.6 at the next print | flat or rising at each month-end; FY27 GAAP EPS guide ($20.12-20.36) kept | prints at or below $13.99 at a month-end before 2027-09-28 (rule exit). That would need Q3 FY27 GAAP EPS about $2.5 below last year's $11.09, i.e. a failed tax season |
| TTM revenue growth (entry +14%) | organic screen | +14%; Q4 FY26 +14% | each quarter at or above guidance; TTM drifts to ~9-10% as guided and no quarter falls below its year-ago quarter | a quarter below its year-ago quarter (fails the organic screen) or an FY27 revenue guide cut below +9% |

Headline adjustments to remember (one-offs, timing items, safe-harbor style revenue, refunds, working-capital releases):

- **Restructuring:** $293M in Q4 FY26 (≈ $0.80/share after tax) depresses the TTM base; only ~$22M expected in FY27, so FY27 GAAP growth (+22-24%) is flattered by the drop-out.
- **Investment gains:** $174M net gains on long-term investments in FY26 (≈ $0.48/share) inflate the base. Net of restructuring, the clean FY26 GAAP EPS is ≈ $16.8.
- **Amortization** of acquired intangibles (Credit Karma, Mailchimp) is $659M a year (≈ $1.81/share after tax). It is in GAAP EPS and excluded from non-GAAP.
- **Share-based comp** is $2.06B (9.6% of revenue). From FY27 it is included in non-GAAP: the FY26 non-GAAP EPS of $24.27 becomes ≈ $18.6 on the new basis (implied by the +23-24% guide). Consensus EPS mixes both bases (Yahoo FY27 $23.77, high $28.88). The screen's "forward EPS $27.08" is Yahoo's FY2028 average, so the 10.2x forward P/E in section 1 is on FY28, mixed basis.
- **Tax:** FY26 effective rate 24.1% (FY25 20.0%). Cash taxes were only $281M (OBBBA R&D expensing) and ~$2B is expected in FY27, so FY26 FCF ($8.62B) overstates the run-rate by ~$1.7B.
- **Seasonality:** Q3 (April) carries ~40% of revenue and ~67% of GAAP EPS ($11.09 of $16.46). The TTM figure mostly moves at the May print; the rule's trigger is effectively a test of the 2027 tax season.
- **Acquisitions:** none material in FY26 (one $184M deal in FY25); diluted shares -2%. **Reporting changes:** Mailchimp becomes its own segment in FY27; the $5.8B early-refund credit line (Jan-Feb 2026) is working capital, not earnings.

## 5. Valuation — three scenarios, 3-year horizon

Year 3 = FY2029 (ending July 2029). EPS on the new non-GAAP basis (SBC included, acquired-intangible amortization and one-offs excluded) = revenue × operating margin × (1 − 24% tax) / diluted shares; net interest is ignored (about neutral). GAAP EPS would be about $2 lower (acquired-intangible amortization). Returns are from $275.79 and include ~$17 of dividends ($1.38 a quarter now, +10% a year assumed).

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue (yr 3) | $24.5B (+4.5% a year from FY26 $21.45B: FY27 guide missed, TurboTax and Mailchimp shrink, GBS ~8%) | $27.8B (+9% a year: FY27 guide midpoint $23.4B, then ~9% a year, in line with FY28 consensus $25.6B) | $29.5B (+11% a year: top of the FY27 guide, then ~12% as mid-market, money and Credit Karma compound and TurboTax units return) |
| Sustainable margin | 31% operating (price cuts and AI compute absorb the restructuring savings) | 36% (FY26 32.1% on the new basis, FY27 guide ~34.6%, SBC trending toward 8% of revenue) | 38% |
| Net debt / cash (yr 3) | ≈ $1.5-2B net debt (buybacks continue on lower FCF) | ≈ $0.5-1B net debt (FCF returned; notes refinanced) | ≈ $0.5B net debt |
| Diluted shares (yr 3) | 250M | 245M (~3% net reduction a year from ~270M) | 250M (higher price retires fewer shares) |
| Multiple applied | 9x EPS $23.1 (ex-growth tax franchise in secular decline; below the 2008 low of 15.7x GAAP) | 14x EPS $31.0 (≈ 15x GAAP, still below the 5-year low of 15.9x) | 20x EPS $34.1 (≈ 21x GAAP, about a third of the 5-year median GAAP P/E of 58.9x) |
| Implied price | $208 | $435 | $682 |
| Total return / annualised | -19% / -6.6% | +64% / +17.9% | +153% / +36.3% |
| Probability weight | 35% | 45% | 20% |

Probability-weighted value **≈ $405** (+47% on price, ≈ $422 or +53% with dividends, ~15% a year). The spread is wide ($208-682) and the bear case carries a real 35%.

Key assumptions: (1) TurboTax is not replaced outright within three years: AI assistants route filers to paid filing (the OpenAI and Anthropic integrations), and the 2027-2029 IRS filing seasons keep Direct File off. The bear case assumes that fails for DIY, which is 12% of the TurboTax TAM per management. (2) GBS (QuickBooks Online, payments, payroll, mid-market; $12.9B, segment margin 77%) keeps compounding at ≥10%. It drives the base case more than tax does. (3) Buybacks continue at roughly FCF less dividends. (4) Credit Karma ($2.6B, +20%) is cyclical; a credit downturn is part of the bear case.

What does today's price already require the business to deliver?

- At $275.79 (market cap $73.7B on 267.2M shares at 2026-08-31, EV ≈ $74B), INTU trades at **13.6x the FY27 GAAP EPS guide midpoint ($20.24)**, 12.0x the new-basis non-GAAP midpoint ($23.00) and 16.8x trailing GAAP. Normalised FCF (≈ $6.9B after ~$2B of cash taxes) is a 9.4% yield, or 6.6% after treating SBC ($2.02B guided) as a cash cost.
- **Consensus (third-party, [Yahoo Finance](https://finance.yahoo.com/quote/INTU/analysis/), viewed 2026-09-28):** FY27 revenue $23.41B (+9.1%, 28 analysts), FY28 $25.57B (+9.2%); EPS FY27 $23.77, FY28 $27.08 (mixed SBC basis; the FY27 figure was $27.25 thirty days ago before the definition change). [StockAnalysis](https://stockanalysis.com/stocks/intu/forecast/): 34 analysts, average target $405.6 (range $290-732).
- **Reverse-implied growth:** with a 10% discount rate and dividends growing 10%, today's price equals about **8% EPS growth a year for five years** from the $23.00 FY27 base, then a 12x forward exit multiple; it equals 3% a year with a 15x exit and 12% with a 10x exit. As a perpetuity, the ~8.4% SBC-inclusive earnings yield implies about 0.6-1.6% permanent growth at a 9-10% cost of equity. In short, the price requires little more than delivering FY27 and then growing EPS in the high single digits, below management's "high-teens" ambition, **unless the multiple keeps compressing toward 10x**. That is the market's actual bet: a tax franchise in decline.

Own-history anchors (valuation cache, monthly from SEC filings):

| Multiple | Today | 5y median | 5y low | 5y high | Percentile (full history) | At 5y-high month | History from |
|---|---|---|---|---|---|---|---|
| P/S | 3.6 | 10.2 | 3.5 | 17.7 | 0.08 | 12.2 | 2008-10-31 |
| EV/EBITDA | 13.1 | 45.6 | 12.6 | 66.8 | 0.18 | 48.4 | 2008-10-31 |
| P/E (trailing) | 16.8 | 58.9 | 15.9 | 85.5 | 0.02 | 64.1 | 2008-10-31 |

At the 5-year median P/S (10.2) on today's TTM revenue the price would be about $786 (+185%); at the 5-year low (3.5), about $270 (-2%). Mechanical, not a forecast.

## 6. Entry / exit policy

- **Starter condition:** met by rule — `both_opval` top 10 on the 2026-09-28 screen (valuation 0.11, growth +14%); buy at the close of the first trading day after the snapshot
- **Add condition:** none — the v3 rule never adds to a held name
- **Thesis-breaking evidence (exit or reduce):** point-in-time TTM EPS at or below **$13.99** at any month-end before 2027-09-28 (guide-cut proxy, sell all); a filing re-basing of 30%+ while off the list (sell)
- **Financing-risk trigger:** n/a under the rules (no price stop); watch net debt / EBITDA (0.5 today)
- **Price target where recovery is fully reflected:** trim half at **$414** (+50%); sell the rest at a month-end with monthly RSI ≥ 90; above +100% it can be sold to fund a new top-10 name when cash is short
- **Position size:** 10% of the portfolio (rule weight). Stress loss reference: 10th-percentile 12-month outcome of past top-10 picks -21%, median worst year-1 drawdown -24% → about 2.1-2.4% of the portfolio at risk at this weight
- **Correlated exposure:** de-rated software (APPF, INTU, DT, NOW, VEEV): half the basket, one shared driver (AI-disruption / seat-pricing narrative and sector multiple); same-driver holdings: APPF, DT, NOW, VEEV
- **Research overlay (not part of the rule):**
  - *More confident if* Q1 FY27 meets the +11% revenue guide with GBS ≥13%; management reports QuickBooks Free/Lite converting and customer growth above 3%; FY27 guidance is held or raised in February; early 2027-season IRS filing counts are flat or up; buybacks keep running near $280 ($7.9B authorization ≈ 11% of the market cap).
  - *Less confident if* the FY27 guide is cut in November or February; TurboTax units fall again while DIY ARPC is also cut; a large AI platform launches free end-to-end federal filing; Credit Karma slows with the credit cycle; Mailchimp declines faster than -1%; Direct File or an expanded Free File is revived.
  - *Dated catalysts:*
    - Q1 FY27 results in late November 2026 (date not yet announced; last year's was Nov 20).
    - Restructuring substantially complete by Q1 FY27; annual meeting around January 2027.
    - IRS filing season opens in late January 2027 (2026 opened Jan 26), with weekly IRS filing statistics February-April.
    - Q2 FY27 results in late February 2027 (not announced; last year's was Feb 26). This is the last print before the review deadline.
    - Tax deadline April 15, 2027; Q3 FY27 results in late May 2027 (the tax-season read); $500M notes due July 2027.
    - Q4/FY28 guidance in late August 2027; next Investor Day expected around September 2027.
    - Litigation: lead-plaintiff appointment in the N.D. Cal. securities cases (deadline was 2026-09-08); the court's ruling on Intuit's unopposed motion (filed 2026-08-31) to dismiss the remaining FTC suit as moot; Intuit's appeal of the Ontario class certification (2026-07-24).

## 7. Log

| Date | Event / data point | Effect on thesis |
|---|---|---|
| 2026-09-28 | Turnaround v3 `both_opval` top 10, buy #5: val 0.11, growth +14%, entry TTM EPS $16.46, trigger $13.99, trim $414 | Buy signal at today's close |
| 2026-09-28 | Research pass: sections 2-5 filled (sources in research_notes/Turnaround v3 thesis 2026-09-28/INTU.md) | Cause: valuation compression plus a partial DIY-tax/new-customer slowdown. Survival confirmed. Value ≈ $405 (35/45/20); trigger distant (FY27 GAAP EPS guide $20.12-20.36). review_deadline kept: 2027-03-27 already follows the second report from today (Q2 FY27, ~late Feb 2027), though the tax-season read (late May 2027) comes after it. Sections 1/1b unchanged (section 1's forward EPS $27.08 is Yahoo's FY28 mixed-basis average; see section 4) |

## 8. Research conclusion

The research supports holding the rule's buy, with a neutral-to-positive tilt. Intuit's earnings are intact: FY26 revenue +14%, GAAP EPS +20%, FY27 guided at +22-24% GAAP EPS, and the guide-cut trigger ($13.99) would need a failed tax season. But the 66% fall is not only sector noise: the May 2026 TurboTax price and share loss and the FY27 step-down to 9-10% growth are real, and the market is pricing the DIY tax franchise as if it is in decline. The probability-weighted three-year value is about $405 (≈ $422 with dividends) against $275.79, with a wide $208-682 range. The single most important thing to watch is whether the lower 2027 DIY pricing brings back TurboTax units without taking TurboTax revenue below the +2-3% guide. That read arrives with Q3 FY27 in late May 2027; before then, the November and February prints must hold the FY27 guide. In the basket INTU shares the AI-disruption de-rating driver with APPF, DT, NOW and VEEV and fell with them in September (INTU -23%, NOW -8%), so sector moves will hit all five together. Its guide-cut trigger is the most remote of the software group, unlike DT and NOW, whose TTM EPS is drifting toward their triggers. Its own catalyst, the April-May tax season, is independent of the medtech (PODD, DXCM, BSX), KNSL and OLLI drivers.
