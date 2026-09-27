# Synthetic lost decade (1968-1982 market, seed 4) — 1968-01-01 to 1982-08-31

Quarterly scan (1 Jan / 1 Apr / 1 Jul / 1 Oct) with the turnaround scanner's rules (monthly RSI(14) < 42 within the last 6 completed months, ≥ 5 years of history, ≥ $5M average daily dollar volume, ≥ $1B market cap), then: profitable now and in the past, top 20 by trailing-twelve-month revenue growth, top 10 of those by valuation versus the company's own history (mean percentile of trailing P/E, P/S and EV/EBITDA). $100,000 start, at most 10% of the portfolio per stock, no taxes, commissions or slippage, dividends credited as cash, idle cash earns nothing.

Withdrawal rule at each year end: year return > 20% → 10% of the portfolio; 10–20% → 7.5%; below 10% (including losses) → 5%. The partial year 2026 has no withdrawal.

**Synthetic data.** The market is the real S&P 500 daily path from 1962 to August 1982 (Yahoo ^GSPC); each of today's S&P 500 + 400 stocks is re-simulated on it with its own real beta and a block bootstrap of its own real idiosyncratic daily returns (2004-2026), so single-stock crashes and rebounds are realistic while the market goes nowhere. Quarterly fundamentals are generated: revenue grows with CPI inflation plus a company-specific real rate plus part of the stock's own price residual; net margins swing with the stock's residual and the market and can turn negative; EBITDA, debt, cash, shares and the starting market cap are scaled from each company's latest real filing. Dividend yield 3.5%. The benchmark 'Index' is the S&P 500 price path with the same dividends reinvested.

**Read it as a stress test, not a forecast.** Nothing in the generated fundamentals knows the future price, and nothing in the prices knows the fundamentals beyond the contemporaneous link above, so the selection rules cannot cheat. Real (inflation-adjusted) figures use BLS CPI-U annual averages: the CPI rose about 180% over the window, so a nominal result must roughly triple just to stand still.

## Scenario summary

| Scenario | Start | First buy | Final value | Withdrawn | Final + withdrawn | CAGR (final) | CAGR (no-withdrawal index) | IRR | Max DD | Closed trades | Win rate | Avg closed ret. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **base** | 1968 | 1968-01-02 | $85,555 | $95,348 | $180,903 | -1.1% | +5.8% | +6.2% | -40.4% | 18 | +100.0% | +86.8% |
| **no_trim** | 1968 | 1968-01-02 | $87,559 | $99,413 | $186,972 | -0.9% | +6.4% | +6.4% | -48.1% | 19 | +100.0% | +108.9% |
| **rotate** | 1968 | 1968-01-02 | $140,817 | $139,420 | $280,237 | +2.4% | +10.1% | +10.6% | -38.9% | 357 | +57.7% | +4.6% |
| **base_no_wd** | 1968 | 1968-01-02 | $286,596 | $0 | $286,596 | +7.4% | +7.4% | +7.4% | -37.4% | 23 | +100.0% | +98.9% |
| **rsi80** | 1968 | 1968-01-02 | $83,935 | $94,444 | $178,379 | -1.2% | +5.7% | +6.1% | -40.4% | 20 | +100.0% | +81.4% |
| Index (1968) | 1968 | 1968-01-02 | $76,803 | $85,432 | $162,236 | -1.8% | +5.1% | +4.8% | -44.9% |  |  |  |

CAGR (final) compounds the ending value after withdrawals; the no-withdrawal index chains the yearly returns as if nothing had been taken out; IRR is the money-weighted return of the $100,000 in, the withdrawals out and the final value. Max DD is on the no-withdrawal index.

