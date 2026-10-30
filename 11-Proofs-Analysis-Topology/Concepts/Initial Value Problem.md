---
title: Initial Value Problem
aliases: ["IVP", "Cauchy problem", "autonomous system", "state-space reduction"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Initial Value Problem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=681|Lee App. D, p. 663]]; Teschl §1.1.

> [!intuition] In one picture
> Follow the arrows of a vector field from a given starting point: the solution is the path that is always tangent to the field.

> [!key] Definition
> $x'=V(x)$, $x(0)=p$, with $V:U\to\mathbb R^n$ a vector field. A solution is a differentiable curve $x:J\to U$ with $x'(t)=V(x(t))$; equivalently $x(t)=p+\int_0^tV(x(s))\,ds$.

Higher-order and time-dependent equations reduce to this form by adding variables: $\theta''=-\sin\theta\ \Rightarrow\ (\theta,\omega)'=(\omega,-\sin\theta)$; $x'=V(t,x)\ \Rightarrow\ (s,x)'=(1,V(s,x))$. Solutions are the **integral curves** of $V$ ([[DM12 Integral Curves, Flows and Flowouts]]).

Used in: [[PA14 ODE Existence Uniqueness and Smooth Dependence]]. Related: [[Lipschitz Condition]] · [[Picard Iteration]] · [[Maximal Solution of an ODE]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
