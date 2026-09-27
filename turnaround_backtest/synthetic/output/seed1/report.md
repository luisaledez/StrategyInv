# Synthetic lost decade (1968-1982 market, seed 1) — 1968-01-01 to 1982-08-31

Quarterly scan (1 Jan / 1 Apr / 1 Jul / 1 Oct) with the turnaround scanner's rules (monthly RSI(14) < 42 within the last 6 completed months, ≥ 5 years of history, ≥ $5M average daily dollar volume, ≥ $1B market cap), then: profitable now and in the past, top 20 by trailing-twelve-month revenue growth, top 10 of those by valuation versus the company's own history (mean percentile of trailing P/E, P/S and EV/EBITDA). $100,000 start, at most 10% of the portfolio per stock, no taxes, commissions or slippage, dividends credited as cash, idle cash earns nothing.

Withdrawal rule at each year end: year return > 20% → 10% of the portfolio; 10–20% → 7.5%; below 10% (including losses) → 5%. The partial year 2026 has no withdrawal.

**Synthetic data.** The market is the real S&P 500 daily path from 1962 to August 1982 (Yahoo ^GSPC); each of today's S&P 500 + 400 stocks is re-simulated on it with its own real beta and a block bootstrap of its own real idiosyncratic daily returns (2004-2026), so single-stock crashes and rebounds are realistic while the market goes nowhere. Quarterly fundamentals are generated: revenue grows with CPI inflation plus a company-specific real rate plus part of the stock's own price residual; net margins swing with the stock's residual and the market and can turn negative; EBITDA, debt, cash, shares and the starting market cap are scaled from each company's latest real filing. Dividend yield 3.5%. The benchmark 'Index' is the S&P 500 price path with the same dividends reinvested.

**Read it as a stress test, not a forecast.** Nothing in the generated fundamentals knows the future price, and nothing in the prices knows the fundamentals beyond the contemporaneous link above, so the selection rules cannot cheat. Real (inflation-adjusted) figures use BLS CPI-U annual averages: the CPI rose about 180% over the window, so a nominal result must roughly triple just to stand still.

## Scenario summary

| Scenario | Start | First buy | Final value | Withdrawn | Final + withdrawn | CAGR (final) | CAGR (no-withdrawal index) | IRR | Max DD | Closed trades | Win rate | Avg closed ret. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **base** | 1968 | 1968-01-02 | $132,546 | $111,648 | $244,193 | +1.9% | +9.2% | +8.7% | -38.4% | 23 | +100.0% | +85.5% |
| **no_trim** | 1968 | 1968-01-02 | $150,829 | $111,775 | $262,604 | +2.8% | +9.8% | +9.1% | -35.5% | 26 | +100.0% | +114.1% |
| **rotate** | 1968 | 1968-01-02 | $131,191 | $116,980 | $248,171 | +1.9% | +9.2% | +8.9% | -44.8% | 363 | +57.0% | +4.2% |
| **base_no_wd** | 1968 | 1968-01-02 | $351,478 | $0 | $351,478 | +8.9% | +8.9% | +8.9% | -40.8% | 27 | +100.0% | +99.5% |
| **rsi80** | 1968 | 1968-01-02 | $124,838 | $111,203 | $236,041 | +1.5% | +8.8% | +8.4% | -38.4% | 23 | +100.0% | +82.3% |
| Index (1968) | 1968 | 1968-01-02 | $76,803 | $85,432 | $162,236 | -1.8% | +5.1% | +4.8% | -44.9% |  |  |  |

CAGR (final) compounds the ending value after withdrawals; the no-withdrawal index chains the yearly returns as if nothing had been taken out; IRR is the money-weighted return of the $100,000 in, the withdrawals out and the final value. Max DD is on the no-withdrawal index.

