"""Contact sheet: python sheet.py <out.png> <x,y,w,h crop> <cols> <scale> <file> [file ...]"""
import sys

from PIL import Image, ImageDraw

out, box, cols, scale, files = sys.argv[1], [int(v) for v in sys.argv[2].split(",")], int(sys.argv[3]), float(sys.argv[4]), sys.argv[5:]
x, y, w, h = box
tw, th = int(w * scale), int(h * scale)
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (tw * cols, (th + 18) * rows), "white")
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB").crop((x, y, x + w, y + h)).resize((tw, th), Image.LANCZOS)
    cx, cy = (i % cols) * tw, (i // cols) * (th + 18)
    sheet.paste(im, (cx, cy + 18))
    ImageDraw.Draw(sheet).text((cx + 4, cy + 3), f.replace("\\", "/").split("/")[-1][:70], fill="black")
sheet.save(out)
print(sheet.size)
