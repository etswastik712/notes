---
title: Stereographic Projection
aliases: ["stereographic chart", "stereographic atlas"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Stereographic Projection

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-07-hw1|HW1]] Q2; [[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2|HW2]] Q3.

> [!intuition] In one picture
> Project the sphere from a pole onto the equatorial plane along straight lines: every point except the pole gets plane coordinates.

> [!key] Definition
> $\psi_1(x,y,z)=(x,y)/(1-z)$ on $S^2\setminus\{N\}$, $\psi_2(x,y,z)=(x,y)/(1+z)$ on $S^2\setminus\{S\}$, with $\psi_1^{-1}(w)=(2w,|w|^2-1)/(|w|^2+1)$ and transition $\psi_2\circ\psi_1^{-1}(w)=w/|w|^2$ (inversion).

Two charts suffice for $S^n$. Numerically $|\psi_2\psi_1^{-1}(w)-w/|w|^2|<6\times10^{-13}$ on 1000 random $w$. $(\mathbb R^n)^*\cong S^n$ ([[One-Point Compactification]]). Used in [[DM03 Tangent Vectors and the Differential]] (HW2 Q3, HW3).

Used in: [[DM01 Smooth Manifolds]]. Related: [[Transition Map]] · [[Smooth Atlas]] · [[One-Point Compactification]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
