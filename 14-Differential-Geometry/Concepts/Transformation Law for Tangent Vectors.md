---
title: Transformation Law for Tangent Vectors
aliases: ["change of coordinates for tangent vectors", "change of basis between charts", "contravariant transformation"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Transformation Law for Tangent Vectors

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** week 2 post ('how these change when the coordinates change'); [[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2|HW2]] Q3; Test 1 Q4; [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=79|Lee Prop. 3.15, p. 61]].

> [!intuition] In one picture
> The same arrow is described by different numbers in different coordinate systems; the Jacobian of the coordinate change converts them.

> [!key] Definition
> If $\tilde x=\tilde\varphi\circ\varphi^{-1}(x)$ is the transition, components transform by $\tilde v^j=\sum_i\dfrac{\partial\tilde x^j}{\partial x^i}v^i$ and basis vectors by $\partial/\partial x^i=\sum_j\dfrac{\partial\tilde x^j}{\partial x^i}\partial/\partial\tilde x^j$.

HW2 Q3: $X=(1,2)$ becomes $(-\tfrac12-\sqrt3,1-\tfrac{\sqrt3}2)=(-2.2320,0.1340)$ via the Jacobian of $w\mapsto w/|w|^2$. Test 1 Q4: $(1,2)\mapsto(2,4)$ via $2I$.

Used in: [[DM03 Tangent Vectors and the Differential]]. Related: [[Coordinate Basis]] · [[Transition Map]] · [[Stereographic Projection]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
