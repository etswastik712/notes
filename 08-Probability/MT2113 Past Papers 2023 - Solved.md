---
title: MT2113 Past Papers 2023 - Solved
aliases: [Probability midsem 2023, Probability endsem 2023, MT2113 2023, probability past paper 2023]
subject: probability
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/probability, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# MT2113 Introduction to Probability: Mid-sem and End-sem 2023, Solved

[[Probability - Course Map|Course Map]] · [[Probability Quiz Prep]] · other years: [[MT2113 Past Papers 2022 - Solved|2022]] · [[MT2113 Past Papers 2024 - Solved|2024]] · [[MT2113 Past Papers 2025 - Solved|2025]] · [[MT2113 MCQ Paper (undated) - Solved|undated MCQ paper]]

<span class="scope-taught">taught · past papers (Moumanti Podder, Kaneenika Sinha)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive archive (`qp-archive/MT2113/`):
> - **Mid-sem**, 21 Sep 2023, 50 points: `probability_midsem_2023_moumanti_compressed.pdf`.
> - **End-sem**, 22 Nov 2023, 60 points, five questions: `probability_endsem_2023_kaneenika_compressed.pdf`.
>
> Both are photographs read as images. Numbers are in `scripts/pr_qp_archive_numbers.py`.

## Mid-semester examination (21 September 2023)

> [!question] Q1 · $n$ people including $A$ and $B$. (a) In a random line, probability of exactly $r$ people between $A$ and $B$? (b) In a random circular arrangement, probability of exactly $r$ people on the clockwise arc from $A$ to $B$?

> [!example]- Solution ([[PR01 Counting and the Axioms of Probability]])
> **(a)** Only the pair of positions $(A,B)$ matters, and all $n(n-1)$ ordered pairs of distinct positions are equally likely, because every arrangement is. Exactly $r$ people between them means the positions are $i$ and $i+r+1$. There are $n-r-1$ choices of $i$, and $A$ can be on either side:
> $$P=\frac{2(n-r-1)}{n(n-1)},\qquad r=0,1,\dots,n-2 .$$
> (Check: summing over $r$ gives $\frac{2}{n(n-1)}\cdot\frac{(n-1)n}{2}=1$. For $n=10$, $r=3$: $0.1333$, and a simulation gives $0.1326$.)
> **(b)** (The paper says "these $r$ people"; it means the $n$ people.) Rotations do not count, so fix $A$'s seat. $B$ is then equally likely to be in any of the other $n-1$ seats. Exactly $r$ people clockwise between them pins $B$ to the $(r+1)$-th seat clockwise:
> $$P=\frac1{n-1},\qquad r=0,\dots,n-2 .$$
> On a circle every gap is equally likely; on a line short gaps are more likely, because there are more ways to place a short gap.

> [!question] Q2 · $P(n\text{ children})=\alpha p^n$ ($n\ge1$); all sex distributions equally likely. For $k\ge1$, find $P(\text{exactly }k\text{ girls})$.

> [!example]- Solution ([[PR02 Conditional Probability Bayes Rule and Independence]], [[PR03 Discrete Random Variables and Distributions]])
> Total probability over the family size $n\ge k$: given $n$ children, the number of girls is Bin$(n,\tfrac12)$, so
> $$P(k\text{ girls})=\sum_{n\ge k}\alpha p^n\binom nk2^{-n}=\alpha\sum_{n\ge k}\binom nk\Big(\frac p2\Big)^n .$$
> The hint's negative binomial gives the sum. Since $\sum_{n\ge k}\binom nkx^{n-k}(1-x)^{k+1}=1$ is the total probability of a negative binomial, $\sum_{n\ge k}\binom nkx^n=\dfrac{x^k}{(1-x)^{k+1}}$ for $0<x<1$. With $x=p/2$:
> $$\boxed{P(k\text{ girls})=\frac{\alpha\,(p/2)^k}{(1-p/2)^{k+1}}=\frac{2\alpha p^k}{(2-p)^{k+1}}},\qquad k\ge1 .$$
> (Numerically, $\alpha=0.3$, $p=0.6$: the series and the closed form agree, 0.183673, 0.078717, 0.033736 for $k=1,2,3$.) The $k=0$ case also needs $p_0$, which is why the question asks only for $k\ge1$.

> [!question] Q3 · Die $A$ has 4 red faces, die $B$ 2. A fair coin chooses the die once; it is then thrown repeatedly. (a) Show $P(\text{red on each throw})=\tfrac12$. (b) Given the first two throws are red, probability the third is red?

