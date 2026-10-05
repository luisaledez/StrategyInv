"""Today's weekly tier A list (the live twin of yearly_backtest_weekly.py --max-rsi 25 --sector-rsi 0),
with the monthly RSI next to it.

Weekly rule (weeks ending Friday): a new all-time high with weekly RSI(14) >= 70 and >= 5 years of
history arms the stock for 156 weeks; the first week whose RSI closes below 25 is the signal.

Rows:
  signal   weekly signals whose 12-month window is still open (signal week within the last 12 months)
  watch    armed names with no signal yet whose weekly RSI closed below 30 last week

Columns on top of the weekly reading:
  monthly  monthly RSI(14) on the last completed candle and on the provisional current month, and
           whether the monthly rule was met as well: a monthly tier A buy (armed by a monthly ATH with
           RSI >= 70 in the last 36 months, first month closing below 35; Consumer Staples / Utilities /
           Materials below 30) dated from 3 months before to 6 months after the weekly signal (the
           pairing of compare_weekly_monthly.py), or the stock sitting in that zone now
  quality, cheap, quality + cheap
           the study's filters, point in time at the signal (fundamentals row of the last month-end on
           or before the signal week), as in the backtest
  rank     position among the quality + cheap signals of the same calendar year, lowest signal RSI
           first; the backtest buys the top 20 per year

    python live_weekly.py     # ~1 min; writes output/weekly_live_<date>.csv/.json and prints the list
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common  # noqa: E402
import signals as sig  # noqa: E402
import study  # noqa: E402
import live  # noqa: E402
import yearly_backtest as yb  # noqa: E402
import yearly_backtest_weekly as ybw  # noqa: E402

OUT = common.OUT
MAX_RSI = 25.0          # weekly signal level (the list of reports/OpportunityScanner2 tier A weekly vs monthly)
WATCH_RSI = 30.0        # armed, no signal yet, weekly RSI below this
M_RSI, M_SECTOR_RSI = 35.0, 30.0
TARGET = 0.20
FUND_KEYS = ("q_end", "rev_yoy", "eps_yoy", "eps_ttm", "prof_past", "oneoff", "acq", "val_pct_op", "mcap", "ps", "ev_ebitda", "pe")


def armed_now(w: pd.DataFrame, last_signal: pd.Timestamp | None) -> pd.Timestamp | None:
    """The last arming week still live at the last bar (within 156 weeks and after the last signal)."""
    arm = ((w["High"] >= w["ath_prev"]) & (w["rsi"] >= ybw.OB) & (w["years"] >= ybw.MIN_YEARS)).to_numpy()
    idx = np.where(arm)[0]
    if not len(idx) or len(w) - 1 - idx[-1] > ybw.WINDOW_W:
        return None
    d = w.index[idx[-1]]
    return d if last_signal is None or d > last_signal else None


def fund_at(fund: dict, t: str, month: pd.Timestamp) -> dict:
    f = study.fund_row(type("U", (), {"fund": fund}), t, month)
    if not f:
        return {}
    f["quality"] = bool(len(study.f_quality(pd.DataFrame([f]))))
    f["cheap"] = f.get("val_pct_op") is not None and f["val_pct_op"] <= 0.5
    return f


def monthly_side(d: pd.DataFrame, sector: str, ref: pd.Timestamp) -> dict:
    """Monthly RSI now and the monthly tier A buy paired with the weekly date `ref`."""
    done, prov = sig.monthly(d, common.LAST_MONTH), sig.monthly(d, None)
    lvl = M_SECTOR_RSI if sector in yb.STRICT_SECTORS else M_RSI
    out = {"m_rsi": float(done["rsi"].iloc[-1]), "m_rsi_prov": float(prov["rsi"].iloc[-1]),
           "m_month": done.index[-1].date().isoformat()[:7], "m_prov_month": prov.index[-1].date().isoformat()[:7]}
    ev = [e for e in sig.detect(prov, yb.TRIGGER) if e["rsi"] < lvl
          and ref - pd.DateOffset(months=3) <= e["signal_month"] <= ref + pd.DateOffset(months=6)]
    if ev:
        e = min(ev, key=lambda e: abs((e["signal_month"] - ref).days))
        out.update({"m_signal": e["signal_month"].date().isoformat()[:7], "m_signal_rsi": e["rsi"],
                    "m_signal_prov": bool(e["signal_month"] > common.LAST_MONTH),
                    "m_lead_weeks": float((e["signal_month"] - ref).days / 7)})
    for k, m in (("m_zone", done), ("m_zone_prov", prov)):
        z = live.zone(m)
        out[k] = bool(z and "A" in z["tier"] and z["rsi"] < lvl)
    out["m_hit"] = bool(out.get("m_signal") or out["m_zone"] or out["m_zone_prov"])
    out["m_status"] = (f"buy {out['m_signal']}" + (" (prov.)" if out["m_signal_prov"] else "") if out.get("m_signal")
                       else f"RSI < {lvl:.0f} now" if out["m_zone"] else f"RSI < {lvl:.0f} now (prov.)" if out["m_zone_prov"] else "")
    return out


def main() -> None:
    meta = common.universe()
    fund = common.fundamentals_tables(list(meta.index))
    spy = common.load_daily("SPY")
    last_week = ybw.last_completed_week(spy)
    open_from = last_week - pd.DateOffset(months=yb.HORIZON_M)
    rank_from = pd.Timestamp(f"{open_from.year}-01-01")      # whole calendar years, so the yearly rank is complete
    rows = []
    for t in meta.index:
        d = common.load_daily(t)
        if d is None or len(d) < 300:
            continue
        w = ybw.weekly(d, last_week)
        if len(w) < 30:
            continue
        sector = meta["sector"].get(t, "")
        adv = (d["Close"] * d["Volume"]).rolling(63, min_periods=20).mean()
        ev = ybw.detect(w, max_rsi=MAX_RSI)
        base = {"ticker": t, "name": meta["name"].get(t, ""), "sector": sector, "w_rsi": float(w["rsi"].iloc[-1]),
                "w_rsi_prov": float(ybw.weekly(d, d.index[-1] + pd.offsets.Week(weekday=4))["rsi"].iloc[-1]),
                "last_px": float(d["Close"].iloc[-1]), "last_date": d.index[-1].date().isoformat(),
                "dd_ath_now": float(d["Close"].iloc[-1] / w["ath"].iloc[-1] - 1.0)}
        adj = d["AdjClose"]
        for e in ev:
            sd = e["signal_date"]
            if sd < rank_from or not (adv.asof(sd) >= study.MIN_ADV):
                continue
            entry = float(adj.loc[:sd].iloc[-1])
            rel = adj.loc[sd + pd.Timedelta(days=1):] / entry - 1.0
            r = {**base, "status": "signal", "signal_date": sd.date().isoformat(), "year": int(sd.year), "open": bool(sd > open_from),
                 "rsi": e["rsi"], "peak_rsi": e["peak_rsi"], "last_ath_date": e["last_ath_date"].date().isoformat(),
                 "weeks_from_ath": e["weeks_from_ath"], "weeks_since": int(round((last_week - sd).days / 7)),
                 "close": e["close"], "dd_ath": e["dd_ath"],
                 "ret_since": float(rel.iloc[-1]) if len(rel) else 0.0, "max_dd": float(min(rel.min(), 0.0)) if len(rel) else 0.0,
                 "max_gain": float(max(rel.max(), 0.0)) if len(rel) else 0.0, "hit": bool(len(rel) and rel.max() >= TARGET)}
            f = fund_at(fund, t, ybw.month_end_before(sd))
            r.update({k: f.get(k) for k in FUND_KEYS + ("quality", "cheap")})
            r.update(monthly_side(d, sector, sd))
            rows.append(r)
        last_sig = ev[-1]["signal_date"] if ev else None
        arm = armed_now(w, last_sig)
        if arm is not None and base["w_rsi"] < WATCH_RSI and float(adv.iloc[-1]) >= study.MIN_ADV:
            r = {**base, "status": "watch", "rsi": base["w_rsi"], "last_ath_date": arm.date().isoformat(),
                 "weeks_from_ath": int(round((last_week - arm).days / 7)), "close": float(w["Close"].iloc[-1]),
                 "dd_ath": float(w["Close"].iloc[-1] / w["ath"].iloc[-1] - 1.0), "open": True}
            f = fund_at(fund, t, ybw.month_end_before(last_week))
            r.update({k: f.get(k) for k in FUND_KEYS + ("quality", "cheap")})
            r.update(monthly_side(d, sector, last_week))
            rows.append(r)
    df = pd.DataFrame(rows)
    df["quality"] = df["quality"].fillna(False).astype(bool)
    df["cheap"] = df["cheap"].fillna(False).astype(bool)
    df["qc"] = df["quality"] & df["cheap"]
    # the backtest's list: quality + cheap signals of a calendar year, lowest signal RSI first, top 20
    s = df[(df["status"] == "signal") & df["qc"]].sort_values(["year", "rsi", "ticker"])
    df["rank"] = s.groupby("year").cumcount() + 1
    df["rank_of"] = s.groupby("year")["ticker"].transform("size")
    df["top20"] = df["rank"] <= yb.TOP_N
    df = df[df["open"]].drop(columns="open")
    df = df.sort_values(["status", "signal_date", "rsi"], ascending=[True, False, True]).reset_index(drop=True)

    stamp = pd.Timestamp.today().date().isoformat()
    df.to_csv(OUT / f"weekly_live_{stamp}.csv", index=False)
    res = {"generated": stamp, "last_week": last_week.date().isoformat(), "last_bar": spy.index[-1].date().isoformat(),
           "last_month": common.LAST_MONTH.date().isoformat(), "max_rsi": MAX_RSI, "watch_rsi": WATCH_RSI, "top_n": yb.TOP_N,
           "rows": json.loads(df.to_json(orient="records", default_handler=str))}
    (OUT / f"weekly_live_{stamp}.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    cols = ["status", "ticker", "signal_date", "rsi", "w_rsi", "m_rsi", "m_rsi_prov", "m_status", "quality", "cheap", "qc", "rank",
            "dd_ath", "ret_since", "max_dd", "val_pct_op", "rev_yoy", "eps_yoy"]
    pd.set_option("display.width", 250); pd.set_option("display.max_rows", 400)
    print(df[cols].to_string(index=False, float_format=lambda v: f"{v:.2f}"))
    print(f"\n{len(df)} rows, last completed week {last_week.date()} -> {OUT / f'weekly_live_{stamp}.csv'}")


if __name__ == "__main__":
    main()
