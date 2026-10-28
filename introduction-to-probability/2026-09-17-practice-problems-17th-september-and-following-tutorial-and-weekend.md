---
id: introduction-to-probability/2026-09-17-practice-problems-17th-september-and-following-tutorial-and-weekend
aliases: [Practice problems 17 September 2026]
tags: [introduction-to-probability, practice-problems]
trust_tier: agent_written
---

# Practice problems for 17 September 2026 and the following tutorial and weekend

## Covered
An 11-problem sheet for the problem discussion session, covering the whole mid-semester syllabus: discrete distributions, pmfs from cdfs, Bayes, and a first continuous problem (Classroom: Practice problems 17th September and following tutorial and weekend.pdf).

Problems and what each practises:
1. A company has $m$ men and $n$ women. (a) $t$ employees are promoted uniformly at random: distribution of the number of women promoted (hypergeometric). (b) Each employee is promoted independently with probability $p$: distribution of the number of women promoted (binomial). Practises sampling without vs with replacement.
2. Two coins with head probabilities $p_1,p_2$; one is chosen at random (each equally likely) and flipped $n\ge2$ times; $X$ = number of heads. Find the pmf of $X$ (a mixture of two binomials by total probability) and the special case $p_1=p_2$.
3. Flight with 100 seats, 110 bookings, each passenger shows up with probability $0.9$ independently: probability that there are enough seats, left in sum form. Practises the binomial.
4. Two balls drawn without replacement from 8 white, 4 black, 2 orange; win \$2 per black, lose \$1 per white; pmf of the winnings $X$. Practises a function of a count.
5. Five men and five women ranked by exam score, all rankings equally likely; $X$ = best rank achieved by a woman; pmf of $X$.
6. $X=X_H-X_T$ for $n$ tosses of a coin: possible values; pmf for $n=3$. Practises a transformation of a binomial.
7. A salesman has two appointments with sale probabilities $0.3$ and $0.6$ (independent); any sale is equally likely a \$1000 or a \$500 model; pmf and $E[X]$ of the total value.
8. Five distinct numbers distributed to players 1 to 5; players 1 and 2 compare, the winner compares with player 3, and so on; $X$ = number of times player 1 wins; pmf of $X$.
9. A cdf with a continuous piece and jumps ($F(x)=x/4$ on $[0,1)$, $1/2+(x-1)/4$ on $[1,2)$, $11/12$ on $[2,3)$, $1$ for $x\ge3$): find $P[X=i]$ for $i\in\{1,2,3\}$. The sheet recalls that $\lim_{y\to x^-}F(y)=P[X<x]$ and $\lim_{y\to x^+}F(y)=F(x)=P[X\le x]$, so $P[X=x]=F(x)-F(x^-)$.
10. Voters: 46% Independents, 30% Liberals, 24% Conservatives; turnout 35%, 62%, 58% respectively. Given that a random voter voted, the probability they are a Liberal (Bayes' rule).
11. Continuous $X$ with pdf $c(1-x^2)$ on $(-1,1)$, $0$ otherwise: find $c$ and the cdf.

## From the post
Dear everyone, here are some problems we can discuss from, today (apart from whatever else you wish to ask me from the past lists of suggested problems, or from anywhere else).

## Files
- [Practice problems 17th September and following tutorial and weekend.pdf](https://drive.google.com/file/d/1gGJb7apjC5y5zVEa8CC5V9TvUgb1Gyhx/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend]]: earlier sheet on the same discrete-distribution patterns.
- [[introduction-to-probability/2026-09-10-practice-problems-weekend-of-12th-september-2026]]: previous sheet (variances, Poisson approximation).
- [[introduction-to-probability/2026-09-10-class-notes-10th-september-2026]]: pdf and cdf for problem 11.
- [[08-Probability/PR03 Discrete Random Variables and Distributions]]: their chapter on these distributions.

<!-- kurooto:material7e711675 -->
## Concepts in Practice problems 17th September and following tutorial and weekend
[[zettel/hypergeometric-promotion-model]], [[zettel/binomial-promotion-model]], [[zettel/binomial-overbooking-survival-sum]], [[zettel/order-statistic-of-first-rank-in-uniform-random-permutations]], [[zettel/difference-random-variable-of-symmetrical-binomial-counters]], [[zettel/consecutive-comparison-win-count-in-random-permutations]]
<!-- /kurooto:material7e711675 -->
