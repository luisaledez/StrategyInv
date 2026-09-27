# Synthetic lost decade (1968-1982 market, seed 2) — 1968-01-01 to 1982-08-31

Quarterly scan (1 Jan / 1 Apr / 1 Jul / 1 Oct) with the turnaround scanner's rules (monthly RSI(14) < 42 within the last 6 completed months, ≥ 5 years of history, ≥ $5M average daily dollar volume, ≥ $1B market cap), then: profitable now and in the past, top 20 by trailing-twelve-month revenue growth, top 10 of those by valuation versus the company's own history (mean percentile of trailing P/E, P/S and EV/EBITDA). $100,000 start, at most 10% of the portfolio per stock, no taxes, commissions or slippage, dividends credited as cash, idle cash earns nothing.

Withdrawal rule at each year end: year return > 20% → 10% of the portfolio; 10–20% → 7.5%; below 10% (including losses) → 5%. The partial year 2026 has no withdrawal.

**Synthetic data.** The market is the real S&P 500 daily path from 1962 to August 1982 (Yahoo ^GSPC); each of today's S&P 500 + 400 stocks is re-simulated on it with its own real beta and a block bootstrap of its own real idiosyncratic daily returns (2004-2026), so single-stock crashes and rebounds are realistic while the market goes nowhere. Quarterly fundamentals are generated: revenue grows with CPI inflation plus a company-specific real rate plus part of the stock's own price residual; net margins swing with the stock's residual and the market and can turn negative; EBITDA, debt, cash, shares and the starting market cap are scaled from each company's latest real filing. Dividend yield 3.5%. The benchmark 'Index' is the S&P 500 price path with the same dividends reinvested.

**Read it as a stress test, not a forecast.** Nothing in the generated fundamentals knows the future price, and nothing in the prices knows the fundamentals beyond the contemporaneous link above, so the selection rules cannot cheat. Real (inflation-adjusted) figures use BLS CPI-U annual averages: the CPI rose about 180% over the window, so a nominal result must roughly triple just to stand still.

## Scenario summary

| Scenario | Start | First buy | Final value | Withdrawn | Final + withdrawn | CAGR (final) | CAGR (no-withdrawal index) | IRR | Max DD | Closed trades | Win rate | Avg closed ret. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **base** | 1968 | 1968-01-02 | $125,510 | $117,054 | $242,563 | +1.6% | +8.6% | +8.6% | -35.5% | 30 | +100.0% | +87.7% |
| **no_trim** | 1968 | 1968-01-02 | $132,757 | $125,838 | $258,595 | +1.9% | +9.5% | +9.4% | -34.3% | 29 | +100.0% | +111.1% |
| **rotate** | 1968 | 1968-01-02 | $195,930 | $149,771 | $345,701 | +4.7% | +12.8% | +12.1% | -51.0% | 361 | +64.5% | +5.8% |
| **base_no_wd** | 1968 | 1968-01-02 | $381,363 | $0 | $381,363 | +9.6% | +9.6% | +9.6% | -38.4% | 36 | +100.0% | +100.3% |
| **rsi80** | 1968 | 1968-01-02 | $140,368 | $119,803 | $260,171 | +2.3% | +9.5% | +9.3% | -38.7% | 35 | +97.1% | +79.8% |
| Index (1968) | 1968 | 1968-01-02 | $76,803 | $85,432 | $162,236 | -1.8% | +5.1% | +4.8% | -44.9% |  |  |  |

CAGR (final) compounds the ending value after withdrawals; the no-withdrawal index chains the yearly returns as if nothing had been taken out; IRR is the money-weighted return of the $100,000 in, the withdrawals out and the final value. Max DD is on the no-withdrawal index.

