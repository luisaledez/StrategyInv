"""Monthly-RSI turnaround scanner.

Step 1 of the strategy: find distress. Screens a universe on the last
*completed* monthly candle, then pulls fundamentals only for the names that
pass the price screen and applies the survival gate.

Usage
-----
  python scan.py                          # S&P 500 + 400, default rules
  python scan.py --universe sp500,sp400,sp600
  python scan.py --tickers ENPH,INTC,NKE  # ad-hoc list, no index universe
  python scan.py --extra ENPH,BABA        # index universe + extra names
  python scan.py --no-fundamentals        # price screen only (fast)
  python scan.py --init-thesis ENPH       # create thesis/ENPH.md from template
  python scan.py --as-of 2025-06-30       # run the price screen as of a past date

Outputs (turnaround/output/):
  screen_all.csv      every ticker with RSI / drawdown / liquidity metrics
  watchlist.csv/json  qualifiers with fundamentals + survival gate
  watchlist.md        human-readable watchlist with links to thesis files
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import indicators as ind  # noqa: E402
import prices  # noqa: E402
import universe as uni_mod  # noqa: E402

OUT = HERE / "output"
OUT.mkdir(exist_ok=True)
THESIS = HERE / "thesis"
THESIS.mkdir(exist_ok=True)


# ------------------------------------------------------------------ price screen
def price_metrics(ticker: str, daily: pd.DataFrame, threshold: float, lookback: int,
                  as_of: pd.Timestamp | None, rsi_period: int = 14) -> dict | None:
    if as_of is not None:
        daily = daily.loc[:as_of]
    if len(daily) < 30:
        return None
    m = ind.monthly_bars(daily, as_of=as_of)
    if len(m) < rsi_period + 2:
        return None
    rsi = ind.wilder_rsi(m["Close"], rsi_period)
    rsi_now = float(rsi.iloc[-1])
    rsi_prev = float(rsi.iloc[-2])
    if math.isnan(rsi_now):
        return None

    # RSI including the current partial month (informational only)
    m_part = ind.monthly_bars(daily, as_of=as_of, drop_partial=False)
    rsi_partial = float(ind.wilder_rsi(m_part["Close"], rsi_period).iloc[-1])

    eps = ind.rsi_episodes(rsi, threshold)
    last_month = m.index[-1]
    cutoff = (last_month.to_period("M") - (lookback - 1)).to_timestamp(how="end").normalize()
    ep = eps[-1] if eps else None
    ep_active = bool(ep and ep["exit"] is None)
    ep_recent = bool(ep and ep["end"] >= cutoff)
    months_since = None
    if ep:
        months_since = (last_month.to_period("M") - ep["end"].to_period("M")).n

    dd, high, high_date = ind.drawdown_from_high(daily["Close"], 5.0)
    close = daily["Close"]
    last = float(close.iloc[-1])

    def ret(months: int) -> float:
        ref = close.loc[: close.index[-1] - pd.DateOffset(months=months)]
        return last / float(ref.iloc[-1]) - 1.0 if len(ref) else math.nan

    ma200 = float(close.tail(200).mean()) if len(close) >= 200 else math.nan
    years = (daily.index[-1] - daily.index[0]).days / 365.25

    return {
        "ticker": ticker,
        "price": last,
        "last_bar": daily.index[-1].date().isoformat(),
        "last_month": last_month.date().isoformat(),
        "rsi_m": round(rsi_now, 1),
        "rsi_m_prev": round(rsi_prev, 1),
        "rsi_partial_month": round(rsi_partial, 1),
        "oversold_now": rsi_now < threshold,
        "qualified": ep_recent,
        "episode_active": ep_active,
        "episode_start": ep["start"].date().isoformat() if ep else None,
        "episode_end": ep["end"].date().isoformat() if ep else None,
        "episode_exit": ep["exit"].date().isoformat() if ep and ep["exit"] is not None else None,
        "episode_months": ep["months"] if ep else 0,
        "episode_min_rsi": round(ep["min_rsi"], 1) if ep else None,
        "months_since_oversold": months_since,
        "episodes_15y": len(eps),
        "drawdown_5y": round(dd, 4),
        "high_5y": round(high, 2),
        "high_date": high_date.date().isoformat(),
        "ret_3m": round(ret(3), 4),
        "ret_12m": round(ret(12), 4),
        "pct_vs_200dma": round(last / ma200 - 1.0, 4) if not math.isnan(ma200) else None,
        "adv_3m_usd": round(ind.avg_dollar_volume(daily), 0),
        "years_history": round(years, 1),
        "first_bar": daily.index[0].date().isoformat(),
    }


# ------------------------------------------------------------------ formatting
def _money(x) -> str:
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "n/a" if x is None or math.isnan(x) else "inf"
    a = abs(x)
    s = "-" if x < 0 else ""
    if a >= 1e9:
        return f"{s}${a / 1e9:.2f}B"
    if a >= 1e6:
        return f"{s}${a / 1e6:.0f}M"
    return f"{s}${a:,.0f}"


def _pct(x) -> str:
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:+.1f}%"


def _num(x, d=1) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    if isinstance(x, float) and math.isinf(x):
        return "inf"
    return f"{x:.{d}f}"


def _runway(v) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    return "inf" if v >= 1e6 else f"{v:.0f}m"


def write_markdown(wl: pd.DataFrame, args, as_of_label: str) -> Path:
    p = OUT / "watchlist.md"
    lines = [f"# Turnaround watchlist — {as_of_label}", ""]
    lines.append(f"Rules: monthly Wilder RSI({args.rsi_period}) < {args.threshold} on the last completed "
                 f"monthly candle, or oversold within the last {args.lookback} completed months; "
                 f"market cap ≥ {_money(args.min_mcap)}; avg daily $ volume (3m) ≥ {_money(args.min_adv)}; "
                 f"≥ {args.min_years} years of price history. Drawdown is from the trailing 5-year high "
                 f"of daily closes. Priority = drawdown ≤ {args.priority_dd:.0%}.")
    lines.append("")
    lines.append("Survival gate is a *proxy* from Yahoo statements: PASS = cash covers 24 months of "
                 "current FCF burn plus all debt due within a year; REVIEW = burn is covered but "
                 "near-term maturities need refinancing; FAIL = cash does not cover 24 months of burn. "
                 "Verify against the filings before relying on it.")
    lines.append("")
    if wl.empty:
        lines.append("_No qualifiers._")
    else:
        hdr = ["Ticker", "Name", "Sector", "RSI(m)", "Oversold since", "Months", "DD 5y", "Mkt cap",
               "ADV$ 3m", "Gate", "Runway", "ND/EBITDA", "P/E trail", "P/E fwd", "PEG", "P/S", "EV/Sales",
               "EPS YoY", "Rev YoY", "Thesis"]
        lines.append("| " + " | ".join(hdr) + " |")
        lines.append("|" + "---|" * len(hdr))
        for _, r in wl.iterrows():
            tp = THESIS / f"{r['ticker']}.md"
            thesis = f"[{r['ticker']}.md](../thesis/{r['ticker']}.md)" if tp.exists() else "—"
            lines.append("| " + " | ".join([
                f"**{r['ticker']}**" + (" ★" if r.get("priority") else ""),
                str(r.get("name", ""))[:28],
                str(r.get("sector", ""))[:22],
                _num(r["rsi_m"]),
                str(r["episode_start"]),
                str(r["episode_months"]) + ("" if r["episode_active"] else f" (exit {r['episode_exit']})"),
                _pct(r["drawdown_5y"]),
                _money(r.get("market_cap")),
                _money(r["adv_3m_usd"]),
                str(r.get("survival_gate", "n/a")),
                _runway(r.get("runway_months")),
                _num(r.get("net_debt_to_ebitda")),
                _num(r.get("pe_trailing")),
                _num(r.get("pe_forward")),
                _num(r.get("peg"), 2),
                _num(r.get("p_sales"), 2),
                _num(r.get("ev_to_sales")),
                _pct(r.get("eps_growth_yoy")),
                _pct(r.get("revenue_yoy_last_q")),
                thesis,
            ]) + " |")
    lines += ["", "★ = drawdown beyond the priority threshold. Runway = cash ÷ monthly FCF burn (inf when FCF is positive).",
              "", f"Create a research file for a name with `python scan.py --init-thesis TICKER`."]
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


def init_thesis(ticker: str, wl_json: Path) -> Path:
    ticker = ticker.upper()
    target = THESIS / f"{ticker}.md"
    if target.exists():
        print(f"{target} already exists — not overwriting.")
        return target
    row = {}
    if wl_json.exists():
        for r in json.loads(wl_json.read_text(encoding="utf-8")):
            if r["ticker"] == ticker:
                row = r
                break
    if not row:
        # Not on the current watchlist: compute the screen facts directly.
        px = prices.load_many([ticker])
        if ticker in px:
            row = price_metrics(ticker, px[ticker], 35.0, 6, None) or {}
        import fundamentals
        f = fundamentals.get(ticker)
        row.update({k: v for k, v in f.items() if v is not None})
        uni = uni_mod.load()
        hit = uni[uni["ticker"] == ticker]
        if len(hit):
            row.setdefault("name", hit.iloc[0]["name"])
            row.setdefault("sector", hit.iloc[0]["sector"])
            row.setdefault("industry", hit.iloc[0]["industry"])
    today = date.today()
    fields = {
        "ticker": ticker, "name": row.get("name") or row.get("long_name") or "", "today": today.isoformat(),
        "review_deadline": (today + timedelta(days=180)).isoformat(),
        "episode_start": row.get("episode_start", "n/a"), "rsi_m": _num(row.get("rsi_m")),
        "episode_months": row.get("episode_months", "n/a"), "episode_min_rsi": _num(row.get("episode_min_rsi")),
        "drawdown_5y": _pct(row.get("drawdown_5y")), "high_5y": _num(row.get("high_5y"), 2),
        "high_date": row.get("high_date", "n/a"), "market_cap": _money(row.get("market_cap")),
        "adv_3m": _money(row.get("adv_3m_usd")), "sector": row.get("sector") or row.get("sector_y") or "",
        "industry": row.get("industry") or row.get("industry_y") or "",
        "survival_gate": row.get("survival_gate", "n/a"), "cash": _money(row.get("cash")),
        "current_debt": _money(row.get("current_debt")), "fcf_ttm": _money(row.get("fcf_ttm")),
        "gap_24m": _money(row.get("gap_24m")), "net_debt_to_ebitda": _num(row.get("net_debt_to_ebitda")),
        "interest_coverage": _num(row.get("interest_coverage")), "ev_to_sales": _num(row.get("ev_to_sales")),
        "ev_to_ebitda": _num(row.get("ev_to_ebitda")), "pe_ttm": _num(row.get("pe_ttm")),
        "p_fcf": _num(row.get("p_fcf")), "revenue_yoy_last_q": _pct(row.get("revenue_yoy_last_q")),
        "pe_trailing": _num(row.get("pe_trailing")), "pe_forward": _num(row.get("pe_forward")),
        "peg": _num(row.get("peg"), 2), "p_sales": _num(row.get("p_sales"), 2),
        "eps_ttm": _num(row.get("eps_ttm"), 2), "eps_forward": _num(row.get("eps_forward"), 2),
        "eps_growth_yoy": _pct(row.get("eps_growth_yoy")), "eps_growth_last_q": _pct(row.get("eps_growth_last_q")),
        "eps_forward_growth": _pct(row.get("eps_forward_growth")),
        "profitable_years": row.get("profitable_years", "n/a"), "years_reported": row.get("years_reported", "n/a"),
    }
    tpl = (HERE / "thesis_template.md").read_text(encoding="utf-8")
    target.write_text(tpl.format(**fields), encoding="utf-8")
    print(f"created {target}")
    return target


# ------------------------------------------------------------------------ main
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--universe", default="sp500,sp400", help="comma list of sp500,sp400,sp600")
    ap.add_argument("--tickers", default="", help="scan only these tickers (comma list)")
    ap.add_argument("--extra", default="", help="add these tickers to the index universe")
    ap.add_argument("--threshold", type=float, default=35.0, help="monthly RSI threshold")
    ap.add_argument("--rsi-period", type=int, default=14)
    ap.add_argument("--lookback", type=int, default=6, help="months a past qualification stays valid")
    ap.add_argument("--min-mcap", type=float, default=1e9)
    ap.add_argument("--min-adv", type=float, default=5e6, help="min avg daily $ volume, 3 months")
    ap.add_argument("--min-years", type=float, default=5.0)
    ap.add_argument("--priority-dd", type=float, default=-0.40)
    ap.add_argument("--as-of", default=None, help="YYYY-MM-DD: run price screen as of this date")
    ap.add_argument("--no-fundamentals", action="store_true")
    ap.add_argument("--refresh", action="store_true", help="force re-download of prices")
    ap.add_argument("--refresh-fundamentals", action="store_true")
    ap.add_argument("--init-thesis", default=None, help="create thesis/<TICKER>.md and exit")
    args = ap.parse_args(argv)

    if args.init_thesis:
        init_thesis(args.init_thesis, OUT / "watchlist.json")
        return

    as_of = pd.Timestamp(args.as_of) if args.as_of else None
    as_of_label = args.as_of or date.today().isoformat()

    # ---- universe
    if args.tickers:
        tickers = [uni_mod.yahoo_symbol(t) for t in args.tickers.split(",") if t.strip()]
        uni = uni_mod.load(custom=tickers)
        uni = uni[uni["ticker"].isin(tickers)]
    else:
        extra = [t for t in args.extra.split(",") if t.strip()]
        uni = uni_mod.load(tuple(args.universe.split(",")), custom=extra)
    meta = uni.set_index("ticker")
    tickers = list(meta.index)
    print(f"scan: {len(tickers)} tickers, as of {as_of_label}", file=sys.stderr)

    # ---- prices + price screen
    px = prices.load_many(tickers, refresh=args.refresh)
    rows = []
    for t in tickers:
        d = px.get(t)
        if d is None:
            continue
        r = price_metrics(t, d, args.threshold, args.lookback, as_of, args.rsi_period)
        if r is None:
            continue
        r["name"] = meta.at[t, "name"] if "name" in meta else ""
        r["sector"] = meta.at[t, "sector"] if "sector" in meta else ""
        r["industry"] = meta.at[t, "industry"] if "industry" in meta else ""
        r["index"] = meta.at[t, "index"] if "index" in meta else ""
        rows.append(r)
    allr = pd.DataFrame(rows)
    if allr.empty:
        print("no price data", file=sys.stderr)
        return
    allr["liquid"] = allr["adv_3m_usd"] >= args.min_adv
    allr["history_ok"] = allr["years_history"] >= args.min_years
    allr["priority"] = allr["drawdown_5y"] <= args.priority_dd
    allr = allr.sort_values(["qualified", "drawdown_5y"], ascending=[False, True])
    allr.to_csv(OUT / "screen_all.csv", index=False)

    cand = allr[allr["qualified"] & allr["liquid"] & allr["history_ok"]].copy()
    print(f"scan: {int(allr['oversold_now'].sum())} oversold now, {int(allr['qualified'].sum())} qualified "
          f"within {args.lookback}m, {len(cand)} after liquidity/history", file=sys.stderr)

    # ---- fundamentals + survival gate (candidates only)
    if not args.no_fundamentals and len(cand):
        import fundamentals
        fund = fundamentals.get_many(list(cand["ticker"]), refresh=args.refresh_fundamentals)
        fcols = ["market_cap", "long_name", "sector_y", "industry_y", "bs_date", "cash", "total_debt",
                 "current_debt", "net_debt", "fcf_ttm", "ocf_ttm", "ttm_quarters", "revenue_ttm",
                 "revenue_yoy_last_q", "ebitda_ttm", "profitable_years", "years_reported", "dilution_1y",
                 "fcf_burn_annual", "runway_months", "need_24m", "gap_24m", "survival_gate",
                 "net_debt_to_ebitda", "interest_coverage", "cash_to_debt", "ev", "ev_to_sales",
                 "ev_to_ebitda", "pe_ttm", "p_fcf", "p_book", "pe_trailing", "pe_forward", "peg", "p_sales",
                 "eps_ttm", "eps_forward", "eps_growth_yoy", "eps_growth_basis", "eps_growth_last_q",
                 "eps_forward_growth", "error"]
        fdf = pd.DataFrame([{k: fund[t].get(k) for k in fcols} | {"ticker": t} for t in cand["ticker"]])
        cand = cand.merge(fdf, on="ticker", how="left")
        # fill name/sector for custom tickers from Yahoo
        cand["name"] = np.where(cand["name"].astype(str).str.len() > 0, cand["name"], cand["long_name"].fillna(""))
        cand["sector"] = np.where(cand["sector"].astype(str).str.len() > 0, cand["sector"], cand["sector_y"].fillna(""))
        cand["industry"] = np.where(cand["industry"].astype(str).str.len() > 0, cand["industry"], cand["industry_y"].fillna(""))
        cand["mcap_ok"] = cand["market_cap"].fillna(0) >= args.min_mcap
        wl = cand[cand["mcap_ok"]].copy()
        print(f"scan: {len(wl)} after market-cap filter; survival gate: "
              f"{wl['survival_gate'].value_counts().to_dict()}", file=sys.stderr)
    else:
        wl = cand.copy()

    wl["runway_months"] = wl.get("runway_months", pd.Series(dtype=float)).replace([np.inf], 1e6) if "runway_months" in wl else None
    wl = wl.sort_values(["priority", "drawdown_5y"], ascending=[False, True]).reset_index(drop=True)
    wl.to_csv(OUT / "watchlist.csv", index=False)
    recs = json.loads(wl.to_json(orient="records"))
    (OUT / "watchlist.json").write_text(json.dumps(recs, indent=1), encoding="utf-8")
    md = write_markdown(wl, args, as_of_label)

    # ---- console summary
    show = ["ticker", "sector", "rsi_m", "episode_start", "episode_months", "drawdown_5y", "adv_3m_usd"]
    if "survival_gate" in wl:
        show += ["market_cap", "survival_gate", "runway_months", "net_debt_to_ebitda", "pe_trailing", "pe_forward",
                 "peg", "p_sales", "eps_growth_yoy"]
    with pd.option_context("display.width", 200, "display.max_rows", 500):
        out = wl[show].copy()
        out["drawdown_5y"] = out["drawdown_5y"].map(_pct)
        out["adv_3m_usd"] = out["adv_3m_usd"].map(_money)
        if "market_cap" in out:
            out["market_cap"] = out["market_cap"].map(_money)
            out["runway_months"] = out["runway_months"].map(_runway)
            out["net_debt_to_ebitda"] = out["net_debt_to_ebitda"].map(_num)
            for c in ("pe_trailing", "pe_forward"):
                out[c] = out[c].map(_num)
            for c in ("peg", "p_sales"):
                out[c] = out[c].map(lambda v: _num(v, 2))
            out["eps_growth_yoy"] = out["eps_growth_yoy"].map(_pct)
        print(out.to_string(index=False))
    print(f"\nwrote {OUT / 'screen_all.csv'}, {OUT / 'watchlist.csv'}, {OUT / 'watchlist.json'}, {md}")


if __name__ == "__main__":
    main()
