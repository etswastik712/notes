---
title: MT2113 Past Papers 2022 - Solved
aliases: [Probability midsem 2022, Probability endsem 2022, MT2113 2022, probability past paper 2022]
subject: probability
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/probability, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# MT2113 Introduction to Probability: Mid-sem and End-sem 2022, Solved

[[Probability - Course Map|Course Map]] · [[Probability Quiz Prep]] · other years: [[MT2113 Past Papers 2023 - Solved|2023]] · [[MT2113 Past Papers 2024 - Solved|2024]] · [[MT2113 Past Papers 2025 - Solved|2025]] · [[MT2113 MCQ Paper (undated) - Solved|undated MCQ paper]]

<span class="scope-taught">taught · past papers (Fall 2022, Mainak Poddar)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> Drive **Question Paper Archive → Sem-3 → MT2113**, now in `math/probability/lecture-notes-slides/past-papers/qp-archive/MT2113/`:
> - **Mid-sem**, 28 Sep 2022, 40 marks, 2 h: `MT2113_midsem_22.pdf`. `Probability_Midsem_Aug22_Mainak.pdf` is a second photograph of the same paper.
> - **End-sem**, 28 Nov 2022, instructor Mainak Poddar, any 5 of 6 questions × 8 points: `MT2113_endsem_22.pdf`, with `Probability_Endsem_Aug22_Mainak.pdf` again a second copy.
>
> Both are scans; I read them as images. Every number below is recomputed in `scripts/pr_qp_archive_numbers.py`.

## Mid-semester examination (28 September 2022)

### Section A (2 marks each)

> [!question] A1 · $X\sim\text{Poisson}(2)$. Find $P(X=3)$.

> [!example]- Solution ([[PR03 Discrete Random Variables and Distributions]])
> $P(X=3)=e^{-2}\dfrac{2^3}{3!}=\dfrac43e^{-2}=\mathbf{0.1804}$.

> [!question] A2 · If $P(B)>0$, is $P(A\mid B)\ge P(A)$ always true? Justify with an example.

> [!example]- Solution ([[PR02 Conditional Probability Bayes Rule and Independence]])
> **No.** Conditioning can lower a probability as well as raise it. Roll a fair die, $A=\{1\}$, $B=\{2,4,6\}$: $P(A)=\tfrac16$ but $P(A\mid B)=P(A\cap B)/P(B)=0$. Whenever $A$ and $B$ are disjoint with $P(A)>0$, learning $B$ rules $A$ out.

> [!question] A3 · How many arrangements of the word COFFEE?

> [!example]- Solution ([[PR01 Counting and the Axioms of Probability]])
> Six letters with F and E each repeated twice. Swapping the two F's (or the two E's) gives the same word, so divide $6!$ by $2!\,2!$: $\dfrac{720}{4}=\mathbf{180}$.

> [!question] A4 · A fair coin is tossed five times. Probability of a head on the last toss?

> [!example]- Solution
> $\mathbf{\tfrac12}$. The tosses are independent, so the first four outcomes carry no information about the fifth. Counting confirms it: of the $2^5$ equally likely sequences, the $2^4$ ending in H are exactly half.

> [!question] A5 · Write the CDF of a Geometric$(\tfrac12)$ random variable.

> [!example]- Solution ([[PR03 Discrete Random Variables and Distributions]])
> With $X$ = number of trials up to and including the first success on $\{1,2,\dots\}$, $P(X>k)=(1-p)^k$ (the first $k$ trials all fail). So
> $$F(x)=\begin{cases}0,&x<1\\1-\left(\tfrac12\right)^{\lfloor x\rfloor},&x\ge1.\end{cases}$$
> It is a step function, right-continuous, jumping by $(\tfrac12)^k$ at $x=k$. (If your class used the "failures before the first success" convention on $\{0,1,\dots\}$, replace $\lfloor x\rfloor$ by $\lfloor x\rfloor+1$ for $x\ge0$; state which convention you use.)

### Section B (5 marks each)

> [!question] B1 · $X\sim\text{Bin}(n,p)$ with $E[X]=6$, $\operatorname{Var}(X)=2.4$. Find $n,p$.

