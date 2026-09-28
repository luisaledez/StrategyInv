# Turnaround backtest: why the ten worst open positions lost, and what would have said "sell"

Companion to `turnaround_backtest/output/report.md` (base scenario, 2004-01-01 to 2026-08-31).
Numbers come from `turnaround_backtest/post_entry.py` (per-position, point-in-time) and from the four
new loss-control scenarios in `turnaround_backtest/backtest.py`. Company events come from public
filings and press coverage (sources at the end). Research tooling, not investment advice.

## 1. The ten positions

Price return is the report's figure. Total return adds dividends and spin-off distributions, which is
what the engine actually credits: RYN, MUR and LYB are not losses on that basis, just very poor uses
of capital for 12, 17 and 4 years.

| Ticker | Bought | Sector | TTM revenue growth the screen saw | Trailing P/E | Price vs cost | Total return | Worst point | Best point | Months to first -20% | TTM EPS 12 months later vs entry |
|---|---|---|---|---|---|---|---|---|---|---|
| TTD | 2025-10 | Comm. Services | +23% | 59 | -72% | -72% | -72% | +2% | 3 | +6% (9 mo) |
| LULU | 2024-10 | Cons. Discretionary | +13% | 21 | -55% | -55% | -57% | +55% | 10 | +13% |
| TAP | 2018-01 | Cons. Staples | +315% (MillerCoors consolidation) | 8 | -52% | -38% | -59% | -7% | 4 | -38% (3 mo, then missing) |
| KRC | 2021-07 | Real Estate | +6% | 13 | -48% | -31% | -61% | +10% | 12 | -72% |
| RYN | 2014-01 | Real Estate | -119% (bad data) | 10 | -35% | +18% | -35% | +36% | 18 | -59% |
| MOS | 2023-07 | Materials | +35% | 5 | -33% | -26% | -41% | +9% | 13 | -71% |
| BAH | 2025-07 | Industrials | +12% | 14 | -30% | -27% | -43% | +1% | 5 | -5% |
| MUR | 2009-07 | Energy | +50% | 6 | -23% | +39% | -87% | +42% | 73 | -53% |
| GIS | 2025-10 | Cons. Staples | +867% (bad data) | 10 | -19% | -14% | -33% | -7% | 6 | -23% (9 mo) |
| LYB | 2022-10 | Materials | +51% | 5 | -17% | +7% | -45% | +31% | 30 | -61% |

Dollar damage is concentrated in the large late entries, because the engine sizes a buy at 10% of
the portfolio out of whatever cash is idle: GIS ($31,261, the largest buy of the whole backtest),
MOS ($22,277), BAH ($16,696), KRC ($14,162) and RYN ($12,472) account for most of the $37,406
unrealised loss. TTD and LYB were small ($2,690 and $1,705).

## 2. What went wrong, position by position

**TTD (The Trade Desk).** Bought after two 30%+ single-day crashes in eight months (Feb 2025 first
revenue miss in 33 quarters; Aug 2025 CFO departure and a guide-down). Growth then decelerated every
quarter: +18%, +14%, +12%, +3%, and the Q3-2026 guide implied a revenue decline; 15% layoffs and
removal from the S&P 500 in Sept 2026. Amazon's DSP took share. Trailing EPS never fell 30%, so the
fundamentals rule never fired; the price made a new 5-year low in month 2.

**LULU (Lululemon).** Bought 48% below its Dec-2023 high after the Aug-2024 guidance cut. Six more
cuts followed (Mar, Jun, Sep 2025; Mar, Jun, Sep 2026), Americas comps went negative, the CEO left
in Dec 2025, Elliott took a stake, and by Sept 2026 revenue was -4% and comps -10%. Trailing EPS was
still +13% a year after purchase; the market re-rated the stock long before the reported numbers
broke. The stock did reach +55% in Dec 2024 (the engine trimmed half there) before rolling over.

**TAP (Molson Coors).** The +315% revenue growth and the 8x P/E were both artefacts of consolidating
MillerCoors in Oct 2016 (a one-time revaluation gain inflated TTM EPS to $10.53; recurring EPS was
about $4-5, so the real multiple was ~18x). Organic brand volumes were already negative in every 2017
quarter. Volumes fell again six weeks after purchase (Feb 2018), underlying EPS -40% in May 2018, a
$248M tax restatement and material weakness in Feb 2019, dividend suspended May 2020, $1.5B goodwill
impairment in Q4-2020, and the US beer market still shrinking in 2026.

