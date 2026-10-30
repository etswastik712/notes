---
title: Variational Equation
aliases: ["linearised equation", "derivative of the flow", "first variation"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Variational Equation

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Teschl §2.6; Hirsch–Smale Ch. 8.

> [!intuition] In one picture
> How a small change of the starting point spreads along the flow is itself governed by a linear equation built from the derivative of the field.

> [!key] Definition
> $Y(t)=D_p\theta(t,p)$ solves $Y'=DV(\theta(t,p))\,Y$, $Y(0)=I$.

For $x'=x^2$: $Y'=2xY$ gives $\partial_{x_0}\theta=1/(1-x_0t)^2$ ($=4$ at $x_0=1$, $t=\tfrac12$, verified numerically). At an equilibrium $p$ with $DV(p)=A$, $Y=e^{tA}$: linear stability; compare the matrix exponential in [[DM14 One-Parameter Subgroups and the Exponential Map]].

Used in: [[PA14 ODE Existence Uniqueness and Smooth Dependence]]. Related: [[Smooth Dependence on Initial Conditions]] · [[Total Derivative]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
