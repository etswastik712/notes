---
title: Probability Quiz Prep
aliases: [MT2113 quiz prep, probability quiz, HW4 HW5 HW6 quiz, PR quiz prep]
subject: probability
type: moc
scope: [taught]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/moc, taught, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw4, quiz/pr-hw5, quiz/pr-hw6]
---
# Probability Quiz Prep (Homework 4, 5 and 6)

◀ [[Probability - Course Map|Course Map]] · chapters [[PR07 Sums of Independent Variables Covariance and Correlation|PR07 (HW4)]] · [[PR08 Order Statistics and the Multinomial Distribution|PR08 (HW5)]] · [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms|PR09 (HW6, Weeks 4–5)]] · background [[PR04 Joint Distributions Expectation and Variance|PR04]] · [[PR05 Continuous Random Variables|PR05]] · [[PR06 Moments Generating Functions and Limit Theorems|PR06]]

<span class="scope-taught">taught · in syllabus (Homework 4, 5, 6 and the Week 4–5 lecture summaries)</span>

> [!warning] What this page covers (written 2026-11-12 for the quiz on 2026-11-13)
> **Scope: Homework 4 ([[hw4.pdf]]), Homework 5 ([[hw5.pdf]], with the instructor's Q1 solution [[HW-5, Q.1.jpg]]) and Homework 6 ([[hw6_edited.pdf]])**, plus the lecture summaries on **joint/marginal/conditional densities, independence, the covariance matrix, the min/max lemma, the multinomial and the change-of-variables formula** ([[Week4_notes.pdf]], [[Week5_notes.pdf]]). There is **no posted solution** for HW4 and HW6 (the solutions in the vault are mine, with numerical checks: `scripts/pr_numbers2.py`, `pr08_numbers.py`, `pr09_numbers.py`). Three ambiguities in the sheets are flagged in PR09 (disc-marginal constant, the "Poisson" race that is solved with exponentials, the two meanings of $\sigma_i^2$ in HW6 Q1) and the HW5 Q2(e) subscript in PR08.

> [!tip] How the tags work
> Open the search pane and type **`tag:#quiz/pr-hw4`**, **`tag:#quiz/pr-hw5`**, **`tag:#quiz/pr-hw6`** (or **`tag:#quiz/probability`** for everything). The tags are on the chapter front matter, on every homework-question section heading (PR07 §3–§6, PR08 §1–§4, PR09 §1–§5) and on the concept notes of §7. #quiz/pr-hw4 #quiz/pr-hw5 #quiz/pr-hw6

## 1. Question map: where every homework question is solved

| Q | What it asks | Key result | Solved in |
|---|---|---|---|
| **HW4 Q1** #quiz/pr-hw4 | $X\sim N(\mu_1,\sigma_1^2)$, $Y\sim N(\mu_2,\sigma_2^2)$ independent: get $X+Y$ **by convolution** | $X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$ (complete the square in $\int f_X(x)f_Y(z-x)\mathrm dx$) | PR07 §3 |
| **HW4 Q2** #quiz/pr-hw4 | (a) $Y\sim N(\mu,\sigma^2)\Rightarrow-Y\sim N(-\mu,\sigma^2)$; (b) $X,Y$ iid $N(0,1)$: $E\lvert X-Y\rvert=2/\sqrt\pi$ (folded Gaussian $\sqrt{2/\pi}$) | cdf method; $X-Y\sim N(0,2)$; $E\lvert X-Y\rvert=\sqrt2\sqrt{2/\pi}=1.1284$ | PR07 §4 |
| **HW4 Q3** #quiz/pr-hw4 | $\mathrm{Var}(\sum c_iX_i)=c^{\mathsf T}Ac$, $A_{ij}=\mathrm{Cov}(X_i,X_j)$; use $\mathrm{Var}(X+tY)\ge0$ to show $\mathrm{Cor}\in[-1,1]$ | discriminant $4\mathrm{Cov}^2-4\mathrm{Var}X\mathrm{Var}Y\le0$ | PR07 §5 |
| **HW4 Q4** (= HW3 Q4) #quiz/pr-hw4 | MGF of the sum of two fair dice | $M(t)=\big(\tfrac16\sum_{k=1}^6e^{kt}\big)^2=\tfrac1{36}\sum_{s=2}^{12}c_se^{st}$, $c_s=1,2,3,4,5,6,5,4,3,2,1$; $M'(0)=7$ | PR07 §6, PR06 §3.3 |
| **HW5 Q1** #quiz/pr-hw5 | joint density of $(\min,\max)$ of two iid variables; $n$ variables | $f_{Y_1,Y_2}=2f(y_1)f(y_2)$ on $y_1<y_2$; $n!\prod f(y_i)$ on $y_1<\dots<y_n$ (two preimages, or the cdf $2F(y_1)F(y_2)-F(y_1)^2$ and $\partial^2/\partial y_1\partial y_2$) | PR08 §1 |
| **HW5 Q2** #quiz/pr-hw5 | $X_i\sim\mathrm{Expo}(\lambda_i)$: $Y_1=\min\sim\mathrm{Expo}(\lambda_1+\lambda_2)$; $(Y_1,Y_2-Y_1)$; $\mathrm{Var}$ and $\mathrm{Corr}(Y_1,Y_2)$ | equal rates: $Y_1\sim\mathrm{Expo}(2\lambda)$, $Y_2-Y_1\sim\mathrm{Expo}(\lambda)$ **independent**; $\mathrm{Var}Y_1=\frac1{4\lambda^2}$, $\mathrm{Var}Y_2=\frac5{4\lambda^2}$ (the sheet's "$5/4\lambda^2$" is $\mathrm{Var}Y_2$), $\mathrm{Corr}=\frac1{\sqrt5}$ | PR08 §3 |
| **HW5 Q3** #quiz/pr-hw5 | multinomial $\mathrm{Mult}_k(n,p)$ via indicators: marginals, moments, covariance | $X_i\sim\mathrm{Bin}(n,p_i)$; $\mathrm{Cov}(X_i,X_k)=-np_ip_k$; $\Sigma=n(\mathrm{diag}\,p-pp^{\mathsf T})$ singular | PR08 §4 |
| **HW6 Q1** #quiz/pr-hw6 | $X\sim N(\mu,\Sigma)$, $Y=OX$, $O\Sigma O^{\mathsf T}$ diagonal $\Rightarrow$ $Y_i$ independent normals | $|\det O|=1$; exponent $\to\sum(y_i-\mu_i')^2/\lambda_i$; $\det\Sigma=\prod\lambda_i$; $Y_i\sim N((O\mu)_i,\lambda_i)$ | PR09 §3 |
| **HW6 Q2** #quiz/pr-hw6 | $X=-\ln U\sim$ ? ; the law of $U_1\cdots U_n$ | $\mathrm{Expo}(1)$; $-\ln(U_1\cdots U_n)\sim\mathrm{Gamma}(n,1)$; $f_{\prod U}=(-\ln u)^{n-1}/(n-1)!$ | PR09 §4 |
| **HW6 Q3** #quiz/pr-hw6 | tangent line of $g$ with $g''>0$ lies below the graph (used for Jensen) | $h=g-\text{tangent}$, $h'$ increasing through $0$ at $a$; $E\,g(X)\ge g(EX)$ | PR09 §5 |
| **Week 4 lecture** #quiz/pr-hw4 #quiz/pr-hw6 | marginals, independence ⇔ factorisation of pdf/cdf/survival fn, conditional pdf, **Bayes for densities**, uniform disc, mgf of a sum | $f_{Y\mid X}=f_{X,Y}/f_X$; disc marginal $\frac2{\pi R}\sqrt{1-(x/R)^2}$ | PR09 §1 |
| **Week 5 lecture** #quiz/pr-hw5 #quiz/pr-hw6 | covariance matrix, two proofs of $\lvert\rho\rvert\le1$ (calculus and eigenvalues), $\max/\min$ lemma, **change of variables**, multinomial | $P(Y_n\le y)=\prod P(X_i\le y)$, $P(Y_1\ge y)=\prod P(X_i\ge y)$; $f_Y=f_X(g^{-1})\lvert\det\partial g^{-1}/\partial y\rvert$ | PR07 §5, PR08, PR09 §2 |

## 2. Formulas to know cold
> [!key] Homework 4 #quiz/pr-hw4
> - **Convolution** (independent $X,Y$): $f_{X+Y}(z)=\int f_X(x)f_Y(z-x)\,\mathrm dx$; discrete $p_{X+Y}(s)=\sum_kp_X(k)p_Y(s-k)$; **MGFs multiply**: $M_{X+Y}=M_XM_Y$.
> - **Normals:** $X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$; $-Y\sim N(-\mu,\sigma^2)$; $X-Y\sim N(\mu_1-\mu_2,\sigma_1^2+\sigma_2^2)$ (variances **add**). $E|Z|=\sqrt{2/\pi}$, so $E|X-Y|=2/\sqrt\pi$ for iid $N(0,1)$ and $4/\sqrt\pi$ for iid $N(\mu,4)$.
> - $\mathrm{Var}(\sum c_iX_i)=\sum c_i^2\mathrm{Var}X_i+2\sum_{i<j}c_ic_j\mathrm{Cov}(X_i,X_j)=c^{\mathsf T}Ac$; $A$ symmetric, **positive semi-definite**.
> - $\rho=\mathrm{Cov}/(\sigma_X\sigma_Y)\in[-1,1]$; $|\rho|=1\iff Y=aX+b$; independent $\Rightarrow\rho=0$, **not conversely**.
> - Two dice: pmf of the sum $(1,2,3,4,5,6,5,4,3,2,1)/36$, $E=7$, $\mathrm{Var}=35/6$.

> [!key] Homework 5 #quiz/pr-hw5
> - $P(\max\le y)=\prod F_i(y)$, $P(\min\ge y)=\prod(1-F_i(y))$; $\min$ of independent $\mathrm{Expo}(\lambda_i)$ is $\mathrm{Expo}(\sum\lambda_i)$; memoryless $\Rightarrow$ the gap $Y_2-Y_1\sim\mathrm{Expo}(\lambda)$ independent of $Y_1$.
> - **Order statistics:** $f_{Y_{(k)}}=\dfrac{n!}{(k-1)!(n-k)!}F^{k-1}(1-F)^{n-k}f$; $f_{Y_1,\dots,Y_n}=n!\prod f(y_i)$ on $y_1<\dots<y_n$.
> - **Multinomial:** $P=\dfrac{n!}{n_1!\cdots n_k!}\prod p_i^{n_i}$; $E=np_i$, $\mathrm{Var}=np_i(1-p_i)$, $\mathrm{Cov}=-np_ip_k$; $X_1\mid X_2=x_2\sim\mathrm{Bin}(n-x_2,\tfrac{p_1}{1-p_2})$.

> [!key] Homework 6 and Weeks 4–5 #quiz/pr-hw6
> - **Change of variables:** $f_Y(y)=f_X(g^{-1}(y))\,\big|\det\partial g^{-1}/\partial y\big|=f_X(g^{-1}(y))/|\det\partial g/\partial x|$; several preimages: sum. Linear: divide by $|\det A|$; polar: Jacobian $r$.
> - **Multivariate normal:** $f_X=\exp(-\frac12(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu))/((2\pi)^{n/2}\sqrt{\det\Sigma})$; $Y=OX$, $O\Sigma O^{\mathsf T}=\mathrm{diag}(\lambda_i)$: independent $N((O\mu)_i,\lambda_i)$ (the $\lambda_i$ are **eigenvalues**, not $\Sigma_{ii}$; only the trace is preserved).
> - $-\ln U\sim\mathrm{Expo}(1)$; $E[U^k]=(k+1)^{-n}$ for $U=\prod U_j$; **Jensen:** $g$ convex $\Rightarrow E\,g(X)\ge g(EX)$ (take $a=EX$ in the tangent-line lemma).
> - **Conditional / Bayes:** $f_{Y|X}=f_{X,Y}/f_X$, $f_{Y|X}=f_{X|Y}f_Y/f_X$.

## 3. Traps
1. **$\mathrm{Var}(X-Y)=\mathrm{Var}X+\mathrm{Var}Y$** (plus). And $|X-Y|$ is **folded** normal: its mean is positive ($2/\sqrt\pi$), not $0$.
2. Normal parameters: $N(\mu,\sigma^2)$ takes the **variance**; the MGF exponent is $+\mu t+\sigma^2t^2/2$.
3. **Uncorrelated $\ne$ independent** (disc, $X$ vs $X^2$); independent normal *marginals* do not make a jointly normal vector.
4. The **covariance matrix** of a multinomial is singular ($\sum X_i=n$); the covariances are **negative**.
5. HW5 Q2(e): "$5/(4\lambda^2)$" is $\mathrm{Var}(Y_2)$, not $\mathrm{Var}(Y_1)=1/(4\lambda^2)$.
6. Change of variables needs the **absolute value** of the Jacobian and the Jacobian of the **inverse** map (or divide by the forward one); non-monotone maps have several preimages.
7. HW6 Q1: after the rotation the variances are the **eigenvalues** $\lambda_i$; $|\det O|=1$ is why the density is not rescaled.
8. $-\log U$ in HW6 is the **natural** logarithm; $-\ln(U_1\cdots U_n)$ is a **sum** of exponentials (Gamma), the product's density is $(-\ln u)^{n-1}/(n-1)!$, not Gamma.
9. Jensen's direction: $E\,g(X)\ge g(EX)$ for **convex** $g$ ($g''>0$); strict unless $X$ is constant.
10. Week 4's "Example 2" is labelled Poisson but integrates **exponential** densities: $P(X_1<X_2)=\lambda_1/(\lambda_1+\lambda_2)$ for exponentials; for Poisson variables it is a sum (PR09 §1).

## 4. Derivations to write from a blank page
- **Convolution of two normals** (HW4 Q1): complete the square in $x$ in the exponent, $\int e^{-(\dots)^2}\mathrm dx$ gives a constant; the rest is $N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.
- **$|\rho|\le1$** (HW4 Q3): $\mathrm{Var}(X+tY)=\mathrm{Var}X+2t\mathrm{Cov}+t^2\mathrm{Var}Y\ge0$ for all $t$; discriminant $\le0$ (or the minimum at $t^*=-\mathrm{Cov}/\mathrm{Var}Y$ equals $\mathrm{Var}X(1-\rho^2)$).
- **$f_{Y_1,Y_2}=2f f$** (HW5 Q1): two preimages of $(y_1,y_2)$, or $F=2F(y_1)F(y_2)-F(y_1)^2$ then the mixed derivative.
- **Independence of $Y_1$ and $Y_2-Y_1$** (HW5 Q2): joint density $2\lambda^2e^{-\lambda(y_1+y_2)}$, substitute $y_2=y_1+g$ (Jacobian $1$): $(2\lambda e^{-2\lambda y_1})(\lambda e^{-\lambda g})$.
- **Multinomial covariance** (HW5 Q3): $X_i=\sum_jY_{ij}$ (trial indicators), $\mathrm{Cov}(Y_{ij},Y_{kj})=-p_ip_k$, independent across trials.
- **Rotation to independent normals** (HW6 Q1): Jacobian, exponent, determinant (three facts).
- **$-\ln U$, the product of uniforms** (HW6 Q2): $P(-\ln U>x)=P(U<e^{-x})=e^{-x}$; mgf $(1-t)^{-n}$; change of variables $U=e^{-V}$.
- **Tangent line below a convex graph** (HW6 Q3) and **Jensen**.

## 5. Self-test (answers collapsed; every answer is a result already checked in the chapters)
1. **(HW4 Q1/Q2)** $X\sim N(1,4)$ and $Y\sim N(-2,9)$ independent. Find $P[X-Y>6]$. For iid $X,Y\sim N(5,4)$ find $E|X-Y|$.
2. **(HW4 Q3)** $\mathrm{Var}X=4$, $\mathrm{Var}Y=9$, $\mathrm{Var}Z=1$, $\mathrm{Cov}(X,Y)=3$, $\mathrm{Cov}(X,Z)=-1$, $\mathrm{Cov}(Y,Z)=0$. Find $\mathrm{Var}(2X-3Y+Z)$.
3. **(HW4 Q4)** Write the MGF of the sum of two fair dice in the form $\frac1{36}\sum c_se^{st}$ and check $M'(0)$.
4. **(HW4)** Two fair dice: the pmf of $X-Y$ and $E|X-Y|$.
5. **(HW5 Q1/Q2)** Two iid $\mathrm{Expo}(2)$: $\mathrm{Var}Y_1$, $\mathrm{Var}Y_2$, $\mathrm{Cov}$ and $\mathrm{Corr}(Y_1,Y_2)$. Three iid $U(0,1)$: density of the median and $P[\text{median}>0.7]$.
6. **(HW5 Q3)** A fair die is rolled $12$ times: $\mathrm{Var}(X_1)$, $\mathrm{Cov}(X_1,X_2)$, $\mathrm{Corr}$, and $P[\text{every face exactly twice}]$. In $\mathrm{Mult}_3(10,(0.2,0.3,0.5))$ find the law of $X_1$ given $X_2=3$.
7. **(HW6 Q1)** $\Sigma=\begin{pmatrix}5&3\\3&5\end{pmatrix}$, $\mu=0$: find $O$, the laws of $Y_1,Y_2$ and of $X_1+X_2$.
8. **(HW6 Q2)** Show $-\frac1\lambda\ln U\sim\mathrm{Expo}(\lambda)$ and find $P(X>1)$ for $\lambda=2$. For $U=U_1U_2U_3$ find $f_U$, $E[U]$, $P[U<\tfrac18]$.
9. **(HW6 Q3)** $X\in\{1,3\}$ equally likely: check $E[1/X]\ge1/E[X]$ and $E[X^2]\ge(EX)^2$. Show $e^x\ge ex$.
10. **(change of variables)** $X\sim\mathrm{Expo}(1)$, $Y=\sqrt X$: find $f_Y$, $E[Y]$. Iid $N(0,1)$ pair: show $R^2\sim\mathrm{Expo}(\tfrac12)$.
11. **(Week 4)** $(X_1,X_2)$ uniform on the disc of radius $2$: $f_{X_1}$, $P(|X_1|<1)$, and the conditional of $X_2$ given $X_1=1$.
12. **(Week 4 Example 2)** $X_1\sim\mathrm{Expo}(2)$, $X_2\sim\mathrm{Expo}(3)$ independent: $P(X_1<X_2)$.

> [!example]- Answers
> 1. $X-Y\sim N(3,13)$: $P[X-Y>6]=1-\Phi\big(\tfrac3{\sqrt{13}}\big)=1-\Phi(0.832)=\mathbf{0.2027}$. $X-Y\sim N(0,8)$: $E|X-Y|=\sqrt8\sqrt{2/\pi}=\mathbf{4/\sqrt\pi=2.2568}$.
> 2. $c=(2,-3,1)$: $16+81+1+2(-18-2)=\mathbf{58}$; $A=\begin{pmatrix}4&3&-1\\3&9&0\\-1&0&1\end{pmatrix}$ gives $c^{\mathsf T}Ac=58$.
> 3. $M(t)=\tfrac1{36}\big(e^{2t}+2e^{3t}+3e^{4t}+4e^{5t}+5e^{6t}+6e^{7t}+5e^{8t}+4e^{9t}+3e^{10t}+2e^{11t}+e^{12t}\big)$; $M'(0)=\tfrac1{36}\sum s\,c_s=\mathbf7$; $\mathrm{Var}=\tfrac{35}6$.
> 4. $P[X-Y=d]=\dfrac{6-|d|}{36}$, $d=-5..5$; $E|X-Y|=\dfrac{35}{18}=\mathbf{1.944}$.
> 5. $\lambda=2$: $\mathrm{Var}Y_1=\tfrac1{16}$, $\mathrm{Var}Y_2=\tfrac5{16}$, $\mathrm{Cov}=\tfrac1{16}$, $\mathrm{Corr}=\tfrac1{\sqrt5}=\mathbf{0.4472}$. Median of $3$ uniforms: $6y(1-y)$, $P[>0.7]=\mathbf{0.216}$.
> 6. $\mathrm{Var}=12\cdot\frac16\cdot\frac56=\mathbf{1.667}$, $\mathrm{Cov}=-\mathbf{0.333}$, $\mathrm{Corr}=-\mathbf{0.2}$; $P=\dfrac{12!}{2^6\,6^{12}}=\mathbf{0.003438}$. $X_1\mid X_2=3\sim\mathrm{Bin}(7,\tfrac27)$, mean $2$.
> 7. $O=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, eigenvalues $8,2$: $Y_1\sim N(0,8)$, $Y_2\sim N(0,2)$ independent; $X_1+X_2=\sqrt2Y_1\sim N(0,16)$.
> 8. $P(-\frac1\lambda\ln U>x)=P(U<e^{-\lambda x})=e^{-\lambda x}$; $\lambda=2$: $e^{-2}=\mathbf{0.1353}$. $f_U=\dfrac{(\ln u)^2}2$ on $(0,1)$, $E[U]=\tfrac18$, $P[U<\tfrac18]=\mathbf{0.6552}$.
> 9. $E[1/X]=\tfrac23\ge\tfrac12$; $E[X^2]=5\ge4$; $g=e^x$ has tangent $ex$ at $a=1$ and $g''>0$, so $e^x\ge ex$ with equality only at $x=1$.
> 10. $x=y^2$, $f_Y=2ye^{-y^2}$, $E[Y]=\sqrt\pi/2=\mathbf{0.8862}$. Polar: $f_{R,\Theta}=\frac1{2\pi}re^{-r^2/2}$, $P(R^2>s)=e^{-s/2}$.
> 11. $f_{X_1}=\dfrac{\sqrt{4-x^2}}{2\pi}$; $P(|X_1|<1)=\dfrac{\sqrt3}{2\pi}+\dfrac13=\mathbf{0.6090}$; $X_2\mid X_1=1$ uniform on $\pm\sqrt3$, density $\tfrac1{2\sqrt3}=0.2887$.
> 12. $\lambda_1/(\lambda_1+\lambda_2)=\tfrac25=\mathbf{0.4}$ (for Poisson$(2)$, Poisson$(3)$ it would be $0.5853$).

## 6. More practice, by homework
Each chapter has 10–12 more problems with solutions: [[PR07 Sums of Independent Variables Covariance and Correlation]] (Practice 1–12: joint density, uncorrelated-dependent disc, convolutions, Poisson sum, normal difference, quadratic form, Cauchy–Schwarz, sample mean $n=385$), [[PR08 Order Statistics and the Multinomial Distribution]] (Practice 1–10) and [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]] (Practice 1–11). Interactive tools: [[Interactive Tools]] → *Joint, marginal and conditional*, *Covariance and correlation*, *Order statistics*, *Rotating a correlated Gaussian*, *Functions of a random variable*.

