# Synthetic lost decade (1968-1982 market, seed 3) — 1968-01-01 to 1982-08-31

Quarterly scan (1 Jan / 1 Apr / 1 Jul / 1 Oct) with the turnaround scanner's rules (monthly RSI(14) < 42 within the last 6 completed months, ≥ 5 years of history, ≥ $5M average daily dollar volume, ≥ $1B market cap), then: profitable now and in the past, top 20 by trailing-twelve-month revenue growth, top 10 of those by valuation versus the company's own history (mean percentile of trailing P/E, P/S and EV/EBITDA). $100,000 start, at most 10% of the portfolio per stock, no taxes, commissions or slippage, dividends credited as cash, idle cash earns nothing.

Withdrawal rule at each year end: year return > 20% → 10% of the portfolio; 10–20% → 7.5%; below 10% (including losses) → 5%. The partial year 2026 has no withdrawal.

**Synthetic data.** The market is the real S&P 500 daily path from 1962 to August 1982 (Yahoo ^GSPC); each of today's S&P 500 + 400 stocks is re-simulated on it with its own real beta and a block bootstrap of its own real idiosyncratic daily returns (2004-2026), so single-stock crashes and rebounds are realistic while the market goes nowhere. Quarterly fundamentals are generated: revenue grows with CPI inflation plus a company-specific real rate plus part of the stock's own price residual; net margins swing with the stock's residual and the market and can turn negative; EBITDA, debt, cash, shares and the starting market cap are scaled from each company's latest real filing. Dividend yield 3.5%. The benchmark 'Index' is the S&P 500 price path with the same dividends reinvested.

**Read it as a stress test, not a forecast.** Nothing in the generated fundamentals knows the future price, and nothing in the prices knows the fundamentals beyond the contemporaneous link above, so the selection rules cannot cheat. Real (inflation-adjusted) figures use BLS CPI-U annual averages: the CPI rose about 180% over the window, so a nominal result must roughly triple just to stand still.

## Scenario summary

| Scenario | Start | First buy | Final value | Withdrawn | Final + withdrawn | CAGR (final) | CAGR (no-withdrawal index) | IRR | Max DD | Closed trades | Win rate | Avg closed ret. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **base** | 1968 | 1968-01-02 | $85,504 | $92,903 | $178,407 | -1.1% | +5.8% | +5.8% | -47.4% | 21 | +100.0% | +86.5% |
| **no_trim** | 1968 | 1968-01-02 | $76,934 | $86,172 | $163,106 | -1.8% | +5.1% | +4.9% | -52.2% | 20 | +100.0% | +114.9% |
| **rotate** | 1968 | 1968-01-02 | $218,251 | $160,422 | $378,673 | +5.5% | +14.1% | +13.6% | -52.8% | 357 | +59.1% | +6.3% |
| **base_no_wd** | 1968 | 1968-01-02 | $238,986 | $0 | $238,986 | +6.1% | +6.1% | +6.1% | -49.0% | 22 | +100.0% | +98.3% |
| **rsi80** | 1968 | 1968-01-02 | $85,238 | $90,777 | $176,015 | -1.1% | +5.6% | +5.6% | -47.4% | 23 | +100.0% | +79.1% |
| Index (1968) | 1968 | 1968-01-02 | $76,803 | $85,432 | $162,236 | -1.8% | +5.1% | +4.8% | -44.9% |  |  |  |

CAGR (final) compounds the ending value after withdrawals; the no-withdrawal index chains the yearly returns as if nothing had been taken out; IRR is the money-weighted return of the $100,000 in, the withdrawals out and the final value. Max DD is on the no-withdrawal index.

