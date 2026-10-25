---
title: Admissible Wavefunction
aliases: ["acceptable wavefunction", "physical wavefunction", "normalisable state"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Admissible Wavefunction

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1).pdf#page=3|L8 §3–5]], [[PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf#page=1|Tutorial P1]].

> [!intuition] In one picture
> Before checking a candidate against the equation, check it can be a probability amplitude at all.

> [!key] Definition
> An ordinary state is **single-valued**, **normalisable** ($\int|\psi|^2<\infty$), and obeys the problem's boundary conditions; for finite non-singular $V$, $\psi$ and $\psi'$ are continuous.

## Verdicts (on $(-\infty,\infty)$)
Allowed: $e^{-ax^2}$, $e^{-a|x|}$ (cusp), $1/(1+|x|)$. Not allowed: $e^{ax^2}$, $1/\sqrt{1+|x|}$ ($|\psi|^2\sim1/|x|$, log divergence), $1/x$ through the origin, $e^{ikx}$ (not normalisable), $e^{i\phi/2}$ on a ring (not single-valued). A top hat is normalisable but has infinite kinetic energy (discontinuity).

> [!pitfall] "Tends to zero" is not enough
> Normalisability needs the tail to fall fast enough; and the verdict depends on the domain: a constant is not normalisable on the line but is on $[0,L]$.

Used in: [[QM02 The Schrodinger Equation and Stationary States]]. Related: [[Wavefunction]] · [[Born Rule]] · [[Delta Function Potential]] · [[Normalisation of a Wavefunction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
