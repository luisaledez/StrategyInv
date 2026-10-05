"""Today's OpportunityScanner2 list.

Arming (all tiers): a new all-time high on a monthly candle with monthly RSI(14)
>= 70 and >= 5 years of history, within the last 36 months (24 for tiers B and C).
Tiers, from the study (README.md):

  A  "leader washed out"     monthly RSI < 40 now (armed in the last 36 months); RSI < 35 is the
                             strongest group in the study
  B  "deep reset"            RSI <= 68% of the highest arming RSI of the last 24 months and the
                             close >= 40% below the ATH
  C  "momentum reset"        RSI <= 68% of that peak (the user's -32% rule) - watchlist only:
                             on its own it has done no better than a random month in the same stock

Each name gets the point-in-time fundamentals the study used (TTM profitability,
revenue growth, EPS growth, one-off / acquisition flags, valuation percentile vs
its own history on P/S, EV/EBITDA, EV/EBIT) plus Yahoo's analyst forward EPS
growth, and a pass/fail on the study's "quality" and "cheap" filters.

Rows use the last completed monthly candle (common.LAST_MONTH, written to each row as
`last_month`) and, separately, a provisional candle for the current month from the latest
daily close (`tier_prov`, `rsi_prov`).

    python live.py            # writes output/live_<date>.csv/.json and prints the list
    python live.py --no-yahoo # skip the analyst estimates download
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common  # noqa: E402
import signals as sig  # noqa: E402
import study  # noqa: E402

OUT = common.OUT
OB, MIN_YEARS = 70.0, 5.0
DROP = 0.32


def zone(m: pd.DataFrame) -> dict | None:
    """Scanner reading at the last row of a monthly frame (from signals.monthly), with the same
    definitions as the study's variants (variants.py):
      C  RSI <= 68% of the highest arming RSI of the last 24 months     ("rsi-32%")
      B  C and the close >= 40% below the all-time high                ("rsi-32% + price-40%")
      A  an arming month in the last 36 months and RSI < 40            ("leader + RSI<40"; RSI < 35 flagged)"""
    if len(m) < 30:
        return None
    last = len(m) - 1
    rsi = m["rsi"].to_numpy(); high = m["High"].to_numpy(); ath_prev = m["ath_prev"].to_numpy(); yrs = m["years"].to_numpy()
    arm = (high >= ath_prev) & (rsi >= OB) & (yrs >= MIN_YEARS)
    arm[last] = False
    arm36 = np.where(arm[max(0, last - 36): last])[0] + max(0, last - 36)
    if not len(arm36):
        return None
    arm24 = arm36[arm36 >= last - 24]
    r = float(rsi[last]); close = float(m["Close"].iloc[-1]); ath = float(m["ath"].iloc[-1])
    dd = close / ath - 1.0
    pk = arm24[np.argmax(rsi[arm24])] if len(arm24) else arm36[np.argmax(rsi[arm36])]
    peak_rsi = float(rsi[pk])
    level = peak_rsi * (1 - DROP)
    tiers = []
    if r < 40:
        tiers.append("A")
    if len(arm24) and r <= level and dd <= -0.40:
        tiers.append("B")
    if len(arm24) and r <= level:
        tiers.append("C")
    # first month since the last arming month in which the -32% rule held
    first_c = next((m.index[j] for j in range(arm36[-1] + 1, last + 1) if rsi[j] <= level), None)
    return {"tier": "".join(tiers) or "-", "rsi35": r < 35, "rsi": r, "peak_rsi": peak_rsi,
            "peak_month": m.index[pk].date().isoformat(), "last_ath_month": m.index[arm36[-1]].date().isoformat(),
            "months_since_ath": int(last - arm36[-1]), "rsi_chg": r / peak_rsi - 1.0, "trigger_c": level,
            "close": close, "ath": ath, "dd_ath": dd,
            "first_c": first_c.date().isoformat() if first_c is not None else None}


def fund_now(fund: dict, t: str) -> dict:
    tb = fund.get(t)
    if tb is None or not len(tb):
        return {}
    row = tb.dropna(subset=["q_end"]).iloc[-1:] if tb["q_end"].notna().any() else tb.iloc[-1:]
    month = row.index[-1]
    u = type("U", (), {"fund": fund})
    f = study.fund_row(u, t, month)
    f["fund_month"] = month.date().isoformat()
    one = pd.DataFrame([{**f, "adv": 1e12}])
    f["quality"] = bool(len(study.f_quality(one)))
    f["cheap"] = f.get("val_pct_op") is not None and f["val_pct_op"] <= 0.5
    return f


def main(yahoo: bool = True) -> None:
    meta = common.universe()
    fund = common.fundamentals_tables(list(meta.index))
    rows = []
    for t in meta.index:
        d = common.load_daily(t)
        if d is None or len(d) < 300:
            continue
        adv = float((d["Close"] * d["Volume"]).tail(63).mean())
        if adv < study.MIN_ADV:
            continue
        done = sig.monthly(d, common.LAST_MONTH)
        prov = sig.monthly(d, None)
        z, zp = zone(done), zone(prov)
        if (z is None or z["tier"] == "-") and (zp is None or zp["tier"] == "-"):
            continue
        r = {"ticker": t, "name": meta["name"].get(t, ""), "sector": meta["sector"].get(t, ""), "adv": adv,
             "last_px": float(d["Close"].iloc[-1]), "last_date": d.index[-1].date().isoformat(),
             "last_month": common.LAST_MONTH.date().isoformat()}
        for k, v in (z or {}).items():
            r[k] = v
        r["tier"] = (z or {}).get("tier", "-")
        r["tier_prov"] = (zp or {}).get("tier", "-")
        r["rsi_prov"] = (zp or {}).get("rsi")
        f = fund_now(fund, t)
        for k in ("q_end", "rev_yoy", "prior_yoy", "gw_ev", "eps_yoy", "eps_ttm", "prof_past", "oneoff", "acq", "val_pct_op", "mcap",
                  "ps", "ev_ebitda", "pe", "quality", "cheap"):
            r[k] = f.get(k)
        rows.append(r)
    df = pd.DataFrame(rows)
    if yahoo and len(df):
        import fundamentals as yf_fund  # turnaround/fundamentals.py, path set by common
        fw = []
        short = df[(df["tier"] != "-") | (df["tier_prov"] != "-")]
        for t in short["ticker"]:
            try:
                g = yf_fund.get(t)
                fw.append({"ticker": t, "eps_fwd_growth": g.get("eps_forward_growth"), "pe_fwd": g.get("pe_forward"),
                           "rev_growth_yahoo": g.get("revenue_growth_yoy")})
            except Exception as e:  # noqa: BLE001
                print(f"  yahoo {t}: {e}", file=sys.stderr)
        if fw:
            df = df.merge(pd.DataFrame(fw), on="ticker", how="left")
    tier_rank = {"A": 0, "AB": 0, "ABC": 0, "AC": 0, "B": 1, "BC": 1, "C": 2}
    df["tier_rank"] = df["tier"].map(tier_rank).fillna(3)
    df = df.sort_values(["tier_rank", "quality", "cheap", "rsi"], ascending=[True, False, False, True])
    stamp = pd.Timestamp.today().date().isoformat()
    df.to_csv(OUT / f"live_{stamp}.csv", index=False)
    (OUT / f"live_{stamp}.json").write_text(df.to_json(orient="records", indent=1, default_handler=str), encoding="utf-8")
    cols = ["ticker", "tier", "rsi35", "tier_prov", "rsi", "rsi_prov", "peak_rsi", "peak_month", "dd_ath", "first_c",
            "quality", "cheap", "rev_yoy", "eps_yoy", "val_pct_op", "eps_fwd_growth", "oneoff", "acq"]
    pd.set_option("display.width", 250); pd.set_option("display.max_rows", 400)
    print(df[[c for c in cols if c in df.columns]].to_string(index=False, float_format=lambda v: f"{v:.2f}"))
    print(f"\n{len(df)} names -> {OUT / f'live_{stamp}.csv'}")


if __name__ == "__main__":
    main(yahoo="--no-yahoo" not in sys.argv)