## base — Base: trim half at +50%, hold rest, RSI(m) 90 exit, replace >100% winners

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +6.6% | $5,328 | $101,235 | $5,328 | 13 | +0.0% | 13 | 14 | +11.9% |
| 1969 | $101,235 | +3.0% | $5,213 | $99,052 | $10,541 | 16 | +0.0% | 4 | 20 | -8.2% |
| 1970 | $99,052 | +0.0% | $4,954 | $94,135 | $15,496 | 19 | +0.0% | 4 | 20 | +3.6% |
| 1971 | $94,135 | +32.4% | $12,460 | $112,138 | $27,956 | 20 | +0.0% | 3 | 26 | +14.7% |
| 1972 | $112,138 | +18.1% | $9,931 | $122,476 | $37,886 | 23 | +0.0% | 3 | 27 | +19.7% |
| 1973 | $122,476 | -12.1% | $5,384 | $102,293 | $43,270 | 25 | +0.0% | 3 | 31 | -14.4% |
| 1974 | $102,293 | -18.4% | $4,174 | $79,309 | $47,444 | 26 | +0.0% | 3 | 29 | -27.2% |
| 1975 | $79,309 | +58.0% | $12,533 | $112,797 | $59,977 | 28 | +0.0% | 4 | 32 | +36.2% |
| 1976 | $112,797 | +16.6% | $9,866 | $121,678 | $69,843 | 29 | +0.0% | 3 | 35 | +23.4% |
| 1977 | $121,678 | -6.5% | $5,689 | $108,090 | $75,532 | 31 | +0.0% | 3 | 32 | -8.4% |
| 1978 | $108,090 | +7.1% | $5,789 | $109,999 | $81,321 | 33 | +0.0% | 3 | 36 | +4.6% |
| 1979 | $109,999 | +20.9% | $13,303 | $119,727 | $94,624 | 35 | +0.0% | 5 | 42 | +16.3% |
| 1980 | $119,727 | +29.7% | $15,533 | $139,798 | $110,157 | 36 | +0.0% | 3 | 44 | +30.3% |
| 1981 | $139,798 | -1.3% | $6,897 | $131,034 | $117,054 | 33 | +0.0% | 6 | 46 | -6.5% |
| 1982 (to Aug) | $131,034 | -4.2% | $0 | $125,510 | $117,054 | 33 | +0.0% | 3 | 3 | -0.8% |

Final value $125,510, withdrawn $117,054, 500 trades, 30 closed positions (win rate +100.0%, average closed return +87.7%, median hold 60.0 months), 33 still open.

Sell reasons: withdrawal × 367, trim +50% × 40, replaced × 30

Open positions at the end: 33, of which 21 below cost (unrealised loss $-29,538). Largest: ORA (-1%, since 1981-10), PG (-13%, since 1980-10), FCFS (-39%, since 1981-01), BDX (+9%, since 1974-04), WDAY (-35%, since 1979-07), DBX (+46%, since 1976-04), STWD (-24%, since 1975-07), XPO (-13%, since 1981-04), STRL (-4%, since 1973-04), HAE (-8%, since 1968-01), SWK (-1%, since 1968-07), COO (-16%, since 1968-01), MTD (-26%, since 1969-10), MRSH (+36%, since 1971-10), XOM (+11%, since 1981-10)

Worst open: ENSG (-81%, since 1973-10), FSLR (-51%, since 1979-10), STLD (-49%, since 1982-01), TXT (-49%, since 1969-10), TTWO (-49%, since 1981-07), FCFS (-39%, since 1981-01), WDAY (-35%, since 1979-07), SLM (-28%, since 1968-01), MTD (-26%, since 1969-10), STWD (-24%, since 1975-07)

Best closed: GE $10,623 (+106%), FTNT $9,105 (+91%), IESC $9,077 (+91%), GILD $8,436 (+84%), FNB $8,425 (+85%)
Worst closed: PCTY $638 (+79%), XOM $653 (+81%), TSLA $681 (+77%), TFC $681 (+101%), SCHW $695 (+90%)

