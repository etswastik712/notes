---
id: introduction-to-probability/exam-prep
aliases: ["Exam prep: Introduction to Probability"]
tags: [exam-prep, introduction-to-probability]
trust_tier: agent_written
---

# Exam prep: Introduction to Probability

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Mid-semester examination: syllabus is everything covered in classes and tutorials from the start of the semester up to and including 18 September 2026; the date is not stated in the posts (Classroom, 2026-09-09). Quiz 3 was moved to Friday 2026-09-18 (past). Rule for any quiz or exam: no electronic gadget on your person; a phone found means 0 for that quiz (Classroom, 2026-08-28).

## Covered so far
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: Bernoulli/binomial as sums of indicators, Poisson as a binomial limit, pmf of $g(X)$, $E[g(X)]$, $E[aX+b]$
- [[introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend]]: sheet of 8 problems (sampling with and without replacement, coupon collector, hypergeometric and Poisson means, pmf from cdf)
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: joint pmf, independence of random variables, indicators, negative binomial, linearity of expectation
- [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv]]: $E[\text{Bin}(n,p)]=np$ by differentiating the binomial theorem
- [[introduction-to-probability/2026-09-03-practice-problems-4th-september-2026]]: sheet not read
- [[introduction-to-probability/2026-09-04-quiz-2-solutions]]: first green before first yellow ball, $g/(g+y)$, by a geometric series and by counting arrangements
- [[introduction-to-probability/2026-09-08-why-the-negative-binomial-distribution-is-called-so]]: negative binomial pmf in terms of failures, link to $(1-q)^{-m}$
- [[introduction-to-probability/2026-09-09-class-notes-9th-september-2026]]: raw and central moments, variance, $\operatorname{Var}[aX+b]=a^2\operatorname{Var}[X]$
- Earlier chapters in the vault: [[08-Probability/Probability - Course Map]]

## Must know
- A discrete random variable takes at most countably many values; pmf $p(x)=P[X=x]$ and $\sum_ip(x_i)=1$ (Classroom: Class notes 20th August).
- cdf $F(a)=P[X\le a]=\sum_{x\le a}p(x)$; monotone increasing, right-continuous, $F\to0$ at $-\infty$ and $\to1$ at $+\infty$ (proofs of the last two are not in the formal course material).
- $E[X]=\sum_ix_ip(x_i)$.
- $\text{Bernoulli}(p)$ is $\text{Binomial}(1,p)$; if $X_i$ are independent Bernoulli($p$) indicators, $\sum_{i=1}^nX_i\sim\text{Binomial}(n,p)$, with $E=np$.
- Binomial arises from sampling with replacement; hypergeometric (urn with $w$ white, $b$ black, $n$ drawn, $X$ = number of white) from sampling without replacement.
- Poisson($\lambda$): $P[X=n]=e^{-\lambda}\lambda^n/n!$, $n\in\mathbb N_0$; it is the limit of $\text{Binomial}(n,c/n)$.
- pmf of $Y=g(X)$: $P[Y=y]=\sum_{i:\,g(x_i)=y}p(x_i)$.
- $E[g(X)]=\sum_ig(x_i)p(x_i)$ (the proof is not examined, the formula is); $E[aX+b]=aE[X]+b$.
- Joint pmf $p(a_i,b_j)=P[X_1=a_i,X_2=b_j]$; $X_1,X_2$ independent iff $P[X_1\le x_1,X_2\le x_2]=P[X_1\le x_1]P[X_2\le x_2]$ for all $x_1,x_2$ (discrete: iff the joint pmf factorises).
- Indicator $\mathbf 1_A$ is $1$ if $A$ happens, else $0$.
- Geometric($p$): tosses until the first head; Negative Binomial($k,p$): tosses until the $k$-th head, a sum of $k$ independent Geometric($p$) variables.
- Negative Binomial pmf: $P(X=n)=\binom{n-1}{m-1}p^m(1-p)^{n-m}$ for $n\ge m$; with $f=n-m$ failures it is $\binom{m+f-1}{f}p^mq^f$, the coefficient of $q^f$ in $p^m(1-q)^{-m}$ (Classroom: negative_binomial_distribution.pdf).
- Linearity: $E[X_1+X_2]=E[X_1]+E[X_2]$ for any random variables on the same sample space, independent or not.
- $n$-th raw moment $E[X^n]=\sum_ix_i^np(x_i)$; $n$-th central moment $E[(X-E[X])^n]$.
- $\operatorname{Var}[X]=E[(X-E[X])^2]=E[X^2]-(E[X])^2$; $\operatorname{Var}[aX+b]=a^2\operatorname{Var}[X]$; standard deviation $=\sqrt{\operatorname{Var}[X]}$.
- In proofs, use only results fully proved in class, and state them with complete clarity (Quiz 2 solutions marking: a non-rigorous remark earns no points).

## Typical questions
- pmf of a count under sampling with vs without replacement; "at least once" via complement. Practise: [[introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend]], problem 1.
- pmf of winnings or another function of a count. Practise: same sheet, problem 2.
- Coupon collector pmf via $P[T>n]$ and inclusion–exclusion. Practise: same sheet, problem 3.
- $E[X]$ for hypergeometric, Poisson, binomial. Practise: same sheet, problems 4, 6, 8; [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv]].
- Choose the better strategy by comparing expected payoffs. Practise: same sheet, problem 5.
- pmf and mean from a step cdf. Practise: same sheet, problem 7.
- Find a normalising constant for $c\lambda^i/i!$, then tail probabilities; first-head-or-$n$-flips pmf; at-least-one-large-number draws; bus example for $E[X]$; random-walk position as a transformation of a binomial. Practise: [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]].
- Joint pmf of sum and max (or sum and absolute difference) of two dice. Practise: [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]].
- Probability that one colour appears before another in draws from an urn, with and without replacement (geometric series; arrangement counting with Pascal's identity). Practise: [[introduction-to-probability/2026-09-04-quiz-2-solutions]].
- Variances of binomial, Poisson, geometric and negative binomial; moment recursions for Poisson. Practise: the practice sheet for 11 September and the weekend (Classroom file, not yet filed as a note) and [[introduction-to-probability/2026-09-09-class-notes-9th-september-2026]].

## Gaps
- Practice problems 4 September 2026: the PDF could not be downloaded (RemoteDisconnected), so its problems are not covered.
- Date and time of the mid-semester examination, and of Quiz 3 (18 September), are not stated in the posts.
- Whether the geometric/negative-binomial derivations and their expectations are examined: the notes say they "will be derived in class", with no written derivation in these files.
- The variance proofs ($E[X^2]-(E[X])^2$, $\operatorname{Var}[aX+b]$) are "done in class", not written in the notes; variance of a sum of independent variables is stated not to be proved in the course.
- Continuous random variables (started 9-10 September) are within the mid-semester syllabus but their class notes are not filed yet; the vault chapter [[08-Probability/PR05 Continuous Random Variables]] covers them.
- Joint cdf and conditional distributions appear in the vault chapters ([[08-Probability/PR04 Joint Distributions Expectation and Variance]]) but not in the class notes filed so far.
<!-- /kurooto:exam-prep -->
