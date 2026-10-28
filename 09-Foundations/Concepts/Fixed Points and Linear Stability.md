---
title: Fixed Points and Linear Stability
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [argha]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/argha, status/draft]
---
# Fixed Points and Linear Stability

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** stability of steady states (Argha L3–L4) · 🔵 **extra:** Jacobian, discrete maps

> [!intuition] In one picture
> A ball in a bowl comes back when nudged (stable); a ball on a hilltop rolls off (unstable). The *slope of the restoring force* at the equilibrium, $f'(x^*)$, decides which, and its inverse is how long the return takes.

> [!key] Method
> For $\dot x=f(x)$, a **fixed point** satisfies $f(x^*)=0$. Linearise: $x=x^*+\theta$, $\dot\theta\approx f'(x^*)\,\theta$, so $\theta\propto e^{f'(x^*)t}$.
> - $f'(x^*)<0$: **stable** (perturbations decay), time constant $\tau=1/|f'(x^*)|$ ([[Relaxation Time]]).
> - $f'(x^*)>0$: **unstable**.
> - $f'(x^*)=0$: linear analysis inconclusive (a bifurcation point).

Graphical rule: a stable fixed point is where $f$ crosses zero *downwards* (positive to the left, negative to the right). With $f=-\mathrm dV/\mathrm dx$, stable points are minima of the potential $V$.

**Examples.** Climate: $f(T)=[\text{ASR}-\text{OLR}]/C$ ([[CL04 Feedback and Multiple Steady States]]). Ecology: logistic growth $f=rN(1-N/K)$: $f'(0)=r>0$ unstable, $f'(K)=-r<0$ stable ([[Ecology and Evolution - Course Map]]).

> [!extra-beyond]- Extra (beyond): higher dimensions and maps
> For $\dot{\mathbf x}=\mathbf f(\mathbf x)$ use the Jacobian $J_{ij}=\partial f_i/\partial x_j$: stable iff all eigenvalues have negative real part (in 2D: $\mathrm{tr}J<0$ and $\det J>0$). For a discrete map $x_{t+1}=g(x_t)$ the criterion is $|g'(x^*)|<1$; the logistic map loses stability at $g'=-1$ (period doubling, route to chaos; May 1976).

Applications of the same ideas: [[Bistability and Tipping Points]]; see also [[Linearisation and Sensitivity]].

> [!connection] See also
> Poles of the linearised system = eigenvalues of the Jacobian: [[Fourier and Laplace Transforms]] §7.6.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
