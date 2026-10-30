---
title: Lipschitz Condition
aliases: ["Lipschitz", "locally Lipschitz", "Lipschitz continuous"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Lipschitz Condition

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=673|Lee Prop. C.29, p. 655]].

> [!intuition] In one picture
> A bound on how fast the output can change relative to the input: no infinitely steep points.

> [!key] Definition
> $V$ is **$L$-Lipschitz** on $K$ if $|V(x)-V(y)|\le L|x-y|$ for $x,y\in K$; **locally Lipschitz** if every point has a neighbourhood on which it is Lipschitz. $C^1$ maps are locally Lipschitz.

It is the hypothesis behind uniqueness: $x'=\sqrt{|x|}$ (not Lipschitz at $0$) has non-unique solutions from $x(0)=0$. $\|DV\|\le L$ on a convex set implies $L$-Lipschitz ([[Total Derivative]]).

Used in: [[PA14 ODE Existence Uniqueness and Smooth Dependence]]. Related: [[Picard Iteration]] · [[Gronwall Inequality]] · [[Contraction Mapping Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