> [!example]- Solution ([[PR02 Conditional Probability Bayes Rule and Independence]])
> (a) $P(R_i)=\tfrac12\cdot\tfrac46+\tfrac12\cdot\tfrac26=\tfrac12$ for every throw $i$.
> (b) The throws are independent **given the die**, but not unconditionally, because two reds are evidence that die $A$ was chosen.
> $$P(R_3\mid R_1R_2)=\frac{P(R_1R_2R_3)}{P(R_1R_2)}=\frac{\frac12(\frac23)^3+\frac12(\frac13)^3}{\frac12(\frac23)^2+\frac12(\frac13)^2}=\frac{9/27}{5/9}=\mathbf{\tfrac35}.$$
> It is above $\tfrac12$ for exactly that reason: after two reds, $P(A\mid R_1R_2)=\tfrac45$.

> [!question] Q4 · (a) 10 balls into 5 boxes independently, box $i$ with probability $p_i$: expected number of empty boxes. (b) $k$ coupon types with probabilities $p_i$: expected number of distinct types among $n$ coupons.

> [!example]- Solution ([[PR04 Joint Distributions Expectation and Variance]])
> **Indicators** turn a hard count into a sum of easy probabilities, using linearity of expectation.
> (a) $E[\#\text{empty}]=\sum_{i=1}^5P(\text{box }i\text{ empty})=\sum_{i=1}^5(1-p_i)^{10}$.
> (b) $E[\#\text{distinct}]=\sum_{i=1}^kP(\text{type }i\text{ appears})=\sum_{i=1}^k\big[1-(1-p_i)^n\big]$.
> The indicators are dependent, but linearity does not need independence.

> [!question] Q5 · (a) For $X\in\{0,1,2,\dots\}$, $E[X]=\sum_{i\ge1}P(X\ge i)$. (b) $X\sim\text{Bin}(n,p)$: $E\big[\frac1{X+1}\big]=\frac{1-(1-p)^{n+1}}{(n+1)p}$.

> [!example]- Solution ([[PR04 Joint Distributions Expectation and Variance]])
> (a) Write $X=\sum_{i\ge1}\mathbf 1\{X\ge i\}$ (the integer $X$ counts how many of $1,2,\dots$ are $\le X$). All terms are non-negative, so expectation can be taken term by term: $E[X]=\sum_{i\ge1}P(X\ge i)$. ∎
> (b) Use $\frac1{k+1}\binom nk=\frac1{n+1}\binom{n+1}{k+1}$:
> $$E\Big[\frac1{X+1}\Big]=\sum_{k=0}^n\frac1{k+1}\binom nkp^kq^{n-k}=\frac1{(n+1)p}\sum_{j=1}^{n+1}\binom{n+1}{j}p^jq^{n+1-j}=\frac{1-q^{n+1}}{(n+1)p},$$
> where the last sum is the Bin$(n+1,p)$ total minus its $j=0$ term $q^{n+1}$. (Check $n=7$, $p=0.35$: both sides 0.345763.) ∎

## End-semester examination (22 November 2023)

> [!question] 1(a) · $f(x,y)=c$ on $x^2+y^2\le\tfrac12$. Find $c$.

> [!example]- Solution
> The disc has radius $1/\sqrt2$ and area $\pi/2$, so $c=\mathbf{2/\pi}$.

> [!question] 1(b) · $X\sim N(1,4)$: express $P((X-1)^2<16)$ with $\Phi$.

> [!example]- Solution
> $(X-1)^2<16\iff|X-1|<4\iff|Z|<2$ with $Z=(X-1)/2$. So $P=2\Phi(2)-1\approx0.9545$.

> [!question] 1(c) · $f(x)=x^2/3$ on $(-2,1)$. Density of $Y=-2X$?

> [!example]- Solution ([[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]])
> $Y=-2X$ is decreasing, maps $(-2,1)$ onto $(-2,4)$, and $X=-Y/2$, $|dx/dy|=\tfrac12$:
> $$f_Y(y)=f_X(-y/2)\cdot\tfrac12=\frac{y^2/4}{3}\cdot\frac12=\frac{y^2}{24},\qquad-2<y<4,$$
> and 0 otherwise. Check: $\int_{-2}^4y^2/24\,dy=(64+8)/72=1$.

> [!question] 1(d) · $f(x,y)=\tfrac12$ on $[0,2]\times[0,1]$. Marginals; independent?

> [!example]- Solution
> $f_X(x)=\int_0^1\tfrac12dy=\tfrac12$ on $[0,2]$; $f_Y(y)=\int_0^2\tfrac12dx=1$ on $[0,1]$. Since $f_Xf_Y=\tfrac12=f$ everywhere, **independent**. A constant density on a rectangle always factors.

> [!question] 2 · Announcements form a Poisson process of rate $\lambda$ per day. (a) $P(\text{none in 2 days})$; (b) $P(\ge2\text{ in 4 days})$; (c) density of the gap $T_n$; (d) mean time for 20 announcements.

> [!example]- Solution ([[PR05 Continuous Random Variables]])
> (a) The count in 2 days is Poisson$(2\lambda)$: $e^{-2\lambda}$.
> (b) $1-e^{-4\lambda}-4\lambda e^{-4\lambda}$.
> (c) $P(T_n>t)=P(\text{no event in a window of length }t)=e^{-\lambda t}$, because counts in disjoint windows are independent with the same law. So $f_{T_n}(t)=\lambda e^{-\lambda t}$, $t>0$.
> (d) The 20th arrival time is $T_1+\dots+T_{20}$, mean $20/\lambda$ days.

> [!question] 3 · $X\sim\text{Exp}(\lambda)$, $Y\sim\text{Exp}(\mu)$ independent; $U=\min$, $V=\max$. (a) densities of $U,V$; (b) are $X$ and $W=V+U$ independent?

> [!example]- Solution ([[PR08 Order Statistics and the Multinomial Distribution]])
> (a) $P(U>u)=P(X>u)P(Y>u)=e^{-(\lambda+\mu)u}$, so $f_U(u)=(\lambda+\mu)e^{-(\lambda+\mu)u}$. $P(V\le v)=(1-e^{-\lambda v})(1-e^{-\mu v})$, so
> $f_V(v)=\lambda e^{-\lambda v}+\mu e^{-\mu v}-(\lambda+\mu)e^{-(\lambda+\mu)v}$, $v>0$.
> (b) $\max+\min$ of two numbers is their sum, so $W=X+Y$. **Not independent**: $\operatorname{Cov}(X,X+Y)=\operatorname{Var}X=1/\lambda^2\ne0$. (Or: $W\ge X$ always, so $P(X>a,W<a)=0$ while both events have positive probability.)

> [!question] 4 · $X\sim\text{Gamma}(n,1)$. (a) Approximate $P(|X/n-1|>0.01)$ with $\Phi$. (b) How large must $n$ be for this to be $<0.01$? ($\Phi^{-1}(0.005)\approx-2.5758$.)

> [!example]- Solution ([[PR06 Moments Generating Functions and Limit Theorems]])
> Gamma$(n,1)$ is a sum of $n$ independent Exp$(1)$, with mean $n$ and variance $n$. By the CLT, $(X-n)/\sqrt n\approx N(0,1)$, so
> $$P\Big(\Big|\frac Xn-1\Big|>0.01\Big)=P\Big(\frac{|X-n|}{\sqrt n}>0.01\sqrt n\Big)\approx2\Phi(-0.01\sqrt n).$$
> (b) $2\Phi(-0.01\sqrt n)<0.01\iff\Phi(-0.01\sqrt n)<0.005\iff0.01\sqrt n>2.5758\iff n>(257.58)^2=66\,347.5$. So $n\ge\mathbf{66\,348}$. A 1 % relative accuracy at 99 % confidence costs tens of thousands of terms, because the error shrinks only as $1/\sqrt n$.

> [!question] 5 · True or false, with reason.

> [!example]- Solution
> - **(a) False.** If $X\sim U[0,1]$ then $P(X^2\le t)=P(X\le\sqrt t)=\sqrt t\ne t$; $X^2$ piles up near 0.
> - **(b) True.** A linear function of a normal is normal; $E=1$, $\operatorname{Var}=4$.
> - **(c) True.** Memorylessness: $P(X>5\mid X>2)=P(X>3)=e^{-3\lambda}$.
> - **(d) True.** $E[X^2]=\operatorname{Var}X+(EX)^2=\sigma^2+0$.
> - **(e) True.** $p_X(u_i)=\sum_jp_{X,Y}(u_i,v_j)$, a sum of non-negative terms, so it is at least each single term.
> - **(f) False.** Densities are not probabilities and can exceed the marginal. For $(X,Y)$ uniform on $[0,1]\times[0,\tfrac12]$, $f_{X,Y}=2$ while $f_X(u)=\int_0^{1/2}2\,dv=1$. The discrete argument of (e) fails because the marginal is an *integral* over $v$, not a sum, so it can be smaller than the integrand.
