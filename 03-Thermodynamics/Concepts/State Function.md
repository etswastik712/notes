---
title: State Function
aliases: ["thermodynamic coordinate", "function of state"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# State Function

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=1|MIT L1 §I.A]], [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=4|§I.C]].

> [!intuition] In one picture
> A quantity that depends only on where the system is, not how it got there.

> [!key] Definition
> A **state function** (pressure, volume, temperature, internal energy, entropy, the potentials) has a value fixed by the equilibrium state; its change between two states is path-independent and its differential is **exact**. Heat and work are **not** state functions.

## Test and examples
A differential $\mathrm dz=M\mathrm dx+N\mathrm dy$ is exact iff $\partial_yM=\partial_xN$. $E$ and $S$ pass; $\bar\mathrm dQ$ and $\bar\mathrm dW$ fail (the bar). For an ideal gas $\bar\mathrm dQ_{\rm rev}/T=C_V\mathrm dT/T+R\mathrm dV/V$ **is** exact (integrating factor $1/T$), which defines $S$.

> [!pitfall] "The heat in the gas" has no meaning
> One can ask how much heat was *added* on a given process, never how much a system *contains*. The ledger ([[Internal Energy]]) stores only the balance.

Used in: [[TH01 Temperature and the Zeroth Law]], [[TH02 Work Heat and the First Law]]. Related: [[Exact Differential]] · [[Internal Energy]] · [[Heat and Work]] · [[Entropy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
