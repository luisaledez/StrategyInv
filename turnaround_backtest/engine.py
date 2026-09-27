"""Portfolio simulation for the turnaround backtest.

Takes the quarterly top-10 lists from screen.py (output/snapshots.json) and
runs a daily simulation from 2004-01-01 to 2026-08-31:

* On the first trading day on/after each snapshot date the new top-10 list is
  applied. Every name on the list that is not already held is bought at that
  day's close with at most MAX_WEIGHT (10%) of the portfolio, from cash.
  If cash is short and a held position has gained more than REPLACE_GAIN
  (100%), that position is sold in full and the proceeds fund the new name.
  Names that drop off the list are kept ("the rest is left on the stock").
* Trim: when a position's close reaches +TRIM_AT (50%) over its average
  cost, TRIM_FRAC (half) of the shares are sold. Once per position.
* Exit: at a month-end whose monthly Wilder RSI(14) closes >= RSI_EXIT (90)
  the whole position is sold.
* Dividends are credited to cash (derived from Yahoo's adjusted close).
  Idle cash earns nothing. No taxes, commissions or slippage.
* Withdrawals: on the last trading day of every complete calendar year the
  year's return is measured on the portfolio value; WITHDRAW_BANDS maps it to
  a share of the portfolio that is taken out as cash (positions are sold
  pro-rata if cash is short). The partial year 2026 has no withdrawal.

Scenario flags switch the trim, the replacement rule, full quarterly
rotation (sell whatever left the list), the withdrawals and the start date.
"""
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass, field, asdict
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
END = data.END
INITIAL = 100_000.0


@dataclass
class Scenario:
    name: str
    label: str
    start: str = "2004-01-01"
    max_weight: float = 0.10
    trim_at: float | None = 0.50        # None disables the trim
    trim_frac: float = 0.50
    rsi_exit: float | None = 90.0
    replace_gain: float | None = 1.00   # sell a >100% winner to fund a new top-10 name; None disables
    rotate: bool = False                # sell every name that left the top-10 list
    withdrawals: bool = True
    withdraw_bands: tuple = ((0.20, 0.10), (0.10, 0.075), (-9.0, 0.05))  # (year return above, share withdrawn)
    initial: float = INITIAL


def withdraw_share(year_return: float, bands) -> float:
    for floor, share in bands:
        if year_return > floor:
            return share
    return 0.0


# ------------------------------------------------------------------ market data
class Market:
    """Aligned daily closes / dividends and month-end RSI for the tickers a run can touch."""

    def __init__(self, tickers: list[str], start: pd.Timestamp):
        spy = data.load_prices("SPY")
        self.calendar = spy.loc[start - pd.Timedelta(days=10): END].index
        self.close: dict[str, pd.Series] = {}
        self.div: dict[str, pd.Series] = {}
        self.rsi_m: dict[str, pd.Series] = {}
        self.spy_tr = spy["AdjClose"].reindex(self.calendar).ffill()
        for t in tickers:
            d = data.load_prices(t)
            if d is None:
                continue
            c = d["Close"].reindex(self.calendar)
            a = d["AdjClose"].reindex(self.calendar)
            # dividend per share on day t: extra total return beyond the price return
            with np.errstate(divide="ignore", invalid="ignore"):
                tr = a / a.shift(1)
                pr = c / c.shift(1)
                div = (c.shift(1) * (tr / pr - 1.0)).fillna(0.0)
            div = div.where(div > 1e-6, 0.0)
            self.close[t] = c
            self.div[t] = div
            m = ind.monthly_bars(d, drop_partial=False)
            self.rsi_m[t] = ind.wilder_rsi(m["Close"], 14)

    def price(self, t: str, dt: pd.Timestamp) -> float | None:
        s = self.close.get(t)
        if s is None:
            return None
        v = s.get(dt)
        return None if v is None or (isinstance(v, float) and math.isnan(v)) else float(v)

    def month_end_rsi(self, t: str, dt: pd.Timestamp) -> float | None:
        s = self.rsi_m.get(t)
        if s is None:
            return None
        me = dt.to_period("M").to_timestamp(how="end").normalize()
        v = s.get(me)
        return None if v is None or (isinstance(v, float) and math.isnan(v)) else float(v)


# ------------------------------------------------------------------ simulation
@dataclass
class Position:
    ticker: str
    shares: float
    avg_cost: float
    entry: pd.Timestamp
    trimmed: bool = False
    realized: float = 0.0
    cost_in: float = 0.0     # total dollars ever invested
    cash_out: float = 0.0    # total dollars ever received (sales + dividends)


