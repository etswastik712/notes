---
title: Gronwall Inequality
aliases: ["Gronwall's inequality", "Grönwall"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Gronwall Inequality

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Teschl §2.2; used in [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=681|Lee App. D]].

> [!intuition] In one picture
> A quantity that grows at most in proportion to its own accumulated size can grow at most exponentially.

> [!key] Definition
> If $u\ge0$ is continuous and $u(t)\le C+L\int_0^tu$ on $[0,T]$, then $u(t)\le Ce^{Lt}$.

Consequences: uniqueness of solutions ($C=0\Rightarrow u\equiv0$) and continuous dependence $|x(t)-y(t)|\le|p-q|e^{L|t|}$. Proof: $w=C+L\int u$ has $w'\le Lw$.

Used in: [[PA14 ODE Existence Uniqueness and Smooth Dependence]]. Related: [[Picard Iteration]] · [[Smooth Dependence on Initial Conditions]] · [[Lipschitz Condition]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
