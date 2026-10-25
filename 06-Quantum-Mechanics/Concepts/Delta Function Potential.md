---
title: Delta Function Potential
aliases: ["delta potential", "delta well"]
subject: qm
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Delta Function Potential

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf#page=2|Tutorial P2]] (the matching condition). · 🟡 **extra · book:** the bound state (Griffiths §2.5).

> [!intuition] In one picture
> An infinitely thin, infinitely strong spike: the wavefunction stays continuous but its slope jumps.

> [!key] Definition
> For $V=\lambda\delta(x-x_0)$: $\psi'(x_0^+)-\psi'(x_0^-)=\dfrac{2m\lambda}{\hbar^2}\psi(x_0)$ (integrate the TISE across $x_0$).

## Bound state
For $V=-\alpha\delta(x)$: $\psi=\sqrt\kappa e^{-\kappa|x|}$ with $\kappa=m\alpha/\hbar^2$ and $E=-m\alpha^2/2\hbar^2$ (one bound state; in units $\hbar=m=\alpha=1$, $E=-\tfrac12$). For $\alpha=1$ eV nm and an electron: $\kappa=13.1$ nm$^{-1}$, $E=-6.6$ eV, decay length $0.076$ nm.

> [!pitfall] A cusp is not automatically forbidden
> A finite jump in $V$ gives continuous $\psi'$; only a singular potential such as $\delta$ allows a kink. A repulsive delta has no bound state.

Used in: [[QM02 The Schrodinger Equation and Stationary States]]. Related: [[Admissible Wavefunction]] · [[Time-Independent Schrodinger Equation]] · [[Boundary Conditions and Quantisation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
