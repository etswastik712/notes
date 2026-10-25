---
id: introduction-to-probability/2026-08-26-class-notes-27th-august-2026
aliases: [Class notes 27 Aug 2026]
tags: [probability, mt2113, class-notes]
trust_tier: agent_written
---

# Class notes 27th August 2026 (posted 26 August, updated 2 September)

## Covered
Two versions were posted. The 26 August version has the first six bullets and a transformation section left open ("if time permits, we shall find $E[Y]$ using this pmf expression, else we shall do it in the next class"). The version re-uploaded on 2 September differs only at the end: it adds the formula for $E[g(X)]$, its proof outline and linearity $E[aX+b]$ (Classroom: Class notes 27th August 2026.pdf, both versions).

**Bernoulli and binomial.** Run $n$ independent trials, each a success with probability $p$. Let $X_i=1$ if trial $i$ succeeds and $X_i=0$ otherwise. Then each $X_i\sim\text{Bernoulli}(p)$ and $X=\sum_{i=1}^n X_i\sim\text{Binomial}(n,p)$. A formal proof needs joint distributions, which had not been covered; the intuition is given in class.

**Worked examples (problems posed in the notes).**
- Three balls drawn without replacement from 20 numbered balls; bet that at least one number is $\ge 17$. Find the probability of winning.
- Flip a coin (head probability $p$) until a head occurs or $n$ flips have been made; $X$ = number of flips. Argue $X$ is a discrete random variable and find its pmf.
- pmf $p(i)=c\lambda^i/i!$ for $i\in\mathbb N_0$, with $\lambda,c>0$: find $c$ in terms of $\lambda$, then $P[X=0]$ and $P[X>2]$.
- School class of 120 students in three buses (36, 40, 44); one student chosen at random, $X$ = number of students on that student's bus. Find $E[X]$.
- Random walk: a particle starts at 0 and makes $n$ independent steps, $+1$ with probability $p$ and $-1$ with probability $1-p$. Let $Y$ be the position after $n$ steps. Find the pmf of $Y$ by writing $Y$ as a transformation of a random variable whose distribution is already known (the binomial). Gambler's ruin is mentioned but is not formally part of the syllabus.

**Poisson as a limit.** The limit of the $\text{Binomial}(n,c/n)$ distributions for a constant $c>0$ is the Poisson distribution; it will be derived in class.

**Transformations of a discrete random variable.** Let $X$ take values $x_1,x_2,\dots$ (finite or countably infinite) with pmf $p(\cdot)$, and let $g$ be real-valued. Then $Y=g(X)$ is a random variable taking values in
$$S=\{y\in\mathbb R: y=g(x_i)\text{ for at least one } i\}.$$
If $g$ is not bijective, several $x_i$ can give the same value, so
$$P[Y=y]=\sum_{i:\,g(x_i)=y}P[X=x_i]=\sum_{i:\,g(x_i)=y}p(x_i)\quad\text{for each }y\in S.$$

**Expectation of a transformation (added 2 September).**
$$E[g(X)]=\sum_{i=1}^\infty g(x_i)\,p(x_i).\tag{1.1}$$
No pmf of $g(X)$ is needed: only the pmf of $X$ and the function $g$.

Proof outline (the instructor says it will not be asked in an exam or quiz, but (1.1) must be known). Let $Y=g(X)$ take values $y_1,y_2,\dots$ (discrete because $X$ is). Put $S_j=\{x_i: g(x_i)=y_j\}$. Each $S_j$ is non-empty and the $S_j$ partition $\{x_1,x_2,\dots\}$ (pairwise disjoint, union everything). Then $Y=y_j$ iff $X\in S_j$, so $P[Y=y_j]=\sum_{x_i\in S_j}p(x_i)$ and
$$\sum_i g(x_i)p(x_i)=\sum_j\sum_{x_i\in S_j}g(x_i)p(x_i)=\sum_j y_j\sum_{x_i\in S_j}p(x_i)=\sum_j y_jP[Y=y_j]=E[Y].$$
The proof is easy when $g$ is bijective (for example strictly increasing).

**Linearity (special case $g$ linear).** $E[aX+b]=aE[X]+b$.

## From the post
26 August (first version): Dear everyone, in tomorrow's class, we shall recall the definition of a random variable, its pmf and cdf and their most important properties, the binomial and Bernoulli distributions, and then cover the rest of the contents from the previous class-notes. Following this, we shall continue with the class-notes attached herewith.

2 September (re-upload): Dear everyone, I am re-uploading here the class notes that were earlier posted on 27th August -- these have now been updated, but only at the very end. I have now added more points regarding the expectations of transformed random variables. We shall either cover it on 3rd September (if we have enough time, after covering the remaining contents from the class notes posted on 2nd September), or else on 9th September.

## Files
- [Class notes 27th August 2026.pdf (26 Aug version)](https://drive.google.com/file/d/1Y7tQBZI9uWOKd7OB8AbjVwZrHLF2YJTy/view?usp=drive_web)
- [Class notes 27th August 2026.pdf (2 Sep updated version)](https://drive.google.com/file/d/1OXYf2eewb7VTP2uYs0lbACPKAr4Ibqct/view?usp=drive_web)

## Related
- [[08-Probability/PR03 Discrete Random Variables and Distributions]]: the chapter on discrete random variables and named distributions.
- [[08-Probability/PR04 Joint Distributions Expectation and Variance]]: linearity of expectation and joint pmfs, which the instructor defers the transformation material to.
- [[introduction-to-probability/2026-08-26-practice-problems-28th-august-and-following-weekend]]: the practice sheet that goes with this class.
- [[introduction-to-probability/2026-09-02-class-notes-2nd-september-2026]]: the next class notes.
