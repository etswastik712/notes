---
title: Compact Exhaustion
aliases: ["exhaustion by compact sets", "exhaustion function"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Compact Exhaustion

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=630|Lee Prop. A.60, p. 612]].

> [!intuition] In one picture
> Fill the space by an increasing sequence of compact sets, each inside the interior of the next (balls of radius $j$ in $\mathbb R^n$).

> [!key] Definition
> A sequence of compact sets $K_j\subseteq\operatorname{int}K_{j+1}$ with $\bigcup K_j=X$. Every second-countable locally compact Hausdorff space (in particular every manifold) has one.

Proof idea: a countable basis of precompact open sets $B_i$; let $K_{j+1}$ be the closure of $B_1\cup\dots\cup B_m$ for $m$ large enough to cover $K_j$. Used to build locally finite refinements and, on manifolds, smooth exhaustion functions.

Used in: [[PA12 Separation, Countability and Local Compactness]]. Related: [[Locally Finite Family]] · [[Paracompact Space]] · [[Second-Countable Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