> [!example]- Solution
> $np=6$ and $np(1-p)=2.4$. Dividing, $1-p=0.4$, so $\mathbf{p=0.6}$ and $\mathbf{n=10}$.

> [!question] B2 · 30 % of girls and 25 % of boys get grade A; 60 % of the class are girls. Given a student got an A, probability the student is a girl?

> [!example]- Solution ([[PR02 Conditional Probability Bayes Rule and Independence]])
> Bayes with the partition {girl, boy}:
> $$P(G\mid A)=\frac{0.30\times0.6}{0.30\times0.6+0.25\times0.4}=\frac{0.18}{0.28}=\frac9{14}=\mathbf{0.643}.$$
> The posterior (0.643) is above the prior (0.6) because an A is a little likelier among girls.

> [!question] B3 · $P(X=1)=1-P(X=0)\in(0,1)$ and $E[X]=3\operatorname{Var}(X)$. Find $P(X=0)$.

> [!example]- Solution
> $X$ is Bernoulli$(p)$ with $p=P(X=1)$: $E[X]=p$, $\operatorname{Var}(X)=p(1-p)$. So $p=3p(1-p)$, and since $p\ne0$, $1=3(1-p)$, $p=\tfrac23$. Hence $P(X=0)=\mathbf{\tfrac13}$.

> [!question] B4 · $X_1\sim\text{Poisson}(\lambda_1)$, $X_2\sim\text{Poisson}(\lambda_2)$ independent. Show $X_1+X_2\sim\text{Poisson}(\lambda_1+\lambda_2)$.

> [!example]- Solution ([[PR07 Sums of Independent Variables Covariance and Correlation]])
> Split $\{X_1+X_2=n\}$ according to the value $k$ of $X_1$. The pieces are disjoint, and independence lets the joint probability factor:
> $$P(X_1+X_2=n)=\sum_{k=0}^n\frac{e^{-\lambda_1}\lambda_1^k}{k!}\cdot\frac{e^{-\lambda_2}\lambda_2^{n-k}}{(n-k)!}=\frac{e^{-(\lambda_1+\lambda_2)}}{n!}\sum_{k=0}^n\binom nk\lambda_1^k\lambda_2^{n-k}=\frac{e^{-(\lambda_1+\lambda_2)}(\lambda_1+\lambda_2)^n}{n!},$$
> by the binomial theorem. That is the Poisson$(\lambda_1+\lambda_2)$ pmf. ∎

### Section C (5 marks each)

> [!question] C1 · $X\sim\text{Geo}(\alpha)$, $Y\sim\text{Geo}(\beta)$ independent. Show $P(X+Y=n)=\dfrac{\alpha\beta}{\alpha-\beta}[(1-\alpha)^{n-1}-(1-\beta)^{n-1}]$ for $n\ge2$.

> [!example]- Solution ([[PR07 Sums of Independent Variables Covariance and Correlation]])
> Write $a=1-\alpha$, $b=1-\beta$ and assume $\alpha\ne\beta$. Condition on $X=k$, which ranges over $1,\dots,n-1$ because $Y\ge1$:
> $$P(X+Y=n)=\sum_{k=1}^{n-1}\alpha a^{k-1}\,\beta b^{n-k-1}=\alpha\beta\sum_{k=1}^{n-1}a^{k-1}b^{n-1-k}=\alpha\beta\,\frac{b^{n-1}-a^{n-1}}{b-a},$$
> using $\sum_{j=0}^{m-1}a^jb^{m-1-j}=(b^m-a^m)/(b-a)$ with $m=n-1$. Since $b-a=\alpha-\beta$,
> $$P(X+Y=n)=\frac{\alpha\beta}{\alpha-\beta}\big[(1-\beta)^{n-1}-(1-\alpha)^{n-1}\big]=\frac{\alpha\beta}{\beta-\alpha}\big[(1-\alpha)^{n-1}-(1-\beta)^{n-1}\big].$$
>
> [!warning] Sign slip in the printed paper
> As printed, $\frac{\alpha\beta}{\alpha-\beta}[(1-\alpha)^{n-1}-(1-\beta)^{n-1}]$ is **negative**. Take $\alpha>\beta$: then $1-\alpha<1-\beta$, so the bracket is negative while $\alpha-\beta>0$. The second photograph has the denominator corrected by hand to $\beta-\alpha$, which is the form derived above. Numerically ($\alpha=0.3$, $\beta=0.55$) the direct sum and the corrected formula agree: 0.165000 ($n=2$), 0.189750 ($n=3$), 0.098747 ($n=6$). For $\alpha=\beta$ the formula is $0/0$; the sum is then $(n-1)\alpha^2(1-\alpha)^{n-2}$, the negative binomial.

