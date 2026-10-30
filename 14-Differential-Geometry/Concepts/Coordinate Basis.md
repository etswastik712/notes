---
title: Coordinate Basis
aliases: ["coordinate vectors", "partial derivative vectors", "d/dx^i"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Coordinate Basis

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** week 2 post: tangent spaces 'calculated in local coordinates'; HW2 Q3; HW3 Q1.

> [!intuition] In one picture
> The $n$ rules 'differentiate along the $i$-th coordinate line', one for each coordinate of the chart.

> [!key] Definition
> For a chart $(U,\varphi=(x^i))$: $\dfrac{\partial}{\partial x^i}\Big|_pf=\dfrac{\partial(f\circ\varphi^{-1})}{\partial x^i}(\varphi(p))$. They form a basis of $T_pM$; the components of $v$ are $v^i=v(x^i)$.

A different chart gives a different basis, related by the Jacobian of the transition ([[Transformation Law for Tangent Vectors]]). Coordinate vector fields $\partial/\partial x^i$ commute: $[\partial_i,\partial_j]=0$ ([[DM10 Vector Fields and Lie Brackets]]).

Used in: [[DM03 Tangent Vectors and the Differential]]. Related: [[Tangent Vector]] · [[Differential of a Smooth Map]] · [[Transformation Law for Tangent Vectors]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