## base — Base: trim half at +50%, hold rest, RSI(m) 90 exit, replace >100% winners

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +15.2% | $8,640 | $106,557 | $8,640 | 13 | +0.0% | 13 | 14 | +11.9% |
| 1969 | $106,557 | -5.5% | $5,035 | $95,668 | $13,675 | 15 | +3.0% | 3 | 4 | -8.2% |
| 1970 | $95,668 | +5.4% | $5,041 | $95,778 | $18,716 | 19 | +3.7% | 4 | 3 | +3.6% |
| 1971 | $95,778 | +10.9% | $7,969 | $98,286 | $26,685 | 23 | +0.0% | 4 | 26 | +14.7% |
| 1972 | $98,286 | +26.9% | $12,474 | $112,269 | $39,159 | 24 | +0.0% | 3 | 28 | +19.7% |
| 1973 | $112,269 | -11.1% | $4,990 | $94,806 | $44,149 | 27 | +0.0% | 5 | 32 | -14.4% |
| 1974 | $94,806 | -21.3% | $3,730 | $70,866 | $47,879 | 30 | +0.0% | 4 | 31 | -27.2% |
| 1975 | $70,866 | +39.3% | $9,871 | $88,842 | $57,750 | 33 | +0.0% | 3 | 36 | +36.2% |
| 1976 | $88,842 | +32.0% | $11,728 | $105,550 | $69,478 | 34 | +0.0% | 4 | 40 | +23.4% |
| 1977 | $105,550 | -3.2% | $5,107 | $97,035 | $74,585 | 36 | +0.0% | 3 | 38 | -8.4% |
| 1978 | $97,035 | +19.1% | $8,666 | $106,875 | $83,251 | 39 | +0.0% | 4 | 45 | +4.6% |
| 1979 | $106,875 | +9.7% | $5,864 | $111,406 | $89,114 | 38 | +0.0% | 4 | 45 | +16.3% |
| 1980 | $111,406 | +39.8% | $15,571 | $140,138 | $104,685 | 39 | +0.0% | 5 | 48 | +30.3% |
| 1981 | $140,138 | -0.6% | $6,963 | $132,293 | $111,648 | 40 | +0.0% | 4 | 46 | -6.5% |
| 1982 (to Aug) | $132,293 | +0.2% | $0 | $132,546 | $111,648 | 42 | +1.2% | 2 | 1 | -0.8% |

Final value $132,546, withdrawn $111,648, 502 trades, 23 closed positions (win rate +100.0%, average closed return +85.5%, median hold 51.0 months), 42 still open.

Sell reasons: withdrawal × 376, trim +50% × 38, replaced × 23

Open positions at the end: 42, of which 25 below cost (unrealised loss $-28,825). Largest: TER (+46%, since 1981-07), ARW (+37%, since 1981-04), TJX (-10%, since 1980-07), DTM (-1%, since 1980-10), LVS (-15%, since 1979-10), MKC (-27%, since 1980-07), AES (+51%, since 1978-10), CDNS (+27%, since 1979-10), XYL (-1%, since 1981-10), CUBE (+32%, since 1976-10), SYF (-32%, since 1973-04), OKTA (-30%, since 1981-01), UNP (+59%, since 1969-07), AFL (+3%, since 1971-04), IFF (-42%, since 1968-01)

Worst open: MP (-93%, since 1975-04), GAP (-93%, since 1968-01), AVTR (-83%, since 1968-10), CRWD (-73%, since 1977-07), COIN (-70%, since 1971-01), BSX (-67%, since 1973-01), FND (-58%, since 1974-07), CNO (-55%, since 1970-01), BBY (-50%, since 1972-04), WMB (-45%, since 1976-07)

Best closed: GLPI $9,234 (+78%), KMI $9,022 (+90%), MS $8,991 (+95%), TDG $8,955 (+90%), CART $8,919 (+90%)
Worst closed: FND $559 (+80%), LSTR $651 (+81%), DCI $686 (+76%), SPXC $766 (+97%), TER $800 (+94%)

