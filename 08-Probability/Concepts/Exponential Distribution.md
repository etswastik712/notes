---
title: Exponential Distribution
aliases: ["exponential", "Exp(lambda)", "Expo(lambda)", "waiting time distribution"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Exponential Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week2_notes.pdf#page=1|Week 2, pp.1–5]] (pdf and cdf, moments, geometric limit, memorylessness and its characterisation), Homework 2 Q1; MGF and skewness in [[Week3_notes.pdf#page=3|Week 3]] and Homework 3. · 🔵 **extra · beyond:** the Rayleigh link, the Gumbel limit, the sampling formula.

> [!intuition] In one picture
> The waiting time until a random event that has no memory; the continuous analogue of the geometric distribution.

> [!key] Definition
> $f(x)=\lambda e^{-\lambda x}$, $F(x)=1-e^{-\lambda x}$, $P[X\ge x]=e^{-\lambda x}$ ($x\ge0$); $E[X^n]=\dfrac{n!}{\lambda^n}$, $E[X]=\dfrac1\lambda$, $\mathrm{Var}[X]=\dfrac1{\lambda^2}$; MGF $\dfrac\lambda{\lambda-t}$ ($t<\lambda$); median $\dfrac{\ln2}\lambda$; mode $0$; skewness $2$, excess kurtosis $6$.

## The Week 2 derivations
- **Moments:** $I_n=\int_0^\infty\lambda x^ne^{-\lambda x}\mathrm dx=\frac n\lambda I_{n-1}\Rightarrow I_n=n!/\lambda^n$ (by parts).
- **Geometric limit:** failures before the first success, $P[G\ge k]=q^k$; with $p=\lambda h$, $kh\to x$: $(1-\lambda h)^{x/h}\to e^{-\lambda x}$. For $\lambda=\tfrac12$, $x=2$: $0.3164,0.3585,0.3670,0.3678\to0.3679$.
- **Memoryless:** $P[X\ge t+s\mid X\ge s]=P[X\ge t]$, and **only** Geom and Expo have it ([[Memoryless Property]]). Example: repair time with $\lambda=\tfrac12$: $P[T\ge10\mid T>9]=e^{-1/2}=0.6065$.

## Relatives
$-\ln U\sim\mathrm{Expo}(1)$ for $U\sim U(0,1)$; if $R$ is Rayleigh then $R^2/2\sim\mathrm{Expo}(1)$; the maximum of $n$ i.i.d. Expo$(1)$ minus $\ln n$ is asymptotically Gumbel ([[Gumbel Distribution]]); $e^{\mathrm{Expo}(a)}$ is Pareto ([[Pareto Distribution]]). Mean $>$ median $>$ mode: $1/\lambda>0.693/\lambda>0$ ([[Median and Mode]]).

> [!pitfall] Rate versus mean
> Expo$(\lambda)$ has **rate** $\lambda$ and mean $1/\lambda$; software often takes the scale $1/\lambda$ (`scipy.stats.expon(scale=1/lam)`). Homework 2 used $\lambda=\tfrac12$, i.e. mean 2 hours.

Used in: [[PR05 Continuous Random Variables]] §6, [[PR06 Moments Generating Functions and Limit Theorems]] §3. Related: [[Memoryless Property]] · [[Geometric Distribution]] · [[Rayleigh Distribution]] · [[Gumbel Distribution]] · [[Probability Integral Transform]] · [[Moment Generating Function]].


## Continued in the vault (added 2026-11-07)
- Minimum and gaps of several exponentials: [[Exponential Order Statistics]] ([[PR08 Order Statistics and the Multinomial Distribution]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Radioactive Decay Law]] (Landscapes): each nucleus's decay time is exponential with mean $\tau=1/\lambda$; the decay law is its survival function and $t_{1/2}=\tau\ln2$ its median.
