# Turnaround v3 (`both_opval`) positions to open on September 28, 2026

*Research tooling output, not investment advice. Screen run on 2026-09-28 at 08:05 EDT, before the open, with the rules of backtest v3's `both_opval` strategy (`turnaround_backtest_v3/STRATEGY_both_opval.md`). Prices: Yahoo cache through the Friday, September 25 close (no bars since). Fundamentals: SEC EDGAR point-in-time tables, latest filings as of September 25; latest quarter June 30, 2026 (July quarter for VEEV, ADSK, INTU; August 1 for OLLI; August 31 for PAYX). Row-level data: `turnaround_backtest_v3/output/live_both_opval_2026-09-28.csv` / `.json`, produced by `turnaround_backtest_v3/live_v3.py`.*

## Rules applied

The quarterly snapshot of backtest v3, evaluated today instead of on October 1:

1. **Price screen**: monthly Wilder RSI(14) below 42 in any of the last 6 monthly candles, at least 5 years of history, 3-month average dollar volume of $5M or more, market cap of $1B or more. Universe: today's S&P 500 + S&P 400 (899 tickers with filings).
2. **Profitable now and in the past**: TTM EPS and net income above zero, at most one losing year among the TTM readings one, two and three years back.
3. **Organic growth**: TTM revenue growth positive and under 100%, no quarter-to-quarter jump of the TTM figure above 60% in the last eight quarters, latest quarter not below its year-ago quarter.
4. **One-off EPS guard** (new in v3): reject when TTM net income exceeds TTM operating income, or one quarter lifted TTM net income by more than 50% while operating income rose less than 25% (without an operating-income tag, a >50% one-quarter jump in TTM EPS).
5. **Acquisition guard** (new in v3): reject when diluted shares are up more than 15% year over year, or growth of 15% or more is at least three times and ten points above the growth a year earlier (recoveries from a decline exempt).
6. **Top 20 by TTM revenue growth**, then **top 10 by valuation on operating multiples** (new in v3): mean percentile of today's trailing P/S, EV/EBITDA and EV/EBIT within the company's own monthly history rebuilt from filings (0 = cheapest ever). P/E is not used.

Portfolio rules, unchanged from v2's re-screen + guide-cut proxy scenario: at most 10% of the portfolio per stock, bought at the close of the first trading day after the snapshot; names that leave the list are kept; trim half at +50%; sell all at a month-end with monthly RSI at or above 90; a winner above +100% is sold to fund a new top-10 name when cash is short; a holding whose filings re-base by 30% or more is sold unless still on the list; **guidance-cut proxy: sold at the month-end when TTM EPS is 15% or more below its level at entry, within the first 12 months**; yearly withdrawals of 5 to 10%. No position cap, no S&P parking, no price stop.

## Funnel today

| Step | Names |
|---|---|
| RSI(14, monthly) < 42 within the last 6 months | 239 |
| ... liquid and with 5 years of history | 233 |
| ... market cap ≥ $1B | 230 |
| ... profitable now and in the past | 193 |
| ... organic growth | 139 |
| ... one-off EPS guard (18 struck) and acquisition guard (4 struck) | 117 |
| Top 20 by revenue growth → top 10 by operating-multiple valuation | 20 → 10 |

The guards strike nine names that were in the reference (v2-rule) top 20, six of which were in its top 10:

| Removed | Growth | Guard | Reason |
|---|---|---|---|
| CELH | +83% | acquisition | diluted shares +55% y/y (Alani Nu) |
| AMCR | +57% | acquisition | shares +46% y/y (Berry Global) |
| DKS | +54% | acquisition | growth 54% vs 3% a year earlier (Foot Locker) |
| BRO | +34% | acquisition | shares +33% y/y (Accession equity raise) |
| DUOL | +29% | one-off | net income 2.61x operating income (deferred-tax release) |
| CSGP | +22% | one-off | TTM net income jumped 3.57x in one quarter (near-zero base) |
| GEN | +20% | one-off | TTM net income jumped 1.61x in one quarter |
| FIS | +18% | one-off | net income 1.76x operating income (Worldpay stake gain) |
| PINS | +17% | one-off | net income 1.11x operating income |

## The top 20

Growth = TTM revenue growth year over year. Val = mean percentile of P/S, EV/EBITDA and EV/EBIT versus own history (lower is cheaper); the three components follow. RSI = monthly RSI(14) on the current (incomplete) September candle; min = lowest monthly RSI in the 6-month window. From 5y high = distance of Friday's close from the 5-year high. EPS Δ 1y = TTM EPS versus 12 months earlier. ND/EBITDA = net debt over TTM EBITDA.

