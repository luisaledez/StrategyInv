"""Condense the study outputs into output/web_summary.json for the web app's /os2 page.

Reads output/study.json, output/timing.json and output/variants.json (run study.py, timing.py and
variants.py first) and keeps only what the page shows, so the deployed bundle does not need the
event files.

    python export_web.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "output"

TIERS = [  # (key in variants.json, tier label, description)
    ("leader + RSI<35", "A ★", "Former overbought-ATH leader (last 36 months), monthly RSI < 35"),
    ("leader + RSI<40", "A", "Former overbought-ATH leader (last 36 months), monthly RSI < 40"),
    ("rsi-32% + price-40%", "B", "RSI ≤ 68% of the 24-month peak and price ≥ 40% below ATH"),
    ("rsi-32% + price-30%", "", "RSI ≤ 68% of the 24-month peak and price ≥ 30% below ATH"),
    ("rsi-32%", "C", "RSI ≤ 68% of the 24-month peak: the −32% rule as stated"),
    ("RSI<35 (any stock)", "ref", "Any stock, first month with RSI < 35 (the old turnaround trigger)"),
]
KEEP = ("n", "median", "hit", "beat_spy", "med_x_spy", "med_x_own", "beat_own", "cl_x_own", "t_own", "med_mae12", "near_bottom")


def clean(o):
    if isinstance(o, float):
        return None if math.isnan(o) or math.isinf(o) else round(o, 4)
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, list):
        return [clean(v) for v in o]
    return o


def main() -> None:
    study = json.loads((OUT / "study.json").read_text(encoding="utf-8"))
    timing = json.loads((OUT / "timing.json").read_text(encoding="utf-8"))
    var = json.loads((OUT / "variants.json").read_text(encoding="utf-8"))
    port = var["_portfolio"]

    tiers = []
    for key, tier, desc in TIERS:
        row = {"key": key, "tier": tier, "desc": desc, "stats": {}}
        for per in ("2009+", "last 10y", "last 5y"):
            for flt in ("none", "quality", "quality + cheap"):
                for h in ("12m", "24m"):
                    s = var[key][per][flt][h]
                    row["stats"][f"{per}|{flt}|{h}"] = {k: s.get(k) for k in KEEP}
        row["portfolio"] = {}
        for flt in ("none", "quality", "quality + cheap"):
            for st in ("2009-01", "2016-08", "2021-08"):
                p = port[f"{key} | {flt} | from {st}"]
                row["portfolio"][f"{flt}|{st}"] = {"cagr": p["signals"]["cagr"], "max_dd": p["signals"]["max_dd"],
                                                    "avg_open": p["avg_open"]}
        tiers.append(row)

    bench = {}
    for st in ("2009-01", "2016-08", "2021-08"):
        p = port[f"rsi-32% | none | from {st}"]
        bench[st] = {"spy": p["spy"], "uni_ew": p["uni_ew"]}

    curves = {"months": port["rsi-32% | none | from 2009-01"]["equity"]["months"]}
    for key, label in (("rsi-32%", "C: RSI −32% alone"), ("rsi-32% + price-40%", "B: RSI −32% + price −40%"),
                       ("leader + RSI<35", "A ★: leader + RSI < 35")):
        curves[label] = port[f"{key} | none | from 2009-01"]["equity"]["signals"]
    curves["SPY"] = port["rsi-32% | none | from 2009-01"]["equity"]["spy"]
    curves["Equal-weight universe"] = port["rsi-32% | none | from 2009-01"]["equity"]["uni_ew"]

    grid = {}  # ob x relative drop, window 24, 2009+, no fundamentals: month-clustered excess vs universe
    for row in study["sweep"]:
        if row["mode"] == "rel" and row["window"] == 24 and not row["ath_tol"] and row["min_years"] == 5 \
                and not row.get("min_dd") and not row.get("max_rsi"):
            s = row["2009+"]
            grid[f"{row['ob']:.0f}|{row['drop']:.2f}"] = {"x": s.get("clustered_x_uni"), "n": s.get("n"),
                                                          "median": s.get("median")}

    summary = {
        "generated": study["generated"], "last_month": study["last_month"], "n_tickers": study["n_tickers"],
        "tiers": tiers, "bench": bench, "curves": curves,
        "sweep": {"obs": [65, 70, 75, 80, 85], "drops": [0.20, 0.25, 0.28, 0.32, 0.36, 0.40, 0.45], "cells": grid},
        "hindsight": {k: {kk: v.get(kk) for kk in ("n", "median", "med_x_spy", "clustered_x_uni")}
                      for k, v in study["hindsight"].items()},
        "hindsight_capture": study["hindsight_capture"],
        "by_dd": {k: {kk: v.get(kk) for kk in ("n", "median", "med_x_spy", "clustered_x_uni", "med_mae12", "near_bottom")}
                  for k, v in study["by_dd"].items()},
        "timing": timing["timing"]["all signals"],
        "default_2009": {k: study["periods"]["2009+"]["signal (default)"].get(k)
                         for k in ("n", "tickers", "median", "beat_spy", "med_x_spy", "med_mae12", "near_bottom", "deep_further")},
        "own_2009": timing["own"]["signal"],
    }
    (OUT / "web_summary.json").write_text(json.dumps(clean(summary), indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT / 'web_summary.json'}")


if __name__ == "__main__":
    main()
