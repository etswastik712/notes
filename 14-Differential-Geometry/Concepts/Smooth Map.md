---
title: Smooth Map
aliases: ["smooth mapping", "smooth maps between manifolds"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Smooth Map

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-07-hw1|HW1]] Q3; [[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2|HW2]] Q4.

> [!intuition] In one picture
> A map that is smooth when written in coordinates on both sides.

> [!key] Definition
> $F:M\to N$ is smooth if each $p$ has smooth charts $(U,\varphi)\ni p$, $(V,\psi)\ni F(p)$ with $F(U)\subseteq V$ and $\psi\circ F\circ\varphi^{-1}$ smooth. For continuous $F$ this need be checked in **one** chart pair at each point (HW1 Q3).

Smooth $\Rightarrow$ continuous; compositions, projections, inclusions of open sets, charts, product maps are smooth. Antipodal map of $S^2$: $u\mapsto-u$ in stereographic charts. Matrix multiplication and inversion on $GL(n,\mathbb R)$ are smooth ([[DM08 Lie Groups]]). The derivative of a smooth map: [[Differential of a Smooth Map]].

Used in: [[DM02 Smooth Maps and Partitions of Unity]]. Related: [[Coordinate Representation of a Map]] · [[Diffeomorphism]] · [[Smooth Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
