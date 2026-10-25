---
title: Stable Age Distribution
aliases: ["SAD", "stable stage distribution"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Stable Age Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the simulation and its two lessons: total size grows exponentially; age proportions become constant ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=19|slide 19]])

> [!intuition] In one picture
> Shake a box of marbles and it settles. Whatever age mix you start with, the matrix keeps squeezing the population toward one shape that it only rescales.

> [!key] Definition
> After transients, $\mathbf n_t\to c\,\lambda^t\mathbf w$: the age proportions are fixed by the right eigenvector $\mathbf w$ of $\mathbf L$ (normalised to sum 1) and the whole population multiplies by the dominant eigenvalue $\lambda$ each step.

## Where the SAD comes from
Seek $\mathbf n_t=\lambda^t\mathbf w$. The sub-diagonal rows give $\lambda w_{x+1}=P_xw_x$, so $w_x=w_1\,l_x\lambda^{-(x-1)}$ with $l_x=P_1\cdots P_{x-1}$; the first row then gives the discrete **Euler-Lotka** condition $1=\sum_xF_xl_x\lambda^{-x}$, whose single positive root is $\lambda$. The right-hand side falls as $\lambda$ rises and equals $R_0$ at $\lambda=1$, so $\lambda>1\iff R_0>1$.

> [!example] Check with the slide
> $1=\dfrac1{\lambda^2}+\dfrac{0.1}{\lambda^3}+\dfrac{0.01}{\lambda^4}$ gives $\lambda=1.05082$. Then $w_2/w_1=P_1/\lambda=0.5/1.0508=0.4758$ and the slide's ratio is $0.302108/0.634921=0.4758$ ✓.
> **How fast.** Starting from anything, $\mathbf n_t=\sum c_i\lambda_i^t\mathbf w_i$. The slowest-decaying transient decays like $(|\lambda_2|/\lambda_1)^t=(0.9518/1.0508)^t=0.906^t$: 40 steps to within one percentage point. A large $|\lambda_2|/\lambda_1$ means long transients (an age structure that "remembers" past booms).

> [!pitfall] Stable is not static, and it needs primitivity
> The SAD is a *shape* (proportions); the numbers keep growing at $\lambda$. If only one age class reproduces (semelparous: $F_3=6$, $P=(0.5,0.4)$) the matrix is imprimitive: totals repeat $100,50,20,120,60,24,144\dots$ and no SAD exists. In real populations, recent history (a drought gap, a baby boom) leaves bumps for many years: [[Age Pyramid]].

Used in: [[EE02 Structured Population Models]]. Related: [[Leslie Matrix]] · [[Dominant Eigenvalue and Perron-Frobenius Theorem]] · [[Relaxation Time]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
