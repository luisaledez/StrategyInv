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

