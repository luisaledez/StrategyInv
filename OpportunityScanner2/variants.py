"""Head-to-head of signal variants on the fairest yardstick (the same stock's own
average forward return, see timing.py) plus SPY and the universe, for 2009+,
the last 10 years and the last 5 years, with and without fundamentals.

Variants keep the user's arming rule (new all-time high with monthly RSI >= 70)
and add how much damage must be done before buying:

    rsi-32%                 the RSI collapse alone (study default)
    rsi-32% + price-30%     ... and the close at least 30% below the ATH
    rsi-32% + price-40%     ... at least 40% below
    leader + RSI<40         a former overbought-ATH leader (armed in the last 36
                            months) whose monthly RSI closes below 40
    leader + RSI<35         ... below 35
    RSI<35 (any stock)      the old turnaround trigger, for reference

    python variants.py      # ~2 min; writes output/variants.json and output/events_<variant>.csv
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
import timing  # noqa: E402

OUT = common.OUT

VARIANTS = {
    "rsi-32%": sig.Params(),
    "rsi-32% + price-30%": sig.Params(min_dd=0.30),
    "rsi-32% + price-40%": sig.Params(min_dd=0.40),
    "leader + RSI<40": sig.Params(drop=0.0, max_rsi=40.0, window=36),
    "leader + RSI<35": sig.Params(drop=0.0, max_rsi=35.0, window=36),
}
PERIODS = {"2009+": "2009-01-01", "last 10y": "2016-09-01", "last 5y": "2021-09-01"}
FILTERS = {"none": lambda d: d, "quality": study.f_quality, "quality + cheap": study.f_quality_val}


def stats(df: pd.DataFrame, h: int) -> dict:
    x = df.dropna(subset=[f"r{h}"])
    if len(x) < 5:
        return {"n": int(len(x))}
    xo = x[f"x{h}_own"].dropna()
    by_m = xo.groupby(x.loc[xo.index, "signal_month"]).mean()
    se = by_m.std(ddof=1) / math.sqrt(len(by_m)) if len(by_m) > 2 else np.nan
    out = {"n": int(len(x)), "tickers": int(x["ticker"].nunique()), "median": float(x[f"r{h}"].median()),
           "hit": float((x[f"r{h}"] > 0).mean()),
           "beat_spy": float((x[f"x{h}_spy"] > 0).mean()), "med_x_spy": float(x[f"x{h}_spy"].median()),
           "med_x_own": float(xo.median()), "beat_own": float((xo > 0).mean()),
           "cl_x_own": float(by_m.mean()), "t_own": float(by_m.mean() / se) if se and se > 0 else np.nan,
           "med_x_uni": float(x[f"x{h}_uni"].median()), "bad_20": float((x[f"r{h}"] < -0.2).mean())}
    if h == 12:
        out["med_mae12"] = float(x["mae12"].median())
        out["near_bottom"] = float((x["mae12"] > -0.10).mean())
    return out


def main() -> None:
    u = study.Universe()
    own = timing.own_baseline(u)
    res = {}
    evs = {}
    for name, p in VARIANTS.items():
        evs[name] = study.liquid(study.collect(u, sig.detect, p=p))
    evs["RSI<35 (any stock)"] = study.liquid(study.collect(u, sig.detect_rsi35))
    for name, ev in evs.items():
        ev = ev.copy()
        for h in (12, 24, 36):
            ev[f"x{h}_own"] = ev[f"r{h}"] - ev["ticker"].map(own[h])
        ev.to_csv(OUT / f"events_{name.replace(' ', '').replace('%', 'pct').replace('<', 'lt').replace('+', '_')}.csv", index=False)
        res[name] = {}
        for pname, start in PERIODS.items():
            pe = ev[ev["signal_month"] >= start]
            res[name][pname] = {fn: {f"{h}m": stats(f(pe), h) for h in (12, 24, 36)} for fn, f in FILTERS.items()}
        print(f"{name}: {len(ev)} events", file=sys.stderr, flush=True)
        evs[name] = ev
    # portfolios: equal weight every open signal, hold 24 months, idle months in SPY
    port = {}
    for name, ev in evs.items():
        for fn, f in FILTERS.items():
            for st in ("2009-01-31", "2016-08-31", "2021-08-31"):
                p = study.portfolio(u, f(ev), 24, st)
                p.pop("equity", None) if st != "2009-01-31" else None
                port[f"{name} | {fn} | from {st[:7]}"] = p
    res["_portfolio"] = port
    (OUT / "variants.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