**KRC (Kilroy Realty).** West Coast office REIT bought in July 2021 with occupancy already 2 points
below pre-COVID and sliding each quarter; Delta and Omicron reversed return-to-office in Aug-Nov 2021.
FFO kept growing into 2022 (so it screened cheap), then 2022 rate hikes took the stock down 40%,
occupancy went 92% to 77% by 2026, and FFO guidance fell from $4.69 to $3.49-3.63.

**RYN (Rayonier).** Three weeks after purchase it announced the spin-off of Performance Fibers, the
segment that produced most of the earnings (completed June 2014). In Nov 2014 it disclosed it had
been harvesting above sustainable levels, restated, cut the dividend and the stock fell 15% in a day.
The screen's revenue figure for 2013 was negative (a filings tagging problem, see section 5), so the
"growth" that put it in the top 20 was meaningless. Merged with PotlatchDeltic in Jan 2026.

**MOS (Mosaic).** Potash peaked at ~$865/t in April 2022 and had already halved by purchase; Q1-2023
(reported May 2023, before the buy) showed realised potash prices -20%. TTM revenue was still up
only because the second half of 2022 was in the window. Four weeks after purchase Q2 sales were -37%;
FY2023 EPS -67%, FY2024 $0.55, CFO and CEO changes, and in Aug 2026 it withdrew phosphate guidance
at a 5.5-year low.

**BAH (Booz Allen).** 98% government revenue, bought five weeks after a -16.5% day on FY26 guidance
below consensus and 2,500 layoffs, and after a GSA memo had named it among consultancies whose
contracts agencies should terminate. Revenue then went -8%, -10%, -4%; two guidance cuts, CFO exit.

**MUR (Murphy Oil).** The +50% revenue growth was the 2008 oil spike; by purchase two quarters had
already shown EPS down 60-75%. It rallied to +42% in 2011 (no rule captured that), then sold its
refineries, spun off Murphy USA in 2013, and as a pure E&P went through the 2014-16 crash and 2020
(-87% below cost at the low), with dividend cuts in 2016 and 2020.

**GIS (General Mills).** The screen saw +867% growth because the filings data carries a quarterly
revenue figure in the TTM slot for 2023-2025 (see section 5); real organic growth was about -3%. In
June 2025, before the buy, the company had already guided FY26 EPS down 10-15%. Cut again in Dec 2025
to -16/-20%, FY27 guided down again in July 2026. Monthly RSI at entry was 32 and hit 20 within six
months.

**LYB (LyondellBasell).** 2021-22 polyethylene spreads inflated revenue and EPS (P/E 4.7 on peak
earnings); Q2-2022 was already down and the refinery exit had been announced in April 2022. Three
weeks after purchase Q3 operating income was -62% quarter on quarter. The stock still ran to +31% in
early 2024 before the 2025 collapse, a net loss for FY2025 and a halved dividend in Feb 2026.

## 3. What they have in common

1. **The "growth" that got them into the top 20 was not organic in six of ten.** TAP was an
   acquisition; MOS, LYB and MUR were commodity-price peaks that had already turned in the most recent
   one or two quarters; GIS and RYN were filings-data artefacts. The screen ranks on trailing-twelve-month
   growth, which is at its most flattering exactly when the cycle has just turned.
2. **Cheap on peak earnings.** Median trailing P/E at entry was 9.9 for the losers versus 13.4 for
   the other 75 positions; MOS 5, LYB 5, MUR 6, TAP 8, GIS 10. A low multiple on a cyclical or one-off
   EPS base is the classic peak-earnings trap. The valuation-vs-own-history percentile cannot see this
   because the history it compares against is the same inflated number.
3. **The earnings base collapsed fast.** Trailing EPS fell 30% below its entry level within a median
   of 4 months for the losers (MUR 3, RYN 3, TAP 2, MOS 4, LYB 8, GIS 10, KRC 12) against 12 months for
   the others; a year after purchase the losers' EPS was down 59% at the median versus 11%.
4. **They never got going.** The losers' best point after entry was +9% at the median versus +110%
   for the others, and at 12 months they were -18% versus +9%. But note the winners did dip: the median
   non-loser hit -20% in month 6 and 13 of 75 were still down 20%+ at month 12 before recovering.
5. **Secular or policy shocks, not cyclical dips**, for the four most recent ones: Amazon in ad-tech
   (TTD), brand fatigue and competition (LULU), DOGE and federal spending (BAH), volume declines and
   private label in packaged food (GIS). Mean reversion never arrived because the mean moved. The
   screen's trailing numbers looked fine for TTD, LULU and BAH; the deterioration was only visible in
   guidance, sequential growth and price.
