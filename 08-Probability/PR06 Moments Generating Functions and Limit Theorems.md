---
title: PR06 Moments Generating Functions and Limit Theorems
aliases: [PR06, moment generating function, MGF, skewness, kurtosis, Chebyshev, law of large numbers, central limit theorem]
subject: probability
type: chapter
chapter: 6
part: IV
scope: [extra-book, extra-beyond]
by: [ai-notes]
status: draft
prereq: [PR04 Joint Distributions Expectation and Variance, PR05 Continuous Random Variables]
tags: [subject/probability, type/chapter, extra/book, extra/beyond, src/ai-notes, src/own-notes, status/draft]
---
# PR06 · Moments, Generating Functions and Limit Theorems

◀ [[PR05 Continuous Random Variables]] · [[Probability - Course Map]]

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Scope of this chapter
> No lecture note in the folder covers MGFs or limit theorems. The AI-written `probability_moments_and_mgf_notes.pdf` states a **course policy**: MGFs and their general theorems may be used in homework and exams, but **the algebraic form of the MGF of any named distribution must first be derived from first principles in the solution**. I therefore treat this chapter as 🟡 (likely to be needed, but not yet backed by a lecture note) and derive every MGF below from the definition. **Ask the instructor** whether the central limit theorem, Chebyshev's inequality and the law of large numbers are examinable.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟡 **Extra · book** (AI notes `probability_moments_and_mgf_notes.pdf`, checked line by line; textbooks Ross Ch. 7–8, Blitzstein and Hwang Ch. 6 and 10)
> - §1 skewness and kurtosis; existence of moments (Cauchy)
> - §2 the MGF: definition, moments by differentiation, linear maps, sums of independent variables, uniqueness (stated)
> - §3 first-principles MGFs of the Bernoulli, binomial, Poisson, geometric, negative binomial, uniform, exponential, normal
> - §4 applications: sum of independent Poissons and normals; the Poisson limit via MGFs
> - §5 Markov and Chebyshev inequalities, the law of large numbers, the central limit theorem and the normal approximation
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §5 the $1/\sqrt n$ rate of the CLT checked against the exact Gamma distribution (leading Edgeworth term $\gamma_1/(6\sqrt{2\pi n})$ agrees to four digits); symbolic checks of every MGF with `sympy` (`scripts/pr_numbers.py`)

> [!key] After this chapter you can
> - compute **skewness** and **kurtosis** and say which moments of a distribution exist,
> - **derive** an MGF from the definition, read off $E[X^k]=M^{(k)}(0)$, and use $M_{aX+b}$ and $M_{\sum X_i}=\prod M_{X_i}$,
> - prove that independent normals (and Poissons) add, and that Binomial$(n,c/n)\to$ Poisson$(c)$, using MGFs,
> - state and apply **Markov, Chebyshev, the law of large numbers and the CLT**, with the continuity correction for the binomial.

> [!intuition] The one-sentence story
> The MGF $E[e^{tX}]$ packs all moments into one function; because $e^{t(X+Y)}=e^{tX}e^{tY}$ it turns sums of independent variables into products, which is why sums of many small independent pieces converge to the normal curve.

## 1. Higher moments, skewness and kurtosis
<span class="scope-extra-book">extra · book</span> *AI notes §1.1–1.4*

Raw moments $E[X^k]$ and central moments $\mu_k=E[(X-\mu)^k]=\sum_{j=0}^k\binom kj(-\mu)^{k-j}E[X^j]$ (binomial expansion, linearity). The standardised third and fourth moments are

> [!key] Shape numbers
> $$\text{skewness }\gamma_1=\frac{E[(X-\mu)^3]}{\sigma^3},\qquad\text{kurtosis }\alpha_4=\frac{E[(X-\mu)^4]}{\sigma^4},\qquad\text{excess kurtosis }\gamma_2=\alpha_4-3 .$$
> $\gamma_1=0$ for any distribution symmetric about its mean (the cube is an odd function); $\gamma_1>0$: long right tail. $\gamma_2=0$ for the normal; $\gamma_2>0$ means heavier tails and a sharper peak than the normal, $\gamma_2<0$ lighter tails.

