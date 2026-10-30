---
title: Smooth Embedding
aliases: ["embedding", "embedded image", "injective immersion"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Smooth Embedding

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** DG12: the figure-eight and the dense line are injective immersions that are not embeddings; HW5 Q1.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=103|Lee Examples 4.17–4.20, p. 85]]; [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=105|Prop. 4.22, p. 87]].

> [!intuition] In one picture
> An immersion that is also a faithful copy topologically: the image looks, with its inherited topology, exactly like the domain.

> [!key] Definition
> A smooth immersion that is a homeomorphism onto its image (subspace topology). An **injective immersion** is an embedding if $F$ is open/closed, **proper**, $M$ is compact, or $\dim M=\dim N$ (HW5 Q1). Immersions are locally embeddings (Lee Thm 4.25).

Not embeddings: figure-eight $\beta(t)=(\sin2t,\sin t)$, dense line $t\mapsto(e^{it},e^{i\sqrt2t})$ on $T^2$ ([[Dense Line on the Torus]]). $t\mapsto(t^3,0)$ is a topological but not smooth embedding. Images of embeddings are embedded submanifolds ([[DM06 Submanifolds]]).

Used in: [[DM05 Immersions, Embeddings, Submersions and Coverings]]. Related: [[Immersion and Submersion]] · [[Proper Map]] · [[Homeomorphism and Embedding]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
