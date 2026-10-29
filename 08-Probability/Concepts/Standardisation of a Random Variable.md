---
title: Standardisation of a Random Variable
aliases: ["z-score", "standardise"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Standardisation of a Random Variable

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Practice problems weekend of 12th September 2026.pdf#page=2|sheet 11–12 Sep, problem 9]].

> [!intuition] In one picture
> Subtract the mean and divide by the standard deviation to measure in units of spread.

> [!key] Definition
> $Y=\frac{X-\mu}\sigma$ has $E[Y]=0$, $\mathrm{Var}[Y]=1$; discrete: $P[Y=y]=p(\mu+\sigma y)$, $F_Y(y)=F_X(\mu+\sigma y)$.

$N(\mu,\sigma^2)$ is defined by $X=\sigma Z+\mu$. The CLT is a statement about the standardised sum $S_n^*=\frac{S_n-n\mu}{\sigma\sqrt n}$. It makes distributions comparable and tables universal.

Used in: [[PR04 Joint Distributions Expectation and Variance]], [[PR05 Continuous Random Variables]]. Related: [[Standard Normal Distribution]] · [[Central Limit Theorem]] · [[08-Probability/Concepts/Variance|Variance]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
