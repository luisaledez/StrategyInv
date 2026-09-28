"""Full-history daily price cache (Yahoo Finance via yfinance, period=max).

Stored as rsi_swing/cache/<TICKER>.csv with columns
Date, Open, High, Low, Close, AdjClose, Volume.
Close is split-adjusted; AdjClose is split- and dividend-adjusted.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import pandas as pd

CACHE = Path(__file__).resolve().parent / "cache"
COLS = ["Open", "High", "Low", "Close", "AdjClose", "Volume"]


def _path(ticker: str) -> Path:
    return CACHE / f"{ticker.upper().replace('/', '-')}.csv"


def download(ticker: str) -> pd.DataFrame | None:
    import yfinance as yf

    raw = yf.download(ticker, period="max", interval="1d", auto_adjust=False, progress=False)
    if raw is None or raw.empty:
        return None
    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)
    df = raw.rename(columns={"Adj Close": "AdjClose"})
    if "AdjClose" not in df.columns:
        df["AdjClose"] = df["Close"]
    df = df[COLS].dropna(subset=["Close"])
    idx = pd.to_datetime(df.index)
    if idx.tz is not None:
        idx = idx.tz_localize(None)
    df.index = idx.normalize()
    df.index.name = "Date"
    CACHE.mkdir(exist_ok=True)
    df.to_csv(_path(ticker))
    return df


def load_daily(ticker: str, max_age_days: float = 1.0, refresh: bool = False) -> pd.DataFrame | None:
    p = _path(ticker)
    fresh = p.exists() and (time.time() - p.stat().st_mtime) < max_age_days * 86400
    if refresh or not fresh:
        print(f"prices: downloading {ticker} (max history)", file=sys.stderr)
        df = download(ticker)
        if df is not None:
            return df
    if not p.exists():
        return None
    return pd.read_csv(p, index_col="Date", parse_dates=True)


if __name__ == "__main__":
    for t in sys.argv[1:] or ["QCOM"]:
        df = load_daily(t, refresh=True)
        print(t, len(df), df.index[0].date(), "->", df.index[-1].date())
