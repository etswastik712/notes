---
title: Inverse Function Theorem
aliases: ["IFT", "inverse function theorem"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Inverse Function Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=675|Lee Thm C.34, p. 657]]; Spivak Thm 2-11.

> [!intuition] In one picture
> If the linear approximation of a map is invertible at a point, the map itself is invertible near that point; the linear solution corrected by a convergent (contracting) iteration.

> [!key] Definition
> $F:U\subseteq\mathbb R^n\to\mathbb R^n$ smooth with $DF(a)$ invertible $\Rightarrow$ $F$ restricts to a diffeomorphism from a neighbourhood of $a$ onto a neighbourhood of $F(a)$, and $D(F^{-1})=(DF)^{-1}\circ F^{-1}$.

Local, not global ($e^x(\cos y,\sin y)$ is a local diffeomorphism that is not injective); sufficient, not necessary ($x\mapsto x^3$). Gives charts-from-submersions and the [[Implicit Function Theorem]], [[Constant Rank Theorem (Euclidean)]]; manifold version in [[DM04 The Tangent Bundle and the Rank Theorem]].

Used in: [[PA13 The Derivative and the Inverse Function Theorem]], [[DM04 The Tangent Bundle and the Rank Theorem]]. Related: [[Contraction Mapping Principle]] · [[Local Diffeomorphism]] · [[Implicit Function Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Rank Theorem]] (Differential Geometry): the rank theorem generalises the inverse function theorem (rank $n$) and the implicit function theorem (rank $m$) to maps of constant rank.
