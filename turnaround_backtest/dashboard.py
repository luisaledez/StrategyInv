"""Interactive dashboard for the second backtest's rescreen_only scenario
(base rules + spin-off re-screen + guidance-cut proxy, organic entries).

    python dashboard.py [port]        # http://localhost:8060

The market (prices, monthly RSI, point-in-time TTM EPS and re-basing events for
every ticker that ever made a top-10 list) is built once and pickled to
output_v2/dashboard_market.pkl; after that a run over any start/end window
takes about a second, so the timeline can be changed from the page.

Endpoints (JSON except /):
    /api/status                        market loading state
    /api/run?start&end&initial         simulate the window: summary, equity, trades, lots, snapshots
    /api/state?start&end&initial&date  holdings, cash and equity on one day (trades replayed)
    /api/series/<T>?start&end          daily close aligned to the run calendar + monthly RSI / TTM EPS
"""
from __future__ import annotations

import dataclasses
import json
import math
import pickle
import sys
import threading
import time
import traceback
from pathlib import Path

import pandas as pd
from flask import Flask, Response, abort, jsonify, request

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine  # noqa: E402
import backtest_v2  # noqa: E402

OUT = HERE / "output_v2"
SNAPS = OUT / "snapshots.json"
MARKET_PKL = OUT / "dashboard_market.pkl"
PAGE = HERE / "dashboard.html"
BASE = next(s for s in backtest_v2.SCENARIOS if s.name == "rescreen_only")
DATA_START = engine.data.START.date().isoformat()
DATA_END = engine.data.END.date().isoformat()

app = Flask(__name__)
STATE: dict = {"ready": False, "message": "starting", "error": None, "mkt": None, "snaps": None, "meta": {}}
RUNS: dict[str, dict] = {}
LOCK = threading.Lock()


# ------------------------------------------------------------------ market
def build_market() -> None:
    try:
        snaps = json.loads(SNAPS.read_text(encoding="utf-8"))
        tickers = sorted({r["ticker"] for s in snaps for r in s["top10"]})
        meta: dict[str, dict] = {}
        for s in snaps:
            for r in s.get("top20", []) + s["top10"]:
                meta.setdefault(r["ticker"], {"name": r.get("name"), "sector": r.get("sector")})
        mkt = None
        if MARKET_PKL.exists() and MARKET_PKL.stat().st_mtime >= SNAPS.stat().st_mtime:
            STATE["message"] = "loading cached market"
            try:
                with MARKET_PKL.open("rb") as f:
                    mkt = pickle.load(f)
                missing = [t for t in tickers if t not in mkt.close and engine.data.load_prices(t) is not None]
                if missing:
                    mkt = None
            except Exception:  # noqa: BLE001
                mkt = None
        if mkt is None:
            STATE["message"] = f"building market for {len(tickers)} tickers (about a minute, only the first time)"
            t0 = time.time()
            mkt = engine.Market(tickers, engine.data.START, fundamentals=True, rebase=True)
            with MARKET_PKL.open("wb") as f:
                pickle.dump(mkt, f)
            print(f"market built in {time.time() - t0:.0f}s, cached to {MARKET_PKL}", file=sys.stderr)
        STATE.update(mkt=mkt, snaps=snaps, meta=meta, ready=True, message="ready")
    except Exception as e:  # noqa: BLE001
        STATE.update(error=f"{e}\n{traceback.format_exc()}", message="failed")


# ------------------------------------------------------------------ helpers
def _num(x):
    if x is None:
        return None
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    return x


def params() -> tuple[str, str, float]:
    start = request.args.get("start") or DATA_START
    end = request.args.get("end") or DATA_END
    try:
        initial = float(request.args.get("initial") or engine.INITIAL)
        s, e = pd.Timestamp(start), pd.Timestamp(end)
    except (ValueError, TypeError):
        abort(400, "bad start / end / initial")
    if s < engine.data.START or e > engine.data.END or s >= e or initial <= 0:
        abort(400, f"window must lie within {DATA_START}..{DATA_END} with start < end and initial > 0")
    return s.date().isoformat(), e.date().isoformat(), initial


