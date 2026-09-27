# Synthetic lost decade (1968-1982 market, seed 0) — 1968-01-01 to 1982-08-31

Quarterly scan (1 Jan / 1 Apr / 1 Jul / 1 Oct) with the turnaround scanner's rules (monthly RSI(14) < 42 within the last 6 completed months, ≥ 5 years of history, ≥ $5M average daily dollar volume, ≥ $1B market cap), then: profitable now and in the past, top 20 by trailing-twelve-month revenue growth, top 10 of those by valuation versus the company's own history (mean percentile of trailing P/E, P/S and EV/EBITDA). $100,000 start, at most 10% of the portfolio per stock, no taxes, commissions or slippage, dividends credited as cash, idle cash earns nothing.

Withdrawal rule at each year end: year return > 20% → 10% of the portfolio; 10–20% → 7.5%; below 10% (including losses) → 5%. The partial year 2026 has no withdrawal.

**Synthetic data.** The market is the real S&P 500 daily path from 1962 to August 1982 (Yahoo ^GSPC); each of today's S&P 500 + 400 stocks is re-simulated on it with its own real beta and a block bootstrap of its own real idiosyncratic daily returns (2004-2026), so single-stock crashes and rebounds are realistic while the market goes nowhere. Quarterly fundamentals are generated: revenue grows with CPI inflation plus a company-specific real rate plus part of the stock's own price residual; net margins swing with the stock's residual and the market and can turn negative; EBITDA, debt, cash, shares and the starting market cap are scaled from each company's latest real filing. Dividend yield 3.5%. The benchmark 'Index' is the S&P 500 price path with the same dividends reinvested.

**Read it as a stress test, not a forecast.** Nothing in the generated fundamentals knows the future price, and nothing in the prices knows the fundamentals beyond the contemporaneous link above, so the selection rules cannot cheat. Real (inflation-adjusted) figures use BLS CPI-U annual averages: the CPI rose about 180% over the window, so a nominal result must roughly triple just to stand still.

## Scenario summary

| Scenario | Start | First buy | Final value | Withdrawn | Final + withdrawn | CAGR (final) | CAGR (no-withdrawal index) | IRR | Max DD | Closed trades | Win rate | Avg closed ret. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **base** | 1968 | 1968-01-02 | $133,894 | $137,730 | $271,624 | +2.0% | +9.9% | +10.4% | -49.0% | 21 | +100.0% | +85.4% |
| **no_trim** | 1968 | 1968-01-02 | $142,229 | $142,166 | $284,395 | +2.4% | +10.4% | +10.9% | -49.6% | 22 | +100.0% | +109.5% |
| **rotate** | 1968 | 1968-01-02 | $177,030 | $122,828 | $299,858 | +4.0% | +12.0% | +10.3% | -46.9% | 338 | +57.7% | +5.7% |
| **base_no_wd** | 1968 | 1968-01-02 | $430,380 | $0 | $430,380 | +10.5% | +10.5% | +10.5% | -46.6% | 26 | +100.0% | +98.7% |
| **rsi80** | 1968 | 1968-01-02 | $125,959 | $136,165 | $262,124 | +1.6% | +9.5% | +10.1% | -49.0% | 23 | +100.0% | +77.5% |
| Index (1968) | 1968 | 1968-01-02 | $76,803 | $85,432 | $162,236 | -1.8% | +5.1% | +4.8% | -44.9% |  |  |  |

CAGR (final) compounds the ending value after withdrawals; the no-withdrawal index chains the yearly returns as if nothing had been taken out; IRR is the money-weighted return of the $100,000 in, the withdrawals out and the final value. Max DD is on the no-withdrawal index.

