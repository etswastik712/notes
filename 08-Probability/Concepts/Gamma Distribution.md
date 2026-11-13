---
title: Gamma Distribution
aliases: ["Gamma(n,1)", "Erlang distribution", "sum of exponentials", "waiting time for the n-th event"]
subject: probability
type: concept
scope: [extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw6]
---
# Gamma Distribution

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** identified in the solution of [[hw6_edited.pdf#page=1|HW6]] Q2(b) (my derivation; the sheet does not name it).

> [!intuition] In one picture
> The time to collect $n$ independent $\mathrm{Expo}(1)$ waiting times: a sum of exponentials, so a bump whose peak moves out like $n-1$.

> [!key] Definition
> $V\sim\mathrm{Gamma}(n,1)$: $f_V(v)=\dfrac{v^{n-1}e^{-v}}{(n-1)!}$, $v>0$; mgf $(1-t)^{-n}$ ($t<1$); mean $n$, variance $n$. $V=\sum_{j=1}^nX_j$, $X_j$ iid $\mathrm{Expo}(1)$ (mgf product $\frac1{(1-t)^n}$). $-\ln(U_1\cdots U_n)\sim\mathrm{Gamma}(n,1)$ for iid $U_j\sim U(0,1)$.

The product $U=U_1\cdots U_n=e^{-V}$ has density $\dfrac{(-\ln u)^{n-1}}{(n-1)!}$ on $(0,1)$ and $E[U^k]=(k+1)^{-n}$. Checked for $n=5$: $V$ has mean $4.997$ and variance $4.990$; $E[U]=2^{-5}=0.03125$.

Used in: [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]]. Related: [[Exponential Distribution]] · [[Sum of Independent Random Variables]] · [[Moment Generating Function]] · [[Poisson Distribution]] · [[Probability Integral Transform]] · [[Change of Variables for Densities]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
