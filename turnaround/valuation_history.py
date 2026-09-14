"""Historical valuation multiples for a ticker.

Two sources, combined per metric:

1. Yahoo "fundamentals-timeseries" snapshots: quarterly P/E, forward P/E,
   PEG, EV/EBITDA, P/S (last ~5 quarters) plus sparse "trailing" snapshots
   (~8 points over ~3 years). This is what Yahoo's Statistics page shows.
2. Reconstruction from reported annual figures: for every month-end close in
   the price cache, trailing P/E = price / diluted EPS of the latest fiscal
   year reported at least `lag_days` before that date, and EV/EBITDA =
   (price x shares + total debt - cash) / EBITDA on the same basis. Yahoo
   serves 4-5 fiscal years, so this gives 4-5 years of monthly history.
   Forward P/E and PEG cannot be reconstructed (they need historical analyst
   estimates), so they only have source 1.

Cached in cache/valuation/<TICKER>.json for 7 days.
"""
from __future__ import annotations

import json
import math
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import indicators as ind  # noqa: E402
import prices  # noqa: E402

from paths import cache_dirs, find, is_fresh  # noqa: E402

READ_CACHE, CACHE = cache_dirs("valuation")

SNAPSHOT_TYPES = {
    "pe": ["quarterlyPeRatio", "trailingPeRatio"],
    "fwd_pe": ["quarterlyForwardPeRatio", "trailingForwardPeRatio"],
    "peg": ["quarterlyPegRatio", "trailingPegRatio"],
    "ev_ebitda": ["quarterlyEnterprisesValueEBITDARatio", "trailingEnterprisesValueEBITDARatio"],
    "ps": ["quarterlyPsRatio", "trailingPsRatio"],
}
ANNUAL_TYPES = {
    "eps": ["annualDilutedEPS", "annualBasicEPS"],
    "ebitda": ["annualEBITDA", "annualNormalizedEBITDA"],
    "debt": ["annualTotalDebt"],
    "cash": ["annualCashCashEquivalentsAndShortTermInvestments", "annualCashAndCashEquivalents"],
    "shares": ["annualOrdinarySharesNumber", "annualShareIssued"],
    "revenue": ["annualTotalRevenue"],
}
LABELS = {"pe": "P/E (trailing)", "fwd_pe": "P/E (forward)", "peg": "PEG", "ev_ebitda": "EV/EBITDA", "ps": "P/S"}


def _fetch_timeseries(ticker: str) -> dict:
    import yfinance as yf

    t = yf.Ticker(ticker)
    types = [x for v in SNAPSHOT_TYPES.values() for x in v] + [x for v in ANNUAL_TYPES.values() for x in v]
    url = f"https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{ticker}"
    params = {"type": ",".join(types), "period1": int(time.time()) - 15 * 365 * 86400,
              "period2": int(time.time()), "merge": "false", "padTimeSeries": "false"}
    r = t._data.get(url=url, params=params, timeout=30)
    r.raise_for_status()
    out: dict[str, list] = {}
    for item in r.json().get("timeseries", {}).get("result", []):
        typ = item["meta"]["type"][0]
        vals = [(v["asOfDate"], v["reportedValue"]["raw"]) for v in item.get(typ, [])
                if v and v.get("reportedValue") and v["reportedValue"].get("raw") is not None]
        if vals:
            out[typ] = vals
    return out


def _series(ts: dict, names: list[str]) -> list[tuple[str, float]]:
    """Merge the listed timeseries types into one date-sorted, de-duplicated list."""
    merged: dict[str, float] = {}
    for n in names:
        for d, v in ts.get(n, []):
            merged.setdefault(d, float(v))
    return sorted(merged.items())


def _first(ts: dict, names: list[str]) -> list[tuple[str, float]]:
    for n in names:
        if ts.get(n):
            return [(d, float(v)) for d, v in ts[n]]
    return []