| Growth rank | Ticker | Company | Sector | Growth | Val | P/S pct | EV/EBITDA pct | EV/EBIT pct | P/S | EV/EBITDA | P/E | RSI (min) | From 5y high | Mkt cap $B | EPS Δ 1y | ND/EBITDA | Top 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ELF | e.l.f. Beauty | Cons. Staples | +31% | 0.45 | 0.42 | 0.49 | 0.43 | 3.4 | 30 | 102 | 51 (40) | -54% | 6.1 | -42% | 2.2 | |
| 2 | PODD | Insulet | Health Care | +29% | **0.00** | 0.00 | 0.00 | 0.00 | 3.1 | 16.3 | 25.5 | 35 (34) | -61% | 9.6 | +62% | 0.7 | **1** |
| 3 | AJG | Arthur J. Gallagher | Financials | +26% | 0.71 | 0.71 | 0.72 | n/a | 3.8 | 25 | 38 | 45 (37) | -34% | 60.1 | -9% | 4.2 | |
| 4 | FICO | Fair Isaac | Info. Tech. | +24% | 0.45 | 0.63 | 0.37 | 0.35 | 8.5 | 20.6 | 25.0 | 37 (37) | -64% | 20.4 | +35% | 4.3 | |
| 5 | NOW | ServiceNow | Info. Tech. | +22% | 0.15 | 0.16 | 0.16 | 0.12 | 9.6 | 64 | 85 | 48 (30) | -42% | 141.6 | +1% | 1.3 | **7** |
| 6 | ISRG | Intuitive Surgical | Health Care | +21% | 0.51 | 0.50 | n/a | 0.51 | 13.2 | n/a | 46 | 45 (37) | -34% | 145.8 | +22% | n/a | |
| 7 | APPF | AppFolio | Info. Tech. | +21% | 0.09 | 0.14 | 0.05 | 0.06 | 7.0 | 35 | 47 | 50 (39) | -36% | 7.3 | -21% | net cash | **3** |
| 8 | ADSK | Autodesk | Info. Tech. | +18% | 0.28 | 0.44 | 0.24 | 0.15 | 5.7 | 19.6 | 27 | 41 (33) | -37% | 44.5 | +61% | net cash | |
| 9 | DT | Dynatrace | Info. Tech. | +18% | 0.14 | 0.13 | 0.14 | 0.14 | 8.4 | 60 | 116 | 63 (36) | -26% | 17.6 | -69% | net cash | **6** |
| 10 | CXT | Crane NXT | Info. Tech. | +17% | 0.59 | 0.55 | 0.51 | 0.71 | 1.5 | 10.5 | 19.7 | 47 (39) | -31% | 2.8 | -7% | 3.2 | |
| 11 | VEEV | Veeva Systems | Health Care | +17% | 0.17 | 0.28 | n/a | 0.06 | 13.5 | n/a | 46 | 61 (35) | -14% | 46.7 | +26% | net cash | **9** |
| 12 | VVV | Valvoline | Cons. Disc. | +16% | 0.56 | 0.33 | n/a | 0.78 | 1.9 | n/a | 36 | 42 (42) | -39% | 3.7 | -63% | n/a | |
| 13 | NFLX | Netflix | Comm. Services | +16% | 0.30 | 0.52 | 0.20 | 0.18 | 6.3 | 21 | 22 | 42 (41) | -47% | 305.4 | +36% | 0.4 | |
| 14 | KNSL | Kinsale Capital | Financials | +16% | **0.01** | 0.01 | n/a | n/a | 3.8 | n/a | 13.4 | 43 (38) | -40% | 7.6 | +29% | n/a | **2** |
| 15 | DXCM | Dexcom | Health Care | +16% | 0.15 | 0.22 | 0.12 | 0.11 | 6.9 | 23.6 | 34 | 53 (40) | -47% | 34.2 | +78% | net cash | **8** |
| 16 | CVLT | CommVault | Info. Tech. | +16% | 0.64 | 0.73 | 0.56 | 0.62 | 5.2 | 64 | 93 | 55 (42) | -26% | 6.4 | -13% | net cash | |
| 17 | OLLI | Ollie's Bargain Outlet | Cons. Disc. | +14% | 0.10 | 0.15 | 0.08 | 0.09 | 1.8 | 13.0 | 18.8 | 44 (36) | -40% | 5.2 | +30% | net cash | **4** |
| 18 | INTU | Intuit | Info. Tech. | +14% | 0.11 | 0.08 | 0.18 | 0.06 | 3.6 | 13.1 | 16.8 | 33 (27) | -66% | 76.5 | +20% | 0.5 | **5** |
| 19 | PAYX | Paychex | Industrials | +14% | 0.30 | 0.23 | 0.34 | 0.31 | 5.7 | 14.6 | 20.1 | 42 (31) | -37% | 36.3 | +10% | 1.3 | |
| 20 | BSX | Boston Scientific | Health Care | +13% | 0.21 | 0.41 | 0.12 | 0.10 | 3.1 | 13.9 | 17.8 | 28 (24) | -59% | 65.2 | +47% | 2.2 | **10** |

