---
title: Internal Energy
aliases: ["internal energy E", "energy function"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Internal Energy

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=4|MIT L1 eq. I.11]].

> [!intuition] In one picture
> The balance in the energy account: set by where the system is, not by how it got there.

> [!key] Definition
> The state function $E(X)$ defined up to a constant by the work needed to change an adiabatically isolated system between two states: $\Delta W_{\rm adiabatic}=E(X_f)-E(X_i)$. Ideal gas: $E=E(T)$, $E=\tfrac f2Nk_BT$.

## Notes
$E$ is extensive; for the monatomic ideal gas $E=\tfrac32PV$. For van der Waals gas $E=C_VT-a/V$ ($(\partial E/\partial V)_T=T(\partial P/\partial T)_V-P=a/V^2$).

> [!pitfall] Only changes matter
> $E$ is defined up to an additive constant; likewise a global potential shift $V\to V+V_0$ shifts all energies and changes no probability ([[QM02 The Schrodinger Equation and Stationary States]]).

Used in: [[TH02 Work Heat and the First Law]], [[TH03 The Ideal Gas and Adiabatic Processes]]. Related: [[First Law of Thermodynamics]] · [[Heat and Work]] · [[Joule Expansion]] · [[Heat Capacity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
