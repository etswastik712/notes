---
title: MT2113 Past Papers 2024 - Solved
aliases: [Probability midsem 2024, Probability endsem 2024, MT2113 2024, probability quizzes 2024]
subject: probability
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/probability, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# MT2113 Introduction to Probability: Mid-sem, End-sem and Quizzes 2024, Solved

[[Probability - Course Map|Course Map]] · [[Probability Quiz Prep]] · other years: [[MT2113 Past Papers 2022 - Solved|2022]] · [[MT2113 Past Papers 2023 - Solved|2023]] · [[MT2113 Past Papers 2025 - Solved|2025]] · [[MT2113 MCQ Paper (undated) - Solved|undated MCQ paper]]

<span class="scope-taught">taught · past papers (Moumanti Podder, Kaneenika Sinha)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine, checked against the official keys)</span>

> [!info] The papers
> From the Drive archive, folder `Sem - 3 Papers (Aug 2024)`:
> - **Mid-sem**, 20 Sep 2024, 37 points (cap 30), with official solutions.
> - **End-sem**, 27 Nov 2024, 30 points: two phone photographs, plus `Probability-end-sem-solutions-2024.pdf`.
> - **Seven quizzes**: 12 Aug, 26 Aug (with a key), 9 Sep, 14 Oct, 28 Oct, 11 Nov and 18 Nov (numbered 1–7 below).
>
> `MT2113/Intro Probability-All Papers 2024-...pdf` (11 pp., scan, no text layer) is probably the same set bundled together; I did not open it page by page. I solved everything independently and then compared with the official keys; the **end-sem key has one mismatch with the paper** (Q4a, flagged below). Numbers: `scripts/pr_qp_archive_numbers.py`.

## Mid-semester examination (20 September 2024)

> [!question] Q1 · 1000 subscribers: 312 professionals, 470 married, 525 graduates; 42 professional graduates, 147 married graduates, 86 married professionals, 25 all three. Show the data are wrong.

> [!example]- Solution ([[PR01 Counting and the Axioms of Probability]])
> Inclusion–exclusion: $|P\cup M\cup C|=312+470+525-42-147-86+25=\mathbf{1057}>1000$. A union cannot contain more people than were surveyed. (Matches the key.)

> [!question] Q2 · 8 indistinguishable rooks placed at random on a chessboard. Probability no two attack each other?

> [!example]- Solution
> There are $\binom{64}8$ equally likely sets of squares. Non-attacking means exactly one rook per row and per column. Row $i$'s rook sits in column $a_i$, and $(a_1,\dots,a_8)$ must be a permutation, so there are $8!$ good placements:
> $$P=\frac{8!}{\binom{64}{8}}=\mathbf{9.11\times10^{-6}}.$$

> [!question] Q3 · Accident probabilities 0.05 / 0.15 / 0.30 for good / average / bad risks (20 / 50 / 30 %). A policyholder had no accident: probability they are good-risk?

> [!example]- Solution ([[PR02 Conditional Probability Bayes Rule and Independence]])
> $$P(G\mid E^c)=\frac{0.95\times0.2}{0.95\times0.2+0.85\times0.5+0.70\times0.3}=\frac{0.19}{0.825}=\mathbf{0.230}.$$
> It is only slightly above the prior 0.2, because a quiet year is common for every class.

> [!question] Q4 · On day: each examiner passes him with probability 0.8; off day 0.4; off days twice as likely as on days. Majority needed. 3 examiners or 5?

> [!example]- Solution
> $P(\text{on})=\tfrac13$. Given the day, examiners are independent, so the number who pass him is binomial.
> - 3 examiners, need $\ge2$: on $0.896$, off $0.352$, total $\tfrac13(0.896)+\tfrac23(0.352)=\mathbf{0.5333}$.
> - 5 examiners, need $\ge3$: on $0.94208$, off $0.31744$, total $\mathbf{0.5257}$.
>
> **Choose 3.** A bigger panel amplifies whichever way each examiner leans. It helps on a good day (0.896 → 0.942) and hurts on a bad one (0.352 → 0.317), and bad days are twice as likely. (Matches the key.)

> [!question] Q5 · Average 3.5 commercial crashes per month. $P(\ge2\text{ next month})$, stating assumptions.

> [!example]- Solution ([[PR03 Discrete Random Variables and Distributions]])
> Model: each of a very large number $N$ of flights crashes independently with a tiny probability $3.5/N$. Then the count is Bin$(N,3.5/N)\approx$ Poisson$(3.5)$ (the Poisson limit). So $P(\ge2)=1-e^{-3.5}(1+3.5)=\mathbf{0.864}$. The assumptions to state are independence of crashes and a constant rate over the month.

