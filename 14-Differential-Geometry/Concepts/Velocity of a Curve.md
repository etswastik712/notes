---
title: Velocity of a Curve
aliases: ["velocity vector", "tangent vector to a curve", "gamma'(t)"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Velocity of a Curve

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2|HW2]] Q5; [[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3|HW3]] Q1(a),(c); [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=88|Lee Props. 3.23–3.24, Cor. 3.25, p. 70]].

> [!intuition] In one picture
> The instantaneous direction of motion along a path, as a rule for differentiating functions along the path.

> [!key] Definition
> For a smooth curve $\gamma:J\to M$: $\gamma'(t_0)=d\gamma_{t_0}(d/dt)$, i.e. $\gamma'(t_0)f=(f\circ\gamma)'(t_0)$; in a chart its components are $(x^i\circ\gamma)'(t_0)$. Every $v\in T_pM$ is $\gamma'(0)$ for some curve; $dF_p(\gamma'(0))=(F\circ\gamma)'(0)$.

HW3 Q1: $\alpha(t)=(t,2t,\sqrt{1-5t^2})$: $\alpha'(\tfrac14)=(1,2)$ in the $\varphi_3^+$ basis and $(1,-5/\sqrt{11})$ in the $\varphi_2^+$ basis. Velocities of curves on $S^2\subset\mathbb R^3$ are orthogonal to the position. Integral curves of vector fields ([[Integral Curve]]) are curves whose velocity is prescribed.

Used in: [[DM03 Tangent Vectors and the Differential]]. Related: [[Tangent Vector]] · [[Differential of a Smooth Map]] · [[Integral Curve]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
