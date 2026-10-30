---
title: Homeomorphism and Embedding
aliases: ["homeomorphism", "topological embedding", "embedding (topological)"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Homeomorphism and Embedding

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Munkres §18; [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=620|Lee App. A]].

> [!intuition] In one picture
> A homeomorphism is a continuous deformation that can be undone continuously; an embedding is a homeomorphism onto a piece of a bigger space, seen with the topology that piece inherits.

> [!key] Definition
> A **homeomorphism** is a continuous bijection with continuous inverse. A **topological embedding** is a continuous injection $f$ that is a homeomorphism $X\to f(X)$ onto its image with the subspace topology.

A continuous bijection need not be a homeomorphism: $[0,1)\to S^1$, $t\mapsto e^{2\pi it}$. A continuous injection need not be an embedding: the figure-eight curve $\beta(t)=(\sin2t,\sin t)$ on $(-\pi,\pi)$. Rescue: compact domain and Hausdorff target ([[Closed Map Lemma]]). Smooth analogue: [[DM05 Immersions, Embeddings, Submersions and Coverings]].

Used in: [[PA11 Subspaces, Products and Quotients]]. Related: [[Subspace Topology]] · [[Closed Map Lemma]] · [[Continuous Function (Topological)]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
