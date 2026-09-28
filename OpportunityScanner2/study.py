"""Event study of the RSI-collapse signal (see signals.py) over the S&P 500 + 400
universe, 2000 - Aug 2026, with baselines, a parameter sweep, point-in-time
fundamental filters and a hindsight "growth ahead" split.

    python study.py            # ~3-4 min; writes output/events_*.csv, output/study.json, output/report.md
    python study.py --rebuild  # also rebuild the cached fundamentals tables

All returns are total returns (Yahoo adjusted closes) from the signal month's last
close to the month-end close h months later. "vs universe" subtracts the
equal-weighted average return of every universe stock (>= 5 years listed) over
the same months, which removes the market's moves and most of the survivorship
bias the universe (today's index members) carries.
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common  # noqa: E402
import signals as sig  # noqa: E402
import screen_v3  # noqa: E402  (path set by common)

OUT = common.OUT
LAST = common.LAST_MONTH
HORIZONS = (3, 6, 12, 24, 36)
MIN_ADV = 5e6
PERIODS = {
    "all (2000+)": ("2000-01-01", None),
    "2009+": ("2009-01-01", None),
    "last 10y (Sep 2016+)": ("2016-09-01", None),
    "last 5y (Sep 2021+)": ("2021-09-01", None),
}


# ------------------------------------------------------------------ loading
class Universe:
    def __init__(self, rebuild: bool = False):
        t0 = time.time()
        self.meta = common.universe()
        tickers = list(self.meta.index)
        self.daily = common.load_all_daily(tickers + ["SPY"])
        self.spy = self.daily.pop("SPY")
        self.monthly = {t: sig.monthly(d, LAST) for t, d in self.daily.items()}
        self.fund = common.fundamentals_tables(list(self.daily), rebuild=rebuild)
        A = common.monthly_adj(self.daily).loc[:LAST]
        first = {t: d.index[0] for t, d in self.daily.items()}
        years = pd.DataFrame({t: (A.index - first[t]).days / 365.25 for t in A.columns}, index=A.index)
        # 3-month average dollar volume at each month-end (liquidity filter)
        self.adv = pd.DataFrame({t: (d["Close"] * d["Volume"]).rolling(63, min_periods=20).mean().resample("ME").last()
                                 for t, d in self.daily.items()}).reindex(A.index)
        self.A = A
        spy_m = self.spy["AdjClose"].resample("ME").last().loc[:LAST]
        uni_ok = years >= 5.0
        self.fwd, self.uni_fwd, self.spy_fwd = {}, {}, {}
        for h in HORIZONS:
            fwd = A.shift(-h) / A - 1.0
            self.fwd[h] = fwd
            self.uni_fwd[h] = fwd.where(uni_ok).mean(axis=1)
            self.spy_fwd[h] = spy_m.shift(-h) / spy_m - 1.0
        # worst adjusted intramonth low over the next 12 / 24 months, relative to the signal close
        L = pd.DataFrame({t: (d["Low"] * d["AdjClose"] / d["Close"]).resample("ME").min()
                          for t, d in self.daily.items()}).reindex(A.index)
        self.mae = {}
        for h in (12, 24):
            fmin = pd.concat([L.shift(-k) for k in range(1, h + 1)]).groupby(level=0).min().reindex(A.index)
            self.mae[h] = (fmin / A - 1.0).where(A.shift(-h).notna())
        self.all_fwd12 = self.fwd[12].where(uni_ok).where(self.adv >= MIN_ADV)
        print(f"loaded {len(self.daily)} tickers in {time.time() - t0:.0f}s", file=sys.stderr, flush=True)


# ------------------------------------------------------------------ event tables
def _f(x):
    if x is None:
        return None
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(x) else x


def fund_row(u: Universe, t: str, month: pd.Timestamp) -> dict:
    tb = u.fund.get(t)
    if tb is None or month not in tb.index:
        return {}
    r = tb.loc[month]
    d = {k: _f(r.get(k)) for k in ("eps_ttm", "ni_ttm", "rev_ttm", "rev_yoy", "prior_yoy", "prof_past", "eps_yoy",
                                   "ni_op", "ni_jump4", "op_jump4", "eps_jump4", "shares_yoy", "mcap", "val_pct_op",
                                   "val_pct", "ps", "ev_ebitda", "pe", "rev_qoq", "rev_jump8")}
    d["q_end"] = r.get("q_end")
    d["oneoff"] = screen_v3.oneoff_flag(d) if d.get("ni_op") is not None or d.get("ni_jump4") is not None or d.get("eps_jump4") is not None else None
    d["acq"] = screen_v3.acq_flag(d)
    return d


def enrich(u: Universe, t: str, events: list[dict], fundamentals: bool = True) -> list[dict]:
    rows = []
    for e in events:
        m = e["signal_month"]
        r = {"ticker": t, "name": u.meta["name"].get(t, ""), "sector": u.meta["sector"].get(t, ""), **e}
        r["adv"] = _f(u.adv[t].get(m)) if t in u.adv else None
        for h in HORIZONS:
            rh = u.fwd[h].at[m, t] if m in u.A.index else np.nan
            r[f"r{h}"] = rh
            r[f"x{h}_spy"] = rh - u.spy_fwd[h].get(m, np.nan)
            r[f"x{h}_uni"] = rh - u.uni_fwd[h].get(m, np.nan)
        for h in (12, 24):
            r[f"mae{h}"] = u.mae[h].at[m, t] if m in u.A.index else np.nan
        if fundamentals:
            f = fund_row(u, t, m)
            r.update({k: v for k, v in f.items()})
        rows.append(r)
    return rows


def collect(u: Universe, detector, fundamentals: bool = True, **kw) -> pd.DataFrame:
    rows = []
    for t, m in u.monthly.items():
        ev = detector(m, **kw)
        if ev:
            rows.extend(enrich(u, t, ev, fundamentals))
    df = pd.DataFrame(rows)
    if len(df):
        df = df.sort_values(["signal_month", "ticker"]).reset_index(drop=True)
    return df


def add_hindsight(df: pd.DataFrame) -> pd.DataFrame:
    """Realised growth of trailing revenue and EPS over the year after the last reported quarter."""
    cache: dict[str, list[dict]] = {}
    fr, fe = [], []
    for t, q in zip(df["ticker"], df.get("q_end", [None] * len(df))):
        if t not in cache:
            cache[t] = common.load_edgar(t)
        qe = q if isinstance(q, str) else None
        fr.append(common.realized_growth(cache[t], qe, "rev_ttm"))
        fe.append(common.realized_growth(cache[t], qe, "eps_ttm"))
    df = df.copy()
    df["fut_rev_g"] = fr
    df["fut_eps_g"] = fe
    return df


# ------------------------------------------------------------------ filters
def liquid(df):
    return df[df["adv"].fillna(0) >= MIN_ADV]


def f_prof(df):
    return df[(df["eps_ttm"] > 0) & (df["ni_ttm"].fillna(1) > 0) & (df["prof_past"] == 1.0)]


def f_grow(df, g=0.05):
    return f_prof(df)[lambda x: x["rev_yoy"] >= g]


def f_quality(df):
    x = f_grow(df, 0.05)
    return x[(x["eps_yoy"].fillna(-1) > 0) & x["oneoff"].isna() & x["acq"].isna()]


def f_quality_val(df):
    x = f_quality(df)
    return x[x["val_pct_op"] <= 0.5]


FILTERS = {
    "no fundamentals": lambda d: d,
    "profitable (TTM + 2 of 3 past yrs)": f_prof,
    "profitable + revenue growth >= 5%": lambda d: f_grow(d, 0.05),
    "profitable + revenue growth >= 10%": lambda d: f_grow(d, 0.10),
    "quality: growth >= 5%, EPS growing, no one-off/acq": f_quality,
    "quality + cheap vs own history (val pct <= 50%)": f_quality_val,
}


# ------------------------------------------------------------------ summaries
def period(df, start, end=None, h=12):
    x = df[df["signal_month"] >= pd.Timestamp(start)]
    if end:
        x = x[x["signal_month"] < pd.Timestamp(end)]
    return x


def summarize(df: pd.DataFrame, h: int = 12) -> dict:
    x = df.dropna(subset=[f"r{h}"])
    if not len(x):
        return {"n": 0, "n_open": int(len(df))}
    r = x[f"r{h}"]; xs = x[f"x{h}_spy"]; xu = x[f"x{h}_uni"]
    by_m = xu.groupby(x["signal_month"]).mean()
    se = by_m.std(ddof=1) / math.sqrt(len(by_m)) if len(by_m) > 2 else np.nan
    out = {
        "n": int(len(x)), "n_open": int(len(df) - len(x)), "tickers": int(x["ticker"].nunique()),
        "months": int(len(by_m)),
        "median": float(r.median()), "mean": float(r.mean()), "hit": float((r > 0).mean()),
        "beat_spy": float((xs > 0).mean()), "med_x_spy": float(xs.median()), "mean_x_spy": float(xs.mean()),
        "med_x_uni": float(xu.median()), "mean_x_uni": float(xu.mean()),
        "clustered_x_uni": float(by_m.mean()), "t_clustered": float(by_m.mean() / se) if se and se > 0 else np.nan,
        "bad_20": float((r < -0.20).mean()),
    }
    if "mae12" in x and h == 12:
        mae = x["mae12"].dropna()
        out["med_mae12"] = float(mae.median()) if len(mae) else np.nan
        out["near_bottom"] = float((mae > -0.10).mean()) if len(mae) else np.nan
        out["deep_further"] = float((mae < -0.25).mean()) if len(mae) else np.nan
    return out


def all_months_baseline(u: Universe, start, end=None) -> dict:
    f = u.all_fwd12.loc[pd.Timestamp(start): pd.Timestamp(end) if end else None]
    v = f.stack().dropna()
    spy = u.spy_fwd[12].reindex(f.index)
    xs = f.sub(spy, axis=0).stack().dropna()
    return {"n": int(len(v)), "median": float(v.median()), "mean": float(v.mean()), "hit": float((v > 0).mean()),
            "beat_spy": float((xs > 0).mean()), "med_x_spy": float(xs.median()), "mean_x_spy": float(xs.mean()),
            "med_x_uni": 0.0, "mean_x_uni": 0.0, "bad_20": float((v < -0.20).mean())}


# ------------------------------------------------------------------ portfolio simulation
def portfolio(u: Universe, ev: pd.DataFrame, hold: int = 12, start="2009-01-31", end=None) -> dict:
    """Equal-weight every open signal, hold `hold` months from the signal month's close, rebalance
    monthly; months with nothing open sit in SPY. Compared with SPY and the equal-weighted universe."""
    A = u.A
    rets = A.pct_change(fill_method=None)
    spy = u.spy["AdjClose"].resample("ME").last().loc[:LAST].pct_change()
    uni = rets.mean(axis=1)
    months = A.loc[pd.Timestamp(start): pd.Timestamp(end) if end else LAST].index[1:]
    port, n_open = [], []
    evs = ev[["ticker", "signal_month"]].to_numpy()
    for m in months:
        prev = m - pd.offsets.MonthEnd(1)
        live = [t for t, s in evs if s <= prev and s > prev - pd.offsets.MonthEnd(hold) and t in rets.columns]
        r = rets.loc[m, live].dropna() if live else pd.Series(dtype=float)
        n_open.append(len(r))
        port.append(float(r.mean()) if len(r) else float(spy.get(m, 0.0)))
    s = pd.Series(port, index=months)

    def stats(x):
        x = x.fillna(0.0)
        eq = (1 + x).cumprod()
        yrs = len(x) / 12
        return {"cagr": float(eq.iloc[-1] ** (1 / yrs) - 1), "vol": float(x.std() * math.sqrt(12)),
                "max_dd": float((eq / eq.cummax() - 1).min()), "total": float(eq.iloc[-1] - 1)}
    return {"hold": hold, "start": months[0].date().isoformat(), "end": months[-1].date().isoformat(),
            "signals": stats(s), "spy": stats(spy.reindex(months)), "uni_ew": stats(uni.reindex(months)),
            "avg_open": float(np.mean(n_open)), "months_empty": float(np.mean([k == 0 for k in n_open])),
            "equity": {"signals": (1 + s).cumprod().round(4).tolist(),
                       "spy": (1 + spy.reindex(months).fillna(0)).cumprod().round(4).tolist(),
                       "uni_ew": (1 + uni.reindex(months).fillna(0)).cumprod().round(4).tolist(),
                       "months": [d.date().isoformat() for d in months]}}


# ------------------------------------------------------------------ main
def pct(x, d=1):
    return "" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:+.{d}f}%"


def pp(x, d=0):
    return "" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:.{d}f}%"


def md_table(rows: list[dict], cols: list[tuple[str, str, callable]]) -> str:
    head = "| " + " | ".join(c[0] for c in cols) + " |\n|" + "|".join("---" for _ in cols) + "|\n"
    body = "".join("| " + " | ".join(str(c[2](r.get(c[1]) if c[1] else r)) for c in cols) + " |\n" for r in rows)
    return head + body


SUMMARY_COLS = [
    ("n", "n", lambda v: v), ("median 12m", "median", pct), ("hit rate", "hit", pp),
    ("beat SPY", "beat_spy", pp), ("median vs SPY", "med_x_spy", pct), ("mean vs universe", "mean_x_uni", pct),
    ("month-clustered vs univ.", "clustered_x_uni", pct), ("t", "t_clustered", lambda v: "" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v:.1f}"),
    ("12m loss > 20%", "bad_20", pp),
]


def main(rebuild: bool = False) -> None:
    u = Universe(rebuild=rebuild)
    res: dict = {"generated": pd.Timestamp.today().date().isoformat(), "last_month": LAST.date().isoformat(),
                 "n_tickers": len(u.daily), "params": sig.DEFAULT.as_dict()}

    # 1. main signal, liquid names
    t0 = time.time()
    ev = liquid(collect(u, sig.detect, p=sig.DEFAULT))
    ev = add_hindsight(ev)
    ev.to_csv(OUT / "events_default.csv", index=False)
    print(f"default events: {len(ev)} ({time.time() - t0:.0f}s)", file=sys.stderr, flush=True)

    # 2. baselines
    base = {}
    for dd in (0.20, 0.25, 0.30):
        b = liquid(collect(u, sig.detect_pullback, fundamentals=True, dd=dd))
        base[f"ATH + overbought, then price -{dd * 100:.0f}% from ATH"] = b
    base["RSI(m) < 35 (old turnaround trigger)"] = liquid(collect(u, sig.detect_rsi35, fundamentals=True))
    for k, b in base.items():
        b.to_csv(OUT / f"events_base_{k.split(',')[0].split(' (')[0].replace(' ', '_').replace('<', 'lt').replace('+', '').replace('%', 'pct')[:40]}.csv", index=False)

    res["periods"] = {}
    for pname, (s, e) in PERIODS.items():
        blk = {"signal (default)": summarize(period(ev, s, e)), "all stock-months": all_months_baseline(u, s, e)}
        for k, b in base.items():
            blk[k] = summarize(period(b, s, e))
        # same, with the quality filter applied to everything with fundamentals
        blk["signal + quality filter"] = summarize(period(f_quality(ev), s, e))
        for k, b in base.items():
            blk[k + " + quality filter"] = summarize(period(f_quality(b), s, e))
        res["periods"][pname] = blk

    # horizons for the default signal
    res["horizons"] = {}
    for pname, (s, e) in PERIODS.items():
        res["horizons"][pname] = {f"{h}m": summarize(period(ev, s, e), h) for h in HORIZONS}
        res["horizons"][pname + " | quality"] = {f"{h}m": summarize(period(f_quality(ev), s, e), h) for h in HORIZONS}

    # 3. fundamentals filters (2009+, the filings era) and last 10/5 years
    res["filters"] = {}
    for pname in ("2009+", "last 10y (Sep 2016+)", "last 5y (Sep 2021+)"):
        s, e = PERIODS[pname]
        res["filters"][pname] = {k: {**summarize(period(fn(ev), s, e)), **{f"h{h}": summarize(period(fn(ev), s, e), h).get("median") for h in (24, 36)}}
                                 for k, fn in FILTERS.items()}

    # 4. hindsight: does "growth ahead" matter, and do point-in-time filters find it?
    e9 = period(ev, "2009-01-01")
    hs = {}
    buckets = [("revenue shrank next year", lambda d: d["fut_rev_g"] < 0),
               ("revenue grew 0-10% next year", lambda d: (d["fut_rev_g"] >= 0) & (d["fut_rev_g"] < 0.10)),
               ("revenue grew >= 10% next year", lambda d: d["fut_rev_g"] >= 0.10),
               ("EPS fell next year", lambda d: d["fut_eps_g"] < 0),
               ("EPS grew next year", lambda d: d["fut_eps_g"] >= 0)]
    for k, fn in buckets:
        hs[k] = summarize(e9[fn(e9)])
    res["hindsight"] = hs
    pred = {}
    for k, fn in FILTERS.items():
        x = fn(e9).dropna(subset=["fut_rev_g"])
        pred[k] = {"n": int(len(x)), "share_rev_grew": float((x["fut_rev_g"] > 0).mean()) if len(x) else np.nan,
                   "share_rev_grew10": float((x["fut_rev_g"] >= 0.10).mean()) if len(x) else np.nan,
                   "share_eps_grew": float((x["fut_eps_g"].dropna() > 0).mean()) if x["fut_eps_g"].notna().any() else np.nan}
    res["hindsight_capture"] = pred

    # 5. parameter sweep (price-only and quality-filtered, 2009+ and last 10y)
    sweep = []
    configs = [sig.Params(ob=ob, drop=dr, window=w) for ob in (65, 70, 75, 80, 85)
               for dr in (0.20, 0.25, 0.28, 0.32, 0.36, 0.40, 0.45) for w in (12, 24)]
    configs += [sig.Params(ob=ob, mode="pts", drop_pts=dp, window=24) for ob in (70, 75, 80) for dp in (15, 20, 25, 30, 35)]
    configs += [sig.Params(ob=70, drop=0.32, window=24, ath_tol=0.05), sig.Params(ob=70, drop=0.32, window=24, min_years=3)]
    for i, p in enumerate(configs, 1):
        e2 = liquid(collect(u, sig.detect, fundamentals=True, p=p))
        row = {"label": p.label(), **p.as_dict()}
        for pname in ("2009+", "last 10y (Sep 2016+)"):
            s, e = PERIODS[pname]
            a = summarize(period(e2, s, e)); q = summarize(period(f_quality(e2), s, e))
            row[pname] = {k: a.get(k) for k in ("n", "median", "hit", "mean_x_uni", "clustered_x_uni", "t_clustered", "med_mae12", "near_bottom")}
            row[pname + " | quality"] = {k: q.get(k) for k in ("n", "median", "hit", "mean_x_uni", "clustered_x_uni", "t_clustered", "med_mae12", "near_bottom")}
        sweep.append(row)
        if i % 10 == 0:
            print(f"  sweep {i}/{len(configs)}", file=sys.stderr, flush=True)
    res["sweep"] = sweep

    # 6. by year and by depth of the drop / peak RSI (default signal, 2009+)
    e9 = e9.copy()
    e9["year"] = e9["signal_month"].dt.year
    res["by_year"] = {int(y): {**summarize(g), "q": summarize(f_quality(g))} for y, g in e9.groupby("year")}
    e9["dd_bucket"] = pd.cut(e9["dd_ath"], [-1, -0.5, -0.4, -0.3, -0.2, -0.1, 0.01],
                             labels=["< -50%", "-50..-40%", "-40..-30%", "-30..-20%", "-20..-10%", "> -10%"])
    res["by_dd"] = {str(k): summarize(g) for k, g in e9.groupby("dd_bucket", observed=True)}
    e9["pk_bucket"] = pd.cut(e9["peak_rsi"], [0, 75, 80, 85, 90, 101], labels=["70-75", "75-80", "80-85", "85-90", "90+"])
    res["by_peak"] = {str(k): summarize(g) for k, g in e9.groupby("pk_bucket", observed=True)}
    e9["m_bucket"] = pd.cut(e9["months_from_ath"], [-1, 3, 6, 12, 25], labels=["0-3", "4-6", "7-12", "13-24"])
    res["by_months_from_ath"] = {str(k): summarize(g) for k, g in e9.groupby("m_bucket", observed=True)}
    res["by_sector"] = {k: summarize(g) for k, g in e9.groupby("sector")}

    # 7. portfolios
    res["portfolio"] = {}
    for name, df in (("signal", ev), ("signal + quality", f_quality(ev)), ("signal + quality + cheap", f_quality_val(ev))):
        for hold in (12, 24):
            for st in ("2009-01-31", "2016-08-31", "2021-08-31"):
                res["portfolio"][f"{name} | hold {hold}m | from {st[:7]}"] = portfolio(u, df, hold, st)

    (OUT / "study.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    print(f"wrote {OUT / 'study.json'}", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main(rebuild="--rebuild" in sys.argv)
