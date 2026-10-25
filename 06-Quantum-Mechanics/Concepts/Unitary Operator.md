---
title: Unitary Operator
aliases: ["unitary", "U dagger U = 1"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Unitary Operator

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> A rotation of state space: lengths and angles between states are unchanged.

> [!key] Definition
> $\hat U^\dagger\hat U=\hat U\hat U^\dagger=\hat1$; $\ \langle\hat U\phi|\hat U\psi\rangle=\langle\phi|\psi\rangle$; eigenvalues have modulus 1.

## Examples
Time evolution $e^{-i\hat Ht/\hbar}$ (eigenvalues $e^{-iEt/\hbar}$); the Fourier transform; parity ($\hat P^2=\hat1$, eigenvalues $\pm1$); the displacement operator $\hat D(\alpha)$; basis changes in the two-level system. If $\hat G$ is Hermitian then $e^{i\hat G}$ is unitary: that is why Hermitian generators give norm-preserving flows.

> [!pitfall] Unitary ≠ Hermitian
> A Hermitian operator is an observable (real eigenvalues); a unitary operator is a symmetry/evolution (unit-modulus eigenvalues). Parity is both.

Used in: [[QM06 The Oscillator Toolbox]] §6. Related: [[Hermitian Conjugate]] · [[Time Evolution Operator]] · [[Displacement Operator]] · [[Parity Operator]] · [[Hilbert Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
