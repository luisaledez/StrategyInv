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
figure. Every component is taken as it was known on the row's `available`
date (the filing that completed the trailing year), so the three pieces sit
on the same reporting basis even when later filings restated some of them
(spin-offs, discontinued operations); later restatements are not applied,
which is what a point-in-time screen should see. Each concept is built from
one XBRL tag at a time (the best-covered tag first, the others filling the
gaps) so an annual figure and a year-to-date figure from different tags are
never combined; a company can tag a narrow line as `Revenues` in the 10-K
while the total sits under `RevenueFromContractWithCustomer...`. A sanity
guard on revenue drops or repairs readings that are non-positive or jump
more than 2.5x / below 0.4x quarter to quarter unless four discrete quarterly
facts support them; what it did is kept under "warnings" in the cached
table and printed to stderr. EBITDA is operating income + D&A, or pre-tax
income + interest + D&A when a company reports no operating-income line.
Shares are TTM net income / TTM EPS, so they are the diluted count consistent
with the EPS itself.

Raw company-facts JSON (~3 MB each) is cached in cache/edgar_raw/ (not
committed); the extracted table in cache/edgar/<TICKER>.json (committed).

    python edgar.py NKE GIS            # extract (uses caches; refetches raw facts older than 7 days)
    python edgar.py --refresh GIS      # re-extract even if the table is fresh
    python edgar.py --refresh --offline --all   # re-extract every cached table from the raw cache
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

# revenue sanity guard
JUMP_LO, JUMP_HI = 0.4, 2.5      # accepted quarter-to-quarter ratio of consecutive TTM readings
SUPPORT_TOL = 0.15               # a reading within 15% of the sum of four quarterly facts is "supported"
BASELINE_MAX_DAYS = 460          # a previous reading older than this no longer serves as the baseline
RESTATED_TOL = 0.15              # a value that moved more than 15% since first reported counts as restated
PRIMARY_TAG_MIN_SHARE = 0.75     # non-revenue: the first tag (in TAGS order) with >= 75% of the best tag's records leads


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


def _collect(facts: dict, tag: str) -> list[dict]:
    """Records for one tag, one per (start, end) period, with the value from
    every filing that reported it: `filed` is the first filing (when the period
    became public), `vals` maps filing date -> value as reported then."""
    ns, name = ("dei", tag[4:]) if tag.startswith("dei:") else ("us-gaap", tag)
    node = facts.get(ns, {}).get(name)
    if not node:
        return []
    units = node["units"]
    unit = next((u for u in ("USD", "USD/shares", "shares") if u in units), list(units)[0])
    seen: dict[tuple, dict] = {}
    for r in units[unit]:
        if r.get("val") is None:
            continue
        key = (r.get("start"), r["end"])
        cur = seen.get(key)
        if cur is None:
            cur = seen[key] = {"start": r.get("start"), "end": r["end"], "filed": r["filed"], "vals": {}}
        cur["filed"] = min(cur["filed"], r["filed"])
        cur["vals"][r["filed"]] = float(r["val"])
    for rec in seen.values():
        rec["filings"] = sorted(rec["vals"])
        rec["days"] = (_d(rec["end"]) - _d(rec["start"])).days if rec["start"] else None
    return list(seen.values())


def _merge(lists: list[list[dict]]) -> list[dict]:
    """Records from several tags, earlier lists winning when a period is reported under several."""
    best: dict[tuple, dict] = {}
    for recs in lists:
        for r in recs:
            best.setdefault((r["start"], r["end"]), r)
    return list(best.values())


def _records(facts: dict, tags: list[str]) -> list[dict]:
    return _merge([_collect(facts, t) for t in tags])


def _asof(rec: dict, date: str) -> tuple[float, str]:
    """(value, filing date) as known on `date`: the latest filing on or before
    it, or the first filing when the period was not yet public."""
    chosen = rec["filings"][0]
    for f in rec["filings"]:
        if f <= date:
            chosen = f
        else:
            break
    return rec["vals"][chosen], chosen


def _split_factor(splits: list, basis: str) -> float:
    """Cumulative split ratio for splits dated after the filing a figure came from."""
    f = 1.0
    for d, ratio in splits:
        if d > basis:
            f *= ratio
    return f


def _restated(rec: dict, date: str, value, tol: float = RESTATED_TOL) -> bool:
    """True when the value known on `date` differs materially from the value
    first reported (both on today's share basis, so a split is not a restatement)."""
    orig = value(rec, rec["filings"][0])[0]
    now = value(rec, date)[0]
    return abs(now - orig) > tol * max(abs(orig), abs(now), 1e-9)


