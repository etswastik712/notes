---
title: Skewness and Kurtosis
aliases: ["skewness", "kurtosis", "excess kurtosis"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Skewness and Kurtosis

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** AI notes §1.2–1.3.

> [!intuition] In one picture
> Skewness says which tail is longer; kurtosis says how heavy both tails are compared with the normal.

> [!key] Definition
> $\gamma_1=\frac{E[(X-\mu)^3]}{\sigma^3}$; kurtosis $\alpha_4=\frac{E[(X-\mu)^4]}{\sigma^4}$; excess $\gamma_2=\alpha_4-3$.

Normal: $0$, $0$. Exponential: $2$, $6$. Uniform: $0$, $-1.2$. Bernoulli$(\frac12)$: $0$, $-2$. Poisson$(\lambda)$: $\lambda^{-1/2}$, $\lambda^{-1}$ (for $3.2$: $0.559$, $0.3125$). Symmetric distributions have $\gamma_1=0$.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Moments of a Random Variable]] · [[Normal Distribution]] · [[Exponential Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