## base — Base: trim half at +50%, hold rest, RSI(m) 90 exit, replace >100% winners

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +8.1% | $5,405 | $102,692 | $5,405 | 13 | +0.0% | 13 | 14 | +11.9% |
| 1969 | $102,692 | -4.7% | $4,893 | $92,966 | $10,298 | 16 | +3.4% | 3 | 1 | -8.2% |
| 1970 | $92,966 | +21.8% | $11,326 | $101,937 | $21,624 | 20 | +0.0% | 5 | 24 | +3.6% |
| 1971 | $101,937 | +38.5% | $14,122 | $127,099 | $35,746 | 23 | +0.0% | 6 | 30 | +14.7% |
| 1972 | $127,099 | +38.0% | $17,537 | $157,837 | $53,284 | 25 | +0.8% | 5 | 10 | +19.7% |
| 1973 | $157,837 | -21.7% | $6,180 | $117,425 | $59,464 | 28 | +0.0% | 4 | 30 | -14.4% |
| 1974 | $117,425 | -25.8% | $4,357 | $82,789 | $63,821 | 31 | +0.0% | 3 | 33 | -27.2% |
| 1975 | $82,789 | +36.9% | $11,331 | $101,980 | $75,152 | 33 | +0.0% | 3 | 37 | +36.2% |
| 1976 | $101,980 | +33.2% | $13,586 | $122,277 | $88,739 | 35 | +0.0% | 3 | 40 | +23.4% |
| 1977 | $122,277 | +1.7% | $6,217 | $118,115 | $94,955 | 36 | +0.0% | 4 | 40 | -8.4% |
| 1978 | $118,115 | +12.9% | $10,004 | $123,387 | $104,960 | 37 | +0.0% | 3 | 42 | +4.6% |
| 1979 | $123,387 | +12.3% | $10,389 | $128,126 | $115,348 | 40 | +0.0% | 3 | 43 | +16.3% |
| 1980 | $128,126 | +22.9% | $15,747 | $141,722 | $131,095 | 41 | +0.0% | 3 | 50 | +30.3% |
| 1981 | $141,722 | -6.4% | $6,635 | $126,064 | $137,730 | 41 | +0.0% | 4 | 47 | -6.5% |
| 1982 (to Aug) | $126,064 | +6.2% | $0 | $133,894 | $137,730 | 43 | +0.6% | 2 | 1 | -0.8% |

Final value $133,894, withdrawn $137,730, 506 trades, 21 closed positions (win rate +100.0%, average closed return +85.4%, median hold 41.9 months), 43 still open.

Sell reasons: withdrawal × 378, trim +50% × 43, replaced × 21

Open positions at the end: 43, of which 25 below cost (unrealised loss $-35,073). Largest: DY (+47%, since 1981-01), CVX (-9%, since 1980-10), VRSK (-2%, since 1977-07), CL (-10%, since 1977-04), COO (-31%, since 1981-04), HRL (+79%, since 1979-04), CGNX (+97%, since 1968-01), ADC (+9%, since 1978-10), STZ (+74%, since 1971-04), TPL (-25%, since 1981-07), NEU (+94%, since 1968-07), DD (-14%, since 1979-07), MKC (+34%, since 1974-04), BXP (+37%, since 1968-01), TMO (+20%, since 1980-07)

Worst open: OLED (-76%, since 1972-04), SYF (-74%, since 1972-10), WDAY (-71%, since 1968-01), INCY (-68%, since 1976-04), CDE (-59%, since 1974-10), AYI (-55%, since 1978-07), WAT (-54%, since 1969-04), UNM (-54%, since 1973-04), DTM (-50%, since 1973-01), CVLT (-49%, since 1972-07)

Best closed: CF $12,880 (+129%), DAL $10,459 (+105%), SNPS $9,555 (+77%), AR $9,276 (+93%), MMS $9,218 (+92%)
Worst closed: KIM $663 (+79%), GOOG $725 (+85%), NXPI $746 (+91%), MU $827 (+83%), OTIS $838 (+75%)

