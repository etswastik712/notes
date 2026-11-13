---
title: PR09 Change of Variables the Multivariate Normal and Products of Uniforms
aliases: [PR09, change of variables, Jacobian, conditional density, Bayes rule for densities, multivariate normal, orthogonal diagonalisation, independent normals, minus log of a uniform, product of uniforms, Gamma distribution, Jensen's inequality, tangent line of a convex function, Box-Muller, MT2113 homework 6, HW6, week 4 lectures, week 5 lectures]
subject: probability
type: chapter
chapter: 9
part: V
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
prereq: [PR05 Continuous Random Variables, PR07 Sums of Independent Variables Covariance and Correlation, PR08 Order Statistics and the Multinomial Distribution]
tags: [subject/probability, type/chapter, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw6]
---
# PR09 · Change of Variables, the Multivariate Normal and Products of Uniforms

◀ [[PR08 Order Statistics and the Multinomial Distribution]] · [[Probability - Course Map]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Scope of this chapter
> **Added 2026-11-12.** New sources: **Week 4 notes** ([[Week4_notes.pdf]], 4 pages: Homework 4 and "Summary of Lectures Week 4"), **Week 5 notes** ([[Week5_notes.pdf]], 9 pages: Homework 5 on pp. 1–2, "Summary of Week 5 Lectures" on pp. 3–9) and **Homework 6** ([[hw6_edited.pdf]], one handwritten page, three problems); all read from the page images this session. Most of what they contain is **already in the vault**: Homework 4 is [[PR07 Sums of Independent Variables Covariance and Correlation]] §3–§6 (convolution, $E|X-Y|$, $\operatorname{Var}(\sum c_iX_i)=c^{\mathsf T}Ac$, $|\rho|\le1$, the two dice); the Week 5 covariance matrix, the two proofs of $|\rho|\le1$, the min/max lemma, Homework 5 Q2 and the multinomial are PR07 §5 and [[PR08 Order Statistics and the Multinomial Distribution]]. **What was missing, and is the content of this chapter:** (i) the **marginal / conditional density and Bayes' rule for densities** and the disc and "race" examples of Week 4 (§1); (ii) the **change-of-variables formula**, one variable and $n$ variables with the Jacobian (Week 5; §2); (iii) **Homework 6**: the multivariate normal diagonalised to independent normals (§3), $-\ln U$ and the product of uniforms (§4), the tangent line below a convex graph and Jensen's inequality (§5). So this is a **new chapter** under the new-material rule, and the covered parts are only cross-referenced. Three places where the sheets are ambiguous or inconsistent are marked `[!verify]`.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught: Week 4–5 lecture summaries and Homework 6)**
> - §1 joint, marginal and conditional densities, independence as factorisation of the pdf, cdf and survival function, Bayes' rule for densities, the uniform disc, "Example 2" $P(X_1<X_2)$, the mgf of a sum
> - §2 the change-of-variables formula $f_Y(y)=f_X(g^{-1}(y))\,|{\det}\,\partial g^{-1}/\partial y|$ in 1-D and $n$-D
> - §3 **HW6 Q1**: $X\sim N(\mu,\Sigma)$, $Y=OX$ with $O\Sigma O^{\mathsf T}$ diagonal $\Rightarrow$ $Y_i$ independent normals
> - §4 **HW6 Q2**: $-\ln U\sim\mathrm{Expo}(1)$; the law of $U=U_1\cdots U_n$ via $V=-\ln U$
> - §5 **HW6 Q3**: the tangent line of $g$ with $g''>0$ lies below the graph (used in the proof of Jensen's inequality, as the sheet says)
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §1 the corrected "Poisson" race; §2 non-injective maps, polar coordinates, **Box–Muller**; §3 the geometry (ellipses, axes), the 3×3 check, uncorrelated versus independent; §4 the **Gamma$(n,1)$** identification, the density $(-\ln u)^{n-1}/(n-1)!$, moments; §5 the proof of **Jensen** from the tangent line, a quantitative form, AM–GM

> [!key] After this chapter you can
> - compute a **marginal** by integrating out, a **conditional density** as $f_{X,Y}/f_X$, and use **Bayes' rule** for densities,
> - transform a density under $Y=g(X)$ in one or $n$ variables (**Jacobian**), including maps that are not one-to-one, and derive the Rayleigh/polar and Box–Muller results,
> - show that a **multivariate normal** becomes a vector of **independent** normals after the orthogonal change of variables that diagonalises $\Sigma$ (and say what the variances of the new coordinates are),
> - show $-\ln U\sim\mathrm{Expo}(1)$, identify $-\ln(U_1\cdots U_n)$ as $\mathrm{Gamma}(n,1)$ and write the density of the product,
> - prove that a tangent line to a strictly convex function lies below its graph and deduce **Jensen's inequality**.

> [!intuition] The one-sentence story
> A density is a **mass per unit volume**, so when you stretch space by a map $g$, the mass is conserved and the density is divided by the local stretching factor $|\det Dg|$; the only "new" content of a transformation is therefore one number, the Jacobian. For the Gaussian this is the whole story: an **orthogonal** map has stretching factor $1$ and turns the elliptical exponent $(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)$ into a **sum of squares**, which is a product of one-dimensional normal densities, i.e. independence. And $-\ln$ is the map that turns products into sums, so a product of uniforms is the exponential of a sum of exponentials.

![[fig_pr09_change_of_variables.png]]
*A: uniform on a disc of radius $2$: the marginal is a semicircle, the conditional of $X_2$ given $X_1=1$ is uniform on $\pm\sqrt3$ (§1). B: $X\sim N(\mu,\Sigma)$, $\Sigma=\begin{pmatrix}2&1\\1&2\end{pmatrix}$: rotating onto the eigenvectors gives independent $N(0,3)$ and $N(\sqrt2,1)$ (§3; 2500 samples, $1\sigma$ and $2\sigma$ contours). C: the density $(-\ln u)^{n-1}/(n-1)!$ of $U_1\cdots U_n$ for $n=1,\dots,5$; thin red steps are $3\cdot10^5$ simulated products for $n=5$ (§4). D: tangent lines below $e^x$ and the Jensen gap for $X\in\{0,1.6\}$ (§5). Numbers: `scripts/pr09_numbers.py`; `scripts/fig_pr09.py`.*

*The interactive tool for §3 is embedded before the chapter summary; the one-variable version of the formula of §2 is the existing tool [[Interactive Tools]] entry on functions of a random variable (`pr_transform`).*

## 1. Week 4: marginal, conditional and Bayes for densities #quiz/pr-hw4 #quiz/pr-hw6
<span class="scope-taught">taught</span> *Source: [[Week4_notes.pdf#page=2|Summary of Lectures Week 4]], pp. 2–4* · <span class="scope-extra-beyond">extra · beyond</span> *the corrected Example 2 and the numerical checks*

A random vector $X=(X_1,\dots,X_n):S\to\mathbb R^n$ has, "naively speaking", $P(x_i\le X_i\le x_i+\delta x_i,\ i=1..n)\approx f(x_1,\dots,x_n)\,\delta x_1\cdots\delta x_n$: the **joint pdf** (joint pmf in the discrete case).

- **Marginal.** Integrate the others out: $f_{X_i}(x_i)=\int\!\cdots\!\int f(x_1,\dots,x_n)\,\mathrm dx_1\cdots\widehat{\mathrm dx_i}\cdots\mathrm dx_n$; for $n=2$, $f_{X_1}(x)=\int f(x,x_2)\,\mathrm dx_2$, $f_{X_2}(y)=\int f(x_1,y)\,\mathrm dx_1$.
- **Independence.** $X_1,X_2$ are independent iff $f_{X_1,X_2}(x_1,x_2)=f_{X_1}(x_1)f_{X_2}(x_2)$ (pmf version in the discrete case). Integrating this factorised pdf over $(-\infty,x_1]\times(-\infty,x_2]$ gives $P(X_1\le x_1,X_2\le x_2)=F(x_1)F(x_2)$, and over $[x_1,\infty)\times[x_2,\infty)$ gives $P(X_1\ge x_1,X_2\ge x_2)=P(X_1\ge x_1)P(X_2\ge x_2)$; the second form is the one used for $\min$ in [[PR08 Order Statistics and the Multinomial Distribution]] §3.
- **Conditional pdf.** $f_{Y\mid X}(y\mid x)=\dfrac{f_{X,Y}(x,y)}{f_X(x)}$ (where $f_X(x)>0$): the slice of the joint density at $X=x$, **renormalised** so that it integrates to $1$ in $y$.
- **Bayes' rule for densities.** Writing the joint density both ways, $f_{Y\mid X}(y\mid x)=\dfrac{f_{X\mid Y}(x\mid y)\,f_Y(y)}{f_X(x)}$.

> [!example] Uniform on a disc (the sheet's Example 1)
> $(X_1,X_2)$ uniform on $\{x_1^2+x_2^2\le R^2\}$: $f=\frac1{\pi R^2}$ there and $0$ outside. Then
> $$f_{X_1}(x)=\int_{-\sqrt{R^2-x^2}}^{\sqrt{R^2-x^2}}\frac{\mathrm dy}{\pi R^2}=\frac{2\sqrt{R^2-x^2}}{\pi R^2}=\frac{2}{\pi R}\sqrt{1-\Big(\frac xR\Big)^2},\qquad|x|\le R,$$
> a **semicircle** (it integrates to $\frac2{\pi R}\cdot R\cdot\frac\pi2=1$). Not uniform: the disc is thicker through the middle. The **conditional** is $f_{X_2\mid X_1}(y\mid x)=\dfrac{1/(\pi R^2)}{2\sqrt{R^2-x^2}/(\pi R^2)}=\dfrac1{2\sqrt{R^2-x^2}}$, i.e. **uniform on the vertical chord** $|y|\le\sqrt{R^2-x^2}$.
> *Numbers* ($R=2$, `pr09_numbers.py`): the marginal integrates to $1.000000$; $P(|X_1|<1)=\frac{\sqrt3}{2\pi}+\frac13=0.608998$ by the marginal, $0.609378$ by simulation ($2\cdot10^6$ points); at $x=1$ the chord is $\pm1.7321$ with density $0.28868$ (simulation: range $[-1.734,1.736]$, mean $0.008$); Bayes' rule at $(x,y)=(1,0.5)$: $f(y|x)f(x)/f(y)=0.258199=f(x|y)=1/(2\sqrt{R^2-y^2})$. This is the "uncorrelated but dependent" disc of [[PR07 Sums of Independent Variables Covariance and Correlation]] §1: dependence is visible in the conditional (the chord length depends on $x$).

> [!verify] The constant in the sheet's last line
> The sheet writes the middle expression $\frac{2\sqrt{R^2-x_1^2}}{\pi R^2}$ correctly and then simplifies it to a line that, as I read the handwriting, has $\frac2\pi\sqrt{1-(x_1/R)^2}$ with the factor $\frac1R$ missing or unclear. The correct simplification is $\frac2{\pi R}\sqrt{1-(x_1/R)^2}$ (the version with $R=1$ is the sheet's). Check against the file.

> [!example] Week 4's "Example 2": a race of two clocks 🔵 (the label on the sheet is wrong)
> The sheet states *"If $X_1\sim\mathrm{Pois}(\lambda_1)$, $X_2\sim\mathrm{Pois}(\lambda_2)$ are independent, find $P(X_1<X_2)$"*, and the worked answer integrates $\int_0^\infty\!\int_{x_1}^\infty\lambda_1e^{-\lambda_1x_1}\lambda_2e^{-\lambda_2x_2}\,\mathrm dx_2\,\mathrm dx_1=\frac{\lambda_1}{\lambda_1+\lambda_2}$. Those are **exponential densities**, so the computation solves the problem for $X_i\sim\mathrm{Expo}(\lambda_i)$: condition on $X_1=x$ and use the survival function, $P(X_1<X_2)=\int_0^\infty f_{X_1}(x)\,P(X_2>x)\,\mathrm dx=\int_0^\infty\lambda_1e^{-(\lambda_1+\lambda_2)x}\mathrm dx=\frac{\lambda_1}{\lambda_1+\lambda_2}$ (the probability that the faster-rate clock rings first; compare "$\min\sim\mathrm{Expo}(\lambda_1+\lambda_2)$" in PR08 §3).
> For genuinely **Poisson** variables the answer is a double sum and is *not* $\frac{\lambda_1}{\lambda_1+\lambda_2}$: for $\lambda=(2,3)$, $P(X_1<X_2)=\sum_kP(X_1=k)P(X_2>k)=0.58529$ (simulation $0.58512$), against $\frac25=0.40000$ for the exponentials (simulation $0.39978$); here $P(X_1=X_2)=0.16772$ is not zero. For equal rates, $P(X_1<X_2)=\frac12\big(1-e^{-2\lambda}I_0(2\lambda)\big)$, $=0.39650$ at $\lambda=2$ ($I_0$ the modified Bessel function).

> [!verify] Which problem did the lecture mean?
> I treat the sheet's worked integral as the intended problem (an exponential race), because the integrand is exponential and the answer $\frac{\lambda_1}{\lambda_1+\lambda_2}$ is the textbook result for it; it is possible the lecture said "exponential" aloud or that the sheet is a typo for $\mathrm{Expo}(\lambda_i)$. Ask the instructor which was intended.

> [!example] Example 3: the mgf of a sum
> For independent $X,Y$: $M_{X+Y}(t)=\iint e^{t(x+y)}f_X(x)f_Y(y)\,\mathrm dx\,\mathrm dy=M_X(t)M_Y(t)$ ([[PR06 Moments Generating Functions and Limit Theorems]]). Check: $\mathrm{Expo}(1)+\mathrm{Expo}(2)$ at $t=0.3$: $\frac1{0.7}\cdot\frac2{1.7}=1.68067$, simulation $1.68094$.

## 2. Week 5: the change-of-variables formula #quiz/pr-hw5 #quiz/pr-hw6
<span class="scope-taught">taught</span> *Source: [[Week5_notes.pdf#page=8|Week 5 notes, change of variables]] (pp. 8–9, the last two pages of the summary: one variable on p. 8, $n$ variables on p. 9)* · <span class="scope-extra-beyond">extra · beyond</span> *non-injective maps, the examples, Box–Muller*

**One variable.** Let $X$ have density $f_X$ and $Y=g(X)$ with $g:\mathbb R\to\mathbb R$ invertible. Then
$$P(y\le Y\le y+\delta y)=P\big(X\in g^{-1}[y,y+\delta y]\big)=\int_{g^{-1}[y,y+\delta y]}f_X(x)\,\mathrm dx\approx f_X(g^{-1}(y))\Big|\frac{\mathrm d g^{-1}}{\mathrm dy}\Big|\,\delta y,$$
so
$$\boxed{f_Y(y)=f_X\big(g^{-1}(y)\big)\Big|\frac{\mathrm d}{\mathrm dy}g^{-1}(y)\Big|=\frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}.}$$
The **absolute value** is there because the length of the preimage interval is $|\mathrm dg^{-1}/\mathrm dy|\,\delta y$ whether $g$ is increasing or decreasing.

**$n$ variables.** For $\vec Y=\vec g(\vec X)$, $\vec g:\mathbb R^n\to\mathbb R^n$ invertible,
$$f_{\vec Y}(\vec y)=f_{\vec X}\big(\vec g^{-1}(\vec y)\big)\,\Big|\det\frac{\partial\vec g^{-1}}{\partial\vec y}(\vec y)\Big|=f_{\vec X}\big(\vec g^{-1}(\vec y)\big)\,\Big|\det\frac{\partial\vec g}{\partial\vec x}\Big|^{-1}_{\vec x=\vec g^{-1}(\vec y)}.$$
(The second equality is the inverse function theorem: $D(g^{-1})=(Dg)^{-1}$.) This is the formula used in PR08 §3 for $(Y_1,Y_2)\mapsto(Y_1,Y_2-Y_1)$ (Jacobian $1$).

> [!key] Extension 🔵: maps that are not one-to-one
> If $y=g(x)$ has several roots $x_1,\dots,x_k$, add the contributions: $f_Y(y)=\sum_if_X(x_i)/|g'(x_i)|$ (the same bookkeeping as the "two preimages" of PR08 §1; [[PR05 Continuous Random Variables]] §5 does the monotone and non-monotone cases by the cdf method).

**Worked examples** 🔵 (numbers in `pr09_numbers.py`, $2\cdot10^6$ draws):
- **Affine, $Y=aX+b$:** $f_Y(y)=f_X\!\big(\frac{y-b}a\big)/|a|$. $X\sim N(0,1)$, $a=-3$, $b=5$ gives $N(5,9)$: simulation mean $5.001$, s.d. $3.001$, Kolmogorov distance $0.0017$ (the minus sign changes nothing: the absolute value).
- **$Y=e^X$ (log-normal):** $g^{-1}=\ln$, $|\mathrm dg^{-1}/\mathrm dy|=1/y$: $f_Y(y)=\varphi(\ln y)/y$. At $y=0.5,1,2$: $0.6275,\,0.3989,\,0.1569$; histogram $0.6343,\,0.4004,\,0.1535$.
- **$Y=X^2$ (two roots $\pm\sqrt y$):** $f_Y(y)=2\cdot\varphi(\sqrt y)\cdot\frac1{2\sqrt y}=\frac{e^{-y/2}}{\sqrt{2\pi y}}$, the $\chi^2_1$ density: $0.7041,\,0.2420,\,0.0270$ at $y=0.25,1,4$ (histogram $0.6966,\,0.2405,\,0.0264$).
- **A linear map in the plane:** $Y=AX$ gives $f_Y(y)=f_X(A^{-1}y)/|\det A|$. $X$ uniform on the unit square and $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$: $\det A=6$, so $Y$ is uniform with density $\frac16$ on a parallelogram of area $6$; $P(Y\in[0,2]\times[0,3])=\frac{4.5}6=0.75$ (simulation $0.74977$).
- **Polar coordinates and the Rayleigh law.** $(X,Y)$ iid $N(0,1)$, $(x,y)=(r\cos\theta,r\sin\theta)$, $|\partial(x,y)/\partial(r,\theta)|=r$: $f_{R,\Theta}(r,\theta)=\frac1{2\pi}e^{-r^2/2}\cdot r=\big(re^{-r^2/2}\big)\cdot\frac1{2\pi}$. It **factorises**: $R$ has density $re^{-r^2/2}$ (the [[Rayleigh Distribution]]), $\Theta$ is uniform on $[0,2\pi)$, and they are independent; $P(R<1)=1-e^{-1/2}=0.39347$ (simulation $0.39332$) and $R^2\sim\mathrm{Expo}(\frac12)$, $E[R^2]=2$.
- **Box–Muller** (the polar result run backwards): from independent $U_1,U_2\sim U(0,1)$ set $R=\sqrt{-2\ln U_1}$ (then $P(R>r)=P(U_1<e^{-r^2/2})=e^{-r^2/2}$, the Rayleigh survival function) and $\Theta=2\pi U_2$; then $X=R\cos\Theta$, $Y=R\sin\Theta$ are **independent $N(0,1)$**. Checked: means $-0.0005,\,0.0003$, variances $0.9998,\,0.9990$, correlation $0.0005$, Kolmogorov distance of $X$ to $N(0,1)$ $0.0021$.

## 3. Homework 6, Q1: the multivariate normal and independent normals #quiz/pr-hw6
<span class="scope-taught">taught</span> *Source: [[hw6_edited.pdf#page=1|HW6, Q1]]* · <span class="scope-extra-beyond">extra · beyond</span> *the proof, the geometry, the numerical checks*

**The problem.** $X_i\sim N(\mu_i,\sigma_i^2)$ with $\Sigma_{ij}=\operatorname{cov}(X_i,X_j)$ **positive definite** (symmetric, all eigenvalues $>0$). The non-degenerate multivariate normal $\vec X=(X_1,\dots,X_n)$ has pdf
$$f_X(x)=\frac{\exp\!\big(-\tfrac12(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)\big)}{(\sqrt{2\pi})^n\sqrt{\det\Sigma}}.$$
Let $Y=OX$ with $O$ an $n\times n$ matrix, $O^{-1}=O^{\mathsf T}$, and $O\Sigma O^{\mathsf T}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ (such an $O$ exists by the spectral theorem for real symmetric matrices; the sheet writes the diagonal entries as $\sigma_1^2,\dots,\sigma_n^2$ and I write $\lambda_i$, see the flag below). **Show** $Y_i\sim N(\mu_i',\lambda_i)$ with $\mu'=O\mu$ and $Y_1,\dots,Y_n$ **independent**.

> [!derivation] Proof (three facts)
> 1. **Jacobian.** $x=O^{\mathsf T}y$, so $\partial x/\partial y=O^{\mathsf T}$ and $|\det O^{\mathsf T}|=1$ (an orthogonal matrix has $\det=\pm1$). By §2, $f_Y(y)=f_X(O^{\mathsf T}y)$: no rescaling.
> 2. **The exponent.** $O^{\mathsf T}y-\mu=O^{\mathsf T}(y-O\mu)=O^{\mathsf T}(y-\mu')$ (using $OO^{\mathsf T}=I$), so
> $$(O^{\mathsf T}y-\mu)^{\mathsf T}\Sigma^{-1}(O^{\mathsf T}y-\mu)=(y-\mu')^{\mathsf T}\,O\Sigma^{-1}O^{\mathsf T}\,(y-\mu'),\qquad O\Sigma^{-1}O^{\mathsf T}=(O\Sigma O^{\mathsf T})^{-1}=\operatorname{diag}(1/\lambda_i),$$
> because $O^{-1}=O^{\mathsf T}$. The quadratic form is $\sum_i(y_i-\mu_i')^2/\lambda_i$: a **sum of squares**, no cross terms.
> 3. **The determinant.** $\det(O\Sigma O^{\mathsf T})=\det O\,\det\Sigma\,\det O^{\mathsf T}=\det\Sigma$, so $\det\Sigma=\prod_i\lambda_i$ and $\sqrt{\det\Sigma}=\prod\sqrt{\lambda_i}$.
>
> Putting the three together,
> $$f_Y(y)=\prod_{i=1}^n\frac1{\sqrt{2\pi\lambda_i}}\exp\!\Big(-\frac{(y_i-\mu_i')^2}{2\lambda_i}\Big),$$
> a product of $N(\mu_i',\lambda_i)$ densities. A joint pdf that factorises means the coordinates are **independent** (§1). $\square$

> [!verify] Notation on the sheet: two different "$\sigma_i^2$"
> The sheet calls the variances of the $X_i$ "$\sigma_i^2$" (so $\Sigma_{ii}=\sigma_i^2$) **and** writes the diagonal matrix $O\Sigma O^{\mathsf T}=\operatorname{diag}(\sigma_1^2,\dots,\sigma_n^2)$ and the conclusion "$Y_i\sim N(\mu_i',\sigma_i^2)$". These are not the same numbers: the diagonal entries are the **eigenvalues** of $\Sigma$, not the variances of the $X_i$. Example below: $\operatorname{Var}X_i=2,2$ but $\operatorname{Var}Y_i=3,1$ (only the **trace** $\operatorname{tr}\Sigma=\sum\lambda_i$ is preserved). I use $\lambda_i$ for the second set.

> [!example] A worked case 🔵: $\Sigma=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $\mu=(1,-1)$
> Eigenvalues $3$ and $1$ with eigenvectors $\frac1{\sqrt2}(1,1)$ and $\frac1{\sqrt2}(1,-1)$, so $O=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $O\Sigma O^{\mathsf T}=\operatorname{diag}(3,1)$, $\det\Sigma=3=3\cdot1$, $\mu'=O\mu=(0,\sqrt2)$. So $Y_1=\frac{X_1+X_2}{\sqrt2}\sim N(0,3)$ and $Y_2=\frac{X_1-X_2}{\sqrt2}\sim N(\sqrt2,1)$, independent. *Checks* (`pr09_numbers.py`): the largest of $1000$ random differences $|f_X(x)-\prod_if_{Y_i}((Ox)_i)|$ is $4\cdot10^{-17}$ (the pdf identity holds to rounding); simulation ($2\cdot10^6$): sample covariance of $Y$ is $\begin{pmatrix}2.996&0.003\\0.003&0.999\end{pmatrix}$, correlation $0.0015$; Kolmogorov distances to $N(0,3)$ and $N(\sqrt2,1)$ are $0.0011$ and $0.0013$. A $3\times3$ case, $\Sigma=\begin{pmatrix}3&1&0.5\\1&2&-0.7\\0.5&-0.7&1.5\end{pmatrix}$, has eigenvalues $0.5801,\,2.3,\,3.6199$ (all positive, so positive definite) and $O\Sigma O^{\mathsf T}$ is diagonal.

**Geometry.** The level sets of $f_X$ are the ellipses $(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)=c$; their **axes are the eigenvectors** and the semi-axes are $\sqrt{c\lambda_i}$. $O$ is the rotation that lines these axes up with the coordinate axes (panel B of the figure); in the new coordinates the ellipse is $\sum(y_i-\mu_i')^2/\lambda_i=c$, with no tilt, which is exactly independence. For $\Sigma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}$ the eigenvalues are $1\pm\rho$: at $\rho=0.8$ the axis lengths are in the ratio $\sqrt{1.8/0.2}=3$.

> [!connection] Why the eigenvalues must be $\ge0$ (the second proof of $|\rho|\le1$, Week 5)
> Week 5 shows $a^{\mathsf T}\Sigma a=\operatorname{Var}(\sum a_iX_i)\ge0$ for all $a$, so every eigenvalue is $\ge0$ (take $a=O^{\mathsf T}e_i$): the covariance matrix is **positive semidefinite**; for $2\times2$ this is $\operatorname{cov}^2\le\operatorname{Var}X\operatorname{Var}Y$, i.e. $|\rho|\le1$ ([[PR07 Sums of Independent Variables Covariance and Correlation]] §5). The same fact shows what "positive definite" buys here: **no zero eigenvalue**, so $\det\Sigma>0$, $\Sigma^{-1}$ exists and the pdf above makes sense. Numbers: $\operatorname{Var}X=4,\operatorname{Var}Y=9$: $\operatorname{Cov}=3$ ($\rho=0.5$) gives eigenvalues $2.5949,\,10.4051$; $\operatorname{Cov}=6$ ($\rho=1$, $Y=1.5X$) gives $0,\,13$ (degenerate: the distribution lives on a line); $\operatorname{Cov}=7$ ($\rho=1.1667$) gives $-0.933,\,13.933$: not a covariance matrix. The instructor's remark that the same diagonalisation underlies "observables are Hermitian operators" in quantum mechanics (real eigenvalues, an orthonormal eigenbasis; unitary $U$ instead of $O$) is on the Week 5 page ([[QM03 States Operators and Measurement]]).

> [!warning] Uncorrelated $\Rightarrow$ independent only here
> The result says: for **jointly normal** variables, a diagonal covariance matrix gives independence. For general variables $\operatorname{cov}=0$ does *not* imply independence (the disc of §1, $X$ and $X^2$ for $X\sim N(0,1)$; PR07). Independent normal *marginals* do not make a jointly normal vector either; the theorem is about the joint pdf above.

## 4. Homework 6, Q2: $-\ln U$ and the product of uniforms #quiz/pr-hw6
<span class="scope-taught">taught</span> *Source: [[hw6_edited.pdf#page=1|HW6, Q2]]* · <span class="scope-extra-beyond">extra · beyond</span> *Gamma, the density of the product, the moments*

$U_1,\dots,U_n$ iid $U(0,1)$, $X_j=-\ln U_j$ (the sheet writes "$-\ln$" in (a) and "$-\log$" in (b); both are the natural logarithm).

**(a) $X_j\sim\mathrm{Expo}(1)$.** For $x\ge0$: $P(X_j>x)=P(-\ln U_j>x)=P(U_j<e^{-x})=e^{-x}$, the survival function of $\mathrm{Expo}(1)$. (By §2: $U=e^{-X}$, $|\mathrm dU/\mathrm dX|=e^{-x}$, $f_X(x)=1\cdot e^{-x}$.) This is the idea of **inverse-transform sampling**: [[Probability Integral Transform]]. Checked: $P(X>1)=0.36724$ against $e^{-1}=0.36788$, mean $0.9984$, variance $0.9974$.

**(b) The product $U=U_1U_2\cdots U_n$.** Pass to $V=-\ln U=\sum_jX_j$, a sum of $n$ independent $\mathrm{Expo}(1)$ variables. Each has mgf $M_X(t)=\int_0^\infty e^{tx}e^{-x}\mathrm dx=\frac1{1-t}$ ($t<1$), so $M_V(t)=(1-t)^{-n}$ and
$$V\sim\mathrm{Gamma}(n,1):\qquad f_V(v)=\frac{v^{n-1}e^{-v}}{(n-1)!},\ v>0$$
(the sum of $n$ iid exponentials; [[Sum of Independent Random Variables]], [[Gamma Distribution]]). Now $U=e^{-V}$, $v=-\ln u$, $|\mathrm dv/\mathrm du|=\frac1u$, so by §2
$$\boxed{f_U(u)=f_V(-\ln u)\cdot\frac1u=\frac{(-\ln u)^{n-1}\,u}{(n-1)!}\cdot\frac1u=\frac{(-\ln u)^{n-1}}{(n-1)!},\qquad0<u<1.}$$
$n=1$ is the uniform density; $n=2$ is $-\ln u$. The density piles up at $0$ (panel C): products of uniforms are small.

*Checks, $n=5$:* $f_U$ integrates to $1.000000$; $f_U(0.01)=18.7401$, histogram $18.7475$; $V$ has mean $4.9971$ and variance $4.9903$ ($=5,5$ for $\mathrm{Gamma}(5,1)$), mgf at $t=0.3$: simulation $5.94356$, $(0.7)^{-5}=5.94990$. **Moments from independence,** $E[U_j^k]=\frac1{k+1}$: $E[U^k]=(k+1)^{-n}$, so $E[U]=2^{-n}=0.03125$ (numeric $0.03125$, simulation $0.03124$), $E[U^2]=3^{-5}=0.004115$ and $\operatorname{Var}U=3^{-n}-4^{-n}=0.003139$ (simulation $0.003123$). For $n=2$, $P(U_1U_2<0.1)=\int_0^{0.1}(-\ln u)\,\mathrm du=0.1(1-\ln0.1)=0.330259$ (simulation $0.329797$).

## 5. Homework 6, Q3: the tangent line lies below a convex graph; Jensen #quiz/pr-hw6
<span class="scope-taught">taught</span> *Source: [[hw6_edited.pdf#page=1|HW6, Q3]]* · <span class="scope-extra-beyond">extra · beyond</span> *Jensen's inequality from the lemma, the quantitative form, examples*

**The problem.** $g:\mathbb R\to\mathbb R$ with $g''(t)>0$. **Show** the tangent line to the graph of $g$ lies below the graph ("this fact was used in the proof of Jensen's inequality $E(g(X))\ge g(E(X))$").

> [!key] Lemma
> If $g''>0$ then for every $a$ and every $x\ne a$: $\ g(x)>g(a)+g'(a)(x-a)$.
> *Proof.* Put $h(x)=g(x)-g(a)-g'(a)(x-a)$. Then $h(a)=0$ and $h'(x)=g'(x)-g'(a)$. Since $g''>0$, $g'$ is **strictly increasing**, so $h'<0$ for $x<a$ and $h'>0$ for $x>a$: $h$ decreases to $a$ and increases after it, so $a$ is the strict global minimum and $h(x)>h(a)=0$ for $x\ne a$. $\square$
> (*Alternative:* Taylor with Lagrange remainder, $g(x)=g(a)+g'(a)(x-a)+\tfrac12g''(\xi)(x-a)^2$ for some $\xi$ between $a$ and $x$; the last term is $>0$.)

> [!key] Jensen's inequality 🔵
> If $g''>0$ (or just $g$ convex on an interval containing the values of $X$) and $E|X|$, $E|g(X)|<\infty$, then $\ E[g(X)]\ge g(E[X])$, with equality iff $X$ is constant (almost surely) when $g''>0$.
> *Proof.* Take $a=\mu=E[X]$ in the lemma and plug in the random variable: $g(X)\ge g(\mu)+g'(\mu)(X-\mu)$. Take expectations: $E[g(X)]\ge g(\mu)+g'(\mu)\,E[X-\mu]=g(\mu)$. Strictness: the inequality is strict wherever $X\ne\mu$. $\square$
> **Quantitative form.** If $g''\ge m>0$ then $E[g(X)]-g(E[X])\ge\frac m2\operatorname{Var}X$ (use $\frac12g''(\xi)\ge\frac m2$ in the Taylor remainder). Example: $g=e^x$, $X\sim U(0,1)$, $m=1$: bound $\frac1{24}=0.04167$, actual gap $(e-1)-e^{1/2}=0.06956$ (simulation $0.06954$).

*Numbers (`pr09_numbers.py`).* On $[-6,6]$ the gap $g(x)-\text{tangent}(x)$ has minimum exactly $0$ at $x=a$ for $e^x$ ($a=0$), $x^4$ ($a=1$), $x^2$ ($a=-2$). $X\sim N(0,1)$, $g=e^x$: $E\,e^X=e^{1/2}=1.6487\ge e^0=1$ (simulation $1.64798$). $g=1/x$ on $(1,3)$ (convex there), $X\sim U(1,3)$: $E[1/X]=\frac{\ln3}2=0.5493\ge\frac1{E X}=0.5$.

*Consequences* 🔵: $g=x^2$ gives $E[X^2]\ge(E[X])^2$, i.e. $\operatorname{Var}X\ge0$; $g=e^{tx}$ gives $M_X(t)\ge e^{tE[X]}$; $g=-\ln$ gives the **AM–GM inequality** (a positive sample $(1,4,16)$ has geometric mean $4\le$ arithmetic mean $7$).

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Rotating a correlated Gaussian to independent coordinates (HW6 Q1)
> A bivariate normal with s.d.
>
> ![[pr_mvn_rotation.png|720]]
>
> **Try:** σ₁ = σ₂ = 1.5, ρ = 0.8: the eigenvectors are at θ = 45° and the eigenvalues are σ²(1 ± ρ) = 4.05 and 0.45 (ratio of the axis lengths 3); at θ = 45° the Y-cloud is an upright ellipse with correlation 0. Then take σ₁ = 2, σ₂ = 1, ρ = 0.5: the snap angle is not 45° and Var Y₁ + Var Y₂ stays σ₁² + σ₂² = 5 for every θ.
>
> [▶ Open the tool in your browser](../Assets/interactive/pr_mvn_rotation.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/pr_mvn_rotation.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How PR09 connects
> **Builds on:** [[PR05 Continuous Random Variables]] (pdf, cdf method, exponential, normal), [[PR07 Sums of Independent Variables Covariance and Correlation]] (joint density, covariance matrix, $|\rho|\le1$, uncorrelated but dependent), [[PR08 Order Statistics and the Multinomial Distribution]] (the change of variables $(Y_1,Y_2)\to(Y_1,Y_2-Y_1)$ and the independent min and gap), [[PR06 Moments Generating Functions and Limit Theorems]] (mgf of a sum).
> **Leads to:** the **central limit theorem for vectors** (sums of iid vectors converge to $N(0,\Sigma)$), **linear regression and the $\chi^2$, $t$ and $F$ distributions** (all consequences of the rotation of §3 and the $\chi^2_1$ of §2), **maximum likelihood and the Fisher information** (Jensen gives $D(p\|q)\ge0$), Monte Carlo (Box–Muller, inverse transform), **statistical mechanics** (a product of many independent factors is the exponential of a sum: the log-normal and Gamma shapes of §4).
> **Concepts:** [[Conditional Density Function]] · [[Change of Variables for Densities]] · [[Multivariate Normal Distribution]] · [[Gamma Distribution]] · [[Jensen's Inequality]] · [[Box-Muller Transform]]
> **Other subjects:** [[Quantum Mechanics - Course Map]] (observables as Hermitian operators diagonalised by a unitary $U$: the same theorem as the orthogonal $O$ of §3; [[QM03 States Operators and Measurement]]), [[Thermodynamics and Statistical Mechanics - Course Map]] (Gaussian integrals and the Jacobian in the equipartition and Maxwell–Boltzmann calculations: the polar-coordinate trick of §2 evaluates $\int e^{-x^2/2}$; Jensen's inequality gives $\langle e^{-\beta E}\rangle\ge e^{-\beta\langle E\rangle}$ and the **Gibbs inequality**, see [[SM01 Probability Large Numbers and Information]]), [[Differential Geometry - Course Map]] (the Jacobian is the differential of a smooth map in coordinates: [[DM03 Tangent Vectors and the Differential]]; the formula $D(g^{-1})=(Dg)^{-1}$ of §2 is the inverse function theorem, [[PA13 The Derivative and the Inverse Function Theorem]]), [[Group Theory - Course Map]] (the orthogonal group $O(n)$ acts on the multivariate normal by isometries).

## Summary
> [!summary] Cheat-sheet
> - **Marginal** $=\int$ the rest; **conditional** $f_{Y|X}=f_{X,Y}/f_X$; **Bayes** $f_{Y|X}=f_{X|Y}f_Y/f_X$; independence $\iff f=f_Xf_Y\iff F=F_XF_Y$ (also for survival functions).
> - Uniform on a disc: marginal $\frac2{\pi R}\sqrt{1-(x/R)^2}$ (semicircle), conditional uniform on the chord. Week 4's "Poisson" example is the **exponential** race $P(X_1<X_2)=\frac{\lambda_1}{\lambda_1+\lambda_2}$.
> - **Change of variables:** $f_Y(y)=f_X(g^{-1}(y))\,|\det\partial g^{-1}/\partial y|=f_X(g^{-1}(y))/|\det\partial g/\partial x|$; several roots: sum the terms. Polar: Jacobian $r$, $R\sim$ Rayleigh, $\Theta\sim U[0,2\pi)$ independent; Box–Muller $R=\sqrt{-2\ln U_1}$, $\Theta=2\pi U_2$.
> - **Multivariate normal:** $f_X=\exp(-\frac12(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu))/((2\pi)^{n/2}\sqrt{\det\Sigma})$. $Y=OX$, $O\Sigma O^{\mathsf T}=\operatorname{diag}(\lambda)$: $Y_i\sim N((O\mu)_i,\lambda_i)$ **independent** ($|\det O|=1$, exponent $\to\sum(y_i-\mu_i')^2/\lambda_i$, $\det\Sigma=\prod\lambda_i$); the $\lambda_i$ are eigenvalues (not $\Sigma_{ii}$); $\Sigma\succeq0$ is $|\rho|\le1$.
> - $-\ln U\sim\mathrm{Expo}(1)$; $-\ln(U_1\cdots U_n)\sim\mathrm{Gamma}(n,1)$; $f_{U_1\cdots U_n}(u)=(-\ln u)^{n-1}/(n-1)!$; $E[U^k]=(k+1)^{-n}$.
> - $g''>0\Rightarrow g(x)>g(a)+g'(a)(x-a)$ (the function $h=g-\text{tangent}$ has $h'$ increasing through $0$ at $a$); **Jensen** $E g(X)\ge g(EX)$; gap $\ge\frac m2\operatorname{Var}X$ if $g''\ge m$.

## Practice
1. **A disc marginal.** $(X_1,X_2)$ uniform on the disc of radius $R=2$. Find $f_{X_1}$, $P(|X_1|<1)$ and the conditional density of $X_2$ given $X_1=1$.
2. **The race.** $X_1\sim\mathrm{Expo}(2)$, $X_2\sim\mathrm{Expo}(3)$ independent: find $P(X_1<X_2)$. Then do the same for $X_i\sim\mathrm{Poisson}(2),\mathrm{Poisson}(3)$ in one sentence (what changes?).
3. **A one-variable change.** $X\sim\mathrm{Expo}(1)$, $Y=\sqrt X$: find $f_Y$, $E[Y]$ and $P(Y>1)$.
4. **A linear map.** $X_1,X_2$ iid $N(0,1)$, $Y_1=X_1+X_2$, $Y_2=X_1-X_2$: find the joint density of $(Y_1,Y_2)$ and show $Y_1,Y_2$ are independent $N(0,2)$.
5. **Polar coordinates.** For iid $N(0,1)$ variables $X,Y$ show $R^2=X^2+Y^2\sim\mathrm{Expo}(\tfrac12)$ and find $P(R^2>3)$.
6. **A $2\times2$ Gaussian.** $\Sigma=\begin{pmatrix}5&3\\3&5\end{pmatrix}$, $\mu=0$. Find $O$, the laws of $Y_1,Y_2$ and the law of $X_1+X_2$.
7. **Geometry.** For $\Sigma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}$ with $\rho=0.8$: eigenvalues, eigenvectors and the ratio of the ellipse's axis lengths.
8. **Sampling.** Show that $-\frac1\lambda\ln U\sim\mathrm{Expo}(\lambda)$; compute $P(X>1)$ for $\lambda=2$.
9. **Three uniforms.** $U=U_1U_2U_3$: find $f_U$, $E[U]$ and $P(U<\tfrac18)$.
10. **Jensen.** $X\in\{1,3\}$ with probability $\frac12$ each: check $E[X^2]\ge(EX)^2$ and $E[1/X]\ge1/E[X]$. Why does the second inequality need $g=1/x$ convex on $(0,\infty)$ rather than $g''>0$ on $\mathbb R$?
11. **A tangent line.** Show $e^x\ge ex$ for all real $x$ with equality only at $x=1$, and deduce $\ln x\le x/e$ for $x>0$.

> [!example]- Solutions
> 1. $f_{X_1}(x)=\frac{2\sqrt{4-x^2}}{4\pi}=\frac{\sqrt{4-x^2}}{2\pi}$, $|x|\le2$. $P(|X_1|<1)=\frac{\sqrt3}{2\pi}+\frac13=0.6090$. Conditional on $X_1=1$: uniform on $|y|\le\sqrt3=1.732$, density $\frac1{2\sqrt3}=0.2887$.
> 2. $P(X_1<X_2)=\frac{\lambda_1}{\lambda_1+\lambda_2}=\frac25=0.4$ (§1). For Poisson variables it is $\sum_kP(X_1=k)P(X_2>k)=0.5853$: the integrals become sums and the answer is *not* $\frac25$ ($P(X_1=X_2)=0.1677$ no longer vanishes).
> 3. $x=y^2$, $\mathrm dx/\mathrm dy=2y$: $f_Y(y)=2ye^{-y^2}$, $y>0$ (a Weibull). $E[Y]=\int_0^\infty2y^2e^{-y^2}\mathrm dy=\frac{\sqrt\pi}2=0.8862$; $P(Y>1)=P(X>1)=e^{-1}=0.3679$.
> 4. $y=Ax$, $A=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $|\det A|=2$, $x=A^{-1}y$: $x_1^2+x_2^2=\frac{y_1^2+y_2^2}2$. $f_Y=\frac12\cdot\frac1{2\pi}e^{-(y_1^2+y_2^2)/4}=\frac1{\sqrt{4\pi}}e^{-y_1^2/4}\cdot\frac1{\sqrt{4\pi}}e^{-y_2^2/4}$: independent $N(0,2)$ (this is §3 with $\Sigma=I$ and $O=A/\sqrt2$ followed by a scaling by $\sqrt2$).
> 5. Polar: $f_{R,\Theta}=\frac1{2\pi}re^{-r^2/2}$, so $P(R>\rho)=e^{-\rho^2/2}$ and $P(R^2>s)=e^{-s/2}$: $\mathrm{Expo}(\tfrac12)$, mean $2$. $P(R^2>3)=e^{-3/2}=0.2231$.
> 6. Eigenvalues $8$ (eigenvector $(1,1)/\sqrt2$) and $2$ ($(1,-1)/\sqrt2$); $\det\Sigma=16=8\cdot2$. $Y_1=\frac{X_1+X_2}{\sqrt2}\sim N(0,8)$, $Y_2=\frac{X_1-X_2}{\sqrt2}\sim N(0,2)$ independent. $X_1+X_2=\sqrt2Y_1\sim N(0,16)$ ($=5+5+2\cdot3$).
> 7. Eigenvalues $1\pm\rho=1.8,\,0.2$ with eigenvectors $\frac1{\sqrt2}(1,\pm1)$; axis ratio $\sqrt{1.8/0.2}=3$.
> 8. $P(-\frac1\lambda\ln U>x)=P(U<e^{-\lambda x})=e^{-\lambda x}$. $\lambda=2$: $P(X>1)=e^{-2}=0.1353$.
> 9. $f_U(u)=\frac{(\ln u)^2}2$ on $(0,1)$; $E[U]=2^{-3}=\frac18$; $P(U<\frac18)=\Big[\frac u2\big((\ln u)^2-2\ln u+2\big)\Big]_0^{1/8}=\frac1{16}(4.3241+4.1589+2)=0.6552$ (simulation $0.65519$).
> 10. $E[X^2]=5\ge4=(EX)^2$; $E[1/X]=\frac23\ge\frac12$. The values of $X$ lie in $(0,\infty)$ where $1/x$ is convex ($g''=2/x^3>0$); $g''>0$ on all of $\mathbb R$ fails for $1/x$ (undefined at $0$, concave for $x<0$), and Jensen only needs convexity on an interval containing the range of $X$.
> 11. $e^x$ has $g''>0$; the tangent at $a=1$ is $e+e(x-1)=ex$; the lemma gives $e^x>ex$ for $x\ne1$. For $s>0$ take logarithms of $e^s\ge es$: $s\ge1+\ln s$. Put $s=x/e$: $\frac xe\ge1+\ln\frac xe=\ln x$, i.e. $\ln x\le x/e$ (equality at $x=e$).

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (1): the other tool's concept notes from the lectures, unreviewed
> [[zettel/language-model-conditional-probability-generation|Language Model Conditional Probability Generation]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | vector-valued variables, marginals, independence by factorisation of pdf/cdf/survival function, conditional pdf, Bayes for densities, the disc marginal, Example 2, the mgf of a sum | [[Week4_notes.pdf#page=2\|Week 4 notes pp. 2–4]] (handwritten, read from the page images this session); the other tool's note [[introduction-to-probability/2026-10-29-week-4-notes\|Week 4 notes]] (it could read only the HW4 Q4 line) | taught |
> | the change-of-variables formula in 1-D and $n$-D | [[Week5_notes.pdf#page=8\|Week 5 notes pp. 8–9]] (read from images); the other tool's transcription [[introduction-to-probability/2026-11-05-week-5-notes\|Week 5 notes]] (checked: it agrees) | taught |
> | HW6 Q1 (multivariate normal), Q2 ($-\ln U$, the product), Q3 (tangent line, Jensen) | [[hw6_edited.pdf#page=1\|HW6]] (one handwritten page, read from the image) | taught |
> | Homework 4 and the Week 5 covariance, min/max, multinomial pages | already in [[PR07 Sums of Independent Variables Covariance and Correlation]] and [[PR08 Order Statistics and the Multinomial Distribution]] (compared; not repeated) | taught |
> | corrected "Poisson" race, non-injective maps, polar and Box–Muller, the proof of §3, the geometry, Gamma identification, the density and moments of the product, Jensen from the lemma, quantitative form, AM–GM, Practice | derived here; `scripts/pr09_numbers.py` (simulation up to $2\cdot10^6$ draws, numerical integration), `scripts/fig_pr09.py`, tool `pr_mvn_rotation` | extra/beyond |
>
> **Notes.** No textbook was consulted; the formulas are checked numerically rather than cited. The homework solutions are mine (the instructor posted none for HW6). The three ambiguities flagged above are (1) the constant $\frac1R$ in the disc marginal, (2) the label "Poisson" on the exponential race, (3) the two meanings of $\sigma_i^2$ in HW6 Q1. Week 5's pages 1–2 repeat Homework 5 and were not re-read for this chapter beyond what PR08 already covers.

**References.** Box, G. E. P. & Muller, M. E. (1958) *A note on the generation of random normal deviates*, Ann. Math. Stat. 29 · Jensen, J. L. W. V. (1906) *Sur les fonctions convexes et les inégalités entre les valeurs moyennes*, Acta Math. 30. *(The two historical sources for the names, cited by title only; not consulted. No textbook was used.)*
