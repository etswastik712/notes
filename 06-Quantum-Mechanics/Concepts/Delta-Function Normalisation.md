---
title: Delta-Function Normalisation
aliases: ["continuum normalisation", "delta normalisation", "normalising plane waves"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Delta-Function Normalisation

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (the problem):** a plane wave cannot be normalised on a line ([[PH2113_Wavefunction_to_Uncertainty (1).pdf|WU]]). · 🔵 **extra · beyond:** the standard fix.

> [!intuition] In one picture
> Plane waves are not states but a basis for states; their "norm" is a spike, not a number.

> [!key] Definition
> $\phi_k(x)=\dfrac{e^{ikx}}{\sqrt{2\pi}}$: $\ \langle\phi_k|\phi_{k\prime}\rangle=\displaystyle\int\frac{e^{i(k\prime-k)x}}{2\pi}\mathrm dx=\delta(k-k\prime)$; in momentum, $\phi_p=e^{ipx/\hbar}/\sqrt{2\pi\hbar}$, $\langle\phi_p|\phi_{p\prime}\rangle=\delta(p-p\prime)$.

## Use
Physical states are packets $\psi(x)=\int c(k)\phi_k\,\mathrm dk$ with $\int|c|^2\mathrm dk=1$ and $|c(k)|^2\mathrm dk$ the probability of a wavenumber in $\mathrm dk$ ([[Fourier Transform and Wave Packets]]). On a ring of length $L$ the same wave is **box-normalised** to $1/\sqrt L$ and $\delta(k-k')\to\delta_{kk'}$ with $\Delta k=2\pi/L$; $L\to\infty$ gives the continuum.

> [!pitfall] $\delta(0)$ is infinite
> $\langle\phi_k|\phi_k\rangle=\delta(0)=L/2\pi$; never normalise a plane wave to 1 on the whole line ([[Dirac Delta Function]]).

Used in: [[QM06 The Oscillator Toolbox]] §1. Related: [[Free Particle]] · [[Plane Wave]] · [[Normalisation of a Wavefunction]] · [[Dirac Delta Function]] · [[Particle on a Ring]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
