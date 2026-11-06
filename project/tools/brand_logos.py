"""Goodnight Inn logo families for both brand-kit options, as font-independent SVG.

Wordmarks are shaped with HarfBuzz (kerning applied) and converted to outlines
with fontTools, so the logo renders identically everywhere, including as an
embedded PNG under Publish-to-Web. Outline fonts (OFL-1.1, via Fontsource):
  option 1 (design/brand-kits/goodnight-inn): Gelasio (Eben Sorkin), the
           metric-compatible twin of Georgia
  option 2 (design/brand-kits/goodnight-inn-hanger): Lexend SemiBold
           (Bonnie Shaver-Troup, Thomas Jockin et al.)

Setup (one time, outside the repo; fonts are not committed):
  npm install @fontsource/gelasio@5 @fontsource/lexend@5
  pip install fonttools uharfbuzz
  python -c "import glob,os;from fontTools.ttLib import TTFont;[ (lambda t:(setattr(t,'flavor',None),t.save('sfnt/'+os.path.basename(f))))(TTFont(f)) for f in glob.glob('node_modules/@fontsource/*/files/*-latin-*.woff')]"
  (HarfBuzz reads raw sfnt, not WOFF: convert first, into a folder named sfnt/)

Run:
  python project/tools/brand_logos.py <sfnt_dir> design/brand-kits/goodnight-inn/assets design/brand-kits/goodnight-inn-hanger/assets
Then export 2x PNGs beside each SVG (any headless browser; the session used Playwright).
"""
import os, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS, OUT1, OUT2 = sys.argv[1], sys.argv[2], sys.argv[3]

def outline(font_path, text, size, x, y, tracking=0.0):
    """Return (svg path d, advance width in px) for text set at baseline (x, y)."""
    blob = hb.Blob.from_file_path(font_path)
    face = hb.Face(blob)
    font = hb.Font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    tt = TTFont(font_path)
    upem = tt["head"].unitsPerEm
    gs = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    scale = size / upem
    pen = SVGPathPen(gs)
    cx = 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        tx = x + (cx + pos.x_offset) * scale
        ty = y - pos.y_offset * scale
        gs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, tx, ty)))
        cx += pos.x_advance + tracking * upem
    return pen.getCommands(), cx * scale

def svg(w, h, body, label, bg=None):
    bgrect = f'<rect width="{w}" height="{h}" fill="{bg}"/>\n' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{label}">\n{bgrect}{body}\n</svg>\n')

def write(out, files):
    os.makedirs(out, exist_ok=True)
    for name, content in files.items():
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(content)
        print("wrote", os.path.join(out, name))

# ---------------------------------------------------------------- option 1
NIGHT, LINEN, LAMP_MARK = "#1B2638", "#FFFCF6", "#C2690A"

def mark1(tile=NIGHT, moon=LINEN, pane=LAMP_MARK, mid="m"):
    return "\n".join([
        f'<defs><mask id="moon-{mid}"><rect width="96" height="96" fill="white"/>'
        f'<circle cx="61" cy="31" r="15" fill="black"/></mask></defs>',
        f'<rect width="96" height="96" rx="10" fill="{tile}"/>',
        f'<circle cx="66" cy="34" r="17" fill="{moon}" mask="url(#moon-{mid})"/>',
        f'<rect x="18" y="44" width="24" height="30" rx="2" fill="{pane}"/>',
        f'<rect x="29" y="44" width="2" height="30" fill="{tile}"/>',
        f'<rect x="18" y="58" width="24" height="2" fill="{tile}"/>',
        f'<rect x="12" y="76" width="72" height="3" rx="1.5" fill="{moon}"/>',
    ])

def wordmark1(x, y, ink, size=40):
    reg = os.path.join(FONTS, "gelasio-latin-400-normal.woff")
    ita = os.path.join(FONTS, "gelasio-latin-400-italic.woff")
    d1, w1 = outline(reg, "Goodnight ", size, x, y)
    d2, w2 = outline(ita, "Inn", size, x + w1, y)
    return f'<path d="{d1} {d2}" fill="{ink}"/>', w1 + w2