## 7. Tag index: every related note
- **Chapters:** [[PR07 Sums of Independent Variables Covariance and Correlation]] · [[PR08 Order Statistics and the Multinomial Distribution]] · [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]] · background [[PR04 Joint Distributions Expectation and Variance]] · [[PR05 Continuous Random Variables]] · [[PR06 Moments Generating Functions and Limit Theorems]].
- **Concept notes (tagged):** HW4: [[Sum of Independent Random Variables]] · [[Covariance Matrix]] · [[Covariance and Correlation]] · [[Normal Distribution]] · [[Standard Normal Distribution]] · [[Folded Normal Distribution]] · [[Moment Generating Function]] · [[Joint Density Function]] · [[Independence of Random Variables]] · [[Marginal Distribution]] · [[Variance]] · [[Poisson Distribution]]. HW5: [[Order Statistics]] · [[Joint Density of Order Statistics]] · [[Exponential Order Statistics]] · [[Exponential Distribution]] · [[Memoryless Property]] · [[Multinomial Distribution]] · [[Multinomial Covariance Matrix]] · [[Multinomial Coefficient]] · [[Indicator Random Variable]] · [[Binomial Distribution]] · [[Cdf Method for Transformations]]. HW6 and the lectures: [[Conditional Density Function]] · [[Change of Variables for Densities]] · [[Multivariate Normal Distribution]] · [[Gamma Distribution]] · [[Jensen's Inequality]] · [[Box-Muller Transform]] · [[Probability Integral Transform]] · [[Rayleigh Distribution]].

> [!provenance]- Source map
> | Content | Source |
> |---|---|
> | the questions | [[hw4.pdf]], [[hw5.pdf]] + [[HW-5, Q.1.jpg]], [[hw6_edited.pdf]], [[Week4_notes.pdf]], [[Week5_notes.pdf]] |
> | solutions and numbers | [[PR07 Sums of Independent Variables Covariance and Correlation]], [[PR08 Order Statistics and the Multinomial Distribution]], [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]] (mine; simulation-checked) |
> | the answers in §5 | taken from the Practice solutions of those chapters (all recomputed); the dice MGF and mean/variance checked in `scripts/quiz_numbers.py` |

## 8. Also solved, outside this quiz's scope
Homeworks 1–3, Quiz 1 and the earlier weekly sheets are already solved in the chapters: HW2 and HW3 (exponential, memoryless, median and mode, moments, MGFs of the named distributions) in [[PR05 Continuous Random Variables]] and [[PR06 Moments Generating Functions and Limit Theorems]]; Quiz 1 in PR05 Practice 13–15; the practice sheets of August–September in PR01–PR04. The Week 4 "Poisson" example, which is solved with exponentials, is explained in [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]] §1.
