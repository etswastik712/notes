---
title: Folded Normal Distribution
aliases: ["half-normal", "|Z|", "folded normal"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw4]
---
# Folded Normal Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week2_notes.pdf#page=1|Week 2, p.1]] (cdf, pdf, mean, variance) and Homework 3 Q6 (the MGF). · 🔵 **extra · beyond:** the closed-form MGF and the half-normal name.

> [!intuition] In one picture
> Take the bell curve and fold the left half over onto the right: the density on $y\ge0$ doubles.

> [!key] Definition
> $X=|Z|$, $Z\sim N(0,1)$: $f_X(y)=\dfrac2{\sqrt{2\pi}}e^{-y^2/2}$ ($y\ge0$); $F_X(y)=2\Phi(y)-1$; $E[X]=\sqrt{2/\pi}=0.7979$; $E[X^2]=1$; $\mathrm{Var}[X]=1-\tfrac2\pi=0.3634$; $M_X(t)=2e^{t^2/2}\Phi(t)$.

## Derivation (lecture p.1)
$P[X\le c]=P[-c\le Z\le c]=F(c)-F(-c)$ for $c\ge0$; differentiate: $f_X(c)=f(c)+f(-c)=2f(c)$. $E[X]=\frac2{\sqrt{2\pi}}\int_0^\infty xe^{-x^2/2}\mathrm dx=\frac2{\sqrt{2\pi}}\int_0^\infty e^{-t}\mathrm dt$ with $t=x^2/2$. $E[X^2]=E[Z^2]=1$.

## MGF (Homework 3 Q6)
Two integrals: $\int_0^\infty e^{ty}f_X(y)\mathrm dy$ and, by LOTUS, $\int_{-\infty}^\infty e^{t|z|}\varphi(z)\mathrm dz$ (equal, even integrand). Complete the square: $2e^{t^2/2}\Phi(t)$; at $t=0.7$: $1.936967$ by both integrals and by the formula.

> [!pitfall] Folded vs half-normal
> The general "folded normal" is $|N(\mu,\sigma^2)|$; $|Z|$ is the special case $\mu=0$, $\sigma=1$ (half-normal). Its mean is *not* $0$ and its MGF is *not* $e^{t^2/2}$.

Used in: [[PR05 Continuous Random Variables]] §5, [[PR06 Moments Generating Functions and Limit Theorems]] §3.3. Related: [[Normal Distribution]] · [[Standard Normal Distribution]] · [[Cdf Method for Transformations]] · [[Moment Generating Function]] · [[Rayleigh Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
