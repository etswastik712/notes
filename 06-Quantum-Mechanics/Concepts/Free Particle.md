---
title: Free Particle
aliases: ["free particle on a line", "V = 0"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Free Particle

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture9_FreeParticle_Ring_GeneralProperties.pdf#page=2|L9 §2]].

> [!intuition] In one picture
> With no force there is nothing to restrict the wavelength, so every energy is allowed.

> [!key] Definition
> $V=0$: $\psi=Ae^{ikx}+Be^{-ikx}$, $E=\hbar^2k^2/2m\ge0$ with $k$ **continuous**: a continuous spectrum. A localised particle is a wave packet of nearby $k$.

## Properties
- $e^{ikx}$ moves right (constant phase $kx-\omega t$), $e^{-ikx}$ left; choosing $B=0$ prepares a right-mover.
- Dispersion $\omega=\hbar k^2/2m$: phase velocity $v/2$, group velocity $v$.
- $\hat H=\hat p^2/2m$ commutes with $\hat p$: $E$ and $p$ are simultaneously definite ([[Commutator]]).

> [!pitfall] Quantum does not mean discrete
> The equation alone gives a continuum. Discreteness appears only with boundary conditions: $x\equiv x+L$ gives $k_n=2\pi n/L$ ([[Particle on a Ring]]), walls give the box.

Used in: [[QM01 From Waves to Probabilities]], [[QM02 The Schrodinger Equation and Stationary States]]. Related: [[Plane Wave]] · [[Gaussian Wave Packet]] · [[Boundary Conditions and Quantisation]] · [[Particle on a Ring]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
