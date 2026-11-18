"""Deterministic taste-lint over PBIR JSON — mechanizes the report craft floor.

Usage:
    python scripts/pbir_detect.py                     # scan project/pbip
    python scripts/pbir_detect.py path/to/x.Report    # one report
    python scripts/pbir_detect.py --waivers project/project-state/pbir-detect-waivers.yaml
    python scripts/pbir_detect.py --list-rules

Checks the enforceable slice of `design/report-craft-floor.md` and the
consistency locks (rules 7-9 in `.claude/rules/design-hard-rules.md`)
directly against the PBIR source. Rule logic adapted to Power BI from
impeccable's antipattern detector (Apache-2.0) — see CREDITS.md.

Rules:
    accent-lock           second accent hue introduced outside the theme (lock 7)
    radius-system         more distinct corner radii than the radius system (lock 8)
    grid-8px              visual x/y/width/height off the 8px grid (craft floor)
    ai-dash-emoji         em/en-dash or emoji in visible titles/textboxes (AI tell)
    section-kicker-repeat identical uppercase textbox repeated across pages (AI tell)
    theme-color-drift     literal hexes in visuals that the theme does not define
    flat-type-hierarchy   theme textClasses sizes too uniform (no hierarchy)
    text-fill-contrast    literal text-on-fill pair below WCAG AA

Waivers: `project/project-state/pbir-detect-waivers.yaml` (auto-resolved by
walking up from the report; override with --waivers). miniyaml subset — a
`waivers:` mapping of named entries, each with `rule`, `path` (glob matched
against the finding path shown in the output), a non-empty `reason`, and
`date`. A waiver without a reason is invalid and waives nothing. Unwaived
findings exit 1; the s6/s7 gates treat that as a failure, while the
PostToolUse hook runs this warn-only (see .claude/hooks/posttool_validate.py).

Example waiver file:

    waivers:
      free-form-layout:
        rule: grid-8px
        path: "pages/*"
        reason: "Illustrated free-form layout per approved design handoff"
        date: 2026-08-04
"""

import argparse
import fnmatch
import json
import os
import re
import sys
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import miniyaml

try:  # reuse the house WCAG math; fall back if run standalone
    from check_contrast import contrast_ratio
except ImportError:  # pragma: no cover

    def _lum(hexv):
        hexv = hexv.lstrip("#")
        rgb = tuple(int(hexv[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
        lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
        return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]

    def contrast_ratio(fg, bg):
        l1, l2 = _lum(fg), _lum(bg)
        return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")
# Emoji + pictograph blocks; deliberately excludes arrows and punctuation.
EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿⭐⭕️✅❌❗❤]"
)
DASH_RE = re.compile("[–—]")

GRID = 8
GRID_TOLERANCE = 0.5  # float jitter, not a licence to drift
MAX_RADII = 2  # one radius token, or a documented 2-step scale (lock 8)
ACCENT_CHROMA = 40  # channel spread below this reads as neutral, not accent
ACCENT_HUE_TOLERANCE = 24  # degrees; nearer hues are shades of one accent
FLAT_TYPE_RATIO = 2.0  # max/min textClasses size below this is flat (impeccable)
KICKER_MIN_PAGES = 3  # same uppercase textbox on this many pages = scaffolding
EXAMPLES = 3  # locations quoted per aggregated finding

RULES = {
    "accent-lock": "second accent hue outside the theme (consistency lock 7)",
    "radius-system": "distinct corner radii exceed the radius system (lock 8)",
    "grid-8px": "visual position/size off the 8px grid (craft floor)",
    "ai-dash-emoji": "em/en-dash or emoji in visible report text (AI tell)",
    "section-kicker-repeat": "identical uppercase textbox across pages (AI tell)",
    "theme-color-drift": "literal hex not defined by the report theme",
    "flat-type-hierarchy": "theme textClasses sizes too uniform",
    "text-fill-contrast": "literal text-on-fill pair below WCAG AA",
}


class Finding:
    def __init__(self, rule, path, location, message):
        self.rule = rule
        self.path = path  # forward-slash, definition-relative; waiver glob target
        self.location = location  # human "page/visual" style anchor
        self.message = message
        self.waived_by = None


# ── PBIR literal plumbing ───────────────────────────────────────────────────


def load_json(path):
    with open(path, encoding="utf-8-sig") as handle:
        return json.load(handle)


def literal(prop):
    """Unwrap {"expr": {"Literal": {"Value": "..."}}} (or a bare scalar)."""
    node = prop
    for key in ("expr", "Literal", "Value"):
        if isinstance(node, dict) and key in node:
            node = node[key]
        elif key == "expr" and isinstance(node, dict):
            node = node.get("Literal", node)
        else:
            break
    if isinstance(node, (str, bool, int, float)):
        return node
    return None


