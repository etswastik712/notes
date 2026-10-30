---
title: Smooth Dependence on Initial Conditions
aliases: ["flow of an ODE", "smooth dependence", "ODE flow"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Smooth Dependence on Initial Conditions

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=685|Lee Thm D.5, p. 667]]; Hirsch–Smale Ch. 8.

> [!intuition] In one picture
> Nearby starting points give nearby solutions, and the dependence is as smooth as the field itself.

> [!key] Definition
> For smooth $V$, the domain $\mathcal D=\{(t,p):a_p<t<b_p\}$ is open in $\mathbb R\times U$ and the flow $\theta(t,p)=\gamma_p(t)$ is smooth on it. Group law: $\theta_s\circ\theta_t=\theta_{s+t}$ where defined; each $\theta_t$ is a diffeomorphism $U_t\to U_{-t}$.

Flow of $y\partial_x+\partial_y$: $(a,b)\mapsto(a+bt+t^2/2,\,b+t)$; of the rotation field: rotation by $t$. Manifold version: Fundamental Theorem on Flows, [[Flow of a Vector Field]].

Used in: [[PA14 ODE Existence Uniqueness and Smooth Dependence]]. Related: [[Variational Equation]] · [[Gronwall Inequality]] · [[Maximal Solution of an ODE]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
