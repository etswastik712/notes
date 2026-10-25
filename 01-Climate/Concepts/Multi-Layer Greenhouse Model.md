---
title: Multi-Layer Greenhouse Model
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [argha, suhas-pre]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# Multi-Layer Greenhouse Model

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** 'can we improve the model by having many layers?' (Argha L6 sl. 68), Suhas Model 3 and the radiative discontinuity · 🟡 **extra book:** W&H Ex. 4.8 ladder · 🔵 **extra:** the exact solver, grey layers, continuum limit

> [!intuition] In one picture
> A bucket brigade: every handover up the chain needs a temperature step, so the more layers the hotter the bottom of the chain must be to pass the same energy through.

> [!key] Result
> For $N$ fully opaque isothermal layers the net upward flux is $F=\sigma T_e^4$ at every interface, so layer $k$ (from the top) emits $kF$ and the ground $(N+1)F$:
> $$\sigma T_k^4=kF,\qquad T_s=(N+1)^{1/4}T_e .$$

| $N$ | 1 | 2 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| $T_s$ (K), opaque | 302.8 | 335.0 | 360.0 | 398.4 | 463.6 |
| $T_s$ (K), $\varepsilon=0.78$ each | 288.1 | 312.8 | 332.7 | 364.4 | 419.8 |

- The ground is **hotter than the air just above it** (398 vs 381 K for $N=5$): the **radiative discontinuity**; the radiative lapse rate steepens downward until it exceeds the adiabatic one and convection takes over ([[CL09 Radiative-Convective Equilibrium]]).
- Only the **total** optical depth matters: two layers of $\varepsilon=0.5$ equal one of 0.8. Continuum limit: $N+1\leftrightarrow1+0.83\,\tau_s$, one opaque layer ≈ 1.2 optical-depth units.
- Venus: $(T_s/T_e)^4=112$ ⇒ $N\sim10^2$.

Derived and solved numerically (`scripts/cl08_layers.py`) in [[CL08 Greenhouse Models]]. See [[One-Layer Greenhouse Model]], [[Greenhouse Effect]]; linear systems: [[Linearisation and Sensitivity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
