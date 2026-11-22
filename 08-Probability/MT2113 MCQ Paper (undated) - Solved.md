---
title: MT2113 MCQ Paper (undated) - Solved
aliases: [Probability MCQ paper, MT2113 multiple choice, qpaper (3)]
subject: probability
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/probability, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# MT2113 Probability: the Undated Multiple-Choice Paper, Solved

[[Probability - Course Map|Course Map]] · [[Probability Quiz Prep]] · dated papers: [[MT2113 Past Papers 2022 - Solved|2022]] · [[MT2113 Past Papers 2023 - Solved|2023]] · [[MT2113 Past Papers 2024 - Solved|2024]] · [[MT2113 Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · an older MT2113 paper (year unknown)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine; Markov chains are not in this year's syllabus)</span>

> [!info] The paper
> `qp-archive/MT2113/qpaper (3).pdf`: 8 typeset pages, no date or instructor, in three parts:
> - I: single answer, any 9 × 1 mark;
> - II: single answer, any 11 × 2;
> - III: multiple answers, any 6 × 3.
>
> In this copy **some options are printed grey**, apparently the marked or keyed answers. Below, "key" means the grey option.
>
> I agree with the key everywhere except **II.11 and II.12, where the keyed answer is wrong**, and **II.1, whose keyed answer is right only for disjoint events**, although the question says the events are independent. Three questions on Markov chains (I.10, II.12, III.3) go beyond this year's course ([[Probability - Course Map]]). Checks: `scripts/pr_qp_archive_numbers.py`.

## Part I (single answer)

| # | answer | why |
|---|---|---|
| 1 | $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ | inclusion–exclusion; the others fail for overlapping events |
| 2 | $e^{-35}$ | memoryless: $P(X>10\mid X>3)=P(X>7)=e^{-5\cdot7}$ (rate 5) |
| 3 | always $\ge1$ | Cauchy–Schwarz: $1=(E[X\cdot\tfrac1X])^2\le E[X^2]E[1/X^2]$ |
| 4 | $P(X+Y>10)\le P(X>5\text{ or }Y>5)$ | if both $\le5$ then the sum is $\le10$: $\{X+Y>10\}\subseteq\{X>5\}\cup\{Y>5\}$ |
| 5 | $F$ jumps at the points of $S$ | a jump of size $P(X=k)$ (assuming each value has positive mass) |
| 6 | "the empty set has positive probability" is false | $P(\varnothing)=0$ |
| 7 | $\tfrac43e^{-2}$ | $e^{-2}2^3/3!$ |
| 8 | $(1-p)^4$ | $X\ge5$ iff the first 4 trials fail |
| 9 | $\tfrac32$ | strong law: numerator $/n\to3$, denominator $/n\to2$ almost surely |
| 10 | $\tfrac32$ | below |
| 11 | 980 | $\binom82\binom73=28\times35$ |

> [!example]- I.10 · Expected return time to green
> From green, the light stays green with probability $\tfrac23$ (returns in 1 step) or turns red ($\tfrac13$). From red, the time to turn green is geometric with mean $1/\tfrac23=\tfrac32$. So $E=\tfrac23\cdot1+\tfrac13(1+\tfrac32)=\tfrac32$. Equivalently, the stationary law has $\pi_G\cdot\tfrac13=\pi_R\cdot\tfrac23$, so $\pi_G=\tfrac23$, and the mean return time is $1/\pi_G=\tfrac32$.

## Part II (single answer)

| # | answer | why |
|---|---|---|
| 1 | key: $\frac{P(A)}{P(A)+P(B)}$, but see below | |
| 2 | $F(x)+F(-x)=1+P(X=x)$ | symmetry: $F(-x)=P(X\ge x)=1-F(x)+P(X=x)$ |
| 3 | $\tfrac18$ | $\tfrac12$ (pick the orange) $\times\tfrac14$ (sweet) |
| 4 | $\tfrac{40}{41}$ | $\frac{0.8\cdot0.1}{0.8\cdot0.1+0.2\cdot0.01}=\frac{0.08}{0.082}$ |
| 5 | $\sqrt2$ | $\int\frac{1}{\sqrt{2\pi}}e^{-z^2/2+z^2/4}dz=\frac{\sqrt{4\pi}}{\sqrt{2\pi}}$ (numerically 1.41421) |
| 6 | $\tfrac{16}{27}$ | $(\tfrac23)^4+4\cdot\tfrac13(\tfrac23)^3=\tfrac{48}{81}$ |
| 7 | Uniform$[0,t]$ | the joint density $\lambda^2e^{-\lambda t}$ is constant along $x_1+x_2=t$ |
| 8 | $\tfrac9{23}$ | $\frac{0.7a}{0.7a+0.3(1-a)}=0.6\Rightarrow a=\frac{0.18}{0.46}$ |
| 9 | $\tfrac16$ | $E[X]-E[X^2]=\tfrac12-\tfrac13$ |
| 10 | 1 | $\tfrac32-\tfrac34+\tfrac14$ |
| 11 | **42 (not offered; key 41)** | below |
| 12 | **9 (key 10)** | below |

> [!warning] II.1 · "Independent" events are not disjoint
> If $A$ and $B$ are independent with positive probabilities, then $P(A\cap B)=P(A)P(B)>0$, so a single trial can produce **both**. "A before B" then means that the first trial producing either produces $A$ alone. Its probability is
> $$\frac{P(A\cap B^c)}{P(A\cup B)}=\frac{P(A)(1-P(B))}{P(A)+P(B)-P(A)P(B)} .$$
> The keyed $\frac{P(A)}{P(A)+P(B)}$ is the answer for **mutually exclusive** $A,B$ (the "5 before 7" problem of [[PR02 Conditional Probability Bayes Rule and Independence]] §5). The question's word "independent" was probably meant to say that the *trials* are independent.

> [!warning] II.11 · Two 1's in a row: $E[N]=42$
> Condition on the first throws, as the hint suggests. Let $E$ be the expected number of throws needed. If throw 1 is not a 1 ($\tfrac56$), we start over: cost $1+E$. If it is a 1 and throw 2 is a 1 ($\tfrac1{36}$), we are done in 2. If it is a 1 and throw 2 is not ($\tfrac5{36}$), we start over after 2: cost $2+E$. So
> $$E=\tfrac56(1+E)+\tfrac1{36}\cdot2+\tfrac5{36}(2+E)\ \Rightarrow\ E\big(1-\tfrac56-\tfrac5{36}\big)=\tfrac56+\tfrac2{36}+\tfrac{10}{36}\ \Rightarrow\ \tfrac1{36}E=\tfrac{42}{36},$$
> so $E=42$ (the general formula is $1/p+1/p^2=6+36$; a simulation of 40 000 runs gives 41.8). None of the options (6, 36, 37, 41) is correct; the keyed 41 is wrong.

> [!warning] II.12 · Returns to a transient state: $E[N]=9$
> Each time the chain is at $s$, it returns again with probability $\tfrac9{10}$, independently of the past (the Markov property). So the number of **returns** is geometric: $P(N=k)=(\tfrac9{10})^k\tfrac1{10}$, $k=0,1,\dots$, with mean $\frac{9/10}{1/10}=9$. The keyed 10 counts the visit at time 0 too (it is $E[N]+1$), but the question defines $N$ over $i\ge1$.

## Part III (multiple answers)

| # | correct options | why |
|---|---|---|
| 1 | increases then decreases; maximum at $k=5$ | Bin$(9,\tfrac12)$ is symmetric about 4.5, so $f(4)=f(5)$ are the joint maxima (so "max at 5" is true, though 4 is also a maximiser) |
| 2 | $EX=c\frac p{1-p}$; $\operatorname{var}X=\frac{cp(1-cp)}{(1-p)^2}$ | $c=-1/\ln(1-p)$ (so "$c=-\ln(1-p)$" is false); $E[X^2]=c\frac p{(1-p)^2}$ |
| 3 | stationary $(\tfrac49,\tfrac19,\tfrac49)$; irreducible | $0\to1\to2\to0$, so no state is transient; balance gives $\pi_2=\pi_0$, $\pi_1=\pi_0/4$ (checked numerically) |
| 4 | both convolution forms | substitute $t\to a-t$ to see that they are equal |
| 5 | $\tfrac52$ | $\tfrac14(1+2+3+4)$ (total expectation over the ward) |
| 6 | $P(X=0)=P(X=1)=\tfrac12$; $E[3^X]=2$ | $E[X^2]=\tfrac12$, not 2 |
| 7 | $EX=\frac n2(p_1+p_2)$; $\operatorname{var}=\frac{n^2}4(p_1-p_2)^2+\frac n2\sum p_i(1-p_i)$ | total variance $=E[\operatorname{Var}(X\mid\text{coin})]+\operatorname{Var}(E[X\mid\text{coin}])$ |
| 8 | $E\ln X\le\ln EX$; $P(X>c)\le E\sqrt X/\sqrt c$; $E(\sin^2+\cos^2)=1$ | Jensen; Markov applied to $\sqrt X$ ($c>0$); $E(XY)=\sqrt{E X^2EY^2}$ is false in general (Cauchy–Schwarz gives only $\le$) |
