"""Cover images for the gallery post (16 Nov 2026, doc 35): three candidates, each a 1920 x 1080 page drawn in HTML and
captured with headless Edge.

  python project/tools/gallery/cover.py [--size 1920x1080] [--only a,b,c]

Another --size keeps the 1920 x 1080 composition and adds Night around it (1920x1440 for a 4:3 tile, 1920x1920 for a
square one); the file then carries the size in its name.

  a  "456 ways to spend $60M. The best one spends $9.4M."  every package the rules allow as a dot (packages.json: capex
     and NPV through 2032 in the Expected case, read from the model's Package table), the six that pay back in blue,
     package A marked.
  b  "Full rooms. A slipping margin."  the two report pages as they are.
  c  "Same room. Same night. $17.47 apart."  one room night through an online agency and booked direct (card II of
     page 1).

Every number is on the report. Writes cover-a.png, cover-b.png, cover-c.png (and the .html each was drawn from) to
project/deliverables/final-room-to-invest/gallery/.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUT = ROOT / "project" / "deliverables" / "final-room-to-invest" / "gallery"
ASSETS = ROOT / "design" / "brand-kits" / "goodnight-inn-wakeup" / "assets"
PAGE1 = ROOT / "project" / "deliverables" / "final-room-to-invest" / "hover-align" / "page1.png"
PAGE2 = ROOT / "project" / "deliverables" / "final-room-to-invest" / "plan-chart" / "final-copy-page2.png"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

NIGHT, COFFEE_BLUE, SKY, OAT, GREY, ORANGE = "#12233D", "#2589D8", "#5AAEF0", "#F5E7DC", "#B9B2A3", "#FF783D"

args = sys.argv[1:]
W, H = 1920, 1080
if "--size" in args:
    W, H = (int(n) for n in args[args.index("--size") + 1].split("x"))
ONLY = args[args.index("--only") + 1].split(",") if "--only" in args else ["a", "b", "c"]
SUFFIX = "" if (W, H) == (1920, 1080) else f"-{W}x{H}"


def uri(p):
    return Path(p).resolve().as_uri()


CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:'Segoe UI',sans-serif;color:#fff;background:{NIGHT};position:relative;
  background-image:radial-gradient(1200px 800px at 88% -10%, #24467A 0%, rgba(36,70,122,0) 60%),
                   radial-gradient(900px 700px at -10% 110%, #0B1729 0%, rgba(11,23,41,0) 60%)}}
.logo{{position:absolute;left:110px;top:84px;height:60px}}
.foot{{position:absolute;left:110px;bottom:76px;font-size:20px;letter-spacing:.12em;text-transform:uppercase;color:{OAT};opacity:.72}}
h1{{font-weight:600;letter-spacing:-.015em;line-height:1.04}}
h1 .hot{{color:{ORANGE}}}
.sub{{color:{OAT};opacity:.9;line-height:1.36}}
"""

# the 1920 x 1080 composition, centred on the canvas: another --size only adds Night around it (a 4:3 or square tile)
HEAD = ("<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{css}</style></head><body>"
        f"<div style='position:absolute;left:{(W - 1920) // 2}px;top:{(H - 1080) // 2}px;width:1920px;height:1080px'>")
LOGO = f"<img class='logo' src='{uri(ASSETS / 'gi-lockup-reversed.svg')}' alt='Goodnight Inn'>"
FOOT = "<div class='foot'>Room to Invest &nbsp;·&nbsp; Power BI Dataviz World Champs 2027 &nbsp;·&nbsp; Round 1</div>"


