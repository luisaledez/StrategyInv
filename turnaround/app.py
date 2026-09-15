"""Local web UI for the turnaround scanner.

  python app.py            # http://localhost:8050

Pages: /            watchlist (sortable, filterable, rescan button)
       /ticker/<T>  screen facts, price + monthly RSI chart, fundamentals, thesis file
       /all         every ticker in the universe with its RSI / drawdown metrics
       /study       historical episode study
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from flask import Flask, abort, jsonify, redirect, render_template_string, request, url_for
from markdown import markdown

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import indicators as ind  # noqa: E402
import prices  # noqa: E402
import valuation_history as vh  # noqa: E402
from paths import ON_VERCEL  # noqa: E402

OUT = HERE / "output"
THESIS = HERE / "thesis"
FUND = HERE / "cache" / "fundamentals"

app = Flask(__name__)
JOB = {"running": False, "log": "", "started": None, "finished": None, "rc": None}


# ------------------------------------------------------------------ data access
def load_watchlist() -> list[dict]:
    p = OUT / "watchlist.json"
    if not p.exists():
        return []
    rows = json.loads(p.read_text(encoding="utf-8"))
    for r in rows:
        r["has_thesis"] = (THESIS / f"{r['ticker']}.md").exists()
        r["status"] = thesis_status(r["ticker"])
    return rows


def load_all() -> list[dict]:
    p = OUT / "screen_all.csv"
    if not p.exists():
        return []
    df = pd.read_csv(p)
    return json.loads(df.to_json(orient="records"))


def thesis_status(ticker: str) -> str | None:
    p = THESIS / f"{ticker}.md"
    if not p.exists():
        return None
    for line in p.read_text(encoding="utf-8").splitlines()[:12]:
        if line.startswith("status:"):
            return line.split(":", 1)[1].split("<!--")[0].strip()
    return "?"


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


app.jinja_env.filters.update(money=money, pct=pct, num=num, pctc=pctc, moneyc=moneyc, numc=numc)


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
// column kinds
function col(field,title,kind,o={}){
  const base={field,title,headerFilter:opFilter,headerFilterFunc:opFilterFunc,headerFilterLiveFilter:true,headerTooltip:o.tip||title,minWidth:60};
  const k={
    text:{headerFilterParams:{ops:TXTOPS},sorter:'string'},
    num:{headerFilterParams:{ops:NUMOPS},sorter:'number',hozAlign:'right',formatter:c=>fmt.num(c.getValue(),o.d==null?1:o.d)},
    pct:{headerFilterParams:{ops:NUMOPS,scale:100,placeholder:'%'},sorter:'number',hozAlign:'right',formatter:c=>`<span class="${o.good?colored(c.getValue(),o.good):''}">${fmt.pct(c.getValue())}</span>`},
    money:{headerFilterParams:{ops:NUMOPS,scale:1e-6,placeholder:'$M'},sorter:'number',hozAlign:'right',formatter:c=>fmt.money(c.getValue())},
  }[kind]||{};
  const {tip,d,good,...rest}=o;const def=Object.assign(base,k,rest);def.headerFilterFuncParams=def.headerFilterParams;return def;}
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
  const table=new Tabulator(el,Object.assign({data,columns,layout:'fitDataFill',height:'calc(100vh - 235px)',
    resizableColumnFit:false,movableColumns:true,columnDefaults:{resizable:true,headerSortTristate:true},
    persistence:{columns:true,sort:true},persistenceID:id,
    placeholder:'No rows match the filters'},extra));
  table.on('dataFiltered',(f,rows)=>{const c=document.getElementById('count');if(c)c.textContent=rows.length+' of '+data.length+' shown';});
  document.getElementById('reset-layout')?.addEventListener('click',()=>{Object.keys(localStorage).filter(k=>k.startsWith('tabulator-'+id)).forEach(k=>localStorage.removeItem(k));location.reload();});
  return table;}
function quickFilters(table,fn){
  const apply=()=>table.setFilter(fn);
  document.querySelectorAll('.toolbar input').forEach(e=>e.addEventListener('input',apply));apply();}
</script>
<style>
.tabulator{font-size:13px;border:1px solid var(--line);border-radius:8px;background:#fff}
.tabulator .tabulator-header .tabulator-col{background:#f3f4f6}
.tabulator .tabulator-header .tabulator-col .tabulator-col-content{padding:5px 6px}
.tabulator-row .tabulator-cell{padding:5px 8px}
.tabulator .tabulator-header-filter .hf{display:flex;gap:2px}
.tabulator .tabulator-header-filter .hf select{width:52px;font-size:11px;padding:1px}
.tabulator .tabulator-header-filter .hf input{flex:1;min-width:40px;font-size:11px;padding:2px 3px}
.tabulator-menu{font-size:13px;max-height:70vh;overflow:auto}
.tabulator-menu .tabulator-menu-item{padding:4px 12px}
.tabulator-row.tabulator-row-even{background:#fafafa}
.tabulator-cell.r{text-align:right}
:root{--bg:#fafafa;--fg:#1a1a1a;--muted:#6b6b6b;--line:#e3e3e3;--acc:#1d4ed8;--pass:#15803d;--rev:#b45309;--fail:#b91c1c;--shade:#fde68a}
*{box-sizing:border-box}body{margin:0;font:14px/1.45 system-ui,Segoe UI,sans-serif;color:var(--fg);background:var(--bg)}
header{display:flex;gap:18px;align-items:center;padding:12px 24px;border-bottom:1px solid var(--line);background:#fff;position:sticky;top:0;z-index:2}
header a{color:var(--fg);text-decoration:none;font-weight:600}header a.active{color:var(--acc)}header .sp{flex:1}
main{padding:20px 24px;max-width:1500px}h1{font-size:20px;margin:0 0 6px}h2{font-size:16px;margin:22px 0 8px}
.muted{color:var(--muted)}.small{font-size:12px}
table{border-collapse:collapse;width:100%;background:#fff;border:1px solid var(--line)}
th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}
th:first-child,td:first-child,td.l,th.l{text-align:left}th{background:#f3f4f6;cursor:pointer;position:sticky;top:49px;user-select:none}
th.sorted::after{content:" ▾"}th.sorted.asc::after{content:" ▴"}
tr:hover td{background:#f8fafc}a{color:var(--acc)}
.gate{font-weight:600;padding:1px 6px;border-radius:4px;font-size:12px}
.PASS{color:var(--pass);background:#dcfce7}.REVIEW{color:var(--rev);background:#fef3c7}.FAIL{color:var(--fail);background:#fee2e2}.UNKNOWN{color:var(--muted);background:#eee}
.neg{color:var(--fail)}.pos{color:var(--pass)}.star{color:#d97706}
.toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:12px 0}
.toolbar input,.toolbar select{padding:5px 8px;border:1px solid var(--line);border-radius:6px;font:inherit}
button{padding:6px 12px;border:1px solid var(--acc);background:var(--acc);color:#fff;border-radius:6px;font:inherit;cursor:pointer}
button.sec{background:#fff;color:var(--acc)}button:disabled{opacity:.5;cursor:default}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:10px 0 18px}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px 12px}.card b{font-size:20px;display:block}
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
</style></head><body>
<header><a href="/" class="{{ 'active' if nav=='home' }}">Watchlist</a><a href="/all" class="{{ 'active' if nav=='all' }}">All tickers</a>
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
<h1>Turnaround watchlist <span class="muted small">monthly RSI({{ meta.rsi_period }}) &lt; {{ meta.threshold|num(0) }} on the last completed month, or within the last {{ meta.lookback }} months · {{ meta.universe }}</span></h1>
<div class="cards">
<div class="card"><span class="muted">qualifiers</span><b>{{ rows|length }}</b></div>
<div class="card"><span class="muted">below {{ meta.threshold|num(0) }} now</span><b>{{ rows|selectattr('oversold_now')|list|length }}</b></div>
<div class="card"><span class="muted">drawdown &gt; 40%</span><b>{{ rows|selectattr('priority')|list|length }}</b></div>
<div class="card"><span class="muted">survival PASS</span><b class="pos">{{ gates.get('PASS',0) }}</b></div>
<div class="card"><span class="muted">REVIEW / FAIL</span><b>{{ gates.get('REVIEW',0) }} / {{ gates.get('FAIL',0) }}</b></div>
<div class="card"><span class="muted">with thesis file</span><b>{{ rows|selectattr('has_thesis')|list|length }}</b></div>
</div>
<pre id="joblog" class="log" style="display:none"></pre>
<div class="toolbar"><input id="q" placeholder="search ticker / name" size="24">
<label><input type="checkbox" id="active"> below {{ meta.threshold|num(0) }} now only</label>
<label><input type="checkbox" id="prio"> drawdown &gt; 40% only</label>
<span id="count" class="muted small"></span><span class="sp" style="flex:1"></span>
<button id="reset-layout" class="sec">Reset layout</button></div>
<div id="grid"></div>
<p class="muted small">Drag a column edge to resize, drag a header to reorder, click a header to sort. The ☰ menu on each header hides it, moves it to the front or back, or shows and hides any column. The filter row under the headers takes an operator (≥, ≤, =, contains…) and a value; percentages are typed as plain numbers (15 means 15%), money as $ millions. Your layout is remembered in this browser. ★ drawdown beyond 40% from the trailing 5-year high. Survival gate is a proxy from Yahoo statements: PASS = cash covers 24 months of current FCF burn plus debt due within a year; REVIEW = burn covered but maturities need refinancing; FAIL = cash does not cover 24 months of burn. Runway = cash ÷ monthly burn (∞ when FCF is positive).</p>
<script>
const DATA={{ rows|tojson }};
const THRESH={{ meta.threshold }};
const COLS=[
 col('ticker','Ticker','text',{frozen:true,width:88,formatter:c=>{const r=c.getRow().getData();return `<a href="/ticker/${r.ticker}"><b>${r.ticker}</b></a>${r.priority?' <span class="star" title="drawdown beyond 40%">★</span>':''}`;}}),
 col('name','Name','text',{width:170}),
 col('sector','Sector','text',{width:150,formatter:c=>`<span class="muted">${c.getValue()||''}</span>`}),
 col('industry','Industry','text',{visible:false,width:170}),
 col('price','Price','num',{d:2,visible:false}),
 col('rsi_m','RSI(m)','num',{formatter:c=>`<span class="${c.getValue()<THRESH?'neg':''}">${fmt.num(c.getValue(),1)}</span>`,tip:'monthly Wilder RSI(14), last completed month'}),
 col('rsi_m_prev','Prev','num',{formatter:c=>`<span class="muted">${fmt.num(c.getValue(),1)}</span>`,tip:'RSI the month before'}),
 col('rsi_partial_month','RSI partial','num',{visible:false,tip:'RSI including the current, incomplete month'}),
 col('episode_start','Oversold since','text',{headerFilterParams:{ops:['≥','≤','contains','='],placeholder:'YYYY-MM'},tip:'first month below the threshold in the current episode'}),
 col('episode_months','Months','num',{d:0,formatter:c=>{const r=c.getRow().getData();return r.episode_months+(r.episode_active?'':` <span class="muted small">exit ${r.episode_exit}</span>`);},tip:'consecutive months below the threshold; "exit" = first month back above it'}),
 col('episode_min_rsi','Min RSI','num',{visible:false}),
 col('episodes_15y','Episodes 15y','num',{d:0,visible:false}),
 col('drawdown_5y','DD 5y','pct',{formatter:c=>`<span class="neg">${fmt.pct(c.getValue())}</span>`,tip:'decline from the trailing 5-year high of daily closes'}),
 col('ret_3m','3m ret','pct',{good:'up',visible:false}),
 col('ret_12m','12m ret','pct',{good:'up'}),
 col('pct_vs_200dma','vs 200d','pct',{good:'up',visible:false}),
 col('survival_gate','Gate','text',{headerFilterParams:{ops:['=','≠','contains']},formatter:c=>`<span class="gate ${c.getValue()}">${c.getValue()||'–'}</span>`,hozAlign:'center'}),
 col('eps_growth_last_q','EPS Last Q YoY','pct',{good:'up',tip:'latest quarter vs same quarter a year ago'}),
 col('eps_growth_yoy','EPS YoY Prev','pct',{good:'up',tip:'last full fiscal year vs the year before (TTM vs prior TTM when 8 quarters are available)'}),
 col('revenue_yoy_last_q','Rev YoY','pct',{good:'up'}),
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
 col('pe_forward','P/E fwd','num'),
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
const table=makeGrid('#grid',COLS,DATA,'watchlist-v2',{initialSort:[{column:'drawdown_5y',dir:'asc'}]});
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
{% if r.survival_gate %}<span class="gate {{ r.survival_gate }}">{{ r.survival_gate }}</span>{% endif %}</h1>
<p class="muted small">{{ r.sector or f.sector_y or '' }} · {{ r.industry or f.industry_y or '' }} · last bar {{ r.last_bar }} · price {{ r.price|num(2) }}</p>
{{ chart|safe }}
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
<h2 id="thesis">Research file <span class="muted small">thesis/{{ t }}.md</span></h2>
{% if thesis_html %}<div class="md">{{ thesis_html|safe }}</div>
<p class="muted small">Edit the file in your editor; this page re-renders it on refresh.</p>
{% elif on_vercel %}<p class="muted small">No research file yet. Create one locally with <code>python scan.py --init-thesis {{ t }}</code> and push.</p>
{% else %}<form method="post" action="/thesis/{{ t }}"><button>Create thesis file from template</button> <span class="muted small">pre-fills the screen facts; diagnosis, survival table, indicators, valuation and entry rules are yours to write</span></form>{% endif %}
{% endblock %}"""

