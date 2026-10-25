---
title: Normalisation of a Wavefunction
aliases: ["normalisation", "normalization"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Normalisation of a Wavefunction

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Wavefunction_to_Uncertainty (1).pdf#page=1|WU §2]], [[Particle_in_a_box.pdf#page=5|box lecture pp.5–6]].

> [!intuition] In one picture
> Scale the amplitude so that the total probability is exactly 1.

> [!key] Definition
> Choose the constant $A$ in $\psi$ so that $\int|\psi|^2\mathrm dx=1$. It fixes $|A|$ only; the overall phase is free.

## Standard constants
Box $\sqrt{2/a}$ ($\int_0^a\sin^2(n\pi x/a)=a/2$); ring $1/\sqrt L$; Gaussian $(2\pi\sigma^2)^{-1/4}$; $e^{-|x|/a}$: $1/\sqrt a$; oscillator ground state $(m\omega/\pi\hbar)^{1/4}$.

> [!pitfall] A plane wave cannot be normalised on the line
> $\int|A|^2\mathrm dx$ diverges; on a ring of length $L$ the same wave is normalised by $1/\sqrt L$. Normalisability depends on the domain.

Used in: [[QM01 From Waves to Probabilities]], [[QM02 The Schrodinger Equation and Stationary States]], [[QM04 The Particle in a Box]]. Related: [[Born Rule]] · [[Admissible Wavefunction]] · [[Orthonormality of Eigenfunctions]] · [[Gaussian Integral]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