> [!question] C2 · $X,Y$ independent on $\mathbb N$; $f,g:\mathbb N\to[0,\infty)$. Show $E[f(X)g(Y)]=E[f(X)]E[g(Y)]$.

> [!example]- Solution ([[PR04 Joint Distributions Expectation and Variance]])
> $$E[f(X)g(Y)]=\sum_{i,j}f(i)g(j)P(X=i,Y=j)=\sum_{i,j}f(i)P(X=i)\,g(j)P(Y=j)=\Big(\sum_if(i)P(X=i)\Big)\Big(\sum_jg(j)P(Y=j)\Big).$$
> The middle step is independence. The last step splits a double sum into a product. That is legitimate because every term is $\ge0$ (that is why $f,g\ge0$ is assumed): a double series of non-negative terms can be summed in any order, even when it diverges. ∎ (The paper's "$E[G(Y)]$" is a typo for $E[g(Y)]$.)

## End-semester examination (28 November 2022; any 5 of 6)

> [!question] 1(a) · A dart hits a board of radius 10 uniformly. $R$ = distance from the centre. Find $P(4\le R\le6)$.

> [!example]- Solution ([[PR05 Continuous Random Variables]])
> "Uniform on the board" means probability is proportional to **area**, not to radius. $P(R\le r)=\pi r^2/(\pi\,10^2)=r^2/100$, so $P(4\le R\le6)=(36-16)/100=\mathbf{0.2}$. (The tempting answer $2/10$ from "uniform in $r$" happens to coincide here; for $P(0\le R\le2)$ it would give 0.2 against the correct 0.04.)

> [!question] 1(b) · $X$ has density $f$. Express the density of $e^X$ in terms of $f$.

> [!example]- Solution ([[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]])
> $Y=e^X>0$. For $y>0$: $F_Y(y)=P(X\le\ln y)=F_X(\ln y)$, and differentiating gives $f_Y(y)=\dfrac{f(\ln y)}{y}$. For $y\le0$, $f_Y(y)=0$.

> [!question] 1(c) · $X\sim\text{Exp}(\lambda)$: compute $E(X)$.

> [!example]- Solution
> $E(X)=\int_0^\infty x\lambda e^{-\lambda x}\,dx=\big[-xe^{-\lambda x}\big]_0^\infty+\int_0^\infty e^{-\lambda x}dx=\mathbf{1/\lambda}$ (by parts).

> [!question] 1(d) · $X\sim N(\mu,\sigma^2)$: $P(|X-\mu|\le2\sigma)$ to 2 decimals.

> [!example]- Solution
> $=P(|Z|\le2)=2\Phi(2)-1=0.9545\approx\mathbf{0.95}$.

> [!question] 2 · $X,Y$ independent Uniform$[0,1]$. Are $X$ and $2X+Y$ independent?

> [!example]- Solution ([[PR07 Sums of Independent Variables Covariance and Correlation]])
> **No.** Exhibit two events whose joint probability does not factor. Let $A=\{X>\tfrac12\}$ and $B=\{2X+Y<1\}$. On $A$, $2X>1$, so $2X+Y>1$: $P(A\cap B)=0$. But $P(A)=\tfrac12$ and $P(B)=\int_0^{1/2}(1-2x)\,dx=\tfrac14$, so $P(A)P(B)=\tfrac18\ne0$. (Simulation: $P(A\cap B)=0$ against a product 0.125.) A second route: $\operatorname{Cov}(X,2X+Y)=2\operatorname{Var}X=\tfrac16\ne0$, and independent variables are uncorrelated.

> [!question] 3 · (a) Show $Z=(X-\mu)/\sigma$ is standard normal. (b) State the CLT.

> [!example]- Solution ([[PR06 Moments Generating Functions and Limit Theorems]])
> (a) $F_Z(z)=P(X\le\mu+\sigma z)=\int_{-\infty}^{\mu+\sigma z}\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}dx$. Substitute $u=(x-\mu)/\sigma$, $dx=\sigma\,du$: $F_Z(z)=\int_{-\infty}^z\frac1{\sqrt{2\pi}}e^{-u^2/2}du=\Phi(z)$. ∎
> (b) If $X_1,X_2,\dots$ are i.i.d. with mean $\mu$ and finite variance $\sigma^2>0$, then for every real $a$
> $$P\Big(\frac{X_1+\dots+X_n-n\mu}{\sigma\sqrt n}\le a\Big)\to\Phi(a)\quad(n\to\infty).$$

