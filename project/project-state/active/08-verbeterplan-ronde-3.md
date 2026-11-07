# 08 - Verbeterplan ronde 3 (7 november 2026, middag)

**Datum:** 2026-11-07 - **Gevraagd door:** Bjorn (na review-ronde 2: "Ja maak maar
weer een verbeterplan van", plus vier nieuwe feedbackpunten en een merkpunt via
WhatsApp) - **Stage:** 0. Dit bestand is het **vervolg** op
`07-fixgids-review-v2.md`, geen vervanging: de fixgids blijft de bron voor ronde
1 en 2; dit plan legt Bjorns nieuwe punten vast plus de punten die na ronde 2
nog open staan. Per punt: wat, waar, hoe de fix eruitziet en hoe je controleert
dat hij werkt.

## 0. Bronnen en status

- **Feedback van Bjorn, 7 nov 13:20-13:36 (WhatsApp):** (1) C moet qua framing
  naar voren komen als het antwoord op "waarom niet alles renoveren", niet als
  derde kandidaat; (2) tooltips bij de scatter: high-end kaartjes die in een
  oogopslag de kern van het plan tonen; (3) de nullijn subtieler (dunner,
  gedempte contrastkleur); (4) het canvasruimte-gebruik is nog niet optimaal;
  (5) merkbeeld en merkherkenning mogen sterker terugkomen.
- **Ronde-2 review (32 renders, map `2026-11-07-desktop-batch2` op PR #5):**
  alle drie de dealbreakers (F1-F3) opgelost, 0 blockers, 0 nieuwe fouten.
  Open gebleven: N8, N9, N11, S1, R4, S10 en de Publish-to-Web-gate (R6/N10).
- **Fixgids ronde 1+2:** `07-fixgids-review-v2.md`; volledige bevindingen:
  `research/log/2026-11-07-screenshot-review-v2.md`.
- De punten hier gelden voor de build op/na PR #5 (fixes zitten in commit
  aaab95b). Controleer per punt eerst of het op de dan-actuele build nog speelt.

## 1. Werkwijze (ongewijzigd: generator-first)

Gelijk aan fixgids paragraaf 2: **nooit handmatig in Power BI Desktop fixen.**
Model, measures en copy in `project/tools/sketch_model.py`; rapport, visuals,
tooltip-pagina's en knoppen in `project/tools/opzet_report.py`; posities in
`project/design-prototypes/opzet-layout.json`; thema via
`project/deliverables/theme.json` (`compile_theme.py`). Na elke wijziging:
`schema_check.py`, openen in Desktop, verversen, betrokken states opnieuw
renderen op 1920 x 1080 en met eigen ogen beoordelen. PR #5 en PR #2 blijven
ongemoeid; dit plan wordt op een eigen branch gebouwd.

## 2. Nieuwe punten van Bjorn (V1-V5)

### V1 - C framen als het antwoord op "waarom niet alles renoveren" (risico: framing)

- **Wat:** C leest nu als een derde kandidaat ("the alternatives B and C"),
  terwijl zijn functie anders is: C is het bewijs dat het dure pad serieus is
  doorgerekend en binnen de horizon niet terugverdient. Bjorn: "dan moet dat
  ook wel zodanig naar voren komen." Zonder die framing kan een jury C lezen
  als een slordige nominatie.
- **Waar:** dropdown-label en planheader van C, landingsregel; tekstmeasures in
  `sketch_model.py`.
