# Turnaround scanner — monthly RSI < 35 discovery filter

Tooling for the five-step turnaround process: **find distress → diagnose the
cause → verify survival → identify recovery evidence → assess the price.**
The code automates step 1, gives a screen-level proxy for step 3, and
scaffolds steps 2, 4 and 5 as a research file per company. It also runs the
historical study that tests whether the RSI condition has predictive value.

> Research tooling, not investment advice. Every number here comes from Yahoo
> Finance's standardised data and must be verified against the filings before
> it is relied on.

## Layout

```
turnaround/
  scan.py             the scanner: universe -> price screen -> fundamentals -> watchlist
  episodes.py         historical study of RSI<35 episodes (forward returns vs SPY / sector)
  indicators.py       Wilder RSI, monthly candles, episode grouping, drawdown, dollar volume
  prices.py           15-year daily price cache (cache/prices/<TICKER>.csv)
  fundamentals.py     Yahoo statements -> survival gate + valuation proxies (cache/fundamentals/)
  universe.py         S&P 500 / 400 / 600 constituents from Wikipedia (cache/universe.csv)
  thesis_template.md  research file template (steps 2-5 of the process)
  thesis/             one file per company you are actually researching
  output/             screen_all.csv, watchlist.{csv,json,md}, episodes*.csv/md
```

Requires Python 3.11+, `pandas`, `numpy`, `yfinance`, `lxml` (`pip install yfinance lxml`).

## Run it

```
python scan.py                              # S&P 500 + 400, default rules, with fundamentals
python scan.py --no-fundamentals            # price screen only, ~10 s from cache
python scan.py --extra ENPH,BABA,NVO        # add names outside the index universe
python scan.py --tickers ENPH,INTC,NKE      # ad-hoc list only
python scan.py --universe sp500,sp400,sp600 # widen the universe (first run downloads prices)
python scan.py --threshold 30 --lookback 3 --min-mcap 2e9 --min-adv 1e7
python scan.py --as-of 2025-06-30           # price screen as of a past month-end
python scan.py --init-thesis NKE            # create thesis/NKE.md pre-filled with the screen facts
python episodes.py                          # the historical study (see below)
```

Prices are refreshed when the cache is older than a day (`--refresh` forces
it); fundamentals when older than a week (`--refresh-fundamentals`).

## What the screen computes

| Field | Definition |
|---|---|
| `rsi_m` | 14-period Wilder RSI on **monthly closes**, last *completed* calendar month. The current partial month is never used for qualification (`rsi_partial_month` is shown for information). |
| `oversold_now` | `rsi_m < 35` |
| episode | consecutive oversold months are one distress episode: `episode_start` is the qualification date, `episode_months` its length, `episode_exit` the first month back above 35 |
| `qualified` | the latest episode was active in any of the last 6 completed months, so a name is kept while its recovery begins |
| `drawdown_5y` | last close ÷ highest daily close of the trailing 5 years − 1; `priority` when ≤ −40% |
| `adv_3m_usd` | mean of close × volume over the last 63 trading days (≥ $5M required) |
| `years_history` | span of available prices (≥ 5 required); `first_bar` shows the start |
| `market_cap` | from Yahoo (≥ $1B required, applied after fundamentals are fetched) |

Prices are split-adjusted; `Close` is used for RSI and drawdown, the
dividend-adjusted `AdjClose` only for total-return maths in the study.

### Survival gate (proxy)

From the latest quarterly balance sheet and trailing-four-quarter cash flow:

```
burn        = max(0, -FCF_ttm)
need_24m    = 2 × burn + debt due within 12 months
gap_24m     = need_24m − cash & short-term investments
PASS        gap ≤ 0                        (24 months of burn + all near-term maturities covered by cash)
REVIEW      cash ≥ 2 × burn but gap > 0    (operations funded; maturities need refinancing)
FAIL        cash < 2 × burn
UNKNOWN     statements missing
```

Also reported: runway in months, net debt / EBITDA, interest coverage,
cash / debt, 1-year share-count change (dilution), and EV/Sales, EV/EBITDA,
P/E, P/FCF, P/B for the price-assessment step. Yahoo cannot show undrawn
revolvers, covenants or the maturity ladder, so the gate ranks and flags;
the thesis file's survival table is where the real assessment goes.

## Watchlist and thesis files

`output/watchlist.md` is the ranked list (priority names first, then by
drawdown). `python scan.py --init-thesis TICKER` creates `thesis/TICKER.md`
from the template with the screen facts filled in and the rest blank:
diagnosis of the decline, the survival table, the testable recovery thesis
with one leading and one confirming indicator, bear/base/bull valuation over
three years, entry/add/exit conditions, sizing, and a dated log. The
watchlist links to the file once it exists.

## Historical study (`episodes.py`)

For every ticker, groups consecutive oversold months into one episode and
measures, using only prices known at the decision date:

* `first_oversold` — buy the month-end close that first prints RSI < 35 (the raw screen)
* `rsi_recovery` — wait for the first monthly close with RSI back ≥ 35
* `rsi_recovery40` — wait for RSI ≥ 40
* each split by whether the stock was already ≥ 40% below its 5-year high at entry
* `baseline_all_months` — unconditional forward returns of the same stocks, the control

Outputs 6/12/24/36-month total returns, excess over SPY and the sector ETF,
hit rates, worst drawdown from entry within 36 months, and time to recover.
Results land in `output/episodes.csv` (every episode) and
`output/episodes_summary.md`.

**Known limitations, stated in the output:** the universe is today's index
constituents, so failed and delisted names are missing (add casualties with
`--extra` where Yahoo still serves their history); episodes cluster in
2020 and 2022; and the "RSI + survival + valuation" arm of the comparison
needs point-in-time financial statements that Yahoo does not provide. The
study therefore answers "does the technical condition alone carry
information?" and "does waiting for RSI confirmation help?", not whether
business selection improves outcomes.
