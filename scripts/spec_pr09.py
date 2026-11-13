"""Concept notes for PR09 (change of variables, multivariate normal, products of uniforms, Jensen).   .venv/bin/python -W ignore scripts/spec_pr09.py"""
from mkconcept import write

CH = "PR09 Change of Variables the Multivariate Normal and Products of Uniforms"
T, EBY = "taught", "extra-beyond"
BY = ["lecture-notes", "own-notes"]
W4 = "[[Week4_notes.pdf#page=2|Week 4 notes]]"
W5 = "[[Week5_notes.pdf#page=8|Week 5 notes]]"
HW = "[[hw6_edited.pdf#page=1|HW6]]"

ITEMS = [
    dict(title="Conditional Density Function", aliases=["conditional pdf", "f_{Y|X}", "Bayes rule for densities", "conditional density"], scope=[T, EBY], by=BY,
         syl={T: f"{W4}, p. 3: $f_{{Y|X}}=f_{{X,Y}}/f_X$, Bayes' rule for densities, the uniform-disc example.", EBY: "the chord interpretation and the numerical Bayes check (mine)."},
         intuition="Take the joint density, cut it along the line $X=x$, and **rescale the slice so that its area is 1**: the denominator $f_X(x)$ is exactly the area of the slice.",
         key="$f_{Y\\mid X}(y\\mid x)=\\dfrac{f_{X,Y}(x,y)}{f_X(x)}$ where $f_X(x)>0$; $\\int f_{Y\\mid X}(y\\mid x)\\,\\mathrm dy=1$. **Bayes:** $f_{Y\\mid X}(y\\mid x)=\\dfrac{f_{X\\mid Y}(x\\mid y)\\,f_Y(y)}{f_X(x)}$. Independence $\\iff f_{Y\\mid X}(y\\mid x)=f_Y(y)$ for all $x$.",
         body="Uniform on the disc of radius $R$: $f_{X_1}(x)=\\frac{2\\sqrt{R^2-x^2}}{\\pi R^2}$ and $X_2\\mid X_1=x$ is uniform on the chord $|y|\\le\\sqrt{R^2-x^2}$, density $\\frac1{2\\sqrt{R^2-x^2}}$ ($R=2$, $x=1$: $0.2887$). The chord length depends on $x$, so $X_1,X_2$ are dependent although uncorrelated.",
         used=[CH, "PR07 Sums of Independent Variables Covariance and Correlation"], related=["Joint Density Function", "Marginal Distribution", "Conditional Probability", "Bayes' Theorem", "Independence of Random Variables", "Probability Density Function"]),
    dict(title="Change of Variables for Densities", aliases=["Jacobian", "transformation of densities", "f_Y = f_X(g^{-1}(y)) |dg^{-1}/dy|", "density of g(X)", "determinant of the Jacobian"], scope=[T, EBY], by=BY,
         syl={T: f"{W5}, pp. 8–9: the formula in one variable and in $n$ variables with $\\det\\partial g^{-1}/\\partial y$.", EBY: "several roots, polar coordinates, the linear map and Box–Muller examples (mine, simulation-checked)."},
         intuition="Probability is conserved; densities are probability per unit length (area, volume). Stretch space by a factor $|\\det Dg|$ and the density is divided by it.",
         key="$Y=g(X)$, $g$ invertible: $f_Y(y)=f_X(g^{-1}(y))\\,\\Big|\\dfrac{\\mathrm dg^{-1}}{\\mathrm dy}(y)\\Big|=\\dfrac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}$. In $n$ variables: $f_Y(y)=f_X(g^{-1}(y))\\,|\\det\\partial g^{-1}/\\partial y|=f_X(g^{-1}(y))/|\\det\\partial g/\\partial x|$. Several roots $x_i$ of $g(x)=y$: sum $f_X(x_i)/|g'(x_i)|$.",
         body="$Y=e^X$ ($X\\sim N(0,1)$): $f_Y=\\varphi(\\ln y)/y$. $Y=X^2$: $\\frac{e^{-y/2}}{\\sqrt{2\\pi y}}$ (two roots). $Y=AX$: divide by $|\\det A|$. Polar coordinates (Jacobian $r$): iid $N(0,1)$ pairs give $R\\sim$ Rayleigh and $\\Theta\\sim U[0,2\\pi)$ independent.",
         used=[CH, "PR05 Continuous Random Variables", "PR08 Order Statistics and the Multinomial Distribution"], related=["Cdf Method for Transformations", "Probability Integral Transform", "Box-Muller Transform", "Rayleigh Distribution", "Multivariate Normal Distribution", "Joint Density Function"]),
    dict(title="Multivariate Normal Distribution", aliases=["multivariate Gaussian", "N(mu, Sigma)", "jointly normal", "non-degenerate multivariate normal", "orthogonal diagonalisation of the covariance matrix"], scope=[T, EBY], by=BY,
         syl={T: f"{HW}, Q1: the pdf, $Y=OX$ with $O\\Sigma O^{{\\mathsf T}}$ diagonal $\\Rightarrow$ independent normals.", EBY: "the three-step proof, the geometry and the numerical checks (mine)."},
         intuition="A bell-shaped cloud whose level sets are ellipses. Rotate to the ellipse's axes and the cloud becomes a product of one-dimensional bells: **independent** coordinates whose variances are the eigenvalues of $\\Sigma$.",
         key="$X\\sim N(\\mu,\\Sigma)$ with $\\Sigma\\succ0$: $f_X(x)=\\dfrac{\\exp(-\\frac12(x-\\mu)^{\\mathsf T}\\Sigma^{-1}(x-\\mu))}{(2\\pi)^{n/2}\\sqrt{\\det\\Sigma}}$. If $O^{-1}=O^{\\mathsf T}$ and $O\\Sigma O^{\\mathsf T}=\\operatorname{diag}(\\lambda_i)$ then $Y=OX$ has independent coordinates $Y_i\\sim N((O\\mu)_i,\\lambda_i)$.",
         body="Proof: $|\\det O|=1$; the exponent becomes $\\sum(y_i-\\mu_i')^2/\\lambda_i$; $\\det\\Sigma=\\prod\\lambda_i$. $\\Sigma=\\begin{pmatrix}2&1\\\\1&2\\end{pmatrix}$: $\\lambda=3,1$, $Y_1=\\frac{X_1+X_2}{\\sqrt2}$, $Y_2=\\frac{X_1-X_2}{\\sqrt2}$. Only the trace is preserved ($\\operatorname{Var}X_i=2,2$ against $\\operatorname{Var}Y_i=3,1$). For *jointly* normal variables uncorrelated $\\Rightarrow$ independent.",
         used=[CH, "PR07 Sums of Independent Variables Covariance and Correlation", "QM03 States Operators and Measurement"], related=["Covariance Matrix", "Normal Distribution", "Standard Normal Distribution", "Change of Variables for Densities", "Independence of Random Variables", "Covariance and Correlation"]),
    dict(title="Gamma Distribution", aliases=["Gamma(n,1)", "Erlang distribution", "sum of exponentials", "waiting time for the n-th event"], scope=[EBY], by=BY,
         syl={EBY: f"identified in the solution of {HW} Q2(b) (my derivation; the sheet does not name it)."},
         intuition="The time to collect $n$ independent $\\mathrm{Expo}(1)$ waiting times: a sum of exponentials, so a bump whose peak moves out like $n-1$.",
         key="$V\\sim\\mathrm{Gamma}(n,1)$: $f_V(v)=\\dfrac{v^{n-1}e^{-v}}{(n-1)!}$, $v>0$; mgf $(1-t)^{-n}$ ($t<1$); mean $n$, variance $n$. $V=\\sum_{j=1}^nX_j$, $X_j$ iid $\\mathrm{Expo}(1)$ (mgf product $\\frac1{(1-t)^n}$). $-\\ln(U_1\\cdots U_n)\\sim\\mathrm{Gamma}(n,1)$ for iid $U_j\\sim U(0,1)$.",
         body="The product $U=U_1\\cdots U_n=e^{-V}$ has density $\\dfrac{(-\\ln u)^{n-1}}{(n-1)!}$ on $(0,1)$ and $E[U^k]=(k+1)^{-n}$. Checked for $n=5$: $V$ has mean $4.997$ and variance $4.990$; $E[U]=2^{-5}=0.03125$.",
         used=[CH], related=["Exponential Distribution", "Sum of Independent Random Variables", "Moment Generating Function", "Poisson Distribution", "Probability Integral Transform", "Change of Variables for Densities"]),
    dict(title="Jensen's Inequality", aliases=["Jensen inequality", "E g(X) >= g(E X)", "convex function inequality", "tangent line below the graph", "AM-GM from Jensen"], scope=[T, EBY], by=BY,
         syl={T: f"{HW} Q3: the tangent line of $g$ with $g''>0$ lies below the graph (the sheet says this is used in the proof of Jensen).", EBY: "Jensen's inequality from the lemma, the quantitative form, AM–GM (mine)."},
         intuition="A convex curve sags below its chords and **sits above its tangents**; averaging the inequality 'curve $\\ge$ tangent at the mean' over the random variable gives 'average of the curve $\\ge$ curve at the average'.",
         key="**Lemma:** $g''>0\\Rightarrow g(x)>g(a)+g'(a)(x-a)$ for $x\\ne a$ ($h=g-\\text{tangent}$ has $h'$ increasing through $0$ at $a$). **Jensen:** $g$ convex $\\Rightarrow E[g(X)]\\ge g(E[X])$ (take $a=E X$, expectation of $g(X)\\ge g(\\mu)+g'(\\mu)(X-\\mu)$); equality iff $X$ constant when $g''>0$. If $g''\\ge m>0$: $E g(X)-g(EX)\\ge\\frac m2\\operatorname{Var}X$.",
         body="$g=x^2$: $\\operatorname{Var}X\\ge0$. $g=e^{tx}$: $M_X(t)\\ge e^{tEX}$. $g=-\\ln$: AM–GM ($(1,4,16)$: GM $4\\le$ AM $7$). $X\\sim N(0,1)$: $E e^X=e^{1/2}=1.6487\\ge1$. $e^x\\ge ex$ with equality only at $x=1$, so $\\ln x\\le x/e$.",
         used=[CH, "PR06 Moments Generating Functions and Limit Theorems"], related=["Expectation", "Variance", "Moment Generating Function", "Law of the Unconscious Statistician", "Markov and Chebyshev Inequalities"]),
    dict(title="Box-Muller Transform", aliases=["Box–Muller", "generating normal random variables", "polar method for normals", "Rayleigh from uniforms"], scope=[EBY], by=BY,
         syl={EBY: "the polar-coordinate use of the change-of-variables formula (mine; Box and Muller 1958 is the source of the name)."},
         intuition="Two independent normals form a point in the plane whose **direction is uniform** and whose **distance has the Rayleigh law**; run it backwards and two uniforms make two normals.",
         key="For independent $U_1,U_2\\sim U(0,1)$: $R=\\sqrt{-2\\ln U_1}$ (so $P(R>r)=e^{-r^2/2}$) and $\\Theta=2\\pi U_2$; then $X=R\\cos\\Theta$, $Y=R\\sin\\Theta$ are **independent $N(0,1)$**. Reason: polar coordinates have Jacobian $r$, so $\\frac1{2\\pi}e^{-(x^2+y^2)/2}\\,\\mathrm dx\\,\\mathrm dy=(re^{-r^2/2}\\,\\mathrm dr)\\,\\frac{\\mathrm d\\theta}{2\\pi}$.",
         body="Checked on $2\\cdot10^6$ draws: means $-0.0005,0.0003$, variances $0.9998,0.9990$, correlation $0.0005$; $P(R<1)=1-e^{-1/2}=0.3935$ (simulation $0.3933$). The integral $\\iint e^{-(x^2+y^2)/2}=2\\pi$ is the same computation: $\\int e^{-x^2/2}\\mathrm dx=\\sqrt{2\\pi}$.",
         used=[CH], related=["Change of Variables for Densities", "Rayleigh Distribution", "Standard Normal Distribution", "Probability Integral Transform", "Uniform Distribution"]),
]

if __name__ == "__main__":
    write("08-Probability", "probability", ITEMS)
