---
id: introduction-to-probability/exam-prep
aliases: ["Exam prep: Introduction to Probability"]
tags: [exam-prep, introduction-to-probability]
trust_tier: agent_written
---

# Exam prep: Introduction to Probability

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Not announced yet. The mid-semester examination has taken place (solutions posted 2026-09-22, answer scripts shown 2026-09-26 and 2026-10-13); no later quiz or exam date is in the posts, the latest of which is dated 2026-10-24. Rule for any quiz or exam: no electronic gadget, notes or paper on your person; a phone found means 0 for that quiz (Classroom, 2026-08-28), and at the mid-semester a violation cancelled the examination and was reported to the Academic Office (Classroom, 2026-09-18). No calculator was needed at the mid-semester.

## Covered so far
- [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]: Bernoulli/binomial as sums of indicators, Poisson as a binomial limit, pmf of $g(X)$, $E[g(X)]$, $E[aX+b]$
- [[introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend]]: sheet of 8 problems (sampling with and without replacement, coupon collector, hypergeometric and Poisson means, pmf from cdf)
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: joint pmf, independence of random variables, indicators, negative binomial, linearity of expectation
- [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv]]: $E[\text{Bin}(n,p)]=np$ by differentiating the binomial theorem
- [[introduction-to-probability/2026-09-03-practice-problems-4th-september-2026]]: sheet not read
- [[introduction-to-probability/2026-09-04-quiz-2-solutions]]: first green before first yellow ball, $g/(g+y)$, by a geometric series and by counting arrangements
- [[introduction-to-probability/2026-09-08-why-the-negative-binomial-distribution-is-called-so]]: negative binomial pmf in terms of failures, link to $(1-q)^{-m}$
- [[introduction-to-probability/2026-09-09-class-notes-9th-september-2026]]: raw and central moments, variance, $\operatorname{Var}[aX+b]=a^2\operatorname{Var}[X]$
- [[introduction-to-probability/2026-09-10-practice-problems-weekend-of-12th-september-2026]]: 11 problems: Poisson approximation, variances of binomial/Poisson/geometric/negative binomial, Poisson moment recursion, modes, standardisation, $E[1/(X+1)]$, $\sum iP[N>i]$
- [[introduction-to-probability/2026-09-10-class-notes-10th-september-2026]]: continuous random variables, pdf, $P[X=x]=0$, cdf-pdf link, $E[X]$, $E[g(X)]$, variance for continuous $X$
- [[introduction-to-probability/2026-09-17-practice-problems-17th-september-and-following-tutorial-and-weekend]]: 11 mixed problems (hypergeometric vs binomial, mixture of two coins, Bayes, pmf from a mixed cdf, normalising a pdf)
- [[introduction-to-probability/2026-09-18-quiz-3-solutions]]: $P[\text{NegBin}>n]=P[\text{Bin}<r]$, memorylessness of the geometric
- [[introduction-to-probability/2026-09-22-mid-semester-solutions]]: Poisson moment recursion, matchbox problem, bus paradox, Bayes with guessing, normalising constant, inclusion-exclusion, stamps
- [[introduction-to-probability/2026-10-08-week-1-post-mid-term-hw-and-lecture-notes]]: uniform, logistic, Rayleigh, standard normal and Gaussian; LOTUS with proof for $g\ge0$; $E(Y)=\int_0^\infty P(Y>y)\,dy$; homework of 6 problems
- [[introduction-to-probability/2026-10-15-hw-2-problems]]: HW 2 (exponential repair time, Gumbel and the maximum of exponentials, $E[F(X)]$)
- [[introduction-to-probability/2026-10-22-hw3-problems-and-median-clarification]]: median of a discrete variable (corrected definition); HW3 (median, mode, skewness, mgf, folded normal)
- Earlier chapters in the vault: [[08-Probability/Probability - Course Map]]

