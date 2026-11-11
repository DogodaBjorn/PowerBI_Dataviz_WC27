"""Validate PBIR JSON files against their declared $schema (research-first rule, done by machine).

usage:  python project/tools/schema_check.py FILE [FILE ...]
        SCHEMA_CACHE=<dir> to reuse downloaded schemas (default /tmp/schemacache)
Each file's $schema (developer.microsoft.com/json-schemas/...) is fetched from Microsoft's public
mirror github.com/microsoft/json-schemas (raw.githubusercontent.com), with every $ref resolved the
same way. Requires `pip install jsonschema`. It checks containers, queries, filters, bookmarks and
pages; visual-specific formatting objects are loosely typed in the schema, so a pass there is
necessary, not sufficient: Desktop remains the final check.
"""
import json, sys, urllib.request, pathlib, os, hashlib
from jsonschema import Draft7Validator, Draft202012Validator
from referencing import Registry, Resource
CACHE = pathlib.Path(os.environ.get("SCHEMA_CACHE", "/tmp/schemacache")); CACHE.mkdir(exist_ok=True)
def fetch(uri):
    raw = uri.replace("https://developer.microsoft.com/json-schemas/", "https://raw.githubusercontent.com/microsoft/json-schemas/main/")
    f = CACHE / (hashlib.sha1(raw.encode()).hexdigest() + ".json")  # stable key: hash() is salted per process, so the cache never hit across runs
    if not f.exists():
        f.write_bytes(urllib.request.urlopen(raw).read())
    return json.loads(f.read_text(encoding="utf-8"))
def retrieve(uri):
    return Resource.from_contents(fetch(uri))
reg = Registry(retrieve=retrieve)
bad = 0; n = 0
for p in sys.argv[1:]:
    d = json.loads(pathlib.Path(p).read_text(encoding="utf-8")); s = d.get("$schema")
    if not s: continue
    sch = fetch(s); n += 1
    V = Draft202012Validator if "2020-12" in sch.get("$schema", "") else Draft7Validator
    errs = sorted(V(sch, registry=reg).iter_errors(d), key=lambda e: list(e.path))
    if errs:
        bad += 1; print("FAIL", p)
        for e in errs[:6]: print("   ", "/".join(map(str, e.path)), "->", e.message[:220])
print(f"schema_check: {n} files, {bad} failing")
