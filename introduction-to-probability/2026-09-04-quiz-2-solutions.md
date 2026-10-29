---
id: introduction-to-probability/2026-09-04-quiz-2-solutions
aliases: [Quiz 2 solutions]
tags: [probability, mt2113, quiz]
trust_tier: agent_written
---

# Quiz 2 solutions

## Covered
The problem statement itself is not in the file; from the solution it is an urn with red, green and yellow balls in proportions $r,g,y$ ($r+g+y=1$). Question: the probability that the first green ball appears before the first yellow ball, (a) when drawing with replacement, (b) when the urn holds exactly $rN$ red, $gN$ green and $yN$ yellow balls and all $N$ are drawn one by one (without replacement). The answer is $\frac{g}{g+y}$ in both cases (Classroom: Quiz 2 solutions.pdf).

**Part 1 (with replacement).**
- Let $E_n$ = first $n-1$ draws red and the $n$-th green. Because of replacement the proportions never change, so $P[E_n]=r^{n-1}g$.
- The event "first green before first yellow" is $\bigcup_nE_n$, and the $E_n$ are pairwise disjoint, so by the third axiom
$$P\Big[\bigcup_nE_n\Big]=\sum_{n\in\mathbb N}r^{n-1}g=\frac{g}{1-r}=\frac{g}{g+y}.$$

**Part 2 (arrangements of the whole urn).**
- Arrange all $N$ balls in the order of drawing; balls of the same colour are indistinguishable, so there are $\frac{N!}{(rN)!(gN)!(yN)!}$ sequences, all equally likely (as in class examples and class notes).
- Count the favourable sequences. Place $k$ red balls ($0\le k\le rN$) to the left of the first green ball. To its right go the remaining $rN-k$ red, the other $gN-1$ green and all $yN$ yellow balls, in $\frac{[(rN-k)+(gN-1)+yN]!}{(rN-k)!(gN-1)!(yN)!}$ ways.
- Summing over $k$ and writing $j=rN-k$:
$$\sum_{k=0}^{rN}\frac{(N-k-1)!}{(gN+yN-1)!\,(rN-k)!}\cdot(gN+yN-1)!\;\to\;\binom{gN+yN-1}{yN}\sum_{j=0}^{rN}\binom{N-rN+j-1}{j}.$$
- Repeated use of Pascal's identity gives $\sum_{j=0}^{rN}\binom{N-rN+j-1}{j}=\binom{N}{rN}$ (hockey-stick identity).
- So the number of favourable sequences is $\binom{gN+yN-1}{yN}\binom{N}{rN}$, and dividing by the total,
$$P=\frac{(rN)!(gN)!(yN)!}{N!}\cdot\frac{(gN+yN-1)!}{(gN-1)!(yN)!}\cdot\frac{N!}{(gN+yN)!(rN)!}=\frac{g}{g+y}.$$

**Marking scheme stated in the post.**
- Full points if the second part is done correctly up to, but not including, the final simplification of the sum (the blue-font simplification).
- Full points also for an argument like part 1 using conditional probabilities directly, if correct, even without simplifying the resulting sum.
- No points for only remarking that the number of red balls does not matter, so the answer is unchanged: that is not a rigorous argument.

## From the post
Dear everyone, here are the solutions (they need not be unique) to Quiz 2. Please note that if you have been able to accurately complete the second part of the question up to, but not including, the simplification I have carried out here in blue font, you will be awarded full points. Likewise, if you have utilized an argument similar to the first part of the problem for the second part (i.e. utilized conditional probabilities directly), and accurately completed the solution but not the simplification of the resulting sum, you will still be awarded full points.

If you have simply remarked, for the second part of the question, that the number of red balls does not matter and hence the answer remains unchanged, we won't be awarding you any points because this is not a rigorous mathematical argument.

## Files
- [Quiz 2 solutions.pdf](https://drive.google.com/file/d/1ETN_EBc19_3H8clxvxVMWVgnAYzYQ1pe/view?usp=drive_web)

## Related
- [[08-Probability/PR02 Conditional Probability Bayes Rule and Independence]]: conditional probability and counting arguments used here.
- [[08-Probability/PR01 Counting and the Axioms of Probability]]: multinomial arrangements and the third axiom (countable additivity).
- [[introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend]]: sampling with and without replacement practice.

<!-- kurooto:material160895af -->
## Concepts in Quiz 2 solutions
[[zettel/first-colour-arrival-probability-under-sampling-with-replacement]], [[zettel/first-colour-arrival-probability-under-sampling-without-replacement]]
<!-- /kurooto:material160895af -->
