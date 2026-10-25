---
title: Einstein Heat Capacity
aliases: ["Einstein solid", "Einstein function", "vibrational heat capacity"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Einstein Heat Capacity

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond** (Einstein 1907; the thermodynamics side is [[Heat Capacity]]).

> [!intuition] In one picture
> A vibration that cannot absorb a quantum $\hbar\omega$ from the heat bath is frozen out; one that can contributes the full classical $k_B$.

> [!key] Definition
> $C=\dfrac{\mathrm d\langle E\rangle}{\mathrm dT}=k_B\dfrac{x^2e^x}{(e^x-1)^2}$, $\ x=\theta_v/T$; $\ C\to k_B\big(1-\tfrac{x^2}{12}\big)$ for $x\ll1$, $\ C\approx k_Bx^2e^{-x}$ for $x\gg1$.

## Values of $C/k_B$
$x=0.1$: $0.99917$; $x=1$: $0.92067$; $x=3$: $0.49627$; $x=10$: $0.00454$. At 288 K: CO stretch $0.0026$ (frozen), CO$_2$ bend $0.426$ (partly active). Diatomic gases such as N$_2$, O$_2$ keep $C_V=\frac52R$ at room temperature for this reason.

## Meaning
High $T$: the two quadratic terms (kinetic and potential, $\tfrac12k_BT$ each) give the **equipartition** value $k_B$ ([[Equipartition of Energy]]). Low $T$: the exponential freeze-out; Einstein's 1907 insight that a solid's heat capacity falls at low $T$ because lattice vibrations are quantised. (The real $T^3$ law needs a spread of frequencies, the Debye model; not in the folder.)

> [!pitfall] Not the Schottky anomaly
> A two-level system has a *peak* in $C$ ([[Schottky Anomaly]]); the oscillator's $C$ rises monotonically to $k_B$ because its ladder never ends.

Used in: [[QM06 The Oscillator Toolbox]] §8. Related: [[Thermal Harmonic Oscillator]] · [[Heat Capacity]] · [[Equipartition of Energy]] · [[Partition Function]] · [[Schottky Anomaly]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
