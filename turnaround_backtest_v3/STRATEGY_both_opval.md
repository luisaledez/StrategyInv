# Strategy `both_opval`: turnaround candidates with entry-data guards, ranked on operating multiples

*Defined 2026-09-28. Backtest v3 scenario `both_opval` in this folder. Research tooling, not investment advice.*

`both_opval` is backtest v2's **re-screen + guide-cut proxy** strategy (`rescreen_only`) with three
changes at the entry stage and nothing changed after the buy: candidates whose trailing earnings
contain a one-off item are rejected, candidates whose growth came from an acquisition are rejected,
and the valuation ranking uses price-to-sales, EV/EBITDA and EV/EBIT instead of P/E, P/S and
EV/EBITDA. Everything else (snapshot dates, price screen, profitability, organic-growth tests,
position sizing, trim, exits, re-screen, guidance-cut proxy, withdrawals) is identical.

## 1. The rules, end to end

### Data

* Universe: today's S&P 500 and S&P 400 constituents (898 tickers with filings). Survivorship bias:
  companies that failed or were taken over are missing.
* Prices: Yahoo daily bars, full history (`../turnaround_backtest/cache/prices/`).
* Fundamentals: SEC EDGAR XBRL company facts, rebuilt quarter by quarter as **point-in-time**
  tables (`../turnaround/cache/edgar/`): every figure is used from the date it was first public,
  never restated. Trailing-twelve-month (TTM) revenue, net income, operating income, EPS, D&A;
  quarter-end cash, debt and diluted shares. SEC data starts with fiscal-2007 comparatives, so the
  first buys happen in 2008-2009.

### When

Quarterly snapshots on 1 January, 1 April, 1 July and 1 October, each evaluated as of the previous
day so the last **completed** monthly candle is used. Orders are executed at the close of the
first trading day after the snapshot.

### Screen (only data public on the snapshot date)

| Step | Rule | Threshold |
|---|---|---|
| 1 | Distress: monthly Wilder RSI(14) on the close was below 42 in at least one of the last 6 completed months | 42 / 6 |
| 2 | Tradeable: at least 5 years of price history; 3-month average daily dollar volume; market cap (month-end close × diluted shares) | 5 y / $5M / $1B |
| 3 | Profitable now: TTM EPS > 0 and TTM net income > 0 | |
| 4 | Profitable in the past: at most one losing year among the TTM net-income readings one, two and three years earlier | |
| 5 | Organic growth (from backtest v2): TTM revenue growth year over year positive and below 100%; no quarter-to-quarter jump of the TTM revenue figure above 60% in the last eight quarters; latest quarter not below its year-ago quarter while the trailing year is up | 0 < g < 100% / 1.6x / — |
| 6 | **One-off EPS guard (new)**: reject if TTM net income exceeds TTM operating income (a non-operating gain or a tax benefit is inside the trailing year), or if one quarter lifted TTM net income by more than 50% while TTM operating income rose less than 25%. Without an operating-income tag in the filings, reject a one-quarter jump of more than 50% in TTM EPS | 1.0x / 1.5x vs 1.25x |
| 7 | **Acquisition guard (new)**: reject if diluted shares are up more than 15% year over year (stock-financed deal or equity raise), or if TTM revenue growth is 15% or more and at least three times and ten points above the growth reported one year earlier while that earlier growth was not negative (cash-financed deal phasing in; recoveries from a decline are exempt) | 15% / 15%, 3x, 10 pp |
| 8 | Top 20 of the survivors by TTM revenue growth | 20 |
| 9 | **Valuation on operating multiples (new)**: rank those 20 by the mean percentile of today's trailing P/S, EV/EBITDA and EV/EBIT within the company's own monthly history rebuilt from filings (0 = cheapest ever). At least 12 months of history per multiple. Ties broken by higher growth. Take the top 10 | 10 |

### Portfolio

| Rule | Detail |
|---|---|
| Capital | $100,000 at the start; dividends credited as cash; idle cash earns nothing; no taxes, commissions or slippage |
| Buy | On the first trading day after a snapshot, every top-10 name not already held is bought, in valuation-rank order, with at most **10% of the portfolio value** per stock, from cash. If cash is short, a held position that is up more than 100% is sold in full to fund the purchase; otherwise the name is skipped |
| Names that leave the list | Kept |
| Trim | Sell half when a position closes at or above **+50%** over average cost (once per position) |
| Overbought exit | Sell all at a month-end whose monthly RSI(14) is at or above 90 (fired once in 22 years) |
| Spin-off / divestiture re-screen | At a month-end when a holding's filings re-base its history by 30% or more (a year-ago comparative restated to 0.70x or below, or a reported annual revenue at 0.70x or below the trailing reading, read from the EDGAR loader's warnings), the position is sold unless the name is on the current top-10 list |
| Guidance-cut proxy | Within 12 months of purchase, sold at the month-end when the point-in-time TTM EPS is 15% or more below its level at entry (no guidance history exists in the data set) |
| Withdrawal | On the last trading day of each complete year: year return above 20% → 10% of the portfolio; 10-20% → 7.5%; below 10% including losses → 5%. Positions are sold pro-rata when cash is short. No withdrawal in the partial year 2026 |
| Not in the strategy | No position cap, no S&P 500 correction parking, no price stop-loss, no time stop (all tested and rejected in backtests v1 and v2) |

