"""The cover as the Contests Gallery shows it on its tiles (17 Nov 2026, doc 41).

  python project/tools/gallery/cover_tile.py

Bjorn posted the entry on 16 Nov; his screenshot of the gallery shows what no document said: a tile shows the cover
538 px wide and 225 px high, a band of 2.39:1 cut from the image's middle. Of a 1920 x 1080 image that is the part from
y 138 to y 942, at 0.28 of its size. cover-final.png loses its logo to that cut, and its badge is 10 px high on a tile.
This cover is the same design with everything that matters inside the band and large enough for a tile:

  the logo, the headline (86 px, 24 px on a tile), the badge "100% native Power BI visuals" (44 px, 12 px on a tile);
  the two views of page 2 at the right, the dots of the 456 packages at the band's top.

Writes to project/deliverables/final-room-to-invest/gallery/: cover-tile.png (1920 x 1080), cover-tile.jpg (the same,
for a form that refuses a PNG or its size) and cover-tile-as-shown.png (the band, 538 x 225: what a tile shows).
"""
import subprocess
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "project" / "deliverables" / "final-room-to-invest" / "gallery"
ASSETS = ROOT / "design" / "brand-kits" / "goodnight-inn-wakeup" / "assets"
FRONT = OUT / "report-page2.png"                                                              # Recommended: A, as last saved
BACK = ROOT / "project" / "deliverables" / "final-room-to-invest" / "step-tints" / "page2-what-waits.png"  # What waits, and why
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

NIGHT, COFFEE_BLUE, OAT, ORANGE = "#12233D", "#2589D8", "#F5E7DC", "#FF783D"
W, H = 1920, 1080
TILE = (538, 225)                      # measured on the gallery, 16 Nov
BAND_H = round(W * TILE[1] / TILE[0])  # 803
BAND = ((H - BAND_H) // 2, (H - BAND_H) // 2 + BAND_H)


def uri(p):
    return Path(p).resolve().as_uri()


CHECK = ("<svg width='44' height='44' viewBox='0 0 34 34' style='flex:none'><circle cx='17' cy='17' r='17' fill='" + COFFEE_BLUE + "'/>"
         "<path d='M9.5 17.5l5 5 10-11' fill='none' stroke='#fff' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/></svg>")
SHOT = "position:absolute;border-radius:14px;box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.10)"

html = f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:'Segoe UI',sans-serif;color:#fff;background:{NIGHT};position:relative;
  background-image:radial-gradient(1200px 800px at 88% -10%, #24467A 0%, rgba(36,70,122,0) 60%),
                   radial-gradient(900px 700px at -10% 110%, #0B1729 0%, rgba(11,23,41,0) 60%)}}
.logo{{position:absolute;left:96px;top:176px;height:54px}}
h1{{position:absolute;left:96px;top:262px;font-size:86px;font-weight:600;letter-spacing:-.015em;line-height:1.04;white-space:nowrap}}
h1 .hot{{color:{ORANGE}}}
.badge{{position:absolute;left:96px;top:672px;height:96px;padding:0 44px 0 26px;border-radius:48px;background:{OAT};color:{NIGHT};
  font-size:44px;font-weight:600;display:flex;align-items:center;gap:20px;box-shadow:0 10px 30px rgba(0,0,0,.35)}}
.proof{{position:absolute;left:96px;top:800px;font-size:26px;color:{OAT};opacity:.86}}
.foot{{position:absolute;left:96px;bottom:56px;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:{OAT};opacity:.66}}
</style></head><body>
<img class='logo' src='{uri(ASSETS / 'gi-lockup-reversed.svg')}' alt='Goodnight Inn'>
<h1>456 ways<br>to spend $60M.<br><span class='hot'>The best one<br>spends $9.4M.</span></h1>
<div class='badge'>{CHECK}<span>100% native Power BI visuals</span></div>
<p class='proof'>No custom visuals &nbsp;·&nbsp; 2 pages &nbsp;·&nbsp; 3 scenarios &nbsp;·&nbsp; all 456 packages computed</p>
<div style='{SHOT};left:940px;top:{BAND[0] + 22}px;width:1180px;height:330px;overflow:hidden;border-radius:14px 14px 0 0'><img src='{uri(BACK)}' style='width:1180px;display:block' alt=''></div>
<img src='{uri(FRONT)}' style='{SHOT};left:1030px;top:{BAND[0] + 330}px;width:1180px' alt=''>
<div class='foot'>Room to Invest &nbsp;·&nbsp; Power BI Dataviz World Champs 2027 &nbsp;·&nbsp; Round 1</div>
</body></html>"""

page, png = OUT / "earlier" / "cover-tile.html", OUT / "cover-tile.png"
page.write_text(html, encoding="utf-8")
png.unlink(missing_ok=True)
subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", f"--window-size={W},{H}",
                f"--user-data-dir={Path.home() / 'AppData' / 'Local' / 'Temp' / 'gi-cover-edge'}", f"--screenshot={png}", page.as_uri()],
               check=False, capture_output=True, timeout=120)
for _ in range(60):  # Edge can return before the file is written
    if png.exists() and png.stat().st_size > 0:
        break
    time.sleep(0.5)
im = Image.open(png).convert("RGB")
im.save(OUT / "cover-tile.jpg", quality=90, optimize=True)
im.crop((0, BAND[0], W, BAND[1])).resize(TILE, Image.LANCZOS).save(OUT / "cover-tile-as-shown.png")
print(f"cover-tile.png {im.size}, {png.stat().st_size // 1024} kB; cover-tile.jpg {(OUT / 'cover-tile.jpg').stat().st_size // 1024} kB; the band y {BAND[0]} to {BAND[1]}")
