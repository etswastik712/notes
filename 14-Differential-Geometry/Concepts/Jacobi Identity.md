---
title: Jacobi Identity
aliases: ["Jacobi", "Lie algebra axioms"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Jacobi Identity

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG17 via [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12|Sep 7–12 note]].

> [!intuition] In one picture
> The consistency law of a commutator: it says $\operatorname{ad}_X=[X,\cdot]$ is a derivation of the bracket.

> [!key] Definition
> $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$. Together with bilinearity and antisymmetry it defines a **Lie algebra**. For vector fields it is verified by expanding the twelve terms $XYZ,XZY,\dots$ which cancel in pairs; for matrices $[A,B]=AB-BA$ it is the same computation.

Examples: $\mathfrak X(M)$ with the Lie bracket, $\mathfrak{gl}(n,\mathbb R)$ with the matrix commutator, $\mathbb R^3$ with the cross product. Checked exactly on three fields of $\mathbb R^3$ with polynomial and trigonometric components. The cross-product case is [[DM11 The Lie Algebra of a Lie Group]].

Used in: [[DM10 Vector Fields and Lie Brackets]], [[DM11 The Lie Algebra of a Lie Group]]. Related: [[Lie Bracket of Vector Fields]] · [[Lie Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
