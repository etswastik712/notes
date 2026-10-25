---
title: Selection Rules
aliases: ["dipole selection rule", "Delta n = +-1"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Selection Rules

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** stated without proof in QM05 §9; derived in QM06.

> [!intuition] In one picture
> Light grabs the oscillator through $\hat x$, and $\hat x$ can only move it one rung.

> [!key] Definition
> For the harmonic oscillator $\langle m|\hat x|n\rangle\neq0$ only if $|m-n|=1$, so the absorption/emission rate $\propto|\langle m|\hat x|n\rangle|^2$ is non-zero only for $\Delta n=\pm1$: **one spectral line** at $\omega$.

## Why
$\hat x\propto\hat a+\hat a^\dagger$ changes $n$ by exactly $\pm1$. Parity alone gives only "$n-m$ odd" (since $\hat x$ is odd and $\psi_n$ has parity $(-1)^n$); the ladder gives the stronger "$|n-m|=1$". Checked in the matrix for all $m,n<12$.

## Consequences
- Equal level spacing plus $\Delta n=\pm1$ means every allowed absorption has the **same frequency** $\omega$ (the fundamental).
- Anharmonic terms ($x^3$, $x^4$) mix rungs and allow weak **overtones** $\Delta n=\pm2,\pm3$.
- A molecule must also have a **dipole moment that changes** with the vibration: the CO$_2$ symmetric stretch does not (infrared-inactive), the bend and asymmetric stretch do ([[CL07 Optical Properties of the Atmosphere]], [[Greenhouse Gases and Absorption Bands]]).

> [!pitfall] A rule is not a calculation of the rate
> The rule says which transitions are possible; the strength also needs the matrix element (here $\sigma\sqrt{n+1}$, growing with $n$) and the light's field.

Used in: [[QM05 The Harmonic Oscillator]] §9, [[QM06 The Oscillator Toolbox]] §3. Related: [[Matrix Elements of Position and Momentum]] · [[Parity Operator]] · [[Ladder Operators]] · [[Anharmonic Oscillator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
