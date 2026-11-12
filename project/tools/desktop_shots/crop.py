"""Crop the report page out of a Desktop Bridge capture, anchored on the white card frames.

Both pages draw their card frames from logical x 32 to 1888 and y 184 to 1016 (opzet-layout.json), so the white
extent gives the page scale k and origin. Writes the native-resolution page and a 1920 x 1080 version.
usage: python crop.py <raw.png> <out-native.png> <out-1920.png>
"""
import json
import sys

import numpy as np
from PIL import Image

raw, out_native, out_1920 = sys.argv[1:4]
im = Image.open(raw).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape
white = (a[:, :, 0] == 255) & (a[:, :, 1] == 255) & (a[:, :, 2] == 255)
pane = np.where(white.mean(axis=0) > 0.9)[0]          # Desktop's collapsed Filters pane: white over the full height
xmax = int(pane.min()) if len(pane) else W
w2 = white[:, :xmax]
rows = np.where(w2.sum(axis=1) > 0.3 * xmax)[0]
T, B = int(rows.min()), int(rows.max())
cols = np.where(w2[T:B + 1].sum(axis=0) > 0.5 * (B - T))[0]
L, R = int(cols.min()), int(cols.max())
# white starts just inside the 1 px hairline border of each frame: logical 33 .. 1887, 185 .. 1015
k = (R - L + 1) / 1854
kv = (B - T + 1) / 830
ox, oy = L - 33 * k, T - 185 * k
box = (round(ox), round(oy), round(ox + 1920 * k), round(oy + 1080 * k))
crop = im.crop(box)
crop.save(out_native)
crop.resize((1920, 1080), Image.LANCZOS).save(out_1920)
print(json.dumps({"raw": [W, H], "frames": [L, T, R, B], "k": round(k, 4), "k_vertical": round(kv, 4),
                  "box": box, "native": list(crop.size)}))