## base — Base: trim half at +50%, hold rest, RSI(m) 90 exit, replace >100% winners

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +20.0% | $12,004 | $108,039 | $12,004 | 13 | +0.0% | 13 | 15 | +11.9% |
| 1969 | $108,039 | -11.3% | $4,791 | $91,031 | $16,796 | 15 | +0.0% | 4 | 18 | -8.2% |
| 1970 | $91,031 | +6.5% | $4,847 | $92,090 | $21,642 | 18 | +0.0% | 3 | 18 | +3.6% |
| 1971 | $92,090 | +15.6% | $7,985 | $98,478 | $29,627 | 20 | +0.0% | 3 | 26 | +14.7% |
| 1972 | $98,478 | +20.8% | $11,897 | $107,074 | $41,524 | 23 | +0.0% | 4 | 28 | +19.7% |
| 1973 | $107,074 | -5.4% | $5,064 | $96,215 | $46,588 | 27 | +1.9% | 4 | 6 | -14.4% |
| 1974 | $96,215 | -24.3% | $3,641 | $69,171 | $50,229 | 31 | +0.0% | 4 | 32 | -27.2% |
| 1975 | $69,171 | +40.9% | $9,745 | $87,709 | $59,974 | 34 | +0.0% | 4 | 37 | +36.2% |
| 1976 | $87,709 | +19.1% | $7,837 | $96,662 | $67,812 | 35 | +0.0% | 4 | 41 | +23.4% |
| 1977 | $96,662 | -10.5% | $4,324 | $82,162 | $72,136 | 38 | +0.0% | 3 | 42 | -8.4% |
| 1978 | $82,162 | +1.3% | $4,160 | $79,046 | $76,296 | 40 | +0.0% | 4 | 43 | +4.6% |
| 1979 | $79,046 | +16.5% | $6,908 | $85,194 | $83,204 | 42 | +0.0% | 3 | 43 | +16.3% |
| 1980 | $85,194 | +19.0% | $7,604 | $93,788 | $90,808 | 43 | +0.0% | 6 | 54 | +30.3% |
| 1981 | $93,788 | -3.2% | $4,540 | $86,256 | $95,348 | 47 | +0.0% | 5 | 51 | -6.5% |
| 1982 (to Aug) | $86,256 | -0.8% | $0 | $85,555 | $95,348 | 48 | +1.4% | 2 | 4 | -0.8% |

Final value $85,555, withdrawn $95,348, 524 trades, 18 closed positions (win rate +100.0%, average closed return +86.8%, median hold 51.0 months), 48 still open.

Sell reasons: withdrawal × 399, trim +50% × 41, replaced × 18

Open positions at the end: 48, of which 33 below cost (unrealised loss $-39,742). Largest: TMUS (+0%, since 1982-07), FSLR (+64%, since 1981-07), XPO (-25%, since 1973-04), CROX (-39%, since 1980-01), GLPI (-35%, since 1978-07), COHR (-1%, since 1980-07), PNC (-33%, since 1968-01), LH (-4%, since 1977-04), LIN (+21%, since 1968-01), MORN (-32%, since 1980-10), BALL (+26%, since 1971-10), NDSN (-49%, since 1968-01), HAE (-5%, since 1968-01), ITW (+19%, since 1975-04), VZ (-23%, since 1971-04)

Worst open: PPC (-99%, since 1968-01), SANM (-84%, since 1969-04), PVH (-82%, since 1977-10), ANF (-80%, since 1976-10), CNH (-75%, since 1975-07), CNC (-72%, since 1975-07), FERG (-67%, since 1981-01), CLF (-66%, since 1968-01), OXY (-58%, since 1973-10), BIIB (-52%, since 1972-01)

Best closed: LSTR $9,214 (+92%), APPF $9,084 (+92%), THC $8,911 (+89%), BA $8,889 (+89%), LYB $8,876 (+89%)
Worst closed: SWK $541 (+80%), DUOL $586 (+74%), WDAY $630 (+82%), DOW $645 (+84%), CNC $712 (+87%)

