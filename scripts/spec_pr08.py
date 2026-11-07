"""Concept notes for PR08 (order statistics, multinomial).   .venv/bin/python -W ignore scripts/spec_pr08.py"""
from mkconcept import write

CH = "PR08 Order Statistics and the Multinomial Distribution"
T, EBY = "taught", "extra-beyond"
BY = ["lecture-notes", "own-notes"]
HW = "[[hw5.pdf#page=1|HW5]]"

ITEMS = [
    dict(title="Order Statistics", aliases=["order statistic", "k-th smallest", "sorted sample", "minimum and maximum", "Y(k)"], scope=[T, EBY], by=BY,
         syl={T: f"{HW}, Problems 1–2 (min and max of two; the sorted sample of $n$).", EBY: "the $k$-th order statistic for general $n$ (my derivation, simulation-checked)."},
         intuition="Sort $n$ independent draws: the sorted values are *dependent* (each is squeezed between its neighbours) even though the draws were independent.",
         key="$Y_{(1)}\\le\\dots\\le Y_{(n)}$ the sorted iid sample (cdf $F$, density $f$). $Y_{(1)}=\\min$, $Y_{(n)}=\\max$; $f_{Y_{(k)}}=\\frac{n!}{(k-1)!(n-k)!}F^{k-1}(1-F)^{n-k}f$; $F_{\\max}=F^n$, $F_{\\min}=1-(1-F)^n$. Uniform$(0,1)$: $Y_{(k)}\\sim\\mathrm{Beta}(k,n-k+1)$, mean $\\frac{k}{n+1}$.",
         body="$n=5$ uniforms: means $\\frac16,\\frac26,\\frac36,\\frac46,\\frac56$ (simulation $0.1666\\ldots0.8334$). $n=3$ uniforms: median density $6y(1-y)$, $P(\\text{median}>0.7)=0.216$.",
         used=[CH], related=["Joint Density of Order Statistics", "Exponential Order Statistics", "Cumulative Distribution Function", "Uniform Distribution", "Joint Density Function"]),
    dict(title="Joint Density of Order Statistics", aliases=["joint density of the sorted sample", "n! f(y1)...f(yn)", "min and max joint density", "two preimages"], scope=[T], by=BY,
         syl={T: f"{HW} Problem 1 and the instructor's solution [[HW-5, Q.1.jpg]]."},
         intuition="Sorting forgets the labels: $n!$ different orderings of the labels give the same sorted vector, so the density on the ordered region is $n!$ times the product density.",
         key="For iid $X_i$ with density $f$: $f_{Y_1,\\dots,Y_n}(y_1,\\dots,y_n)=n!\\,f(y_1)\\cdots f(y_n)$ on $y_1<\\dots<y_n$ ($0$ elsewhere). For $n=2$: $f_{Y_1,Y_2}=2f(y_1)f(y_2)$, proved by the two preimages $(y_1,y_2),(y_2,y_1)$ or by $F_{Y_1,Y_2}=2F(y_1)F(y_2)-F(y_1)^2$ and $\\partial^2/\\partial y_1\\partial y_2$.",
         body="Check: Expo(1), $y_1=0.5,y_2=1.2$: cdf formula $0.39510$ vs simulation $0.39502$; $\\iint_{y_1<y_2}2f f=1$.",
         used=[CH], related=["Order Statistics", "Cdf Method for Transformations", "Joint Density Function"]),
    dict(title="Exponential Order Statistics", aliases=["Renyi representation", "gaps of exponential order statistics", "minimum of exponentials", "HW5 Problem 2"], scope=[T, EBY], by=BY,
         syl={T: f"{HW} Problem 2 ($n=2$).", EBY: "the general-$n$ spacings (my argument by repeated memorylessness, simulation-checked)."},
         intuition="$n$ independent alarm clocks: the first rings at rate $n\\lambda$; after that the survivors are \"as good as new\" (memoryless), so the next ring comes at rate $(n-1)\\lambda$, and so on.",
         key="For iid $\\mathrm{Expo}(\\lambda)$: $Y_{(k)}-Y_{(k-1)}\\sim\\mathrm{Expo}((n-k+1)\\lambda)$, independent; $E[Y_{(k)}]=\\frac1\\lambda\\sum_{j=1}^k\\frac{1}{n-j+1}$, $E[\\max]=H_n/\\lambda$. For $n=2$: $Y_1\\sim\\mathrm{Expo}(2\\lambda)$, $Y_2-Y_1\\sim\\mathrm{Expo}(\\lambda)$ independent of $Y_1$; $\\mathrm{Var}\\,Y_2=\\frac5{4\\lambda^2}$, $\\mathrm{Corr}(Y_1,Y_2)=\\frac1{\\sqrt5}$.",
         body="Two parallel components, $\\lambda=0.1$/h: first failure at $5$ h, system failure at $15$ h on average, $P(\\text{gap}>10\\,\\text{h})=e^{-1}=0.368$. $n=5$: mean gaps $0.2,0.25,0.333,0.5,1$ and $E\\max=2.2833$.",
         used=[CH], related=["Order Statistics", "Memoryless Property", "Exponential Distribution", "Independence of Random Variables"]),
    dict(title="Multinomial Distribution", aliases=["multinomial random vector", "Mult_k(n,p)", "multinomial counts", "HW5 Problem 3"], scope=[T, EBY], by=BY,
         syl={T: f"{HW} Problem 3.", EBY: "rank, conditional laws, Poissonisation (mine, exactly checked)."},
         intuition="$n$ independent trials, each landing in one of $k$ boxes with probabilities $p_i$; $X_i$ counts the trials in box $i$. The binomial is the case $k=2$.",
         key="$P(X=x)=\\frac{n!}{x_1!\\cdots x_k!}\\prod p_i^{x_i}$ on $\\sum x_i=n$. $E X_i=np_i$, $\\mathrm{Var}X_i=np_i(1-p_i)$, $\\mathrm{Cov}(X_i,X_k)=-np_ip_k$. Marginals binomial; $X_1\\mid X_2=x_2\\sim\\mathrm{Bin}(n-x_2,\\frac{p_1}{1-p_2})$; independent $\\mathrm{Poisson}(\\mu p_i)$ counts conditioned on their sum $n$ are multinomial.",
         body="Fair die, 12 rolls: $\\mathrm{Var}=1.667$, $\\mathrm{Cov}=-0.333$, $P(\\text{every face twice})=0.003438$.",
         used=[CH, "PR01 Counting and the Axioms of Probability"], related=["Multinomial Covariance Matrix", "Multinomial Coefficient", "Binomial Distribution", "Indicator Random Variable", "Poisson Distribution"]),
    dict(title="Multinomial Covariance Matrix", aliases=["n(diag p - p p^T)", "covariance of multinomial counts", "singular covariance matrix"], scope=[T, EBY], by=BY,
         syl={T: f"{HW} Problem 3(b).", EBY: "rank and eigenvalues (mine)."},
         intuition="The counts must add to $n$, so a big count forces small ones: every off-diagonal entry is negative, and the all-ones direction has zero variance.",
         key="$\\Sigma=n\\big(\\mathrm{diag}(p)-pp^{\\mathsf T}\\big)$, from the indicator covariances $\\mathrm{Cov}(Y_{ij},Y_{kj})=-p_ip_k$ ($i\\ne k$), $p_i(1-p_i)$ ($i=k$), and independence across trials. $\\Sigma\\mathbf 1=0$: rank $k-1$. $\\mathrm{Corr}(X_i,X_k)=-\\sqrt{p_ip_k/((1-p_i)(1-p_k))}$.",
         body="$n=10$, $p=(0.2,0.3,0.5)$: $\\Sigma=\\begin{pmatrix}1.6&-0.6&-1.0\\\\-0.6&2.1&-1.5\\\\-1.0&-1.5&2.5\\end{pmatrix}$ (exact enumeration of 66 outcomes), eigenvalues $0,\\,2.319,\\,3.881$.",
         used=[CH, "PR07 Sums of Independent Variables Covariance and Correlation"], related=["Multinomial Distribution", "Covariance Matrix", "Covariance and Correlation", "Indicator Random Variable"]),
]

if __name__ == "__main__":
    write("08-Probability", "probability", ITEMS)