> [!example] Values (recomputed)
> Exponential$(\lambda)$: $E[X^k]=k!/\lambda^k$, so $\mu_3=\tfrac6{\lambda^3}-3\tfrac1\lambda\tfrac2{\lambda^2}+2\tfrac1{\lambda^3}=\tfrac2{\lambda^3}$, $\gamma_1=2$ for every $\lambda$, $\gamma_2=6$. Normal: $E[Z^4]=3$ (by parts: $\int_0^\infty x^4e^{-x^2/2}=3\int_0^\infty x^2e^{-x^2/2}$), so $\gamma_2=0$; more generally $E[Z^{2k}]=\tfrac{(2k)!}{2^kk!}=1,3,15,105,945,\dots$ Uniform: $\gamma_2=-1.2$. Bernoulli$(\tfrac12)$: $\gamma_2=-2$. Poisson$(3.2)$: $\gamma_1=1/\sqrt\lambda=0.559$, $\gamma_2=1/\lambda=0.3125$.

> [!key] Do the moments exist? (Theorem 1.9 of the AI notes)
> If $E|X|^s<\infty$ then $E|X|^r<\infty$ for $0<r<s$, because $|X|^r\le1+|X|^s$. So existence of a high moment implies existence of all lower ones.

> [!example] The Cauchy distribution has no mean
> $f(x)=\dfrac1{\pi(1+x^2)}$: $E|X|=\dfrac2\pi\displaystyle\int_0^\infty\frac{x\,\mathrm dx}{1+x^2}=\dfrac1\pi\big[\ln(1+x^2)\big]_0^\infty=\infty$. So $E[X]$ is undefined, and so are the variance and the MGF. The running mean of Cauchy samples never settles (Figure PR6.1 B). A Pareto$(x_m,\alpha)$ density has $E[X^k]<\infty$ iff $k<\alpha$; for $\alpha=1.5$ the mean is finite ($3x_m$) and the variance infinite.

![[fig_pr06_limits.png]]
*Figure PR6.1. A: the Binomial$(30,0.3)$ pmf and its normal approximation; $P(X\le10)$ exact $0.7304$, with continuity correction $0.7250$, without $0.6548$. B: running means of 5000 draws (two runs each): the normal mean converges, the Cauchy mean does not.*

## 2. The moment generating function
<span class="scope-extra-book">extra · book</span> *AI notes §2.2*

> [!key] Definition and basic theorems
> $$M_X(t)=E\big[e^{tX}\big]=\sum_xe^{tx}p(x)\ \text{ or }\ \int e^{tx}f(x)\,\mathrm dx,$$
> defined for those $t$ where it is finite; "the MGF exists" means it is finite on some interval $(-h,h)$.
> 1. **Moments:** $E[X^k]=M_X^{(k)}(0)$.
> 2. **Linear map:** $M_{aX+b}(t)=e^{bt}M_X(at)$.
> 3. **Independent sum:** $M_{X_1+\dots+X_n}(t)=\prod_iM_{X_i}(t)$.
> 4. **Uniqueness (stated):** if $M_X=M_Y$ on an interval around 0 then $X$ and $Y$ have the same cdf.
> 5. **Continuity (stated):** if $M_{X_n}(t)\to M_X(t)$ for $|t|<h$ then $X_n\to X$ in distribution.

> [!derivation] Proofs of 1–3
> 1. Expand $e^{tX}=\sum_k\tfrac{t^k}{k!}X^k$ and take expectations term by term: $M_X(t)=\sum_k\tfrac{t^k}{k!}E[X^k]$; the coefficient of $t^k/k!$ is $E[X^k]$, so the $k$-th derivative at 0 is $E[X^k]$.
> 2. $E[e^{t(aX+b)}]=e^{bt}E[e^{(at)X}]=e^{bt}M_X(at)$.
> 3. $E[e^{t\sum X_i}]=E[\prod e^{tX_i}]=\prod E[e^{tX_i}]$, since for independent variables the expectation of a product is the product of expectations (PR04 §6).

