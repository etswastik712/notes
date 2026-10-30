---
title: Generalised Uncertainty Principle
aliases: ["Robertson uncertainty relation", "commutator uncertainty bound"]
subject: qm
type: concept
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Generalised Uncertainty Principle

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** stated in [[PH2113_states_operators_notes.pdf#page=5|SO §5]] and [[PH2113_matrices_expectation_uncertainty.pdf#page=3|MX §8]]. · 🟡 **extra · book:** the Cauchy–Schwarz proof (Griffiths §3.4). · 🔵 **extra · beyond:** the proof written out.

> [!intuition] In one picture
> The more the commutator of two observables averages to, the less sharp both can be together.

> [!key] Definition
> $\Delta A\,\Delta B\ge\tfrac12\big|\langle[\hat A,\hat B]\rangle\big|$. For $\hat x,\hat p$: $\hbar/2$.

## Proof idea and examples
Let $f=(\hat A-\langle A\rangle)\psi$, $g=(\hat B-\langle B\rangle)\psi$. Cauchy–Schwarz: $(\Delta A)^2(\Delta B)^2\ge|\langle f|g\rangle|^2\ge(\mathrm{Im}\langle f|g\rangle)^2=\tfrac14|\langle[\hat A,\hat B]\rangle|^2$.

> [!example] Two-level checks
> $|{+z}\rangle$: $\Delta X\,\Delta Y=1=\tfrac12|\langle[X,Y]\rangle|$ (saturated). $(\tfrac{\sqrt3}2,\tfrac12)$: $\Delta Z\,\Delta X=\tfrac{\sqrt3}4=0.433$ vs bound $|\langle Y\rangle|=0$ (satisfied). The family $\cos\frac\theta2|{+z}\rangle+\sin\frac\theta2|{-z}\rangle$ saturates the $X,Y$ bound for every $\theta$.

> [!pitfall] The bound depends on the state
> The right side is $\langle[\hat A,\hat B]\rangle$, a state-dependent number unless the commutator is a constant ($x,p$). If it vanishes in that state the bound is empty, not violated.

Used in: [[QM03 States Operators and Measurement]]. Related: [[Heisenberg Uncertainty Principle]] · [[Commutator]] · [[Uncertainty of an Observable]] · [[Pauli Matrices]].

See also: [[Cauchy-Schwarz Inequality]] (the inequality behind it; the probability version is $|\rho|\le1$ in [[PR07 Sums of Independent Variables Covariance and Correlation]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
