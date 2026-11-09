"""OPTIONAL canvas for the night-glow variant (plan 10-design-rebuild.md, item D7): only used if
Bjorn waives design hard rule 6 for the header zone. The spec itself (variant "night") needs no
image from this script: its flat Night zone is drawn by opzet_backgrounds.mjs.
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

Run: python project/tools/brand_canvas_v3.py <out_dir>
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw

W, H = 1920, 1080
HORIZON = 340                     # bottom of the dark header zone (night canvas)
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


def night(out):
    img = np.empty((H, W, 3), np.float32); img[:] = rgb("#F3F1EA")
    img = mix(img, "#F7DFCF", glow(1880, 1180, 900, 0.55))
    img = mix(img, "#E3EDF8", glow(0, HORIZON, 800, 0.45))
    t = (xx / W)[..., None]                                    # Night (left) to navy (right)
    top = rgb("#0F1E36") * (1 - t) + rgb("#163760") * t
    top = mix(top, "#2589D8", glow(1760, 250, 620, 0.22))      # Coffee Blue light, right, below the band text
    zone = (yy < HORIZON)[..., None]
    img = np.where(zone, top, img)
    # the faceless hanger, tilted 10 degrees, cropped by the horizon
    m = hanger_mask(7.2, 10)
    canvas = Image.new("L", (W, H), 0)
    canvas.paste(m, (1350, -150))
    a = (np.asarray(canvas, np.float32) / 255.0 * 0.06)[..., None] * zone
    img = mix(img, "#E9E5D6", a)
    img[HORIZON - 1:HORIZON] = mix(img[HORIZON - 1:HORIZON], "#2589D8", 0.35)   # a hairline of light on the horizon
    finish(img, os.path.join(out, "canvas-night.jpg"))


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    night(out)
