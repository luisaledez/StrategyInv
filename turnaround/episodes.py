"""Historical study of monthly-RSI distress episodes.

Tests the hypothesis behind the screen: does a stock that prints a monthly
RSI(14) below the threshold go on to deliver attractive forward returns?

For every ticker in the universe, consecutive oversold months are grouped into
ONE episode. Three entry rules are measured for each episode:

  first_oversold   buy at the close of the first month RSI < threshold
                   (what the raw screen would do)
  rsi_recovery     buy at the close of the first month RSI is back >= exit
                   level after the episode (confirmation rule; default 35)
  rsi_recovery40   same, but require RSI >= 40

and, as a control, the unconditional forward return of the same stocks over
all months ("baseline"). Returns use dividend-adjusted closes (total return),
compared with SPY and the GICS sector ETF over identical windows.

Only price information available at the decision date is used. Two caveats
you cannot fix from Yahoo alone, stated in the output:
  * survivorship bias — the universe is today's index constituents, so names
    that failed and were delisted are missing. Add known casualties with
    --extra to reduce this; Yahoo still serves some delisted histories.
  * episodes cluster in market-wide sell-offs (2020, 2022), so the effective
    sample is smaller than the episode count.

Usage:  python episodes.py                      # sp500+sp400, 15y history
        python episodes.py --threshold 30 --exit 40
        python episodes.py --tickers ENPH,INTC,NKE
        python episodes.py --extra SVB,FRC,BBBY  # add delisted names
Outputs: output/episodes.csv, output/episodes_summary.csv, output/episodes_summary.md
"""
from __future__ import annotations

import argparse
import math
import sys
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


def monthly_adj(daily: pd.DataFrame, as_of=None) -> pd.DataFrame:
    m = ind.monthly_bars(daily, as_of=as_of)
    return m


def forward_stats(adj: np.ndarray, i: int, horizons: list[int], bench: dict[str, np.ndarray],
                  max_h: int = 36) -> dict:
    """Forward total returns from month index i, plus drawdown and recovery.
    `adj` and every `bench` array are pre-aligned to the same monthly index."""
    out: dict = {}
    entry = float(adj[i])
    n = len(adj)
    for h in horizons:
        j = i + h
        if j < n:
            out[f"ret_{h}m"] = float(adj[j]) / entry - 1.0
            for name, b in bench.items():
                if not (math.isnan(b[i]) or math.isnan(b[j])):
                    out[f"{name}_{h}m"] = float(b[j]) / float(b[i]) - 1.0
                    out[f"excess_{name}_{h}m"] = out[f"ret_{h}m"] - out[f"{name}_{h}m"]
        else:
            out[f"ret_{h}m"] = math.nan
    path = adj[i + 1: i + 1 + max_h]
    if len(path):
        rel = path / entry - 1.0
        out["max_dd_from_entry_36m"] = float(rel.min())
        out["months_to_low"] = int(rel.argmin() + 1)
        rec = np.where(rel >= 0)[0]
        out["months_to_recover"] = int(rec[0] + 1) if len(rec) else math.nan
        out["path_months"] = int(len(path))
    return out


