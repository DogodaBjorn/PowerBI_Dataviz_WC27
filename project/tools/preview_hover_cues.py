"""Preview of the hover-cue redesign of 12 Nov (night; doc 18), composited on the FinalV2 Desktop renders. NOT a Desktop
render: the header line and the badges are erased (the Night zone from backgrounds/canvas-night.jpg, cards in white), the pills
are drawn at their opzet-layout.json slots in Liberation Sans Bold (Arial metrics, the Mac fallback; Segoe UI Semibold is
narrower), and P2's slimmer source line is set in Liberation Sans. Needs Pillow (like a11y_check.py and brand_canvas_v3.py).
usage (repo root):  python project/tools/preview_hover_cues.py . project/deliverables/screenshots/Preview-hover-cues-2026-11-12"""
import json
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO, OUT = Path(sys.argv[1]), Path(sys.argv[2])
SHOTS = REPO / "project/deliverables/screenshots/ScreenshotsFinalV2"
BG = Image.open(REPO / "project/deliverables/backgrounds/canvas-night.jpg").convert("RGB")
L = json.loads((REPO / "project/design-prototypes/opzet-layout.json").read_text(encoding="utf-8"))
SLOT = {p["name"]: {v["name"]: v for v in p["visuals"]} for p in L["pages"]}
FD = "/usr/share/fonts/truetype/liberation/"
TINT, TANG, INK, BURNT, ICE, WHITE = (252, 230, 219), (224, 90, 34), (18, 35, 61), (166, 63, 14), (234, 242, 251), (255, 255, 255)


def font(px, bold=True):
    return ImageFont.truetype(FD + ("LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"), max(1, round(px)))


class Shot:
    def __init__(self, fn):
        self.im = Image.open(SHOTS / fn).convert("RGB")
        self.s = self.im.width / 1920
        self.bg = BG.resize(self.im.size, Image.LANCZOS)

    def R(self, x, y, w, h):
        s = self.s
        return (round(x * s), round(y * s), round((x + w) * s), round((y + h) * s))

    def erase_bg(self, x, y, w, h):
        box = self.R(x, y, w, h)
        self.im.paste(self.bg.crop(box), box[:2])

    def fill(self, x, y, w, h, c):
        ImageDraw.Draw(self.im).rectangle(self.R(x, y, w, h), fill=c)

    def pill(self, x, y, w, label=None, code=None):
        """The pill at 4x, downsampled: tint, Tangerine disc, white i, label in Night, code in Burnt Tangerine."""
        k = self.s * 4
        W, H = round(w * k), round(28 * k)
        t = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(t)
        d.rounded_rectangle((0, 0, W - 1, H - 1), radius=14 * k, fill=TINT)
        d.ellipse(((14 - 10) * k, (14 - 10) * k, (14 + 10) * k, (14 + 10) * k), fill=TANG)
        d.ellipse(((14 - 1.6) * k, (9.4 - 1.6) * k, (14 + 1.6) * k, (9.4 + 1.6) * k), fill=WHITE)
        d.rounded_rectangle((12.8 * k, 12.2 * k, 15.2 * k, 19.6 * k), radius=1.2 * k, fill=WHITE)
        if label:
            d.text((32 * k, 19.5 * k), label, font=font(16 * k), fill=INK, anchor="ls")
        if code:
            d.text(((w - 12) * k, 19.5 * k), code, font=font(16 * k), fill=BURNT, anchor="rs")
        t = t.resize((round(w * self.s), round(28 * self.s)), Image.LANCZOS)
        self.im.paste(t, (round(x * self.s), round(y * self.s)), t)

    def slot_pill(self, page, name, label=None, code=None):
        v = SLOT[page][name]
        self.pill(v["x"], v["y"], v["w"], label, code)

    def text(self, x, y_base, s, px=16, colour=INK, bold=False, width=None, lead=21):
        d = ImageDraw.Draw(self.im)
        f = font(px * self.s, bold)
        lines, cur = [], ""
        for word in s.split():
            trial = (cur + " " + word).strip()
            if width and f.getlength(trial) > width * self.s and cur:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        lines.append(cur)
        for i, ln in enumerate(lines):
            d.text((x * self.s, (y_base + i * lead) * self.s), ln, font=f, fill=colour, anchor="ls")

    def save(self, fn):
        self.im.save(OUT / fn)


P1, P2 = "p1-brand-review", "p2-investment-strategy"

