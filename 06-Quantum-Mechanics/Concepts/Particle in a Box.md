---
title: Particle in a Box
aliases: ["infinite square well", "Infinite Square Well", "infinite well"]
subject: qm
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Particle in a Box

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Particle_in_a_box.pdf#page=2|handwritten pp.2–9]], [[PH2113_states_operators_notes.pdf#page=9|SO §8.2]], [[tutorial1.pdf#page=1|Tutorial I]]. · 🟡 **extra · book:** the finite well (Griffiths §2.6).

> [!intuition] In one picture
> A standing wave that must be zero at both walls: only whole numbers of half wavelengths fit.

> [!key] Definition
> $V=0$ for $0<x<a$, $\infty$ elsewhere: $\psi_n=\sqrt{2/a}\,\sin(n\pi x/a)$, $E_n=\dfrac{n^2\pi^2\hbar^2}{2ma^2}=n^2E_1$, $n=1,2,3,\dots$ Boundary conditions $\psi(0)=\psi(a)=0$ quantise the energy.

## Results (recomputed)
- $n-1$ nodes; parity $(-1)^{n+1}$ about the centre; stationary $\Psi_n=\psi_ne^{-iE_nt/\hbar}$.
- $\langle x\rangle=a/2$, $\Delta x=a\sqrt{1/12-1/2n^2\pi^2}$, $\langle p\rangle=0$, $\Delta p=n\pi\hbar/a$; $\Delta x\,\Delta p=0.568\hbar$ for $n=1$.
- Electron, $a=1$ nm: $E_1=0.376$ eV, $E_2=1.50$ eV, $1\to2$ photon $1.10$ µm. Classical: uniform density $1/a$, any energy.

> [!pitfall] Not an extra postulate, and $E_1\ne0$
> Quantisation follows from the boundary conditions; $n=0$ is not a state ($\psi\equiv0$). The lowest energy $\pi^2\hbar^2/2ma^2>0$ is the zero-point energy ([[Zero-Point Energy]]).

Used in: [[QM02 The Schrodinger Equation and Stationary States]], [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]]. Related: [[Energy Quantisation]] · [[Zero-Point Energy]] · [[Normalisation of a Wavefunction]] · [[Orthonormality of Eigenfunctions]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