## no_trim — No trim: hold until RSI(m) 90 exit or replaced

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +8.5% | $5,424 | $103,062 | $5,424 | 13 | +0.0% | 13 | 13 | +11.9% |
| 1969 | $103,062 | -5.5% | $4,872 | $92,571 | $10,296 | 16 | +0.0% | 3 | 16 | -8.2% |
| 1970 | $92,571 | +24.1% | $11,487 | $103,381 | $21,783 | 20 | +0.0% | 5 | 21 | +3.6% |
| 1971 | $103,381 | +47.6% | $15,255 | $137,299 | $37,039 | 24 | +0.0% | 7 | 27 | +14.7% |
| 1972 | $137,299 | +31.5% | $18,057 | $162,516 | $55,096 | 27 | +0.0% | 6 | 30 | +19.7% |
| 1973 | $162,516 | -23.9% | $6,187 | $117,545 | $61,283 | 30 | +0.0% | 3 | 30 | -14.4% |
| 1974 | $117,545 | -24.2% | $4,453 | $84,602 | $65,735 | 33 | +0.0% | 3 | 33 | -27.2% |
| 1975 | $84,602 | +36.2% | $11,524 | $103,713 | $77,259 | 35 | +0.0% | 3 | 36 | +36.2% |
| 1976 | $103,713 | +35.7% | $14,070 | $126,631 | $91,329 | 37 | +0.0% | 3 | 38 | +23.4% |
| 1977 | $126,631 | -0.4% | $6,309 | $119,866 | $97,638 | 39 | +0.0% | 6 | 43 | -8.4% |
| 1978 | $119,866 | +14.1% | $10,259 | $126,531 | $107,897 | 40 | +0.0% | 3 | 42 | +4.6% |
| 1979 | $126,531 | +14.0% | $10,814 | $133,367 | $118,711 | 42 | +0.0% | 3 | 43 | +16.3% |
| 1980 | $133,367 | +24.0% | $16,536 | $148,823 | $135,247 | 45 | +0.0% | 5 | 47 | +30.3% |
| 1981 | $148,823 | -7.0% | $6,919 | $131,464 | $142,166 | 45 | +0.0% | 4 | 49 | -6.5% |
| 1982 (to Aug) | $131,464 | +8.2% | $0 | $142,229 | $142,166 | 47 | +0.0% | 2 | 0 | -0.8% |

Final value $142,229, withdrawn $142,166, 537 trades, 22 closed positions (win rate +100.0%, average closed return +109.5%, median hold 42.0 months), 47 still open.

Sell reasons: withdrawal × 446, replaced × 22

Open positions at the end: 47, of which 28 below cost (unrealised loss $-31,651). Largest: DY (+47%, since 1981-01), CVX (-9%, since 1980-10), STZ (+74%, since 1971-04), COO (-31%, since 1981-04), CNC (-38%, since 1980-10), EOG (+68%, since 1979-10), CGNX (+97%, since 1968-01), POR (-28%, since 1977-04), EXE (-10%, since 1972-01), BXP (+37%, since 1968-01), CBSH (+21%, since 1968-01), ZBH (-1%, since 1980-10), ADC (+9%, since 1978-10), BBWI (-48%, since 1971-10), LHX (-10%, since 1970-07)

Worst open: OLED (-76%, since 1972-04), SYF (-74%, since 1972-10), WDAY (-71%, since 1968-01), INCY (-68%, since 1976-04), CDE (-59%, since 1974-10), AYI (-55%, since 1978-07), WAT (-54%, since 1969-04), UNM (-54%, since 1973-04), CVLT (-49%, since 1972-07), MTB (-49%, since 1973-07)

Best closed: CF $19,116 (+191%), MDT $13,565 (+111%), DAL $13,527 (+135%), AR $11,596 (+116%), MMS $11,024 (+110%)
Worst closed: NXPI $840 (+103%), KIM $894 (+105%), GOOG $1,000 (+114%), JAZZ $1,064 (+104%), MU $1,135 (+114%)

