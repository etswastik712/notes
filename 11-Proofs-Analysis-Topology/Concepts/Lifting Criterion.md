---
title: Lifting Criterion
aliases: ["lifting criterion", "lifting theorem"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Lifting Criterion

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=634|Lee Prop. A.78, p. 616]]; Hatcher Prop. 1.33.

> [!intuition] In one picture
> A map can be lifted through a covering exactly when its loops are the images of loops upstairs.

> [!key] Definition
> $f:(Y,y_0)\to(X,x_0)$, $Y$ path-connected and locally path-connected, lifts through the covering $\pi:(E,e_0)\to(X,x_0)$ iff $f_*\pi_1(Y)\subseteq\pi_*\pi_1(E)$. If $Y$ is simply connected the lift always exists (and is unique).

Every map $S^2\to S^1$ lifts to $\mathbb R$, hence is null-homotopic. Used to show that homomorphisms and smooth maps from simply connected groups/manifolds lift through covering homomorphisms.

Used in: [[PA15 Covering Spaces and the Fundamental Group]]. Related: [[Path Lifting]] · [[Universal Cover]] · [[Fundamental Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
