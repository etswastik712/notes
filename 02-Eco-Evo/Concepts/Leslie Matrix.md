---
title: Leslie Matrix
aliases: ["age-structured model", "age-structured projection"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Leslie Matrix

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the 4-class example: $P=(0.5,0.2,0.1,0)$, $F=(0,2,1,1)$, 200 newborns, 200 steps, $\lambda=1.05082$ ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=15|slide 15]])

> [!intuition] In one picture
> Keep a separate count for each age. Each year every age class either moves up one step (if it survives) or has babies that land in the first class. A matrix is just the book-keeping for that.

> [!key] Definition
> $\mathbf n_{t+1}=\mathbf L\,\mathbf n_t$ where the first row of $\mathbf L$ holds the fecundities $F_x$, the sub-diagonal holds the survival probabilities $P_x$ (class $x\to x+1$) and every other entry is 0. After transients the total grows by a fixed factor $\lambda$ per step and the age proportions become constant ([[Stable Age Distribution]]).

## Anatomy and use
For age classes $1,\dots,k$ the projection is $\mathbf n_{t+1}=\mathbf L\mathbf n_t$ with fecundities $F_x$ in the first row and survival probabilities $P_x$ on the sub-diagonal. In a *post-breeding* census (counted just after reproduction, as Crowder et al. do) $F_x=P_x\cdot m_{x+1}$ and newborns are counted at the next census; in a *pre-breeding* census the roles shift by one class. Different conventions give different but equivalent matrices.

> [!example] Slide example by hand
> $P=(0.5,0.2,0.1)$, $F=(0,2,1,1)$, start $(200,0,0,0)$: $t=1:(0,100,0,0)$; $t=2:(200,0,20,0)$; $t=3:(20,100,0,2)$; totals $200,100,220,122$. The zig-zag is a negative second eigenvalue ($-0.952$) of the two-step loop $F_2P_1=1$. The simulation settles to $\lambda=1.05082$ and proportions $0.635,\ 0.302,\ 0.057,\ 0.005$ (40 steps to within 0.01).
> **Another matrix.** $F=(0,1.2,0.8)$, $P=(0.5,0.4)$ has $R_0=0.76<1$ and $\lambda=0.884$: an 11.6 % annual decline with shares $(0.549,0.311,0.141)$.

**Assumptions.** Rates constant in time and independent of density (so growth is geometric forever), individuals in a class identical, a single sex (usually females). Relaxing them gives density-dependent, stochastic or stage-based matrices ([[Lefkovitch Stage-Structured Matrix]]).

> [!extra-beyond]- 🔵 Extra (beyond): reproductive value
> The left eigenvector $\mathbf v$ ($\mathbf v^{T}\mathbf L=\lambda\mathbf v^{T}$) is the **reproductive value**: an individual's expected contribution to the long-term population. For the slide matrix $\mathbf v\propto(1,\ 2.10,\ 1.04,\ 0.95)$: a 1-year-old is worth twice a newborn because it has survived the risky first step. Reproductive value and the [[Stable Age Distribution]] together give the sensitivities of $\lambda$ ([[Sensitivity and Elasticity of Growth Rate]]).

Used in: [[EE02 Structured Population Models]]. Related: [[Stable Age Distribution]] · [[Dominant Eigenvalue and Perron-Frobenius Theorem]] · [[Net Reproductive Rate]] · [[Lefkovitch Stage-Structured Matrix]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Eigenstate and Eigenvalue]] (Quantum Mechanics): both are matrix eigenproblems: the dominant eigenvalue of the Leslie matrix is the growth rate, and Perron-Frobenius (a positive dominant eigenvector) is the matrix analogue of a nodeless, non-degenerate ground state.
- [[Fibonacci Numbers]] (Analysis): Fibonacci's rabbits are a two-age-class Leslie model: $N_{t+2}=N_{t+1}+N_t$ is the matrix $\begin{pmatrix}1&1\\1&0\end{pmatrix}$ whose dominant eigenvalue is the golden ratio $\varphi$, the asymptotic growth factor.
