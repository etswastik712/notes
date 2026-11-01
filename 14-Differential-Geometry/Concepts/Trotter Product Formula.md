---
title: Trotter Product Formula
aliases: ["Lie product formula", "Corollary 20.11", "Proposition 20.10", "sum from products"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Trotter Product Formula

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=540|Lee Prop. 20.10, p. 522]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=541|Lee Cor. 20.11, p. 523]].

> [!intuition] In one picture
> Alternating tiny steps along $X$ and $Y$ gives, in the limit, a step along $X+Y$.

> [!key] Definition
> $\exp tX\exp tY=\exp\big(t(X+Y)+t^2Z(t)\big)$ with $Z$ smooth, hence $\lim_n\big(\exp\tfrac tnX\exp\tfrac tnY\big)^n=\exp t(X+Y)$. Proof: $\varphi=\exp^{-1}(\exp tX\exp tY)$ has $\varphi'(0)=X+Y$ ($dm_{(e,e)}(X,Y)=X+Y$).

Numerically the error for random $3\times3$ $X,Y$ is $2.46\times10^{-1},\dots,2.46\times10^{-4}$ for $n=10,\dots,10^4$ (rate $1/n$). It makes $\{X:\exp tX\in H\}$ a vector space for closed $H$: the Closed Subgroup Theorem ([[DM15 Closed Subgroups and the Lie Correspondence]]). Used in physics for operator splitting.

Used in: [[DM14 One-Parameter Subgroups and the Exponential Map]], [[DM15 Closed Subgroups and the Lie Correspondence]]. Related: [[Exponential Map]] · [[Lie Subgroup]] · [[Matrix Exponential]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
