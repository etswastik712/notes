---
title: Matrix Exponential
aliases: ["e^A", "exp of a matrix", "Rodrigues formula", "Proposition 20.2"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Matrix Exponential

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG26 via [[mt3184-differential-geometry-and-lie-groups/2026-10-24-october-19-24|Oct 19–24 note]].
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=535|Lee Prop. 20.2, p. 517]].

> [!intuition] In one picture
> The power series of $e^x$ with a matrix plugged in; it solves $\dot X=XA$.

> [!key] Definition
> $e^A=\sum_kA^k/k!$ converges (M-test, $\|A^k/k!\|\le\|A\|^k/k!$) to an invertible matrix; $t\mapsto e^{tA}$ is the one-parameter subgroup of $GL(n,\mathbb R)$ with velocity $A$; $\exp A=e^A$ on $GL(n)$ and its subgroups; $\det e^A=e^{\operatorname{tr}A}$.

$e^{tJ}=R(t)$ for $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$; nilpotent $A$: $e^{tA}=I+tA$. $SO(3)$: $e^{\hat\omega}=I+\tfrac{\sin|\omega|}{|\omega|}\hat\omega+\tfrac{1-\cos|\omega|}{|\omega|^2}\hat\omega^2$ (checked); $SU(2)$: $\cos\tfrac{|\omega|}2I-i\sin\tfrac{|\omega|}2\hat\omega\!\cdot\!\sigma$. Linear ODE solutions in [[PA14 ODE Existence Uniqueness and Smooth Dependence]].

Used in: [[DM14 One-Parameter Subgroups and the Exponential Map]]. Related: [[Exponential Map]] · [[One-Parameter Subgroup]] · [[Matrix Lie Algebras]] · [[General Linear Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
