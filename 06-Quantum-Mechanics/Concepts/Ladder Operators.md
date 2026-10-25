---
title: Ladder Operators
aliases: ["raising and lowering operators", "creation and annihilation operators", "a and a dagger", "a plus and a minus"]
subject: qm
type: concept
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes, book, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, extra/beyond, src/lecture-notes, src/book, src/own-notes, status/draft]
---
# Ladder Operators

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Harmonic_oscillator.pdf#page=2|oscillator lecture pp.2–11]] (factorisation, ladder property, ground state, $c_n,d_n$, the adjoint identity), [[Tutorial2.pdf#page=1|Tutorial II (eqs. 1–5)]], [[Tutorial3.pdf#page=1|Tutorial III eqs. 1–6]]. · 🟡 **extra · book:** Griffiths §2.3.1 ([[Griffiths - Introduction to quantum mechanics.pdf#page=47|PDF p.47]]). · 🔵 **extra · beyond:** operator identities, matrices, Heisenberg and coherent-state uses.

> [!intuition] In one picture
> Two operators that step the energy up or down by exactly $\hbar\omega$; the whole spectrum is one rung plus a staircase, and the bottom step is where the staircase stops.

> [!key] Definition
> $\hat a_\pm=\dfrac1{\sqrt{2\hbar m\omega}}(m\omega\hat x\mp i\hat p)$, i.e. $\hat a\equiv\hat a_-$ (lowering, annihilation) and $\hat a^\dagger\equiv\hat a_+$ (raising, creation). $[\hat a,\hat a^\dagger]=1$, $\ \hat H=\hbar\omega(\hat a^\dagger\hat a+\tfrac12)$, $\ \hat a\psi_0=0$, $\ \hat a^\dagger\psi_n=\sqrt{n+1}\,\psi_{n+1}$, $\ \hat a\psi_n=\sqrt n\,\psi_{n-1}$.

## Where they come from
$\hat H=\frac1{2m}[\hat p^2+(m\omega\hat x)^2]$ is a sum of two squares, and $a^2+b^2=(ia+b)(-ia+b)$. The factors are $\hat a_\mp$; non-commutativity leaves $\hat a_-\hat a_+=\hat H/\hbar\omega+\tfrac12$ and $\hat a_+\hat a_-=\hat H/\hbar\omega-\tfrac12$, so $[\hat a_-,\hat a_+]=1$ (lecture p.3).

## The ladder property (two proofs)
- **Direct** (lecture pp.4–5): $\hat H\hat a_+\psi=\hbar\omega\,\hat a_+(\hat a_-\hat a_++\tfrac12)\psi=\hat a_+(\hat H+\hbar\omega)\psi=(E+\hbar\omega)\hat a_+\psi$; likewise $\hat H\hat a_-\psi=(E-\hbar\omega)\hat a_-\psi$.
- **Commutators:** $[\hat H,\hat a_\pm]=\pm\hbar\omega\,\hat a_\pm$, so $\hat H\hat a_\pm\psi=\hat a_\pm\hat H\psi\pm\hbar\omega\hat a_\pm\psi$.

## Why the ladder stops, and the constants
$\hat a^\dagger=\hat a_-^{\,\dagger}$ gives $\|\hat a\psi\|^2=\langle\psi|\hat a^\dagger\hat a|\psi\rangle\ge0$, so $\langle\hat H\rangle\ge\tfrac12\hbar\omega$ and the lowest state must obey $\hat a\psi_0=0$ (the zero vector is no state), a first-order equation giving $\psi_0\propto e^{-m\omega x^2/2\hbar}$. From $\langle\hat H\rangle=E_n$: $\|\hat a\psi_n\|^2=n$, $\|\hat a^\dagger\psi_n\|^2=n+1$, hence the constants $\sqrt n$, $\sqrt{n+1}$ and $\psi_n=(\hat a^\dagger)^n\psi_0/\sqrt{n!}$ ([[Normalisation of a Wavefunction]]).

## Operator identities (derived from $[\hat a,\hat a^\dagger]=1$)
$\hat N=\hat a^\dagger\hat a$, $\ \hat a\hat a^\dagger=\hat N+1$; $\ [\hat N,\hat a]=-\hat a$, $[\hat N,\hat a^\dagger]=\hat a^\dagger$; $\ [\hat a,(\hat a^\dagger)^k]=k(\hat a^\dagger)^{k-1}$ (used to prove orthogonality in QM05 §10). In terms of position and momentum, $\hat x=\sigma(\hat a+\hat a^\dagger)$, $\hat p=\frac{i\hbar}{2\sigma}(\hat a^\dagger-\hat a)$, $\sigma^2=\hbar/2m\omega$. In $\xi$-space $\hat a_\pm=\frac1{\sqrt2}(\xi\mp\partial_\xi)$, and these act on $H_n e^{-\xi^2/2}$ as $H_n\to H_{n+1}$ (raising) and $H_n\to2nH_{n-1}$ (lowering) ([[Hermite Generating Function and Recurrences]]).

## Where they appear again
In momentum space they are $\pm i\times$ the same operators ([[Fourier Invariance of Hermite Functions]]); in the Heisenberg picture $\hat a(t)=\hat ae^{-i\omega t}$ ([[Heisenberg Picture]]); their eigenstates are the **coherent states** ([[Coherent State]]); the algebra $[\hat a,\hat a^\dagger]=1$ is the **Heisenberg algebra** that reappears for every field mode and, in a different guise, in angular momentum (not in the folder). Matrix elements: [[Matrix Elements of Position and Momentum]]; basis: [[Number Basis]]; ordering rules: [[Normal Ordering]].

> [!pitfall] Not observables, and a sign convention
> $\hat a_\pm$ are **not** Hermitian ($\hat a_\pm^\dagger=\hat a_\mp$), so they are not measured. The lecture's page 9 writes $\hat a_+$ with the sign of $\hat a_-$ (a slip, flagged in [[QM05 The Harmonic Oscillator]] §5). Books such as Sakurai use $\hat a$ for lowering with the same convention; some texts swap the roles of $\hat x$ and $\hat p$ and get $\hat a$ with a factor $i$.

Used in: [[QM05 The Harmonic Oscillator]], [[QM06 The Oscillator Toolbox]]. Related: [[Harmonic Oscillator]] · [[Number Operator]] · [[Number Basis]] · [[Hermite Polynomials]] · [[Hermitian Conjugate]] · [[Canonical Commutation Relation]] · [[Commutator]] · [[Coherent State]] · [[Heisenberg Picture]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
