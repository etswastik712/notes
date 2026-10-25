---
title: Gibbs Free Energy
aliases: ["Gibbs energy", "G = E - TS - Jx"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Gibbs Free Energy

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=2|MIT L3 eqs. I.38–I.39]].

> [!intuition] In one picture
> The potential that is minimal when temperature and pressure are held fixed, as in most laboratories and in the atmosphere.

> [!key] Definition
> $G=E-TS-J\!\cdot\!x$ (fluid $E-TS+PV$); $\mathrm dG=-S\,\mathrm dT-x\!\cdot\!\mathrm dJ$; $\delta G\le0$ at constant $T,J$. For a one-component fluid $G=\mu N$.

## Use
$(\partial G/\partial P)_T=V$, so ideal-gas $G=G_0(T)+Nk_BT\ln(P/P_0)$. Phase equilibrium: $G_l=G_g$, i.e. $\mu_l=\mu_g$, gives Clausius–Clapeyron.

> [!pitfall] Chemical work is treated separately
> Traditionally $\mu\,\mathrm dN$ is not subtracted in $G$; the grand potential ([[Grand Potential]]) does that.

Used in: [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Chemical Potential]] · [[Gibbs-Duhem Relation]] · [[Maxwell Relations]] · [[Clausius-Clapeyron Relation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
