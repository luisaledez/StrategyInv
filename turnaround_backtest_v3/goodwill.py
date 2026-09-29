"""Point-in-time goodwill + acquired intangibles per quarter end, from the SEC company-facts files the
scanner's edgar.py already caches (turnaround/cache/edgar_raw/, no network).

An acquisition puts goodwill and intangible assets on the balance sheet; organic growth does not. The
acquisition guard in screen_v3.py uses the year-over-year change of this figure, scaled by the prior
year's trailing revenue, as the evidence that a jump in revenue growth was bought.

    goodwill = Goodwill
             + IntangibleAssetsNetExcludingGoodwill   (else FiniteLived + IndefiniteLived intangibles)
    (IntangibleAssetsNetIncludingGoodwill when neither goodwill tag is reported)

Each quarter end keeps the value as first filed ("available" = that filing date), so a backtest only
sees what was public at the time.

    python goodwill.py        # ~2 min, writes cache/goodwill.json  {ticker: [[end, available, value], ...]}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "turnaround"))
import edgar  # noqa: E402

OUT = HERE / "cache" / "goodwill.json"
GW = ["Goodwill"]
INTANG = ["IntangibleAssetsNetExcludingGoodwill"]
INTANG_PARTS = ["FiniteLivedIntangibleAssetsNet", "IndefiniteLivedIntangibleAssetsExcludingGoodwill"]
INCL = ["IntangibleAssetsNetIncludingGoodwill"]


def _first(facts: dict, tags: list[str]) -> dict[str, tuple[str, float]]:
    """end -> (first filing date, value as first filed) for balance-sheet instants."""
    out = {}
    for r in edgar._records(facts, tags):
        if r["start"]:
            continue
        f = r["filings"][0]
        out[r["end"]] = (f, r["vals"][f])
    return out


def series(facts: dict) -> list[list]:
    f = facts["facts"]
    gw, it = _first(f, GW), _first(f, INTANG)
    parts = [_first(f, [t]) for t in INTANG_PARTS]
    incl = _first(f, INCL)
    ends = sorted(set(gw) | set(it) | set().union(*[set(p) for p in parts]) | set(incl))
    rows = []
    for e in ends:
        vals, avail = [], []
        if e in gw or e in it or any(e in p for p in parts):
            for src in [gw, it] if e in it else [gw, *parts]:
                if e in src:
                    avail.append(src[e][0]); vals.append(src[e][1])
        elif e in incl:
            avail.append(incl[e][0]); vals.append(incl[e][1])
        if vals:
            rows.append([e, max(avail), sum(vals)])
    return rows


def build(tickers: list[str]) -> dict:
    res = {}
    for i, t in enumerate(tickers, 1):
        try:
            facts = edgar.company_facts(t, max_age_days=float("inf"))
        except Exception as e:  # noqa: BLE001
            print(f"  {t}: {e}", file=sys.stderr)
            continue
        if facts:
            res[t] = series(facts)
        if i % 100 == 0:
            print(f"  goodwill {i}/{len(tickers)}", file=sys.stderr, flush=True)
    return res


def load() -> dict:
    return json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}


if __name__ == "__main__":
    sys.path.insert(0, str(HERE.parent / "turnaround_backtest"))
    import data  # noqa: E402
    OUT.parent.mkdir(exist_ok=True)
    res = build(list(data.universe_meta().index))
    OUT.write_text(json.dumps(res, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT}: {len(res)} tickers, {sum(1 for v in res.values() if v)} with goodwill data")