STUDY = """{% extends "base" %}{% block body %}
<h1>Episode study</h1>
{% if html %}<div class="md">{{ html|safe }}</div>{% else %}<p class="muted">No study output yet. Run <code>python episodes.py</code>.</p>{% endif %}
{% endblock %}"""

from jinja2 import DictLoader  # noqa: E402
app.jinja_loader = DictLoader({"base": BASE, "home": HOME, "all": ALL, "ticker": TICKER, "study": STUDY})


# ------------------------------------------------------------------ routes
@app.route("/")
def home():
    rows = load_watchlist()
    gates = pd.Series([r.get("survival_gate") or "UNKNOWN" for r in rows]).value_counts().to_dict()
    sectors = sorted({r.get("sector") or "" for r in rows} - {""})
    return render_template_string(HOME, rows=rows, gates=gates, sectors=sectors, as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(), nav="home", title="Watchlist")


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
    tp = THESIS / f"{t}.md"
    thesis_html = markdown(tp.read_text(encoding="utf-8"), extensions=["tables"]) if tp.exists() else None
    name = r.get("name") or f.get("long_name") or ""
    return render_template_string(TICKER, t=t, r=r, f=f, name=name, quarters=quarters, chart=chart_svg(t), epsg=epsg, vhist=vhist, vcharts=vcharts,
                                  thesis_html=thesis_html, as_of=as_of(), on_vercel=ON_VERCEL, meta=scan_meta(), nav="", title=t)


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


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8050
    app.run(host="127.0.0.1", port=port, debug=False)
