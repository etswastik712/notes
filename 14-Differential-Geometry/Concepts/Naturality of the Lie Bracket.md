---
title: Naturality of the Lie Bracket
aliases: ["Proposition 8.30", "pushforward of brackets", "brackets and diffeomorphisms"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Naturality of the Lie Bracket

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=206|Lee Prop. 8.30, p. 188]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=207|Lee Cor. 8.31, p. 189]].

> [!intuition] In one picture
> The bracket is defined by derivatives alone, so any smooth change of variables carries brackets to brackets.

> [!key] Definition
> If $X_i$ is $F$-related to $Y_i$ ($i=1,2$) then $[X_1,X_2]$ is $F$-related to $[Y_1,Y_2]$ (Prop 8.30). For a diffeomorphism: $F_*[X_1,X_2]=[F_*X_1,F_*X_2]$ (Cor 8.31). For an immersed submanifold: brackets of fields tangent to $S$ are tangent to $S$ (Cor 8.32).

Checked for $F(x,y)=(xy,y/x)$, $X_1=x\partial_x+y\partial_y$, $X_2=y\partial_x+x^2\partial_y$ ($[X_1,X_2]=x^2\partial_y$ pushes to $((u/v)^{3/2},(u/v)^{1/2})$ on both sides). It is the reason left-invariant fields are closed under brackets and why $F_*:\mathrm{Lie}(G)\to\mathrm{Lie}(H)$ is a Lie algebra homomorphism ([[DM11 The Lie Algebra of a Lie Group]]); the Frobenius-necessity half is in [[DM15 Closed Subgroups and the Lie Correspondence]].

Used in: [[DM10 Vector Fields and Lie Brackets]], [[DM11 The Lie Algebra of a Lie Group]]. Related: [[F-Related Vector Fields]] · [[Lie Bracket of Vector Fields]] · [[Lie Group Homomorphism]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
