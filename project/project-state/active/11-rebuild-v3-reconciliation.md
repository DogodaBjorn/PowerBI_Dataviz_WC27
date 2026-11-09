# 11 - Rebuild-pakket 09 + 10 op de v3-build: afstemming en besluiten

**Datum:** 2026-11-09 · **Gevraagd door:** Bjorn ("I have added two commits to the Dataviz WC 27 repository both consisting of rebuild instructions. One is data and content related one is design related. I want both implemented in the Goodnight Inn report. Then finally I want a double triple check on accessibility alt text etc.") · **Branch:** `rebuild-09-10` (afgetakt van `upgrade-opzet-v3`, met `origin/design-rebuild` erin gemerged; lokale commits, geen push zonder Bjorns ja).

## 1. Waarom dit document

Plan 09 (`09-research-based-rebuild.md`, inhoud) en plan 10 (`10-design-rebuild.md`, vorm) zijn geschreven tegen `main`. De echte build staat op `upgrade-opzet-v3` (tien commits verder, niet in `main`): review-v2-fixes (K1, vaste A/B/C), verbeterplan ronde 3 (V1-V5, 11 pt-vloer) en het meubilair als visuals. Daardoor bestaan meerdere doelen uit de plannen niet meer:

- `hero_brand_compare` en `c_compare_sub` zijn weg: P1 is nu de KPI-band (vier cellen) plus F1-F4. De KPI_ROWS-tabel en de `KPI Text *`/`Trend Title *`-measures staan niet meer op het canvas (BUILD_LOG).
- De koppen zijn measures (`Headline P1/P2 (text)`), geen statische deurhanger-zinnen; die staan nu in de pay-off (`PAYOFF`) naast het logo.
- Kaarten en logo zijn visuals (`card_frames()`, `brand_row()`), geen achtergrond-PNG: een pagina-achtergrond met Fit verschoof op 7 november toen Desktop het canvas niet-uniform schaalde (BUILD_LOG:112). Plan 10 D2 tekent zone en schaduw in die achtergrond-PNG.
- Regelnummers zijn verschoven (sketch_model.py +17 tot +460, opzet_report.py +10 tot +190).

Dit document legt per punt vast hoe de **bedoeling** van 09 en 10 op de v3-architectuur landt. De inhoud van 09 en 10 verandert niet; waar dit document afwijkt, gaat dit document voor.

## 2. Besluiten van Bjorn (9 november, in de sessie)

| Onderwerp | Besluit |
|---|---|
| 138 ongecommitte Desktop-bestanden op v3 (schema 2.11 naar 2.14, herordening, cultures-bestand) | Weggegooid: geen inhoudelijke wijziging, de generators schrijven alles opnieuw. |
| Night header | **D7 night-glow, met waiver**: verloop Night naar navy in de zone, Coffee Blue gloed, zwaardere schaduw onder de hoofdkaart, blauwe gloed onder de aanbeveling, plus de D2b-hanger. |
| Lettervloer | **12 pt / 16 px** (kit 3.1 `typography.floor`). Past het P2-paneel niet op 1366, dan gaat detail naar de tooltip, nooit kleinere letters. Vervangt de 11 pt van 08 R4. |
| R1 (prijskracht) | KPI-cel 4 wordt de **RevPAR-index** in plaats van NPS (R1 en R2 in één); alleen als de haalbaarheidscheck slaagt. Het optionele vierde trendslot vervalt: P1 heeft geen ruimte. |
| Koppen (D5) | De v3-koppen (measures) blijven. D5 geldt alleen voor de resterende deurhanger-copy en kleurnamen. |
| Brand row | Vignettes (hanger met gezicht) en pay-off-regels eruit; in het pay-off-slot de eyebrow "01  THE BRAND REVIEW" / "02  THE INVESTMENT STRATEGY". |
| Git | Branch `rebuild-09-10`, lokale commits per stap, geen push. |

**WAIVER D7, 2026-11-09, Bjorn:** voor de header-zone vervalt design hard rule 6 voor gradients (verloop Night naar navy, Coffee Blue gloed); lock 9 (één kaartstijl per pagina) wordt gebogen voor de zwaardere schaduw onder de hoofdkaart en de gloed onder de aanbeveling. Reden: Bjorn koos de night-glow-variant ("more oompf", plan 10 paragraaf "Hoe we hier kwamen"). De D2b-waiver (de vervaagde hanger) blijft van kracht.

## 3. Afstemming per punt

### Deel A: plan 09

