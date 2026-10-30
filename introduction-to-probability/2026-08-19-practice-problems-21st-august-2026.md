---
id: introduction-to-probability/2026-08-19-practice-problems-21st-august-2026
aliases: [Practice problems 21 August 2026]
tags: [introduction-to-probability, problem-sheet, bayes, independence, gamblers-ruin]
trust_tier: agent_written
---

# Practice problems 21 August 2026

## Covered
The updated list of suggested problems for 21 August and the following weekend (10 problems; the file was read in full).

| # | Problem | What it practises |
|---|---------|-------------------|
| 1 | Urn with $b$ black and $w$ white, $n$ drawn without replacement. $B$ = first ball black, $B_k$ = exactly $k$ black drawn. $P[B]=\frac b{b+w}$, $P[B_k]=\binom bk\binom w{n-k}/\binom{b+w}n$. Find $P[B_k\mid B]$, then $P[B\mid B_k]$ from the definition | conditional probability, hypergeometric, alternative to the exchangeability argument |
| 2 | Student knows the answer with probability $p$, otherwise guesses, correct with probability $1/m$ ($m$ alternatives). $P[\text{knew}\mid\text{correct}]$ | Bayes' theorem |
| 3 | Accident-prone people have accident probability 0.4 per year, others 0.2; 30% are accident-prone. $P[\text{accident-prone}\mid\text{accident in a year}]$ | Bayes' theorem |
| 4 | Inspector 60% convinced of the suspect's guilt; the criminal has a characteristic shared by 20% of the population; the suspect has it. Updated certainty. Hint: $A$ = suspect is the perpetrator, $B$ = suspect has the characteristic; decide $P[B\mid A]$ and $P[B\mid A^c]$, then Bayes | Bayes with degree-of-belief probabilities |
| 5 | Urn with 8 red and 4 white, 2 drawn without replacement. (a) both red when each ball is equally likely; (b) both red when a ball is chosen with probability weight/(sum of weights of balls currently in the urn), red weight $r$, white weight $w$ | multiplication rule, weighted draws |
| 6 | For independent $E_1,\dots,E_n$, show $P[\bigcap E_i]=\prod P[E_i]$ using the chain rule of conditional probabilities (as in class) | multiplication rule, independence |
| 7 | Can an event be independent of itself? Necessary condition? (Trivia: key to Kolmogorov's zero-one law) | definition of independence |
| 8 | $E,F$ independent: what about (a) $E^c,F$ (b) $E,F^c$ (c) $E^c,F^c$? | independence and complements |
| 9 | Gambler's ruin: gambler with $i$ units, casino with $n-i$; each round the gambler wins 1 with probability $p$, loses 1 otherwise, rounds independent; bankrupt if the fortune reaches 0 before $n$. Let $p_i$ = probability of bankruptcy from $i$; $p_0=1$, $p_n=0$. Condition on the first round: $p_i=p\,p_{i+1}+(1-p)p_{i-1}$, equivalently $p_{i+1}-p_i=\frac{1-p}{p}(p_i-p_{i-1})$. Solving explicitly is left for the tutorial | recurrence from conditioning on the first step, boundary conditions |
| 10 | A bag holds one marble, blue or green with equal probability; a green marble is added; a marble drawn at random is green. Probability the marble remaining is green | Bayes, conditioning on the content of the bag |
**Update (post of 2026-08-20, file Practice problems 21st August 2026.pdf, 11 problems).** The instructor added one more problem because there were few examples on independence:

| # | Problem | What it practises |
|---|---------|-------------------|
| 11 | Independent trials, each a roll of a pair of fair dice, outcome = sum. Probability that a sum of 5 appears before a sum of 7. Hint: $A$ = trial gives 5, $B$ = trial gives 7; $E_n$ = neither 5 nor 7 in the first $n-1$ trials and 5 at trial $n$, so $P[E_n]=(1-P[A]-P[B])^{n-1}P[A]$ (justify independence and mutual exclusivity); the $E_n$ are disjoint, and "5 before 7" is their union, so sum with the third axiom | independence across trials, countable additivity, geometric series |

The same post says the syllabus for Quiz 2 is conditional probability and independence: everything covered since the last quiz, up to everything covered in the 21 August tutorial.

## From the post
Dear everyone, here is the updated list of suggested problems for this week.

## Files
- [Practice problems 21st August 2026.pdf](https://drive.google.com/file/d/1cxzqkreK24W9p3FCkvVDD8RrBttuO6-9/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-08-11-class-notes-13th-august-2026]]: urn model, exchangeability, Bayes formula for problems 1-5
- [[introduction-to-probability/2026-08-13-practice-problems-14th-august-2026]]: previous sheet of Bayes problems
- [[introduction-to-probability/2026-08-19-class-notes-20th-august-2026]]: that week's lecture on random variables

<!-- kurooto:materiald58afbd3 -->
## Concepts in Practice problems 21st August 2026
[[zettel/bayes-rule-for-multiple-choice-guessing]], [[zettel/self-independent-event]], [[zettel/independence-of-complements]], [[zettel/chain-rule-for-finite-intersection-probabilities]], [[zettel/gambler-s-ruin-difference-recurrence]], [[zettel/first-colour-arrival-probability-under-sampling-with-replacement]], [[zettel/weighted-urn-sampling-without-replacement]], [[zettel/hypergeometric-first-draw-posterior-probability]]
<!-- /kurooto:materiald58afbd3 -->

<!-- kurooto:materialf7d6bebe -->
## Concepts in Practice problems 21st August 2026
[[zettel/hypergeometric-first-draw-posterior-probability]], [[zettel/bayes-rule-for-multiple-choice-guessing]], [[zettel/accident-proneness-posterior-inference]], [[zettel/subjective-bayesian-criminal-investigation-updating]], [[zettel/weighted-urn-sampling-without-replacement]]
<!-- /kurooto:materialf7d6bebe -->

<!-- kurooto:material8eec3958 -->
## Concepts in Class notes 20th August 2026
[[zettel/random-variable]], [[zettel/discrete-random-variable]], [[zettel/joint-probability-mass-function]], [[zettel/binomial-distribution]], [[zettel/discrete-uniform-distribution]]
<!-- /kurooto:material8eec3958 -->
