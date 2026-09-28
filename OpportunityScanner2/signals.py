"""Signal definitions for the "overbought all-time high, then RSI collapse" scanner.

The idea (from the user): a stock goes very overbought on the monthly chart while
it is making all-time highs, then its monthly RSI falls by more than about 32%
from that peak reading. The collapse in momentum after a blow-off top often
marks a good area to buy a quality company.

Definitions (monthly bars built from daily Yahoo data, Wilder RSI(14) on the
monthly close, the same RSI as the turnaround scanner and TradingView):

  arming month  a completed month whose high is a new all-time high (or within
                `ath_tol` of it) and whose RSI is >= `ob`, with at least
                `min_years` of price history behind it. The ATH is the
                highest monthly high so far.
  peak RSI      the highest RSI among the arming months of the last `window`
                months (older overbought readings expire), counting only arming
                months after the previous signal.
  signal month  the first month whose RSI is at or below
                peak_rsi * (1 - drop)        (mode "rel", the default)
                peak_rsi - drop_pts          (mode "pts")
                (plus the optional `min_dd` / `max_rsi` conditions). The signal
                disarms the scanner: the next signal needs a new arming month.
  entry         the study buys at the signal month's closing price: the monthly
                candle is almost final on the last trading day.

Alternative events used as baselines, same arming logic where noted:
  "pullback"    first month whose close is `dd` below the ATH after an arming
                month (price-only version of the same idea)
  "rsi35"       first month with RSI < 35 after at least 12 months >= 35
                (the older turnaround scanner's trigger)
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "turnaround"))
import indicators as ind  # noqa: E402


@dataclass(frozen=True)
class Params:
    ob: float = 70.0          # peak RSI must reach this on an ATH month
    drop: float = 0.32        # relative RSI drop from the peak (mode "rel")
    drop_pts: float = 25.0    # absolute RSI drop from the peak (mode "pts")
    mode: str = "rel"
    window: int = 24          # months the peak stays valid
    ath_tol: float = 0.0      # arming month high within this fraction of the ATH
    min_years: float = 5.0    # price history needed at the arming month
    min_dd: float = 0.0       # also require the close this far below the ATH (0 = off)
    max_rsi: float = 0.0      # also require RSI below this absolute level (0 = off)

    def label(self) -> str:
        d = f"{self.drop * 100:.0f}%" if self.mode == "rel" else f"{self.drop_pts:.0f}pt"
        return (f"ob{self.ob:.0f}_drop{d}_w{self.window}" + (f"_tol{self.ath_tol * 100:.0f}" if self.ath_tol else "")
                + (f"_dd{self.min_dd * 100:.0f}" if self.min_dd else "") + (f"_rsi<{self.max_rsi:.0f}" if self.max_rsi else ""))

    def fires(self, r: float, level: float, close: float, ath: float) -> bool:
        return (r <= level and (not self.min_dd or close / ath - 1.0 <= -self.min_dd)
                and (not self.max_rsi or r < self.max_rsi))

    def as_dict(self) -> dict:
        return asdict(self)


DEFAULT = Params()


def monthly(daily: pd.DataFrame, last_month: pd.Timestamp | None = None) -> pd.DataFrame:
    """Completed monthly bars with RSI, running all-time high and history length.
    `last_month` (a month-end) cuts the series so the last row is a completed month."""
    m = ind.monthly_bars(daily, drop_partial=False)
    if last_month is not None:
        m = m.loc[:last_month]
    m = m.copy()
    m["rsi"] = ind.wilder_rsi(m["Close"], 14).to_numpy()
    m["ath_prev"] = m["High"].cummax().shift(1)          # highest high before this month
    m["ath"] = m["High"].cummax()
    m["years"] = (m.index - daily.index[0]).days / 365.25
    return m


def _scan(m: pd.DataFrame, p: Params):
    """Walk the monthly frame; yields (i, peak, fired) for every month with an RSI, where `peak` is
    (rsi, i_peak, i_last_arm) of the live overbought peak or None and `fired` says the signal fired."""
    rsi = m["rsi"].to_numpy(); high = m["High"].to_numpy(); close = m["Close"].to_numpy()
    ath_prev = m["ath_prev"].to_numpy(); ath = m["ath"].to_numpy(); years = m["years"].to_numpy()
    arms: list[tuple[int, float]] = []       # arming months since the last signal
    for i in range(len(m)):
        r = rsi[i]
        if np.isnan(r):
            continue
        is_ath = not np.isnan(ath_prev[i]) and high[i] >= ath_prev[i] * (1.0 - p.ath_tol)
        if is_ath and r >= p.ob and years[i] >= p.min_years:
            arms.append((i, r))
            yield i, None, False
            continue
        arms = [a for a in arms if i - a[0] <= p.window]
        if not arms:
            yield i, None, False
            continue
        j, pk = max(arms, key=lambda a: a[1])
        peak = (pk, j, arms[-1][0])
        level = pk * (1.0 - p.drop) if p.mode == "rel" else pk - p.drop_pts
        if p.fires(r, level, close[i], ath[i]):
            arms = []
            yield i, peak, True
        else:
            yield i, peak, False


def detect(m: pd.DataFrame, p: Params = DEFAULT) -> list[dict]:
    """RSI-collapse events for one ticker's monthly frame (from `monthly`)."""
    rsi = m["rsi"].to_numpy(); close = m["Close"].to_numpy(); ath = m["ath"].to_numpy()
    idx = m.index
    out = []
    for i, peak, fired in _scan(m, p):
        if not fired:
            continue
        pk, j, last_arm = peak
        level = pk * (1.0 - p.drop) if p.mode == "rel" else pk - p.drop_pts
        out.append({
            "signal_month": idx[i], "peak_month": idx[j], "last_ath_month": idx[last_arm],
            "peak_rsi": float(pk), "rsi": float(rsi[i]), "trigger_level": float(level),
            "rsi_chg": float(rsi[i] / pk - 1.0),
            "months_from_peak": int(i - j), "months_from_ath": int(i - last_arm),
            "close": float(close[i]), "ath": float(ath[i]), "dd_ath": float(close[i] / ath[i] - 1.0),
        })
    return out


