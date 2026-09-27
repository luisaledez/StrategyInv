"""Point-in-time quarterly screen for the turnaround backtest.

Every snapshot date (1 Jan / 1 Apr / 1 Jul / 1 Oct, 2004 .. 2026) runs the
scanner's price screen as of the previous day (so the last *completed*
monthly candle is used, exactly like `scan.py --as-of`), then applies the
selection rules with only data that was public on that day:

  1. scanner price screen: monthly Wilder RSI(14) < THRESHOLD in any of the
     last LOOKBACK completed months, >= 5 years of history, 3-month average
     dollar volume >= $5M, market cap >= $1B
  2. profitable now (trailing-twelve-month EPS and net income > 0) and
     profitable in the past (at most one losing year among the last three
     TTM readings taken one, two and three years earlier)
  3. top 20 by trailing-twelve-month revenue growth YoY (when the year-ago
     TTM reading is missing, as in the first XBRL years, the last complete
     fiscal year versus the one before is used instead)
  4. of those, top 10 by valuation versus the company's own history: the
     mean percentile of the current trailing P/E, P/S and EV/EBITDA within
     the monthly series reconstructed from filings (lower = cheaper than
     usual); needs at least MIN_VAL_MONTHS of history

Fundamentals come from SEC XBRL company facts via the scanner's edgar.py.
XBRL starts with fiscal 2007 comparatives for large filers and 2009-2011 for
smaller ones, so nothing can pass rule 2/3 before 2008: the 2004-2008
snapshots are empty by construction and are reported as such.

    python screen.py                 # writes output/snapshots.json + snapshots.csv
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SCANNER = HERE.parent / "turnaround"
sys.path.insert(0, str(SCANNER))
sys.path.insert(0, str(HERE))
import indicators as ind  # noqa: E402
import data  # noqa: E402

OUT = data.OUT
EDGAR_DIR = data.EDGAR_DIR

# scanner rules (scan.py defaults)
THRESHOLD = 42.0
RSI_PERIOD = 14
LOOKBACK = 6
MIN_YEARS = 5.0
MIN_ADV = 5e6
MIN_MCAP = 1e9
# selection rules
TOP_GROWTH = 20
TOP_VALUE = 10
MIN_VAL_MONTHS = 12

START = data.START
END = data.END


def snapshot_dates() -> list[pd.Timestamp]:
    out = []
    d = START
    while d <= END:
        out.append(d)
        d = d + pd.DateOffset(months=3)
    return out


# ------------------------------------------------------------------ per-ticker tables
def load_edgar(t: str) -> list[dict]:
    p = EDGAR_DIR / f"{t}.json"
    if not p.exists():
        return []
    d = json.loads(p.read_text(encoding="utf-8"))
    q = [r for r in d.get("quarters", []) if r.get("available")]
    q.sort(key=lambda r: (r["available"], r["end"]))
    return q


def _nearest_row(rows: list[dict], end: pd.Timestamp, years_back: int, tol_days: int = 45) -> dict | None:
    target = end - pd.DateOffset(years=years_back)
    best, best_gap = None, tol_days + 1
    for r in rows:
        gap = abs((pd.Timestamp(r["end"]) - target).days)
        if gap < best_gap:
            best, best_gap = r, gap
    return best


def ticker_table(t: str, daily: pd.DataFrame | None, quarters: list[dict]) -> pd.DataFrame | None:
    """One row per month-end with everything the screen needs at that as-of date."""
    if daily is None or len(daily) < 300:
        return None
    m = ind.monthly_bars(daily, drop_partial=False)
    if len(m) < RSI_PERIOD + 2:
        return None
    rsi = ind.wilder_rsi(m["Close"], RSI_PERIOD)
    below = (rsi < THRESHOLD) & rsi.notna()
    qualified = below.rolling(LOOKBACK, min_periods=1).max().astype(bool)
    dv = (daily["Close"] * daily["Volume"]).rolling(63, min_periods=20).mean()
    adv = dv.resample("ME").last().reindex(m.index)
    first_bar = daily.index[0]
    years = (m.index - first_bar).days / 365.25
    close = m["Close"]
    high5 = daily["Close"].rolling("1826D", min_periods=1).max().resample("ME").last().reindex(m.index)
    dd5 = close / high5 - 1.0

    tbl = pd.DataFrame({
        "close": close, "rsi": rsi, "qualified": qualified, "adv": adv,
        "years": years, "dd5": dd5,
    })

    # ---- point-in-time fundamentals: latest quarter public at each month-end
    n = len(tbl)
    eps = np.full(n, np.nan); ni = np.full(n, np.nan); rev = np.full(n, np.nan)
    ebitda = np.full(n, np.nan); debt = np.full(n, np.nan); cash = np.full(n, np.nan)
    shares = np.full(n, np.nan); rev_yoy = np.full(n, np.nan)
    prof_past = np.full(n, np.nan); q_end = [None] * n
    if quarters:
        avail = np.array([np.datetime64(r["available"]) for r in quarters])
        last_shares = np.nan
        by_avail_idx = 0
        latest = None          # quarter with the latest period end among those public so far
        seen: list[dict] = []  # every quarter public so far (for year-ago comparisons)
        for i, dt in enumerate(tbl.index):
            d64 = np.datetime64(dt.date())
            while by_avail_idx < len(quarters) and avail[by_avail_idx] <= d64:
                r = quarters[by_avail_idx]
                seen.append(r)
                if latest is None or r["end"] > latest["end"]:
                    latest = r
                if r.get("shares"):
                    last_shares = r["shares"]
                by_avail_idx += 1
            if latest is None:
                continue
            r = latest
            q_end[i] = r["end"]
            eps[i] = r["eps_ttm"] if r.get("eps_ttm") is not None else np.nan
            ni[i] = r["ni_ttm"] if r.get("ni_ttm") is not None else np.nan
            rev[i] = r["rev_ttm"] if r.get("rev_ttm") is not None else np.nan
            ebitda[i] = r["ebitda_ttm"] if r.get("ebitda_ttm") is not None else np.nan
            debt[i] = r["debt"] if r.get("debt") is not None else np.nan
            cash[i] = r["cash"] if r.get("cash") is not None else np.nan
            shares[i] = r["shares"] if r.get("shares") else last_shares
            e = pd.Timestamp(r["end"])
            cur, prev = r, _nearest_row(seen, e, 1)
            if prev is None:
                # the year-ago TTM reading does not exist (first XBRL years only report annual
                # comparatives): fall back to the latest pair of readings twelve months apart,
                # i.e. the last complete fiscal year versus the one before
                for cand in sorted(seen, key=lambda x: x["end"], reverse=True):
                    if cand["end"] >= r["end"]:
                        continue
                    p2 = _nearest_row(seen, pd.Timestamp(cand["end"]), 1)
                    if p2 is not None:
                        cur, prev = cand, p2
                        break
                e = pd.Timestamp(cur["end"])
            if prev and prev.get("rev_ttm") and cur.get("rev_ttm") is not None and prev["rev_ttm"] > 0:
                rev_yoy[i] = cur["rev_ttm"] / prev["rev_ttm"] - 1.0
            pts = []
            for k in (1, 2, 3):
                pr = _nearest_row(seen, e, k)
                if pr is None:
                    continue
                v = pr.get("ni_ttm") if pr.get("ni_ttm") is not None else pr.get("eps_ttm")
                if v is not None:
                    pts.append(v > 0)
            if pts:
                prof_past[i] = float(sum(pts) >= max(1, len(pts) - 1))
    tbl["q_end"] = q_end
    tbl["eps_ttm"] = eps; tbl["ni_ttm"] = ni; tbl["rev_ttm"] = rev; tbl["ebitda_ttm"] = ebitda
    tbl["debt"] = debt; tbl["cash"] = cash; tbl["shares"] = shares
    tbl["rev_yoy"] = rev_yoy; tbl["prof_past"] = prof_past
    tbl["mcap"] = tbl["close"] * tbl["shares"]
    with np.errstate(divide="ignore", invalid="ignore"):
        tbl["pe"] = np.where(tbl["eps_ttm"] > 0, tbl["close"] / tbl["eps_ttm"], np.nan)
        tbl["ps"] = np.where(tbl["rev_ttm"] > 0, tbl["mcap"] / tbl["rev_ttm"], np.nan)
        ev = tbl["mcap"] + tbl["debt"].fillna(0.0) - tbl["cash"].fillna(0.0)
        tbl["ev_ebitda"] = np.where(tbl["ebitda_ttm"] > 0, ev / tbl["ebitda_ttm"], np.nan)
    for k in ("pe", "ps", "ev_ebitda"):
        tbl[f"{k}_pct"] = _expanding_percentile(tbl[k].to_numpy())
    tbl["val_pct"] = tbl[["pe_pct", "ps_pct", "ev_ebitda_pct"]].mean(axis=1, skipna=True)
    return tbl


def _expanding_percentile(v: np.ndarray, min_points: int = MIN_VAL_MONTHS) -> np.ndarray:
    """For each month, the share of earlier valid readings (and this one) that are below the
    current reading; NaN until `min_points` readings exist."""
    out = np.full(len(v), np.nan)
    hist: list[float] = []
    for i, x in enumerate(v):
        if np.isnan(x):
            continue
        hist.append(x)
        if len(hist) >= min_points:
            a = np.asarray(hist)
            out[i] = float((a < x).mean())
    return out


# ------------------------------------------------------------------ the screen
def build_tables(tickers: list[str], verbose: bool = True) -> dict[str, pd.DataFrame]:
    tables = {}
    for i, t in enumerate(tickers, 1):
        if verbose and i % 100 == 0:
            print(f"  tables {i}/{len(tickers)}", file=sys.stderr, flush=True)
        tbl = ticker_table(t, data.load_prices(t), load_edgar(t))
        if tbl is not None:
            tables[t] = tbl
    return tables


def _f(x):
    return None if x is None or (isinstance(x, float) and math.isnan(x)) else float(x)


def screen_at(tables: dict[str, pd.DataFrame], meta: pd.DataFrame, snap: pd.Timestamp) -> dict:
    as_of = snap - pd.Timedelta(days=1)
    month_end = as_of.to_period("M").to_timestamp(how="end").normalize()
    rows = []
    for t, tbl in tables.items():
        if month_end not in tbl.index:
            continue
        r = tbl.loc[month_end]
        if not bool(r["qualified"]):
            continue
        rows.append({
            "ticker": t, "name": meta["name"].get(t, ""), "sector": meta["sector"].get(t, ""),
            "rsi_m": round(float(r["rsi"]), 1), "close": round(float(r["close"]), 4),
            "dd5": round(float(r["dd5"]), 4), "adv": _f(r["adv"]),
            "years": round(float(r["years"]), 1),
            "mcap": _f(r["mcap"]),
            "q_end": r["q_end"],
            "eps_ttm": _f(r["eps_ttm"]), "ni_ttm": _f(r["ni_ttm"]), "rev_ttm": _f(r["rev_ttm"]),
            "rev_yoy": _f(r["rev_yoy"]), "prof_past": _f(r["prof_past"]),
            "pe": _f(r["pe"]), "ps": _f(r["ps"]), "ev_ebitda": _f(r["ev_ebitda"]),
            "pe_pct": _f(r["pe_pct"]), "ps_pct": _f(r["ps_pct"]), "ev_ebitda_pct": _f(r["ev_ebitda_pct"]),
            "val_pct": _f(r["val_pct"]),
        })
    qualified = rows
    liquid = [r for r in qualified if r["adv"] is not None and r["adv"] >= MIN_ADV and r["years"] >= MIN_YEARS]
    big = [r for r in liquid if r["mcap"] is not None and r["mcap"] >= MIN_MCAP]
    profitable = [r for r in big if r["eps_ttm"] is not None and r["eps_ttm"] > 0
                  and (r["ni_ttm"] is None or r["ni_ttm"] > 0) and r["prof_past"] == 1.0]
    eligible = [r for r in profitable if r["rev_yoy"] is not None]
    top20 = sorted(eligible, key=lambda r: -r["rev_yoy"])[:TOP_GROWTH]
    valued = [r for r in top20 if r["val_pct"] is not None]
    top10 = sorted(valued, key=lambda r: (r["val_pct"], -r["rev_yoy"]))[:TOP_VALUE]
    for i, r in enumerate(top20, 1):
        r["growth_rank"] = i
    for i, r in enumerate(top10, 1):
        r["value_rank"] = i
    return {
        "date": snap.date().isoformat(), "as_of": as_of.date().isoformat(),
        "month_end": month_end.date().isoformat(),
        "n_universe": len(tables), "n_qualified": len(qualified), "n_liquid": len(liquid),
        "n_mcap": len(big), "n_profitable": len(profitable), "n_eligible": len(eligible),
        "top20": top20, "top10": top10,
    }


def run(verbose: bool = True) -> list[dict]:
    meta = data.universe_meta()
    tickers = list(meta.index)
    print(f"screen: building monthly tables for {len(tickers)} tickers", file=sys.stderr, flush=True)
    tables = build_tables(tickers, verbose)
    snaps = []
    for snap in snapshot_dates():
        s = screen_at(tables, meta, snap)
        snaps.append(s)
        if verbose:
            print(f"  {s['date']}: qualified {s['n_qualified']:3d} liquid {s['n_liquid']:3d} "
                  f"mcap {s['n_mcap']:3d} profitable {s['n_profitable']:3d} eligible {s['n_eligible']:3d} "
                  f"-> top10 {', '.join(r['ticker'] for r in s['top10']) or '-'}", file=sys.stderr, flush=True)
    (OUT / "snapshots.json").write_text(json.dumps(snaps, indent=1), encoding="utf-8")
    flat = []
    for s in snaps:
        for r in s["top20"]:
            flat.append({"date": s["date"], **r, "in_top10": "value_rank" in r})
    pd.DataFrame(flat).to_csv(OUT / "snapshots.csv", index=False)
    print(f"wrote {OUT / 'snapshots.json'} ({len(snaps)} snapshots)", file=sys.stderr)
    return snaps


if __name__ == "__main__":
    run()
