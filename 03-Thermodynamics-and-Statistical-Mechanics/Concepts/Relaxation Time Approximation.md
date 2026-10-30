---
title: Relaxation Time Approximation
aliases: ["BGK approximation", "single collision time approximation", "Krook model"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Relaxation Time Approximation

> [!info] Source
> Kardar §3.9 (eqs. 3.111–3.114, p. 85); Huang §5.5; [[SM04 Kinetic Theory and the Boltzmann Equation]] §10.

> [!intuition] In one picture
> Replace the full collision integral by 'every molecule returns to local equilibrium in a time $\tau$': crude but it keeps the conservation laws and gives all the right structure.

> [!key] Key facts
> $C[f]\simeq-(f-f_0)/\tau$ with $\tau\sim\tau_\times$. First order: $g=-\tau\mathcal Lf_0/f_0$, $\mathcal Lf_0/f_0=\frac m{k_BT}(c_\alpha c_\beta-\tfrac13c^2\delta_{\alpha\beta})\partial_\alpha u_\beta+(\frac{mc^2}{2k_BT}-\frac52)\mathbf c\cdot\nabla T/T$. Results: $\eta=nk_BT\tau$, $\kappa=\frac52\frac{nk_B^2T\tau_K}m$; with $\tau_K=\tau$: $\mathrm{Pr}=1$.

> [!example] Air (recomputed)
> $\tau=\tau_\times=1.41\times10^{-10}$ s: $\eta=14.3$ µPa s against the measured $\approx18.5$ and the exact first approximation $18.2$.

*Defect:* one time cannot serve both modes; the exact theory has $\tau_K/\tau=\tfrac32$ ($\mathrm{Pr}=\tfrac23$).

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Boltzmann Equation]] · [[Viscosity of a Gas]] · [[Thermal Conductivity of a Gas]] · [[Chapman-Enskog Expansion]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