def cover_a():
    pk = json.loads((HERE / "packages.json").read_text(encoding="utf-8"))
    assert len(pk) == 456 and sum(p["npv"] >= 0 for p in pk) == 6
    a = next(p for p in pk if p["preset"] == "A")
    assert a["npv"] == max(p["npv"] for p in pk) and round(a["capex"] / 1e6, 1) == 9.4
    # the plot: capex $5M to $62M across, NPV +17M to -53M down
    x0, x1, y0, y1 = 980, 1830, 120, 890

    def X(c):
        return x0 + (c / 1e6 - 5) / 57 * (x1 - x0)

    def Y(n):
        return y0 + (17 - n / 1e6) / 70 * (y1 - y0)

    zero = Y(0)
    dots = []
    for p in sorted(pk, key=lambda p: p["npv"]):
        if p["preset"] == "A":
            continue
        if p["npv"] >= 0:
            dots.append(f"<circle cx='{X(p['capex']):.1f}' cy='{Y(p['npv']):.1f}' r='9' fill='{SKY}'/>")
        else:
            dots.append(f"<circle cx='{X(p['capex']):.1f}' cy='{Y(p['npv']):.1f}' r='6.5' fill='{GREY}' fill-opacity='.62'/>")
    ax, ay = X(a["capex"]), Y(a["npv"])
    svg = f"""
<svg width='1920' height='1080' viewBox='0 0 1920 1080' style='position:absolute;left:0;top:0' xmlns='http://www.w3.org/2000/svg' font-family='Segoe UI'>
  <rect x='{x0}' y='{y0}' width='{x1 - x0}' height='{zero - y0:.1f}' fill='{SKY}' fill-opacity='.10'/>
  <line x1='{x0}' x2='{x1}' y1='{zero:.1f}' y2='{zero:.1f}' stroke='#fff' stroke-width='2'/>
  <text x='{x1}' y='{zero - 16:.1f}' text-anchor='end' font-size='24' fill='#fff'>pays back by 2032</text>
  <text x='{x1}' y='{zero + 36:.1f}' text-anchor='end' font-size='24' fill='{OAT}' fill-opacity='.75'>does not</text>
  {''.join(dots)}
  <circle cx='{ax:.1f}' cy='{ay:.1f}' r='30' fill='none' stroke='{ORANGE}' stroke-width='3'/>
  <circle cx='{ax:.1f}' cy='{ay:.1f}' r='15' fill='{ORANGE}' stroke='#fff' stroke-width='3'/>
  <line x1='{ax + 24:.1f}' y1='{ay - 24:.1f}' x2='{ax + 66:.1f}' y2='{ay - 66:.1f}' stroke='{ORANGE}' stroke-width='2'/>
  <text x='{ax + 78:.1f}' y='{ay - 62:.1f}' font-size='32' font-weight='600' fill='#fff'>Package A: $9.4M now</text>
  <text x='{X(10e6):.1f}' y='{y1 + 56}' text-anchor='middle' font-size='24' fill='{OAT}' fill-opacity='.75'>$10M</text>
  <text x='{X(60e6):.1f}' y='{y1 + 56}' text-anchor='middle' font-size='24' fill='{OAT}' fill-opacity='.75'>$60M</text>
  <text x='{(X(10e6) + X(60e6)) / 2:.1f}' y='{y1 + 56}' text-anchor='middle' font-size='24' fill='{OAT}' fill-opacity='.75'>what the package costs →</text>
  <text x='{X(59.65e6) - 22:.1f}' y='{Y(-49.5e6) + 34:.1f}' text-anchor='end' font-size='24' fill='{OAT}' fill-opacity='.75'>−$49M through 2032</text>
</svg>"""
    return HEAD.format(css=CSS) + LOGO + f"""
<h1 style='position:absolute;left:110px;top:262px;font-size:106px'>456 ways<br>to spend $60M.<br><span class='hot'>The best one<br>spends $9.4M.</span></h1>
<p class='sub' style='position:absolute;left:110px;top:742px;width:760px;font-size:31px'>Every dot is an investment package for Goodnight Inn.<br>Six pay back by 2032. Think you can beat ours?<br>Build your own.</p>
{svg}{FOOT}</div></body></html>"""


