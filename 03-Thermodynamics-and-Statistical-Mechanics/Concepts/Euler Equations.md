---
title: Euler Equations
aliases: ["ideal fluid equations", "zeroth-order hydrodynamics"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Euler Equations

> [!info] Source
> Kardar §3.8 (pp. 82–84); Huang §5.4 (p. 100); [[SM04 Kinetic Theory and the Boltzmann Equation]] §9.

> [!intuition] In one picture
> What the Boltzmann equation gives when collisions have just enough time to make the gas locally Maxwellian, and no time to cause friction.

> [!key] Key facts
> With $f_0$ (local $n,\mathbf u,T$): $P_{\alpha\beta}=nk_BT\delta_{\alpha\beta}$, $\mathbf h=0$. $D_tn=-n\nabla\cdot\mathbf u$; $mn\,D_t\mathbf u=-\nabla(nk_BT)+n\mathbf F$; $D_tT=-\tfrac23T\nabla\cdot\mathbf u$, i.e. $D_t(Tn^{-2/3})=0$ (adiabatic, no dissipation). Sound: $c=\sqrt{5k_BT/3m}$.

> [!example] Modes and numbers (recomputed)
> Five conserved densities, five modes: two sound ($\omega=\pm ck$), two shear and one entropy (all $\omega=0$, undamped). He 293 K: $c=1007.4$ m s$^{-1}$; Ar $318.9$; air ($\gamma=1.4$) $343.2$. $\bar v/c=1.236$. Damping requires first order ([[Navier-Stokes Equations]]).

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Hydrodynamic Modes]] · [[Speed of Sound]] · [[Ratio of Specific Heats]] · [[Navier-Stokes Equations]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