## no_trim — No trim: hold until RSI(m) 90 exit or replaced

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +2.9% | $5,143 | $97,708 | $5,143 | 13 | +0.0% | 13 | 13 | +11.9% |
| 1969 | $97,708 | +14.6% | $8,396 | $103,552 | $13,539 | 15 | +0.0% | 3 | 16 | -8.2% |
| 1970 | $103,552 | -3.5% | $4,999 | $94,972 | $18,537 | 19 | +0.0% | 5 | 20 | +3.6% |
| 1971 | $94,972 | +33.8% | $12,710 | $114,387 | $31,247 | 21 | +0.0% | 4 | 23 | +14.7% |
| 1972 | $114,387 | +12.4% | $9,642 | $118,918 | $40,889 | 24 | +0.0% | 3 | 24 | +19.7% |
| 1973 | $118,918 | -12.4% | $5,207 | $98,932 | $46,096 | 26 | +0.0% | 3 | 27 | -14.4% |
| 1974 | $98,932 | -13.0% | $4,305 | $81,797 | $50,401 | 29 | +0.0% | 5 | 31 | -27.2% |
| 1975 | $81,797 | +60.4% | $13,121 | $118,089 | $63,522 | 32 | +0.0% | 5 | 34 | +36.2% |
| 1976 | $118,089 | +20.9% | $14,278 | $128,505 | $77,800 | 33 | +0.0% | 3 | 35 | +23.4% |
| 1977 | $128,505 | -10.2% | $5,769 | $109,605 | $83,569 | 35 | +0.0% | 3 | 36 | -8.4% |
| 1978 | $109,605 | +6.5% | $5,838 | $110,928 | $89,407 | 37 | +0.0% | 3 | 38 | +4.6% |
| 1979 | $110,928 | +20.1% | $13,323 | $119,903 | $102,730 | 38 | +0.0% | 4 | 41 | +16.3% |
| 1980 | $119,903 | +32.8% | $15,923 | $143,307 | $118,653 | 39 | +0.0% | 3 | 41 | +30.3% |
| 1981 | $143,307 | +0.3% | $7,185 | $136,521 | $125,838 | 38 | +0.0% | 7 | 46 | -6.5% |
| 1982 (to Aug) | $136,521 | -2.8% | $0 | $132,757 | $125,838 | 38 | +0.0% | 3 | 3 | -0.8% |

Final value $132,757, withdrawn $125,838, 495 trades, 29 closed positions (win rate +100.0%, average closed return +111.1%, median hold 60.0 months), 38 still open.

Sell reasons: withdrawal × 399, replaced × 29

Open positions at the end: 38, of which 23 below cost (unrealised loss $-22,292). Largest: L (+18%, since 1981-10), ORA (-1%, since 1981-10), VMRK (+25%, since 1975-07), FCFS (-39%, since 1981-01), VRSK (-21%, since 1981-01), MRSH (+36%, since 1971-10), ALV (+58%, since 1975-07), BDX (+9%, since 1974-04), STWD (-24%, since 1975-07), TDG (+77%, since 1971-10), DBX (+46%, since 1976-04), HAE (-8%, since 1968-01), CDNS (-10%, since 1968-01), COO (-16%, since 1968-01), CL (+11%, since 1982-07)

Worst open: ENSG (-81%, since 1973-10), DELL (-80%, since 1974-04), FSLR (-51%, since 1979-10), STLD (-49%, since 1982-01), TTWO (-49%, since 1981-07), TXT (-43%, since 1970-01), FCFS (-39%, since 1981-01), WDAY (-35%, since 1979-07), SLM (-28%, since 1968-01), MTD (-26%, since 1969-10)

Best closed: CXT $15,767 (+132%), GE $14,388 (+144%), FTNT $12,700 (+127%), IESC $10,989 (+110%), MTZ $10,906 (+104%)
Worst closed: PCTY $753 (+95%), TFC $819 (+118%), XOM $870 (+108%), TSLA $905 (+102%), JBHT $917 (+116%)

