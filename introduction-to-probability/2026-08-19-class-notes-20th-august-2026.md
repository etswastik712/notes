---
id: introduction-to-probability/2026-08-19-class-notes-20th-august-2026
aliases: [Class notes 20 August 2026]
tags: [introduction-to-probability, lecture, random-variables, pmf, cdf, expectation]
trust_tier: agent_written
---

# Class notes 20 August 2026

## Covered
Posted 2026-08-19. The instructor said the next day would start with the example on independent events mentioned at the end of the 19 August class (recalling the definition of independence / mutual independence), and then cover as much of these notes as possible.

**Random variable.** A function of the outcome of a random experiment (e.g. the sum of $n$ dice rather than each die). In this course only real-valued (or at most $\mathbb R^n$-valued) random variables. A **discrete** random variable takes at most countably many values.

**pmf.** $p(x)=P[X=x]$ for all $x\in\mathbb R$. If $X$ takes values $x_1,x_2,\dots$ only, then $p(x_i)>0$, $p(x)=0$ elsewhere, and $\sum_ip(x_i)=1$. A frequency distribution is the empirical pmf.

**cdf.** $F(a)=P[X\le a]$, defined for any random variable; for discrete $X$, $F(a)=\sum_{x\le a}p(x)$, a step function. Properties:
1. Monotone increasing: $x_1\le x_2\Rightarrow F(x_1)\le F(x_2)$ (can be proved rigorously).
2. Right-continuous: $F(a)=\lim_{x\to a^+}F(x)$. Proof idea: for $x_n\downarrow a$, $A_n=\{X\le x_n\}$ is a decreasing sequence with $\bigcap A_n=\{X\le a\}$, so $F(x_n)\to F(a)$ by continuity of probability ([[introduction-to-probability/2026-08-11-class-notes-12th-august-2026]], further-reading section). This proof is not part of the formal course material.
3. $\lim_{x\to\infty}F(x)=1$, $\lim_{x\to-\infty}F(x)=0$ (similar argument).

**Expectation (discrete).** $E[X]=\sum_{x:p(x)>0}xp(x)=\sum_ix_ip(x_i)$: the probability-weighted average of the values (countably many terms).

**Examples.**
- $n$ independent tosses, each head with probability $p$, $X$ = number of heads: the **binomial** distribution; pmf and expectation found in class. $n=1$ gives the **Bernoulli** distribution.
- Fair die rolled twice, sum recorded: find pmf and expectation. With $X_1,X_2$ the two faces: they have the same distribution, but are they equal as random variables? (No: same distribution is not equality.)
- Binomial arises from sampling **with** replacement; the **hypergeometric** from sampling **without** replacement: urn with $w$ white and $b$ black, $n$ drawn without replacement, $X$ = number of white in the sample; pmf and expectation found in class.
- **Discrete uniform**: finite non-empty $\Omega$ with equally likely values, $P[X=x]=1/|\Omega|$; e.g. a slip drawn from a hat holding $1,\dots,n$: $P[X=i]=1/n$.

## From the post
Dear everyone, we shall begin with the example on independent events that I mentioned at the end of today's class, tomorrow (including recalling the definition of independence / mutual independence). We shall then cover as much as possible of the class notes attached here.

## Files
- [Class notes 20th August 2026.pdf](https://drive.google.com/file/d/1eVqOMfIRgPufoDNAOhYN_xE7mw49RaTG/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-08-11-class-notes-12th-august-2026]]: continuity of probability used for the cdf properties
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026]]: the sheet for this week
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: continues with binomial/Bernoulli as sums of indicators and Poisson
