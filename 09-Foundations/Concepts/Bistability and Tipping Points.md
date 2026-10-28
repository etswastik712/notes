---
title: Bistability and Tipping Points
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [argha, paper]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/argha, src/paper, status/draft]
---
# Bistability and Tipping Points

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** steady states, stability, snowball (Argha L4) · 🔵 **extra:** fold bifurcation, critical slowing down, ecology examples

> [!intuition] In one picture
> A light switch is bistable: it rests firmly on or off, the halfway position is unstable, and you need a push beyond a threshold to flip it. Tipping points are the same thing in the Earth and in ecosystems, except the threshold creeps closer as conditions change.

> [!key] Core idea
> A system is **bistable** if, for the same external conditions, it has two stable steady states separated by an unstable one. As a control parameter $\mu$ changes slowly, a stable state can disappear at a **fold (saddle-node) bifurcation**, forcing an abrupt jump to the other branch. Because the way back is at a different value of $\mu$, there is **hysteresis**.

Normal form: $\dot x=\mu+x-x^{3}$ (S-shaped equilibrium curve), or at the fold itself $\dot x=\mu-x^{2}$.

**Early warning.** Near a fold, $f'(x^*)\to0$, so the [[Relaxation Time]] $\tau=1/|f'|$ diverges: *critical slowing down*. Fluctuations then show rising variance and lag-1 autocorrelation before the tip.

| System | state variable | control | two states | feedback | note |
|---|---|---|---|---|---|
| **Climate (this vault)** | global $T$ | solar constant or CO₂ | ice-free / snowball | ice–albedo | [[CL04 Feedback and Multiple Steady States]], [[Snowball Earth]] |
| **Shallow lakes** | submerged vegetation vs algae | nutrient (P) loading | clear / turbid | plants clear the water | Scheffer et al. 2001 (in the eco-evo reading list) |
| **Population with Allee effect** | density $N$ | growth/mortality | extinct / persisting | positive density dependence | [[Ecology and Evolution - Course Map]] |
| **Daisyworld** | daisy cover | solar luminosity | regulated / dead | albedo of daisies | *The Earth System* Ch. 2 |

The mathematics is [[Fixed Points and Linear Stability]]. The same S-curve appears in chemical kinetics (autocatalysis), in neural populations and perception (see [[Neuroscience - Course Map]]) and in phase transitions of matter ([[Thermodynamics - Course Map]]).

> [!connection] See also
> Critical slowing down as a pole approaching the origin: [[Fourier and Laplace Transforms]] §7.6.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
