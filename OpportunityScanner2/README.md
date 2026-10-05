# OpportunityScanner2: overbought all-time high, then a monthly-RSI collapse

Study of the idea: *a stock gets very overbought on the monthly chart while it
makes all-time highs, then its monthly RSI drops more than ~32% from that peak;
that collapse marks a good buying area for a company with good fundamentals and
growth ahead.* Tested on today's S&P 500 + S&P 400 (899 tickers), monthly
candles 2000 – Aug 2026, fundamentals from SEC filings from 2009.

> Research tooling, not investment advice. Universe = today's index members
> (survivorship bias, see below), no costs or taxes.

## Short answer

1. **The RSI collapse on its own is not a bottom signal.** Since 2009 it fired
   1,486 times (669 stocks). Twelve months later the median stock was up 16.7%,
   the same as SPY (+0.5 points median, 51% beat SPY), and it did **worse than
   buying the same stock in a random month** (beat its own average 47% of the
   time, month-clustered −6.7 points, t = −3.7). It fires early: after the
   signal the median stock fell another **14.5%**, only 37% of signals were
   within 10% of the low of the following year, and a quarter fell another 25%+.
   No threshold fixes it: every combination of peak RSI 65–85 and drop 20–45%
   (or 15–35 points) sits between about 0 and −10 points versus the universe,
   month-clustered; none is positive.
2. **What works is the same idea with more damage done.** Keep the arming rule
   (an overbought all-time high) but wait until the price or the RSI is really
   washed out:

   | since 2009, 12 months after the signal | n | median | vs SPY (median) | beat own-stock average | 24m vs own |
   |---|---|---|---|---|---|
   | RSI −32% (the idea as stated) | 1486 | +16.7% | +0.5 | 47% | −1.0 |
   | RSI −32% and price ≥ 30% below ATH | 881 | +21.8% | +2.2 | 52% | +3.0 |
   | RSI −32% and price ≥ 40% below ATH | 513 | +28.2% | +4.3 | 58% | +17.1 |
   | former leader, monthly RSI < 40 | 562 | +29.2% | +4.2 | 65% | +16.7 |
   | former leader, monthly RSI < 35 | 276 | +43.0% | +10.4 | 80% | +31.9 |

   "Former leader" = made an all-time high with monthly RSI ≥ 70 in the last 36
   months. The price-40% and RSI<35 versions also beat the equal-weighted
   universe as 24-month portfolios (25.8% and 22.7% CAGR vs 22.5%; SPY 15.5%).
