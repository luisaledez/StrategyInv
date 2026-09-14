# Monthly-RSI distress episodes — study

Universe: sp500,sp400. Threshold RSI(14) < 35.0; confirmation exit level 35.0. 1214 episodes across 563 tickers, 15 years of monthly closes.

Forward returns are total returns (dividend-adjusted) from the month-end close of the entry month. `excess` = stock return minus SPY (or sector ETF) over the same window. `max dd` = worst point relative to the entry price within 36 months; `recovered` = price back at/above entry within 36 months.

**Caveats.** (1) Survivorship: the universe is today's constituents; delisted failures are absent, which flatters every row. (2) Episodes cluster in 2020 and 2022, so independent observations are fewer than N. (3) No fundamentals are applied here; this is the 'RSI alone' arm of the comparison. The 'RSI + survival + valuation' arm needs point-in-time financials that Yahoo does not provide.

Episodes per start year: 2012: 11, 2013: 8, 2014: 14, 2015: 118, 2016: 70, 2017: 45, 2018: 126, 2019: 67, 2020: 292, 2021: 2, 2022: 121, 2023: 98, 2024: 49, 2025: 100, 2026: 93

| Rule | H | N | Median | Mean | P25 | P75 | % > 0 | Med. excess SPY | % beat SPY | Med. excess sector | % beat sector | Med. max DD 36m | % recovered 36m | Med. months to recover |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| first_oversold | 6m | 1147 | +13.9% | +16.9% | -3.5% | +31.9% | 71% | +0.4% | 51% | +2.2% | 53% |  |  |  |
| first_oversold | 12m | 1096 | +33.7% | +51.3% | +3.0% | +70.1% | 77% | +10.2% | 60% | +8.7% | 60% |  |  |  |
| first_oversold | 24m | 998 | +55.1% | +95.9% | +13.4% | +102.9% | 82% | +7.6% | 55% | +8.4% | 57% |  |  |  |
| first_oversold | 36m | 922 | +61.8% | +125.5% | +18.8% | +123.8% | 83% | +6.6% | 53% | +11.8% | 57% | -10.5% | 98% | 1 |
| first_oversold | dd>40% | 6m | 940 | +14.7% | +18.0% | -4.2% | +34.2% | 70% | +0.6% | 51% | +2.2% | 53% |  |  |  |
| first_oversold | dd>40% | 12m | 896 | +37.4% | +56.8% | +2.8% | +78.1% | 77% | +11.5% | 61% | +10.9% | 61% |  |  |  |
| first_oversold | dd>40% | 24m | 813 | +61.8% | +108.9% | +13.6% | +121.8% | 82% | +12.2% | 56% | +10.3% | 57% |  |  |  |
| first_oversold | dd>40% | 36m | 748 | +69.5% | +143.1% | +21.8% | +133.4% | 84% | +11.4% | 55% | +15.3% | 58% | -11.6% | 99% | 1 |
| first_oversold | dd<40% | 6m | 207 | +11.5% | +11.8% | -0.9% | +26.2% | 74% | -0.1% | 50% | +1.6% | 54% |  |  |  |
| first_oversold | dd<40% | 12m | 200 | +27.1% | +26.9% | +3.6% | +46.5% | 79% | +3.7% | 54% | +4.0% | 56% |  |  |  |
| first_oversold | dd<40% | 24m | 185 | +38.3% | +39.1% | +13.0% | +67.5% | 84% | +0.4% | 50% | +0.8% | 54% |  |  |  |
| first_oversold | dd<40% | 36m | 174 | +50.5% | +49.6% | +9.2% | +84.4% | 80% | -8.5% | 44% | +3.8% | 52% | -7.6% | 96% | 1 |
| rsi_recovery | 6m | 1113 | +11.5% | +16.4% | -6.4% | +29.5% | 67% | +2.1% | 54% | +2.0% | 55% |  |  |  |
| rsi_recovery | 12m | 1076 | +26.6% | +42.1% | -1.4% | +60.0% | 74% | +4.1% | 54% | +3.5% | 54% |  |  |  |
| rsi_recovery | 24m | 991 | +40.8% | +74.8% | +7.1% | +83.4% | 79% | +4.5% | 53% | +4.9% | 54% |  |  |  |
| rsi_recovery | 36m | 907 | +46.4% | +91.3% | +7.6% | +99.6% | 80% | -2.5% | 48% | +2.7% | 52% | -13.5% | 98% | 1 |
| rsi_recovery | dd>40% | 6m | 910 | +11.6% | +17.9% | -6.7% | +31.6% | 66% | +2.0% | 53% | +1.8% | 55% |  |  |  |
| rsi_recovery | dd>40% | 12m | 878 | +29.0% | +46.6% | -2.1% | +66.9% | 74% | +5.4% | 55% | +4.2% | 54% |  |  |  |
| rsi_recovery | dd>40% | 24m | 806 | +44.3% | +84.7% | +6.8% | +96.5% | 79% | +7.4% | 54% | +6.5% | 55% |  |  |  |
| rsi_recovery | dd>40% | 36m | 734 | +48.7% | +103.3% | +9.6% | +109.9% | 80% | -0.5% | 50% | +3.6% | 52% | -14.5% | 98% | 1 |
| rsi_recovery | dd<40% | 6m | 203 | +11.5% | +9.6% | -3.0% | +22.0% | 71% | +2.5% | 56% | +2.1% | 55% |  |  |  |
| rsi_recovery | dd<40% | 12m | 198 | +22.4% | +22.1% | +3.0% | +40.0% | 77% | +1.1% | 52% | +2.3% | 53% |  |  |  |
| rsi_recovery | dd<40% | 24m | 185 | +31.7% | +31.6% | +7.5% | +56.4% | 82% | -1.2% | 49% | +2.8% | 53% |  |  |  |
| rsi_recovery | dd<40% | 36m | 173 | +38.6% | +40.4% | +4.9% | +69.9% | 78% | -12.0% | 42% | -0.1% | 49% | -8.7% | 97% | 1 |
| rsi_recovery40 | 6m | 1093 | +13.1% | +22.0% | -4.4% | +31.9% | 70% | +3.3% | 58% | +2.6% | 57% |  |  |  |
| rsi_recovery40 | 12m | 1049 | +23.7% | +43.9% | -1.6% | +53.1% | 74% | +1.3% | 53% | +1.8% | 52% |  |  |  |
| rsi_recovery40 | 24m | 985 | +39.1% | +64.2% | +5.5% | +76.1% | 79% | +3.0% | 53% | +3.8% | 53% |  |  |  |
| rsi_recovery40 | 36m | 871 | +43.7% | +76.1% | +7.4% | +94.3% | 79% | -4.0% | 47% | -0.8% | 49% | -13.1% | 97% | 1 |
| rsi_recovery40 | dd>40% | 6m | 892 | +13.7% | +24.4% | -6.1% | +34.4% | 68% | +3.2% | 57% | +2.3% | 56% |  |  |  |
| rsi_recovery40 | dd>40% | 12m | 857 | +25.0% | +49.1% | -2.3% | +58.7% | 73% | +2.2% | 53% | +2.2% | 52% |  |  |  |
| rsi_recovery40 | dd>40% | 24m | 800 | +40.7% | +72.2% | +5.4% | +85.1% | 78% | +5.6% | 54% | +4.7% | 54% |  |  |  |
| rsi_recovery40 | dd>40% | 36m | 702 | +45.8% | +84.2% | +8.4% | +102.1% | 79% | -2.4% | 49% | -0.9% | 49% | -15.0% | 97% | 1 |
| rsi_recovery40 | dd<40% | 6m | 201 | +12.6% | +11.5% | +1.1% | +21.2% | 79% | +3.3% | 60% | +2.7% | 61% |  |  |  |
| rsi_recovery40 | dd<40% | 12m | 192 | +19.8% | +20.6% | +2.5% | +36.3% | 76% | -0.4% | 49% | -1.1% | 49% |  |  |  |
| rsi_recovery40 | dd<40% | 24m | 185 | +27.8% | +29.8% | +6.2% | +56.4% | 79% | -0.6% | 49% | +0.7% | 51% |  |  |  |
| rsi_recovery40 | dd<40% | 36m | 169 | +38.8% | +42.2% | +5.1% | +71.3% | 78% | -10.6% | 41% | -0.8% | 48% | -8.7% | 98% | 1 |
| baseline_all_months | 6m | 131253 | +6.7% | +9.8% | -5.5% | +19.6% | 65% | -0.5% | 49% | +0.3% | 51% |  |  |  |
| baseline_all_months | 12m | 125871 | +12.9% | +20.5% | -4.9% | +32.6% | 69% | -1.4% | 48% | +0.2% | 50% |  |  |  |
| baseline_all_months | 24m | 115158 | +25.6% | +41.8% | +0.5% | +55.9% | 75% | -3.0% | 47% | -0.1% | 50% |  |  |  |
| baseline_all_months | 36m | 104567 | +39.6% | +63.8% | +7.8% | +79.1% | 80% | -5.3% | 46% | -0.1% | 50% | -12.4% | 98% | 1 |

Rules: `first_oversold` = buy the close of the first month RSI < threshold. `rsi_recovery` = wait for the first monthly close with RSI back above the exit level. `rsi_recovery40` = wait for RSI ≥ 40. `dd>40%` rows restrict to episodes where the stock was already ≥ 40% below its trailing 5-year high at entry. `baseline_all_months` = unconditional forward returns of the same stocks sampled every month, the control the episode rows must beat.
