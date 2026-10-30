---
title: Constant Rank Theorem (Euclidean)
aliases: ["rank theorem in R^n", "normal form of constant rank maps"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Constant Rank Theorem (Euclidean)

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Lee Thm 4.12 ([[John M. Lee - Introduction to Smooth Manifolds.pdf#page=99|p. 81]]), specialised to $\mathbb R^m$; Spivak Problem 2-32.

> [!intuition] In one picture
> A map whose derivative has the same rank $r$ everywhere is, after nonlinear changes of coordinates in source and target, the plain 'keep $r$ coordinates, zero the rest' map.

> [!key] Definition
> $F:U\subseteq\mathbb R^m\to\mathbb R^n$ smooth of constant rank $r$ $\Rightarrow$ local diffeomorphisms $\varphi,\psi$ with $\psi\circ F\circ\varphi^{-1}(x)=(x^1,\dots,x^r,0,\dots,0)$.

Special cases: a submersion is locally a projection, an immersion locally an inclusion. Fails if the rank jumps ($x\mapsto x^2$). Manifold form: [[DM04 The Tangent Bundle and the Rank Theorem]].

Used in: [[PA13 The Derivative and the Inverse Function Theorem]], [[DM04 The Tangent Bundle and the Rank Theorem]]. Related: [[Inverse Function Theorem]] · [[Local Diffeomorphism]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
