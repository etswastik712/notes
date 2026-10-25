---
title: Cdf Method for Transformations
aliases: ["transformation of random variables", "change of variables for densities"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Cdf Method for Transformations

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=27|class notes 9 Sep]], [[week1_mt2113.pdf#page=1|week 1 homework Q2]].

> [!intuition] In one picture
> To get the law of $Y=g(X)$, ask when $g(X)\le y$ and rewrite that event in terms of $X$.

> [!key] Definition
> $F_Y(y)=P[g(X)\le y]$; differentiate for the pdf. If $g$ is strictly increasing: $f_Y(y)=f_X(g^{-1}(y))\,\big|\frac{d}{dy}g^{-1}(y)\big|$. Discrete: $P[Y=y]=\sum_{g(x_i)=y}p(x_i)$.

## Examples
$A=\pi R^2$, $R\sim U(0,1)$: $F_A(a)=\sqrt{a/\pi}$ on $[0,\pi]$, $f_A=\frac1{2\sqrt{\pi a}}$. $Y=-\ln X$ for $X\sim U(0,1)$: $F_Y=1-e^{-y}$ (Exp$(1)$). $W=Z^2$ (non-monotone): $F_W(w)=2\Phi(\sqrt w)-1$, $f_W=\frac{e^{-w/2}}{\sqrt{2\pi w}}$ ($\chi^2_1$).

> [!pitfall] Non-monotone $g$
> $\{Z^2\le w\}=\{-\sqrt w\le Z\le\sqrt w\}$ has two branches; keeping only one halves the density.

Used in: [[PR05 Continuous Random Variables]]. Related: [[Law of the Unconscious Statistician]] · [[Cumulative Distribution Function]] · [[Uniform Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
