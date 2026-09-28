# Turnaround candidates backtest v3: entry-data guards (2004 – Aug 2026)

Third backtest, kept apart from `../turnaround_backtest/` (first and second
backtests). Same data (Yahoo full-history prices in
`../turnaround_backtest/cache/prices/`, SEC EDGAR point-in-time tables in
`../turnaround/cache/edgar/`), same engine, same quarterly snapshots
(1 Jan / 1 Apr / 1 Jul / 1 Oct, 2004-01-01 to 2026-07-01) and the same rule
set as the second backtest's **re-screen + guide-cut proxy** scenario
(`rescreen_only`): organic-growth screen, top 20 by trailing revenue growth,
top 10 by valuation versus own history, max 10% per stock, trim half at +50%,
RSI(m) ≥ 90 exit, >100% winners sold to fund new names, spin-off re-screen,
guidance-cut proxy (TTM EPS ≥ 15% below entry within 12 months → sell),
yearly withdrawals. No position cap, no S&P parking.

> Research tooling, not investment advice. Same caveats as before: today's
> index constituents (survivorship bias), no taxes or costs, filings data
> from 2008 only, so 2009-start scenarios are the meaningful window.

The best variant, `both_opval`, is written up rule by rule with a side-by-side
comparison against backtest v2's `rescreen_only` in
[STRATEGY_both_opval.md](STRATEGY_both_opval.md).

## Why

The 2026-09-27 live run (`../reports/Turnaround top 20 - 2026-09-27.md`)
showed two ways the organic filter lets bad entry data through:

* **one-off EPS gains**: FIS (Worldpay stake gain) and Duolingo (deferred-tax
  release) ranked as the cheapest names on P/E because a non-operating item
  sat in trailing EPS. Such names look cheap at entry and then get sold by
  the guidance-cut proxy when the item rolls out of the trailing year.
* **acquisitions that step up gradually**: Amcor/Berry (57% "growth") passed
  the 60% quarter-to-quarter jump test because the merged revenue phased in
  over four quarters; FIS/Issuer Solutions and Dick's/Foot Locker likewise.

## Guards (`screen_v3.py`)

Computed only from figures public on the snapshot date, applied after the
organic filter and before the top-20 growth rank:

| Guard | Test | Catches |
|---|---|---|
| **one-off** | TTM net income > TTM operating income (net income cannot exceed operating income without a non-operating gain or a tax benefit); or one quarter lifted TTM net income by > 50% while TTM operating income rose < 25%; without operating income in the filings, a > 50% one-quarter jump in TTM EPS | FIS, DUOL, PINS (2024 tax-asset release), CSGP (near-zero EPS swinging 3.6x), GEN |
| **acq** | diluted shares up > 15% year over year (stock-financed deal or equity raise); or trailing revenue growth ≥ 15% that is ≥ 3x and ≥ 10 points above the growth reported a year earlier, when that earlier growth was not negative (cash-financed deal; a recovery from a decline is exempt) | AMCR (+46% shares), CELH (+55% shares), DKS (54% vs 3%) |
| **opval** (ranking variant) | valuation percentile from P/S, EV/EBITDA and EV/EBIT, dropping P/E | one-offs cannot make a name look cheap even if a guard misses them |

Variants: `ref` (organic screen only, identical to backtest v2's
`rescreen_only`), `oneoff`, `acq`, `both`, `both_opval`. Each from 2004-01-01
and from 2009-01-01.

## Run it

```
python screen_v3.py      # ~2 min: output/snapshots_<variant>.json/.csv and current_<variant>.json (today's list)
python backtest_v3.py    # ~2 min: output/results.json, report.md, <scenario>_trades.csv, *_equity.csv
```

## Results (run 2026-09-28)

