---
id: introduction-to-probability/2026-09-10-practice-problems-weekend-of-12th-september-2026
aliases: [Practice problems 12 Sep 2026]
tags: [probability, mt2113, problem-set, variance, poisson, binomial]
trust_tier: agent_written
---

# Practice problems for 11 September 2026 and the following weekend

## Covered
An 11-problem sheet on discrete distributions and variance. No problems on continuous random variables; those come in the following week's list (Classroom: Practice problems weekend of 12th September 2026.pdf).

Problems and what each practises:
1. Number of $\alpha$ particles in 1 s from 1 g of material, mean 3.2: approximate $P[X\le2]$. Model as $\text{Binomial}(N,3.2/N)$ with $N$ huge, then use the Poisson limit. Practises the Poisson approximation to the binomial; any result used must be one fully proved in class and stated with complete clarity.
2. $\operatorname{Var}[X]$ for $X\sim\text{Binomial}(n,p)$.
3. $\operatorname{Var}[X]$ for $X\sim\text{Poisson}(\lambda)$.
4. $\operatorname{Var}[X]$ for $X\sim\text{Geometric}(p)$.
5. $\operatorname{Var}[X]$ for $X\sim\text{Negative Binomial}(r,p)$. Remark: for independent $X_i$, $\operatorname{Var}\big[\sum X_i\big]=\sum\operatorname{Var}[X_i]$ (1.1), which would give the answer from $r$ independent Geometric($p$) variables, but (1.1) is not proved in this course, so it cannot be used.
6. Show $E[X^n]=\lambda E[(X+1)^{n-1}]$ for $X\sim\text{Poisson}(\lambda)$, then compute $E[X^3]$ (using $E[X]$ and the variance from problem 3). Practises moment recursions.
7. Mode(s) of $\text{Binomial}(n,p)$: the $k$ maximising $P[X=k]$.
8. Mode of $\text{Poisson}(\lambda)$.
9. $X$ with mean $\mu$ and variance $\sigma^2$; $Y=(X-\mu)/\sigma$: find $E[Y]$ and $\operatorname{Var}[Y]$; for discrete $X$ give the pmf and cdf of $Y$. Practises standardisation and $E[aX+b]$, $\operatorname{Var}[aX+b]$.
10. For $X\sim\text{Binomial}(n,p)$: $E\!\left[\frac1{X+1}\right]=\frac{1-(1-p)^{n+1}}{(n+1)p}$.
11. For non-negative integer-valued $N$: $\sum_{i=1}^\infty i\,P[N>i]=\tfrac12\big(E[N^2]-E[N]\big)$. Hint: use the idea from class proving $E[N]=\sum_{i\ge1}P[N\ge i]$.

## From the post
Dear everyone, here are some suggested problems. I have not included problems about continuous random variables, since we have just begun discussing them. There will be some suggested problems on continuous random variables next week.

## Files
- [Practice problems weekend of 12th September 2026.pdf](https://drive.google.com/file/d/1XlSENBPp24lqIJXWC6Tvur9HguLrWPrd/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-09-09-class-notes-9th-september-2026]]: moments and variance used throughout.
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: Poisson as a binomial limit (problem 1).
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: negative binomial and linearity of expectation (problems 5, 10).
- [[08-Probability/PR03 Discrete Random Variables and Distributions]]: their chapter on these distributions.
