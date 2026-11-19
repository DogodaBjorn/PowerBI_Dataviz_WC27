---
name: advertentieteksten
description: Schrijft advertentieteksten en varianten per platform binnen de tekenlimieten (Meta, Google RSA/PMax/Demand Gen, TikTok, LinkedIn, Pinterest), met de USP in de kop en een testmatrix. Gebruik bij "ad copy", "advertentieteksten", "headlines", "varianten", "RSA", "primary text".
---

# Advertentieteksten per platform

## Werkwijze
1. Neem uit de hypothese: persona, USP-prikkel, situatie, toegestane boodschap, verboden woorden (`regels.md`).
2. Schrijf per platform binnen de specs uit `knowledge/platforms/<platform>.md` (sectie Ad specs). Limieten met [CHECK] daar: houd marge aan.
3. Varieer één ding tegelijk, zodat de test iets leert: invalshoek (pijn, voordeel, situatie, sociaal bewijs), taal/register, CTA.
4. Draai `scripts/woordcheck.py` en tel de tekens na (script hieronder).

## Regels
- USP in de kop, situatie in het beeld. Kop zonder USP verloor in ronde 1 (NG-17).
- Eén belofte per advertentie; geen claims die de brief niet toestaat.
- Lokale taal/register als de brief dat ondersteunt (Pidgin won in ronde 1), en test het tegen Engels binnen hetzelfde kanaal.
- Google RSA: koppen die elk los kunnen staan; pin alleen wat moet (merk, verplichte zin).
- TikTok/Reels: de tekst op het scherm doet het werk, de caption is ondersteuning.
- Luxe: rust, geen uitroeptekens, geen prijs- of kortingstaal; zie `luxe-merkpoort`.

## Output
Tabel per platform: veld · variant A · B · C · tekens. Daaronder de testmatrix: wat verschilt er tussen A, B en C en welke KPI beslist.

Tekens tellen:
```
python -I -c "import sys; [print(len(l.rstrip('\n')), l.rstrip()) for l in open(sys.argv[1], encoding='utf-8')]" teksten.txt
```
