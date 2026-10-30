---
title: Winding Number
aliases: ["degree of a loop", "winding number around a point"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Winding Number

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=632|Lee Prop. A.68, p. 614]]; Hatcher Thm 1.7.

> [!intuition] In one picture
> How many times a loop goes around, counted with sign: the integer at which the lifted path ends.

> [!key] Definition
> For a loop $\gamma$ in $S^1$ (or in $\mathbb C\setminus\{0\}$, via $\gamma/|\gamma|$), lift through $t\mapsto e^{2\pi it}$ starting at $0$; the endpoint $\tilde\gamma(1)\in\mathbb Z$ is the winding number. $\pi_1(S^1)\cong\mathbb Z$ via this map; $z\mapsto z^k$ multiplies it by $k$.

Computed values: $e^{2\pi i3t}\mapsto3$, $e^{-2\pi i2t}\mapsto-2$, a wobbly $3$-turn loop $\mapsto3$, circles of radius $1$ centred at $0.99$ and $1.01$ $\mapsto1$ and $0$ (jumps when $0$ crosses the curve). Homotopy invariant.

Used in: [[PA15 Covering Spaces and the Fundamental Group]]. Related: [[Fundamental Group]] · [[Path Lifting]] · [[Homotopy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
