"""Post-entry analysis of every base-scenario position: what the losers looked like at
entry, how they evolved (price + point-in-time fundamentals), and which simple sell
rules would have helped across ALL positions (not only the losers).

    python post_entry.py            # -> output/post_entry_positions.csv, post_entry_rules.csv, tables on stdout

See ../research_notes/turnaround_worst_open.md for the write-up."""
import sys
from pathlib import Path
import numpy as np, pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "turnaround"))
import data, screen  # noqa

OUTDIR = Path(sys.argv[1]) if len(sys.argv) > 1 else data.OUT
END = pd.Timestamp("2026-08-31")
LOSERS = ["TTD", "LULU", "TAP", "KRC", "RYN", "MOS", "BAH", "MUR", "GIS", "LYB"]

trades = pd.read_csv(HERE / "output/base_trades.csv", parse_dates=["date"]).sort_values(["date", "ticker"])
snaps = pd.read_csv(HERE / "output/snapshots.csv", parse_dates=["date"])
snaps = snaps[snaps.in_top10]

# ---- position episodes (a ticker can be bought again after a full exit)
episodes = []
for t, g in trades.groupby("ticker"):
    sh = 0.0; ep = None
    for _, r in g.sort_values("date").iterrows():
        if r.side == "BUY":
            if sh < 1e-6:
                ep = {"ticker": t, "entry": r.date, "price": r.price, "amount": r.amount}
                episodes.append(ep)
            sh += r.shares
        else:
            sh -= r.shares
            if sh < 1e-6 and ep is not None:
                ep["exit"] = r.date; ep["exit_reason"] = r.reason; ep = None
for ep in episodes:
    ep.setdefault("exit", END); ep.setdefault("exit_reason", "open")

tables = {}; dailies = {}
def get(t):
    if t not in tables:
        d = data.load_prices(t); dailies[t] = d
        tables[t] = screen.ticker_table(t, d, screen.load_edgar(t))
    return tables[t], dailies[t]

def adj_at(d, ts):
    s = d["AdjClose"]; i = s.index.searchsorted(ts, side="right") - 1
    return float(s.iloc[max(i, 0)])
def close_at(d, ts):
    s = d["Close"]; i = s.index.searchsorted(ts, side="right") - 1
    return float(s.iloc[max(i, 0)])

RULES = {
    "stop20": lambda m: m.pr <= -0.20,
    "stop30": lambda m: m.pr <= -0.30,
    "stop40": lambda m: m.pr <= -0.40,
    "trail30": lambda m: m.dd_peak <= -0.30,
    "time12_uw": lambda m: (m.months >= 12) & (m.pr < 0),
    "time24_uw": lambda m: (m.months >= 24) & (m.pr < 0),
    "eps_dn30": lambda m: m.eps_chg <= -0.30,
    "eps_dn50": lambda m: m.eps_chg <= -0.50,
    "rev_neg": lambda m: m.rev_yoy < 0,
    "rev_neg_uw": lambda m: (m.rev_yoy < 0) & (m.pr < 0),
    "eps_dn30_uw": lambda m: (m.eps_chg <= -0.30) & (m.pr < 0),
    "eps_dn20_stop20": lambda m: (m.eps_chg <= -0.20) & (m.pr <= -0.20),
    "rsi_lt30": lambda m: m.rsi < 30,
    "ma10_uw2": lambda m: m.below_ma10_2 & (m.pr < 0),
    "newlow5y": lambda m: m.newlow,
    "newlow5y_uw20": lambda m: m.newlow & (m.pr <= -0.20),
}