## rotate — Rotate: hold exactly the current top 10 each quarter

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +23.1% | $12,305 | $110,748 | $12,305 | 10 | +0.0% | 25 | 25 | +11.9% |
| 1969 | $110,748 | -16.4% | $4,630 | $87,973 | $16,936 | 10 | +2.0% | 27 | 27 | -8.2% |
| 1970 | $87,973 | +4.4% | $4,593 | $87,266 | $21,528 | 10 | +0.3% | 19 | 19 | +3.6% |
| 1971 | $87,266 | +8.9% | $4,752 | $90,296 | $26,281 | 10 | +0.0% | 19 | 29 | +14.7% |
| 1972 | $90,296 | +22.5% | $11,065 | $99,588 | $37,346 | 10 | +0.7% | 22 | 22 | +19.7% |
| 1973 | $99,588 | -20.6% | $3,955 | $75,144 | $41,301 | 10 | +0.0% | 22 | 32 | -14.4% |
| 1974 | $75,144 | -25.7% | $2,791 | $53,020 | $44,092 | 10 | +0.0% | 25 | 35 | -27.2% |
| 1975 | $53,020 | +60.3% | $8,498 | $76,484 | $52,590 | 10 | +0.0% | 19 | 29 | +36.2% |
| 1976 | $76,484 | +36.7% | $10,457 | $94,115 | $63,047 | 10 | +0.0% | 27 | 37 | +23.4% |
| 1977 | $94,115 | +15.0% | $8,117 | $100,108 | $71,164 | 10 | +0.0% | 26 | 36 | -8.4% |
| 1978 | $100,108 | +12.6% | $8,451 | $104,234 | $79,615 | 10 | +1.2% | 25 | 25 | +4.6% |
| 1979 | $104,234 | +41.2% | $14,722 | $132,499 | $94,337 | 10 | +0.0% | 21 | 31 | +16.3% |
| 1980 | $132,499 | +50.3% | $19,920 | $179,280 | $114,257 | 10 | +0.0% | 26 | 36 | +30.3% |
| 1981 | $179,280 | -4.4% | $8,570 | $162,836 | $122,828 | 10 | +0.0% | 26 | 36 | -6.5% |
| 1982 (to Aug) | $162,836 | +8.7% | $0 | $177,030 | $122,828 | 10 | +5.6% | 19 | 19 | -0.8% |

Final value $177,030, withdrawn $122,828, 786 trades, 338 closed positions (win rate +57.7%, average closed return +5.7%, median hold 3.1 months), 10 still open.

Sell reasons: left list × 338, withdrawal × 100

Open positions at the end: 10, of which 4 below cost (unrealised loss $-5,693). Largest: DPZ (+79%, since 1982-07), YETI (+17%, since 1982-04), AGCO (+17%, since 1982-07), TRV (+13%, since 1982-07), COST (+12%, since 1982-07), HPQ (-3%, since 1982-01), TKR (+4%, since 1982-07), SBRA (-0%, since 1982-07), FCX (-10%, since 1982-04), TPR (-22%, since 1982-01)

Worst open: TPR (-22%, since 1982-01), FCX (-10%, since 1982-04), HPQ (-3%, since 1982-01), SBRA (-0%, since 1982-07)

Best closed: SFM $11,525 (+64%), VAL $10,368 (+99%), ULTA $8,666 (+60%), MUR $7,770 (+52%), CDE $7,099 (+55%)
Worst closed: DY $-6,680 (-37%), CPT $-5,476 (-27%), TXT $-5,264 (-32%), DD $-4,849 (-27%), HXL $-4,489 (-57%)

## base_no_wd — Base without withdrawals

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +8.1% | $0 | $108,096 | $0 | 13 | +0.9% | 13 | 1 | +11.9% |
| 1969 | $108,096 | -5.0% | $0 | $102,729 | $0 | 17 | +8.1% | 4 | 1 | -8.2% |
| 1970 | $102,729 | +22.4% | $0 | $125,735 | $0 | 20 | +7.4% | 5 | 6 | +3.6% |
| 1971 | $125,735 | +36.4% | $0 | $171,481 | $0 | 24 | +0.8% | 7 | 7 | +14.7% |
| 1972 | $171,481 | +36.9% | $0 | $234,775 | $0 | 26 | +13.2% | 5 | 11 | +19.7% |
| 1973 | $234,775 | -19.6% | $0 | $188,768 | $0 | 30 | +0.9% | 5 | 2 | -14.4% |
| 1974 | $188,768 | -24.9% | $0 | $141,702 | $0 | 34 | +0.9% | 4 | 2 | -27.2% |
| 1975 | $141,702 | +39.1% | $0 | $197,144 | $0 | 37 | +1.4% | 4 | 5 | +36.2% |
| 1976 | $197,144 | +28.5% | $0 | $253,285 | $0 | 40 | +2.1% | 4 | 5 | +23.4% |
| 1977 | $253,285 | +5.1% | $0 | $266,191 | $0 | 42 | +0.9% | 5 | 5 | -8.4% |
| 1978 | $266,191 | +13.3% | $0 | $301,637 | $0 | 44 | +4.1% | 4 | 6 | +4.6% |
| 1979 | $301,637 | +11.7% | $0 | $336,961 | $0 | 48 | +4.2% | 4 | 3 | +16.3% |
| 1980 | $336,961 | +26.2% | $0 | $425,279 | $0 | 49 | +11.1% | 5 | 13 | +30.3% |
| 1981 | $425,279 | -6.5% | $0 | $397,491 | $0 | 50 | +1.6% | 5 | 7 | -6.5% |
| 1982 (to Aug) | $397,491 | +8.3% | $0 | $430,380 | $0 | 51 | +0.6% | 3 | 3 | -0.8% |

