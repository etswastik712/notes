---
title: First Law of Thermodynamics
subject: thermo
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/thermo, type/concept, extra/book, src/book, status/draft, quiz/thermo, quiz/th-tut1, quiz/th-background]
---
# First Law of Thermodynamics

<span class="scope-extra-book">extra · book</span>

> [!key] Statement
> Energy is conserved: the change in internal energy of a system equals the heat added minus the work done by the system, $\mathrm dU=\delta Q-\delta W$. For a unit mass of gas doing only expansion work $p\,\mathrm d\alpha$ ($\alpha=1/\rho$ the specific volume):
> $$\mathrm dq=c_v\,\mathrm dT+p\,\mathrm d\alpha=c_p\,\mathrm dT-\alpha\,\mathrm dp .$$

- **Heat capacities of air.** $c_v=717$ J kg⁻¹ K⁻¹, $c_p=1004$ J kg⁻¹ K⁻¹, $R_d=c_p-c_v=287$ J kg⁻¹ K⁻¹, $\gamma=c_p/c_v=1.40$. Check from kinetic theory: air is mostly diatomic (N₂, O₂) with 5 active degrees of freedom at atmospheric temperatures, so $c_v=\tfrac52R_d$ and $c_p=\tfrac72R_d$: $717.5$ and $1004.5$ J kg⁻¹ K⁻¹ ✓.
- **Special cases.** isochoric ($\mathrm d\alpha=0$): $\mathrm dq=c_v\mathrm dT$; isobaric: $\mathrm dq=c_p\mathrm dT$; isothermal: heat in = work out; **adiabatic**: $\mathrm dq=0$ ([[Adiabatic Process and Potential Temperature]]).
- **Enthalpy** $h=c_pT$ per unit mass: the natural energy for a parcel at fixed pressure; with height, the **dry static energy** $c_pT+gz$.

> [!intuition] An energy ledger
> Heat you add can go to two places: warming the gas (internal energy) or pushing the walls out (work). Squeeze a bicycle pump quickly and the work you do has nowhere to go but the air's internal energy: it heats. Let a gas expand and it spends its own warmth to do the pushing: it cools. A rising air parcel is exactly a gas that expands into lower pressure.

Used in the atmosphere: the dry adiabatic lapse rate ([[Dry Adiabatic Lapse Rate]], derived from this law and hydrostatic balance in [[CL09 Radiative-Convective Equilibrium]]), latent-heat effects on parcels ([[Clausius-Clapeyron Relation]]), moist static energy and the energy budget of the column ([[Poleward Energy Transport]]).

Connections: [[Thermodynamics and Statistical Mechanics - Course Map]] (full treatment: the first law as the energy form of the conservation principle, the second law adding the arrow of time); [[Ideal Gas Law]] (the other half of every parcel calculation).

## Continued in the vault (added 2026-11-04)
- Enthalpy bookkeeping for reactions and calorimeters: [[TH07 Enthalpy Thermochemistry and Calorimetry]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
