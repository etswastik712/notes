---
title: Chain Rule
aliases: ["chain rule for total derivatives"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Chain Rule

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=661|Lee Prop. C.3, p. 643]].

> [!intuition] In one picture
> Linear approximations compose: the derivative of a composition is the composition of the derivatives.

> [!key] Definition
> $D(G\circ F)(a)=DG(F(a))\circ DF(a)$. For a diffeomorphism, $D(F^{-1})(F(a))=DF(a)^{-1}$.

It makes the differential on manifolds functorial: $d(G\circ F)_p=dG_{F(p)}\circ dF_p$ ([[Differential of a Smooth Map]]), and shows transition maps between charts have invertible Jacobians.

Used in: [[PA13 The Derivative and the Inverse Function Theorem]]. Related: [[Total Derivative]] · [[Local Diffeomorphism]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
