---
id: introduction-to-probability/2026-09-09-class-notes-9th-september-2026
aliases: [Class notes 9 Sep 2026]
tags: [probability, mt2113, class-notes, variance, moments]
trust_tier: agent_written
---

# Class notes 9th September 2026

## Covered
**Plan for the class.** First finish transformations of random variables (cdf, pmf and expectation of a transformed variable) from the updated class notes of 27 August 2026; then the material below (Classroom: Class notes 9th September 2026.pdf).

**Moments.**
- $E[X]$ is the first moment (first raw moment). The $n$-th (raw) moment, $n\in\mathbb N$, is $E[X^n]$; for discrete $X$ with values $x_1,x_2,\dots$,
$$E[X^n]=\sum_{i=1}^\infty x_i^n\,p(x_i).$$
- The $n$-th central moment is $E\big[(X-E[X])^n\big]$. By the binomial expansion it can be written in terms of the $k$-th raw moments, $k=1,\dots,n$.

**Variance.**
- $\operatorname{Var}[X]=E\big[(X-E[X])^2\big]$: the second central moment, related to the second raw moment.
- Alternative form: $\operatorname{Var}[X]=E[X^2]-(E[X])^2$ (proof to be done in class).
- For constants $a,b$: $\operatorname{Var}[aX+b]=a^2\operatorname{Var}[X]$ (to be shown in class).
- Standard deviation $=\sqrt{\operatorname{Var}[X]}$.
- Variances of the well-known discrete distributions will be computed in class or tutorials (see the practice sheet for 11 September).

**Next.** Time permitting, the start of continuous random variables and continuous distributions; the class notes for that will be posted the next day.

## From the post
Dear everyone, we shall first finish our discussion on transformations of random variables (from the updated class notes dated 27th August 2026), then move on to the class notes attached here.

## Files
- [Class notes 9th September 2026.pdf](https://drive.google.com/file/d/1UiF22T33QVFBx0lnB2RBz2HyaNKPUNPw/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: the transformations discussion finished here, and $E[g(X)]$.
- [[08-Probability/PR04 Joint Distributions Expectation and Variance]]: variance in their own chapter notes.
- [[08-Probability/PR06 Moments Generating Functions and Limit Theorems]]: moments in their own notes.
- [[08-Probability/PR05 Continuous Random Variables]]: where the continuous material starts.

<!-- kurooto:material20276d9b -->
## Concepts in Class notes 9th September 2026
[[zettel/raw-moment]], [[zettel/central-moment]], [[zettel/variance]], [[zettel/standard-deviation]]
<!-- /kurooto:material20276d9b -->