Final value $430,380, withdrawn $0, 154 trades, 26 closed positions (win rate +100.0%, average closed return +98.7%, median hold 40.5 months), 51 still open.

Sell reasons: trim +50% × 51, replaced × 26

Open positions at the end: 51, of which 31 below cost (unrealised loss $-96,204). Largest: DY (+47%, since 1981-01), CVX (-9%, since 1980-10), ZBH (+6%, since 1981-01), TPL (-25%, since 1981-07), TMO (+20%, since 1980-07), DD (-14%, since 1979-07), ADC (+9%, since 1978-10), FCX (-10%, since 1982-04), POR (-28%, since 1977-04), STZ (+74%, since 1971-04), EOG (+68%, since 1979-10), DTM (-50%, since 1973-01), CNC (-38%, since 1980-10), CGNX (+97%, since 1968-01), MRSH (+22%, since 1973-01)

Worst open: OLED (-76%, since 1972-04), SYF (-74%, since 1972-10), WDAY (-71%, since 1968-01), INCY (-70%, since 1976-01), ORA (-68%, since 1978-04), CDE (-59%, since 1974-10), IFF (-57%, since 1974-01), AYI (-55%, since 1978-07), WAT (-54%, since 1969-04), UNM (-54%, since 1973-04)

Best closed: MDT $23,463 (+95%), HPQ $18,657 (+107%), CPRT $15,552 (+103%), SNPS $15,359 (+82%), RF $14,993 (+93%)
Worst closed: GOOG $833 (+88%), NXPI $950 (+116%), CELH $1,162 (+116%), KIM $1,179 (+81%), ENTG $1,350 (+101%)

## rsi80 — Base with the monthly-RSI exit at 80 instead of 90

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +8.1% | $5,405 | $102,692 | $5,405 | 13 | +0.0% | 13 | 14 | +11.9% |
| 1969 | $102,692 | -4.7% | $4,893 | $92,966 | $10,298 | 16 | +3.4% | 3 | 1 | -8.2% |
| 1970 | $92,966 | +21.8% | $11,326 | $101,937 | $21,624 | 20 | +0.0% | 5 | 24 | +3.6% |
| 1971 | $101,937 | +37.2% | $13,984 | $125,856 | $35,608 | 23 | +0.0% | 6 | 30 | +14.7% |
| 1972 | $125,856 | +38.6% | $17,437 | $156,931 | $53,045 | 25 | +0.8% | 5 | 10 | +19.7% |
| 1973 | $156,931 | -21.7% | $6,147 | $116,785 | $59,191 | 28 | +0.0% | 4 | 30 | -14.4% |
| 1974 | $116,785 | -25.8% | $4,335 | $82,362 | $63,526 | 31 | +0.0% | 3 | 33 | -27.2% |
| 1975 | $82,362 | +36.5% | $11,243 | $101,185 | $74,769 | 33 | +0.0% | 3 | 37 | +36.2% |
| 1976 | $101,185 | +33.0% | $13,454 | $121,082 | $88,223 | 35 | +0.0% | 3 | 40 | +23.4% |
| 1977 | $121,082 | +0.5% | $6,085 | $115,619 | $94,308 | 36 | +0.0% | 4 | 40 | -8.4% |
| 1978 | $115,619 | +14.1% | $9,891 | $121,992 | $104,199 | 36 | +0.0% | 4 | 41 | +4.6% |
| 1979 | $121,992 | +11.3% | $10,186 | $125,627 | $114,385 | 39 | +0.0% | 3 | 42 | +16.3% |
| 1980 | $125,627 | +22.6% | $15,398 | $138,579 | $129,783 | 41 | +0.0% | 4 | 49 | +30.3% |
| 1981 | $138,579 | -7.9% | $6,383 | $121,270 | $136,165 | 41 | +0.0% | 4 | 47 | -6.5% |
| 1982 (to Aug) | $121,270 | +3.9% | $0 | $125,959 | $136,165 | 43 | +0.6% | 2 | 1 | -0.8% |

