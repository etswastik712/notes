---
title: Locally Finite Family
aliases: ["locally finite", "refinement of a cover"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Locally Finite Family

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Munkres §39.

> [!intuition] In one picture
> Zooming in anywhere, you only ever see finitely many of the sets.

> [!key] Definition
> A family of subsets is **locally finite** if every point has a neighbourhood meeting only finitely many members. A **refinement** of a cover $\mathcal U$ is a cover each of whose members lies in a member of $\mathcal U$.

It depends on the ambient space: $\{(\tfrac1{n+2},\tfrac1n)\}$ is locally finite in $(0,1)$ but not in $[0,1)$ (every ball around $0$ meets infinitely many). Locally finite sums are the reason partitions of unity can be added up ([[DM02 Smooth Maps and Partitions of Unity]]).

Used in: [[PA12 Separation, Countability and Local Compactness]]. Related: [[Paracompact Space]] · [[Compact Exhaustion]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
