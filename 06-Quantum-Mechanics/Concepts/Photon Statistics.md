---
title: Photon Statistics
aliases: ["Mandel Q", "photon number distribution", "Poissonian light", "thermal light", "sub-Poissonian"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Photon Statistics

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond** (links quantum states to the probability distributions of [[PR03 Discrete Random Variables and Distributions]]).

> [!intuition] In one picture
> The same average number of quanta can be spread in three very different ways.

> [!key] Definition
> Mandel $Q=\dfrac{\mathrm{Var}\,n}{\langle n\rangle}-1$: Fock state $Q=-1$ (sharp), coherent state $Q=0$ (Poisson), thermal state $Q=\langle n\rangle$ (geometric).

## For $\langle n\rangle=4$ (Fig. QM6.1 C)
| State | $P(n)$ | $\mathrm{Var}\,n$ | $Q$ |
|---|---|---|---|
| Fock $n=4$ | $\delta_{n4}$ | 0 | $-1$ |
| coherent | Poisson(4): $P(0)=0.0183$, $P(4)=0.1954$ | 4 | 0 |
| thermal | geometric: $P(n)=\tfrac15(\tfrac45)^n$ | 20 | 4 |

Thermal light is **bunched** (quanta come in clumps, variance $\langle n\rangle(1+\langle n\rangle)$), coherent light is random, Fock light is antibunched (not classical). In the failures-counting convention of the Week 3 probability lecture the thermal $P(n)$ is exactly Geometric$(p)$ with $p=1-e^{-\hbar\omega/k_BT}$.

> [!pitfall] Mean alone does not identify the state
> A detector counting quanta over many trials sees the *distribution*, which discriminates the three.

Used in: [[QM06 The Oscillator Toolbox]] §7–§8. Related: [[Coherent State]] · [[Thermal Harmonic Oscillator]] · [[Poisson Distribution]] · [[Geometric Distribution]] · [[Number Basis]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
