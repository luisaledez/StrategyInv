"""Self-contained HTML report for the backtest: output/report.html.

Reads output/results.json and the *_equity.csv files written by backtest.py.
"""
from __future__ import annotations

import json
import math
import sys
from html import escape
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import data  # noqa: E402

import sys as _sys
# python report_html.py [--out DIR]   (DIR defaults to output/; output_v2 for the second backtest)
OUT = data.OUT
if "--out" in _sys.argv:
    OUT = Path(_sys.argv[_sys.argv.index("--out") + 1])
    if not OUT.is_absolute():
        OUT = Path(__file__).resolve().parent / OUT

PALETTE_LIGHT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
PALETTE_DARK = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767"]


def money(x) -> str:
    return "n/a" if x is None else f"${x:,.0f}"


def pct(x) -> str:
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:+.1f}%"


def load_equity(name: str) -> pd.Series:
    df = pd.read_csv(OUT / f"{name}_equity.csv", index_col=0, parse_dates=True)
    if "tr_index" in df:
        return df["tr_index"]
    return df["equity"] / df["equity"].iloc[0]


def line_chart(series: dict[str, pd.Series], title: str, chart_id: str) -> str:
    """Log-scale line chart of growth indices (1 = start), monthly samples, with crosshair tooltip."""
    W, H, L, R, T, B = 960, 420, 56, 120, 28, 36
    monthly = {k: s.resample("ME").last().dropna() for k, s in series.items()}
    x0 = min(s.index[0] for s in monthly.values())
    x1 = max(s.index[-1] for s in monthly.values())
    ymin = min(s.min() for s in monthly.values())
    ymax = max(s.max() for s in monthly.values())
    lo, hi = math.log10(ymin * 0.9), math.log10(ymax * 1.1)

    def sx(d):
        return L + (d - x0).days / max(1, (x1 - x0).days) * (W - L - R)

    def sy(v):
        return T + (hi - math.log10(v)) / (hi - lo) * (H - T - B)

    parts = [f'<svg viewBox="0 0 {W} {H}" class="chart" id="{chart_id}" role="img" aria-label="{escape(title)}">']
    # gridlines at powers / halves
    ticks = []
    v = 10 ** math.floor(lo)
    while v <= 10 ** hi:
        for m in (1, 2, 5):
            tv = v * m
            if 10 ** lo <= tv <= 10 ** hi:
                ticks.append(tv)
        v *= 10
    for tv in ticks:
        y = sy(tv)
        parts.append(f'<line x1="{L}" x2="{W - R}" y1="{y:.1f}" y2="{y:.1f}" class="grid"/>')
        parts.append(f'<text x="{L - 6}" y="{y + 4:.1f}" class="tick" text-anchor="end">{tv:g}x</text>')
    for yr in range(x0.year, x1.year + 1, 2):
        d = pd.Timestamp(f"{yr}-01-01")
        if x0 <= d <= x1:
            parts.append(f'<text x="{sx(d):.1f}" y="{H - B + 16}" class="tick" text-anchor="middle">{yr}</text>')
    parts.append(f'<line x1="{L}" x2="{W - R}" y1="{sy(1):.1f}" y2="{sy(1):.1f}" class="baseline"/>')
    names = list(monthly)
    for i, k in enumerate(names):
        s = monthly[k]
        pts = " ".join(f"{sx(d):.1f},{sy(v):.1f}" for d, v in s.items() if v > 0)
        parts.append(f'<polyline points="{pts}" class="line s{i + 1}" data-name="{escape(k)}"/>')
        lx, ly = sx(s.index[-1]) + 6, sy(s.iloc[-1]) + 4
        parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" class="dl s{i + 1}">{escape(k)}</text>')
    parts.append(f'<line class="xhair" x1="0" x2="0" y1="{T}" y2="{H - B}" style="display:none"/>')
    parts.append("</svg>")
    data = {k: [[d.strftime("%Y-%m"), round(float(v), 3)] for d, v in s.items()] for k, s in monthly.items()}
    xs = {k: [round(sx(d), 1) for d in s.index] for k, s in monthly.items()}
    legend = "".join(f'<span class="lg"><i class="sw s{i + 1}"></i>{escape(k)}</span>' for i, k in enumerate(names))
    return (f'<figure><figcaption>{escape(title)}</figcaption>{"".join(parts)}'
            f'<div class="legend">{legend}</div><div class="tip" id="{chart_id}-tip"></div>'
            f'<script>chartData["{chart_id}"]={{data:{json.dumps(data)},xs:{json.dumps(xs)},L:{L},R:{W - R}}};</script></figure>')


