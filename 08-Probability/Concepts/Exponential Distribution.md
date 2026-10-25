---
title: Exponential Distribution
aliases: ["exponential", "Exp(lambda)"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Exponential Distribution

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Blitzstein and Hwang Ch. 5; the AI notes' MGF section. Not in the class notes seen.

> [!intuition] In one picture
> The waiting time until a random event that has no memory.

> [!key] Definition
> $f(x)=\lambda e^{-\lambda x}$, $F(x)=1-e^{-\lambda x}$ ($x\ge0$); $E[X]=\frac1\lambda$, $\mathrm{Var}[X]=\frac1{\lambda^2}$, $E[X^k]=\frac{k!}{\lambda^k}$; MGF $\frac\lambda{\lambda-t}$ ($t<\lambda$).

$E[X]=\int_0^\infty P[X>y]dy=\int e^{-\lambda y}dy=\frac1\lambda$ (tail formula). Skewness 2, excess kurtosis 6 for every $\lambda$. If $U\sim U(0,1)$ then $-\ln U\sim$ Exp$(1)$. The continuous analogue of the [[Geometric Distribution]].

Used in: [[PR05 Continuous Random Variables]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Memoryless Property]] · [[Geometric Distribution]] · [[Rayleigh Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