> [!question] Q6 · A coin with $P(H)=p$ is flipped until the 10th head. pmf of $X$ = number of tails?

> [!example]- Solution
> $X=i$ means $i+10$ flips, the last a head, with 9 heads among the first $i+9$:
> $$P(X=i)=\binom{i+9}{9}p^{10}(1-p)^i,\qquad i=0,1,2,\dots$$
> (negative binomial, failures convention).

## End-semester examination (27 November 2024)

> [!question] Q1 · A dart lands uniformly on a unit disc; $D$ = distance from the centre. (a) $P(D<a)$; (b) density; (c) $E[D]$, $\operatorname{Var}D$; (d) with $X_n=\sum_1^nD_i$, evaluate $\lim_n P\big(|X_n/n-\tfrac23|\ge1-(\tfrac1{18})^n\big)$.

> [!example]- Solution ([[PR05 Continuous Random Variables]], [[PR06 Moments Generating Functions and Limit Theorems]])
> (a) $P(D<a)=0$ for $a<0$, $a^2$ for $0\le a\le1$ (area ratio), and 1 for $a>1$.
> (b) $f_D(x)=2x$ on $[0,1]$.
> (c) $E[D]=\int_0^12x^2dx=\tfrac23$, $E[D^2]=\tfrac12$, so $\operatorname{Var}D=\tfrac12-\tfrac49=\tfrac1{18}$.
> (d) **The limit is 0.** The key argues by the weak law: the threshold $1-(1/18)^n$ is at least the fixed $\varepsilon=17/18$, and $P(|\bar D-\tfrac23|\ge\varepsilon)\to0$. There is an even shorter argument. $\bar D=X_n/n\in[0,1]$, so $|\bar D-\tfrac23|\le\tfrac23<\tfrac{17}{18}\le1-(1/18)^n$ **for every $n$**, and the probability is exactly 0 for all $n$, with no limit theorem needed.

> [!question] Q2 · Two independent darts; $D_1,D_2$ their distances. (a) $E|D_1-D_2|$. (b) What follows: darts land at the same point? equidistant? neither? both?

> [!example]- Solution
> (a) $E|D_1-D_2|=\int_0^1\!\int_0^1|x-y|\,(2x)(2y)\,dy\,dx=2\int_0^1\!\int_0^x(x-y)4xy\,dy\,dx=8\int_0^1x\cdot\frac{x^3}6dx=\mathbf{\tfrac4{15}}$ (numerical 0.26667; the key's "4/15, TAs please check" is right).
> (b) **Neither.** $|D_1-D_2|$ is the difference of *distances from the centre*, not the distance between the landing points, so (i) is not addressed at all. And $E|D_1-D_2|=\tfrac4{15}>0$, so they are not expected to be equidistant either.

> [!question] Q3 · $Y=X^2$: (a) density in general; (b) $X\sim N(0,1)$; (c) $X\sim U(-1,2)$.

> [!example]- Solution ([[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]])
> (a) For $y>0$, $F_Y(y)=F_X(\sqrt y)-F_X(-\sqrt y)$, so $f_Y(y)=\dfrac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y}$; 0 for $y\le0$. Two branches because two values of $x$ give the same $y$.
> (b) $f_Y(y)=\dfrac{e^{-y/2}}{\sqrt{2\pi y}}$, $y>0$ (the $\chi^2_1$ density).
> (c) $f_X=\tfrac13$ on $(-1,2)$. For $0<y<1$ both $\pm\sqrt y$ are in range: $f_Y=\dfrac{1}{3\sqrt y}$. For $1\le y<4$ only $+\sqrt y$ is: $f_Y=\dfrac1{6\sqrt y}$. Otherwise 0. (Total: $\tfrac23+\tfrac13=1$.)

> [!question] Q4 · Poisson process of announcements, rate $\lambda$/day. (a) $P(\text{none in 2 days})$; (b) $P(\ge2\text{ in 4 days})$; (c) gap density; (d) mean time to 20.

> [!example]- Solution
> (a) $e^{-2\lambda}$. (b) $1-e^{-4\lambda}(1+4\lambda)$. (c) $\lambda e^{-\lambda t}$, $t>0$. (d) $20/\lambda$ (same reasoning as [[MT2113 Past Papers 2023 - Solved|2023]] Q2).
>
> [!warning] Key mismatch
> The official solutions answer (a) as "one announcement in a **three**-day period", $3\lambda e^{-3\lambda}$. The paper asks for **no** announcements in **two** days. Answer the paper: $e^{-2\lambda}$.

