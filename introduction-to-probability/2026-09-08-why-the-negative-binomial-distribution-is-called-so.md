---
id: introduction-to-probability/2026-09-08-why-the-negative-binomial-distribution-is-called-so
aliases: [Negative binomial: reason for the name]
tags: [probability, mt2113, negative-binomial]
trust_tier: agent_written
---

# Why the Negative Binomial Distribution Is Called So

## Covered
**Setup.** Let $X$ be the number of trials needed to achieve the $m$-th success; each trial succeeds with probability $p$, fails with $q=1-p$ (Classroom: negative_binomial_distribution.pdf).

**pmf.** $X=n$ means $m-1$ successes in the first $n-1$ trials, then a success on trial $n$:
$$P(X=n)=\binom{n-1}{m-1}p^{m-1}(1-p)^{n-m}\cdot p=\binom{n-1}{m-1}p^m(1-p)^{n-m}.$$

**Counting failures.** Let $f=n-m$ be the number of failures before the $m$-th success. Substituting $n=f+m$:
$$P(X=n)=\binom{m+f-1}{f}\,p^m\,q^f\quad(\text{using }\tbinom{f+m-1}{m-1}=\tbinom{m+f-1}{f}).$$

**Why "negative binomial".** By the generalized binomial theorem, $\binom{m+f-1}{f}$ is the coefficient of $q^f$ in
$$(1-q)^{-m}=1+mq+\binom{m+1}{2}q^2+\binom{m+2}{3}q^3+\cdots+\binom{m+f-1}{f}q^f+\cdots,$$
a binomial expansion with a negative exponent $-m$. Hence the name.

Consistency check (follows from the expansion): $\sum_f\binom{m+f-1}{f}q^f=(1-q)^{-m}=p^{-m}$, so the pmf sums to $1$.

## From the post
Why the Negative Binomial Distribution Is Called So

## Files
- [negative_binomial_distribution.pdf](https://drive.google.com/file/d/1tQRe0LFyFt6tG8MVWJgUcI-UPYbT2eRO/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: negative binomial defined as a sum of $k$ geometric variables.
- [[08-Probability/PR03 Discrete Random Variables and Distributions]]: geometric and negative binomial background.
