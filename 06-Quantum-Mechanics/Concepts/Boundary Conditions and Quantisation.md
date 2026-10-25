---
title: Boundary Conditions and Quantisation
aliases: ["quantisation from boundary conditions", "why energies are discrete"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Boundary Conditions and Quantisation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture9_FreeParticle_Ring_GeneralProperties.pdf#page=6|L9 §6, §12]], [[Particle_in_a_box.pdf#page=4|box lecture p.4]].

> [!intuition] In one picture
> The equation has solutions for every energy; only some of them fit the physical situation.

> [!key] Definition
> **Schrödinger equation + boundary condition $\Rightarrow$ allowed energies.** Discreteness arises when the condition (periodicity, vanishing at a wall, normalisability at infinity) admits only selected wavelengths.

## Examples
| system | condition | allowed | $E$ |
|---|---|---|---|
| free line | none | any $k$ | $\hbar^2k^2/2m$ (continuous) |
| ring | $\psi(x+L)=\psi(x)$ | $k_n=2\pi n/L$ | $\propto n^2$ |
| box | $\psi(0)=\psi(a)=0$ | $k_n=n\pi/a$ | $\propto n^2$ |
| oscillator | $\psi\to0$ at $\pm\infty$ | $E_n=(n+\tfrac12)\hbar\omega$ | $\propto n+\tfrac12$ |

> [!pitfall] Not an extra postulate
> Quantisation is a consequence of wave behaviour in a confined or periodic setting, not a separate rule added by hand.

Used in: [[QM02 The Schrodinger Equation and Stationary States]], [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]]. Related: [[Energy Quantisation]] · [[Particle on a Ring]] · [[Particle in a Box]] · [[Free Particle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
