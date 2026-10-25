---
title: Correspondence Principle
aliases: ["classical limit"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Correspondence Principle

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_states_operators_notes.pdf#page=1|SO §1.1]], [[Particle_in_a_box.pdf#page=5|box lecture p.5]].

> [!intuition] In one picture
> Quantum rules don't switch off for big things; they become too fine to see.

> [!key] Definition
> For large quantum numbers or large systems, quantum predictions merge into classical ones: level spacing $\Delta E/E\to0$, $|\psi_n|^2$ averages to the classical density, $\Delta x\to$ classical.

## Examples (recomputed)
Ring of 1 cm: $E_1=1.5\times10^{-14}$ eV, far below $k_BT$. Marble (1 g, 10 cm box, 1 cm/s): $n\approx3\times10^{27}$, $\Delta E/E\sim7\times10^{-28}$. Box: $a|\psi_n|^2$ averages $1$ (classical $1/a$) and $\Delta x\to a/\sqrt{12}$. Oscillator $n=10$: density oscillates about $1/\pi\sqrt{x_t^2-x^2}$.

> [!pitfall] Large $n$ is not the same as $\hbar\to0$
> The principle says averages match; single eigenstates still have nodes and tunnelling into forbidden regions (oscillator ground state: $15.7\%$ beyond the turning points).

Used in: [[QM02 The Schrodinger Equation and Stationary States]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]]. Related: [[Energy Quantisation]] · [[Particle on a Ring]] · [[Particle in a Box]] · [[Harmonic Oscillator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
