---
title: Bayes' Theorem
aliases: [Bayes rule, Bayesian inference, posterior probability]
subject: probability
type: concept
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes, pigliucci]
status: draft
tags: [subject/probability, subject/eco-evo, type/concept, taught, extra/book, extra/beyond, src/lecture-notes, src/paper, src/own-notes, status/draft]
---
# Bayes' Theorem

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (MT2113):** the formula, the disease-test, plane-search, multiple-choice, insurance and Monty Hall examples ([[ilovepdf_merged-1.pdf#page=15|class notes 19 Aug]], [[Practice problems 14th August 2026.pdf|sheet 14 Aug]], [[Practice problems 21st August 2026.pdf|sheet 21 Aug]]; chapter [[PR02 Conditional Probability Bayes Rule and Independence]]) · 🟡 **extra · book:** Pigliucci's use of Bayes' rule as a philosophy of science ([[Pigliucci_Philosophy of Ecology.pdf#page=9|PDF p.9–10]]) · 🔵 **extra · beyond:** the derivation and the numerical example below.

> [!intuition] Updating a bet
> You begin with a belief (the *prior*), see evidence, and shift your belief by how much better each rival explains that evidence than the others. Belief never reaches 0 or 1; it moves.

> [!key] Statement
> For mutually exclusive, exhaustive hypotheses $H_1,\dots,H_n$ and data $D$:
> $$P(H_i\mid D)=\frac{P(D\mid H_i)\,P(H_i)}{\sum_{j=1}^{n}P(D\mid H_j)\,P(H_j)}\tag{posterior = likelihood × prior / evidence}$$

> [!derivation]- From the definition of conditional probability
> $P(H_i\cap D)=P(D\mid H_i)P(H_i)=P(H_i\mid D)P(D)$. Divide by $P(D)$, and expand $P(D)=\sum_jP(D\mid H_j)P(H_j)$ (law of total probability).

- **Pitfall:** $P(D\mid H)\neq P(H\mid D)$. A significance test gives the first ("how surprising are these data if the null is true?"); we usually want the second.
- Pigliucci's points: the denominator forces a *fair competition* among stated hypotheses (no privileged null); priors make previous knowledge explicit; the probability is a degree of belief. Cost: choosing priors (objective vs subjective) is contested.

> [!example] Worked example (illustrative numbers, not Holdo's)
> Why do wildebeest enter the plains at the start of the rains? Four rival hypotheses, a prior, and the likelihood of the observation *D = "models using intake plus protein fit best, biomass-only models worst"*:
>
> | hypothesis | prior | $P(D\mid H)$ | prior × like | posterior |
> |---|---|---|---|---|
> | forage biomass | 0.35 | 0.05 | 0.0175 | **0.080** |
> | intake + protein | 0.25 | 0.60 | 0.1500 | **0.690** |
> | surface water | 0.20 | 0.10 | 0.0200 | 0.092 |
> | predator escape | 0.20 | 0.15 | 0.0300 | 0.138 |
>
> $P(D)=0.2175$. Belief in "intake + protein" rises from 0.25 to 0.69, in "biomass" falls from 0.35 to 0.08; no hypothesis is eliminated. (`scripts/ee01_numbers.py`, §7.)

## In the probability course (MT2113)
With a **partition** $E_1,\dots,E_n$ of $\Omega$: $P[E_i\mid F]=\dfrac{P[F\mid E_i]P[E_i]}{\sum_jP[F\mid E_j]P[E_j]}$. Odds form: posterior odds = likelihood ratio × prior odds.

> [!example] The class disease test
> Sensitivity $0.95$, false positives $0.01$, prevalence $0.5\%$: $P[D\mid+]=\frac{0.95\times0.005}{0.95\times0.005+0.01\times0.995}=0.323$ (Figure PR2.1). With a $95\%/95\%$ test at $1\%$ prevalence the posterior is only $0.161$. Plane search: after a failed search of region 1, $P[R_1]=\frac{\beta_1}{\beta_1+2}$ and $P[R_2]=P[R_3]=\frac1{\beta_1+2}$. Monty Hall: switching wins with probability $\tfrac23$ ([[Monty Hall Problem]]).

Used in: [[PR02 Conditional Probability Bayes Rule and Independence]] · [[EE01 Introduction to Biology and Ecological Thinking]] · [[Strong Inference]] · [[Akaike Information Criterion]].
Connections: [[Probability - Course Map]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
