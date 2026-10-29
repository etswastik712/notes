---
title: Factorial Moments
aliases: ["E[X(X-1)]", "second factorial moment"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Factorial Moments

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Practice problems weekend of 12th September 2026.pdf#page=1|sheet 11–12 Sep, problems 2–5]] (method used to compute the variances).

> [!intuition] In one picture
> $x(x-1)$ cancels against $x!$ and $\binom nx$, making sums collapse.

> [!key] Definition
> $E[X(X-1)\cdots(X-r+1)]$; then $E[X^2]=E[X(X-1)]+E[X]$ and $\mathrm{Var}=E[X(X-1)]+E[X]-E[X]^2$.

Binomial: $n(n-1)p^2$. Poisson: $\lambda^2$ (and the $r$-th is $\lambda^r$). Geometric: $\frac{2q}{p^2}$. NegBin: use $n\binom{n-1}{r-1}=r\binom nr$ to get $E[Y^2]=\frac rp(\frac{r+1}p-1)$. Poisson recursion: $E[X^n]=\lambda E[(X+1)^{n-1}]$.

Used in: [[PR04 Joint Distributions Expectation and Variance]]. Related: [[08-Probability/Concepts/Variance|Variance]] · [[Binomial Distribution]] · [[Poisson Distribution]] · [[Geometric Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
