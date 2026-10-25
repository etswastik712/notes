---
title: Plane Wave
aliases: ["travelling wave", "momentum eigenstate on a line"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Plane Wave

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Wavefunction_to_Uncertainty (1).pdf#page=2|WU §5]], [[PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1).pdf#page=5|L8 §5]].

> [!intuition] In one picture
> One pure note: a single wavelength fills all of space, so it knows the momentum exactly and the position not at all.

> [!key] Definition
> $\psi(x,t)=Ae^{i(kx-\omega t)}$ with $p=\hbar k$, $E=\hbar\omega$. It has $|\psi|^2=|A|^2$ everywhere (so $\Delta x=\infty$), $\Delta p=0$, and is **not normalisable** on the whole line: an idealised state.

## Properties
- **Operators on it:** $-i\hbar\partial_x\psi=\hbar k\,\psi$, $i\hbar\partial_t\psi=\hbar\omega\,\psi$: it is an eigenstate of $\hat p$ and of $\hat E$ ([[Schrodinger Equation]]).
- **Free-particle dispersion:** $\omega=\hbar k^2/2m$; phase velocity $v/2$, group velocity $v$.
- **Current:** $j=(\hbar k/m)|A|^2=v|A|^2$ ([[Probability Current]]).
- **Direction:** $e^{ikx}$ moves to $+x$ (constant phase $kx-\omega t$); $e^{-ikx}$ to $-x$.

> [!pitfall] A cosine is not a plane wave
> $\cos kx=\tfrac12(e^{ikx}+e^{-ikx})$ is an equal mixture of $+\hbar k$ and $-\hbar k$: a standing wave with $j=0$, not one momentum. Real physical particles are **wave packets** of nearby $k$ ([[Gaussian Wave Packet]]).

Used in: [[QM01 From Waves to Probabilities]], [[QM02 The Schrodinger Equation and Stationary States]]. Related: [[Free Particle]] · [[Fourier Transform and Wave Packets]] · [[Heisenberg Uncertainty Principle]] · [[Probability Current]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
