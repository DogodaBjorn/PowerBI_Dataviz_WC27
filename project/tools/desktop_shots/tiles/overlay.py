"""Overlay a page render on the comp: the comp's ink in red, the render's in cyan; where both have ink the pixel is dark.
usage: overlay.py <render_1920.png> <comp_page.png> <out prefix>"""
import sys
from PIL import Image, ImageChops
r = Image.open(sys.argv[1]).convert("L"); c = Image.open(sys.argv[2]).convert("L")
ov = Image.merge("RGB", (r, c, c))   # red channel = render, so comp-only ink shows red, render-only ink shows cyan
ov.save(sys.argv[3] + "_full.png")
for n, box in (("top", (0, 150, 1920, 300)), ("mid", (0, 300, 1920, 790)), ("bot", (0, 790, 1920, 1080))):
    ov.crop(box).save(f"{sys.argv[3]}_{n}.png")
