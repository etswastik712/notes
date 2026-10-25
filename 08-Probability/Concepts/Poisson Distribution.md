---
title: Poisson Distribution
aliases: ["Poisson", "rare events"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Poisson Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=21|class notes 27 Aug]], [[Practice problems weekend of 12th September 2026.pdf#page=1|sheet 11–12 Sep]].

> [!intuition] In one picture
> The count of rare events when there are many chances and each is unlikely.

> [!key] Definition
> $P[X=n]=e^{-\lambda}\frac{\lambda^n}{n!}$, $n\ge0$. $E[X]=\mathrm{Var}[X]=\lambda$; MGF $e^{\lambda(e^t-1)}$; $E[X^n]=\lambda E[(X+1)^{n-1}]$.

## Normalisation and moments
$\sum\frac{\lambda^i}{i!}=e^\lambda$ forces $c=e^{-\lambda}$. $E[X(X-1)]=\lambda^2$, so $\mathrm{Var}=\lambda$; $E[X^3]=\lambda^3+3\lambda^2+\lambda$ ($=22$ at $\lambda=2$). Mode: $\lfloor\lambda\rfloor$ (two modes if $\lambda$ is an integer).

> [!example] Alpha particles
> 3.2 particles per second on average; $P[X\le2]=0.3799$ (the binomial with $N$ atoms each emitting with probability $3.2/N$ gives $0.3758$ at $N=100$ and $0.3795$ at $N=1000$).

> [!pitfall] Mean = variance
> If the variance clearly exceeds the mean (over-dispersion) the data are not Poisson.

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR04 Joint Distributions Expectation and Variance]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Poisson Limit Theorem]] · [[Binomial Distribution]] · [[Moment Generating Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
