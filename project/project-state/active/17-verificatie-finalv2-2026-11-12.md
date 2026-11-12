# 17 - Verificatie FinalV2, 12 november 2026

**Bekeken:** `main` op `c8d13c6` (FinalV2-build `f4a487d`, gemerged via PR #13). Toets: bouwplan 15 en review 14. Alle 15 Desktop-PNG's uit `project/deliverables/screenshots/ScreenshotsFinalV2/` zijn visueel bekeken, inclusief detailuitsneden waar nodig. De bouwlog en README zijn als toelichting gebruikt, niet als bewijs dat een visuele fix werkt.

## Oordeel

De Desktop-uitwerking is grotendeels goed en staat op main. De twee belangrijkste visuele fixes zijn geslaagd: de pakketbereikbalk op A en C leest zonder botsingen, en de hanger is in de volledige achtergrond-jpg verplaatst, zonder overlay. De masthead is vrij; de F-chips staan in de footer. De generators reproduceren de gecommitte uitwerking.

**Nog geen finale vrijgave:** de Publish-to-Web-poort is niet gedaan. De gevulde en over-budget-renders bewijzen de cijfers en waterval, maar niet de werkende selectie en selector-voetregel. In de gevulde waterval blijft bovendien een categorienaam afgekapt.

Statussen: **DONE** = zichtbaar of onafhankelijk technisch gecontroleerd; **NOT DONE** = vereist resultaat ontbreekt; **CANNOT VERIFY** = bewijs ontbreekt of bewijst de gevraagde werking niet. DONE op een Desktop-fix betekent niet dat de browserpoort al geslaagd is.

## Per bouwplanpunt

Rendernummers hieronder verwijzen naar de bestanden in `ScreenshotsFinalV2/`; de README koppelt de nummers aan de volledige bestandsnamen.

| Punt | Status | Bewijs en oordeel |
|---|---|---|
| M1 - bereikbalk pakket-tooltip | DONE | `16_tt-package-A.png`, `17_tt-package-C.png`: A boven, B onder de band; Low/High op een aparte rij. Letters, stip en bereiklabels botsen niet meer. De implementatie gebruikt 72 px hoogte in plaats van de aanvankelijk genoemde 56; dat levert het bedoelde resultaat. |
| M2 - hanger/achtergrond en chips | DONE | `01`, `02`: masthead niet door het hangergat; hanger vrij in P2-banner; vier leesbare chips in footer naast bronregel. Technisch: `brand_canvas_v3.py` verplaatst het masker van y -150 naar -56 (94 px omlaag, niet 50); de volledige `canvas-night.jpg` is gewijzigd en bytegelijk aan het registered resource. P1/P2 gebruiken die jpg als Fit-achtergrond. Geen `z_canvas`-visual; `SCENE_VISUAL` blijft False. De extra verplaatsing en de aangepaste chipkleuren/hoogtepositie zijn in doc 16 gemotiveerd en werken in de renders. Tooltip-bindingen van de chips staan nog op tt-f1 t/m tt-f4; de daadwerkelijke hover vanaf elke footerchip is niet in deze set vastgelegd. |
| M3 - notatie | CANNOT VERIFY | De besloten aanpak (mix accepteren en in browser toetsen) is vastgelegd. `01`, `12`, `14`, `15` tonen nog de verwachte nl-NL-native labels naast en-US-tekst. Dat is volgens het plan geen nieuwe conversieklus. De vereiste en-US-browsercontrole en nl-NL-browserrender `26` ontbreken nog. Een aanname over de browser-locale is geen geslaagde test. |
| M4 - Publish-to-Web-poort | NOT DONE | Geen van `20` t/m `28` aanwezig; README meldt expliciet NOT RENDERED. Geen live schaal-, placement-, Deneb-klik-, zoom-, Mac-font- of toetsenbordcontrole aangetoond. Uiterlijk 17 november uitvoeren zoals plan 15 voorschrijft. |
| M5 - route naar main | DONE | PR's #2, #5, #8 en #11 live gesloten. FinalV1 via #12, FinalV2 via #13 naar main; GitHub toont #13 als merged en main bevat PBIP, V2-set en docs 13-16. De route gebruikte twee opeenvolgende PR's in plaats van één, maar het vereiste eindresultaat staat er. De koppeling met de gepubliceerde juryversie blijft onderdeel van M4. |
| S1 - F2-legenda | DONE | `01` en `11`: bovenlegenda, Goodnight Inn en "The other three brands"; geen naamloze lijn. De in het plan toegestane samenvoegvariant is gebruikt. |
| S2 - lege build-stand | DONE | `04`: "NPV range, $M" volledig zichtbaar; "Pick moves on the left; your plan appears here." boven de lege waterval. `05`: gevulde waterval aanwezig. De nulrest blijft staan zoals het plan toestaat. Werkende selector-interactie hiermee nog niet bewezen, zie hieronder. |
| S3 - detail-tooltipkleuren | DONE | `14`, `15`: Goodnight Inn-lijn en legendastip Coffee Blue; gehoverde band/hotel Night. |
| S4 - vergelijker-titel | DONE | `03`: "B ends within $1M of A by 2032; C never breaks even", consistent met de B-tegel die $0.6M lagere NPV noemt. |
| S5 - F1-beginjaar | DONE | `01`, `10`: "fell 2.8 points since 2023". |
| S6 - generator-pariteit | DONE | Onafhankelijke rebuild van `opzet_report.py --out` geeft geen semantische JSON-verschillen met het gecommitte rapport. Rebuild van `sketch_model.py` naar een tijdelijke map is bytegelijk aan het gecommitte model. Bjorns z/tab-volgorde staat in `opzet-layering.json` en wordt toegepast. Vergelijking met `1361f71`: 146 bestaande visualposities gelijk, 19 doelbewuste wijzigingen voor deze fixes; geen positieverschil tussen huidige generatoruitvoer en huidige PBIR. |
| N1 - selector-capexprecisie | DONE | `05`, `06`: één decimaal, onder meer $4.3M en $24.8M. De onderliggende tooltip-optelbedragen zijn niet naar dat formaat teruggebracht. |
| N2 - comparatorprecisie | DONE | `14`, `15`: geldbedragen in merkregel en KPI's beide op twee decimalen; percentages op één decimaal. Het zijn verschillende populaties, dus de bedragen hoeven niet gelijk te zijn. Komma/punt-verschil blijft M3. |
| N3 - jaartooltip-titel | DONE | `18`: "where the four options stand". |
| N4 - F3-nullijn | DONE | `01`, `12`: dunne Dusk-lijn; PBIR/generator stelt width 2 in. |
| N5 - verticale tooltipruimte | DONE | `10` t/m `12`: grafiek en noot verschoven; lay-out bevestigt +8 px voor beide. Geen botsingen of afgekapte noot in de originele pixels. Pakketkaart 2 blijft bewust top-aligned in `16`/`17`, zoals besloten. |
| N6 - room-nights-regel | DONE | `15`: segmentregel weg; geen visual meer voor `ttd_foot`. De kaart/pagina is verkort in plaats van de vrijgekomen ruimte te laten staan; visueel schoon. |

## Screenshotopdracht: bestanden compleet, functioneel bewijs deels open

**15 van 15 expliciet benoemde Desktop-bestanden aanwezig**, plus README: `01`-`06`, `10`-`18`. De eerdere omschrijving "18 Desktop-renders" was een telfout: de tabel in plan 15 benoemt er 15. Er ontbreken dus geen drie onbenoemde Desktop-bestanden.

**0 van 9 Publish-to-Web-bestanden aanwezig** (`20`-`28`). Ook de service-toetsenbordalinea beschrijft nog een niet-uitgevoerde test, geen geslaagde ronde.

### CANNOT VERIFY - echte klik en selector-voetregel

In `05` toont de tegel drie zetten en $13.2M capex, maar alle selectorrondjes zijn leeg en de selector-voetregel zegt "Nothing picked yet". In `06` toont de tegel $69.25M en een correcte oranje overschrijdingsband van $9.25M, maar dezelfde selector-voetregel blijft "Nothing picked yet". De README legt dit eerlijk uit: tijdelijke filters sturen de bouwvisuals, niet de selector zelf.

Deze renders bewijzen dus **wel** de gevulde waterval, regelzin en budgetband, maar **niet** dat een klik de hele keten aanstuurt of dat de selector-voetregel bij overbudget klopt. Geen bewijs dat de echte selector defect is; evenmin bewijs dat hij werkt.

**Vervolg:** maak `05` en `06` opnieuw na echte klikken in de selector, met geselecteerde rondjes en bijbehorende voetregel in beeld. Doe ook `22` in de service. Gebruik geen losse visualfilters als vervanging voor dit interactiebewijs.

### NOT DONE - leesbare categorienaam in gevulde waterval (open punt uit review 14/doc 13)

`05` toont **"Revenue managem..."**. De gevulde staat maakt het eerder onverifieerde afkappunt nu zichtbaar. De cijfers en drie balken zijn er, maar de categorienaam is niet volledig leesbaar.

**Vervolg:** geef alleen de zichtbare korte naam in de bouw-waterval een kortere, volledige tekst (bijvoorbeeld "Revenue mgmt") of meer labelruimte; behoud de volledige projectnaam in de selector en tooltip. Render de gevulde staat opnieuw en controleer dat alle drie de namen zonder ellips leesbaar zijn.

## Onafhankelijke technische controles

- `validate_tmdl.py --strict`: 34 bestanden, 0 fouten, 0 waarschuwingen.
- `a11y_check.py`: 0 fouten, 0 notities.
- `schema_check.py`: 183 JSON-bestanden, 0 falend.
- Rapportrebuild: geen semantische JSON-verschillen; modelrebuild: geen byteverschillen.

Dit zijn statische controles. Ze vervangen geen Desktop-kliktest, service-render, toetsenbordronde of fontcontrole. De bredere Microsoft-validator is hier niet opnieuw gedraaid; doc 16 meldt daarvoor nog een bekende fout en waarschuwingen, dus deze verificatie claimt geen volledige validatorvrijgave.

## Wat nu nog moet

1. Watervalnaam in `05` leesbaar maken en `05`/`06` vastleggen na echte selector-klikken, inclusief voetregel.
2. Publish-to-Web-poort uitvoeren en alle negen browserrenders plus toetsenborduitkomst vastleggen. Daarmee M3/M4 en het service-interactiebewijs sluiten.
3. Publicatie laten overeenkomen met de geverifieerde main-staat. README/bouwlog-status daarna bijwerken.

Er is ook een open **PR #14**, alleen voor een aanvulling op doc 16 over een Desktop-save-incident. Dat is niet hetzelfde als nog ongemergde FinalV2-code: de FinalV2-code en screenshots staan al op main. In deze verificatie is geen rapportcode of bestaand screenshot gewijzigd.

## Bronnen

- [Bouwplan 15](15-bouwplan-finalv2-2026-11-12.md), [review 14](14-review-finalv2-2026-11-12.md), [bouwlog 16](16-finalv2-bouwlog-2026-11-12.md).
- [Desktop-renders en README](../../deliverables/screenshots/ScreenshotsFinalV2/).
- [FinalV2 PR #13](https://github.com/DogodaBjorn/PowerBI_Dataviz_WC27/pull/13), [FinalV1 PR #12](https://github.com/DogodaBjorn/PowerBI_Dataviz_WC27/pull/12).
- Gesloten oude PR's: [#2](https://github.com/DogodaBjorn/PowerBI_Dataviz_WC27/pull/2), [#5](https://github.com/DogodaBjorn/PowerBI_Dataviz_WC27/pull/5), [#8](https://github.com/DogodaBjorn/PowerBI_Dataviz_WC27/pull/8), [#11](https://github.com/DogodaBjorn/PowerBI_Dataviz_WC27/pull/11). Documentatie-aanvulling: [#14](https://github.com/DogodaBjorn/PowerBI_Dataviz_WC27/pull/14).
