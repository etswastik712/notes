---
title: Lie Derivative of a Vector Field
aliases: ["Lie derivative", "L_V W", "Theorem 9.38", "derivative along a flow"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Lie Derivative of a Vector Field

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG24–DG25 via [[mt3184-differential-geometry-and-lie-groups/2026-10-16-october-12-16|Oct 12–16]] and [[mt3184-differential-geometry-and-lie-groups/2026-10-24-october-19-24|Oct 19–24]] notes; HW8 Q5–Q6.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=246|Lee Lemma 9.36, p. 228]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=247|Lee Thm 9.38, p. 229]].

> [!intuition] In one picture
> How $W$ changes as seen by an observer carried along by the flow of $V$: pull $W$ back to $p$ with the flow and differentiate.

> [!key] Definition
> $(\mathcal L_VW)_p=\frac d{dt}|_0\,d(\theta_{-t})_{\theta_t(p)}W_{\theta_t(p)}$ ($\theta$ the flow of $V$). Exists and is smooth (Lemma 9.36). **Theorem 9.38: $\mathcal L_VW=[V,W]$** (flow-box proof by cases). Properties: $\mathcal L_VW=-\mathcal L_WV$; $\mathcal L_{[V,W]}=[\mathcal L_V,\mathcal L_W]$; $\mathcal L_V(gW)=(Vg)W+g\mathcal L_VW$; $F_*\mathcal L_VX=\mathcal L_{F_*V}F_*X$.

Constant $V=v$ on $\mathbb R^n$: $\mathcal L_VW=D_vW$ (HW8 Q5). Shear $y\partial_x+\partial_y$ and $x\partial_y$: $[V,W]=(-x,y)$ checked from the definition. Depends on $V$ near $p$, not just along an integral curve (HW8 Q6). Quantum analogue: Heisenberg equation $\dot A=\tfrac i\hbar[H,A]$.

Used in: [[DM13 Lie Derivatives and Commuting Vector Fields]], [[DM14 One-Parameter Subgroups and the Exponential Map]]. Related: [[Lie Bracket of Vector Fields]] · [[Flow of a Vector Field]] · [[Invariant Vector Field]] · [[Commuting Vector Fields]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
