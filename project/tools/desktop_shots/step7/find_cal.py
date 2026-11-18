"""Find the Tangerine calibration rectangle in a t_cal capture; write 'x0 x1 y0 y1' (capture px, x1 and y1 exclusive)."""
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert("RGB"); px = im.load(); W, H = im.size
on = lambda p: abs(p[0] - 0xE0) < 12 and abs(p[1] - 0x5A) < 12 and abs(p[2] - 0x22) < 12  # noqa: E731
cols = [x for x in range(W) if sum(on(px[x, y]) for y in range(0, H, 3)) > 20]
rows = [y for y in range(H) if sum(on(px[x, y]) for x in range(0, W, 3)) > 20]
out = f"{cols[0]} {cols[-1] + 1} {rows[0]} {rows[-1] + 1}"
open(sys.argv[2], "w").write(out)
print(out, "capture", W, H, "scale", (cols[-1] + 1 - cols[0]) / 480, (rows[-1] + 1 - rows[0]) / 270)
