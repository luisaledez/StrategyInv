# PDD — weekly RSI(14) ≤ 32 swing study

- Data: 2018-07-26 → 2026-09-18 (426 weekly bars, total return)
- Entry: next bar open; re-arm when RSI closes above 32; first bar of each episode only
- Exit window: 2–10 months after entry
- Signals: 5 (completed: 3)

## Return by fixed exit horizon (completed trades)

| horizon_m | trades | win_rate | avg | median | min | max | losses | avg_loss | avg_win |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | +33.3% | -2.7% | -2.6% | -12.8% | +7.3% | 2 | -7.7% | +7.3% |
| 3 | 3 | +33.3% | +4.1% | -5.8% | -29.5% | +47.6% | 2 | -17.6% | +47.6% |
| 4 | 3 | +33.3% | +2.8% | -17.2% | -29.7% | +55.2% | 2 | -23.5% | +55.2% |
| 5 | 3 | +33.3% | -15.6% | -30.2% | -35.5% | +18.9% | 2 | -32.9% | +18.9% |
| 6 | 3 | +33.3% | +13.1% | -1.8% | -29.5% | +70.6% | 2 | -15.7% | +70.6% |
| 7 | 3 | +66.7% | +6.7% | +12.7% | -51.0% | +58.5% | 1 | -51.0% | +35.6% |
| 8 | 3 | +33.3% | -3.7% | -12.9% | -52.2% | +53.9% | 2 | -32.6% | +53.9% |
| 9 | 3 | +66.7% | +25.1% | +21.7% | -60.5% | +114.0% | 1 | -60.5% | +67.9% |
| 10 | 3 | +66.7% | +41.3% | +19.2% | -33.6% | +138.2% | 1 | -33.6% | +78.7% |

## Whole-window view (2–10 month exit range)

- Trades: 3
- Average return across the window: +4.9%
- Average best exit inside the window: +61.1%
- Average worst exit inside the window: -37.0%; single worst: -63.7%
- Trades that stayed above entry at every weekly close in the window: 0 / 3
- Trades with at least one losing month-end horizon: 3 / 3
- Trades negative at every horizon: 0 / 3
- Drawdown before the window opens (entry → month 2): avg -11.8%, worst -19.9%
- Max drawdown entry → month 10: avg -41.6%, worst -63.7%

## Hold until +30% (no time limit)

- Reached the target: 3 of 5 signals; still waiting: 2
- Months to target: median 8.8, average 13.0, longest 27.3
- Reached within 4 / 10 / 12 / 24 months: 1 / 2 / 2 / 2
- Worst close before the target: average -36.7%, single worst -71.1%; 3 signals fell 20% or more first

| Signal | RSI | Entry | Entry px | Reached | Months | Return | Worst on the way | Worst date |
|---|---|---|---|---|---|---|---|---|
| 2021-08-06 | 31.74 | 2021-08-09 | 88.4 | 2023-11-17 | 27.3 | +30.3% | -71.1% | 2022-03-14 |
| 2021-12-03 | 30.65 | 2021-12-06 | 54.73 | 2022-08-31 | 8.8 | +30.3% | -53.4% | 2022-03-14 |
| 2022-03-04 | 31.41 | 2022-03-07 | 40.1 | 2022-06-02 | 2.9 | +31.3% | -36.3% | 2022-03-14 |
| 2026-05-29 | 31.7 | 2026-06-01 | 83.83 | **not yet** | 3.6 | -5.9% | -12.6% | 2026-06-25 |
| 2026-06-12 | 30.32 | 2026-06-15 | 81.56 | **not yet** | 3.1 | -3.3% | -10.1% | 2026-06-25 |

## Base rate: forward return from *any* week (no signal)

| horizon_m | weeks | win_rate | avg | median | min |
|---|---|---|---|---|---|
| 2 | 417 | +51.8% | +6.1% | +1.3% | -57.7% |
| 3 | 412 | +50.5% | +9.2% | +1.0% | -46.7% |
| 4 | 408 | +53.2% | +12.9% | +3.1% | -73.1% |
| 5 | 404 | +56.4% | +16.9% | +5.8% | -70.9% |
| 6 | 399 | +56.4% | +19.8% | +8.5% | -65.5% |
| 7 | 395 | +59.0% | +23.4% | +9.4% | -69.7% |
| 8 | 391 | +59.6% | +28.3% | +13.2% | -65.7% |
| 9 | 386 | +61.9% | +33.4% | +17.5% | -73.7% |
| 10 | 382 | +62.6% | +39.0% | +19.3% | -78.4% |

## Trades

| signal_week | rsi | entry_date | entry_px | ret_2m | ret_3m | ret_4m | ret_5m | ret_6m | ret_7m | ret_8m | ret_9m | ret_10m | best_in_window | worst_in_window | max_dd_pre_window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021-08-06 | 31.74 | 2021-08-09 | 88.40 | +7.3% | -5.8% | -29.7% | -35.5% | -29.5% | -51.0% | -52.2% | -60.5% | -33.6% | +12.0% | -63.7% | -12.6% |
| 2021-12-03 | 30.65 | 2021-12-06 | 54.73 | -2.6% | -29.5% | -17.2% | -30.2% | -1.8% | +12.7% | -12.9% | +21.7% | +19.2% | +31.9% | -41.3% | -3.1% |
| 2022-03-04 | 31.41 | 2022-03-07 | 40.10 | -12.8% | +47.6% | +55.2% | +18.9% | +70.6% | +58.5% | +53.9% | +114.0% | +138.2% | +139.3% | -5.9% | -19.9% |
| 2026-05-29 | 31.70 | 2026-06-01 | 83.83 | +7.5% | -0.8% | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | -8.7% |
| 2026-06-12 | 30.32 | 2026-06-15 | 81.56 | +6.6% | -4.3% | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | -6.1% |
