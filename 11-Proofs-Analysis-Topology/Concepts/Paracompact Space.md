---
title: Paracompact Space
aliases: ["paracompact", "paracompactness"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Paracompact Space

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Munkres §39.

> [!intuition] In one picture
> Every open cover can be traded for a finer one that is locally finite.

> [!key] Definition
> A Hausdorff space is **paracompact** if every open cover has a locally finite open refinement. Second-countable locally compact Hausdorff spaces (all manifolds) are paracompact.

Proof: refine over the annuli $A_j=K_j\setminus\operatorname{int}K_{j-1}$ of a compact exhaustion. Paracompactness is exactly what partitions of unity need; the long line is a connected, locally Euclidean, Hausdorff space that is not paracompact.

Used in: [[PA12 Separation, Countability and Local Compactness]]. Related: [[Locally Finite Family]] · [[Compact Exhaustion]] · [[Second-Countable Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