> [!question] Q5 · 15 % support abolishing exams; class of 200, independent opinions. By the CLT, which is true: $P(\ge35)$ in $[0.15,0.16]$; $\ge0.16$; $\ge0.2$; $\ge0.22$? ($0.8389\le\Phi(5\sqrt{10}/\sqrt{255})\le0.839$.)

> [!example]- Solution ([[PR06 Moments Generating Functions and Limit Theorems]])
> $X\sim\text{Bin}(200,0.15)$: mean 30, variance 25.5. $P(X\ge35)\approx1-\Phi\big(5/\sqrt{25.5}\big)$, and $5/\sqrt{25.5}=5\sqrt{10}/\sqrt{255}$ is exactly the hint's argument. So $P\in[0.161,0.1611]$: **(b) is true**. (a) fails because 0.161 > 0.16, and (c), (d) fail.
> *Beyond the question:* with the continuity correction, $P(X\ge34.5)\approx0.186$, and the exact binomial value is 0.185. The plain CLT estimate is off by 0.025; the answer is still (b).

## Quizzes

> [!question] Quiz 1 (12 Aug) · Q1. Home $H$ to work $W$ is 9 blocks east and 8 north, walking only east or north. (a) Number of routes? (b) Avoiding the flooded point $P$ (4 east, 3 north of $H$)? · Q2. Prove inclusion–exclusion for three events.

