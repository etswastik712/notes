---
title: Complete Vector Field
aliases: ["complete", "Uniform Time Lemma", "global flow", "compactly supported vector field is complete", "Theorem 9.16"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Complete Vector Field

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG22–DG23 via [[mt3184-differential-geometry-and-lie-groups/2026-10-16-october-12-16|Oct 12–16 note]]; HW8 Q2.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=234|Lee Lemma 9.15, Thm 9.16, Thm 9.18, p. 216]].

> [!intuition] In one picture
> A field whose particles never escape to infinity in finite time, so the flow exists for all time.

> [!key] Definition
> $\mathcal D=\mathbb R\times M$. **Uniform Time Lemma:** if $(-\varepsilon,\varepsilon)\subseteq\mathcal D^{(p)}$ for all $p$ then $V$ is complete. Hence: compactly supported fields are complete (HW8 Q2); on a compact manifold every field is complete; **every left-invariant field on a Lie group is complete** (Thm 9.18).

Complete: $x\partial_x$, translations, rotation field, $\sin x\,\partial_x$, left-invariant $\tilde A$ on $GL(n)$. Not complete: $x^2\partial_x$ (blow-up at $1/x_0$), $\partial_x$ on $\mathbb R^2\setminus\{0\}$ (hole). Detection of incompleteness: [[Escape Lemma]].

Used in: [[DM12 Integral Curves, Flows and Flowouts]], [[DM14 One-Parameter Subgroups and the Exponential Map]]. Related: [[Flow of a Vector Field]] · [[Escape Lemma]] · [[Left-Invariant Vector Field]] · [[Integral Curve]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
