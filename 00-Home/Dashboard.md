---
title: Dashboard
tags: [meta, type/meta]
---
# Dashboard

Live lists built from tags and properties (requires the Dataview plugin). Definitions of the tags: [[Tag Index]].

## Chapters by subject and status
```dataview
TABLE WITHOUT ID file.link AS "Chapter", subject AS "Subject", chapter AS "#", by AS "Taught by", scope AS "Scope", status AS "Status"
FROM #type/chapter
SORT subject ASC, chapter ASC
```

## Counts
```dataview
TABLE WITHOUT ID subject AS "Subject", length(rows) AS "Notes"
FROM #type/chapter OR #type/concept OR #type/moc
GROUP BY subject
```

## Everything labelled **extra**
**Extra from the assigned books**
```dataview
LIST
FROM #extra/book
SORT file.name ASC
```
**Extra added from outside the course**
```dataview
LIST
FROM #extra/beyond
SORT file.name ASC
```

## Still to write (stubs)
```dataview
TABLE WITHOUT ID file.link AS "Note", subject AS "Subject", by AS "Taught by"
FROM #status/stub
SORT subject ASC, file.name ASC
```

## Syllabus core: notes that contain taught material
```dataview
LIST
FROM #taught AND #type/chapter
SORT chapter ASC
```

## Notes by instructor
**Argha**
```dataview
LIST FROM #src/argha SORT file.name ASC
```
**Suhas (pre-midsem)**
```dataview
LIST FROM #src/suhas-pre SORT file.name ASC
```
**Suhas (post-midsem)**
```dataview
LIST FROM #src/suhas-post SORT file.name ASC
```

## Diagrams and handouts
```dataview
LIST
FROM "Assets/excalidraw"
```