rows = []; rule_rows = []
for ep in episodes:
    t = ep["ticker"]; tbl, d = get(t)
    if tbl is None: continue
    entry, exit_ = ep["entry"], ep["exit"]
    me0 = (entry - pd.Timedelta(days=1)).to_period("M").to_timestamp(how="end").normalize()
    if me0 not in tbl.index: continue
    e = tbl.loc[me0]
    m = tbl.loc[(tbl.index > me0) & (tbl.index <= exit_)].copy()
    if len(m) == 0: continue
    p0 = ep["price"]; a0 = adj_at(d, entry)
    m["pr"] = m["close"] / p0 - 1.0
    m["peak"] = np.maximum.accumulate(np.r_[p0, m["close"].to_numpy()])[1:]
    m["dd_peak"] = m["close"] / m["peak"] - 1.0
    m["months"] = np.arange(1, len(m) + 1)
    eps0 = e["eps_ttm"] if e["eps_ttm"] and e["eps_ttm"] > 0 else np.nan
    m["eps_chg"] = m["eps_ttm"] / eps0 - 1.0
    ma10 = tbl["close"].rolling(10).mean().reindex(m.index)
    below = (m["close"] < ma10)
    m["below_ma10_2"] = below & below.shift(1, fill_value=False)
    low60 = tbl["close"].rolling(60, min_periods=12).min().reindex(m.index)
    m["newlow"] = m["close"] <= low60 + 1e-9
    m["adj"] = [adj_at(d, ts) for ts in m.index]
    m["tr"] = m["adj"] / a0 - 1.0
    hold_tr = adj_at(d, exit_) / a0 - 1.0
    hold_pr = close_at(d, exit_) / p0 - 1.0

    def at_months(col, k):
        return float(m[col].iloc[k - 1]) if len(m) >= k else np.nan
    def first_month(mask):
        idx = np.flatnonzero(mask.to_numpy())
        return int(idx[0]) + 1 if len(idx) else None

    snap = snaps[(snaps.ticker == t) & (snaps.date <= entry) & (snaps.date >= entry - pd.Timedelta(days=7))]
    s = snap.iloc[-1] if len(snap) else None
    row = {
        "ticker": t, "entry": entry.date(), "exit": exit_.date(), "reason": ep["exit_reason"],
        "amount": ep["amount"], "months": len(m), "hold_pr": hold_pr, "hold_tr": hold_tr,
        "sector": s.sector if s is not None else "", "rsi_m": e["rsi"], "dd5": e["dd5"],
        "rev_yoy0": e["rev_yoy"], "val_pct0": e["val_pct"], "pe0": e["pe"], "ps0": e["ps"], "ev_ebitda0": e["ev_ebitda"],
        "growth_rank": s.growth_rank if s is not None else np.nan,
        "maxdd_cost": float(m["pr"].min()), "max_gain": float(m["pr"].max()),
        "m_first_-20": first_month(m["pr"] <= -0.20), "m_first_-30": first_month(m["pr"] <= -0.30),
        "pct_months_uw": float((m["pr"] < 0).mean()),
        "pr_6m": at_months("pr", 6), "pr_12m": at_months("pr", 12), "pr_24m": at_months("pr", 24),
        "rev_yoy_12m": at_months("rev_yoy", 12), "rev_yoy_24m": at_months("rev_yoy", 24),
        "eps_chg_12m": at_months("eps_chg", 12), "eps_chg_24m": at_months("eps_chg", 24),
        "eps_chg_min": float(m["eps_chg"].min()) if m["eps_chg"].notna().any() else np.nan,
        "m_first_eps-30": first_month(m["eps_chg"] <= -0.30),
        "m_first_rev_neg": first_month(m["rev_yoy"] < 0),
        "m_first_newlow5y": first_month(m["newlow"]),
        "rsi_min": float(m["rsi"].min()),
        "shares_chg_24m": at_months("shares", 24) / e["shares"] - 1 if e["shares"] else np.nan,
    }
    rows.append(row)
    for name, f in RULES.items():
        k = first_month(f(m).fillna(False))
        if k is None:
            rule_rows.append({"ticker": t, "entry": entry.date(), "rule": name, "fired": False, "month": None,
                              "rule_tr": hold_tr, "hold_tr": hold_tr, "amount": ep["amount"], "exit_date": exit_, "horizon": exit_})
        else:
            rule_rows.append({"ticker": t, "entry": entry.date(), "rule": name, "fired": True, "month": k,
                              "rule_tr": float(m["tr"].iloc[k - 1]), "hold_tr": hold_tr, "amount": ep["amount"],
                              "exit_date": m.index[k - 1], "horizon": exit_})
    if t in LOSERS and ep["exit_reason"] == "open":
        tl = m[["pr", "rev_yoy", "eps_chg", "rsi"]].iloc[[i for i in range(len(m)) if (i + 1) % 3 == 0 and i < 36]]
        tl.index = [f"m{i+1}" for i in range(len(m)) if (i + 1) % 3 == 0 and i < 36]
        print(f"--- {t} timeline (entry {entry.date()}, eps_ttm at entry {eps0:.2f}, rev_yoy at entry {e['rev_yoy']:.2f})")
        print(tl.T.to_string(float_format=lambda x: f"{x:.2f}"))