| Punt | Plan (tegen `main`) | Op v3 |
|---|---|---|
| R1 | Twee indexrijen in `KPI_ROWS` (hero-tabel), optioneel vierde trendslot | KPI-cel 4 `kpi_nps` wordt `kpi_revpar`: waarde RevPAR-index 2025 (2021 = 100), context "rang van 4 · ADR-index N". Measures `RevPAR Index GI`, `KPI RevPAR Index GI (text)`, `KPI RevPAR Index Context (text)`. Eerst de haalbaarheidscheck `project/analysis/42_price_index.py`; meet 2021 = 100 vooral het COVID-herstel, dan stop en beide bases aan Bjorn voorleggen. |
| R2 | Label "F3 · Recommend us?" en `Trend Title NPS` herformuleren | NPS verlaat de KPI-band (via R1). F3 houdt NPS als operationeel signaal (renovatieleeftijd). Keller-ladder-commentaar bij `KPI_ROWS` meebewegen. Methodologiezin rijdt mee met R4. |
| R3 | Nieuwe `Plan Margin (text)` op een leeg slot | Geen vrij slot; `Rec Held`/`Not Funded` dragen het argument al. De marginale toets wordt een bijzin in **`Rec Held (text)`**: het beste pakket dat A plus minstens één initiatief bevat, de extra capex en het NPV-verschil in het gekozen scenario. Alleen als die NPV lager is dan A's; anders leeg (geen valse claim in High). |
| R4 | Zin in `FOOTER` | Zin in `FOOTER` (P1) en in `Footer P2 (text)`. Geen repo-pad op het canvas. |
| R5 | Zin in `c_compare_sub` | Zin in `F2 Note (text)`, gelabeld "Our reading:" (INSCHATTING), met aantal hotels en rang uit het model. |

### Deel B: plan 10

| Punt | Op v3 |
|---|---|
| D1 | Zoals gepland (kit, theme, constanten). Fonts als de stack die Desktop zelf schrijft: `'Segoe UI', wf_segoe-ui_normal, helvetica, arial, sans-serif` en `'Segoe UI Semibold', wf_segoe-ui_semibold, …`; `wf_segoe-ui_*` zijn de webfonts van de service (antwoord op de Mac-vraag, te bevestigen in de Publish-to-Web-test). |
| D2 + D7 | Geen pagina-achtergrond: `opzet_backgrounds.mjs` tekent per pagina het volledige night-glow-canvas (SVG-port van `brand_canvas_v3.py`) en het komt als **decoratieve image-visual `z_canvas`** op z 0, zodat het met de visuals meeschaalt. Kaartschaduw via de per-visual `dropShadow` van de kaartframes (geen theme-schaduw). **Horizon = bovenkant eerste kaartrij + 64 = y 248**: de +128 uit plan 10 (y 312) is gemeten op de `main`-layout; op v3 eindigt de P1-KPI-kaart op y 304 en zou hij los in de zone zweven. |
| D2b | `hangerLayer()` in hetzelfde canvas, binnen de zone. |
| D3 | Zonetekst licht: masthead en subtitel ZONE_MUTED, kop ZONE_TEXT, eyebrow ZONE_EYEBROW. |
| D4 | Kaartframes zonder haarlijn, met schaduw. Binnentegel `z_tile_rec` (de aanbeveling) krijgt onder de D7-waiver de blauwe gloed; de bookmarkcode verbergt `z_tile_*` al in de planstaat. |
| D5 | Kleurnamen uit copy, alt-teksten en docstrings; pay-off vervangen door de eyebrow. |
| D6 | Marks ACCENT_MARK, tekst ACCENT, signalen SIGNAL_MARK, zusters en context SLATE (`#8E897D`). `Package Point Color` loopt op v3 via `Package[Preset]`: A ACCENT_MARK, B en C INK, de wolk SLATE (was LILAC, 2,10:1). Chips: de gezichtsloze hanger. |

## 4. Toegankelijkheid (de drievoudige controle)

Basislijn (verkenning 9 november): alle visuals behalve acht tekstvakken hadden alt-tekst, maar alles statisch; 33 alt-teksten waren alleen een measure-naam; drie noemden kleuren die na de merkwissel fout zijn; zeven bevatten hard getypte getallen; decoratief meubilair zat in de tab-volgorde en de brand row werd na de footer voorgelezen; kickers (13 px) en mastheads (14 px) lagen onder de vloer; reekslabels in Warm Grey haalden 3,5:1 (tekst vraagt 4,5:1); de lila wolk 2,10:1; de luchthavenbalken alleen in kleur.

Aanpak:

1. **Machinecontrole**: nieuw `project/tools/a11y_check.py` (stdlib) over de gegenereerde PBIR, het canvas en de zone-samples.
2. **Gerenderde controle**: Desktop via de WebView2-DevTools-poort: screenshots op 1920 en 1366, de accessibility tree (wat een schermlezer krijgt) en een gescripte toetsenbordwandeling.
3. **Onafhankelijke review**: een verse agent zonder mijn bevindingen, met de checklist en de renders.

Onderzoek vooraf (research-first):

- `general.altText` accepteert elke expressie (schema visualConfiguration 2.6.0: `altText: {}`), dus een measure-binding valideert.
- Een PBIR-vlag "hide from tab order" bestaat niet in `VisualContainerPosition`; Desktop schrijft decoratieve visuals met een **negatieve `tabOrder`** (-1, -1000; gezien in Desktop-bestanden van hp-world-champs). Dat gebruiken we; de toetsenbordwandeling bevestigt het.

Uitkomst: zie paragraaf 5 (na de build).

## 5. Uitkomst

(volgt na de build)