## 3. First-principles MGFs
<span class="scope-extra-book">extra · book</span> *AI notes §2.3 (course policy: derive before use). Every result below was also checked symbolically.*

Write $q=1-p$.

> [!derivation] Bernoulli, binomial
> **Bernoulli$(p)$:** $M(t)=e^{t\cdot0}q+e^{t\cdot1}p=q+pe^t$.
> **Binomial$(n,p)$:** $M(t)=\sum_{k=0}^ne^{tk}\binom nkp^kq^{n-k}=\sum_k\binom nk(pe^t)^kq^{n-k}=(q+pe^t)^n$ (binomial theorem).
> *Moments:* $M'(t)=npe^t(q+pe^t)^{n-1}\Rightarrow E[X]=np$; $M''(0)=n(n-1)p^2+np\Rightarrow\mathrm{Var}=np(1-p)$ (agrees with PR04).

> [!derivation] Poisson$(\lambda)$
> $M(t)=\sum_{k\ge0}e^{tk}e^{-\lambda}\dfrac{\lambda^k}{k!}=e^{-\lambda}\sum_k\dfrac{(\lambda e^t)^k}{k!}=e^{-\lambda}e^{\lambda e^t}=\exp\big(\lambda(e^t-1)\big)$ for all $t$.
> $M'=\lambda e^tM\Rightarrow E[X]=\lambda$; $M''(0)=\lambda^2+\lambda$; $M'''(0)=\lambda^3+3\lambda^2+\lambda$ (matches the recursion of PR04 §4: $E[X^3]=22$ for $\lambda=2$).

> [!derivation] Geometric$(p)$ and negative binomial$(r,p)$ (trials)
> $M(t)=\sum_{n\ge1}e^{tn}q^{n-1}p=pe^t\sum_{n\ge0}(qe^t)^n=\dfrac{pe^t}{1-qe^t}$ for $qe^t<1$, i.e. $t<-\ln q$. Then $M'(0)=\tfrac1p$ and $M''(0)-M'(0)^2=\tfrac{1-p}{p^2}$. Since NegBin$(r,p)$ is a sum of $r$ independent geometrics, $M(t)=\Big(\dfrac{pe^t}{1-qe^t}\Big)^r$, mean $r/p$, variance $r(1-p)/p^2$ (PR04).

> [!derivation] Uniform, exponential
> **Uniform$(a,b)$:** $M(t)=\int_a^b\dfrac{e^{tx}}{b-a}\mathrm dx=\dfrac{e^{tb}-e^{ta}}{t(b-a)}$ ($t\ne0$, $M(0)=1$); for $U(0,1)$, $M(t)=\tfrac{e^t-1}t=\sum_k\tfrac{t^k}{(k+1)!}$ so $E[X^k]=\tfrac1{k+1}$.
> **Exponential$(\lambda)$:** $M(t)=\lambda\int_0^\infty e^{-(\lambda-t)x}\mathrm dx=\dfrac\lambda{\lambda-t}$ for $t<\lambda$; expanding, $\sum_k(t/\lambda)^k$, so $E[X^k]=k!/\lambda^k$.

> [!derivation] Standard normal and $N(\mu,\sigma^2)$
> $M_Z(t)=\dfrac1{\sqrt{2\pi}}\displaystyle\int e^{tx}e^{-x^2/2}\mathrm dx$. Complete the square, $x^2-2tx=(x-t)^2-t^2$:
> $$M_Z(t)=e^{t^2/2}\cdot\frac1{\sqrt{2\pi}}\int e^{-(x-t)^2/2}\mathrm dx=e^{t^2/2},$$
> since the last integral is the total mass of an $N(t,1)$ density. With $X=\mu+\sigma Z$ and the linear-map rule, $M_X(t)=e^{\mu t}M_Z(\sigma t)=\exp\big(\mu t+\tfrac12\sigma^2t^2\big)$. Differentiating gives $E[X]=\mu$, $\mathrm{Var}[X]=\sigma^2$ and $E[(X-\mu)^4]=3\sigma^4$; the series $e^{t^2/2}=\sum_k\tfrac{t^{2k}}{2^kk!}$ gives $E[Z^{2k}]=\tfrac{(2k)!}{2^kk!}$.

