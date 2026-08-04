# Power BI-safe font pairings

Mood-indexed pairing menu for brand kits — use with `bk-brand-kit` (no-brand
path step) to fill `typography.display` / `body` / `numeric`. Adapted from the
ui-ux-pro-max skill's typography.csv (74 web pairings, MIT); filtered to fonts
that ship with Windows/Office and render in Power BI without embedding.
`~` = closest PBI-safe metric twin of a web-only font — design for the twin,
it is what readers actually see. Office-only fonts (Century Gothic, Bodoni MT,
Garamond) need Office on reader machines; when in doubt, fall back to Segoe UI.

| Mood keywords | Display | Body | Numeric | From (web pairing) |
|---|---|---|---|---|
| **editorial**, elegant, luxury | ~Georgia | ~Segoe UI | Segoe UI | Playfair Display + Inter |
| editorial, classic, literary | Garamond | ~Georgia | Georgia | Cormorant Garamond + Libre Baskerville |
| editorial, magazine, refined | ~Bodoni MT | ~Segoe UI | Segoe UI | Libre Bodoni + Public Sans |
| luxury, minimal, high-end | ~Bodoni MT | ~Century Gothic | Segoe UI | Bodoni Moda + Jost |
| **authoritative**, legal, formal | Garamond | ~Calibri | Calibri | EB Garamond + Lato |
| authoritative, corporate, accessible | ~Segoe UI Semibold | ~Segoe UI | Segoe UI | Lexend + Source Sans 3 |
| authoritative, financial, serious | ~Segoe UI | ~Segoe UI | Consolas | IBM Plex Sans |
| authoritative, academic, scholarly | ~Cambria | ~Verdana | Segoe UI | Crimson Pro + Atkinson Hyperlegible |
| **technical**, minimal, swiss | Segoe UI Semibold | Segoe UI | Segoe UI | Inter (single family) |
| technical, tech, innovative | ~Bahnschrift | ~Segoe UI | Consolas | Space Grotesk + DM Sans |
| technical, developer, precise | Consolas | ~Segoe UI | Consolas | JetBrains Mono + IBM Plex Sans |
| technical, dashboard, data-dense | ~Segoe UI Semibold | ~Segoe UI | Consolas | Fira Code + Fira Sans |
| modern, geometric, versatile | ~Century Gothic | ~Segoe UI | Segoe UI | Outfit + Work Sans |
| **warm**, approachable, professional | ~Century Gothic | ~Segoe UI | Segoe UI | Poppins + Open Sans |
| warm, calm, wellness, organic | ~Cambria | ~Corbel | Segoe UI | Lora + Raleway |
| warm, friendly, saas | ~Segoe UI | ~Segoe UI | Segoe UI | Plus Jakarta Sans (single family) |
| warm, humanist, readable | Trebuchet MS | ~Segoe UI | Segoe UI | Nunito + DM Sans (nearest safe) |
| **bold**, impactful, headline-led | ~Bahnschrift SemiCondensed | ~Segoe UI | Segoe UI | Bebas Neue + Source Sans 3 |
| bold, sports, athletic | ~Bahnschrift Condensed | ~Corbel | Segoe UI | Barlow Condensed + Barlow |
| bold, vintage, dramatic | ~Bodoni MT | ~Cambria | Georgia | Abril Fatface + Merriweather |
| **accessible**, hyperlegible, inclusive | ~Verdana | ~Verdana | Verdana | Atkinson Hyperlegible |
| accessible, news, informative | ~Cambria | ~Segoe UI | Segoe UI | Newsreader + Roboto |

Dropped without a twin (unfit for reports or no Windows metric neighbor):
script/handwritten (Caveat, Great Vibes, Kalam), pixel/retro (Press Start 2P,
VT323), sci-fi display (Orbitron, Syncopate), and the CJK/RTL Noto sets
(out of scope for this template's deliverables).

Rules: numeric column assumes tabular figures — Consolas only where the brand
allows a mono feel. Whatever you pick, write it into `brand.yaml` as
"<font>, <fallback>" and validate per the bk-brand-kit checklist.
