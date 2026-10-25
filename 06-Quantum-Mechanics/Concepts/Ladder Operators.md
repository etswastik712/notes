---
title: Ladder Operators
aliases: ["raising and lowering operators", "creation and annihilation operators"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Ladder Operators

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Tutorial2.pdf#page=1|Tutorial II (eqs. 1–5)]].

> [!intuition] In one picture
> Two operators that step the energy up or down by exactly $\hbar\omega$; the whole spectrum is one rung plus a staircase.

> [!key] Definition
> $\hat a_\pm=\dfrac{1}{\sqrt{2\hbar m\omega}}(m\omega\hat x\mp i\hat p)$, $[\hat a_-,\hat a_+]=1$, $\hat H=\hbar\omega(\hat a_+\hat a_-+\tfrac12)$, $[\hat H,\hat a_\pm]=\pm\hbar\omega\hat a_\pm$, $\hat a_+\psi_n=\sqrt{n+1}\psi_{n+1}$, $\hat a_-\psi_n=\sqrt n\psi_{n-1}$, $\hat a_-\psi_0=0$.

## Proof of the ladder property
$[\hat H,\hat a_-]=\hbar\omega[\hat a_+,\hat a_-]\hat a_-=-\hbar\omega\hat a_-$, so $\hat H\hat a_-\psi=(E-\hbar\omega)\hat a_-\psi$. Inverse: $\hat x=\sqrt{\hbar/2m\omega}(\hat a_++\hat a_-)$, $\hat p=i\sqrt{m\hbar\omega/2}(\hat a_+-\hat a_-)$.

> [!pitfall] Not observables
> $\hat a_\pm$ are not Hermitian ($\hat a_\pm^\dagger=\hat a_\mp$). The ladder stops at $\hat a_-\psi_0=0$ (the zero vector has no energy), which is how the bottom rung is found.

Used in: [[QM05 The Harmonic Oscillator]]. Related: [[Harmonic Oscillator]] · [[Number Operator]] · [[Canonical Commutation Relation]] · [[Commutator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