> [!pitfall] Existence region
> The exponential MGF exists only for $t<\lambda$, the geometric for $t<-\ln q$, the Cauchy for no $t\neq0$. A formula without its domain is incomplete, and uniqueness needs an interval around 0.

## 4. Applications of MGFs
<span class="scope-extra-book">extra · book</span> *AI notes §2.4*

> [!example] Independent normals add
> $X\sim N(\mu_1,\sigma_1^2)$ and $Y\sim N(\mu_2,\sigma_2^2)$ independent: $M_{X+Y}(t)=\exp\big(\mu_1t+\tfrac12\sigma_1^2t^2\big)\exp\big(\mu_2t+\tfrac12\sigma_2^2t^2\big)=\exp\big((\mu_1+\mu_2)t+\tfrac12(\sigma_1^2+\sigma_2^2)t^2\big)$, which is the MGF of $N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$; by uniqueness $X+Y$ has that law. Numeric check: for $\mu=1$, $\sigma=2$, $t=0.3$ the MGF is $1.6161$ both from the formula and by direct integration.

> [!example] Independent Poissons add (🔵)
> $M_{X+Y}(t)=e^{\lambda_1(e^t-1)}e^{\lambda_2(e^t-1)}=e^{(\lambda_1+\lambda_2)(e^t-1)}$: $X+Y\sim$ Poisson$(\lambda_1+\lambda_2)$. Similarly $\sum$ of $n$ iid Bernoulli$(p)$ has MGF $(q+pe^t)^n$, which proves that the sum is binomial.

> [!derivation] The Poisson limit by MGFs (🔵; compare PR03 §5)
> $X_n\sim$ Bin$(n,c/n)$ has $M_n(t)=\big(1+\tfrac cn(e^t-1)\big)^n\to e^{c(e^t-1)}$ as $n\to\infty$, using $(1+a_n/n)^n\to e^{a}$ when $a_n\to a$. This is the MGF of Poisson$(c)$, so by the continuity theorem Bin$(n,c/n)\to$ Poisson$(c)$ in distribution. Numerically at $t=0.7$, $c=3.2$: $M_{100}=24.349$, $M_{10^4}=25.623$, $M_{10^6}=25.636$, limit $25.636$.

## 5. Inequalities and limit theorems
<span class="scope-extra-book">extra · book</span> *AI notes Example 2.8 and §1.5; Ross Ch. 8; Blitzstein and Hwang Ch. 10*

> [!key] Markov and Chebyshev
> - **Markov:** $X\ge0$, $a>0$: $P[X\ge a]\le\dfrac{E[X]}a$ (since $a\mathbf 1\{X\ge a\}\le X$).
> - **Chebyshev:** $P\big[|X-\mu|\ge k\sigma\big]\le\dfrac1{k^2}$ (Markov applied to $(X-\mu)^2$ and $a=k^2\sigma^2$).
> They hold for every distribution with the needed moments, and are therefore loose. For $k=2$ the bound is $0.25$ against the true tail probabilities $0.0455$ (normal) and $0.0498$ (Exp$(1)$); for $k=3$: $0.111$ against $0.0027$ and $0.0183$. Markov for Exp$(1)$ at $a=3$: $\tfrac13$ against $e^{-3}=0.0498$.

> [!key] Weak law of large numbers
> If $X_1,X_2,\dots$ are independent with the same mean $\mu$ and variance $\sigma^2$, and $\bar X_n=\tfrac1n\sum X_i$, then $E[\bar X_n]=\mu$, $\mathrm{Var}[\bar X_n]=\sigma^2/n$ (PR04 §6), and by Chebyshev
> $$P\big[|\bar X_n-\mu|>\varepsilon\big]\le\frac{\sigma^2}{n\varepsilon^2}\to0 .$$
> For the mean of $n=100$ dice and $\varepsilon=0.25$: bound $0.467$, true probability $0.135$ (simulation of 200,000 runs).

