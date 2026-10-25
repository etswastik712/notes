---
title: Hermitian Conjugate
aliases: ["adjoint", "dagger", "Hermitian adjoint", "adjoint operator"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Hermitian Conjugate

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (as the identity $\int f^*\hat a_+g=\int(\hat a_-f)^*g$):** [[Harmonic_oscillator.pdf#page=9|lecture p.9]]. · 🔵 **extra · beyond:** the general definition and rules.

> [!intuition] In one picture
> For matrices: transpose and conjugate. For operators: the thing that can be moved to the other side of a bracket at the cost of a dagger.

> [!key] Definition
> $\langle\phi|\hat A\psi\rangle=\langle\hat A^\dagger\phi|\psi\rangle$ for all $\phi,\psi$. For matrices $(A^\dagger)_{mn}=A_{nm}^*$. $\hat A$ is **Hermitian** if $\hat A^\dagger=\hat A$.

## Rules
$(\hat A\hat B)^\dagger=\hat B^\dagger\hat A^\dagger$, $(c\hat A)^\dagger=c^*\hat A^\dagger$, $(\hat A^\dagger)^\dagger=\hat A$. A commutator of Hermitian operators is **anti-Hermitian**: $[\hat A,\hat B]^\dagger=[\hat B,\hat A]=-[\hat A,\hat B]$, so $i[\hat A,\hat B]$ is Hermitian (consistent with $[\hat x,\hat p]=i\hbar$).

## The oscillator
$\hat x,\hat p$ Hermitian and $\hat a=(m\omega\hat x+i\hat p)/\sqrt{2\hbar m\omega}$ give $\hat a^\dagger=(m\omega\hat x-i\hat p)/\sqrt{2\hbar m\omega}=\hat a_+$. The lecture proves $\int f^*\hat a_+g=\int(\hat a_-f)^*g$ by integrating by parts with vanishing boundary terms. So $\hat N=\hat a^\dagger\hat a$ is Hermitian and $\|\hat a\psi\|^2=\langle\psi|\hat a^\dagger\hat a|\psi\rangle=\langle N\rangle\ge0$, which is why $\hat a\psi_0=0$.

> [!pitfall] Hermitian is not the same as real
> $\hat p=-i\hbar\,\mathrm d/\mathrm dx$ has an $i$ and is Hermitian; $\mathrm d/\mathrm dx$ alone is anti-Hermitian. Boundary terms must vanish for the integration by parts.

Used in: [[QM05 The Harmonic Oscillator]], [[QM06 The Oscillator Toolbox]] §2. Related: [[Hermitian Operator]] · [[Ladder Operators]] · [[Dirac Notation]] · [[Commutator]] · [[Unitary Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