def _ttm_series(rows: list[dict], splits: list | None = None) -> dict[str, dict]:
    """{end: {val, available, basis, derived, mismatch}} trailing-twelve-month
    values from annual + YTD facts of ONE concept/tag. Every component is
    valued as it was known on the row's `available` date. When a period is
    reported under several (start, end) pairs, the one first reported earliest
    is the period's record (a later duplicate is a restated comparative, e.g.
    continuing operations after a spin-off). A derived reading whose year-ago
    comparative was restated in the current filing while the annual anchor
    was not (or the other way round) mixes two reporting bases: it is flagged
    `mismatch` for the caller to drop. For per-share figures pass `splits`:
    every component is first put on today's share basis (divided by the splits
    that came after the filing it was taken from), so annual and year-to-date
    values from filings on different sides of a split can be combined."""
    dur = sorted((r for r in rows if r["start"]), key=lambda r: r["filed"])

    def value(r: dict, date: str) -> tuple[float, str]:
        v, f = _asof(r, date)
        if splits:
            v = v / _split_factor(splits, f)
        return v, f

    annual: dict[str, dict] = {}
    for r in dur:
        if 350 <= r["days"] <= 380:
            annual.setdefault(r["end"], r)      # earliest first-filed record wins
    by_end: dict[str, list[dict]] = {}
    for r in dur:
        if 80 <= r["days"] <= 290:
            by_end.setdefault(r["end"], []).append(r)
    out: dict[str, dict] = {}
    for end, a in annual.items():
        v, f = value(a, a["filed"])
        out[end] = {"val": v, "available": a["filed"], "basis": f, "derived": False, "mismatch": False}
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
        # YTD fact: starts right after the fiscal year end (longest span; earliest filed on a tie)
        ytd = [r for r in cands if abs((_d(r["start"]) - _d(f)).days - 1) <= 7]
        if not ytd:
            continue
        ytd = max(ytd, key=lambda r: (r["days"], -int(r["filed"].replace("-", ""))))
        # same YTD a year earlier (earliest filed first, since `dur` is sorted by first filing)
        prior = [r for r2 in by_end.values() for r in r2
                 if abs((e - _d(r["end"])).days - 365) <= 10 and abs(r["days"] - ytd["days"]) <= 10]
        if not prior:
            continue
        pr = min(prior, key=lambda r: r["filed"])
        available = max(annual[f]["filed"], ytd["filed"], pr["filed"])
        va, fa = value(annual[f], available)
        vy, fy = value(ytd, available)
        vp, fp = value(pr, available)
        pr_re, an_re = _restated(pr, available, value), _restated(annual[f], available, value)
        ratio = None
        if pr_re != an_re:
            rec = pr if pr_re else annual[f]
            o = value(rec, rec["filings"][0])[0]
            ratio = value(rec, available)[0] / o if o else None
        out[end] = {"val": va + vy - vp, "available": available, "basis": max(fa, fy, fp),
                    "derived": True, "mismatch": pr_re != an_re, "restate_ratio": ratio}
    return out


