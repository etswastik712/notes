---
title: Implicit Function Theorem
aliases: ["implicit function theorem", "regular level set as a graph"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Implicit Function Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=679|Lee Thm C.40, p. 661]]; Spivak Thm 2-12.

> [!intuition] In one picture
> Where an equation $\Phi(x,y)=c$ can be solved for $y$ to first order, it can be solved exactly near the point, and the solution $y=g(x)$ is smooth.

> [!key] Definition
> $\Phi:U\subseteq\mathbb R^n\times\mathbb R^k\to\mathbb R^k$ smooth, $\Phi(a,b)=c$, $\partial_y\Phi(a,b)$ invertible $\Rightarrow$ near $(a,b)$ the level set is the graph of a smooth $g$, with $g'=-(\partial_y\Phi)^{-1}\partial_x\Phi$.

The circle $x^2+y^2=1$ is the graph $y=\sqrt{1-x^2}$ near $(0,1)$ ($g'(0.6)=-0.75$) but not near $(1,0)$ where $\partial_y\Phi=0$. Regular level sets are submanifolds ([[DM06 Submanifolds]]).

Used in: [[PA13 The Derivative and the Inverse Function Theorem]], [[DM06 Submanifolds]]. Related: [[Inverse Function Theorem]] · [[Constant Rank Theorem (Euclidean)]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
