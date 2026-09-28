# rsi_swing — weekly-RSI oversold swing study

Backtests a simple mean-reversion swing trade: **buy when the 14-week Wilder
RSI closes at or below a threshold, exit somewhere 4–10 months later.** Built
on QCOM but written so any ticker (and any threshold) can be tested the same
way.

> Research tooling, not investment advice. Yahoo Finance data, no commissions
> or slippage, no position sizing.

## Run it

```
python backtest.py QCOM                                # RSI<=32, exit 4-10 months, full history
python backtest.py QCOM --start 1996-01-01             # last ~30 years
python backtest.py QCOM --sweep 25,28,30,32,34,36,38   # compare thresholds
python backtest.py NVDA AMD INTC --threshold 30        # several tickers, one setting
python backtest.py QCOM --min-hold 3 --max-hold 12     # different exit window
python backtest.py QCOM --every-week                   # every oversold week is a trade
python backtest.py QCOM --entry close                  # buy the signal week's close
python backtest.py QCOM --rearm 40                     # need RSI>40 before a new signal
python backtest.py QCOM --price-only                   # ignore dividends
```

Prices are cached in `cache/<TICKER>.csv` (full Yahoo history, refreshed when
older than a day, `--refresh` forces it).

## Rules

| Step | Rule | Flag |
|---|---|---|
| Bars | daily → weekly (Friday close) | |
| Indicator | 14-period Wilder RSI on weekly split-adjusted closes | `--rsi-period` |
| Signal | first week with RSI ≤ threshold | `--threshold` (32) |
| Re-arm | no new signal until RSI has closed above `rearm` | `--rearm` (= threshold) |
| Entry | next Monday's open (or signal week close) | `--entry` |
| Exit window | months `min_hold`..`max_hold` after entry | `--min-hold 4 --max-hold 10` |
| Returns | dividend-adjusted (total return) | `--price-only` to disable |

`--every-week` disables the re-arm rule so every oversold week becomes its own
(overlapping) trade — useful to see whether adding on the way down helps.

## What the report shows (`output/<TICKER>_t<threshold>_summary.md`)

- **Per horizon (4, 5 … 10 months):** trades, win rate, average, median,
  worst, best, number of losing trades, average loss / win.
- **Whole-window view:** average return over the window, average best and
  worst exit available inside it, how many trades never closed a week below
  entry during the window, how many had at least one losing horizon, how many
  were negative at *every* horizon, and the drawdown suffered before month 4.
- **Base rate:** the same forward returns from *every* week regardless of
  RSI, so you can tell whether the signal adds anything over just owning the
  stock. Compare medians; the mean base rate is skewed by bubble years.
- **Trade list** with every horizon, also saved as `..._trades.csv`.

`--sweep` writes `output/<TICKER>_sweep.csv` with one row per threshold so the
right level for a given stock can be picked (signals, average/median window
return, win rate, average best/worst exit, worst single exit, trades with any
losing horizon, trades negative everywhere, worst drawdown).

## Caveats

- Few signals per stock (QCOM: 12 completed in 30 years). Treat win rates as
  indicative, not statistical proof.
- The threshold that looks best in a sweep is partly fitted to that stock's
  past; prefer a level that is also sensible on neighbouring thresholds.
- A stock that never recovers (or is delisted) never enters the sample:
  survivorship bias favours the strategy.
- Signals are on weekly closes; in practice you would see the RSI cross
  intra-week and act earlier or later than the model.
