---
title: Heisenberg Uncertainty Principle
aliases: ["uncertainty principle", "uncertainty relation", "Heisenberg relation"]
subject: qm
type: concept
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Heisenberg Uncertainty Principle

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1).pdf#page=1|L8 §1]], [[PH2113_Lecture6-7.pdf#page=2|L7 §5]], [[PH2113_states_operators_notes.pdf#page=5|SO §5]]. · 🟡 **extra · book:** the proof from the commutator (Griffiths §3.4). · 🔵 **extra · beyond:** written-out proof; numerical scales.

> [!intuition] In one picture
> A narrow thing is made of many wavelengths, and wavelength is momentum. You cannot have both a sharp place and a sharp speed.

> [!key] Definition
> $\Delta x\,\Delta p\ge\hbar/2$, where $\Delta x,\Delta p$ are the standard deviations of position and momentum outcomes for identically prepared systems. In general $\Delta A\,\Delta B\ge\tfrac12|\langle[\hat A,\hat B]\rangle|$ ([[Generalised Uncertainty Principle]]).

## Meaning and numbers
**Not** a statement about clumsy instruments: the state itself has no arbitrarily sharp pair. It follows from $\Delta x\,\Delta k\ge\tfrac12$ (a Fourier fact) and $p=\hbar k$.

> [!example] Scales (recomputed)
> Tennis ball (57 g) at 1 mm: $\Delta v\ge\hbar/2m\Delta x=9\times10^{-31}$ m/s. Electron at $a_0$: $\Delta v\ge1.1\times10^{6}$ m/s. Particle-in-a-box ground state: $\Delta x\,\Delta p=0.568\hbar$. Oscillator: $(n+\tfrac12)\hbar$.

> [!pitfall] Do not test it on the extremes
> A plane wave ($\Delta p=0$, $\Delta x=\infty$) and a delta function ($\Delta x=0$, $\Delta p=\infty$) are not normalisable states with finite spreads. Use the Gaussian (equality) or the box/oscillator (strict inequality).

Used in: [[QM01 From Waves to Probabilities]], [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]]. Related: [[Gaussian Wave Packet]] · [[Fourier Transform and Wave Packets]] · [[Commutator]] · [[Hydrogen Atom Stability]].

## Added with QM06 (oscillator toolbox)
$\Delta x\Delta p=(n+\tfrac12)\hbar$ for $|n\rangle$ (minimum only for $n=0$); equality $\hbar/2$ also for every coherent and squeezed state ([[Minimum Uncertainty State]]); the principle gives the exact oscillator zero-point energy ([[Zero-Point Energy]]).

> [!connection] See also
> The Fourier proof of $\Delta x\,\Delta k\ge\frac12$ (Cauchy–Schwarz, equality only for Gaussians): [[Fourier and Laplace Transforms]] §3.5.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