| Scenario | IRR | Max DD | Final + withdrawn | Closed | Win rate | Avg closed | Median closed |
|---|---|---|---|---|---|---|---|
| ref (= v2 `rescreen_only`) | 14.0% | -38.0% | $945k | 118 | 71% | +39% | +40% |
| oneoff | 13.9% | -34.6% | $959k | 111 | 75% | +42% | +51% |
| acq | 14.3% | -30.6% | $1,025k | 119 | 76% | +41% | +36% |
| both | 14.0% | -35.4% | $954k | 117 | 77% | +41% | +37% |
| **both_opval** | **14.6%** | -33.7% | **$1,101k** | 119 | **79%** | **+45%** | +51% |
| SPY 2004, same withdrawals | 9.1% | -55% | $387k | | | | |
| ref_2009 | 22.9% | -38.1% | $1,197k | 119 | 71% | +39% | |
| oneoff_2009 | 22.7% | -35.3% | $1,231k | 112 | 74% | +40% | |
| acq_2009 | 23.3% | -30.6% | $1,309k | 120 | 76% | +40% | |
| both_2009 | 23.1% | -34.3% | $1,225k | 118 | 76% | +41% | |
| **both_opval_2009** | **23.7%** | -34.3% | **$1,444k** | 118 | **79%** | **+45%** | |
| SPY 2009, same withdrawals | 14.8% | -34% | $526k | | | | |

Full tables, year by year, and the snapshot-by-snapshot list of what each
guard removed are in `output/report.md`.

### Findings

* **The guards remove below-average entries.** Across the 91 snapshots the
  reference top 10 contained 677 names; the guards strike 138 of them (79
  one-off, 81 acquisition, some both). Most were never bought because the
  book was full or the name was already held; the 15 that were bought ended
  at a median of 0% and a 47% win rate (mean +8%), against +40% and 71% for
  all closed positions. The worst position of the whole history, FANG
  (-69%, Oct 2019 to Mar 2020), was an acquisition-guard case (shares +30%
  after the Energen deal); others struck were RRC -24%, ORA -12%, ALB -10%,
  MO -10%.
* **Drawdown falls more than return rises.** Both guards together trim the
  maximum drawdown from -38% to -35%; the acquisition guard alone gets it to
  -31% (the FANG / energy-deal cluster of 2019-20 is gone). The IRR is
  roughly unchanged (+0.0 to +0.4 points) because the guards also drop some
  winners (DLR +85%, COKE +69%, GEN +53%) and the replacements are ordinary.
* **Ranking on operating multiples is the better change.** `both_opval`
  beats every other variant on IRR, win rate (79%) and average closed return
  (+45%), from 2004 and from 2009. Its year-by-year returns differ from
  `both` mostly in 2020 (+38% vs +34%), 2025 (+20% vs +16%) and 2026 to
  August (+17% vs +9%).
* **Mechanical guide-cut exits do not fall much** (70 → 63-69 of about 140
  entries) because most guide-cut exits in the history are ordinary
  earnings declines, not one-off roll-offs.
* **Financials dominate the one-off strikes** (MET, HIG, CINF, MS, FHN,
  HBAN, JEF): insurers' and banks' trailing net income swings a lot without
  a change in operating income tag, or has no operating income tag at all.
  That is a feature for this strategy (their "growth" was rarely organic)
  but it does mean the one-off guard is partly a financials filter.

### Today's list (as of 2026-09-27, September candle two days short)

* `ref`: PODD, FIS, NOW, VEEV, APPF, DUOL, AMCR, PINS, CSGP, GEN
* `both`: PODD, KNSL, OLLI, INTU, DXCM, NOW, VEEV, APPF, BSX, PAYX
* `both_opval`: PODD, KNSL, APPF, OLLI, INTU, DT, NOW, DXCM, VEEV, BSX

The guards remove FIS, DUOL, PINS, CSGP and GEN (one-off) and AMCR, CELH and
DKS (acquisition) from today's top 20; KNSL, DXCM, OLLI, INTU, BSX, PAYX,
NFLX and VVV move up into it.

## Layout

```
screen_v3.py     extends ../turnaround_backtest/screen.py tables with the guard diagnostics
                 (ni_op, ni_jump4, op_jump4, eps_jump4, shares_yoy, prior_yoy, ev_ebit_pct, val_pct_op)
                 and writes one snapshot set per variant
backtest_v3.py   runs the rescreen_only rule set on every variant from 2004 and 2009
output/          snapshots_<variant>.json/.csv, current_<variant>.json, results.json, report.md,
                 <scenario>_trades.csv, <scenario>_equity.csv, spy_<year>_equity.csv
```
