"""Write concept notes (type: concept) from a Python spec.  Library used by scripts/spec_*.py.

    from mkconcept import write
    write("11-Proofs-Analysis-Topology", "analysis", ITEMS)            # skips notes that already exist
    write(..., force=True)                                              # overwrite (only your own generated notes!)

Item keys: title, aliases, scope (list of 'taught' | 'extra-book' | 'extra-beyond'), syl (str, or dict scope -> str),
intuition, key, body (markdown, optional), used (chapter names), related (concept names), by (list, default ['book']).
Layout = Conventions section 2 (Concept): scope chip, [!syllabus], [!intuition], [!key], body, "Used in / Related", Linked from.
Concept notes live in <vault>/Concepts/ (user's global folder rule, 2026-10-25); existing files are never touched without force.
"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SPAN = {"taught": '<span class="scope-taught">taught · in syllabus</span>',
        "extra-book": '<span class="scope-extra-book">extra · book</span>',
        "extra-beyond": '<span class="scope-extra-beyond">extra · beyond</span>'}
TAG = {"taught": "taught", "extra-book": "extra/book", "extra-beyond": "extra/beyond"}
ICON = {"taught": "🟢 **taught:**", "extra-book": "🟡 **extra · book:**", "extra-beyond": "🔵 **extra · beyond:**"}
SRC_TAG = {"book": "src/book", "lecture-notes": "src/lecture-notes", "own-notes": "src/own-notes", "ai-notes": "src/ai-notes"}


def render(it, subject):
    scope = it["scope"]
    by = it.get("by", ["book"])
    tags = [f"subject/{subject}", "type/concept"] + [TAG[s] for s in scope] + [SRC_TAG.get(b, "src/" + b) for b in by] + ["status/draft"]
    aliases = ", ".join(f'"{a}"' for a in it.get("aliases", []))
    syl = it.get("syl", "")
    if isinstance(syl, str):
        syl = {scope[0]: syl} if syl else {}
    syl_lines = "\n".join(f"> {ICON[s]} {syl[s]}" for s in scope if s in syl)
    out = ["---", f"title: {it['title']}", f"aliases: [{aliases}]", f"subject: {subject}", "type: concept",
           f"scope: [{', '.join(scope)}]", f"by: [{', '.join(by)}]", "status: draft", f"tags: [{', '.join(tags)}]", "---",
           f"# {it['title']}", "", " ".join(SPAN[s] for s in scope), ""]
    if syl_lines:
        out += ["> [!syllabus] In the syllabus vs extra", syl_lines, ""]
    out += ["> [!intuition] In one picture", "> " + it["intuition"].replace("\n", "\n> "), "",
            "> [!key] Definition", "> " + it["key"].replace("\n", "\n> "), ""]
    if it.get("body"):
        out += [it["body"].strip(), ""]
    links = []
    if it.get("used"):
        links.append("Used in: " + ", ".join(f"[[{u}]]" for u in it["used"]) + ".")
    if it.get("related"):
        links.append("Related: " + " · ".join(f"[[{r}]]" for r in it["related"]) + ".")
    if links:
        out += [" ".join(links), ""]
    out += ["## Linked from", "```dataview", "LIST FROM [[]] AND -#type/moc SORT file.name ASC", "```", ""]
    return "\n".join(out)


def write(folder, subject, items, force=False):
    cdir = os.path.join(ROOT, folder, "Concepts")
    os.makedirs(cdir, exist_ok=True)
    made, skipped = 0, []
    for it in items:
        path = os.path.join(cdir, it["title"] + ".md")
        if os.path.exists(path) and not force:
            skipped.append(it["title"])
            continue
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(it, subject))
        made += 1
    print(f"{folder}/Concepts: wrote {made}, skipped {len(skipped)} existing" + (f" ({', '.join(skipped)})" if skipped else ""))