def year_table(years, bench_years=None) -> str:
    by = {y["year"]: y for y in (bench_years or [])}
    rows = []
    cum = 0.0
    for y in years:
        cum += y["withdrawal"]
        b = by.get(y["year"])
        cls = "neg" if y["return"] < 0 else ""
        rows.append("<tr>" + "".join(f"<td{' class=num' if i else ''}>{c}</td>" for i, c in enumerate([
            str(y["year"]) + (" (to Aug)" if y.get("partial") else ""), money(y["start"]),
            f'<span class="{cls}">{pct(y["return"])}</span>', money(y["withdrawal"]), money(y["end"]), money(cum),
            str(y.get("positions", "")), pct(y["cash_pct"]) if y.get("cash_pct") is not None else "",
            pct(b["return"]) if b else ""])) + "</tr>")
    hdr = ["Year", "Start", "Return", "Withdrawal", "End (after)", "Cum. withdrawn", "Positions", "Cash", BENCH]
    return ('<table><thead><tr>' + "".join(f"<th>{h}</th>" for h in hdr) + "</tr></thead><tbody>"
            + "".join(rows) + "</tbody></table>")


CFG = data.CONFIG
BENCH = CFG.get("benchmark", "SPY")
REAL_INTRO = """<p class="lead">2004-01-01 to 2026-08-31. Quarterly scan with the turnaround scanner's rules (monthly RSI(14) &lt; 42 within the last 6 completed months,
≥ 5 years of history, ≥ $5M average daily dollar volume, ≥ $1B market cap), then profitable now and in the past, top 20 by trailing revenue growth,
top 10 of those by valuation versus own history. $100,000 start, at most 10% per stock, no taxes or costs, dividends as cash, idle cash earns nothing.
Withdrawals at each year end: return &gt; 20% → 10% of the portfolio; 10–20% → 7.5%; below 10% → 5%.</p>
<p>Filings data (SEC XBRL) begins with fiscal-2007 comparatives, so nothing qualifies before 2008 and the first real purchases are in 2009: from 2004 to 2008 the
portfolio is cash and still pays the 5% withdrawal. The universe is today's S&amp;P 500 + 400 members, so failed and acquired companies are missing (survivorship bias).
A monthly RSI of 90 is essentially never printed, so that exit never fires; see the rsi80 scenario.</p>"""


def intro_html() -> str:
    if not CFG.get("notes"):
        return REAL_INTRO
    import re
    head = (f'<p class="lead">{data.START.date()} to {data.END.date()}. Quarterly scan with the turnaround scanner rules, then profitable now and in the past, '
            'top 20 by trailing revenue growth, top 10 of those by valuation versus own history. $100,000 start, at most 10% per stock, no taxes or costs, '
            'dividends as cash, idle cash earns nothing. Withdrawals at each year end: return &gt; 20% → 10%; 10–20% → 7.5%; below 10% → 5%.</p>')
    paras = "".join("<p>" + re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escape(n)) + "</p>" for n in CFG["notes"])
    return head + paras


