---
title: Skewness and Kurtosis
aliases: ["skewness", "kurtosis", "excess kurtosis", "shape of a distribution"]
subject: probability
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/probability, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Skewness and Kurtosis

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week3_notes.pdf#page=2|Week 3, p.2]] (definitions) and Homework 3 Q3 (the skewness of the exponential). · 🟡 **extra · book:** AI notes §1.2–1.3 (further values).

> [!intuition] In one picture
> Skewness says which tail is longer; kurtosis says how heavy both tails are compared with the normal.

> [!key] Definition
> $\gamma_1=\dfrac{E[(X-\mu)^3]}{\sigma^3}$; kurtosis $\alpha_4=\dfrac{E[(X-\mu)^4]}{\sigma^4}$; **excess** $\gamma_2=\alpha_4-3$. The lecture writes $\mathrm{Kurtosis}(X)=E[(\frac{X-\mu}\sigma)^4]-3$, i.e. it already means the **excess**.

Normal: $0$, $0$. Exponential: $2$, $6$ (every $\lambda$; HW3 Q3: $E[(X-\mu)^3]=2/\lambda^3$, long right tail, scale-invariant). Uniform: $0$, $-1.2$. Bernoulli$(\tfrac12)$: $0$, $-2$. Poisson$(\lambda)$: $\lambda^{-1/2}$, $\lambda^{-1}$ ($3.2$: $0.559$, $0.3125$). Gumbel: $1.1395$, $2.4$. Symmetric laws have $\gamma_1=0$. For the oscillator, the position kurtosis $\langle x^4\rangle/\langle x^2\rangle^2$ is $3$ for $n=0$ and $\to1.5$ (arcsine) as $n\to\infty$ ([[Oscillator Expectation Values]]).

> [!pitfall] Which kurtosis?
> Books differ by $3$: "kurtosis $=3$" (normal) versus "excess $=0$". The course's lecture uses the excess form; state the convention.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]] §1. Related: [[Moments of a Random Variable]] · [[Normal Distribution]] · [[Exponential Distribution]] · [[Median and Mode]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
