"""Goodnight Inn logo family, kit 3.0 (design/brand-kits/goodnight-inn-wakeup,
assets/). Font-independent SVG, original work.

3.0 is the business register: the door hanger stays as the symbol but loses
its face, and the wordmark is a calm lowercase "goodnight inn." with a
Tangerine full stop, the brand's one signal color, closing the sentence the
way the promise does ("A good night. A fair price.").

Outline font: Plus Jakarta Sans ExtraBold (Tokotype, OFL-1.1), via Fontsource.
Setup: npm install @fontsource/plus-jakarta-sans@5; convert the
*-latin-800-normal.woff to raw sfnt (see brand_logos.py).

Run:
  python project/tools/brand_logos_v3.py <sfnt_dir> design/brand-kits/goodnight-inn-wakeup/assets
Then rsvg-convert -z 2 for @2x PNGs.
"""
import os, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTS, OUT = sys.argv[1], sys.argv[2]
FONT = os.path.join(FONTS, "plus-jakarta-sans-latin-800-normal.woff")
OAT, COFFEE, TANG, NIGHT, POSTER = "#E9E5D6", "#2589D8", "#E05A22", "#12233D", "#FF783D"


def outline(text, size, x, y, tracking=0.0):
    face = hb.Face(hb.Blob.from_file_path(FONT))
    font = hb.Font(face)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    tt = TTFont(FONT); upem = tt["head"].unitsPerEm; gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    s = size / upem
    glyphs, cx = [], 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        pen, bpen = SVGPathPen(gs), BoundsPen(gs)
        m = (s, 0, 0, -s, x + (cx + pos.x_offset) * s, y - pos.y_offset * s)
        gs[name].draw(TransformPen(pen, m)); gs[name].draw(TransformPen(bpen, m))
        glyphs.append((pen.getCommands(), bpen.bounds))
        cx += pos.x_advance + tracking * upem
    return glyphs, cx * s


def hanger(x=0, y=0, fill=COFFEE, mid="m"):
    """The hanger symbol: option 2's geometry, no face."""
    return (f'<defs><mask id="v3-{mid}" maskUnits="userSpaceOnUse" x="{x}" y="{y}" width="72" height="104">'
            f'<rect x="{x}" y="{y}" width="72" height="104" fill="white"/>'
            f'<circle cx="{x+32}" cy="{y+24}" r="10" fill="black"/>'
            f'<rect x="{x+32}" y="{y+22.5}" width="40" height="3" fill="black"/></mask></defs>'
            f'<rect x="{x+4}" y="{y+4}" width="56" height="96" rx="14" fill="{fill}" mask="url(#v3-{mid})"/>')


def wordmark(x, baseline, size, ink, stop=TANG):
    """'goodnight inn' in ink, the full stop in Tangerine. Returns (svg, right edge)."""
    glyphs, adv = outline("goodnight inn.", size, x, baseline, tracking=-0.015)
    body = " ".join(d for d, _ in glyphs[:-1])
    dot_d, dot_b = glyphs[-1]
    return (f'<path d="{body}" fill="{ink}"/><path d="{dot_d}" fill="{stop}"/>', dot_b[2])


def svg(w, h, inner, label, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{label}">\n{b}{inner}\n</svg>\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    files = {}
    files["gi-mark.svg"] = svg(64, 104, hanger(), "Goodnight Inn")
    files["gi-mark-mono-night.svg"] = svg(64, 104, hanger(fill=NIGHT, mid="n"), "Goodnight Inn")
    files["gi-mark-mono-oat.svg"] = svg(64, 104, hanger(fill=OAT, mid="o"), "Goodnight Inn")
    wm, r = wordmark(86, 80, 60, NIGHT)
    W = int(r + 6)
    files["gi-lockup.svg"] = svg(W, 104, hanger() + wm, "Goodnight Inn")
    wm_r, _ = wordmark(86, 80, 60, OAT, stop=POSTER)
    files["gi-lockup-reversed.svg"] = svg(W, 104, hanger(mid="r") + wm_r, "Goodnight Inn")
    wm_w, rw = wordmark(0, 64, 60, NIGHT)
    files["gi-wordmark.svg"] = svg(int(rw + 4), 84, wm_w, "Goodnight Inn")
    for name, content in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(content)
    print(len(files), "files")


if __name__ == "__main__":
    main()
