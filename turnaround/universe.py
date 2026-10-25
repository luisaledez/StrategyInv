"""Build the scan universe: S&P 500 + S&P 400 constituents from Wikipedia,
plus any custom tickers. Cached to turnaround/cache/universe.csv.

The "nasdaq" universe is every Nasdaq-listed common stock with a market cap of
$1B or more (Nasdaq's stock screener feed), cached separately to
turnaround/cache/universe_nasdaq.csv. Set SCAN_UNIVERSE=nasdaq to point the
scanners at it: the turnaround scan, backtest data, v3 live list and
OpportunityScanner2 live lists then read this universe and write to their
output_nasdaq/ folders, leaving the S&P outputs alone.

Usage:  python universe.py                 # rebuild sp500+sp400
        python universe.py nasdaq          # rebuild the Nasdaq universe
        python universe.py --show          # print cached universe summary
"""
from __future__ import annotations

import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache" / "universe.csv"
NASDAQ_CACHE = HERE / "cache" / "universe_nasdaq.csv"

SOURCES = {
    "sp500": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "sp400": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
    "sp600": "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies",
}
NASDAQ_SCREENER = "https://api.nasdaq.com/api/screener/stocks"
NASDAQ_MIN_MCAP = 1e9

# Universe the scanners use by default; SCAN_UNIVERSE=nasdaq switches them, and TAG is the
# suffix of their output folders ("" for the S&P default, "_nasdaq" otherwise).
NAME = os.environ.get("SCAN_UNIVERSE", "sp500,sp400").strip().lower()
TAG = "" if NAME == "sp500,sp400" else "_" + NAME.replace(",", "_")


def default_indexes() -> tuple[str, ...]:
    return tuple(NAME.split(","))

# Nasdaq screener sector -> GICS sector name used everywhere else (names also in the S&P
# lists keep their GICS sector instead).
NASDAQ_SECTOR = {
    "Technology": "Information Technology",
    "Health Care": "Health Care",
    "Finance": "Financials",
    "Consumer Discretionary": "Consumer Discretionary",
    "Industrials": "Industrials",
    "Real Estate": "Real Estate",
    "Telecommunications": "Communication Services",
    "Consumer Staples": "Consumer Staples",
    "Energy": "Energy",
    "Utilities": "Utilities",
    "Basic Materials": "Materials",
}
# not common equity: warrants, units, rights, preferred and debt listings
NASDAQ_EXCLUDE = r"\b(?:Warrants?|Units?|Rights?|Preferred|Notes?|Debentures?|Subordinated)\b"

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


def build_nasdaq() -> pd.DataFrame:
    """Nasdaq-listed common stocks with market cap >= NASDAQ_MIN_MCAP."""
    print("universe: fetching Nasdaq-listed stocks ...", file=sys.stderr)
    q = urllib.parse.urlencode({"tableonly": "true", "limit": "10000", "exchange": "nasdaq", "download": "true"})
    req = urllib.request.Request(f"{NASDAQ_SCREENER}?{q}", headers={"User-Agent": "Mozilla/5.0",
                                                                    "Accept": "application/json"})
    rows = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))["data"]["rows"]
    t = pd.DataFrame(rows)
    t["mcap"] = pd.to_numeric(t["marketCap"], errors="coerce")
    t = t[(t["mcap"] >= NASDAQ_MIN_MCAP) & (t["industry"] != "Blank Checks")
          & ~t["name"].str.contains(NASDAQ_EXCLUDE, case=False, regex=True)]
    df = pd.DataFrame({
        "ticker": t["symbol"].map(yahoo_symbol),
        "name": t["name"].str.replace(r"\s+(?:Class [A-Z] )?(?:Common|Ordinary) (?:Stock|Shares?).*$", "",
                                      regex=True).str.strip(),
        "sector": t["sector"].map(NASDAQ_SECTOR).fillna(""),
        "industry": t["industry"].astype(str),
        "index": "nasdaq",
    })
    if CACHE.exists():  # GICS sector and name from the S&P lists where the stock is in one
        sp = pd.read_csv(CACHE).drop_duplicates("ticker").set_index("ticker")
        inn = df["ticker"].isin(sp.index)
        for c in ("name", "sector", "industry"):
            df.loc[inn, c] = df.loc[inn, "ticker"].map(sp[c]).fillna(df.loc[inn, c])
    df = df.drop_duplicates("ticker").sort_values("ticker").reset_index(drop=True)
    df["sector_etf"] = df["sector"].map(SECTOR_ETF).fillna("SPY")
    df.to_csv(NASDAQ_CACHE, index=False)
    print(f"universe: {len(df)} Nasdaq tickers -> {NASDAQ_CACHE}", file=sys.stderr)
    return df


def load(indexes: list[str] | None = None, custom: list[str] = (),
         rebuild: bool = False) -> pd.DataFrame:
    indexes = tuple(indexes or default_indexes())
    if indexes == ("nasdaq",):
        uni = pd.read_csv(NASDAQ_CACHE) if NASDAQ_CACHE.exists() and not rebuild else build_nasdaq()
        uni = uni.fillna({"name": "", "sector": "", "industry": ""})
        missing = [yahoo_symbol(c) for c in custom if yahoo_symbol(c) not in set(uni["ticker"])]
        if missing:
            extra = pd.DataFrame([{"ticker": m, "name": "", "sector": "", "industry": "",
                                   "index": "custom", "sector_etf": "SPY"} for m in missing])
            uni = pd.concat([uni, extra], ignore_index=True)
        return uni
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
    elif "nasdaq" in sys.argv:
        build_nasdaq()
    else:
        build()
