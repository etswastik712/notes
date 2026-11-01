---
title: Commuting Frame
aliases: ["holonomic frame", "coordinate frame criterion", "canonical form for commuting vector fields", "Theorem 9.46"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Commuting Frame

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=252|Lee Ex. 9.45, Thm 9.46, p. 234]].

> [!intuition] In one picture
> A frame that is secretly the coordinate frame of some chart: its brackets vanish.

> [!key] Definition
> $(E_i)$ with $[E_i,E_j]=0$. **Thm 9.46:** independent commuting $V_1,\dots,V_k$ are $\partial/\partial s^1,\dots,\partial/\partial s^k$ in some chart centred at each point (flowout along all flows at once). Hence **a frame is a coordinate frame iff it commutes.**

$(E,R)=(r\partial_r,\partial_\theta)$ commute: log-polar coordinates $(\log r,\theta)$. The orthonormal polar frame $(\partial_r,\tfrac1r\partial_\theta)$ has $[\cdot,\cdot]=-\tfrac1{r^2}\partial_\theta\ne0$, so is not a coordinate frame. Obstruction for distributions: Frobenius ([[DM15 Closed Subgroups and the Lie Correspondence]]).

Used in: [[DM13 Lie Derivatives and Commuting Vector Fields]]. Related: [[Commuting Vector Fields]] · [[Local Frame]] · [[Flowout Theorem]] · [[Regular and Singular Points]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