## rotate — Rotate: hold exactly the current top 10 each quarter

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +12.3% | $8,426 | $103,920 | $8,426 | 10 | +0.0% | 24 | 24 | +11.9% |
| 1969 | $103,920 | +0.1% | $5,200 | $98,797 | $13,626 | 10 | +5.2% | 27 | 27 | -8.2% |
| 1970 | $98,797 | +9.2% | $5,397 | $102,541 | $19,023 | 10 | +0.0% | 23 | 33 | +3.6% |
| 1971 | $102,541 | +24.3% | $12,746 | $114,713 | $31,769 | 10 | +0.0% | 24 | 34 | +14.7% |
| 1972 | $114,713 | +39.1% | $15,958 | $143,626 | $47,727 | 10 | +0.0% | 27 | 37 | +19.7% |
| 1973 | $143,626 | +1.5% | $7,289 | $138,485 | $55,016 | 10 | +0.0% | 25 | 35 | -14.4% |
| 1974 | $138,485 | -38.7% | $4,243 | $80,622 | $59,259 | 10 | +0.0% | 28 | 38 | -27.2% |
| 1975 | $80,622 | +43.9% | $11,602 | $104,422 | $70,861 | 10 | +0.0% | 28 | 38 | +36.2% |
| 1976 | $104,422 | +25.2% | $13,075 | $117,672 | $83,936 | 10 | +0.0% | 22 | 32 | +23.4% |
| 1977 | $117,672 | +8.2% | $6,369 | $121,002 | $90,305 | 10 | +0.0% | 27 | 37 | -8.4% |
| 1978 | $121,002 | +6.8% | $6,463 | $122,801 | $96,768 | 10 | +0.0% | 23 | 33 | +4.6% |
| 1979 | $122,801 | +28.9% | $15,830 | $142,466 | $112,597 | 10 | +0.0% | 20 | 30 | +16.3% |
| 1980 | $142,466 | +49.0% | $21,233 | $191,101 | $133,831 | 10 | +0.0% | 26 | 36 | +30.3% |
| 1981 | $191,101 | +11.2% | $15,940 | $196,595 | $149,771 | 10 | +0.0% | 30 | 40 | -6.5% |
| 1982 (to Aug) | $196,595 | -0.3% | $0 | $195,930 | $149,771 | 10 | +0.4% | 17 | 17 | -0.8% |

Final value $195,930, withdrawn $149,771, 862 trades, 361 closed positions (win rate +64.5%, average closed return +5.8%, median hold 3.1 months), 10 still open.

Sell reasons: left list × 361, withdrawal × 130

Open positions at the end: 10, of which 3 below cost (unrealised loss $-3,679). Largest: IESC (+48%, since 1982-07), HUBB (+18%, since 1982-04), NI (+10%, since 1982-04), RMD (+12%, since 1982-07), MTD (-4%, since 1982-01), CL (+4%, since 1982-04), WTS (+6%, since 1982-07), LPX (+5%, since 1982-07), DRI (-2%, since 1982-04), NSC (-13%, since 1982-01)

Worst open: NSC (-13%, since 1982-01), MTD (-4%, since 1982-01), DRI (-2%, since 1982-04)

Best closed: TSLA $11,884 (+84%), UAL $10,704 (+110%), CTAS $9,908 (+66%), TRGP $9,458 (+51%), AMKR $9,044 (+81%)
Worst closed: AAL $-9,083 (-80%), H $-9,007 (-55%), STLD $-8,829 (-45%), TKR $-6,307 (-52%), FCFS $-4,884 (-25%)

