---
title: Path Lifting
aliases: ["homotopy lifting", "unique path lifting", "monodromy"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Path Lifting

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=634|Lee Prop. A.77, p. 616]]; Hatcher Props. 1.30, 1.33.

> [!intuition] In one picture
> Walk in the base and the covering tells you, uniquely, where you are walking upstairs once you fix where you start.

> [!key] Definition
> For a covering $\pi:E\to X$, every path $\gamma$ in $X$ with a chosen start $e_0$ over $\gamma(0)$ has a unique lift $\tilde\gamma$ with $\tilde\gamma(0)=e_0$; homotopies lift likewise. Path-homotopic paths have lifts with the same endpoint; $\pi_*$ is injective.

Proof: cut $[0,1]$ into pieces mapping into evenly covered sets (compactness), lift piece by piece, glue ([[Gluing Lemma]]); uniqueness: the coincidence set is open and closed. Winding number = end of the lift through $\mathbb R\to S^1$ ([[Winding Number]]).

Used in: [[PA15 Covering Spaces and the Fundamental Group]]. Related: [[Covering Space]] · [[Lifting Criterion]] · [[Fundamental Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
