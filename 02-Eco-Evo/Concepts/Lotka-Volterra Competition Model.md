---
title: Lotka-Volterra Competition Model
aliases: ["Lotka-Volterra competition equations", "competition equations", "alpha coefficients"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Lotka-Volterra Competition Model

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the equations, the zero-growth isoclines, and the main message: in 3 of 4 parameter regions one species excludes the other ([[04-Competition_25-Aug_2026.pdf#page=10|slide 10]])

> [!intuition] In one picture
> Each species follows logistic growth, but the other species' individuals count against its carrying capacity, each worth $\alpha$ of its own. Who wins depends on whether each species hurts itself more than it hurts the other.

> [!key] Definition
> $$\frac{dN_1}{dt}=\frac{r_1N_1\,(K_1-N_1-\alpha_{12}N_2)}{K_1},\qquad \frac{dN_2}{dt}=\frac{r_2N_2\,(K_2-N_2-\alpha_{21}N_1)}{K_2}$$ $\alpha_{12}$ is the effect of one individual of species 2 on the growth of species 1. Isoclines: $N_1=K_1-\alpha_{12}N_2$ and $N_2=K_2-\alpha_{21}N_1$. Stable coexistence needs $\alpha_{12}<K_1/K_2$ and $\alpha_{21}<K_2/K_1$.

## From the logistic to four outcomes
With $\alpha_{ij}$ the effect of an individual of species $j$ on species $i$, in units of species-$i$ individuals:
$$\dot N_1=\frac{r_1N_1(K_1-N_1-\alpha_{12}N_2)}{K_1},\qquad \dot N_2=\frac{r_2N_2(K_2-N_2-\alpha_{21}N_1)}{K_2}.$$
Isoclines: $N_1=K_1-\alpha_{12}N_2$ (intercepts $K_1$, $K_1/\alpha_{12}$) and $N_2=K_2-\alpha_{21}N_1$ (intercepts $K_2$, $K_2/\alpha_{21}$). The line that lies outside the other on both axes wins; if each lies outside on one axis there is an interior equilibrium: stable if $\alpha_{12}\alpha_{21}<1$ (coexistence), a saddle if $>1$ (priority effect).

> [!example] $K_1=100$, $K_2=80$, $r_1=r_2=0.5$
> - $\alpha_{12}=0.5,\ \alpha_{21}=1.5$: species 1 wins; $\alpha_{12}=1.5,\ \alpha_{21}=0.5$: species 2 wins.
> - $\alpha_{12}=0.5,\ \alpha_{21}=0.6$: coexistence at $(85.7,\ 28.6)$; Jacobian eigenvalues $-0.50,\ -0.107$.
> - $\alpha_{12}=\alpha_{21}=1.5$: interior point $(16,\ 56)$ is a saddle (eigenvalues $+0.07,\ -0.50$); both axis states are stable.
> Coexistence thresholds: $\alpha_{12}<K_1/K_2=1.25$ and $\alpha_{21}<K_2/K_1=0.8$.

**$\alpha$ from niche overlap.** For bell-shaped resource use of width $\sigma$ whose centres are $d$ apart, $\alpha=\exp(-d^2/4\sigma^2)$: 1 for equal species, 0.78 at $d=\sigma$, 0.37 at $d=2\sigma$. Partitioning lowers $\alpha$ ([[Niche Partitioning]]).

> [!pitfall] The usual slips
> Index order: $\alpha_{12}$ is the effect of 2 *on* 1. "3 of 4 regions give exclusion" does not mean exclusion is common in nature; it means a model with one shared resource and linear effects needs *self-limitation to exceed cross-limitation* for coexistence. Slide 11 shows three of the four panels; the fourth is the mirror of the first. Phase-plane method: [[Phase Plane and Isoclines]].

Used in: [[EE04 Competition and Invasions]]. Related: [[Phase Plane and Isoclines]] · [[Competitive Exclusion Principle]] · [[Logistic Growth]] · [[Niche Partitioning]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
