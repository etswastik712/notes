"""Concept notes for PA13 (The Derivative and the Inverse Function Theorem).  .venv/bin/python -W ignore scripts/spec_pa13.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "PA13 The Derivative and the Inverse Function Theorem"
EB = ["extra-book"]

ITEMS = [
    dict(title="Total Derivative", aliases=["derivative", "Jacobian", "differential of a map between Euclidean spaces", "Frechet derivative"], scope=EB,
         syl=f"[[{LEE}#page=660|Lee App. C, p. 642]]; Spivak Ch. 2.",
         intuition="The best linear approximation of $F$ near $a$: $F(a+h)\\approx F(a)+DF(a)h$, with error smaller than linear in $|h|$.",
         key="$F:U\\to\\mathbb R^m$ is differentiable at $a$ if some linear $DF(a)$ has $|F(a+h)-F(a)-DF(a)h|/|h|\\to0$. Its matrix is the Jacobian $(\\partial F^i/\\partial x^j)$. $C^1$ (continuous partials) implies differentiable.",
         body="Matrix examples: $d(\\det)_X(B)=\\det X\\operatorname{tr}(X^{-1}B)$ (so $d(\\det)_I=\\operatorname{tr}$), $d(\\mathrm{inv})_X(B)=-X^{-1}BX^{-1}$, $d(AA^T)_X(B)=BX^T+XB^T$. Manifold version: [[Differential of a Smooth Map]].",
         used=[CH], related=["Chain Rule", "Inverse Function Theorem", "Local Diffeomorphism"]),
    dict(title="Chain Rule", aliases=["chain rule for total derivatives"], scope=EB,
         syl=f"[[{LEE}#page=661|Lee Prop. C.3, p. 643]].",
         intuition="Linear approximations compose: the derivative of a composition is the composition of the derivatives.",
         key="$D(G\\circ F)(a)=DG(F(a))\\circ DF(a)$. For a diffeomorphism, $D(F^{-1})(F(a))=DF(a)^{-1}$.",
         body="It makes the differential on manifolds functorial: $d(G\\circ F)_p=dG_{F(p)}\\circ dF_p$ ([[Differential of a Smooth Map]]), and shows transition maps between charts have invertible Jacobians.",
         used=[CH], related=["Total Derivative", "Local Diffeomorphism"]),
    dict(title="Contraction Mapping Principle", aliases=["Banach fixed point theorem", "contraction lemma", "contraction"], scope=EB,
         syl=f"[[{LEE}#page=675|Lee Lemma C.35, p. 657]].",
         intuition="A map that shrinks all distances by a fixed factor $L<1$ pulls every point toward one fixed point, as a photocopier reducing a photo of itself.",
         key="If $X$ is a nonempty complete metric space and $d(Tx,Ty)\\le L\\,d(x,y)$ with $L<1$, then $T$ has a unique fixed point $x^*$, and $d(x_n,x^*)\\le L^nd(x_1,x_0)/(1-L)$ for $x_{n+1}=Tx_n$.",
         body="$\\cos x=x$: $L=\\sin1=0.841$, 67 steps to $10^{-12}$ (a-priori bound 166). Engine of the [[Inverse Function Theorem]] and of Picard's existence theorem for ODEs ([[PA14 ODE Existence Uniqueness and Smooth Dependence]]). Completeness is essential: $x\\mapsto x/2$ on $(0,1]$ has no fixed point.",
         used=[CH], related=["Inverse Function Theorem", "Cauchy Sequence"]),
    dict(title="Inverse Function Theorem", aliases=["IFT", "inverse function theorem"], scope=EB,
         syl=f"[[{LEE}#page=675|Lee Thm C.34, p. 657]]; Spivak Thm 2-11.",
         intuition="If the linear approximation of a map is invertible at a point, the map itself is invertible near that point; the linear solution corrected by a convergent (contracting) iteration.",
         key="$F:U\\subseteq\\mathbb R^n\\to\\mathbb R^n$ smooth with $DF(a)$ invertible $\\Rightarrow$ $F$ restricts to a diffeomorphism from a neighbourhood of $a$ onto a neighbourhood of $F(a)$, and $D(F^{-1})=(DF)^{-1}\\circ F^{-1}$.",
         body="Local, not global ($e^x(\\cos y,\\sin y)$ is a local diffeomorphism that is not injective); sufficient, not necessary ($x\\mapsto x^3$). Gives charts-from-submersions and the [[Implicit Function Theorem]], [[Constant Rank Theorem (Euclidean)]]; manifold version in [[DM04 The Tangent Bundle and the Rank Theorem]].",
         used=[CH, "DM04 The Tangent Bundle and the Rank Theorem"], related=["Contraction Mapping Principle", "Local Diffeomorphism", "Implicit Function Theorem"]),
    dict(title="Implicit Function Theorem", aliases=["implicit function theorem", "regular level set as a graph"], scope=EB,
         syl=f"[[{LEE}#page=679|Lee Thm C.40, p. 661]]; Spivak Thm 2-12.",
         intuition="Where an equation $\\Phi(x,y)=c$ can be solved for $y$ to first order, it can be solved exactly near the point, and the solution $y=g(x)$ is smooth.",
         key="$\\Phi:U\\subseteq\\mathbb R^n\\times\\mathbb R^k\\to\\mathbb R^k$ smooth, $\\Phi(a,b)=c$, $\\partial_y\\Phi(a,b)$ invertible $\\Rightarrow$ near $(a,b)$ the level set is the graph of a smooth $g$, with $g'=-(\\partial_y\\Phi)^{-1}\\partial_x\\Phi$.",
         body="The circle $x^2+y^2=1$ is the graph $y=\\sqrt{1-x^2}$ near $(0,1)$ ($g'(0.6)=-0.75$) but not near $(1,0)$ where $\\partial_y\\Phi=0$. Regular level sets are submanifolds ([[DM06 Submanifolds]]).",
         used=[CH, "DM06 Submanifolds"], related=["Inverse Function Theorem", "Constant Rank Theorem (Euclidean)"]),
    dict(title="Constant Rank Theorem (Euclidean)", aliases=["rank theorem in R^n", "normal form of constant rank maps"], scope=EB,
         syl=f"Lee Thm 4.12 ([[{LEE}#page=99|p. 81]]), specialised to $\\mathbb R^m$; Spivak Problem 2-32.",
         intuition="A map whose derivative has the same rank $r$ everywhere is, after nonlinear changes of coordinates in source and target, the plain 'keep $r$ coordinates, zero the rest' map.",
         key="$F:U\\subseteq\\mathbb R^m\\to\\mathbb R^n$ smooth of constant rank $r$ $\\Rightarrow$ local diffeomorphisms $\\varphi,\\psi$ with $\\psi\\circ F\\circ\\varphi^{-1}(x)=(x^1,\\dots,x^r,0,\\dots,0)$.",
         body="Special cases: a submersion is locally a projection, an immersion locally an inclusion. Fails if the rank jumps ($x\\mapsto x^2$). Manifold form: [[DM04 The Tangent Bundle and the Rank Theorem]].",
         used=[CH, "DM04 The Tangent Bundle and the Rank Theorem"], related=["Inverse Function Theorem", "Local Diffeomorphism"]),
    dict(title="Local Diffeomorphism", aliases=["local diffeomorphism", "diffeomorphism"], scope=EB,
         syl=f"[[{LEE}#page=678|Lee Cor. C.36, p. 660]].",
         intuition="A map that looks like a smooth, smoothly invertible change of coordinates around every point, without being globally one-to-one.",
         key="$F$ is a **diffeomorphism** if it is a smooth bijection with smooth inverse; a **local diffeomorphism** if every point has a neighbourhood on which $F$ is a diffeomorphism onto an open set. By the [[Inverse Function Theorem]], $F$ is a local diffeomorphism iff $DF$ is invertible everywhere.",
         body="$F(x,y)=(e^x\\cos y,e^x\\sin y)$ is one but not injective (a covering map); $x\\mapsto x^3$ is a smooth bijection that is not a diffeomorphism.",
         used=[CH], related=["Inverse Function Theorem", "Chain Rule", "Total Derivative"]),
]

if __name__ == "__main__":
    write("11-Proofs-Analysis-Topology", "analysis", ITEMS)