## Positions to open today

By the rule: every top-10 name, 10% of the account each, bought at today's close, in valuation-rank order. Share counts are for a $100,000 account at Friday's close and are only a sizing guide; the rule's fills are today's closing prices. The guide-cut trigger is 85% of the TTM EPS at entry: if the point-in-time TTM EPS prints at or below it at any month-end in the next 12 months, the position is sold. Trim = the price at which half is sold (+50% over cost).

| Buy order | Ticker | Weight | $ per $100k | Shares at Fri close | Fri close | Val | Entry TTM EPS | Guide-cut trigger EPS | Trim price |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PODD | 10% | $10,000 | 73 | $136.13 | 0.000 | $5.33 | $4.53 | $204 |
| 2 | KNSL | 10% | $10,000 | 30 | $330.49 | 0.008 | $24.64 | $20.94 | $496 |
| 3 | APPF | 10% | $10,000 | 48 | $204.22 | 0.085 | $4.39 | $3.73 | $306 |
| 4 | OLLI | 10% | $10,000 | 118 | $84.25 | 0.105 | $4.47 | $3.80 | $126 |
| 5 | INTU | 10% | $10,000 | 36 | $275.79 | 0.106 | $16.46 | $13.99 | $414 |
| 6 | DT | 10% | $10,000 | 172 | $57.95 | 0.140 | $0.50 | $0.43 | $87 |
| 7 | NOW | 10% | $10,000 | 73 | $135.62 | 0.146 | $1.60 | $1.36 | $203 |
| 8 | DXCM | 10% | $10,000 | 115 | $86.62 | 0.151 | $2.53 | $2.15 | $130 |
| 9 | VEEV | 10% | $10,000 | 35 | $280.68 | 0.167 | $6.10 | $5.19 | $421 |
| 10 | BSX | 10% | $10,000 | 227 | $43.92 | 0.212 | $2.47 | $2.10 | $66 |

Fully invested, no cash. Mix: five software names (APPF, INTU, DT, NOW, VEEV), three medical-device names (PODD, DXCM, BSX), one specialty insurer (KNSL), one discount retailer (OLLI). Half the book is de-rated software and a third is medtech, so the basket is more correlated than the base rates below assume.

## Name by name

EPS path = point-in-time TTM EPS over the last six quarters, oldest first. Base rates are the 12-month forward returns of past `both_opval` top-10 picks in the same valuation and drawdown buckets (next section).

