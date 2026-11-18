"""HTML comps of P1 and P2 at 1920 x 1080 in the Goodnight Inn 3.0 kit.

Restyles the current build (opzet) without changing its analysis: every figure
comes from project/design-prototypes/opzet-data.json (the offline decode) and
is re-derived from the model at stage 4/6 before it ships. The comps are a
design target for opzet_report.py, not the report.

Run:
  python project/tools/comps_v3.py <out_dir> [font_dir] [night|night-glow|flat]
font_dir (optional) holds open-sans-latin-{400,600,700}-normal.woff2; when given
they are embedded so the comp renders the same everywhere (Open Sans is the
closest open stand-in for Segoe UI). The page asks for Segoe UI first.
"""
import base64, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(os.path.join(ROOT, "design-prototypes", "opzet-data.json"), encoding="utf-8"))
OUT = sys.argv[1]
FONTDIR = sys.argv[2] if len(sys.argv) > 2 else None
VARIANT = sys.argv[3] if len(sys.argv) > 3 else "night"    # night (the spec) | night-glow (optional) | flat (3.0)
assert VARIANT in ("flat", "night", "night-glow"), VARIANT
LOGO = os.path.join(os.path.dirname(ROOT), "design", "brand-kits", "goodnight-inn-wakeup", "assets", "gi-lockup-reversed.svg")

C = dict(canvas="#F3F1EA", white="#FFFFFF", night="#12233D", dusk="#4B5466", seam="#E3DFD3",
         oat="#E9E5D6", muted="#9AA3B5", deep="#1763A8", coffee="#2589D8", ice="#EAF2FB",
         burnt="#A63F0E", tang="#E05A22", tint="#FCE6DB", grey="#8E897D", greyl="#C9C4B7", chip="#EEEBE2")
BRANDS = ["Goodnight Inn", "P&K Select", "Maison d'Or", "Pebble & Pine"]
MINUS = "−"


def fonts_css():
    if not FONTDIR:
        return ""
    css = ""
    for w in (400, 600, 700):
        p = os.path.join(FONTDIR, f"open-sans-latin-{w}-normal.woff2")
        b = base64.b64encode(open(p, "rb").read()).decode()
        css += f"@font-face{{font-family:'Open Sans';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2')}}\n"
    return css


def sgn(v, d=1, unit="", money=False):
    s = MINUS if v < 0 else "+"
    a = abs(v)
    return f"{s}${a:.{d}f}{unit}" if money else f"{s}{a:.{d}f}{unit}"


CSS = """
*{box-sizing:border-box}
body{margin:0;background:#d9d5ca}
.page{width:1920px;height:1080px;background:var(--canvas);position:relative;overflow:hidden;color:var(--night);
  font-family:"Segoe UI","Open Sans",Arial,sans-serif;font-size:13px;line-height:1.4;font-variant-numeric:tabular-nums}
.band{height:64px;background:var(--night);display:flex;align-items:center;gap:40px;padding:0 32px}
.band .logo svg{height:34px;width:auto;display:block}
.tabs{display:flex;gap:6px}
.tab{color:var(--muted);font-weight:600;font-size:13px;padding:7px 14px;border-radius:999px;letter-spacing:.01em}
.tab b{font-weight:600;margin-right:8px;opacity:.7}
.tab.on{background:rgba(233,229,214,.12);color:var(--oat)}
.band .meta{margin-left:auto;color:var(--muted);font-size:12px;letter-spacing:.06em;text-transform:uppercase;font-weight:600}
.head{padding:22px 32px 0}
.eyebrow{font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--deep)}
h1{margin:6px 0 0;font-size:40px;line-height:1.1;font-weight:600;letter-spacing:-.01em}
.sub{margin-top:8px;font-size:15px;color:var(--dusk);white-space:nowrap}
.grid{position:absolute;left:32px;right:32px;top:212px;bottom:44px;display:grid;gap:20px}
.card{background:var(--white);border:1px solid var(--seam);border-radius:12px;padding:20px 22px;min-width:0;min-height:0;display:flex;flex-direction:column}
.ct{font-size:15px;font-weight:600;line-height:1.3}
.cs{font-size:12px;color:var(--dusk);margin-top:4px}
.foot{position:absolute;left:32px;right:32px;bottom:14px;font-size:11px;color:var(--dusk);display:flex;justify-content:space-between}
.chip{display:inline-flex;align-items:center;gap:5px;border-radius:999px;padding:2px 9px;font-size:11px;font-weight:600;white-space:nowrap}
.c-b{background:var(--ice);color:var(--deep)}
.c-t{background:var(--tint);color:var(--burnt)}
.c-n{background:var(--chip);color:var(--dusk)}
.c-x{color:var(--dusk);font-weight:400}
.up{color:var(--deep);font-weight:600}.down{color:var(--burnt);font-weight:600}.flat{color:var(--dusk)}
table{border-collapse:collapse;width:100%}
th{font-size:11px;font-weight:600;color:var(--dusk);text-align:right;padding:0 10px 8px;border-bottom:1px solid var(--night);white-space:nowrap}
th.l,td.l{text-align:left}
td{text-align:right;padding:0 10px;border-bottom:1px solid var(--seam);white-space:nowrap}
td.gi,th.gi{background:var(--ice)}
th.gi{color:var(--deep)}
td.gi{font-weight:600}
.grp{font-size:11px;font-weight:600;color:var(--deep);letter-spacing:.02em}
svg text{font-family:"Segoe UI","Open Sans",Arial,sans-serif}
"""


