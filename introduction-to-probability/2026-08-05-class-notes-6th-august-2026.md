---
id: introduction-to-probability/2026-08-05-class-notes-6th-august-2026
aliases: [Class notes 6 August 2026]
tags: [introduction-to-probability, lecture, axioms]
trust_tier: agent_written
---

# Class notes 6 August 2026

## Covered
Sample spaces, events, the naive definition and the axioms of probability (Classroom: Class notes 6th August 2026).

- **Left over from the previous notes.** $k$ labelled boxes and $n$ identical balls: how many ways to place the balls, and how many if every box must hold at least one ball? The class maps this to writing a positive integer as an ordered sum of non-negative (respectively positive) integers.
- **Random experiment.** An experiment where the set of possible outcomes is known but which outcome will occur is not. Examples in the notes: administering a drug (better / worse / same), or measuring blood pressure in whole mmHg (sample space the positive integers, in practice a finite subset).
- **Sample space** $S$ (or $\Omega$): the set of all possible outcomes; each element is a **sample point**.
- **Event:** any subset $E\subseteq S$. Posed examples: sample space of 3 coin tosses; of 2 dice throws; the events "sum of the two outcomes is even" and "sum divisible by 3"; light-bulb lifetimes of at least 1000 hours, with the events "at least 2000 hours" and "between 2000 and 3000 hours".
- **Event algebra.** $E\cup F$ is the event of points in $E$ or $F$ (or both); $E\cap F$ the points in both. Commutative, associative and distributive laws hold: $(E\cup F)\cap G=(E\cap G)\cup(F\cap G)$ and $(E\cap F)\cup G=(E\cup G)\cap(F\cup G)$.
- **De Morgan's laws:** $\Big(\bigcup_{i=1}^nE_i\Big)^c=\bigcap_{i=1}^nE_i^c$ and $\Big(\bigcap_{i=1}^nE_i\Big)^c=\bigcup_{i=1}^nE_i^c$, with $E^c=S\setminus E$.
- **Naive definition.** For a finite sample space $S$ and event $A\subset S$: $P[A]=\dfrac{|A|}{|S|}=\dfrac{\text{number of outcomes favourable to }A}{\text{total number of outcomes}}$.
- **Frequency definition.** Repeat the experiment $n$ times under identical conditions and let $n(E)$ be the number of trials in which $E$ occurs: $P(E)=\lim_{n\to\infty}n(E)/n$. Two drawbacks stated: (1) why should $n(E)/n$ converge, and (2) why to the same limit for every sequence of repetitions.
- **Axiomatic definition.** Each event $E$ has a number $P(E)$ with
  1. $0\le P(E)\le1$,
  2. $P(S)=1$,
  3. for pairwise disjoint events $E_1,E_2,\dots$ ($E_i\cap E_j=\emptyset$ for $i\ne j$): $P\Big(\bigcup_{i=1}^\infty E_i\Big)=\sum_{i=1}^\infty P(E_i)$.
- **Consequence.** $1=P(S)=P(S\cup\emptyset)=P(S)+P(\emptyset)=1+P(\emptyset)$, so $P(\emptyset)=0$. Setting $E_j=\emptyset$ for $j>n$ gives finite additivity: $P\Big(\bigcup_{i=1}^nE_i\Big)=\sum_{i=1}^nP(E_i)$ for pairwise disjoint $E_1,\dots,E_n$.
- **Reading set:** pages 22 and 23 of Blitzstein and Hwang, the frequentist and Bayesian views of probability.

## From the post
Dear everyone, we shall continue with what is left to cover from today's class notes, and then continue with the notes attached below.

## Files
- [Class notes 6th August 2026.pdf](https://drive.google.com/file/d/1RU_sHKR9WcfVWBSnYnnwkFFfKDtd1L8l/view?usp=drive_web)

## Related
- [[08-Probability/PR01 Counting and the Axioms of Probability]]: the vault chapter on counting and the axioms
- [[08-Probability/Concepts/Sample Space and Events]]: your concept note on sample spaces and events
- [[08-Probability/Concepts/Axioms of Probability]]: your concept note on the three axioms
- [[08-Probability/Concepts/Naive Definition of Probability]]: your concept note on the naive definition
- [[introduction-to-probability/2026-08-05-class-notes-5th-august-2026]]: the counting rules this builds on
- [[introduction-to-probability/2026-08-06-practice-problems-7th-august-2026]]: problems on the naive definition and the axioms