## base — Base: trim half at +50%, hold rest, RSI(m) 90 exit, replace >100% winners

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +6.7% | $5,336 | $101,392 | $5,336 | 13 | +3.3% | 13 | 1 | +11.9% |
| 1969 | $101,392 | -6.7% | $4,733 | $89,919 | $10,069 | 17 | +0.0% | 4 | 19 | -8.2% |
| 1970 | $89,919 | +6.7% | $4,799 | $91,174 | $14,868 | 20 | +0.0% | 4 | 21 | +3.6% |
| 1971 | $91,174 | +31.6% | $11,999 | $107,990 | $26,866 | 24 | +0.0% | 4 | 30 | +14.7% |
| 1972 | $107,990 | +19.7% | $9,691 | $119,526 | $36,558 | 25 | +4.5% | 4 | 10 | +19.7% |
| 1973 | $119,526 | -22.8% | $4,612 | $87,631 | $41,170 | 26 | +0.0% | 4 | 29 | -14.4% |
| 1974 | $87,631 | -24.9% | $3,290 | $62,515 | $44,460 | 29 | +0.0% | 3 | 29 | -27.2% |
| 1975 | $62,515 | +35.4% | $8,463 | $76,164 | $52,923 | 32 | +0.0% | 3 | 33 | +36.2% |
| 1976 | $76,164 | +30.5% | $9,940 | $89,460 | $62,863 | 34 | +0.0% | 5 | 43 | +23.4% |
| 1977 | $89,460 | -6.9% | $4,165 | $79,142 | $67,028 | 36 | +0.0% | 4 | 38 | -8.4% |
| 1978 | $79,142 | +0.9% | $3,992 | $75,850 | $71,020 | 39 | +0.0% | 3 | 41 | +4.6% |
| 1979 | $75,850 | +11.2% | $6,328 | $78,046 | $77,348 | 40 | +0.0% | 3 | 43 | +16.3% |
| 1980 | $78,046 | +38.0% | $10,769 | $96,924 | $88,118 | 40 | +0.9% | 4 | 13 | +30.3% |
| 1981 | $96,924 | -1.2% | $4,786 | $90,926 | $92,903 | 43 | +1.6% | 4 | 8 | -6.5% |
| 1982 (to Aug) | $90,926 | -6.0% | $0 | $85,504 | $92,903 | 44 | +1.1% | 3 | 4 | -0.8% |

Final value $85,504, withdrawn $92,903, 427 trades, 21 closed positions (win rate +100.0%, average closed return +86.5%, median hold 48.0 months), 44 still open.

Sell reasons: withdrawal × 297, trim +50% × 44, replaced × 21

Open positions at the end: 44, of which 26 below cost (unrealised loss $-33,694). Largest: KMI (-9%, since 1973-01), WMT (-8%, since 1981-04), BR (-16%, since 1976-10), WAT (-30%, since 1972-04), HQY (-4%, since 1980-10), SLGN (+27%, since 1976-10), ICE (+109%, since 1979-10), WELL (-21%, since 1972-04), WM (+30%, since 1977-01), CNH (+14%, since 1968-01), AXP (+14%, since 1982-07), ETN (-26%, since 1981-07), ALV (+22%, since 1969-01), HPQ (-21%, since 1968-01), CRBG (-25%, since 1968-01)

Worst open: GME (-98%, since 1968-01), GPC (-83%, since 1968-04), HWC (-76%, since 1968-01), TPL (-73%, since 1976-04), DVA (-69%, since 1968-01), MEDP (-67%, since 1968-01), PHM (-61%, since 1974-07), CSGP (-38%, since 1970-10), WING (-37%, since 1980-01), AMH (-37%, since 1981-01)

Best closed: BKNG $10,735 (+107%), KR $8,581 (+84%), UBER $7,706 (+77%), LIN $7,215 (+86%), GLW $5,980 (+84%)
Worst closed: EXP $442 (+69%), PHM $502 (+82%), UNM $522 (+82%), DOCN $594 (+82%), THO $639 (+77%)

