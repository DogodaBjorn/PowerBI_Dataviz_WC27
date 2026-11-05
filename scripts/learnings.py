"""Per-client learnings memory: append-only JSONL under project-state.

Usage:
    python scripts/learnings.py add --type TYPE --key KEY --insight TEXT
                                    [--confidence N] [--source SRC] [--supersedes KEY]
    python scripts/learnings.py search [--key TEXT] [--type TYPE] [--all]

Types: pitfall | preference | decision | taste.

Entries append to project/project-state/learnings.jsonl — one project
instance, one memory; never read across clients. Append-only: correct an
entry by appending a new one with --supersedes <key>, never by editing.
Search hides superseded entries and shows the latest entry per (type, key)
unless --all; --key matches a substring of the key or the insight.
"""

import json
import os
import sys
from datetime import datetime, timezone

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TYPES = {"pitfall", "preference", "decision", "taste"}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEARNINGS = os.path.join(ROOT, "project", "project-state", "learnings.jsonl")


def opt(argv, flag):
    return argv[argv.index(flag) + 1] if flag in argv[:-1] else None


def load():
    entries = []
    if os.path.isfile(LEARNINGS):
        with open(LEARNINGS, encoding="utf-8") as handle:
            for lineno, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    print(f"WARNING: line {lineno} is not valid JSON - skipped")
    return entries


def add(argv):
    kind, key, insight = opt(argv, "--type"), opt(argv, "--key"), opt(argv, "--insight")
    if kind not in TYPES or not key or not insight:
        print(f"add requires --type {{{'|'.join(sorted(TYPES))}}}, --key, --insight")
        return 1
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "type": kind,
        "key": key,
        "insight": insight,
        "confidence": int(opt(argv, "--confidence") or 7),
        "source": opt(argv, "--source") or "session",
    }
    if opt(argv, "--supersedes"):
        entry["supersedes"] = opt(argv, "--supersedes")
    os.makedirs(os.path.dirname(LEARNINGS), exist_ok=True)
    with open(LEARNINGS, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"recorded {kind} '{key}' -> {os.path.relpath(LEARNINGS, ROOT)}")
    return 0


def search(argv):
    entries = load()
    if not entries:
        print("no learnings recorded yet")
        return 0
    if "--all" not in argv:
        superseded = {e["supersedes"] for e in entries if e.get("supersedes")}
        latest = {}
        for e in entries:  # later lines win per (type, key)
            latest[(e.get("type"), e.get("key"))] = e
        entries = [
            e for e in latest.values()
            if e.get("key") not in superseded or e.get("supersedes")
        ]
    kind, key = opt(argv, "--type"), (opt(argv, "--key") or "").lower()
    hits = [
        e for e in entries
        if (not kind or e.get("type") == kind)
        and (not key or key in str(e.get("key", "")).lower()
             or key in str(e.get("insight", "")).lower())
    ]
    for e in sorted(hits, key=lambda e: e.get("ts", "")):
        print(f"[{e.get('type')}] {e.get('key')}: {e.get('insight')} "
              f"(confidence {e.get('confidence')}, {e.get('source')}, "
              f"{str(e.get('ts', ''))[:10]})")
    print(f"{len(hits)} matching learning(s)")
    return 0


def main(argv):
    if argv[:1] == ["add"]:
        return add(argv[1:])
    if argv[:1] == ["search"]:
        return search(argv[1:])
    print(__doc__.strip())
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
