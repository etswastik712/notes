---
title: Open System Energy Balance
aliases: ["big equation", "energy balance of an open system", "flow work", "steady-flow enthalpy balance", "throttling", "tank filling"]
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Open System Energy Balance

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Bhagwat.pdf#page=1|Bhagwat notes]], p. 1: $\mathrm dU^{\rm t}/\mathrm dt=\dot Q-P\,\mathrm dV^{\rm t}/\mathrm dt+\dot n(U+PV)+\dot W$ and its closed, no-work case.
> 🔵 **extra · beyond:** the steady-flow form, the entropy balance examples (heater, throttle, tank filling) (mine, checked).

> [!intuition] In one picture
> Energy in minus energy out equals energy accumulated: heat crosses the boundary, work crosses it, and **matter carries $U+PV=H$ across it** (its energy plus the work of pushing it in).

> [!key] Definition
> $\dfrac{\mathrm dU^{\rm t}}{\mathrm dt}=\dot Q-P\dfrac{\mathrm dV^{\rm t}}{\mathrm dt}+\dot n(U+PV)+\dot W$, with $\dot n$ the net molar inflow and $\dot W$ all non-$PV$ work. Closed, no work: the first law. **Steady flow:** $\sum\dot nH_{\rm in}-\sum\dot nH_{\rm out}+\dot Q+\dot W=0$. Entropy: $\mathrm dS^{\rm t}/\mathrm dt=\dot Q/T+\dot nS+\dot S_{\rm gen}$, $\dot S_{\rm gen}\ge0$.

**Throttle** ($\dot Q=\dot W=0$): $H_{\rm in}=H_{\rm out}$, $T$ unchanged for an ideal gas, $\dot S_{\rm gen}=\dot nR\ln(P_{\rm in}/P_{\rm out})$ ($10\to1$ bar, 1 mol s$^{-1}$: $19.15$ W K$^{-1}$). **Tank filling** (rigid, adiabatic, evacuated): $U_{\rm final}=NH_{\rm line}$, $T_f=\gamma T_{\rm line}$ ($420$ K for a 300 K diatomic line). **Heater** 300→600 K, 1 mol s$^{-1}$: $\dot Q=8730$ W.

Used in: [[TH10 Open Systems Mixing and Reacting Gases]], [[TH02 Work Heat and the First Law]]. Related: [[Entropy Production]] · [[Enthalpy]] · [[First Law of Thermodynamics]] · [[Joule Expansion]] · [[Gibbs Free Energy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
