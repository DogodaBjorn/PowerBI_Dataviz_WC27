# Web2Wave en Runway laten samenwerken

Uitgezocht op 2026-10-23 uit de Web2Wave-docs (docs.web2wave.com, MCP-server en API-referentie) en de tooldefinities van de Runway-MCP. Nog niet getest: de Web2Wave-MCP is nog niet aangesloten.

Afspraak: eerst het Web2Wave-tegoed opmaken, Runway/Gemini pas na overleg met Bjorn (zie memory `web2wave-credits-eerst`).

## Van Web2Wave naar Runway

| Wat uit Web2Wave | Hoe Runway het gebruikt |
|---|---|
| Doelgroepen, angles, hooks, `exact_copy`, `brand_hex` (case log) | Gaan als tekst in de Runway-prompt, zodat de video dezelfde belofte en kleur heeft als de statics. |
| Gegenereerde static (URL uit `web2wave_creatives_get_rework`) | Als `startFrame.url` in Runway `generate_video`: de goedgekeurde static wordt de eerste frame van een video. Goedkoopste route naar video die bij de static past. Vooraf checken dat de URL publiek is. |
| Meerdere statics van één doelgroep | Als `referenceImages` (stijl- en onderwerpreferentie) of als `firstSceneImage` in `generate_multishot_video`. |
| Quiz-screenshot (`web2wave_render_quiz_screen`) | Als referentie voor beeldtaal, zodat advertentie en funnel op elkaar lijken. |
| Winnende concurrentadvertentie (`web2wave_creatives_get_ad`) | Alleen het patroon (hook, opbouw, tempo) in de prompt beschrijven. Niet als referentiebeeld invoeren: dan kopieer je de creative. |

## Van Runway (of Gemini) naar Web2Wave

| Doel | Route | Via MCP? |
|---|---|---|
| Beeld of video in de quiz of paywall | Bestand uploaden met de API `POST https://api.web2wave.com/api/project-files/upload` (multipart, veld `file`, optioneel `path`, header `api_key`, max 100 MB). Geeft een publieke `url` terug. Die URL gaat in het `src` van een Image- of Video-blok of als achtergrond van een scherm. | Nee, met curl. De skill noemt geen MCP-tool hiervoor. |
| Eigen beeld als referentie voor een Web2Wave-generatie | `POST /creatives/generate` als multipart met `assets[]` (referentiebestanden). Kost wel Web2Wave-tegoed. | Nee: de MCP-tool kan geen bestanden meesturen. Wel met curl op de API. |
| Runway-video als officiële Web2Wave-creative | Kan niet: er is geen endpoint om kant-en-klare creatives te importeren. Runway-output blijft een losse link in de case log en de samenvatting. | — |

Een Runway-URL kan misschien direct in een quizblok, maar de links van Runway zijn ondertekend en kunnen verlopen. Voor een funnel die moet blijven werken altijd eerst uploaden naar Web2Wave.

## Wat nodig is

- Web2Wave-API-key (Cabinet → Project Settings → API, één key per project). MCP-adres: `https://mcp.web2wave.com/mcp`, header `Authorization: Bearer <key>`. Voor de uploads met curl dezelfde key, maar in de header `api_key`.
- Key nooit in een bestand in de repo of in de chat-output zetten.
- Runway: al verbonden. Video vraagt een betaald Runway-abonnement; `show_plans_and_credits` laat het saldo zien.

## Open punten bij aansluiten

1. Zijn de beeld-URL's in `get_rework` publiek (nodig voor Runway `startFrame`)?
2. Heeft de MCP toch een uploadtool (`web2wave_*upload*`)? Na het aansluiten de toollijst checken.
3. Welke velden heeft het Image- en Video-blok precies? Opvragen met `web2wave_describe_block`.
