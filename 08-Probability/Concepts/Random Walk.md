---
title: Random Walk
aliases: [simple random walk, Polya theorem, drunkard's walk]
subject: probability
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/probability, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Random Walk

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond** ([[THX1 Diffusion Random Walks and the Heat Equation]] §1; no random-walk material in the PR chapters).

> [!intuition] In one picture
> Add up independent unbiased steps and the position spreads like $\sqrt{\text{time}}$.

> [!key] Definition and key results
> Steps $\pm\ell$ every $\tau$: $\langle x\rangle=0$, $\langle x^2\rangle=n\ell^2=2Dt$, $D=\ell^2/2\tau$; Gaussian by the CLT (kurtosis 2.92 at 25 steps, 2.99 at 400); in $d$ dimensions $\langle r^2\rangle=2dDt$. Pólya: returns to the origin with probability 1 in $d=1,2$ and 0.3405 in $d=3$.

> [!pitfall] Pitfall
> $\sqrt t$ growth needs *zero mean* steps; a bias adds a linear drift $vt$.

Used in: [[THX1 Diffusion Random Walks and the Heat Equation]]. Related: [[Central Limit Theorem]] · [[Normal Distribution]] · [[Binomial Distribution]] · [[Diffusion Equation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Diffusion Equation]] (Thermodynamics): the continuum limit; [[Wright-Fisher Drift as Diffusion]] (Eco-Evo): a random walk in gene frequency
- [[Gaussian Integral]] (Foundations): the normalisation of the kernel
- [[TH06 From Kinetic Theory to Statistical Mechanics]] (Thermodynamics): molecular collisions are a random walk of the velocity and position of a molecule; the mean free path and collision time give $D=\ell^2/2\tau$.
