---
title: Zeroth Law
aliases: ["zeroth law of thermodynamics"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Zeroth Law

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=2|MIT L1 §I.B]].

> [!intuition] In one picture
> If two bodies are each in balance with a third, they are in balance with each other: so temperature can be a property.

> [!key] Definition
> If systems A and B are separately in thermal equilibrium with C, they are in equilibrium with each other. This implies a state function $\Theta(\text{coordinates})$, the empirical temperature, equal for systems in equilibrium.

## Proof idea
$f_{AC}=0$ and $f_{BC}=0$ each solve for a coordinate $C_1$; equating them and using $f_{AB}=0$, which cannot involve $C$, forces $C$'s coordinates to cancel and leaves $\Theta_A(A_i)=\Theta_B(B_i)$ ([[TH01 Temperature and the Zeroth Law]] §2). The relation $\Theta=$ const is an **isotherm** (the equation of state).

> [!pitfall] Existence, not value
> The zeroth law gives isotherms and a transitivity, not a scale: that needs a reference system (the dilute gas) or the Carnot construction ([[Thermodynamic Temperature]]).

Used in: [[TH01 Temperature and the Zeroth Law]]. Related: [[Empirical Temperature]] · [[Equation of State]] · [[Thermodynamic Equilibrium]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
