---
title: Heisenberg Picture
aliases: ["Heisenberg equation of motion", "operators evolve"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Heisenberg Picture

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond** (the course uses the Schrödinger picture).

> [!intuition] In one picture
> Instead of letting the state move and the operators stand still, let the operators move and the state stand still; every expectation value is identical.

> [!key] Definition
> $\hat A_H(t)=e^{i\hat Ht/\hbar}\hat Ae^{-i\hat Ht/\hbar}$, $\ \dfrac{\mathrm d\hat A_H}{\mathrm dt}=\dfrac i\hbar[\hat H,\hat A_H]$ (time-independent $\hat H$, $\hat A$).

## Oscillator
$[\hat H,\hat a]=-\hbar\omega\hat a\Rightarrow\hat a(t)=\hat ae^{-i\omega t}$, hence $\hat x(t)=\hat x\cos\omega t+\dfrac{\hat p}{m\omega}\sin\omega t$ and $\hat p(t)=\hat p\cos\omega t-m\omega\hat x\sin\omega t$: the classical solution as an operator identity, valid in every state. Verified with matrix exponentials (errors $\sim10^{-14}$), and $[\hat H,\hat x]=-i\hat p$, $[\hat H,\hat p]=i\hat x$ in units $\hbar=m=\omega=1$.

## Equivalence
$\langle\Psi(t)|\hat A|\Psi(t)\rangle=\langle\Psi(0)|\hat A_H(t)|\Psi(0)\rangle$ because $|\Psi(t)\rangle=\hat U|\Psi(0)\rangle$ ([[Time Evolution Operator]]).

> [!pitfall] Commutators are time-dependent too
> $[\hat x(t),\hat p(t)]=i\hbar$ at every time (unitary conjugation preserves it), but $[\hat x(t),\hat x(0)]\ne0$.

Used in: [[QM06 The Oscillator Toolbox]] §6.2. Related: [[Ehrenfest Theorem]] · [[Ladder Operators]] · [[Commutator]] · [[Unitary Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