## no_trim — No trim: hold until RSI(m) 90 exit or replaced

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +16.6% | $8,743 | $107,825 | $8,743 | 13 | +0.0% | 13 | 13 | +11.9% |
| 1969 | $107,825 | -4.6% | $5,141 | $97,682 | $13,884 | 16 | +0.0% | 4 | 17 | -8.2% |
| 1970 | $97,682 | +0.8% | $4,922 | $93,509 | $18,805 | 19 | +0.0% | 3 | 19 | +3.6% |
| 1971 | $93,509 | +8.9% | $5,093 | $96,775 | $23,899 | 22 | +0.0% | 3 | 22 | +14.7% |
| 1972 | $96,775 | +19.6% | $8,680 | $107,057 | $32,579 | 23 | +0.0% | 3 | 25 | +19.7% |
| 1973 | $107,057 | -5.8% | $5,044 | $95,839 | $37,623 | 26 | +0.0% | 5 | 28 | -14.4% |
| 1974 | $95,839 | -10.8% | $4,276 | $81,250 | $41,900 | 29 | +0.0% | 4 | 30 | -27.2% |
| 1975 | $81,250 | +29.0% | $10,483 | $94,344 | $52,382 | 32 | +0.0% | 3 | 32 | +36.2% |
| 1976 | $94,344 | +38.9% | $13,108 | $117,968 | $65,490 | 35 | +0.0% | 6 | 38 | +23.4% |
| 1977 | $117,968 | -6.4% | $5,521 | $104,898 | $71,011 | 37 | +0.0% | 4 | 39 | -8.4% |
| 1978 | $104,898 | +15.7% | $9,106 | $112,303 | $80,116 | 39 | +0.0% | 3 | 40 | +4.6% |
| 1979 | $112,303 | +7.4% | $6,032 | $114,616 | $86,149 | 38 | +0.0% | 5 | 44 | +16.3% |
| 1980 | $114,616 | +56.0% | $17,876 | $160,886 | $104,025 | 38 | +0.0% | 5 | 43 | +30.3% |
| 1981 | $160,886 | -3.7% | $7,750 | $147,253 | $111,775 | 40 | +0.0% | 5 | 43 | -6.5% |
| 1982 (to Aug) | $147,253 | +2.4% | $0 | $150,829 | $111,775 | 42 | +0.0% | 2 | 0 | -0.8% |

Final value $150,829, withdrawn $111,775, 501 trades, 26 closed positions (win rate +100.0%, average closed return +114.1%, median hold 52.5 months), 42 still open.

Sell reasons: withdrawal × 407, replaced × 26

Open positions at the end: 42, of which 24 below cost (unrealised loss $-22,981). Largest: TER (+46%, since 1981-07), DTM (-1%, since 1980-10), CDNS (+27%, since 1979-10), MKC (-12%, since 1980-10), AES (+51%, since 1978-10), LVS (-15%, since 1979-10), VMRK (-14%, since 1979-10), UNP (+59%, since 1969-07), ROST (+21%, since 1980-10), TJX (-10%, since 1980-07), PEP (+24%, since 1977-01), RGEN (-24%, since 1976-01), OKTA (-30%, since 1981-01), DG (-27%, since 1968-01), ALLE (+1%, since 1979-07)

Worst open: MP (-93%, since 1975-04), GAP (-93%, since 1968-01), AVTR (-83%, since 1968-10), WMB (-74%, since 1973-10), CRWD (-73%, since 1977-07), BSX (-67%, since 1973-01), FND (-58%, since 1974-07), BBY (-50%, since 1972-04), ADP (-44%, since 1968-01), IFF (-42%, since 1968-01)

Best closed: EQT $12,993 (+166%), PTC $12,989 (+108%), TDG $11,631 (+116%), DDOG $11,439 (+114%), KMI $11,208 (+112%)
Worst closed: FND $739 (+107%), LSTR $846 (+106%), PG $878 (+99%), DCI $896 (+103%), OSK $1,027 (+104%)

