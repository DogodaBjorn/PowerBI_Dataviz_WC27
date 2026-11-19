"""A short film for LinkedIn about the entry (17 Nov 2026, doc 41): 16 seconds, 1080 x 1350 (4:5), no sound.

  python project/tools/gallery/promo_video.py [--still 5.6]

Drawn frame by frame with Pillow from what the report holds, and encoded with the ffmpeg that imageio_ffmpeg ships
(the one the reels of the Hugo's repository use; FFMPEG_PATH overrides). No generated footage, no stock.

  0.0 -  6.6   "The Board has $60M. I tested all 456 ways to spend it." The 456 packages arrive as dots (packages.json:
               capex against NPV through 2032, Expected case). "Only 6 pay back by 2032." The line, the six in blue.
               "The best one spends $9.4M." Package A in orange.
  6.7 -  9.4   "Full rooms. A slipping margin." Page 1, a slow pan.
  9.4 - 12.3   "One plan: fix the middleman first." Page 2, from the table to the $60M plan. "100% native Power BI visuals".
 12.3 - 16.0   The end card: Room to Invest, the contest, the badge, "Think you can beat my plan? Link in the comments."

Writes to project/deliverables/final-room-to-invest/linkedin/: room-to-invest-linkedin.mp4 and poster.png (a still).
--still T writes only the frame at T seconds (still-T.png), for a look without encoding.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
GAL = ROOT / "project" / "deliverables" / "final-room-to-invest" / "gallery"
OUT = ROOT / "project" / "deliverables" / "final-room-to-invest" / "linkedin"
ASSETS = ROOT / "design" / "brand-kits" / "goodnight-inn-wakeup" / "assets"
FONTS = Path(r"C:\Windows\Fonts")

W, H, FPS, DUR = 1080, 1350, 30, 16.0
NIGHT, OAT, ORANGE, SKY, GREY, BLUE, WHITE = "#12233D", "#F5E7DC", "#FF783D", "#5AAEF0", "#B9B2A3", "#2589D8", "#FFFFFF"
M = 80  # side margin


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def font(size, bold=True):
    return ImageFont.truetype(str(FONTS / ("seguisb.ttf" if bold else "segoeui.ttf")), size)


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def window(t, t_in, t_out, fade=0.35):
    """Opacity of an element that is there from t_in to t_out."""
    return min(ease((t - t_in) / fade), ease((t_out - t) / fade))


def faded(img, op):
    if op >= 0.999:
        return img
    out = img.copy()
    out.putalpha(img.getchannel("A").point(lambda a: int(a * op)))
    return out


def text_block(lines, size, bold=True, gap=1.1):
    """lines: [(text, colour)]; one RGBA image, left-aligned."""
    f = font(size, bold)
    asc, desc = f.getmetrics()
    lh = int(size * gap)
    w = max(int(f.getlength(t)) for t, _ in lines) + 8
    im = Image.new("RGBA", (w, lh * len(lines) + desc), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, (t, c) in enumerate(lines):
        d.text((0, i * lh), t, font=f, fill=rgb(c) + (255,))
    return im


def wrapped(text, size, width, colour, bold=False):
    f = font(size, bold)
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        if f.getlength((cur + " " + w_).strip()) <= width:
            cur = (cur + " " + w_).strip()
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    return text_block([(l, colour) for l in lines], size, bold, gap=1.32)


def chip(text, size=40):
    f = font(size)
    tw = int(f.getlength(text))
    h = int(size * 2.1)
    r = h // 2
    icon = int(size * 1.0)
    w = tw + icon + int(size * 2.0)
    S = 3
    big = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    d.rounded_rectangle((0, 0, w * S - 1, h * S - 1), radius=r * S, fill=rgb(OAT) + (255,))
    cx, cy, cr = int(size * 1.0) * S, h * S // 2, icon * S // 2
    d.ellipse((cx - cr, cy - cr, cx + cr, cy + cr), fill=rgb(BLUE) + (255,))
    k = cr / 17
    d.line([(cx - 7.5 * k, cy + 0.5 * k), (cx - 2.5 * k, cy + 5.5 * k), (cx + 7.5 * k, cy - 5.5 * k)], fill=(255, 255, 255, 255), width=max(2, int(3.4 * k)), joint="curve")
    im = big.resize((w, h), Image.LANCZOS)
    ImageDraw.Draw(im).text((int(size * 1.0) + icon // 2 + int(size * 0.45), (h - int(size * 1.34)) // 2), text, font=f, fill=rgb(NIGHT) + (255,))
    return im


def sprite(radius, colour, alpha=255, ring=None):
    S = 4
    r = radius * S
    pad = 4 * S
    im = Image.new("RGBA", (2 * r + 2 * pad, 2 * r + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((pad, pad, pad + 2 * r, pad + 2 * r), fill=rgb(colour) + (alpha,), outline=(rgb(ring) + (255,)) if ring else None, width=3 * S if ring else 0)
    return im.resize((im.width // S, im.height // S), Image.LANCZOS)


def rounded(img, radius=22):
    S = 3
    mask = Image.new("L", (img.width * S, img.height * S), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.width * S - 1, img.height * S - 1), radius=radius * S, fill=255)
    out = img.convert("RGBA")
    out.putalpha(mask.resize(img.size, Image.LANCZOS))
    return out


def background():
    import numpy as np
    y, x = np.mgrid[0:H, 0:W].astype("float32")
    base = np.array(rgb(NIGHT), dtype="float32")
    glow = np.array(rgb("#24467A"), dtype="float32")
    deep = np.array(rgb("#0B1729"), dtype="float32")
    g = np.clip(1 - np.hypot((x - W * 0.95) / 900, (y + 80) / 760), 0, 1) ** 1.6
    k = np.clip(1 - np.hypot((x + 60) / 800, (y - H * 1.05) / 760), 0, 1) ** 1.6
    img = base[None, None, :] * (1 - g[..., None]) + glow[None, None, :] * g[..., None]
    img = img * (1 - k[..., None]) + deep[None, None, :] * k[..., None]
    return Image.fromarray(img.clip(0, 255).astype("uint8"), "RGB").convert("RGBA")


# ---------------------------------------------------------------- the material
BG = background()
LOGO = Image.open(ASSETS / "gi-lockup-reversed@2x.png").convert("RGBA")
LOGO_S = LOGO.resize((int(LOGO.width * 56 / LOGO.height), 56), Image.LANCZOS)
LOGO_L = LOGO.resize((int(LOGO.width * 88 / LOGO.height), 88), Image.LANCZOS)
PAGE1 = Image.open(GAL / "report-page1.png").convert("RGB")
PAGE2 = Image.open(GAL / "report-page2.png").convert("RGB")
PK = json.loads((HERE / "packages.json").read_text(encoding="utf-8"))
assert len(PK) == 456 and sum(p["npv"] >= 0 for p in PK) == 6

BIG = 80
T1 = text_block([("The Board has $60M.", WHITE)], BIG)
T2 = text_block([("I tested all 456 ways", WHITE), ("to spend it.", WHITE)], BIG)
T3 = text_block([("Only 6 pay back", WHITE), ("by 2032.", WHITE)], BIG)
T4 = text_block([("The best one", ORANGE), ("spends $9.4M.", ORANGE)], BIG)
T5 = text_block([("Full rooms.", WHITE), ("A slipping margin.", ORANGE)], BIG)
T5S = wrapped("Goodnight Inn fills more rooms than any sister brand. So where does the money go?", 36, W - 2 * M, OAT)
T6 = text_block([("One plan:", WHITE), ("fix the middleman first.", ORANGE)], 76)
T6S = wrapped("$9.4M now. The rest of the $60M waits for one Board meeting in 2028.", 36, W - 2 * M, OAT)
CHIP = chip("100% native Power BI visuals", 40)
E_TITLE = text_block([("Room to Invest", WHITE)], 104)
E_SUB = text_block([("My entry for the Power BI", OAT), ("Dataviz World Champs 2027", OAT)], 46, bold=False, gap=1.3)
E_CTA = text_block([("Think you can beat my plan?", ORANGE)], 58)
E_LINK = text_block([("Link in the comments", WHITE)], 44, bold=False)
E_NAME = text_block([("TrainerBjorn", OAT)], 36, bold=False)
LBL_PAYS = text_block([("pays back by 2032", WHITE)], 30, bold=False)
LBL_A = text_block([("Package A", WHITE)], 34)

# the dots: capex $5M..$62M across, NPV +14M..-52M down
PX0, PX1, PY0, PY1 = 90, 990, 650, 1270


def X(c):
    return PX0 + (c / 1e6 - 5) / 57 * (PX1 - PX0)


def Y(n):
    return PY0 + (14 - n / 1e6) / 66 * (PY1 - PY0)


ZERO = Y(0)
ORDER = sorted(PK, key=lambda p: (p["capex"], -p["npv"]))
SP_GREY, SP_BLUE, SP_A = sprite(7, GREY, 170), sprite(11, SKY), sprite(17, ORANGE, ring=WHITE)
A = next(p for p in PK if p["preset"] == "A")
CARD = (M - 20, 520, W - M + 20, 1170)  # where a page shows
CW, CH = CARD[2] - CARD[0], CARD[3] - CARD[1]


def page_view(page, box0, box1, k):
    """The page cut from box0 to box1 (x, y, w; the height follows the card), at k of the way."""
    x = box0[0] + (box1[0] - box0[0]) * k
    y = box0[1] + (box1[1] - box0[1]) * k
    w = box0[2] + (box1[2] - box0[2]) * k
    h = w * CH / CW
    return rounded(page.resize((CW, CH), Image.BICUBIC, box=(x, y, x + w, y + h)))


def put(frame, img, xy, op=1.0, rise=0.0):
    if op <= 0.003:
        return
    frame.alpha_composite(faded(img, op), (int(xy[0]), int(xy[1] + rise)))


def frame_at(t):
    f = BG.copy()
    d = ImageDraw.Draw(f)
    put(f, LOGO_S, (M, 84), window(t, 0.0, 12.2))

    # ---- the 456 packages
    put(f, T1, (M, 190), o := window(t, 0.3, 3.4), rise=24 * (1 - ease((t - 0.3) / 0.5)))
    put(f, T2, (M, 300), o := window(t, 1.1, 3.4), rise=24 * (1 - ease((t - 1.1) / 0.5)))
    put(f, T3, (M, 190), window(t, 3.6, 6.5), rise=24 * (1 - ease((t - 3.6) / 0.5)))
    put(f, T4, (M, 380), window(t, 4.9, 6.5), rise=24 * (1 - ease((t - 4.9) / 0.5)))
    dots_out = ease((6.75 - t) / 0.35)
    if 1.3 < t < 6.8:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        zl = ease((t - 3.3) / 0.6)
        if zl > 0:
            ld.rectangle((PX0, PY0 - 40, PX0 + (PX1 - PX0) * zl, ZERO), fill=rgb(SKY) + (int(26 * zl),))
            ld.line((PX0, ZERO, PX0 + (PX1 - PX0) * zl, ZERO), fill=(255, 255, 255, 255), width=3)
            layer.alpha_composite(faded(LBL_PAYS, ease((t - 3.7) / 0.4)), (PX1 - LBL_PAYS.width, int(ZERO) - 46))
        blue = ease((t - 3.8) / 0.5)
        for i, p in enumerate(ORDER):
            a = ease((t - (1.4 + 1.7 * i / len(ORDER))) / 0.18)
            if a <= 0:
                continue
            x, y = X(p["capex"]), Y(p["npv"])
            if p["preset"] == "A":
                continue
            sp = SP_GREY
            if p["npv"] >= 0 and blue > 0:
                layer.alpha_composite(faded(SP_GREY, a * (1 - blue)), (int(x - SP_GREY.width / 2), int(y - SP_GREY.height / 2)))
                sp, a = SP_BLUE, a * blue
            layer.alpha_composite(faded(sp, a), (int(x - sp.width / 2), int(y - sp.height / 2)))
        ax, ay = X(A["capex"]), Y(A["npv"])
        aa = ease((t - 1.45) / 0.18)
        hot = ease((t - 4.9) / 0.4)
        if hot > 0:
            pulse = (t - 4.9) % 1.1 / 1.1
            r = 22 + 46 * pulse
            ld.ellipse((ax - r, ay - r, ax + r, ay + r), outline=rgb(ORANGE) + (int(230 * (1 - pulse) * hot),), width=4)
            layer.alpha_composite(faded(SP_A, hot), (int(ax - SP_A.width / 2), int(ay - SP_A.height / 2)))
            layer.alpha_composite(faded(LBL_A, hot), (int(ax + 34), int(ay - 86)))
        if hot < 1:
            layer.alpha_composite(faded(SP_BLUE if blue > 0 else SP_GREY, aa * (1 - hot)), (int(ax - SP_BLUE.width / 2), int(ay - SP_BLUE.height / 2)))
        f.alpha_composite(faded(layer, dots_out))

    # ---- page 1
    o = window(t, 6.7, 9.5)
    if o > 0:
        put(f, T5, (M, 190), o, rise=24 * (1 - ease((t - 6.7) / 0.5)))
        put(f, T5S, (M, 392), window(t, 7.1, 9.5))
        k = ease((t - 6.8) / 2.7)
        put(f, page_view(PAGE1, (22, 142, 760), (640, 142, 760), k), CARD[:2], o, rise=40 * (1 - ease((t - 6.7) / 0.6)))

    # ---- page 2
    o = window(t, 9.5, 12.3)
    if o > 0:
        put(f, T6, (M, 190), o, rise=24 * (1 - ease((t - 9.5) / 0.5)))
        put(f, T6S, (M, 392), window(t, 9.9, 12.3))
        k = ease((t - 10.0) / 1.9)
        put(f, page_view(PAGE2, (22, 142, 760), (22, 462, 900), k), CARD[:2], o, rise=40 * (1 - ease((t - 9.5) / 0.6)))
        put(f, CHIP, ((W - CHIP.width) // 2, 1214), window(t, 10.4, 12.3), rise=20 * (1 - ease((t - 10.4) / 0.5)))

    # ---- the end card
    o = ease((t - 12.4) / 0.5)
    if o > 0:
        def mid(img, y, at, op=None):
            put(f, img, ((W - img.width) // 2, y), o if op is None else op, rise=26 * (1 - ease((t - at) / 0.5)))
        mid(LOGO_L, 236, 12.4)
        mid(E_TITLE, 372, 12.5, ease((t - 12.5) / 0.5))
        mid(E_SUB, 532, 12.8, ease((t - 12.8) / 0.5))
        mid(CHIP, 716, 13.2, ease((t - 13.2) / 0.5))
        mid(E_CTA, 880, 13.7, ease((t - 13.7) / 0.5))
        mid(E_LINK, 968, 14.0, ease((t - 14.0) / 0.5))
        mid(E_NAME, 1196, 14.3, ease((t - 14.3) / 0.5))
    return f.convert("RGB")


def ffmpeg_exe():
    if os.environ.get("FFMPEG_PATH") and Path(os.environ["FFMPEG_PATH"]).exists():
        return os.environ["FFMPEG_PATH"]
    for exe in (["py", "-3.14"], ["python3"], ["python"], ["py"]):
        try:
            r = subprocess.run(exe + ["-c", "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"], capture_output=True, text=True, timeout=60)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip()
        except OSError:
            pass
    return "ffmpeg"


OUT.mkdir(parents=True, exist_ok=True)
if "--still" in sys.argv:
    for ts in sys.argv[sys.argv.index("--still") + 1].split(","):
        frame_at(float(ts)).save(OUT / f"still-{ts}.png")
        print(f"still-{ts}.png written")
    sys.exit(0)

mp4 = OUT / "room-to-invest-linkedin.mp4"
enc = subprocess.Popen([ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", "-movflags", "+faststart", str(mp4)], stdin=subprocess.PIPE)
n = int(DUR * FPS)
for i in range(n):
    enc.stdin.write(frame_at(i / FPS).tobytes())
enc.stdin.close()
enc.wait()
frame_at(5.8).save(OUT / "poster.png")
print(f"{mp4.name}: {n} frames, {DUR:.0f} s, {mp4.stat().st_size // 1024} kB; poster.png")