def scenario(start: str, end: str, initial: float) -> engine.Scenario:
    return dataclasses.replace(BASE, name="rescreen_only", start=start, end=end, initial=initial)


def replay(trades: list[dict], upto: str | None = None):
    """Rebuild positions from the trade log (up to and including `upto`).
    Returns (positions, lots, spy): lots are the distinct holding periods."""
    pos: dict[str, dict] = {}
    lots: list[dict] = []
    spy = {"units": 0.0, "cost": 0.0, "entry": None}
    for tr in trades:
        if upto is not None and tr["date"] > upto:
            break
        t, side = tr["ticker"], tr["side"]
        if t == "SPY":
            if side == "BUY":
                if spy["units"] <= 0:
                    spy["entry"], spy["cost"] = tr["date"], 0.0
                spy["units"] += tr["shares"]
                spy["cost"] += tr["amount"]
            else:
                frac = tr["shares"] / spy["units"] if spy["units"] > 0 else 1.0
                spy["cost"] *= max(0.0, 1.0 - frac)
                spy["units"] = max(0.0, spy["units"] - tr["shares"])
                if spy["units"] < 1e-6:
                    spy.update(units=0.0, cost=0.0, entry=None)
            continue
        if side == "BUY":
            p = pos.get(t)
            if p is None:
                p = pos[t] = {"ticker": t, "shares": 0.0, "avg_cost": 0.0, "entry": tr["date"], "cost_in": 0.0,
                              "cash_out": 0.0, "trimmed": False, "lot": len(lots)}
                lots.append({"ticker": t, "entry": tr["date"], "exit": None, "invested": 0.0, "returned": 0.0,
                             "trades": [], "last_reason": None, "trimmed": False})
            p["avg_cost"] = (p["avg_cost"] * p["shares"] + tr["amount"]) / (p["shares"] + tr["shares"])
            p["shares"] += tr["shares"]
            p["cost_in"] += tr["amount"]
            lots[p["lot"]]["invested"] += tr["amount"]
        else:
            p = pos.get(t)
            if p is None:
                continue
            p["shares"] = max(0.0, p["shares"] - tr["shares"])
            p["cash_out"] += tr["amount"]
            lot = lots[p["lot"]]
            lot["returned"] += tr["amount"]
            lot["last_reason"] = tr["reason"]
            if tr["reason"].startswith("trim"):
                p["trimmed"] = lot["trimmed"] = True
            if p["shares"] <= 0.01:
                lot["exit"] = tr["date"]
                del pos[t]
        lots[p["lot"]]["trades"].append(tr["i"])
    return pos, lots, spy


def last_value(series: pd.Series | None, dt: pd.Timestamp):
    """(value, date) of the last non-null reading on or before dt."""
    if series is None:
        return None, None
    s = series.loc[:dt].dropna()
    if s.empty:
        return None, None
    return float(s.iloc[-1]), s.index[-1].date().isoformat()


