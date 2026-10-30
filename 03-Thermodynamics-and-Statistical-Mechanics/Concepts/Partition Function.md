---
title: Partition Function
aliases: ["Z", "canonical partition function"]
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Partition Function

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** `Thermo_StatMech_Notes.pdf` §5.3. · 🔵 **extra · beyond:** oscillator and two-level examples.

> [!intuition] In one picture
> The sum of Boltzmann weights over all states: it generates every thermodynamic quantity.

> [!key] Definition
> $Z=\sum_ie^{-\beta E_i}$, $\beta=1/k_BT$. $F=-k_BT\ln Z$; $\langle E\rangle=-\partial_\beta\ln Z$; $S=k_B\ln Z+\langle E\rangle/T$; $C_V=\partial\langle E\rangle/\partial T$; $\mathrm{Var}(E)=k_BT^2C_V$.

## Examples
Two-level: $Z=1+e^{-\beta\varepsilon}$. Oscillator: $Z=e^{-x/2}/(1-e^{-x})$, $x=\hbar\omega/k_BT$. Product rule: independent systems have $Z=Z_1Z_2$ (so $F$ adds).

> [!pitfall] Sum over states, not levels
> Degenerate levels count with their degeneracy $g_i$: $Z=\sum_ig_ie^{-\beta E_i}$.

Used in: [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Canonical Ensemble]] · [[Helmholtz Free Energy]] · [[Planck Mean Energy]] · [[Schottky Anomaly]].

## Added with QM06 (oscillator toolbox)
Oscillator: $Z=\sum_ne^{-\beta\hbar\omega(n+\frac12)}=1/(2\sinh(\hbar\omega\beta/2))$; $P(n)=e^{-\beta E_n}/Z$ is geometric ([[Thermal Harmonic Oscillator]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Moment Generating Function]] (Probability): $Z(\beta)=\sum_i e^{-\beta E_i}$ is the moment generating function of the energy at $t=-\beta$ (up to normalisation); $\langle E\rangle=-\partial_\beta\ln Z$ and $\mathrm{Var}\,E=\partial_\beta^2\ln Z$ are the first two cumulants.
- [[Closure Temperature]] (Landscapes): the Boltzmann factor $e^{-E/RT}$ is the Arrhenius activation law behind $D=D_0e^{-E/RT}$ and hence the closure temperature of a mineral.