## no_trim — No trim: hold until RSI(m) 90 exit or replaced

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +6.4% | $5,319 | $101,053 | $5,319 | 13 | +0.0% | 13 | 13 | +11.9% |
| 1969 | $101,053 | -7.0% | $4,700 | $89,293 | $10,018 | 16 | +0.0% | 3 | 16 | -8.2% |
| 1970 | $89,293 | +4.2% | $4,653 | $88,411 | $14,671 | 19 | +0.0% | 4 | 20 | +3.6% |
| 1971 | $88,411 | +23.1% | $10,880 | $97,920 | $25,551 | 22 | +0.0% | 3 | 22 | +14.7% |
| 1972 | $97,920 | +29.9% | $12,720 | $114,476 | $38,271 | 24 | +0.0% | 5 | 27 | +19.7% |
| 1973 | $114,476 | -22.1% | $4,456 | $84,672 | $42,727 | 26 | +0.0% | 4 | 28 | -14.4% |
| 1974 | $84,672 | -32.4% | $2,864 | $54,413 | $45,591 | 29 | +0.0% | 3 | 29 | -27.2% |
| 1975 | $54,413 | +35.8% | $7,388 | $66,495 | $52,980 | 32 | +0.0% | 3 | 32 | +36.2% |
| 1976 | $66,495 | +32.8% | $8,833 | $79,498 | $61,813 | 32 | +0.0% | 3 | 35 | +23.4% |
| 1977 | $79,498 | -4.3% | $3,803 | $72,252 | $65,616 | 35 | +0.0% | 5 | 37 | -8.4% |
| 1978 | $72,252 | -1.7% | $3,550 | $67,457 | $69,166 | 38 | +0.0% | 3 | 38 | +4.6% |
| 1979 | $67,457 | +7.9% | $3,640 | $69,169 | $72,806 | 39 | +0.0% | 3 | 41 | +16.3% |
| 1980 | $69,169 | +36.5% | $9,443 | $84,990 | $82,250 | 39 | +0.0% | 3 | 42 | +30.3% |
| 1981 | $84,990 | -7.7% | $3,922 | $74,526 | $86,172 | 42 | +0.0% | 4 | 43 | -6.5% |
| 1982 (to Aug) | $74,526 | +3.2% | $0 | $76,934 | $86,172 | 43 | +0.0% | 4 | 3 | -0.8% |

Final value $76,934, withdrawn $86,172, 489 trades, 20 closed positions (win rate +100.0%, average closed return +114.9%, median hold 51.0 months), 43 still open.

Sell reasons: withdrawal × 406, replaced × 20

Open positions at the end: 43, of which 26 below cost (unrealised loss $-23,502). Largest: WM (+30%, since 1977-01), UBER (-6%, since 1982-04), SLGN (+43%, since 1979-10), XOM (+126%, since 1977-01), CNH (+14%, since 1968-01), NEE (-3%, since 1982-04), WAT (-30%, since 1972-04), HPQ (-21%, since 1968-01), CRBG (-25%, since 1968-01), HQY (-4%, since 1980-10), AXP (+14%, since 1982-07), ASB (-36%, since 1968-01), NI (+52%, since 1979-07), CL (+4%, since 1977-07), MEDP (-67%, since 1968-01)

Worst open: GME (-98%, since 1968-01), GPC (-83%, since 1968-04), HWC (-76%, since 1968-01), TPL (-73%, since 1976-04), DVA (-69%, since 1968-01), MEDP (-67%, since 1968-01), PHM (-61%, since 1974-07), CSGP (-38%, since 1970-10), AMH (-37%, since 1981-01), ASB (-36%, since 1968-01)

Best closed: BKNG $13,919 (+139%), ALV $12,151 (+116%), UBER $7,785 (+78%), ALLY $3,419 (+136%), PNC $1,829 (+117%)
Worst closed: EXP $533 (+95%), PHM $593 (+102%), UNM $616 (+112%), PCTY $656 (+104%), EEFT $691 (+101%)