## Must know
- A discrete random variable takes at most countably many values; pmf $p(x)=P[X=x]$ and $\sum_ip(x_i)=1$ (Classroom: Class notes 20th August).
- cdf $F(a)=P[X\le a]=\sum_{x\le a}p(x)$; monotone increasing, right-continuous, $F\to0$ at $-\infty$ and $\to1$ at $+\infty$ (proofs of the last two are not in the formal course material).
- $P[X=x]=F(x)-F(x^-)$, where $F(x^-)=\lim_{y\to x^-}F(y)=P[X<x]$ (Classroom: practice sheet of 17 September).
- $E[X]=\sum_ix_ip(x_i)$.
- $\text{Bernoulli}(p)$ is $\text{Binomial}(1,p)$; if $X_i$ are independent Bernoulli($p$) indicators, $\sum_{i=1}^nX_i\sim\text{Binomial}(n,p)$, with $E=np$.
- Binomial arises from sampling with replacement; hypergeometric (urn with $w$ white, $b$ black, $n$ drawn, $X$ = number of white) from sampling without replacement.
- Poisson($\lambda$): $P[X=n]=e^{-\lambda}\lambda^n/n!$, $n\in\mathbb N_0$; it is the limit of $\text{Binomial}(n,c/n)$. Moment recursion: $E[X^n]=\lambda E[(X+1)^{n-1}]$ (Classroom: mid-semester solutions, problem 1).
- pmf of $Y=g(X)$: $P[Y=y]=\sum_{i:\,g(x_i)=y}p(x_i)$.
- $E[g(X)]=\sum_ig(x_i)p(x_i)$ (the proof is not examined, the formula is); $E[aX+b]=aE[X]+b$.
- Joint pmf $p(a_i,b_j)=P[X_1=a_i,X_2=b_j]$; $X_1,X_2$ independent iff $P[X_1\le x_1,X_2\le x_2]=P[X_1\le x_1]P[X_2\le x_2]$ for all $x_1,x_2$ (discrete: iff the joint pmf factorises).
- Indicator $\mathbf 1_A$ is $1$ if $A$ happens, else $0$.
- Geometric($p$): tosses until the first head, $P[X=i]=(1-p)^{i-1}p$, $P[X>i]=(1-p)^i$; memoryless: $P[X>m+n\mid X>m]=P[X>n]$ (Classroom: Quiz 3 solutions).
- Negative Binomial($k,p$): tosses until the $k$-th head, a sum of $k$ independent Geometric($p$) variables; $P[\text{NegBin}(r,p)>n]=P[\text{Bin}(n,p)<r]$ (Classroom: Quiz 3 solutions).
- Negative Binomial pmf: $P(X=n)=\binom{n-1}{m-1}p^m(1-p)^{n-m}$ for $n\ge m$; with $f=n-m$ failures it is $\binom{m+f-1}{f}p^mq^f$, the coefficient of $q^f$ in $p^m(1-q)^{-m}$ (Classroom: negative_binomial_distribution.pdf).
- Linearity: $E[X_1+X_2]=E[X_1]+E[X_2]$ for any random variables on the same sample space, independent or not (also for continuous or mixed variables).
- $n$-th raw moment $E[X^n]=\sum_ix_i^np(x_i)$; $n$-th central moment $E[(X-E[X])^n]$.
- $\operatorname{Var}[X]=E[(X-E[X])^2]=E[X^2]-(E[X])^2$; $\operatorname{Var}[aX+b]=a^2\operatorname{Var}[X]$; standard deviation $=\sqrt{\operatorname{Var}[X]}$.
- Bayes' rule with total probability: $P[K\mid R]=\dfrac{P[R\mid K]P[K]}{P[R\mid K]P[K]+P[R\mid K^c]P[K^c]}$ (Classroom: mid-semester solutions, problem 4).
- $X$ is continuous if its cdf is absolutely continuous (so continuous); equivalently there is a pdf $f\ge0$ with $P[X\in B]=\int_Bf(x)\,dx$ (Classroom: Class notes 10th September 2026).
- A pdf satisfies $f\ge0$ and $\int_{-\infty}^\infty f(x)\,dx=1$; it is required to be continuous except at finitely many points (Classroom: week1_mt2113.pdf).
- For continuous $X$: $P[X=x]=0$ for every $x$, because $P[X=x]=F(x)-F(x^-)=0$ when $F$ is continuous; so $P[a<X<b]=P[a\le X\le b]=\int_a^bf(x)\,dx$.
- $F(x)=\int_{-\infty}^xf(y)\,dy$ and $F'(x)=f(x)$; to find a distribution, find the cdf first and differentiate.
- Continuous $X$: $E[X]=\int xf(x)\,dx$; $E[g(X)]=\int g(x)f(x)\,dx$ (LOTUS; proved in class for $g\ge0$); $\operatorname{Var}[X]=\int(x-\mu)^2f(x)\,dx=E[X^2]-(E[X])^2$.
- Lemma: for a non-negative random variable $Y$, $E(Y)=\int_0^\infty P(Y>y)\,dy$ (proved by interchanging the order of integration) (Classroom: week1_mt2113.pdf).
- $\text{Unif}(a,b)$: $f=1/(b-a)$ on $[a,b]$, $E=(a+b)/2$, $\operatorname{Var}=(b-a)^2/12$.
- Standard normal $\varphi(x)=e^{-x^2/2}/\sqrt{2\pi}$, with $\int e^{-x^2/2}dx=\sqrt{2\pi}$ (via $I^2$ in polar coordinates); $E(Z)=0$, $\operatorname{Var}(Z)=1$. $X\sim N(\mu,\sigma)$ iff $X=\sigma Z+\mu$; then $E(X)=\mu$, $\operatorname{Var}(X)=\sigma^2$.
- Rayleigh: $f(x)=xe^{-x^2/2}$ for $x>0$, $F(x)=1-e^{-x^2/2}$, $E=\sqrt{\pi/2}$. Logistic: $f(x)=e^x/(1+e^x)^2$, $F(x)=e^x/(1+e^x)$, $E=0$.
- Median: $c$ is a median of $X$ if $P(X\le c)\ge\tfrac12$ and $P(X\ge c)\ge\tfrac12$ (the instructor corrected the board, which had $P(X\ge c)\le\tfrac12$). For a discrete $X$ with values $x_1<\dots<x_n$, if $p_1+\dots+p_{i-1}<\tfrac12\le p_1+\dots+p_i$, then $x_i$ is a median (the smallest that works), since $p_i+\dots+p_n=1-(p_1+\dots+p_{i-1})\ge\tfrac12$ (Classroom: announcement of 2026-10-22).
- Skewness is the standardised third central moment and kurtosis the fourth; higher moments matter e.g. for the Lyapunov condition in central limit theorems (Classroom: announcement of 2026-09-15).
- In proofs, use only results fully proved in class, and state them with complete clarity (Quiz 2 solutions marking: a non-rigorous remark earns no points).
- A solution may use mgfs as a concept, but the mgf of a known distribution (e.g. binomial) must be derived before use, or points are lost (Classroom, 2026-09-17).
- $\operatorname{Var}\big[\sum X_i\big]=\sum\operatorname{Var}[X_i]$ for independent $X_i$ is not proved in this course, so it cannot be used in solutions (Classroom: practice sheet, problem 5).

