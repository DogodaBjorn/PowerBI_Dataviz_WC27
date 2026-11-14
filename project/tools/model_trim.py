"""The column and table trim of the submission model (build step 12, Bjorn 14 Nov: "only what is used in the report").

`sketch_model.py --submission` first drops the measures and helper tables the report cannot reach (reachability(),
build step 11). This module then drops, from the TMDL just written:
  - every table nothing reads any more (also an organisers' table: GuestSegments, GuestComplaints, ...), with its
    relationships;
  - every column nothing reads: a source column leaves the table and its Power Query (Table.SelectColumns before
    the types), a calculated column leaves with its DAX, a column of a calculated table leaves through a
    SELECTCOLUMNS around the table's DAX that names the columns kept.

What "read" means (usage()): bound by the report (visuals, filters, bookmarks, formatting); an end of a relationship
between two tables that stay; the sort column of a column that stays; or named in DAX that stays (the measures, the
DAX of a calculated table that stays, the DAX of a calculated column that stays). A qualified name Table[Column]
counts for that table; a bare [Column] counts for every table with a column of that name that stays for another
reason (unless it is a measure's name). On the model of 14 Nov this gives exactly the engine's own answer (INFO.CALCDEPENDENCY from the report's
bindings: 124 of 190 columns, 25 of 29 tables), and never less: a rule that only reads names cannot miss a reader.
A table that is read by nothing still stays when it carries a filter between two tables that stay (the one side of
one relationship and the many side of another).

The script decides, not a list: usage() is also the gate (build_checks.py check 6: nothing unused left).
"""
import re
from pathlib import Path

BLOCK = re.compile(r"(?m)^\t(?=(?:///|column |partition |annotation |measure |hierarchy ))")
REF = re.compile(r"(?:'((?:[^']|'')+)'|\b([A-Za-z_]\w*))?\[([^\[\]]+)\]")
COL = re.compile(r"column ('(?:[^']|'')*'|[^\s=]+)( =)?")
REL = re.compile(r"relationship [^\n]+\n(?:\t[^\n]*\n)*?\tfromColumn: ([^\n]+)\n(?:\t[^\n]*\n)*?\ttoColumn: ([^\n]+)\n(?:\t[^\n]*\n)*")


def _name(s):
    return s[1:-1].replace("''", "'") if s.startswith("'") else s


def _end(s):
    """'Table'.'Column' of a relationship end -> (table, column)."""
    m = re.match(r"('(?:[^']|'')*'|[^.]+)\.(.+)$", s.strip())
    return _name(m.group(1)), _name(m.group(2).strip())


def blocks(text):
    """A table file as [head, block, ...]: a block is one column, partition, annotation or measure with the /// lines
    above it. Joined again they are the file."""
    parts = BLOCK.split(text)
    out, carry = [parts[0]], ""
    for p in parts[1:]:
        if p.startswith("///"):
            carry += "\t" + p
        else:
            out.append(carry + "\t" + p); carry = ""
    if carry:
        out.append(carry)
    return out


def _code(block):
    return "\n".join(ln for ln in block.splitlines() if not ln.lstrip().startswith("///")).lstrip("\t")


def read_model(definition):
    tables = {}
    for f in sorted((Path(definition) / "tables").glob("*.tmdl")):
        bl = blocks(f.read_text(encoding="utf-8"))
        cols, part = {}, ""
        for b in bl[1:]:
            code = _code(b)
            m = COL.match(code)
            if m:
                cols[_name(m.group(1))] = {"code": code, "calc": bool(m.group(2))}
            elif code.startswith("partition"):
                part = code
        tables[f.stem] = {"cols": cols, "partition": part, "calc": " = calculated" in (part.splitlines() or [""])[0]}
    rel_text = (Path(definition) / "relationships.tmdl").read_text(encoding="utf-8")
    rels = [(_end(m.group(1)), _end(m.group(2))) for m in REL.finditer(rel_text)]
    return tables, rels


