# Turnaround candidates backtest (2004 – Aug 2026)

Backtests the turnaround scanner's shortlisted candidates as a portfolio
strategy. Uses the scanner in `../turnaround/` (its RSI, monthly-candle and
episode rules, its universe and its SEC EDGAR fundamentals) but keeps its own
data and outputs here so the scanner's 15-year price cache is untouched.

> Research tooling, not investment advice. Yahoo prices, SEC XBRL filings,
> today's index constituents (survivorship bias), no taxes or costs.

## Layout

```
data.py       full-history prices for the S&P 500 + 400 universe (cache/prices/, not committed)
              and EDGAR quarterly tables through the scanner's edgar.py (../turnaround/cache/edgar/)
screen.py     quarterly point-in-time screen -> output/snapshots.json / snapshots.csv
engine.py     daily portfolio simulation (trim, RSI exit, replacement, rotation, withdrawals)
backtest.py   scenarios + SPY benchmark -> output/results.json, report.md, <scenario>_trades.csv, *_equity.csv
```

## Run it

```
python data.py prices        # ~5 min: Yahoo, period=max, 904 tickers + SPY
python data.py edgar         # ~30 min: SEC company facts for every ticker (3 MB each, raw not committed)
python screen.py             # ~1 min
python backtest.py           # seconds
```

## Rules

**Snapshots** on 1 Jan / 1 Apr / 1 Jul / 1 Oct from 2004-01-01 to 2026-07-01,
each evaluated as of the previous day so the last *completed* monthly candle
is used, like `scan.py --as-of`.

**Selection at each snapshot** (only data public on that day):

1. scanner price screen: monthly Wilder RSI(14) < 42 in any of the last 6
   completed months, ≥ 5 years of history, 3-month average dollar volume
   ≥ $5M, market cap ≥ $1B (month-end close × diluted shares from the filings)
2. profitable now (TTM EPS and net income > 0) and profitable in the past (at
   most one losing year among the TTM readings one, two and three years back)
3. top 20 by TTM revenue growth YoY (fiscal-year growth when the year-ago TTM
   reading does not exist, which only happens in the first XBRL years)
4. top 10 of those by valuation versus the company's own history: the mean
   percentile of the current trailing P/E, P/S and EV/EBITDA within the
   monthly series rebuilt from filings (≥ 12 months of history required)

**Portfolio** ($100,000, no taxes, no costs, dividends credited as cash, idle
cash earns nothing):

* on the first trading day after a snapshot, every top-10 name not already
  held is bought with at most 10% of the portfolio, from cash; if cash is
  short, a held position that is up more than 100% is sold in full to fund it
* names that fall off the list are kept
* trim: sell half when a position closes ≥ +50% over its average cost (once)
* exit: sell all at a month-end whose monthly RSI(14) is ≥ 90
* withdrawal on the last trading day of each complete year: year return
  > 20% → 10% of the portfolio; 10–20% → 7.5%; below 10% (and losses) → 5%;
  positions are sold pro-rata when cash is short; 2026 (to August) has none

**Scenarios** in `backtest.py`: `base` (rules above), `no_trim`, `rotate`
(hold exactly the current top 10), `base_no_wd`, `rsi80`, and `base_2009` /
`rotate_2009` started on 2009-01-01, plus SPY total return with the same
withdrawal rule from each start date.

## Data limits, stated up front

* SEC XBRL starts with fiscal-2007 comparatives for large filers (2009–2011
  for smaller ones), so no stock can pass rules 2–4 before 2008: the
  2004–2008 snapshots are empty, the portfolio sits in cash and still pays the
  5% withdrawal. The 2009-start scenarios show the strategy on the window
  where the data exists.
* The universe is today's S&P 500 + 400. Companies that failed, were taken
  over or dropped out are absent, which flatters every scenario.
* A monthly RSI of 90 is essentially never printed by a large-cap stock, so
  the "sell the rest at RSI 90" rule never fires; losers are only ever sold
  pro-rata for withdrawals. `rsi80` shows the sensitivity.
* Figures from filings are used from the date they were first public (capped
  at 90 days after the quarter end for pre-XBRL comparatives).