## no_trim — No trim: hold until RSI(m) 90 exit or replaced

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +22.4% | $12,235 | $110,116 | $12,235 | 13 | +0.0% | 13 | 13 | +11.9% |
| 1969 | $110,116 | -11.3% | $4,882 | $92,751 | $17,117 | 16 | +0.0% | 5 | 18 | -8.2% |
| 1970 | $92,751 | +5.5% | $4,891 | $92,923 | $22,007 | 19 | +0.0% | 3 | 19 | +3.6% |
| 1971 | $92,923 | +18.1% | $8,229 | $101,493 | $30,237 | 21 | +0.0% | 3 | 22 | +14.7% |
| 1972 | $101,493 | +13.2% | $8,620 | $106,309 | $38,856 | 24 | +0.0% | 4 | 25 | +19.7% |
| 1973 | $106,309 | -18.0% | $4,360 | $82,836 | $43,216 | 27 | +0.0% | 3 | 27 | -14.4% |
| 1974 | $82,836 | -24.0% | $3,148 | $59,811 | $46,364 | 30 | +0.0% | 3 | 30 | -27.2% |
| 1975 | $59,811 | +46.5% | $8,761 | $78,847 | $55,125 | 33 | +0.0% | 4 | 34 | +36.2% |
| 1976 | $78,847 | +30.0% | $10,254 | $92,285 | $65,379 | 35 | +0.0% | 5 | 38 | +23.4% |
| 1977 | $92,285 | -4.8% | $4,392 | $83,453 | $69,771 | 38 | +0.0% | 3 | 38 | -8.4% |
| 1978 | $83,453 | -0.7% | $4,145 | $78,755 | $73,916 | 40 | +0.0% | 4 | 42 | +4.6% |
| 1979 | $78,755 | +26.8% | $9,986 | $89,878 | $83,902 | 42 | +0.0% | 3 | 43 | +16.3% |
| 1980 | $89,878 | +23.5% | $11,096 | $99,865 | $94,999 | 43 | +0.0% | 7 | 49 | +30.3% |
| 1981 | $99,865 | -11.6% | $4,415 | $83,877 | $99,413 | 46 | +0.0% | 4 | 47 | -6.5% |
| 1982 (to Aug) | $83,877 | +4.4% | $0 | $87,559 | $99,413 | 47 | +0.0% | 2 | 1 | -0.8% |

Final value $87,559, withdrawn $99,413, 512 trades, 19 closed positions (win rate +100.0%, average closed return +108.9%, median hold 51.0 months), 47 still open.

Sell reasons: withdrawal × 427, replaced × 19

Open positions at the end: 47, of which 32 below cost (unrealised loss $-31,401). Largest: HIG (+51%, since 1980-01), MORN (-32%, since 1980-10), BBY (-4%, since 1980-01), LIN (+21%, since 1968-01), CYTK (-16%, since 1980-10), COHR (-1%, since 1980-07), CROX (-39%, since 1980-01), GLPI (-35%, since 1978-07), BAH (+19%, since 1969-01), HAE (-5%, since 1968-01), EOG (-31%, since 1969-01), SWK (+75%, since 1979-04), PNC (-33%, since 1968-01), WDAY (+114%, since 1978-04), USB (+3%, since 1982-04)

Worst open: PPC (-99%, since 1968-01), SANM (-84%, since 1969-04), PVH (-82%, since 1977-10), ANF (-80%, since 1976-10), CNH (-75%, since 1975-07), CNC (-72%, since 1975-07), FERG (-67%, since 1981-01), CLF (-66%, since 1968-01), OXY (-58%, since 1973-10), BIIB (-52%, since 1972-01)

Best closed: THC $11,228 (+112%), LYB $11,141 (+111%), LSTR $10,803 (+108%), APPF $10,724 (+121%), BA $10,547 (+105%)
Worst closed: SWK $743 (+105%), DOW $830 (+104%), WDAY $883 (+112%), CASY $894 (+102%), AWK $899 (+105%)