## rotate — Rotate: hold exactly the current top 10 each quarter

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +4.7% | $5,233 | $99,426 | $5,233 | 10 | +0.0% | 27 | 27 | +11.9% |
| 1969 | $99,426 | +22.0% | $12,132 | $109,187 | $17,365 | 10 | +0.0% | 27 | 37 | -8.2% |
| 1970 | $109,187 | +15.6% | $9,462 | $116,701 | $26,827 | 10 | +0.0% | 25 | 35 | +3.6% |
| 1971 | $116,701 | +23.0% | $14,358 | $129,224 | $41,185 | 10 | +0.0% | 25 | 35 | +14.7% |
| 1972 | $129,224 | +46.0% | $18,862 | $169,760 | $60,047 | 10 | +0.0% | 22 | 32 | +19.7% |
| 1973 | $169,760 | -7.4% | $7,863 | $149,404 | $67,911 | 10 | +4.2% | 27 | 27 | -14.4% |
| 1974 | $149,404 | -40.1% | $4,474 | $85,001 | $72,385 | 10 | +8.4% | 23 | 23 | -27.2% |
| 1975 | $85,001 | +43.7% | $12,216 | $109,946 | $84,601 | 10 | +0.0% | 21 | 31 | +36.2% |
| 1976 | $109,946 | +29.1% | $14,195 | $127,756 | $98,796 | 10 | +0.0% | 25 | 35 | +23.4% |
| 1977 | $127,756 | -3.6% | $6,158 | $117,008 | $104,954 | 10 | +0.0% | 26 | 36 | -8.4% |
| 1978 | $117,008 | -0.8% | $5,801 | $110,228 | $110,756 | 10 | +2.6% | 22 | 22 | +4.6% |
| 1979 | $110,228 | +30.0% | $14,327 | $128,941 | $125,082 | 10 | +0.0% | 26 | 36 | +16.3% |
| 1980 | $128,941 | +56.3% | $20,155 | $181,399 | $145,238 | 10 | +0.0% | 23 | 33 | +30.3% |
| 1981 | $181,399 | +11.6% | $15,184 | $187,273 | $160,422 | 10 | +0.0% | 27 | 37 | -6.5% |
| 1982 (to Aug) | $187,273 | +16.5% | $0 | $218,251 | $160,422 | 10 | +5.6% | 21 | 21 | -0.8% |

Final value $218,251, withdrawn $160,422, 834 trades, 357 closed positions (win rate +59.1%, average closed return +6.3%, median hold 3.0 months), 10 still open.

Sell reasons: left list × 357, withdrawal × 110

Open positions at the end: 10, of which 5 below cost (unrealised loss $-5,633). Largest: PCTY (+40%, since 1982-07), DKS (+15%, since 1982-07), AXP (+14%, since 1982-07), FCN (+8%, since 1982-07), AME (+8%, since 1982-04), TPL (-2%, since 1982-07), WING (-4%, since 1982-07), LULU (-6%, since 1982-07), UBER (-6%, since 1982-04), INVH (-12%, since 1981-04)

Worst open: INVH (-12%, since 1981-04), UBER (-6%, since 1982-04), LULU (-6%, since 1982-07), WING (-4%, since 1982-07), TPL (-2%, since 1982-07)

Best closed: THO $11,581 (+104%), HQY $11,043 (+64%), AXP $10,830 (+66%), META $10,214 (+70%), TPR $10,185 (+60%)
Worst closed: FTNT $-12,274 (-67%), GME $-9,839 (-54%), WELL $-9,642 (-53%), KMI $-7,969 (-47%), AFG $-7,508 (-51%)

