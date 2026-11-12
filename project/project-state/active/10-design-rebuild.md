# 10 - Design rebuild: merkkit 3.1 "night header" op de opzet

**Datum:** 2026-11-09 · **Gevraagd door:** Bjorn (chat, 9 november 10:08: "I like the last two ones can you push a description and example of this including how to technically and push it to the data viz wc 27 repository under the name of Design rebuild. If possible look for the research based rebuild git commit and incorporate this into that one to make one rebuild package") · **Stage:** 0 (plan, geen build-wijziging).

**Rebuild-pakket.** Dit plan is deel B van één rebuild-pakket:

| Deel | Plan | Over | Raakt |
|---|---|---|---|
| A | `09-research-based-rebuild.md` (PR #10) | inhoud: KPI's, framing, copy (R1-R5) | `sketch_model.py`, `opzet_report.py` (copy) |
| B | dit document | vorm: merkkit, kleur, typografie, diepte (D1-D7, met D2b) | `project.yaml`, theme, `opzet_backgrounds.mjs`, `opzet_report.py`, `sketch_model.py` (kleurmeasures) |

Beide delen raken dezelfde generators, dus ze worden samen gebouwd: één rebuild van `sketch_model.py` en één van `opzet_backgrounds.mjs` + `opzet_report.py`, in de gezamenlijke volgorde van paragraaf 4. Dit plan verandert niets aan de inhoud van 09; waar de twee elkaar raken staat het in paragraaf 3.

**Hoe we hier kwamen (8-9 november, chat met Bjorn).**

1. Kit-optie 3 1.0: palet uit een reel die Bjorn deelde (Oat Cream `#E9E5D6`, Coffee Blue `#2589D8`, Tangerine `#FF783D`), in posterstijl.
2. 2.0: de deurhanger als mascotte ("Hank") met riso, papierkorrel en AI-illustraties. **Afgewezen** door Bjorn: "dit lijkt toch niet op een high end basis voor dashboard visual passend bij een zakelijk/business focused internationaal hotel merk en ook niet op iets voor een investor deck." Mascotte en illustraties zitten niet in dit pakket.
3. 3.0 boardroom: "hip, modern en zakelijk". Kleur met één betekenis, Segoe UI, gezichtsloze hanger, data als beeld.
4. 3.1 night header: Bjorn wilde meer "oompf" ("the background can be turned to live somehow adding some 3d or shadowing"). Drie dieptes gerenderd op P1 (lift, light, night); gekozen: **night**, op P1 en P2 ("I like the last two ones").

**Voorbeeld.** In `design/brand-kits/goodnight-inn-wakeup/comps/`:

| Bestand | Wat |
|---|---|
| `p1-brand-review-night.jpg`, `p2-investment-strategy-night.jpg` | **de spec** (D1-D6, met de vervaagde hanger uit D2b) |
| `p1-brand-review-night-glow.jpg`, `p2-investment-strategy-night-glow.jpg` | optionele variant, alleen met waiver (D7) |
| `p1-brand-review-flat.jpg`, `p2-investment-strategy-flat.jpg` | 3.0 zonder diepte, ter vergelijking |
| `*.html` | de bron-comps, gegenereerd door `project/tools/comps_v3.py` uit `project/design-prototypes/opzet-data.json` |
| `opzet-background-p1-night.png`, `opzet-background-p2-night.png` | de D2/D2b-achtergrond op de **echte** slotmap (`opzet-layout.json`), getest met de code uit D2 en D2b |

De comps tonen de look, niet de slotmap of de lettergroottes: ze gebruiken de 3.0-compositie (band met paginatabs, iets andere kaartindeling) en enkele labels van 11-13 px. Voor de build blijven `opzet-layout.json` (met de twee wijzigingen uit D2 en D3) en het R4-minimum uit plan 08 leidend.

**Geldende randvoorwaarden (ongewijzigd):**

- *Do-not-fabricate:* de cijfers in de comps komen uit de offline decode (`opzet-data.json`); niets landt op het canvas zonder heraflelding uit het model (stage 4/6).
- *Design hard rules* (`.claude/rules/design-hard-rules.md`). Regel 6 (geen gradients of decoratieve beelden): de zone is vlak Night, zonder gradient of gloed; voor de vervaagde hanger in de zone (D2b) geldt Bjorns waiver van 9 november. Schaduw-token "subtle only, ~10% opacity": de kaartschaduw is 10 %. Lock 7 (één accent): Coffee Blue; Deep Coffee is de tekstsnede van dezelfde tint. Lock 8 (radius): kaarten 12 px, chips en knoppen volrond, gedocumenteerd in de kit. Lock 9 (één kaartstijl per pagina): alle kaarten dezelfde schaduw, geen haarlijn.
- *Publish-to-Web:* alleen ingebouwde fonts, alleen ingebedde beelden. Segoe UI zit alleen op Windows: zie D1 en de open vragen.
- *Mutatieveiligheid:* alles via de generators; `project/pbip/` alleen via de pbir-operator; niets handmatig in Desktop behalve de bestaande VERIFY-fallbacks.
- *Accessibility:* contrast gemeten (D1-tabel, D3); een verdict nooit alleen in kleur.
- *Lettergrootte:* R4 uit plan 08: secundaire tekst minimaal circa 16 px op 1920 (12 pt). De kit (`typography.floor`) volgt dat.

---

## D1 - Merkkit wisselen: goodnight-inn-hanger naar goodnight-inn-wakeup 3.1

**Inhoudelijk.** Goodnight Inn is overal Coffee Blue; de drie zustermerken zijn altijd Warm Grey; Tangerine verschijnt alleen als signaal (een kostenpost, een risico, "last of 4", het Low-scenario). Night en Oat dragen de pagina. Typografie Segoe UI (Semibold voor koppen en cijfers). Logo: de gezichtsloze hanger met het woordmerk "goodnight inn." en een Tangerine punt.

**Data.** Geen.

**Technisch.**

- `project/project.yaml`: `brand_kit: goodnight-inn-wakeup` (commentaar met datum en verwijzing naar het addendum in `00-brand-decision.md`).
- `python project/tools/compile_theme.py` schrijft `project/deliverables/theme.json`. Getest op 9 november in een kopie van de repo: de kit compileert, `check_contrast.py --theme` geeft 8/8, `dropShadow` blijft `show: false` (zie D2). `check_contrast.py --kit` op de kit: 10/10.
- `project/tools/opzet_report.py` regel 38: `THEME_FILE = "goodnight-inn-wakeup.json"`.
- `project/tools/opzet_report.py` regel 44: `DISPLAY, BODY = "Segoe UI Semibold", "Segoe UI"`. De bestaande groottes blijven (headline 37 px mag naar 40 px), met het R4-minimum.
- Kleurconstanten in `opzet_report.py` regels 42-43 en `sketch_model.py` regel 561:

| Constante | Nu (hanger) | Wordt (3.1) | Kit-token | Rol |
|---|---|---|---|---|
| `CANVAS` | `#F5F3F0` | `#F3F1EA` | canvas | pagina, P2-binnentegels |
| `SURFACE` | `#FFFFFF` | `#FFFFFF` | surface | kaarten |
| `INK` | `#24192B` | `#12233D` | ink | tekst, totalen |
| `INK2` | `#5B5163` | `#4B5466` | ink_secondary | labels, assen |
| `HAIR` | `#E4DEE3` | `#E3DFD3` | hairline | rasterlijnen, binnentegels |
| `ACCENT_MARK` (nieuw) | - | `#2589D8` | accent_mark | GN-reeks, airport-balken, punten zonder refresh |
| `ACCENT` | `#B5175F` | `#1763A8` | accent | blauwe tekst, knopvulling met witte tekst |
| `GOOD` | `#1D5FA8` | `#1763A8` | good | ▲ |
| `BAD` | `#B45309` | `#A63F0E` | bad | ▼ |
| `SLATE` | `#82798A` | `#8E897D` | neutral_data | zusters, context |
| `PLUM` | `#3E2C55` | `#12233D` | ink | het pakket in focus (D6) |
| `LILAC` | `#B8B0BE` | `#C9C4B7` | neutral_light | gelabelde achtergrondmarks |
| `TINT` | `#F8D7E3` | `#EAF2FB` | accent_tint | GN-kolom, heat-stap 1 |
| `TINT2` | `#EE9DBA` | `#C5DCF3` | sequential[1] | heat-stap 2 |
| (nieuw) `SIGNAL_MARK` | - | `#E05A22` | signal_mark | Low-lijn (D6) |

  `ACCENT` splitst in twee constanten, omdat wit op Coffee Blue 3.7:1 haalt: genoeg voor een mark (3:1), te weinig voor 11 pt knoptekst (4.5:1). Wit op Deep Coffee is 6.2:1. Night op Ice 13.9:1, Night op heat-stap 2 11.2:1. Coffee Blue 3.7:1 en Warm Grey 3.5:1 op wit (mark-drempel 3:1).
- Logo: `design/brand-kits/goodnight-inn-wakeup/assets/gi-lockup-reversed.svg` (504 × 104; 194 × 40 px in het logoslot), zie D2.
- De slicer-`accent`-parameter in `pbir_lib.slicer` (regel 322) wordt in de functie niet gebruikt; de selectiekleur komt uit `theme.json`. Geen wijziging nodig in `sl_scenario` / `sl_package` behalve de constanten.

**Acceptatiecheck.** `theme.json` komt uit de nieuwe kit; `check_contrast.py --theme` slaagt; in de renders is GN op elke visual Coffee Blue en zijn de zusters grijs; geen raspberry meer op het canvas (`grep -i "B5175F"` in de generators leeg).

---

## D2 - De night header-zone en de kaartschaduw, in de achtergrondafbeelding

**Inhoudelijk.** Een vlakke Night-zone van de bovenrand tot de *horizon*: de bovenkant van de eerste kaartrij + 128 px. Logo, mastheadregel, headline en subtitel staan erin; de eerste kaartrij begint in de zone en hangt over de horizon. Dat overlappen geeft de diepte. Kaarten hebben geen haarlijn meer, maar één zachte schaduw.

**Data.** Geen.

**Technisch.** Alles in `project/tools/opzet_backgrounds.mjs`. De kaarten staan nu al als meubilair in de pagina-achtergrond (canvas-studio), met de visuals transparant erboven; daar komen de zone en de schaduw bij. Er komt **geen** shadow-property op een visual en `shape.shadow` in de kit blijft `none`: `compile_theme.py` regel 83 zet die waarde om in een standaardschaduw op elke visual, ook op tekstvakken en slicers.

- Tokens (regel 26): `const T = { canvas: '#F3F1EA', surface: '#FFFFFF', zone: '#12233D', shadow: '#12233D' };`
- Logo (regels 16-25): lees `design/brand-kits/goodnight-inn-wakeup/assets/gi-lockup-reversed.svg`; de asleep/awake-afleiding (`SLEEP_EYES` / `AWAKE_EYES` en de `throw`) vervalt, de 3.1-hanger heeft geen gezicht. Schaal: `p.logo.h / 104`.
- Zone, schaduwfilter en kaarten (vervangt de `cards`-regel en de SVG-template):

```js
const top = p.cards.filter(c => !c.state);
const horizon = Math.min(...top.map(c => c.y)) + 128;            // opzet: 184 + 128 = 312
const cards = top.map(c => `<rect x="${c.x}" y="${c.y}" width="${c.w}" height="${c.h}" rx="12" fill="${T.surface}" filter="url(#card-shadow)"/>`).join('\n');
const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
<defs><filter id="card-shadow" filterUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}">
<feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="${T.shadow}" flood-opacity="0.10"/></filter></defs>
<rect width="100%" height="100%" fill="${T.canvas}"/>
<rect id="zone" width="${W}" height="${horizon}" fill="${T.zone}"/>
${cards}
<g transform="translate(${p.logo.x} ${p.logo.y}) scale(${p.logo.h / 104})">${LOCKUP}</g>
</svg>`;
```

  (`W`/`H` = `layout.canvas.w`/`.h`.) Getest op 9 november met een kopie van het script op de echte slotmap: horizon 312 op beide pagina's; de resultaten staan als `comps/opzet-background-p1-night.png` en `-p2-night.png`. `filterUnits="userSpaceOnUse"` over het hele canvas voorkomt dat de schaduw onder lage kaarten (216 px) wordt afgeknipt.
- `opzet-layout.json`: logoslot `w` 144 → 194 op beide pagina's; `z_masthead` / `z_masthead2` `x` 192 → 240, `w` 1696 → 1648 (rechts uitgelijnd, dus de tekst verschuift niet).
- Registratie blijft zoals nu (`opzet_report.py` `page()`, regels 268-273, VERIFY-fallback: Format page > Canvas background > image, Fit, 0 %).

**Acceptatiecheck.** De renders op 1920 en 1366 tonen de zone tot y 312 en de eerste kaartrij die erover hangt; geen haarlijnen om de kaarten; de schaduw is op beide pagina's identiek; de PNG's zijn per pagina gegenereerd, niet met de hand bewerkt (canvas-guide paragraaf 4).

---

## D2b - De vervaagde hanger in de zone

**Inhoudelijk.** Rechtsboven in de zone de gezichtsloze hanger, groot, Oat op 6 %, 10 graden gekanteld en afgesneden door de horizon. Het enige stuk merktheater op de pagina, en het blijft in het kader. Bjorn wilde hem houden (chat, 9 november 10:24: "It feels like the faded door hanger on the right top has been lost ... Can you verify and fix when needed"). Daarmee vervallen voor de header-zone hard rule 6 (decoratieve beelden) en de canvas-guide-regel "no logos" in de achtergrond; vastgelegd in `status.yaml`. De gradient en de gloed blijven buiten de spec (D7).

**Data.** Geen.

**Technisch.** `opzet_backgrounds.mjs`, in de `<defs>` en direct na de zone-rect (`${hangerLayer(horizon)}`). Getest op de echte slotmap; de hanger valt in de opzet rechts van de headline en boven `card_geo` / `card_panel`.

```js
// D2b: 6 % Oat, scale 7.2, tilted 10 degrees counter-clockwise about the hole, clipped by the horizon.
// Same geometry as comps_v3.hanger_layer and brand_canvas_v3.py.
function hangerLayer(horizon, k = 7.2, x = 1350, y = -150, tilt = 10, opacity = 0.06) {
  const ox = x + 12 * k, oy = y + 7 * k, cx = ox + 28 * k, cy = oy + 20 * k;
  return `<clipPath id="zone-clip"><rect width="${W}" height="${horizon}"/></clipPath>
<mask id="hanger-hole" maskUnits="userSpaceOnUse" x="0" y="-400" width="${W}" height="1600">
<rect x="0" y="-400" width="${W}" height="1600" fill="white"/>
<circle cx="${cx}" cy="${cy}" r="${10 * k}" fill="black"/><rect x="${cx}" y="${oy + 18.5 * k}" width="${28 * k + 1}" height="${3 * k}" fill="black"/></mask>
<g id="zone-hanger" clip-path="url(#zone-clip)"><g transform="rotate(${-tilt} ${cx} ${cy})">
<rect x="${ox}" y="${oy}" width="${56 * k}" height="${96 * k}" rx="${14 * k}" fill="#E9E5D6" fill-opacity="${opacity}" mask="url(#hanger-hole)"/></g></g>`;
}
```

Contrast van de zonetekst over de hanger (achtergrond dan `#1E2E46`): headline 12.6:1, masthead/subtitel 8.8:1, eyebrow 8.3:1.

**Acceptatiecheck.** De hanger is zichtbaar maar zacht (6 %), staat alleen in de zone, wordt door de horizon afgesneden en raakt geen data; zonder de waiver in `status.yaml` gaat deze `hangerLayer`-regel eruit.

---

## D3 - Tekst in de zone

**Inhoudelijk.** Alles wat op de Night-zone staat, wordt licht.

**Data.** Geen.

**Technisch.** `opzet_report.py`, drie constanten erbij (kit-tokens `zone_text`, `zone_text_muted`, `zone_eyebrow`):

```python
ZONE_TEXT, ZONE_MUTED, ZONE_EYEBROW = "#F7F5EE", "#C9D0DC", "#A9CDF0"
```

| Visual | Regel | Nu | Wordt | Contrast op Night |
|---|---|---|---|---|
| `z_masthead`, `z_masthead2` | 118, 199 | `colour=INK2` (default) | `colour=ZONE_MUTED` | 10.2:1 |
| `z_headline`, `z_headline2` | 119, 200 | `colour=INK` | `colour=ZONE_TEXT` | 14.4:1 |
| `c_subtitle`, `c_subtitle2` | 120, 201 | `colour=INK2` (default) | `colour=ZONE_MUTED` | 10.2:1 |

`ZONE_EYEBROW` is voor een eventuele eyebrow-regel ("01  THE BRAND REVIEW", zoals in de comps); de opzet heeft die nu niet en hij is geen eis.

**Acceptatiecheck.** `ax-audit` / `check_contrast.py` op de zonetekst groen; de tekst blijft leesbaar op 1366 (R4).

---

## D4 - Eén kaartstijl per pagina

**Inhoudelijk.** Lock 9: elke kaart op een pagina heeft dezelfde stijl. Topkaarten: wit, radius 12, geen haarlijn, de D2-schaduw. De P2-binnentegels (`tile_preset_a/b/c`, tekstvakken in `tile()`, regels 190-195) staan **binnen** `card_panel` en zijn dus geen topkaart: zij houden canvasvulling + haarlijn, zonder schaduw (een schaduw binnen een kaart leest als een tweede laag).

**Data.** Geen.

**Technisch.** Niets extra's: `tile()` gebruikt `CANVAS` en `HAIR`, die met D1 meekomen. Visuals op kaartslots blijven transparant (canvas-guide paragraaf 3).

**Acceptatiecheck.** Op elke pagina hebben alle topkaarten dezelfde schaduw en geen rand; de binnentegels zijn zichtbaar als tegels zonder schaduw.

---

## D5 - Koppen en woordkeus

**Inhoudelijk.** De deurhanger-koppen horen bij de mascotte-richting. 3.1 spreekt in korte, zakelijke stellingen; de getallen staan in de subtitel en in de kaarttitels.

| Visual | Nu | Wordt |
|---|---|---|
| `z_headline` (+ alt) | "Do not disturb, since 2020." | "Full rooms, fading guests." |
| `z_headline2` (+ alt) | "Please make up the room." | "Fix the booking before the building." |
| `c_full_title` (regel 150) | "... airports in raspberry" | "... airports in blue" |
| `c_scatter_sub` (regel 203) | "Raspberry: the package in focus ..." | "Dark: the package in focus. Blue: without the refresh. Grey: with the refresh." (exacte zin bij de build) |
| measure-docstrings `sketch_model.py` 604, 605, 639, 668, 670 (`Initiative Chip`) | noemen raspberry/plum | nieuwe kleurnamen (docstrings zijn documentatie, geen canvas) |

**Data.** Geen.

**Technisch.** `opzet_report.py` regels 119, 150, 200, 203; de docstrings in `sketch_model.py`. Dezelfde copy-rebuild als 09 R2, R4 en R5; `Subtitle P1 (text)` / `Subtitle P2 (text)` volgen de 09-formulering (geen NPS als hoofdbewijs).

**Acceptatiecheck.** `copy-polish` zonder bevindingen op deze strings; geen kleurnaam op het canvas die niet meer klopt.

---

## D6 - Grafiek- en statuskleuren

**Inhoudelijk.** Dezelfde regel op elke visual: GN blauw, zusters grijs, Tangerine alleen bij een signaal, Night voor het pakket in focus en voor totalen.

**Data.** Geen.

**Technisch.**

- `sketch_model.py` (de kleurmeasures volgen de nieuwe constanten automatisch; deze vragen een expliciete keuze):
  - `Hotel Bar Color` (605): airport `ACCENT_MARK` (was `ACCENT`), overig `SLATE`.
  - `Package Point Color` (639): focus `INK` (Night, 15.8:1 op wit; was `ACCENT`), zonder refresh `ACCENT_MARK` (was `PLUM`), met refresh `SLATE`.
  - `Initiative Status Color` (668): funded `ACCENT` (Deep Coffee, 6.2:1), niet funded `INK2`.
  - `Occupancy Heat Color` (603) en `GN Column Tint` (604): `TINT` / `TINT2` uit de D1-tabel.
  - `_chip()` / `_hanger()` (regels 536-552): gezichtsloze hanger. Funded: pil Ice `%23EAF2FB`, hanger Coffee Blue `%232589D8` met het gat in Ice; niet funded: pil wit met haarlijn `%23E3DFD3`, hanger `%23C9C4B7`. De `face`-tak vervalt. De chip blijft decoratief; het woord Funded/Not funded draagt de betekenis.
- `opzet_report.py`:
  - trends (regel 163): `mref(ms[0]): ACCENT_MARK`, zusters `SLATE`.
  - cumulatief netto (regel 256): Low `SIGNAL_MARK` (1 px), Expected `ACCENT_MARK` (2 px), High `ACCENT_MARK` (1 px). Gestippeld voor Low alleen als de lineStyles-shape dat ondersteunt: VERIFY tegen het visualContainer-schema 2.11.0 (research-first); anders volstaat de kleur plus het label "Low".
  - waterfall `sentimentColors` (regel 237): `increaseFill` `ACCENT_MARK`, `decreaseFill` `SIGNAL_MARK`, `totalFill` `INK`.
  - knoppen (regel 183): `ACCENT` (Deep Coffee) als vulling met witte tekst.

**Acceptatiecheck.** Geen visual waarin Tangerine een merk of reeks-identiteit tekent; verdicts altijd met ▲/▼ of woord; contrast van marks ≥ 3:1 op wit.

---

## D7 - Optioneel, alleen met waiver: night-glow

**Inhoudelijk.** De variant die Bjorn als eerste zag, minus de hanger (die zit sinds 9 november in de spec, D2b): de zone als verloop van Night naar navy, een Coffee Blue gloed, een zwaardere schaduw onder de hoofdkaart en een blauwe gloed onder het aanbevolen pakket. Iets rijker, maar het buigt hard rule 6 (gradients) en lock 9 (twee kaartstijlen op één pagina).

**Data.** Geen.

**Technisch.** De achtergrond wordt dan `design/brand-kits/goodnight-inn-wakeup/assets/canvas-night.jpg` (gegenereerd door `project/tools/brand_canvas_v3.py`; numpy + Pillow, design-time, geen onderdeel van de stdlib-buildketen) in plaats van de D2-zone. Alleen met een waiver van Bjorn in `status.yaml`, met reden.

**Acceptatiecheck.** Waiver geregistreerd vóór de build; anders geldt D2.

---

## 3. Raakvlakken met 09 (deel A)

- **R1** (ADR/RevPAR-index): het optionele vierde trend-slot gebruikt "GN in raspberry/ACCENT, zusters in SLATE". Met D1/D6 wordt dat `ACCENT_MARK` en `SLATE` (nieuwe waarde).
- **R2, R4, R5** (copy): zelfde copy-rebuild als D5; `Subtitle P1 (text)` volgt R2, de headline volgt D5.
- **R3** (`Plan Margin (text)` op de P2-landing): de zin staat op een witte kaart, niet in de zone; lettergrootte volgens R4.
- **K1/V1** uit 07/08: ongewijzigd voorwaarde voor R3.

## 4. Gezamenlijke implementatievolgorde (rebuild-pakket 09 + 10)

0. **Bjorn:** go-ahead op het pakket; besluit over D7 (waiver voor de gradient ja of nee; de hanger-waiver D2b staat al); de kitwissel staat in het addendum van `00-brand-decision.md`.
1. **D1:** `project.yaml` + `compile_theme.py` + `check_contrast.py --theme` (één commit).
2. **Eén rebuild van `sketch_model.py`:** 09 R3 met K1/V1, R2, R4, R5, plus D6 (kleurmeasures, chip) en de D5-docstrings.
3. **Eén rebuild van `opzet_backgrounds.mjs` + `opzet_report.py`:** D2, D2b, D3, D4, D5, D6 (+ de `opzet-layout.json`-wijzigingen uit D2).
4. **09 R1** na de haalbaarheidscheck van de indexlijnen; trend-slot alleen als het canvas het toelaat (V4).
5. **De vaste cyclus:** `schema_check.py`, rebuild, renders op 1920 en 1366, vergelijking met `comps/*-night.jpg` (look) en de slotmap (posities), `ax-audit`, eigen-ogen review (K6), en de Publish-to-Web-gate bij Bjorn, **inclusief de Segoe UI-test op een Mac of in een browser zonder Segoe UI**.

## Open questions

- **Segoe UI op een Mac onder Publish-to-Web:** levert de service het als webfont? Onbekend. Test vóór stap 5; terugval Arial en de layout opnieuw meten.
- **D7:** waiver of niet (Bjorn).
- **Dichtheid P2 rechterkolom** op 1366 met het R4-minimum: als het niet past, gaat de initiatieventabel naar een tooltip (tt-tooltips) in plaats van kleinere letters.
- **Naam van de kit:** `goodnight-inn-wakeup` stamt uit de posterfase; hernoemen kan, maar dan ook `project.yaml`, de tools en dit plan.
