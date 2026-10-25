---
title: Entropy
aliases: ["thermodynamic entropy"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Entropy

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[1a131e225246d9749a298f49675c5fe5_MIT8_333F13_Lec2.pdf#page=4|MIT L2 eqs. I.25–I.29]].

> [!intuition] In one picture
> The state function that measures irreversibility; in an isolated system it only grows.

> [!key] Definition
> $S(B)-S(A)=\int_A^B\bar\mathrm dQ_{\rm rev}/T$ (path-independent); $\mathrm dS\ge\bar\mathrm dQ/T$; isolated: $\delta S\ge0$ and $S$ is maximal at equilibrium; $\mathrm dE=T\mathrm dS+\sum J_i\mathrm dx_i$; $(\partial S/\partial E)_x=1/T$.

## Numbers
Heat flow $1000$ J, $500\to300$ K: $\Delta S=+1.333$ J K$^{-1}$. Free expansion of 1 mol, $V\to2V$: $R\ln2=5.76$. Melting 1 kg ice: $1223$ J K$^{-1}$. Heating 1 kg water $20\to80$ °C reversibly: $780$ J K$^{-1}$. Ideal gas $S=C_V\ln T+R\ln V+S_0$.

> [!pitfall] Compute along a reversible path
> $\Delta S$ between two states uses a reversible path even if the real process is irreversible; the real $\int\bar\mathrm dQ/T$ is smaller.

Used in: [[TH04 The Second Law Carnot Engines and Entropy]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]], [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Clausius Theorem]] · [[Fundamental Thermodynamic Relation]] · [[Statistical Entropy]] · [[Third Law of Thermodynamics]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
