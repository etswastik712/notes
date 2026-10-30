---
title: Chapman-Enskog Expansion
aliases: ["Chapman-Enskog theory", "first approximation transport coefficients"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Chapman-Enskog Expansion

> [!info] Source
> Chapman and Cowling (1939), recalled; checked against data in [[SM04 Kinetic Theory and the Boltzmann Equation]] §10.3.

> [!intuition] In one picture
> Solve the Boltzmann equation order by order in $\tau_\times/\tau_U$ around the local Maxwellian, with the exact linearised collision operator instead of a single relaxation time.

> [!key] Key facts
> First approximation, hard spheres: $\eta=\frac5{16}\frac{\sqrt{mk_BT/\pi}}{d^2}$, $\kappa=\frac{15}4\frac{k_B}m\eta$, $D_{\rm self}=\frac65\frac\eta\rho$, $\mathrm{Pr}=\frac23$. The elementary estimate $\frac13nm\bar v\lambda$ has coefficient $0.2122$ instead of $0.3125$ (32 % low). Real gases: $\eta\propto T^{0.66\text{–}0.7}$ (soft repulsion), not $\sqrt T$.

> [!example] Test (recomputed, 300 K)
> $\kappa_{\rm pred}/\kappa_{\rm meas}=0.994,0.997,1.000,1.004,0.968$ for He, Ne, Ar, Kr, Xe (measured values recalled from CRC/NIST); $\mathrm{Pr}=0.66$–$0.67$. Diatomics: modified Eucken $\kappa=\eta(c_v+\frac94R/M)$, N$_2$: $0.0252$ vs $0.0260$.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Relaxation Time Approximation]] · [[Viscosity of a Gas]] · [[Thermal Conductivity of a Gas]] · [[Prandtl Number]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
