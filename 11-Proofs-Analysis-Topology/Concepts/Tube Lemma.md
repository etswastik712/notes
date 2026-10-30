---
title: Tube Lemma
aliases: ["tube lemma"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Tube Lemma

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Munkres §26 (Lemma 26.8).

> [!intuition] In one picture
> A box around a whole compact slice $\{x_0\}\times Y$ can be thickened to a tube $W\times Y$ inside any open set containing the slice.

> [!key] Definition
> If $Y$ is compact and $N\subseteq X\times Y$ is open with $\{x_0\}\times Y\subseteq N$, then some open $W\ni x_0$ has $W\times Y\subseteq N$.

Proof: cover the slice by boxes $U_y\times V_y\subseteq N$, take finitely many $V_y$ covering $Y$ and $W=\bigcap U_y$. Consequence: finite products of compact spaces are compact. Fails for non-compact $Y$: $N=\{|x|<1/(1+y^2)\}\subset\mathbb R^2$.

Used in: [[PA11 Subspaces, Products and Quotients]]. Related: [[Product Topology]] · [[Compact Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
