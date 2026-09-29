"""Shared data for the RSI-collapse study: full-history prices, the universe, monthly
adjusted closes, point-in-time fundamentals and forward-return helpers.

Prices come from the turnaround backtest's full-history cache
(`../turnaround_backtest/cache/prices/`, Yahoo, refreshed by `python
../turnaround_backtest/data.py prices`). Fundamentals are the backtest-v3
monthly tables (SEC EDGAR, point in time: each month-end only sees filings
public by then), cached here as a pickle because they take ~2 minutes to build.
"""
from __future__ import annotations

import json
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "turnaround_backtest_v3"))
sys.path.insert(0, str(ROOT / "turnaround_backtest"))
sys.path.insert(0, str(ROOT / "turnaround"))
import data as bt_data  # noqa: E402  (turnaround_backtest/data.py)
import screen_v3  # noqa: E402

CACHE = HERE / "cache"
CACHE.mkdir(exist_ok=True)
OUT = HERE / "output"
OUT.mkdir(exist_ok=True)
EDGAR_DIR = ROOT / "turnaround" / "cache" / "edgar"

# last completed monthly candle used by the study (prices run to late September 2026)
LAST_MONTH = pd.Timestamp("2026-08-31")


def universe() -> pd.DataFrame:
    return bt_data.universe_meta()


def load_daily(t: str) -> pd.DataFrame | None:
    return bt_data.load_prices(t)


def load_all_daily(tickers: list[str]) -> dict[str, pd.DataFrame]:
    out = {}
    for t in tickers:
        d = load_daily(t)
        if d is not None and len(d) > 300:
            out[t] = d
    return out


def monthly_adj(daily: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Month-end total-return (adjusted) closes, months x tickers."""
    cols = {t: d["AdjClose"].resample("ME").last() for t, d in daily.items()}
    return pd.DataFrame(cols).sort_index()


def fundamentals_tables(tickers: list[str], rebuild: bool = False) -> dict[str, pd.DataFrame]:
    p = CACHE / "fund_tables.pkl"
    if p.exists() and not rebuild:
        return pickle.loads(p.read_bytes())
    print("building point-in-time fundamentals tables (~2 min) ...", file=sys.stderr, flush=True)
    tables = screen_v3.build_tables(tickers)
    keep = ["eps_ttm", "ni_ttm", "rev_ttm", "rev_yoy", "prior_yoy", "prof_past", "rev_qoq", "rev_jump8",
            "opinc_ttm", "ni_op", "ni_jump4", "op_jump4", "eps_jump4", "shares_yoy", "debt", "cash",
            "ebitda_ttm", "mcap", "pe", "ps", "ev_ebitda", "ev_ebit", "val_pct", "val_pct_op", "q_end", "adv",
            "gw_ev", "gw_ratio"]
    slim = {t: tb[[c for c in keep if c in tb.columns]].copy() for t, tb in tables.items()}
    for tb in slim.values():
        tb["eps_yoy"] = np.where(tb["eps_ttm"].shift(12) > 0, tb["eps_ttm"] / tb["eps_ttm"].shift(12) - 1.0, np.nan)
    p.write_bytes(pickle.dumps(slim))
    return slim


def load_edgar(t: str) -> list[dict]:
    p = EDGAR_DIR / f"{t}.json"
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8")).get("quarters", [])


def realized_growth(quarters: list[dict], q_end: str | None, key: str = "rev_ttm", years: int = 1) -> float:
    """Hindsight: growth of a trailing-twelve-month figure from the quarter `q_end` to the quarter
    ending about `years` later, both as first published. NaN if either is missing."""
    if not q_end or not quarters:
        return np.nan
    first = {}
    for r in sorted(quarters, key=lambda r: (r.get("available") or "9999", r["end"])):
        if r.get(key) is not None and r["end"] not in first:
            first[r["end"]] = r[key]
    if q_end not in first or not first[q_end] or first[q_end] <= 0:
        return np.nan
    target = pd.Timestamp(q_end) + pd.DateOffset(years=years)
    best, gap = None, 46
    for e, v in first.items():
        g = abs((pd.Timestamp(e) - target).days)
        if g < gap:
            best, gap = v, g
    if best is None:
        return np.nan
    return best / first[q_end] - 1.0


def forward_stats(daily: pd.DataFrame, month: pd.Timestamp, horizons=(3, 6, 12, 24, 36),
                  last_month: pd.Timestamp = LAST_MONTH) -> dict:
    """Returns from the signal month's last close (adjusted, dividends included) to the month-end
    close `h` months later, plus the worst drawdown and the bottom in the following 12/24 months."""
    adj = daily["AdjClose"]
    f = daily["AdjClose"] / daily["Close"]
    low_adj = daily["Low"] * f
    upto = adj.loc[:month]
    if upto.empty:
        return {}
    entry = float(upto.iloc[-1])
    out = {"entry_adj": entry}
    for h in horizons:
        end = (month + pd.offsets.MonthEnd(h)).normalize()
        if end > last_month:
            out[f"r{h}"] = np.nan
            continue
        px = adj.loc[:end]
        out[f"r{h}"] = float(px.iloc[-1]) / entry - 1.0
    for h in (12, 24):
        end = (month + pd.offsets.MonthEnd(h)).normalize()
        win = low_adj.loc[month + pd.Timedelta(days=1): min(end, last_month + pd.offsets.MonthEnd(1))]
        closes = adj.loc[month + pd.Timedelta(days=1): min(end, last_month + pd.offsets.MonthEnd(1))]
        complete = end <= last_month
        if len(win) and complete:
            out[f"mae{h}"] = float(win.min()) / entry - 1.0
            # month offset of the lowest close after entry
            out[f"bottom_m{h}"] = int(round((closes.idxmin() - month).days / 30.44))
        else:
            out[f"mae{h}"] = np.nan
            out[f"bottom_m{h}"] = np.nan
    return out
