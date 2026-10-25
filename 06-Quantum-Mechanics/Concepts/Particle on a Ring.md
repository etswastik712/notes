---
title: Particle on a Ring
aliases: ["ring", "periodic boundary condition"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Particle on a Ring

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture9_FreeParticle_Ring_GeneralProperties.pdf#page=4|L9 §5]], [[PH2113_states_operators_notes.pdf#page=1|SO §1]].

> [!intuition] In one picture
> Walk once round and you must meet yourself in phase: only whole numbers of wavelengths fit.

> [!key] Definition
> Free particle at fixed radius $R$: $\psi_n=Ae^{in\theta}$, single-valuedness $\psi(\theta+2\pi)=\psi(\theta)\Rightarrow n\in\mathbb Z$, $E_n=\hbar^2n^2/2mR^2$ ($=2\pi^2\hbar^2n^2/mL^2$, $L=2\pi R$). $E_n=E_{-n}$: opposite directions are degenerate.

## Numbers (recomputed)
> [!example] Electron on a benzene-size ring ($L=0.83$ nm)
> $p_1=h/L=7.98\times10^{-25}$ kg m/s ($v_1=8.8\times10^5$ m/s); $E_1=2.18$ eV, $E_2=8.73$ eV, gap $6.55$ eV: discrete and optical. On a **1 cm** ring $E_1=1.5\times10^{-14}$ eV, $10^{12}$ times below $k_BT$: the levels cannot be resolved.

The states $e^{\pm ik_nx}/\sqrt L$ have uniform density; the cosine and sine combinations have $n$ maxima ([[Superposition Principle]]).

> [!pitfall] The ground state has $E=0$
> Unlike the box, the ring allows the constant $n=0$ state: no confinement, no zero-point energy ([[Zero-Point Energy]]).

Used in: [[QM02 The Schrodinger Equation and Stationary States]], [[QM03 States Operators and Measurement]]. Related: [[Free Particle]] · [[Degeneracy]] · [[Boundary Conditions and Quantisation]] · [[Correspondence Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
