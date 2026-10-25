---
title: Convective Adjustment
subject: climate
type: concept
scope: [taught, extra-beyond]
by: [suhas-pre]
status: draft
tags: [subject/climate, type/concept, taught, extra/beyond, src/suhas-pre, status/draft]
---
# Convective Adjustment

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!key] Definition
> **Convective adjustment** replaces the details of convection by a rule: wherever the lapse rate of a column would exceed a critical value $\Gamma_c$ (the dry adiabatic 9.8 K km⁻¹, or the observed ≈6.5 K km⁻¹, or the moist adiabat), mix the layers just enough to bring it back to $\Gamma_c$, conserving energy.

The taught statement (Suhas pre-midsem; M&P §4.7): convection transports heat upward until "the environment itself approaches a state of neutrality", producing **radiative–convective equilibrium**: a convective profile below the tropopause, radiative above.

> [!extra-beyond]- 🔵 Extra (beyond): the Manabe algorithm
> For adjacent layers $k$ (upper) and $k+1$ (lower) with masses $\Delta p_k$, $\Delta p_{k+1}$: if $T_{k+1}>rT_k$ with $r=(p_{k+1}/p_k)^{R\Gamma_c/g}$, set $T_k'=\dfrac{\Delta p_kT_k+\Delta p_{k+1}T_{k+1}}{\Delta p_k+\Delta p_{k+1}\,r}$ and $T'_{k+1}=rT'_k$ (enthalpy $\sum\Delta p\,T$ conserved). Sweep until no pair violates the rule. **Example:** layers at 900 hPa (300 K) and 700 hPa (275 K), equal mass: $r=1.0745$, $T_{\rm up}'=277.2$ K, $T'_{\rm low}=297.8$ K. Implemented in `scripts/cl09_rce.py`.

> [!intuition] A speed limiter
> Radiation alone would let the lapse rate run away; convection is a governor that cuts it back whenever it exceeds the limit, like a speed limiter on an engine. It does not change the energy, only where it sits.

It cools the surface and warms the free troposphere (CL09 Fig. 2). Real convection is not instantaneous or uniform: adjustment is the simplest *parametrisation* (a model of unresolved processes), used in 1-D models and as the ancestor of the schemes in climate models ([[Convection]], [[Atmospheric Stability]], [[Dry Adiabatic Lapse Rate]]). Chapter: [[CL09 Radiative-Convective Equilibrium]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