## rotate — Rotate: hold exactly the current top 10 each quarter

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +11.0% | $8,326 | $102,687 | $8,326 | 10 | +2.7% | 30 | 20 | +11.9% |
| 1969 | $102,687 | -4.9% | $4,885 | $92,821 | $13,211 | 10 | +0.0% | 30 | 40 | -8.2% |
| 1970 | $92,821 | +15.7% | $8,056 | $99,356 | $21,267 | 10 | +0.0% | 21 | 31 | +3.6% |
| 1971 | $99,356 | +26.2% | $12,537 | $112,834 | $33,804 | 10 | +0.0% | 22 | 32 | +14.7% |
| 1972 | $112,834 | +45.9% | $16,458 | $148,121 | $50,262 | 10 | +0.0% | 26 | 36 | +19.7% |
| 1973 | $148,121 | +0.1% | $7,417 | $140,924 | $57,679 | 10 | +0.0% | 24 | 34 | -14.4% |
| 1974 | $140,924 | -23.6% | $5,385 | $102,316 | $63,064 | 10 | +0.0% | 24 | 34 | -27.2% |
| 1975 | $102,316 | +46.4% | $14,978 | $134,806 | $78,043 | 10 | +0.0% | 27 | 37 | +36.2% |
| 1976 | $134,806 | +8.2% | $7,294 | $138,580 | $85,336 | 10 | +2.6% | 22 | 22 | +23.4% |
| 1977 | $138,580 | +7.5% | $7,447 | $141,492 | $92,783 | 10 | +0.0% | 27 | 37 | -8.4% |
| 1978 | $141,492 | -15.3% | $5,993 | $113,858 | $98,776 | 10 | +5.6% | 22 | 22 | +4.6% |
| 1979 | $113,858 | +22.3% | $13,924 | $125,312 | $112,700 | 10 | +0.0% | 23 | 33 | +16.3% |
| 1980 | $125,312 | +20.7% | $15,121 | $136,090 | $127,821 | 10 | +0.2% | 23 | 23 | +30.3% |
| 1981 | $136,090 | +13.6% | $11,599 | $143,052 | $139,420 | 10 | +0.0% | 25 | 35 | -6.5% |
| 1982 (to Aug) | $143,052 | -1.6% | $0 | $140,817 | $139,420 | 10 | +0.0% | 21 | 21 | -0.8% |

Final value $140,817, withdrawn $139,420, 824 trades, 357 closed positions (win rate +57.7%, average closed return +4.6%, median hold 3.0 months), 10 still open.

Sell reasons: left list × 357, withdrawal × 100

Open positions at the end: 10, of which 2 below cost (unrealised loss $-2,148). Largest: T (+25%, since 1982-07), AON (+23%, since 1982-07), EEFT (+14%, since 1982-04), COHR (+17%, since 1982-07), EOG (+30%, since 1982-07), BBY (+7%, since 1982-07), USB (+3%, since 1982-04), TMUS (+0%, since 1982-07), NDSN (-2%, since 1982-07), WYNN (-15%, since 1982-07)

Worst open: WYNN (-15%, since 1982-07), NDSN (-2%, since 1982-07)

Best closed: COHR $11,324 (+83%), FSLR $9,773 (+68%), WYNN $8,607 (+117%), YETI $7,687 (+59%), BC $7,114 (+58%)
Worst closed: SANM $-10,007 (-60%), DUOL $-8,726 (-67%), CNC $-7,140 (-44%), PVH $-6,953 (-50%), FCX $-6,769 (-49%)

