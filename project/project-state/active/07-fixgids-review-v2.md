# 07 - Fixgids screenshot-review v2 (7 november 2026)

**Datum:** 2026-11-07 - **Gevraagd door:** Bjorn ("Kun je alles vastleggen met een
how to op te lossen door claude in de repo?") - **Stage:** 0. Dit bestand legt alle
bevindingen uit de screenshot-review van 7 november vast als werkinstructie voor
Claude Code: per punt wat er mis is, waar het zit, hoe de fix eruitziet en hoe je
controleert dat hij werkt. Het sluit geen gate; `status.yaml` krijgt alleen een
gate note.

## 0. Bronnen en status

- **29 Desktop-screenshots + onafhankelijke review:** branch `upgrade-opzet-v2`
  (PR #5), map `project/deliverables/screenshots/2026-11-07-desktop/`. Verwijzingen
  als B1, M1-M11, m1-m11 en p1-p10 zijn de ID's uit `REVIEW.md` in die map.
  PR #5 was nog niet gemerged toen dit geschreven werd; PR #2 blijft ook ongemoeid.
- **Volledige bevindingen met cijferverificatie:**
  `research/log/2026-11-07-screenshot-review-v2.md`. Dat is de bron van waarheid
  voor wat er mis is; dit bestand is de bron voor hoe het opgelost wordt.
- De screenshots tonen de build op PR #5 (commit 2a3e6ae). Controleer per punt
  eerst of het op de dan-actuele build nog speelt; punten kunnen al gefixt zijn.

## 1. Geverifieerde cijfers

Nagerekend tegen `project/analysis/output/packages.csv` en `project_yearly.csv`;
de rekenkern klopt, de problemen zitten in presentatie en randgevallen.

- 456 geldige pakketten; NPV-positief tot 2032: 6 in Expected, 0 in Low, 57 in High.
- A = 01+02+10: $9.4M capex, NPV +$3.3M (range -5.5 / +12.7), run-rate $3.5M,
  terugverdiening 2031 (Expected), 2029 (High), na 2032 (Low).
- B = 01+09+10: $11.7M, +$2.7M (Expected). C = 01+07+10: $36.9M, -$23.4M (Expected).
- B en C zijn op dit moment dynamische regels, geen vaste pakketten: B in High =
  01+02+09+10 ($13.7M); C in Low = 01+02+07, in High = 01+02+07+10.
- Het $60M-pakket kost exact $60.0M; de tabel toont 60.1 door afronding van delen.
- A voldoet aan de growth-eis: booking app en revenue management tellen als growth.

## 2. Werkwijze voor elke fix (generator-first)

**Nooit handmatig in Power BI Desktop fixen.** Bij de volgende rebuild verdwijnt de
fix. Pas de generators aan en bouw opnieuw:

| Laag | Generator | Output |
|---|---|---|
| Model, measures, DAX | `python project/tools/sketch_model.py` | `project/pbip/PillowKey.SemanticModel` |
| Rapport, visuals, knoppen, bladwijzerstaten | `python project/tools/opzet_report.py` | `project/pbip/GoodnightInn-opzet.Report` |
| Posities | `project/design-prototypes/opzet-layout.json` (slot map) | via opzet_report.py |
| Thema | `project/deliverables/theme.json` (`compile_theme.py`) | rapportthema |

Na elke wijziging:

1. `python project/tools/schema_check.py` op de gewijzigde bestanden.
2. Open in Desktop, ververs, en render de betrokken states opnieuw op 1920 x 1080
   (recept: `README.md` bij de screenshots op PR #5; vaste states via de eigen
   bookmarks `bm_p2_shortlist` / `bm_p2_plan`, kliks via de L-serie-aanpak).
3. Beoordeel de nieuwe renders met eigen ogen, niet alleen via tool-samenvattingen.
   Herhaal de onafhankelijke review (zie kans K6) voordat iets "klaar" heet.

Relevante skills: `fx-focus` (focuswissel en bookmark-regels), `dax-patterns`,
`tmdl-patterns`, `pbir-authoring`, `chart-grounding` en `dataviz-canon` voor de
visuele keuzes, `verification-before-completion` voor de afronding.

## 3. Fouten (aantoonbaar, dealbreakers eerst)

### F1 - B in het Low-scenario geeft een kapotte planpagina met een valse zin (REVIEW B1)

- **Wat:** kies B en klik Low (twee kliks vanaf de openingsstate). De planpagina
  toont een lege waterfall, overal "Not funded", en de risicoregel beweert
  "the cumulative net turns positive in 2027" terwijl niets gefinancierd is. De
  header zegt "No package in focus" terwijl de dropdown nog B toont.
- **Waar:** screenshots `15` (via `14`). Measures o.a. `Plan Risk (text)` in
  `sketch_model.py`; empty-state van de planvisuals in `opzet_report.py`.
- **Fix:** de echte oplossing is kans K1 (A/B/C bevriezen als vaste sets), dan kan
  deze state niet meer leeg zijn. Bewaken blijft nodig voor elk leeg pakket:
  - `Plan Risk (text)` geeft geen NPV-fragment als NPV blank is (nooit "+M") en
    geen terugverdienjaar-fragment als niets gefinancierd is.
  - De header leest "B heeft geen pakket in het Low-scenario" in plaats van
    "No package in focus".
  - De landing toont een waarschuwingsregel onder de dropdown als de focus leeg is.
  - Geen lege waterfall met drie identieke nul-ticks: leg een message card overheen,
    aangestuurd door een measure.
- **Acceptatiecheck:** state 14/15 opnieuw renderen. Geen verzonnen
  terugverdienjaar; de pagina leest als een bewuste, verklaarde lege state; de
  ops-tiles gebruiken een consequente null-weergave.

### F2 - De titel "Fund the three moves that pay" wordt tegengesproken door de eigen waterfall (REVIEW M3)

- **Wat:** de kiosks hebben NPV -$0.6M (Expected), -$1.2M (Low), +$0.0M (High) en
  betalen nooit terug tot 2032. De titel claimt drie moves die "pay". De
  not-funded-zin op de landing gebruikt dezelfde toets die de kiosks niet halen.
- **Waar:** alle P2-states; waterfall in `08`-`10`; titelmeasures in
  `sketch_model.py`, titelvisual in `opzet_report.py`. Let op: de titel komt uit
  beslissing 2 in `06-d1-briefing-opzet.md`; leg de herziening daar ook vast.
- **Fix:** een titel die in alle drie de scenario's klopt, bijvoorbeeld "Fund one
  package of three moves: $9.4M now, $50.6M held back." Voeg op de landing een zin
  toe: "Kiosks alone don't pay back by 2032 (-$0.6M); they are the cheapest answer
  to F3, and the package still returns +$3.3M." Verander de not-funded-reden naar
  wat de selectie echt toetst ("each would lower the package NPV"). Voeg buiten
  Expected "recommendation set on the Expected case" aan de ondertitel toe.
- **Acceptatiecheck:** in states `03`, `09` en `16` spreekt geen enkel element de
  titel tegen; de sterkere ware versie (het pakket betaalt; kiosks zijn het
  goedkoopste antwoord op F3) staat er expliciet.

### F3 - "C" toont twee verschillende Low-NPV's: -$34.8M vs -$34.5M (REVIEW M6)

- **Wat:** plan C in Expected (`12`) zegt in de risicoregel "NPV in the Low case
  -$34.8M"; de Low-landing (`03`) en plan C in Low (`16`) tonen C op -$34.5M. Ook B
  verschilt per scenario (-$6.9M in `11` vs leeg in `15`). Oorzaak: B en C zijn
  dynamische regels, dus de samenstelling verschuift per scenario.
- **Waar:** `12` vs `03`/`16`; preset-measures `Preset A/B/C Package` in
  `sketch_model.py`.
- **Fix:** kans K1: bevries A, B en C als vaste initiatiefsets gedefinieerd op
  Expected, en evalueer die vaste sets onder Low en High. Dan wordt overal -$34.8M
  de Low-waarde van C en verdwijnt F1. Moeten de regels dynamisch blijven, zeg het
  dan in de landingsregel en de dropdown ("C = best package with the refresh in
  this scenario: ...").
- **Acceptatiecheck:** een jurylid dat de scenarioknop test vindt voor B en C in
  elke state dezelfde samenstelling en dezelfde cijfers.

### F4 - Afronding: delen tellen niet op tot totalen (REVIEW M8)

- **Wat:** het $60M-pakket toont 60.1 in de capex-kolom (24.75 -> 24.8, 4.25 ->
  4.3) terwijl de header $60.0M zegt; waterfall B telt 2.8 terwijl het totaal 2.7
  zegt; run-rates van A tellen op tot 3.6 terwijl de landing "+$3.5M profit a year
  by 2032" zegt; P1 F2 heeft cent-verschillen; F1 zegt 2.8 pt waar de KPI -2.7 pt
  zegt. Onderliggend klopt alles; het is pure weergave.
- **Waar:** `13`, `11`, `02` vs `08`, `01`. Formatstrings en tekstmeasures in
  `sketch_model.py`.
- **Fix:** toon capex met twee decimalen (let op: leid het totaal NIET af van
  afgeronde delen, dan toont het $60.1M en lijkt de $60M-cap gebroken), of leid
  getoonde totalen consequent af van de getoonde delen. Bereken de KPI-delta uit
  de getoonde waarden. Geef "Run-rate" en "profit a year by 2032" dezelfde naam en
  definitie, of benoem het verschil.
- **Acceptatiecheck:** elke tabel is na te tellen met de getoonde cijfers; het
  $60M-pakket toont nergens meer dan $60.0M.

### F5 - Twee getalformaten door elkaar (REVIEW M7)

- **Wat:** visual-opmaak is nl-NL ("79,4%", "$9,4M", "Totaal") en DAX-tekst is
  en-US ("64.7%", "-5.5 to +12.7"), vaak naast elkaar. Ergste geval: "1.180 rooms
  refreshed" boven "15% of 1,180 rooms" in plan C: voor een en-US jury verandert
  daar de betekenis. Na Publish to Web formatteert de viewer naar browser-locale,
  dus elke niet-en-US jury ziet deze mix.
- **Waar:** `01`, `12`, `16`, eigenlijk alle P1/P2-states.
- **Fix:** zet het bestand op English (US). Neem elk getoond getal uit een bron:
  render kaarten en KPI's als DAX-tekst met FORMAT(..., "en-US"), zoals de
  subteksten al doen. Vervang de automatische waterfall-totaalregel "Totaal" door
  een expliciete categorie "Package", zoals in de comp.
- **Acceptatiecheck:** de Publish-to-Web-link in een nl-NL en een en-US browser
  openen; nergens twee formaten naast elkaar; "1,180" overal met komma.

### F6 - De Back-knop verliest zijn label bij hover (REVIEW M1)

- **Wat:** bij hover/press wordt de fill donker maroon (rgb 109,14,57) en blijft
  het label plum-black: contrast 1.4:1, "Back to the recommendation" is onleesbaar.
  De "Open the plan"-knop doet het wel goed (wit op hover, 11.9:1).
- **Waar:** `L3c`, `L4b`. Knopstijl in `opzet_report.py`.
- **Fix:** Back-knop > Style > Hover en Press: witte tekst, of een lichte hover-fill
  (#F3E6EC) met plum-black tekst. Controleer alle vier de states van beide knoppen.
- **Acceptatiecheck:** een hover-screenshot als `L3c` waarop het label gewoon
  leesbaar is.

### F7 - De P1-titel overclaimt tegen het eigen bewijs in (REVIEW M4)

- **Wat:** "...and is losing its guests", terwijl occupancy best-of-4 is (79.4%) en
  F3 zelf zegt "age costs loyalty, not yet rooms".
- **Waar:** `01`. Titelmeasure in `sketch_model.py`.
- **Fix:** bijvoorbeeld "...pays the middleman, and its oldest hotels are losing
  goodwill" of "...and its welcome is fading" (sluit aan bij het F3-label).
- **Acceptatiecheck:** de headline overleeft een jury die hem als eerste tegen de
  kaarten houdt; geen claim verder dan F3's eigen bewijs.

## 4. Risico's (geen fout, wel zichtbaar voor een jury)

### R1 - Scatter: wolk te zwaar, B en C verdwijnen, $60M-dot gesneden, selectie blijft hangen (REVIEW M2 + m7)

- **Wat:** de grijze stippen zijn circa 3x zo zwaar als in de goedgekeurde comp;
  B en C verdwijnen eronder (grijze stippen worden eroverheen getekend); elke dot
  op capex $60M wordt aan de rand doormidden gesneden; een aangeklikte selectie
  overleeft de Open/Back-ronde en wist de kleurcodering.
- **Fix:** terug naar de comp-stijl: kleinere, lichtere stippen (#C9C3CC, 40-50%
  transparant). Leg de highlights erbovenop met een tweede scatter (transparante
  achtergrond, dezelfde vaste assen) die alleen A, B, C en de focus plot, met
  datalabels "A", "B", "C". Zet het x-as-einde op circa $62M zodat randdots niet
  geknipt worden. Bouw de ondertitel uit een measure die "B" laat vallen als B geen
  pakket heeft. Laat de Open/Back-bookmarks de scatter-selectie wissen (Data,
  Selected visuals: alleen scatter) en test dat een klik op een willekeurige dot de
  panelcijfers onveranderd laat.
- **Acceptatiecheck:** in `06`, `16` en `07` zijn B, C en de $60M-dot volledig
  zichtbaar en gelabeld; na L4a-L4c is de kleurcodering weer intact.

### R2 - De cumulatieve grafiek kan de payback-claims niet tonen (REVIEW M9)

- **Wat:** geen x-as, geen jaartallen, drie ongelabelde lijnen, twee y-ticks; de
  dikke lijn volgt het scenario niet; de risicoregel claimt jaren (2031 / 2029 /
  na 2032) die de grafiek niet kan laten zien.
- **Fix:** jaartallen 2027-2032 en een $0-lijn toevoegen; lijneinden labelen Low /
  Expected / High of de gekozen scenariolijn kleuren via een measure; meer hoogte
  geven (ruimte boven de knop, of de nul-ops-tiles laten vallen). Alternatief: de
  grafiek vervangen door een zin: "Pays back: 2029 (High), 2031 (Expected), after
  2032 (Low)".
- **Acceptatiecheck:** de grafiek (of zin) toont zelfstandig dezelfde jaren als de
  risicoregel, in alle scenario's.

### R3 - "Funded" onder niet-aanbevolen pakketten en interne codes in koppen en dropdown (REVIEW M5)

- **Wat:** planheaders lezen "01+07+10 in focus..."; de dropdown bevat 456
  code-labels plus duplicaten van A en B; de statuskolom zegt "Funded" in het plan
  van C, wat als een beslissing leest.
- **Fix:** header uit een measure: "Package A (our recommendation): $9.4M on 3
  initiatives, all live by Apr 2028" of "Package C (considered, not recommended):
  ...". Statuskolom "In package / Not in package", tenzij de focus A is. Beperk de
  dropdown tot A, B, C (plus eventueel het volle $60M-pakket als benoemde
  comparator) en laat de scatter-tooltip de rest dekken; blijven de 456, label ze
  dan met initiatiefnamen en verwijder de duplicaten.
- **Acceptatiecheck:** nergens in board-facing tekst een kale code; niemand die C
  opent leest "Funded" als beslissing.

### R4 - Leesbaarheid op 1366 breed (REVIEW M10)

- **Wat:** vrijwel alle secundaire tekst is circa 9 px op 1366 breed.
- **Fix:** minimum naar circa 16 px op 1920 (11-12 px op 1366) voor tabel-, as- en
  notetekst. Maak ruimte door in de planstate alleen de gefundeerde rijen plus de
  een of twee dichtstbijzijnde missers te tonen en nul-ops-tiles te verbergen.
- **Acceptatiecheck:** renders beoordelen op 1366 breed (71% schaal); de planstate
  voelt niet meer als een spreadsheet.

### R5 - Compliance met de wedstrijdregels is onzichtbaar (REVIEW M11)

- **Wat:** nergens staat welk initiatief de growth-eis dekt; de tabel heeft geen
  type-kolom en toont "0 rooms added", dus wie growth aan kamers gelijkstelt ziet A
  "falen" terwijl A er twee heeft (booking app en revenue management).
- **Fix:** een "Type"-kolom in de tabel (Growth / Margin / Guest) en een
  complianceregel op de landing: "Within the rules: 3 initiatives, 1 growth
  (...), $9.4M of $60M, impact through 2032."
- **Acceptatiecheck:** een jurylid kan de regels afvinken zonder te rekenen.

### R6 - Publish to Web is nog niet getest

- **Wat:** de wedstrijd vereist het; pas daarna zijn locale-gedrag (F5) en
  hover-iconen definitief.
- **Fix:** nu testen, niet vlak voor de deadline. Zet voor publicatie alle visual
  header icons uit (REVIEW p10) zodat hover-iconen geen tekst kunnen bedekken.
- **Acceptatiecheck:** de gepubliceerde link werkt in een schone browser, in nl-NL
  en en-US, zonder inlog.

## 5. Smaak en afwerking (allemaal minor, allemaal zichtbaar)

| # | Punt | Fix | Ref |
|---|---|---|---|
| S1 | Standaard grijze scenario-tiles in plaats van de pills uit het ontwerp | dunne afgeronde outline voor niet-geselecteerd, plum-black voor geselecteerd, hoogte gelijk aan de dropdown, uitlijnen op x 1112, kale "Scenario"-header | m10 |
| S2 | Afgekapte dropdown-labels ("NPV a...") | kortere labels ("B - Most hotels with a score lift, NPV > 0") of bredere slicer | m1 |
| S3 | Tabellen: sorteerpijltjes, links uitgelijnde koppen boven rechts uitgelijnde cijfers, ontbrekende vetregel, alfabetische missers, scrollbar | numerieke koppen rechts; totaalrij vet; sorteren op status dan NPV aflopend; "In package" accentueren; tabelbox vergroten | m5 |
| S4 | F2-legenda met drie identieke grijze stippen | legenda uit, lijneinden direct labelen zoals in de comp (of een grijs label "the other three brands") | m3 |
| S5 | F3 zonder nul-lijn, labels met losse separator | constante lijn op 0; eenregelige labels ("<=5 years (14 hotels)") of twee gestapelde velden; caption "44 of 50 hotels with a renovation date" | m4, m8 |
| S6 | Ops-tiles die "0 rooms added" tonen | verberg een tile als hij nul is | p9 |
| S7 | Waterfall-details | scenario in de titel via een measure ("(Expected)"); korte categorienamen ("Revenue mgmt"); labels buiten de bars; "$0.0M" zonder teken | m6 |
| S8 | Focuswissel geeft nauwelijks feedback op de landing | knoptekst uit een measure ("Open the plan for package B ->") en een focusregel onder de dropdown ("In focus: B - $11.7M - NPV +$2.7M") | m2 |
| S9 | Namen drift tussen panel en tabel ("Toronto extension" vs "Toronto +40 rooms"; "profit a year by 2032" vs "Run-rate") | een naam per ding op elk oppervlak | m9 |
| S10 | Twee open vragen op de landing (welke 20 hotels krijgen kiosks; waarvoor en wanneer wordt $50.6M vastgehouden) | elk in een bijzin beantwoorden, alleen met wat het model ondersteunt | m11 |
| S11 | Kleine polish: headergrid P1/P2 gelijk, paneelritme, F1/F4-assen en labels, scatter-hoeklabels, footertekst, KPI-pijltjes | zie REVIEW.md p2-p8 | p2-p8 |

**Bewust niet "gefixt":** het logo dat tussen P1 (slapend) en P2 (wakker) wisselt
is een brandkit-keuze (REVIEW p1, bevestigd als intentie).

## 6. Kansen

1. **K1 - Vries A, B en C als vaste initiatiefsets (gedefinieerd op Expected).**
   Een ingreep lost F1, F3 en de schuivende B/C-cijfers tegelijk op en past bij
   "investor deck, geen playground". Implementatie: in `sketch_model.py` de
   `Preset A/B/C Package`-regels vervangen door vaste sets (A = 01+02+10,
   B = 01+09+10, C = 01+07+10) en die sets onder elk scenario evalueren. Update
   `04-p2-build-method.md` ("the rules, not the points") en de A5-notitie in
   `05-doorlichting-nieuwe-opzet.md` met het nieuwe besluit.
2. **K2 - Snijden levert meer op dan toevoegen.** Beperk de dropdown tot A, B, C
   (+ eventueel het volle $60M-pakket), verberg ops-tiles die nul zijn, en toon in
   de tabel alleen de gefundeerde rijen plus de dichtstbijzijnde missers.
3. **K3 - De dim-toestand van L4a bewijst hoe rustig een lichtere scatter oogt.**
   Terug naar de comp-stijl is goedkoop en het verschil is groot (zie R1).
4. **K4 - Doe de fixes in de generator, niet handmatig in Desktop** (zie paragraaf
   2). Anders verdwijnen ze bij de volgende rebuild.
5. **K5 - Test Publish to Web nu al** (zie R6).
6. **K6 - Herhaal de render-en-reviewcyclus na de fixes.** Deze ronde vond met 29
   plaatjes 1 blocker en 11 majors zonder dat iemand het rapport hoefde te openen.
   Leg nieuwe renders weer in `project/deliverables/screenshots/` met een eigen
   README en REVIEW.

## 7. Volgorde tot 18 november

1. K1: A/B/C bevriezen + alle plan-measures bewaken tegen een leeg pakket (F1, F3).
2. F6: Back-hover.
3. Woorden waar maken: P2-titel en not-funded-reden (F2), P1-titel (F7), namen in
   plaats van codes en "In package" in plaats van "Funded" (R3).
4. R1: scatter naar comp-stijl.
5. F5 + F4: een getalvorm (en-US) en totalen die kloppen met hun delen.
6. Daarna pas polish (R2, R4, R5, paragraaf 5).

Inschatting uit de review: een dag of twee werk, ruim binnen de deadline van
18 november 2026 23:59 PT.

## 8. Status na batch 2 (7 november, Claude Code)

Uitgevoerd in de generators (`sketch_model.py`, `opzet_report.py`, `opzet-layout.json`), gerenderd in Desktop
en vastgelegd in `project/deliverables/screenshots/2026-11-07-desktop-batch2/`. De eigen review per punt, met het
screenshot dat het laat zien: `SELF-REVIEW.md` in die map. Een onafhankelijke review van batch 2 (K6) moet nog.

| Punt | Status | Kort |
|---|---|---|
| K1 | gedaan | A, B en C zijn vaste pakketten (`Package[Preset]`, regels op Expected); `04-p2-build-method.md` bijgewerkt |
| F1 | gedaan | B in Low heeft een pakket (01+09+10, -$6,9M); Plan Risk bewaakt tegen een leeg pakket |
| F2 | gedaan | "Fund one package of three moves"; kiosk-zin; nieuwe not-funded-reden; ondertitel buiten Expected; `06` bijgewerkt |
| F3 | gedaan | C is overal 01+07+10, Low -$34,8M |
| F4 | gedaan | capex tot op $10K, delen afgerond tot ze optellen (largest remainder), folio en KPI-delta uit getoonde waarden; afwegingen in SELF-REVIEW N1 |
| F5 | deels | kaarten, KPI's en tabellen zijn DAX-tekst; grafieklabels en "Totaal" volgen de locale; P2W-test beslist (N2) |
| F6 | gedaan | hover- en press-states op beide knoppen, themakleuren |
| F7 | gedaan | "... pays the middleman, and its welcome is fading." |
| R1 | gedaan | lichte wolk, A/B/C bovenop met letters (twee lagen, N3), x-as tot $62M, geen hangende selectie |
| R2 | gedaan | jaren, nullijn, gelabelde lijnen, scenario in beeld in framboos |
| R3 | gedaan | namen in plaats van codes; dropdown alleen A/B/C; Included / Excluded onder B en C |
| R4 | open | minimum nog 10 pt |
| R5 | gedaan | regelregel op de landing en een Type-kolom |
| R6 | open | P2W-test door Björn; visual-header-iconen stonden al uit (`pbir_lib.vco`), de iconen op de screenshots zijn Desktop-bewerkmodus |
| S1, S10 | open | tegels nog standaard; de twee vragen (welke 20 hotels, waarvoor $50,6M) niet beantwoord |
| S3, S11 | deels | zie SELF-REVIEW |
| S2, S4-S9 | gedaan | zie SELF-REVIEW |
| Nieuw | gedaan | schakelaar "All packages / Zoom on A, B, C" op de scatter (Björn, 7 nov), native, standaard alles |