def build() -> Path:
    intro = intro_html()
    res = json.loads((OUT / "results.json").read_text(encoding="utf-8"))
    benches = res.pop("benchmarks")
    res.pop("rebase_events", None)   # extra key written by backtest_v2.py
    snaps = json.loads((OUT / "snapshots.json").read_text(encoding="utf-8"))
    order = [k for k in res]
    # ---- summary table
    hdr = ["Scenario", "Start", "First buy", "Final value", "Withdrawn", "Final + withdrawn", "CAGR final",
           "CAGR index", "IRR", "Max DD", "Closed", "Win rate", "Open"]
    srows = []
    for k in order:
        s = res[k]["summary"]
        srows.append([f"<b>{k}</b>", s["start"][:4], s["first_buy"] or "-", money(s["final_value"]),
                      money(s["total_withdrawn"]), money(s["final_plus_withdrawn"]), pct(s["cagr_final"]),
                      pct(s["cagr_tr_index"]), pct(s["irr"]), pct(s["max_drawdown"]), str(s["closed_positions"]),
                      pct(s["win_rate"]) if s["win_rate"] is not None else "n/a", str(s["open_positions"])])
    for key, b in benches.items():
        s = b["summary"]
        srows.append([f"{BENCH} from {key}", key, s["start"], money(s["final_value"]), money(s["total_withdrawn"]),
                      money(s["final_plus_withdrawn"]), pct(s["cagr_final"]), pct(s["cagr_tr_index"]), pct(s["irr"]),
                      pct(s["max_drawdown"]), "", "", ""])
    summary = ('<table><thead><tr>' + "".join(f"<th>{h}</th>" for h in hdr) + "</tr></thead><tbody>"
               + "".join("<tr>" + "".join(f"<td{' class=num' if i else ''}>{c}</td>" for i, c in enumerate(r)) + "</tr>" for r in srows)
               + "</tbody></table>")

    # ---- charts
    s04 = {k: load_equity(k) for k in order if res[k]["scenario"]["start"].startswith("2004")}
    y0 = str(data.START.year)
    s04 = {k: load_equity(k) for k in order if res[k]["scenario"]["start"].startswith(y0)}
    s04[BENCH] = load_equity(f"spy_{y0}")
    charts = line_chart(s04, f"Growth of $1 ignoring withdrawals, {y0} start (log scale)", "c04")
    s09 = {k: load_equity(k) for k in order if res[k]["scenario"]["start"].startswith("2009")}
    if s09 and "2009" in benches:
        s09[BENCH] = load_equity("spy_2009")
        charts += line_chart(s09, "Growth of $1 ignoring withdrawals, 2009 start (log scale)", "c09")

    # ---- per scenario
    sections = []
    for k in order:
        r = res[k]
        sc = r["scenario"]
        s = r["summary"]
        by = benches[sc["start"][:4]]["years"]
        reasons = pd.Series([t["reason"] for t in r["trades"] if t["side"] == "SELL"]).value_counts()
        losers = sorted([p for p in r["open"] if p["gain_pct"] < 0], key=lambda p: p["gain_pct"])
        top = sorted(r["open"], key=lambda p: -p["value"])[:12]
        notes = [f"{s['trades']} trades, {s['closed_positions']} closed positions"
                 + (f" (win rate {pct(s['win_rate'])}, average closed return {s['avg_closed_return_pct']:+.1f}%, "
                    f"median hold {s['median_hold_months']} months)" if s["closed_positions"] else "") + "."]
        if len(reasons):
            notes.append("Sell reasons: " + ", ".join(f"{a} × {b}" for a, b in reasons.items()) + ".")
        if r["open"]:
            notes.append(f"Open at the end: {len(r['open'])}, {len(losers)} below cost. Largest: "
                         + ", ".join(f"{p['ticker']} ({p['gain_pct']:+.0f}%)" for p in top) + ".")
            if losers:
                notes.append("Worst open: " + ", ".join(f"{p['ticker']} ({p['gain_pct']:+.0f}%)" for p in losers[:8]) + ".")
        if r["closed"]:
            best = sorted(r["closed"], key=lambda c: -c["pnl"])[:5]
            notes.append("Best closed: " + ", ".join(f"{c['ticker']} {money(c['pnl'])} ({c['return_pct']:+.0f}%)" for c in best) + ".")
        sections.append(f'<section><h2>{escape(k)} <small>{escape(sc["label"])}</small></h2>'
                        f'<p>Final value {money(s["final_value"])}, withdrawn {money(s["total_withdrawn"])}, '
                        f'together {money(s["final_plus_withdrawn"])}; IRR {pct(s["irr"])}.</p>'
                        + year_table(r["years"], by) + "<p>" + " ".join(escape(n) for n in notes) + "</p></section>")
    for key, b in benches.items():
        sections.append(f'<section><h2>{BENCH} from {key} <small>same withdrawal rule, dividends reinvested</small></h2>'
                        + year_table(b["years"]) + "</section>")
    lists = "".join(f"<tr><td>{s['date']}</td><td class=num>{s['n_qualified']}</td><td class=num>{s['n_eligible']}</td>"
                    f"<td>{', '.join(r['ticker'] for r in s['top10']) or '—'}</td></tr>" for s in snaps)
    sections.append('<section><h2>Quarterly top-10 lists</h2><table><thead><tr><th>Snapshot</th><th>Qualified</th>'
                    '<th>Eligible</th><th>Top 10 (value-rank order)</th></tr></thead><tbody>' + lists + '</tbody></table></section>')

    css_series = "".join(f".s{i + 1}{{--c:{c}}}" for i, c in enumerate(PALETTE_LIGHT))
    css_series_dark = "".join(f".s{i + 1}{{--c:{c}}}" for i, c in enumerate(PALETTE_DARK))
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(CFG.get("label", "Turnaround backtest"))}</title>
<style>
:root{{color-scheme:light;--bg:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#8a8984;--grid:#e6e5e1;--row:#f4f3f0;--neg:#d03b3b}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{color-scheme:dark;--bg:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--muted:#8a8984;--grid:#333331;--row:#232322;--neg:#e66767}}
:root:not([data-theme="light"]) {css_series_dark}}}
:root[data-theme="dark"]{{color-scheme:dark;--bg:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--muted:#8a8984;--grid:#333331;--row:#232322;--neg:#e66767}}
:root[data-theme="dark"] {css_series_dark}
{css_series}
body{{margin:0;padding:24px 16px 48px;background:var(--bg);color:var(--ink);font:15px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}}
main{{max-width:1080px;margin:0 auto}}
h1{{font-size:24px;margin:0 0 4px}} h2{{font-size:18px;margin:36px 0 8px}} h2 small{{font-weight:400;color:var(--ink2);font-size:14px;margin-left:8px}}
p{{color:var(--ink2);max-width:80ch}} .lead{{color:var(--ink)}}
table{{border-collapse:collapse;width:100%;font-size:13.5px;font-variant-numeric:tabular-nums}}
th,td{{padding:6px 8px;text-align:left;border-bottom:1px solid var(--grid);white-space:nowrap}} td.num,th{{}} td.num{{text-align:right}}
tbody tr:nth-child(even){{background:var(--row)}} th{{color:var(--ink2);font-weight:600}}
.neg{{color:var(--neg)}} .wrap{{overflow-x:auto}}
figure{{margin:24px 0;position:relative}} figcaption{{color:var(--ink2);font-size:14px;margin-bottom:6px}}
.chart{{width:100%;height:auto;display:block}} .grid{{stroke:var(--grid);stroke-width:1}} .baseline{{stroke:var(--muted);stroke-width:1;stroke-dasharray:3 3}}
.tick{{fill:var(--ink2);font-size:11px}} .line{{fill:none;stroke:var(--c);stroke-width:2;stroke-linejoin:round}}
.dl{{fill:var(--ink2);font-size:11px}} .xhair{{stroke:var(--muted);stroke-width:1}}
.legend{{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:13px;color:var(--ink2);margin-top:4px}} .sw{{display:inline-block;width:14px;height:3px;background:var(--c);vertical-align:middle;margin-right:6px;border-radius:2px}}
.tip{{position:absolute;display:none;background:var(--bg);border:1px solid var(--grid);border-radius:6px;padding:6px 8px;font-size:12px;color:var(--ink);pointer-events:none;box-shadow:0 2px 8px rgba(0,0,0,.15);z-index:2}}
.tip b{{display:block;margin-bottom:2px}} .tip i{{display:inline-block;width:10px;height:3px;margin-right:6px;vertical-align:middle;background:var(--c)}}
</style></head><body><main>
<h1>{escape(CFG.get("label", "Turnaround candidates backtest"))}</h1>
{intro}
<h2>Scenario summary</h2><div class="wrap">{summary}</div>
<p>CAGR final compounds the ending value after withdrawals; CAGR index chains the yearly returns as if nothing had been withdrawn; IRR is the money-weighted return of $100,000 in, withdrawals out, final value. Max DD is on the no-withdrawal index.</p>
{charts}
{"".join(sections)}
</main>
<script>
const chartData={{}};
</script>
<script>
document.querySelectorAll("figure").forEach(fig=>{{
  const svg=fig.querySelector("svg"), id=svg.id, tip=fig.querySelector(".tip"), xh=svg.querySelector(".xhair");
  svg.addEventListener("mousemove",ev=>{{
    const cd=chartData[id]; if(!cd) return;
    const pt=svg.createSVGPoint(); pt.x=ev.clientX; pt.y=ev.clientY; const p=pt.matrixTransform(svg.getScreenCTM().inverse());
    if(p.x<cd.L||p.x>cd.R){{tip.style.display="none";xh.style.display="none";return}}
    let html="", bx=null, date="";
    Object.keys(cd.data).forEach((k,i)=>{{
      const xs=cd.xs[k]; let j=0; while(j<xs.length-1&&xs[j+1]<=p.x) j++;
      if(Math.abs(xs[j]-p.x)>40) return;
      if(bx===null){{bx=xs[j];date=cd.data[k][j][0]}}
      html+=`<div><i class="s${{i+1}}"></i>${{k}}: ${{cd.data[k][j][1].toFixed(2)}}x</div>`;
    }});
    if(bx===null){{tip.style.display="none";xh.style.display="none";return}}
    xh.setAttribute("x1",bx);xh.setAttribute("x2",bx);xh.style.display="";
    tip.innerHTML=`<b>${{date}}</b>`+html; tip.style.display="block";
    const r=fig.getBoundingClientRect(); let lx=ev.clientX-r.left+14; if(lx+180>r.width) lx-=200; tip.style.left=lx+"px"; tip.style.top=(ev.clientY-r.top-10)+"px";
  }});
  svg.addEventListener("mouseleave",()=>{{tip.style.display="none";xh.style.display="none"}});
}});
</script></body></html>"""
    # the per-chart <script> blocks reference chartData before the const is declared: move the declaration first
    html = html.replace("<script>\nconst chartData={};\n</script>\n", "")
    html = html.replace("<h2>Scenario summary</h2>", "<script>const chartData={};</script>\n<h2>Scenario summary</h2>", 1)
    p = OUT / "report.html"
    p.write_text(html, encoding="utf-8")
    return p


if __name__ == "__main__":
    print(build())
