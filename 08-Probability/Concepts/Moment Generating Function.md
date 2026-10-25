---
title: Moment Generating Function
aliases: ["MGF", "mgf"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Moment Generating Function

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** AI notes `probability_moments_and_mgf_notes.pdf` §2 (including the course policy: derive any named MGF from first principles before using it).

> [!intuition] In one picture
> A function whose Taylor coefficients are the moments, and which multiplies when independent variables are added.

> [!key] Definition
> $M_X(t)=E[e^{tX}]$ (finite near 0). $E[X^k]=M_X^{(k)}(0)$; $M_{aX+b}(t)=e^{bt}M_X(at)$; $M_{\sum X_i}=\prod M_{X_i}$ for independent $X_i$; equal MGFs near 0 imply equal laws.

## First-principles table (derive before use)
Bernoulli $q+pe^t$; Binomial $(q+pe^t)^n$; Poisson $e^{\lambda(e^t-1)}$; Geometric $\frac{pe^t}{1-qe^t}$ ($t<-\ln q$); Exponential $\frac\lambda{\lambda-t}$ ($t<\lambda$); Uniform $\frac{e^{tb}-e^{ta}}{t(b-a)}$; Normal $e^{\mu t+\sigma^2t^2/2}$ (complete the square).

> [!example] Independent normals
> $M_{X+Y}=e^{(\mu_1+\mu_2)t+\frac12(\sigma_1^2+\sigma_2^2)t^2}$, so $X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

The Cauchy has no MGF.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Moments of a Random Variable]] · [[Central Limit Theorem]] · [[Poisson Limit Theorem]] · [[Normal Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