def root_vars():
    return ":root{" + ";".join(f"--{k}:{v}" for k, v in C.items()) + "}"


def band(active):
    logo = open(LOGO, encoding="utf-8").read()
    tabs = "".join(f'<div class="tab{" on" if i == active else ""}"><b>0{i}</b>{n}</div>'
                   for i, n in ((1, "Brand review"), (2, "Investment strategy")))
    meta = ("Pillow &amp; Key Group &middot; Board review &middot; 2021 to 2025" if active == 1
            else "Budget $60.0M &middot; horizon 2027 to 2032")
    return f'<div class="band"><div class="logo">{logo}</div><div class="tabs">{tabs}</div><div class="meta">{meta}</div></div>'


# Depth variants (kit 3.1, plan 10-design-rebuild.md).
#   night       THE SPEC. A flat Night header zone from the top of the page to the horizon
#               (first card row + 128 px); the first card row hangs over it. In the zone, top right,
#               the faceless door hanger at 6 % Oat, tilted 10 degrees and cut off by the horizon
#               (item D2b, kept on Bjorn's request of 9 Nov; waives hard rule 6 "decorative images"
#               and the canvas-guide "no logos" rule for the header zone only). One card style per
#               page (design hard rule lock 9): no hairline, one shadow, Night at 10 %, y 8, blur 24
#               (hard-rule token "subtle only: ~10 % opacity"). In Power BI the zone and the shadows
#               are drawn into the page background image (opzet_backgrounds.mjs), not set per visual.
#   night-glow  OPTIONAL, needs Bjorn's waiver of hard rule 6 (gradients, decorative images) and the
#               canvas-guide "no logos" rule: the zone as a Night-to-navy gradient with a Coffee Blue
#               glow and the faceless hanger at 6 % (brand_canvas_v3.py), stronger hero shadow and a
#               Coffee Blue glow under the recommended plan.
#   flat        kit 3.0 baseline, for before/after.
HORIZON = 340   # comp geometry: first card row at 212 + 128


def hanger_layer(horizon, k=7.2, x=1350, y=-150, tilt=10, opacity=0.06):
    """The faded hanger (D2b) as a 1920 x 1080 SVG, clipped to the zone. Same geometry as
    brand_canvas_v3.py and the D2b block in opzet_backgrounds.mjs: the mark's 56 x 96 tile
    (radius 14, hole r 10, slit to the right edge) scaled by k, rotated -10 degrees (counter-
    clockwise) about the hole."""
    ox, oy = x + 12 * k, y + 7 * k
    cx, cy = ox + 28 * k, oy + 20 * k
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">'
            f'<defs><clipPath id="zone"><rect width="1920" height="{horizon}"/></clipPath>'
            '<mask id="hole" maskUnits="userSpaceOnUse" x="0" y="-400" width="1920" height="1600">'
            '<rect x="0" y="-400" width="1920" height="1600" fill="white"/>'
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{10 * k:.1f}" fill="black"/>'
            f'<rect x="{cx:.1f}" y="{oy + 18.5 * k:.1f}" width="{28 * k + 1:.1f}" height="{3 * k:.1f}" fill="black"/></mask></defs>'
            f'<g clip-path="url(#zone)"><g transform="rotate({-tilt} {cx:.1f} {cy:.1f})">'
            f'<rect x="{ox:.1f}" y="{oy:.1f}" width="{56 * k:.1f}" height="{96 * k:.1f}" rx="{14 * k:.1f}" '
            f'fill="#E9E5D6" fill-opacity="{opacity}" mask="url(#hole)"/></g></g></svg>')


def svg_url(svg):
    return 'url("data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode() + '")'
CARD_SHADOW = "0 8px 24px rgba(18,35,61,.10)"
ZONE_TEXT = """
.band{background:transparent;border-bottom:1px solid rgba(233,229,214,.14)}
.tab{color:#C9D0DC}.band .meta{color:#C9D0DC}
.head .eyebrow{color:#A9CDF0}.head h1{color:#F7F5EE}.head .sub{color:#C9D0DC}
.lbl{color:#C9D0DC!important}
"""
NIGHT = ZONE_TEXT + f"""
.page{{background:{svg_url(hanger_layer(HORIZON))} 0 0/1920px 1080px no-repeat,linear-gradient(to bottom,#12233D 0,#12233D {HORIZON}px,#F3F1EA {HORIZON}px)}}
.card,.plan{{border-color:transparent!important;box-shadow:{CARD_SHADOW}}}
.plan.sel{{border-color:var(--coffee)!important}}
.segtrack{{border-color:transparent!important}}
"""
GLOW = ZONE_TEXT + """
.card{border-color:transparent;box-shadow:0 14px 36px rgba(8,18,34,.16)}
.card.hero{box-shadow:0 24px 56px rgba(8,18,34,.28)}
.plan{border-color:transparent!important;box-shadow:0 8px 24px rgba(18,35,61,.09)}
.plan.sel{border-color:var(--coffee)!important;box-shadow:0 14px 34px rgba(37,137,216,.30)}
.segtrack{border-color:transparent!important;box-shadow:0 6px 18px rgba(18,35,61,.10)}
"""