6. **Guidance had already been cut, or was cut within two quarters, in every recent case**: BAH and
   GIS before the buy; TTD, LULU, MOS, LYB, TAP within 1-6 months after. Senior departures followed
   in TTD (CFO), LULU (CPO, CEO), BAH (CFO), MOS (CFO, CEO), KRC (CEO), RYN (CEO, EVP).
7. **Sector.** Materials, Energy, Real Estate and Consumer Staples hold 7 of the 10 losers but only
   34 of 85 positions; their average total return was +61% to +112% against +192% for everything else.
8. **Corporate actions changed the company** shortly after entry (RYN and MUR spin-offs, LYB refinery
   exit), and dividend cuts or suspensions followed in RYN, MUR, TAP and LYB.
9. **Most are recent.** Seven of the ten were bought in or after 2021; the 29 post-2021 entries average
   +39% with 11 below cost, against +221% for earlier entries. The base strategy's winners typically
   needed years (median closed hold 51 months), so part of the "loss" is unripe positions.

## 4. Which sell rules would actually have helped

### Per position, first with no reinvestment, then with proceeds parked in SPY

Every rule was applied at month-ends to all 85 base positions. Measured against simply holding to the
position's actual exit (or Aug 2026), **every mechanical rule loses money**: stops of 20/30/40%, a
30% trailing stop, monthly RSI below 30, new 5-year lows, 12- or 24-month time stops, revenue growth
turning negative, EPS down 30/50%. They save a few thousand dollars on the ten losers and cost
hundreds of thousands on winners that dipped first (GME, FIVE, SGI, SSD all traded below cost early).

With the sale proceeds put into SPY until the position's horizon, the ranking flips for the
fundamental rules: **sell when point-in-time TTM EPS is 30% below its entry level** helped 26
positions by more than 10 points and hurt 20, for roughly +$400k of extra ending value across the 85
positions; the 12-month time stop and "revenue growth negative while underwater" were next. Price
stops stayed near zero (stop 30%) or negative (stop 40%, RSI below 30) even with reinvestment.

For the ten losers the EPS -30% rule would have exited seven of them early and mostly near cost:
MUR month 3 at +6%, RYN month 3 at +7%, LYB month 8 at +22%, MOS month 4 at +1%, TAP month 2 at -8%,
GIS month 10 at -25%, KRC month 12 at -23%. It never fires on TTD, LULU or BAH, whose trailing EPS
held up while the stock collapsed.

### As full portfolio scenarios (proper reinvestment into the next quarter's picks)

Four scenarios were added to `backtest.py`, all otherwise identical to `base`:

| Scenario | Final + withdrawn | IRR | Max DD | Closed | Win rate |
|---|---|---|---|---|---|
| base | $580,894 | 11.2% | -46.3% | 53 | 100% |
| eps_dn30: sell at a month-end when TTM EPS is 30% below entry | $668,338 | 12.2% | -42.2% | 125 | 70% |
| eps_dn30_uw: same, only while below cost | $645,551 | 12.0% | -44.0% | 99 | 65% |
| stop25: sell at a month-end close 25% below cost | $512,208 | 10.7% | -34.7% | 102 | 58% |
| time12: sell if 12+ months held and below cost | $558,104 | 11.2% | -53.3% | 128 | 66% |
| rsi80 (existing): monthly RSI exit at 80 | $651,603 | 11.8% | -45.1% | 59 | 100% |