### What changed versus backtest v2 `rescreen_only`

| | v2 `rescreen_only` | v3 `both_opval` |
|---|---|---|
| One-off EPS guard | none | step 6 |
| Acquisition guard | none (only the 60% one-quarter jump test of the organic filter) | step 7 |
| Valuation percentile | mean of P/E, P/S, EV/EBITDA percentiles | mean of P/S, EV/EBITDA, EV/EBIT percentiles |
| Everything else | identical | identical |

## 2. Performance, side by side

Both strategies on the same data, same engine, same snapshot dates. "Final + withdrawn" is the ending
value plus everything taken out; IRR is the money-weighted return of the $100,000 in, the withdrawals
out and the final value; max drawdown is on the no-withdrawal index.

| | v2 `rescreen_only` | v3 `both_opval` | SPY, same withdrawals |
|---|---|---|---|
| **From 2004** (cash until 2008): IRR | 14.0% | **14.6%** | 9.1% |
| Final + withdrawn | $945k | **$1,101k** | $387k |
| Max drawdown | -38.0% (18 Mar 2020) | **-33.7%** (23 Mar 2020) | -55.2% |
| **From 2009**: IRR | 22.9% | **23.7%** | 14.8% |
| Final + withdrawn | $1,197k | **$1,444k** | $526k |
| Max drawdown | -38.1% | **-34.3%** | -33.7% |
| No-withdrawal CAGR 2009-Aug 2026 | 21.1% | **23.2%** | 14.7% |
| Annualised daily volatility 2009+ | 18.2% | 18.2% | |
| Return / volatility | 1.16 | **1.27** | |
| Negative calendar years (of 17) | 1 (2025: -1.2%) | 1 (2015: -6.0%) | |

### Year by year (2004 start; both sit in cash until 2008)

| Year | v2 | v3 | SPY | Year | v2 | v3 | SPY |
|---|---|---|---|---|---|---|---|
| 2009 | +51.1% | +49.1% | +26.4% | 2018 | +1.3% | +0.4% | -4.6% |
| 2010 | +12.2% | +15.3% | +15.1% | 2019 | +36.2% | +38.1% | +31.2% |
| 2011 | +10.0% | +7.5% | +1.9% | 2020 | +29.9% | +38.0% | +18.3% |
| 2012 | +20.7% | +23.1% | +16.0% | 2021 | +27.1% | +32.4% | +28.7% |
| 2013 | +49.6% | +46.9% | +32.3% | 2022 | +7.3% | +6.6% | -18.2% |
| 2014 | +20.3% | +20.7% | +13.5% | 2023 | +41.8% | +31.4% | +26.2% |
| 2015 | +1.0% | -6.0% | +1.2% | 2024 | +26.0% | +23.5% | +24.9% |
| 2016 | +37.9% | +35.0% | +12.0% | 2025 | -1.2% | +20.5% | +17.7% |
| 2017 | +18.2% | +24.6% | +21.7% | 2026 (to Aug) | +1.5% | +17.3% | +13.1% |

v3 divided by v2, no-withdrawal index at year ends: 0.99 (2009), 1.01, 0.99, 1.01, 0.99, 0.99,
0.93 (2015), 0.91 (2016), 0.96, 0.95, 0.96, 1.02 (2020), 1.06, 1.06, 0.98, 0.96 (2024), 1.17
(2025), 1.35 (Aug 2026).

### Positions

