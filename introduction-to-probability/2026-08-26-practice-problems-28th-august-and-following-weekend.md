---
id: introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend
aliases: [Practice problems 28 Aug 2026]
tags: [probability, mt2113, problem-sheet]
trust_tier: agent_written
---

# Practice problems for 28 August 2026 and the following weekend

## Covered
Problem sheet for the (shortened, because of Quiz 2) tutorial of 28 August and the weekend after. Eight problems, all on discrete random variables (Classroom: Practice problems 28th August and following weekend.pdf).

| # | Problem | What it practises |
|---|---|---|
| 1 | 100 numbered slips, 5 drawn one at a time. With replacement: $X$ = number of slips with value $\ge 80$ (pmf of $X$), and $P[100 \text{ drawn at least once}]$. Without replacement (each ordered 5-tuple equally likely): the same two questions for $Y$ | binomial pmf (sampling with replacement) vs hypergeometric pmf (without replacement); complement event for "at least once" |
| 2 | 3 balls chosen from an urn with 3 white, 3 red, 5 black; win 1 rupee per white, lose 1 per red; pmf of total winnings $X$ | pmf of a function of counts; counting by cases |
| 3 | Coupon collector: $N$ types, $T$ = number of coupons collected until a full set. Values of $T$ and pmf of $T$ | tail probability $P[T>n]$ via the events $A_i$ ("no coupon of type $i$ in the first $n$ draws"), $\{T>n\}=\bigcup_i A_i$, inclusion–exclusion, then $P[T=n]=P[T>n-1]-P[T>n]$ |
| 4 | Hypergeometric: urn with $w$ white, $b$ black, $n$ drawn without replacement, $X$ = number of white. Find $E[X]$ | expectation of the hypergeometric |
| 5 | Quiz show: two questions, $V_i$ dollars for question $i$, may attempt $j$ only if $i$ is correct; $p_i$ = probability of knowing answer $i$, events $E_1,E_2$ independent. Which question first to maximise expected winnings? | expectation of a payoff, comparing two strategies |
| 6 | Two independent coins, heads probabilities $0.6$ and $0.7$; $X$ = total heads. Find $P[X=1]$ and $E[X]$ | pmf of a sum of independent Bernoulli variables |
| 7 | Given a step cdf with jumps at $0,1,2,3,3.5$ (values $1/2, 3/5, 4/5, 9/10, 1$), find the pmf and $E[X]$ | pmf from cdf (jump sizes); expectation |
| 8 | $X\sim\text{Poisson}(\lambda)$, $P[X=n]=e^{-\lambda}\lambda^n/n!$ for $n\in\mathbb N_0$. Find $E[X]$ | expectation of the Poisson |

## From the post
Dear everyone, here are some practice problems for the upcoming tutorial (which will be shorter in duration because of Quiz 2) and for the weekend that follows.

## Files
- [Practice problems 28th August and following weekend.pdf](https://drive.google.com/file/d/1A8JdRD24jZhzNgo_xtSx9Vzg9Uep52dZ/view?usp=drive_web)

## Related
- [[08-Probability/PR03 Discrete Random Variables and Distributions]]: the chapter built from the class notes and this sheet (binomial, hypergeometric, Poisson, expectation).
- [[08-Probability/PR04 Joint Distributions Expectation and Variance]]: linearity of expectation gives a shorter route to problems 4 and 8.
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: the class notes this sheet follows.