| # | Ticker | EPS path (6 quarters) | Reward case | Main risks under these rules | Verdict |
|---|---|---|---|---|---|
| 1 | PODD | 5.55, 3.28, 3.43, 3.48, 4.28, 5.33 | Cheapest ever on all three operating multiples after a 61% fall; TTM EPS up 62% and rising four quarters running; net debt 0.7x EBITDA. The repository's Sept 27 Dexcom-versus-Insulet comparison weights a $90-260 scenario range at 30/50/20. | Late-October print is the first test of the mid-teens US guide; consensus still falling, short interest rising; two Class I pod corrections in 2026; three tubeless competitors entering over the next nine months. Guide-cut trigger $4.53 is 15% below a still-rising figure, so the proxy needs a real miss. | Cleanest fit; deepest-and-cheapest bucket. |
| 2 | KNSL | 17.37, 19.16, 20.35, 21.65, 22.70, 24.64 | P/S at the cheapest 1% of its history, P/E 13.4, TTM EPS up every quarter for six (+29%), 40% below the 5-year high. Held in the running v3 portfolio since April 2026 (+8%). | The valuation percentile rests on one multiple: the filings carry no EBITDA or operating-income tag for an insurer, so EV/EBITDA and EV/EBIT are missing and the one-off guard could only test the EPS jump. Specialty-insurance pricing is cyclical and the growth (16%) is the slowest of its own history. | Solid; single-multiple valuation is the caveat. |
| 3 | APPF | 5.36, 5.54, 5.57, 3.88, 4.20, 4.39 | EV/EBITDA and EV/EBIT at the cheapest 5-6% of its history, net cash, 21% growth; TTM EPS rising again for two quarters. In the running portfolio since July 2026 at $164.82 (+42% to August). | The -21% EPS change is the tax item that left the trailing year in Q4 2025; the $4.39 entry base is clean, so the trigger ($3.73) needs an operating miss. Monthly RSI already back at 50; P/S 7 in a sector being re-rated. | Fair. |
| 4 | OLLI | 3.25, 3.45, 3.61, 3.89, 4.04, 4.47 | Steadiest fundamentals on the list: TTM EPS up every quarter (+30%), net cash, 14% growth, 18.8x earnings at the 10th percentile of its history, 40% below the high. | One of the slowest growers in the top 20 (growth rank 17); a consumer slowdown would show in comparable sales before EPS. Trigger $3.80. | Clean; low variance. |
| 5 | INTU | 12.25, 13.67, 14.56, 15.37, 16.39, 16.46 | 66% below the 5-year high, the deepest drawdown after PODD, monthly RSI 33 (min 27); 16.8x earnings at the 6-18th percentile on the three multiples; EPS up 20% and rising every quarter; net debt 0.5x EBITDA. | The de-rating is the AI-disruption narrative on tax and small-business software, not an earnings problem; the last quarter's EPS was flat (16.39 to 16.46), and a 15% TTM decline would need a large miss. Trigger $13.99. | Good fit; deepest-drawdown bucket has the widest spread. |
| 6 | DT | 1.59, 1.62, 1.67, 0.60, 0.54, 0.50 | 18% growth at the 13-14th percentile of all three multiples; net cash of about 4x EBITDA. Bought by v3 in the backtest's last window (+48%). | **Least distressed and highest proxy-exit risk.** Monthly RSI 63 and only 26% below the high (qualified on the March-April dip). The drop from 1.67 to 0.60 four quarters ago is a non-operating item leaving the trailing year, so the $0.50 base is clean, but TTM EPS has drifted down 10% and 7% in the last two quarters; two more such quarters reach the $0.43 trigger without any operating miss. P/E 116, P/S 8.4. | Bought by the rule; likeliest mechanical exit of the ten. |
| 7 | NOW | 1.47, 1.59, 1.65, 1.67, 1.68, 1.60 | 22% growth at the 12-16th percentile; 42% below the high. New to the v3 portfolio (the v2 portfolio holds it from April 2026). | TTM EPS slipped 1.68 to 1.60 last quarter; the trigger ($1.36) is one and a half more such quarters away. P/S 9.6 and EV/EBITDA 64 are cheap only against its own past; seat-based software under AI pressure. | Fair; watch the EPS base. |
| 8 | DXCM | 1.33, 1.42, 1.80, 2.09, 2.33, 2.53 | TTM EPS up 78% and rising every quarter, net cash, 16% growth, 47% below the high at the 11-22nd percentile. In the running portfolio since October 2025 at $66.08 (+38%). The repository's Sept 27 deep dive weights a $55-135 scenario range at 25/50/25 and finds execution risk down after three beat-and-raise quarters. | Management-flagged H2 headwinds (FX, Ireland start-up), Abbott competition, pleading-stage litigation. Monthly RSI 53 already, so the entry is not at the low. Trigger $2.15. | Good; the higher-confidence half of the PODD/DXCM pair. |
| 9 | VEEV | 4.71, 4.86, 5.13, 5.44, 5.64, 6.10 | EPS up every quarter (+26%), net cash, 17% growth, EV/EBIT at the 6th percentile. In the running portfolio since April 2026 at $172.74 (+65%, trimmed). | Least distressed name after DT: 14% below its 5-year high, monthly RSI 61; the P/S percentile (0.28) is the honest one and the 0.17 mean is pulled down by EV/EBIT. No EBITDA tag, so two multiples only. Trigger $5.19. | Low risk, smallest valuation edge; already a winner in the backtest. |
| 10 | BSX | 1.37, 1.68, 1.87, 1.94, 2.39, 2.47 | Most oversold name on the list (monthly RSI 28, min 24), 59% below the 5-year high; EV/EBITDA and EV/EBIT at the 10-12th percentile; TTM EPS up 47% and rising every quarter. | Net debt 2.2x EBITDA, the highest of the ten; the P/S percentile (0.41) is not cheap, and growth (13.5%) is exactly rank 20, so this is the seat most exposed to the October 1 re-run (below). Trigger $2.10. | Fair; boundary case on growth rank. |

