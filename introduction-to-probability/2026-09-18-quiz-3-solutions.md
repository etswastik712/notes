---
id: introduction-to-probability/2026-09-18-quiz-3-solutions
aliases: [Quiz 3 solutions]
tags: [introduction-to-probability, quiz, solutions]
trust_tier: agent_written
---

# Quiz 3 solutions

## Covered
Three quiz problems; the solutions to 1 and 2 are given, the third is only referred to class (Classroom: Quiz 3 solutions.pdf).

1. Negative binomial vs binomial. Let $X\sim\text{NegBin}(r,p)$ (the number of trials up to and including the $r$-th success) and $Y\sim\text{Binomial}(n,p)$ (the number of successes in the first $n$ trials). Let $E$ be the event that the first $n$ trials contain fewer than $r$ successes. Then $\{X>n\}=E$ and $\{Y<r\}=E$, so
$$P[X>n]=P[Y<r]=P[E].$$
2. Memorylessness of the geometric distribution. For $X\sim\text{Geometric}(p)$, $P[X=i]=(1-p)^{i-1}p$ for $i\in\mathbb N$, so
$$P[X>i]=\sum_{j=i+1}^\infty(1-p)^{j-1}p=p(1-p)^i\sum_{k=0}^\infty(1-p)^k=(1-p)^i.$$
Then
$$P[X>m+n\mid X>m]=\frac{P[X>m+n]}{P[X>m]}=\frac{(1-p)^{m+n}}{(1-p)^m}=(1-p)^n=P[X>n].$$
The tail $P[X>i]$ may also be deduced directly from the interpretation (the first $i$ trials all fail), but all steps must be shown with complete clarity for full credit.
3. "This has already been deduced in class in detail." The statement of problem 3 is not in the file.

## From the post
Dear everyone, here are the solutions to today's quiz.

## Files
- [Quiz 3 solutions.pdf](https://drive.google.com/file/d/1VSduZDZ_sqYrUo0zbm2GttoyZu4DvRaM/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: negative binomial and geometric variables.
- [[introduction-to-probability/2026-09-08-why-the-negative-binomial-distribution-is-called-so]]: the negative binomial as a trial count.
- [[introduction-to-probability/2026-09-04-quiz-2-solutions]]: previous quiz; same geometric-series technique.