## base_no_wd — Base without withdrawals

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +6.7% | $0 | $106,728 | $0 | 13 | +8.1% | 13 | 1 | +11.9% |
| 1969 | $106,728 | -7.5% | $0 | $98,743 | $0 | 17 | +1.6% | 4 | 2 | -8.2% |
| 1970 | $98,743 | +6.2% | $0 | $104,885 | $0 | 20 | +0.8% | 4 | 1 | +3.6% |
| 1971 | $104,885 | +32.6% | $0 | $139,126 | $0 | 25 | +4.2% | 5 | 7 | +14.7% |
| 1972 | $139,126 | +22.9% | $0 | $171,058 | $0 | 27 | +10.7% | 5 | 11 | +19.7% |
| 1973 | $171,058 | -23.3% | $0 | $131,176 | $0 | 28 | +0.9% | 5 | 4 | -14.4% |
| 1974 | $131,176 | -26.4% | $0 | $96,524 | $0 | 32 | +0.9% | 4 | 0 | -27.2% |
| 1975 | $96,524 | +38.6% | $0 | $133,797 | $0 | 36 | +0.9% | 4 | 2 | +36.2% |
| 1976 | $133,797 | +29.6% | $0 | $173,363 | $0 | 38 | +0.8% | 6 | 9 | +23.4% |
| 1977 | $173,363 | -6.2% | $0 | $162,652 | $0 | 41 | +0.9% | 4 | 1 | -8.4% |
| 1978 | $162,652 | +4.3% | $0 | $169,647 | $0 | 45 | +0.9% | 4 | 2 | +4.6% |
| 1979 | $169,647 | +11.8% | $0 | $189,675 | $0 | 47 | +0.9% | 4 | 4 | +16.3% |
| 1980 | $189,675 | +36.2% | $0 | $258,278 | $0 | 47 | +11.6% | 4 | 13 | +30.3% |
| 1981 | $258,278 | -2.1% | $0 | $252,956 | $0 | 51 | +4.9% | 5 | 8 | -6.5% |
| 1982 (to Aug) | $252,956 | -5.5% | $0 | $238,986 | $0 | 52 | +1.3% | 3 | 4 | -0.8% |

Final value $238,986, withdrawn $0, 143 trades, 22 closed positions (win rate +100.0%, average closed return +98.3%, median hold 46.5 months), 52 still open.

Sell reasons: trim +50% × 47, replaced × 22

Open positions at the end: 52, of which 29 below cost (unrealised loss $-77,934). Largest: AMH (-37%, since 1981-01), KMI (-9%, since 1973-01), ICE (+109%, since 1979-10), BR (-16%, since 1976-10), WMT (-8%, since 1981-04), ALV (+22%, since 1969-01), HQY (-4%, since 1980-10), WAT (-30%, since 1972-04), NKE (+5%, since 1981-01), FFIV (-32%, since 1982-01), SLGN (+27%, since 1976-10), WM (+30%, since 1977-01), ETN (-26%, since 1981-07), WELL (-21%, since 1972-04), AXP (+14%, since 1982-07)

Worst open: GME (-98%, since 1968-01), GPC (-83%, since 1968-04), HWC (-76%, since 1968-01), TPL (-73%, since 1976-04), DVA (-69%, since 1968-01), MEDP (-67%, since 1968-01), MTB (-63%, since 1975-07), PHM (-61%, since 1974-07), CSGP (-38%, since 1970-10), WING (-37%, since 1980-01)

Best closed: BKNG $11,747 (+117%), ALLY $11,402 (+143%), UBER $11,008 (+110%), KR $10,984 (+92%), LIN $8,221 (+98%)
Worst closed: PHM $587 (+87%), THO $670 (+77%), UGI $857 (+100%), G $858 (+98%), PRU $875 (+103%)

## rsi80 — Base with the monthly-RSI exit at 80 instead of 90

