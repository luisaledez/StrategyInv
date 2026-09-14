"""Daily price cache backed by Yahoo Finance (via yfinance).

Each ticker is stored as turnaround/cache/prices/<TICKER>.csv with columns
Date, Open, High, Low, Close, AdjClose, Volume. Close is split-adjusted;
AdjClose is split- and dividend-adjusted (used for total-return maths).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache" / "prices"
CACHE.mkdir(parents=True, exist_ok=True)

COLS = ["Open", "High", "Low", "Close", "AdjClose", "Volume"]


def _path(ticker: str) -> Path:
    return CACHE / f"{ticker.upper().replace('/', '-')}.csv"


def _is_fresh(p: Path, max_age_days: float) -> bool:
    return p.exists() and (time.time() - p.stat().st_mtime) < max_age_days * 86400


def _normalise(df: pd.DataFrame) -> pd.DataFrame | None:
    """Turn one ticker's yfinance frame into the canonical layout."""
    if df is None or df.empty:
        return None
    df = df.rename(columns={"Adj Close": "AdjClose"})
    if "AdjClose" not in df.columns:
        df["AdjClose"] = df["Close"]
    df = df[COLS].dropna(subset=["Close"])
    idx = pd.to_datetime(df.index)
    if idx.tz is not None:
        idx = idx.tz_localize(None)
    df.index = idx.normalize()
    df.index.name = "Date"
    return df if len(df) else None


def download(tickers: list[str], period: str = "15y", batch: int = 100,
             pause: float = 1.0, verbose: bool = True) -> dict[str, pd.DataFrame]:
    import yfinance as yf

    out: dict[str, pd.DataFrame] = {}
    for i in range(0, len(tickers), batch):
        chunk = tickers[i:i + batch]
        if verbose:
            print(f"  downloading {i + 1}-{i + len(chunk)} of {len(tickers)} ...", file=sys.stderr)
        raw = yf.download(chunk, period=period, interval="1d", auto_adjust=False,
                          group_by="ticker", threads=True, progress=False)
        if raw is None or raw.empty:
            continue
        for t in chunk:
            try:
                sub = raw[t] if isinstance(raw.columns, pd.MultiIndex) else raw
            except KeyError:
                continue
            df = _normalise(sub)
            if df is not None:
                df.to_csv(_path(t))
                out[t] = df
        time.sleep(pause)
    return out


def load(ticker: str) -> pd.DataFrame | None:
    p = _path(ticker)
    if not p.exists():
        return None
    df = pd.read_csv(p, index_col="Date", parse_dates=True)
    return df if len(df) else None


def load_many(tickers: list[str], max_age_days: float = 1.0, refresh: bool = False,
              verbose: bool = True) -> dict[str, pd.DataFrame]:
    """Load cached prices, downloading anything missing or stale."""
    tickers = [t.upper() for t in tickers]
    need = [t for t in tickers if refresh or not _is_fresh(_path(t), max_age_days)]
    if need:
        if verbose:
            print(f"prices: refreshing {len(need)} of {len(tickers)} tickers", file=sys.stderr)
        download(need, verbose=verbose)
    out = {}
    for t in tickers:
        df = load(t)
        if df is not None:
            out[t] = df
    return out


if __name__ == "__main__":
    ts = [a.upper() for a in sys.argv[1:]] or ["SPY"]
    d = load_many(ts, refresh=True)
    for t, df in d.items():
        print(t, len(df), df.index[0].date(), "->", df.index[-1].date())
