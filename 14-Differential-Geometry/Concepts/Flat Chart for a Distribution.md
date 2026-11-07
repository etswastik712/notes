---
title: Flat Chart for a Distribution
aliases: ["completely integrable distribution", "flat chart", "chart flat for D"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Flat Chart for a Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG29 via the [[mt3184-differential-geometry-and-lie-groups/2026-11-06-november-2-6|Nov 2–6 note (DG29–30)]].
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=514|Lee p. 496]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=516|Cor 19.13, p. 498]].

> [!intuition] In one picture
> Coordinates in which the plane field becomes the constant planes spanned by the first $k$ coordinate axes, so the integral manifolds are the slices.

> [!key] Definition
> A chart $(U,x^i)$ is **flat for $D$** if $D_q=\mathrm{span}(\partial_1,\dots,\partial_k)|_q$ on $U$ (Lee: $\varphi(U)$ a cube). $D$ is **completely integrable** if flat charts exist around every point. Chain: completely integrable ⇒ integrable ⇒ involutive; **Frobenius** closes the loop.

Recipe (Lee Ex. 19.14): project to $\mathbb R^k$, lift $\partial_i$ to commuting fields $V_i=(d\pi|_D)^{-1}\partial_i$, flow out of a transversal. Result there: coordinates $(x,y,z-xy)$ and leaves $z-xy=c$.

Used in: [[DM16 Distributions, Involutivity and the Frobenius Theorem]], [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]]. Related: [[Frobenius Theorem]] · [[Slice Chart]] · [[Commuting Frame]] · [[Involutive Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