The EPS rule is the only loss-control exit that improves both return and drawdown, and the gain is
modest (+15% on ending wealth, +1 point of IRR) and noisy: it sold GME at -4% in Dec 2012 (the base
run's biggest winner, +340%) and still came out ahead because the freed cash went into other picks.
Its worst open list shrinks to TTD, LULU and RYN. A 25% stop cuts the maximum drawdown by a quarter
but costs return, which is the trade-off to expect from price stops in a strategy that deliberately
buys stocks that are already down 40-65%.

### Rules that could not be tested with this data but the research supports

* Sell on the first full-year guidance cut (or an initial guide below the prior year) within 12 months
  of purchase. This is the signal that fired on TTD, LULU, BAH and GIS, the four the EPS rule misses.
* Sell on a dividend cut or suspension, a restatement or a material weakness (RYN Nov 2014, TAP Feb
  2019, MUR 2016, LYB 2026).
* Treat a spin-off or major divestiture of more than about 30% of earnings as a new position and re-run
  the entry screen (RYN, MUR).
* Sell on a CEO or CFO departure that coincides with a miss or a guide-down.

## 5. Entry-side fixes suggested by the losers (more valuable than any sell rule)

1. **Reject non-organic growth.** Six of ten losers entered on growth from an acquisition, a
   commodity spike or a data artefact. Testable proxies: skip when TTM revenue growth is above 100%
   or negative; skip when the latest quarter's revenue is down year on year while the TTM figure is up
   (spike fading; would have caught MOS, LYB, MUR, TAP); require the TTM series to be continuous (no
   jump of more than 60% between consecutive readings).
2. **Fix the filings data.** GIS's `rev_ttm` in the EDGAR cache is a single quarter (~$2.0B) from
   2023-08 to 2025-02 and jumps to $19.5B in 2025-05, which produced the +867% growth; RYN's 2013
   `rev_ttm` is negative. Both are tag-selection problems in `turnaround/edgar.py`. Eight positions
   entered with growth above 100% or negative; they averaged +90% against +159% for the rest, and three
   of them are on this list.
3. **Be wary of a low absolute P/E.** Seventeen positions entered below 8x trailing earnings; four of
   them are on this list. The screen's "cheap versus own history" test is blind to peak earnings.
4. **Cap the position size in dollars, not only in percent.** The five biggest losers by dollars were
   the five biggest late buys.
5. **Sector tilt.** Materials, Energy and Real Estate delivered less than half the average return of
   the other sectors in this sample (n is small, so treat as a hint, not a rule).

## 6. Follow-up (same day): filings data fixed, second backtest run

**The EDGAR loader bug.** Three causes, all in `turnaround/edgar.py`: (1) tags were merged per period with
`Revenues` first, so a narrow line a company tags as `Revenues` only in its 10-K (GIS ~$2B, PG $28B,
AIT $18M) became the annual anchor while the year-to-date pieces came from the real total; (2) values were
taken from the latest filing, so after a spin-off the restated comparatives were subtracted from
unrestated ones (RYN: negative revenue in 2013; MUR: -$8.6B in 2012); (3) a restated annual refiled under a
slightly different start date replaced the original. The loader now builds each concept from one tag at
a time (revenue: the tag with the largest typical value leads), values every component as it was known
on the day the trailing year became public (point-in-time, no later restatements), drops readings whose
year-ago comparative was restated while the annual anchor was not (the two bases cannot be combined;
these are exactly the spin-off / discontinued-operations quarters), and guards revenue against
non-positive readings and unsupported jumps. Every table keeps a `warnings` list of what was done.
92 of 898 tickers had non-positive or jumping revenue series before; the ones left are genuine (cruise
lines in 2021, reported annual figures after a spin-off) or bank revenue tags. All 903 tables were
re-extracted from the cached raw facts; the previous outputs are kept in `output/before_edgar_fix/`.

**Effect on the first backtest.** 57 of 74 non-empty snapshots changed at least one top-10 name (99 names
out, 99 in); GIS left four lists, RYN three, and JEF, LUV, NOV, DVN two each. The base scenario improved
on the corrected data, mostly through a smaller drawdown:

| Scenario | Final + withdrawn before → after | IRR | Max DD |
|---|---|---|---|
| base | $580,894 → $673,984 | 11.2% → 12.0% | -46.3% → -37.3% |
| base_2009 | $741,275 → $860,181 | 18.4% → 19.7% | -47.1% → -36.7% |
| eps_dn30 | $668,338 → $751,695 | 12.2% → 12.7% | -42.2% → -43.4% |
| time12 | $558,104 → $771,186 | 11.2% → 12.9% | -53.3% → -40.4% |
| stop25 | $512,208 → $522,877 | 10.7% → 10.7% | -34.7% → -26.7% |

**Second backtest** (`turnaround_backtest/backtest_v2.py`, outputs in `output_v2/`, the first backtest's
`output/` untouched). Rules added to the base scenario: organic-growth entries only (trailing revenue
growth in [0%, 100%), no >60% quarter-to-quarter jump of the trailing figure in eight quarters, latest
quarter not below its year-ago quarter), fewer than 15 stocks (cap 14; a full book admits a new name only
by selling a >100% winner that left the list), S&P 500 correction parking (SPY 10% or more below its
one-year high: no new stocks, idle cash into SPY until the drawdown is back within 5%; SPY then funds the
next new names), the spin-off / divestiture re-screen (a holding whose filings re-base by ≥ 30% is sold at
that month-end unless it is on the current top-10 list), and a guidance-cut proxy (no guidance data
exists here: TTM EPS ≥ 15% below its entry level within the first 12 months → sell).

| Scenario (organic entries throughout) | Final + withdrawn | IRR | Max DD | Closed | Win rate |
|---|---|---|---|---|---|
| first backtest base, for reference | $673,984 | 12.0% | -37.3% | 53 | 100% |
| organic_only (base rules + entry filter) | $833,336 | 13.2% | -34.1% | 60 | 100% |
| rescreen_only (+ re-screen + guide-cut proxy) | $945,433 | 14.0% | -38.0% | 118 | 71% |
| cap14_only (+ cap only) | $610,994 | 11.6% | -44.3% | | |
| park_only (+ parking only) | $494,897 | 9.9% | -51.5% | | |
| v2 (all rules) | $541,520 | 10.3% | -51.5% | 70 | 77% |
| v2_no_park | $668,077 | 12.2% | -33.2% | 84 | 75% |
| v2_eps30 | $485,167 | 9.8% | -51.5% | | |
| base_2009, for reference | $860,181 | 19.7% | -36.7% | | |
| v2_2009 | $970,163 | 20.3% | -31.0% | 70 | 77% |
| v2_no_park_2009 | $820,582 | 20.0% | -33.5% | | |

What the pieces did:

* **Organic-growth filter**: the single most useful change (+1.2 points of IRR, lower drawdown), and it
  removes TAP, MOS, LYB, MUR, GIS and RYN from the entries by construction. TTD, LULU, KRC and BAH still get
  bought: their trailing growth was organic.
* **Re-screen and guidance proxy**: 70 sales in the first year on the EPS proxy; it caught MTDR (-86%),
  IVZ, RRC, RL, FSLR and BBY early but also sold DECK (+52%), GEN (+55%) and AKAM (+42%) whose EPS dipped
  on the way up. Net effect positive (14.0% IRR) because the freed cash bought the next quarter's names.
  The spin-off re-screen fired only 8 times in 22 years; one (MTB, 0.16x) is a bank revenue-tag artefact.
* **Cap at 14 stocks**: costs return (11.6% versus 13.2%) and does not reduce the drawdown, because the
  strategy's winners take years and a full book blocks new entries; the base run averages 25-35 holdings.
* **S&P correction parking**: the most sensitive rule. From the 2004 start the idle pre-2008 cash (no
  candidates exist before 2008 in this data set) is parked in SPY in January 2008 and rides the crash;
  from the 2009 start the same rule parks the whole $100,000 in SPY on 2 January 2009 (a correction by
  any measure) and misses the 2009 stock entries, yet still ends slightly ahead of the no-parking variant
  (20.3% versus 20.0% IRR) with the lowest drawdown of any run (-31%), thanks to the 2018, 2020, 2022 and
  2025 parks. SPY buys total $554k over the 2009 run; the position was open at the end (+65% since Feb 2022).
  Whether parking helps therefore depends entirely on whether a 10% correction becomes a bear market.
* **All rules together, 2009 start**: 20.3% IRR, -31% drawdown, 14 stocks at most, 77% win rate, median hold
  12 months, worst open position LULU (-55%), no other open loss beyond -9%.

Caveats unchanged: survivorship bias (today's index members), no costs or taxes, and the guidance proxy is
a stand-in for real guidance data.

## Sources (selection)

TTD: CNBC 2025-08-08 (CFO exit, Amazon competition); MediaPost 2025-02-13 (first miss in 33 quarters);
Digiday Feb 2026 (Q1-26 guide); Adweek Aug 2026 (15% layoffs). LULU: CNBC 2024-08-29, 2025-06-05,
2025-12-11, 2026-06-04, 2026-09-03. BAH: Washington Technology May 2025 (7% workforce cut); Semafor
2025-04-10 (DOGE); BAH 8-K 2026-05-22. GIS: press releases 2025-06-25 and 2025-09-17; Investing.com
2025-12-17 and 2026-09-23. KRC: 8-Ks Q2/Q3-2021; BusinessWire 2023-12-14 (CEO transition);
Investing.com Q2-2026 (77% occupancy). TAP: IR release 2018-02-14; Zacks 2018-05-02; CFO.com Feb 2019
(restatement); 10-Q 2021 (goodwill impairment). RYN: BusinessWire 2014-06-30 (spin-off) and 2014-11-10
(restatement, dividend cut). MOS: 8-Ks Q1 and Q2 2023; 10-K 2024. MUR: 8-K Q2-2009; 8-Ks 2016-08-03
and 2020-04-01 (dividend cuts). LYB: 8-K Q3-2022; 2025 results release; IR 2026-02-20 (dividend cut).