def detect_pullback(m: pd.DataFrame, dd: float = 0.25, p: Params = DEFAULT) -> list[dict]:
    """Price-only twin: after an arming month (ATH with RSI >= ob), the first month-end close
    `dd` or more below the all-time high."""
    rsi = m["rsi"].to_numpy(); high = m["High"].to_numpy(); close = m["Close"].to_numpy()
    ath_prev = m["ath_prev"].to_numpy(); ath = m["ath"].to_numpy(); years = m["years"].to_numpy()
    out, armed_at = [], None
    for i in range(len(m)):
        r = rsi[i]
        if np.isnan(r):
            continue
        if not np.isnan(ath_prev[i]) and high[i] >= ath_prev[i] and r >= p.ob and years[i] >= p.min_years:
            armed_at = i
            continue
        if armed_at is None or i - armed_at > p.window:
            armed_at = None
            continue
        if close[i] / ath[i] - 1.0 <= -dd:
            out.append({"signal_month": m.index[i], "peak_month": m.index[armed_at], "rsi": float(r),
                        "close": float(close[i]), "ath": float(ath[i]), "dd_ath": float(close[i] / ath[i] - 1.0),
                        "months_from_ath": int(i - armed_at)})
            armed_at = None
    return out


def detect_rsi35(m: pd.DataFrame, level: float = 35.0, min_years: float = 5.0) -> list[dict]:
    """First month with RSI below `level` after at least 12 months at or above it."""
    rsi = m["rsi"].to_numpy(); close = m["Close"].to_numpy(); ath = m["ath"].to_numpy(); years = m["years"].to_numpy()
    out, above = [], 0
    for i in range(len(m)):
        r = rsi[i]
        if np.isnan(r):
            continue
        if r < level:
            if above >= 12 and years[i] >= min_years:
                out.append({"signal_month": m.index[i], "rsi": float(r), "close": float(close[i]),
                            "ath": float(ath[i]), "dd_ath": float(close[i] / ath[i] - 1.0)})
            above = 0
        else:
            above += 1
    return out