## rotate — Rotate: hold exactly the current top 10 each quarter

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +23.5% | $12,350 | $111,148 | $12,350 | 10 | +0.0% | 32 | 32 | +11.9% |
| 1969 | $111,148 | -3.2% | $5,378 | $102,177 | $17,728 | 10 | +0.0% | 24 | 34 | -8.2% |
| 1970 | $102,177 | +4.1% | $5,319 | $101,069 | $23,047 | 10 | +1.3% | 23 | 23 | +3.6% |
| 1971 | $101,069 | +4.1% | $5,262 | $99,974 | $28,309 | 10 | +0.0% | 20 | 30 | +14.7% |
| 1972 | $99,974 | +18.6% | $8,890 | $109,641 | $37,199 | 10 | +0.0% | 20 | 30 | +19.7% |
| 1973 | $109,641 | -0.6% | $5,451 | $103,573 | $42,650 | 10 | +0.0% | 28 | 38 | -14.4% |
| 1974 | $103,573 | -30.1% | $3,618 | $68,742 | $46,268 | 10 | +0.0% | 28 | 38 | -27.2% |
| 1975 | $68,742 | +64.9% | $11,338 | $102,041 | $57,606 | 10 | +1.1% | 25 | 25 | +36.2% |
| 1976 | $102,041 | +13.7% | $8,701 | $107,310 | $66,306 | 10 | +0.0% | 24 | 34 | +23.4% |
| 1977 | $107,310 | -4.3% | $5,134 | $97,555 | $71,441 | 10 | +0.0% | 28 | 38 | -8.4% |
| 1978 | $97,555 | +29.8% | $12,660 | $113,939 | $84,101 | 10 | +0.0% | 25 | 35 | +4.6% |
| 1979 | $113,939 | +8.9% | $6,202 | $117,831 | $90,302 | 10 | +0.0% | 25 | 35 | +16.3% |
| 1980 | $117,831 | +29.2% | $15,223 | $137,006 | $105,525 | 10 | +0.0% | 25 | 35 | +30.3% |
| 1981 | $137,006 | +11.5% | $11,454 | $141,271 | $116,980 | 10 | +0.0% | 30 | 40 | -6.5% |
| 1982 (to Aug) | $141,271 | -7.1% | $0 | $131,191 | $116,980 | 10 | +2.9% | 16 | 16 | -0.8% |

Final value $131,191, withdrawn $116,980, 856 trades, 363 closed positions (win rate +57.0%, average closed return +4.2%, median hold 3.0 months), 10 still open.

Sell reasons: left list × 363, withdrawal × 120

Open positions at the end: 10, of which 5 below cost (unrealised loss $-3,878). Largest: PBF (+95%, since 1982-07), UNH (-1%, since 1982-01), DTM (+16%, since 1982-07), AFG (+5%, since 1982-04), BKR (+3%, since 1982-04), XRAY (+11%, since 1982-07), LFUS (-0%, since 1982-04), XYL (-3%, since 1982-04), DLR (-10%, since 1982-07), TREX (-18%, since 1982-04)

Worst open: TREX (-18%, since 1982-04), DLR (-10%, since 1982-07), XYL (-3%, since 1982-04), UNH (-1%, since 1982-01), LFUS (-0%, since 1982-04)

Best closed: THC $9,990 (+104%), FND $9,245 (+102%), RDDT $8,562 (+95%), STT $8,269 (+75%), TER $6,466 (+57%)
Worst closed: NXST $-5,890 (-54%), LVS $-5,854 (-47%), CNO $-5,853 (-51%), CNO $-5,682 (-42%), WMB $-5,120 (-43%)