def simulate(sc: Scenario, snaps: list[dict], mkt: Market) -> dict:
    start = pd.Timestamp(sc.start)
    cal = mkt.calendar[mkt.calendar >= start]
    snap_by_day: dict[pd.Timestamp, dict] = {}
    for s in snaps:
        d = pd.Timestamp(s["date"])
        if d < start:
            continue
        idx = cal.searchsorted(d)
        if idx < len(cal):
            snap_by_day[cal[idx]] = s

    cash = sc.initial
    pos: dict[str, Position] = {}
    trades: list[dict] = []
    equity_rows: list[tuple] = []
    withdrawals: list[dict] = []
    closed: list[dict] = []
    year_start_equity = sc.initial
    year_withdrawn = 0.0
    year_stats = {}
    years: list[dict] = []
    tr_index = 1.0
    prev_equity_after = sc.initial

    def equity_at(dt: pd.Timestamp) -> float:
        tot = cash
        for p in pos.values():
            px = mkt.price(p.ticker, dt)
            if px is not None:
                tot += p.shares * px
        return tot

    def sell(dt: pd.Timestamp, t: str, frac: float, reason: str) -> float:
        nonlocal cash
        p = pos[t]
        px = mkt.price(t, dt)
        if px is None:
            return 0.0
        sh = p.shares * frac if frac < 1.0 else p.shares
        amt = sh * px
        gain = px / p.avg_cost - 1.0
        cash += amt
        p.shares -= sh
        p.realized += sh * (px - p.avg_cost)
        p.cash_out += amt
        trades.append({"date": dt.date().isoformat(), "ticker": t, "side": "SELL", "reason": reason,
                       "shares": round(sh, 4), "price": round(px, 4), "amount": round(amt, 2),
                       "gain_pct": round(gain * 100, 2), "held_days": (dt - p.entry).days})
        if p.shares <= 1e-9:
            closed.append({"ticker": t, "entry": p.entry.date().isoformat(), "exit": dt.date().isoformat(),
                           "invested": round(p.cost_in, 2), "returned": round(p.cash_out, 2),
                           "pnl": round(p.cash_out - p.cost_in, 2),
                           "return_pct": round((p.cash_out / p.cost_in - 1) * 100, 2) if p.cost_in else None,
                           "months": round((dt - p.entry).days / 30.4375, 1), "last_reason": reason})
            del pos[t]
        return amt

    def buy(dt: pd.Timestamp, t: str, amount: float, reason: str) -> bool:
        nonlocal cash
        px = mkt.price(t, dt)
        if px is None or amount <= 0:
            return False
        sh = amount / px
        cash -= amount
        if t in pos:
            p = pos[t]
            p.avg_cost = (p.avg_cost * p.shares + amount) / (p.shares + sh)
            p.shares += sh
            p.cost_in += amount
        else:
            pos[t] = Position(t, sh, px, dt, cost_in=amount)
        trades.append({"date": dt.date().isoformat(), "ticker": t, "side": "BUY", "reason": reason,
                       "shares": round(sh, 4), "price": round(px, 4), "amount": round(amount, 2),
                       "gain_pct": None, "held_days": None})
        return True

    for i, dt in enumerate(cal):
        # ---- quarterly rebalance at the close
        s = snap_by_day.get(dt)
        if s is not None:
            wanted = [r["ticker"] for r in s["top10"] if r["ticker"] in mkt.close]
            if sc.rotate:
                for t in [t for t in pos if t not in wanted]:
                    sell(dt, t, 1.0, "left list")
            new = [t for t in wanted if t not in pos]
            eq = equity_at(dt)
            cap = sc.max_weight * eq
            for t in new:
                if mkt.price(t, dt) is None:
                    continue
                if cash < cap and sc.replace_gain is not None:
                    winners = sorted(((mkt.price(q, dt) or 0) / p.avg_cost - 1.0, q) for q, p in pos.items())
                    winners = [(g, q) for g, q in winners if g > sc.replace_gain and q not in wanted]
                    while cash < cap and winners:
                        g, q = winners.pop()      # largest gain first
                        sell(dt, q, 1.0, "replaced")
                amt = min(cap, cash)
                if amt >= max(100.0, 0.005 * eq):
                    buy(dt, t, amt, "top10")

        # ---- daily rules at the close
        is_month_end = (i + 1 == len(cal)) or cal[i + 1].month != dt.month
        for t in list(pos):
            p = pos[t]
            px = mkt.price(t, dt)
            if px is None:
                continue
            d = mkt.div[t].get(dt, 0.0)
            if d > 0:
                cash += p.shares * d
                p.cash_out += p.shares * d
            if sc.trim_at is not None and not p.trimmed and px >= p.avg_cost * (1.0 + sc.trim_at):
                p.trimmed = True
                sell(dt, t, sc.trim_frac, "trim +50%")
                continue
            if is_month_end and sc.rsi_exit is not None:
                r = mkt.month_end_rsi(t, dt)
                if r is not None and r >= sc.rsi_exit:
                    sell(dt, t, 1.0, f"RSI(m) {r:.0f}")

        # ---- bookkeeping, year end
        eq = equity_at(dt)
        is_year_end = (i + 1 < len(cal) and cal[i + 1].year != dt.year)
        wd = 0.0
        if is_year_end:
            yr_ret = eq / year_start_equity - 1.0
            if sc.withdrawals:
                share = withdraw_share(yr_ret, sc.withdraw_bands)
                wd = share * eq
                if wd > cash:
                    short = wd - cash
                    invested = eq - cash
                    for t in list(pos):
                        frac = short / invested if invested > 0 else 0.0
                        sell(dt, t, min(frac, 1.0), "withdrawal")
                    wd = min(wd, cash)   # a position without a price that day cannot be sold
                cash -= wd
                withdrawals.append({"date": dt.date().isoformat(), "year": dt.year, "amount": round(wd, 2),
                                    "share": share, "year_return": round(yr_ret, 4)})
            years.append({"year": dt.year, "start": round(year_start_equity, 2), "end_before_withdrawal": round(eq, 2),
                          "return": round(yr_ret, 4), "withdrawal": round(wd, 2),
                          "end": round(eq - wd, 2), "positions": len(pos),
                          "cash": round(cash, 2), "cash_pct": round(cash / (eq - wd), 4) if eq - wd > 0 else None,
                          "buys": sum(1 for x in trades if x["side"] == "BUY" and x["date"][:4] == str(dt.year)),
                          "sells": sum(1 for x in trades if x["side"] == "SELL" and x["date"][:4] == str(dt.year))})
            eq_after = eq - wd
            year_start_equity = eq_after
        else:
            eq_after = eq
        # total-return index: growth ignoring withdrawals
        if prev_equity_after > 0:
            tr_index *= eq / prev_equity_after
        prev_equity_after = eq_after
        equity_rows.append((dt, eq, eq_after, cash, len(pos), tr_index))

    # partial final year
    last = cal[-1]
    if not years or years[-1]["year"] != last.year:
        eq = equity_at(last)
        years.append({"year": last.year, "start": round(year_start_equity, 2), "end_before_withdrawal": round(eq, 2),
                      "return": round(eq / year_start_equity - 1.0, 4), "withdrawal": 0.0, "end": round(eq, 2),
                      "positions": len(pos), "cash": round(cash, 2),
                      "cash_pct": round(cash / eq, 4) if eq > 0 else None,
                      "buys": sum(1 for x in trades if x["side"] == "BUY" and x["date"][:4] == str(last.year)),
                      "sells": sum(1 for x in trades if x["side"] == "SELL" and x["date"][:4] == str(last.year)),
                      "partial": True})

    eqdf = pd.DataFrame(equity_rows, columns=["date", "equity", "equity_after_wd", "cash", "positions", "tr_index"]).set_index("date")
    final = float(eqdf["equity_after_wd"].iloc[-1])
    total_wd = float(sum(w["amount"] for w in withdrawals))
    yrs = (cal[-1] - cal[0]).days / 365.25
    peak = eqdf["tr_index"].cummax()
    mdd = float((eqdf["tr_index"] / peak - 1.0).min())
    flows = [(cal[0], -sc.initial)] + [(pd.Timestamp(w["date"]), w["amount"]) for w in withdrawals] + [(cal[-1], final)]
    open_pos = []
    for t, p in pos.items():
        px = mkt.price(t, last) or 0.0
        open_pos.append({"ticker": t, "entry": p.entry.date().isoformat(), "shares": round(p.shares, 4),
                         "avg_cost": round(p.avg_cost, 4), "price": round(px, 4), "value": round(p.shares * px, 2),
                         "gain_pct": round((px / p.avg_cost - 1) * 100, 2), "trimmed": p.trimmed})
    wins = [c for c in closed if c["pnl"] > 0]
    first_buy = next((x["date"] for x in trades if x["side"] == "BUY"), None)
    return {
        "scenario": asdict(sc),
        "summary": {
            "start": cal[0].date().isoformat(), "end": cal[-1].date().isoformat(), "first_buy": first_buy,
            "initial": sc.initial, "final_value": round(final, 2), "total_withdrawn": round(total_wd, 2),
            "final_plus_withdrawn": round(final + total_wd, 2),
            "cagr_final": round((final / sc.initial) ** (1 / yrs) - 1, 4) if final > 0 else None,
            "cagr_tr_index": round(float(eqdf["tr_index"].iloc[-1]) ** (1 / yrs) - 1, 4),
            "irr": round(xirr(flows), 4),
            "max_drawdown": round(mdd, 4),
            "trades": len(trades), "closed_positions": len(closed), "open_positions": len(open_pos),
            "win_rate": round(len(wins) / len(closed), 3) if closed else None,
            "avg_closed_return_pct": round(float(np.mean([c["return_pct"] for c in closed if c["return_pct"] is not None])), 2) if closed else None,
            "median_hold_months": round(float(np.median([c["months"] for c in closed])), 1) if closed else None,
        },
        "years": years, "withdrawals": withdrawals, "closed": closed, "open": open_pos,
        "trades": trades,
        "equity": eqdf,
    }


