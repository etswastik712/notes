---
id: introduction-to-probability/2026-10-15-hw-2-problems
aliases: [HW 2 problems, Week 2 homework]
tags: [introduction-to-probability, continuous-random-variables, homework]
trust_tier: agent_written
---

# HW 2 problems

## Covered
A problem sheet only: the file Week2_notes.pdf holds the same three problems as the post and no lecture text (the announcement of 2026-10-24 says the lecture notes for Weeks 2 and 3 were posted, but they are not in this file). The due date is not stated.

1. Repair time (in hours) is exponentially distributed with parameter $\lambda=1/2$. (a) Find $P(\text{repair time}>2)$. (b) Find the conditional probability that a repair takes at least 10 hours given that it exceeds 9 hours. Practises: the exponential tail $P(X>x)$ and its memorylessness (compare the geometric case in [[introduction-to-probability/2026-09-18-quiz-3-solutions]]).
2. The Gumbel distribution is the distribution of $-\log X$ with $X\sim\text{Expo}(1)$. (a) Find the CDF of the Gumbel distribution. (b) Let $X_1,\dots,X_n$ be i.i.d. $\text{Expo}(1)$ and $M_n=\max(X_1,\dots,X_n)$. Show that $M_n-\log n$ converges in distribution to the Gumbel distribution, i.e. as $n\to\infty$ the CDF of $M_n-\log n$ converges to the Gumbel CDF. Practises: the cdf method for a transformed variable, the cdf of a maximum of independent variables, and a limit of cdfs.
3. For a continuous random variable $X$ with CDF $F(x)$, find $E[F(X)]$ (a) without LOTUS and (b) again with LOTUS. Practises: LOTUS $E[g(X)]=\int g(x)f(x)\,dx$ against a direct computation of the distribution of $F(X)$ ([[introduction-to-probability/2026-10-08-week-1-post-mid-term-hw-and-lecture-notes]]).

## From the post
HW 2 problems

1) The time (in hours) required to repair a machine is an exponentially distributed random variable with parameter lambda=1/2. a. What is the probability that a repair time exceeds 2 hours? b. the conditional probability that a repair takes at least 10 hours, given that its duration exceeds 9 hours?

2) The Gumbel distribution is the distribution of -logX with X ~ Expo(1). (a) Find the CDF of the Gumbel distribution. (b) Let X_1,X_2,..., X_n be i.i.d. Expo(1) and let M_n = max(X_1,..,X_n). Show that (M_n - log n) converges in distribution to the Gumbel distribution, i.e., as n --> infinity, the CDF of (M_n - log n) converges to the Gumbel CDF.

3) For a continuous random variable X, with CDF F(x), find the expectation of the the random variable F(X), without using L.O.T.U.S and also again by using L.O.T.U.S .

## Files
- [Week2_notes.pdf](https://drive.google.com/file/d/1hw5LGeID4qPvQ-wpmeFdk6z7-PHR2WqI/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-10-08-week-1-post-mid-term-hw-and-lecture-notes]]: LOTUS and cdf/pdf background for problems 2 and 3.
- [[introduction-to-probability/2026-09-18-quiz-3-solutions]]: memorylessness of the geometric, the discrete counterpart of problem 1(b).
- [[08-Probability/PR05 Continuous Random Variables]]: their chapter on continuous densities, including the exponential.

<!-- kurooto:materialebf94e67 -->
## Concepts in announcement
(none new)
<!-- /kurooto:materialebf94e67 -->