Final value $125,959, withdrawn $136,165, 505 trades, 23 closed positions (win rate +100.0%, average closed return +77.5%, median hold 42.0 months), 43 still open.

Sell reasons: withdrawal × 376, trim +50% × 40, replaced × 17, RSI(m) 81 × 3, RSI(m) 80 × 2, RSI(m) 83 × 1

Open positions at the end: 43, of which 26 below cost (unrealised loss $-38,252). Largest: DY (+47%, since 1981-01), CVX (-9%, since 1980-10), CL (-10%, since 1977-04), VRSK (-2%, since 1977-07), ADC (+9%, since 1978-10), COO (-31%, since 1981-04), HRL (+79%, since 1979-04), CGNX (+97%, since 1968-01), STZ (+74%, since 1971-04), DD (-14%, since 1979-07), NEU (+94%, since 1968-07), TPL (-25%, since 1981-07), MKC (+34%, since 1974-04), CNC (-38%, since 1980-10), CBSH (+21%, since 1968-01)

Worst open: OLED (-76%, since 1972-04), SYF (-74%, since 1972-10), WDAY (-71%, since 1968-01), INCY (-68%, since 1976-04), CDE (-59%, since 1974-10), AYI (-55%, since 1978-07), WAT (-54%, since 1969-04), UNM (-54%, since 1973-04), ORA (-53%, since 1978-10), DTM (-50%, since 1973-01)

Best closed: CF $12,880 (+129%), DAL $10,459 (+105%), SNPS $9,487 (+77%), AR $9,276 (+93%), MMS $9,218 (+92%)
Worst closed: OTIS $466 (+42%), KIM $659 (+79%), GOOG $725 (+85%), NXPI $736 (+90%), MU $820 (+83%)

## Index benchmark from 1968 (same withdrawal rule)

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +11.9% | $8,391 | $103,492 | $8,391 |  |  |  |  |  |
| 1969 | $103,492 | -8.2% | $4,750 | $90,244 | $13,141 |  |  |  |  |  |
| 1970 | $90,244 | +3.6% | $4,676 | $88,848 | $17,817 |  |  |  |  |  |
| 1971 | $88,848 | +14.7% | $7,643 | $94,258 | $25,460 |  |  |  |  |  |
| 1972 | $94,258 | +19.7% | $8,463 | $104,378 | $33,923 |  |  |  |  |  |
| 1973 | $104,378 | -14.4% | $4,467 | $84,871 | $38,390 |  |  |  |  |  |
| 1974 | $84,871 | -27.2% | $3,089 | $58,695 | $41,479 |  |  |  |  |  |
| 1975 | $58,695 | +36.2% | $7,994 | $71,949 | $49,473 |  |  |  |  |  |
| 1976 | $71,949 | +23.4% | $8,876 | $79,880 | $58,349 |  |  |  |  |  |
| 1977 | $79,880 | -8.4% | $3,659 | $69,530 | $62,008 |  |  |  |  |  |
| 1978 | $69,530 | +4.6% | $3,637 | $69,108 | $65,646 |  |  |  |  |  |
| 1979 | $69,108 | +16.3% | $6,028 | $74,348 | $71,674 |  |  |  |  |  |
| 1980 | $74,348 | +30.3% | $9,685 | $87,164 | $81,359 |  |  |  |  |  |
| 1981 | $87,164 | -6.5% | $4,074 | $77,397 | $85,432 |  |  |  |  |  |
| 1982 (to Aug) | $77,397 | -0.8% | $0 | $76,803 | $85,432 |  |  |  |  |  |

## Quarterly top-10 lists

