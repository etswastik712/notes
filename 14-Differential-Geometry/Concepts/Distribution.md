---
title: Distribution
aliases: ["tangent distribution", "k-plane field", "tangent subbundle", "rank-k distribution"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG29 via the [[mt3184-differential-geometry-and-lie-groups/2026-11-06-november-2-6|Nov 2–6 note (DG29–30)]].
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=509|Lee p. 491, Example 19.1]].

> [!intuition] In one picture
> A smooth choice of a $k$-dimensional plane $D_p\subseteq T_pM$ at every point: a line field is a vector field up to scale; from rank 2 on the planes may fail to fit together into surfaces.

> [!key] Definition
> A **distribution of rank $k$** on $M$ is $D=\coprod_pD_p\subseteq TM$ with $\dim D_p=k$, **smooth** if each point has a neighbourhood with smooth fields $V_1,\dots,V_k$ forming a basis of $D_q$ for all $q$ (a rank-$k$ subbundle of $TM$). Equivalently $D=\ker\omega^1\cap\dots\cap\ker\omega^{n-k}$ locally (Lee Lemma 19.5).

Examples: a nowhere-vanishing field $V$; $\mathrm{span}\{\partial_1,\dots,\partial_k\}$; the orthogonal complement of the radial field on $\mathbb R^n\setminus0$ (leaves = spheres); the non-integrable $\mathrm{span}\{\partial_x+y\partial_z,\partial_y\}$ (Lee Ex. 19.1(d)).

Used in: [[DM16 Distributions, Involutivity and the Frobenius Theorem]], [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]]. Related: [[Integral Manifold]] · [[Involutive Distribution]] · [[Tangent Bundle]] · [[Local Frame]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