> [!key] Central limit theorem
> If $X_i$ are iid with mean $\mu$ and variance $\sigma^2>0$ (MGF finite near 0), then
> $$S_n^*=\frac{\sum_{i=1}^nX_i-n\mu}{\sigma\sqrt n}\ \xrightarrow{\ d\ }\ N(0,1),\qquad\text{i.e. }P[S_n^*\le x]\to\Phi(x).$$

> [!derivation] Proof by MGFs (AI notes Example 2.8)
> Put $Z_i=(X_i-\mu)/\sigma$, so $E[Z_i]=0$, $E[Z_i^2]=1$ and $S_n^*=\tfrac1{\sqrt n}\sum Z_i$. By independence $M_{S_n^*}(t)=\big[M_Z(t/\sqrt n)\big]^n$. Taylor-expanding $M_Z(s)=1+0\cdot s+\tfrac12s^2+o(s^2)$ at $s=t/\sqrt n$:
> $$M_{S_n^*}(t)=\Big(1+\frac{t^2}{2n}+o\big(\tfrac1n\big)\Big)^n\longrightarrow e^{t^2/2},$$
> the $N(0,1)$ MGF. The continuity theorem gives convergence in distribution. (The Lyapunov version allows non-identical independent terms provided $\sum E|X_i-\mu_i|^{2+\delta}/s_n^{2+\delta}\to0$, so that no single term dominates the variance.)

![[fig_pr06_clt.png]]
*Figure PR6.2. A: standardised sums of $n$ iid Exp$(1)$ variables (Gamma$(n,1)$ densities) against the standard normal. B: the largest gap between the exact cdf and $\Phi$ falls like $1/\sqrt n$ and follows the leading Edgeworth term $\gamma_1/(6\sqrt{2\pi n})$ with $\gamma_1=2$ (🔵).*

> [!example] Using the CLT: the normal approximation to a binomial
> $X\sim$ Bin$(n,p)$ is a sum of $n$ Bernoulli variables, so $X\approx N(np,\,npq)$. Since $X$ is integer-valued, use the **continuity correction** $P[X\le k]\approx\Phi\Big(\dfrac{k+\frac12-np}{\sqrt{npq}}\Big)$. Bin$(30,0.3)$, $P[X\le10]$: exact $0.7304$; corrected $\Phi\big(\tfrac{10.5-9}{2.51}\big)=0.7250$; uncorrected $0.6548$. Bin$(100,0.5)$, $P[X\le45]$: exact $0.18410$, corrected $0.18406$, uncorrected $0.1587$. Poisson$(100)$, $P[X\le90]$: exact $0.1714$, corrected normal $0.1711$.

> [!pitfall] The CLT needs a finite variance
> For Cauchy variables the sample mean has the **same** Cauchy distribution for every $n$ (its MGF does not exist), so neither the law of large numbers nor the CLT applies (Figure PR6.1 B). Likewise Pareto with $\alpha\le2$.

## Map of this chapter
> [!connection] How PR06 connects
> **Builds on:** [[PR04 Joint Distributions Expectation and Variance]] (variance of a sum, independence) and [[PR05 Continuous Random Variables]] (the normal and exponential densities).
> **Leads to:** statistics and stochastic processes (confidence intervals, Poisson processes, random walks).
> **Concepts:** [[Moment Generating Function]] · [[Skewness and Kurtosis]] · [[Markov and Chebyshev Inequalities]] · [[Law of Large Numbers]] · [[Central Limit Theorem]] · [[Normal Approximation to the Binomial]] · [[Cauchy Distribution]] · [[Poisson Limit Theorem]]
> **Other subjects:** [[Probability - Course Map]], [[TH06 From Kinetic Theory to Statistical Mechanics]] (the partition function is a Laplace transform of the density of states, the same device as an MGF with $t=-\beta$; fluctuations $\sim1/\sqrt N$ are the CLT), [[QM01 From Waves to Probabilities]] (Fourier transform of a Gaussian is a Gaussian, the characteristic function version of the CLT), [[Akaike Information Criterion]] (large-sample normal approximations of the likelihood).