wm, wmw = wordmark1(116, 62, NIGHT)
W1 = int(116 + wmw + 8)
wm_rev, _ = wordmark1(116, 62, LINEN)
write(OUT1, {
    "goodnight-inn-mark.svg": svg(96, 96, mark1(), "Goodnight Inn"),
    "goodnight-inn-mark-mono.svg": svg(96, 96, mark1(pane=LINEN, mid="mono"), "Goodnight Inn"),
    "goodnight-inn-lockup.svg": svg(W1, 96, mark1() + "\n" + wm, "Goodnight Inn"),
    "goodnight-inn-lockup-reversed.svg": svg(W1, 96, mark1(tile=LINEN, moon=NIGHT, mid="rev") + "\n" + wm_rev,
                                             "Goodnight Inn", bg=NIGHT),
})

# ---------------------------------------------------------------- option 2
# The door hanger: a pillow-soft tall tile with the handle hole and slit, and a
# sleeping face (two closed eyes). Awake variant (open eyes) is the P2 state icon.
INK, RASP, WHITE, CANVAS = "#24192B", "#B5175F", "#FFFFFF", "#F5F3F0"

def hanger(x=0, y=0, fill=RASP, face=WHITE, awake=False, mid="h"):
    hole = (f'<defs><mask id="hole-{mid}"><rect x="{x}" y="{y}" width="64" height="104" fill="white"/>'
            f'<circle cx="{x+32}" cy="{y+24}" r="10" fill="black"/>'
            f'<rect x="{x+32}" y="{y+22.5}" width="40" height="3" fill="black"/></mask></defs>')
    body = f'<rect x="{x+4}" y="{y+4}" width="56" height="96" rx="14" fill="{fill}" mask="url(#hole-{mid})"/>'
    if awake:
        eyes = (f'<circle cx="{x+22}" cy="{y+62}" r="4" fill="{face}"/>'
                f'<circle cx="{x+42}" cy="{y+62}" r="4" fill="{face}"/>')
    else:
        eyes = (f'<path d="M{x+16} {y+60} q6 7 12 0 M{x+36} {y+60} q6 7 12 0" fill="none" '
                f'stroke="{face}" stroke-width="4" stroke-linecap="round"/>')
    return "\n".join([hole, body, eyes])

def wordmark2(x, y, ink, size=40):
    f = os.path.join(FONTS, "lexend-latin-600-normal.woff")
    d, w = outline(f, "goodnight inn", size, x, y, tracking=-0.01)
    return f'<path d="{d}" fill="{ink}"/>', w

wm2, w2 = wordmark2(84, 66, INK)
W2 = int(84 + w2 + 8)
wm2_rev, _ = wordmark2(84, 66, WHITE)
write(OUT2, {
    "goodnight-inn-hanger.svg": svg(64, 104, hanger(), "Goodnight Inn"),
    "goodnight-inn-hanger-awake.svg": svg(64, 104, hanger(awake=True, mid="a"), "Goodnight Inn, awake"),
    "goodnight-inn-hanger-mono.svg": svg(64, 104, hanger(fill=INK, mid="mono"), "Goodnight Inn"),
    "goodnight-inn-hanger-awake-on-accent.svg": svg(64, 104, hanger(fill=WHITE, face=RASP, awake=True, mid="aoa"),
                                                    "Goodnight Inn, awake"),
    "goodnight-inn-lockup.svg": svg(W2, 104, hanger() + "\n" + wm2, "Goodnight Inn"),
    "goodnight-inn-lockup-reversed.svg": svg(W2, 104, hanger(fill=WHITE, face=INK, mid="rev") + "\n" + wm2_rev,
                                             "Goodnight Inn", bg=INK),
})