def xirr(flows: list[tuple[pd.Timestamp, float]]) -> float:
    t0 = flows[0][0]
    ts = np.array([(d - t0).days / 365.25 for d, _ in flows])
    cf = np.array([v for _, v in flows])

    def npv(r):
        return float(np.sum(cf / (1 + r) ** ts))
    lo, hi = -0.99, 5.0
    if npv(lo) * npv(hi) > 0:
        return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(lo) * npv(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def benchmark(sc: Scenario, mkt: Market) -> dict:
    """SPY total return with the same withdrawal rule (dividends reinvested)."""
    start = pd.Timestamp(sc.start)
    cal = mkt.calendar[mkt.calendar >= start]
    tr = mkt.spy_tr.reindex(cal)
    eq = sc.initial
    year_start = eq
    years, withdrawals, rows = [], [], []
    prev = tr.iloc[0]
    for i, dt in enumerate(cal):
        eq *= float(tr.iloc[i] / prev)
        prev = tr.iloc[i]
        is_year_end = (i + 1 < len(cal) and cal[i + 1].year != dt.year)
        wd = 0.0
        if is_year_end:
            r = eq / year_start - 1.0
            if sc.withdrawals:
                wd = withdraw_share(r, sc.withdraw_bands) * eq
                withdrawals.append({"date": dt.date().isoformat(), "year": dt.year, "amount": round(wd, 2), "year_return": round(r, 4)})
            years.append({"year": dt.year, "start": round(year_start, 2), "end_before_withdrawal": round(eq, 2),
                          "return": round(r, 4), "withdrawal": round(wd, 2), "end": round(eq - wd, 2)})
            eq -= wd
            year_start = eq
        rows.append((dt, eq))
    last = cal[-1]
    if not years or years[-1]["year"] != last.year:
        years.append({"year": last.year, "start": round(year_start, 2), "end_before_withdrawal": round(eq, 2),
                      "return": round(eq / year_start - 1.0, 4), "withdrawal": 0.0, "end": round(eq, 2), "partial": True})
    eqdf = pd.DataFrame(rows, columns=["date", "equity"]).set_index("date")
    total_wd = sum(w["amount"] for w in withdrawals)
    yrs = (cal[-1] - cal[0]).days / 365.25
    idx = tr / tr.iloc[0]
    mdd = float((idx / idx.cummax() - 1.0).min())
    flows = [(cal[0], -sc.initial)] + [(pd.Timestamp(w["date"]), w["amount"]) for w in withdrawals] + [(cal[-1], eq)]
    return {"summary": {"start": cal[0].date().isoformat(), "end": cal[-1].date().isoformat(), "initial": sc.initial,
                        "final_value": round(eq, 2), "total_withdrawn": round(total_wd, 2),
                        "final_plus_withdrawn": round(eq + total_wd, 2),
                        "cagr_final": round((eq / sc.initial) ** (1 / yrs) - 1, 4),
                        "cagr_tr_index": round(float(idx.iloc[-1]) ** (1 / yrs) - 1, 4),
                        "irr": round(xirr(flows), 4), "max_drawdown": round(mdd, 4)},
            "years": years, "withdrawals": withdrawals, "equity": eqdf}


def load_snapshots() -> list[dict]:
    return json.loads((OUT / "snapshots.json").read_text(encoding="utf-8"))
