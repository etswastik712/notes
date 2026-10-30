"""Concept notes for PA14 (ODE: existence, uniqueness, smooth dependence).  .venv/bin/python -W ignore scripts/spec_pa14.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "PA14 ODE Existence Uniqueness and Smooth Dependence"
EB = ["extra-book"]

ITEMS = [
    dict(title="Initial Value Problem", aliases=["IVP", "Cauchy problem", "autonomous system", "state-space reduction"], scope=EB,
         syl=f"[[{LEE}#page=681|Lee App. D, p. 663]]; Teschl §1.1.",
         intuition="Follow the arrows of a vector field from a given starting point: the solution is the path that is always tangent to the field.",
         key="$x'=V(x)$, $x(0)=p$, with $V:U\\to\\mathbb R^n$ a vector field. A solution is a differentiable curve $x:J\\to U$ with $x'(t)=V(x(t))$; equivalently $x(t)=p+\\int_0^tV(x(s))\\,ds$.",
         body="Higher-order and time-dependent equations reduce to this form by adding variables: $\\theta''=-\\sin\\theta\\ \\Rightarrow\\ (\\theta,\\omega)'=(\\omega,-\\sin\\theta)$; $x'=V(t,x)\\ \\Rightarrow\\ (s,x)'=(1,V(s,x))$. Solutions are the **integral curves** of $V$ ([[DM12 Integral Curves, Flows and Flowouts]]).",
         used=[CH], related=["Lipschitz Condition", "Picard Iteration", "Maximal Solution of an ODE"]),
    dict(title="Lipschitz Condition", aliases=["Lipschitz", "locally Lipschitz", "Lipschitz continuous"], scope=EB,
         syl=f"[[{LEE}#page=673|Lee Prop. C.29, p. 655]].",
         intuition="A bound on how fast the output can change relative to the input: no infinitely steep points.",
         key="$V$ is **$L$-Lipschitz** on $K$ if $|V(x)-V(y)|\\le L|x-y|$ for $x,y\\in K$; **locally Lipschitz** if every point has a neighbourhood on which it is Lipschitz. $C^1$ maps are locally Lipschitz.",
         body="It is the hypothesis behind uniqueness: $x'=\\sqrt{|x|}$ (not Lipschitz at $0$) has non-unique solutions from $x(0)=0$. $\\|DV\\|\\le L$ on a convex set implies $L$-Lipschitz ([[Total Derivative]]).",
         used=[CH], related=["Picard Iteration", "Gronwall Inequality", "Contraction Mapping Principle"]),
    dict(title="Picard Iteration", aliases=["Picard-Lindelof theorem", "Picard–Lindelöf", "Picard operator", "local existence and uniqueness"], scope=EB,
         syl=f"[[{LEE}#page=683|Lee Thm D.3, D.4, pp. 665–667]].",
         intuition="Guess the solution is constant, then repeatedly correct it by integrating the field along the current guess; the corrections shrink geometrically.",
         key="For $V$ Lipschitz and bounded on $\\overline B_r(p)$ ($|V|\\le M$, constant $L$), the operator $(Px)(t)=p+\\int_0^tV(x(s))ds$ is a contraction of $C([-\\varepsilon,\\varepsilon],\\overline B_r(p))$ for $\\varepsilon<\\min(r/M,1/L)$; its unique fixed point is the unique solution.",
         body="For $x'=x$, $x(0)=1$ the iterates are the Taylor polynomials of $e^t$ (at $t=1$: $1,2,2.5,2.667,2.708,\\dots$). Proof engine: [[Contraction Mapping Principle]]. Uniqueness among all solutions: [[Gronwall Inequality]].",
         used=[CH], related=["Contraction Mapping Principle", "Gronwall Inequality", "Initial Value Problem"]),
    dict(title="Gronwall Inequality", aliases=["Gronwall's inequality", "Grönwall"], scope=EB,
         syl="Teschl §2.2; used in [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=681|Lee App. D]].",
         intuition="A quantity that grows at most in proportion to its own accumulated size can grow at most exponentially.",
         key="If $u\\ge0$ is continuous and $u(t)\\le C+L\\int_0^tu$ on $[0,T]$, then $u(t)\\le Ce^{Lt}$.",
         body="Consequences: uniqueness of solutions ($C=0\\Rightarrow u\\equiv0$) and continuous dependence $|x(t)-y(t)|\\le|p-q|e^{L|t|}$. Proof: $w=C+L\\int u$ has $w'\\le Lw$.",
         used=[CH], related=["Picard Iteration", "Smooth Dependence on Initial Conditions", "Lipschitz Condition"]),
    dict(title="Maximal Solution of an ODE", aliases=["maximal integral curve", "escape lemma", "finite escape time", "blow-up"], scope=EB,
         syl=f"[[{LEE}#page=235|Lee Lemma 9.19 (Escape Lemma), p. 217]]; Lee Thm D.6.",
         intuition="Extend the solution as far as it will go; if it stops in finite time it must have run off to infinity or to the edge of the domain.",
         key="For locally Lipschitz $V$ there is a unique maximal solution $\\gamma_p:(a_p,b_p)\\to U$ through $p$; any other solution is a restriction. **Escape lemma:** if $b_p<\\infty$, $\\gamma_p(t)$ leaves every compact set as $t\\to b_p$.",
         body="$x'=x^2$, $x(0)=x_0>0$: $x=x_0/(1-x_0t)$, $b=1/x_0$ (at $t=0.99/x_0$, $x=100x_0$). Compactly supported fields are complete. Manifold version: [[Integral Curve]] and [[Complete Vector Field]] in [[DM12 Integral Curves, Flows and Flowouts]].",
         used=[CH], related=["Initial Value Problem", "Smooth Dependence on Initial Conditions"]),
    dict(title="Smooth Dependence on Initial Conditions", aliases=["flow of an ODE", "smooth dependence", "ODE flow"], scope=EB,
         syl=f"[[{LEE}#page=685|Lee Thm D.5, p. 667]]; Hirsch–Smale Ch. 8.",
         intuition="Nearby starting points give nearby solutions, and the dependence is as smooth as the field itself.",
         key="For smooth $V$, the domain $\\mathcal D=\\{(t,p):a_p<t<b_p\\}$ is open in $\\mathbb R\\times U$ and the flow $\\theta(t,p)=\\gamma_p(t)$ is smooth on it. Group law: $\\theta_s\\circ\\theta_t=\\theta_{s+t}$ where defined; each $\\theta_t$ is a diffeomorphism $U_t\\to U_{-t}$.",
         body="Flow of $y\\partial_x+\\partial_y$: $(a,b)\\mapsto(a+bt+t^2/2,\\,b+t)$; of the rotation field: rotation by $t$. Manifold version: Fundamental Theorem on Flows, [[Flow of a Vector Field]].",
         used=[CH], related=["Variational Equation", "Gronwall Inequality", "Maximal Solution of an ODE"]),
    dict(title="Variational Equation", aliases=["linearised equation", "derivative of the flow", "first variation"], scope=EB,
         syl="Teschl §2.6; Hirsch–Smale Ch. 8.",
         intuition="How a small change of the starting point spreads along the flow is itself governed by a linear equation built from the derivative of the field.",
         key="$Y(t)=D_p\\theta(t,p)$ solves $Y'=DV(\\theta(t,p))\\,Y$, $Y(0)=I$.",
         body="For $x'=x^2$: $Y'=2xY$ gives $\\partial_{x_0}\\theta=1/(1-x_0t)^2$ ($=4$ at $x_0=1$, $t=\\tfrac12$, verified numerically). At an equilibrium $p$ with $DV(p)=A$, $Y=e^{tA}$: linear stability; compare the matrix exponential in [[DM14 One-Parameter Subgroups and the Exponential Map]].",
         used=[CH], related=["Smooth Dependence on Initial Conditions", "Total Derivative"]),
]

if __name__ == "__main__":
    write("11-Proofs-Analysis-Topology", "analysis", ITEMS)
