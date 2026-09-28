"""Third turnaround backtest: entry-data guards on top of the organic screen.

Same snapshots, rules and data as `../turnaround_backtest/screen.py --organic`
(monthly RSI(14) < 42 in the last 6 months, liquidity, size, profitability,
organic growth, top 20 by trailing revenue growth, top 10 by valuation versus
own history), plus two guards that the organic filter does not provide, both
computed only from figures public on the snapshot date:

  one-off EPS guard ("oneoff")
    trailing net income is compared with trailing operating income: a company
    whose TTM net income exceeds its TTM operating income booked a
    non-operating gain or a tax benefit (FIS's Worldpay gain, Duolingo's
    deferred-tax release) and its trailing P/E is not a valuation; likewise
    when a single quarter lifted TTM net income by more than 50% while TTM
    operating income rose less than 25%. Without operating income in the
    filings, the same 50% test is applied to TTM EPS alone.

  acquisition guard ("acq")
    growth that arrives through a deal that closed during the year shows up as
    a share-count jump (stock-financed: Amcor/Berry) or as a step change in
    growth (cash-financed: FIS/Issuer Solutions, Dick's/Foot Locker): diluted
    shares up more than 15% year over year, or trailing revenue growth of 15%
    or more that is at least three times, and at least ten points above, the
    growth rate reported one year earlier (when that earlier rate was not
    negative, so a cyclical recovery from a decline is not an acquisition).

  operating-multiple valuation ("opval", a variant of the ranking)
    the valuation percentile drops the trailing P/E and uses P/S, EV/EBITDA
    and EV/EBIT instead, so one-off gains cannot make a name look cheap.

Variants written to output/snapshots_<variant>.json:
    ref        organic screen only (identical to output_v2/snapshots.json)
    oneoff     + one-off EPS guard
    acq        + acquisition guard
    both       + both guards
    both_opval + both guards, valuation on operating multiples

    python screen_v3.py          # ~2 min, writes every variant + current_<variant>.json (today's list)
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
BT = HERE.parent / "turnaround_backtest"
sys.path.insert(0, str(BT))
import data  # noqa: E402
import screen  # noqa: E402

OUT = HERE / "output"
VARIANTS = ("ref", "oneoff", "acq", "both", "both_opval")

# guard thresholds
ONEOFF_NI_OVER_OPINC = 1.0      # TTM net income above TTM operating income -> non-operating gain / tax benefit
ONEOFF_NI_JUMP = 1.5            # one quarter lifted TTM net income by > 50% ...
ONEOFF_OP_JUMP_OK = 1.25        # ... while TTM operating income rose < 25%
ACQ_SHARES_YOY = 0.15           # diluted shares up > 15% y/y
ACQ_MIN_GROWTH = 0.15           # step change: growth >= 15% ...
ACQ_STEP_MULT = 3.0             # ... at least 3x the growth reported a year earlier ...
ACQ_STEP_PP = 0.10              # ... and at least 10 points above it


# ------------------------------------------------------------------ point-in-time chains
def _first_published(quarters: list[dict], key: str) -> tuple[dict, list[str]]:
    by_end = {}
    for r in quarters:
        if r.get(key) is not None and r["end"] not in by_end:
            by_end[r["end"]] = (r["available"], r[key])
    return by_end, sorted(by_end)


def _chain(by_end: dict, ends: list[str], qe: str, asof: str, n: int) -> list[float]:
    """Latest reading first, then the previous first-published readings that were public at `asof`,
    stopping at a gap in the quarterly sequence; at most n+1 values."""
    if qe not in by_end:
        return []
    chain = [by_end[qe][1]]
    j = ends.index(qe)
    while j > 0 and len(chain) < n + 1:
        j -= 1
        a, v = by_end[ends[j]]
        if a > asof:
            continue
        gap = (pd.Timestamp(ends[j + 1]) - pd.Timestamp(ends[j])).days
        if not 60 <= gap <= 120:
            break
        chain.append(v)
    return chain


def _max_jump(chain: list[float]) -> float:
    ratios = [chain[k] / chain[k + 1] for k in range(len(chain) - 1) if chain[k + 1] and chain[k + 1] > 0 and chain[k] is not None]
    return max(ratios) if ratios else np.nan


def extend_table(tbl: pd.DataFrame, quarters: list[dict]) -> pd.DataFrame:
    """Add the guard diagnostics to a screen.ticker_table() frame."""
    n = len(tbl)
    ni_jump = np.full(n, np.nan); op_jump = np.full(n, np.nan); eps_jump = np.full(n, np.nan)
    opinc = np.full(n, np.nan)
    if quarters:
        ni_by, ni_ends = _first_published(quarters, "ni_ttm")
        op_by, op_ends = _first_published(quarters, "opinc_ttm")
        eps_by, eps_ends = _first_published(quarters, "eps_ttm")
        # latest operating income public at each month-end (same quarter the screen uses)
        latest_op = {}
        for r in quarters:
            if r.get("opinc_ttm") is not None:
                latest_op.setdefault(r["end"], r["opinc_ttm"])
        for i, qe in enumerate(tbl["q_end"]):
            if qe is None:
                continue
            asof = tbl.index[i].date().isoformat()
            ni_jump[i] = _max_jump(_chain(ni_by, ni_ends, qe, asof, 4))
            op_jump[i] = _max_jump(_chain(op_by, op_ends, qe, asof, 4))
            eps_jump[i] = _max_jump(_chain(eps_by, eps_ends, qe, asof, 4))
            if qe in latest_op:
                opinc[i] = latest_op[qe]
    tbl = tbl.copy()
    tbl["opinc_ttm"] = opinc
    tbl["ni_jump4"] = ni_jump; tbl["op_jump4"] = op_jump; tbl["eps_jump4"] = eps_jump
    with np.errstate(divide="ignore", invalid="ignore"):
        tbl["ni_op"] = np.where(tbl["opinc_ttm"] > 0, tbl["ni_ttm"] / tbl["opinc_ttm"], np.nan)
        tbl["shares_yoy"] = tbl["shares"] / tbl["shares"].shift(12) - 1.0
        tbl["debt_yoy"] = tbl["debt"] / tbl["debt"].shift(12) - 1.0
        ev = tbl["mcap"] + tbl["debt"].fillna(0.0) - tbl["cash"].fillna(0.0)
        tbl["ev_ebit"] = np.where(tbl["opinc_ttm"] > 0, ev / tbl["opinc_ttm"], np.nan)
    tbl["prior_yoy"] = tbl["rev_yoy"].shift(12)
    tbl["ev_ebit_pct"] = screen._expanding_percentile(tbl["ev_ebit"].to_numpy())
    tbl["val_pct_op"] = tbl[["ps_pct", "ev_ebitda_pct", "ev_ebit_pct"]].mean(axis=1, skipna=True)
    return tbl


def build_tables(tickers: list[str], verbose: bool = True) -> dict[str, pd.DataFrame]:
    tables = {}
    for i, t in enumerate(tickers, 1):
        if verbose and i % 100 == 0:
            print(f"  tables {i}/{len(tickers)}", file=sys.stderr, flush=True)
        q = screen.load_edgar(t)
        tbl = screen.ticker_table(t, data.load_prices(t), q)
        if tbl is not None:
            tables[t] = extend_table(tbl, q)
    return tables


# ------------------------------------------------------------------ guards
def _f(x):
    return None if x is None or (isinstance(x, float) and math.isnan(x)) else float(x)


def oneoff_flag(r: dict) -> str | None:
    """Reason the trailing earnings look one-off, or None."""
    if r["ni_op"] is not None and r["ni_op"] > ONEOFF_NI_OVER_OPINC:
        return f"net income {r['ni_op']:.2f}x operating income"
    if r["ni_jump4"] is not None and r["ni_jump4"] > ONEOFF_NI_JUMP:
        if r["op_jump4"] is None or r["op_jump4"] < ONEOFF_OP_JUMP_OK:
            return f"TTM net income jumped {r['ni_jump4']:.2f}x in one quarter"
    if r["ni_op"] is None and r["eps_jump4"] is not None and r["eps_jump4"] > ONEOFF_NI_JUMP:
        return f"TTM EPS jumped {r['eps_jump4']:.2f}x in one quarter (no operating income reported)"
    return None


def acq_flag(r: dict) -> str | None:
    """Reason the growth looks acquired, or None."""
    if r["shares_yoy"] is not None and r["shares_yoy"] > ACQ_SHARES_YOY:
        return f"shares +{r['shares_yoy'] * 100:.0f}% y/y"
    g, p = r["rev_yoy"], r["prior_yoy"]
    if g is not None and p is not None and p >= 0 and g >= ACQ_MIN_GROWTH and g >= ACQ_STEP_MULT * p and g - p >= ACQ_STEP_PP:
        return f"growth {g * 100:.0f}% vs {p * 100:.0f}% a year earlier"
    return None


def screen_at(tables: dict[str, pd.DataFrame], meta: pd.DataFrame, snap: pd.Timestamp, variant: str) -> dict:
    as_of = snap - pd.Timedelta(days=1)
    month_end = as_of.to_period("M").to_timestamp(how="end").normalize()
    rows = []
    for t, tbl in tables.items():
        if month_end not in tbl.index:
            continue
        r = tbl.loc[month_end]
        if not bool(r["qualified"]):
            continue
        d = {
            "ticker": t, "name": meta["name"].get(t, ""), "sector": meta["sector"].get(t, ""),
            "rsi_m": round(float(r["rsi"]), 1), "close": round(float(r["close"]), 4),
            "dd5": round(float(r["dd5"]), 4), "adv": _f(r["adv"]), "years": round(float(r["years"]), 1),
            "mcap": _f(r["mcap"]), "q_end": r["q_end"],
            "eps_ttm": _f(r["eps_ttm"]), "ni_ttm": _f(r["ni_ttm"]), "rev_ttm": _f(r["rev_ttm"]),
            "opinc_ttm": _f(r["opinc_ttm"]),
            "rev_yoy": _f(r["rev_yoy"]), "prof_past": _f(r["prof_past"]),
            "rev_qoq": _f(r["rev_qoq"]), "rev_jump8": _f(r["rev_jump8"]),
            "pe": _f(r["pe"]), "ps": _f(r["ps"]), "ev_ebitda": _f(r["ev_ebitda"]), "ev_ebit": _f(r["ev_ebit"]),
            "pe_pct": _f(r["pe_pct"]), "ps_pct": _f(r["ps_pct"]), "ev_ebitda_pct": _f(r["ev_ebitda_pct"]),
            "ev_ebit_pct": _f(r["ev_ebit_pct"]), "val_pct": _f(r["val_pct"]), "val_pct_op": _f(r["val_pct_op"]),
            "ni_op": _f(r["ni_op"]), "ni_jump4": _f(r["ni_jump4"]), "op_jump4": _f(r["op_jump4"]),
            "eps_jump4": _f(r["eps_jump4"]), "shares_yoy": _f(r["shares_yoy"]), "debt_yoy": _f(r["debt_yoy"]),
            "prior_yoy": _f(r["prior_yoy"]),
        }
        d["oneoff"] = oneoff_flag(d)
        d["acq"] = acq_flag(d)
        rows.append(d)
    qualified = rows
    liquid = [r for r in qualified if r["adv"] is not None and r["adv"] >= screen.MIN_ADV and r["years"] >= screen.MIN_YEARS]
    big = [r for r in liquid if r["mcap"] is not None and r["mcap"] >= screen.MIN_MCAP]
    profitable = [r for r in big if r["eps_ttm"] is not None and r["eps_ttm"] > 0
                  and (r["ni_ttm"] is None or r["ni_ttm"] > 0) and r["prof_past"] == 1.0]
    eligible = [r for r in profitable if r["rev_yoy"] is not None and screen.is_organic(r)]
    n_organic = len(eligible)
    use_oneoff = variant in ("oneoff", "both", "both_opval")
    use_acq = variant in ("acq", "both", "both_opval")
    if use_oneoff:
        eligible = [r for r in eligible if r["oneoff"] is None]
    if use_acq:
        eligible = [r for r in eligible if r["acq"] is None]
    vkey = "val_pct_op" if variant == "both_opval" else "val_pct"
    top20 = sorted(eligible, key=lambda r: -r["rev_yoy"])[:screen.TOP_GROWTH]
    valued = [r for r in top20 if r[vkey] is not None]
    top10 = sorted(valued, key=lambda r: (r[vkey], -r["rev_yoy"]))[:screen.TOP_VALUE]
    for i, r in enumerate(top20, 1):
        r["growth_rank"] = i
    for i, r in enumerate(top10, 1):
        r["value_rank"] = i
    return {
        "date": snap.date().isoformat(), "as_of": as_of.date().isoformat(),
        "month_end": month_end.date().isoformat(), "variant": variant, "organic": True,
        "n_universe": len(tables), "n_qualified": len(qualified), "n_liquid": len(liquid),
        "n_mcap": len(big), "n_profitable": len(profitable), "n_organic": n_organic, "n_eligible": len(eligible),
        "n_flag_oneoff": sum(1 for r in profitable if r["oneoff"] is not None and screen.is_organic(r)),
        "n_flag_acq": sum(1 for r in profitable if r["acq"] is not None and screen.is_organic(r)),
        "top20": top20, "top10": top10,
    }


def run(verbose: bool = True) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    meta = data.universe_meta()
    tickers = list(meta.index)
    print(f"screen v3: building monthly tables for {len(tickers)} tickers", file=sys.stderr, flush=True)
    tables = build_tables(tickers, verbose)
    today = pd.Timestamp.today().normalize()
    for variant in VARIANTS:
        snaps = []
        for snap in screen.snapshot_dates():
            s = screen_at(tables, meta, snap, variant)
            snaps.append(s)
        (OUT / f"snapshots_{variant}.json").write_text(json.dumps(snaps, indent=1), encoding="utf-8")
        flat = [{"date": s["date"], **r, "in_top10": "value_rank" in r} for s in snaps for r in s["top20"]]
        pd.DataFrame(flat).to_csv(OUT / f"snapshots_{variant}.csv", index=False)
        cur = screen_at(tables, meta, today, variant)
        (OUT / f"current_{variant}.json").write_text(json.dumps(cur, indent=1), encoding="utf-8")
        removed = sum(s["n_organic"] - s["n_eligible"] for s in snaps)
        print(f"  {variant:11s}: {len(snaps)} snapshots, {removed} organic-eligible rows removed by the guards; "
              f"today's top10 {', '.join(r['ticker'] for r in cur['top10'])}", file=sys.stderr, flush=True)
    print(f"wrote {OUT}", file=sys.stderr)


if __name__ == "__main__":
    run()
