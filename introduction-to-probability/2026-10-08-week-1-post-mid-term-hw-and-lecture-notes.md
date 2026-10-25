---
id: introduction-to-probability/2026-10-08-week-1-post-mid-term-hw-and-lecture-notes
aliases: [Week 1 (post mid-term) HW and lecture notes]
tags: [introduction-to-probability, continuous-random-variables, homework]
trust_tier: agent_written
---

# Week 1 (post mid-term): homework and lecture notes

## Covered
A 9-page handwritten PDF: homework on page 1-2, lecture notes from page 3 (Classroom: week1_mt2113.pdf). Read from the page images; the due date is not stated.

### Homework
1. Rayleigh distribution, pdf $f(x)=xe^{-x^2/2}$ for $x>0$, $0$ for $x\le0$. (a) Find $P(1<X<3)$. (b) Find the first quartile, median and third quartile: the $q_i$ with $P(X\le q_i)=i/4$, $i=1,2,3$.
2. A circle has radius $R\sim\text{Unif}(0,1)$ and area $A$. (a) Mean and variance of $A$ without first finding the cdf or pdf of $A$. (b) The cdf and pdf of $A$.
3. A stick of length 1 is broken at a uniformly distributed point $u$. For a fixed point $p$ on the stick, $X$ is the length of the piece containing $p$. Find $E(X)$ and the $p$ that maximises it.
4. $Z\sim N(0,1)$, $c\in(0,\infty)$: find $E(\max\{Z-c,0\})$.
5. Points of inflection of the standard normal pdf $\varphi(x)=e^{-x^2/2}/\sqrt{2\pi}$; for $N(\mu,\sigma)$ show the pdf is $\frac1\sigma\varphi\big(\frac{x-\mu}{\sigma}\big)$ and find its inflection points.
6. (starred) For a non-negative random variable $Y$, $E(Y)=\int_0^\infty P(Y>y)\,dy$. (a) Show that for any $Y$, $E(Y)=\int_0^\infty P(Y>y)\,dy-\int_0^\infty P(Y<-y)\,dy$. (b) Using (a), prove LOTUS for any function $g$ (the class proof covers non-negative $g$).

### Lecture notes
- A continuous random variable $X:S\to\mathbb R$: we do not talk about $P(X=x)$, or take it to be $0$. Naively $P(x<X<x+\delta x)=f(x)\,\delta x$ for the probability density function (pdf) $f_X$, the continuous analogue of the pmf. $P(a<X<b):=\int_a^bf_X(x)\,dx$ and, for any "nice" $B\subset\mathbb R$, $P(X\in B)=\int_Bf_X(x)\,dx$. A pdf must satisfy (i) $f_X\ge0$ and (ii) $\int_{\mathbb R}f_X(x)\,dx=1$; it is required to be continuous except at finitely many points.
- Uniform on $[a,b]$, $\text{Unif}(a,b)$: $f_X=\frac1{b-a}$ on $[a,b]$, $0$ outside; $P(X\in B)=\frac1{b-a}\int_B dx$ for $B\subset[a,b]$.
- Logistic: $f_X(x)=\dfrac{e^x}{(1+e^x)^2}$, $x\in\mathbb R$. It is non-negative and continuous, and with $u=1+e^x$, $\int_{-\infty}^\infty f=\int_1^\infty u^{-2}\,du=1$. The cdf $F(x)=\int_{-\infty}^xf_X(t)\,dt$ is here $F(x)=\dfrac{e^x}{1+e^x}$.
- Rayleigh: $F(x)=0$ for $x<0$ and $1-e^{-x^2/2}$ for $x\ge0$, so $f=F'$ is as above and $\lim_{x\to\infty}F=1$. In general the pdf is the derivative of the cdf, because $\frac d{dx}\int_{-\infty}^xf(t)\,dt=f(x)$.
- Expectation $E(X):=\int_{-\infty}^\infty xf_X(x)\,dx$. Uniform: $\frac{a+b}2$. Logistic: $0$ (odd integrand). Rayleigh: $\int_0^\infty x^2e^{-x^2/2}dx=\tfrac12\int_{-\infty}^\infty e^{-x^2/2}dx$ by parts, $=\sqrt{\pi/2}$ once $I=\sqrt{2\pi}$ is shown.
- LOTUS (law of the unconscious statistician): for $Y=g(X)$, $E(g(X))=\int g(x)f_X(x)\,dx$, with no need to find $f_Y$.
  - Lemma: for non-negative $Y$, $E(Y)=\int_0^\infty P(Y>y)\,dy$. Proof: write $P(Y>y)=\int_y^\infty f_Y(t)\,dt$ and interchange the order of integration over the region $0\le y\le t$.
  - Proof for $g\ge0$: $E(g(X))=\int_0^\infty P(g(X)>y)\,dy=\int_0^\infty\int_{\{x:g(x)>y\}}f_X(x)\,dx\,dy$; swapping the order gives $\int_{\{g>0\}}f_X(x)\,g(x)\,dx=\int_{\mathbb R}g(x)f_X(x)\,dx$, since the integrand is $0$ where $g=0$. The general case is the optional homework problem 6.
- Variance $\operatorname{Var}(X)=E(X^2)-E(X)^2=E((X-\mu)^2)$ for $\mu=E(X)$: expand $\int(x-\mu)^2f=E(X^2)+\mu^2-2\mu^2$. Uniform: $\operatorname{Var}=\frac{(b-a)^2}{12}$.
- Standard normal $N(0,1)$: $\varphi(x)=e^{-x^2/2}/\sqrt{2\pi}$. To show $\int\varphi=1$ one needs $I=\int_{-\infty}^\infty e^{-x^2/2}dx=\sqrt{2\pi}$: compute $I^2=\iint_{\mathbb R^2}e^{-(x^2+y^2)/2}dx\,dy$ in polar coordinates, $=2\pi\int_0^\infty e^{-r^2/2}r\,dr=2\pi$.
- For $Z\sim N(0,1)$: $E(Z)=0$ (odd integrand) and $\operatorname{Var}(Z)=E(Z^2)=\frac2{\sqrt{2\pi}}\int_0^\infty x^2e^{-x^2/2}dx=1$ (using the Rayleigh computation).
- Gaussian $N(\mu,\sigma)$, $\sigma>0$, $\mu\in\mathbb R$: $X\sim N(\mu,\sigma)$ if $Z=(X-\mu)/\sigma$ is standard normal, i.e. $X=\sigma Z+\mu$. Then $E(X)=\mu$ and $\operatorname{Var}(X)=\sigma^2E(Z^2)=\sigma^2$, so the standard deviation is $\sigma$.

## From the post
HW for week 1, as well as lecture notes

## Files
- [week1_mt2113.pdf](https://drive.google.com/file/d/1A4MEFmAKwnUAWUp2zi59rwjr6blvGqMb/view?usp=drive_web)

## Related
- [[introduction-to-probability/2026-09-10-class-notes-10th-september-2026]]: pdf, cdf, expectation and variance for continuous variables, which this extends.
- [[08-Probability/PR05 Continuous Random Variables]]: their chapter on uniform, normal and other densities.
- [[introduction-to-probability/2026-09-09-class-notes-9th-september-2026]]: variance formula used here.