## base_no_wd — Base without withdrawals

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +20.0% | $0 | $120,044 | $0 | 13 | +7.7% | 13 | 2 | +11.9% |
| 1969 | $120,044 | -8.6% | $0 | $109,676 | $0 | 16 | +0.9% | 5 | 3 | -8.2% |
| 1970 | $109,676 | +8.0% | $0 | $118,487 | $0 | 20 | +0.8% | 4 | 1 | +3.6% |
| 1971 | $118,487 | +18.3% | $0 | $140,180 | $0 | 24 | +2.9% | 5 | 8 | +14.7% |
| 1972 | $140,180 | +24.4% | $0 | $174,409 | $0 | 26 | +11.6% | 4 | 6 | +19.7% |
| 1973 | $174,409 | -6.3% | $0 | $163,405 | $0 | 32 | +5.5% | 6 | 6 | -14.4% |
| 1974 | $163,405 | -20.1% | $0 | $130,620 | $0 | 36 | +0.9% | 4 | 1 | -27.2% |
| 1975 | $130,620 | +35.8% | $0 | $177,379 | $0 | 39 | +0.9% | 4 | 4 | +36.2% |
| 1976 | $177,379 | +24.3% | $0 | $220,549 | $0 | 41 | +10.2% | 5 | 6 | +23.4% |
| 1977 | $220,549 | -10.2% | $0 | $198,113 | $0 | 44 | +0.9% | 4 | 5 | -8.4% |
| 1978 | $198,113 | +3.9% | $0 | $205,811 | $0 | 46 | +0.9% | 5 | 6 | +4.6% |
| 1979 | $205,811 | +20.7% | $0 | $248,390 | $0 | 48 | +1.3% | 4 | 3 | +16.3% |
| 1980 | $248,390 | +18.1% | $0 | $293,374 | $0 | 48 | +9.7% | 5 | 13 | +30.3% |
| 1981 | $293,374 | -0.8% | $0 | $291,113 | $0 | 51 | +6.7% | 5 | 5 | -6.5% |
| 1982 (to Aug) | $291,113 | -1.6% | $0 | $286,596 | $0 | 53 | +0.0% | 3 | 3 | -0.8% |

Final value $286,596, withdrawn $0, 148 trades, 23 closed positions (win rate +100.0%, average closed return +98.9%, median hold 45.0 months), 53 still open.

Sell reasons: trim +50% × 49, replaced × 23

Open positions at the end: 53, of which 35 below cost (unrealised loss $-117,242). Largest: USB (+3%, since 1982-04), TMUS (+0%, since 1982-07), FSLR (+64%, since 1981-07), RSG (+49%, since 1977-01), LYB (-17%, since 1982-01), XPO (-25%, since 1973-04), COHR (-1%, since 1980-07), FCX (-48%, since 1981-01), CROX (-39%, since 1980-01), FERG (-67%, since 1981-01), NTRS (+6%, since 1980-07), LH (-4%, since 1977-04), PNC (-33%, since 1968-01), LIN (+21%, since 1968-01), BALL (+26%, since 1971-10)

Worst open: PPC (-99%, since 1968-01), SANM (-84%, since 1969-04), PVH (-82%, since 1977-10), ANF (-80%, since 1976-10), CNH (-75%, since 1975-07), FERG (-67%, since 1981-01), CLF (-66%, since 1968-01), CNC (-62%, since 1975-10), OXY (-58%, since 1973-10), BIIB (-52%, since 1972-01)

Best closed: DUOL $20,215 (+91%), APPF $18,966 (+94%), AIZ $18,089 (+103%), WDAY $17,870 (+87%), LSTR $12,688 (+127%)
Worst closed: SWK $683 (+82%), CNC $724 (+88%), DOW $943 (+101%), AAON $1,174 (+102%), CW $1,356 (+101%)

