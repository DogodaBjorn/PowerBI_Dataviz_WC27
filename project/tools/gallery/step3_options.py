"""A sketch, not the report (16 Nov 2026 night, doc 38): four ways to give step 3 its own accent, drawn side by side so
Bjorn can choose before anything is built. The plan bar's four segments at their real widths ($9.4M, $12.4M, $29.5M,
$8.7M of $60M) and four rows of the table's bars (a move of package A, of step 2, one that is not in the plan, the refresh).

  python project/tools/gallery/step3_options.py   ->  project/deliverables/final-room-to-invest/step3-accent/options.png
"""
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "project" / "deliverables" / "final-room-to-invest" / "step3-accent"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

BLUE, NIGHT, SLATE, GREY, LIGHT, DUSK, BURNT, DEEP = "#2589D8", "#12233D", "#717B8B", "#8E897D", "#C9C4B7", "#4B5466", "#A63F0E", "#1763A8"
CLAY, PALE_BLUE = "#C17956", "#8DBBE8"  # Burnt Tangerine at 70 % on white; the kit's sequential blue, third step
# name, what it is, step 3, outside the plan, the ink of step 3's label
OPTIONS = [
    ("Now", "slate for step 3, Warm Grey for what is not in the plan", SLATE, GREY, NIGHT),
    ("A · Clay", "step 3 in a softened Burnt Tangerine (the brand's second colour at 70 %)", CLAY, GREY, BURNT),
    ("B · Recede the rest", "step 3 stays slate; what is not in the plan goes to the kit's light neutral", SLATE, LIGHT, NIGHT),
    ("A + B · Clay, and the rest recedes", "both: three accents for three steps, everything else pale", CLAY, LIGHT, BURNT),
    ("C · Pale Coffee", "step 3 in the kit's light blue: the same family as package A, further away", PALE_BLUE, GREY, NIGHT),
]
SEG = [9.4, 12.4, 29.5, 8.7]
ROWS = [("Kiosks at the 20 busiest hotels", "package A", 0.206, "a"), ("Gatwick +40 rooms", "step 2 · 2028", 0.158, "2"),
        ("Energy programme", "not now", 0.118, "x"), ("Refresh, 10 oldest hotels", "step 3 · 2028", 0.079, "3")]

W = 1920
blocks = []
for name, what, step3, rest, ink3 in OPTIONS:
    fills = [BLUE, NIGHT, step3, rest]
    x, segs, labels = 0, [], []
    names = [("Step 1 · package A", DEEP), ("Step 2 · airport rooms", NIGHT), ("Step 3 · the refresh", ink3), ("Not needed · $8.7M", NIGHT)]
    for v, f, (lab, ink) in zip(SEG, fills, names):
        w = v / 60 * 1100
        segs.append(f"<rect x='{x:.1f}' y='26' width='{w - 3:.1f}' height='30' fill='{f}'/>")
        labels.append(f"<text x='{x:.1f}' y='16' font-size='15' fill='{ink}'>{lab}</text>")
        x += w
    rows = []
    for i, (move, status, y, kind) in enumerate(ROWS):
        fill = {"a": BLUE, "2": NIGHT, "3": step3, "x": rest}[kind]
        ink = {"a": DEEP, "2": NIGHT, "3": ink3 if ink3 != NIGHT else DUSK, "x": DUSK}[kind]
        yy = 8 + i * 30
        ground = "<rect x='0' y='%d' width='640' height='30' fill='#EAF2FB'/>" % (yy - 8) if kind == "a" else ""
        rows.append(f"{ground}<text x='8' y='{yy + 12}' font-size='15' fill='{NIGHT}'>{move}</text>"
                    f"<text x='290' y='{yy + 12}' font-size='15' fill='{ink}'>{status}</text>"
                    f"<rect x='430' y='{yy - 2}' width='{y * 420:.1f}' height='20' fill='{fill}'/>"
                    f"<text x='632' y='{yy + 12}' font-size='15' fill='{NIGHT}' text-anchor='end'>{y * 100:.1f}%</text>")
    blocks.append(f"""
<section>
  <h2>{name}</h2><p>{what}</p>
  <div class='card'>
    <svg width='1100' height='62' font-family='Segoe UI'>{''.join(labels)}{''.join(segs)}</svg>
    <svg width='640' height='122' font-family='Segoe UI' style='margin-left:48px'>{''.join(rows)}<line x1='463.6' x2='463.6' y1='0' y2='122' stroke='{NIGHT}' stroke-width='1'/></svg>
  </div>
</section>""")

H = 60 + len(OPTIONS) * 246
html = f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><style>
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:'Segoe UI',sans-serif;background:#F3F1EA;color:{NIGHT};padding:30px 40px}}
section{{margin-bottom:22px}} h2{{font-size:22px;font-weight:600}} p{{font-size:16px;color:{DUSK};margin:2px 0 8px}}
.card{{background:#fff;border-radius:12px;padding:20px 24px;display:flex;align-items:center;box-shadow:0 2px 10px rgba(18,35,61,.10)}}
</style></head><body>{''.join(blocks)}</body></html>"""
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "options.html").write_text(html, encoding="utf-8")
png = OUT / "options.png"
png.unlink(missing_ok=True)
subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", f"--window-size={W},{H}",
                f"--user-data-dir={Path.home() / 'AppData' / 'Local' / 'Temp' / 'gi-cover-edge'}", f"--screenshot={png}", (OUT / "options.html").as_uri()],
               check=False, capture_output=True, timeout=120)
for _ in range(60):
    if png.exists() and png.stat().st_size > 0:
        break
    time.sleep(0.5)
print("options.png", "written" if png.exists() else "NOT written")
