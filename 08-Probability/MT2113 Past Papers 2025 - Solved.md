---
title: MT2113 Past Papers 2025 - Solved
aliases: [Probability midsem 2025, Probability endsem 2025, MT2113 2025, probability past paper 2025]
subject: probability
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/probability, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# MT2113 Introduction to Probability: Mid-sem and End-sem 2025, Solved

[[Probability - Course Map|Course Map]] · [[Probability Quiz Prep]] · other years: [[MT2113 Past Papers 2022 - Solved|2022]] · [[MT2113 Past Papers 2023 - Solved|2023]] · [[MT2113 Past Papers 2024 - Solved|2024]] · [[MT2113 MCQ Paper (undated) - Solved|undated MCQ paper]]

<span class="scope-taught">taught · last year's papers (Moumanti Podder, Mainak Poddar)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive archive, folder `Sem-3 Papers(Aug 2025)`, both titled `Introduction to Probability.pdf`:
> - **Mid-sem**, 25 Sep 2025, 40 points, capped at 35.
> - **End-sem**, 25 Nov 2025, 5 × 7 points.
>
> Both are scans read as images. Numbers: `scripts/pr_qp_archive_numbers.py`. Mid-sem Q4 and Q7 repeat class and quiz problems word for word: the CDF of [[PR03 Discrete Random Variables and Distributions]] §1, and the buses of 2024 Quiz 3.

## Mid-semester examination (25 September 2025)

> [!question] Q1 · Three people each toss a coin; the game ends when one outcome differs from the other two. Probability it ends on the first round with fair coins? With $P(H)=\tfrac14$?

> [!example]- Solution
> The round fails only if all three agree. Fair: $1-2(\tfrac12)^3=\mathbf{\tfrac34}$. Biased: $1-(\tfrac14)^3-(\tfrac34)^3=1-\tfrac1{64}-\tfrac{27}{64}=\mathbf{\tfrac9{16}}$. Bias makes "all tails" likely, so the game is *less* likely to end.

> [!question] Q2 · 100 students; Spanish 28, French 26, German 16; S∩F 12, S∩G 4, F∩G 6, all three 2. (a) $P(\text{no class})$; (b) $P(\text{exactly one})$; (c) two distinct students: $P(\text{at least one takes a class})$.

> [!example]- Solution ([[PR01 Counting and the Axioms of Probability]])
> $|S\cup F\cup G|=28+26+16-12-4-6+2=50$.
> (a) $50/100=\mathbf{\tfrac12}$.
> (b) Only-S $=28-12-4+2=14$, only-F $=26-12-6+2=10$, only-G $=16-4-6+2=8$. In each case the triple overlap is subtracted twice, so it is added back once. Total $32$: $\mathbf{0.32}$.
> (c) The complement is that both are among the 50 non-takers: $1-\binom{50}2/\binom{100}2=1-\tfrac{1225}{4950}=\mathbf{\tfrac{149}{198}}=0.7525$. (Without replacement, so $\ne1-\tfrac14$.)

> [!question] Q3 · Urn with $b$ black, $r$ red; the drawn ball is returned with $c$ more of its colour (Pólya). Show $P(\text{first black}\mid\text{second red})=b/(b+r+c)$.

> [!example]- Solution ([[PR02 Conditional Probability Bayes Rule and Independence]])
> $P(R_2)=\frac b{b+r}\cdot\frac r{b+r+c}+\frac r{b+r}\cdot\frac{r+c}{b+r+c}=\frac{r(b+r+c)}{(b+r)(b+r+c)}=\frac r{b+r}$: the second draw is red with the same probability as the first (exchangeability). Then
> $$P(B_1\mid R_2)=\frac{P(R_2\mid B_1)P(B_1)}{P(R_2)}=\frac{\frac r{b+r+c}\cdot\frac b{b+r}}{\frac r{b+r}}=\frac b{b+r+c}.\ ∎$$
> The reading: a red second ball is mild evidence that the first was red, which would have added $c$ reds, so the posterior for black falls from $\frac b{b+r}$ to $\frac b{b+r+c}$.

> [!question] Q4 · The CDF $F$ jumps to $\tfrac12,\tfrac35,\tfrac45,\tfrac9{10},1$ at $0,1,2,3,3.5$. Find the pmf.

> [!example]- Solution
> Each jump is a probability: $p(0)=\tfrac12$, $p(1)=\tfrac1{10}$, $p(2)=\tfrac15$, $p(3)=\tfrac1{10}$, $p(3.5)=\tfrac1{10}$ (sum 1). The same example is worked in [[PR03 Discrete Random Variables and Distributions]] §1.

> [!question] Q5 · One ticket in each of 50 independent lotteries, each winning with probability $1/100$. Approximate $P(\text{exactly 2 wins})$ and $P(\ge2)$.

> [!example]- Solution ([[PR03 Discrete Random Variables and Distributions]])
> Bin$(50,0.01)\approx$ Poisson$(0.5)$, with many trials each of small probability. (a) $e^{-0.5}\frac{0.5^2}2=\mathbf{0.0758}$ (exact binomial 0.0756). (b) $1-e^{-0.5}(1+0.5)=\mathbf{0.0902}$ (exact 0.0894).

> [!question] Q6 · Teams A (win probability $p$) and B play until one wins 4 games. Expected number of games?

