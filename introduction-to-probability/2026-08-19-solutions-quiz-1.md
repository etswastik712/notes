---
id: introduction-to-probability/2026-08-19-solutions-quiz-1
aliases: [Solutions to Quiz 1]
tags: [introduction-to-probability, quiz, solutions, counting, axioms]
trust_tier: agent_written
---

# Solutions to Quiz 1

## Covered
Two problems with solutions (the problem statements are reconstructed from the solutions; the instructor notes the solutions need not be unique) (Classroom: Solutions Quiz 1.pdf).

**Problem 1: committee with exactly $j$ married couples.** There are $n$ couples ($2n$ people); a committee of $k$ people is chosen with all choices equally likely. Find the probability that it contains exactly $j$ married couples.
- Total committees: $\binom{2n}{k}$.
- Choose the $j$ couples that are fully included: $\binom nj$.
- The remaining $k-2j$ members must come from distinct couples among the other $n-j$ couples: choose those couples in $\binom{n-j}{k-2j}$ ways, then one partner from each in $2^{k-2j}$ ways.
- Hence
$$P=\frac{\binom nj\binom{n-j}{k-2j}2^{k-2j}}{\binom{2n}{k}}.$$

**Problem 2: symmetric difference.** Show $P[A\triangle B]=P[A]+P[B]-2P[A\cap B]$.
- $A\triangle B=(A\cap B^c)\cup(A^c\cap B)$, a disjoint union, so by the third axiom $P[A\triangle B]=P[A\cap B^c]+P[A^c\cap B]$.
- $A=(A\cap B^c)\cup(A\cap B)$, disjoint, so $P[A\cap B^c]=P[A]-P[A\cap B]$.
- Likewise $P[A^c\cap B]=P[B]-P[A\cap B]$.
- Adding gives the claim.

Pattern for exam answers: decompose into disjoint pieces, name the axiom used at each step, count by the multiplication principle (choose the couples, then the singles, then a partner from each).

## From the post
Dear everyone, I forgot to post the solutions (these need not be unique) to Quiz 1. Here they are.

## Files
- [Solutions Quiz 1.pdf](https://drive.google.com/file/d/1rE8aQKW3OANr-M635eq4CeVHhN2S1W3v/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-08-05-class-notes-5th-august-2026]]: counting, binomial coefficients
- [[introduction-to-probability/2026-08-05-class-notes-6th-august-2026]]: axioms of probability used in problem 2
- [[introduction-to-probability/2026-08-06-practice-problems-7th-august-2026]]: Quiz 1 practice sheet
