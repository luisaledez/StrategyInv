"""Today's `both_opval` list with the extra diagnostics used in the live reports, plus the same
screen on the last completed monthly candle (sensitivity to the next official snapshot) and the
12-month forward base rates of past `both_opval` top-10 picks.

    python live_v3.py            # ~2 min, writes output/live_both_opval_<date>.csv / .json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import screen_v3 as s3  # noqa: E402
from screen_v3 import data, screen  # noqa: E402

VARIANT = "both_opval"


def enrich(rows: list[dict], tables: dict[str, pd.DataFrame], month_end: pd.Timestamp) -> list[dict]:
    out = []
    for r in rows:
        tbl = tables[r["ticker"]]
        i = tbl.index.get_loc(month_end)
        eps_1y = tbl["eps_ttm"].iloc[i - 12] if i >= 12 else np.nan
        rsi6 = tbl["rsi"].iloc[max(0, i - 5): i + 1].min()
        ebitda = tbl["ebitda_ttm"].iloc[i]; debt = tbl["debt"].iloc[i]; cash = tbl["cash"].iloc[i]
        nd = (0 if np.isnan(debt) else debt) - (0 if np.isnan(cash) else cash)
        d = dict(r)
        d["eps_1y"] = s3._f(eps_1y)
        d["eps_chg_1y"] = s3._f(r["eps_ttm"] / eps_1y - 1) if eps_1y and eps_1y > 0 else None
        d["rsi_min6"] = s3._f(rsi6)
        d["net_debt"] = s3._f(nd)
        d["nd_ebitda"] = s3._f(nd / ebitda) if ebitda and ebitda > 0 else None
        d["eps_guidecut_trigger"] = round(0.85 * r["eps_ttm"], 3) if r["eps_ttm"] else None
        d["trim_price"] = round(1.5 * r["close"], 2)
        # trailing EPS path over the last 6 quarters (point-in-time), latest last
        q = screen.load_edgar(r["ticker"])
        by, ends = s3._first_published(q, "eps_ttm")
        chain = s3._chain(by, ends, r["q_end"], month_end.date().isoformat(), 5)
        d["eps_path"] = [round(x, 2) for x in chain[::-1]]
        out.append(d)
    return out


def forward_base_rates(tables: dict[str, pd.DataFrame]) -> dict:
    snaps = json.loads((s3.OUT / f"snapshots_{VARIANT}.json").read_text(encoding="utf-8"))
    spy = data.load_prices("SPY")["Close"]
    recs = []
    for s in snaps:
        snap = pd.Timestamp(s["date"])
        if snap < pd.Timestamp("2009-01-01") or snap > pd.Timestamp("2025-09-30"):
            continue
        for r in s["top20"]:
            px = data.load_prices(r["ticker"])
            if px is None:
                continue
            c = px["Close"]
            after = c.index[c.index > snap]
            if len(after) == 0:
                continue
            t0 = after[0]; t1 = t0 + pd.DateOffset(months=12)
            c1 = c[c.index <= t1]
            if c1.index[-1] < t1 - pd.Timedelta(days=7):
                continue
            ret = c1.iloc[-1] / c.loc[t0] - 1
            spy_ret = spy[spy.index <= t1].iloc[-1] / spy[spy.index >= t0].iloc[0] - 1
            path = c[(c.index >= t0) & (c.index <= t1)]
            mdd = (path / path.cummax() - 1).min()
            recs.append({"ticker": r["ticker"], "date": s["date"], "top10": "value_rank" in r,
                         "val": r.get("val_pct_op"), "dd5": r["dd5"], "ret12": ret, "spy12": spy_ret, "mdd": mdd})
    df = pd.DataFrame(recs)

    def stats(x: pd.DataFrame) -> dict:
        return {"n": int(len(x)), "mean": round(x["ret12"].mean(), 3), "median": round(x["ret12"].median(), 3),
                "win": round((x["ret12"] > 0).mean(), 3), "beat_spy": round((x["ret12"] > x["spy12"]).mean(), 3),
                "p10": round(x["ret12"].quantile(0.1), 3), "p90": round(x["ret12"].quantile(0.9), 3),
                "median_mdd": round(x["mdd"].median(), 3)}
    top = df[df["top10"]]
    return {
        "top10": stats(top), "bench_11_20": stats(df[~df["top10"]]),
        "top10_val_le_0.10": stats(top[top["val"] <= 0.10]),
        "top10_val_0.10_0.25": stats(top[(top["val"] > 0.10) & (top["val"] <= 0.25)]),
        "top10_val_gt_0.25": stats(top[top["val"] > 0.25]),
        "top10_dd5_worse_than_-60%": stats(top[top["dd5"] <= -0.60]),
        "top10_dd5_-40_to_-60%": stats(top[(top["dd5"] > -0.60) & (top["dd5"] <= -0.40)]),
        "top10_dd5_better_than_-40%": stats(top[top["dd5"] > -0.40]),
    }


def main() -> None:
    meta = data.universe_meta()
    tables = s3.build_tables(list(meta.index))
    today = pd.Timestamp.today().normalize()
    cur = s3.screen_at(tables, meta, today, VARIANT)
    me = pd.Timestamp(cur["month_end"])
    cur["top20"] = enrich(cur["top20"], tables, me)
    cur["top10"] = [r for r in cur["top20"] if "value_rank" in r]
    cur["top10"].sort(key=lambda r: r["value_rank"])
    # same screen on the last completed monthly candle
    prev_snap = me.to_period("M").to_timestamp(how="start")  # first day of the current month
    prev = s3.screen_at(tables, meta, prev_snap, VARIANT)
    cur["prev_candle"] = {"month_end": prev["month_end"],
                          "top10": [r["ticker"] for r in sorted(prev["top10"], key=lambda r: r["value_rank"])],
                          "top20": [r["ticker"] for r in prev["top20"]]}
    # what the guards removed from today's organic-eligible set, and the v2-style (P/E) ranking of the same 20
    ref = s3.screen_at(tables, meta, today, "ref")
    cur["ref_top10"] = [r["ticker"] for r in sorted(ref["top10"], key=lambda r: r["value_rank"])]
    cur["removed_by_guards"] = [{"ticker": r["ticker"], "rev_yoy": r["rev_yoy"], "oneoff": r["oneoff"], "acq": r["acq"]}
                                for r in ref["top20"] if r["oneoff"] or r["acq"]]
    cur["base_rates_12m_2009_2025"] = forward_base_rates(tables)
    tag = today.date().isoformat()
    (s3.OUT / f"live_{VARIANT}_{tag}.json").write_text(json.dumps(cur, indent=1), encoding="utf-8")
    pd.DataFrame(cur["top20"]).to_csv(s3.OUT / f"live_{VARIANT}_{tag}.csv", index=False)
    print(json.dumps({k: v for k, v in cur.items() if k not in ("top20", "top10")}, indent=1))
    cols = ["value_rank", "growth_rank", "ticker", "rev_yoy", "val_pct_op", "ps_pct", "ev_ebitda_pct", "ev_ebit_pct",
            "close", "rsi_m", "rsi_min6", "dd5", "eps_ttm", "eps_1y", "eps_chg_1y", "nd_ebitda", "eps_path"]
    pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)
    print(pd.DataFrame(cur["top20"])[cols].round(3).to_string())


if __name__ == "__main__":
    main()