def literal_str(prop):
    value = literal(prop)
    if isinstance(value, str):
        value = value.strip()
        if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
            value = value[1:-1].replace("''", "'")
        return value
    return None


def literal_num(prop):
    value = literal(prop)
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = re.match(r"^'?(-?\d+(?:\.\d+)?)[DL]?'?$", value.strip())
        if match:
            return float(match.group(1))
    return None


def solid_hex(prop):
    """Literal hex from a color property (solid wrapper or direct literal)."""
    node = prop
    if isinstance(node, dict) and "solid" in node:
        node = node["solid"].get("color")
    value = literal_str(node) if node is not None else None
    if value is None and isinstance(node, str):
        value = node
    if isinstance(value, str) and HEX_RE.fullmatch(value.strip()):
        return value.strip().upper()
    return None


def bag_visible(props):
    """A properties bag hides its colors via show:false or transparency>=100."""
    show = literal(props.get("show")) if "show" in props else None
    if show in (False, "false"):
        return False
    transparency = literal_num(props.get("transparency"))
    if transparency is not None and transparency >= 100:
        return False
    return True


def hue_of(hexv):
    r, g, b = (int(hexv[i : i + 2], 16) for i in (1, 3, 5))
    mx, mn = max(r, g, b), min(r, g, b)
    if mx == mn:
        return 0
    d = mx - mn
    if mx == r:
        h = ((g - b) / d) % 6
    elif mx == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return round(h * 60) % 360


def chroma_of(hexv):
    r, g, b = (int(hexv[i : i + 2], 16) for i in (1, 3, 5))
    return max(r, g, b) - min(r, g, b)