| | v2 `rescreen_only` | v3 `both_opval` |
|---|---|---|
| Buys / distinct names | 141 / 125 | 141 / 126 |
| Names bought by both | 90 | 90 |
| Closed positions | 118 | 119 |
| Win rate | 71% | **79%** |
| Average / median closed return | +39% / +40% | **+45% / +51%** |
| Average winner / average loser | +61% / -13% | +61% / -15% |
| 10th / 90th percentile | -12% / +93% | -13% / +91% |
| Worst closed | FANG -69%, META -59%, HPQ -30% | META -59%, HPQ -30%, TRU -27% |
| Best closed | LAD +130%, ETR +126%, PAG +111% | LAD +118%, LLY +113%, FHI +105% |
| Guide-cut proxy exits (of ~140 entries) | 70, averaging +10% | 66, averaging +12% |
| Median hold | 8.9 months | 9.0 months |
| Open at the end / below cost / unrealised | 23 / 12 / -$5k | 22 / 10 / **+$42k** |
| Quarterly top-10 lists in common | 72% of the 677 reference slots | |
| Sector mix of buys | Health care 22, cons. disc. 21, financials 21, industrials 17, tech 16, energy 12 | Health care 26, cons. disc. 23, tech 21, financials 21, industrials 17, energy 5 |

## 3. Where the difference comes from, honestly

1. **Through 2024 the two strategies are a tie.** The v3/v2 index ratio oscillates between 0.91 and
   1.06 and stands at 0.96 at the end of 2024. The guards did not add return over 16 years; they
   changed which names were bought (36 names each way out of about 125) at roughly the same result.
2. **The IRR gap is the last twenty months.** 2025 (+20.5% vs -1.2%) and 2026 to August (+17.3%
   vs +1.5%) account for the whole margin. v2 bought TTD (-72%), BAH (-30%), SLB, NOV, CNC and MOH
   in this window and carried 18-22% cash; v3 bought DT (+48%), VEEV (+65%), APPF (+42%), YETI (+22%)
   and a larger DXCM position instead. Of v2's entries in this window only NOV and CNC (and the
   flat SON) were actually removed by the guards. TTD, BAH, SLB and MOH were on v3's top-10 list as well; v3 did not own them
   because its cash was already committed to names that ranked higher on operating multiples. That
   is a genuine ranking effect, but it is one window and it is path-dependent. Treat the 2025-26
   margin as a favourable draw, not as the expected edge.
3. **What is robust across the whole history:** the win rate (71% → 79%), the median closed
   return (+40% → +51%), the maximum drawdown (-38% → -34%, 2020 in both) and the absence of
   the FANG-type entry (an all-stock energy acquisition ranked cheap on the acquirer's pre-deal
   history). Across the 91 snapshots the guards strike 138 of the 677 reference top-10 slots; the
   15 struck names that v2 actually bought ended at a median of 0% and a 47% win rate, against +40%
   and 71% for v2's closed positions overall.
4. **The one-off guard is partly a financials filter.** Insurers and banks (MET, HIG, CINF, MS,
   FHN, HBAN, JEF) dominate the one-off strikes because their trailing net income swings without a
   matching operating-income tag. That suited this strategy historically (their growth was rarely
   organic) and v3's energy and financials exposure is lower for it.
5. **Thresholds were set once, not tuned.** The 1.0x / 1.5x / 1.25x / 15% / 3x / 10 pp values were
   chosen from the FIS, DUOL and AMCR cases before the backtest was run and were not changed
   afterwards. That limits overfitting but means their sensitivity is untested.
6. **Same caveats as every version:** survivorship bias in the universe, no costs or taxes, filings
   data only from 2008, and the guidance-cut proxy still fires on ordinary earnings declines.

## 4. Today's list (as of 27 September 2026)

Top 10 under `both_opval`, in buy order: **PODD, KNSL, APPF, OLLI, INTU, DT, NOW, DXCM, VEEV, BSX**
(the September candle was two trading days short; the official 1 October snapshot uses the
30 September close). Compared with the v2 list of the same day (PODD, FIS, NOW, VEEV, APPF, DUOL,
AMCR, PINS, CSGP, GEN), the guards removed FIS, DUOL, PINS, CSGP and GEN (one-off earnings) and
AMCR (Berry Global shares), and KNSL, OLLI, INTU, DT, DXCM and BSX moved up. Rule allocation:
10% each. In the running backtest portfolio PODD, KNSL, APPF, VEEV and DXCM are already held
(PODD from April 2026 at $207, now -28%), so only OLLI, INTU, DT, NOW and BSX would be new buys
there. The per-name risk notes for the names shared with the v2 list are in
`../reports/Turnaround top 20 - 2026-09-27.md`.

## 5. Files

```
screen_v3.py                    guards and the operating-multiple percentile; writes output/snapshots_both_opval.json
backtest_v3.py                  runs the portfolio rules; scenario names both_opval and both_opval_2009
output/results.json             summaries, yearly tables, closed and open positions, trades
output/report.md                every scenario side by side, the snapshot-by-snapshot list of what the guards removed
output/both_opval_trades.csv    trade log; both_opval_equity.csv daily equity and no-withdrawal index
output/current_both_opval.json  today's top 20 / top 10 with every diagnostic
```
