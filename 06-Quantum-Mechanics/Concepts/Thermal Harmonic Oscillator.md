---
title: Thermal Harmonic Oscillator
aliases: ["Bose-Einstein occupation", "quantum oscillator at temperature T", "Planck oscillator"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Thermal Harmonic Oscillator

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond** (the $\hbar\omega/(e^{\hbar\omega/kT}-1)$ result is the Planck mean energy of [[TH06 From Kinetic Theory to Statistical Mechanics]]).

> [!intuition] In one picture
> At temperature $T$ the oscillator is on rung $n$ with a Boltzmann weight; because the rungs are evenly spaced the weights form a geometric series.

> [!key] Definition
> $x=\hbar\omega/k_BT$: $\ P(n)=(1-e^{-x})e^{-nx}$, $\ \langle n\rangle=\dfrac1{e^x-1}$, $\ \langle E\rangle=\hbar\omega\big(\tfrac12+\langle n\rangle\big)$, $\ Z=\dfrac1{2\sinh(x/2)}$.

## Probability link
$P(n)$ is Geometric (failures counted, $P(N=k)=q^kp$, $q=e^{-x}$): mean $q/p=1/(e^x-1)$, variance $q/p^2=\langle n\rangle(1+\langle n\rangle)$ (checked at $x=1.7$: mean $0.223516$, variance $0.27348$). So $\langle n\rangle$ is the **Bose–Einstein** occupation and the zero-point-free energy is **Planck's** $\hbar\omega/(e^x-1)$.

## Numbers at 288 K ($\theta_v=1.4388\ \mathrm{K\,cm}\times\tilde\nu$)
- CO stretch, $2143$ cm$^{-1}$: $\theta_v=3083$ K, $x=10.71$, $P(n\ge1)=2.2\times10^{-5}$: frozen.
- CO$_2$ bend, $667$ cm$^{-1}$: $\theta_v=960$ K, $x=3.33$, $\langle n\rangle=0.0370$, $P(n\ge1)=3.6\%$ (4.1 % at 300 K).

> [!pitfall] Zero-point energy does not heat anything
> $\tfrac12\hbar\omega$ is present at $T=0$ and does not contribute to $C$; only $\langle n\rangle\hbar\omega$ does.

Used in: [[QM06 The Oscillator Toolbox]] §8. Related: [[Einstein Heat Capacity]] · [[Planck Mean Energy]] · [[Partition Function]] · [[Canonical Ensemble]] · [[Photon Statistics]] · [[Geometric Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
