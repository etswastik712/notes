---
title: Poles and Stability
aliases: ["poles", "pole-zero", "stability from poles"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Poles and Stability

> [!intuition] In one picture
> A linear system is stable iff every pole of its transfer function has negative real part; the pole gives the decay rate and frequency.

> [!key] Key facts
> Mode $e^{s_jt}$; relaxation time $1/\lvert\mathrm{Re}\,s_j\rvert$, frequency $\mathrm{Im}\,s_j$. Poles of the linearised system = eigenvalues of the Jacobian ([[Fixed Points and Linear Stability]]). Second-order: $s=-\zeta\omega_0\pm i\omega_0\sqrt{1-\zeta^2}$, overshoot $e^{-\pi\zeta/\sqrt{1-\zeta^2}}$.

## In this vault
Phase-plane node/spiral/saddle $\leftrightarrow$ pole pairs ([[Phase Plane and Isoclines]]).

> [!pitfall] Watch out
> Marginal case $\mathrm{Re}\,s=0$ needs the nonlinear terms.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Critical Slowing Down]] · [[Transfer Function]] · [[Fixed Points and Linear Stability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