# ---- P1
a = Shot("01_p1-brand-review.png")
a.erase_bg(1580, 12, 330, 40)                      # the header line: hint, dot, Definitions
a.fill(1850, 326, 28, 28, WHITE)                    # bdg_f3
a.fill(1850, 830, 28, 28, WHITE)                    # bdg_f4
a.slot_pill(P1, "tag_f3", "Hover a bar")
a.slot_pill(P1, "tag_f4", "Hover a hotel")
# the footer line moves 12 px down (y 1032 -> 1044), level with P2's
def move_text_down(shot, x0, y0, x1, y1, dy):
    """Lift the text pixels off a smooth ground (column-wise interpolated) and put them back dy canvas px lower."""
    s = shot.s
    X0, Y0, X1, Y1, D = round(x0 * s), round(y0 * s), round(x1 * s), round(y1 * s), round(dy * s)
    px = shot.im.load()
    def ground(x, y, ya, yb):
        ta, tb = px[x, ya], px[x, yb]
        f = (y - ya) / (yb - ya)
        return tuple(round(ta[i] + (tb[i] - ta[i]) * f) for i in range(3))
    glyph = {}
    for x in range(X0, X1):
        for y in range(Y0, Y1):
            g = ground(x, y, Y0 - 1, Y1)
            o = px[x, y]
            gl, ol = sum(g) / 3, sum(o) / 3
            al = max(0.0, min(1.0, (gl - ol) / max(1, gl - 85)))
            if al > 0.02:
                glyph[(x, y)] = al
    for x in range(X0, X1):                       # clear the old line
        for y in range(Y0, Y1):
            px[x, y] = ground(x, y, Y0 - 1, Y1)
    ink = (75, 84, 102)
    for (x, y), al in glyph.items():              # the line, dy lower
        b = px[x, y + D]
        px[x, y + D] = tuple(round(b[i] * (1 - al) + ink[i] * al) for i in range(3))


move_text_down(a, 32, 1036, 1300, 1056, 12)
a.slot_pill(P1, "chip_def", "Definitions")
a.save("preview_p1_brand-review.png")

FACTS = (("1", "The margin", 160), ("2", "The middleman", 300), ("3", "The fading welcome", 472), ("4", "Where we are full", 680))


def clear_band(shot, x0, y0, x1, y1):
    """Erase text on a smooth ground: each column interpolated between the rows just above and below."""
    s = shot.s
    X0, Y0, X1, Y1 = round(x0 * s), round(y0 * s), round(x1 * s), round(y1 * s)
    px = shot.im.load()
    for x in range(X0, X1):
        ta, tb = px[x, Y0 - 1], px[x, Y1]
        for y in range(Y0, Y1):
            f = (y - Y0 + 1) / (Y1 - Y0 + 1)
            px[x, y] = tuple(round(ta[i] + (tb[i] - ta[i]) * f) for i in range(3))


def p2_footer(shot):
    """P2's footer row: the slimmer source line, 'Revisit the facts' (one pill, four findings), Definitions."""
    clear_band(shot, 28, 1046, 1000, 1072)
    shot.text(32, 1064, "Source: Pillow & Key Group dataset. Parts are rounded to add up.", colour=(75, 84, 102))
    v = SLOT[P2]["z_pill_facts"]
    k = shot.s * 4
    X, Y, W = v["x"], v["y"], v["w"]
    t = Image.new("RGBA", (round(W * k), round(28 * k)), (0, 0, 0, 0))
    d = ImageDraw.Draw(t)
    d.rounded_rectangle((0, 0, W * k - 1, 28 * k - 1), radius=14 * k, fill=TINT)
    d.ellipse((4 * k, 4 * k, 24 * k, 24 * k), fill=TANG)
    d.ellipse(((14 - 1.6) * k, (9.4 - 1.6) * k, (14 + 1.6) * k, (9.4 + 1.6) * k), fill=WHITE)
    d.rounded_rectangle((12.8 * k, 12.2 * k, 15.2 * k, 19.6 * k), radius=1.2 * k, fill=WHITE)
    d.text((32 * k, 19.5 * k), "Revisit the facts", font=font(16 * k, bold=False), fill=(75, 84, 102), anchor="ls")
    for j, (code, name, x) in enumerate(FACTS):
        d.text((x * k, 19.5 * k), "F" + code, font=font(16 * k), fill=BURNT, anchor="ls")
        d.text(((x + 26) * k, 19.5 * k), name, font=font(16 * k), fill=INK, anchor="ls")
        if j < 3:
            cw = SLOT[P2]["chip_f" + code]["w"]
            cx = x + cw + 8
            d.ellipse(((cx - 1.75) * k, (14 - 1.75) * k, (cx + 1.75) * k, (14 + 1.75) * k), fill=(142, 137, 125))
    t = t.resize((round(W * shot.s), round(28 * shot.s)), Image.LANCZOS)
    shot.im.paste(t, (round(X * shot.s), round(Y * shot.s)), t)
    shot.slot_pill(P2, "chip_def2", "Definitions")


# ---- P2, rec
b = Shot("02_p2-investment-strategy_recommended-A.png")
b.erase_bg(1250, 12, 660, 40)                      # hint, 'Revisit the facts', F1-F4, Definitions
b.fill(1034, 186, 30, 28, WHITE)                    # bdg_scatter
b.fill(1834, 742, 28, 28, WHITE)                    # bdg_rec_cum
b.fill(650, 293, 194, 26, ICE)                      # 'Hover a dot for its moves.' leaves the guide
b.slot_pill(P2, "tag_scatter", "Hover a dot")
b.slot_pill(P2, "tag_rec_cum", "Hover a year")
p2_footer(b)
b.save("preview_p2_recommended-A.png")

# ---- P2, alts
c = Shot("03_p2-investment-strategy_considered-B-C.png")
c.erase_bg(1250, 12, 660, 40)
c.fill(714, 186, 28, 28, WHITE)                     # bdg_scatter_s
c.fill(1834, 678, 28, 28, WHITE)                    # bdg_cmp_alts
c.slot_pill(P2, "tag_scatter_s", "Hover a dot")
c.slot_pill(P2, "tag_cmp_alts", "Hover a year")
p2_footer(c)
c.save("preview_p2_considered-B-C.png")
print("written", OUT)
