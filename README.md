# StrategiesInv — dip-ladder backtesting

Backtest code and playbook for the lot-based dip-buying strategy ("Dip Ladder"
/ "Growth Combo"). The strategy rules — when to buy, hold, sell, capital
allocation, and put sizing — are in **[STRATEGY.md](STRATEGY.md)**.

Interactive report with all results and charts:
https://claude.ai/code/artifact/152b871b-c680-4fc4-8167-bec9b5bd475b

## Layout

```
fetch_data.py       download/refresh Yahoo daily data into data/*.json
backtest.py         round 1 engine: tier ladder + 20% lot rotation + options
sensitivity.py      round 1 scenarios (50% starter, never-sell)
improved.py         round 2 engine: trend filter, SPY parking, core, % tiers
round3.py           round 3: growth combo + puts, out-of-sample tickers
data/               raw Yahoo chart JSON per ticker (incl. SPY)
report/             HTML report template + data prep + builder
```

## Reproduce everything

Run from this folder (plain Python 3, no packages needed):

```
python fetch_data.py          # optional: refresh prices (writes data/*.json)
python backtest.py            # -> results.json          (round 1)
python sensitivity.py         # -> sensitivity.json      (round 1 scenarios)
python improved.py            # -> improved.json         (round 2 variants)
python round3.py              # -> round3.json           (round 3 out-of-sample)
python report/prep_report.py  # -> report_data.json
python report/prep_round2.py  # -> round2.json
python report/prep_round3.py  # -> round3_report.json
python report/build_report.py # -> report/report.html
```

Each engine prints a summary table as it runs. To test new tickers, fetch them
(`python fetch_data.py COST LLY`) and add the symbols to the ticker lists at
the bottom of `backtest.py` / `round3.py`.

## Model assumptions

Split-adjusted daily closes; dividends credited as cash; idle cash earns
2.5%/yr; option premiums via Black–Scholes at 1.1× trailing 63-day realized
volatility, monthly expiries, no early assignment; no taxes, commissions, or
slippage. Backtest window: 2015-01-02 onward. Educational simulation — not
investment advice.

## Turnaround scanner (`turnaround/`)

A separate tool set for the monthly-RSI < 35 turnaround process: universe
screen, survival-gate proxies, per-company thesis files, and the historical
episode study. See **[turnaround/README.md](turnaround/README.md)**.

```
python turnaround/scan.py        # watchlist -> turnaround/output/watchlist.md
python turnaround/episodes.py    # study    -> turnaround/output/episodes_summary.md
```

## Turnaround candidates backtest (`turnaround_backtest/`)

Backtests the scanner's shortlisted candidates as a quarterly-rebalanced
portfolio from 2004 to August 2026 (trim at +50%, monthly-RSI exit, yearly
withdrawals, several scenarios vs SPY). Uses the scanner's rules and EDGAR
fundamentals with its own full-history price cache. See
**[turnaround_backtest/README.md](turnaround_backtest/README.md)**.

```
python turnaround_backtest/data.py prices && python turnaround_backtest/data.py edgar
python turnaround_backtest/screen.py && python turnaround_backtest/backtest.py
python turnaround_backtest/report_html.py   # -> turnaround_backtest/output/report.html
```

## Weekly-RSI swing study (`rsi_swing/`)

Backtests "buy when the 14-week RSI closes at/below a threshold, exit 4-10
months later" on any ticker, with a threshold sweep. See
**[rsi_swing/README.md](rsi_swing/README.md)**.

```
python rsi_swing/backtest.py QCOM --start 1996-01-01
python rsi_swing/backtest.py QCOM --sweep 28,30,32,34,36
```


## Synthetic lost decade (`synthetic.py`, `synthetic_run.py`)

A stress test of the same rules in a market like 1968–1982: the real S&P 500
daily path (Yahoo ^GSPC, +1.5%/yr price, a 48% drawdown in 1973–74, CPI up
180%). Each of today's 900 stocks is re-simulated on that path with its own
real beta and a block bootstrap (126-day blocks) of its own real idiosyncratic
daily returns, so single-stock crashes and rebounds keep their real shape while
the market goes nowhere. Quarterly fundamentals are generated: revenue grows
with CPI inflation plus a persistent company-specific real rate plus a share of
the stock's own quarterly price residual; net margins swing with the stock's
residual and the market and can turn negative; EBITDA, debt, cash, shares and
the starting market cap are scaled from each company's latest real filing.
Dividend yield 3.5%. Nothing in the fundamentals knows the future price.

```
python synthetic_run.py --seeds 0,1,2,3,4     # ~4 min per seed
```

writes `synthetic/output/seed<k>/` (the usual report.md / report.html /
results.json / trades) and `synthetic/output/summary.md` with every scenario
per seed in nominal and CPI-deflated terms, the median across seeds, and the
year-by-year comparison of base / no_trim / rotate against the index.