spy = data.load_prices("SPY")["AdjClose"]
def spy_tr(a, b):
    ia = spy.index.searchsorted(a, side="right") - 1; ib = spy.index.searchsorted(b, side="right") - 1
    return float(spy.iloc[ib] / spy.iloc[ia] - 1.0)

df = pd.DataFrame(rows); df["is_loser"] = df.ticker.isin(LOSERS) & (df.reason == "open")
df.to_csv(OUTDIR / "post_entry_positions.csv", index=False)
rr = pd.DataFrame(rule_rows)
loser_keys = set(zip(df[df.is_loser].ticker, df[df.is_loser].entry))
rr["is_loser"] = [(a, b) in loser_keys for a, b in zip(rr.ticker, rr.entry)]
rr["delta"] = rr.rule_tr - rr.hold_tr; rr["delta_usd"] = rr.delta * rr.amount
# fairer: proceeds of a rule sale go into SPY until the position's horizon
rr["rule_tr_spy"] = [(1 + r.rule_tr) * (1 + spy_tr(r.exit_date, r.horizon)) - 1 if r.fired else r.hold_tr for r in rr.itertuples()]
rr["delta_spy"] = rr.rule_tr_spy - rr.hold_tr; rr["delta_spy_usd"] = rr.delta_spy * rr.amount
rr.to_csv(OUTDIR / "post_entry_rules.csv", index=False)

print("\n=== entry-time buckets: average / median hold total return, n, losers in bucket ===")
def bucket(lab, mask):
    a = df[mask]
    print(f"  {lab:40s} n={len(a):2d} avg={a.hold_tr.mean():+.2f} med={a.hold_tr.median():+.2f} <0:{int((a.hold_tr<0).sum()):2d} losers={int(a.is_loser.sum())}")
bucket("all", df.hold_tr.notna())
bucket("rev_yoy0 >= 0.30", df.rev_yoy0 >= 0.30); bucket("rev_yoy0 < 0.30", df.rev_yoy0 < 0.30)
bucket("rev_yoy0 >= 1.0 or < 0 (suspect)", (df.rev_yoy0 >= 1.0) | (df.rev_yoy0 < 0))
bucket("pe0 < 8", df.pe0 < 8); bucket("pe0 8-15", (df.pe0 >= 8) & (df.pe0 < 15)); bucket("pe0 >= 15", df.pe0 >= 15)
bucket("Materials/Energy", df.sector.isin(["Materials", "Energy"])); bucket("Real Estate", df.sector == "Real Estate")
bucket("Consumer Staples", df.sector == "Consumer Staples"); bucket("other sectors", ~df.sector.isin(["Materials", "Energy", "Real Estate", "Consumer Staples"]))
bucket("rsi_m < 40", df.rsi_m < 40); bucket("rsi_m >= 40", df.rsi_m >= 40)
bucket("dd5 <= -0.45", df.dd5 <= -0.45); bucket("dd5 > -0.45", df.dd5 > -0.45)
bucket("growth_rank <= 5", df.growth_rank <= 5); bucket("growth_rank > 5", df.growth_rank > 5)
bucket("entry >= 2021", pd.to_datetime(df.entry) >= "2021-01-01"); bucket("entry < 2021", pd.to_datetime(df.entry) < "2021-01-01")
print("\n  sector table:"); print(df.groupby("sector").agg(n=("hold_tr", "size"), avg=("hold_tr", "mean"), med=("hold_tr", "median"), neg=("hold_tr", lambda s: int((s < 0).sum())), losers=("is_loser", "sum")).sort_values("avg").to_string())