## base_no_wd — Base without withdrawals

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +6.6% | $0 | $106,563 | $0 | 13 | +0.9% | 13 | 1 | +11.9% |
| 1969 | $106,563 | +3.2% | $0 | $109,954 | $0 | 17 | +0.9% | 5 | 4 | -8.2% |
| 1970 | $109,954 | -0.2% | $0 | $109,726 | $0 | 21 | +0.8% | 5 | 1 | +3.6% |
| 1971 | $109,726 | +32.4% | $0 | $145,312 | $0 | 23 | +6.0% | 4 | 7 | +14.7% |
| 1972 | $145,312 | +20.8% | $0 | $175,493 | $0 | 26 | +5.1% | 4 | 6 | +19.7% |
| 1973 | $175,493 | -10.7% | $0 | $156,654 | $0 | 29 | +1.6% | 4 | 6 | -14.4% |
| 1974 | $156,654 | -21.2% | $0 | $123,468 | $0 | 31 | +0.9% | 4 | 3 | -27.2% |
| 1975 | $123,468 | +58.9% | $0 | $196,162 | $0 | 34 | +9.3% | 5 | 6 | +36.2% |
| 1976 | $196,162 | +19.6% | $0 | $234,688 | $0 | 36 | +6.9% | 5 | 8 | +23.4% |
| 1977 | $234,688 | -4.1% | $0 | $225,084 | $0 | 39 | +0.9% | 4 | 2 | -8.4% |
| 1978 | $225,084 | +11.3% | $0 | $250,489 | $0 | 41 | +0.9% | 4 | 4 | +4.6% |
| 1979 | $250,489 | +19.4% | $0 | $299,148 | $0 | 42 | +4.3% | 4 | 8 | +16.3% |
| 1980 | $299,148 | +30.1% | $0 | $389,231 | $0 | 43 | +3.8% | 5 | 12 | +30.3% |
| 1981 | $389,231 | +1.8% | $0 | $396,172 | $0 | 40 | +0.9% | 6 | 13 | -6.5% |
| 1982 (to Aug) | $396,172 | -3.7% | $0 | $381,363 | $0 | 39 | +0.0% | 3 | 4 | -0.8% |

Final value $381,363, withdrawn $0, 160 trades, 36 closed positions (win rate +100.0%, average closed return +100.3%, median hold 60.0 months), 39 still open.

Sell reasons: trim +50% × 49, replaced × 36

Open positions at the end: 39, of which 24 below cost (unrealised loss $-90,303). Largest: ORA (-1%, since 1981-10), PG (-13%, since 1980-10), VRSK (-21%, since 1981-01), AIG (+3%, since 1980-10), XPO (-13%, since 1981-04), DBX (+46%, since 1976-04), SEIC (+45%, since 1978-04), STWD (-24%, since 1975-07), STLD (-49%, since 1982-01), WDAY (-35%, since 1979-07), EQIX (+96%, since 1980-01), L (+18%, since 1981-10), ED (+11%, since 1981-01), STRL (-4%, since 1973-04), TTWO (-49%, since 1981-07)

Worst open: ENSG (-81%, since 1973-10), DELL (-80%, since 1974-04), FCFS (-62%, since 1978-01), VOYA (-54%, since 1974-01), FSLR (-51%, since 1979-10), STLD (-49%, since 1982-01), TXT (-49%, since 1969-10), TTWO (-49%, since 1981-07), WDAY (-35%, since 1979-07), SLM (-28%, since 1968-01)

Best closed: PVH $21,306 (+88%), CNP $16,841 (+105%), NKE $16,727 (+92%), CXT $14,026 (+101%), GE $13,614 (+136%)
Worst closed: XOM $674 (+84%), HBAN $722 (+82%), PCTY $767 (+90%), SCHW $793 (+93%), TFC $925 (+123%)

