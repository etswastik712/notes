---
title: Law of the Unconscious Statistician
aliases: ["LOTUS"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Law of the Unconscious Statistician

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=21|class notes 27 Aug (discrete)]], [[week1_mt2113.pdf#page=6|week 1 pp.6–7 (continuous, proof)]].

> [!intuition] In one picture
> To average $g(X)$, average $g$ against the distribution of $X$; you never need the distribution of $g(X)$.

> [!key] Definition
> $E[g(X)]=\sum_ig(x_i)p(x_i)$ (discrete), $E[g(X)]=\int g(x)f(x)\,\mathrm dx$ (continuous).

## Proof (discrete)
Group the $x_i$ by the value $y_j=g(x_i)$: $\sum_ig(x_i)p(x_i)=\sum_jy_j\sum_{x_i\in S_j}p(x_i)=\sum_jy_jP[Y=y_j]=E[Y]$.

## Proof (continuous, $g\ge0$)
Use the lemma $E[Y]=\int_0^\infty P[Y>y]\,\mathrm dy$ and swap the order of integration: $\int_0^\infty\!\int_{\{g>y\}}f\,\mathrm dx\,\mathrm dy=\int f(x)\,g(x)\,\mathrm dx$. For general $g$ split $g=g^+-g^-$.

> [!example] Random circle
> $R\sim U(0,1)$, $A=\pi R^2$: $E[A]=\int_0^1\pi r^2\mathrm dr=\frac\pi3$, $E[A^2]=\frac{\pi^2}5$, $\mathrm{Var}=\frac{4\pi^2}{45}$, without finding the density of $A$.

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR05 Continuous Random Variables]]. Related: [[Expectation]] · [[08-Probability/Concepts/Variance|Variance]] · [[Cdf Method for Transformations]] · [[Linearity of Expectation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
