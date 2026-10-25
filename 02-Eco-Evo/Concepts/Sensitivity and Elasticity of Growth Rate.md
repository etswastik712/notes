---
title: Sensitivity and Elasticity of Growth Rate
aliases: ["matrix sensitivity", "elasticity analysis", "perturbation analysis"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, caswell, crowder]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Sensitivity and Elasticity of Growth Rate

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the slide's version: raise one stage's survival by 10, 50 or 90 % and see how $\lambda$ changes (Crowder et al. 1994) ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=26|slide 26]])  ·  🟡 **extra · book:** the formulas of Caswell (1997): eigenvector expressions for sensitivity and elasticity

> [!intuition] In one picture
> Which knob matters most? Turn each survival or fecundity up a little, one at a time, and see how much the population growth rate responds. Aim management at the knob with the biggest response.

> [!key] Definition
> **Sensitivity** of $\lambda$ to a matrix entry: $s_{ij}=\partial\lambda/\partial a_{ij}=v_iw_j/(\mathbf v\!\cdot\!\mathbf w)$, with $\mathbf w,\mathbf v$ the right and left eigenvectors. **Elasticity** $e_{ij}=(a_{ij}/\lambda)\,s_{ij}$ is the proportional change of $\lambda$ per proportional change of $a_{ij}$; all elasticities sum to 1.

## Formulas and a table
For $\mathbf A\mathbf w=\lambda\mathbf w$ and $\mathbf v^{T}\mathbf A=\lambda\mathbf v^{T}$, a first-order perturbation gives $d\lambda=\mathbf v^{T}d\mathbf A\,\mathbf w/\mathbf v^{T}\mathbf w$, hence
$$s_{ij}=\frac{\partial\lambda}{\partial a_{ij}}=\frac{v_iw_j}{\mathbf v\!\cdot\!\mathbf w},\qquad e_{ij}=\frac{a_{ij}}{\lambda}s_{ij},\quad\sum_{ij}e_{ij}=1.$$
Sensitivity is the effect of a small *additive* change; elasticity the effect of a small *proportional* change, so elasticities compare entries of different size.

> [!example] Loggerhead matrix (computed from Table 2)
> $P_5$ (adult stays): $s=0.329$, $e=0.280$; $P_2,P_3,P_4$: $e=0.164,\ 0.129,\ 0.147$; $G_1,G_2,G_3$: $e=0.058$ each; $G_4$: $0.049$; $F_4,F_5$: $0.009,\ 0.049$. By type $P$ 0.72, $G$ 0.22, $F$ 0.06. The *sensitivity* of $G_3$ is the largest (2.90) because the entry is tiny; its elasticity is small.
> **By survival.** Elasticity of $\lambda$ to annual survival $\sigma_i$ (my self-consistent version): $0.04,\ 0.25,\ 0.29,\ 0.22,\ 0.21$ (sum 1): large juveniles first, then small juveniles. Raising $\sigma_3$ by 10 % raises $\lambda$ by about $0.29\times10\,\%=2.9\,\%$ (exact: $0.9516\to0.9786$).

> [!pitfall] Which elasticities sum to one?
> Only those with respect to *matrix entries*. For lower-level parameters (survival, stage duration) the elasticities "do not in general sum to one" (Caswell eq. 33). Crowder et al.'s Fig. 2 holds $\lambda$ fixed inside the stage-duration formula and sums to about 1.6; the ranking is the same.

Management use: change the entry with the largest elasticity that can actually be altered ([[Loggerhead Turtle and Turtle Excluder Devices]]). Linearisation background: [[Linearisation and Sensitivity]].

Used in: [[EE02 Structured Population Models]]. Related: [[Lefkovitch Stage-Structured Matrix]] · [[Loggerhead Turtle and Turtle Excluder Devices]] · [[Linearisation and Sensitivity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