def reconstruct(ticker: str, ts: dict, lag_days: int = 75) -> dict[str, list]:
    """Monthly trailing P/E, EV/EBITDA and P/S from annual figures and month-end closes."""
    daily = prices.load(ticker)
    if daily is None:
        return {}
    m = ind.monthly_bars(daily, drop_partial=False)
    annual = {k: _first(ts, v) for k, v in ANNUAL_TYPES.items()}
    if not annual["eps"]:
        return {}

    def latest(series, date):
        """Value of the latest fiscal year reported (period end + lag) on/before `date`."""
        best = None
        for d, v in series:
            if datetime.strptime(d, "%Y-%m-%d") + timedelta(days=lag_days) <= date:
                best = v
        return best

    pe, ev_ebitda, ps = [], [], []
    for dt, close in m["Close"].items():
        d = dt.to_pydatetime()
        eps = latest(annual["eps"], d)
        if eps is not None and eps > 0:
            pe.append((dt.date().isoformat(), close / eps))
        sh = latest(annual["shares"], d)
        if sh:
            mcap = close * sh
            ebitda = latest(annual["ebitda"], d)
            debt = latest(annual["debt"], d) or 0.0
            cash = latest(annual["cash"], d) or 0.0
            if ebitda and ebitda > 0:
                ev_ebitda.append((dt.date().isoformat(), (mcap + debt - cash) / ebitda))
            rev = latest(annual["revenue"], d)
            if rev and rev > 0:
                ps.append((dt.date().isoformat(), mcap / rev))
    return {"pe": pe, "ev_ebitda": ev_ebitda, "ps": ps}


def stats(values: list[float], current: float | None) -> dict:
    v = np.array([x for x in values if x is not None and not math.isnan(x)], dtype=float)
    if len(v) == 0:
        return {"n": 0}
    out = {"n": int(len(v)), "avg": float(v.mean()), "median": float(np.median(v)),
           "high": float(v.max()), "low": float(v.min())}
    if current is not None and not math.isnan(current):
        out["current"] = current
        out["percentile"] = float((v < current).mean())
        out["vs_avg"] = current / out["avg"] - 1.0 if out["avg"] else math.nan
    return out


def build(ticker: str) -> dict:
    ts = _fetch_timeseries(ticker)
    snaps = {k: _series(ts, v) for k, v in SNAPSHOT_TYPES.items()}
    recon = reconstruct(ticker, ts)
    metrics = {}
    for k in SNAPSHOT_TYPES:
        s = snaps.get(k, [])
        r = recon.get(k, [])
        # current = most recent snapshot (Yahoo's own figure), else last reconstructed point
        current = s[-1][1] if s else (r[-1][1] if r else None)
        hist_vals = [v for _, v in r] if r else [v for _, v in s]
        st = stats(hist_vals, current)
        st["source"] = "reconstructed monthly from annual reports" if r else "Yahoo snapshots"
        span = r if r else s
        st["from"] = span[0][0] if span else None
        st["to"] = span[-1][0] if span else None
        metrics[k] = {"label": LABELS[k], "stats": st, "snapshots": s, "monthly": r}
    return {"ticker": ticker, "fetched": time.strftime("%Y-%m-%d"), "metrics": metrics,
            "annual": {k: _first(ts, v) for k, v in ANNUAL_TYPES.items()}}


def get(ticker: str, max_age_days: float = 7.0, refresh: bool = False) -> dict:
    fname = f"{ticker.upper()}.json"
    existing = find("valuation", fname)
    if existing and not refresh and is_fresh("valuation", existing, max_age_days):
        return json.loads(existing.read_text(encoding="utf-8"))
    p = CACHE / fname
    try:
        data = build(ticker.upper())
    except Exception as e:  # noqa: BLE001
        data = {"ticker": ticker, "error": str(e)[:200], "metrics": {}}
    p.write_text(json.dumps(data, indent=1), encoding="utf-8")
    return data


if __name__ == "__main__":
    for tk in [a for a in sys.argv[1:] if not a.startswith("--")] or ["NKE"]:
        d = get(tk, refresh="--refresh" in sys.argv)
        print(tk, d.get("error", ""))
        for k, mtr in d["metrics"].items():
            s = mtr["stats"]
            print(f"  {mtr['label']:16s} n={s.get('n', 0):3d} cur={s.get('current', float('nan')):7.2f} "
                  f"avg={s.get('avg', float('nan')):7.2f} med={s.get('median', float('nan')):7.2f} "
                  f"high={s.get('high', float('nan')):7.2f} low={s.get('low', float('nan')):7.2f} "
                  f"pct={s.get('percentile', float('nan')):5.2f}  [{s.get('source')} {s.get('from')}..{s.get('to')}]")
