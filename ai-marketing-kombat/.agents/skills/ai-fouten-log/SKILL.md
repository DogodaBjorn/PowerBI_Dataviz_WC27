---
name: ai-fouten-log
description: Houdt tijdens een ronde bij welke AI-fouten we vingen en schrijft aan het eind de sectie "How we worked" (max 5 regels, minstens één gevangen AI-fout). Gebruik bij "log deze fout", "AI zat fout", "how we worked", "werkwijze", of aan het eind van een ronde.
---

# AI-fouten-log en "How we worked"

## Tijdens de ronde
Elke keer dat een AI (Codex, ChatGPT, een creatortool) iets fout heeft en wij het vangen, één regel in `rondes/<ronde>/ai-fouten.md`:
`- [tijd] [welke AI] zei: … | Werkelijk: … | Gevangen door: [zelf rekenen / beeld bekeken / brief herlezen / tweede AI] | Gevolg: …`

Soorten fouten die terugkomen:
- Beeld verkeerd beschrijven zonder het te zien.
- Een winnaar kiezen op onmogelijke data.
- Woorden die net buiten de merkregel vallen ("choose your ride" vs "choose your driver").
- Formaten of veldwaarden die het template niet kent.
- Getallen die niet optellen of verkeerd afgerond zijn.
- Verzonnen bronnen of cijfers.

## Aan het eind: How we worked (Engels, max 5 regels)
Begin bij `HOW-WE-WORKED.md`: daar staan de vaste regels over de voorbereiding (toolkit, panel, compliance-check) en een voorbeeld van 5 regels. Vul aan met wat er in deze ronde echt gebeurde; schrap wat we niet gebruikten.

1. Welke tools wat deden (Codex + welke MCP, ChatGPT, Codex Design), met wat het opleverde dat anders niet kon.
2. Hoe we samenvoegden (twee AI's, wie won op welk punt).
3-5. Gevangen fouten: "Caught and fixed: [AI] [fout]; [wat het bewijs liet zien]; [wat we deden]."

## Na de ronde
Werk `lessons/<ronde>.md` bij: wat werkte, wat beter moet, nieuwe jury-patronen. Commit.
