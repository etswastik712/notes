---
title: Local Diffeomorphism
aliases: ["local diffeomorphism", "diffeomorphism"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Local Diffeomorphism

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=678|Lee Cor. C.36, p. 660]].

> [!intuition] In one picture
> A map that looks like a smooth, smoothly invertible change of coordinates around every point, without being globally one-to-one.

> [!key] Definition
> $F$ is a **diffeomorphism** if it is a smooth bijection with smooth inverse; a **local diffeomorphism** if every point has a neighbourhood on which $F$ is a diffeomorphism onto an open set. By the [[Inverse Function Theorem]], $F$ is a local diffeomorphism iff $DF$ is invertible everywhere.

$F(x,y)=(e^x\cos y,e^x\sin y)$ is one but not injective (a covering map); $x\mapsto x^3$ is a smooth bijection that is not a diffeomorphism.

Used in: [[PA13 The Derivative and the Inverse Function Theorem]]. Related: [[Inverse Function Theorem]] · [[Chain Rule]] · [[Total Derivative]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
