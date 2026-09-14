"""Download daily OHLC history + dividends from Yahoo Finance into data/*.json.

Usage:  python fetch_data.py            # refreshes the default universe
        python fetch_data.py COST LLY   # adds/refreshes specific tickers
"""
import json, sys, urllib.request

DEFAULT = ["NFLX", "MSFT", "ENPH", "NVDA", "CVX", "SPY",
           "XOM", "NVO", "INTC", "QCOM", "AMKR", "AEHR", "BABA"]

def fetch(ticker):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           "?range=15y&interval=1d&events=div,splits")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    raw = urllib.request.urlopen(req, timeout=30).read()
    data = json.loads(raw)
    result = data["chart"]["result"][0]
    n = len(result["timestamp"])
    with open(f"data/{ticker.lower()}.json", "wb") as f:
        f.write(raw)
    print(f"{ticker}: {n} rows")

if __name__ == "__main__":
    tickers = [t.upper() for t in sys.argv[1:]] or DEFAULT
    for t in tickers:
        fetch(t)
