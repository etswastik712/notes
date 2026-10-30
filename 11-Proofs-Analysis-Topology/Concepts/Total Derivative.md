---
title: Total Derivative
aliases: ["derivative", "Jacobian", "differential of a map between Euclidean spaces", "Frechet derivative"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Total Derivative

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=660|Lee App. C, p. 642]]; Spivak Ch. 2.

> [!intuition] In one picture
> The best linear approximation of $F$ near $a$: $F(a+h)\approx F(a)+DF(a)h$, with error smaller than linear in $|h|$.

> [!key] Definition
> $F:U\to\mathbb R^m$ is differentiable at $a$ if some linear $DF(a)$ has $|F(a+h)-F(a)-DF(a)h|/|h|\to0$. Its matrix is the Jacobian $(\partial F^i/\partial x^j)$. $C^1$ (continuous partials) implies differentiable.

Matrix examples: $d(\det)_X(B)=\det X\operatorname{tr}(X^{-1}B)$ (so $d(\det)_I=\operatorname{tr}$), $d(\mathrm{inv})_X(B)=-X^{-1}BX^{-1}$, $d(AA^T)_X(B)=BX^T+XB^T$. Manifold version: [[Differential of a Smooth Map]].

Used in: [[PA13 The Derivative and the Inverse Function Theorem]]. Related: [[Chain Rule]] · [[Inverse Function Theorem]] · [[Local Diffeomorphism]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