def bg_css(name):
    p = os.path.join(os.path.dirname(LOGO), name)
    b = base64.b64encode(open(p, "rb").read()).decode()
    return f".page{{background:url(data:image/jpeg;base64,{b}) center/cover no-repeat}}"


def variant_css():
    if VARIANT == "flat": return ""
    if VARIANT == "night": return NIGHT
    return GLOW + bg_css("canvas-night.jpg")


def page(title, body):
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{title}</title>"
            f"<style>{fonts_css()}{root_vars()}{CSS}{variant_css()}</style></head><body><div class='page'>{body}</div></body></html>")


# ------------------------------------------------------------------ charts
def nice_ticks(lo, hi, n=4):
    import math
    span = hi - lo
    step = 10 ** math.floor(math.log10(span / n))
    for m in (1, 2, 2.5, 5, 10):
        if span / (step * m) <= n:
            step *= m; break
    a = math.floor(lo / step) * step
    ticks = []
    v = a
    while v <= hi + 1e-9:
        ticks.append(round(v, 10)); v += step
    if ticks[-1] < hi: ticks.append(ticks[-1] + step)
    return ticks


def line_chart(series, w, h, fmt, focus="Goodnight Inn", years=("2021", "2022", "2023", "2024", "2025"),
               lo=None, hi=None, note=None):
    pl, pr, pt, pb = 44, 120, 10, 24
    vals = [v for s in series.values() for v in s]
    lo = min(vals) if lo is None else lo
    hi = max(vals) if hi is None else hi
    ticks = nice_ticks(lo, hi, 3)
    lo, hi = ticks[0], ticks[-1]
    X = lambda i: pl + i * (w - pl - pr) / (len(years) - 1)
    Y = lambda v: pt + (hi - v) * (h - pt - pb) / (hi - lo)
    out = []
    for t in ticks:
        out.append(f'<line x1="{pl}" x2="{w-pr}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" stroke="{C["seam"]}"/>'
                   f'<text x="{pl-8}" y="{Y(t)+4:.1f}" text-anchor="end" font-size="11" fill="{C["dusk"]}">{fmt(t, axis=True)}</text>')
    for i, yname in enumerate(years):
        out.append(f'<text x="{X(i):.1f}" y="{h-4}" text-anchor="middle" font-size="11" fill="{C["dusk"]}">{yname}</text>')
    labels = []
    for name, s in series.items():
        f = name == focus
        col, sw = (C["coffee"], 3) if f else (C["grey"], 1.5)
        pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(s))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>')
        if f:
            out.append(f'<circle cx="{X(len(s)-1):.1f}" cy="{Y(s[-1]):.1f}" r="4.5" fill="{col}"/>')
        labels.append([Y(s[-1]), name, f])
    labels.sort()
    for i in range(1, len(labels)):
        if labels[i][0] - labels[i - 1][0] < 14:
            labels[i][0] = labels[i - 1][0] + 14
    for y, name, f in labels:
        out.append(f'<text x="{w-pr+10}" y="{y+4:.1f}" font-size="{12 if f else 11}" font-weight="{600 if f else 400}" '
                   f'fill="{C["deep"] if f else C["dusk"]}">{name.replace("&", "&amp;")}</text>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">{"".join(out)}</svg>'


# ------------------------------------------------------------------ P1
def p1():
    b = {n: D["brands"][n]["y2025"] for n in BRANDS}
    g23 = D["brands"]["Goodnight Inn"]["y2023"]
    rk = D["ranks"]

    def pct(v): return f"{v*100:.1f}%"
    def money(v): return f"${v:,.0f}"
    rows = [  # group, label, key, fmt, rank key, change fmt, polarity (+1 higher is better, 0 neutral)
        ("F1 &middot; Full, margin slipping", "Occupancy", "occupancy", pct, "occupancy", "pt", 1),
        ("", "Average daily rate (segment)", "adr", money, None, "$", 0),
        ("", "RevPAR (segment)", "revpar", money, None, "$", 0),
        ("", "GOP margin before commissions", "gop_margin", pct, "gop_margin", "pt", 1),
        ("", "GOP margin after commissions", "gop_margin_after", pct, "gop_margin_after", "pt", 1),
        ("F2 &middot; Booked with us?", "OTA share of room revenue", "ota_share", pct, "ota_share", "pt", -1),
        ("", "Direct share (web, app, phone)", "direct_share", pct, "direct_share", "pt", 1),
        ("", "Distribution cost, % of room revenue", "dist_pct_room", pct, "dist_pct_room", "pt", -1),
        ("F3 &middot; A good night?", "Room comfort score (0 to 10)", "comfort", lambda v: f"{v:.2f}", "comfort", "2", 1),
        ("", "Room-condition complaints per 1,000 nights", "room_cond_1k", lambda v: f"{v:.2f}", "room_cond_1k", "2", -1),
        ("", "All complaints per 1,000 nights", "complaints_1k", lambda v: f"{v:.1f}", "complaints_1k", "1", -1),
        ("F3 &middot; A fair price?", "Value for money score (0 to 10)", "value", lambda v: f"{v:.2f}", "value", "2", 1),
        ("F3 &middot; Recommend us?", "Net promoter score", "nps", lambda v: f"{'+' if v>=0 else MINUS}{abs(v):.1f}", "nps", "1", 1),
    ]
    trs = []
    for grp, lab, k, f, rkey, cu, pol in rows:
        cells = "".join(f'<td class="{"gi" if n == "Goodnight Inn" else ""}">{f(b[n][k])}</td>' for n in BRANDS)
        if rkey is None:
            chip = '<span class="chip c-x">not ranked</span>'
        else:
            r = rk[rkey]
            chip = ('<span class="chip c-b">&#9650; Best of 4</span>' if r == 1 else
                    '<span class="chip c-t">&#9660; Last of 4</span>' if r == 4 else
                    f'<span class="chip c-n">{"2nd" if r == 2 else "3rd"} of 4</span>')
        dv = b["Goodnight Inn"][k] - g23[k]
        if cu == "pt": txt = sgn(dv * 100, 1, " pt")
        elif cu == "$": txt = sgn(dv, 0, money=True)
        else: txt = sgn(dv, int(cu))
        cls = "flat" if pol == 0 else ("up" if dv * pol > 0 else "down")
        arrow = "" if pol == 0 else ("&#9650; " if dv > 0 else "&#9660; ")
        trs.append(f'<tr style="height:33px"><td class="l grp">{grp}</td><td class="l">{lab}</td>{cells}'
                   f'<td>{chip}</td><td class="{cls}">{arrow}{txt}</td></tr>')
    score = (f'<div class="card hero" style="grid-area:score">'
             f'<div class="ct">Goodnight Inn fills the most rooms, and is last of four on what guests and booking channels say</div>'
             f'<div class="cs">2025, the four Pillow &amp; Key brands &middot; rates reflect each segment and are not ranked &middot; change is 2023 to 2025 &middot; hover a row for the method</div>'
             f'<table style="margin-top:14px"><thead><tr><th class="l" style="width:180px">Finding</th><th class="l">Measure</th>'
             + "".join(f'<th class="{"gi" if n == "Goodnight Inn" else ""}">{n.replace("&", "&amp;")}</th>' for n in BRANDS)
             + '<th>Goodnight Inn rank</th><th>Since 2023</th></tr></thead><tbody>' + "".join(trs) + "</tbody></table></div>")

    # geography
    H = D["hotels"]
    def occ(f):
        hs = [h for h in H if f(h)]
        return (sum(h["occ"] * h["rooms"] for h in hs) / sum(h["rooms"] for h in hs), len(hs)) if hs else (None, 0)
    regions = ["Asia-Pacific", "Europe", "North America", "Total"]
    types = ["Airport", "City", "Highway", "Total"]
    def tint(v):
        if v is None: return C["white"]
        t = max(0, min(1, (v - 0.76) / (0.84 - 0.76)))
        steps = ["#F6F9FD", "#EAF2FB", "#D6E6F7", "#BFD8F2", "#A6C9EE"]
        return steps[min(4, int(t * 5))]
    rows_g = []
    for r in regions:
        tds = ""
        for t in types:
            v, n = occ(lambda h: (r == "Total" or h["region"] == r) and (t == "Total" or h["type"] == t))
            txt = f'{v*100:.1f}% <span style="color:{C["dusk"]};font-weight:400">&middot; {n}</span>' if v else "&mdash;"
            fw = 600 if (r == "Total" or t == "Total") else 400
            tds += f'<td style="background:{tint(v)};font-weight:{fw};text-align:center">{txt}</td>'
        rows_g.append(f'<tr style="height:31px"><td class="l" style="font-weight:{600 if r=="Total" else 400}">{r}</td>{tds}</tr>')
    matrix = ('<table style="margin-top:12px"><thead><tr><th class="l">Region</th>'
              + "".join(f'<th style="text-align:center">{t}</th>' for t in types) + "</tr></thead><tbody>"
              + "".join(rows_g) + "</tbody></table>")
    top = sorted(H, key=lambda h: -h["occ"])[:7]
    bw = 330
    bars = []
    for i, h in enumerate(top):
        y = i * 33
        w = (h["occ"] - 0) / 1.0 * bw
        col = C["coffee"] if h["type"] == "Airport" else C["grey"]
        bars.append(f'<text x="0" y="{y+15}" font-size="12" fill="{C["night"]}">{h["name"]}</text>'
                    f'<rect x="210" y="{y+3}" width="{w:.1f}" height="16" rx="3" fill="{col}"/>'
                    f'<text x="{210+w+8:.1f}" y="{y+15}" font-size="12" font-weight="600" fill="{C["night"]}">{h["occ"]*100:.1f}%</text>')
    bars_svg = f'<svg width="600" height="{7*33}" viewBox="0 0 600 {7*33}" role="img">{"".join(bars)}</svg>'
    geo = (f'<div class="card" style="grid-area:geo">'
           f'<div class="ct">F4 &middot; The airports are the fullest: 82.0% occupancy, against 77.5% on the highway</div>'
           f'<div class="cs">Occupancy 2025 by region and location type &middot; number of hotels</div>{matrix}'
           f'<div style="display:flex;justify-content:space-between;align-items:center;margin:18px 0 8px">'
           f'<div class="ct" style="font-size:13px">The seven fullest hotels, 2025</div>'
           f'<div style="display:flex;gap:6px"><span class="chip c-b">Airport</span><span class="chip c-n">Other</span></div></div>{bars_svg}</div>')

    # trends
    T = {n: D["brands"][n]["trend"] for n in BRANDS}
    yrs = ["2021", "2022", "2023", "2024", "2025"]
    def ser(k, m=1): return {n: [T[n][y][k] * m for y in yrs] for n in BRANDS}
    pf = lambda v, axis=False: f"{v:.0f}%"
    nf = lambda v, axis=False: (f"+{v:.0f}" if v > 0 else (f"{MINUS}{abs(v):.0f}" if v < 0 else "0"))
    w, h = 560, 168
    gi = T["Goodnight Inn"]
    def tcard(title, chip, svg):
        return (f'<div class="card" style="padding:16px 18px 10px"><div style="display:flex;justify-content:space-between;gap:10px;align-items:flex-start">'
                f'<div class="ct" style="font-size:14px">{title}</div>{chip}</div><div style="margin-top:8px">{svg}</div></div>')
    t1 = tcard(f"F1 &middot; After commissions, the margin slid from {gi['2023']['gop_margin_after']*100:.1f}% (2023) to {gi['2025']['gop_margin_after']*100:.1f}%",
               '<span class="chip c-n">2nd of 4</span>',
               line_chart(ser("gop_margin_after", 100), w, h, pf))
    t2 = tcard(f"F2 &middot; OTAs now book {gi['2025']['ota_share']*100:.1f}% of room revenue, up from {gi['2021']['ota_share']*100:.1f}%",
               '<span class="chip c-t">&#9660; Last of 4</span>',
               line_chart(ser("ota_share", 100), w, h, pf))
    t3 = tcard(f"F3 &middot; NPS down every year, from +{gi['2021']['nps']:.1f} to +{gi['2025']['nps']:.1f}; every sister is higher",
               '<span class="chip c-t">&#9660; Last of 4</span>',
               line_chart(ser("nps"), w, h, nf))
    trends = f'<div style="grid-area:trends;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;min-height:0">{t1}{t2}{t3}</div>'

    head = ('<div class="head"><div class="eyebrow">01 &nbsp;The brand review</div><h1>Full rooms, fading guests.</h1>'
            '<div class="sub">Goodnight Inn fills the most rooms of the four brands (79.4%) and keeps the widest margin before commissions (44.4%). '
            'After commissions it is second (33.7%), and on guests, booking channels and complaints it is last of four.</div></div>')
    grid = (f'<div class="grid" style="grid-template-columns:1176px 1fr;grid-template-rows:556px 1fr;'
            f'grid-template-areas:\'score geo\' \'trends trends\'">{score}{geo}{trends}</div>')
    foot = ('<div class="foot"><span>Data: Pillow &amp; Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores response-weighted. '
            '2021 is a depressed base year. Method in the tooltips.</span><span>goodnight inn. &middot; 01 / 02</span></div>')
    return page("Goodnight Inn P1 comp", band(1) + head + grid + foot)


# ------------------------------------------------------------------ P2
def p2():
    P = {p["id"]: p for p in D["projects"]}
    PK = {p["id"]: p for p in D["packages"]}
    sc = "Expected"
    # scatter
    w, h = 1000, 690
    pl, pr, pt, pb = 64, 24, 20, 48
    xs = lambda v: pl + v / 60e6 * (w - pl - pr)
    ylo, yhi = -50e6, 10e6
    ys = lambda v: pt + (yhi - v) / (yhi - ylo) * (h - pt - pb)
    o = [f'<rect x="{pl}" y="{ys(yhi):.1f}" width="{w-pl-pr}" height="{ys(0)-ys(yhi):.1f}" fill="{C["ice"]}"/>']
    for t in range(-50, 11, 10):
        o.append(f'<line x1="{pl}" x2="{w-pr}" y1="{ys(t*1e6):.1f}" y2="{ys(t*1e6):.1f}" stroke="{C["seam"] if t else C["night"]}" stroke-width="{1}"/>'
                 f'<text x="{pl-10}" y="{ys(t*1e6)+4:.1f}" text-anchor="end" font-size="12" fill="{C["dusk"]}">{"+" if t>0 else (MINUS if t<0 else "")}${abs(t)}M</text>')
    for t in range(0, 61, 10):
        o.append(f'<text x="{xs(t*1e6):.1f}" y="{h-22}" text-anchor="middle" font-size="12" fill="{C["dusk"]}">${t}M</text>')
    o.append(f'<text x="{(pl+w-pr)/2:.0f}" y="{h-2}" text-anchor="middle" font-size="12" fill="{C["dusk"]}">Capex of the package</text>')
    o.append(f'<text x="{w-pr-8}" y="{ys(0)-8:.1f}" text-anchor="end" font-size="12" font-weight="600" fill="{C["deep"]}" stroke="{C["ice"]}" stroke-width="5" stroke-linejoin="round" paint-order="stroke">Worth its cost by 2032 above this line</text>')
    pk = sorted(D["packages"], key=lambda p: p["refresh"])  # refresh (grey) drawn first
    pk = [p for p in D["packages"] if p["refresh"]] + [p for p in D["packages"] if not p["refresh"]]
    for p in pk:
        col = C["grey"] if p["refresh"] else C["coffee"]
        o.append(f'<circle cx="{xs(p["capex"]):.1f}" cy="{ys(p["npv"][sc]):.1f}" r="3.6" fill="{col}" stroke="#fff" stroke-width=".8"/>')
    def mark(pid, col, letter, label, dx, dy, ring=False):
        p = PK[pid]; x, y = xs(p["capex"]), ys(p["npv"][sc])
        r = 11
        s = (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r+4}" fill="none" stroke="{col}" stroke-width="2"/>' if ring else "")
        s += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" stroke="#fff" stroke-width="2"/>'
              f'<text x="{x:.1f}" y="{y+4.5:.1f}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{letter}</text>'
              f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="13" font-weight="600" fill="{col}" stroke="#fff" stroke-width="5" stroke-linejoin="round" paint-order="stroke">{label}</text>')
        return s
    o.append(mark("01+07+10", C["burnt"], "C", f"C &middot; full refresh, {MINUS}$23.4M", 18, -14))
    o.append(mark("01+09+10", C["night"], "B", "B &middot; +$2.7M", 18, 22))
    o.append(mark("01+02+10", C["deep"], "A", "A &middot; recommended, +$3.3M", 22, -12, ring=True))
    scatter = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">{"".join(o)}</svg>'
    left = (f'<div class="card hero" style="grid-area:scatter">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px">'
            f'<div><div class="ct">6 of 456 valid packages are worth more than they cost by December 2032</div>'
            f'<div class="cs">One dot per package the rules allow: three or more initiatives, at least one growth initiative, within $60M, kiosks only with the app &middot; NPV through 2032, 2025 dollars, 8% &middot; Expected case</div></div>'
            f'<div style="display:flex;gap:6px;flex:none"><span class="chip c-b">&#9679; Without the refresh</span><span class="chip c-n">&#9679; With the refresh</span></div></div>'
            f'<div style="margin-top:10px">{scatter}</div></div>')

    # right column
    seg = ''.join(f'<span style="padding:6px 16px;border-radius:999px;font-weight:600;font-size:12px;{"background:"+C["night"]+";color:"+C["oat"] if s=="Expected" else "color:"+C["dusk"]}">{s}</span>'
                  for s in ("Low", "Expected", "High"))
    controls = (f'<div style="display:flex;justify-content:space-between;align-items:center">'
                f'<div class="lbl" style="font-size:12px;color:{C["dusk"]};font-weight:600;letter-spacing:.08em;text-transform:uppercase">Three packages, one recommendation</div>'
                f'<div class="segtrack" style="display:flex;gap:2px;background:{C["white"]};border:1px solid {C["seam"]};border-radius:999px;padding:3px">{seg}</div></div>')
    def plan(letter, tagcls, tag, title, what, npv, line, sel=False):
        st = f'border:2px solid {C["coffee"]};background:{C["ice"]}' if sel else f'border:1px solid {C["seam"]};background:{C["white"]}'
        ncol = C["deep"] if not npv.startswith(MINUS) else C["burnt"]
        return (f'<div class="plan{" sel" if sel else ""}" style="{st};border-radius:12px;padding:14px 16px;display:grid;gap:6px;align-content:start">'
                f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-weight:700;font-size:13px">{letter}</span><span class="chip {tagcls}">{tag}</span></div>'
                f'<div style="font-weight:600;font-size:14px;line-height:1.25">{title}</div>'
                f'<div style="font-size:11.5px;color:{C["dusk"]};min-height:30px">{what}</div>'
                f'<div style="font-size:28px;font-weight:600;color:{ncol};line-height:1">{npv}</div>'
                f'<div style="font-size:11.5px;color:{C["dusk"]}">{line}</div></div>')
    cards = ('<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">'
             + plan("A", "c-b", "Recommended", "Booking first", "Booking app, revenue management, check-in kiosks", "+$3.3M", "NPV 2032 &middot; $9.4M &middot; pays back 2031", True)
             + plan("B", "c-n", "Alternative", "Balanced", "Booking app, revenue management, breakfast upgrade", "+$2.7M", "NPV 2032 &middot; $11.65M &middot; all 50 hotels")
             + plan("C", "c-t", "Comparator", "Why not renovate everything?", "Booking app, revenue management, refresh of the 10 oldest", f"{MINUS}$23.4M", "NPV 2032 &middot; $36.9M &middot; negative to 2032")
             + "</div>")
    # waterfall for A
    parts = [("Booking app", P["GI-01"]["npv"][sc]), ("Revenue mgmt", P["GI-10"]["npv"][sc]), ("Kiosks", P["GI-02"]["npv"][sc])]
    total = PK["01+02+10"]["npv"][sc]
    ww, wh = 360, 150
    top, bot = 4.0e6, -1.0e6
    Yw = lambda v: 22 + (top - v) / (top - bot) * (wh - 52)
    bx = 10; step = (ww - 20) / 4; bwid = step - 18
    wo = [f'<line x1="0" x2="{ww}" y1="{Yw(0):.1f}" y2="{Yw(0):.1f}" stroke="{C["night"]}"/>']
    run = 0
    for i, (n, v) in enumerate(parts + [("Package A", total)]):
        last = i == 3
        a, b2 = (0, v) if last else (run, run + v)
        col = C["night"] if last else (C["coffee"] if v >= 0 else C["tang"])
        y1, y2 = Yw(max(a, b2)), Yw(min(a, b2))
        x = bx + i * step
        wo.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{bwid:.1f}" height="{max(2,y2-y1):.1f}" rx="3" fill="{col}"/>'
                  f'<text x="{x+bwid/2:.1f}" y="{y1-6:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{C["night"] if v>=0 else C["burnt"]}">{sgn(v/1e6,1,"M",money=True)}</text>'
                  f'<text x="{x+bwid/2:.1f}" y="{wh-6}" text-anchor="middle" font-size="11" fill="{C["dusk"]}">{n}</text>')
        if not last: run += v
    wf = f'<svg width="{ww}" height="{wh}" viewBox="0 0 {ww} {wh}" role="img">{"".join(wo)}</svg>'
    # cumulative net for A, Low / Expected / High
    A = ["GI-01", "GI-02", "GI-10"]
    yrs = ["2027", "2028", "2029", "2030", "2031", "2032"]
    cum = {}
    for s2 in ("Low", "Expected", "High"):
        c, out = 0, []
        for y in yrs:
            c += sum(P[i]["net_by_year"][s2][y] for i in A); out.append(c / 1e6)
        cum[s2] = out
    cw, chh = 360, 150
    clo, chi = -10, 20
    Xc = lambda i: 34 + i * (cw - 50) / 5
    Yc = lambda v: 10 + (chi - v) / (chi - clo) * (chh - 36)
    co = []
    for t in (-10, 0, 10, 20):
        co.append(f'<line x1="34" x2="{cw-16}" y1="{Yc(t):.1f}" y2="{Yc(t):.1f}" stroke="{C["night"] if t==0 else C["seam"]}"/>'
                  f'<text x="28" y="{Yc(t)+4:.1f}" text-anchor="end" font-size="11" fill="{C["dusk"]}">{"+" if t>0 else (MINUS if t<0 else "")}{abs(t)}</text>')
    band_pts = " ".join(f"{Xc(i):.1f},{Yc(v):.1f}" for i, v in enumerate(cum["High"])) + " " + \
               " ".join(f"{Xc(i):.1f},{Yc(v):.1f}" for i, v in reversed(list(enumerate(cum["Low"]))))
    co.append(f'<polygon points="{band_pts}" fill="{C["coffee"]}" opacity=".15"/>')
    co.append(f'<polyline points="{" ".join(f"{Xc(i):.1f},{Yc(v):.1f}" for i, v in enumerate(cum["Low"]))}" fill="none" stroke="{C["tang"]}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    co.append(f'<polyline points="{" ".join(f"{Xc(i):.1f},{Yc(v):.1f}" for i, v in enumerate(cum["Expected"]))}" fill="none" stroke="{C["coffee"]}" stroke-width="3"/>')
    for i, y in enumerate(yrs):
        co.append(f'<text x="{Xc(i):.1f}" y="{chh-6}" text-anchor="middle" font-size="11" fill="{C["dusk"]}">{y}</text>')
    co.append(f'<text x="{Xc(5)-4:.1f}" y="{Yc(cum["Expected"][5])-8:.1f}" text-anchor="end" font-size="12" font-weight="600" fill="{C["deep"]}">Expected +${cum["Expected"][5]:.1f}M</text>')
    co.append(f'<text x="{Xc(5)-4:.1f}" y="{Yc(cum["Low"][5])+16:.1f}" text-anchor="end" font-size="11" font-weight="600" fill="{C["burnt"]}">Low {MINUS}${abs(cum["Low"][5]):.1f}M</text>')
    cumsvg = f'<svg width="{cw}" height="{chh}" viewBox="0 0 {cw} {chh}" role="img">{"".join(co)}</svg>'
    mid = ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">'
           f'<div class="card" style="padding:14px 16px"><div class="ct" style="font-size:13px">Where A\'s +$3.3M comes from</div><div class="cs" style="margin-top:2px">NPV through 2032, $M, Expected</div><div style="margin-top:6px">{wf}</div></div>'
           f'<div class="card" style="padding:14px 16px"><div class="ct" style="font-size:13px">Cumulative net turns positive in 2031</div><div class="cs" style="margin-top:2px">Package A, cumulative net, $M &middot; band Low to High</div><div style="margin-top:6px">{cumsvg}</div></div></div>')
    # initiatives table
    names = {"GI-01": "Booking app", "GI-10": "Revenue management", "GI-02": "Check-in kiosks, 20 hotels", "GI-09": "Breakfast upgrade",
             "GI-05": "Gatwick +40 rooms", "GI-04": "Toronto +40 rooms", "GI-06": "Kingston +40 rooms", "GI-03": "Energy programme",
             "GI-08": "Boston new hotel", "GI-07": "Refresh 10 oldest"}
    ans = {"GI-01": "F2", "GI-10": "F1", "GI-02": "F3", "GI-09": "F3", "GI-05": "F4", "GI-04": "F4", "GI-06": "F4", "GI-03": "F1", "GI-08": "F4", "GI-07": "F3"}
    order = ["GI-01", "GI-10", "GI-02"] + sorted([k for k in P if k not in A], key=lambda k: -P[k]["npv"][sc])
    import datetime
    trs = []
    for k in order:
        p = P[k]; f = k in A
        live = datetime.date(int(p["live"][:4]), int(p["live"][5:]), 1).strftime("%b %Y")
        npv = p["npv"][sc] / 1e6
        trs.append(f'<tr style="height:24px"><td class="l">{"<span class=\"chip c-b\">Funded</span>" if f else "<span class=\"chip c-x\">Not funded</span>"}</td>'
                   f'<td class="l" style="font-weight:{600 if f else 400}">{names[k]}</td><td class="l"><span class="chip c-n">{ans[k]}</span></td>'
                   f'<td>${p["capex"]/1e6:.1f}M</td><td>{live}</td><td>{sgn(p["runrate"][sc]/1e6,1,"M",money=True)}</td>'
                   f'<td class="{"up" if npv>=0 else "down"}">{sgn(npv,1,"M",money=True)}</td></tr>')
    table = (f'<div class="card" style="padding:14px 16px;flex:1"><div style="display:flex;justify-content:space-between;align-items:baseline">'
             f'<div class="ct" style="font-size:13px">The ten initiatives, and what each answers on page 1</div><div class="cs">Expected &middot; run-rate a year by 2032</div></div>'
             f'<table style="margin-top:6px"><thead><tr><th class="l">Status</th><th class="l">Initiative</th><th class="l">Answers</th><th>Capex</th><th>Live</th><th>Run-rate</th><th>NPV 2032</th></tr></thead><tbody>'
             + "".join(trs) + '</tbody></table>'
             f'<div style="margin-top:8px;display:flex;gap:8px;flex-wrap:wrap;align-items:center"><span class="chip c-t">Risk</span>'
             f'<span style="font-size:12px;color:{C["dusk"]}">Low case NPV {MINUS}$5.5M. Kiosks start only when the app is live. Operational: 0 rooms added, guest effect at 20 hotels.</span></div></div>')
    right = f'<div style="grid-area:right;display:flex;flex-direction:column;gap:16px;min-height:0">{controls}{cards}{mid}{table}</div>'

    head = ('<div class="head"><div class="eyebrow">02 &nbsp;The investment strategy</div><h1>Fix the booking before the building.</h1>'
            '<div class="sub">Recommended: package A, the booking app, revenue management and check-in kiosks. $9.4M of the $60.0M budget; '
            f'NPV through 2032 +$3.3M (Expected; Low {MINUS}$5.5M, High +$12.7M); cumulative net positive from 2031.</div></div>')
    grid = (f'<div class="grid" style="grid-template-columns:1044px 1fr;grid-template-areas:\'scatter right\'">{left}{right}</div>')
    foot = ('<div class="foot"><span>Data: Pillow &amp; Key Group dataset, Power BI Dataviz World Champs 2027. Constant 2025 dollars, 8% discounting, horizon 2027 to 2032, no residual value. '
            'Method in the tooltips.</span><span>goodnight inn. &middot; 02 / 02</span></div>')
    return page("Goodnight Inn P2 comp", band(2) + head + grid + foot)


os.makedirs(OUT, exist_ok=True)
sfx = "-" + VARIANT
for name, fn in ((f"p1-brand-review{sfx}.html", p1), (f"p2-investment-strategy{sfx}.html", p2)):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(fn())
    print("wrote", name)
