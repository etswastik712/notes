---
id: introduction-to-probability/2026-10-22-hw3-problems-and-median-clarification
aliases: [HW3 problems, Median clarification]
tags: [introduction-to-probability, median, mode, skewness, mgf, homework]
trust_tier: agent_written
---

# HW3 problems and the median clarification

## Covered
**Median of a discrete random variable (correction by the instructor).** $c$ is a median of $X$ if $P(X\le c)\ge\tfrac12$ and $P(X\ge c)\ge\tfrac12$. (The board had $P(X\ge c)\le\tfrac12$ by mistake.) Let $x_1<x_2<\dots<x_n$ be the values of $X$ and $p_i=P(X=x_i)$. Take $i$ with $p_1+\dots+p_{i-1}<\tfrac12$ and $p_1+\dots+p_i\ge\tfrac12$. Then $p_i+\dots+p_n=1-(p_1+\dots+p_{i-1})\ge\tfrac12$, so $x_i$ is a median (it is the smallest $c$ that works).

**Homework 3** (Week3_notes.pdf; due date not stated). Problem 4 is marked "postponed to next hw" in the file, but the post lists it without that remark.
1. $U\sim\text{Unif}(a,b)$: median and mode. $X\sim\text{Expo}(\lambda)$: median and mode. Practises: median via $F(c)=\tfrac12$, mode as the maximiser of the pdf (modes of discrete laws: 12 September sheet, problems 7-8).
2. Pareto with parameter $a>0$, pdf $f(x)=a/x^{a+1}$ for $x\ge1$ and $0$ otherwise: median and mode. Practises: the same, for a pdf with a boundary maximum.
3. $X\sim\text{Expo}(\lambda)$: the skewness, with an explanation of why it is positive and why it does not depend on $\lambda$. Practises: third central moment (standardised), and scaling (see the instructor's note on skewness in [[maps/courses/introduction-to-probability]], 2026-09-15).
4. (postponed to next hw, per the file) A fair die is rolled twice, outcomes $X$ and $Y$. Find the mgf $M_{X+Y}(t)$; the answer may contain unsimplified finite sums. Practises: mgf of a sum of independent variables.
5. Use the mgf of $\text{Geom}(p)$ to prove again that the mean is $q/p$ and the variance is $q/p^2$, $q=1-p$. Practises: moments from derivatives of the mgf. Per the rule of 2026-09-17, derive the mgf before using it.
6. $Z\sim N(0,1)$, $Y=|Z|$ (the folded normal, discussed in class): two expressions for the mgf of $Y$ as unsimplified integrals, one from the pdf of $Y$ and one from the pdf of $Z$. Practises: the mgf by the pdf of $Y$ against by LOTUS.

## From the post
Clarification about Median for discrete RV. We say that c is a median of a random variable X if P(X <= c) >= 1/2 and P(X >=c) >= 1/2. (By mistake I had written P(X >=c) <= 1/2 on the board). If x_1<x_2<....<x_n are the values taken by the RV X, and p_i=P(X=x_i) Let i be such that p_1+...+p_{i-1}<1/2 and p_1+...+p_i >=1/2. Then , we note that p_i+...+p_n=1-(p_1+...+p_{i-1})>=1/2 Therefore, x_i is a median (taking smallest c which works)

HW3 Problems

1) Let U ~ Unif(a; b). Find the median and mode of U. Let X ~ Expo(lambda). Find the median and mode of X.

2) Let X have the Pareto distribution with parameter a > 0; this means that X has PDF f(x) = a/x^{a+1} for x >= 1 (and 0 otherwise). Find the median and mode of X.

3) Let X ~ Expo(lambda). Find the skewness of X, and explain why it is positive and why it does not depend on lambda

4) A fair die is rolled twice, with outcomes X for the first roll and Y for the second roll. Find the moment generating function M_{X+Y} (t) of X + Y (your answer should be a function of t and can contain unsimplified finite sums).

5) Use the MGF of the Geom(p) distribution to give another proof that the mean of this distribution is q/p and the variance is q/p^2, with q = 1 - p

6) Let Z ~ N(0; 1), and Y = |Z|. So Y has the Folded Normal distribution, discussed in class. Find two expressions for the MGF of Y as unsimplified integrals: one integral based on the PDF of Y , and one based on the PDF of Z.

## Files
- [Week3_notes.pdf](https://drive.google.com/file/d/1EuadKCwJCer-Ap1PMINmw3etNLk12gZs/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-10-15-hw-2-problems]]: previous homework, exponential distribution.
- [[introduction-to-probability/2026-09-09-class-notes-9th-september-2026]]: moments and variance, which skewness and mgfs build on.
- [[introduction-to-probability/2026-09-10-practice-problems-weekend-of-12th-september-2026]]: modes of discrete distributions.
- [[08-Probability/PR06 Moments Generating Functions and Limit Theorems]]: their chapter on mgfs and moments.
