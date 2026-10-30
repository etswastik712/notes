---
title: Maximal Solution of an ODE
aliases: ["maximal integral curve", "escape lemma", "finite escape time", "blow-up"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Maximal Solution of an ODE

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=235|Lee Lemma 9.19 (Escape Lemma), p. 217]]; Lee Thm D.6.

> [!intuition] In one picture
> Extend the solution as far as it will go; if it stops in finite time it must have run off to infinity or to the edge of the domain.

> [!key] Definition
> For locally Lipschitz $V$ there is a unique maximal solution $\gamma_p:(a_p,b_p)\to U$ through $p$; any other solution is a restriction. **Escape lemma:** if $b_p<\infty$, $\gamma_p(t)$ leaves every compact set as $t\to b_p$.

$x'=x^2$, $x(0)=x_0>0$: $x=x_0/(1-x_0t)$, $b=1/x_0$ (at $t=0.99/x_0$, $x=100x_0$). Compactly supported fields are complete. Manifold version: [[Integral Curve]] and [[Complete Vector Field]] in [[DM12 Integral Curves, Flows and Flowouts]].

Used in: [[PA14 ODE Existence Uniqueness and Smooth Dependence]]. Related: [[Initial Value Problem]] · [[Smooth Dependence on Initial Conditions]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