def run(args) -> tuple[pd.DataFrame, pd.DataFrame]:
    horizons = [int(h) for h in args.horizons.split(",")]
    if args.tickers:
        tickers = [uni_mod.yahoo_symbol(t) for t in args.tickers.split(",") if t.strip()]
        uni = uni_mod.load(custom=tickers)
        uni = uni[uni["ticker"].isin(tickers)]
    else:
        extra = [t for t in args.extra.split(",") if t.strip()]
        uni = uni_mod.load(tuple(args.universe.split(",")), custom=extra)
    meta = uni.set_index("ticker")
    etfs = sorted(set(meta["sector_etf"])) + ["SPY"]
    px = prices.load_many(list(meta.index) + etfs)
    bench_m = {e: monthly_adj(px[e])["AdjClose"] for e in etfs if e in px}

    rows = []
    base = []  # baseline: (ticker, forward returns for every month)
    for t in meta.index:
        d = px.get(t)
        if d is None or len(d) < 300:
            continue
        m = monthly_adj(d)
        if len(m) < args.rsi_period + 12:
            continue
        rsi = ind.wilder_rsi(m["Close"], args.rsi_period)
        adj = m["AdjClose"]
        sector_etf = meta.at[t, "sector_etf"] if "sector_etf" in meta else "SPY"
        bench = {"spy": bench_m["SPY"].reindex(adj.index).to_numpy(dtype=float)}
        if sector_etf in bench_m:
            bench["sector"] = bench_m[sector_etf].reindex(adj.index).to_numpy(dtype=float)
        adj_arr = adj.to_numpy(dtype=float)
        # trailing 5y drawdown at each month (monthly closes)
        dd5 = m["Close"] / m["Close"].rolling(60, min_periods=12).max() - 1.0

        # ---- baseline: every month with a valid RSI
        valid = np.where(rsi.notna().values)[0]
        for i in valid[::args.baseline_step]:
            fs = forward_stats(adj_arr, i, horizons, bench)
            base.append({"ticker": t, "date": adj.index[i]} | fs)

        # ---- episodes
        for ep in ind.rsi_episodes(rsi, args.threshold):
            i0 = adj.index.get_loc(ep["start"])
            rec = {
                "ticker": t, "sector": meta.at[t, "sector"] if "sector" in meta else "",
                "episode_start": ep["start"].date(), "episode_end": ep["end"].date(),
                "episode_months": ep["months"], "min_rsi": round(ep["min_rsi"], 1),
                "rsi_at_entry": round(float(rsi.iloc[i0]), 1),
                "dd5y_at_entry": float(dd5.iloc[i0]) if not math.isnan(dd5.iloc[i0]) else math.nan,
                "still_active": ep["exit"] is None,
            }
            rows.append(rec | {"rule": "first_oversold", "entry_date": adj.index[i0].date()}
                        | forward_stats(adj_arr, i0, horizons, bench))
            # confirmation entries: first month after start with RSI >= level
            for rule, level in (("rsi_recovery", args.exit), ("rsi_recovery40", 40.0)):
                later = rsi.iloc[i0 + 1:]
                hit = later[later >= level]
                if len(hit):
                    ic = adj.index.get_loc(hit.index[0])
                    rows.append(rec | {"rule": rule, "entry_date": adj.index[ic].date(),
                                       "months_waited": ic - i0}
                                | forward_stats(adj_arr, ic, horizons, bench))
    eps = pd.DataFrame(rows)
    basedf = pd.DataFrame(base)
    return eps, basedf


def summarise(eps: pd.DataFrame, basedf: pd.DataFrame, horizons: list[int]) -> pd.DataFrame:
    out = []

    def block(label: str, df: pd.DataFrame):
        for h in horizons:
            col = f"ret_{h}m"
            if col not in df:
                continue
            s = df[col].dropna()
            if len(s) == 0:
                continue
            ex = df.get(f"excess_spy_{h}m", pd.Series(dtype=float)).dropna()
            exs = df.get(f"excess_sector_{h}m", pd.Series(dtype=float)).dropna()
            row = {
                "rule": label, "horizon_m": h, "n": int(len(s)),
                "median_ret": s.median(), "mean_ret": s.mean(), "pct_positive": (s > 0).mean(),
                "p25_ret": s.quantile(0.25), "p75_ret": s.quantile(0.75),
                "median_excess_spy": ex.median() if len(ex) else math.nan,
                "pct_beat_spy": (ex > 0).mean() if len(ex) else math.nan,
                "median_excess_sector": exs.median() if len(exs) else math.nan,
                "pct_beat_sector": (exs > 0).mean() if len(exs) else math.nan,
            }
            if h == max(horizons) and "max_dd_from_entry_36m" in df:
                full = df[df["path_months"] >= 36] if "path_months" in df else df
                row["median_max_dd_36m"] = full["max_dd_from_entry_36m"].median()
                row["pct_recovered_36m"] = full["months_to_recover"].notna().mean() if len(full) else math.nan
                row["median_months_to_recover"] = full["months_to_recover"].median()
            out.append(row)

    for rule in ["first_oversold", "rsi_recovery", "rsi_recovery40"]:
        sub = eps[eps["rule"] == rule]
        block(rule, sub)
        deep = sub[sub["dd5y_at_entry"] <= -0.40]
        block(f"{rule} | dd>40%", deep)
        shallow = sub[sub["dd5y_at_entry"] > -0.40]
        block(f"{rule} | dd<40%", shallow)
    block("baseline_all_months", basedf)
    return pd.DataFrame(out)


