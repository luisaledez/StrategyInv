"""Screen-level fundamentals and the survival gate, from Yahoo Finance via
yfinance. Cached as JSON in turnaround/cache/fundamentals/<TICKER>.json.

Everything here is a *proxy* computed from Yahoo's standardised statements.
It is meant to rank and flag candidates for a proper read of the filings,
not to replace one: Yahoo's "Total Debt" already includes capital leases,
revolver availability is not visible, and maturities are only split into
current vs non-current.
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache" / "fundamentals"
CACHE.mkdir(parents=True, exist_ok=True)


def _row(df: pd.DataFrame | None, *names: str) -> pd.Series | None:
    """First matching row (columns are period-ends, most recent first)."""
    if df is None or df.empty:
        return None
    for n in names:
        if n in df.index:
            s = df.loc[n]
            if isinstance(s, pd.DataFrame):
                s = s.iloc[0]
            return pd.to_numeric(s, errors="coerce")
    return None


def _latest(s: pd.Series | None) -> float:
    if s is None:
        return math.nan
    s = s.dropna()
    return float(s.iloc[0]) if len(s) else math.nan


def _ttm(s: pd.Series | None, n: int = 4) -> tuple[float, int]:
    """Sum of the most recent `n` quarters; returns (value, quarters used)."""
    if s is None:
        return math.nan, 0
    s = s.dropna()
    if len(s) < n:
        return math.nan, int(len(s))
    return float(s.iloc[:n].sum()), n


def _list(s: pd.Series | None, n: int = 8) -> list:
    if s is None:
        return []
    s = s.dropna().iloc[:n]
    return [{"period": str(k.date()) if hasattr(k, "date") else str(k), "value": float(v)}
            for k, v in s.items()]


def _safe_div(a: float, b: float) -> float:
    if a is None or b is None or math.isnan(a) or math.isnan(b) or b == 0:
        return math.nan
    return a / b


def _nan_to_none(o):
    if isinstance(o, float) and math.isnan(o):
        return None
    if isinstance(o, dict):
        return {k: _nan_to_none(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_nan_to_none(v) for v in o]
    return o


def fetch(ticker: str) -> dict:
    import yfinance as yf

    t = yf.Ticker(ticker)
    out: dict = {"ticker": ticker, "fetched": time.strftime("%Y-%m-%d")}

    # ---- market data -------------------------------------------------------
    try:
        fi = t.fast_info
        out["market_cap"] = float(fi.get("marketCap") or math.nan)
        out["shares_out"] = float(fi.get("shares") or math.nan)
        out["price"] = float(fi.get("lastPrice") or math.nan)
    except Exception as e:  # noqa: BLE001
        out["market_cap"] = out["shares_out"] = out["price"] = math.nan
        out["warn_fast_info"] = str(e)[:120]

    try:
        info = t.info or {}
        out["long_name"] = info.get("longName") or info.get("shortName")
        out["sector_y"] = info.get("sector")
        out["industry_y"] = info.get("industry")
        if math.isnan(out.get("market_cap", math.nan)) and info.get("marketCap"):
            out["market_cap"] = float(info["marketCap"])
    except Exception as e:  # noqa: BLE001
        out["warn_info"] = str(e)[:120]

    # ---- statements --------------------------------------------------------
    def grab(attr):
        try:
            return getattr(t, attr)
        except Exception as e:  # noqa: BLE001
            out[f"warn_{attr}"] = str(e)[:120]
            return None

    qbs = grab("quarterly_balance_sheet")
    qcf = grab("quarterly_cashflow")
    qis = grab("quarterly_income_stmt")
    ais = grab("income_stmt")

    # balance sheet (latest quarter)
    cash = _latest(_row(qbs, "Cash Cash Equivalents And Short Term Investments"))
    if math.isnan(cash):
        cash = _latest(_row(qbs, "Cash And Cash Equivalents"))
        sti = _latest(_row(qbs, "Other Short Term Investments"))
        if not math.isnan(sti):
            cash = (0 if math.isnan(cash) else cash) + sti
    total_debt = _latest(_row(qbs, "Total Debt"))
    current_debt = _latest(_row(qbs, "Current Debt And Capital Lease Obligation", "Current Debt"))
    leases = _latest(_row(qbs, "Capital Lease Obligations"))
    equity = _latest(_row(qbs, "Stockholders Equity", "Common Stock Equity"))
    shares_hist = _row(qbs, "Ordinary Shares Number", "Share Issued")
    bs_date = str(qbs.columns[0].date()) if qbs is not None and not qbs.empty else None

    # cash flow (TTM)
    ocf, q_ocf = _ttm(_row(qcf, "Operating Cash Flow"))
    capex, _ = _ttm(_row(qcf, "Capital Expenditure"))
    fcf, q_fcf = _ttm(_row(qcf, "Free Cash Flow"))
    if math.isnan(fcf) and not math.isnan(ocf):
        fcf = ocf + (0 if math.isnan(capex) else capex)
        q_fcf = q_ocf
    buybacks, _ = _ttm(_row(qcf, "Repurchase Of Capital Stock"))
    issuance, _ = _ttm(_row(qcf, "Net Common Stock Issuance"))

    # income statement (TTM + quarterly series)
    revenue, q_rev = _ttm(_row(qis, "Total Revenue"))
    net_income, _ = _ttm(_row(qis, "Net Income"))
    ebitda, _ = _ttm(_row(qis, "EBITDA", "Normalized EBITDA"))
    ebit, _ = _ttm(_row(qis, "EBIT", "Operating Income"))
    interest, _ = _ttm(_row(qis, "Interest Expense"))
    rev_q = _row(qis, "Total Revenue")
    gp_q = _row(qis, "Gross Profit")
    gm_q = None
    if rev_q is not None and gp_q is not None:
        gm_q = (gp_q / rev_q).replace([math.inf, -math.inf], math.nan)

    rev_list = _list(rev_q)
    yoy = math.nan
    if rev_q is not None and rev_q.dropna().shape[0] >= 5:
        r = rev_q.dropna()
        yoy = _safe_div(float(r.iloc[0]), float(r.iloc[4])) - 1.0

    # annual history
    a_rev = _row(ais, "Total Revenue")
    a_ni = _row(ais, "Net Income")
    annual = []
    if a_rev is not None:
        for k in a_rev.dropna().index:
            annual.append({"year": str(k.year) if hasattr(k, "year") else str(k),
                           "revenue": float(a_rev[k]),
                           "net_income": float(a_ni[k]) if a_ni is not None and k in a_ni and not math.isnan(a_ni[k]) else math.nan})
    profitable_years = sum(1 for a in annual if not math.isnan(a["net_income"]) and a["net_income"] > 0)

    # dilution: share count change over the last 4 quarters
    dilution_1y = math.nan
    if shares_hist is not None:
        sh = shares_hist.dropna()
        if len(sh) >= 5:
            dilution_1y = _safe_div(float(sh.iloc[0]), float(sh.iloc[4])) - 1.0

    # ---- survival gate -----------------------------------------------------
    burn = max(0.0, -fcf) if not math.isnan(fcf) else math.nan
    runway_months = math.nan
    if not math.isnan(burn) and not math.isnan(cash):
        runway_months = math.inf if burn == 0 else cash / (burn / 12.0)
    cd = 0.0 if math.isnan(current_debt) else current_debt
    need_24m = (2.0 * burn + cd) if not math.isnan(burn) else math.nan
    gap_24m = need_24m - cash if not (math.isnan(need_24m) or math.isnan(cash)) else math.nan

    if math.isnan(gap_24m):
        gate = "UNKNOWN"
    elif gap_24m <= 0:
        gate = "PASS"         # cash covers 24m of current burn + all debt due within a year
    elif cash >= 2.0 * burn:
        gate = "REVIEW"       # operations are funded; near-term maturities need refinancing
    else:
        gate = "FAIL"         # cannot fund 24 months of current burn from cash

    ev = out.get("market_cap", math.nan)
    if not math.isnan(ev):
        ev = ev + (0 if math.isnan(total_debt) else total_debt) - (0 if math.isnan(cash) else cash)

    out.update({
        "bs_date": bs_date,
        "cash": cash, "total_debt": total_debt, "current_debt": current_debt,
        "lease_obligations": leases, "equity": equity,
        "net_debt": (total_debt - cash) if not (math.isnan(total_debt) or math.isnan(cash)) else math.nan,
        "ocf_ttm": ocf, "capex_ttm": capex, "fcf_ttm": fcf, "ttm_quarters": q_fcf,
        "buybacks_ttm": buybacks, "stock_issuance_ttm": issuance,
        "revenue_ttm": revenue, "net_income_ttm": net_income, "ebitda_ttm": ebitda,
        "ebit_ttm": ebit, "interest_ttm": interest,
        "revenue_yoy_last_q": yoy,
        "revenue_quarters": rev_list,
        "gross_margin_quarters": _list(gm_q),
        "annual": annual, "years_reported": len(annual), "profitable_years": profitable_years,
        "dilution_1y": dilution_1y,
        # survival
        "fcf_burn_annual": burn, "runway_months": runway_months,
        "need_24m": need_24m, "gap_24m": gap_24m, "survival_gate": gate,
        "net_debt_to_ebitda": _safe_div(total_debt - cash, ebitda) if not (math.isnan(total_debt) or math.isnan(cash)) else math.nan,
        "interest_coverage": _safe_div(ebit, abs(interest)) if not math.isnan(interest) else math.nan,
        "cash_to_debt": _safe_div(cash, total_debt),
        # valuation
        "ev": ev,
        "ev_to_sales": _safe_div(ev, revenue),
        "ev_to_ebitda": _safe_div(ev, ebitda) if not math.isnan(ebitda) and ebitda > 0 else math.nan,
        "pe_ttm": _safe_div(out.get("market_cap", math.nan), net_income) if not math.isnan(net_income) and net_income > 0 else math.nan,
        "p_fcf": _safe_div(out.get("market_cap", math.nan), fcf) if not math.isnan(fcf) and fcf > 0 else math.nan,
        "p_book": _safe_div(out.get("market_cap", math.nan), equity) if not math.isnan(equity) and equity > 0 else math.nan,
    })
    return out


def get(ticker: str, max_age_days: float = 7.0, refresh: bool = False) -> dict:
    p = CACHE / f"{ticker.upper().replace('/', '-')}.json"
    if p.exists() and not refresh and (time.time() - p.stat().st_mtime) < max_age_days * 86400:
        with open(p) as f:
            return json.load(f)
    try:
        data = fetch(ticker)
    except Exception as e:  # noqa: BLE001
        data = {"ticker": ticker, "error": str(e)[:200], "survival_gate": "UNKNOWN"}
    with open(p, "w") as f:
        json.dump(_nan_to_none(data), f, indent=1, default=str)
    with open(p) as f:
        return json.load(f)


def get_many(tickers: list[str], max_age_days: float = 7.0, refresh: bool = False,
             pause: float = 0.5, verbose: bool = True) -> dict[str, dict]:
    out = {}
    for i, t in enumerate(tickers, 1):
        if verbose:
            print(f"  fundamentals {i}/{len(tickers)}: {t}", file=sys.stderr)
        out[t] = get(t, max_age_days, refresh)
        time.sleep(pause)
    return out


if __name__ == "__main__":
    for tk in [a for a in sys.argv[1:] if not a.startswith("--")] or ["ENPH"]:
        d = get(tk, refresh="--refresh" in sys.argv)
        keys = ["market_cap", "cash", "total_debt", "current_debt", "fcf_ttm", "runway_months",
                "need_24m", "gap_24m", "survival_gate", "net_debt_to_ebitda", "interest_coverage",
                "revenue_ttm", "revenue_yoy_last_q", "profitable_years", "years_reported",
                "dilution_1y", "ev_to_sales", "ev_to_ebitda", "pe_ttm"]
        print(tk, json.dumps({k: d.get(k) for k in keys}, indent=1))
