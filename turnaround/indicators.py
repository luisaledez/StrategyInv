"""Price-based indicators for the turnaround screen.

All functions are pure pandas/numpy and take *daily* OHLCV frames with a
DatetimeIndex and columns: Open, High, Low, Close, AdjClose, Volume.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# --------------------------------------------------------------------------- RSI
def wilder_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    """Classic Wilder RSI: seeded with a simple average of the first `period`
    changes, then Wilder-smoothed (alpha = 1/period). Matches the textbook /
    TradingView definition rather than the un-seeded pandas ewm."""
    c = close.to_numpy(dtype=float)
    n = len(c)
    out = np.full(n, np.nan)
    if n <= period:
        return pd.Series(out, index=close.index, name="rsi")
    d = np.diff(c)
    gains = np.where(d > 0, d, 0.0)
    losses = np.where(d < 0, -d, 0.0)
    ag = gains[:period].mean()
    al = losses[:period].mean()
    out[period] = 100.0 if al == 0 else 100.0 - 100.0 / (1.0 + ag / al)
    for i in range(period, n - 1):
        ag = (ag * (period - 1) + gains[i]) / period
        al = (al * (period - 1) + losses[i]) / period
        out[i + 1] = 100.0 if al == 0 else 100.0 - 100.0 / (1.0 + ag / al)
    return pd.Series(out, index=close.index, name="rsi")


# ----------------------------------------------------------------- monthly bars
def monthly_bars(daily: pd.DataFrame, as_of: pd.Timestamp | None = None,
                 drop_partial: bool = True) -> pd.DataFrame:
    """Resample daily bars to calendar-month bars (last close of the month).

    `as_of` limits the data to bars on/before that date. With `drop_partial`
    the month containing the reference date (default: today) is removed unless
    it has fully elapsed, so the last row is always a *completed* monthly candle.
    """
    df = daily
    if as_of is not None:
        df = df.loc[: pd.Timestamp(as_of)]
    if df.empty:
        return df
    m = pd.DataFrame({
        "Open": df["Open"].resample("ME").first(),
        "High": df["High"].resample("ME").max(),
        "Low": df["Low"].resample("ME").min(),
        "Close": df["Close"].resample("ME").last(),
        "AdjClose": df["AdjClose"].resample("ME").last(),
        "Volume": df["Volume"].resample("ME").sum(),
        "Days": df["Close"].resample("ME").count(),
    }).dropna(subset=["Close"])
    if drop_partial and len(m):
        ref = pd.Timestamp(as_of) if as_of is not None else pd.Timestamp.today().normalize()
        last_period = m.index[-1].to_period("M")
        # A month is complete only once the reference date reaches its last day.
        if ref.to_period("M") <= last_period and ref < last_period.end_time.normalize():
            m = m.iloc[:-1]
    return m


# --------------------------------------------------------------------- episodes
def rsi_episodes(rsi: pd.Series, threshold: float = 35.0) -> list[dict]:
    """Group consecutive months with RSI < threshold into distress episodes.

    Returns a list of dicts: start (first oversold month), end (last oversold
    month so far), months, min_rsi, exit (first month back at/above the
    threshold, or None if the episode is still active at the end of the series).
    """
    below = (rsi < threshold) & rsi.notna()
    episodes: list[dict] = []
    cur = None
    for dt, flag in below.items():
        if flag and cur is None:
            cur = {"start": dt, "end": dt, "months": 1, "min_rsi": float(rsi[dt])}
        elif flag:
            cur["end"] = dt
            cur["months"] += 1
            cur["min_rsi"] = min(cur["min_rsi"], float(rsi[dt]))
        elif cur is not None:
            cur["exit"] = dt
            episodes.append(cur)
            cur = None
    if cur is not None:
        cur["exit"] = None
        episodes.append(cur)
    return episodes


# --------------------------------------------------------------------- helpers
def drawdown_from_high(daily_close: pd.Series, years: float = 5.0):
    """(drawdown, trailing high, date of high) using daily closes over the
    trailing `years` window ending at the last bar. Drawdown is negative."""
    end = daily_close.index[-1]
    start = end - pd.DateOffset(years=years)
    window = daily_close.loc[start:end]
    high = float(window.max())
    high_date = window.idxmax()
    last = float(daily_close.iloc[-1])
    return last / high - 1.0, high, high_date


def avg_dollar_volume(daily: pd.DataFrame, days: int = 63) -> float:
    tail = daily.tail(days)
    return float((tail["Close"] * tail["Volume"]).mean())


def max_drawdown(series: pd.Series) -> float:
    """Max peak-to-trough decline of a price series (negative number)."""
    if series.empty:
        return float("nan")
    peak = series.cummax()
    return float((series / peak - 1.0).min())
