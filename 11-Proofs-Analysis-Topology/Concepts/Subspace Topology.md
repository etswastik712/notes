---
title: Subspace Topology
aliases: ["induced topology", "relative topology", "subspace"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Subspace Topology

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=620|Lee Prop. A.17, p. 602]]; Munkres §16.

> [!intuition] In one picture
> A subset keeps every open set you can see from outside: its open sets are the traces $U\cap A$ of open sets of the ambient space.

> [!key] Definition
> For $A\subseteq X$ the subspace topology is $\{U\cap A: U\text{ open in }X\}$, the coarsest topology making the inclusion continuous. A map $f:Z\to A$ is continuous iff $\iota\circ f:Z\to X$ is.

$[0,\tfrac12)$ is open in $[0,1]$ but not in $\mathbb R$. Hausdorff and countability axioms are inherited; compactness passes to closed subsets. An **embedding** is a homeomorphism onto the image with this topology ([[Homeomorphism and Embedding]]).

Used in: [[PA11 Subspaces, Products and Quotients]]. Related: [[Topological Space]] · [[Homeomorphism and Embedding]] · [[Gluing Lemma]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
