---
title: Equipartition of Energy
aliases: ["equipartition theorem"]
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Equipartition of Energy

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** `KTG_Chapter.pdf` §1.5; `Thermo_StatMech_Notes.pdf` §5.5. · 🔵 **extra · beyond:** the freeze-out criterion.

> [!intuition] In one picture
> At equilibrium every independent quadratic way of storing energy gets the same share, $\tfrac12k_BT$.

> [!key] Definition
> Classically, each quadratic degree of freedom contributes $\tfrac12k_BT$ to the mean energy: $E=\tfrac f2Nk_BT$, $C_V=\tfrac f2Nk_B$. An oscillator has two (kinetic and potential): $E=k_BT$.

## Proof for one term and its limit
$\langle\tfrac12\kappa x^2\rangle$ with weight $e^{-\kappa x^2/2k_BT}$ equals $\tfrac12k_BT$ ([[Gaussian Integral]]). Quantum: a mode with $x=\hbar\omega/k_BT\gg1$ is **frozen** ($C\to k_Bx^2e^{-x}$); $x\to0$ recovers equipartition. CO$_2$ bend at 288 K: $x=3.33$, $C=0.43k_B$.

> [!pitfall] Not valid at low $T$
> Heat capacities of solids and diatomic vibrations fall below the equipartition value at low $T$ (and must vanish at $T\to0$: third law).

Used in: [[TH03 The Ideal Gas and Adiabatic Processes]], [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Ratio of Specific Heats]] · [[Partition Function]] · [[Heat Capacity]] · [[Maxwell-Boltzmann Distribution]].

## Added with QM06 (oscillator toolbox)
The oscillator reaches the equipartition value $k_B$ per mode only for $T\gg\theta_v$ ($C/k_B=0.99917$ at $x=0.1$, $0.0045$ at $x=10$): vibrations freeze out ([[Einstein Heat Capacity]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