## rsi80 — Base with the monthly-RSI exit at 80 instead of 90

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +20.0% | $12,004 | $108,039 | $12,004 | 13 | +0.0% | 13 | 15 | +11.9% |
| 1969 | $108,039 | -11.3% | $4,791 | $91,031 | $16,796 | 15 | +0.0% | 4 | 18 | -8.2% |
| 1970 | $91,031 | +6.5% | $4,847 | $92,090 | $21,642 | 18 | +0.0% | 3 | 18 | +3.6% |
| 1971 | $92,090 | +15.6% | $7,985 | $98,478 | $29,627 | 20 | +0.0% | 3 | 26 | +14.7% |
| 1972 | $98,478 | +20.8% | $11,897 | $107,074 | $41,524 | 23 | +0.0% | 4 | 28 | +19.7% |
| 1973 | $107,074 | -6.2% | $5,022 | $95,409 | $46,546 | 27 | +2.0% | 5 | 8 | -14.4% |
| 1974 | $95,409 | -24.1% | $3,622 | $68,821 | $50,168 | 31 | +0.0% | 4 | 32 | -27.2% |
| 1975 | $68,821 | +40.8% | $9,691 | $87,220 | $59,859 | 34 | +0.0% | 4 | 37 | +36.2% |
| 1976 | $87,220 | +18.5% | $7,754 | $95,634 | $67,613 | 34 | +0.0% | 4 | 41 | +23.4% |
| 1977 | $95,634 | -9.9% | $4,309 | $81,872 | $71,922 | 36 | +0.0% | 3 | 41 | -8.4% |
| 1978 | $81,872 | +1.0% | $4,135 | $78,558 | $76,057 | 38 | +0.0% | 4 | 41 | +4.6% |
| 1979 | $78,558 | +12.6% | $6,636 | $81,840 | $82,692 | 40 | +0.0% | 3 | 41 | +16.3% |
| 1980 | $81,840 | +18.4% | $7,271 | $89,671 | $89,963 | 41 | +0.0% | 5 | 51 | +30.3% |
| 1981 | $89,671 | -0.1% | $4,481 | $85,143 | $94,444 | 45 | +0.0% | 5 | 49 | -6.5% |
| 1982 (to Aug) | $85,143 | -1.4% | $0 | $83,935 | $94,444 | 46 | +0.2% | 2 | 3 | -0.8% |

Final value $83,935, withdrawn $94,444, 515 trades, 20 closed positions (win rate +100.0%, average closed return +81.4%, median hold 43.5 months), 46 still open.

Sell reasons: withdrawal × 388, trim +50% × 41, replaced × 16, RSI(m) 81 × 2, RSI(m) 82 × 1, RSI(m) 86 × 1

Open positions at the end: 46, of which 32 below cost (unrealised loss $-39,536). Largest: TMUS (+0%, since 1982-07), FSLR (+64%, since 1981-07), XPO (-25%, since 1973-04), LH (-4%, since 1977-04), GLPI (-35%, since 1978-07), UBSI (-39%, since 1973-04), COHR (-1%, since 1980-07), PNC (-33%, since 1968-01), LIN (+21%, since 1968-01), MORN (-32%, since 1980-10), BALL (+26%, since 1971-10), NDSN (-49%, since 1968-01), HAE (-5%, since 1968-01), ITW (+19%, since 1975-04), VZ (-23%, since 1971-04)

Worst open: PPC (-99%, since 1968-01), SANM (-84%, since 1969-04), PVH (-82%, since 1977-10), ANF (-80%, since 1976-10), CNH (-75%, since 1975-07), CNC (-72%, since 1975-07), FERG (-67%, since 1981-01), CLF (-66%, since 1968-01), BIIB (-52%, since 1972-01), NDSN (-49%, since 1968-01)

