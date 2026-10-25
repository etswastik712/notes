---
title: Number Operator
aliases: ["N operator"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, status/draft]
---
# Number Operator

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** implicit in [[Tutorial2.pdf#page=1|Tutorial II eq. 4]]. · 🔵 **extra · beyond:** the name and the norm calculation.

> [!intuition] In one picture
> It simply counts the rung.

> [!key] Definition
> $\hat N=\hat a_+\hat a_-$, $\hat N\psi_n=n\psi_n$, $\hat H=\hbar\omega(\hat N+\tfrac12)$. $\|\hat a_+\psi_n\|^2=n+1$, $\|\hat a_-\psi_n\|^2=n$.

## Use
Moments follow from $\hat x^2=\frac\hbar{2m\omega}(\hat a_+^2+\hat a_-^2+\hat a_+\hat a_-+\hat a_-\hat a_+)$: only the last two have diagonal elements, $n+(n+1)$, so $\langle x^2\rangle=(n+\tfrac12)\hbar/m\omega$. $\hat a_-\hat a_+=\hat N+1$.

> [!pitfall] $\hat N$ is Hermitian, $\hat a_\pm$ are not
> $\hat N^\dagger=(\hat a_+\hat a_-)^\dagger=\hat a_+\hat a_-$: a genuine observable with integer eigenvalues.

Used in: [[QM05 The Harmonic Oscillator]]. Related: [[Ladder Operators]] · [[Harmonic Oscillator]] · [[Hermitian Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
