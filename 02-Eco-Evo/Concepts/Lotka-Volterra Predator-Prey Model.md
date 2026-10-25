---
title: Lotka-Volterra Predator-Prey Model
aliases: ["Lotka-Volterra equations", "predator-prey model", "LV model"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Lotka-Volterra Predator-Prey Model

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the two equations, the equilibria, neutral oscillations, the assumptions, and the density-dependent version ([[05_01_Sep_2026_Predation.pdf#page=5|slide 5]])  ·  🔵 **extra · beyond:** the conserved quantity and the structural-instability argument

> [!intuition] In one picture
> Prey grow on their own and are eaten at a rate proportional to meeting; predators grow only by eating and die at a constant rate. Each overshoots the other, giving endless cycles.

> [!key] Definition
> $$\dot H=rH-pHP,\qquad \dot P=apHP-mP.$$ Equilibrium: $P^*=r/p$, $H^*=m/(ap)$. Trajectories are closed orbits around it (neutral cycles; $V=apH-m\ln H+pP-r\ln P$ is constant). With logistic prey, $\dot H=rH(1-H/K)-pHP$, the equilibrium becomes a stable spiral and the cycles die out.

## Properties
$\dot H=rH-pHP$, $\dot P=apHP-mP$. Equilibrium $(H^*,P^*)=(m/ap,\ r/p)$. Linearisation gives eigenvalues $\pm i\sqrt{rm}$: neutral cycles of period $2\pi/\sqrt{rm}$ for small amplitude. The function $V=apH-m\ln H+pP-r\ln P$ is conserved ($\dot V=0$), so each orbit is a closed curve and is kept for ever.

> [!example] Numbers ($r=1,\ p=0.02,\ a=0.5,\ m=0.5$)
> $H^*=P^*=50$; small-cycle period $8.9$; the orbit started at $(30,30)$ ranges over $H\in[19.5,102.5]$ and $P\in[26.4,84.6]$ with period 9.25 (large cycles are slower) and the predator peak 1.7 after the prey peak (a quarter period for small cycles). Doubling $r$ gives $P^*=100$ but leaves $H^*=50$.
> **Volterra's principle.** Killing both species at an extra rate $\delta=0.1$ ($r\to0.9,\ m\to0.6$) moves the equilibrium from $(50,50)$ to $(60,45)$: prey up, predators down; indiscriminate control helps the prey. With logistic prey, $P^*=(r/p)(1-H^*/K)$ needs $K>m/ap$; the eigenvalues become $-0.125\pm0.60i$ (damped, period 10.5).

**Assumptions** (slide 7): prey limited only by predation; a specialist predator; no environmental change; random encounters in a homogeneous environment. Each is relaxed in the later parts of the lecture: density dependence, refuges ([[Gause Predator-Prey Experiments]]), space ([[Huffaker Mite Experiment]]), saturation ([[Functional and Numerical Responses]]).

> [!pitfall] Neutral means no memory of amplitude
> Any shock puts the system on another orbit, and any extra term in the equations turns closed orbits into spirals: the cycle is structurally unstable, so it cannot be the explanation of persistent real cycles. Tools: [[Phase Plane and Isoclines]], [[Fixed Points and Linear Stability]].

Used in: [[EE05 Predation]]. Related: [[Phase Plane and Isoclines]] · [[Predator-Prey Cycles]] · [[Functional and Numerical Responses]] · [[Fixed Points and Linear Stability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