Bench (ranks 11-20 of the top 20, not bought): ADSK is first out on valuation (0.28, EPS +61%), then PAYX (0.30) and NFLX (0.30, which held the 10th seat on the August candle). FICO, ELF, ISRG, VVV, CXT, CVLT and AJG sit at the 45th to 71st percentile of their own history and are not cheap by this measure.

## What the backtest says about a basket like this

Strategy `both_opval`, 2004 to August 2026 (cash until 2008), $100,000 start, withdrawals included: IRR 14.6% versus 9.1% for SPY with the same withdrawals; max drawdown -34% (March 2020) versus -55%; 119 closed positions, 79% winners, average +45%, median +51%, average loser -15%; 66 of about 140 entries sold by the guide-cut proxy inside year one at an average of +12%. Full tables in `turnaround_backtest_v3/STRATEGY_both_opval.md`.

**Forward returns of the picks themselves** under `both_opval`, every snapshot from January 2009 to September 2025, buy at the first close after the snapshot and hold 12 months, no portfolio rules (620 top-10 picks, 436 bench picks):

| Group | n | Mean | Median | Win rate | Beat SPY | 10th pct | 90th pct | Median worst drawdown in year 1 |
|---|---|---|---|---|---|---|---|---|
| Top 10 (bought) | 620 | +22% | +16% | 69% | 53% | -21% | +65% | -24% |
| Ranks 11-20 (bench) | 436 | +19% | +14% | 67% | 46% | -21% | +62% | -24% |
| Top 10, val ≤ 0.10 (PODD, KNSL, APPF) | 218 | +38% | +23% | 80% | 58% | -16% | +96% | -24% |
| Top 10, val 0.10 to 0.25 (the other seven) | 222 | +17% | +16% | 66% | 52% | -25% | +58% | -25% |
| Top 10, val > 0.25 | 180 | +11% | +4% | 58% | 47% | -22% | +47% | -23% |
| Top 10, 60% or more below 5y high (PODD, INTU) | 64 | +56% | +24% | 73% | 55% | -32% | +181% | -32% |
| Top 10, 40-60% below (KNSL, NOW, DXCM, OLLI, BSX) | 250 | +24% | +19% | 68% | 55% | -20% | +66% | -25% |
| Top 10, less than 40% below (APPF, DT, VEEV) | 306 | +14% | +13% | 68% | 51% | -20% | +50% | -21% |

The pattern from the v2 report holds under the operating-multiple ranking: the cheapest tenth of a company's own history is where the edge is (median +23%, 80% winners), the 0.10-0.25 band is ordinary, and above 0.25 the picks barely beat a coin flip against SPY. Three of today's ten are in the cheap bucket and seven in the ordinary band, so the basket's base case is a median return in the mid-to-high teens with about 7 of 10 positive, one or two names down 25% or more at some point in the year, and by the backtest's history roughly half sold by the proxy before their first anniversary. The "60% or more below the high" cell has 64 observations concentrated in 2009 and 2020, so its +56% mean is a regime statement, not a forecast for PODD and INTU.

## Sensitivity to the October 1 snapshot

Today's screen uses the September candle with two trading days still to come (the run was made before the open on Monday the 28th; the candle closes on Wednesday the 30th). On the completed August candle the `both_opval` top 10 was PODD, KNSL, OLLI, APPF, DT, DXCM, NOW, VEEV, INTU, NFLX: nine of today's ten, with NFLX in place of BSX. BSX entered the top 20 at growth rank 20 exactly, so any organic-eligible name with growth above 13.5% whose monthly RSI dips under 42 on the September candle pushes it out; the next names by valuation are ADSK (0.28), PAYX (0.30) and NFLX (0.30). The other nine seats are stable across both views. Buying today means entering three trading days before the official snapshot; the rule set has no opinion on that, and the list itself is what the backtest would have bought on October 1 if the last three sessions change nothing.

Re-run on October 1 (or any day) with:

```bash
cd turnaround_backtest_v3 && python live_v3.py
```

## Running backtest portfolio, for reference

The v3 backtest portfolio (to August 31, 2026) already holds PODD (April 2026 at $207.04, -28%), KNSL (+8%), VEEV (+65%, trimmed), DXCM (+38%) and APPF (+42%), so in that book only OLLI, INTU, DT, NOW and BSX would be new buys and PODD would not be averaged down (the rule never adds to a held name). A fresh account buys all ten.