## Typical questions
- pmf of a count under sampling with vs without replacement; "at least once" via complement. Practise: [[introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend]], problem 1; [[introduction-to-probability/2026-09-17-practice-problems-17th-september-and-following-tutorial-and-weekend]], problem 1.
- pmf of winnings or another function of a count. Practise: 28 August sheet, problem 2; 17 September sheet, problems 4, 6, 7.
- Coupon collector pmf via $P[T>n]$ and inclusion–exclusion. Practise: 28 August sheet, problem 3.
- $E[X]$ for hypergeometric, Poisson, binomial. Practise: 28 August sheet, problems 4, 6, 8; [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv]].
- Choose the better strategy by comparing expected payoffs. Practise: 28 August sheet, problem 5.
- pmf and mean from a step cdf; pmf from a cdf with a continuous part and jumps. Practise: 28 August sheet, problem 7; 17 September sheet, problem 9.
- Mixture distributions by total probability (random choice of coin); Bayes' rule on populations. Practise: 17 September sheet, problems 2 and 10; [[introduction-to-probability/2026-09-22-mid-semester-solutions]], problem 4.
- Ranking and comparison problems (best rank of a woman, number of wins of player 1). Practise: 17 September sheet, problems 5 and 8.
- Find a normalising constant for $c\lambda^i/i!$, then tail probabilities; first-head-or-$n$-flips pmf; at-least-one-large-number draws; bus example for $E[X]$; random-walk position as a transformation of a binomial. Practise: [[introduction-to-probability/2026-08-26-class-notes-27th-august-2026]]; bus problem also in the mid-semester solutions, problem 3.
- Joint pmf of sum and max (or sum and absolute difference) of two dice. Practise: [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]].
- Probability that one colour appears before another in draws from an urn, with and without replacement. Practise: [[introduction-to-probability/2026-09-04-quiz-2-solutions]].
- Relations between negative binomial, binomial and geometric tails; memorylessness. Practise: [[introduction-to-probability/2026-09-18-quiz-3-solutions]].
- Matchbox-type counting by arrangements of L/R draws; inclusion-exclusion consistency check; "at least one of type $i$" events in independent draws. Practise: mid-semester solutions, problems 2, 6, 7.
- Poisson approximation to a binomial with huge $N$ and small success probability. Practise: [[introduction-to-probability/2026-09-10-practice-problems-weekend-of-12th-september-2026]], problem 1.
- Variances of binomial, Poisson, geometric and negative binomial, without using the variance of a sum of independent variables. Practise: same sheet, problems 2-5.
- Moment recursion $E[X^n]=\lambda E[(X+1)^{n-1}]$ for Poisson, then $E[X^3]$. Practise: same sheet, problem 6; mid-semester solutions, problem 1.
- Modes of binomial and Poisson. Practise: 12 September sheet, problems 7-8.
- Standardised variable $Y=(X-\mu)/\sigma$: mean, variance, pmf, cdf. Practise: 12 September sheet, problem 9.
- $E[1/(X+1)]$ for binomial; $\sum_ii\,P[N>i]$ in terms of $E[N^2]$ and $E[N]$. Practise: 12 September sheet, problems 10-11.
- Pdf basics: check a function is a pdf, find $c$, compute $P[a<X<b]$, cdf from pdf and back, $E[X]$ and $\operatorname{Var}[X]$ by integration. Practise: [[introduction-to-probability/2026-09-10-class-notes-10th-september-2026]]; 17 September sheet, problem 11; mid-semester solutions, problem 5; Week 1 homework, problem 1.
- Quantiles of a continuous distribution (Rayleigh). Practise: [[introduction-to-probability/2026-10-08-week-1-post-mid-term-hw-and-lecture-notes]], homework problem 1.
- Mean and variance of a function of a continuous variable via LOTUS, and its cdf/pdf by the cdf method (area of a circle with uniform radius). Practise: Week 1 homework, problem 2.
- Expectation of a truncated normal, $E(\max\{Z-c,0\})$; inflection points of the normal pdf. Practise: Week 1 homework, problems 4-5.
- Proof that $E(Y)=\int_0^\infty P(Y>y)\,dy-\int_0^\infty P(Y<-y)\,dy$ and LOTUS for general $g$. Practise: Week 1 homework, problem 6 (starred, optional).
- Exponential tail and conditional tail (repair time with $\lambda=1/2$: $P(>2)$, $P(\ge10\mid>9)$). Practise: [[introduction-to-probability/2026-10-15-hw-2-problems]], problem 1.
- Cdf of a transformed variable ($-\log X$, Gumbel) and convergence in distribution of $M_n-\log n$ for the maximum of i.i.d. $\text{Expo}(1)$. Practise: HW 2, problem 2.
- $E[F(X)]$ for continuous $X$, with and without LOTUS. Practise: HW 2, problem 3.
- Median and mode of uniform, exponential and Pareto distributions; skewness of the exponential (positive, free of $\lambda$). Practise: [[introduction-to-probability/2026-10-22-hw3-problems-and-median-clarification]], problems 1-3.
- Mgf of a sum of two dice rolls; mean and variance of $\text{Geom}(p)$ from its mgf (derive the mgf first); two integral expressions for the mgf of the folded normal $|Z|$. Practise: HW3, problems 4-6.

