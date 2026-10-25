---
title: Net Reproductive Rate
aliases: ["R0", "R_0", "basic reproductive number of a cohort"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Net Reproductive Rate

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $R_0$ as the average number of offspring per individual ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=10|slide 10]])  ·  🔵 **extra · beyond:** generation time, $r\approx\ln R_0/T$, Euler-Lotka equation

> [!intuition] In one picture
> If the average newborn leaves more than one newborn behind, each generation is larger than the last.

> [!key] Definition
> $$R_0=\sum_x l_x m_x$$ the mean number of offspring produced by a newborn over its lifetime. $R_0>1$: the population grows from generation to generation; $R_0<1$: it declines. From the slide's table the column sum is $\approx 2.42$.

## From $R_0$ to a rate per unit time
$R_0=\sum_xl_xm_x$ is a growth factor *per generation*. To convert it, you need the generation length: $T=\sum_xx\,l_xm_x/R_0$ (the mean age of reproduction), and then $r\approx\ln R_0/T$. The exact $r$ solves the **Euler-Lotka equation** $\sum_xe^{-rx}l_xm_x=1$ (discrete form: $\sum_xF_xl_x\lambda^{-x}=1$, see [[Stable Age Distribution]]). Both give the same threshold: $r>0\iff\lambda>1\iff R_0>1$.

> [!example] *Phlox*
> $R_0=2.4177$ (slide; 2.4176 from the printed columns). With class mid-points in days, $T=331$ d and $r\approx\ln2.4177/331=0.00267\ \text{d}^{-1}$, which the Euler-Lotka root confirms; per 365 days, $e^{0.00267\times365}=2.65$. Because *Phlox* is an annual with non-overlapping generations, Molles uses $\lambda=R_0=2.4177$ per year and projects $N_t=996\times2.4177^t$ (1.16 million after 8 years).
> **The Leslie example** of the slides has $R_0=\sum l_xF_x=0+1+0.1+0.01=1.11>1$ and indeed $\lambda=1.0508>1$.

> [!pitfall] $R_0$ is not $\lambda$
> They coincide only for non-overlapping generations. With overlap, $\lambda$ is the dominant eigenvalue of the projection matrix ([[Dominant Eigenvalue and Perron-Frobenius Theorem]]) and $R_0$ is the spectral radius of the *next-generation* matrix; they agree on whether the population grows. Also, human **replacement fertility**: $R_0=\text{TFR}\times0.488\times s=1$ gives TFR $\approx2.05/s\approx2.1$ ([[Age Pyramid]]).

Used in: [[EE02 Structured Population Models]]. Related: [[Cohort Life Table]] · [[Leslie Matrix]] · [[Exponential Growth]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
