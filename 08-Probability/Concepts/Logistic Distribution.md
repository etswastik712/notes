---
title: Logistic Distribution
aliases: ["logistic"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Logistic Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[week1_mt2113.pdf#page=4|week 1 p.4 (pdf, cdf)]], [[week1_mt2113.pdf#page=5|p.5 (mean)]].

> [!intuition] In one picture
> A bell-shaped law whose cdf is the logistic curve $\frac{e^x}{1+e^x}$.

> [!key] Definition
> $f(x)=\frac{e^x}{(1+e^x)^2}$, $F(x)=\frac{e^x}{1+e^x}$, symmetric about 0; $E[X]=0$, $\mathrm{Var}[X]=\frac{\pi^2}3=3.290$.

## Checks
Substitute $u=1+e^x$ to get $\int f=\int_1^\infty u^{-2}du=1$ and $F(x)=1-\frac1{1+e^x}$. $f(-x)=f(x)$, so $\int xf=0$ (odd integrand). Median 0; $P[X>1]=\frac1{1+e}=0.269$. The variance $\frac{\pi^2}3$ is a numerical result (simulation $3.292$).

Used in: [[PR05 Continuous Random Variables]]. Related: [[Probability Density Function]] · [[Normal Distribution]] · [[Cumulative Distribution Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Logistic Growth]] (Eco-Evo): the solution $N(t)=K/(1+e^{-r(t-t_0)})$ of logistic growth is $K$ times the cdf of a logistic distribution with location $t_0$ and scale $1/r$, so growth quantiles are logistic quantiles.