## base_no_wd — Base without withdrawals

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +15.2% | $0 | $115,197 | $0 | 13 | +0.9% | 13 | 1 | +11.9% |
| 1969 | $115,197 | -5.6% | $0 | $108,734 | $0 | 16 | +7.8% | 4 | 4 | -8.2% |
| 1970 | $108,734 | +6.9% | $0 | $116,190 | $0 | 20 | +8.7% | 4 | 4 | +3.6% |
| 1971 | $116,190 | +9.9% | $0 | $127,712 | $0 | 25 | +0.8% | 5 | 3 | +14.7% |
| 1972 | $127,712 | +29.1% | $0 | $164,879 | $0 | 27 | +1.4% | 4 | 4 | +19.7% |
| 1973 | $164,879 | -13.6% | $0 | $142,494 | $0 | 30 | +0.9% | 5 | 4 | -14.4% |
| 1974 | $142,494 | -22.7% | $0 | $110,223 | $0 | 34 | +0.9% | 5 | 2 | -27.2% |
| 1975 | $110,223 | +39.6% | $0 | $153,883 | $0 | 37 | +0.9% | 4 | 5 | +36.2% |
| 1976 | $153,883 | +34.2% | $0 | $206,541 | $0 | 37 | +0.8% | 4 | 7 | +23.4% |
| 1977 | $206,541 | -5.0% | $0 | $196,244 | $0 | 40 | +0.9% | 4 | 2 | -8.4% |
| 1978 | $196,244 | +19.1% | $0 | $233,768 | $0 | 44 | +0.8% | 5 | 7 | +4.6% |
| 1979 | $233,768 | +11.0% | $0 | $259,456 | $0 | 44 | +0.9% | 5 | 8 | +16.3% |
| 1980 | $259,456 | +39.5% | $0 | $361,808 | $0 | 45 | +6.0% | 6 | 13 | +30.3% |
| 1981 | $361,808 | -1.9% | $0 | $354,843 | $0 | 46 | +0.9% | 5 | 7 | -6.5% |
| 1982 (to Aug) | $354,843 | -0.9% | $0 | $351,478 | $0 | 49 | +1.3% | 3 | 1 | -0.8% |

Final value $351,478, withdrawn $0, 148 trades, 27 closed positions (win rate +100.0%, average closed return +99.5%, median hold 33.1 months), 49 still open.

Sell reasons: trim +50% × 45, replaced × 27

Open positions at the end: 49, of which 28 below cost (unrealised loss $-77,945). Largest: TER (+46%, since 1981-07), TJX (-10%, since 1980-07), ARW (+37%, since 1981-04), OKTA (-30%, since 1981-01), DTM (-1%, since 1980-10), LVS (-15%, since 1979-10), MKC (-27%, since 1980-07), AES (+51%, since 1978-10), CDNS (+27%, since 1979-10), AFL (+3%, since 1971-04), XYL (-1%, since 1981-10), SYF (-32%, since 1973-04), CUBE (+32%, since 1976-10), UNP (+59%, since 1969-07), IFF (-42%, since 1968-01)

Worst open: MP (-93%, since 1975-04), GAP (-93%, since 1968-01), AVTR (-83%, since 1968-10), CRWD (-73%, since 1977-07), COIN (-70%, since 1971-01), BSX (-67%, since 1973-01), FND (-58%, since 1974-07), CNO (-55%, since 1970-01), BBY (-50%, since 1972-04), WMB (-45%, since 1976-07)

Best closed: MS $20,375 (+98%), GLPI $20,234 (+84%), EQT $15,739 (+154%), CART $12,704 (+109%), HLI $12,465 (+105%)
Worst closed: FND $649 (+82%), LSTR $807 (+101%), SPXC $893 (+100%), FLS $935 (+88%), USB $1,008 (+99%)

