---
title: Number Basis
aliases: ["Fock states", "Fock basis", "occupation number basis", "|n>"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Number Basis

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (as $\psi_n$):** [[Harmonic_oscillator.pdf#page=10|lecture pp.10–11]]. · 🔵 **extra · beyond:** the ket notation, matrices and Fock-space language.

> [!intuition] In one picture
> A ladder with one rung per energy level; $|n\rangle$ says "the oscillator is on rung $n$", or "there are $n$ quanta".

> [!key] Definition
> $|n\rangle\equiv\psi_n$ with $\hat N|n\rangle=n|n\rangle$, $\hat a|n\rangle=\sqrt n|n-1\rangle$, $\hat a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle$, $|n\rangle=(\hat a^\dagger)^n|0\rangle/\sqrt{n!}$; $\langle m|n\rangle=\delta_{mn}$, $\sum_n|n\rangle\langle n|=\hat 1$.

## Matrices
$\hat a_{mn}=\sqrt n\,\delta_{m,n-1}$, $\hat a^\dagger=\hat a^{\mathsf T}$, $\hat H=\hbar\omega\,\mathrm{diag}(\tfrac12,\tfrac32,\dots)$, $\hat x=\sigma(\hat a+\hat a^\dagger)$, $\hat p=\tfrac{i\hbar}{2\sigma}(\hat a^\dagger-\hat a)$ with $\sigma=\sqrt{\hbar/2m\omega}$: tridiagonal (see [[Matrix Elements of Position and Momentum]]). This is the infinite version of the $2\times2$ matrices $X,Y,Z$ of [[QM03 States Operators and Measurement]].

## Reading $n$
An energy measurement gives $E_n=(n+\tfrac12)\hbar\omega$ with probability $|c_n|^2$ for $|\psi\rangle=\sum c_n|n\rangle$. For a light mode $n$ counts **photons**, for a crystal mode **phonons**; $\hat a^\dagger$ **creates** and $\hat a$ **annihilates** one quantum ([[Photon Statistics]]).

> [!pitfall] Truncation corrupts the top
> In an $N\times N$ truncation $[\hat a,\hat a^\dagger]$ has diagonal $1,1,\dots,1,-(N-1)$ (the trace of a commutator is $0$). Only use rows with $n\ll N$.

Used in: [[QM06 The Oscillator Toolbox]] §2. Related: [[Ladder Operators]] · [[Number Operator]] · [[Dirac Notation]] · [[Completeness Relation]] · [[Coherent State]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
