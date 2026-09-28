"""Two follow-up checks on the default events (output/events_default.csv):

1. Own-stock baseline: each signal's forward return minus the average forward
   return of the *same stock* over every month it was in the universe (>= 5
   years listed, liquid) from 2009. Survivorship lifts both sides equally, so
   what is left is the value of the timing alone.
2. Entry timing: the signal fires early (the median stock falls another 14-20%
   afterwards). Compared entries, all measured to the same exit (the month-end
   close 24 months after the signal month) so they are directly comparable:
     signal     buy the signal month's close
     hook       first month within 12 months whose RSI and close are both above
                the previous month's (momentum turning up)
     dip15      first month-end close >= 15% below the signal close within 12 months
     rsi40      first month within 12 months with RSI < 40
     thirds     1/3 at the signal, 1/3 at -10%, 1/3 at -20% (month-end closes, within
                12 months); unfilled thirds stay in cash
   A variant that never triggers is "missed" and reported separately.

    python timing.py     # after study.py; writes output/timing.json and output/events_timing.csv
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
EXIT_M = 24


def own_baseline(u: study.Universe, start="2009-01-31") -> dict[int, pd.Series]:
    first = {t: d.index[0] for t, d in u.daily.items()}
    A = u.A.loc[pd.Timestamp(start):]
    years = pd.DataFrame({t: (A.index - first[t]).days / 365.25 for t in A.columns}, index=A.index)
    ok = (years >= 5.0) & (u.adv.loc[A.index] >= study.MIN_ADV)
    return {h: u.fwd[h].loc[A.index].where(ok).mean() for h in (12, 24, 36)}


def entries(m: pd.DataFrame, A: pd.Series, s_month: pd.Timestamp) -> dict:
    """Entry price and date for each variant (adjusted closes), plus the exit price."""
    idx = m.index
    if s_month not in idx:
        return {}
    i0 = idx.get_loc(s_month)
    exit_m = s_month + pd.offsets.MonthEnd(EXIT_M)
    if exit_m > common.LAST_MONTH or exit_m not in A.index or pd.isna(A.get(exit_m)):
        return {}
    px_exit = float(A[exit_m])
    adj = A.reindex(idx)
    p0 = float(adj.iloc[i0])
    out = {"exit": px_exit, "signal": (s_month, p0)}
    win = range(i0 + 1, min(i0 + 13, len(idx)))
    rsi, close = m["rsi"].to_numpy(), m["Close"].to_numpy()
    out["hook"] = next(((idx[j], float(adj.iloc[j])) for j in win if rsi[j] > rsi[j - 1] and close[j] > close[j - 1]), None)
    out["dip15"] = next(((idx[j], float(adj.iloc[j])) for j in win if adj.iloc[j] <= p0 * 0.85), None)
    out["rsi40"] = next(((idx[j], float(adj.iloc[j])) for j in range(i0, min(i0 + 13, len(idx))) if rsi[j] < 40), None)
    t2 = next((float(adj.iloc[j]) for j in win if adj.iloc[j] <= p0 * 0.90), None)
    t3 = next((float(adj.iloc[j]) for j in win if adj.iloc[j] <= p0 * 0.80), None)
    fills = [p0] + [x for x in (t2, t3) if x is not None]
    # thirds: each filled third earns exit/price - 1; unfilled thirds earn 0
    out["thirds_ret"] = sum(px_exit / x - 1.0 for x in fills) / 3.0
    return out


def main() -> None:
    u = study.Universe()
    ev = pd.read_csv(OUT / "events_default.csv", parse_dates=["signal_month", "peak_month", "last_ath_month"])
    ev = ev[ev["signal_month"] >= "2009-01-01"].copy()
    own = own_baseline(u)
    for h in (12, 24, 36):
        ev[f"own{h}"] = ev["ticker"].map(own[h])
        ev[f"x{h}_own"] = ev[f"r{h}"] - ev[f"own{h}"]
    res = {"own": {}}
    groups = {"signal": ev, "signal + quality": study.f_quality(ev), "signal + quality + cheap": study.f_quality_val(ev)}
    rsi35 = [p for p in OUT.glob("events_base_RSI*.csv")]
    if rsi35:
        b = pd.read_csv(rsi35[0], parse_dates=["signal_month"])
        b = b[b["signal_month"] >= "2009-01-01"].copy()
        for h in (12, 24, 36):
            b[f"x{h}_own"] = b[f"r{h}"] - b["ticker"].map(own[h])
        groups["RSI(m) < 35 (old trigger)"] = b
        groups["RSI(m) < 35 + quality"] = study.f_quality(b)
    for g, df in groups.items():
        row = {}
        for h in (12, 24, 36):
            x = df[f"x{h}_own"].dropna()
            by_m = x.groupby(df.loc[x.index, "signal_month"]).mean()
            se = by_m.std(ddof=1) / math.sqrt(len(by_m)) if len(by_m) > 2 else np.nan
            row[f"{h}m"] = {"n": int(len(x)), "median": float(x.median()), "mean": float(x.mean()),
                            "beat_own": float((x > 0).mean()), "clustered": float(by_m.mean()),
                            "t": float(by_m.mean() / se) if se else np.nan}
        res["own"][g] = row

    # entry timing
    rows = []
    for _, e in ev.iterrows():
        t = e["ticker"]
        en = entries(u.monthly[t], u.A[t], e["signal_month"])
        if not en:
            continue
        r = {"ticker": t, "signal_month": e["signal_month"], "quality": bool(len(study.f_quality(ev.loc[[e.name]])))}
        for k in ("signal", "hook", "dip15", "rsi40"):
            v = en.get(k)
            r[k] = en["exit"] / v[1] - 1.0 if v else np.nan
            r[k + "_lag"] = (v[0].to_period("M") - e["signal_month"].to_period("M")).n if v else np.nan
        r["thirds"] = en["thirds_ret"]
        rows.append(r)
    tm = pd.DataFrame(rows)
    tm.to_csv(OUT / "events_timing.csv", index=False)
    res["timing"] = {}
    for g, df in (("all signals", tm), ("quality signals", tm[tm["quality"]])):
        blk = {}
        for k in ("signal", "hook", "dip15", "rsi40", "thirds"):
            x = df[k]
            hit = x.notna()
            blk[k] = {"n": int(len(df)), "filled": float(hit.mean()), "median": float(x[hit].median()),
                      "mean": float(x[hit].mean()), "hit": float((x[hit] > 0).mean()),
                      # a missed entry keeps the money in cash (0%) to compare like for like
                      "mean_all": float(x.fillna(0.0).mean()),
                      "median_lag": float(df[k + "_lag"].median()) if k + "_lag" in df else 0.0,
                      "better_than_signal": float((x[hit] > df.loc[hit, "signal"]).mean())}
        res["timing"][g] = blk
    (OUT / "timing.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    print(json.dumps(res, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
