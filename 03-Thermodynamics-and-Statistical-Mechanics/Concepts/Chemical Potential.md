---
title: Chemical Potential
aliases: ["mu"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Chemical Potential

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=3|MIT L3 §I.G]], [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=5|eq. I.51]].

> [!intuition] In one picture
> The energy cost of adding one particle: particles flow from high $\mu$ to low $\mu$.

> [!key] Definition
> $\mu=(\partial E/\partial N)_{S,x}=(\partial F/\partial N)_{T,V}$; equilibrium between phases or regions requires equal $\mu$. Ideal gas: $\mu=\mu_0+k_BT\ln(P/P_0)$.

## Numbers
At 300 K doubling $P$ raises $\mu$ by $k_BT\ln2=2.87\times10^{-21}$ J ($=1729$ J mol$^{-1}$). Steam: minimise $F(V,T,N|N_w)$ over $N_w$ to get $\mu_w=\mu_s$.

> [!pitfall] Intensive
> $\mu$ is intensive; the Gibbs-Duhem relation $S\mathrm dT+x\!\cdot\!\mathrm dJ+N\mathrm d\mu=0$ ties it to $T$ and $J$.

Used in: [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Gibbs-Duhem Relation]] · [[Grand Potential]] · [[Clausius-Clapeyron Relation]] · [[Gibbs Free Energy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- $\mu=-T\partial_NS$ as the entropy price of a particle, the Gibbs factor, $\sum\nu_i\mu_i=0$ and Widom's insertion formula: [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]] ([[Fugacity]], [[Law of Mass Action]], [[Widom Insertion Method]]).