3. **Fundamentals matter, and "growth ahead" matters most.** With hindsight,
   signals whose revenue then grew ≥ 10% over the next year beat the universe
   by +5.6 points; those whose revenue shrank lagged by −15.7. The point-in-time
   filters help on the event level: "quality" (profitable now and in 2 of the 3
   past years, revenue growth ≥ 5%, EPS growing, no one-off gain, no
   acquisition-driven growth) and "cheap" (operating multiples in the bottom half
   of the company's own history). The acquisition check is the turnaround v3
   guard: diluted shares up more than 15%, or a jump in growth (≥ 15%, 3x and
   10 points above a year earlier) backed by new goodwill + intangibles (≥ 5% of
   revenue and ≥ 25% above their 24-month low). Since 2026-09-29 a growth jump
   without new goodwill (AAON, MasTec) counts as organic.
   * former leader + RSI < 35 + quality: 46 signals since 2009, median +48.8% in
     12 months, **89% beat their own stock's average**, month-clustered +24
     points (t = 5.1); last 5 years 19 signals, 84%.
   * RSI −32% + price −40% + quality + cheap: 152 signals, median +32.5%, 60%
     beat own average, +22.9 points at 24 months.

   The filters raise the share of signals that grew revenue the next year from
   77% to 85%. That is useful, but it leaves plenty of misses, so the forward
   view (guidance, estimates, the thesis) still has to be checked by hand.
4. **Timing tweaks do not help.** On the plain signal, waiting for the RSI to
   hook back up cost ~4 points (24-month return 29.6% vs 33.9% median). Waiting
   for another −15%, or for RSI < 40, only filled in 26–31% of cases. When the
   signal is right, buying at the signal was best. The fix is a stricter signal,
   not a later entry.

## How it is scored

* Monthly candles from daily Yahoo data; Wilder RSI(14) on the monthly close
  (same as TradingView and the turnaround scanner).
* **Arming month**: the month's high is a new all-time high, RSI ≥ 70, ≥ 5
  years of history. **Peak RSI**: the highest RSI of the arming months in the
  last 24 months. **Signal**: first month RSI ≤ peak × 0.68. After a signal the
  next one needs a new arming month.
* Entry at the signal month's close. Returns are total returns to the
  month-end close 3/6/12/24/36 months later. Liquid names only (3-month average
  dollar volume ≥ $5M).
* Yardsticks:
  * SPY.
  * The equal-weighted universe over the same months.
  * **The same stock's own average forward return** over 2009–2026, the
    fairest comparison. Every stock in the universe survived to today, so this
    nets out most of the survivorship lift and leaves the value of the timing.
* Month-clustered means average each calendar month first. Signals bunch up in
  sell-offs (2011, 2015, 2018, 2020, 2022), and t-statistics without this
  clustering would be far too optimistic.

### Caveats

* **Survivorship**: the universe is today's index members. Stocks that
  collapsed after a blow-off top and were dropped or went bust are missing.
  That flatters every "buy the drop" rule, and the deeper the drop the more it
  flatters (RSI<35 variants most). The own-stock comparison removes the level
  effect but not all of this.
* Fundamentals come from SEC XBRL filings, point in time, so filters only work
  from 2009. The quality filter uses only information public at the signal.
* Small samples for the strictest variants (46 and 19 signals); the
  month-clustered t-stats are the honest measure of confidence.
* The last 5 years are mixed for 24-month horizons: the 2022 signals recovered,
  but the 2024 ones are still out.

## Files

| File | What |
|---|---|
| `signals.py` | signal definitions (`Params`: `ob`, `drop`, `mode` rel/pts, `window`, `min_dd`, `max_rsi`, ...) |
| `common.py` | prices (`../turnaround_backtest/cache/prices`), universe, point-in-time fundamentals (`cache/fund_tables.pkl`, from `../turnaround_backtest_v3/screen_v3.py`), realized growth |
| `study.py` | event study: baselines, horizons, fundamentals filters, hindsight growth split, 87-config sweep, buckets, portfolios → `output/study.json`, `output/events_default.csv` |
| `timing.py` | own-stock baseline and entry-timing variants → `output/timing.json` |
| `variants.py` | head-to-head of the stricter variants, 3 periods × 3 filters, 24-month portfolios → `output/variants.json`, `output/events_<variant>.csv` |
| `yearly_backtest.py` | tier A (leader + RSI<35) + quality + cheap, 2010+, one calendar year of signals at a time, top 20 per year: hit rate of a +25% recovery within 12 months, time to hit, max gain, max drawdown, RSI-went-lower share, misses; plus the unfiltered trigger for comparison → `output/yearly_backtest.{md,json}`, `output/yearly_backtest_events.csv` |
| `yearly_backtest_v2.py` | same lists with the lessons from the losers: staples / utilities / materials only below RSI 30, half at the signal and half on a new monthly low close within 4 months with the RSI higher (`--t2-rule higher`, default), lower or any (`--window`, `--sector-rsi`, `--target`) → `output/yearly_backtest_v2[_lower|_any].{md,json}` and `_events.csv` |
| `yearly_backtest_weekly.py` | the same tier A list read on **weekly** candles (ATH week with weekly RSI ≥ 70 arms for 156 weeks, first weekly RSI < 35 buys, staples / utilities / materials only below 30, fundamentals as of the last month-end before the signal week), +20% target, top 20 per year; compares the list with the monthly one and shows a threshold / cap sensitivity (`--max-rsi`, `--sector-rsi`, `--target`) → `output/yearly_backtest_weekly_t20_sector30.{md,json}`, `_events.csv`; `--max-rsi 25 --sector-rsi 0` is the better weekly list → `output/yearly_backtest_weekly_rsi25_t20.*` |
| `compare_weekly_monthly.py` | side-by-side report of the weekly RSI < 25 and monthly RSI < 35 tier A lists (totals, year by year, depth of the decline, shared names and their two entries, misses, sectors) → `../reports/OpportunityScanner2 tier A weekly vs monthly - <date>.md` |
| `live.py` | today's list with tiers A/B/C and fundamentals → `output/live_<date>.csv/.json` |
| `live_weekly.py` | today's weekly list (weekly RSI < 25 signals with an open 12-month window, plus armed names under 30 as a watch set) with the monthly RSI next to it, a flag when the monthly tier A rule is met as well, quality / cheap / quality + cheap at the signal and the backtest's yearly rank (lowest signal RSI first, top 20) → `output/weekly_live_<date>.csv/.json`; shown on the web app's **Opportunity 2 weekly** tab (`/os2w`) |
| `report.py` | writes `../reports/OpportunityScanner2 candidates - <date>.md` from the newest live list |
| `export_web.py` | condenses study.json / timing.json / variants.json into `output/web_summary.json` for the web app's **Opportunity 2** tab (`/os2` in `../turnaround/app.py`) |

```
python study.py      # ~4 min (first run builds the fundamentals cache, +4 min; --rebuild to refresh it)
python timing.py     # ~1 min
python variants.py   # ~2 min
python yearly_backtest.py  # ~2 min; --target 0.20 --sector-rsi 30 (staples/utilities/materials only below RSI 30), --rank val
python yearly_backtest_v2.py  # ~2 min; sector rule + two-tranche entry
python yearly_backtest_weekly.py  # ~3 min; weekly-candle twin of yearly_backtest.py --target 0.20 --sector-rsi 30, with a monthly comparison
python yearly_backtest_weekly.py --max-rsi 25 --sector-rsi 0  # the weekly list that comes closest to the monthly one
python compare_weekly_monthly.py  # weekly vs monthly comparison report in ../reports
python live.py       # ~1-3 min (downloads Yahoo analyst estimates for the shortlisted names)
                     # after a month-end: refresh prices (python ../turnaround_backtest/data.py prices) and move
                     # common.LAST_MONTH to the new completed candle; the list, report and page label the months from it
python live_weekly.py # ~1 min; today's weekly list with the monthly RSI (the Opportunity 2 weekly tab reads the newest weekly_live_<date>.json)
python export_web.py # refresh the web page's summary; the page reads the newest live_<date>.json
python report.py     # today's candidates report (the page renders the newest one)
```

The deployed app (`ll-turnaround-strat` on Vercel) ships only `output/live_*.json` and
`output/web_summary.json` from this folder (see `../.vercelignore`); the page also renders the newest
`../reports/OpportunityScanner2 candidates - <date>.md`.

Refresh prices first with `python ../turnaround_backtest/data.py prices`, and
EDGAR tables with `python ../turnaround_backtest/data.py edgar`, then
`python study.py --rebuild`.

## Live tiers (`live.py`)

| Tier | Rule | History since 2009 (12m median / beat own average) |
|---|---|---|
| **A** | former overbought-ATH leader (last 36 months), monthly RSI < 40; ★ if < 35 | +29% / 65%; ★ +43% / 80% |
| **B** | RSI ≤ 68% of the 24-month peak **and** price ≥ 40% below ATH | +28% / 58% |
| **C** | RSI ≤ 68% of the 24-month peak (the rule as stated) | +17% / 47%: watchlist only |

Use A/B names that pass **quality** (and ideally **cheap**), then check the
forward story by hand. The live table also carries Yahoo's analyst forward EPS
growth. That figure is next year's (usually adjusted) EPS over trailing GAAP
EPS, so it runs high; use it only as a cross-check.