> [!example]- Solution ([[PR01 Counting and the Axioms of Probability]])
> 1(a) A route is a word of 9 E's and 8 N's: $\binom{17}8=\mathbf{24\,310}$.
> 1(b) Routes through $P=(4,3)$: $\binom73\binom{10}5=35\times252=8820$. So $24\,310-8820=\mathbf{15\,490}$ avoid it. ($P$'s position is read off Figure 1: the 5th vertical line and the 4th horizontal line from $H$.)
> 2. Apply the two-set rule twice: $P(E_1\cup E_2\cup E_3)=P(E_1\cup E_2)+P(E_3)-P((E_1\cup E_2)\cap E_3)$. Then expand $P(E_1\cup E_2)$, and expand $P((E_1\cap E_3)\cup(E_2\cap E_3))$ by the two-set rule, using $(E_1\cap E_3)\cap(E_2\cap E_3)=E_1\cap E_2\cap E_3$. Collecting terms gives the formula.

> [!question] Quiz 2 (26 Aug) · Q1. A ball moves from urn 1 ($m_1$ white, $n_1$ red) to urn 2 ($m_2$, $n_2$); then a ball is drawn from urn 2. $P(\text{white})$? · Q2. 5 % of men, 0.25 % of women colour-blind. A colour-blind person: probability male, if the sexes are equal in number? If males are twice as many?

> [!example]- Solution ([[PR02 Conditional Probability Bayes Rule and Independence]])
> 1. Condition on the transferred ball: $P=\dfrac{m_1}{m_1+n_1}\cdot\dfrac{m_2+1}{m_2+n_2+1}+\dfrac{n_1}{m_1+n_1}\cdot\dfrac{m_2}{m_2+n_2+1}=\dfrac{m_1(m_2+1)+n_1m_2}{(m_1+n_1)(m_2+n_2+1)}$ (matches the key).
> 2. Equal: $\dfrac{0.05}{0.05+0.0025}=\tfrac{20}{21}=0.952$. Twice as many males: $\dfrac{0.05\cdot\frac23}{0.05\cdot\frac23+0.0025\cdot\frac13}=\tfrac{40}{41}=0.976$.

> [!question] Quiz 3 (9 Sep) · Q1. Buses with 40, 33, 25, 50 students; $X$ = bus size of a random student, $Y$ = bus size of a random driver: $E[X]$, $E[Y]$. · Q2. $\operatorname{Var}(aX+b)$. · Q3. 3 of 20 items, 4 defective, without replacement: expected defectives.

> [!example]- Solution ([[PR03 Discrete Random Variables and Distributions]], [[PR04 Joint Distributions Expectation and Variance]])
> 1. $E[Y]=\tfrac{148}4=37$. But a random **student** is more likely to be on a full bus: $P(X=n)=n/148$, so $E[X]=\sum n^2/148=5814/148=\mathbf{39.28}>37$ (the size-biased average; the "inspection paradox").
> 2. $a^2\operatorname{Var}X$: a shift does not change spread, and scaling by $a$ scales deviations by $a$.
> 3. Indicators: each of the 3 draws is defective with probability $4/20$, so $E=3\cdot\tfrac4{20}=\mathbf{0.6}$ (hypergeometric mean).

> [!question] Quiz 4 (14 Oct) · Q1. Processing time has density $\lambda e^{-x/10}$ ($x\ge0$): (a) $P(10<X<15)$; (b) mean. · Q2. $X\sim N(0,1)$: $P(X<0)$, $P(X=-1)$, $P(|X|>2)$, $P(|X|<3)$. · Q3. CDF of $f(x)=\frac{x}{\sigma^2}e^{-x^2/2\sigma^2}$, $x>0$.

> [!example]- Solution ([[PR05 Continuous Random Variables]])
> 1. Normalisation forces $\lambda=\tfrac1{10}$. (a) $e^{-1}-e^{-1.5}=0.1447$. (b) $10$ days.
> 2. $\tfrac12$; $0$ (a single point has zero probability for a continuous law); $2(1-\Phi(2))$; $2\Phi(3)-1$.
> 3. $F(x)=\int_0^x\frac t{\sigma^2}e^{-t^2/2\sigma^2}dt=1-e^{-x^2/2\sigma^2}$ for $x>0$, and 0 otherwise (the Rayleigh law; substitute $u=t^2/2\sigma^2$).

> [!question] Quiz 5 (28 Oct) · Q1. The Poisson-process questions (a, b, d of end-sem Q4). · Q2. Three fair tosses, $X$ = heads, $Y=|\#H-\#T|$, with the joint pmf given: marginals and CDFs.

> [!example]- Solution ([[PR04 Joint Distributions Expectation and Variance]])
> 1. $e^{-2\lambda}$; $1-e^{-4\lambda}(1+4\lambda)$; $20/\lambda$.
> 2. Summing rows and columns: $p_X=(\tfrac18,\tfrac38,\tfrac38,\tfrac18)$ on $0,1,2,3$; $p_Y(1)=\tfrac34$, $p_Y(3)=\tfrac14$. CDFs: $F_X$ steps to $\tfrac18,\tfrac12,\tfrac78,1$ at $0,1,2,3$; $F_Y=0$ for $y<1$, $\tfrac34$ on $[1,3)$, 1 for $y\ge3$.

> [!question] Quiz 6 (11 Nov) · Q1. $X,Y$ i.i.d. $U(0,1)$: density of $\max$. · Q2. $X,Y$ independent ⇒ $-X,Y$ independent. · Q3. $f=e^{-(x+y)}$ on the positive quadrant: (a) show $Z=Y-X$ has $f(z)=\tfrac12e^{-|z|}$; (b) $P(X<Y)$.

> [!example]- Solution ([[PR08 Order Statistics and the Multinomial Distribution]], [[PR07 Sums of Independent Variables Covariance and Correlation]])
> 1. $P(\max\le m)=m^2$, so the density is $2m$ on $(0,1)$.
> 2. $P(-X\le a,Y\le b)=P(X\ge-a,Y\le b)=P(X\ge-a)P(Y\le b)=P(-X\le a)P(Y\le b)$ for all $a,b$. ∎
> 3. (a) $f_Z(z)=\int f_X(x)f_Y(x+z)\,dx$ over $x\ge0$ and $x+z\ge0$. For $z\ge0$: $\int_0^\infty e^{-2x-z}dx=\tfrac12e^{-z}$. For $z<0$: $\int_{-z}^\infty e^{-2x-z}dx=\tfrac12e^{z}$. ∎ (b) $P(X<Y)=P(Z>0)=\tfrac12$, as symmetry demands.

> [!question] Quiz 7 (18 Nov) · Q1. $T\sim U(0,2\pi)$, $X=\cos T$, $Y=\sin T$: means, covariance; are $X^2,Y^2$ independent? $X,Y$? · Q2. $E[X^k]=0.8$ for all $k\ge1$: (a) $E[e^{tX}]$; (b) if Bernoulli, its pmf.

> [!example]- Solution ([[PR07 Sums of Independent Variables Covariance and Correlation]], [[PR06 Moments Generating Functions and Limit Theorems]])
> 1. $E[X]=E[Y]=0$ (a full period averages to 0). $\operatorname{Cov}=E[\cos T\sin T]=\tfrac12E[\sin2T]=0$. **$X^2,Y^2$ are not independent**: $X^2+Y^2=1$, so $P(X^2>\tfrac34,Y^2>\tfrac34)=0$ while each probability is $\tfrac13$. Hence **$X,Y$ are not independent** either (functions of independent variables would be independent). This is the standard example of **uncorrelated but dependent** variables.
> 2. (a) $E[e^{tX}]=1+\sum_{k\ge1}\frac{t^k}{k!}0.8=1+0.8(e^t-1)=0.2+0.8e^t$. (b) That is the Bernoulli(0.8) mgf: $P(X=1)=0.8$, $P(X=0)=0.2$ (indeed $E[X^k]=P(X=1)$ for a 0/1 variable).
