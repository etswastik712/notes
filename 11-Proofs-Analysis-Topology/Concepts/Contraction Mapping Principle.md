---
title: Contraction Mapping Principle
aliases: ["Banach fixed point theorem", "contraction lemma", "contraction"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Contraction Mapping Principle

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=675|Lee Lemma C.35, p. 657]].

> [!intuition] In one picture
> A map that shrinks all distances by a fixed factor $L<1$ pulls every point toward one fixed point, as a photocopier reducing a photo of itself.

> [!key] Definition
> If $X$ is a nonempty complete metric space and $d(Tx,Ty)\le L\,d(x,y)$ with $L<1$, then $T$ has a unique fixed point $x^*$, and $d(x_n,x^*)\le L^nd(x_1,x_0)/(1-L)$ for $x_{n+1}=Tx_n$.

$\cos x=x$: $L=\sin1=0.841$, 67 steps to $10^{-12}$ (a-priori bound 166). Engine of the [[Inverse Function Theorem]] and of Picard's existence theorem for ODEs ([[PA14 ODE Existence Uniqueness and Smooth Dependence]]). Completeness is essential: $x\mapsto x/2$ on $(0,1]$ has no fixed point.

Used in: [[PA13 The Derivative and the Inverse Function Theorem]]. Related: [[Inverse Function Theorem]] · [[Cauchy Sequence]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