def write_md(summary: pd.DataFrame, eps: pd.DataFrame, args) -> Path:
    p = OUT / "episodes_summary.md"
    horizons = [int(h) for h in args.horizons.split(",")]
    n_ep = int((eps["rule"] == "first_oversold").sum())
    n_tk = eps["ticker"].nunique()
    yrs = eps[eps["rule"] == "first_oversold"]["episode_start"].map(lambda d: d.year).value_counts().sort_index()
    L = [f"# Monthly-RSI distress episodes — study", "",
         f"Universe: {args.universe if not args.tickers else args.tickers}"
         + (f" + {args.extra}" if args.extra else "") + f". Threshold RSI({args.rsi_period}) < {args.threshold}; "
         f"confirmation exit level {args.exit}. {n_ep} episodes across {n_tk} tickers, 15 years of monthly closes.",
         "",
         "Forward returns are total returns (dividend-adjusted) from the month-end close of the entry month. "
         "`excess` = stock return minus SPY (or sector ETF) over the same window. `max dd` = worst point "
         "relative to the entry price within 36 months; `recovered` = price back at/above entry within 36 months.",
         "",
         "**Caveats.** (1) Survivorship: the universe is today's constituents; delisted failures are absent, "
         "which flatters every row. (2) Episodes cluster in 2020 and 2022, so independent observations are fewer "
         "than N. (3) No fundamentals are applied here; this is the 'RSI alone' arm of the comparison. "
         "The 'RSI + survival + valuation' arm needs point-in-time financials that Yahoo does not provide.",
         "", "Episodes per start year: " + ", ".join(f"{y}: {c}" for y, c in yrs.items()), ""]

    def fmt(v, kind):
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return ""
        if kind == "pct":
            return f"{v * 100:+.1f}%"
        if kind == "share":
            return f"{v * 100:.0f}%"
        if kind == "int":
            return f"{v:.0f}"
        return str(v)

    hdr = ["Rule", "H", "N", "Median", "Mean", "P25", "P75", "% > 0", "Med. excess SPY", "% beat SPY",
           "Med. excess sector", "% beat sector", "Med. max DD 36m", "% recovered 36m", "Med. months to recover"]
    L.append("| " + " | ".join(hdr) + " |")
    L.append("|" + "---|" * len(hdr))
    for _, r in summary.iterrows():
        L.append("| " + " | ".join([
            r["rule"], f"{int(r['horizon_m'])}m", str(int(r["n"])),
            fmt(r["median_ret"], "pct"), fmt(r["mean_ret"], "pct"), fmt(r["p25_ret"], "pct"), fmt(r["p75_ret"], "pct"),
            fmt(r["pct_positive"], "share"), fmt(r["median_excess_spy"], "pct"), fmt(r["pct_beat_spy"], "share"),
            fmt(r["median_excess_sector"], "pct"), fmt(r["pct_beat_sector"], "share"),
            fmt(r.get("median_max_dd_36m"), "pct"), fmt(r.get("pct_recovered_36m"), "share"),
            fmt(r.get("median_months_to_recover"), "int"),
        ]) + " |")
    L += ["", "Rules: `first_oversold` = buy the close of the first month RSI < threshold. "
          "`rsi_recovery` = wait for the first monthly close with RSI back above the exit level. "
          "`rsi_recovery40` = wait for RSI ≥ 40. `dd>40%` rows restrict to episodes where the stock was already "
          "≥ 40% below its trailing 5-year high at entry. `baseline_all_months` = unconditional forward returns "
          "of the same stocks sampled every month, the control the episode rows must beat.", ""]
    p.write_text("\n".join(L), encoding="utf-8")
    return p


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--universe", default="sp500,sp400")
    ap.add_argument("--tickers", default="")
    ap.add_argument("--extra", default="", help="add tickers (e.g. delisted names) to the universe")
    ap.add_argument("--threshold", type=float, default=35.0)
    ap.add_argument("--exit", type=float, default=35.0, help="RSI level for the confirmation entry")
    ap.add_argument("--rsi-period", type=int, default=14)
    ap.add_argument("--horizons", default="6,12,24,36")
    ap.add_argument("--baseline-step", type=int, default=1, help="sample baseline every k months")
    args = ap.parse_args(argv)
    horizons = [int(h) for h in args.horizons.split(",")]

    eps, basedf = run(args)
    if eps.empty:
        print("no episodes found", file=sys.stderr)
        return
    eps.to_csv(OUT / "episodes.csv", index=False)
    summary = summarise(eps, basedf, horizons)
    summary.to_csv(OUT / "episodes_summary.csv", index=False)
    md = write_md(summary, eps, args)

    show = summary[["rule", "horizon_m", "n", "median_ret", "mean_ret", "pct_positive",
                     "median_excess_spy", "pct_beat_spy", "median_max_dd_36m", "pct_recovered_36m"]].copy()
    for c in ["median_ret", "mean_ret", "median_excess_spy", "median_max_dd_36m"]:
        show[c] = show[c].map(lambda v: "" if pd.isna(v) else f"{v * 100:+.1f}%")
    for c in ["pct_positive", "pct_beat_spy", "pct_recovered_36m"]:
        show[c] = show[c].map(lambda v: "" if pd.isna(v) else f"{v * 100:.0f}%")
    with pd.option_context("display.width", 200, "display.max_rows", 500):
        print(show.to_string(index=False))
    print(f"\n{int((eps['rule'] == 'first_oversold').sum())} episodes, {eps['ticker'].nunique()} tickers")
    print(f"wrote {OUT / 'episodes.csv'}, {OUT / 'episodes_summary.csv'}, {md}")


if __name__ == "__main__":
    main()