## rsi80 — Base with the monthly-RSI exit at 80 instead of 90

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +6.6% | $5,328 | $101,235 | $5,328 | 13 | +0.0% | 13 | 14 | +11.9% |
| 1969 | $101,235 | +3.0% | $5,214 | $99,063 | $10,542 | 15 | +6.7% | 4 | 5 | -8.2% |
| 1970 | $99,063 | +0.5% | $4,978 | $94,574 | $15,520 | 19 | +0.0% | 4 | 19 | +3.6% |
| 1971 | $94,574 | +32.5% | $12,532 | $112,789 | $28,052 | 20 | +0.0% | 4 | 27 | +14.7% |
| 1972 | $112,789 | +24.1% | $14,000 | $126,002 | $42,052 | 23 | +0.5% | 4 | 6 | +19.7% |
| 1973 | $126,002 | -14.6% | $5,379 | $102,200 | $47,431 | 25 | +0.0% | 3 | 31 | -14.4% |
| 1974 | $102,200 | -20.1% | $4,084 | $77,597 | $51,515 | 27 | +0.0% | 3 | 29 | -27.2% |
| 1975 | $77,597 | +58.3% | $12,281 | $110,530 | $63,796 | 29 | +0.0% | 3 | 32 | +36.2% |
| 1976 | $110,530 | +19.5% | $9,909 | $122,206 | $73,705 | 30 | +0.0% | 5 | 38 | +23.4% |
| 1977 | $122,206 | -4.6% | $5,827 | $110,712 | $79,532 | 32 | +0.0% | 3 | 34 | -8.4% |
| 1978 | $110,712 | +5.4% | $5,836 | $110,877 | $85,367 | 33 | +0.0% | 3 | 36 | +4.6% |
| 1979 | $110,877 | +19.9% | $9,967 | $122,929 | $95,334 | 35 | +0.0% | 4 | 41 | +16.3% |
| 1980 | $122,929 | +35.1% | $16,613 | $149,519 | $111,948 | 34 | +0.0% | 4 | 45 | +30.3% |
| 1981 | $149,519 | +5.1% | $7,855 | $149,245 | $119,803 | 31 | +0.0% | 7 | 46 | -6.5% |
| 1982 (to Aug) | $149,245 | -5.9% | $0 | $140,368 | $119,803 | 32 | +0.0% | 3 | 2 | -0.8% |

Final value $140,368, withdrawn $119,803, 472 trades, 35 closed positions (win rate +97.1%, average closed return +79.8%, median hold 60.0 months), 32 still open.

Sell reasons: withdrawal × 328, trim +50% × 42, replaced × 25, RSI(m) 80 × 4, RSI(m) 81 × 3, RSI(m) 82 × 2, RSI(m) 83 × 1

Open positions at the end: 32, of which 18 below cost (unrealised loss $-28,371). Largest: ORA (-1%, since 1981-10), PG (-13%, since 1980-10), JNJ (+41%, since 1981-07), FCFS (-39%, since 1981-01), AIG (+3%, since 1980-10), TTWO (-49%, since 1981-07), SBRA (+49%, since 1976-04), DBX (+46%, since 1976-04), STRL (-4%, since 1973-04), STWD (-24%, since 1975-07), MRSH (+36%, since 1971-10), SWK (-1%, since 1968-07), MTD (-26%, since 1969-10), NI (+14%, since 1976-10), XPO (-13%, since 1981-04)

Worst open: ENSG (-81%, since 1973-10), FSLR (-51%, since 1979-10), STLD (-49%, since 1982-01), TXT (-49%, since 1969-10), TTWO (-49%, since 1981-07), FCFS (-39%, since 1981-01), WDAY (-35%, since 1979-07), SLM (-28%, since 1968-01), MTD (-26%, since 1969-10), STWD (-24%, since 1975-07)