Best closed: APPF $9,010 (+92%), THC $8,911 (+89%), BA $8,889 (+89%), LYB $8,876 (+89%), AWK $7,734 (+92%)
Worst closed: SWK $541 (+80%), DUOL $582 (+74%), WDAY $630 (+82%), DOW $645 (+84%), BRKR $681 (+51%)

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
| 1968-01-01 | 237 | 227 | LIN, LSTR, PNC, HAE, BA, NDSN, PPC, THC, LYB, CLF |
| 1968-04-01 | 292 | 280 | CNC, DINO, SLGN, MIDD, STX, DT, LSTR, FOX, IT, NVST |
| 1968-07-01 | 277 | 265 | DT, GEHC, NVST, AWK, STX, NVDA, ONTO, NNN, CNC, FE |
| 1968-10-01 | 201 | 188 | AWK, DT, NNN, TSN, PII, NVDA, TSCO, LYB, STX, FBIN |
| 1969-01-01 | 184 | 171 | EOG, BAH, DT, AWK, ELV, NNN, AEP, PII, TSN, CI |
| 1969-04-01 | 192 | 183 | SANM, COLB, OSK, TTEK, DT, FOX, BAC, CF, LIN, OVV |
| 1969-07-01 | 248 | 243 | ELS, NTAP, MOS, HII, BIIB, CTRE, REG, DT, CASY, LIN |
| 1969-10-01 | 352 | 342 | CRM, NTAP, EXLS, ELS, CI, EOG, MCK, WYNN, AMD, CW |
| 1970-01-01 | 420 | 407 | NDSN, DCI, BRKR, IRM, EEFT, BA, AMD, NTAP, CRM, ELS |
| 1970-04-01 | 478 | 463 | NDSN, WDAY, PYPL, LSCC, DCI, LSTR, CRM, EQIX, ESS, BA |
| 1970-07-01 | 661 | 634 | SWK, NDSN, PRU, EQIX, WAB, DT, WYNN, BA, HR, EOG |
| 1970-10-01 | 668 | 642 | DOW, DT, WYNN, AMH, HR, NDSN, EOG, PRU, BA, SWK |
| 1971-01-01 | 515 | 491 | GEHC, NDSN, AMH, FLS, NRG, EOG, VZ, DT, EIX, DOW |
| 1971-04-01 | 335 | 317 | EOG, NDSN, VZ, DT, XPO, NRG, FLG, ED, FLS, ESS |
| 1971-07-01 | 203 | 184 | EOG, PEN, VZ, FLS, DINO, PNC, PPL, TTEK, ELV, MA |
| 1971-10-01 | 214 | 201 | BALL, GDDY, PPL, VZ, TRGP, FLS, LSCC, CRM, NDAQ, PNC |
| 1972-01-01 | 266 | 250 | BIIB, SW, MA, CASY, PPL, AWK, PNC, COHR, BALL, BA |
| 1972-04-01 | 260 | 245 | CASY, O, BIIB, FLS, ZBRA, PPL, AWK, NFG, PNC, HPE |
| 1972-07-01 | 181 | 171 | CW, COKE, JBL, ONTO, ZBRA, AAON, HPE, HR, CASY, AWK |
| 1972-10-01 | 182 | 176 | ONTO, AAPL, WAB, FSLR, LIN, NXST, AIZ, LH, PFE, ZBRA |
| 1973-01-01 | 171 | 164 | AIZ, PFE, NXST, AAON, CRM, SPXC, AAPL, WAB, LIN, ZBRA |
| 1973-04-01 | 198 | 188 | XPO, UBSI, BRKR, IT, MORN, ZBRA, AIZ, BIIB, EVR, SHC |
| 1973-07-01 | 299 | 291 | CRS, ESS, RRX, XPO, BIIB, MORN, UNH, OC, UBSI, CRWD |
| 1973-10-01 | 343 | 331 | OXY, PEN, BIIB, ESS, THO, BALL, EQIX, UNH, EEFT, SANM |
| 1974-01-01 | 429 | 412 | BIIB, UNH, PYPL, EQIX, EEFT, NRG, SANM, PPL, CRS, BALL |
| 1974-04-01 | 489 | 470 | EQIX, SANM, SYK, LH, HR, WYNN, NRG, AAON, BIIB, NTRS |
| 1974-07-01 | 599 | 577 | WSM, GNRC, ODFL, SYK, SANM, KKR, EQIX, EEFT, CI, VZ |
| 1974-10-01 | 814 | 781 | TRGP, MA, KKR, EQIX, NDSN, P, LSCC, AIZ, ODFL, DT |
| 1975-01-01 | 816 | 770 | TRGP, AAON, ITW, BALL, CW, MA, AIZ, NDSN, DT, REG |
| 1975-04-01 | 702 | 661 | ITW, AAON, GEHC, EEFT, EOG, ELS, NDSN, CW, P, STRL |
| 1975-07-01 | 441 | 407 | CNH, ITW, CNC, AGCO, WWD, INVH, CW, RMD, PPL, WYNN |
| 1975-10-01 | 330 | 313 | CNC, MIDD, SWK, DT, CNH, BAX, TTC, RDDT, UBSI, HR |
| 1976-01-01 | 317 | 303 | CNC, BAX, DT, TTC, SWK, MOG-A, STRL, HR, APPF, NBIX |
| 1976-04-01 | 224 | 216 | CNC, APPF, GNRC, CNH, TTC, MOG-A, UBSI, PPL, VZ, RMD |
| 1976-07-01 | 153 | 142 | CNC, CNH, IRT, RMD, AMH, TTC, SYK, SLM, DUOL, VZ |
| 1976-10-01 | 176 | 160 | ANF, RSG, WST, CNC, EVRG, GEHC, UBSI, VZ, IESC, RMD |
| 1977-01-01 | 198 | 181 | UBSI, RSG, JBL, BG, LH, VZ, AEP, EVRG, SWX, COLB |
| 1977-04-01 | 268 | 253 | LH, VZ, ROST, COLB, PFE, ANF, CCL, NFG, A, MCK |
| 1977-07-01 | 327 | 311 | DIS, DT, RGEN, NBIX, LH, CCL, MCK, NFG, ROST, TSLA |
| 1977-10-01 | 361 | 343 | PVH, SHW, CNM, NVST, EXE, CHWY, NDSN, OLN, DIS, NTRS |
| 1978-01-01 | 402 | 383 | PRU, CNC, MORN, BAH, PEG, PVH, MIDD, NDSN, NBIX, FCX |
| 1978-04-01 | 473 | 454 | EOG, MIDD, WDAY, AVT, GLPI, PRU, REG, PVH, WTFC, BAH |
| 1978-07-01 | 442 | 422 | WDAY, GLPI, CVLT, MCK, STRL, HPE, DUOL, EOG, MIDD, REG |
| 1978-10-01 | 280 | 263 | DUOL, GLPI, WWD, WDAY, DT, STRL, CLH, CVLT, EOG, MCK |
| 1979-01-01 | 309 | 292 | SHC, EOG, OVV, DT, WWD, VOYA, PYPL, CAR, ELV, WDAY |
| 1979-04-01 | 348 | 326 | SWK, CAR, CTRE, AVT, VOYA, HUBB, XPO, WWD, WSM, LH |
| 1979-07-01 | 295 | 284 | IT, MOG-A, UNH, HUBB, MORN, SWK, MA, WWD, LH, RMD |
| 1979-10-01 | 236 | 221 | UNH, HCA, MOG-A, RMD, IT, DVA, HUBB, DUK, LH, CNH |
| 1980-01-01 | 228 | 212 | CROX, VZ, LH, HIG, BBY, RMD, SW, MIDD, BC, PVH |
| 1980-04-01 | 264 | 246 | YETI, CROX, XPO, LH, BKH, GLPI, RMD, PVH, NTRS, ITW |
| 1980-07-01 | 243 | 229 | CROX, LH, COHR, NTRS, GLPI, PVH, RYAN, NBIX, XPO, BKH |
| 1980-10-01 | 195 | 184 | PVH, MORN, CYTK, GLPI, FERG, AIZ, NTRS, CTRE, RMD, LH |
| 1981-01-01 | 110 | 100 | COHR, FERG, FCX, BBY, CTRE, RYAN, MORN, CYTK, RMD, NTRS |
| 1981-04-01 | 104 | 94 | LSCC, FERG, STAG, BBY, FCX, EOG, NVST, IRM, NFG, COHR |
| 1981-07-01 | 131 | 119 | FSLR, NTAP, BIIB, TKO, EOG, CNC, GLPI, LSCC, NVST, LH |
| 1981-10-01 | 265 | 251 | NVST, EOG, CRS, MIDD, VRSK, YETI, CRM, VRT, MPWR, PRU |
| 1982-01-01 | 283 | 268 | EOG, NVST, LYB, EIX, MIDD, FAF, YETI, BBY, PRU, FBIN |
| 1982-04-01 | 347 | 328 | USB, CPRT, EEFT, LIN, PCTY, DE, FAF, PRU, WTFC, MOS |
| 1982-07-01 | 422 | 398 | TMUS, T, USB, COHR, AON, WYNN, BBY, NDSN, EOG, EEFT |