---
id: introduction-to-probability/2026-11-18-week-7-lectures-summary
aliases: [Week 7 lectures summary]
tags: [probability, mt2113, lecture-notes]
trust_tier: agent_written
---

# Week 7 lectures summary: central limit theorem

## Covered
Source: handwritten PDF week7_lectures.pdf, read from the page images (formulas worth checking against the file). The post says the two examples at the end were not discussed in class for lack of time.

**Recall (LLN).** $X_1,X_2,\dots$ i.i.d. with mean $\mu$, variance $\sigma^2$; $\bar X_n$ has mean $\mu$ and variance $\sigma^2/n$. WLLN: for all $\epsilon>0$, $P(|\bar X_n-\mu|>\epsilon)\to0$.

**Central limit theorem (CLT).** Normalise: $\dfrac{\bar X_n-\mu}{\sigma/\sqrt n}\to N(0,1)$ in distribution, i.e. the cdf converges: $P\Big(\dfrac{\bar X_n-\mu}{\sigma/\sqrt n}\le x\Big)\to\displaystyle\int_{-\infty}^x\frac{e^{-t^2/2}}{\sqrt{2\pi}}\,dt=\Phi(x)$.

**Corollary (CLT approximation).** For large $n$, $\bar X_n$ is "approximately" $N(\mu,\sigma^2/n)$; no precise assertion is made. Roughly: $\frac{\bar X_n-\mu}{\sigma/\sqrt n}$ is approximately $N(0,1)$ for large $n$.

**Lemma needed for the proof (proof skipped).** Let $Z_1,Z_2,\dots$ have cdfs $F_{Z_n}$ and mgfs $M_{Z_n}(t)$. If $M_{Z_n}(t)\to M_Z(t)$ for all $t$, where $Z$ has mgf $M_Z$ and cdf $F_Z$, then $F_{Z_n}(x)\to F_Z(x)$ at every $x$ where $F_Z$ is continuous.

**Proof of the CLT under the assumption that the common mgf $M(t)$ of the $X_i$ exists.**
1. Standardise: $Y_i=(X_i-\mu)/\sigma$ has $E(Y_i)=0$, $\operatorname{Var}(Y_i)=1$, and $\frac{\bar Y_n-\mu_Y}{\sigma_Y/\sqrt n}=\frac{\bar X_n-\mu}{\sigma/\sqrt n}$, so WLOG $\mu=0,\sigma=1$.
2. By the lemma it suffices to show the mgf of $\frac{\bar X_n-\mu}{\sigma/\sqrt n}=\frac1{\sqrt n}\sum X_i$ tends to $M_{N(0,1)}(t)=e^{t^2/2}$. That mgf is $M(t/\sqrt n)^n$.
3. Let $L(t)=\ln M(t)$. Then $L(0)=\ln1=0$, $L'(0)=M'(0)/M(0)=0$, and $L''(0)=\Big(\dfrac{M''(t)}{M(t)}-\dfrac{M'(t)^2}{M(t)^2}\Big)\Big|_{t=0}=1-0=1$.
4. It is enough to show $nL(t/\sqrt n)\to t^2/2$. With $y=1/\sqrt n$: $\lim_{y\to0}\dfrac{L(ty)}{y^2}$ is of form $0/0$ (as $L(0)=0$); L'Hôpital gives $\lim\dfrac{tL'(ty)}{2y}$, again $0/0$ because $L'(0)=0$; once more gives $\lim\dfrac{t^2L''(ty)}{2}=\dfrac{t^2}2$ because $L''(0)=1$.

**Example 1.** A fair die is rolled 10 times; approximate in terms of $\Phi$ the probability that the total is between 30 and 40 inclusive. $E(X_i)=7/2$, $\operatorname{Var}(X_i)=\frac{91}6-\frac{49}4=\frac{35}{12}$. With the continuity correction, $P(29.5\le X\le40.5)=P\big(-\tfrac{0.55}{\sqrt{35/120}}\le\frac{\bar X-7/2}{\sqrt{35/120}}\le\tfrac{0.55}{\sqrt{35/120}}\big)=2\Phi\big(\tfrac{0.55}{\sqrt{35/120}}\big)-1$ (the working on the page writes the half-width as 0.55 for the mean, $\bar X\in[2.95,4.05]$).

**Example 2.** $X_1,\dots,X_{10}$ i.i.d. $\text{Unif}(0,1)$; approximate $P(\sum X_i>6)$. $P(\bar X>0.6)=P\Big(\frac{\bar X-0.5}{\sqrt{1/120}}>\frac{0.1}{\sqrt{1/120}}\Big)=1-\Phi(\sqrt{1.2})$ (using $\operatorname{Var}=1/12$, so the standard deviation of $\bar X$ is $\sqrt{1/120}$).

## From the post
Week 7 lecture summary attached. There are two examples also, which were not discussed in class, due to lack of time.

There is NO review lecture tomorrow, 19 November. Instead, I will post a video lecture for the review, later.

## Files
- [week7_lectures.pdf](https://drive.google.com/file/d/1YmVukB4Vn3AIEiqJSr9E5UAjcVYtuwHr/view?usp=drive_web) (handwritten; read from page images)

## Related
- [[introduction-to-probability/2026-11-18-week-6-lectures-summary]]: Chebyshev and the weak law, which the CLT refines
- [[introduction-to-probability/2026-10-29-week-4-notes]]: mgfs, used in the proof
- [[introduction-to-probability/2026-10-22-hw3-problems-and-median-clarification]]: mgf problems (HW3)
- [[08-Probability/PR06 Moments Generating Functions and Limit Theorems]]: vault chapter on mgfs and limit theorems
