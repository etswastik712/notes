---
title: Lie Bracket of Vector Fields
aliases: ["Lie bracket", "commutator of vector fields", "[X,Y]", "bracket of vector fields"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Lie Bracket of Vector Fields

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG16–DG17 via [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12|Sep 7–12 note]]; HW6 Q4–Q5.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=204|Lee Lemma 8.25, Prop. 8.26, p. 186]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=205|Lee Prop. 8.28, p. 187]].

> [!intuition] In one picture
> The part of the second derivatives $XY$ and $YX$ that does not cancel: the first-order measure of how far the flows of $X$ and $Y$ are from commuting.

> [!key] Definition
> $[X,Y]f=X(Yf)-Y(Xf)$ is again a vector field (the second-order terms cancel: Leibniz rule, HW6 Q4). Coordinates: $[X,Y]=(XY^j-YX^j)\partial_j$; $[\partial_i,\partial_j]=0$. Properties: bilinear, antisymmetric, Jacobi, $[fX,gY]=fg[X,Y]+f(Xg)Y-g(Yf)X$.

HW6 Q5: $[x\partial_y-y\partial_x,\,y\partial_z-z\partial_y]=x\partial_z-z\partial_x$; $[\partial_x,x\partial_y]=\partial_y$; $[x\partial_x,\partial_x]=-\partial_x$; $[r\partial_r,\partial_\theta]=0$. The rotation fields satisfy $[L_x,L_y]=-L_z$. The flow quadrilateral closes up to $\varepsilon^2[X,Y]$ ([[DM13 Lie Derivatives and Commuting Vector Fields]]). Quantum-mechanical analogue: $[\hat x,\hat p]=i\hbar$.

Used in: [[DM10 Vector Fields and Lie Brackets]], [[DM11 The Lie Algebra of a Lie Group]]. Related: [[Jacobi Identity]] · [[Naturality of the Lie Bracket]] · [[Vector Field]] · [[Lie Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