def get_run(start: str, end: str, initial: float) -> dict:
    key = f"{start}|{end}|{initial:.2f}"
    with LOCK:
        if key in RUNS:
            return RUNS[key]
    mkt, snaps = STATE["mkt"], STATE["snaps"]
    sc = scenario(start, end, initial)
    r = engine.simulate(sc, snaps, mkt)
    b = engine.benchmark(sc, mkt)
    eq: pd.DataFrame = r["equity"]
    dates = [d.date().isoformat() for d in eq.index]
    for i, tr in enumerate(r["trades"]):
        tr["i"] = i
    _, lots, _ = replay(r["trades"])
    closed_by = {(c["ticker"], c["entry"]): c for c in r["closed"]}
    open_by = {o["ticker"]: o for o in r["open"]}
    for lot in lots:
        c = closed_by.get((lot["ticker"], lot["entry"]))
        if c:
            lot.update(pnl=c["pnl"], return_pct=c["return_pct"], months=c["months"], returned=c["returned"])
        else:
            o = open_by.get(lot["ticker"])
            if o:
                lot.update(value=o["value"], return_pct=o["gain_pct"], open=True)
    first_entry = {}
    for lot in lots:
        first_entry.setdefault(lot["ticker"], lot["entry"])
    held = sorted(first_entry, key=lambda t: (first_entry[t], t))
    bench_eq = b["equity"]["equity"].reindex(eq.index)
    rebase = {t: [(d.date().isoformat(), ratio) for d, ratio in mkt.rebase.get(t, [])
                  if start <= d.date().isoformat() <= end] for t in held}
    run = {
        "key": key, "params": {"start": start, "end": end, "initial": initial},
        "scenario": dataclasses.asdict(sc),
        "summary": r["summary"], "benchmark": b["summary"], "years": r["years"], "withdrawals": r["withdrawals"],
        "closed": r["closed"], "open": r["open"], "trades": r["trades"], "lots": lots,
        "tickers": [{"ticker": t, **STATE["meta"].get(t, {})} for t in held],
        "equity": {"dates": dates,
                   "equity": [round(float(v), 2) for v in eq["equity_after_wd"]],
                   "cash": [round(float(v), 2) for v in eq["cash"]],
                   "positions": [int(v) for v in eq["positions"]],
                   "tr_index": [round(float(v), 5) for v in eq["tr_index"]],
                   "spy": [None if pd.isna(v) else round(float(v), 2) for v in bench_eq]},
        "snapshots": [{"date": s["date"], "as_of": s["as_of"], "top10": [x["ticker"] for x in s["top10"]]}
                      for s in snaps if start <= s["date"] <= end],
        "rebase": {t: v for t, v in rebase.items() if v},
        "_eq": eq,
    }
    with LOCK:
        RUNS[key] = run
    return run


def public(run: dict) -> dict:
    return {k: v for k, v in run.items() if not k.startswith("_")}


# ------------------------------------------------------------------ routes
@app.route("/")
def index():
    return Response(PAGE.read_text(encoding="utf-8"), mimetype="text/html")


@app.route("/api/status")
def status():
    return jsonify(ready=STATE["ready"], message=STATE["message"], error=STATE["error"],
                   data_start=DATA_START, data_end=DATA_END, scenario=BASE.label, n_runs=len(RUNS))


def require_ready() -> None:
    if not STATE["ready"]:
        abort(503, STATE["error"] or STATE["message"])


@app.route("/api/run")
def api_run():
    require_ready()
    start, end, initial = params()
    return jsonify(public(get_run(start, end, initial)))


