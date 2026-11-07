# 2026-11-07 - Screenshot-review v2: 29 Desktop-renders, volledige bevindingen

**Type:** scout/review-log - **Aanleiding:** Bjorn ("Er staan 29 screenshots in de
deliverables map inclusief bevindingen. Kun jij de bevindingen en de screenshots
analyseren en feedback geven waar gaatjes zitten of kansen liggen?") -
**Werkinstructie:** `project/project-state/active/07-fixgids-review-v2.md`.

## Wat beoordeeld is

- 29 renders in `project/deliverables/screenshots/2026-11-07-desktop/` op branch
  `upgrade-opzet-v2` (PR #5): 16 vaste states (01-16) en 13 echte kliks
  (L1a-L4c), gerenderd door Power BI Desktop zelf op 1920 x 1080. Geen
  HTML-schetsen meer.
- De onafhankelijke beeldenreview in dezelfde map (`REVIEW.md`: 1 blocker,
  11 major, 11 minor, 10 polish), geschreven door een reviewer die alleen de
  beelden zag; haar databevindingen zijn daarna tegen het model geverifieerd
  (kader bovenin REVIEW.md).
- Eigen visuele inspectie van o.a. 01, 02, 03, 07, 08, 11, 12, 13, 14, 15, 16,
  L3a, L3c en L4a, vergeleken met de goedgekeurde comp in
  `project/design-prototypes/reference_screenshots/`.
- Alle data-afhankelijke bevindingen onafhankelijk nagerekend tegen
  `project/analysis/output/packages.csv` en `project_yearly.csv`.

## Kernoordeel

Dit is een echte stap. De musts van 6 november zijn aantoonbaar gedaan: het
rapport draait in Desktop, de focuswissel en de scenariowissel zijn met echte
kliks vastgelegd, er is herkenbaar een aanbeveling (A), en de horizon-aanname
staat zichtbaar in de ondertitel ("nothing after 2032 is counted"). Toch nog niet
inleverklaar: twee onafhankelijke reviews komen op dezelfde kern uit. De
openingsstates zijn sterk, maar wie klikt (en een jurylid klikt) vindt binnen een
minuut een kapotte state, verschillende cijfers voor hetzelfde ding en een titel
die zijn eigen paneel tegenspreekt.

## Cijfers kloppen (nagerekend)

456 pakketten; positief tot 2032: 6 in Expected, 0 in Low, 57 in High.
A = 01+02+10: $9.4M capex, NPV +$3.3M, range -5.5 tot +12.7, run-rate $3.5M,
terugverdiening 2031 (Expected), 2029 (High), na 2032 (Low). B = 01+09+10:
$11.7M, +$2.7M. C = 01+07+10: $36.9M, -$23.4M. Het $60M-pakket kost exact $60.0M
(de tabel toont 60.1 door afronding van delen). A voldoet aan de growth-regel
(booking app en revenue management tellen als growth). De getoonde cijfers zijn
dus betrouwbaar; de problemen zitten in presentatie en randgevallen, niet in de
rekenkern.

## Aantoonbare fouten (7)

| # | Wat | Waar te zien | Waarom het ertoe doet | REVIEW |
|---|---|---|---|---|
| 1 | B in Low geeft een kapotte planpagina met een valse zin. Lege waterfall, alles "Not funded", en de risicoregel beweert: cumulatief positief in 2027, terwijl niets gefinancierd is | 15 (via 14: kies B, klik Low) | In twee kliks bereikbaar. Een verzonnen terugverdienjaar ondermijnt vertrouwen in elk ander getal | B1 |
| 2 | De titel "Fund the three moves that pay" wordt weersproken door het eigen paneel: de kiosks hebben NPV -$0.6M en betalen nooit terug tot 2032 | alle P2-states; waterfall in 08-10 | De sterkere, ware versie is: het pakket betaalt; de kiosks zijn het goedkoopste antwoord op F3 | M3 |
| 3 | "C" heeft twee verschillende Low-NPV's: -$34.8M in het plan, -$34.5M op de landing. B en C zijn regels, geen vaste pakketten, dus de samenstelling verschuift per scenario | 12 vs 16 en 03 | Leest als een rekenfout bij iedereen die de scenarioknop test | M6 |
| 4 | Afronding: delen tellen niet op tot totalen. Het $60M-pakket toont 60.1 in de capex-kolom; waterfall B telt 2.8 terwijl het totaal 2.7 zegt; F2 cent-verschillen; F1 2.8 pt vs KPI -2.7 pt | 13, 11; ook 01 | Juryleden rekenen tabellen na. Onderliggend klopt alles; het is puur weergave | M8 |
| 5 | Twee getalformaten door elkaar (nl-NL visual vs en-US DAX): "1.180 rooms refreshed" boven "15% of 1,180 rooms" | 12, 16; overal op P1/P2 | Verandert op die plek de betekenis; na Publish to Web ziet elke niet-en-US jury dit | M7 |
| 6 | De Back-knop verliest zijn label bij hover (donker op donker, contrast 1.4:1) | L3c, L4b | Het is de enige weg terug; iedereen hovert erover | M1 |
| 7 | P1-titel overclaimt: "is losing its guests", terwijl occupancy best-of-4 is en F3 zelf zegt "age costs loyalty, not yet rooms" | 01 | De headline wordt als eerste geciteerd; hij moet zijn eigen bewijs overleven | M4 |

## Risico's (geen fout, wel zichtbaar voor een jury)

- **Scatter:** de grijze wolk is 3x zo zwaar als in het goedgekeurde ontwerp; B en
  C verdwijnen eronder, de $60M-focusdot wordt aan de rand doormidden gesneden,
  en een aangeklikte selectie blijft hangen en wist de kleurcodering
  (02-07, 14, 16, L3b, L4a; REVIEW M2, m7).
- **Cumulatieve grafiek** zonder jaartallen kan de payback-claims uit de
  risicoregel niet tonen (08-13; M9).
- **"Funded" onder niet-aanbevolen pakketten** en interne codes ("01+07+10 in
  focus") in headers en dropdown (11-16, L3a; M5).
- **Leesbaarheid op 1366 breed:** bijna alle secundaire tekst wordt circa 9 px (M10).
- **Compliance is onzichtbaar:** nergens staat welk initiatief de growth-eis dekt;
  de tabel toont geen type (M11).
- **Publish to Web is nog niet getest;** pas daarna zijn locale-gedrag en
  hover-iconen definitief.

## Smaak en afwerking

Standaard grijze scenario-tiles in plaats van de pills uit het ontwerp; afgekapte
dropdown-labels; sorteerpijltjes, uitlijning en ontbrekende vetregel in tabellen;
F2-legenda met drie identieke grijze stippen; F3 zonder nul-lijn; ops-tiles die
"0 rooms added" tonen; het logo dat tussen P1 en P2 van gezicht wisselt. Allemaal
minor, allemaal zichtbaar. (Het wisselende logo is een bewuste brandkit-keuze:
slapend op P1, wakker op P2.)

## Kansen

1. **Vries A, B en C als vaste initiatiefsets (gedefinieerd op Expected).** Een
   ingreep lost de kapotte B-Low-state, de schuivende B/C-cijfers en de
   -34.8/-34.5-inconsistentie tegelijk op. Past bij "investor deck, geen
   playground".
2. **Snijden levert meer op dan toevoegen:** beperk de dropdown tot A, B, C
   (+ eventueel het volle $60M-pakket), verberg ops-tiles die nul zijn, en toon in
   de tabel alleen de gefundeerde rijen plus de dichtstbijzijnde missers.
3. **De dim-toestand van L4a bewijst hoe rustig een lichtere scatter oogt.** Terug
   naar de comp-stijl (kleinere, lichtere stippen, highlights bovenop met labels)
   is goedkoop en het verschil is groot.
4. **Doe de fixes in de generator (`project/tools/sketch_model.py` voor model en
   measures, `project/tools/opzet_report.py` voor het rapport), niet handmatig in
   Desktop.** Anders verdwijnen ze bij de volgende rebuild.
5. **Test Publish to Web nu al,** niet vlak voor de deadline: de wedstrijd vereist
   het en alleen dan zie je het echte locale- en hovergedrag.
6. **Herhaal deze render-en-reviewcyclus na de fixes;** hij vond met 29 plaatjes
   1 blocker en 11 majors zonder dat iemand het rapport hoefde te openen.

## Afweging van de bevindingen in REVIEW.md

De data-afhankelijke bevindingen zijn onafhankelijk nagerekend en kloppen (B is
leeg in Low; B/C zijn dynamisch; kiosks -$0.6M; $60M exact; de growth-correctie
op M11 is terecht). Strenger dan de review: fout 1, 2 en 3 hierboven zijn voor een
data-jury dealbreakers, geen majors. Milder: de 9px-leesbaarheid (M10) is reeel
maar secundair als de jury op 1920 kijkt. Niet meegenomen als fout: het wisselende
logo (bewuste brandkit-keuze, REVIEW p1).

## Volgorde tot 18 november

1. A/B/C bevriezen + alle plan-measures bewaken tegen een leeg pakket.
2. Back-hover.
3. Woorden waar maken: P2-titel en not-funded-reden, P1-titel, namen in plaats
   van codes, "In package" in plaats van "Funded".
4. Scatter naar comp-stijl.
5. Een getalvorm (en-US) en totalen die kloppen met hun delen.
6. Daarna pas polish.

Een dag of twee werk, ruim binnen de deadline (18 november 2026 23:59 PT).

**Bewerking repo:** deze review heeft niets aan de repo gewijzigd. De screenshots
en REVIEW.md staan op branch `upgrade-opzet-v2` (PR #5), nog niet op main;
PR #2 staat ook nog open.
