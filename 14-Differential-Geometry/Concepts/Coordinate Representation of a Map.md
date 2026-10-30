---
title: Coordinate Representation of a Map
aliases: ["local expression", "coordinate expression", "representation in charts"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Coordinate Representation of a Map

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2|HW2]] Q4, [[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3|HW3]] Q1; Test 1 Q2–Q4.

> [!intuition] In one picture
> Write the map in the coordinates you choose on each side; all calculus (Jacobians, differentials) is done there.

> [!key] Definition
> For $F:M\to N$ and charts $(U,\varphi)$, $(V,\psi)$ with $F(U)\subseteq V$: $\widehat F=\psi\circ F\circ\varphi^{-1}:\varphi(U)\to\psi(V)$. The differential $dF_p$ has the Jacobian $D\widehat F(\varphi(p))$ as matrix in the coordinate bases ([[DM03 Tangent Vectors and the Differential]]).

Choose charts that make $\widehat F$ simple: e.g. antipodal map of $S^2$ in $\psi_2$ (at $N$) and $\psi_1$ (at $S$) is $u\mapsto-u$.

Used in: [[DM02 Smooth Maps and Partitions of Unity]]. Related: [[Smooth Map]] · [[Transition Map]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