## Summary
> [!summary] Cheat-sheet
> - $\gamma_1=\mu_3/\sigma^3$, $\gamma_2=\mu_4/\sigma^4-3$. Exp: $\gamma_1=2$, $\gamma_2=6$; normal $\gamma_2=0$; uniform $-1.2$; Poisson $1/\sqrt\lambda$, $1/\lambda$.
> - $M_X(t)=E[e^{tX}]$; $E[X^k]=M^{(k)}(0)$; $M_{aX+b}=e^{bt}M_X(at)$; $M_{\sum}=\prod M_i$ (independent); equal MGFs near 0 ⇒ equal laws.
> - **MGFs (derive first):** Bern $q+pe^t$; Bin $(q+pe^t)^n$; Poisson $e^{\lambda(e^t-1)}$; Geom $\frac{pe^t}{1-qe^t}$; NegBin its $r$-th power; Unif $\frac{e^{tb}-e^{ta}}{t(b-a)}$; Exp $\frac\lambda{\lambda-t}$ ($t<\lambda$); $N(\mu,\sigma^2)$ $e^{\mu t+\sigma^2t^2/2}$.
> - Markov $P[X\ge a]\le E[X]/a$; Chebyshev $P[|X-\mu|\ge k\sigma]\le1/k^2$; WLLN $P[|\bar X-\mu|>\varepsilon]\le\sigma^2/(n\varepsilon^2)$; **CLT** $(S_n-n\mu)/(\sigma\sqrt n)\to N(0,1)$, error $\sim\gamma_1/(6\sqrt{2\pi n})$.
> - Binomial $\approx N(np,npq)$ with continuity correction; Cauchy: no mean, no CLT.

## Practice
1. **MGF from scratch.** Derive the MGF of $X$ with $P[X=-1]=\tfrac14$, $P[X=0]=\tfrac12$, $P[X=2]=\tfrac14$, and use it to find $E[X]$ and $E[X^2]$.
2. **Binomial.** Show from the definition that Bin$(n,p)$ has MGF $(q+pe^t)^n$ and use it to find the third raw moment of Bin$(4,0.5)$.
3. **Exponential.** Derive the MGF of Exp$(\lambda)$ and find $E[X^3]$. For which $t$ is it finite?
4. **Uniqueness.** A variable has MGF $\big(\tfrac13+\tfrac23e^t\big)^5$. Identify its distribution and find $P[X=3]$.
5. **Sums.** $X\sim$ Poisson$(2)$ and $Y\sim$ Poisson$(3)$ are independent. Find $P[X+Y=4]$ using the MGF argument.
6. **Normal sum.** $X\sim N(1,4)$ and $Y\sim N(-2,9)$ independent. Find $P[X+Y>2]$ and $P[2X-Y<5]$.
7. **Chebyshev.** A variable has mean 50 and standard deviation 5. Give a lower bound for $P[40<X<60]$ and compare with the normal value.
8. **WLLN.** How many tosses of a fair coin guarantee, by Chebyshev, that the proportion of heads is within $0.05$ of $\tfrac12$ with probability at least $0.95$?
9. **CLT.** 100 independent fair dice are rolled. Approximate $P[\text{sum}\le340]$.
10. **Continuity correction.** Approximate $P[X\ge60]$ for $X\sim$ Bin$(100,0.5)$, with and without the correction, and compare with the exact value $0.0284$.

