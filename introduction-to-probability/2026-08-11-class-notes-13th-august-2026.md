---
id: introduction-to-probability/2026-08-11-class-notes-13th-august-2026
aliases: [Class notes 13 August 2026]
tags: [introduction-to-probability, lecture, conditional-probability, bayes, urn-model]
trust_tier: agent_written
---

# Class notes 13 August 2026

## Covered
Posted 2026-08-11 for the class of 13 August. The instructor said he might update the notes before class and would notify students if so. This note holds the version posted on 2026-08-11.

**Conditional probability.** Partial information (earlier experiments, collected data) should enter the computation of probabilities. For events $E,F$ with $P[F]>0$:
$$P[E\mid F]=\frac{P[E\cap F]}{P[F]}.$$
Meaning: given that $F$ has occurred, how does that change our belief that $E$ has occurred.

**Reduced sample space.** When all outcomes are equally likely, it is often easier to work in the sample space obtained by assuming the conditioning event, then count in it. Example in class: the 52 cards are dealt equally to North, South, East, West; if North and South have 8 spades between them, what is the probability that East has 3 spades?

**Urn models (sampling without replacement).** Urn with $b$ black and $w$ white balls, draw one at random and do not replace, then draw another.
- Compute $P[\text{1st black, 2nd white}]$ and $P[\text{1st white, 2nd black}]$ and compare (the observation to make is that they are equal).
- Question for the student: does this persist for more draws without replacement? A formal proof is suggested for self-convincing, not for examinations.
- Question: $n$ balls drawn sequentially without replacement from $w$ white and $b$ black ($n\le w+b$); given that $k$ of the $n$ are black, what is the probability that the first ball is black? Use the previous observation.

**Multiplication rule.**
$$P\Big[\bigcap_{i=1}^nE_i\Big]=P[E_1]\,P[E_2\mid E_1]\,P[E_3\mid E_1\cap E_2]\cdots P\Big[E_n\,\Big|\,\bigcap_{i=1}^{n-1}E_i\Big].$$

**Total probability / Bayes formula (first form).**
$$E=(E\cap F)\cup(E\cap F^c)\ \Rightarrow\ P[E]=P[E\mid F]P[F]+P[E\mid F^c](1-P[F]).$$
Several applications to come in the tutorial sessions.

**Exchangeability in the urn model (section 2 of the notes).** At each draw, $P[\text{black}]=\dfrac{\text{black balls left}}{\text{balls left}}$ and the denominator is $b+w$, $b+w-1$, $b+w-2,\dots$ whatever the earlier colours were. So for the event $\{$1st ball has colour $C_1$, …, $k$-th has colour $C_k\}$, each $C_i$ black or white, the denominator is
$$(b+w)(b+w-1)\cdots(b+w-k+1).$$
In the numerator, black balls contribute $b(b-1)\cdots(b-\ell+1)$ if $\ell$ of the $k$ are black, and white balls contribute $w(w-1)\cdots(w-k+\ell+1)$. Hence, whenever exactly $\ell$ of $C_1,\dots,C_k$ are black,
$$P=\frac{b(b-1)\cdots(b-\ell+1)\;w(w-1)\cdots(w-k+\ell+1)}{(b+w)(b+w-1)\cdots(b+w-k+1)},$$
independent of the order in which blacks and whites appear. This property is called **exchangeability**.

## From the post
Dear everyone, here are the class notes I am planning to refer to for the class day after tomorrow. You need not read them ahead of time. I may update them tomorrow or before class on Thursday (if so, I shall notify you all).

## Files
- [Class notes 13th August 2026.pdf](https://drive.google.com/file/d/1LYu3VH41-9fQZzK9vt-dDlNhJYcRDTfP/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-08-11-class-notes-12th-august-2026]]: axioms, inclusion-exclusion, previous class
- [[introduction-to-probability/2026-08-13-practice-problems-14th-august-2026]]: Bayes problems following this class
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026]]: problem 1 reworks the urn question via $P[B\mid B_k]$
