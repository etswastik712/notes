---
title: Probability Integral Transform
aliases: ["universality of the uniform", "inverse transform sampling", "F(X) is uniform"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Probability Integral Transform

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (as a computation):** $E[F(X)]=\tfrac12$, Homework 2 Q3 ([[Week2_notes.pdf#page=5|Week 2, p.5]]). · 🔵 **extra · beyond:** the general statement and sampling.

> [!intuition] In one picture
> Pushing a continuous variable through its own cdf flattens it into a uniform on $(0,1)$; run it backwards to manufacture any distribution from random numbers.

> [!key] Definition
> If $X$ is continuous with cdf $F$ then $F(X)\sim U(0,1)$; if $U\sim U(0,1)$ then $F^{-1}(U)$ has cdf $F$.

## Proof
$P[F(X)\le u]=P[X\le F^{-1}(u)]=F(F^{-1}(u))=u$ for $0<u<1$. Hence $E[F(X)]=E[U]=\tfrac12$ (and $E[F(X)^2]=\tfrac13$); the LOTUS route gives the same, $\int F\,F'\,\mathrm dx=[\tfrac12F^2]=\tfrac12$.

## Sampling
$X=-\ln(U)/\lambda$ is Expo$(\lambda)$ ($P[-\ln U\le y]=1-e^{-y}$); $Y=-\ln(-\ln U)$ is Gumbel; $X=U^{-1/a}$ is Pareto$(a)$. Checked by simulation for the normal, exponential, Rayleigh and uniform laws ($E[F(X)]=0.4995$–$0.5000$).

> [!pitfall] Needs a continuous cdf
> For a discrete $X$, $F(X)$ is not uniform (it takes only finitely many values).

Used in: [[PR05 Continuous Random Variables]] §4 (HW2 Q3). Related: [[Cumulative Distribution Function]] · [[Uniform Distribution]] · [[Cdf Method for Transformations]] · [[Law of the Unconscious Statistician]] · [[Gumbel Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