pd.set_option("display.width", 300); pd.set_option("display.max_columns", 60); pd.set_option("display.float_format", lambda x: f"{x:,.2f}")
print("=== LOSERS at entry and after ===")
cols = ["ticker","entry","sector","rsi_m","dd5","rev_yoy0","val_pct0","pe0","growth_rank","hold_pr","hold_tr","maxdd_cost","max_gain","m_first_-20","m_first_-30","pct_months_uw","pr_6m","pr_12m","rev_yoy_12m","rev_yoy_24m","eps_chg_12m","eps_chg_24m","eps_chg_min","m_first_eps-30","m_first_rev_neg","m_first_newlow5y","rsi_min"]
print(df[df.is_loser][cols].to_string(index=False))
print("\n=== ALL positions: losers vs the rest (medians) ===")
num = df.select_dtypes("number").columns
print(df.groupby("is_loser")[num].median().T.to_string())
print("\n=== quick tests: how many of the losers vs others ... ===")
for lab, mask in [("rev_yoy_12m < 0", df.rev_yoy_12m < 0), ("eps_chg_12m <= -0.20", df.eps_chg_12m <= -0.20),
                  ("pr_6m <= -0.20", df.pr_6m <= -0.20), ("pr_12m <= -0.20", df.pr_12m <= -0.20),
                  ("rev_yoy0 >= 0.30", df.rev_yoy0 >= 0.30), ("dd5 <= -0.40", df.dd5 <= -0.40),
                  ("new 5y low within 12m", df.m_first_newlow5y <= 12)]:
    a = df[df.is_loser]; b = df[~df.is_loser]
    print(f"  {lab:28s} losers {int(mask[a.index].sum())}/{len(a)}   others {int(mask[b.index].sum())}/{len(b)}")
print("\n=== sell rules across ALL episodes (total return incl. dividends; hold = to actual exit or 2026-08-31) ===")
g = rr.groupby("rule")
summ = pd.DataFrame({
    "fired": g.fired.sum(), "n": g.size(),
    "fired_on_losers": rr[rr.is_loser].groupby("rule").fired.sum(),
    "avg_hold_tr": g.hold_tr.mean(), "avg_rule_tr": g.rule_tr.mean(),
    "median_delta_when_fired": rr[rr.fired].groupby("rule").delta.median(),
    "helped(>+10pt)": rr[rr.delta > 0.10].groupby("rule").size(),
    "hurt(<-10pt)": rr[rr.delta < -0.10].groupby("rule").size(),
    "sum_delta_usd": g.delta_usd.sum(),
    "sum_delta_usd_losers": rr[rr.is_loser].groupby("rule").delta_usd.sum(),
    "avg_rule_tr_spy": g.rule_tr_spy.mean(),
    "helped_spy(>+10pt)": rr[rr.delta_spy > 0.10].groupby("rule").size(),
    "hurt_spy(<-10pt)": rr[rr.delta_spy < -0.10].groupby("rule").size(),
    "sum_delta_spy_usd": g.delta_spy_usd.sum(),
    "sum_delta_spy_usd_losers": rr[rr.is_loser].groupby("rule").delta_spy_usd.sum(),
}).fillna(0).sort_values("sum_delta_spy_usd", ascending=False)
print(summ.to_string())
print("\n=== per-loser: month each rule fired ===")
print(rr[rr.is_loser].pivot(index="ticker", columns="rule", values="month").to_string())
print("\n=== per-loser: total return at rule exit (hold_tr in last col) ===")
p2 = rr[rr.is_loser].pivot(index="ticker", columns="rule", values="rule_tr")
p2["HOLD"] = rr[rr.is_loser].groupby("ticker").hold_tr.first()
print(p2.to_string())