> [!question] 4 · (a) State Chebyshev. (b) 1000 independent bulb lifetimes, each exponential with mean 400. Lower bound for $P(300<\bar X<500)$.

> [!example]- Solution ([[PR06 Moments Generating Functions and Limit Theorems]])
> (a) If $E[X]=\mu$ and $\operatorname{Var}(X)=\sigma^2<\infty$, then for every $k>0$, $P(|X-\mu|\ge k)\le\sigma^2/k^2$.
> (b) Exponential with mean 400 has variance $400^2=1.6\times10^5$. By independence $\operatorname{Var}(\bar X)=1.6\times10^5/1000=160$, with $E[\bar X]=400$. Chebyshev with $k=100$: $P(|\bar X-400|\ge100)\le160/10^4=0.016$, so
> $$P(300<\bar X<500)\ge\mathbf{0.984}.$$
> (The true value is essentially 1: simulating 20 000 averages never left the interval. Chebyshev is crude but needs only the variance.)

> [!question] 5 · $X,Y$ independent with continuous densities. Density of $X-Y$?

> [!example]- Solution ([[PR07 Sums of Independent Variables Covariance and Correlation]])
> Condition on $Y=y$: $P(X-Y\le z)=\int_{-\infty}^\infty P(X\le z+y)f_Y(y)\,dy=\int F_X(z+y)f_Y(y)\,dy$. Differentiate in $z$ (allowed for continuous densities):
> $$f_{X-Y}(z)=\int_{-\infty}^{\infty}f_X(z+y)\,f_Y(y)\,dy .$$
> This is the convolution of $f_X$ with the density $f_Y(-\,\cdot)$ of $-Y$.

> [!question] 6 · $X,Y$ i.i.d. Uniform$[0,1]$, $M=\max(X,Y)$. Find $f_{X\mid M=m}(x)$.

> [!example]- Solution ([[PR08 Order Statistics and the Multinomial Distribution]])
> Given $M=m$, either $X$ *is* the maximum ($X=m$) or $Y$ is and $X<m$. By symmetry each happens with probability $\tfrac12$. In the second case $X$ is just "uniform conditioned to be below $m$", i.e. uniform on $[0,m)$. So the conditional law of $X$ is a **mixture**:
> $$P(X=m\mid M=m)=\tfrac12,\qquad f_{X\mid M=m}(x)=\frac{1}{2m}\ \ (0\le x<m),\qquad 0\ \ (x>m).$$
> Check: the continuous part integrates to $\tfrac12$, the atom adds $\tfrac12$. Simulation with $M\approx0.6$: $X=M$ in 50.2 % of cases, and the mean of $X$ given $X<M$ is 0.296 (theory 0.3).
>
> [!pitfall] The "pdf" in the question
> The conditional law has an **atom** at $x=m$, so it has no pure density. An answer that gives only $1/m$ on $[0,m]$ (forgetting that $X$ can be the maximum) integrates to 1 but is wrong. One way to write it: $\frac1{2m}\mathbf 1_{[0,m)}(x)+\frac12\delta(x-m)$.
