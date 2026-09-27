"""Run the turnaround backtest scenarios and write the report.

    python data.py prices && python data.py edgar   # once (slow)
    python screen.py                                # quarterly top-20 / top-10 lists
    python backtest.py                              # -> output/results.json, report.md, *_trades.csv

Scenarios (all: $100,000 start, max 10% per stock, quarterly scan, no taxes):

  base            trim half at +50%; keep the rest until monthly RSI >= 90 or a new
                  top-10 name needs cash and the position is up > 100% (then sell it all)
  no_trim         same, but never trim
  rotate          hold exactly the current top 10: sell whatever left the list each quarter
  base_no_wd      base without the yearly withdrawals (shows the withdrawal drag)
  rsi80           base with the monthly-RSI exit at 80 (a monthly RSI of 90 is almost never printed)
  base_2009       base started on 2009-01-01, the first snapshot with usable filings data
  rotate_2009     rotate started on 2009-01-01

SPY total return with the same withdrawal rule is the benchmark for each start.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine  # noqa: E402
from engine import Scenario  # noqa: E402

OUT = engine.OUT

CFG = engine.data.CONFIG
S0 = engine.data.START.date().isoformat()
SCENARIOS = [
    Scenario("base", "Base: trim half at +50%, hold rest, RSI(m) 90 exit, replace >100% winners", start=S0),
    Scenario("no_trim", "No trim: hold until RSI(m) 90 exit or replaced", start=S0, trim_at=None),
    Scenario("rotate", "Rotate: hold exactly the current top 10 each quarter", start=S0, trim_at=None, rotate=True, replace_gain=None),
    Scenario("base_no_wd", "Base without withdrawals", start=S0, withdrawals=False),
    Scenario("rsi80", "Base with the monthly-RSI exit at 80 instead of 90", start=S0, rsi_exit=80.0),
]
if not CFG.get("synthetic"):
    SCENARIOS += [
        Scenario("base_2009", "Base, started 2009-01-01", start="2009-01-01"),
        Scenario("rotate_2009", "Rotate, started 2009-01-01", start="2009-01-01", trim_at=None, rotate=True, replace_gain=None),
    ]
BENCH = CFG.get("benchmark", "SPY")


def money(x) -> str:
    return "n/a" if x is None else f"${x:,.0f}"


def pct(x) -> str:
    return "n/a" if x is None or x != x else f"{x * 100:+.1f}%"


def year_table(years: list[dict], bench_years: list[dict] | None = None) -> list[str]:
    by = {y["year"]: y for y in (bench_years or [])}
    hdr = ["Year", "Start", "Return", "Withdrawal", "End (after)", "Cum. withdrawn", "Positions", "Cash %", "Buys", "Sells", f"{BENCH} return"]
    lines = ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
    cum = 0.0
    for y in years:
        cum += y["withdrawal"]
        b = by.get(y["year"])
        lines.append("| " + " | ".join([
            str(y["year"]) + (" (to Aug)" if y.get("partial") else ""), money(y["start"]), pct(y["return"]),
            money(y["withdrawal"]), money(y["end"]), money(cum), str(y.get("positions", "")),
            pct(y["cash_pct"]) if y.get("cash_pct") is not None else "", str(y.get("buys", "")), str(y.get("sells", "")),
            pct(b["return"]) if b else "",
        ]) + " |")
    return lines


def summary_table(results: dict, benches: dict) -> list[str]:
    hdr = ["Scenario", "Start", "First buy", "Final value", "Withdrawn", "Final + withdrawn", "CAGR (final)",
           "CAGR (no-withdrawal index)", "IRR", "Max DD", "Closed trades", "Win rate", "Avg closed ret."]
    lines = ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
    for name, r in results.items():
        s = r["summary"]
        lines.append("| " + " | ".join([
            f"**{name}**", s["start"][:4], s["first_buy"] or "-", money(s["final_value"]), money(s["total_withdrawn"]),
            money(s["final_plus_withdrawn"]), pct(s["cagr_final"]), pct(s["cagr_tr_index"]), pct(s["irr"]),
            pct(s["max_drawdown"]), str(s["closed_positions"]), pct(s["win_rate"]) if s["win_rate"] is not None else "n/a",
            f"{s['avg_closed_return_pct']:+.1f}%" if s["avg_closed_return_pct"] is not None else "n/a",
        ]) + " |")
    for key, b in benches.items():
        s = b["summary"]
        lines.append("| " + " | ".join([
            f"{BENCH} ({key})", s["start"][:4], s["start"], money(s["final_value"]), money(s["total_withdrawn"]),
            money(s["final_plus_withdrawn"]), pct(s["cagr_final"]), pct(s["cagr_tr_index"]), pct(s["irr"]),
            pct(s["max_drawdown"]), "", "", "",
        ]) + " |")
    return lines


def write_report(results: dict, benches: dict, snaps: list[dict]) -> Path:
    L = [f"# {CFG.get('label', 'Turnaround candidates backtest')} — {S0} to {engine.data.END.date().isoformat()}", ""]
    L += ["Quarterly scan (1 Jan / 1 Apr / 1 Jul / 1 Oct) with the turnaround scanner's rules "
          "(monthly RSI(14) < 42 within the last 6 completed months, ≥ 5 years of history, ≥ $5M average daily "
          "dollar volume, ≥ $1B market cap), then: profitable now and in the past, top 20 by trailing-twelve-month "
          "revenue growth, top 10 of those by valuation versus the company's own history (mean percentile of "
          "trailing P/E, P/S and EV/EBITDA). $100,000 start, at most 10% of the portfolio per stock, no taxes, "
          "commissions or slippage, dividends credited as cash, idle cash earns nothing.", ""]
    L += ["Withdrawal rule at each year end: year return > 20% → 10% of the portfolio; 10–20% → 7.5%; "
          "below 10% (including losses) → 5%. The partial year 2026 has no withdrawal.", ""]
    if CFG.get("notes"):
        for n in CFG["notes"]:
            L += [n, ""]
    else:
        L += ["**Data caveats.** Fundamentals are SEC XBRL filings, which start with fiscal-2007 comparatives for "
              "large filers and 2009–2011 for smaller ones, so no stock can pass the profitability / growth / "
              "valuation rules before 2008 and the first purchases happen in 2009: from 2004 to 2008 the portfolio "
              "sits in cash and still pays the 5% withdrawal. The universe is today's S&P 500 + 400 constituents, "
              "so companies that failed, were acquired or were dropped are missing (survivorship bias flatters "
              "every scenario, including the turnaround premise). Yahoo prices; multiples are rebuilt from filings.", ""]
    L += ["## Scenario summary", ""] + summary_table(results, benches) + [""]
    L += ["CAGR (final) compounds the ending value after withdrawals; the no-withdrawal index chains the "
          "yearly returns as if nothing had been taken out; IRR is the money-weighted return of the "
          "$100,000 in, the withdrawals out and the final value. Max DD is on the no-withdrawal index.", ""]
    for name, r in results.items():
        sc = r["scenario"]
        bkey = sc["start"][:4]
        L += [f"## {name} — {sc['label']}", ""]
        L += year_table(r["years"], benches[bkey]["years"]) + [""]
        s = r["summary"]
        L += [f"Final value {money(s['final_value'])}, withdrawn {money(s['total_withdrawn'])}, "
              f"{s['trades']} trades, {s['closed_positions']} closed positions "
              f"(win rate {pct(s['win_rate'])}, average closed return "
              f"{s['avg_closed_return_pct']:+.1f}%, median hold {s['median_hold_months']} months), "
              f"{s['open_positions']} still open." if s["closed_positions"] else
              f"Final value {money(s['final_value'])}, withdrawn {money(s['total_withdrawn'])}, no closed positions.", ""]
        reasons = pd.Series([t["reason"] for t in r["trades"] if t["side"] == "SELL"]).value_counts()
        if len(reasons):
            L += ["Sell reasons: " + ", ".join(f"{k} × {v}" for k, v in reasons.items()), ""]
        if r["open"]:
            top = sorted(r["open"], key=lambda p: -p["value"])[:15]
            losers = sorted([p for p in r["open"] if p["gain_pct"] < 0], key=lambda p: p["gain_pct"])
            L += [f"Open positions at the end: {len(r['open'])}, of which {len(losers)} below cost "
                  f"(unrealised loss {money(sum(p['value'] - p['shares'] * p['avg_cost'] for p in losers))}). "
                  "Largest: " + ", ".join(f"{p['ticker']} ({p['gain_pct']:+.0f}%, since {p['entry'][:7]})" for p in top), ""]
            if losers:
                L += ["Worst open: " + ", ".join(f"{p['ticker']} ({p['gain_pct']:+.0f}%, since {p['entry'][:7]})" for p in losers[:10]), ""]
        if r["closed"]:
            best = sorted(r["closed"], key=lambda c: -c["pnl"])[:5]
            worst = sorted(r["closed"], key=lambda c: c["pnl"])[:5]
            L += ["Best closed: " + ", ".join(f"{c['ticker']} {money(c['pnl'])} ({c['return_pct']:+.0f}%)" for c in best)]
            L += ["Worst closed: " + ", ".join(f"{c['ticker']} {money(c['pnl'])} ({c['return_pct']:+.0f}%)" for c in worst), ""]
    for key, b in benches.items():
        L += [f"## {BENCH} benchmark from {key} (same withdrawal rule)", ""] + year_table(b["years"]) + [""]
    L += ["## Quarterly top-10 lists", ""]
    L += ["| Snapshot | Qualified | Eligible | Top 10 (value rank order) |", "|---|---|---|---|"]
    for s in snaps:
        L.append(f"| {s['date']} | {s['n_qualified']} | {s['n_eligible']} | "
                 f"{', '.join(r['ticker'] for r in s['top10']) or '—'} |")
    p = OUT / "report.md"
    p.write_text("\n".join(L), encoding="utf-8")
    return p


def main():
    snaps = engine.load_snapshots()
    tickers = sorted({r["ticker"] for s in snaps for r in s["top10"]})
    print(f"backtest: {len(snaps)} snapshots, {len(tickers)} distinct top-10 tickers", file=sys.stderr)
    mkt = engine.Market(tickers, engine.data.START)
    results, benches = {}, {}
    for sc in SCENARIOS:
        r = engine.simulate(sc, snaps, mkt)
        results[sc.name] = r
        s = r["summary"]
        print(f"  {sc.name:12s} final {s['final_value']:>12,.0f}  withdrawn {s['total_withdrawn']:>10,.0f}  "
              f"IRR {s['irr'] * 100:5.1f}%  maxDD {s['max_drawdown'] * 100:5.1f}%  trades {s['trades']}", file=sys.stderr)
        pd.DataFrame(r["trades"]).to_csv(OUT / f"{sc.name}_trades.csv", index=False)
        r["equity"].to_csv(OUT / f"{sc.name}_equity.csv")
        if sc.start[:4] not in benches:
            benches[sc.start[:4]] = engine.benchmark(sc, mkt)
    for key, b in benches.items():
        s = b["summary"]
        print(f"  {BENCH} {key}     final {s['final_value']:>12,.0f}  withdrawn {s['total_withdrawn']:>10,.0f}  "
              f"IRR {s['irr'] * 100:5.1f}%  maxDD {s['max_drawdown'] * 100:5.1f}%", file=sys.stderr)
        b["equity"].to_csv(OUT / f"spy_{key}_equity.csv")
    out = {name: {k: v for k, v in r.items() if k != "equity"} for name, r in results.items()}
    out["benchmarks"] = {k: {kk: vv for kk, vv in b.items() if kk != "equity"} for k, b in benches.items()}
    (OUT / "results.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    p = write_report(results, benches, snaps)
    print(f"wrote {p}", file=sys.stderr)


if __name__ == "__main__":
    main()
