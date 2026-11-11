"""OPTIONAL canvas for the night-glow variant (plan 10-design-rebuild.md, item D7): only used if
Bjorn waives design hard rule 6 for gradients. The spec itself (variant "night") needs no image
from this script: its flat Night zone and the faded hanger (D2b) are drawn as SVG by
opzet_backgrounds.mjs.
Requires numpy and Pillow (design-time tool, not part of the stdlib build pipeline).

Canvas backgrounds for the Goodnight Inn 3.x report (1920 x 1080 JPEG, for
Power BI's page canvas background, image fit "Fit", transparency 0 %).

  canvas-light.jpg  "Morning light": the Oat page lit by a cool Ice glow top-left
                    and a warm glow bottom-right.
  canvas-night.jpg  "Night header": a deep Night-to-navy header zone (band,
                    headline and the top of the cards sit in it), a Coffee Blue
                    glow and the faceless door hanger, tilted and cropped, at 6 %;
                    below the horizon the Oat page with a soft warm glow.

Depth lives in the chrome only: nothing here sits behind a chart's plot area
except the warm glow, which stays under 4 % luminance change on white cards
(cards are opaque, so it never reaches the data).

Run: python project/tools/brand_canvas_v3.py <out_dir>                      # the comps (horizon 340)
     python project/tools/brand_canvas_v3.py <out_dir> <opzet-layout.json>   # the report (plan 11)

Plan 11 (Björn chose night-glow, D7 waiver in status.yaml 2026-11-09): with a slot map the horizon is the top of the
report's first card row + 64 px (y 248 on v3; plan 10's +128 assumed main's layout), the Coffee Blue light keeps its
place in the zone (250 of 340), and the result is project/deliverables/backgrounds/canvas-night.jpg, which
project/tools/opzet_report.py places as a decorative image visual (z_canvas) under every other visual: an image
visual scales with the content, where a page background with Fit drifted (7 Nov, BUILD_LOG).
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw

W, H = 1920, 1080
HORIZON = 340                     # bottom of the dark header zone (night canvas); the report's comes from its slot map
if len(sys.argv) > 2:
    _layout = json.load(open(sys.argv[2], encoding="utf-8"))
    # report pages only (tooltip pages have their own banner); a card's state (round 4) does not move the first row
    _tops = {min(c["y"] for c in p["cards"]) for p in _layout["pages"] if p.get("cards") and not p.get("tooltip")}
    assert len(_tops) == 1, f"pages start their first card row at different heights: {_tops}"
    HORIZON = _tops.pop() + 64
rng = np.random.default_rng(7)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)


def rgb(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], np.float32)


def glow(cx, cy, r, strength):
    d2 = ((xx - cx) ** 2 + (yy - cy) ** 2) / (r * r)
    return (np.exp(-2.2 * d2) * strength)[..., None]


def mix(img, color, a):
    return img * (1 - a) + rgb(color) * a


def finish(img, path):
    img = img + rng.normal(0, 0.7, img.shape)          # dither: no gradient banding
    Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(path, quality=90, optimize=True)
    print("wrote", os.path.basename(path), os.path.getsize(path) // 1024, "KB")


def hanger_mask(scale, tilt):
    """Faceless hanger (56 x 96, r 14, hole r 10 at (28, 20), slit to the right) as an L mask."""
    k = scale
    w, h = int(80 * k), int(110 * k)
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    ox, oy = 12 * k, 7 * k
    d.rounded_rectangle([ox, oy, ox + 56 * k, oy + 96 * k], radius=14 * k, fill=255)
    d.ellipse([ox + 28 * k - 10 * k, oy + 20 * k - 10 * k, ox + 28 * k + 10 * k, oy + 20 * k + 10 * k], fill=0)
    d.rectangle([ox + 28 * k, oy + 18.5 * k, ox + 56 * k + 1, oy + 21.5 * k], fill=0)
    return m.rotate(tilt, resample=Image.BICUBIC, center=(ox + 28 * k, oy + 20 * k), expand=False)


def light(out):
    img = np.empty((H, W, 3), np.float32); img[:] = rgb("#F3F1EA")
    img = mix(img, "#D6E6F7", glow(160, -120, 1150, 0.80))     # cool Ice light, top-left
    img = mix(img, "#F7DFCF", glow(1880, 1180, 980, 0.70))    # warm light, bottom-right
    finish(img, os.path.join(out, "canvas-light.jpg"))


def night(out, extra_top=0, name="canvas-night.jpg"):
    """The night-glow canvas. extra_top (round 6, 11 Nov): the same scene with that many rows of banner added above it,
    for the page BACKGROUND image: Desktop paints the page background over a display area 20 px taller than the page,
    so a 1920 x 1100 background whose scene starts 20 px lower shows the banner from the very top, seamless with the
    on-page canvas visual (which stays the exact 1920 x 1080 scene, aligned with the cards)."""
    h = H + extra_top
    y, x = np.mgrid[0:h, 0:W].astype(np.float32)
    y = y - extra_top                                          # scene coordinates: row 0 of the page at y = 0
    def g(cx, cy, r, strength):
        d2 = ((x - cx) ** 2 + (y - cy) ** 2) / (r * r)
        return (np.exp(-2.2 * d2) * strength)[..., None]
    img = np.empty((h, W, 3), np.float32); img[:] = rgb("#F3F1EA")
    img = mix(img, "#F7DFCF", g(1880, 1180, 900, 0.55))
    img = mix(img, "#E3EDF8", g(0, HORIZON, 800, 0.45))
    t = (x / W)[..., None]                                     # Night (left) to navy (right)
    top = rgb("#0F1E36") * (1 - t) + rgb("#163760") * t
    top = mix(top, "#2589D8", g(1760, round(HORIZON * 250 / 340), 620, 0.22))  # Coffee Blue light, right, below the band text
    zone = (y < HORIZON)[..., None]
    img = np.where(zone, top, img)
    # the faceless hanger, tilted 10 degrees, cropped by the horizon
    m = hanger_mask(7.2, 10)
    canvas = Image.new("L", (W, h), 0)
    canvas.paste(m, (1350, -150 + extra_top))
    a = (np.asarray(canvas, np.float32) / 255.0 * 0.06)[..., None] * zone
    img = mix(img, "#E9E5D6", a)
    hz = HORIZON + extra_top
    img[hz - 1:hz] = mix(img[hz - 1:hz], "#2589D8", 0.35)     # a hairline of light on the horizon
    finish(img, os.path.join(out, name))


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    night(out)
    night(out, extra_top=20, name="canvas-night-page.jpg")   # the page background (Desktop's display strip)
