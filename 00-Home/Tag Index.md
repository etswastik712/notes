---
title: Tag Index
tags: [meta, type/meta]
---
# Tag Index

The tag vocabulary (see [[Conventions]] for the rules). Click a tag in the tag pane to list its notes.

| Tag | Meaning |
|---|---|
| `#subject/climate`, `#subject/eco-evo`, `#subject/thermo`, `#subject/foundations`, `#subject/qm`, `#subject/waves`, `#subject/probability`, `#subject/group-theory`, `#subject/analysis`, `#subject/chemistry`, `#subject/earth-evolution`, `#subject/landscapes`, `#subject/neuroscience` | which course or support area owns the note |
| `#type/moc`, `#type/chapter`, `#type/concept`, `#type/derivation`, `#type/handout`, `#type/diagram`, `#type/meta` | what kind of note it is |
| `#taught` | content shown or said in class, therefore **in the syllabus** |
| `#extra/book` | in an assigned book or excerpt, **not** shown in class |
| `#extra/beyond` | added from outside the course materials |
| `#src/argha` · `#src/suhas-pre` · `#src/suhas-post` | which instructor taught it |
| `#src/book` · `#src/paper` · `#src/web` · `#src/own-notes` | non-lecture provenance |
| `#status/stub` · `#status/draft` · `#status/reviewed` | maturity |

## Usage counts
```dataview
TABLE WITHOUT ID tag AS "Tag", length(rows) AS "Notes"
FROM ""
FLATTEN file.etags AS tag
WHERE startswith(tag, "#subject") OR startswith(tag, "#extra") OR tag = "#taught" OR startswith(tag, "#src") OR startswith(tag, "#status")
GROUP BY tag
SORT tag ASC
```