Best closed: FRT $11,259 (+94%), FTNT $9,369 (+94%), IESC $9,319 (+93%), MOG-A $8,762 (+88%), MTZ $8,723 (+85%)
Worst closed: KR $-25 (-3%), XOM $667 (+83%), PCTY $672 (+83%), TFC $692 (+102%), SCHW $699 (+90%)

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
| 1968-01-01 | 214 | 209 | CDNS, COO, FTNT, GILD, HAE, MOG-A, SWKS, GE, SLM, IESC |
| 1968-04-01 | 285 | 281 | GILD, XOM, MA, BDX, FTNT, PPG, UNH, WTS, CDNS, FDS |
| 1968-07-01 | 264 | 262 | SWK, AZO, FTNT, GILD, XOM, UNH, BDX, WTS, MA, ZTS |
| 1968-10-01 | 177 | 175 | KR, KO, WTS, BDX, XOM, UNH, ORA, BIIB, SWK, AZO |
| 1969-01-01 | 178 | 176 | KR, IDXX, IESC, BIIB, KO, WTS, TSCO, ORA, ED, DLTR |
| 1969-04-01 | 212 | 205 | PCTY, HL, KR, ZTS, ST, IDXX, BDX, IESC, SEIC, ED |
| 1969-07-01 | 269 | 263 | TKR, TDY, LEN, ORA, BDX, KO, CSL, AAL, CDW, RBA |
| 1969-10-01 | 392 | 384 | MTD, TXT, STLD, ORA, BDX, CHDN, AAL, UNM, MGM, MUR |
| 1970-01-01 | 426 | 413 | MTD, FNB, TXT, BDX, XPO, CHDN, TXN, ORA, D, MGM |
| 1970-04-01 | 464 | 446 | FIS, SEIC, MA, TSCO, RGEN, SLM, MTD, RDDT, BDX, TXN |
| 1970-07-01 | 664 | 637 | TFC, SWKS, LDOS, SEIC, MGM, WTS, MKC, TTWO, STLD, TKR |
| 1970-10-01 | 652 | 621 | TKR, SCHW, STLD, SEIC, SWKS, MRSH, TFC, MKC, TTWO, SWK |
| 1971-01-01 | 504 | 479 | HBAN, IDXX, TKR, IESC, PSA, SEIC, VLTO, SWK, NI, FR |
| 1971-04-01 | 329 | 311 | IESC, DAR, MNST, PSA, HRL, IDXX, NI, COO, FANG, NWE |
| 1971-07-01 | 193 | 181 | HRL, DAR, PSA, TDG, UAL, MRSH, TKR, BIO, IDXX, NI |
| 1971-10-01 | 229 | 217 | MRSH, TDG, FANG, FFIN, MRNA, HRL, TFC, DAR, XPO, AMKR |
| 1972-01-01 | 280 | 268 | SBRA, JNJ, STWD, CHTR, MRNA, TDG, DRI, D, COO, MRSH |
| 1972-04-01 | 267 | 254 | KR, SLM, CLF, VLTO, TDG, JNJ, MOH, D, COO, XPO |
| 1972-07-01 | 185 | 171 | KR, FRT, CNC, ZTS, TCBI, ANET, VOYA, CLF, TXT, T |
| 1972-10-01 | 184 | 171 | IESC, TCBI, GIS, PSA, FRT, ZTS, CASY, XPO, TRMB, KR |
| 1973-01-01 | 181 | 170 | KR, TTWO, GIS, ZTS, XPO, FRT, IESC, R, CASY, IDXX |
| 1973-04-01 | 201 | 187 | MRSH, STRL, DCI, FRT, HII, TGT, TTWO, CNX, MKC, KR |
| 1973-07-01 | 295 | 281 | AXTA, COO, CBSH, ALV, CTSH, STRL, AMT, FRT, CNX, MKC |
| 1973-10-01 | 341 | 325 | ENSG, ORA, FNB, H, DELL, GNTX, CTSH, VMRK, SWKS, FANG |
| 1974-01-01 | 429 | 412 | VOYA, STLD, CHDN, CVS, GNTX, PCTY, IBOC, H, BDX, ENSG |
| 1974-04-01 | 507 | 482 | BDX, DELL, FRT, STLD, RGEN, BAC, GNTX, H, FIS, VMRK |
| 1974-07-01 | 598 | 568 | MTZ, QCOM, TKR, H, R, J, VMRK, SEIC, FRT, AMP |
| 1974-10-01 | 820 | 780 | JBHT, KLAC, AMP, L, KDP, PSA, SEIC, AXTA, CNC, GILD |
| 1975-01-01 | 830 | 774 | TTWO, AXTA, AMP, XOM, JBHT, CLH, PSA, MRSH, HII, SEIC |
| 1975-04-01 | 711 | 660 | CLH, ROP, JBHT, ANET, AMP, PSA, GILD, BDX, CTSH, AAPL |
| 1975-07-01 | 453 | 418 | STWD, VMRK, ALV, AMP, FIS, STRL, TKR, CVNA, CTSH, GILD |
| 1975-10-01 | 342 | 312 | AAPL, IR, ANET, NKE, MRSH, ALB, ORA, CUBE, MUR, HRL |
| 1976-01-01 | 326 | 299 | AAPL, NKE, OHI, TSLA, MRSH, HRL, MTD, DELL, ORA, ANET |
| 1976-04-01 | 244 | 224 | DBX, SBRA, TSLA, OHI, STRL, HRL, DELL, VICR, AAPL, NKE |
| 1976-07-01 | 156 | 138 | CLX, DLB, DELL, EXPE, KDP, KR, VFC, MO, LEA, ZTS |
| 1976-10-01 | 175 | 155 | NI, CLX, LEA, SBRA, CNP, ZTS, PRI, DLB, DAL, KR |
| 1977-01-01 | 174 | 160 | COO, CNP, KR, PRI, MTD, STAG, SBRA, JAZZ, MO, KHC |
| 1977-04-01 | 243 | 232 | BDX, DLTR, ALB, TSCO, QCOM, AIG, XOM, MTD, STAG, VLTO |
| 1977-07-01 | 289 | 272 | AAPL, KR, QCOM, ST, TDY, DLTR, ALB, BKR, TSCO, XPO |
| 1977-10-01 | 334 | 314 | ANET, CL, ALB, KR, KDP, ST, MTD, L, DELL, JBL |
| 1978-01-01 | 371 | 349 | FCFS, L, ANET, DELL, TFC, J, ROP, CL, KR, JBL |
| 1978-04-01 | 477 | 449 | TSLA, DBX, SEIC, H, DELL, TKR, L, ROP, NXST, FCFS |
| 1978-07-01 | 449 | 427 | SWKS, VTRS, FCFS, SBRA, INTU, TFC, H, TSLA, AMP, CHTR |
| 1978-10-01 | 251 | 233 | AZO, PSA, CLH, DELL, ZION, GILD, TSLA, CHTR, INTU, SWKS |
| 1979-01-01 | 323 | 301 | IBOC, RTX, AZO, MTD, L, KNF, SWK, GNTX, PSA, ENSG |
| 1979-04-01 | 342 | 321 | AAPL, CLX, IBOC, DLB, DLTR, L, SWK, GNTX, MTD, DELL |
| 1979-07-01 | 278 | 259 | STRL, WDAY, DLTR, AAPL, CLX, L, CNX, TKR, DELL, DLB |
| 1979-10-01 | 238 | 220 | FSLR, TKR, WDAY, APP, STRL, DLTR, CLX, CDNS, DELL, AAPL |
| 1980-01-01 | 224 | 204 | EQIX, ECL, VMC, FSLR, HSY, TKR, CDNS, TSLA, STRL, PSA |
| 1980-04-01 | 244 | 227 | PVH, EQIX, LIVN, CDNS, WDAY, CTAS, ECL, VVV, TKR, IESC |
| 1980-07-01 | 203 | 188 | CXT, AIG, SPGI, GILD, GDDY, PVH, GBCI, MKC, BJ, CTAS |
| 1980-10-01 | 169 | 156 | PG, AIG, KTOS, AM, MKC, FCFS, SPGI, LPX, GILD, MO |
| 1981-01-01 | 101 | 95 | FCFS, VRSK, ED, HAS, TREX, DGX, MCD, PG, MNST, SPGI |
| 1981-04-01 | 102 | 94 | XPO, WELL, DGX, GILD, ED, VRSK, LEN, MCD, FFIN, ELF |
| 1981-07-01 | 124 | 115 | TTWO, JNJ, GILD, ARES, GBCI, TRGP, PSA, SWX, HBAN, CDNS |
| 1981-10-01 | 256 | 243 | ORA, L, XOM, TDG, INTU, CASY, CLX, TTWO, PSA, AMP |
| 1982-01-01 | 284 | 272 | MTD, STLD, NSC, LEA, CASY, AIG, AMP, TDG, GILD, ORA |
| 1982-04-01 | 368 | 354 | DRI, CL, QCOM, NI, HUBB, NSC, ALLY, MTD, LEA, SCHW |
| 1982-07-01 | 436 | 416 | CL, DRI, WTS, IESC, RMD, NI, NSC, HUBB, MTD, LPX |