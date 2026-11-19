"""One sheet of the plan chart in Low, Expected and High, cut from three stitched strip renders (step C of doc 25).

  python plan_sheet.py <out.png> <rec_Low.png> <rec_Expected.png> <rec_High.png>
"""
import sys

from PIL import Image

BOX = (780, 776, 1890, 1006)  # page px: from the plan bar to the milestone line, the chart's column
ims = []
for f in sys.argv[2:5]:
    im = Image.open(f)
    s = im.width / 1920
    ims.append(im.crop(tuple(round(v * s) for v in BOX)))
w, h = ims[0].size
sheet = Image.new("RGB", (w, h * 3 + 20), "white")
for i, im in enumerate(ims):
    sheet.paste(im, (0, i * (h + 10)))
sheet.save(sys.argv[1])
print(sheet.size)
