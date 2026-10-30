---
title: Regular Value
aliases: ["critical value", "critical point", "regular point"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Regular Value

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-27-hw4|HW4]] Q1.

> [!intuition] In one picture
> A value that the map approaches 'transversally': at every preimage the differential is onto.

> [!key] Definition
> $q\in N$ is a **regular value** of $F:M\to N$ if $dF_p$ is surjective for every $p\in F^{-1}(q)$; otherwise $q$ is a **critical value** and points with $dF_p$ not onto are **critical points**.

$F=x^2-y^2$: every $c\neq0$ is regular, $0$ is critical (level set a cross). Sard's theorem: critical values have measure zero ([[DM07 Sard Whitney and Transversality]]). Regular values of $\det$: all of $\mathbb R^\times$.

Used in: [[DM06 Submanifolds]]. Related: [[Regular Level Set Theorem]] · [[Immersion and Submersion]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
