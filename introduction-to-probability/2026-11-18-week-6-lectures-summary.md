---
id: introduction-to-probability/2026-11-18-week-6-lectures-summary
aliases: [Week 6 lectures summary]
tags: [probability, mt2113, lecture-notes]
trust_tier: agent_written
---

# Week 6 lectures summary

## Covered
Source: handwritten PDF week6_lectures.pdf, read from the page images (formulas worth checking against the file).

**Cauchy-Schwarz inequality.** For random variables $X,Y$: $|E(XY)|\le\sqrt{E(X^2)E(Y^2)}$.
- Proof 1: $E((X+tY)^2)\ge0$ gives $E(X^2)+2tE(XY)+t^2E(Y^2)\ge0$ for all $t$. If $E(Y^2)=0$, the inequality forces $E(XY)=0$ and the claim holds. If $E(Y^2)\ne0$, complete the square: $\big(t\sqrt{E(Y^2)}+E(XY)/\sqrt{E(Y^2)}\big)^2+E(X^2)-E(XY)^2/E(Y^2)\ge0$, so $E(X^2)-E(XY)^2/E(Y^2)\ge0$.
- Proof 2: $|E(XY)|=|\operatorname{Cov}(X,Y)+E(X)E(Y)|\le|E(X)||E(Y)|+\sqrt{\operatorname{Var}X\operatorname{Var}Y}$, which is a dot product of the vectors $(|E(X)|,\sqrt{\operatorname{Var}X})$ and $(|E(Y)|,\sqrt{\operatorname{Var}Y})$. The Cauchy-Schwarz inequality for vectors bounds it by $\sqrt{(|E X|^2+\operatorname{Var}X)(|E Y|^2+\operatorname{Var}Y)}=\sqrt{E(X^2)E(Y^2)}$.

**Application (joint mgf exists).** If $\vec X=(X_1,X_2)$ has a joint distribution and the marginals have mgfs $M_{X_1}(t),M_{X_2}(t)$ finite for $|t|<2\epsilon$, then $M_{\vec X}(t_1,t_2)=E(e^{t_1X_1+t_2X_2})$ is finite for $|t_1|,|t_2|<\epsilon$. Proof: $E(e^{t_1X_1}e^{t_2X_2})\le\sqrt{E(e^{2t_1X_1})E(e^{2t_2X_2})}=\sqrt{M_{X_1}(2t_1)M_{X_2}(2t_2)}<\infty$.

**Jensen's inequality.** If $g:\mathbb R\to\mathbb R$ has $g''(x)\ge0$ for all $x$, then $E(g(X))\ge g(E(X))$. Example: $g(x)=x^2$ gives $E(X^2)-(E X)^2=\operatorname{Var}X\ge0$.
Proof: (by the HW problem) the graph of $g$ lies above its tangent line at any point. Take the tangent at $(\mu,g(\mu))$ with $\mu=E(X)$: $g(X)\ge(X-\mu)g'(\mu)+g(\mu)$. Use that $Y\ge X$ implies $E(Y)\ge E(X)$ (since $E(Y-X)\ge0$). Taking expectations, $E(g(X))\ge g'(\mu)E(X-\mu)+g(\mu)=g(E(X))$, as $E(X-\mu)=0$.

**Markov's inequality.** For a non-negative random variable $X$ and $a>0$: $P(X\ge a)\le E(X)/a$.
Proof: pass to $X/a$ so that $a=1$. Let $Y=1$ if $X\ge1$ and $0$ otherwise. Then $Y\le X$ in both cases, so $P(X\ge1)=E(Y)\le E(X)$.

**Chebyshev's inequality.** For $X$ with mean $\mu$ and variance $\sigma^2$, and any $a>0$: $P\big(\left|\frac{X-\mu}{\sigma}\right|\ge a\big)\le\frac1{a^2}$ (the probability of being $a$ or more standard deviations from the mean is at most $1/a^2$).
Proof: apply Markov to $Y=(X-\mu)^2/\sigma^2\ge0$: $P(Y\ge a^2)\le E(Y)/a^2=1/a^2$, since $E(Y)=1$.

**Law of large numbers.** Let $X_1,X_2,\dots$ be i.i.d. with mean $\mu$ and variance $\sigma^2$; sample mean $\bar X_n=(X_1+\dots+X_n)/n$.
- Weak law (WLLN): $\bar X_n\to\mu$ in probability, i.e. for every $\epsilon>0$, $P(|\bar X_n-\mu|>\epsilon)\to0$ as $n\to\infty$.
- Proof: $\operatorname{Var}(\bar X_n)=\sigma^2/n$; by Chebyshev $P(|\bar X_n-\mu|\ge\epsilon)\le\dfrac{\sigma^2}{n\epsilon^2}$, and the sandwich theorem gives the limit $0$.
- Strong law (stated without proof): $\bar X_n\to\mu$ pointwise with probability 1, i.e. $\lim_n\bar X_n(x)=\mu$ for all $x\in S$ except a set $B$ with $P(B)=0$.

## From the post
Week 6 lectures summary

## Files
- [week6_lectures.pdf](https://drive.google.com/file/d/1y9A6kNUlv2_pNKaMX31n2DgxOOOo56kh/view?usp=drive_web) (handwritten; read from page images)

## Related
- [[introduction-to-probability/2026-11-12-hw-6]]: HW 6 Q3 is the tangent-line fact used in the proof of Jensen
- [[introduction-to-probability/2026-11-05-week-5-notes]]: covariance and $|\operatorname{corr}|\le1$, the Cauchy-Schwarz idea in the second proof of this week
- [[introduction-to-probability/2026-11-18-week-7-lectures-summary]]: the next week, CLT, building on the weak law
- [[08-Probability/PR06 Moments Generating Functions and Limit Theorems]]: vault chapter on mgfs and limit theorems
