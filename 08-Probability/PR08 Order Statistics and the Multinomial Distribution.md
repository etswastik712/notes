---
title: PR08 Order Statistics and the Multinomial Distribution
aliases: [PR08, order statistics, min and max, joint density of order statistics, exponential order statistics, multinomial distribution, multinomial covariance, MT2113 homework 5, HW5]
subject: probability
type: chapter
chapter: 8
part: V
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
prereq: [PR04 Joint Distributions Expectation and Variance, PR05 Continuous Random Variables, PR07 Sums of Independent Variables Covariance and Correlation]
tags: [subject/probability, type/chapter, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# PR08 · Order Statistics and the Multinomial Distribution

◀ [[PR07 Sums of Independent Variables Covariance and Correlation]] · [[Probability - Course Map]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Scope of this chapter
> **Added 2026-11-07.** The instructor posted **Homework 5** ([[hw5.pdf#page=1|the sheet]], two handwritten pages, three problems) and, separately, a handwritten **solution of Problem 1** ([[HW-5, Q.1.jpg|the instructor's Q1 solution]]). No chapter covered **order statistics** (the joint law of the sorted sample) or the **multinomial distribution as a random vector**; so this is a **new chapter**, not extra Practice items (new-material rule: compare first, add a chapter only for uncovered topics). The sheet is the only taught source: it announces "lecture notes on the weekend" which are **not in the folder**; Problem 2(a) and 2(e) are marked "done in class". Everything beyond the three problems (the general-$n$ formulas, the Rényi gaps, Poissonisation) is **mine** (extra · beyond), verified by simulation and exact enumeration in `scripts/pr08_numbers.py`; no book was consulted for this chapter. Overlap with earlier chapters is deliberate and small: the memoryless property and $\min\sim\mathrm{Expo}(2\lambda)$ ([[PR05 Continuous Random Variables]], HW2), indicators and covariance ([[PR04 Joint Distributions Expectation and Variance]]), covariance matrices ([[PR07 Sums of Independent Variables Covariance and Correlation]] §5).

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught: Homework 5)**
> - §1 **Problem 1**: the joint density of $(\min,\max)$ of two iid variables, $f_{Y_1,Y_2}(y_1,y_2)=2f(y_1)f(y_2)$ for $y_1<y_2$, by the two-preimages picture (the sheet's diagram) **and** by the joint cdf (the instructor's solution); the general statement $n!\,f(y_1)\cdots f(y_n)$ on $y_1<\dots<y_n$ (stated on the sheet)
> - §3 **Problem 2**: $Y_1\sim\mathrm{Expo}(2\lambda)$ (done in class), the change of variables $(Y_1,Y_2)\to(Y_1,Y_2-Y_1)$, $Y_2-Y_1\sim\mathrm{Expo}(\lambda)$, independence of $Y_1$ and $Y_2-Y_1$, the variance and the correlation $1/\sqrt5$
> - §4 **Problem 3**: the multinomial vector via trial indicators $Y_{ij}$; $E,\mathrm{Var}$, $\mathrm{Cov}(X_i,X_k)=-np_ip_k$ and the covariance matrix $n\,\mathrm{diag}(p)-n\,pp^{\mathsf T}$
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 the density of the **$k$-th order statistic** for general $n$ and its Beta form for uniforms; §3 the **Rényi gaps** for $n$ exponentials; §4 rank of the multinomial covariance matrix, conditional laws, **Poissonisation**; the reliability reading of Problem 2

> [!key] After this chapter you can
> - derive $f_{Y_1,Y_2}=2f(y_1)f(y_2)$ in two ways and extend it to $n!\prod f(y_i)$,
> - write down the density of the $k$-th smallest of $n$ iid variables,
> - show that for iid exponentials the minimum and the gap are **independent** exponentials, and compute $\mathrm{Var}(Y_2)$ and $\mathrm{Corr}(Y_1,Y_2)=1/\sqrt5$,
> - derive the multinomial means, variances, covariances and covariance matrix **from indicators**, and explain why the covariance is negative and the matrix singular.

> [!intuition] The one-sentence story
> Sorting a sample throws away *which* variable was which, and that costs exactly a factor $n!$ in the density: the sorted vector lives on the ordered region $y_1<\dots<y_n$, which has $1/n!$ of the volume of the cube, so the density there is $n!$ times the product. For exponentials sorting does something magical: waiting for the **first** of $n$ clocks, then (by the memoryless property) restarting the $n-1$ survivors, turns the order statistics into a **sum of independent exponentials**. The multinomial is the other face of "labelling": $k$ labels, $n$ independent trials, and the counts must **add up to $n$**, which is the whole reason their covariances are negative.

![[fig_pr08_order_multinomial.png]]
*A: the two preimages $(y_1,y_2)$, $(y_2,y_1)$ of a point of the ordered region (§1). B: for exponentials the minimum and the gap are independent (§3; 2500 samples, contours of the product density). C: the joint pmf of two multinomial counts, $n=10$, $p=(0.2,0.3,0.5)$, with the $2\sigma$ ellipse of $n(\mathrm{diag}\,p-pp^{\mathsf T})$ (§4). Numbers: `scripts/pr08_numbers.py`; `scripts/fig_pr08.py`.*

> [!tip] 🔬 Interactive: the $k$-th order statistic
> Open [[Assets/interactive/pr_order_statistics.html|▶ pr_order_statistics.html]] (self-contained, works offline). Choose a distribution (uniform, exponential, normal), $n$ and $k$: the thick curve is $\frac{n!}{(k-1)!(n-k)!}F^{k-1}(1-F)^{n-k}f$, the thin ones are the other order statistics, the histogram is a 4000-sample simulation; on the right the mean gaps between consecutive points, which for the exponential are exactly $1/(n-k+1)$.

## 1. Problem 1: the joint density of the minimum and the maximum
<span class="scope-taught">taught</span> *Source: HW5 Q1 and the instructor's solution*

Let $X_1,X_2$ be iid with pdf $f$ and cdf $F$, $Y_1=\min\{X_1,X_2\}$, $Y_2=\max\{X_1,X_2\}$.

> [!key] Problem 1 (HW5)
> For $y_1<y_2$: $\quad f_{Y_1,Y_2}(y_1,y_2)=2\,f(y_1)f(y_2)$, and $f_{Y_1,Y_2}=0$ for $y_1>y_2$.

**Proof 1: two preimages (the sheet's schematic).** A small rectangle $[y_1,y_1+dy_1]\times[y_2,y_2+dy_2]$ with $y_1<y_2$ in the $(y_1,y_2)$-plane is the image of **two** small rectangles of the $(x_1,x_2)$-plane: $\{x_1\approx y_1,\,x_2\approx y_2\}$ (where $x_1$ is the min) and $\{x_1\approx y_2,\,x_2\approx y_1\}$ (where $x_1$ is the max). They are disjoint (since $y_1\ne y_2$) and each has probability $f(y_1)f(y_2)\,dy_1dy_2$ (independence). Adding, $P(Y_1\in dy_1,Y_2\in dy_2)=2f(y_1)f(y_2)\,dy_1dy_2$. The map $(x_1,x_2)\mapsto(\min,\max)$ is a reflection on each half-plane (Jacobian $\pm1$), which is why only the number of preimages matters. $\square$

**Proof 2: the joint cdf (the instructor's solution, [[HW-5, Q.1.jpg]]).** For $y_1<y_2$,
$$F_{Y_1,Y_2}(y_1,y_2)=P(\min\le y_1,\ \max\le y_2)$$
$$=P(X_1\le y_1,X_2\le y_2)+P(X_2\le y_1,X_1\le y_2)-P(X_1\le y_1,\,X_2\le y_1,\,X_1\le y_2,\,X_2\le y_2)$$
(inclusion–exclusion on "$X_1\le y_1$ or $X_2\le y_1$"; the last event is $\{X_1\le y_1,X_2\le y_1\}$ because $y_1<y_2$), so
$$F_{Y_1,Y_2}(y_1,y_2)=2F(y_1)F(y_2)-F(y_1)^2,\qquad f_{Y_1,Y_2}=\frac{\partial^2F_{Y_1,Y_2}}{\partial y_1\partial y_2}=2f(y_1)f(y_2).\ \square$$
*Check (Expo(1), $y_1=0.5$, $y_2=1.2$):* the formula gives $0.39510$, a $2\times10^6$-sample simulation $0.39502$; the mixed second difference of the cdf is $0.365367=2e^{-0.5}e^{-1.2}$; $\iint_{y_1<y_2}2f\,f=1.000000$.

> [!key] The general statement (HW5, stated on the sheet)
> If $X_1,\dots,X_n$ are iid with density $f$ and $Y_1<\dots<Y_n$ is the sorted sample, then
> $$f_{Y_1,\dots,Y_n}(y_1,\dots,y_n)=n!\,f(y_1)\cdots f(y_n)\quad\text{for }y_1<y_2<\dots<y_n,$$
> and $0$ elsewhere. *Why:* the $n!$ orderings of the $n$ labels each map the ordered region from a different region of $\mathbb R^n$ with the same density $\prod f$ (the same two-preimage count: $n!$ preimages). *Check:* the ordered region has volume $1/n!$ in $[0,1]^n$ so $n!\cdot\frac1{n!}=1$ (total mass $1$).

## 2. The $k$-th order statistic 🔵
<span class="scope-extra-beyond">extra · beyond</span> *my derivation, checked by simulation*

Integrating the joint density gets the marginal of one coordinate, but a direct count is quicker. $Y_{(k)}\in dy$ means: exactly $k-1$ of the $n$ values lie below $y$ (probability $F(y)$ each), one lies in $dy$ (probability $f(y)dy$), and $n-k$ lie above ($1-F(y)$ each); the number of ways to choose the labels is the multinomial coefficient $\frac{n!}{(k-1)!\,1!\,(n-k)!}$:
$$\boxed{f_{Y_{(k)}}(y)=\frac{n!}{(k-1)!\,(n-k)!}\,F(y)^{k-1}\big(1-F(y)\big)^{n-k}f(y)}$$
For $k=1$: $nf(1-F)^{n-1}$ (the minimum); for $k=n$: $nF^{n-1}f$ (the maximum). **Uniform$(0,1)$:** $F(y)=y$, so $f_{Y_{(k)}}\propto y^{k-1}(1-y)^{n-k}$, i.e. $Y_{(k)}\sim\mathrm{Beta}(k,n-k+1)$ with mean $\frac k{n+1}$ (the $n$ points cut the unit interval into $n+1$ gaps of mean length $\frac1{n+1}$).

*Numbers* ($n=5$, $10^6$ samples): $E[Y_{(k)}]=1/6,2/6,3/6,4/6,5/6$ against simulated $0.1666,0.3332,0.5001,0.6667,0.8334$; $P(Y_{(2)}\le0.3)=0.47178$ (Beta(2,4)) against $0.47192$. The constant for $n=5,k=2$ is $\frac{5!}{1!3!}=20$ and $20y(1-y)^3$ integrates to $1.000000$.

## 3. Problem 2: exponential order statistics
<span class="scope-taught">taught</span> *Source: HW5 Q2* · <span class="scope-extra-beyond">extra · beyond</span> *Rényi gaps, reliability reading*

Let $X_1,X_2\sim\mathrm{Expo}(\lambda)$ be independent, $Y_1=\min$, $Y_2=\max$ ($\lambda=2$ in the numbers below).

> [!example] (a) $Y_1\sim\mathrm{Expo}(2\lambda)$ — done in class
> $P(Y_1>y)=P(X_1>y)P(X_2>y)=e^{-2\lambda y}$. (Simulation: $P(Y_1>0.3)=0.30130$ against $e^{-1.2}=0.30119$.) *Intuition:* two independent clocks tick; the first ring comes at rate $2\lambda$.

> [!example] (b) the joint density of $(Y_1,\,G=Y_2-Y_1)$
> From §1, $f_{Y_1,Y_2}(y_1,y_2)=2\lambda^2e^{-\lambda(y_1+y_2)}$ for $0<y_1<y_2$. The map $(y_1,y_2)\mapsto(y_1,g)=(y_1,y_2-y_1)$ is linear with Jacobian $\begin{vmatrix}1&0\\-1&1\end{vmatrix}=1$, so with $y_2=y_1+g$:
> $$f_{Y_1,G}(y_1,g)=2\lambda^2e^{-\lambda(2y_1+g)}=\big(2\lambda e^{-2\lambda y_1}\big)\big(\lambda e^{-\lambda g}\big),\qquad y_1>0,\ g>0.$$

> [!example] (c) the marginal of $G$ and (d) independence
> The density **factorises** into a function of $y_1$ times a function of $g$ on the rectangle $y_1>0,g>0$ (a product region): integrating out $y_1$ leaves $\lambda e^{-\lambda g}$, so **$G=Y_2-Y_1\sim\mathrm{Expo}(\lambda)$** (c); integrating out $g$ leaves $2\lambda e^{-2\lambda y_1}$ (consistent with (a)); and since the joint density is the product of the marginals, **$Y_1$ and $Y_2-Y_1$ are independent** (d). *Numbers:* $E[G]=0.50048$ ($1/\lambda=0.5$), $\mathrm{Var}\,G=0.25011$ ($1/\lambda^2=0.25$); $P(G>0.3)=0.5495$ against $e^{-0.6}=0.5488$; sample correlation of $Y_1,G$: $-0.0008$; $P(Y_1>0.2,G>0.3)=0.24698$ against the product $0.24713$.
> *Meaning:* after the first clock rings, the survivor's remaining waiting time is again $\mathrm{Expo}(\lambda)$ (the memoryless property, [[Memoryless Property]]) and **does not depend on when** the first one rang.

> [!example] (e) variance and correlation — done in class
> $Y_2=Y_1+G$ with independent summands, so $\mathrm{Var}(Y_2)=\mathrm{Var}(Y_1)+\mathrm{Var}(G)=\dfrac1{4\lambda^2}+\dfrac1{\lambda^2}=\dfrac5{4\lambda^2}$; $\mathrm{Cov}(Y_1,Y_2)=\mathrm{Var}(Y_1)+\mathrm{Cov}(Y_1,G)=\dfrac1{4\lambda^2}$; hence
> $$\mathrm{Corr}(Y_1,Y_2)=\frac{1/4\lambda^2}{\sqrt{1/4\lambda^2}\sqrt{5/4\lambda^2}}=\frac1{\sqrt5}=0.4472.$$
> *Numbers ($\lambda=2$, $2\times10^6$ samples):* $\mathrm{Var}\,Y_1=0.06266$ ($0.0625$), $\mathrm{Var}\,Y_2=0.31257$ ($0.3125$), $\mathrm{Cov}=0.06256$, $\mathrm{Corr}=0.44703$.
> > [!verify] A reading problem on the sheet
> > The sheet reads "Show $\mathrm{Var}(Y_\cdot)=5/(4\lambda^2)$ and that $\mathrm{Corr}(Y_1,Y_2)=1/\sqrt5$". The value $\frac5{4\lambda^2}$ is $\mathrm{Var}(Y_2)$; with $Y_1\sim\mathrm{Expo}(2\lambda)$ one has $\mathrm{Var}(Y_1)=\frac1{4\lambda^2}$ (the OCR of the other tool wrote $Y_1$; the subscript in the handwriting is ambiguous). The correlation $1/\sqrt5$ is consistent only with $\mathrm{Var}(Y_2)=\frac5{4\lambda^2}$.

**Reliability reading** 🔵. Two components in parallel with independent lifetimes $\mathrm{Expo}(\lambda)$, $\lambda=0.1$ per hour: the first failure comes at mean $\frac1{2\lambda}=5$ h, the system fails at $E[Y_2]=\frac3{2\lambda}=15$ h, and $P(\text{second fails more than 10 h after the first})=e^{-\lambda\cdot10}=e^{-1}=0.3679$ **whatever the time of the first failure** (independence).

> [!key] The Rényi gaps for $n$ exponentials 🔵
> For $n$ iid $\mathrm{Expo}(\lambda)$ variables, the **spacings** $Y_{(1)},\ Y_{(2)}-Y_{(1)},\dots,Y_{(n)}-Y_{(n-1)}$ are **independent** and $Y_{(k)}-Y_{(k-1)}\sim\mathrm{Expo}\big((n-k+1)\lambda\big)$ ($Y_{(0)}=0$). *Argument (memorylessness, repeated):* $n$ clocks, the first rings at rate $n\lambda$; the $n-1$ survivors restart afresh, the next ring is at rate $(n-1)\lambda$, and so on. Hence $E[Y_{(k)}]=\frac1\lambda\sum_{j=1}^k\frac1{n-j+1}$ and $E[\max]=\frac{H_n}\lambda$, the harmonic number. *Numbers* ($n=5$, $\lambda=1$, $10^6$ samples): mean gaps $0.2001,0.2497,0.3331,0.5005,1.0000$ against $\frac15,\frac14,\frac13,\frac12,1$; $E[\max]=2.2835$ against $H_5=2.2833$; the largest sample correlation between distinct gaps is $0.0020$ (independence). The case $n=2$ is Problem 2.

## 4. Problem 3: the multinomial distribution through indicators
<span class="scope-taught">taught</span> *Source: HW5 Q3* · <span class="scope-extra-beyond">extra · beyond</span> *rank, conditionals, Poissonisation*

$(X_1,\dots,X_k)\sim\mathrm{Mult}_k(n,\vec p)$, $p_1+\dots+p_k=1$: $n$ independent trials, each lands in outcome $i$ with probability $p_i$, and $X_i$ is the number of trials giving outcome $i$,
$$P(X_1=x_1,\dots,X_k=x_k)=\frac{n!}{x_1!\cdots x_k!}\,p_1^{x_1}\cdots p_k^{x_k}\qquad(x_1+\dots+x_k=n)$$
(the multinomial coefficient of [[PR01 Counting and the Axioms of Probability]] times the probability of one arrangement). The sheet's tool: $Y_{ij}=1$ if the $i$-th outcome appears in the $j$-th trial, else $0$.

> [!example] (a) means and covariances of the indicators
> $E(Y_{ij})=P(\text{trial }j\text{ gives outcome }i)=p_i$. Within **one trial** exactly one outcome occurs, so $Y_{ij}Y_{kj}=0$ for $i\ne k$ and
> $$\mathrm{Cov}(Y_{ij},Y_{kj})=E[Y_{ij}Y_{kj}]-p_ip_k=0-p_ip_k=-p_ip_k\quad(i\ne k),$$
> while for $i=k$, $Y_{ij}^2=Y_{ij}$ gives $\mathrm{Var}(Y_{ij})=p_i-p_i^2=p_i(1-p_i)$. Indicators from **different trials** are independent: $\mathrm{Cov}(Y_{ij},Y_{kj'})=0$ for $j\ne j'$.

> [!example] (b) the counts
> $X_i=Y_{i1}+\dots+Y_{in}$ ($n$ trials). Linearity: $E(X_i)=np_i$. Bilinearity of covariance and the vanishing across trials give
> $$\mathrm{Var}(X_i)=np_i(1-p_i),\qquad\mathrm{Cov}(X_i,X_k)=\sum_{j,j'}\mathrm{Cov}(Y_{ij},Y_{kj'})=\sum_j\mathrm{Cov}(Y_{ij},Y_{kj})=-np_ip_k\ (i\ne k).$$
> The **covariance matrix** is therefore
> $$\Sigma=n\begin{pmatrix}p_1&&\\&\ddots&\\&&p_k\end{pmatrix}-n\begin{pmatrix}p_1\\\vdots\\p_k\end{pmatrix}\begin{pmatrix}p_1&\cdots&p_k\end{pmatrix}=n\big(\mathrm{diag}(p)-pp^{\mathsf T}\big).$$

**Exact check** ($n=10$, $p=(0.2,0.3,0.5)$; all 66 outcomes enumerated, total mass $1.000000000000$):
$$\Sigma=\begin{pmatrix}1.6&-0.6&-1.0\\-0.6&2.1&-1.5\\-1.0&-1.5&2.5\end{pmatrix}\ \text{(enumeration = formula to all printed digits)},\qquad\text{mean }(2,3,5)=np.$$
A $10^6$-draw simulation gives $\mathrm{Cov}(X_1,X_2)=-0.5994$ against $-np_1p_2=-0.6$.

> [!key] Why the covariance is negative and $\Sigma$ is singular 🔵
> The counts satisfy $X_1+\dots+X_k=n$ **exactly**, so $\mathrm{Var}(\sum X_i)=\mathbf 1^{\mathsf T}\Sigma\mathbf 1=0$: the vector $(1,\dots,1)$ is in the kernel (eigenvalues for the example: $0,\ 2.318975,\ 3.881025$) and $\Sigma$ has **rank $k-1$**, the largest possible. If one count is large the others must be small: $\mathrm{Corr}(X_i,X_k)=-\sqrt{\dfrac{p_ip_k}{(1-p_i)(1-p_k)}}$ (example: $-0.32733$). For a fair die rolled $12$ times: $\mathrm{Var}(X_i)=1.6667$, $\mathrm{Cov}=-\frac13$, $\mathrm{Corr}=-\frac15$ for every pair; $P(\text{every face exactly twice})=\frac{12!}{(2!)^66^{12}}=0.003438$ (one in $291$) and $P(\text{no face missing})=0.437816$ (inclusion–exclusion).
> **Marginals and conditionals** (extra · beyond): each $X_i\sim\mathrm{Bin}(n,p_i)$ ($P(X_1=2)=0.301990$ from the pmf and from $\mathrm{Bin}(10,0.2)$) and, given $X_2=x_2$, $X_1\sim\mathrm{Bin}\big(n-x_2,\frac{p_1}{1-p_2}\big)$ (checked to $2\times10^{-16}$ for $x_2=3$: $\mathrm{Bin}(7,\frac27)$, $E[X_1\mid X_2=3]=2$).
> **Poissonisation** (extra · beyond): if $N_i\sim\mathrm{Poisson}(\mu p_i)$ are independent, then *given* $N_1+\dots+N_k=n$ the vector is $\mathrm{Mult}_k(n,p)$ (checked exactly for $n=4$, $\mu=3$: maximum pmf difference $6\times10^{-17}$); a Poisson number of trials turns the counts independent (the negative covariance disappears because $n$ is no longer fixed).

## Map of this chapter
> [!connection] How PR08 connects
> **Builds on:** [[PR04 Joint Distributions Expectation and Variance]] (joint laws, indicators, $\mathrm{Cov}$), [[PR05 Continuous Random Variables]] (exponential, memoryless, change of variables), [[PR07 Sums of Independent Variables Covariance and Correlation]] (covariance matrix, quadratic form), [[PR01 Counting and the Axioms of Probability]] (multinomial coefficients).
> **Leads to:** statistics (confidence intervals for quantiles, the sample median and range), reliability and queueing (Poisson processes: the order statistics of arrival times), the chi-squared test (multinomial counts and their covariance $n(\mathrm{diag}\,p-pp^{\mathsf T})$; recalled, not worked), maximum likelihood for categorical data.
> **Concepts:** [[Order Statistics]] · [[Joint Density of Order Statistics]] · [[Exponential Order Statistics]] · [[Multinomial Distribution]] · [[Multinomial Covariance Matrix]]
> **Other subjects:** [[Landscapes and Geomorphology - Course Map]] (extreme-value statistics of floods: the **maximum of $n$ iid** annual flows has cdf $F^n$; [[LS22 Floods Planform and River Profiles]]), [[Thermodynamics and Statistical Mechanics - Course Map]] (occupation numbers of microstates are multinomial: [[SM01 Probability Large Numbers and Information]]; the constraint $\sum X_i=n$ is why canonical and microcanonical fluctuations differ), [[Eco-Evo - Course Map]] (genotype counts in a population are multinomial: Hardy–Weinberg sampling), [[Group Theory - Course Map]] (random permutations and the ordering of a sample).

## Summary
> [!summary] Cheat-sheet
> - **(min, max) of 2 iid:** $f_{Y_1,Y_2}=2f(y_1)f(y_2)$ on $y_1<y_2$ (two preimages); via cdf: $F=2F(y_1)F(y_2)-F(y_1)^2$ then $\partial^2/\partial y_1\partial y_2$. **$n$ iid:** $n!\prod f(y_i)$ on the ordered region.
> - **$k$-th smallest:** $\frac{n!}{(k-1)!(n-k)!}F^{k-1}(1-F)^{n-k}f$; uniform: Beta$(k,n-k+1)$, mean $\frac k{n+1}$.
> - **Exponential:** $Y_1\sim\mathrm{Expo}(2\lambda)$; $Y_2-Y_1\sim\mathrm{Expo}(\lambda)$, **independent** of $Y_1$ (joint density factorises, Jacobian $1$); $\mathrm{Var}\,Y_1=\frac1{4\lambda^2}$, $\mathrm{Var}\,Y_2=\frac5{4\lambda^2}$, $\mathrm{Corr}=\frac1{\sqrt5}$; $n$ clocks: gaps $\mathrm{Expo}((n-k+1)\lambda)$, $E\max=H_n/\lambda$.
> - **Multinomial:** $\frac{n!}{\prod x_i!}\prod p_i^{x_i}$; $E=np_i$, $\mathrm{Var}=np_i(1-p_i)$, $\mathrm{Cov}=-np_ip_k$, $\Sigma=n(\mathrm{diag}\,p-pp^{\mathsf T})$ singular (rank $k-1$, $\sum X_i=n$); $\mathrm{Corr}=-\sqrt{p_ip_k/((1-p_i)(1-p_k))}$; $X_1\mid X_2\sim\mathrm{Bin}(n-x_2,\frac{p_1}{1-p_2})$.

## Practice
1. **Problem 1 by the cdf.** Redo the proof of $f_{Y_1,Y_2}=2f(y_1)f(y_2)$ for $X_i\sim U(0,1)$ and check that the density integrates to $1$ over $y_1<y_2$.
2. **Uniform extremes.** $X_1,X_2,X_3\sim U(0,1)$ iid. Find the densities and means of the minimum, median and maximum, and $P(\text{median}>0.7)$.
3. **Expected range.** For two iid $U(0,1)$ find $E[Y_2-Y_1]$ and $\mathrm{Corr}(Y_1,Y_2)$.
4. **Problem 2(b)–(d).** Carry out the change of variables for $\lambda=3$ and state the marginals of $Y_1$ and $Y_2-Y_1$.
5. **Problem 2(e).** Compute $\mathrm{Var}(Y_1)$, $\mathrm{Var}(Y_2)$, $\mathrm{Cov}(Y_1,Y_2)$ and $\mathrm{Corr}(Y_1,Y_2)$ for $\lambda=2$ and explain the sheet's "$5/(4\lambda^2)$".
6. **Three clocks.** $X_1,X_2,X_3\sim\mathrm{Expo}(1)$ iid: find $E[Y_{(1)}],E[Y_{(2)}],E[Y_{(3)}]$ and $\mathrm{Var}(Y_{(3)})$.
7. **Indicators.** For $\mathrm{Mult}_3(10,(0.2,0.3,0.5))$ compute $\mathrm{Cov}(Y_{1j},Y_{2j})$, $\mathrm{Cov}(X_1,X_2)$ and the matrix $\Sigma$.
8. **Singularity.** Show $\Sigma\mathbf 1=0$ for $\Sigma=n(\mathrm{diag}\,p-pp^{\mathsf T})$ and interpret.
9. **A die.** A fair die is rolled $12$ times. Find $\mathrm{Var}(X_1)$, $\mathrm{Cov}(X_1,X_2)$, $\mathrm{Corr}(X_1,X_2)$ and $P(X_1=X_2=X_3=X_4=X_5=X_6)$.
10. **Conditional.** In $\mathrm{Mult}_3(10,(0.2,0.3,0.5))$ find the law and mean of $X_1$ given $X_2=3$.

> [!example]- Solutions
> 1. $F_{Y_1,Y_2}=2y_1y_2-y_1^2$ on $0<y_1<y_2<1$; $\partial^2/\partial y_1\partial y_2=2$; $\iint_{y_1<y_2}2=2\cdot\frac12=1$.
> 2. $n=3$: min $3(1-y)^2$ (mean $\frac14$), median $6y(1-y)$ (mean $\frac12$, Beta(2,2)), max $3y^2$ (mean $\frac34$). $P(\text{median}>0.7)=\int_{0.7}^16y(1-y)\mathrm dy=3(1-0.49)-2(1-0.343)=1.53-1.314=0.216$.
> 3. $E[Y_2-Y_1]=\frac23-\frac13=\frac13$ ($E[Y_1]=\frac13$, $E[Y_2]=\frac23$). $\mathrm{Var}(Y_1)=\mathrm{Var}(Y_2)=\frac1{18}$ (Beta(1,2): $\frac{1\cdot2}{3^2\cdot4}=\frac1{18}$); $E[Y_1Y_2]=E[X_1X_2]=\frac14$, $\mathrm{Cov}=\frac14-\frac29=\frac1{36}$, $\mathrm{Corr}=\frac12$.
> 4. $f_{Y_1,Y_2}=2\cdot9e^{-3(y_1+y_2)}$; $(Y_1,G)$: $(6e^{-6y_1})(3e^{-3g})$; $Y_1\sim\mathrm{Expo}(6)$, $G\sim\mathrm{Expo}(3)$, independent.
> 5. $\lambda=2$: $\mathrm{Var}\,Y_1=\frac1{16}=0.0625$, $\mathrm{Var}\,Y_2=\frac5{16}=0.3125$, $\mathrm{Cov}=\frac1{16}$, $\mathrm{Corr}=\frac1{\sqrt5}=0.4472$; the sheet's $\frac5{4\lambda^2}$ is $\mathrm{Var}(Y_2)$ (§3 `[!verify]`).
> 6. Gaps $\frac13,\frac12,1$: $E[Y_{(1)}]=\frac13$, $E[Y_{(2)}]=\frac56$, $E[Y_{(3)}]=\frac{11}6=H_3$; $\mathrm{Var}(Y_{(3)})=\frac19+\frac14+1=\frac{49}{36}=1.361$.
> 7. $\mathrm{Cov}(Y_{1j},Y_{2j})=-0.06$, $\mathrm{Cov}(X_1,X_2)=-0.6$; $\Sigma$ as in §4.
> 8. $(\Sigma\mathbf 1)_i=n\big(p_i-p_i\sum_kp_k\big)=0$. $\mathrm{Var}(\sum X_i)=0$ because $\sum X_i=n$ is constant.
> 9. $\mathrm{Var}=12\cdot\frac16\cdot\frac56=1.6667$, $\mathrm{Cov}=-12\cdot\frac1{36}=-0.3333$, $\mathrm{Corr}=-0.2$; $P(\text{all faces twice})=\frac{12!}{2^6\cdot6^{12}}=0.003438$.
> 10. $X_1\mid X_2=3\sim\mathrm{Bin}(7,\frac27)$, mean $2$, equal to the unconditional mean $np_1$ because $X_2=3$ is exactly its own mean $np_2$.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | Problem 1 statement and the schematic, the general $n!\prod f$ statement, Problem 2(a)–(e), Problem 3(a)–(b) | [[hw5.pdf#page=1\|HW5, page 1]] and [[hw5.pdf#page=2\|page 2]] (handwritten; read from the page images in this session) | taught |
> | instructor's solution of Problem 1 (joint cdf, mixed derivative) | [[HW-5, Q.1.jpg]] (image, read in this session; the other tool's note [[introduction-to-probability/2026-11-06-hw-5-q1-solution\|2026-11-06]] could not read it) | taught |
> | the other tool's notes on the sheet | [[introduction-to-probability/2026-11-05-hw5\|HW5 note]] (OCR; its "$\mathrm{Var}(Y_1)=5/(4\lambda^2)$" is the sheet's ambiguous subscript) | secondary |
> | $k$-th order statistic, Beta form, Rényi gaps, multinomial rank/conditionals/Poissonisation, reliability reading | derived here; `scripts/pr08_numbers.py` (simulation $10^6$–$2\times10^6$ draws, exact enumeration of the 66 multinomial outcomes), `scripts/fig_pr08.py`, tool `pr_order_statistics` | extra/beyond |
>
> **Notes.** The lecture notes announced for the weekend (the sheet's source post says "will add notes in weekend") are **not in the folder**: if they add examples or define $Y_{(k)}$ differently (e.g. ascending $Y_1\le\dots\le Y_n$ as on the sheet), compare first. No textbook was consulted; the formulas are checked numerically rather than cited. The name "Rényi" for the exponential spacings and the chi-squared remark are from memory (not read).
