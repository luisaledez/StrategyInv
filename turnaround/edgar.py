"""Quarterly trailing-twelve-month fundamentals from SEC EDGAR XBRL "company
facts" (free, no key, US filers, data from ~2008 when XBRL became mandatory).

For each ticker this produces a small table, one row per fiscal quarter end:

  end        quarter end date
  available  date the figures were public: the first filing that reported
             them, capped at 90 days after the quarter end (pre-2010 periods
             only exist in XBRL as comparatives in later filings, but were
             public within the normal reporting deadline)
  eps_ttm, ni_ttm, rev_ttm, opinc_ttm, da_ttm   trailing four quarters
  ebitda_ttm = opinc_ttm + da_ttm (when both are reported)
  debt, cash, shares                             point-in-time at quarter end

TTM at a 10-Q date is FY(last fiscal year) + YTD(this year) - YTD(same period
last year), the standard way to get four trailing quarters from the
year-to-date figures companies actually file. At a 10-K date it is the annual
figure. Restated values are resolved by taking the latest filing. EBITDA is
operating income + D&A, or pre-tax income + interest + D&A when a company
reports no operating-income line. Shares are TTM net income / TTM EPS, so
they are the diluted count consistent with the EPS itself.

Raw company-facts JSON (~3 MB each) is cached in cache/edgar_raw/ (not
committed); the extracted table in cache/edgar/<TICKER>.json (committed).
"""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from paths import cache_dirs, find, is_fresh  # noqa: E402

RAW_READ, RAW_CACHE = cache_dirs("edgar_raw")
READ_CACHE, CACHE = cache_dirs("edgar")
UA = "StrategiesInv turnaround scanner (contact: lledezma@healthprocanada.com)"

TAGS = {
    "eps": ["EarningsPerShareDiluted", "EarningsPerShareBasicAndDiluted", "EarningsPerShareBasic"],
    "ni": ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss"],
    "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueGoodsNet",
            "RevenuesNetOfInterestExpense", "TotalRevenuesAndOtherIncome"],
    "opinc": ["OperatingIncomeLoss"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic"],
    "interest": ["InterestExpense", "InterestExpenseDebt", "InterestExpenseNonoperating", "InterestAndDebtExpense"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
           "DepreciationAmortizationAndAccretionNet", "DepreciationAmortizationAndOther", "Depreciation"],
}
INSTANT_TAGS = {
    "debt_noncurrent": ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations",
                        "LongTermDebtAndFinanceLeasesNoncurrent", "LongTermDebt"],
    "debt_current": ["DebtCurrent", "LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent",
                     "ShortTermBorrowings", "CommercialPaper"],
    "cash": ["CashCashEquivalentsAndShortTermInvestments", "CashAndCashEquivalentsAtCarryingValue",
             "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
    "sti": ["ShortTermInvestments", "MarketableSecuritiesCurrent", "AvailableForSaleSecuritiesDebtSecuritiesCurrent",
            "AvailableForSaleSecuritiesCurrent"],
    "shares": ["dei:EntityCommonStockSharesOutstanding", "CommonStockSharesOutstanding",
               "WeightedAverageNumberOfDilutedSharesOutstanding"],
}


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            import gzip
            data = gzip.decompress(data)
        return data


_TICKER_MAP: dict[str, int] | None = None


def cik_for(ticker: str) -> int | None:
    global _TICKER_MAP
    if _TICKER_MAP is None:
        p = find("edgar_raw", "company_tickers.json")
        if p is None or not is_fresh("edgar_raw", p, 30):
            p = RAW_CACHE / "company_tickers.json"
            p.write_bytes(_get("https://www.sec.gov/files/company_tickers.json"))
        raw = json.loads(p.read_text(encoding="utf-8"))
        _TICKER_MAP = {v["ticker"].upper(): int(v["cik_str"]) for v in raw.values()}
    t = ticker.upper()
    return _TICKER_MAP.get(t) or _TICKER_MAP.get(t.replace("-", "")) or _TICKER_MAP.get(t.replace("-", "."))