- **Fix:** benoem de rol van C expliciet, bijvoorbeeld in de dropdown ("C - the
  full refresh: fixes the estate, doesn't pay back by 2032") en een regel onder
  de planheader van C ("Shown to answer 'why not renovate everything?': the
  full refresh costs $36.9M and stays negative through 2032."). Alleen claims
  gebruiken die het model ondersteunt; het patroon "meer geld = slechtere NPV"
  wordt al door de scatter ondersteund (6 van 456 positief in Expected).
  Overweging: A en B blijven wel echte kandidaten; alleen C krijgt deze
  comparator-rol, zoals R3 de dropdown al tot benoemde opties beperkte.
- **Acceptatiecheck:** iemand die alleen de landing en plan C ziet, kan zonder
  mondelinge uitleg zeggen waarom C getoond wordt; nergens presenteert de copy
  C als aanbevolen kandidaat; de cijfers in de framing ($36.9M, -$34.8M Low)
  zijn natelbaar.

### V2 - Tooltip-kaartjes bij de scatter (kans)

- **Wat:** Bjorn wil bij hover een mooi kaartje dat in een oogopslag de kern
  van een pakket toont, "desnoods custom visual based".
- **Route (eerst native, custom visual alleen als fallback):** bouw dit met een
  native **report tooltip page**. Die blijft binnen de bestaande architectuur,
  is volledig te sturen vanuit `opzet_report.py` en is Publish to Web-proof.
  Een custom visual mag alleen als **gedocumenteerde fallback**: uitsluitend
  een AppSource-**gecertificeerde** visual (niet-gecertificeerde visuals breken
  Publish to Web), vastgelegd als besluit in dit bestand, en pas na een
  expliciete Publish to Web-check in de browser. Die check hoort bij de
  user-owned gate in paragraaf 3.
- **Concreet ontwerp (native tooltip page, ca. 380 x 220 px):**
  - *Header:* pakketnaam of initiatiefcodes + capex ("Package A - $9.4M").
  - *Kerngetal:* NPV in het gekozen scenario, groot, in raspberry (boven nul)
    of ember (onder nul); eronder de range "Low -5.5 / High +12.7" in klein.
  - *Regel:* payback ("Pays back 2031" / "Does not pay back by 2032" - zie N11).
  - *Regel:* inhoud ("3 initiatives: booking app, revenue mgmt, kiosks").
  - *Stijl:* sheet-wit kaart, 12px radius, plum-black ink, Trebuchet/Verdana
    volgens de brand kit; geen standaardtooltip-look.
  - Dezelfde tooltip werkt voor A, B, C (highlights) en voor de grijze wolk:
    elke dot vertelt zijn eigen verhaal.
- **Acceptatiecheck:** hover-renders in Desktop op A, B, C en een willekeurige
  grijze dot tonen naam, capex, NPV en payback binnen 3 seconden, zonder klik;
  na publicatie dezelfde check in de browser (hoort bij de P2W-gate). De
  hoofdconclusie (6 van 456 boven de lijn) blijft op het canvas staan - de
  tooltip is verdieping, geen verstopplek.

### V3 - Nullijn subtieler (smaak)

- **Wat:** de nullijn in de scatter is de vonnislijn van de grafiek: hij moet
  zichtbaar blijven maar niet de baas spelen. Nu oogt hij zwaar.
- **Waar:** scatter-configuratie in `opzet_report.py` / `opzet-layout.json`.
- **Fix:** dunner (1 px) en in een gedempte contrastkleur in plaats van zwart -
  bijvoorbeeld plum-slate `#82798A` (neutral data uit de kit) of plum-grey
  `#5B5163`. Niet hairline-licht (`#E4DEE3`): dan verdwijnt de betekenis.
- **Acceptatiecheck:** op de gerenderde landing (state 02) is de lijn op 100%
  zoom direct vindbaar, maar valt hij niet op als zwaarste lijnelement van de
  pagina; A, B en C blijven visueel boven de lijn uitkomen.

### V4 - Canvasruimte van de scatter (risico/smaak)

- **Wat:** de scatter ligt als brede strook in het midden met loze ruimte erboven
  en eronder; de actie zit in een smalle band rond de nullijn terwijl de
  uitschieters de schaal bepalen. Het interessante deel krijgt de minste pixels.
- **Waar:** layout-slot map in `opzet-layout.json`, kopregels via measures in
  `sketch_model.py`.
- **Fix:** geef de scatter de volle hoogte tussen kop en bronregel en trek de
  kop strakker (titel + een ondertitel). Evalueer daarna of **zoom op A/B/C als
  uitgangspunt** de ruimte beter benut: de zoom-schakelaar (default "all")
  bestaat al. Als ingezoomd de default wordt, moet de state dat expliciet
  labelen ("zoomed on A, B and C - full view one click away") en de
  all-knop zichtbaar blijven; de volledige wolk blijft een klik weg.
- **Acceptatiecheck:** renders op 1920 en op 1366 breed tonen geen loze banden;
  kop maximaal twee regels; bij een ingezoomde default zijn A, B en C gelabeld
  zichtbaar, staat er een duidelijke zoom-aanduiding en werkt de weg terug naar
  de volledige wolk (render als bewijs).

### V5 - Merkbeeld en herkenbaarheid versterken (kans)

- **Wat:** Bjorn: het merkbeeld en de herkenning van het merk mogen beter
  terugkomen; zo nodig ontwerpwerk in Gemini of ChatGPT voor logo's en
  merkherkenbaarheid. De brand kit (`goodnight-inn-hanger`) en het bewust
  wisselende logo (slapend op P1, wakker op P2) zijn al besloten; dit punt gaat
  over zichtbaarheid ervan in de build.
- **Concrete ingrepen (native, Publish to Web-proof):**
  - *Lockup + pay-off:* de hanger-lockup prominenter op beide mastheads, met
    de pay-off zichtbaar op P1 ("Do not disturb, since 2020." / "Please make up
    the room." op P2) - dat is het merkidee dat een jury kan quoten.
  - *S1 scenario-tiles in huisstijl:* de stock grijze tiles zijn het enige
    element dat nog "stock Power BI" oogt op een verder gebrande pagina: dunne
    afgeronde outline voor niet-geselecteerd, plum-black voor geselecteerd,
    hoogte gelijk aan de dropdown, uitlijnen op x 1112. Dit punt dekt S1 uit
    de fixgids.
  - *Kleur en typografie consequent:* raspberry `#B5175F` als enige accent,
    plum-black ink, Trebuchet/Verdana volgens de kit; audit de renders op
    afwijkingen (standaardkleuren, standaardfonts).
- **Extern gegenereerde beeldassets (Gemini/ChatGPT):** alleen als vastgelegde
  **asset-stap**, niet als losse afbeelding: (1) genereer het asset, (2) leg
  het met bron en datum vast in `design/brand-kits/goodnight-inn-hanger/assets/`,
  (3) embed het via de generator in het rapport (Publish to Web vereist embedded
  images; externe links mogen niet), (4) verifieer op de renders dat het landt.
  Merkassets handmatig in Desktop plakken is dezelfde fout als handmatig fixen.
- **Acceptatiecheck:** de renders van P1 en P2 tonen lockup, pay-off en
  huisstijl-tiles; geen stock-elementen of standaardkleuren zichtbaar; elk
  extern asset staat in de brand-kit-map met bron en zit embedded in de build.

## 3. Vervolg: open punten uit review-ronde 2

- **N8 - Hover-bewijs Back-knop (fout-bewijs, klein).** F6 is geclaimd maar niet
  aangetoond: geen render toont de muis op Back. Een extra render met de muis op
  Back bewijst de fix en sluit meteen uit dat de risicotekst een verdwaalde
  knop-actie draagt. Acceptatiecheck: de render toont een leesbaar Back-label
  bij hover en geen cursor-feedback op de risicotekst.
- **N9 - Risicoregel scenario-bewust (smaak).** In het eigen scenario leest
  "NPV in the Low case ... (Low)" tautologisch; gebruik daar "in this case".
  Tekstmeasure in `sketch_model.py`. Acceptatiecheck: de regel leest strak in
  elk van de drie scenario's.
- **N11 - Horizonclaim waterdicht (risico).** "The cumulative net turns positive
  after 2032" claimt iets buiten de horizon die de pagina zelf uitsluit
  ("nothing after 2032 is counted"). Vervang door "does not pay back by 2032".
  Acceptatiecheck: geen enkele regel claimt iets over de periode na 2032.
- **R4 - Minimum-font (risico).** Secundaire tekst is circa 9 px op 1366 breed;
  minimum naar circa 16 px op 1920 (11-12 px op 1366) voor tabel-, as- en
  notetekst. Ruimte komt uit V4 (strakkere kop) en uit het verbergen van
  nul-ops-tiles (K2). Acceptatiecheck: renders op 1366 breed (71% schaal)
  beoordeeld; de planstate voelt niet als een spreadsheet.
- **S10 - Twee open vragen beantwoorden (copy).** Welke 20 hotels krijgen
  kiosks, en waarvoor en wanneer wordt $50.6M vastgehouden. Elk in een bijzin,
  alleen met wat het model ondersteunt. Acceptatiecheck: beide vragen zijn op
  de landing te beantwoorden zonder te rekenen.
- **R6/N10 - Publish to Web: user-owned gate (Bjorn, geen Claude-taak).** De
  wedstrijd vereist Publish to Web; de test beslist definitief over de
  locale-mix (N10: "+$3,4M" direct boven "+$3.4M" in state 08) en over de
  header-iconen. De bouw houdt alles P2W-proof (ingebouwde fonts, embedded
  images, native tooltip pages, geen ongecertificeerde custom visuals), maar
  het publiceren en de browser-test zijn van Bjorn: de link openen in een
  schone browser, zonder inlog, in nl-NL en en-US. Acceptatiecheck: de
  gepubliceerde link werkt in beide locales en toont nergens twee
  getalformaten naast elkaar.

## 4. Volgorde tot 18 november

1. **Copy en framing:** V1 (C-framing), N9, N11, S10 - allemaal measures in
   `sketch_model.py`, een rebuild.
2. **Canvas en nullijn:** V4, V3 - layout en scatter-config.
3. **Tooltips:** V2 - native tooltip page; fallback-besluit alleen als het
   native ontwerp de kaartjes aantoonbaar niet mooi genoeg krijgt.
4. **Merk en leesbaarheid:** V5 (inclusief S1), R4.
5. **Bewijs:** N8 hover-render; daarna de volledige render-en-reviewcyclus (K6)
   op de finale build.
6. **Bjorn (user-owned):** de Publish-to-Web-gate (R6/N10), in een nl-NL en een
   en-US browser, zonder inlog. Dit is het kritieke pad: plan het niet vlak
   voor de deadline.

Deadline: 18 november 2026 23:59 PT; streven blijft inleveren op 17 november.

## 5. Status na batch 3 (7 november, Claude Code)

Gebouwd in de generators op branch `upgrade-opzet-v3` (op de build van PR #5). Renders en eigen review:
`project/deliverables/screenshots/2026-11-07-desktop-batch3/` (README + SELF-REVIEW, 35 beelden).

| Punt | Status | Kort |
|---|---|---|
| V1 C-framing | gedaan | Dropdown "C · Why not renovate? For comparison"; landing, plantitel en eerste planregel noemen C het antwoord op "waarom niet renoveren"; "in elk scenario onder nul (High −$11,4M)" wordt berekend, niet getypt. |
| V2 Tooltips | gedaan (P2W-check bij Björn) | Native tooltip-pagina `tt-package`: chip (wakker/slapend), naam, NPV in raspberry/ember, capex, drie scenario's, payback, de ingrepen. Werkt op A, B, C én de wolk via een derde, transparante scatterlaag; N3 is daarmee dicht. |
| V3 Nullijn | gedaan | 1 px plum-slate; het vlak erboven licht gearceerd met het label "Pays back by 2032". |
| V4 Canvasruimte | deels | Assen in stappen van $5M met marge, capex vanaf $5M, het lege vlak boven nul is nu de payback-zone. Zoom als default afgewogen en niet gedaan (Björns keuze "All packages"; "6 of 456" heeft de hele wolk nodig); omzetten is één waarde. |
| V5 Merk | gedaan | Merkrij op beide pagina's: lockup op 56 px, pay-off in raspberry, masthead, en een met Gemini gegenereerde vignet van dezelfde hoteldeur (P1 dicht, hanger slaapt; P2 open, hanger wakker). Vastgelegd in `design/brand-kits/goodnight-inn-hanger/assets/GENERATED-ASSETS.md`, embedded via de generator. Chip bij de aanbeveling en in de tooltip. |
| S1 Tegels | gedaan | Button slicers in huisstijl (afgeronde outline, geselecteerd plum-black met witte tekst), 40 px, uitgelijnd op x 1112. |
| N8 Hover Back | gedaan | L2b/Z1: grijze hover, label leesbaar; Z2: de risicoregel draagt geen knopactie. |
| N9 Risicoregel | gedaan | "in this case" voor het scenario in beeld. |
| N11 Horizon | gedaan | Geen claim meer na 2032 ("does not pay back by 2032"). |
| R4 Minimumfont | gedaan, op 11 pt | 11 pt (15 px) is de kleinste tekst; renders op 1366 breed in W1366a-c. 16 px op 1920 zou een derde minder tekst in het P2-paneel vragen. |
| S10 Open vragen | gedaan | Kiosks naar de 20 volste hotels (9 airport, 7 highway, 4 city; gecontroleerd op bezetting 2025); $50,6M wordt achtergehouden tot alle drie de ingrepen live zijn (apr 2028), omdat geen ander initiatief vóór 2032 terugverdient, ook niet in High. |
| R6/N10 P2W | deels, Björn | Gepubliceerd in de Power BI-service (7 nov): https://app.powerbi.com/groups/me/reports/4888e342-dfcc-49d7-8df1-ad893b9789a0/p1-brand-review?experience=power-bi . Dat is een werkruimtelink met inlog; de anonieme Publish-to-Web-link (`view?r=...`) en de browsertest in nl-NL en en-US blijven het kritieke pad. |

Nieuwe eigen bevindingen N12-N17 (o.a. hover op de rand van B kan een buur-stip tonen, de cumulatieve grafiek is
kleiner geworden, het paneel blijft het dichtste deel): zie SELF-REVIEW.