## rsi80 — Base with the monthly-RSI exit at 80 instead of 90

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +15.2% | $8,640 | $106,557 | $8,640 | 13 | +0.0% | 13 | 14 | +11.9% |
| 1969 | $106,557 | -5.5% | $5,035 | $95,668 | $13,675 | 15 | +3.0% | 3 | 4 | -8.2% |
| 1970 | $95,668 | +5.4% | $5,041 | $95,778 | $18,716 | 19 | +3.7% | 4 | 3 | +3.6% |
| 1971 | $95,778 | +10.9% | $7,969 | $98,286 | $26,685 | 23 | +0.0% | 4 | 26 | +14.7% |
| 1972 | $98,286 | +26.9% | $12,474 | $112,269 | $39,159 | 24 | +0.0% | 3 | 28 | +19.7% |
| 1973 | $112,269 | -11.1% | $4,990 | $94,806 | $44,149 | 27 | +0.0% | 5 | 32 | -14.4% |
| 1974 | $94,806 | -21.3% | $3,730 | $70,866 | $47,879 | 30 | +0.0% | 4 | 31 | -27.2% |
| 1975 | $70,866 | +39.3% | $9,871 | $88,842 | $57,750 | 33 | +0.0% | 3 | 36 | +36.2% |
| 1976 | $88,842 | +32.0% | $11,728 | $105,550 | $69,478 | 34 | +0.0% | 4 | 40 | +23.4% |
| 1977 | $105,550 | -3.2% | $5,107 | $97,035 | $74,585 | 36 | +0.0% | 3 | 38 | -8.4% |
| 1978 | $97,035 | +19.1% | $8,666 | $106,875 | $83,251 | 39 | +0.0% | 4 | 45 | +4.6% |
| 1979 | $106,875 | +9.6% | $5,855 | $111,244 | $89,106 | 38 | +0.0% | 4 | 45 | +16.3% |
| 1980 | $111,244 | +39.2% | $15,485 | $139,366 | $104,591 | 38 | +0.0% | 5 | 48 | +30.3% |
| 1981 | $139,366 | -5.1% | $6,612 | $125,635 | $111,203 | 40 | +0.0% | 4 | 45 | -6.5% |
| 1982 (to Aug) | $125,635 | -0.6% | $0 | $124,838 | $111,203 | 42 | +1.3% | 2 | 1 | -0.8% |

Final value $124,838, withdrawn $111,203, 501 trades, 23 closed positions (win rate +100.0%, average closed return +82.3%, median hold 51.0 months), 42 still open.

Sell reasons: withdrawal × 375, trim +50% × 38, replaced × 20, RSI(m) 81 × 2, RSI(m) 83 × 1

Open positions at the end: 42, of which 25 below cost (unrealised loss $-29,790). Largest: ARW (+37%, since 1981-04), TJX (-10%, since 1980-07), LVS (-15%, since 1979-10), MKC (-27%, since 1980-07), DTM (-1%, since 1980-10), AES (+51%, since 1978-10), CDNS (+27%, since 1979-10), XYL (-1%, since 1981-10), CUBE (+32%, since 1976-10), SYF (-32%, since 1973-04), OKTA (-30%, since 1981-01), UNP (+59%, since 1969-07), AFL (+3%, since 1971-04), IFF (-42%, since 1968-01), ADP (-44%, since 1968-01)

Worst open: MP (-93%, since 1975-04), GAP (-93%, since 1968-01), AVTR (-83%, since 1968-10), CRWD (-73%, since 1977-07), COIN (-70%, since 1971-01), BSX (-67%, since 1973-01), FND (-58%, since 1974-07), CNO (-55%, since 1970-01), BBY (-50%, since 1972-04), WMB (-45%, since 1976-07)