def company_facts(ticker: str, max_age_days: float = 7.0) -> dict | None:
    cik = cik_for(ticker)
    if cik is None:
        return None
    fname = f"CIK{cik:010d}.json"
    p = find("edgar_raw", fname)
    if p is None or not is_fresh("edgar_raw", p, max_age_days):
        p = RAW_CACHE / fname
        p.write_bytes(_get(f"https://data.sec.gov/api/xbrl/companyfacts/{fname}"))
        time.sleep(0.15)  # SEC asks for <= 10 requests/second
    return json.loads(p.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ extraction
def _d(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


def _records(facts: dict, tags: list[str]) -> list[dict]:
    """Records for a concept, merged across the listed tags (earlier tags win
    when a period is reported under several), de-duplicated by period.
    The value comes from the latest filing (restatements), `filed` is the
    FIRST filing that reported the period (when it became public)."""
    best: dict[tuple, dict] = {}
    for tag in tags:
        ns, name = ("dei", tag[4:]) if tag.startswith("dei:") else ("us-gaap", tag)
        node = facts.get(ns, {}).get(name)
        if not node:
            continue
        units = node["units"]
        unit = next((u for u in ("USD", "USD/shares", "shares") if u in units), list(units)[0])
        seen: dict[tuple, dict] = {}
        for r in units[unit]:
            if r.get("val") is None:
                continue
            key = (r.get("start"), r["end"])
            cur = seen.get(key)
            if cur is None:
                seen[key] = {"start": r.get("start"), "end": r["end"], "val": float(r["val"]),
                             "filed": r["filed"], "filed_last": r["filed"]}
            else:
                cur["filed"] = min(cur["filed"], r["filed"])
                if r["filed"] > cur["filed_last"]:
                    cur["filed_last"], cur["val"] = r["filed"], float(r["val"])
        for key, rec in seen.items():
            best.setdefault(key, rec)
    return list(best.values())


def _split_factor(splits: list, basis: str) -> float:
    """Cumulative split ratio for splits dated after the filing a figure came from."""
    f = 1.0
    for d, ratio in splits:
        if d > basis:
            f *= ratio
    return f


def _ttm_series(rows: list[dict], splits: list | None = None) -> dict[str, dict]:
    """{end: {val, available}} trailing-twelve-month values from annual + YTD facts.
    For per-share figures pass `splits`: every component is first put on today's
    share basis (divided by the splits that came after the filing it was taken
    from), so annual and year-to-date values from filings on different sides
    of a split can be combined."""
    dur = [r for r in rows if r["start"]]
    for r in dur:
        r["days"] = (_d(r["end"]) - _d(r["start"])).days
        if splits:
            r["val"] = r["val"] / _split_factor(splits, r["filed_last"])
    annual = {r["end"]: r for r in dur if 350 <= r["days"] <= 380}
    by_end: dict[str, list[dict]] = {}
    for r in dur:
        if 80 <= r["days"] <= 290:
            by_end.setdefault(r["end"], []).append(r)
    out: dict[str, dict] = {}
    for end, a in annual.items():
        out[end] = {"val": a["val"], "available": a["filed"], "basis": a["filed_last"]}
    ann_ends = sorted(annual)
    for end, cands in by_end.items():
        if end in out:
            continue
        e = _d(end)
        # fiscal year that this quarter belongs to: latest annual end before it, within ~300 days
        prev_fy = [f for f in ann_ends if _d(f) < e and (e - _d(f)).days <= 300]
        if not prev_fy:
            continue
        f = prev_fy[-1]
        # YTD fact: starts right after the fiscal year end
        ytd = [r for r in cands if abs((_d(r["start"]) - _d(f)).days - 1) <= 7]
        if not ytd:
            continue
        ytd = max(ytd, key=lambda r: r["days"])
        # same YTD a year earlier
        prior = [r for r2 in by_end.values() for r in r2
                 if abs((e - _d(r["end"])).days - 365) <= 10 and abs(r["days"] - ytd["days"]) <= 10]
        if not prior:
            continue
        pr = prior[0]
        out[end] = {"val": annual[f]["val"] + ytd["val"] - pr["val"],
                    "available": max(annual[f]["filed"], ytd["filed"], pr["filed"]),
                    "basis": max(annual[f]["filed_last"], ytd["filed_last"], pr["filed_last"])}
    return out


def _instant_series(rows: list[dict]) -> dict[str, dict]:
    return {r["end"]: {"val": r["val"], "available": r["filed"]} for r in rows if not r["start"]}


def extract(facts: dict, splits: list | None = None) -> list[dict]:
    flows = {k: _ttm_series(_records(facts["facts"], v), splits if k == "eps" else None) for k, v in TAGS.items()}
    inst = {k: _instant_series(_records(facts["facts"], v)) for k, v in INSTANT_TAGS.items()}
    # shares from the weighted-average tag are durations; fall back to those if no instants
    if not inst["shares"]:
        wa = _records(facts["facts"], ["WeightedAverageNumberOfDilutedSharesOutstanding"])
        inst["shares"] = {r["end"]: {"val": r["val"], "available": r["filed"]} for r in wa if r["start"]}

    ends = sorted(set(flows["eps"]) | set(flows["rev"]) | set(flows["ni"]))

    def nearest(series: dict, end: str, tol: int = 45):
        """Instant value at/near a quarter end (cover-page share counts are dated a few weeks later)."""
        e = _d(end)
        best = None
        for d, v in series.items():
            gap = abs((_d(d) - e).days)
            if gap <= tol and (best is None or gap < best[0]):
                best = (gap, v)
        return best[1] if best else None

    rows = []
    for end in ends:
        row = {"end": end}
        avail = []
        for k in TAGS:
            v = flows[k].get(end)
            row[f"{k}_ttm"] = v["val"] if v else None
            if v:
                avail.append(v["available"])
                if k == "eps":
                    # EPS is already on today's share basis (see _ttm_series), so no later
                    # split applies; keep the field for transparency
                    row["basis"] = time.strftime("%Y-%m-%d")
        for k in ("cash", "sti", "shares", "debt_noncurrent", "debt_current"):
            v = nearest(inst[k], end)
            row[k] = v["val"] if v else None
            if v:
                avail.append(v["available"])
        if row.get("cash") is not None and row.get("sti") is not None:
            row["cash"] += row["sti"]
        row["debt"] = (row.pop("debt_noncurrent") or 0.0) + (row.pop("debt_current") or 0.0)
        row.pop("sti", None)
        ebit = row.get("opinc_ttm")
        if ebit is None and row.get("pretax_ttm") is not None:
            ebit = row["pretax_ttm"] + abs(row.get("interest_ttm") or 0.0)
        da = row.get("da_ttm")
        row["ebitda_ttm"] = (ebit + da) if ebit is not None and da is not None and da > 0 else None
        # diluted shares implied by TTM net income / TTM EPS: consistent with the EPS itself and
        # immune to multi-class share counts; fall back to the reported instant count
        if row.get("ni_ttm") and row.get("eps_ttm"):
            implied = row["ni_ttm"] / row["eps_ttm"]
            if implied > 0:
                row["shares"] = implied
        for k in ("pretax_ttm", "interest_ttm"):
            row.pop(k, None)
        cap = (_d(end) + timedelta(days=90)).strftime("%Y-%m-%d")
        row["available"] = min(max(avail), cap) if avail else cap
        if row["eps_ttm"] is not None or row["rev_ttm"] is not None:
            rows.append(row)
    return rows


def _splits(ticker: str) -> list:
    """[[date, ratio], ...] stock splits from Yahoo (ratio 2 = 2-for-1)."""
    try:
        import yfinance as yf
        s = yf.Ticker(ticker).splits
        return [[d.strftime("%Y-%m-%d"), float(v)] for d, v in s.items() if v and v > 0]
    except Exception:  # noqa: BLE001
        return []


def get(ticker: str, refresh: bool = False) -> dict:
    fname = f"{ticker.upper()}.json"
    existing = find("edgar", fname)
    if existing and not refresh and is_fresh("edgar", existing, 7.0):
        return json.loads(existing.read_text(encoding="utf-8"))
    p = CACHE / fname
    try:
        facts = company_facts(ticker)
        if facts is None:
            data = {"ticker": ticker, "error": "no CIK for ticker (not a US SEC filer?)", "quarters": []}
        else:
            splits = _splits(ticker)
            data = {"ticker": ticker, "cik": facts.get("cik"), "name": facts.get("entityName"),
                    "fetched": time.strftime("%Y-%m-%d"), "quarters": extract(facts, splits),
                    "splits": splits}
    except Exception as e:  # noqa: BLE001
        data = {"ticker": ticker, "error": str(e)[:200], "quarters": []}
    p.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    return data


if __name__ == "__main__":
    for tk in [a for a in sys.argv[1:] if not a.startswith("--")] or ["NKE"]:
        d = get(tk, refresh="--refresh" in sys.argv)
        q = d["quarters"]
        print(tk, d.get("name"), d.get("error", ""), f"{len(q)} quarters",
              f"{q[0]['end']} .. {q[-1]['end']}" if q else "")
        for r in q[-3:] + q[:2]:
            print("  ", {k: (round(v, 2) if isinstance(v, float) and abs(v) < 1e4 else v) for k, v in r.items()})
        have = {k: sum(1 for r in q if r.get(k) is not None) for k in ("eps_ttm", "rev_ttm", "ebitda_ttm", "debt", "cash", "shares")}
        print("   coverage:", have)
