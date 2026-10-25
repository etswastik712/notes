---
id: introduction-to-probability/2026-09-10-class-notes-10th-september-2026
aliases: [Class notes 10 Sep 2026]
tags: [probability, mt2113, class-notes, continuous-random-variables, pdf]
trust_tier: agent_written
---

# Class notes 10th September 2026

## Covered
**Continuous random variable (definition 1, via the cdf).** $X$ is continuous if its cdf $F$ is absolutely continuous everywhere (the definition of absolute continuity is not needed; it implies that $F(x)=P[X\le x]$ is continuous for all $x\in\mathbb R$). Only real-valued random variables are considered (Classroom: Class notes 10th September 2026.pdf).

**Why $P[X=x]=0$.**
- The cdf of any random variable is right-continuous: $\lim_{y\to x^+}F(y)=F(x)$ (proof not in the syllabus).
- Also $\lim_{y\to x^-}F(y)=F(x^-)=P[X<x]$ (1.1) (follows from the properties of probability in Section 2 of the 12 August notes; not in the syllabus).
- If $F$ is continuous, $\lim_{y\to x^-}F(y)=F(x)$ (1.2). Comparing (1.1) and (1.2):
$$P[X=x]=F(x)-F(x^-)=0\quad\text{for every }x\in\mathbb R.$$

**Continuous random variable (definition 2, via a density).** There is a function $f\ge 0$ on $\mathbb R$ with
$$P[X\in B]=\int_B f(x)\,dx\quad\text{for every ``reasonable'' (measurable) }B\subset\mathbb R.$$
$f$ is the probability density function (pdf). Measurability need not be worried about for now.

**Why "density".** If $f$ is well-behaved near $x$ (e.g. continuous at $x$) and $\varepsilon>0$ is tiny,
$$P[x-\varepsilon<X<x+\varepsilon]=\int_{x-\varepsilon}^{x+\varepsilon}f(y)\,dy\approx f(x)\cdot 2\varepsilon,$$
so probability "mass" of the interval $\approx$ density $\times$ "volume" $2\varepsilon$.

**Properties of a pdf.**
1. $f(x)\ge 0$ for each $x\in\mathbb R$.
2. $\int_{-\infty}^{\infty}f(x)\,dx=1$ (compare with $\sum_i p(x_i)=1$ for a pmf).

**Probabilities from the pdf.**
- $P[X=x]=\int_x^x f(y)\,dy=0$ (motivated in the 9 September class by measurement errors).
- For $a,b\in\mathbb R$: $P[a<X<b]=P[a\le X<b]=P[a<X\le b]=P[a\le X\le b]=\int_a^b f(x)\,dx$.
- cdf from pdf: $F(x)=P[X\le x]=P[X<x]=\int_{-\infty}^x f(y)\,dy$.
- pdf from cdf: $F'(x)=f(x)$ for each $x$ (where $F$ is differentiable).

**cdf versus pdf and pmf.** The cdf is the fundamental object, defined for every random variable; a pdf exists only for continuous random variables, a pmf only for discrete ones. To find the distribution of a random variable, usually find its cdf first and, if it is continuous, differentiate to get the pdf.

**Expectation and variance.**
- $E[X]=\int_{-\infty}^\infty x f(x)\,dx$: a weighted average in integral form.
- For a function $g$ on $\mathbb R$ (or on the support of $X$): $E[g(X)]=\int_{-\infty}^\infty g(x)f(x)\,dx$ (1.3). Only the identity is examined; the proof (for non-negative $g$, possibly shown in class) is not in the syllabus.
- $\operatorname{Var}[X]=E[(X-\mu)^2]=\int_{-\infty}^\infty (x-\mu)^2 f(x)\,dx$ with $\mu=E[X]$; also $\operatorname{Var}[X]=E[X^2]-(E[X])^2=\int x^2f(x)\,dx-\big(\int xf(x)\,dx\big)^2$.
- $E[aX+b]=aE[X]+b$ and $\operatorname{Var}[aX+b]=a^2\operatorname{Var}[X]$.
- Linearity: $E\big[\sum_{i=1}^nX_i\big]=\sum_{i=1}^nE[X_i]$ for any random variables, continuous, discrete or mixed.

**Emphasis (from the post).** Continuous random variables are not easy or intuitive at first; only 2-3 classes are spent on them, so they carry somewhat less weight in the mid-semester examination than the topics covered in far greater detail so far.

## From the post
Dear everyone, here are the class notes for today. Please note that certain concepts pertaining to continuous random variables are not necessarily easy or intuitive to grasp at the beginning, and as such, we shall spend only 2-3 classes on this topic -- hence, the emphasis on continuous random variables in the mid-semester examination will be somewhat less compared to the remaining topics that have been covered (in far greater detail) so far.

## Files
- [Class notes 10th September 2026.pdf](https://drive.google.com/file/d/1mMscDMjL_NUP1w840EG4XoxLH8dpzZb4/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-09-09-class-notes-9th-september-2026]]: the discrete moments and variance that are extended here to integrals.
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: $E[g(X)]$ for discrete $X$, whose analogue is (1.3).
- [[08-Probability/PR05 Continuous Random Variables]]: their own chapter on continuous random variables.
- [[08-Probability/PR06 Moments Generating Functions and Limit Theorems]]: moments in their own notes.
