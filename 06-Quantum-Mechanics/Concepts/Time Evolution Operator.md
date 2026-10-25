---
title: Time Evolution Operator
aliases: ["propagator", "U(t)", "unitary evolution"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Time Evolution Operator

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (the content, as $\Psi=\sum c_ne^{-iE_nt/\hbar}\psi_n$):** [[PH2113_states_operators_notes.pdf#page=10|SO §9]]. · 🔵 **extra · beyond:** the operator form and oscillator facts.

> [!intuition] In one picture
> A machine that advances any state by time $t$ and never changes its length.

> [!key] Definition
> $|\Psi(t)\rangle=\hat U(t)|\Psi(0)\rangle$, $\ \hat U=e^{-i\hat Ht/\hbar}$ ($\hat H$ time-independent); $\hat U^\dagger\hat U=\hat1$ (**unitary**), so $\langle\Psi|\Psi\rangle$ is conserved.

## In the energy basis
$\hat U|n\rangle=e^{-iE_nt/\hbar}|n\rangle$. For the oscillator $\hat U|n\rangle=e^{-i(n+\frac12)\omega t}|n\rangle$:
- **period** $T=2\pi/\omega$: $e^{-i(2n+1)\pi}=-1$: every state returns to itself up to the global phase $-1$ (perfect revival);
- **half period:** $e^{-i(n+\frac12)\pi}=-i(-1)^n$, i.e. $-i\times$ parity;
- **quarter period:** $e^{-i\pi/4}(-i)^n$, i.e. $e^{-i\pi/4}\times$ the Fourier transform ([[Fourier Invariance of Hermite Functions]]).
With unequal level spacings (box: $E_n\propto n^2$) revivals are partial and have a longer period.

> [!pitfall] Global phase
> $-1$ after a period is unobservable; relative phases decide $|\Psi|^2$.

Used in: [[QM06 The Oscillator Toolbox]] §6.2. Related: [[Unitary Operator]] · [[Heisenberg Picture]] · [[Time Evolution of a Superposition]] · [[Stationary State]] · [[Schrodinger Equation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
