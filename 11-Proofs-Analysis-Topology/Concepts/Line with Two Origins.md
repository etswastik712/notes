---
title: Line with Two Origins
aliases: ["non-Hausdorff manifold-like space"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Line with Two Origins

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=47|Lee Problem 1-1, p. 29]].

> [!intuition] In one picture
> Two copies of the real line glued everywhere except at $0$: from far away it is a line, but the two origins cannot be separated by disjoint open sets.

> [!key] Definition
> $M=(\mathbb R\times\{\pm1\})/\big((x,1)\sim(x,-1),\ x\neq0\big)$ is locally Euclidean and second-countable but **not Hausdorff**: every neighbourhood of $0_1$ meets every neighbourhood of $0_2$.

It is the standard example showing why a manifold must be required to be Hausdorff ([[DM01 Smooth Manifolds]]). The gluing relation is not closed in $(\mathbb R\times\{\pm1\})^2$, so the Hausdorff quotient criterion does not apply.

Used in: [[PA11 Subspaces, Products and Quotients]]. Related: [[Quotient Topology]] · [[Topological Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
