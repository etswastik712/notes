---
id: introduction-to-probability/2026-09-22-mid-semester-solutions
aliases: [Mid-semester solutions]
tags: [introduction-to-probability, exam, solutions]
trust_tier: agent_written
---

# Solutions to the mid-semester examination

## Covered
Solutions to seven problems (Classroom: Mid-semester solutions.pdf). The teacher notes that solutions need not be unique.

1. Poisson moment recursion. For $X\sim\text{Poisson}(\lambda)$, shift the index ($i\to j+1$) in $E[X^n]=\sum_{i\ge1}i^n e^{-\lambda}\lambda^i/i!$ to get
$$E[X^n]=\lambda\,E[(X+1)^{n-1}].$$
2. Matchbox problem. With $N$ matches in each box, the event $E$ that the left box is found empty while exactly $k$ matches remain in the right box happens iff the first $2N-k$ draws contain $N$ L's (and $N-k$ R's) and draw $2N-k+1$ is L. There are $\binom{2N-k}{N}$ such arrangements, each of probability $(1/2)^{2N-k+1}$, so $P[E]=\binom{2N-k}{N}(1/2)^{2N-k+1}$. The event $F$ (right box found empty, $k$ left in the left box) has the same probability; $E,F$ are disjoint, so by additivity
$$P[E\cup F]=\binom{2N-k}{N}\left(\tfrac12\right)^{2N-k}.$$
3. Bus problem: a student chosen at random vs a bus chosen at random. Buses carry 40, 33, 25, 50 students (148 in total). For a random student, $X$ is the size of their bus, $P[X=40]=40/148$ etc., so $E[X]=\dfrac{40^2+33^2+25^2+50^2}{148}$. For a random bus, $Y$ takes the same values with probability $1/4$ each, so $E[Y]=\tfrac14(40+33+25+50)=37$.
4. Bayes with guessing. $K$: he knows the answer; $R$: he gets it right; $P[R\mid K]=1$, $P[R\mid K^c]=1/n$ ($n$ options). Then $P[R]=p+\tfrac1n(1-p)$ and
$$P[K\mid R]=\frac{p}{p+\frac1n(1-p)}=\frac{np}{1+p(n-1)}.$$
5. Normalising constant of a density $Cxe^{-x/2}$ on $(0,\infty)$: by parts, $\int_0^\infty Cxe^{-x/2}\,dx=2C\int_0^\infty e^{-x/2}\,dx=4C$; setting this equal to $1$ gives $C=1/4$.
6. Inclusion-exclusion contradiction. With $|P|=312$, $|M|=470$, $|C|=525$, $|P\cap C|=42$, $|M\cap C|=147$, $|M\cap P|=86$, $|P\cap M\cap C|=25$, one gets $|P\cup M\cup C|=1057>1000$, a contradiction: the data cannot all be right. Either cardinalities or proportions may be used.
7. Stamps. $A_i$: a stamp of type $i$ appears in $k$ independent draws. $P[A_i]=1-(1-p_i)^k$; $P[A_i\cup A_j]=1-(1-p_i-p_j)^k$; hence
$$P[A_i\cap A_j]=1-(1-p_i)^k-(1-p_j)^k+(1-p_i-p_j)^k,\qquad P[A_i\mid A_j]=\frac{P[A_i\cap A_j]}{1-(1-p_j)^k}.$$

## From the post
Dear everyone, here are the solutions (which, as always, need not be unique) for the mid-semester examination. Hope everyone enjoyed writing the examination, and please feel free to reach out to me at any point of time over the rest of the semester if you need any help :-)

## Files
- [Mid-semester solutions.pdf](https://drive.google.com/file/d/1xkUTHy0QTmLDKs5xiED7pKCVqpqqmrIF/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-09-10-practice-problems-weekend-of-12th-september-2026]]: problem 6 there is the Poisson moment recursion (problem 1 here).
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: expectation and the bus example (problem 3).
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: indicators and counting arguments.
- [[introduction-to-probability/2026-09-10-class-notes-10th-september-2026]]: pdf normalisation (problem 5).
