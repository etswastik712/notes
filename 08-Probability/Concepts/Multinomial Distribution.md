---
title: Multinomial Distribution
aliases: ["multinomial random vector", "Mult_k(n,p)", "multinomial counts", "HW5 Problem 3"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw5]
---
# Multinomial Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[hw5.pdf#page=1|HW5]] Problem 3.
> 🔵 **extra · beyond:** rank, conditional laws, Poissonisation (mine, exactly checked).

> [!intuition] In one picture
> $n$ independent trials, each landing in one of $k$ boxes with probabilities $p_i$; $X_i$ counts the trials in box $i$. The binomial is the case $k=2$.

> [!key] Definition
> $P(X=x)=\frac{n!}{x_1!\cdots x_k!}\prod p_i^{x_i}$ on $\sum x_i=n$. $E X_i=np_i$, $\mathrm{Var}X_i=np_i(1-p_i)$, $\mathrm{Cov}(X_i,X_k)=-np_ip_k$. Marginals binomial; $X_1\mid X_2=x_2\sim\mathrm{Bin}(n-x_2,\frac{p_1}{1-p_2})$; independent $\mathrm{Poisson}(\mu p_i)$ counts conditioned on their sum $n$ are multinomial.

Fair die, 12 rolls: $\mathrm{Var}=1.667$, $\mathrm{Cov}=-0.333$, $P(\text{every face twice})=0.003438$.

Used in: [[PR08 Order Statistics and the Multinomial Distribution]], [[PR01 Counting and the Axioms of Probability]]. Related: [[Multinomial Covariance Matrix]] · [[Multinomial Coefficient]] · [[Binomial Distribution]] · [[Indicator Random Variable]] · [[Poisson Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Microstate]] (Thermodynamics): occupation numbers of microstates are multinomial; the constraint sum n_i = N is why the counts are negatively correlated.