| Snapshot | Qualified | Eligible | Top 10 (value rank order) |
|---|---|---|---|
| 1968-01-01 | 200 | 190 | CBSH, BXP, WDAY, CF, AR, DAL, HUM, ABBV, CGNX, MMS |
| 1968-04-01 | 275 | 265 | NXPI, IFF, VRT, AR, IQV, PEP, NWSA, HUM, GOOG, BXP |
| 1968-07-01 | 257 | 244 | NEU, OTIS, GOOG, VRT, PEP, HUM, NXPI, TXT, IFF, DUOL |
| 1968-10-01 | 196 | 188 | AWK, FCX, OTIS, VRT, DUOL, FERG, NEU, PEP, TXT, PKG |
| 1969-01-01 | 188 | 180 | WDAY, CELH, BKNG, OGE, GPK, AWK, EXPO, WAL, FERG, ABBV |
| 1969-04-01 | 221 | 213 | BXP, WAT, OMC, WDAY, NKE, AR, MU, GAP, EOG, GOOG |
| 1969-07-01 | 265 | 256 | BEN, AR, BXP, WDAY, HPQ, GOOG, NXPI, VICR, WAT, OMC |
| 1969-10-01 | 370 | 359 | PEP, EXPD, VICR, BEN, GOOG, BXP, NEU, EQH, DRI, INCY |
| 1970-01-01 | 416 | 400 | NEU, EQH, EXE, PEP, GNRC, GOOG, EXPD, OTIS, PKG, BXP |
| 1970-04-01 | 435 | 414 | GNTX, LH, MTB, EQH, EXE, PEP, INGR, NEU, LHX, PKG |
| 1970-07-01 | 660 | 626 | NXPI, NEU, EXPD, LHX, YETI, GOOG, GNTX, BBWI, DIS, EXE |
| 1970-10-01 | 655 | 626 | GOOG, LHX, EXPD, JLL, YETI, BXP, DIS, NXPI, PCTY, AMT |
| 1971-01-01 | 496 | 470 | LHX, AMT, EXPD, COO, STZ, PCTY, BXP, PEP, NRG, JLL |
| 1971-04-01 | 328 | 303 | AMT, STZ, VRSK, COO, LHX, GNTX, BXP, GE, PEP, NKE |
| 1971-07-01 | 208 | 185 | BXP, AMT, CPRT, CME, GNTX, DTM, NKE, DD, COO, GM |
| 1971-10-01 | 236 | 219 | BBWI, ULTA, AMT, EXE, BKNG, CME, NOVT, DTM, NEU, CPRT |
| 1972-01-01 | 289 | 268 | ULTA, EXE, CPRT, AMT, NEU, CHTR, CRL, BBWI, MDT, CME |
| 1972-04-01 | 267 | 248 | OLED, ULTA, IR, CMCSA, LSTR, NEU, EXE, MDT, AMT, BKNG |
| 1972-07-01 | 192 | 178 | OLED, WAT, CVLT, LSTR, MAT, EXE, FERG, VICI, YETI, ROP |
| 1972-10-01 | 201 | 187 | SYF, MRSH, LULU, ROP, EXE, KIM, OLED, UNM, NKE, DTM |
| 1973-01-01 | 186 | 169 | DTM, MRSH, A, BBY, EXE, LSTR, LIVN, SRE, UNM, KIM |
| 1973-04-01 | 195 | 183 | SYF, UNM, ORA, BLK, CL, EXE, LSTR, LHX, ZBH, DTM |
| 1973-07-01 | 304 | 287 | PEP, SYF, MTB, ARE, DRI, OTIS, ULTA, EXE, BBWI, YETI |
| 1973-10-01 | 338 | 318 | LSTR, OTIS, CL, PEP, MTB, ARE, YETI, BBWI, DRI, KIM |
| 1974-01-01 | 416 | 389 | AMT, MTB, IFF, SYNA, TAP, PEP, CL, OTIS, LSTR, FOX |
| 1974-04-01 | 495 | 465 | MKC, LSTR, SMTC, UNP, NXPI, OTIS, IFF, CL, AMT, HXL |
| 1974-07-01 | 600 | 566 | MKC, NKE, ENTG, LULU, PEP, SYF, MTB, GNRC, HXL, NXPI |
| 1974-10-01 | 817 | 766 | CDE, PEP, NKE, LYV, BXP, TPL, GOOG, CL, EXPD, GM |
| 1975-01-01 | 816 | 754 | ENTG, SYF, BXP, NKE, BKNG, CDE, CL, GM, LYV, PEP |
| 1975-04-01 | 710 | 649 | KIM, ENTG, NKE, BXP, WDAY, CL, EQH, LYV, CDE, SYF |
| 1975-07-01 | 435 | 395 | SNPS, RJF, INGR, WAL, WDAY, PEP, LYV, BXP, SYF, LSTR |
| 1975-10-01 | 306 | 274 | VRSN, SNPS, ADM, RJF, WDAY, HRL, BWA, TOL, TMO, SCHW |
| 1976-01-01 | 296 | 272 | INCY, SYF, HPQ, WDAY, AMT, VRSN, MU, ICE, ZBH, FITB |
| 1976-04-01 | 227 | 207 | INCY, WDAY, HPQ, CDE, SYF, RGEN, IESC, ICE, VRSN, SCHW |
| 1976-07-01 | 139 | 126 | MU, VICI, WDAY, ROP, INCY, AMT, EXE, MTB, VAL, HPQ |
| 1976-10-01 | 157 | 140 | JAZZ, CL, VAL, RGLD, AGCO, CDE, NKE, LSTR, VMC, VICI |
| 1977-01-01 | 167 | 148 | CL, BMY, ATO, NEU, POR, CSGP, COO, JAZZ, LSTR, ADC |
| 1977-04-01 | 242 | 222 | CL, SYF, MDT, POR, NEU, FERG, HRB, MTB, TPL, VRSK |
| 1977-07-01 | 294 | 268 | VRSK, CL, LHX, RF, MDT, NEU, MSFT, PEP, LYV, POR |
| 1977-10-01 | 334 | 311 | MSFT, ULS, IVZ, LHX, NEU, VMRK, AMCR, NLY, EQH, FCX |
| 1978-01-01 | 386 | 356 | CINF, TTWO, IDA, AES, VAL, EQH, MSFT, RJF, NEU, HUM |
| 1978-04-01 | 474 | 434 | SYF, CINF, ORA, KMI, NXPI, AES, NEU, COST, LUV, RJF |
| 1978-07-01 | 461 | 423 | AYI, CRL, TMO, CAR, SYF, IFF, NXPI, ORA, NEU, CINF |
| 1978-10-01 | 292 | 259 | ADC, ORA, PFGC, POR, WAT, AYI, DD, COO, CINF, HUM |
| 1979-01-01 | 327 | 297 | COO, BXP, HST, FITB, MTB, IFF, CINF, ADC, CL, VAL |
| 1979-04-01 | 355 | 327 | CVLT, HRL, COO, MSFT, ADC, BMY, EOG, BXP, MTB, HST |
| 1979-07-01 | 279 | 253 | CVLT, DD, MTB, COO, MSFT, AEP, HRL, URI, CRL, HXL |
| 1979-10-01 | 233 | 211 | HRL, EOG, URI, EXC, CVLT, NRG, DD, GNTX, MTB, MSFT |
| 1980-01-01 | 240 | 218 | MSFT, CL, IFF, CDE, DLTR, HRL, FOX, IDA, URI, MKC |
| 1980-04-01 | 275 | 251 | ULTA, CL, TGT, DLTR, SYF, IFF, IDA, COO, WSO, NFLX |
| 1980-07-01 | 230 | 211 | TMO, SN, CL, ABBV, WTRG, TTWO, AES, COO, WAT, ULTA |
| 1980-10-01 | 196 | 182 | CVX, AYI, WDAY, CNC, ZBH, TTWO, TMO, HR, WTRG, SN |
| 1981-01-01 | 111 | 100 | DY, CVX, DTM, CNC, ZBH, EXPO, SYF, TMO, DD, SFM |
| 1981-04-01 | 115 | 103 | COO, TKO, CL, CPT, TXT, DD, NEE, DY, EXE, CVX |
| 1981-07-01 | 142 | 131 | TPL, DD, INVH, HUM, EXE, BF-B, CPT, FERG, COO, DY |
| 1981-10-01 | 294 | 275 | VRSK, TPL, FFIN, DLTR, TXT, SBRA, HUM, WAT, TKR, GNRC |
| 1982-01-01 | 324 | 306 | HPQ, ADC, TXT, VRSK, CBT, TPR, TKR, ESAB, VRSN, GNRC |
| 1982-04-01 | 383 | 368 | FCX, HPQ, TPR, YETI, CNM, IESC, VRSN, RPM, CINF, MUR |
| 1982-07-01 | 440 | 417 | DPZ, FCX, YETI, SBRA, TPR, TRV, TKR, COST, AGCO, HPQ |