> [!example]- Solution
> The series ends at game $n$ ($4\le n\le7$) if the winner takes game $n$ and exactly 3 of the first $n-1$: $P(N=n)=\binom{n-1}3\big[p^4q^{n-4}+q^4p^{n-4}\big]$. So
> $$E[N]=\sum_{n=4}^7n\binom{n-1}3\big[p^4q^{n-4}+q^4p^{n-4}\big].$$
> For $p=\tfrac12$ this is $\tfrac{93}{16}=5.8125$; for $p=0.6$, $5.697$; for $p=0.7$, $5.378$. Lopsided series end sooner.

> [!question] Q7 · Buses with 40, 33, 25, 50 students: $E[X]$ for a random student's bus, $E[Y]$ for a random driver's.

> [!example]- Solution
> $E[Y]=37$, $E[X]=\sum n^2/148=39.28$. A random student is more likely to be on a big bus; see [[MT2113 Past Papers 2024 - Solved|2024]] Quiz 3.

## End-semester examination (25 November 2025)

> [!question] Q1 · $Y=X^3+4$. (a) $F_Y(y)=F_X((y-4)^{1/3})$; (b) $f_Y(y)=f_X((y-4)^{1/3})\cdot\tfrac13(y-4)^{-2/3}$; (c) deduce $E(Y)=\int(x^3+4)f_X(x)\,dx$.

> [!example]- Solution ([[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]])
> (a) $x\mapsto x^3+4$ is strictly increasing on $\mathbb R$, so $Y\le y\iff X\le(y-4)^{1/3}$ (the real cube root, defined for negative arguments too): $F_Y(y)=F_X((y-4)^{1/3})$.
> (b) Chain rule, valid for $y\ne4$, where the cube root has an infinite slope; a single point does not affect a density.
> (c) $E(Y)=\int y\,f_Y(y)\,dy$. Substitute $y=x^3+4$, so $dy=3x^2dx$ and $(y-4)^{-2/3}=x^{-2}$:
> $$\int(x^3+4)f_X(x)\,\tfrac13x^{-2}\cdot3x^2\,dx=\int(x^3+4)f_X(x)\,dx .$$
> This is the "law of the unconscious statistician" for this $g$. ∎

> [!question] Q2 · $X\sim\text{Exp}(2)$, $Y\sim\text{Exp}(8)$ independent, $M=\min$. Joint density, CDF, density and mean of $M$.

> [!example]- Solution ([[PR08 Order Statistics and the Multinomial Distribution]])
> $f(x,y)=16e^{-2x-8y}$ on $x,y>0$. $P(M>m)=e^{-2m}e^{-8m}$, so $F_M(m)=1-e^{-10m}$, $f_M=10e^{-10m}$, $E[M]=\tfrac1{10}$. The minimum of independent exponentials is exponential with the **sum of the rates**: two clocks racing ring at the combined rate.

> [!question] Q3 · $A,B$ i.i.d. $U[0,1]$. (a) $P(|A-B|\le\tfrac12)$. (b) Density of $|A-B|$.

> [!example]- Solution
> (a) The complement is two corner triangles of the unit square, each of area $\tfrac12(\tfrac12)^2$: $P=1-\tfrac14=\mathbf{\tfrac34}$.
> (b) $P(|A-B|>z)=(1-z)^2$ (the two triangles of legs $1-z$), so $F(z)=1-(1-z)^2$ and $f(z)=2(1-z)$ on $[0,1]$: small differences are the most likely.

> [!question] Q4 · $f(x,y)=ce^{-y}$ on $0\le x\le y\le1$. (a) $c$; (b) $f_X$; (c) $P(Y<\tfrac12\mid X<\tfrac12)$.

> [!example]- Solution ([[PR04 Joint Distributions Expectation and Variance]])
> (a) $\int_0^1\!\int_0^yce^{-y}dx\,dy=c\int_0^1ye^{-y}dy=c(1-2e^{-1})$, so $c=\dfrac{e}{e-2}=3.784$.
> (b) $f_X(x)=c\int_x^1e^{-y}dy=c(e^{-x}-e^{-1})$ for $0\le x\le1$.
> (c) Since $X\le Y$, the event $\{Y<\tfrac12\}$ is contained in $\{X<\tfrac12\}$, so the ratio is $P(Y<\tfrac12)/P(X<\tfrac12)$:
> $$\frac{c\int_0^{1/2}ye^{-y}dy}{c\int_0^{1/2}(e^{-x}-e^{-1})dx}=\frac{1-\tfrac32e^{-1/2}}{1-e^{-1/2}-\tfrac12e^{-1}}=\mathbf{0.4305}.$$

> [!question] Q5 · Scores have mean 70, variance 16. (a) Chebyshev bound for $P(62<\text{score}<78)$. (b) By the CLT, how many students for $P(|\bar X-70|\le2)\ge0.95$? ($\Phi(1.96)=0.975$.)

> [!example]- Solution ([[PR06 Moments Generating Functions and Limit Theorems]])
> (a) $P(|X-70|\ge8)\le16/64=\tfrac14$, so $P(62<X<78)\ge\mathbf{\tfrac34}$.
> (b) $\bar X\approx N(70,16/n)$. Then $P(|\bar X-70|\le2)\approx2\Phi(2\sqrt n/4)-1\ge0.95$ needs $\sqrt n/2\ge1.96$, i.e. $n\ge15.37$: **$n=16$**.