## Gaps
- Practice problems 4 September 2026: the PDF could not be downloaded (RemoteDisconnected), so its problems are not covered.
- No date is announced for the next quiz or exam (end-semester or otherwise), nor its syllabus.
- Week 1 homework: due date and whether it is collected are not stated. The PDF is handwritten and was read from page images, so formulas should be checked against the file. The due dates of HW 2 and HW3 are not stated either.
- The Week2_notes.pdf and Week3_notes.pdf files hold only the homework problems; the lecture notes for Weeks 2 and 3 (announced as posted on 2026-10-24) are not filed, so the exponential distribution, the median/mode/skewness lectures, the mgf definition and the folded normal "discussed in class" have no class notes here yet.
- HW3 problem 4 is marked "postponed to next hw" in the file but listed without that remark in the post.
- Quiz 3, problem 3: statement not in the solutions file ("deduced in class in detail").
- Whether the geometric/negative-binomial derivations and their expectations are examined: the notes say they "will be derived in class", with no written derivation in these files.
- The variance proofs ($E[X^2]-(E[X])^2$, $\operatorname{Var}[aX+b]$) are "done in class", not written in the notes; variance of a sum of independent variables is stated not to be proved in the course.
- Class notes after 10 September other than Week 1 are not filed (the lecture of 15-17 September where mgfs were mentioned). The vault chapter [[08-Probability/PR05 Continuous Random Variables]] covers more densities and [[08-Probability/PR06 Moments Generating Functions and Limit Theorems]] mgfs.
- Joint cdf and conditional distributions appear in the vault chapters ([[08-Probability/PR04 Joint Distributions Expectation and Variance]]) but not in the class notes filed so far; joint distributions of continuous variables are not yet filed.
- Mid-semester solutions problem 6 shows the data are contradictory ($1057>1000$); the original problem statement is not in the file.
<!-- /kurooto:exam-prep -->
