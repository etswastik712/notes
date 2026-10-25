---
title: Phase Plane and Isoclines
aliases: ["zero-growth isocline", "nullcline", "phase portrait"]
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Phase Plane and Isoclines

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the zero-growth isoclines of the competition model and, next, of the predator-prey model ([[04-Competition_25-Aug_2026.pdf#page=11|slide 11]])  ·  🔵 **extra · beyond:** Jacobian stability of interior equilibria

> [!intuition] In one picture
> Draw the plane of the two populations. One curve marks where species 1 stops changing, another where species 2 stops changing. Where they cross, both are still: an equilibrium. The arrows between show where the system moves.

> [!key] Definition
> For $\dot x=f(x,y),\ \dot y=g(x,y)$ the **phase plane** is the $(x,y)$ plane. The **zero-growth isoclines** (nullclines) are the curves $f=0$ and $g=0$; the first has purely vertical flow, the second purely horizontal. Equilibria are their intersections. The arrows reverse across each isocline, giving the qualitative picture without solving the equations.

## Method in four steps, with the vault's examples
1. Draw the **isoclines** $f=0$ and $g=0$ (nullclines): on the first $x$ is momentarily constant, on the second $y$ is.
2. Mark the **equilibria** at their intersections (and on the axes, for population models).
3. In each region between isoclines draw the direction of the flow: it reverses across an isocline.
4. Classify each equilibrium with the Jacobian $J$: eigenvalues with negative real parts mean stable ($\mathrm{tr}J<0$, $\det J>0$); $\det J<0$ a saddle; $\mathrm{tr}^2<4\det$ a spiral.

> [!example] Three equilibria, three pictures
> **Competition**, $\alpha_{12}\alpha_{21}=0.30$: both isoclines straight lines, a stable node (eigenvalues $-0.50,\ -0.107$). With $\alpha_{12}\alpha_{21}=2.25$: a saddle ($+0.07,\ -0.50$) between two stable axis states. **Predator-prey (basic)**: isoclines $H=m/ap=50$ (vertical) and $P=r/p=50$ (horizontal); eigenvalues $\pm0.707i$: a centre (neutral). **Predator-prey with logistic prey**: the prey isocline tilts down and the eigenvalues become $-0.125\pm0.60i$, a stable spiral ([[Lotka-Volterra Predator-Prey Model]]).

> [!pitfall] Intersection does not mean stability
> The isocline crossing is only a fixed point; its stability needs the Jacobian (the slope of the isoclines, in the competition model, decides the sign of $1-\alpha_{12}\alpha_{21}$). Trajectories cross a nullcline in a purely horizontal or vertical direction, and cannot cross each other. Higher-dimensional systems (three species) can show chaos, which a 2-D phase plane cannot (May 1976: it needs three dimensions for differential equations).

Basis: [[Fixed Points and Linear Stability]]. Uses: [[Lotka-Volterra Competition Model]], [[Alternative Stable States]].

Used in: [[EE04 Competition and Invasions]]. Related: [[Fixed Points and Linear Stability]] · [[Lotka-Volterra Competition Model]] · [[Lotka-Volterra Predator-Prey Model]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
