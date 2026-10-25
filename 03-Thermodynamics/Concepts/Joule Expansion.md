---
title: Joule Expansion
aliases: ["free expansion"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Joule Expansion

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=5|MIT L1 (Joule free expansion)]].

> [!intuition] In one picture
> Let a gas rush into a vacuum: no work done, no heat exchanged, yet the entropy rises.

> [!key] Definition
> Adiabatic free expansion from $V_i$ to $V_f$: $\Delta Q=\Delta W=0\Rightarrow\Delta E=0$. For a dilute gas $\Delta T=0$, so $E=E(T)$. A real gas cools: $\Delta T=-(a/C_V)(1/V_i-1/V_f)$ for van der Waals.

## Numbers
1 mol doubling $V$: $\Delta S=R\ln2=5.76$ J K$^{-1}$ (irreversible). CO$_2$ from 1 L to 2 L: $\Delta T\approx-6.3$ K. Proof that $E=E(T)$ follows from $P=Nk_BT/V$: $(\partial E/\partial V)_T=T(\partial P/\partial T)_V-P=0$.

> [!pitfall] Not isentropic
> Although adiabatic, it does **not** follow $PV^\gamma=$ const; that applies only to reversible adiabats ([[Reversible Adiabatic Process]]).

Used in: [[TH02 Work Heat and the First Law]], [[TH04 The Second Law Carnot Engines and Entropy]]. Related: [[Internal Energy]] · [[Entropy]] · [[Irreversibility]] · [[Mayer Relation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
