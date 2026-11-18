"""The final cover for the gallery post (16 Nov 2026 night, doc 40): the hook of candidate a, the report itself, and the
report's selling point that it is built with native Power BI visuals only.

  python project/tools/gallery/cover_final.py [--size 1920x1080]

  left    the logo, "456 ways to spend $60M. The best one spends $9.4M.", one line of invitation, the badge
          "100% native Power BI visuals" and a line of what is in the report.
  right   two views of page 2 as they stand: behind, "What waits, and why" with the 456 packages as dots (the chart the
          headline is about); in front, "Recommended: A" with the three plans highlighted and the $60M plan bar.

Every number is on the report; "100% native" was read from the report's files (194 visuals, every type one of Power
BI's own, no custom visual). Another --size keeps the 1920 x 1080 composition and adds Night around it (1920x1440 for a
4:3 tile, 1920x1920 for a square one). Writes cover-final.png (and its .html) to
project/deliverables/final-room-to-invest/gallery/.
"""
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GAL = ROOT / "project" / "deliverables" / "final-room-to-invest" / "gallery"
OUT = GAL / "earlier"  # superseded by cover-tile.png, which survives the crop of the gallery tile (doc 41)
ASSETS = ROOT / "design" / "brand-kits" / "goodnight-inn-wakeup" / "assets"
FRONT = GAL / "report-page2.png"                                                              # Recommended: A, as last saved
BACK = ROOT / "project" / "deliverables" / "final-room-to-invest" / "step-tints" / "page2-what-waits.png"  # What waits, and why
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

NIGHT, COFFEE_BLUE, OAT, ORANGE = "#12233D", "#2589D8", "#F5E7DC", "#FF783D"

args = sys.argv[1:]
W, H = 1920, 1080
if "--size" in args:
    W, H = (int(n) for n in args[args.index("--size") + 1].split("x"))
SUFFIX = "" if (W, H) == (1920, 1080) else f"-{W}x{H}"


def uri(p):
    return Path(p).resolve().as_uri()


CHECK = ("<svg width='34' height='34' viewBox='0 0 34 34' style='flex:none'><circle cx='17' cy='17' r='17' fill='" + COFFEE_BLUE + "'/>"
         "<path d='M9.5 17.5l5 5 10-11' fill='none' stroke='#fff' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/></svg>")
SHOT = "position:absolute;border-radius:14px;box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.10)"

html = f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:'Segoe UI',sans-serif;color:#fff;background:{NIGHT};position:relative;
  background-image:radial-gradient(1200px 800px at 88% -10%, #24467A 0%, rgba(36,70,122,0) 60%),
                   radial-gradient(900px 700px at -10% 110%, #0B1729 0%, rgba(11,23,41,0) 60%)}}
.stage{{position:absolute;left:{(W - 1920) // 2}px;top:{(H - 1080) // 2}px;width:1920px;height:1080px}}
.logo{{position:absolute;left:100px;top:76px;height:58px}}
h1{{position:absolute;left:100px;top:196px;font-size:90px;font-weight:600;letter-spacing:-.015em;line-height:1.05;white-space:nowrap}}
h1 .hot{{color:{ORANGE}}}
.sub{{position:absolute;left:100px;top:600px;width:720px;font-size:29px;line-height:1.36;color:{OAT};opacity:.92}}
.badge{{position:absolute;left:100px;top:748px;height:78px;padding:0 36px 0 22px;border-radius:39px;background:{OAT};color:{NIGHT};
  font-size:35px;font-weight:600;display:flex;align-items:center;gap:16px;box-shadow:0 10px 30px rgba(0,0,0,.35)}}
.proof{{position:absolute;left:100px;top:852px;font-size:24px;color:{OAT};opacity:.86}}
.foot{{position:absolute;left:100px;bottom:66px;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:{OAT};opacity:.66}}
</style></head><body><div class='stage'>
<img class='logo' src='{uri(ASSETS / 'gi-lockup-reversed.svg')}' alt='Goodnight Inn'>
<h1>456 ways<br>to spend $60M.<br><span class='hot'>The best one<br>spends $9.4M.</span></h1>
<p class='sub'>A Board report for Goodnight Inn, the budget brand with the fullest hotels of the group. Think you can beat our plan? Build your own.</p>
<div class='badge'>{CHECK}<span>100% native Power BI visuals</span></div>
<p class='proof'>No custom visuals &nbsp;·&nbsp; 2 pages &nbsp;·&nbsp; 3 scenarios &nbsp;·&nbsp; all 456 packages computed</p>
<div style='{SHOT};left:920px;top:64px;width:1180px;height:420px;overflow:hidden;border-radius:14px 14px 0 0'><img src='{uri(BACK)}' style='width:1180px;display:block' alt=''></div>
<img src='{uri(FRONT)}' style='{SHOT};left:1010px;top:452px;width:1180px' alt=''>
<div class='foot'>Room to Invest &nbsp;·&nbsp; Power BI Dataviz World Champs 2027 &nbsp;·&nbsp; Round 1</div>
</div></body></html>"""

OUT.mkdir(parents=True, exist_ok=True)
page = OUT / f"cover-final{SUFFIX}.html"
png = OUT / f"cover-final{SUFFIX}.png"
page.write_text(html, encoding="utf-8")
png.unlink(missing_ok=True)
subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", f"--window-size={W},{H}",
                f"--user-data-dir={Path.home() / 'AppData' / 'Local' / 'Temp' / 'gi-cover-edge'}", f"--screenshot={png}", page.as_uri()],
               check=False, capture_output=True, timeout=120)
for _ in range(60):  # Edge can return before the file is written
    if png.exists() and png.stat().st_size > 0:
        break
    time.sleep(0.5)
print(f"cover-final{SUFFIX}.png", "written" if png.exists() else "NOT written")