Best closed: GLPI $9,234 (+78%), KMI $9,022 (+90%), MS $8,991 (+95%), TDG $8,955 (+90%), CART $8,919 (+90%)
Worst closed: FND $559 (+80%), LSTR $651 (+81%), DCI $686 (+76%), FLR $707 (+84%), SPXC $766 (+97%)

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
| 1968-01-01 | 223 | 213 | TREX, DDOG, ADP, GAP, KMI, IFF, DG, TDG, SAIC, CPT |
| 1968-04-01 | 295 | 285 | LSTR, ADP, SN, WFC, WTW, UNP, MRK, NVR, D, TT |
| 1968-07-01 | 286 | 273 | NVST, MGM, ADP, SAIC, RGLD, UNP, RBC, MLI, WTW, TDG |
| 1968-10-01 | 201 | 188 | SAIC, AVTR, AVAV, UNP, RMD, MGM, NEE, EBAY, RGLD, SN |
| 1969-01-01 | 201 | 190 | LEN, DHI, GE, UNP, SAIC, IRT, AVTR, USB, ILMN, EBAY |
| 1969-04-01 | 251 | 235 | ADP, CR, SBRA, IDA, AAPL, UNP, NI, RRX, NEE, DHI |
| 1969-07-01 | 303 | 285 | UNP, ADP, ATR, IDA, CR, NI, SBRA, SAIC, PTC, TWLO |
| 1969-10-01 | 386 | 367 | DOCS, KVUE, IDXX, CART, UNP, ATR, USB, ROST, SBRA, IDA |
| 1970-01-01 | 438 | 416 | CNO, BMY, SAIC, EQT, MP, CART, FND, IDA, JEF, UNP |
| 1970-04-01 | 501 | 482 | SPXC, DLR, AGCO, CART, EQT, SN, CNO, FND, XYL, WY |
| 1970-07-01 | 682 | 659 | FND, INTC, WY, PG, FBIN, SN, FLS, TDG, SYF, AGCO |
| 1970-10-01 | 657 | 631 | INTC, COIN, PG, DCI, SN, FBIN, WY, NWS, FLS, UNP |
| 1971-01-01 | 515 | 493 | COIN, PG, INTC, DCI, WEC, GE, NWS, FBIN, UNP, DG |
| 1971-04-01 | 342 | 324 | AFL, IDA, UNP, WEC, DCI, COIN, PODD, VTRS, GE, PG |
| 1971-07-01 | 186 | 173 | ADP, IBM, AFL, RRX, WEC, WYNN, IDA, TJX, THC, COIN |
| 1971-10-01 | 210 | 198 | DCI, WYNN, CR, TJX, CART, FBIN, XYL, ROST, GE, WEC |
| 1972-01-01 | 263 | 246 | TREX, ROST, IDA, BBY, CART, DCI, FNB, AMZN, WYNN, CR |
| 1972-04-01 | 244 | 230 | BBY, ROST, JLL, TREX, CART, FNB, DCI, IBOC, WYNN, PG |
| 1972-07-01 | 169 | 156 | CART, PM, NOW, FFIN, MUSA, CMS, LSTR, TREX, ROST, INTC |
| 1972-10-01 | 184 | 169 | LEN, REG, CR, IPGP, LSTR, NOW, TREX, CART, ALGM, ROST |
| 1973-01-01 | 179 | 166 | BSX, TREX, LSTR, REG, AES, CR, BBY, LEN, STT, CSGP |
| 1973-04-01 | 209 | 198 | SYF, RRC, WEC, LSTR, XYL, HAL, BSX, CHRD, CNP, MUSA |
| 1973-07-01 | 305 | 290 | RRX, IDA, KEX, XYL, PM, REG, RRC, CUBE, SYF, ETR |
| 1973-10-01 | 350 | 332 | THC, WMB, LAD, CNO, UNP, FNB, RRX, CBT, XYL, RVTY |
| 1974-01-01 | 437 | 414 | MUSA, JKHY, LAD, JEF, AVAV, UNP, CINF, WMB, ALK, AMKR |
| 1974-04-01 | 510 | 479 | TER, LSTR, AFL, CNO, DHI, CART, COIN, RVTY, WMB, UNP |
| 1974-07-01 | 591 | 556 | FND, CNO, WY, EQT, LEN, DHI, NXST, USB, CEG, TER |
| 1974-10-01 | 820 | 769 | EQT, FLS, ZBRA, COHR, LFUS, WY, MDT, PG, TER, LEN |
| 1975-01-01 | 829 | 759 | USB, TER, IPGP, SN, CNO, COHR, PG, MDT, EQT, ZBRA |
| 1975-04-01 | 726 | 658 | MP, COHR, USB, PG, BBY, LSTR, TER, NEE, OMC, CPT |
| 1975-07-01 | 461 | 405 | PG, DLR, GXO, INTC, CART, BBY, THC, IDA, RGEN, DRI |
| 1975-10-01 | 333 | 294 | IPGP, INTC, DLR, PG, IR, GLPI, GIS, BSX, ACN, BC |
| 1976-01-01 | 326 | 298 | RGEN, IPGP, GLPI, INTC, WTRG, PG, HLI, BF-B, WMB, CHRD |
| 1976-04-01 | 230 | 208 | HLI, AMCR, WMB, LAD, PG, IPGP, FND, LHX, WTRG, INTC |
| 1976-07-01 | 147 | 135 | WMB, PTC, MGM, BXP, VEEV, IPGP, MP, IRM, EG, SWK |
| 1976-10-01 | 152 | 138 | CUBE, FND, MP, WMB, FTI, KR, LECO, RNR, BXP, VEEV |
| 1977-01-01 | 162 | 150 | PEP, LFUS, KNSL, KR, BBY, GEF, BXP, FND, WMB, CUBE |
| 1977-04-01 | 251 | 224 | EQT, FLR, MDT, DHI, PH, WMB, KEX, RGEN, AOS, COHR |
| 1977-07-01 | 305 | 279 | CRWD, UBER, FLR, BC, AVAV, PAG, KEX, DHI, MDT, GEF |
| 1977-10-01 | 356 | 329 | WY, CRWD, ORA, PAG, LEN, RS, CNO, EGP, FBIN, NOW |
| 1978-01-01 | 411 | 381 | THC, WY, SANM, FIX, FBIN, RVTY, AVGO, CNO, LEN, PAG |
| 1978-04-01 | 512 | 478 | FND, VICR, ADI, FBIN, WY, CNO, LEN, THC, RDDT, INTC |
| 1978-07-01 | 493 | 462 | MS, USB, ALGM, VICR, CNO, THC, ADP, FND, SPG, RVTY |
| 1978-10-01 | 292 | 273 | GLPI, AES, TWLO, MS, EQT, WY, WAL, FTI, BC, MGM |
| 1979-01-01 | 308 | 286 | SPG, EQT, GLPI, DVA, HPQ, BALL, ECL, SFM, CNO, WY |
| 1979-04-01 | 347 | 323 | OSK, ECL, EQT, CRWD, CNO, WY, ATO, FBIN, AVNT, SFM |
| 1979-07-01 | 282 | 255 | ALLE, ADP, VMRK, CLH, WY, TKO, PRI, CNO, WHR, AOS |
| 1979-10-01 | 235 | 213 | LVS, CDNS, VMRK, ALLE, LEN, MRSH, AOS, CUBE, WHR, CNO |
| 1980-01-01 | 243 | 221 | ROST, CDNS, TREX, XYL, FBIN, AVGO, UNP, UBER, JPM, LEN |
| 1980-04-01 | 284 | 258 | RCL, QCOM, CDNS, PAG, THG, MDT, XYL, UNP, HAL, FBIN |
| 1980-07-01 | 256 | 227 | TJX, MKC, PAG, DTM, ROST, QCOM, CDNS, CNO, WEC, UNP |
| 1980-10-01 | 211 | 192 | MKC, DTM, ROST, MANH, PAG, CNO, RS, GD, GRMN, AGCO |
| 1981-01-01 | 112 | 99 | OKTA, MANH, TNL, UNH, MKC, GMED, OGE, BKH, DGX, TWLO |
| 1981-04-01 | 124 | 114 | MKC, ARW, MP, OKTA, RVTY, EQIX, UNH, WEX, THC, MANH |
| 1981-07-01 | 150 | 139 | TER, WMB, ABBV, FERG, CNO, MKC, UNH, WEC, FND, CTSH |
| 1981-10-01 | 259 | 237 | CNO, XYL, CI, WMB, SN, BKH, GD, BBY, OSK, COHR |
| 1982-01-01 | 291 | 267 | UNH, CPAY, PAYX, FNB, BBY, CNO, WMB, BKNG, LEN, JPM |
| 1982-04-01 | 395 | 369 | UNH, PAYX, LFUS, CNO, TREX, BBY, AFG, WMB, XYL, BKR |
| 1982-07-01 | 465 | 433 | DTM, LFUS, DLR, XRAY, AFG, TREX, UNH, PBF, BKR, XYL |