def cover_b():
    shot = "position:absolute;border-radius:14px;box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.10)"
    return HEAD.format(css=CSS) + LOGO + f"""
<h1 style='position:absolute;left:110px;top:262px;font-size:84px;white-space:nowrap'>Full rooms.<br><span class='hot'>A slipping margin.</span></h1>
<p class='sub' style='position:absolute;left:110px;top:490px;width:640px;font-size:31px'>Goodnight Inn has the fullest hotels in the group. So where does the money go, and what should the Board fund first?</p>
<p class='sub' style='position:absolute;left:110px;top:700px;width:640px;font-size:31px;opacity:1;color:#fff;font-weight:600'>$9.4M now.<br>The rest of the $60M waits for 2028.</p>
<img src='{uri(PAGE2)}' style='{shot};left:1090px;top:70px;width:1150px' alt=''>
<img src='{uri(PAGE1)}' style='{shot};left:990px;top:480px;width:1150px' alt=''>
{FOOT}</div></body></html>"""


def cover_c():
    # one room night in 2025 (page 1, card II): what the guest pays = what Goodnight Inn keeps + commission and fees
    rows = [("Through an online agency", 109.31, 89.63, 19.68), ("Booked direct, web or app", 111.56, 107.10, 4.46)]
    assert all(abs(k + c - g) < 0.006 for _, g, k, c in rows) and round(rows[1][2] - rows[0][2], 2) == 17.47
    x0, full, top, pitch, bh = 930, 880, 330, 300, 104
    px = full / 111.56
    parts = []
    for i, (name, guest, keeps, comm) in enumerate(rows):
        y = top + i * pitch
        wk, wc = keeps * px, comm * px
        parts.append(f"""
  <text x='{x0}' y='{y - 22}' font-size='30' fill='#fff' font-weight='600'>{name}</text>
  <text x='{x0 + (wk + wc):.1f}' y='{y - 22}' font-size='26' fill='{OAT}' fill-opacity='.8' text-anchor='end'>the guest pays ${guest:.2f}</text>
  <rect x='{x0}' y='{y}' width='{wk - 3:.1f}' height='{bh}' fill='{OAT}'/>
  <rect x='{x0 + wk:.1f}' y='{y}' width='{wc:.1f}' height='{bh}' fill='{ORANGE}'/>
  <text x='{x0 + 28}' y='{y + 68}' font-size='50' font-weight='600' fill='{NIGHT}'>${keeps:.2f}</text>
  <text x='{x0 + 28 + 200}' y='{y + 66}' font-size='26' fill='{NIGHT}'>Goodnight Inn keeps</text>
  <text x='{x0 + wk + wc:.1f}' y='{y + bh + 40}' font-size='26' fill='{ORANGE}' text-anchor='end'>commission and fees ${comm:.2f}</text>""")
    svg = f"<svg width='1920' height='1080' viewBox='0 0 1920 1080' style='position:absolute;left:0;top:0' xmlns='http://www.w3.org/2000/svg' font-family='Segoe UI'>{''.join(parts)}</svg>"
    return HEAD.format(css=CSS) + LOGO + f"""
<h1 style='position:absolute;left:110px;top:262px;font-size:100px'>Same room.<br>Same night.<br><span class='hot'>$17.47 apart.</span></h1>
<p class='sub' style='position:absolute;left:110px;top:640px;width:700px;font-size:31px'>Half of Goodnight Inn's room revenue now arrives through online agencies. The Board has $60M. This report says what to fund first.</p>
<p class='sub' style='position:absolute;left:930px;top:850px;width:880px;font-size:26px;opacity:.75'>One room night at Goodnight Inn, 2025.</p>
{svg}{FOOT}</div></body></html>"""


OUT.mkdir(parents=True, exist_ok=True)
for key, fn in (("a", cover_a), ("b", cover_b), ("c", cover_c)):
    if key not in ONLY:
        continue
    html = OUT / f"cover-{key}{SUFFIX}.html"
    png = OUT / f"cover-{key}{SUFFIX}.png"
    html.write_text(fn(), encoding="utf-8")
    png.unlink(missing_ok=True)
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={W},{H}", f"--user-data-dir={Path.home() / 'AppData' / 'Local' / 'Temp' / 'gi-cover-edge'}",
                    f"--screenshot={png}", html.as_uri()], check=False, capture_output=True, timeout=120)
    for _ in range(60):  # Edge can return before the file is written
        if png.exists() and png.stat().st_size > 0:
            break
        time.sleep(0.5)
    print(f"cover-{key}{SUFFIX}.png", "written" if png.exists() else "NOT written")
