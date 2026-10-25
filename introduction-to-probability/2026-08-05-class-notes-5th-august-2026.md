---
id: introduction-to-probability/2026-08-05-class-notes-5th-august-2026
aliases: [Class notes 5 August 2026]
tags: [introduction-to-probability, lecture, counting]
trust_tier: agent_written
---

# Class notes 5 August 2026

## Covered
Recap of counting, the first "technical" notes of the course (Classroom: Class notes 5th August 2026).

- **Basic principle of counting.** Experiment 1 has $m$ outcomes and experiment 2 has $n$ outcomes, so there are $mn$ outcome pairs. For $r$ experiments, with the $i$-th having $m_i$ outcomes, the number of $r$-tuples is $m_1m_2\cdots m_r$.
- **Permutations.** $n$ distinguishable objects can be arranged in $n!$ ways. If $k_1$ are of one kind, $k_2$ of a second, ..., $k_r$ of an $r$-th kind, with $k_1+\dots+k_r=n$ and objects of the same kind indistinguishable, the number of arrangements is $\dfrac{n!}{k_1!k_2!\cdots k_r!}$.
- **Combinations.** The number of ways to choose $r$ of $n$ distinguishable objects ($r\le n$) is $\binom nr=\dfrac{n!}{(n-r)!\,r!}=\dfrac{n(n-1)\cdots(n-r+1)}{r!}$. The proof uses equivalence classes that partition a suitable set of permutations (done in class, not written in the notes).
- **Antenna problem (posed).** $n$ antennas, $m$ defective (defective ones indistinguishable from each other, working ones likewise). How many arrangements have no two defective antennas consecutive?
- **Pascal's identity.** $\binom nr=\binom{n-1}r+\binom{n-1}{r-1}$.
- **Binomial theorem.** $(x+y)^n=\sum_{k=0}^n\binom nk x^ky^{n-k}$, provable by induction on $n$ or by a combinatorial argument.
- **Multinomial coefficients.** Dividing $n$ distinct items into $r$ distinct groups of sizes $m_1,\dots,m_r$ ($m_1+\dots+m_r=n$) can be done in $\dbinom{n}{m_1,\dots,m_r}=\dfrac{n!}{m_1!m_2!\cdots m_r!}$ ways. The notes ask to compare this with the count of permutations with repetitions above.
- **Multinomial theorem.** $(x_1+\dots+x_r)^n=\displaystyle\sum_{\substack{m_1,\dots,m_r\in\mathbb N_0\\ m_1+\dots+m_r=n}}\binom{n}{m_1,\dots,m_r}x_1^{m_1}\cdots x_r^{m_r}$.

## From the post
Dear everyone, this is the first set of 'technical' notes. However, today, I am thinking of starting with some motivations for studying this subject, following which we shall cover as much of the contents of these notes as possible, and then proceed with the rest tomorrow.

## Files
- [Class notes 5th August 2026.pdf](https://drive.google.com/file/d/1t9tHB2nEgBKMiEeJj_TQ4_fGAkzhRXoi/view?usp=drive_web)

## Related
- [[08-Probability/PR01 Counting and the Axioms of Probability]]: the vault chapter on counting and the axioms
- [[08-Probability/Concepts/Counting Principles]]: your concept note on the basic counting rules
- [[08-Probability/Concepts/Multinomial Coefficient]]: your concept note on multinomial coefficients
- [[introduction-to-probability/2026-08-05-class-notes-6th-august-2026]]: the next class, sample spaces and the axioms
- [[introduction-to-probability/2026-08-06-practice-problems-7th-august-2026]]: problems that use these counting rules
