---
title: Time Evolution of a Superposition
aliases: ["Bohr frequency", "time-dependent superposition"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Time Evolution of a Superposition

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=10|SO §9]], [[tutorial1.pdf#page=1|Tutorial I Q3]].

> [!intuition] In one picture
> Every energy component spins at its own rate $E_n/\hbar$; the density moves when the components fall out of step.

> [!key] Definition
> $\Psi(x,t)=\sum_nc_ne^{-iE_nt/\hbar}\psi_n(x)$. $|c_n|^2$, $\langle E\rangle$, $\Delta E$ are constant; $|\Psi|^2$ changes at the **Bohr frequencies** $(E_m-E_n)/\hbar$.

## Examples
> [!example] Box, $\tfrac1{\sqrt2}(\psi_1+\psi_2)$
> $|\Psi|^2=\tfrac12(\psi_1^2+\psi_2^2)+\psi_1\psi_2\cos(3E_1t/\hbar)$; $\langle x\rangle=\frac a2-\frac{16a}{9\pi^2}\cos(3E_1t/\hbar)$ (amplitude $0.180a$). Left-heavy at $t=0$, symmetric at $\pi\hbar/2E_1$, right-heavy at $\pi\hbar/E_1$, back at $2\pi\hbar/E_1$.
> **Ring, $E_0=0$:** $\tfrac1{\sqrt2}(\psi_0+\psi_1)$ gives $|\Psi|^2=\tfrac1L[1+\cos(kx-\omega t)]$, a pattern moving at $\hbar k/2m$. **Oscillator:** $\tfrac1{\sqrt2}(\psi_0+\psi_1)$: $\langle x\rangle=\sqrt{\hbar/2m\omega}\cos\omega t$.

> [!pitfall] Same energy: no motion
> $\tfrac1{\sqrt2}(\psi_n+\psi_{-n})$ has one common phase, so it is stationary.

Used in: [[QM02 The Schrodinger Equation and Stationary States]], [[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]]. Related: [[Stationary State]] · [[Global and Relative Phase]] · [[Superposition Principle]] · [[Particle in a Box]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