| Year | Start | Return | Withdrawal | End (after) | Cum. withdrawn | Positions | Cash % | Buys | Sells | Index return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1968 | $100,000 | +6.7% | $5,336 | $101,392 | $5,336 | 13 | +3.3% | 13 | 1 | +11.9% |
| 1969 | $101,392 | -6.7% | $4,733 | $89,919 | $10,069 | 17 | +0.0% | 4 | 19 | -8.2% |
| 1970 | $89,919 | +6.7% | $4,799 | $91,174 | $14,868 | 20 | +0.0% | 4 | 21 | +3.6% |
| 1971 | $91,174 | +31.6% | $11,999 | $107,990 | $26,866 | 24 | +0.0% | 4 | 30 | +14.7% |
| 1972 | $107,990 | +19.7% | $9,691 | $119,526 | $36,558 | 25 | +4.5% | 4 | 10 | +19.7% |
| 1973 | $119,526 | -22.8% | $4,612 | $87,631 | $41,170 | 26 | +0.0% | 4 | 29 | -14.4% |
| 1974 | $87,631 | -24.9% | $3,290 | $62,515 | $44,460 | 29 | +0.0% | 3 | 29 | -27.2% |
| 1975 | $62,515 | +35.4% | $8,463 | $76,164 | $52,923 | 32 | +0.0% | 3 | 33 | +36.2% |
| 1976 | $76,164 | +30.5% | $9,940 | $89,460 | $62,863 | 34 | +0.0% | 5 | 43 | +23.4% |
| 1977 | $89,460 | -6.9% | $4,165 | $79,142 | $67,028 | 36 | +0.0% | 4 | 38 | -8.4% |
| 1978 | $79,142 | +0.4% | $3,975 | $75,526 | $71,003 | 37 | +0.0% | 3 | 41 | +4.6% |
| 1979 | $75,526 | +9.4% | $4,131 | $78,484 | $75,134 | 39 | +0.0% | 3 | 41 | +16.3% |
| 1980 | $78,484 | +37.9% | $10,826 | $97,434 | $85,960 | 39 | +0.0% | 4 | 52 | +30.3% |
| 1981 | $97,434 | -1.1% | $4,817 | $91,528 | $90,777 | 41 | +1.6% | 4 | 8 | -6.5% |
| 1982 (to Aug) | $91,528 | -6.9% | $0 | $85,238 | $90,777 | 42 | +1.1% | 3 | 4 | -0.8% |

Final value $85,238, withdrawn $90,777, 464 trades, 23 closed positions (win rate +100.0%, average closed return +79.1%, median hold 51.0 months), 42 still open.

Sell reasons: withdrawal × 333, trim +50% × 43, replaced × 20, RSI(m) 83 × 1, RSI(m) 84 × 1, RSI(m) 82 × 1

Open positions at the end: 42, of which 26 below cost (unrealised loss $-34,223). Largest: WMT (-8%, since 1981-04), KMI (-9%, since 1973-01), BR (-16%, since 1976-10), WAT (-30%, since 1972-04), HQY (-4%, since 1980-10), SLGN (+27%, since 1976-10), WELL (-21%, since 1972-04), WM (+30%, since 1977-01), IT (+49%, since 1978-10), CNH (+14%, since 1968-01), ETN (-26%, since 1981-07), AXP (+14%, since 1982-07), ALV (+22%, since 1969-01), HPQ (-21%, since 1968-01), CRBG (-25%, since 1968-01)

Worst open: GME (-98%, since 1968-01), GPC (-83%, since 1968-04), HWC (-76%, since 1968-01), TPL (-73%, since 1976-04), DVA (-69%, since 1968-01), MEDP (-67%, since 1968-01), PHM (-61%, since 1974-07), CSGP (-38%, since 1970-10), WING (-37%, since 1980-01), AMH (-37%, since 1981-01)

