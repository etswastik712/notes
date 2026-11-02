---
title: Closed Subgroup Theorem
aliases: ["Cartan's theorem", "Theorem 20.12", "closed subgroups are embedded", "Corollary 20.13"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Closed Subgroup Theorem

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG14 via [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12|Sep 7–12 note]]; HW9 Q6.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=541|Lee Thm 20.12, p. 523]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=543|Lee Cor. 20.13, p. 525]].

> [!intuition] In one picture
> Topology forces smoothness: a subgroup that is merely a closed set is automatically cut out by a linear subspace of $\mathfrak g$ near $e$.

> [!key] Definition
> $H\le G$: closed $\iff$ embedded submanifold $\iff$ embedded Lie subgroup. Proof of (closed $\Rightarrow$ embedded): $\mathfrak h=\{X:\exp tX\in H\ \forall t\}$ is a subspace by the **Trotter formula**; $\exp(U\cap\mathfrak h)=\exp U\cap H$ for small $U$ (sequence argument with $\Phi=\exp X\exp Y$); left translates give slice charts; $\mathrm{Lie}(H)=\mathfrak h$. (Embedded $\Rightarrow$ closed: slice chart + $W^{-1}W\subseteq V$.)

Closed: $SL(n)$, $O(n)$, $U(n)$, centres, $\mathbb Z\subset\mathbb R$, the circle $\{(2t,3t)\}\subset T^2$. Not closed: $\mathbb Q\subset\mathbb R$, the dense line in $T^2$. HW9 Q6: the closure of any Lie subgroup is an embedded Lie subgroup, so a Lie subgroup is embedded or dense in an embedded one.

Used in: [[DM15 Closed Subgroups and the Lie Correspondence]], [[DM08 Lie Groups]]. Related: [[Lie Subgroup]] · [[Trotter Product Formula]] · [[Exponential Map]] · [[Embedded Submanifold]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
