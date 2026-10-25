---
title: Schrodinger Equation
aliases: ["Schrödinger equation", "TDSE", "time-dependent Schrödinger equation"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Schrodinger Equation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1).pdf#page=5|L8 §6–10]], [[PH2113_Lecture6-7.pdf#page=4|L7 §8–12]].

> [!intuition] In one picture
> The law of motion of the wavefunction: it rotates in phase at a rate set by the energy, so it never decays, only evolves.

> [!key] Definition
> $i\hbar\,\dfrac{\partial\psi}{\partial t}=-\dfrac{\hbar^2}{2m}\dfrac{\partial^2\psi}{\partial x^2}+V(x,t)\,\psi=\hat H\psi$, a **postulate** of non-relativistic quantum mechanics (in 3-D, $\partial_x^2\to\nabla^2$). Its form is motivated by $E\to i\hbar\partial_t$, $p\to-i\hbar\partial_x$ in $E=p^2/2m+V$.

## What it does
Given $\psi(x,0)$ it fixes $\psi(x,t)$. It is **linear** (superpositions solve it) and, for real $V$, **unitary**: probability is conserved ([[Probability Current]]). The $i$ makes $\psi$ oscillate rather than diffuse.

> [!example] Free-particle check
> $\psi=Ae^{i(kx-\omega t)}$, $V=0$: $\hbar\omega=\hbar^2k^2/2m$, i.e. $\omega=\hbar k^2/2m$. This is a **check** that the equation reproduces $E=p^2/2m$, not a derivation of it.

> [!pitfall] Two different questions
> "Is $\psi$ an admissible state?" ([[Admissible Wavefunction]]) is not "does $\psi$ solve the equation for this $V$?" A normalisable function need not be an energy eigenfunction; and the equation alone does not make energies discrete (boundary conditions do: [[Boundary Conditions and Quantisation]]).

Used in: [[QM02 The Schrodinger Equation and Stationary States]], [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]]. Related: [[Time-Independent Schrodinger Equation]] · [[Stationary State]] · [[Probability Current]] · [[Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
