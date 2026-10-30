---
title: Transition Map
aliases: ["change of coordinates", "transition function", "coordinate change"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Transition Map

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** HW1 Q2; slide DG3–DG4 (change of coordinates).

> [!intuition] In one picture
> How to convert coordinates from one page of the atlas to the next on their overlap.

> [!key] Definition
> For charts $(U,\varphi)$, $(V,\psi)$ the **transition map** is $\psi\circ\varphi^{-1}:\varphi(U\cap V)\to\psi(U\cap V)$. The charts are **smoothly compatible** if it and its inverse are smooth, i.e. it is a diffeomorphism.

$S^2$ stereographic charts: $w\mapsto w/|w|^2$, $\det=-1/|w|^4$. $S^2$ graph charts: $(y,z)\mapsto(\sqrt{1-y^2-z^2},y)$, $\det=z/x$. $\mathbb{RP}^2$: $(a,b)\mapsto(1/a,b/a)$, $\det=-1/a^3$. The Jacobian of a transition map is the change-of-basis matrix of tangent vectors ([[DM03 Tangent Vectors and the Differential]]).

Used in: [[DM01 Smooth Manifolds]]. Related: [[Coordinate Chart]] · [[Smooth Atlas]] · [[Stereographic Projection]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