Best closed: BKNG $10,735 (+107%), KR $8,581 (+84%), UBER $7,706 (+77%), LIN $7,215 (+86%), GLW $5,977 (+84%)
Worst closed: FTNT $138 (+15%), FLEX $218 (+29%), EXP $447 (+70%), PHM $502 (+82%), UNM $522 (+82%)

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
| 1968-01-01 | 226 | 210 | HWC, CRBG, MEDP, UBER, BKNG, DVA, GME, CNH, HPQ, ASB |
| 1968-04-01 | 308 | 292 | UBER, GPC, CSCO, CRWD, PCTY, ATO, G, BKNG, AVY, HWC |
| 1968-07-01 | 295 | 282 | G, BKNG, IT, REG, CRBG, ATO, UBER, CMCSA, CLX, CRWD |
| 1968-10-01 | 205 | 191 | UGI, MRSH, BKNG, GPC, CRBG, FLEX, WMB, IT, G, UBER |
| 1969-01-01 | 207 | 196 | G, ALV, RGLD, CRWD, TPL, BBY, WST, PEN, CRBG, UBER |
| 1969-04-01 | 222 | 210 | LIN, ALV, G, AM, TPR, RGLD, PEN, IBOC, WST, CRBG |
| 1969-07-01 | 274 | 261 | VTRS, NTRS, LEA, INGR, GPC, ST, TLN, MMM, APTV, DVA |
| 1969-10-01 | 367 | 354 | THO, LHX, APTV, ELF, LYV, DVA, TLN, PNC, OGS, MMM |
| 1970-01-01 | 418 | 405 | PNC, DVA, ZBRA, G, SN, MAS, TLN, APTV, AXP, LHX |
| 1970-04-01 | 456 | 443 | FLEX, PEN, CYTK, FRT, INTC, EXP, PHM, PEP, LECO, APTV |
| 1970-07-01 | 654 | 631 | PHM, NEM, AAON, CRBG, TLN, LECO, EXP, UDR, CSGP, DOV |
| 1970-10-01 | 649 | 620 | PHM, CSGP, HGV, AAON, TLN, GME, HPQ, LECO, UAL, DOV |
| 1971-01-01 | 490 | 468 | PRU, AMCR, GME, PHM, HGV, ATO, CSGP, UAL, NTRS, AEE |
| 1971-04-01 | 332 | 315 | KR, HGV, ED, AMCR, PHM, TPR, PEN, ATO, APO, MTB |
| 1971-07-01 | 187 | 172 | PEN, O, MRK, CVS, WEC, ATI, KR, MTB, ED, FTNT |
| 1971-10-01 | 218 | 203 | O, TPR, SFM, PHM, PAYX, CHD, RGLD, GAP, DVA, PEN |
| 1972-01-01 | 267 | 251 | SFM, DVA, AMCR, TPR, KMI, GAP, O, BR, PHM, ARE |
| 1972-04-01 | 254 | 239 | PHM, ALV, WAT, PEN, WELL, GAP, SFM, KMI, AMCR, TPR |
| 1972-07-01 | 179 | 169 | AMGN, META, HWC, LULU, INGR, WELL, MDT, WTS, KDP, PNR |
| 1972-10-01 | 189 | 177 | ALLY, AFG, DGX, AMGN, LULU, FTNT, HWC, META, INGR, WAT |
| 1973-01-01 | 183 | 173 | PEN, KMI, C, AMGN, NXT, SMG, NEE, AFG, FRT, DGX |
| 1973-04-01 | 196 | 187 | CSGP, FTNT, AMGN, BA, STAG, MAT, PEN, KMI, NEE, LULU |
| 1973-07-01 | 310 | 291 | AME, AVY, TPR, NWSA, HWC, FLEX, CSGP, AXP, STAG, DPZ |
| 1973-10-01 | 349 | 330 | HWC, STAG, TPR, DOCN, CLX, AME, WELL, MRK, GME, FTNT |
| 1974-01-01 | 439 | 424 | FTNT, WELL, HGV, KR, CLX, MCO, AME, GME, TNL, META |
| 1974-04-01 | 518 | 494 | HGV, LH, AFG, WELL, UDR, FTNT, CBRE, KEY, SYF, PEN |
| 1974-07-01 | 595 | 567 | PHM, FTNT, NTRS, SCHW, AFG, WM, LULU, SFM, WELL, CBRE |
| 1974-10-01 | 812 | 769 | PHM, FTNT, NRG, SYF, NTRS, ATI, UDR, WELL, PCTY, CBRE |
| 1975-01-01 | 818 | 765 | NRG, PCTY, ATI, UDR, EXP, INVH, SYF, CBRE, PHM, EEFT |
| 1975-04-01 | 700 | 650 | EXP, FTNT, MTB, PHM, INVH, NRG, PCTY, SYF, CRWD, KMI |
| 1975-07-01 | 452 | 422 | PCTY, MTB, TEL, WELL, UNM, UDR, MMM, FTNT, AFG, NRG |
| 1975-10-01 | 328 | 301 | CSGP, DOCN, EXP, HAS, MSI, INVH, TEL, DKS, PCTY, NTRS |
| 1976-01-01 | 312 | 291 | CSGP, TTC, ZBRA, MSI, IVZ, DVA, FTNT, UPS, INVH, DKS |
| 1976-04-01 | 235 | 218 | TPL, GLW, TTC, KBR, CSGP, PHM, INVH, FTNT, ATO, OGS |
| 1976-07-01 | 174 | 159 | EEFT, MTB, DPZ, SFM, BR, MSI, GM, CLX, TPL, PG |
| 1976-10-01 | 187 | 169 | BR, SLGN, EXP, PHM, SFM, EEFT, ARMK, CLX, MSI, PG |
| 1977-01-01 | 194 | 178 | EXP, WM, XOM, BR, ECL, DOCN, SFM, UAL, EEFT, CLX |
| 1977-04-01 | 252 | 234 | INVH, WM, BR, APG, EXP, COLM, DPZ, NTRS, RCL, PHM |
| 1977-07-01 | 293 | 276 | CL, BMY, AAON, RS, DPZ, AMCR, RCL, NTRS, INVH, KBR |
| 1977-10-01 | 331 | 313 | JBL, IBM, AMCR, GPC, WST, AHR, KMI, UBER, LSTR, AAON |
| 1978-01-01 | 388 | 368 | DVA, CG, MMM, DASH, CSGP, IBM, FTNT, ED, AMCR, JBL |
| 1978-04-01 | 484 | 455 | FTNT, EXP, UNM, IBM, DVA, CRBG, HL, NTRS, FCN, CSGP |
| 1978-07-01 | 462 | 439 | IBM, FCN, AMCR, LULU, CSGP, NTRS, FTNT, EXP, TPL, DVA |
| 1978-10-01 | 275 | 256 | IT, TPL, CMC, LULU, IBM, TTD, PHM, WAT, FCN, ZBH |
| 1979-01-01 | 308 | 285 | EQIX, DVA, IT, GM, AFG, ICE, TPL, SWKS, HL, MKSI |
| 1979-04-01 | 327 | 305 | EQIX, OGS, CRWD, CVS, GEHC, ICE, AFG, GAP, IT, DVA |
| 1979-07-01 | 268 | 246 | NI, ICE, THO, GD, OGS, AYI, NEM, TPL, EQIX, CPRT |
| 1979-10-01 | 246 | 228 | SLGN, ICE, NNN, UBER, AAON, ZBRA, TPL, PG, OGS, EQIX |
| 1980-01-01 | 236 | 218 | TPL, WING, UBER, LULU, MKSI, LHX, SCHW, SLGN, NTRS, ICE |
| 1980-04-01 | 272 | 252 | WELL, JBL, UBER, DLR, COLM, NEM, TPL, HGV, WAT, NTRS |
| 1980-07-01 | 244 | 220 | JBL, TPL, NEM, WELL, GEHC, COLM, CG, FLR, DIS, GS |
| 1980-10-01 | 203 | 184 | NEM, HQY, TPL, GEHC, CEG, WAT, JBL, WELL, DVA, LH |
| 1981-01-01 | 100 | 85 | AMH, NKE, BALL, PG, SNPS, MSA, SMTC, WELL, APTV, NEM |
| 1981-04-01 | 100 | 86 | WMT, GPC, KNSL, F, SNPS, LULU, MSA, NEM, INVH, NVR |
| 1981-07-01 | 145 | 131 | GPC, WMT, ETN, DVA, CLX, WPC, F, MSA, INVH, NVR |
| 1981-10-01 | 256 | 238 | TPR, INVH, WMB, WAT, DVA, WM, PHM, CMC, MTB, FCN |
| 1982-01-01 | 284 | 263 | TPL, IBM, JBL, FFIV, INVH, WM, TLN, MTB, WAT, DVA |
| 1982-04-01 | 392 | 363 | UBER, NEE, INVH, MKSI, DLB, SMG, MSI, AME, NBIX, DLR |
| 1982-07-01 | 446 | 411 | AXP, PCTY, LULU, TPL, INVH, UBER, AME, WING, FCN, DKS |