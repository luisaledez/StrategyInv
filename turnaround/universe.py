"""Build the scan universe: S&P 500 + S&P 400 constituents from Wikipedia,
plus any custom tickers. Cached to turnaround/cache/universe.csv.

Usage:  python universe.py                 # rebuild sp500+sp400
        python universe.py --show          # print cached universe summary
"""
from __future__ import annotations

import io
import sys
import time
import urllib.request
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache" / "universe.csv"

SOURCES = {
    "sp500": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "sp400": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
    "sp600": "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies",
}

# GICS sector -> SPDR sector ETF used as the "sector" benchmark.
SECTOR_ETF = {
    "Information Technology": "XLK",
    "Health Care": "XLV",
    "Financials": "XLF",
    "Consumer Discretionary": "XLY",
    "Communication Services": "XLC",
    "Industrials": "XLI",
    "Consumer Staples": "XLP",
    "Energy": "XLE",
    "Utilities": "XLU",
    "Real Estate": "XLRE",
    "Materials": "XLB",
}


def _fetch_table(url: str) -> pd.DataFrame:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    tables = pd.read_html(io.StringIO(html))
    for t in tables:
        cols = [str(c) for c in t.columns]
        if "Symbol" in cols and "Security" in cols:
            return t
    raise RuntimeError(f"no constituent table found at {url}")


def yahoo_symbol(sym: str) -> str:
    """Wikipedia uses BRK.B / BF.B; Yahoo wants BRK-B / BF-B."""
    return str(sym).strip().upper().replace(".", "-")


def build(indexes: list[str] = ("sp500", "sp400"), custom: list[str] = ()) -> pd.DataFrame:
    frames = []
    for name in indexes:
        url = SOURCES[name]
        print(f"universe: fetching {name} ...", file=sys.stderr)
        t = _fetch_table(url)
        df = pd.DataFrame({
            "ticker": t["Symbol"].map(yahoo_symbol),
            "name": t["Security"].astype(str),
            "sector": t["GICS Sector"].astype(str) if "GICS Sector" in t else "",
            "industry": t["GICS Sub-Industry"].astype(str) if "GICS Sub-Industry" in t else "",
            "index": name,
        })
        frames.append(df)
        time.sleep(1)
    for c in custom:
        frames.append(pd.DataFrame([{"ticker": yahoo_symbol(c), "name": "", "sector": "",
                                     "industry": "", "index": "custom"}]))
    uni = pd.concat(frames, ignore_index=True).drop_duplicates("ticker").reset_index(drop=True)
    uni["sector_etf"] = uni["sector"].map(SECTOR_ETF).fillna("SPY")
    uni.to_csv(CACHE, index=False)
    print(f"universe: {len(uni)} tickers -> {CACHE}", file=sys.stderr)
    return uni


def load(indexes: list[str] = ("sp500", "sp400"), custom: list[str] = (),
         rebuild: bool = False) -> pd.DataFrame:
    if CACHE.exists() and not rebuild:
        uni = pd.read_csv(CACHE)
        have = set(uni["index"])
        if all(i in have for i in indexes):
            uni = uni[uni["index"].isin(list(indexes) + ["custom"])]
            missing = [yahoo_symbol(c) for c in custom if yahoo_symbol(c) not in set(uni["ticker"])]
            if missing:
                extra = pd.DataFrame([{"ticker": m, "name": "", "sector": "", "industry": "",
                                       "index": "custom", "sector_etf": "SPY"} for m in missing])
                uni = pd.concat([uni, extra], ignore_index=True)
            return uni.reset_index(drop=True)
    return build(indexes, custom)


if __name__ == "__main__":
    if "--show" in sys.argv and CACHE.exists():
        u = pd.read_csv(CACHE)
        print(u.groupby(["index", "sector"]).size().to_string())
        print(len(u), "tickers")
    else:
        build()
