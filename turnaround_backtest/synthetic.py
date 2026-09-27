"""Synthetic "lost decade" data set: the same S&P 500 + 400 stocks re-simulated
over the 1968-1982 market, so the strategy can be tested in a period where
buy-and-hold went nowhere in nominal terms and lost money after inflation.

How the data is made (per random seed):

* Market: the real S&P 500 daily index path (^GSPC, Yahoo) from 1962 to
  August 1982. January 1968 to August 1982 is the test window: the index went
  from 96 to 120 (+1.5%/yr price), fell 48% in 1973-74, and the CPI rose 180%.
* Each stock keeps its own character from real data: beta to the market and
  the distribution of its idiosyncratic daily returns, estimated on 2004-2026
  (or whatever history exists). Its synthetic daily log return is
  beta * market return + a residual drawn by block bootstrap (126-day blocks)
  from its real, demeaned residuals. That keeps single-stock crashes, rebounds
  and half-year momentum/mean-reversion realistic while the market itself is
  the 1970s market.
* Dividends: DIV_YIELD a year, paid quarterly, in AdjClose (the engine credits
  them as cash; the benchmark reinvests them).
* Fundamentals (quarterly, EDGAR-style tables, public 45 days after quarter
  end): revenue grows with that year's CPI inflation plus a persistent real
  growth rate per company plus a share of the stock's own quarterly price
  residual (bad quarters in the stock coincide with weak sales); the net
  margin swings around the company's real margin with the stock's residual and
  the market (a stock that has crashed idiosyncratically shows a profit
  collapse and can turn loss-making); EBITDA, debt, cash and shares are
  scaled from the company's latest real filing. Market cap starts at the
  company's real market cap today, so the $1B / $5M screen thresholds bind the
  same way. Trailing P/E, P/S and EV/EBITDA therefore fall when the price falls
  faster than earnings, which is what the valuation-vs-history rule looks for.
* Inflation: BLS CPI-U annual averages (approximate), used for nominal
  revenue growth and to report real (deflated) results.

    python synthetic.py --seed 0            # writes synthetic/data/{cache,config.json}
    python synthetic_run.py --seeds 0,1,2,3,4
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SCANNER = HERE.parent / "turnaround"
sys.path.insert(0, str(SCANNER))
sys.path.insert(0, str(HERE))

SYN = HERE / "synthetic"
GSPC = SYN / "cache" / "GSPC.csv"
DATA_ROOT = SYN / "data"

PRE_START = "1962-01-01"      # price / fundamentals pre-history (RSI seed, 5-year history rule, valuation history)
TEST_START = "1968-01-01"
TEST_END = "1982-08-31"
DIV_YIELD = 0.035
BLOCK = 126
MARGIN_SENS = 4.0   # net margin = real margin * (1 + MARGIN_SENS * mu); mu tracks the stock's and the market's returns
# BLS CPI-U, annual average percent change (approximate)
CPI = {1962: 1.0, 1963: 1.3, 1964: 1.3, 1965: 1.6, 1966: 2.9, 1967: 3.1, 1968: 4.2, 1969: 5.5, 1970: 5.7,
       1971: 4.4, 1972: 3.2, 1973: 6.2, 1974: 11.0, 1975: 9.1, 1976: 5.8, 1977: 6.5, 1978: 7.6, 1979: 11.3,
       1980: 13.5, 1981: 10.3, 1982: 6.2}


def market_path() -> pd.DataFrame:
    if not GSPC.exists():
        import yfinance as yf
        raw = yf.download("^GSPC", period="max", interval="1d", auto_adjust=False, progress=False)
        if isinstance(raw.columns, pd.MultiIndex):
            raw.columns = raw.columns.get_level_values(0)
        raw = raw.rename(columns={"Adj Close": "AdjClose"})[["Open", "High", "Low", "Close", "AdjClose", "Volume"]]
        raw.index = pd.to_datetime(raw.index).tz_localize(None).normalize()
        raw.index.name = "Date"
        GSPC.parent.mkdir(parents=True, exist_ok=True)
        raw.to_csv(GSPC)
    g = pd.read_csv(GSPC, index_col="Date", parse_dates=True)
    return g.loc[PRE_START:TEST_END]


# ------------------------------------------------------------------ real-data character
def stock_profile(t: str, spy: pd.Series, real_prices, real_edgar) -> dict | None:
    d = real_prices(t)
    if d is None or len(d) < 500:
        return None
    c = d["Close"].loc["2004-01-01":]
    if len(c) < 500:
        c = d["Close"]
    r = np.log(c).diff().dropna()
    m = np.log(spy).diff().reindex(r.index).dropna()
    r = r.reindex(m.index)
    ok = r.notna() & m.notna() & (r.abs() < 0.5)
    r, m = r[ok].to_numpy(), m[ok].to_numpy()
    if len(r) < 400:
        return None
    beta = float(np.cov(r, m)[0, 1] / np.var(m))
    beta = float(np.clip(beta, 0.3, 2.5))
    resid = r - beta * m
    resid = resid - resid.mean()
    q = [x for x in real_edgar(t) if x.get("rev_ttm") and x.get("shares")]
    last = q[-1] if q else None
    price_now = float(d["Close"].iloc[-1])
    if last:
        shares = float(last["shares"])
        mcap = price_now * shares
        rev = float(last["rev_ttm"])
        ni = float(last.get("ni_ttm") or 0.0)
        ebitda = float(last.get("ebitda_ttm") or 0.0)
        debt = float(last.get("debt") or 0.0)
        cash = float(last.get("cash") or 0.0)
    else:
        mcap, rev, ni, ebitda, debt, cash = 5e9, 3e9, 2e8, 4e8, 1e9, 5e8
    ni_margin = ni / rev if rev > 0 else 0.06
    ni_margin = float(np.clip(ni_margin, 0.02, 0.30)) if ni_margin > 0 else 0.04
    eb_margin = ebitda / rev if rev > 0 and ebitda > 0 else ni_margin * 2.2
    eb_margin = float(np.clip(eb_margin, ni_margin + 0.03, 0.60))
    ps = mcap / rev if rev > 0 else 2.0
    return {"ticker": t, "beta": beta, "resid": resid, "mcap": max(mcap, 3e8), "ps": float(np.clip(ps, 0.4, 12.0)),
            "ni_margin": ni_margin, "eb_margin": eb_margin,
            "debt_to_rev": float(np.clip(debt / rev if rev > 0 else 0.3, 0.0, 3.0)),
            "cash_to_rev": float(np.clip(cash / rev if rev > 0 else 0.1, 0.0, 2.0))}


def block_bootstrap(resid: np.ndarray, n: int, rng: np.random.Generator, block: int = BLOCK) -> np.ndarray:
    out = np.empty(n)
    i = 0
    L = len(resid)
    while i < n:
        s = rng.integers(0, max(1, L - block))
        k = min(block, n - i)
        out[i:i + k] = resid[s:s + k]
        i += k
    return out


# ------------------------------------------------------------------ generation
def generate(seed: int, tickers: list[str], root: Path = DATA_ROOT, verbose: bool = True) -> dict:
    import data as real_data
    import screen as real_screen

    rng = np.random.default_rng(seed)
    g = market_path()
    cal = g.index
    mret = np.log(g["Close"]).diff().fillna(0.0).to_numpy()
    n = len(cal)
    spy_real = real_data.load_prices("SPY")["Close"]

    prices_dir = root / "cache" / "prices"
    edgar_dir = root / "cache" / "edgar"
    for d in (prices_dir, edgar_dir):
        d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*"):
            f.unlink()

    # quarter ends and per-day inflation
    q_ends = pd.date_range(cal[0], cal[-1], freq="QE")
    year_infl = np.array([CPI[d.year] / 100.0 for d in cal])
    day_pos = {d: i for i, d in enumerate(cal)}
    q_idx = [cal.searchsorted(qe, side="right") - 1 for qe in q_ends]   # last trading day <= quarter end

    # market benchmark file (index level, dividends reinvested in AdjClose)
    idx = g["Close"].to_numpy()
    _write_prices(prices_dir / "SPY.csv", cal, idx, rng, shares=None, dividends=True)

    profiles = 0
    for k, t in enumerate(tickers, 1):
        p = stock_profile(t, spy_real, real_data.load_prices, real_screen.load_edgar)
        if p is None:
            continue
        profiles += 1
        resid = block_bootstrap(p["resid"], n, rng)
        lr = p["beta"] * mret + resid
        lr[0] = 0.0
        p0 = float(rng.uniform(15.0, 60.0))
        px = p0 * np.exp(np.cumsum(lr))
        shares = p["mcap"] / p0
        _write_prices(prices_dir / f"{t}.csv", cal, px, rng, shares=shares, dividends=True)
        _write_fundamentals(edgar_dir / f"{t}.json", t, p, cal, px, resid, mret, year_infl, q_ends, q_idx, shares, rng)
        if verbose and k % 100 == 0:
            print(f"  synthetic {k}/{len(tickers)}", file=sys.stderr, flush=True)

    cfg = {"synthetic": True, "seed": seed, "start": TEST_START, "end": TEST_END, "benchmark": "Index",
           "label": f"Synthetic lost decade (1968-1982 market, seed {seed})",
           "cpi": CPI, "div_yield": DIV_YIELD,
           "notes": [
               "**Synthetic data.** The market is the real S&P 500 daily path from 1962 to August 1982 (Yahoo ^GSPC); "
               "each of today's S&P 500 + 400 stocks is re-simulated on it with its own real beta and a block bootstrap "
               "of its own real idiosyncratic daily returns (2004-2026), so single-stock crashes and rebounds are "
               "realistic while the market goes nowhere. Quarterly fundamentals are generated: revenue grows with CPI "
               "inflation plus a company-specific real rate plus part of the stock's own price residual; net margins "
               "swing with the stock's residual and the market and can turn negative; EBITDA, debt, cash, shares and "
               "the starting market cap are scaled from each company's latest real filing. Dividend yield "
               f"{DIV_YIELD:.1%}. The benchmark 'Index' is the S&P 500 price path with the same dividends reinvested.",
               "**Read it as a stress test, not a forecast.** Nothing in the generated fundamentals knows the future price, "
               "and nothing in the prices knows the fundamentals beyond the contemporaneous link above, so the selection "
               "rules cannot cheat. Real (inflation-adjusted) figures use BLS CPI-U annual averages: the CPI rose about "
               "180% over the window, so a nominal result must roughly triple just to stand still.",
           ]}
    (root / "config.json").write_text(json.dumps(cfg, indent=1), encoding="utf-8")
    if verbose:
        print(f"synthetic: seed {seed}, {profiles} stocks generated into {root}", file=sys.stderr)
    return cfg


def _write_prices(path: Path, cal: pd.DatetimeIndex, px: np.ndarray, rng: np.random.Generator,
                  shares: float | None, dividends: bool) -> None:
    n = len(cal)
    # quarterly dividend on the first trading day of Mar/Jun/Sep/Dec
    div = np.zeros(n)
    if dividends:
        months = cal.month
        for i in range(1, n):
            if months[i] in (3, 6, 9, 12) and months[i - 1] != months[i]:
                div[i] = px[i - 1] * DIV_YIELD / 4.0
    adj = np.empty(n)
    adj[0] = px[0]
    for i in range(1, n):
        adj[i] = adj[i - 1] * (px[i] + div[i]) / px[i - 1]
    noise = rng.normal(0, 0.006, n)
    hi = px * (1 + np.abs(noise)); lo = px * (1 - np.abs(noise))
    op = np.roll(px, 1); op[0] = px[0]
    vol = (0.005 * (shares if shares else 1e9 / px.mean()) * np.exp(rng.normal(0, 0.3, n))).round()
    df = pd.DataFrame({"Open": op, "High": hi, "Low": lo, "Close": px, "AdjClose": adj, "Volume": vol}, index=cal)
    df.index.name = "Date"
    df.round(4).to_csv(path)


def _write_fundamentals(path: Path, t: str, p: dict, cal, px, resid, mret, year_infl, q_ends, q_idx, shares, rng) -> None:
    g_real = float(rng.normal(0.02, 0.04))                     # persistent real growth per company
    rev_ttm0 = p["mcap"] / p["ps"]
    rev_q = rev_ttm0 / 4.0
    mu = 0.0
    rows = []
    hist_rev, hist_ni, hist_eb = [], [], []
    prev_i = 0
    for qi, (qe, i) in enumerate(zip(q_ends, q_idx)):
        if i <= 0:
            continue
        e_q = float(resid[prev_i + 1:i + 1].sum())               # the stock's own log return this quarter
        m_q = float(mret[prev_i + 1:i + 1].sum())                # the market's
        infl = float(year_infl[i])
        g_q = (infl + g_real) / 4.0 + 0.10 * e_q + 0.10 * m_q + float(rng.normal(0, 0.015))
        rev_q *= np.exp(g_q)
        mu = 0.7 * mu + 0.35 * (e_q + m_q) + float(rng.normal(0, 0.06))
        ni_margin = p["ni_margin"] * (1.0 + MARGIN_SENS * mu)
        eb_margin = p["eb_margin"] + (ni_margin - p["ni_margin"])
        hist_rev.append(rev_q); hist_ni.append(rev_q * ni_margin); hist_eb.append(rev_q * eb_margin)
        prev_i = i
        if len(hist_rev) < 4:
            continue
        rev_ttm = float(sum(hist_rev[-4:])); ni_ttm = float(sum(hist_ni[-4:])); eb_ttm = float(sum(hist_eb[-4:]))
        end = qe.date().isoformat()
        avail = (qe + pd.Timedelta(days=45)).date().isoformat()
        rows.append({"end": end, "available": avail, "eps_ttm": ni_ttm / shares, "ni_ttm": ni_ttm,
                     "rev_ttm": rev_ttm, "ebitda_ttm": eb_ttm if eb_ttm > 0 else None,
                     "debt": rev_ttm * p["debt_to_rev"], "cash": rev_ttm * p["cash_to_rev"], "shares": shares})
    path.write_text(json.dumps({"ticker": t, "synthetic": True, "quarters": rows}, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--root", default=str(DATA_ROOT))
    args = ap.parse_args()
    import data as real_data
    generate(args.seed, real_data.universe_tickers(), Path(args.root))
