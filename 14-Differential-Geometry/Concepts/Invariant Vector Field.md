---
title: Invariant Vector Field
aliases: ["invariant under a flow", "flow-invariant vector field", "Theorem 9.42"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Invariant Vector Field

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=249|Lee Prop. 9.41, Thm 9.42, p. 231]].

> [!intuition] In one picture
> A field that the flow carries onto itself: moving the field along the flow changes nothing.

> [!key] Definition
> $W$ is invariant under the flow $\theta$ of $V$ if $d(\theta_t)_pW_p=W_{\theta_t(p)}$. **Thm 9.42:** $[V,W]=0\iff W$ is $\theta^V$-invariant $\iff V$ is $\theta^W$-invariant. Cor 9.43: every field is invariant under its own flow. Proof via $X(t)=d(\theta_{-t})W_{\theta_tp}$ and $X'(t_0)=d(\theta_{-t_0})(\mathcal L_VW)_{\theta_{t_0}p}$ (Prop 9.41).

Left-invariant fields on a Lie group are invariant under all left translations ([[Left-Invariant Vector Field]]); a field is invariant under its own flow ($[V,V]=0$). The shear field is not invariant under translation along $x$-flows of non-parallel fields.

Used in: [[DM13 Lie Derivatives and Commuting Vector Fields]]. Related: [[Lie Derivative of a Vector Field]] · [[Commuting Vector Fields]] · [[Flow of a Vector Field]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
