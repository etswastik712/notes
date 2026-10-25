---
title: Zero-Point Energy
aliases: ["ground-state energy", "confinement energy"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, status/draft]
---
# Zero-Point Energy

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Particle_in_a_box.pdf#page=5|box lecture p.5]], [[tutorial1.pdf#page=1|Tutorial I Q5]]. · 🔵 **extra · beyond:** the oscillator and ring comparison.

> [!intuition] In one picture
> Squeeze a wave and it must have curvature, so even the lowest state carries kinetic energy.

> [!key] Definition
> The lowest energy of a confined system is above the potential minimum: box $E_1=\pi^2\hbar^2/2ma^2$, oscillator $E_0=\tfrac12\hbar\omega$, hydrogen estimate $-13.6$ eV. In general $E>V_{\min}$ for every normalisable state.

## Why and numbers
Confinement to $\Delta x$ forces $\Delta p\gtrsim\hbar/2\Delta x$, hence $E\gtrsim\hbar^2/8m\Delta x^2$. If $E<V_{\min}$ then $\psi''/\psi>0$ everywhere and $\psi$ blows up at an end: no normalisable state (Tutorial I Q5). Oscillator: $\Delta x\Delta p=(n+\tfrac12)\hbar$, $\langle V\rangle=\langle T\rangle=E/2$.

> [!pitfall] The ring has none
> The periodic ring allows the constant $n=0$ state with $E=0$: no confinement, no zero-point energy ([[Particle on a Ring]]).

Used in: [[QM01 From Waves to Probabilities]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]]. Related: [[Heisenberg Uncertainty Principle]] · [[Particle in a Box]] · [[Hydrogen Atom Stability]] · [[Harmonic Oscillator]].

## Added with QM06 (oscillator toolbox)
**Oscillator, sharp:** the uncertainty principle gives $E\ge\hbar^2/8m\,\Delta x^2+\tfrac12m\omega^2\Delta x^2\ge\tfrac12\hbar\omega$, with equality for the Gaussian ground state ($\Delta x^2=\hbar/2m\omega$; numerically $0.500000$). **Thermal:** the $\tfrac12\hbar\omega$ never contributes to the heat capacity ([[Thermal Harmonic Oscillator]]). **Virial:** it is half kinetic, half potential, $\langle T\rangle=\langle V\rangle=\tfrac14\hbar\omega$ ([[Virial Theorem]]). **3-D:** $\tfrac32\hbar\omega$ ([[Isotropic Oscillator and Degeneracy]]). See [[Minimum Uncertainty State]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