@app.route("/api/state")
def api_state():
    require_ready()
    start, end, initial = params()
    run = get_run(start, end, initial)
    eq: pd.DataFrame = run["_eq"]
    want = request.args.get("date") or end
    idx = int(eq.index.searchsorted(pd.Timestamp(want), side="right")) - 1
    idx = max(0, min(idx, len(eq) - 1))
    dt = eq.index[idx]
    day = dt.date().isoformat()
    mkt = STATE["mkt"]
    pos, lots, spy = replay(run["trades"], day)
    snap = next((s for s in reversed(run["snapshots"]) if s["date"] <= day), None)
    on_list = set(snap["top10"]) if snap else set()
    cash = float(eq["cash"].iloc[idx])
    equity = float(eq["equity_after_wd"].iloc[idx])
    holdings = []
    for t, p in pos.items():
        px, px_date = last_value(mkt.close.get(t), dt)
        rsi, rsi_date = last_value(mkt.rsi_m.get(t), dt)
        eps_now, eps_date = last_value(mkt.eps_m.get(t), dt)
        entry = pd.Timestamp(p["entry"])
        eps_entry = mkt.month_end_eps(t, entry - pd.DateOffset(months=1))
        value = p["shares"] * px if px is not None else None
        holdings.append({
            "ticker": t, "name": STATE["meta"].get(t, {}).get("name"), "sector": STATE["meta"].get(t, {}).get("sector"),
            "entry": p["entry"], "held_days": int((dt - entry).days), "shares": round(p["shares"], 4),
            "avg_cost": round(p["avg_cost"], 4), "price": _num(px), "price_date": px_date,
            "value": _num(round(value, 2) if value is not None else None),
            "weight": _num(round(value / equity, 4) if value is not None and equity > 0 else None),
            "gain_pct": _num(round((px / p["avg_cost"] - 1) * 100, 2) if px is not None else None),
            "cost_in": round(p["cost_in"], 2), "cash_out": round(p["cash_out"], 2),
            "rsi_m": _num(round(rsi, 1) if rsi is not None else None), "rsi_date": rsi_date,
            "eps_entry": _num(round(eps_entry, 3) if eps_entry else None),
            "eps_now": _num(round(eps_now, 3) if eps_now is not None else None), "eps_date": eps_date,
            "eps_chg": _num(round(eps_now / eps_entry - 1, 4) if eps_entry and eps_now is not None else None),
            "guide_window_end": (entry + pd.DateOffset(months=BASE.guide_cut_months)).date().isoformat(),
            "trimmed": p["trimmed"], "on_list": t in on_list, "lot": p["lot"],
        })
    holdings.sort(key=lambda h: -(h["value"] or 0))
    spy_value = spy["units"] * float(mkt.spy_tr.loc[dt]) if spy["units"] > 0 else 0.0
    trades = run["trades"]
    today = [tr["i"] for tr in trades if tr["date"] == day]
    prev_tr = next((tr["date"] for tr in reversed(trades) if tr["date"] < day), None)
    next_tr = next((tr["date"] for tr in trades if tr["date"] > day), None)
    return jsonify({
        "date": day, "index": idx, "equity": round(equity, 2), "cash": round(cash, 2),
        "cash_pct": round(cash / equity, 4) if equity > 0 else None,
        "invested": round(equity - cash - spy_value, 2), "spy_value": round(spy_value, 2),
        "spy_cost": round(spy["cost"], 2), "n_positions": len(holdings),
        "tr_index": round(float(eq["tr_index"].iloc[idx]), 4),
        "holdings": holdings, "snapshot": snap, "trades_today": today,
        "prev_trade": prev_tr, "next_trade": next_tr,
    })


@app.route("/api/series/<ticker>")
def api_series(ticker: str):
    require_ready()
    start, end, initial = params()
    run = get_run(start, end, initial)
    mkt = STATE["mkt"]
    t = ticker.upper()
    cal = run["_eq"].index
    if t == "SPY":
        close = mkt.spy_close.reindex(cal)
        spy_daily = engine.data.load_prices("SPY")
        rsi = engine.ind.wilder_rsi(engine.ind.monthly_bars(spy_daily, drop_partial=False)["Close"], 14)
        eps = None
    elif t in mkt.close:
        close = mkt.close[t].reindex(cal)
        rsi = mkt.rsi_m.get(t)
        eps = mkt.eps_m.get(t)
    else:
        abort(404, f"{t} is not in the market")

    def monthly(s: pd.Series | None, nd: int) -> dict:
        if s is None:
            return {"dates": [], "values": []}
        s = s.loc[pd.Timestamp(start) - pd.DateOffset(months=1): pd.Timestamp(end)].dropna()
        return {"dates": [d.date().isoformat() for d in s.index], "values": [round(float(v), nd) for v in s]}

    return jsonify({
        "ticker": t, **STATE["meta"].get(t, {}),
        "close": [None if pd.isna(v) else round(float(v), 4) for v in close],
        "rsi": monthly(rsi, 1), "eps": monthly(eps, 3),
        "rebase": run["rebase"].get(t, []),
    })


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8060
    threading.Thread(target=build_market, daemon=True).start()
    app.run(host="127.0.0.1", port=port, debug=False, threaded=True)
