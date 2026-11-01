---
title: Integral Curve
aliases: ["integral curves", "maximal integral curve", "trajectory", "orbit curve"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Integral Curve

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG21–DG22 via [[mt3184-differential-geometry-and-lie-groups/2026-10-10-october-5-9|Oct 5–9]] and [[mt3184-differential-geometry-and-lie-groups/2026-10-16-october-12-16|Oct 12–16]] notes; HW7 Q4–Q5, HW8 Q1.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=225|Lee Prop. 9.2, p. 207]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=226|Lee Prop. 9.6, p. 208]].

> [!intuition] In one picture
> The path of a particle that always moves with the velocity the vector field prescribes at its current location.

> [!key] Definition
> $\gamma:J\to M$ with $\gamma'(t)=V_{\gamma(t)}$, an ODE $\dot x^i=V^i(x)$ in a chart. Exists and is unique through each point (Prop 9.2). $\gamma(at)$ is an integral curve of $aV$; $F\circ\gamma$ is an integral curve of $Y$ if $X\sim_FY$ (Prop 9.6). A maximal integral curve is **constant, injective or periodic**.

$V=-y\partial_x+x\partial_y$: rotation, period $2\pi$. $V=y\partial_x+\partial_y$: $(x_0+y_0t+t^2/2,\,y_0+t)$. $x^2\partial_x$: $x_0/(1-x_0t)$, escapes in finite time. Left-invariant field on $GL(n)$ through $X_0$: $X_0e^{tA}$ ([[DM14 One-Parameter Subgroups and the Exponential Map]]). Existence theory: [[PA14 ODE Existence Uniqueness and Smooth Dependence]].

Used in: [[DM12 Integral Curves, Flows and Flowouts]]. Related: [[Flow of a Vector Field]] · [[Complete Vector Field]] · [[Vector Field]] · [[Regular and Singular Points]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
