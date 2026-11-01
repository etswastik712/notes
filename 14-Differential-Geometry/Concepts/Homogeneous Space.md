---
title: Homogeneous Space
aliases: ["G/H", "coset space", "homogeneous manifold", "G-homogeneous space"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Homogeneous Space

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=569|Lee Thm 21.17, p. 551]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=570|Lee Thm 21.18, p. 552]].

> [!intuition] In one picture
> A space on which a group acts transitively, so that all points look alike; it is the group modulo the stabiliser of one point.

> [!key] Definition
> If $G$ acts transitively on $M$, $\theta^{(p)}:G\to M$ is a surjective submersion with fibres the cosets $gG_p$, and $G/G_p\to M$ is a diffeomorphism (Lee Thm 21.18). For closed $H\le G$, $G/H$ is a manifold of dimension $\dim G-\dim H$ (Thm 21.17).

$S^n=O(n+1)/O(n)$ ($n$), $S^{2n+1}=U(n+1)/U(n)$ ($2n+1$), $S^2=SU(2)/U(1)$ ($2$), $\mathbb{RP}^n=O(n+1)/(O(n)\times O(1))$ ($n$), $\mathbb R^n=E(n)/O(n)$ ($n$). Full treatment in the quotient-manifold chapter of Lee (beyond MT3184).

Used in: [[DM09 Group Actions and Semidirect Products]]. Related: [[Orbit Map and Stabiliser]] · [[Equivariant Rank Theorem]] · [[Smooth Action]] · [[Real Projective Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
