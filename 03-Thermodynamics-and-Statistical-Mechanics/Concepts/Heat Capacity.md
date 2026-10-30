---
title: Heat Capacity
aliases: ["specific heat", "heat capacities"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Heat Capacity

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=5|MIT L1 eq. I.14]].

> [!intuition] In one picture
> How much heat per kelvin: it depends on the road (constant volume or constant pressure).

> [!key] Definition
> $C_V=\bar\mathrm dQ/\mathrm dT|_V=(\partial E/\partial T)_V$; $C_P=\bar\mathrm dQ/\mathrm dT|_P=(\partial E/\partial T)_P+P(\partial V/\partial T)_P=(\partial H/\partial T)_P$. Ideal gas: $C_V=\tfrac f2Nk_B$, $C_P=C_V+Nk_B$.

## Numbers
1 mol diatomic, 300 → 400 K: $Q_V=2079$ J, $Q_P=2910$ J (difference $=R\Delta T=831$ J of expansion work). Air: $c_p=1004.5$, $c_v=717.5$, $R_d=287.0$ J kg$^{-1}$K$^{-1}$.

> [!pitfall] Must specify the path
> "The heat capacity" of a gas is ambiguous: $C_P\ne C_V$. Stability requires $C_V\ge0$ (and $C_P\ge C_V$); third law: $C\to0$ as $T\to0$.

Used in: [[TH02 Work Heat and the First Law]], [[TH03 The Ideal Gas and Adiabatic Processes]]. Related: [[Mayer Relation]] · [[Ratio of Specific Heats]] · [[Enthalpy]] · [[Equipartition of Energy]].

## Added with QM06 (oscillator toolbox)
**Quantum oscillator:** $C=k_B\,x^2e^x/(e^x-1)^2$, $x=\theta_v/T$; frozen for CO ($\theta_v=3083$ K), partly active for the CO$_2$ bend ($\theta_v=960$ K, $C/k=0.43$ at 288 K) ([[Einstein Heat Capacity]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- Heat conduction through a gas: the thermal diffusivity $\kappa/\rho c_p$ and the Prandtl number: [[SM04 Kinetic Theory and the Boltzmann Equation]] §10–§11 ([[Prandtl Number]]).
