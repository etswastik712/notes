---
title: Quotient Topology
aliases: ["quotient space", "quotient map", "identification space", "gluing"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Quotient Topology

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=623|Lee Thms. A.27, A.30, A.31, p. 605]]; Munkres §22.

> [!intuition] In one picture
> Glue points together, then declare a set of glued points open when the corresponding set upstairs is open: the finest topology keeping the gluing map continuous.

> [!key] Definition
> For a surjection $\pi:X\to Y$, $V\subseteq Y$ is open iff $\pi^{-1}(V)$ is open. A map $\hat g:Y\to Z$ out of the quotient is continuous iff $\hat g\circ\pi$ is. Open or closed continuous surjections are quotient maps.

$[0,1]/(0\sim1)\cong S^1$, the torus and Klein bottle (square with edge words), $\mathbb{RP}^n=S^n/\pm$ ([[Real Projective Space]]). A quotient of a Hausdorff space need not be Hausdorff ([[Line with Two Origins]]); criterion: $\pi$ open and the relation closed.

Used in: [[PA11 Subspaces, Products and Quotients]]. Related: [[Line with Two Origins]] · [[Real Projective Space]] · [[Closed Map Lemma]] · [[Subspace Topology]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
