---
title: Covering Space
aliases: ["covering map", "evenly covered", "sheet", "covering"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Covering Space

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=633|Lee App. A 'Covering Maps', p. 615]]; Hatcher §1.3.

> [!intuition] In one picture
> Several identical floors stacked over each small region of the base, joined by ramps as you go around holes.

> [!key] Definition
> A continuous surjection $\pi:E\to X$ such that each point has an open neighbourhood $U$ with $\pi^{-1}(U)=\bigsqcup\widetilde U_\alpha$, each $\widetilde U_\alpha\to U$ a homeomorphism. Covering maps are local homeomorphisms and open maps; fibres are discrete.

$\mathbb R\to S^1$ (fibre $\mathbb Z$), $z\mapsto z^k$ ($k$ sheets), $S^n\to\mathbb{RP}^n$ (2 sheets), $\mathbb R^n\to T^n$, $SU(2)\to SO(3)$ (2 sheets). Not a covering: $(0,2)\to S^1$ (local homeomorphism, surjective, but not evenly covered at $1$). Smooth version: [[DM05 Immersions, Embeddings, Submersions and Coverings]].

Used in: [[PA15 Covering Spaces and the Fundamental Group]], [[DM05 Immersions, Embeddings, Submersions and Coverings]]. Related: [[Path Lifting]] · [[Universal Cover]] · [[Deck Transformation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Smooth Covering Map]] (Differential Geometry): a smooth covering is a covering space whose projection is a local diffeomorphism: $\mathbb R\to S^1$, $SU(2)\to SO(3)$, $\mathbb R^n\to T^n$.
