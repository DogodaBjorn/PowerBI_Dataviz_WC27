"""Stitch the 16 tile captures into one page image. usage: stitch.py <tiles dir> <cal txt> <out.png> [--page]
Writes <out> at capture resolution (about 1.84 px per page px) and <out>_1920.png resampled to page pixels."""
import sys
from PIL import Image
d, cal, out = sys.argv[1], sys.argv[2], sys.argv[3]
x0, x1, y0, y1 = map(int, open(cal).read().split())
tw, th = x1 - x0, y1 - y0
big = Image.new("RGB", (tw * 4, th * 4))
for r in range(4):
    for c in range(4):
        big.paste(Image.open(f"{d}/t_{r}_{c}.png").convert("RGB").crop((x0, y0, x1, y1)), (c * tw, r * th))
big.save(out)
big.resize((1920, 1080), Image.LANCZOS).save(out.replace(".png", "_1920.png"))
print(big.size, "scale", tw / 480, th / 270)
