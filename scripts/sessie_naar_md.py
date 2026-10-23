"""Zet een Claude Code-sessie (.jsonl) om naar een leesbare werklog in Markdown.

Gebruik: python scripts/sessie_naar_md.py <sessie.jsonl> <uit.md>
Neemt op: prompts van de gebruiker, tekstantwoorden van het model, en per toolaanroep
de toolnaam met een korte samenvatting van de invoer. Geen thinking, geen tool-output.
"""
import json
import sys


def kort(waarde, n=160):
    tekst = json.dumps(waarde, ensure_ascii=False) if not isinstance(waarde, str) else waarde
    tekst = " ".join(tekst.split())
    return tekst if len(tekst) <= n else tekst[:n] + " ..."


def tool_regel(blok):
    naam = blok.get("name", "?")
    inv = blok.get("input", {}) or {}
    for sleutel in ("description", "skill", "query", "search_terms", "file_path", "command", "prompt"):
        if sleutel in inv:
            return f"- tool `{naam}`: {kort(inv[sleutel])}"
    return f"- tool `{naam}`"


def main(pad_in, pad_uit):
    regels = ["# Work log (exported from the Claude Code session)", ""]
    with open(pad_in, encoding="utf-8") as f:
        for lijn in f:
            d = json.loads(lijn)
            if d.get("isSidechain") or d.get("type") not in ("user", "assistant"):
                continue
            inhoud = (d.get("message") or {}).get("content")
            tijd = (d.get("timestamp") or "")[11:16]
            if d["type"] == "user":
                if d.get("isMeta") or not isinstance(inhoud, (list, str)):
                    continue
                if isinstance(inhoud, str):
                    inhoud = [{"type": "text", "text": inhoud}]
                teksten = [b.get("text", "") for b in inhoud if b.get("type") == "text"]
                docs = [b for b in inhoud if b.get("type") == "document"]
                if docs:
                    regels += [f"## {tijd} UTC · User", "", "[attached: brief PDF]", ""]
                tekst = "\n".join(t for t in teksten if t and not t.startswith("<system-reminder>")).strip()
                if tekst:
                    regels += [f"## {tijd} UTC · User", "", tekst, ""]
            else:
                for b in inhoud or []:
                    if b.get("type") == "text" and b.get("text", "").strip():
                        regels += [f"**Model ({tijd} UTC):**", "", b["text"].strip(), ""]
                    elif b.get("type") == "tool_use":
                        regels.append(tool_regel(b))
                regels.append("")
    with open(pad_uit, "w", encoding="utf-8") as f:
        f.write("\n".join(regels))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
