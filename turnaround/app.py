"""Local web UI for the turnaround scanner.

  python app.py            # http://localhost:8050

Pages: /            candidates: watchlist rows with Gate GREEN (stored as PASS), monthly RSI < 55 and
                    revenue YoY >= 10% or EPS last-quarter YoY >= 10%
       /watchlist   full watchlist (sortable, filterable, rescan button)
       /ticker/<T>  screen facts, price + monthly RSI chart, fundamentals, thesis file
       /all         every ticker in the universe with its RSI / drawdown metrics
       /v3          strategy v3 (`both_opval`) top 10 and ranks 11-20 with every screen diagnostic, from the
                    newest turnaround_backtest_v3/output/live_both_opval_<date>.json; /v3/report renders the
                    matching reports/Turnaround v3 positions - <date>.md
       /study       historical episode study
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import quote, unquote

import pandas as pd
from flask import Flask, abort, jsonify, redirect, render_template_string, request, url_for
from markdown import markdown

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import indicators as ind  # noqa: E402
import prices  # noqa: E402
import valuation_history as vh  # noqa: E402
from paths import ON_VERCEL  # noqa: E402
from scan import CAND_GROWTH_MIN, CAND_RSI_MAX, is_candidate  # noqa: E402

OUT = HERE / "output"
THESIS = HERE / "thesis"
V3_THESIS = HERE.parent / "turnaround_backtest_v3" / "thesis"  # research files for names bought by the v3 rule
THESIS_DIRS = [(V3_THESIS, "turnaround_backtest_v3/thesis"), (THESIS, "turnaround/thesis")]
FUND = HERE / "cache" / "fundamentals"
V3_OUT = HERE.parent / "turnaround_backtest_v3" / "output"     # live `both_opval` lists from live_v3.py
REPORTS = HERE.parent / "reports"

app = Flask(__name__)
JOB = {"running": False, "log": "", "started": None, "finished": None, "rc": None}


# ------------------------------------------------------------------ data access
def load_watchlist() -> list[dict]:
    p = OUT / "watchlist.json"
    if not p.exists():
        return []
    rows = json.loads(p.read_text(encoding="utf-8"))
    for r in rows:
        r["has_thesis"] = bool(thesis_files(r["ticker"]))
        r["status"] = thesis_status(r["ticker"])
    return rows


def load_candidates() -> list[dict]:
    return [r for r in load_watchlist() if is_candidate(r)]


def load_all() -> list[dict]:
    p = OUT / "screen_all.csv"
    if not p.exists():
        return []
    df = pd.read_csv(p)
    return json.loads(df.to_json(orient="records"))


def load_v3() -> dict | None:
    """Newest live `both_opval` list written by turnaround_backtest_v3/live_v3.py (falls back to the
    screen's own current_both_opval.json, which lacks the enrichment fields)."""
    if not V3_OUT.exists():
        return None
    files = sorted(V3_OUT.glob("live_both_opval_*.json"))
    p = files[-1] if files else V3_OUT / "current_both_opval.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text(encoding="utf-8"))
    d["source_file"] = p.name
    for r in d.get("top20", []):
        r.setdefault("eps_guidecut_trigger", round(0.85 * r["eps_ttm"], 3) if r.get("eps_ttm") else None)
        r.setdefault("trim_price", round(1.5 * r["close"], 2) if r.get("close") else None)
        r["eps_path_s"] = ", ".join(f"{x:.2f}" for x in r["eps_path"]) if r.get("eps_path") else ""
        r["in_top10"] = r.get("value_rank") is not None
        r["has_thesis"] = bool(thesis_files(r["ticker"]))
        r["status"] = thesis_status(r["ticker"])
    d["top10"] = sorted([r for r in d["top20"] if r["in_top10"]], key=lambda r: r["value_rank"])
    d["bench"] = [r for r in d["top20"] if not r["in_top10"]]
    return d


def v3_row(ticker: str) -> tuple[dict | None, dict | None]:
    d = load_v3()
    if not d:
        return None, None
    return d, next((r for r in d["top20"] if r["ticker"] == ticker), None)


def latest_v3_report() -> Path | None:
    files = sorted(REPORTS.glob("Turnaround v3 positions - *.md")) if REPORTS.exists() else []
    return files[-1] if files else None


def thesis_files(ticker: str) -> list[tuple[Path, str]]:
    """Research files for a ticker, v3 folder first: [(path, label)]."""
    return [(d / f"{ticker}.md", label) for d, label in THESIS_DIRS if (d / f"{ticker}.md").exists()]


def thesis_status(ticker: str) -> str | None:
    files = thesis_files(ticker)
    if not files:
        return None
    p = files[0][0]
    for line in p.read_text(encoding="utf-8").splitlines()[:12]:
        if line.startswith("status:"):
            return line.split(":", 1)[1].split("<!--")[0].strip()
    return "?"


# Markdown documents the app may render at /doc/<path>: research files, reports and notes.
ROOT = HERE.parent
DOC_ROOTS = ["reports", "research_notes", "turnaround_backtest_v3", "turnaround/thesis"]
_HREF = re.compile(r'(href|src)="([^"]+)"')


def doc_path(rel: str) -> Path | None:
    """Repo-relative path -> file or folder inside DOC_ROOTS, else None (no traversal outside them)."""
    try:
        p = (ROOT / unquote(rel)).resolve()
        r = p.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return None
    if not any(r == d or r.startswith(d + "/") for d in DOC_ROOTS) or not p.exists():
        return None
    if p.is_file() and p.suffix.lower() != ".md":
        return None
    return p


def render_md(path: Path) -> str:
    """Markdown -> HTML, with links to other repository documents rewritten to /doc/ (and /v3/report)."""
    html = markdown(path.read_text(encoding="utf-8"), extensions=["tables"])
    root = ROOT.resolve()
    repo = root.as_posix().lower()
    latest = latest_v3_report()

    def fix(m):
        attr, href = m.group(1), m.group(2)
        if href.startswith(("http:", "https:", "mailto:", "#", "/doc/", "/ticker/", "/v3")):
            return m.group(0)
        target, _, frag = href.partition("#")
        t = unquote(target).replace("\\", "/")
        if t.lower().startswith(repo):                      # absolute paths to the repo in older reports
            cand = root / t[len(repo):].lstrip("/")
        else:
            cand = path.parent / t
        try:
            rel = cand.resolve().relative_to(root).as_posix()
        except ValueError:
            return m.group(0)
        dp = doc_path(rel)
        if dp is None:
            return m.group(0)
        if latest is not None and dp == latest.resolve():
            return f'{attr}="/v3/report"'
        return f'{attr}="/doc/{quote(rel)}' + (f"#{frag}" if frag else "") + '"'
    return _HREF.sub(fix, html)


def research_index() -> dict:
    """v3 thesis files with their headline fields, plus the reports and research-note folders."""
    rows = []
    for p in sorted(V3_THESIS.glob("*.md")) if V3_THESIS.exists() else []:
        text = p.read_text(encoding="utf-8")
        head = {}
        for line in text.splitlines()[:12]:
            k, _, v = line.partition(":")
            if k in ("status", "review_deadline", "last_updated"):
                head[k] = v.split("<!--")[0].strip()
        title = text.splitlines()[0].lstrip("# ").strip()
        m = re.search(r"buy #(\d+)", text)
        c = re.search(r"^## 8\. Research conclusion\s*\n+(.+?)(?:\n## |\Z)", text, flags=re.S | re.M)
        concl = markdown(c.group(1).strip().split("\n\n")[0]) if c else ""
        rows.append({"ticker": p.stem, "title": title, "order": int(m.group(1)) if m else 99, "concl": concl,
                     "rel": p.relative_to(ROOT).as_posix(), **head})
    rows.sort(key=lambda r: (r["order"], r["ticker"]))
    reports = sorted(p.relative_to(ROOT).as_posix() for p in REPORTS.glob("*.md")) if REPORTS.exists() else []
    nd = ROOT / "research_notes"
    notes = sorted(p.relative_to(ROOT).as_posix() for p in nd.iterdir() if p.is_dir()) if nd.exists() else []
    return {"theses": rows, "reports": reports, "notes": notes}


def scan_meta() -> dict:
    p = OUT / "scan_meta.json"
    default = {"threshold": 35.0, "rsi_period": 14, "lookback": 6, "universe": "sp500,sp400"}
    if not p.exists():
        return default
    try:
        return default | json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return default


def as_of() -> str:
    """Date the scan's price data runs through (taken from the data itself, since
    file timestamps are not meaningful in a deployed bundle)."""
    p = OUT / "watchlist.json"
    if not p.exists():
        return "never"
    try:
        rows = json.loads(p.read_text(encoding="utf-8"))
        bars = [r.get("last_bar") for r in rows if r.get("last_bar")]
        if bars:
            return "data through " + max(bars)
    except Exception:  # noqa: BLE001
        pass
    return datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M")


# ------------------------------------------------------------------ formatting
def money(x):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "–"
    a, s = abs(x), "-" if x < 0 else ""
    if a >= 1e9:
        return f"{s}${a / 1e9:.2f}B"
    if a >= 1e6:
        return f"{s}${a / 1e6:.0f}M"
    return f"{s}${a:,.0f}"


def pct(x, signed=True):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    return f"{x * 100:+.1f}%" if signed else f"{x * 100:.1f}%"


def num(x, d=1):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    if isinstance(x, float) and math.isinf(x):
        return "∞"
    if isinstance(x, (int, float)) and x >= 1e6:
        return "∞"
    return f"{x:.{d}f}"


from markupsafe import Markup  # noqa: E402


def _cls(x, good):
    if x is None or (isinstance(x, float) and math.isnan(x)) or x == 0:
        return ""
    up = x > 0
    return "pos" if (up if good == "up" else not up) else "neg"


def pctc(x, good="up", signed=True):
    """Percentage coloured by whether its sign is a good indicator."""
    return Markup(f'<span class="{_cls(x, good)}">{pct(x, signed)}</span>')


def moneyc(x, good="up"):
    return Markup(f'<span class="{_cls(x, good)}">{money(x)}</span>')


def numc(x, d=1, good="up"):
    return Markup(f'<span class="{_cls(x, good)}">{num(x, d)}</span>')


GATE_LABEL = {"PASS": "GREEN"}  # display names for survival_gate values; the stored value stays PASS


def gate_label(v):
    return GATE_LABEL.get(v, v)


app.jinja_env.filters.update(money=money, pct=pct, num=num, pctc=pctc, moneyc=moneyc, numc=numc, gate=gate_label)


# ------------------------------------------------------------------ SVG chart
def _monthly_from_chart_data(ticker: str) -> pd.DataFrame | None:
    p = OUT / "charts.json"
    if not p.exists():
        return None
    rows = json.loads(p.read_text(encoding="utf-8")).get(ticker)
    if not rows:
        return None
    df = pd.DataFrame(rows, columns=["Date", "Close"])
    df["Date"] = pd.to_datetime(df["Date"])
    return df.set_index("Date")


def chart_svg(ticker: str, years: int = 8, threshold: float | None = None) -> str:
    if threshold is None:
        threshold = float(scan_meta()["threshold"])
    d = prices.load(ticker)
    if d is not None:
        m = ind.monthly_bars(d)
    else:
        m = _monthly_from_chart_data(ticker)
        if m is None:
            return "<p class='muted'>no price data cached for this ticker</p>"
        ref = pd.Timestamp.today().normalize()
        if m.index[-1].to_period("M") == ref.to_period("M") and ref < m.index[-1].to_period("M").end_time.normalize():
            m = m.iloc[:-1]
    rsi = ind.wilder_rsi(m["Close"])
    n = min(len(m), years * 12)
    m, rsi = m.iloc[-n:], rsi.iloc[-n:]
    W, H1, H2, PAD = 900, 220, 120, 40
    xs = [PAD + i * (W - 2 * PAD) / max(n - 1, 1) for i in range(n)]
    lo, hi = float(m["Close"].min()), float(m["Close"].max())
    span = (hi - lo) or 1.0

    def y1(v):
        return PAD + (H1 - 2 * PAD) * (1 - (v - lo) / span) + 10

    def y2(v):
        return H1 + 20 + (H2 - 30) * (1 - v / 100)

    price_pts = " ".join(f"{x:.1f},{y1(v):.1f}" for x, v in zip(xs, m["Close"]))
    rsi_pts = " ".join(f"{x:.1f},{y2(v):.1f}" for x, v in zip(xs, rsi) if not math.isnan(v))
    # shade oversold months
    shade = ""
    bw = (W - 2 * PAD) / max(n - 1, 1)
    for x, v in zip(xs, rsi):
        if not math.isnan(v) and v < threshold:
            shade += f"<rect x='{x - bw / 2:.1f}' y='{PAD - 5}' width='{bw:.1f}' height='{H1 + H2 - PAD - 10}' class='shade'/>"
    # year ticks
    ticks = ""
    for i, dt in enumerate(m.index):
        if dt.month == 1 or (i == 0):
            ticks += f"<text x='{xs[i]:.1f}' y='{H1 + H2 + 8}' class='tick'>{dt.year}</text>"
    grid = "".join(f"<text x='{PAD - 6}' y='{y1(v):.1f}' class='tick r'>{v:,.0f}</text>"
                   f"<line x1='{PAD}' x2='{W - PAD}' y1='{y1(v):.1f}' y2='{y1(v):.1f}' class='grid'/>"
                   for v in (lo, lo + span / 2, hi))
    rsi_grid = "".join(f"<text x='{PAD - 6}' y='{y2(v):.1f}' class='tick r'>{v}</text>"
                       f"<line x1='{PAD}' x2='{W - PAD}' y1='{y2(v):.1f}' y2='{y2(v):.1f}' class='{'thr' if v == threshold else 'grid'}'/>"
                       for v in (threshold, 50, 70))
    last = (f"<text x='{W - PAD}' y='{PAD}' class='tick r'>{m.index[-1].strftime('%b %Y')} close "
            f"{m['Close'].iloc[-1]:,.2f} · RSI {rsi.iloc[-1]:.1f}</text>")
    return (f"<svg viewBox='0 0 {W} {H1 + H2 + 20}' class='chart'>{shade}{grid}{rsi_grid}"
            f"<polyline points='{price_pts}' class='price'/><polyline points='{rsi_pts}' class='rsi'/>"
            f"{ticks}{last}<text x='{PAD}' y='{H1 + 12}' class='lbl'>monthly RSI(14)</text>"
            f"<text x='{PAD}' y='{PAD - 8}' class='lbl'>monthly close (last {n // 12} years)</text></svg>")


def valuation_chart(metric: dict, years: int = 30) -> str:
    """Small panel: reconstructed monthly line, Yahoo snapshot dots, average line, current marker.
    The y-axis is clipped at 3x the median so a near-zero-earnings spike does not flatten the rest."""
    st = metric.get("stats", {})
    monthly = metric.get("monthly") or []
    snaps = metric.get("snapshots") or []
    pts = [(datetime.strptime(d, "%Y-%m-%d"), v) for d, v in monthly] + \
          [(datetime.strptime(d, "%Y-%m-%d"), v) for d, v in snaps]
    if not pts or st.get("n", 0) == 0:
        return "<p class='muted small'>no history</p>"
    cutoff = datetime.today() - timedelta(days=365 * years)
    pts = [(d, v) for d, v in pts if d >= cutoff]
    if not pts:
        return "<p class='muted small'>no history</p>"
    W, H, PL, PR, PT, PB = 440, 150, 42, 12, 24, 20
    d0, d1 = min(d for d, _ in pts), max(d for d, _ in pts)
    span_days = max((d1 - d0).days, 1)
    med = st.get("median", 0) or 0
    cap = max(3 * med, st.get("current", 0) or 0, 1e-9)
    vals = [min(v, cap) for _, v in pts]
    lo, hi = min(vals + [0]), max(vals + [cap if med else 0])
    hi = hi * 1.05 or 1

    def x(d):
        return PL + (W - PL - PR) * (d - d0).days / span_days

    def y(v):
        return PT + (H - PT - PB) * (1 - (min(v, cap) - lo) / (hi - lo))

    line = ""
    if monthly:
        mp = [(datetime.strptime(d, "%Y-%m-%d"), v) for d, v in monthly if datetime.strptime(d, "%Y-%m-%d") >= cutoff]
        if mp:
            line = f"<polyline points='{' '.join(f'{x(d):.1f},{y(v):.1f}' for d, v in mp)}' class='price'/>"
    dots = "".join(f"<circle cx='{x(datetime.strptime(d, '%Y-%m-%d')):.1f}' cy='{y(v):.1f}' r='2.5' class='dot'/>"
                   for d, v in snaps if datetime.strptime(d, "%Y-%m-%d") >= cutoff)
    avg = st.get("avg")
    avg_line = f"<line x1='{PL}' x2='{W - PR}' y1='{y(avg):.1f}' y2='{y(avg):.1f}' class='thr'/>" if avg else ""
    med_line = f"<line x1='{PL}' x2='{W - PR}' y1='{y(med):.1f}' y2='{y(med):.1f}' class='grid'/>" if med else ""
    cur = st.get("current")
    cur_mark = (f"<circle cx='{x(d1):.1f}' cy='{y(cur):.1f}' r='4' class='cur'/>"
                f"<text x='{x(d1) - 6:.1f}' y='{y(cur) - 7:.1f}' class='tick r'>now {cur:.1f}</text>") if cur else ""
    yt = "".join(f"<text x='{PL - 4}' y='{y(v):.1f}' class='tick r'>{v:.0f}</text>" for v in (lo, (lo + hi) / 2, hi / 1.05))
    step = 1 if (d1.year - d0.year) <= 8 else (2 if (d1.year - d0.year) <= 16 else 3)
    xt = "".join(f"<text x='{x(datetime(yr, 1, 1)):.1f}' y='{H - 4}' class='tick'>{yr}</text>"
                 for yr in range(d0.year + 1, d1.year + 1) if yr % step == 0)
    clipped = " (axis clipped)" if any(v > cap for _, v in pts) else ""
    title = f"<text x='{PL}' y='14' class='lbl'>{metric['label']}{clipped}</text>"
    return f"<svg viewBox='0 0 {W} {H}' class='chart mini'>{title}{med_line}{avg_line}{line}{dots}{cur_mark}{yt}{xt}</svg>"


# ------------------------------------------------------------------ templates
BASE = """<!doctype html><html><head><meta charset="utf-8"><title>{{ title }} · Turnaround scanner</title>
<link href="https://cdn.jsdelivr.net/npm/tabulator-tables@6.3.1/dist/css/tabulator_simple.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/tabulator-tables@6.3.1/dist/js/tabulator.min.js"></script>
<script>
// ---------------------------------------------------------------- grid helpers (Tabulator)
const fmt={
  money:v=>v==null||isNaN(v)?'–':Math.abs(v)>=1e9?(v<0?'-':'')+'$'+(Math.abs(v)/1e9).toFixed(2)+'B':Math.abs(v)>=1e6?(v<0?'-':'')+'$'+Math.round(Math.abs(v)/1e6)+'M':(v<0?'-':'')+'$'+Math.round(Math.abs(v)).toLocaleString(),
  pct:v=>v==null||isNaN(v)?'–':(v*100>=0?'+':'')+(v*100).toFixed(1)+'%',
  num:(v,d)=>v==null||isNaN(v)?'–':(v>=1e6?'∞':Number(v).toFixed(d)),
};
function colored(v,good){if(v==null||isNaN(v)||v===0)return'';const up=v>0;return(good==='down'?!up:up)?'pos':'neg';}
// header filter with an operator picker; value passed to the filter function is {op,val}
function opFilter(cell,onRendered,success,cancel,params){
  const ops=params.ops||['=','≥','≤','>','<','≠'];const wrap=document.createElement('div');wrap.className='hf';
  const sel=document.createElement('select');ops.forEach(o=>{const e=document.createElement('option');e.value=o;e.textContent=o;sel.appendChild(e);});
  const inp=document.createElement('input');inp.placeholder=params.placeholder||'';
  const fire=()=>success(inp.value===''?'':{op:sel.value,val:inp.value});
  sel.addEventListener('change',fire);inp.addEventListener('input',fire);
  inp.addEventListener('keydown',e=>{if(e.key==='Escape'){inp.value='';fire();}});
  wrap.append(sel,inp);return wrap;}
function opFilterFunc(hv,rv,row,params){
  if(hv===''||hv==null)return true;const {op,val}=hv;const scale=params.scale||1;
  const text=String(rv==null?'':rv).toLowerCase(),q=String(val).toLowerCase();
  if(op==='contains')return text.includes(q);if(op==='!contains')return!text.includes(q);
  const b=parseFloat(val);
  if(isNaN(b)){if(op==='=')return text===q;if(op==='≠')return text!==q;return true;}
  if(rv==null||rv==='')return false;const a=parseFloat(rv)*scale;if(isNaN(a))return false;
  const eq=Math.abs(a-b)<1e-9;
  return op==='='?eq:op==='≠'?!eq:op==='≥'?a>=b:op==='≤'?a<=b:op==='>'?a>b:op==='<'?a<b:true;}
const NUMOPS=['≥','≤','=','>','<','≠'],TXTOPS=['contains','=','≠','!contains'];
const GATE={PASS:'GREEN'}; // display names for survival_gate values
// column kinds
function col(field,title,kind,o={}){
  const base={field,title,headerFilter:opFilter,headerFilterFunc:opFilterFunc,headerFilterLiveFilter:true,headerTooltip:o.tip||title,minWidth:60};
  const k={
    text:{headerFilterParams:{ops:TXTOPS},sorter:'string'},
    num:{headerFilterParams:{ops:NUMOPS},sorter:'number',hozAlign:'right',formatter:c=>fmt.num(c.getValue(),o.d==null?1:o.d)},
    pct:{headerFilterParams:{ops:NUMOPS,scale:100,placeholder:'%'},sorter:'number',hozAlign:'right',formatter:c=>`<span class="${o.good?colored(c.getValue(),o.good):''}">${fmt.pct(c.getValue())}</span>`},
    money:{headerFilterParams:{ops:NUMOPS,scale:1e-6,placeholder:'$M'},sorter:'number',hozAlign:'right',formatter:c=>fmt.money(c.getValue())},
  }[kind]||{};
  const {tip,d,good,...rest}=o;const def=Object.assign(base,k,rest);def.headerFilterFuncParams=def.headerFilterParams;def.kind=kind;def.decimals=d==null?1:d;return def;}
// header menu: hide / move / show-hide any column
function headerMenu(){
  const t=this;const menu=[
    {label:'Hide this column',action:(e,c)=>c.hide()},
    {label:'Move to front',action:(e,c)=>{const cs=t.getColumns().filter(x=>x.isVisible());c.move(cs[0],false);}},
    {label:'Move to back',action:(e,c)=>{const cs=t.getColumns();c.move(cs[cs.length-1],true);}},
    {label:'Move left',action:(e,c)=>{const cs=t.getColumns().filter(x=>x.isVisible());const i=cs.indexOf(c);if(i>0)c.move(cs[i-1],false);}},
    {label:'Move right',action:(e,c)=>{const cs=t.getColumns().filter(x=>x.isVisible());const i=cs.indexOf(c);if(i<cs.length-1)c.move(cs[i+1],true);}},
    {separator:true},{label:'Show / hide columns:',disabled:true}];
  for(const column of t.getColumns()){
    const label=document.createElement('span');const box=document.createElement('input');box.type='checkbox';box.checked=column.isVisible();box.style.marginRight='6px';
    label.append(box,document.createTextNode(column.getDefinition().title));
    menu.push({label,action:e=>{e.stopPropagation();column.toggle();box.checked=column.isVisible();}});}
  return menu;}
function makeGrid(el,columns,data,id,extra={}){
  columns.forEach(c=>{c.headerMenu=headerMenu;});
  // horizontal scrollbar above the grid: a thin scroller whose inner width tracks the table; kept in sync both ways
  const host=document.querySelector(el);const bar=document.createElement('div');bar.className='hscroll';bar.appendChild(document.createElement('div'));
  host.parentNode.insertBefore(bar,host);
  const height=Math.max(420,window.innerHeight-bar.getBoundingClientRect().top-bar.offsetHeight-14);
  const gp=groupPanel(columns,data,id);  // saved grouping goes into the constructor so it is applied with the initial render
  const table=new Tabulator(el,Object.assign({data,columns,layout:'fitDataFill',height:height+'px',
    resizableColumnFit:false,movableColumns:true,columnDefaults:{resizable:true,headerSortTristate:true},
    persistence:{columns:true,sort:true},persistenceID:id,groupToggleElement:'header',groupStartOpen:true,
    placeholder:'No rows match the filters'},gp.options,extra));
  const sync=()=>{const t=host.querySelector('.tabulator-table');if(t)bar.firstChild.style.width=t.offsetWidth+'px';};
  ['tableBuilt','renderComplete','columnResized','columnVisibilityChanged','columnMoved','dataFiltered'].forEach(e=>table.on(e,sync));
  let lock=false;
  bar.addEventListener('scroll',()=>{if(lock)return;lock=true;const h=host.querySelector('.tabulator-tableholder');if(h)h.scrollLeft=bar.scrollLeft;lock=false;});
  table.on('scrollHorizontal',left=>{if(lock)return;lock=true;bar.scrollLeft=left;lock=false;});
  table.on('dataFiltered',(f,rows)=>{const c=document.getElementById('count');if(c)c.textContent=rows.length+' of '+data.length+' shown';});
  document.getElementById('reset-layout')?.addEventListener('click',()=>{Object.keys(localStorage).filter(k=>k.startsWith('tabulator-'+id)||k==='turnaround-group-'+id).forEach(k=>localStorage.removeItem(k));location.reload();});
  gp.bind(table);
  return table;}
// "Group by" bar: up to three levels, each a column plus optional cut points for numeric columns.
// Cut points are typed in display units (percent for % columns, $M for money), like the header filters.
// Groups are ordered by bucket (or by value) and empty buckets are hidden. The setup is remembered per page.
function groupPanel(columns,data,id){
  const bar=document.getElementById('groupbar');if(!bar)return {options:{},bind(){}};
  let table=null,options={};
  const KEY='turnaround-group-'+id,defs=columns.filter(c=>c.field&&c.title&&c.kind),levels=[];
  const fmtCut=(d,v)=>d.kind==='pct'?v+'%':d.kind==='money'?'$'+v.toLocaleString()+'M':String(v);
  const fmtVal=(d,v)=>d.field==='survival_gate'?(GATE[v]||v):d.kind==='pct'?fmt.pct(v):d.kind==='money'?fmt.money(v):d.kind==='num'?fmt.num(v,d.decimals):String(v);
  bar.innerHTML='<span class="muted small">Group by</span>';
  for(let i=0;i<3;i++){
    const sel=document.createElement('select');sel.innerHTML='<option value="">— none —</option>'+defs.map(d=>`<option value="${d.field}">${d.title}</option>`).join('');
    const inp=document.createElement('input');inp.size=24;inp.disabled=true;
    const upd=()=>{const d=defs.find(x=>x.field===sel.value);inp.disabled=!d||d.kind==='text';
      inp.placeholder=!d?'':d.kind==='text'?'by value':d.kind==='pct'?'cut points in %, e.g. 0, 10':d.kind==='money'?'cut points in $M, e.g. 1000, 10000':'cut points, e.g. 38, 45';
      if(inp.disabled)inp.value='';};
    sel.addEventListener('change',upd);inp.addEventListener('keydown',e=>{if(e.key==='Enter')apply();});
    if(i)bar.appendChild(Object.assign(document.createElement('span'),{textContent:'›',className:'muted'}));
    bar.append(sel,inp);levels.push({sel,inp,upd});}
  const ok=Object.assign(document.createElement('button'),{textContent:'Apply'}),clr=Object.assign(document.createElement('button'),{textContent:'Clear',className:'sec'});bar.append(ok,clr);
  function build(cfg){const fns=[],vals=[],heads=[];
    for(const c of cfg){const d=defs.find(x=>x.field===c.field);if(!d)continue;
      const scale=d.headerFilterParams?.scale||1;
      const cuts=[...new Set((c.cuts||'').split(/[,;\\s]+/).filter(x=>x!=='').map(Number).filter(x=>!isNaN(x)))].sort((a,b)=>a-b);
      let fn,keys;
      if(d.kind!=='text'&&cuts.length){
        const labels=['< '+fmtCut(d,cuts[0]),...cuts.slice(1).map((v,j)=>fmtCut(d,cuts[j])+' – '+fmtCut(d,v)),'≥ '+fmtCut(d,cuts[cuts.length-1])];
        fn=r=>{const v=r[d.field];if(v==null||v==='')return'n/a';const x=parseFloat(v)*scale;if(isNaN(x))return'n/a';let k=0;while(k<cuts.length&&x>=cuts[k])k++;return labels[k];};
        keys=[...labels,'n/a'];
      }else{
        fn=r=>{const v=r[d.field];return v==null||v===''?'n/a':fmtVal(d,v);};
        const order=new Map();data.forEach(r=>{const v=r[d.field];if(v!=null&&v!=='')order.set(fn(r),d.kind==='text'?String(v):parseFloat(v));});
        keys=[...order.keys()].sort((a,b)=>{const x=order.get(a),y=order.get(b);return typeof x==='string'?x.localeCompare(y):x-y;});keys.push('n/a');}
      fns.push(fn);vals.push(keys);
      heads.push((value,count,rows,group)=>{group.getElement().classList.toggle('empty',!count);return `<span class="muted">${d.title}:</span> <b>${value}</b> <span class="muted small">· ${count} row${count===1?'':'s'}</span>`;});}
    return {fns,vals,heads};}
  function apply(){const cfg=levels.map(L=>({field:L.sel.value,cuts:L.inp.value})).filter(c=>c.field);
    try{localStorage.setItem(KEY,JSON.stringify(cfg));}catch(e){}
    if(!table)return;
    if(!cfg.length){table.setGroupBy(false);return;}
    const g=build(cfg);table.setGroupValues(g.vals);table.setGroupHeader(g.heads);table.setGroupBy(g.fns);}
  ok.addEventListener('click',apply);clr.addEventListener('click',()=>{levels.forEach(L=>{L.sel.value='';L.upd();});apply();});
  // restore the saved setup: fill the controls and hand the grouping options to the table constructor
  try{const saved=JSON.parse(localStorage.getItem(KEY)||'[]');saved.forEach((c,i)=>{if(levels[i]){levels[i].sel.value=c.field||'';levels[i].upd();levels[i].inp.value=c.cuts||'';}});
    const cfg=saved.filter(c=>c.field&&defs.some(d=>d.field===c.field));if(cfg.length){const g=build(cfg);options={groupBy:g.fns,groupValues:g.vals,groupHeader:g.heads};}}catch(e){}
  return {options,bind(t){table=t;}};}
function quickFilters(table,fn){
  const apply=()=>table.setFilter(fn);
  document.querySelectorAll('.toolbar input').forEach(e=>e.addEventListener('input',apply));apply();}
</script>
<style>
.tabulator{font-size:13px;border:1px solid var(--line);border-radius:8px;background:#fff}
.tabulator .tabulator-header{background:#fff;border-bottom:2px solid var(--line)}
.tabulator .tabulator-header .tabulator-col{background:#fff;border-right:1px solid #f0f0f0}
.tabulator .tabulator-header .tabulator-col.tabulator-sortable:hover{background:#f7f9fc}
.tabulator .tabulator-header .tabulator-col .tabulator-col-content{padding:6px 6px}
.tabulator .tabulator-header .tabulator-col .tabulator-col-title{font-weight:600;color:#333}
.tabulator .tabulator-header .tabulator-header-filter{background:#fff}
.tabulator-row{border-bottom:1px solid #f0f0f0}
.tabulator-row .tabulator-cell{padding:5px 8px;border-right:1px solid #f4f4f4}
.tabulator-row:hover{background:#f5f8ff}
.tabulator-row .tabulator-cell.tabulator-frozen,.tabulator .tabulator-header .tabulator-col.tabulator-frozen{background:#fff}
.tabulator .tabulator-tableholder::-webkit-scrollbar{width:10px;height:0}
.tabulator .tabulator-tableholder::-webkit-scrollbar-thumb{background:#cfcfcf;border-radius:5px}
.tabulator .tabulator-tableholder::-webkit-scrollbar-track{background:#fff}
.hscroll{overflow-x:auto;overflow-y:hidden;height:14px;margin-bottom:4px}.hscroll>div{height:1px}
.groupbar{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 8px;min-height:30px}
.groupbar select,.groupbar input{padding:4px 6px;border:1px solid var(--line);border-radius:6px;font:inherit;font-size:12px}.groupbar input:disabled{background:#f7f7f7}
.groupbar button{padding:4px 10px;font-size:12px}
.tabulator-row.tabulator-group{background:#f5f8ff;border-bottom:1px solid var(--line);border-top:1px solid var(--line);padding:6px 10px;font-size:13px;font-weight:400}
.tabulator-row.tabulator-group.tabulator-group-level-1{background:#fafbfe;padding-left:26px}.tabulator-row.tabulator-group.tabulator-group-level-2{background:#fff;padding-left:42px}
.tabulator-row.tabulator-group span.tabulator-group-toggle{display:inline}
.tabulator-row.tabulator-group.empty{display:none}
.hscroll::-webkit-scrollbar{height:10px}.hscroll::-webkit-scrollbar-thumb{background:#cfcfcf;border-radius:5px}.hscroll::-webkit-scrollbar-track{background:#f4f4f4;border-radius:5px}
.tabulator .tabulator-header-filter .hf{display:flex;gap:2px}
.tabulator .tabulator-header-filter .hf select{width:52px;font-size:11px;padding:1px}
.tabulator .tabulator-header-filter .hf input{flex:1;min-width:40px;font-size:11px;padding:2px 3px}
.tabulator-menu{font-size:13px;max-height:70vh;overflow:auto}
.tabulator-menu .tabulator-menu-item{padding:4px 12px}
.tabulator-row.tabulator-row-even{background:#fff}
.tabulator-cell.r{text-align:right}
:root{--bg:#fff;--fg:#1a1a1a;--muted:#6b6b6b;--line:#e6e6e6;--acc:#1d4ed8;--pass:#15803d;--rev:#b45309;--fail:#b91c1c;--shade:#fde68a}
*{box-sizing:border-box}body{margin:0;font:14px/1.45 system-ui,Segoe UI,sans-serif;color:var(--fg);background:var(--bg)}
header{display:flex;gap:18px;align-items:center;padding:12px 24px;border-bottom:1px solid var(--line);background:#fff;position:sticky;top:0;z-index:2}
header a{color:var(--fg);text-decoration:none;font-weight:600}header a.active{color:var(--acc)}header .sp{flex:1}
main{padding:20px 24px;max-width:1500px}h1{font-size:20px;margin:0 0 6px}h2{font-size:16px;margin:22px 0 8px}
.muted{color:var(--muted)}.small{font-size:12px}
table{border-collapse:collapse;width:100%;background:#fff;border:1px solid var(--line)}
th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}
th:first-child,td:first-child,td.l,th.l{text-align:left}th{background:#fff;border-bottom:2px solid var(--line);cursor:pointer;position:sticky;top:49px;user-select:none}
th.sorted::after{content:" ▾"}th.sorted.asc::after{content:" ▴"}
tr:hover td{background:#f8fafc}a{color:var(--acc)}
.gate{font-weight:600;padding:1px 6px;border-radius:4px;font-size:12px}
.PASS{color:var(--pass);background:#dcfce7}.REVIEW{color:var(--rev);background:#fef3c7}.FAIL{color:var(--fail);background:#fee2e2}.UNKNOWN{color:var(--muted);background:#f3f3f3}
.neg{color:var(--fail)}.pos{color:var(--pass)}.star{color:#d97706}
.toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:8px 0}
.toolbar input,.toolbar select{padding:5px 8px;border:1px solid var(--line);border-radius:6px;font:inherit}
button{padding:6px 12px;border:1px solid var(--acc);background:var(--acc);color:#fff;border-radius:6px;font:inherit;cursor:pointer}
button.sec{background:#fff;color:var(--acc)}button:disabled{opacity:.5;cursor:default}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:8px 0 12px}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 12px}.card b{font-size:18px;display:block}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px}@media(max-width:1000px){.grid2{grid-template-columns:1fr}}
.kv td:first-child{color:var(--muted);width:45%}
.chart{width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:8px}
.chart .price{fill:none;stroke:var(--acc);stroke-width:1.6}.chart .rsi{fill:none;stroke:#7c3aed;stroke-width:1.4}
.chart .shade{fill:var(--shade);opacity:.6}.chart .grid{stroke:#e5e7eb}.chart .thr{stroke:#d97706;stroke-dasharray:4 3}
.chart .dot{fill:#7c3aed}.chart .cur{fill:#dc2626}.chart.mini{border:none;background:transparent}
.minis{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:8px;background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px}
.chart .tick{font-size:10px;fill:var(--muted)}.chart .tick.r{text-anchor:end}.chart .lbl{font-size:11px;fill:var(--muted)}
.md{background:#fff;border:1px solid var(--line);border-radius:8px;padding:6px 18px}.md table{width:auto}.md td,.md th{text-align:left;white-space:normal}
pre.log{background:#111;color:#ddd;padding:10px;border-radius:6px;max-height:260px;overflow:auto;font-size:12px}
.status{font-size:12px;padding:1px 6px;border-radius:4px;background:#e0e7ff;color:#3730a3}
.status.new{background:#dcfce7;color:var(--pass);font-weight:600}
</style></head><body>
<header><a href="/" class="{{ 'active' if nav=='candidates' }}">Candidates</a><a href="/watchlist" class="{{ 'active' if nav=='home' }}">Watchlist</a><a href="/all" class="{{ 'active' if nav=='all' }}">All tickers</a>
<a href="/v3" class="{{ 'active' if nav=='v3' }}">Top 10 v3</a>
<a href="/research" class="{{ 'active' if nav=='research' }}">Research</a>
<a href="/study" class="{{ 'active' if nav=='study' }}">Episode study</a><span class="sp"></span>
<span class="muted small">{{ as_of }}</span>
{% if not on_vercel %}<button id="rescan" class="sec" onclick="rescan()">Rescan</button>{% else %}<span class="muted small">read-only deployment: rerun <code>scan.py</code> locally and push to update</span>{% endif %}</header>
<main>{% block body %}{% endblock %}</main>
<script>
function sortTable(th){const t=th.closest('table'),i=[...th.parentNode.children].indexOf(th),asc=!th.classList.contains('asc');
t.querySelectorAll('th').forEach(h=>h.classList.remove('sorted','asc'));th.classList.add('sorted');if(asc)th.classList.add('asc');
const rows=[...t.tBodies[0].rows];rows.sort((a,b)=>{const x=a.cells[i].dataset.v??a.cells[i].textContent,y=b.cells[i].dataset.v??b.cells[i].textContent;
const nx=parseFloat(x),ny=parseFloat(y);const c=(!isNaN(nx)&&!isNaN(ny))?nx-ny:String(x).localeCompare(String(y));return asc?c:-c});
rows.forEach(r=>t.tBodies[0].appendChild(r));}
document.querySelectorAll('table.sortable th').forEach(th=>th.onclick=()=>sortTable(th));
function applyFilters(){const q=(document.getElementById('q')||{}).value?.toLowerCase()||'';const gate=(document.getElementById('gate')||{}).value||'';
const sec=(document.getElementById('sector')||{}).value||'';const act=(document.getElementById('active')||{}).checked;const pri=(document.getElementById('prio')||{}).checked;
let n=0;document.querySelectorAll('table.filterable tbody tr').forEach(tr=>{const d=tr.dataset;let ok=true;
if(q&&!(d.ticker+' '+d.name).toLowerCase().includes(q))ok=false;if(gate&&d.gate!==gate)ok=false;if(sec&&d.sector!==sec)ok=false;
if(act&&d.active!=='1')ok=false;if(pri&&d.prio!=='1')ok=false;tr.style.display=ok?'':'none';if(ok)n++;});
const c=document.getElementById('count');if(c)c.textContent=n+' shown';}
document.querySelectorAll('.toolbar input,.toolbar select').forEach(e=>e.addEventListener('input',applyFilters));
async function rescan(){if(!confirm('Re-run the scan now? Prices older than a day are refreshed; fundamentals older than a week. This takes a few minutes.'))return;
await fetch('/rescan',{method:'POST'});poll();}
async function poll(){const b=document.getElementById('rescan');b.disabled=true;b.textContent='Scanning…';
const r=await (await fetch('/status')).json();const box=document.getElementById('joblog');if(box){box.textContent=r.log;box.scrollTop=box.scrollHeight;}
if(r.running){setTimeout(poll,2000);}else{b.disabled=false;b.textContent='Rescan';if(r.finished)location.reload();}}
if(document.getElementById('rescan'))fetch('/status').then(r=>r.json()).then(r=>{if(r.running)poll();});

</script></body></html>"""

HOME = """{% extends "base" %}{% block body %}
{% if nav=='candidates' %}
<h1>Turnaround candidates <span class="muted small">watchlist rows with survival gate GREEN, monthly RSI &lt; {{ cand_rsi_max|num(0) }}, and revenue YoY or EPS last-quarter YoY ≥ {{ (cand_growth_min*100)|num(0) }}% · {{ rows|length }} of {{ total }} watchlist names · <a href="/watchlist">full watchlist</a></span></h1>
{% else %}
<h1>Turnaround watchlist <span class="muted small">monthly RSI({{ meta.rsi_period }}) &lt; {{ meta.threshold|num(0) }} on the last completed month, or within the last {{ meta.lookback }} months · {{ meta.universe }}</span></h1>
{% endif %}
<div class="cards">
<div class="card"><span class="muted">{{ 'candidates' if nav=='candidates' else 'qualifiers' }}</span><b>{{ rows|length }}</b></div>
<div class="card"><span class="muted">new since last scan</span><b class="pos">{{ rows|selectattr(newflag)|list|length }}</b></div>
<div class="card"><span class="muted">below {{ meta.threshold|num(0) }} now</span><b>{{ rows|selectattr('oversold_now')|list|length }}</b></div>
<div class="card"><span class="muted">drawdown &gt; 40%</span><b>{{ rows|selectattr('priority')|list|length }}</b></div>
<div class="card"><span class="muted">survival GREEN</span><b class="pos">{{ gates.get('PASS',0) }}</b></div>
<div class="card"><span class="muted">REVIEW / FAIL</span><b>{{ gates.get('REVIEW',0) }} / {{ gates.get('FAIL',0) }}</b></div>
<div class="card"><span class="muted">with thesis file</span><b>{{ rows|selectattr('has_thesis')|list|length }}</b></div>
</div>
<pre id="joblog" class="log" style="display:none"></pre>
<div class="toolbar"><input id="q" placeholder="search ticker / name" size="24">
<label><input type="checkbox" id="active"> below {{ meta.threshold|num(0) }} now only</label>
<label><input type="checkbox" id="prio"> drawdown &gt; 40% only</label>
<span id="count" class="muted small"></span><span class="sp" style="flex:1"></span>
<button id="reset-layout" class="sec">Reset layout</button></div>
<div id="groupbar" class="groupbar"></div>
<div id="grid"></div>
<p class="muted small">Drag a column edge to resize, drag a header to reorder, click a header to sort. The ☰ menu on each header hides it, moves it to the front or back, or shows and hides any column. The filter row under the headers takes an operator (≥, ≤, =, contains…) and a value; percentages are typed as plain numbers (15 means 15%), money as $ millions. Your layout is remembered in this browser. Group by: pick up to three columns; for a numeric column type cut points to bucket it (RSI(m) with "38, 45" gives &lt; 38, 38 – 45 and ≥ 45; a % column takes plain numbers, money takes $ millions; leave the box empty to group by exact value). Click a group header to collapse it; rows inside a group follow the column sort. ★ drawdown beyond 40% from the trailing 5-year high. Survival gate is a proxy from Yahoo statements: GREEN = cash covers 24 months of current FCF burn plus debt due within a year; REVIEW = burn covered but maturities need refinancing; FAIL = cash does not cover 24 months of burn. Runway = cash ÷ monthly burn (∞ when FCF is positive).</p>
<script>
const DATA={{ rows|tojson }};
const THRESH={{ meta.threshold }};
const ADDED='{{ addedfield }}',NEWFLAG='{{ newflag }}';
const COLS=[
 col('ticker','Ticker','text',{frozen:true,width:88,formatter:c=>{const r=c.getRow().getData();return `<a href="/ticker/${r.ticker}"><b>${r.ticker}</b></a>${r.priority?' <span class="star" title="drawdown beyond 40%">★</span>':''}`;}}),
 col('name','Name','text',{width:170}),
 col('sector','Sector','text',{width:150,formatter:c=>`<span class="muted">${c.getValue()||''}</span>`}),
 col('industry','Industry','text',{visible:false,width:170}),
 col('price','Price','num',{d:2,visible:false}),
 col('rsi_m','RSI(m)','num',{formatter:c=>`<span class="${c.getValue()<THRESH?'neg':''}">${fmt.num(c.getValue(),1)}</span>`,tip:'monthly Wilder RSI(14), last completed month'}),
 col('rsi_m_prev','Prev','num',{formatter:c=>`<span class="muted">${fmt.num(c.getValue(),1)}</span>`,tip:'RSI the month before'}),
 col('rsi_partial_month','RSI partial','num',{visible:false,tip:'RSI including the current, incomplete month'}),
 col('episode_min_rsi','Min RSI','num',{visible:false}),
 col('episodes_15y','Episodes 15y','num',{d:0,visible:false}),
 col('ret_3m','3m ret','pct',{good:'up',visible:false}),
 col('ret_12m','12m ret','pct',{good:'up'}),
 col('pct_vs_200dma','vs 200d','pct',{good:'up',visible:false}),
 col('survival_gate','Gate','text',{headerFilterParams:{ops:['=','≠','contains']},formatter:c=>`<span class="gate ${c.getValue()}">${GATE[c.getValue()]||c.getValue()||'–'}</span>`,hozAlign:'center',
   headerFilterFunc:(hv,rv,row,p)=>opFilterFunc(hv,GATE[rv]||rv,row,p),tip:'survival gate: GREEN / REVIEW / FAIL'}),
 col('eps_growth_last_q','EPS Last Q YoY','pct',{good:'up',tip:'latest quarter vs same quarter a year ago'}),
 col('eps_growth_yoy','EPS YoY Prev','pct',{good:'up',tip:'last full fiscal year vs the year before (TTM vs prior TTM when 8 quarters are available)'}),
 col('revenue_yoy_last_q','Rev YoY','pct',{good:'up'}),
 col('pe_forward','P/E fwd','num'),
 col('drawdown_5y','DD 5y','pct',{formatter:c=>`<span class="neg">${fmt.pct(c.getValue())}</span>`,tip:'decline from the trailing 5-year high of daily closes'}),
 col(ADDED,'Added','text',{width:120,headerFilterParams:{ops:['≥','≤','=','contains'],placeholder:'YYYY-MM'},tip:'first scan that listed the ticker on this page; NEW = it was not on this page in the previous scan',
   formatter:c=>{const r=c.getRow().getData();return (r[NEWFLAG]?'<span class="status new">NEW</span> ':'')+`<span class="muted small">${c.getValue()||'–'}</span>`;}}),
 col('episode_months','Months','num',{d:0,formatter:c=>{const r=c.getRow().getData();return r.episode_months+(r.episode_active?'':` <span class="muted small">exit ${r.episode_exit}</span>`);},tip:'consecutive months below the threshold; "exit" = first month back above it'}),
 col('episode_start','Oversold since','text',{headerFilterParams:{ops:['≥','≤','contains','='],placeholder:'YYYY-MM'},tip:'first month below the threshold in the current episode'}),
 col('market_cap','Mkt cap','money'),
 col('adv_3m_usd','ADV$ 3m','money',{tip:'average daily dollar volume, 3 months'}),
 col('runway_months','Runway','num',{d:0,tip:'cash ÷ monthly FCF burn, months (∞ when FCF is positive)'}),
 col('cash','Cash','money',{visible:false}),
 col('total_debt','Total debt','money',{visible:false}),
 col('current_debt','Debt due <1y','money',{visible:false}),
 col('fcf_ttm','FCF TTM','money',{visible:false}),
 col('gap_24m','24m gap','money',{visible:false,tip:'need − cash; negative = surplus'}),
 col('net_debt_to_ebitda','ND/EBITDA','num'),
 col('interest_coverage','Int cov','num',{visible:false}),
 col('pe_trailing','P/E trail','num'),
 col('peg','PEG','num',{d:2}),
 col('p_sales','P/S','num',{d:2}),
 col('ev_to_sales','EV/Sales','num'),
 col('ev_to_ebitda','EV/EBITDA','num'),
 col('p_fcf','P/FCF','num',{visible:false}),
 col('p_book','P/B','num',{visible:false}),
 col('revenue_ttm','Revenue TTM','money',{visible:false}),
 col('dilution_1y','Dilution 1y','pct',{good:'down',tip:'share count change: an increase dilutes you'}),
 col('status','Thesis','text',{headerFilterParams:{ops:['contains','=']},formatter:c=>{const r=c.getRow().getData();return r.has_thesis?`<a href="/ticker/${r.ticker}#thesis"><span class="status">${r.status}</span></a>`:'<span class="muted">—</span>';}}),
];
const table=makeGrid('#grid',COLS,DATA,'watchlist-v5',{initialSort:[{column:'drawdown_5y',dir:'asc'}]});
quickFilters(table,r=>{const q=(document.getElementById('q').value||'').toLowerCase();
  if(q&&!((r.ticker||'')+' '+(r.name||'')).toLowerCase().includes(q))return false;
  if(document.getElementById('active').checked&&!r.oversold_now)return false;
  if(document.getElementById('prio').checked&&!r.priority)return false;return true;});
</script>
{% endblock %}"""

ALL = """{% extends "base" %}{% block body %}
<h1>All tickers <span class="muted small">{{ rows|length }} in universe · price screen only</span></h1>
<div class="toolbar"><input id="q" placeholder="search ticker / name" size="24">
<label><input type="checkbox" id="active"> below {{ meta.threshold|num(0) }} now only</label>
<label><input type="checkbox" id="prio"> qualified ({{ meta.lookback }}m) only</label>
<span id="count" class="muted small"></span><span class="sp" style="flex:1"></span>
<button id="reset-layout" class="sec">Reset layout</button></div>
<div id="groupbar" class="groupbar"></div>
<div id="grid"></div>
<p class="muted small">Same controls as the watchlist: resize, drag, sort, ☰ header menu to hide / move / show columns, operator filters under each header. Layout remembered in this browser.</p>
<script>
const DATA={{ rows|tojson }};
const THRESH={{ meta.threshold }};
const COLS=[
 col('ticker','Ticker','text',{frozen:true,width:88,formatter:c=>`<a href="/ticker/${c.getValue()}"><b>${c.getValue()}</b></a>`}),
 col('name','Name','text',{width:170}),
 col('sector','Sector','text',{width:150,formatter:c=>`<span class="muted">${c.getValue()||''}</span>`}),
 col('industry','Industry','text',{visible:false,width:170}),
 col('index','Index','text',{visible:false}),
 col('price','Price','num',{d:2}),
 col('rsi_m','RSI(m)','num',{formatter:c=>`<span class="${c.getValue()<THRESH?'neg':''}">${fmt.num(c.getValue(),1)}</span>`}),
 col('rsi_m_prev','Prev','num',{visible:false}),
 col('rsi_partial_month','RSI partial','num',{formatter:c=>`<span class="muted">${fmt.num(c.getValue(),1)}</span>`}),
 col('qualified','Qualified','text',{headerFilterParams:{ops:['=']},formatter:c=>c.getValue()?'yes':'',hozAlign:'center',tip:'below the threshold within the lookback window'}),
 col('episode_start','Oversold since','text',{headerFilterParams:{ops:['≥','≤','contains','='],placeholder:'YYYY-MM'}}),
 col('episode_months','Months','num',{d:0}),
 col('months_since_oversold','Since','num',{d:0,tip:'months since the last month below the threshold'}),
 col('episode_min_rsi','Min RSI','num',{visible:false}),
 col('episodes_15y','Episodes 15y','num',{d:0}),
 col('drawdown_5y','DD 5y','pct',{formatter:c=>`<span class="neg">${fmt.pct(c.getValue())}</span>`}),
 col('high_5y','5y high','num',{d:2,visible:false}),
 col('high_date','High date','text',{visible:false}),
 col('ret_3m','3m','pct',{good:'up'}),
 col('ret_12m','12m','pct',{good:'up'}),
 col('pct_vs_200dma','vs 200d','pct',{good:'up'}),
 col('adv_3m_usd','ADV$ 3m','money'),
 col('years_history','Years','num',{d:1}),
 col('first_bar','First bar','text',{visible:false}),
];
const table=makeGrid('#grid',COLS,DATA,'alltickers',{initialSort:[{column:'drawdown_5y',dir:'asc'}]});
quickFilters(table,r=>{const q=(document.getElementById('q').value||'').toLowerCase();
  if(q&&!((r.ticker||'')+' '+(r.name||'')).toLowerCase().includes(q))return false;
  if(document.getElementById('active').checked&&!r.oversold_now)return false;
  if(document.getElementById('prio').checked&&!r.qualified)return false;return true;});
</script>
{% endblock %}"""

TICKER = """{% extends "base" %}{% block body %}
<h1>{{ t }} <span class="muted">{{ name }}</span>{% if r.priority %} <span class="star">★</span>{% endif %}
{% if r.survival_gate %}<span class="gate {{ r.survival_gate }}">{{ r.survival_gate|gate }}</span>{% endif %}</h1>
<p class="muted small">{{ r.sector or f.sector_y or '' }} · {{ r.industry or f.industry_y or '' }} · last bar {{ r.last_bar }} · price {{ r.price|num(2) }}</p>
{{ chart|safe }}
{% if v3 %}
<h2>Strategy v3 <span class="muted small">{% if v3.in_top10 %}<b class="pos">top 10, buy order {{ v3.value_rank }}</b>{% else %}growth rank {{ v3.growth_rank }} of 20, not in the top 10{% endif %} · screen dated {{ v3d.date }} · <a href="/v3">the list</a></span></h2>
<div class="grid2">
<div><table class="kv">
<tr><td>Growth rank · TTM revenue growth</td><td>{{ v3.growth_rank }} · {{ v3.rev_yoy|pctc }} <span class="muted">(a year earlier {{ v3.prior_yoy|pct }})</span></td></tr>
<tr><td>Valuation percentile (P/S · EV/EBITDA · EV/EBIT)</td><td><b>{{ v3.val_pct_op|num(3) }}</b> <span class="muted">= mean of {{ v3.ps_pct|num(2) }} · {{ v3.ev_ebitda_pct|num(2) }} · {{ v3.ev_ebit_pct|num(2) }}; v2 percentile with P/E {{ v3.val_pct|num(3) }}</span></td></tr>
<tr><td>P/S · EV/EBITDA · EV/EBIT · P/E</td><td>{{ v3.ps|num(2) }} · {{ v3.ev_ebitda|num }} · {{ v3.ev_ebit|num }} · {{ v3.pe|num }}</td></tr>
<tr><td>Monthly RSI now · lowest in 6 months · from 5y high</td><td>{{ v3.rsi_m|num }} · {{ v3.rsi_min6|num }} · <span class="neg">{{ v3.dd5|pct }}</span></td></tr>
<tr><td>Close used · market cap · quarter</td><td>{{ v3.close|num(2) }} · {{ v3.mcap|money }} · {{ v3.q_end }}</td></tr>
</table></div>
<div><table class="kv">
<tr><td>TTM EPS at entry · a year ago · change</td><td><b>{{ v3.eps_ttm|num(2) }}</b> · {{ v3.eps_1y|num(2) }} · {{ v3.eps_chg_1y|pctc }}</td></tr>
<tr><td>EPS path, last six quarters (oldest first)</td><td>{{ v3.eps_path_s or '–' }}</td></tr>
<tr><td>Guide-cut trigger (85% of entry EPS, 12 months)</td><td><b>{{ v3.eps_guidecut_trigger|num(2) }}</b></td></tr>
<tr><td>Trim price (+50%)</td><td>{{ v3.trim_price|num(2) }}</td></tr>
<tr><td>One-off guard: net income / operating income</td><td>{{ v3.ni_op|num(2) }} <span class="muted">(rejects above 1.0; largest one-quarter jump in TTM net income {{ v3.ni_jump4|num(2) }}x, operating income {{ v3.op_jump4|num(2) }}x)</span></td></tr>
<tr><td>Acquisition guard: diluted shares y/y · net debt / EBITDA</td><td>{{ v3.shares_yoy|pctc('down') }} <span class="muted">(rejects above +15%)</span> · {{ v3.nd_ebitda|num }}</td></tr>
</table></div></div>
{% endif %}
<div class="grid2">
<div><h2>Screen facts</h2><table class="kv">
<tr><td>Monthly RSI (last completed / prev / partial month)</td><td>{{ r.rsi_m|num }} / {{ r.rsi_m_prev|num }} / {{ r.rsi_partial_month|num }}</td></tr>
<tr><td>Qualification date (first month with RSI below {{ meta.threshold|num(0) }})</td><td>{{ r.episode_start }}</td></tr>
<tr><td>Episode months / min RSI / exit</td><td>{{ r.episode_months }} / {{ r.episode_min_rsi|num }} / {{ r.episode_exit or 'still active' }}</td></tr>
<tr><td>Distress episodes in 15 years</td><td>{{ r.episodes_15y }}</td></tr>
<tr><td>Drawdown from 5-year high</td><td class="neg">{{ r.drawdown_5y|pct }} <span class="muted">(high {{ r.high_5y }} on {{ r.high_date }})</span></td></tr>
<tr><td>Return, last 3 months</td><td>{{ r.ret_3m|pctc }}</td></tr>
<tr><td>Return, last 12 months</td><td>{{ r.ret_12m|pctc }}</td></tr>
<tr><td>Price vs 200-day moving average</td><td>{{ r.pct_vs_200dma|pctc }}</td></tr>
<tr><td>Avg daily $ volume (3m) · history</td><td>{{ r.adv_3m_usd|money }} · {{ r.years_history }} y (since {{ r.first_bar }})</td></tr>
</table>
<h2>Survival gate <span class="muted small">(proxy, statements to {{ f.bs_date }})</span></h2><table class="kv">
<tr><td>Cash &amp; short-term investments</td><td>{{ f.cash|money }}</td></tr>
<tr><td>Total debt · due within 12 months · leases</td><td>{{ f.total_debt|money }} · {{ f.current_debt|money }} · {{ f.lease_obligations|money }}</td></tr>
<tr><td>Operating cash flow (TTM, {{ f.ttm_quarters }} quarters)</td><td>{{ f.ocf_ttm|moneyc }}</td></tr>
<tr><td>Free cash flow (TTM)</td><td>{{ f.fcf_ttm|moneyc }}</td></tr>
<tr><td>Annual cash burn · runway</td><td>{{ f.fcf_burn_annual|moneyc('down') }} · {{ f.runway_months|num(0) }} months</td></tr>
<tr><td>24-month need (2 × burn + debt due within a year)</td><td>{{ f.need_24m|money }}</td></tr>
<tr><td>Funding gap (need − cash; negative = surplus)</td><td><b>{{ f.gap_24m|moneyc('down') }}</b></td></tr>
<tr><td>Net debt / EBITDA</td><td>{{ f.net_debt_to_ebitda|num }}</td></tr>
<tr><td>Interest coverage (EBIT ÷ interest)</td><td>{{ f.interest_coverage|num }}</td></tr>
<tr><td>Cash / total debt</td><td>{{ f.cash_to_debt|num(2) }}</td></tr>
<tr><td>Share count change, 1 year (increase = dilution)</td><td>{{ f.dilution_1y|pctc('down') }}</td></tr>
<tr><td>Buybacks · stock issuance (TTM)</td><td>{{ f.buybacks_ttm|money }} · {{ f.stock_issuance_ttm|money }}</td></tr>
</table></div>
<div><h2>Price assessment <span class="muted small">(TTM)</span></h2><table class="kv">
<tr><td>Market cap · enterprise value</td><td>{{ f.market_cap|money }} · {{ f.ev|money }}</td></tr>
<tr><td>Revenue · EBITDA · net income</td><td>{{ f.revenue_ttm|money }} · {{ f.ebitda_ttm|money }} · {{ f.net_income_ttm|money }}</td></tr>
<tr><td>P/E trailing · P/E forward · PEG</td><td><b>{{ f.pe_trailing|num }}</b> · <b>{{ f.pe_forward|num }}</b> · <b>{{ f.peg|num(2) }}</b></td></tr>
<tr><td>P/S · EV/Sales · EV/EBITDA · P/FCF · P/B</td><td><b>{{ f.p_sales|num(2) }}</b> · {{ f.ev_to_sales|num }} · {{ f.ev_to_ebitda|num }} · {{ f.p_fcf|num }} · {{ f.p_book|num }}</td></tr>
<tr><td>EPS, trailing 12 months</td><td>{{ f.eps_ttm|numc(2) }}</td></tr>
<tr><td>EPS, forward estimate (analyst consensus)</td><td>{{ f.eps_forward|numc(2) }}</td></tr>
<tr><td>EPS growth implied by the forward estimate</td><td>{{ f.eps_forward_growth|pctc }}</td></tr>
<tr><td>EPS growth, latest quarter vs same quarter last year<br><span class="small">({{ epsg.q_label }})</span></td>
<td>{{ epsg.q_now|numc(2) }} vs {{ epsg.q_ago|numc(2) }} → <b>{{ f.eps_growth_last_q|pctc }}</b></td></tr>
<tr><td>EPS growth, last full {{ 'twelve months vs the twelve before' if f.eps_growth_basis == 'ttm' else 'fiscal year vs the year before' }}<br><span class="small">({{ epsg.y_label }})</span></td>
<td>{{ epsg.y_now|numc(2) }} vs {{ epsg.y_ago|numc(2) }} → <b>{{ f.eps_growth_yoy|pctc }}</b>{% if epsg.note %} <span class="muted small">{{ epsg.note }}</span>{% endif %}</td></tr>
<tr><td>Yahoo earnings growth (latest quarter, YoY)</td><td>{{ f.earnings_growth_y|pctc }}</td></tr>
<tr><td>Revenue growth, latest quarter vs same quarter last year</td><td>{{ f.revenue_yoy_last_q|pctc }}</td></tr>
<tr><td>Profitable years / reported</td><td>{{ f.profitable_years }} / {{ f.years_reported }}</td></tr>
</table>
<h2>Recent quarters <span class="muted small">(recovery evidence: demand + margin)</span></h2>
<table><thead><tr><th class="l">Quarter</th><th>Revenue</th><th>Gross margin</th><th>Diluted EPS</th><th>EPS YoY</th></tr></thead><tbody>
{% for q in quarters %}<tr><td class="l">{{ q.period }}</td><td>{{ q.revenue|money }}</td><td>{{ q.gm|pct(false) }}</td><td>{{ q.eps|numc(2) }}</td><td>{{ q.eps_yoy|pctc }}</td></tr>{% endfor %}
</tbody></table>
<h2>Annual</h2><table><thead><tr><th class="l">Year</th><th>Revenue</th><th>Net income</th><th>Diluted EPS</th></tr></thead><tbody>
{% for a in f.annual or [] %}<tr><td class="l">{{ a.year }}</td><td>{{ a.revenue|money }}</td><td>{{ a.net_income|moneyc }}</td><td>{{ a.eps|numc(2) }}</td></tr>{% endfor %}
</tbody></table></div></div>
<h2>Valuation history <span class="muted small">current multiple against its own past</span></h2>
{% if vhist.metrics %}
<table><thead><tr><th class="l">Multiple</th><th>Now</th><th>Average</th><th>Median</th><th>5y average</th><th>High</th><th>Low</th><th>Now vs avg</th><th>Percentile</th><th class="l">History</th></tr></thead><tbody>
{% for k in ['pe','fwd_pe','peg','ev_ebitda','ps'] %}{% set m = vhist.metrics[k] %}{% set st = m.stats %}
<tr><td class="l">{{ m.label }}</td>
{% if st.n %}<td><b>{{ st.current|num }}</b></td><td>{{ st.avg|num }}</td><td>{{ st.median|num }}</td><td>{{ st.avg_5y|num }}</td><td>{{ st.high|num }}</td><td>{{ st.low|num }}</td>
<td>{{ st.vs_avg|pctc('down') }}</td><td>{{ (st.percentile * 100)|round|int if st.percentile is not none else '–' }}{{ 'th' if st.percentile is not none }}</td>
<td class="l muted small">{{ st.n }} pts, {{ st.source }}, {{ st.from }} → {{ st.to }}</td>
{% else %}<td colspan="9" class="l muted">no history</td>{% endif %}</tr>{% endfor %}
</tbody></table>
<div class="minis" style="margin-top:8px">{% for k in ['pe','fwd_pe','peg','ev_ebitda','ps'] %}{{ vcharts[k]|safe }}{% endfor %}</div>
<p class="muted small">Line = monthly multiple reconstructed from the month-end price and the trailing-twelve-month EPS, revenue, EBITDA, debt, cash and share count that were public at that date, taken from the company's SEC filings (US filers, back to about 2008; Yahoo's 4–5 annual reports are the fallback for non-US filers). EBITDA is operating income plus D&amp;A, or pre-tax income plus interest plus D&amp;A when no operating-income line is reported. Dots = Yahoo's own quarterly and trailing snapshots. Dashed = average, grey = median, red = now. "Now vs avg" is green when the current multiple is below its average. Forward P/E and PEG need historical analyst estimates, which Yahoo does not keep, so they show snapshots only. Multiples are undefined (gaps) while earnings or EBITDA are negative, and a near-zero earnings year produces extreme values, which is why the median is shown and the charts clip at 3× median.</p>
{% else %}<p class="muted">Valuation history unavailable{% if vhist.error %}: {{ vhist.error }}{% endif %}.</p>{% endif %}
<h2 id="thesis">Research file{% if theses|length > 1 %}s{% endif %}{% if theses %} <span class="muted small"><a href="/doc/{{ theses[0].rel|urlencode }}">{{ theses[0].label }}/{{ t }}.md</a> · <a href="/research">all research</a></span>{% endif %}</h2>
{% if theses %}<div class="md">{{ theses[0].html|safe }}</div>
{% for th in theses[1:] %}<details style="margin-top:12px"><summary class="muted">Also: {{ th.label }}/{{ t }}.md</summary><div class="md">{{ th.html|safe }}</div></details>{% endfor %}
<p class="muted small">Edit the file in your editor; this page re-renders it on refresh.</p>
{% elif on_vercel %}<p class="muted small">No research file yet. Create one locally with <code>python scan.py --init-thesis {{ t }}</code> and push.</p>
{% else %}<form method="post" action="/thesis/{{ t }}"><button>Create thesis file from template</button> <span class="muted small">pre-fills the screen facts; diagnosis, survival table, indicators, valuation and entry rules are yours to write</span></form>{% endif %}
{% endblock %}"""

V3 = """{% extends "base" %}{% block body %}
<h1>Top 10 · strategy v3 <span class="muted small">backtest v3 <code>both_opval</code>: organic growth, one-off EPS and acquisition guards, top 20 by revenue growth, top 10 by P/S · EV/EBITDA · EV/EBIT percentile versus own history</span></h1>
{% if not d %}<p class="muted">No v3 list found. Run <code>python turnaround_backtest_v3/live_v3.py</code>.</p>{% else %}
<p class="muted small">Screen dated {{ d.date }} (as of {{ d.as_of }}, {{ d.month_end[:7] }} candle{% if d.month_end > d.as_of %}, incomplete{% endif %}) · file <code>{{ d.source_file }}</code>{% if report %} · <a href="/v3/report">full report</a>{% endif %} · <a href="#rules">rules</a></p>
<div class="cards">
<div class="card"><span class="muted">RSI(m) &lt; 42 in 6 months</span><b>{{ d.n_qualified }}</b></div>
<div class="card"><span class="muted">liquid · ≥ $1B</span><b>{{ d.n_mcap }}</b></div>
<div class="card"><span class="muted">profitable</span><b>{{ d.n_profitable }}</b></div>
<div class="card"><span class="muted">organic growth</span><b>{{ d.n_organic }}</b></div>
<div class="card"><span class="muted">after guards</span><b>{{ d.n_eligible }}</b> <span class="muted small">one-off {{ d.n_flag_oneoff }} · acq {{ d.n_flag_acq }}</span></div>
<div class="card"><span class="muted">top 20 → top 10</span><b>{{ d.top20|length }} → {{ d.top10|length }}</b></div>
</div>
<h2>The top 10 <span class="muted small">buy order = valuation rank · 10% of the portfolio each · click a ticker for its page</span></h2>
<div class="toolbar"><span id="count" class="muted small"></span><span class="sp" style="flex:1"></span><button id="reset-layout" class="sec">Reset layout</button></div>
<div id="grid"></div>
<h2>Ranks 11 – 20 <span class="muted small">on the growth list but not bought · ordered by valuation</span></h2>
<div id="grid2"></div>
<p class="muted small">Growth = trailing-twelve-month revenue versus a year earlier (point-in-time filings). Val = mean percentile of today's P/S, EV/EBITDA and EV/EBIT within the company's own monthly history (0 = cheapest ever); the three components follow, then the v2 percentile (P/E, P/S, EV/EBITDA) for reference. RSI(m) is the monthly Wilder RSI(14) on the current candle, min = lowest in the 6-month window. EPS path = point-in-time TTM EPS over the last six quarters, oldest first. Guide-cut trigger = 85% of the entry TTM EPS: the position is sold at the month-end when TTM EPS prints at or below it within 12 months. Trim = price at which half is sold (+50%). Shares y/y and NI/op inc are the acquisition and one-off guard inputs (both must be clear for a name to be listed). Columns can be hidden, moved and filtered like the other grids.</p>
{% if d.removed_by_guards %}
<h2>Struck by the guards <span class="muted small">names that made the reference (v2-rule) top 20 and were rejected</span></h2>
<table class="sortable"><thead><tr><th class="l">Ticker</th><th>Growth</th><th class="l">Guard</th><th class="l">Reason</th></tr></thead><tbody>
{% for r in d.removed_by_guards %}<tr><td class="l"><a href="/ticker/{{ r.ticker }}"><b>{{ r.ticker }}</b></a></td><td>{{ r.rev_yoy|pct }}</td><td class="l">{{ 'one-off EPS' if r.oneoff else '' }}{{ ' + ' if r.oneoff and r.acq }}{{ 'acquisition' if r.acq else '' }}</td><td class="l">{{ r.oneoff or '' }}{{ '; ' if r.oneoff and r.acq }}{{ r.acq or '' }}</td></tr>{% endfor %}
</tbody></table>{% endif %}
{% if d.prev_candle %}
<h2>Sensitivity <span class="muted small">the same screen on the last completed candle ({{ d.prev_candle.month_end }})</span></h2>
<p>Top 10 then: {% for t in d.prev_candle.top10 %}<a href="/ticker/{{ t }}" class="{{ '' if t in top10_set else 'neg' }}"><b>{{ t }}</b></a>{{ ', ' if not loop.last }}{% endfor %}.
{% set gone = d.prev_candle.top10|reject('in', top10_set)|list %}{% set new = top10_set|reject('in', d.prev_candle.top10)|list %}
{% if gone or new %}Since then {{ gone|join(', ') }} dropped out and {{ new|join(', ') }} came in; the other {{ 10 - new|length }} seats are the same.{% else %}Identical to today's list.{% endif %}
{% if d.ref_top10 %}<span class="muted">Reference (v2 rules, same day): {{ d.ref_top10|join(', ') }}.</span>{% endif %}</p>{% endif %}
{% if d.base_rates_12m_2009_2025 %}
<h2>Base rates <span class="muted small">12-month forward returns of past <code>both_opval</code> picks, snapshots 2009 – Sep 2025, buy-and-hold from the snapshot, no portfolio rules</span></h2>
<table><thead><tr><th class="l">Group</th><th>n</th><th>Mean</th><th>Median</th><th>Win rate</th><th>Beat SPY</th><th>10th pct</th><th>90th pct</th><th>Median worst DD in year 1</th></tr></thead><tbody>
{% for k, s in d.base_rates_12m_2009_2025.items() %}<tr><td class="l">{{ br_labels.get(k, k|replace('_', ' ')) }}</td><td>{{ s.n }}</td><td>{{ s.mean|pctc }}</td><td>{{ s.median|pctc }}</td><td>{{ s.win|pct(false) }}</td><td>{{ s.beat_spy|pct(false) }}</td><td>{{ s.p10|pctc }}</td><td>{{ s.p90|pctc }}</td><td class="neg">{{ s.median_mdd|pct }}</td></tr>{% endfor %}
</tbody></table>{% endif %}
<h2 id="rules">Rules</h2>
<div class="md"><ol>
<li><b>Price screen</b>: monthly Wilder RSI(14) below 42 in any of the last 6 monthly candles; 5+ years of history; 3-month average dollar volume ≥ $5M; market cap ≥ $1B. Universe: S&amp;P 500 + 400.</li>
<li><b>Profitable</b>: TTM EPS and net income above zero; at most one losing year among the TTM readings one, two and three years back.</li>
<li><b>Organic growth</b>: TTM revenue growth positive and under 100%; no quarter-to-quarter jump of the TTM figure above 60% in eight quarters; latest quarter not below its year-ago quarter.</li>
<li><b>One-off EPS guard</b>: reject when TTM net income exceeds TTM operating income, or one quarter lifted TTM net income by more than 50% while operating income rose less than 25% (no operating-income tag: a &gt; 50% one-quarter jump in TTM EPS).</li>
<li><b>Acquisition guard</b>: reject when diluted shares are up more than 15% year over year, or growth of 15% or more is at least three times and ten points above the growth a year earlier (recoveries from a decline exempt).</li>
<li><b>Top 20 by TTM revenue growth</b>, then <b>top 10 by the mean percentile of P/S, EV/EBITDA and EV/EBIT</b> versus the company's own history (ties broken by higher growth).</li>
<li><b>Portfolio</b>: 10% per stock, bought at the close of the first trading day after the snapshot; names that leave the list are kept; trim half at +50%; sell at a month-end with monthly RSI ≥ 90; a &gt; 100% winner is sold to fund a new name when cash is short; spin-off re-screen; <b>guidance-cut proxy</b>: sold when TTM EPS is 15% or more below its entry level within 12 months; yearly withdrawals of 5 – 10%. No position cap, no S&amp;P parking, no price stop.</li>
</ol><p class="muted small">Backtest 2004 – Aug 2026: IRR 14.6% vs 9.1% for SPY with the same withdrawals, max drawdown -34% vs -55%, 79% of closed positions positive, median +51%. Details in <code>turnaround_backtest_v3/STRATEGY_both_opval.md</code>. Research tooling, not investment advice.</p></div>
<script>
const TOP10={{ d.top10|tojson }},BENCH={{ d.bench|tojson }};
const COLS=[
 col('value_rank','#','num',{d:0,frozen:true,width:52,tip:'buy order (valuation rank)'}),
 col('ticker','Ticker','text',{frozen:true,width:88,formatter:c=>{const r=c.getRow().getData();return `<a href="/ticker/${r.ticker}"><b>${r.ticker}</b></a>${r.dd5<=-0.4?' <span class="star" title="drawdown beyond 40%">★</span>':''}`;}}),
 col('name','Name','text',{width:170}),
 col('sector','Sector','text',{width:150,formatter:c=>`<span class="muted">${c.getValue()||''}</span>`}),
 col('growth_rank','Growth #','num',{d:0,width:74,tip:'rank by revenue growth among the guard survivors (top 20 listed)'}),
 col('rev_yoy','Growth','pct',{good:'up',tip:'TTM revenue vs a year earlier'}),
 col('val_pct_op','Val','num',{d:3,formatter:c=>`<b>${fmt.num(c.getValue(),3)}</b>`,tip:'mean percentile of P/S, EV/EBITDA, EV/EBIT vs own history (0 = cheapest ever)'}),
 col('ps_pct','P/S pct','num',{d:2}),
 col('ev_ebitda_pct','EV/EBITDA pct','num',{d:2}),
 col('ev_ebit_pct','EV/EBIT pct','num',{d:2}),
 col('val_pct','Val v2','num',{d:3,visible:false,tip:'v2 percentile: mean of P/E, P/S, EV/EBITDA'}),
 col('ps','P/S','num',{d:2}),
 col('ev_ebitda','EV/EBITDA','num'),
 col('ev_ebit','EV/EBIT','num'),
 col('pe','P/E','num'),
 col('rsi_m','RSI(m)','num',{formatter:c=>`<span class="${c.getValue()<42?'neg':''}">${fmt.num(c.getValue(),1)}</span>`,tip:'monthly RSI(14), current candle'}),
 col('rsi_min6','Min RSI 6m','num',{tip:'lowest monthly RSI in the 6-month window'}),
 col('dd5','From 5y high','pct',{formatter:c=>`<span class="neg">${fmt.pct(c.getValue())}</span>`}),
 col('close','Close','num',{d:2,tip:'month-end / latest close used by the screen'}),
 col('mcap','Mkt cap','money'),
 col('eps_ttm','EPS TTM','num',{d:2,tip:'point-in-time trailing EPS at entry'}),
 col('eps_1y','EPS 1y ago','num',{d:2,visible:false}),
 col('eps_chg_1y','EPS Δ 1y','pct',{good:'up'}),
 col('eps_path_s','EPS path (6q)','text',{width:200,tip:'point-in-time TTM EPS, last six quarters, oldest first'}),
 col('eps_guidecut_trigger','Guide-cut trigger','num',{d:2,tip:'85% of entry TTM EPS: sold at the month-end when TTM EPS is at or below this within 12 months'}),
 col('trim_price','Trim price','num',{d:2,tip:'+50% over the screen close: half the position is sold'}),
 col('nd_ebitda','ND/EBITDA','num',{tip:'net debt / TTM EBITDA (negative = net cash)'}),
 col('shares_yoy','Shares y/y','pct',{good:'down',tip:'diluted shares vs a year earlier (acquisition guard: > +15% rejects)'}),
 col('ni_op','NI / op inc','num',{d:2,tip:'TTM net income over TTM operating income (one-off guard: > 1 rejects)'}),
 col('prior_yoy','Growth 1y ago','pct',{visible:false,tip:'TTM revenue growth reported a year earlier (acquisition guard input)'}),
 col('opinc_ttm','Op income TTM','money',{visible:false}),
 col('ni_ttm','Net income TTM','money',{visible:false}),
 col('rev_ttm','Revenue TTM','money',{visible:false}),
 col('q_end','Quarter','text',{width:100,tip:'latest fiscal quarter in the filings'}),
 col('status','Thesis','text',{headerFilterParams:{ops:['contains','=']},formatter:c=>{const r=c.getRow().getData();return r.has_thesis?`<a href="/ticker/${r.ticker}#thesis"><span class="status">${r.status}</span></a>`:'<span class="muted">—</span>';}}),
];
const table=makeGrid('#grid',COLS,TOP10,'v3top10',{initialSort:[{column:'value_rank',dir:'asc'}],height:Math.min(60+TOP10.length*31,420)});
const COLS2=COLS.map(c=>Object.assign({},c));COLS2[0]=col('growth_rank','Growth #','num',{d:0,frozen:true,width:74});COLS2.splice(4,1);
makeGrid('#grid2',COLS2,BENCH,'v3bench',{initialSort:[{column:'val_pct_op',dir:'asc'}],height:Math.min(60+BENCH.length*31,420)});
</script>
{% endif %}
{% endblock %}"""

V3_REPORT = """{% extends "base" %}{% block body %}
<p class="muted small"><a href="/v3">← Top 10 v3</a> · {{ fname }}</p>
<div class="md">{{ html|safe }}</div>
{% endblock %}"""

RESEARCH = """{% extends "base" %}{% block body %}
<h1>Research <span class="muted small">thesis files for the names bought by strategy v3, reports and working notes</span></h1>
<h2>Strategy v3 thesis files <span class="muted small">turnaround_backtest_v3/thesis/</span></h2>
{% if idx.theses %}<table><thead><tr><th>Buy</th><th class="l">Ticker</th><th class="l">Status</th><th>Updated</th><th>Review by</th><th class="l">Research conclusion</th></tr></thead><tbody>
{% for r in idx.theses %}<tr><td>{{ r.order if r.order != 99 else '' }}</td>
<td class="l"><a href="/doc/{{ r.rel|urlencode }}"><b>{{ r.ticker }}</b></a><br><span class="muted small">{{ r.title.split(' — ',1)[-1] }}</span><br><a class="small" href="/ticker/{{ r.ticker }}">ticker page</a></td>
<td class="l"><span class="status">{{ r.status or '?' }}</span></td><td>{{ r.last_updated or '' }}</td><td>{{ r.review_deadline or '' }}</td>
<td class="l small" style="white-space:normal;max-width:760px">{% if r.concl %}{{ r.concl|safe }}{% else %}<span class="muted">no conclusion section yet</span>{% endif %}</td></tr>{% endfor %}
</tbody></table>{% else %}<p class="muted">No thesis files.</p>{% endif %}
<h2>Reports</h2><ul>{% for r in idx.reports %}<li><a href="/doc/{{ r|urlencode }}">{{ r.split('/')[-1][:-3] }}</a></li>{% endfor %}</ul>
<h2>Research notes</h2><ul>{% for r in idx.notes %}<li><a href="/doc/{{ r|urlencode }}">{{ r.split('/')[-1] }}</a></li>{% endfor %}</ul>
{% endblock %}"""

DOC = """{% extends "base" %}{% block body %}
<p class="muted small"><a href="/research">← Research</a>{% for c in crumbs %} / {% if c.href %}<a href="{{ c.href }}">{{ c.name }}</a>{% else %}{{ c.name }}{% endif %}{% endfor %}
{% if ticker %} · <a href="/ticker/{{ ticker }}">ticker page</a>{% endif %}</p>
{% if listing is not none %}<h1>{{ crumbs[-1].name }}</h1><ul>{% for e in listing %}<li><a href="/doc/{{ e.rel|urlencode }}">{{ e.name }}{{ '/' if e.dir }}</a></li>{% else %}<li class="muted">empty</li>{% endfor %}</ul>
{% else %}<div class="md">{{ html|safe }}</div>{% endif %}
{% endblock %}"""

STUDY = """{% extends "base" %}{% block body %}
<h1>Episode study</h1>
{% if html %}<div class="md">{{ html|safe }}</div>{% else %}<p class="muted">No study output yet. Run <code>python episodes.py</code>.</p>{% endif %}
{% endblock %}"""

from jinja2 import DictLoader  # noqa: E402
app.jinja_loader = DictLoader({"base": BASE, "home": HOME, "all": ALL, "ticker": TICKER, "study": STUDY, "v3": V3, "v3_report": V3_REPORT,
                               "research": RESEARCH, "doc": DOC})


# ------------------------------------------------------------------ routes
def _render_watchlist(rows, nav, title, **extra):
    gates = pd.Series([r.get("survival_gate") or "UNKNOWN" for r in rows]).value_counts().to_dict()
    sectors = sorted({r.get("sector") or "" for r in rows} - {""})
    cand = nav == "candidates"
    return render_template_string(HOME, rows=rows, gates=gates, sectors=sectors, as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(),
                                  nav=nav, title=title, cand_rsi_max=CAND_RSI_MAX, cand_growth_min=CAND_GROWTH_MIN,
                                  addedfield="cand_added" if cand else "added", newflag="cand_is_new" if cand else "is_new", **extra)


@app.route("/")
def candidates():
    all_rows = load_watchlist()
    return _render_watchlist([r for r in all_rows if is_candidate(r)], "candidates", "Candidates", total=len(all_rows))


@app.route("/watchlist")
def home():
    return _render_watchlist(load_watchlist(), "home", "Watchlist", total=None)


@app.route("/all")
def all_tickers():
    rows = load_all()
    sectors = sorted({r.get("sector") or "" for r in rows} - {""})
    return render_template_string(ALL, rows=rows, sectors=sectors, as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(), nav="all", title="All tickers")


@app.route("/ticker/<t>")
def ticker(t):
    t = t.upper()
    r = next((x for x in load_watchlist() if x["ticker"] == t), None)
    if r is None:
        r = next((x for x in load_all() if x["ticker"] == t), None)
    if r is None:
        try:
            d = prices.load_many([t])
        except Exception:  # noqa: BLE001
            d = {}
        if t not in d:
            abort(404)
        from scan import price_metrics
        mt = scan_meta()
        r = price_metrics(t, d[t], float(mt["threshold"]), int(mt["lookback"]), None) or {}
    import fundamentals
    try:
        f = fundamentals.get(t)
    except Exception:  # noqa: BLE001
        f = {}
    gm = {q["period"]: q["value"] for q in f.get("gross_margin_quarters", [])}
    eps = {q["period"]: q["value"] for q in f.get("eps_quarters", [])}
    eps_list = f.get("eps_quarters", [])
    eps_yoy = {}
    for i, q in enumerate(eps_list):
        if i + 4 < len(eps_list) and eps_list[i + 4]["value"] and eps_list[i + 4]["value"] > 0:
            eps_yoy[q["period"]] = q["value"] / eps_list[i + 4]["value"] - 1.0
    quarters = [{"period": q["period"], "revenue": q["value"], "gm": gm.get(q["period"]),
                 "eps": eps.get(q["period"]), "eps_yoy": eps_yoy.get(q["period"])} for q in f.get("revenue_quarters", [])]
    # labels for the EPS growth rows: name the periods and the two figures compared
    def _mon(period):
        try:
            return datetime.strptime(period, "%Y-%m-%d").strftime("%b %Y")
        except Exception:  # noqa: BLE001
            return period
    epsg = {"q_label": "n/a", "q_now": None, "q_ago": None, "y_label": "n/a", "y_now": None, "y_ago": None, "note": ""}
    if len(eps_list) >= 5:
        epsg.update(q_label=f"{_mon(eps_list[0]['period'])} vs {_mon(eps_list[4]['period'])}",
                    q_now=eps_list[0]["value"], q_ago=eps_list[4]["value"])
        if eps_list[4]["value"] is not None and eps_list[4]["value"] <= 0:
            epsg["note"] = ""
    annual = f.get("annual") or []
    if f.get("eps_growth_basis") == "ttm" and len(eps_list) >= 8:
        epsg.update(y_label=f"{_mon(eps_list[3]['period'])}–{_mon(eps_list[0]['period'])} vs the prior four quarters",
                    y_now=f.get("eps_ttm"), y_ago=f.get("eps_ttm_prior"))
    elif len(annual) >= 2:
        epsg.update(y_label=f"FY{annual[0]['year']} vs FY{annual[1]['year']}",
                    y_now=annual[0].get("eps"), y_ago=annual[1].get("eps"))
        if annual[1].get("eps") is not None and annual[1]["eps"] <= 0:
            epsg["note"] = "no % shown: the earlier year was a loss"
    try:
        vhist = vh.get(t)
    except Exception as e:  # noqa: BLE001
        vhist = {"metrics": {}, "error": str(e)[:120]}
    vcharts = {k: valuation_chart(vhist["metrics"][k]) if k in vhist.get("metrics", {}) else "" for k in ("pe", "fwd_pe", "peg", "ev_ebitda", "ps")}
    theses = [{"label": label, "html": render_md(tp), "rel": tp.relative_to(ROOT).as_posix()} for tp, label in thesis_files(t)]
    name = r.get("name") or f.get("long_name") or ""
    v3d, v3 = v3_row(t)
    return render_template_string(TICKER, t=t, r=r, f=f, name=name, quarters=quarters, chart=chart_svg(t), epsg=epsg, vhist=vhist, vcharts=vcharts,
                                  theses=theses, v3=v3, v3d=v3d, as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(), nav="", title=t)


@app.route("/v3")
def v3_top10():
    d = load_v3()
    top10_set = [r["ticker"] for r in d["top10"]] if d else []
    br_labels = {"top10": "Top 10 (bought)", "bench_11_20": "Ranks 11-20 (bench)",
                 "top10_val_le_0.10": "Top 10, val ≤ 0.10", "top10_val_0.10_0.25": "Top 10, val 0.10 – 0.25",
                 "top10_val_gt_0.25": "Top 10, val > 0.25", "top10_dd5_worse_than_-60%": "Top 10, 60% or more below 5y high",
                 "top10_dd5_-40_to_-60%": "Top 10, 40 – 60% below 5y high", "top10_dd5_better_than_-40%": "Top 10, less than 40% below 5y high"}
    return render_template_string(V3, d=d, top10_set=top10_set, br_labels=br_labels, report=latest_v3_report() is not None,
                                  as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(), nav="v3", title="Top 10 v3")


@app.route("/v3/report")
def v3_report():
    p = latest_v3_report()
    if p is None:
        abort(404)
    html = markdown(p.read_text(encoding="utf-8"), extensions=["tables"])
    return render_template_string(V3_REPORT, html=html, fname=p.name, as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(), nav="v3", title="v3 report")


@app.route("/research")
def research():
    return render_template_string(RESEARCH, idx=research_index(), as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(),
                                  nav="research", title="Research")


@app.route("/doc/<path:rel>")
def doc(rel):
    p = doc_path(rel)
    if p is None:
        abort(404)
    r = p.relative_to(ROOT.resolve()).as_posix()
    parts = r.split("/")
    crumbs = [{"name": n, "href": "/doc/" + quote("/".join(parts[:i + 1])) if i < len(parts) - 1 else None}
              for i, n in enumerate(parts)]
    ticker = p.stem if p.is_file() and p.parent.name == "thesis" else None
    if p.is_dir():
        listing = [{"name": c.name, "dir": c.is_dir(), "rel": c.relative_to(ROOT.resolve()).as_posix()}
                   for c in sorted(p.iterdir(), key=lambda c: (not c.is_dir(), c.name.lower()))
                   if (c.is_dir() and not c.name.startswith((".", "__"))) or c.suffix.lower() == ".md"]
        return render_template_string(DOC, listing=listing, html=None, crumbs=crumbs, ticker=None, as_of=as_of(),
                                      on_vercel=ON_VERCEL, meta=scan_meta(), nav="research", title=parts[-1])
    return render_template_string(DOC, listing=None, html=render_md(p), crumbs=crumbs, ticker=ticker, as_of=as_of(),
                                  on_vercel=ON_VERCEL, meta=scan_meta(), nav="research", title=p.stem)


@app.route("/thesis/<t>", methods=["POST"])
def make_thesis(t):
    if ON_VERCEL:
        abort(403)
    from scan import init_thesis
    init_thesis(t.upper(), OUT / "watchlist.json")
    return redirect(url_for("ticker", t=t.upper()) + "#thesis")


@app.route("/study")
def study():
    p = OUT / "episodes_summary.md"
    html = markdown(p.read_text(encoding="utf-8"), extensions=["tables"]) if p.exists() else None
    return render_template_string(STUDY, html=html, as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(), nav="study", title="Study")


def _run_scan():
    JOB.update(running=True, log="", started=time.time(), finished=None, rc=None)
    proc = subprocess.Popen([sys.executable, str(HERE / "scan.py")], cwd=HERE, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
    for line in proc.stdout:
        JOB["log"] += line
    proc.wait()
    JOB.update(running=False, finished=time.time(), rc=proc.returncode)


@app.route("/rescan", methods=["POST"])
def rescan():
    if ON_VERCEL:
        return jsonify(ok=False, error="read-only deployment"), 403
    if not JOB["running"]:
        threading.Thread(target=_run_scan, daemon=True).start()
    return jsonify(ok=True)


@app.route("/status")
def status():
    return jsonify(running=JOB["running"], log=JOB["log"][-4000:], finished=JOB["finished"], rc=JOB["rc"])


@app.route("/api/watchlist")
def api_watchlist():
    return jsonify(load_watchlist())


@app.route("/api/candidates")
def api_candidates():
    return jsonify(load_candidates())


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8050
    app.run(host="127.0.0.1", port=port, debug=False)