def usage(definition, report_refs, measure_names, table_deps):
    """{"tables": kept table names, "columns": kept (table, column), "unused_tables": [...], "unused_columns": {t: [...]}}."""
    tables, rels = read_model(definition)

    maybe = set()  # bare [Column]: in whichever table of that name stays; it never makes a table stay

    def scan(text):
        out = set()
        for m in REF.finditer(text):
            t, c = (m.group(1) or m.group(2)), m.group(3)
            if t in tables:
                out.add((t, c))
            elif c not in measure_names:
                maybe.update((tt, c) for tt in tables if c in tables[tt]["cols"])
        return out

    used, used_t = set(), {"_Measures"}
    for kind, entity, prop in report_refs:
        assert entity in tables or kind == "Measure", f"the report binds {entity!r}[{prop}], which the model does not have"
        if entity in tables:
            used_t.add(entity)
            if kind == "Column":
                used.add((entity, prop))
    mfile = Path(definition) / "tables" / "_Measures.tmdl"
    mtext = "\n".join(ln for ln in mfile.read_text(encoding="utf-8").splitlines() if not ln.lstrip().startswith("///")) if mfile.exists() else ""
    used |= scan(mtext); used_t |= table_deps(mtext, set(tables))
    done_t, done_c = set(), set()
    while True:
        before = (len(used), len(used_t), len(maybe))
        used_t |= {t for t, c in used if t in tables}
        used |= {(t, c) for t, c in maybe if t in used_t}
        for t in sorted(used_t):
            if t in tables and t not in done_t and tables[t]["calc"]:
                done_t.add(t)
                used |= scan(tables[t]["partition"]); used_t |= table_deps(tables[t]["partition"], set(tables))
        for t, c in sorted(used):
            if t in tables and c in tables[t]["cols"] and (t, c) not in done_c:
                done_c.add((t, c))
                code = tables[t]["cols"][c]["code"]
                sb = re.search(r"sortByColumn: ('(?:[^']|'')*'|\S+)", code)
                if sb:
                    used.add((t, _name(sb.group(1))))
                if tables[t]["cols"][c]["calc"]:
                    used |= scan(code) | {(t, m.group(3)) for m in REF.finditer(code) if not (m.group(1) or m.group(2))}
                    used_t |= table_deps(code, set(tables))
        for (ft, fc), (tt, tc) in rels:
            if ft in used_t and tt in used_t:
                used |= {(ft, fc), (tt, tc)}
        # a table nothing reads, between two that stay: the many side of one relationship and the one side of another
        for t in tables:
            if t not in used_t and any(a[0] == t and b[0] in used_t for a, b in rels) and any(b[0] == t and a[0] in used_t for a, b in rels):
                used_t.add(t)
        if (len(used), len(used_t), len(maybe)) == before:
            break
    used = {(t, c) for t, c in used if t in tables and c in tables[t]["cols"]}
    kept_t = {t for t in tables if t in used_t}
    for t in kept_t:  # a key column stays with its table (the Date table's mark)
        used |= {(t, c) for c, v in tables[t]["cols"].items() if "isKey" in v["code"].split()}
    for t in kept_t:  # a table that stays keeps at least one column
        if tables[t]["cols"] and not any(tt == t for tt, _ in used):
            used.add((t, next(iter(tables[t]["cols"]))))
    return {"tables": kept_t, "columns": used, "unused_tables": sorted(set(tables) - kept_t),
            "unused_columns": {t: [c for c in tables[t]["cols"] if (t, c) not in used] for t in sorted(kept_t)
                               if any((t, c) not in used for c in tables[t]["cols"])}}


def _q(name):
    return name if re.fullmatch(r"[A-Za-z_]\w*", name) else "'" + name.replace("'", "''") + "'"


def trim(definition, report_refs, measure_names, table_deps):
    """Applies usage() to the TMDL in <definition>. Returns the usage dict of BEFORE the trim (what was dropped)."""
    definition = Path(definition)
    u = usage(definition, report_refs, measure_names, table_deps)
    tables, _ = read_model(definition)
    for t in u["unused_tables"]:
        (definition / "tables" / f"{t}.tmdl").unlink()
    gone = set(u["unused_tables"])
    # relationships and the model's table list
    rf = definition / "relationships.tmdl"
    text = rf.read_text(encoding="utf-8")
    keep = [m.group(0) for m in REL.finditer(text) if _end(m.group(1))[0] not in gone and _end(m.group(2))[0] not in gone]
    rf.write_text("\n".join(k.rstrip("\n") + "\n" for k in keep), encoding="utf-8", newline="\n")
    mf = definition / "model.tmdl"
    model = mf.read_text(encoding="utf-8")
    for t in gone:
        model = re.sub(r"(?m)^ref table " + re.escape(_q(t)) + r"\n", "", model)
        model = model.replace(f'"{t}",', "").replace(f',"{t}"', "")
    mf.write_text(model, encoding="utf-8", newline="\n")
    # columns
    for t, drop in u["unused_columns"].items():
        f = definition / "tables" / f"{t}.tmdl"
        bl = blocks(f.read_text(encoding="utf-8"))
        out = [bl[0]]
        kept = [c for c in tables[t]["cols"] if c not in drop]
        for b in bl[1:]:
            code = _code(b)
            m = COL.match(code)
            if m and _name(m.group(1)) in drop:
                continue
            if code.startswith("partition") and not tables[t]["calc"]:
                src = [c for c in kept if not tables[t]["cols"][c]["calc"]]
                typed = re.search(r"Typed = Table\.TransformColumnTypes\(Promoted, \{(.*)\}\)", b)
                assert typed, t
                pairs = [p for p in re.findall(r'\{"([^"]+)", ([^{}]+)\}', typed.group(1)) if p[0] in src]
                assert [p[0] for p in pairs] == src, (t, src)
                sel = "Selected = Table.SelectColumns(Promoted, {" + ", ".join(f'"{c}"' for c in src) + "}),"
                new = sel + "\n\t\t\t\t    Typed = Table.TransformColumnTypes(Selected, {" + ", ".join(f'{{"{c}", {ty}}}' for c, ty in pairs) + "})"
                b = b.replace(typed.group(0), new)
            elif code.startswith("partition"):
                m2 = re.search(r"(source = ```\n)(.*?)(\n\t\t\t\t```)", b, re.S)
                assert m2, t
                inner = "\n".join(("\t" + ln if ln.strip() else ln) for ln in m2.group(2).splitlines())
                names = ", ".join(f'"{c}", [{c}]' for c in kept)
                b = b.replace(m2.group(0), m2.group(1) + "\t\t\t\tSELECTCOLUMNS (\n\t\t\t\t\t(\n" + inner + "\n\t\t\t\t\t),\n\t\t\t\t\t" + names + "\n\t\t\t\t)" + m2.group(3))
            out.append(b)
        f.write_text("".join(out), encoding="utf-8", newline="\n")
    return u
