---
title: Induced Lie Algebra Homomorphism
aliases: ["F_*", "Theorem 8.44", "differential of a Lie group homomorphism", "functoriality of Lie"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Induced Lie Algebra Homomorphism

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG17–DG19 via [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12|Sep 7–12 note]]; HW6 Q6–Q7, HW7 Q2.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=213|Lee Thm 8.44, p. 195]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=214|Lee Prop. 8.45, p. 196]].

> [!intuition] In one picture
> A homomorphism of groups differentiates, at the identity, to a homomorphism of their Lie algebras.

> [!key] Definition
> $F:G\to H$ homomorphism: each $X\in\mathrm{Lie}(G)$ is $F$-related to a unique $Y\in\mathrm{Lie}(H)$; $F_*X=Y$ is a Lie algebra homomorphism with $F_*=dF_e$ under $\varepsilon$. Functorial ($(F'F)_*=F'_*F_*$); isomorphisms go to isomorphisms.

$\det_*=\operatorname{tr}$ (HW6 Q7); $G$ abelian $\Rightarrow$ $i_*=-\mathrm{id}$ $\Rightarrow$ $\mathfrak g$ abelian (HW6 Q6); $\ker F_*=\mathrm{Lie}(\ker F)$ (HW7 Q2); $\mathrm{Ad}_*:\mathfrak{su}(2)\to\mathfrak{so}(3)$ is an isomorphism ($SU(2)\to SO(3)$ is $2:1$). Proof uses $F\circ L_g=L_{F(g)}\circ F$ and [[Naturality of the Lie Bracket]].

Used in: [[DM11 The Lie Algebra of a Lie Group]]. Related: [[Lie Algebra of a Lie Group]] · [[Lie Group Homomorphism]] · [[Naturality of the Lie Bracket]] · [[Lie Algebra Representation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