def _flow_series(facts: dict, name: str, tags: list[str], splits: list | None,
                 log: list[str]) -> tuple[dict[str, dict], dict[str, dict]]:
    """(series, alternatives) for a concept. The series is built one tag at a
    time: the leading tag is, for revenue, the one with the largest typical
    annual value (total revenue is the widest revenue concept; a company can
    tag a segment or "other revenue" line as `Revenues`), and otherwise the
    first tag in priority order with at least PRIMARY_TAG_MIN_SHARE of the
    best-covered tag's duration records; the other tags fill missing quarter
    ends in that order, and the old cross-tag merge is the last resort for
    quarter ends no single tag can complete. `alternatives` maps a quarter end
    to every tag's reported annual value there, for the revenue guard. Readings
    that mix two reporting bases (see _ttm_series) are dropped and logged."""
    per_tag = [(t, _collect(facts, t)) for t in tags]
    per_tag = [(t, r) for t, r in per_tag if any(x["start"] for x in r)]
    if not per_tag:
        return {}, {}
    recs = dict(per_tag)
    series = {t: _ttm_series(recs[t], splits) for t, _ in per_tag}
    counts = {t: sum(1 for x in r if x["start"]) for t, r in per_tag}
    if name == "rev":
        def typical(t):
            vals = sorted(v["val"] for v in series[t].values())
            return vals[len(vals) // 2] if vals else 0.0
        order = sorted((t for t, _ in per_tag), key=lambda t: (-typical(t), -counts[t]))
    else:
        best = max(counts.values())
        primary = next(t for t, _ in per_tag if counts[t] >= PRIMARY_TAG_MIN_SHARE * best)
        order = [primary] + sorted((t for t, _ in per_tag if t != primary), key=lambda t: -counts[t])
    out: dict[str, dict] = {}
    alts: dict[str, dict] = {}
    for t in order:
        for end, v in series[t].items():
            out.setdefault(end, {**v, "tag": t, "lead": t == order[0]})
            if not v["derived"]:
                alts.setdefault(end, {})[t] = v["val"]
    for end, v in _ttm_series(_merge([recs[t] for t, _ in per_tag]), splits).items():
        out.setdefault(end, {**v, "tag": "mixed"})
    for end in sorted(out):
        if out[end]["mismatch"]:
            r = out[end].get("restate_ratio")
            how = f"restated to {r:.2f}x its first-reported value" if r is not None else "restated"
            log.append(f"{end} {name}_ttm dropped: year-ago comparative {how} in the filing while the "
                       f"annual anchor was not (or vice versa); the two bases do not combine")
            del out[end]
    return out, alts


def _quarter_sum(end: str, ends: list[str], quarters: dict[str, list[dict]], available: str) -> float | None:
    """Sum of the four discrete-quarter facts ending at `end` and the three
    quarter ends before it, valued as of `available`; None unless all four
    exist and span about a year."""
    i = ends.index(end)
    if i < 3:
        return None
    four = ends[i - 3:i + 1]
    if not 240 <= (_d(four[-1]) - _d(four[0])).days <= 300:
        return None
    tot = 0.0
    for e in four:
        recs = quarters.get(e)
        if not recs:
            return None
        tot += _asof(recs[0], available)[0]
    return tot


def _guard_revenue(series: dict[str, dict], rows: list[dict], alts: dict[str, dict], log: list[str]) -> None:
    """Drop or repair revenue readings that are non-positive or jump outside
    [JUMP_LO, JUMP_HI] versus the previous accepted reading, unless the
    underlying facts support them: a reported annual figure is a primary fact
    (kept, resets the baseline, unless another tag reports an annual figure
    for the same period that fits the baseline, which then replaces it); a
    reading derived from the leading tag, whose three components sit on one
    reporting basis, is exact arithmetic (kept, logged); otherwise the sum of four
    discrete quarterly facts must agree, or replaces the reading, or the
    reading is dropped."""
    quarters: dict[str, list[dict]] = {}
    for r in rows:
        if r["start"] and 80 <= r["days"] <= 100:
            quarters.setdefault(r["end"], []).append(r)
    ends = sorted(series)
    accepted: tuple[str, float] | None = None
    for end in ends:
        v = series[end]
        val = v["val"]
        reason = None
        if val <= 0:
            reason = f"non-positive ({val:,.0f})"
        elif accepted and (_d(end) - _d(accepted[0])).days <= BASELINE_MAX_DAYS:
            ratio = val / accepted[1]
            if not JUMP_LO <= ratio <= JUMP_HI:
                reason = f"{val:,.0f} is {ratio:.2f}x the {accepted[0]} reading"
        if reason is None:
            accepted = (end, val)
            continue
        if val > 0 and not v["derived"]:
            fit = [(t, x) for t, x in alts.get(end, {}).items()
                   if t != v["tag"] and accepted and JUMP_LO <= x / accepted[1] <= JUMP_HI]
            if fit:
                t, x = max(fit, key=lambda tx: tx[1])
                log.append(f"{end} rev_ttm {reason}: reported annual figure ({v['tag']}) replaced by the "
                           f"{t} annual figure {x:,.0f}, which fits the series")
                v["val"], v["tag"], v["repaired"] = x, t, True
                accepted = (end, x)
            else:
                log.append(f"{end} rev_ttm {reason}: reported annual figure ({v['tag']}), kept")
                accepted = (end, val)
            continue
        if val > 0 and v.get("lead"):
            log.append(f"{end} rev_ttm {reason}: derived from {v['tag']} facts on one basis, kept")
            accepted = (end, val)
            continue
        qs = _quarter_sum(end, ends, quarters, v["available"])
        if qs is not None and qs > 0 and abs(val - qs) <= SUPPORT_TOL * qs:
            log.append(f"{end} rev_ttm {reason}: supported by four quarterly facts ({qs:,.0f}), kept")
            accepted = (end, val)
        elif qs is not None and qs > 0:
            log.append(f"{end} rev_ttm {reason}: replaced by the sum of four quarterly facts ({qs:,.0f})")
            v["val"] = qs
            v["repaired"] = True
            accepted = (end, qs)
        else:
            log.append(f"{end} rev_ttm {reason}: no quarterly support, dropped")
            del series[end]


def _instant_series(rows: list[dict]) -> dict[str, dict]:
    return {r["end"]: {"val": _asof(r, r["filed"])[0], "available": r["filed"]} for r in rows if not r["start"]}


def extract(facts: dict, splits: list | None = None) -> tuple[list[dict], list[str]]:
    """(quarter rows, warnings) from a company-facts document."""
    log: list[str] = []
    flows, alts = {}, {}
    for k, v in TAGS.items():
        flows[k], alts[k] = _flow_series(facts["facts"], k, v, splits if k == "eps" else None, log)
    _guard_revenue(flows["rev"], _records(facts["facts"], TAGS["rev"]), alts["rev"], log)
    inst = {k: _instant_series(_records(facts["facts"], v)) for k, v in INSTANT_TAGS.items()}
    # shares from the weighted-average tag are durations; fall back to those if no instants
    if not inst["shares"]:
        wa = _records(facts["facts"], ["WeightedAverageNumberOfDilutedSharesOutstanding"])
        inst["shares"] = {r["end"]: {"val": _asof(r, r["filed"])[0], "available": r["filed"]} for r in wa if r["start"]}

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
    return rows, log


def _splits(ticker: str) -> list:
    """[[date, ratio], ...] stock splits from Yahoo (ratio 2 = 2-for-1)."""
    try:
        import yfinance as yf
        s = yf.Ticker(ticker).splits
        return [[d.strftime("%Y-%m-%d"), float(v)] for d, v in s.items() if v and v > 0]
    except Exception:  # noqa: BLE001
        return []


def get(ticker: str, refresh: bool = False, offline: bool = False, verbose: bool = True) -> dict:
    """Extracted quarterly table for `ticker` (cached 7 days). `refresh`
    re-extracts; `offline` reuses the cached raw facts and the cached split
    list whatever their age (no SEC or Yahoo requests)."""
    fname = f"{ticker.upper()}.json"
    existing = find("edgar", fname)
    if existing and not refresh and is_fresh("edgar", existing, 7.0):
        return json.loads(existing.read_text(encoding="utf-8"))
    p = CACHE / fname
    try:
        facts = company_facts(ticker, max_age_days=float("inf") if offline else 7.0)
        if facts is None:
            data = {"ticker": ticker, "error": "no CIK for ticker (not a US SEC filer?)", "quarters": []}
        else:
            splits = None
            if offline and existing:
                splits = json.loads(existing.read_text(encoding="utf-8")).get("splits")
            if splits is None:
                splits = _splits(ticker)
            quarters, warnings = extract(facts, splits)
            data = {"ticker": ticker, "cik": facts.get("cik"), "name": facts.get("entityName"),
                    "fetched": time.strftime("%Y-%m-%d"), "quarters": quarters,
                    "splits": splits, "warnings": warnings}
            if verbose:
                for w in warnings:
                    print(f"edgar {ticker}: {w}", file=sys.stderr)
    except Exception as e:  # noqa: BLE001
        data = {"ticker": ticker, "error": str(e)[:200], "quarters": []}
    text = json.dumps(data, separators=(",", ":"))
    for attempt in range(3):
        try:
            p.write_text(text, encoding="utf-8")
            break
        except OSError:  # transient lock on Windows (indexer / sync client)
            if attempt == 2:
                raise
            time.sleep(1.0)
    return data


if __name__ == "__main__":
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    names = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--all" in flags:
        names = sorted(p.stem for p in READ_CACHE.glob("*.json"))
    for tk in names or ["NKE"]:
        d = get(tk, refresh="--refresh" in flags, offline="--offline" in flags, verbose="--all" not in flags)
        q = d["quarters"]
        if "--all" in flags:
            if d.get("error") or d.get("warnings"):
                print(tk, d.get("error", ""), f"{len(d.get('warnings', []))} warnings")
            continue
        print(tk, d.get("name"), d.get("error", ""), f"{len(q)} quarters",
              f"{q[0]['end']} .. {q[-1]['end']}" if q else "")
        for r in q[-3:] + q[:2]:
            print("  ", {k: (round(v, 2) if isinstance(v, float) and abs(v) < 1e4 else v) for k, v in r.items()})
        have = {k: sum(1 for r in q if r.get(k) is not None) for k in ("eps_ttm", "rev_ttm", "ebitda_ttm", "debt", "cash", "shares")}
        print("   coverage:", have)
