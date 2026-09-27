"""Data for the turnaround backtest: full-history daily prices for the scan
universe (Yahoo, period=max) and point-in-time quarterly fundamentals from
SEC EDGAR through the scanner's own edgar.py.

The scanner's price cache holds 15 years and is refreshed with 15 years, so a
backtest that starts in 2004 keeps its own copy here (cache/prices/<T>.csv,
same layout as turnaround/cache/prices). EDGAR tables go into the scanner's
cache/edgar/ so the web app's ticker pages benefit from them too.

    python data.py prices      # download/refresh full-history prices (universe + SPY)
    python data.py edgar       # fetch EDGAR quarterly tables for the universe
    python data.py status
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SCANNER = HERE.parent / "turnaround"
sys.path.insert(0, str(SCANNER))
import prices as scanner_prices  # noqa: E402
import universe as uni_mod  # noqa: E402

PRICES = HERE / "cache" / "prices"
PRICES.mkdir(parents=True, exist_ok=True)
BENCHMARKS = ["SPY"]


def universe_tickers() -> list[str]:
    uni = uni_mod.load(("sp500", "sp400"))
    return list(uni["ticker"])


def universe_meta() -> pd.DataFrame:
    return uni_mod.load(("sp500", "sp400")).set_index("ticker")


def price_path(t: str) -> Path:
    return PRICES / f"{t.upper().replace('/', '-')}.csv"


def load_prices(t: str) -> pd.DataFrame | None:
    p = price_path(t)
    if not p.exists():
        return None
    df = pd.read_csv(p, index_col="Date", parse_dates=True)
    return df if len(df) else None


def download_prices(tickers: list[str], batch: int = 100, pause: float = 1.5, max_age_days: float = 3.0) -> None:
    import yfinance as yf
    need = [t for t in tickers if not price_path(t).exists()
            or time.time() - price_path(t).stat().st_mtime > max_age_days * 86400]
    print(f"prices: {len(need)} of {len(tickers)} to download (full history)", file=sys.stderr, flush=True)
    for i in range(0, len(need), batch):
        chunk = need[i:i + batch]
        print(f"  {i + 1}-{i + len(chunk)} of {len(need)}", file=sys.stderr, flush=True)
        for attempt in range(3):
            try:
                raw = yf.download(chunk, period="max", interval="1d", auto_adjust=False,
                                  group_by="ticker", threads=True, progress=False)
                break
            except Exception as e:  # noqa: BLE001
                print(f"  retry {attempt + 1}: {e}", file=sys.stderr, flush=True)
                time.sleep(10)
                raw = None
        if raw is None or raw.empty:
            continue
        for t in chunk:
            try:
                sub = raw[t] if isinstance(raw.columns, pd.MultiIndex) else raw
            except KeyError:
                continue
            df = scanner_prices._normalise(sub)
            if df is not None:
                df.to_csv(price_path(t))
        time.sleep(pause)


def fetch_edgar(tickers: list[str]) -> None:
    import edgar
    done = 0
    for i, t in enumerate(tickers, 1):
        d = edgar.get(t)
        n = len(d.get("quarters", []))
        done += n > 0
        if i % 25 == 0 or i == len(tickers):
            print(f"  edgar {i}/{len(tickers)}: {done} with data", file=sys.stderr, flush=True)
    print(f"edgar: {done} of {len(tickers)} tickers have quarterly data", file=sys.stderr, flush=True)


def status() -> None:
    tickers = universe_tickers()
    have = [t for t in tickers if price_path(t).exists()]
    starts = []
    for t in have[:2000]:
        with open(price_path(t)) as f:
            f.readline()
            starts.append(f.readline()[:4])
    from collections import Counter
    print(f"prices: {len(have)}/{len(tickers)} tickers; first-bar years {sorted(Counter(starts).items())}")
    import edgar
    n = sum(1 for t in tickers if (SCANNER / "cache" / "edgar" / f"{t}.json").exists())
    print(f"edgar: {n}/{len(tickers)} tables cached")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "prices":
        download_prices(universe_tickers() + BENCHMARKS)
    elif cmd == "edgar":
        fetch_edgar(universe_tickers())
    else:
        status()
