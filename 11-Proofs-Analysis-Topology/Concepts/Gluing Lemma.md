---
title: Gluing Lemma
aliases: ["pasting lemma", "gluing lemma for continuous maps"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Gluing Lemma

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=620|Lee Lemma A.20, p. 602]]; Munkres Thm 18.3.

> [!intuition] In one picture
> A function defined piece by piece is continuous if the pieces are continuous and fit together on the overlap, provided the pieces are both closed (or both open).

> [!key] Definition
> If $X=A\cup B$ with $A,B$ closed (or both open) and $f|_A$, $f|_B$ continuous, then $f$ is continuous.

Proof: $f^{-1}(C)=(f|_A)^{-1}(C)\cup(f|_B)^{-1}(C)$ is a union of two closed sets. It fails for mixed pieces, e.g. $0$ on $(-\infty,0]$ and $1$ on $(0,\infty)$.

Used in: [[PA11 Subspaces, Products and Quotients]]. Related: [[Subspace Topology]] · [[Continuous Function (Topological)]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
