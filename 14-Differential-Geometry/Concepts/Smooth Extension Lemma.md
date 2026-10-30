---
title: Smooth Extension Lemma
aliases: ["extension lemma", "extending smooth functions"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/book, status/draft]
---
# Smooth Extension Lemma

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=63|Lee Lemma 2.26, p. 45]].

> [!intuition] In one picture
> A function that is smooth near a closed set can be extended to a smooth function on the whole manifold, because a partition of unity glues the local extensions.

> [!key] Definition
> If $A\subseteq M$ is closed and $f:A\to\mathbb R^k$ is locally the restriction of smooth functions, then for every open $U\supseteq A$ there is a smooth $\tilde f$ on $M$, $\tilde f|_A=f$, $\operatorname{supp}\tilde f\subseteq U$.

Simplest case: $f$ smooth on an open $W\supseteq A$: $\tilde f=\psi f$ with a bump $\psi$. Used to extend vectors and functions from submanifolds ([[DM06 Submanifolds]]).

Used in: [[DM02 Smooth Maps and Partitions of Unity]]. Related: [[Partition of Unity]] · [[Bump Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
