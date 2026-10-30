---
title: Picard Iteration
aliases: ["Picard-Lindelof theorem", "Picard–Lindelöf", "Picard operator", "local existence and uniqueness"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Picard Iteration

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=683|Lee Thm D.3, D.4, pp. 665–667]].

> [!intuition] In one picture
> Guess the solution is constant, then repeatedly correct it by integrating the field along the current guess; the corrections shrink geometrically.

> [!key] Definition
> For $V$ Lipschitz and bounded on $\overline B_r(p)$ ($|V|\le M$, constant $L$), the operator $(Px)(t)=p+\int_0^tV(x(s))ds$ is a contraction of $C([-\varepsilon,\varepsilon],\overline B_r(p))$ for $\varepsilon<\min(r/M,1/L)$; its unique fixed point is the unique solution.

For $x'=x$, $x(0)=1$ the iterates are the Taylor polynomials of $e^t$ (at $t=1$: $1,2,2.5,2.667,2.708,\dots$). Proof engine: [[Contraction Mapping Principle]]. Uniqueness among all solutions: [[Gronwall Inequality]].

Used in: [[PA14 ODE Existence Uniqueness and Smooth Dependence]]. Related: [[Contraction Mapping Principle]] · [[Gronwall Inequality]] · [[Initial Value Problem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