def hue_distance(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


# ── Per-visual scan ─────────────────────────────────────────────────────────


class VisualScan:
    def __init__(self, path, page, name):
        self.path = path
        self.page = page
        self.name = name
        self.location = f"{page}/{name}"
        self.visual_type = None
        self.position = {}
        self.colors = []  # (hex, in_spec) — visible literals only
        self.radii = []  # numeric radius literals
        self.texts = []  # visible strings (titles, textbox runs, button labels)
        self.textbox_texts = []  # textbox strings only (kicker rule)
        self.pairs = []  # (fg_hex, bg_hex, font_size_or_None, context)


FG_KEYS = ("fontColor", "labelColor", "titleColor")
BG_KEYS = ("fillColor", "backColor", "background")


def scan_bag(props, scan, in_spec):
    """Collect colors, radii, texts, and contrast pairs from one properties bag."""
    if not bag_visible(props):
        return
    fg = bg = None
    font_size = literal_num(props.get("fontSize"))
    for key, prop in props.items():
        if "radius" in key.lower():
            value = literal_num(prop)
            if value is not None:
                scan.radii.append(value)
        hexv = solid_hex(prop)
        if hexv:
            scan.colors.append((hexv, in_spec))
            if key in FG_KEYS:
                fg = hexv
            elif key in BG_KEYS:
                bg = hexv
        if key == "text":
            value = literal_str(prop)
            if value:
                scan.texts.append(value)
        if key == "jsonSpec":
            # Deneb/Vega specs are opaque strings: harvest raw hexes only.
            value = literal_str(prop) or ""
            for spec_hex in HEX_RE.findall(value):
                scan.colors.append((spec_hex.upper(), True))
    if fg and bg:
        scan.pairs.append((fg, bg, font_size, "same-object fg/bg"))
    # paragraphs (textboxes) carry raw JSON, not expr-wrapped literals
    paragraphs = props.get("paragraphs")
    if isinstance(paragraphs, list):
        for para in paragraphs:
            for run in (para or {}).get("textRuns", []):
                value = run.get("value")
                if isinstance(value, str) and value.strip():
                    scan.texts.append(value)
                    scan.textbox_texts.append(value)


def walk(node, scan, in_spec=False):
    if isinstance(node, dict):
        props = node.get("properties")
        if isinstance(props, dict):
            scan_bag(props, scan, in_spec)
        for key, value in node.items():
            if key == "properties":
                continue
            walk(value, scan, in_spec or key == "jsonSpec")
    elif isinstance(node, list):
        for item in node:
            walk(item, scan, in_spec)
    elif isinstance(node, str) and in_spec:
        # Deneb/Vega specs are opaque strings: harvest raw hexes only.
        for hexv in HEX_RE.findall(node):
            scan.colors.append((hexv.upper(), True))


def scan_visual(path, page, name):
    data = load_json(path)
    scan = VisualScan(path, page, name)
    scan.position = data.get("position") or {}
    scan.visual_type = (data.get("visual") or {}).get("visualType")
    walk(data, scan)
    return scan


# ── Report resolution ───────────────────────────────────────────────────────


def find_reports(path):
    path = os.path.abspath(path)
    if os.path.isfile(os.path.join(path, "definition", "report.json")):
        return [path]
    if os.path.basename(path) == "definition":
        return [os.path.dirname(path)]
    reports = []
    for root, dirs, _files in os.walk(path):
        for d in sorted(dirs):
            if d.endswith(".Report"):
                candidate = os.path.join(root, d)
                if os.path.isfile(os.path.join(candidate, "definition", "report.json")):
                    reports.append(candidate)
        dirs[:] = [d for d in dirs if not d.endswith((".Report", ".SemanticModel"))]
    return reports


def resolve_theme(report_dir):
    """Custom theme dict + display path, from report.json's themeCollection."""
    try:
        report = load_json(os.path.join(report_dir, "definition", "report.json"))
    except (OSError, json.JSONDecodeError):
        return None, None
    custom = (report.get("themeCollection") or {}).get("customTheme") or {}
    name = custom.get("name")
    if not name:
        return None, None
    if not name.endswith(".json"):
        name += ".json"
    theme_path = os.path.join(
        report_dir, "StaticResources", custom.get("type", "RegisteredResources"), name
    )
    try:
        return load_json(theme_path), f"theme/{name}"
    except (OSError, json.JSONDecodeError):
        return None, None


def theme_hexes(theme):
    return {h.upper() for h in HEX_RE.findall(json.dumps(theme))}


def theme_semantic_hexes(theme):
    """State colors that encode meaning, exempt from the accent lock."""
    hexes = set()
    for key in ("good", "bad", "neutral", "null"):
        value = theme.get(key)
        if isinstance(value, str) and HEX_RE.fullmatch(value):
            hexes.add(value.upper())
    return hexes


# ── Rules ───────────────────────────────────────────────────────────────────


def rule_grid(scans, findings):
    by_page = {}
    for scan in scans:
        by_page.setdefault(scan.page, []).append(scan)
    for page, page_scans in sorted(by_page.items()):
        off = []
        for scan in page_scans:
            bad = {
                k: scan.position[k]
                for k in ("x", "y", "width", "height")
                if isinstance(scan.position.get(k), (int, float))
                and abs(scan.position[k] - GRID * round(scan.position[k] / GRID))
                > GRID_TOLERANCE
            }
            if bad:
                off.append((scan.name, bad))
        if off:
            examples = ", ".join(
                f"{name} ({', '.join(f'{k}={v:g}' for k, v in bad.items())})"
                for name, bad in off[:EXAMPLES]
            )
            findings.append(
                Finding(
                    "grid-8px",
                    f"pages/{page}",
                    page,
                    f"{len(off)} of {len(page_scans)} visuals off the {GRID}px grid, "
                    f"e.g. {examples}",
                )
            )


def rule_radius(scans, findings):
    uses = Counter()
    where = {}
    for scan in scans:
        for value in scan.radii:
            uses[value] += 1
            where.setdefault(value, scan.location)
    # The theme's visualStyles radius is the system's base token.
    if len(uses) > MAX_RADII:
        listing = ", ".join(
            f"{v:g}px x{c} (e.g. {where[v]})" for v, c in uses.most_common()
        )
        findings.append(
            Finding(
                "radius-system",
                "report",
                "report",
                f"{len(uses)} distinct corner radii — the lock allows a single "
                f"token or a documented 2-step scale: {listing}",
            )
        )


def rule_dash_emoji(scans, findings):
    for scan in scans:
        for text in scan.texts:
            tells = []
            if DASH_RE.search(text):
                tells.append("em/en-dash")
            if EMOJI_RE.search(text):
                tells.append("emoji")
            if tells:
                rel = f"pages/{scan.page}/visuals/{scan.name}/visual.json"
                snippet = text if len(text) <= 60 else text[:57] + "..."
                findings.append(
                    Finding(
                        "ai-dash-emoji",
                        rel,
                        scan.location,
                        f"{' + '.join(tells)} in visible text: \"{snippet}\"",
                    )
                )


def rule_kickers(scans, findings):
    pages_by_text = {}
    for scan in scans:
        for text in scan.textbox_texts:
            norm = " ".join(text.split())
            if len(norm) < 3 or not re.search(r"[A-Z]", norm) or re.search(r"[a-z]", norm):
                continue
            pages_by_text.setdefault(norm, set()).add(scan.page)
    for norm, pages in sorted(pages_by_text.items()):
        if len(pages) >= KICKER_MIN_PAGES:
            findings.append(
                Finding(
                    "section-kicker-repeat",
                    "report",
                    "report",
                    f'uppercase textbox "{norm}" repeats on {len(pages)} pages '
                    f"({', '.join(sorted(pages))}) — section-kicker scaffolding",
                )
            )


def rule_theme_drift(scans, theme_set, findings):
    for scan in scans:
        drift = Counter()
        spec_hexes = set()
        for hexv, in_spec in scan.colors:
            if hexv not in theme_set:
                drift[hexv] += 1
                if in_spec:
                    spec_hexes.add(hexv)
        if drift:
            rel = f"pages/{scan.page}/visuals/{scan.name}/visual.json"
            listing = ", ".join(sorted(drift))
            note = " (inside Deneb jsonSpec)" if spec_hexes == set(drift) else ""
            findings.append(
                Finding(
                    "theme-color-drift",
                    rel,
                    scan.location,
                    f"{len(drift)} literal hex(es) not in the theme{note}: {listing}",
                )
            )


def rule_accent(scans, theme, theme_set, findings):
    semantic = theme_semantic_hexes(theme)
    accent = (theme.get("dataColors") or [None])[0]
    accent_hue = hue_of(accent.upper()) if accent else None
    candidates = {}  # hex -> first location; jsonSpec colors are data-art, not chrome
    for scan in scans:
        for hexv, in_spec in scan.colors:
            if in_spec or hexv in theme_set or hexv in semantic:
                continue
            if chroma_of(hexv) >= ACCENT_CHROMA:
                candidates.setdefault(hexv, scan.location)
    # Cluster by hue; shades of the theme accent are drift, not a second accent.
    clusters = []
    for hexv in sorted(candidates):
        hue = hue_of(hexv)
        if accent_hue is not None and hue_distance(hue, accent_hue) <= ACCENT_HUE_TOLERANCE:
            continue
        for cluster in clusters:
            if hue_distance(hue, cluster[0]) <= ACCENT_HUE_TOLERANCE:
                cluster[1].append(hexv)
                break
        else:
            clusters.append((hue, [hexv]))
    for hue, hexes in clusters:
        examples = ", ".join(f"{h} (e.g. {candidates[h]})" for h in hexes[:EXAMPLES])
        findings.append(
            Finding(
                "accent-lock",
                "report",
                "report",
                f"accent hue ~{hue} deg not in the theme — one accent per report "
                f"(lock 7): {examples}",
            )
        )


def rule_flat_type(theme, theme_location, findings):
    classes = theme.get("textClasses") or {}
    sizes = sorted(
        {c.get("fontSize") for c in classes.values() if isinstance(c.get("fontSize"), (int, float))}
    )
    if len(sizes) >= 3 and sizes[-1] / sizes[0] < FLAT_TYPE_RATIO:
        findings.append(
            Finding(
                "flat-type-hierarchy",
                theme_location,
                "theme",
                f"textClasses sizes {', '.join(f'{s:g}pt' for s in sizes)} span only "
                f"{sizes[-1] / sizes[0]:.1f}:1 — aim for >= {FLAT_TYPE_RATIO}:1 "
                f"between smallest and largest",
            )
        )


def rule_contrast(scans, findings):
    for scan in scans:
        for fg, bg, font_size, context in scan.pairs:
            if fg == bg:
                continue  # decorative same-on-same is its own problem, not contrast
            threshold = 3.0 if (font_size or 0) >= 18 else 4.5
            ratio = contrast_ratio(fg, bg)
            if ratio < threshold:
                rel = f"pages/{scan.page}/visuals/{scan.name}/visual.json"
                findings.append(
                    Finding(
                        "text-fill-contrast",
                        rel,
                        scan.location,
                        f"{fg} on {bg}: {ratio:.2f}:1 (needs {threshold}:1, {context})",
                    )
                )


# ── Waivers ─────────────────────────────────────────────────────────────────


def find_waiver_file(report_dir):
    current = os.path.dirname(os.path.abspath(report_dir))
    for _ in range(6):
        candidate = os.path.join(current, "project-state", "pbir-detect-waivers.yaml")
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    return None


def load_waivers(path):
    """Return (valid_waivers, problems). Every waiver needs a non-empty reason."""
    waivers, problems = [], []
    try:
        doc = miniyaml.load(path)
    except (OSError, miniyaml.MiniYamlError) as exc:
        return [], [f"waiver file unreadable: {exc}"]
    entries = doc.get("waivers") or {}
    if not isinstance(entries, dict):
        return [], ["waivers: must be a mapping of named entries"]
    for name, entry in entries.items():
        if not isinstance(entry, dict):
            problems.append(f"waiver '{name}': not a mapping")
            continue
        rule, glob_ = entry.get("rule"), entry.get("path")
        reason = str(entry.get("reason") or "").strip()
        if rule not in RULES:
            problems.append(f"waiver '{name}': unknown rule {rule!r}")
            continue
        if not glob_:
            problems.append(f"waiver '{name}': missing path glob")
            continue
        if not reason:
            problems.append(f"waiver '{name}': missing reason — reasonless waivers waive nothing")
            continue
        waivers.append((name, rule, str(glob_), reason))
    return waivers, problems


def apply_waivers(findings, waivers):
    for finding in findings:
        for name, rule, glob_, reason in waivers:
            if finding.rule == rule and (
                fnmatch.fnmatch(finding.path, glob_)
                or fnmatch.fnmatch(finding.path + "/", glob_)
            ):
                finding.waived_by = f"{name}: {reason}"
                break


# ── Driver ──────────────────────────────────────────────────────────────────


def detect_report(report_dir):
    definition = os.path.join(report_dir, "definition")
    scans = []
    pages_dir = os.path.join(definition, "pages")
    if os.path.isdir(pages_dir):
        for page in sorted(os.listdir(pages_dir)):
            visuals_dir = os.path.join(pages_dir, page, "visuals")
            if not os.path.isdir(visuals_dir):
                continue
            for name in sorted(os.listdir(visuals_dir)):
                visual_path = os.path.join(visuals_dir, name, "visual.json")
                if os.path.isfile(visual_path):
                    scans.append(scan_visual(visual_path, page, name))
    findings = []
    theme, theme_location = resolve_theme(report_dir)
    rule_grid(scans, findings)
    rule_dash_emoji(scans, findings)
    rule_kickers(scans, findings)
    rule_contrast(scans, findings)
    if theme:
        theme_set = theme_hexes(theme)
        rule_radius(scans, findings)
        rule_theme_drift(scans, theme_set, findings)
        rule_accent(scans, theme, theme_set, findings)
        rule_flat_type(theme, theme_location, findings)
    else:
        print("  note: no custom theme resolved — theme rules skipped")
    return scans, findings


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Deterministic taste-lint over PBIR JSON (craft floor + consistency locks)."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=os.path.join("project", "pbip"),
        help="a .Report folder, its definition/ folder, or a tree containing .Report folders",
    )
    parser.add_argument("--waivers", help="waiver YAML (default: nearest project-state/pbir-detect-waivers.yaml)")
    parser.add_argument("--list-rules", action="store_true", help="print rule ids and exit")
    args = parser.parse_args(argv)

    if args.list_rules:
        for rule, blurb in RULES.items():
            print(f"{rule:22s} {blurb}")
        return 0

    reports = find_reports(args.path)
    if not reports:
        print(f"pbir_detect: no .Report definitions under {args.path}")
        return 0

    total = waived = 0
    for report_dir in reports:
        rel_report = os.path.basename(report_dir)
        print(f"pbir_detect: {rel_report}")
        scans, findings = detect_report(report_dir)

        waiver_path = args.waivers or find_waiver_file(report_dir)
        waivers, problems = load_waivers(waiver_path) if waiver_path else ([], [])
        for problem in problems:
            print(f"  WAIVER-INVALID  {problem}")
        apply_waivers(findings, waivers)

        for finding in sorted(findings, key=lambda f: (f.rule, f.path)):
            flag = "waived" if finding.waived_by else "FAIL  "
            print(f"  {flag}  [{finding.rule}] {finding.path} :: {finding.message}")
            if finding.waived_by:
                print(f"          waived by {finding.waived_by}")
        unwaived_here = sum(1 for f in findings if not f.waived_by)
        waived_here = len(findings) - unwaived_here
        print(
            f"  {len(scans)} visuals scanned, {len(findings)} finding(s): "
            f"{unwaived_here} unwaived, {waived_here} waived"
        )
        total += len(findings)
        waived += waived_here

    unwaived = total - waived
    print(
        f"pbir_detect: {total} finding(s) across {len(reports)} report(s) — "
        f"{unwaived} unwaived, {waived} waived -> {'FAIL' if unwaived else 'PASS'}"
    )
    return 1 if unwaived else 0


if __name__ == "__main__":
    sys.exit(main())