> [!example]- Solutions
> 1. $M(t)=\tfrac14e^{-t}+\tfrac12+\tfrac14e^{2t}$. $M'(0)=-\tfrac14+\tfrac12=\tfrac14$, so $E[X]=\tfrac14$; $M''(0)=\tfrac14+1=\tfrac54$, so $E[X^2]=\tfrac54$ (check from the pmf: $\tfrac14+\tfrac{4}{4}=\tfrac54$ ✓).
> 2. $M(t)=\sum_k\binom nk(pe^t)^kq^{n-k}=(q+pe^t)^n$. For $n=4$, $p=q=\tfrac12$: $M=\tfrac1{16}(1+e^t)^4$; $E[X^3]=\tfrac1{16}\sum_kk^3\binom4k=\tfrac{4+48+108+64}{16}=\tfrac{224}{16}=14$, in agreement with the factorial-moment formula $np+3n(n-1)p^2+n(n-1)(n-2)p^3=2+3\cdot3+3=14$.
> 3. $M(t)=\dfrac\lambda{\lambda-t}$ for $t<\lambda$; $E[X^3]=3!/\lambda^3=6/\lambda^3$.
> 4. $(q+pe^t)^n$ with $p=\tfrac23$, $n=5$: Bin$(5,\tfrac23)$ by uniqueness; $P[X=3]=\binom53(\tfrac23)^3(\tfrac13)^2=10\cdot\tfrac8{27}\cdot\tfrac19=\tfrac{80}{243}=0.3292$.
> 5. $M_{X+Y}=e^{5(e^t-1)}$, so Poisson$(5)$: $P[X+Y=4]=e^{-5}\tfrac{5^4}{24}=0.1755$.
> 6. $X+Y\sim N(-1,13)$: $P[X+Y>2]=P[Z>3/\sqrt{13}=0.832]=0.2027$. $2X-Y\sim N(2+2,\,16+9)=N(4,25)$: $P[2X-Y<5]=\Phi(0.2)=0.5793$.
> 7. $P[|X-50|<10]=P[|X-\mu|<2\sigma]\ge1-\tfrac14=0.75$. For a normal: $0.9545$.
> 8. $\mathrm{Var}[\bar X]=\tfrac1{4n}$; $\tfrac{1}{4n(0.05)^2}\le0.05\Rightarrow n\ge\tfrac{1}{4\cdot0.0025\cdot0.05}=2000$.
> 9. Mean $350$, variance $100\cdot\tfrac{35}{12}=291.67$, $\sigma=17.08$. $P[S\le340]\approx\Phi\big(\tfrac{340.5-350}{17.08}\big)=\Phi(-0.556)=0.289$.
> 10. $\mu=50$, $\sigma=5$. Corrected: $P[X\ge60]=1-\Phi\big(\tfrac{59.5-50}5\big)=1-\Phi(1.9)=0.0287$; uncorrected $1-\Phi(2)=0.0228$; exact $0.0284$.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | moments, skewness, kurtosis, Cauchy, Pareto, Lyapunov | `probability_moments_and_mgf_notes.pdf` §1 (AI-written) | extra/book |
> | MGF definition and theorems, first-principles MGFs, normal sum, CLT proof | same file §2 (AI-written, including the course-policy remark) | extra/book |
> | Markov, Chebyshev, WLLN, continuity correction | Ross Ch. 8 (text layer, not opened); Blitzstein and Hwang Ch. 10 | extra/book |
> | symbolic and numeric checks, Edgeworth comparison, figures | `scripts/pr_numbers.py`, `fig_pr06_limits.py`, `fig_pr06_clt.py` | extra/beyond |
>
> **Notes.** The AI notes cite "Theorem 1.7" for the statement that $E|X|=\infty$ implies $E|X|^k=\infty$ for $k\ge1$; the theorem they state is numbered 1.9 and gives the converse form used above. The proofs of uniqueness and of the continuity theorem are not given (they need characteristic functions or measure theory).

**References.** Ross, S. *A First Course in Probability* (8th ed.), Ch. 7–8 · Blitzstein, J. K. and Hwang, J. *Introduction to Probability*, Ch. 6, 10 · Lyapunov, A. M. (1901) *Nouvelle forme du théorème sur la limite de probabilité*.
