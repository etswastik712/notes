---
title: Differential of a Smooth Map
aliases: ["pushforward", "dF_p", "tangent map", "derivative of a smooth map"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Differential of a Smooth Map

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2|HW2]] Q4, [[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3|HW3]] Q1; Test 1 Q2.

> [!intuition] In one picture
> How a map stretches and rotates directions at a point: the best linear approximation of $F$ near $p$, as a map between tangent spaces.

> [!key] Definition
> $dF_p:T_pM\to T_{F(p)}N$, $dF_p(v)f=v(f\circ F)$. Linear; chain rule $d(G\circ F)=dG\circ dF$; $d\,\mathrm{id}=\mathrm{id}$; diffeomorphism $\Rightarrow$ isomorphism. In coordinate bases its matrix is the Jacobian of $\psi\circ F\circ\varphi^{-1}$.

Computed along curves: $dF_p(v)=(F\circ\gamma)'(0)$ when $\gamma'(0)=v$. Example: rotation by $60^\circ$ about the $z$-axis in the graph chart is a rotation matrix; $dF\alpha'(\tfrac14)=(-1.232,1.866)$. Extended to $dF:TM\to TN$ in [[DM04 The Tangent Bundle and the Rank Theorem]]. Euclidean case: [[Total Derivative]].

Used in: [[DM03 Tangent Vectors and the Differential]]. Related: [[Tangent Space]] · [[Coordinate Basis]] · [[Velocity of a Curve]] · [[Total Derivative]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
