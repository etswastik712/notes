---
title: Local Section Theorem
aliases: ["local sections", "Theorem 4.26", "section of a submersion"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/book, status/draft]
---
# Local Section Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=106|Lee Thm 4.26, p. 88]].

> [!intuition] In one picture
> Through every point of the domain of a submersion there is a smooth way of choosing, over a neighbourhood of the image, a point in each fibre.

> [!key] Definition
> $\pi:M\to N$ is a submersion iff every point of $M$ lies in the image of a smooth local section $\sigma:V\to M$ ($\pi\sigma=\mathrm{id}_V$). Consequences: submersions are open; the characteristic property.

Proof: rank theorem gives $\sigma(x)=(x,0)$; converse by $d\pi\circ d\sigma=\mathrm{id}$. For $\pi(x,y)=x+y^2$: $\sigma(s)=(s-y_0^2,y_0)$.

Used in: [[DM05 Immersions, Embeddings, Submersions and Coverings]]. Related: [[Immersion and Submersion]] · [[Characteristic Property of Surjective Submersions]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
