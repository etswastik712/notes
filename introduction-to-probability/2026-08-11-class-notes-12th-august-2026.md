---
id: introduction-to-probability/2026-08-11-class-notes-12th-august-2026
aliases: [Class notes 12 August 2026]
tags: [introduction-to-probability, lecture, inclusion-exclusion, continuity-of-probability]
trust_tier: agent_written
---

# Class notes 12 August 2026

## Covered
Posted 2026-08-11 for the class of 12 August; re-uploaded 2026-08-13 with a worked solution of the coats problem added (both versions otherwise identical).

**Recap.** Naive definition (finite $S=\{1,\dots,N\}$ with equally likely points): $P(E)=\dfrac{|E|}{|S|}$, since each $P(\{i\})=1/N$ by the axioms. Axiomatic definition: a function from the power set $2^\Omega$ to $[0,1]$.

**Consequences of the axioms.**
1. $P(E^c)=1-P(E)$, because $E\cup E^c=S$ is a disjoint union: $1=P(S)=P(E)+P(E^c)$.
2. If $E\subset F$ then $P(E)\le P(F)$: $F=E\cup(F\setminus E)$ is disjoint, so $P(F)=P(E)+P(F\setminus E)$ and $P(F\setminus E)\ge0$.

**Examples (worked in class).**
- A college with 10 time slots assigns 3 statistics courses to random slots; probability that 2 or more share a slot. Pattern: compute $P(A^c)$ (all different) instead of $P(A)$.
- Gimli, Legolas and ten others on one side of a long table, all arrangements equally likely: probability Gimli and Legolas sit next to each other (counting made easier by a smart choice of what to count).
- Left to the student: the same with 12 people around a circular table, chairs unlabelled but left/right neighbours distinguished; be careful which permutations are identical.

**Union of two events.** $P(E\cup F)=P(E)+P(F)-P(E\cap F)$. Hint for the proof: split into $E\setminus F$, $F\setminus E$, $E\cap F$.

**Inclusion-exclusion.** For three events:
$$P(E\cup F\cup G)=P(E)+P(F)+P(G)-P(E\cap F)-P(E\cap G)-P(F\cap G)+P(E\cap F\cap G).$$
For $E_1,\dots,E_n$ on the same sample space:
$$P\Big(\bigcup_{i=1}^nE_i\Big)=\sum_iP(E_i)-\sum_{i<j}P(E_i\cap E_j)+\sum_{i<j<k}P(E_i\cap E_j\cap E_k)-\cdots+(-1)^{n-1}P\Big(\bigcap_{i=1}^nE_i\Big).\tag{1.1}$$
Two proofs: induction, or a counting argument: a sample point lying in exactly $i$ of the events is counted exactly once in total on the right side.

**Matching problem.** $n$ cards numbered $1,\dots,n$ face down in unknown order, touched one by one, you guess each; you win if at least one guess is right. Equivalently (as set in class): $n$ party guests get coats back at random; probability that nobody gets their own coat. The notes point to "derangement" (studied in Discrete Structures).

Solution added on 2026-08-13: let $A_i$ = the $i$-th person gets their own coat (nothing said about the others). "No one gets their own coat" is $\bigcap A_i^c=(\bigcup A_i)^c$, so $P=1-P(\bigcup A_i)$ and inclusion-exclusion (1.2) applies. For distinct $i_1,\dots,i_k$:
$$P[A_{i_1}\cap\cdots\cap A_{i_k}]=\frac{(n-k)!}{n!}$$
(those $k$ people have their coats, the remaining $n-k$ coats are distributed randomly). The number of $k$-fold intersections is $\binom nk$, so
$$P\Big[\bigcap A_i^c\Big]=\sum_{i=0}^n(-1)^i\binom ni\frac{(n-i)!}{n!}.$$
(The notes mention that a second solution via recurrence relations is possible.)

**Further reading, not required for the course (not covered formally in class): probability as a continuous set function.**
- $\{E_n\}$ is increasing if $E_1\subset E_2\subset\cdots$, decreasing if $E_1\supset E_2\supset\cdots$. Limits: $\lim E_n=\bigcup_nE_n$ (increasing), $\lim E_n=\bigcap_nE_n$ (decreasing).
- Result: for an increasing or decreasing sequence, $P(\lim E_n)=\lim P(E_n)$.
- Proof for increasing: disjointification $F_1=E_1$, $F_n=E_n\setminus\bigcup_{i<n}E_i$; the $F_n$ are pairwise disjoint, $E_n=\bigcup_{i\le n}F_i$ and $\bigcup E_n=\bigcup F_n$. By the third axiom $P(E_n)=\sum_{i\le n}P(F_i)$ and $P(\bigcup E_n)=\sum_{n=1}^\infty P(F_n)=\lim_n\sum_{i\le n}P(F_i)=\lim P(E_n)$.
- Decreasing: $E_n^c$ is increasing; apply the above and De Morgan: $\lim[1-P(E_n)]=1-P(\bigcap E_n)$.
- This is used later for right-continuity of the cdf (see [[introduction-to-probability/2026-08-19-class-notes-20th-august-2026]]).

## From the post
Dear everyone, here are the class notes to be referred to for tomorrow's class.

(2026-08-13 update:) Dear everyone, since at least one of you asked, I have now included a detailed solution to the coats-being-returned-to-departing-guests problem using the principle of inclusion and exclusion that we already discussed in class yesterday. Hope this additional written explanation helps.

## Files
- [Class notes 12th August 2026.pdf](https://drive.google.com/file/d/1fQ8knXHLDwYdowXlHclXblIEgf4njYs2/view?usp=drive_web) (original, 2026-08-11)
- [Class notes 12th August 2026.pdf, updated with the coats solution](https://drive.google.com/file/d/1mO1SHMj4vxZbxkuDSoG4K7JEp_foI6lm/view?usp=drive_web) (2026-08-13)

## Related
- [[introduction-to-probability/2026-08-05-class-notes-6th-august-2026]]: the axioms and naive definition this builds on
- [[introduction-to-probability/2026-08-06-practice-problems-7th-august-2026]]: counting practice before this class
- [[introduction-to-probability/2026-08-13-practice-problems-14th-august-2026]]: problems 1-2 prove the inclusion-exclusion identity
- [[08-Probability/PR01 Counting and the Axioms of Probability]]: vault chapter on the same ground
