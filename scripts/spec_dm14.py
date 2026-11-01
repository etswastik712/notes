"""Concept notes for DM14 (One-Parameter Subgroups and the Exponential Map).  .venv/bin/python -W ignore scripts/spec_dm14.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM14 One-Parameter Subgroups and the Exponential Map"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="One-Parameter Subgroup", aliases=["one-parameter subgroups", "Theorem 20.1", "homomorphism from R"], scope=[T, EB], by=BY,
         syl={T: f"slide DG25 via [[{MT}/2026-10-24-october-19-24|Oct 19–24 note]]; HW9 Q1–Q2.", EB: f"[[{LEE}#page=534|Lee Thm 20.1, p. 516]], [[{LEE}#page=536|Lee Prop. 20.3, p. 518]]."},
         intuition="A copy of the real line (or a circle, or a point) inside $G$: a path through $e$ along which the group law is just addition of times.",
         key="A Lie group homomorphism $\\gamma:\\mathbb R\\to G$. **Thm 20.1:** these are exactly the maximal integral curves from $e$ of left-invariant fields; $\\gamma_X'(0)=X_e$. The image is isomorphic to $\\mathbb R$, $S^1$ or $\\{e\\}$ (HW9 Q1). For a subgroup $H$: the one-parameter subgroups of $G$ with velocity in $T_eH$ (Prop 20.3).",
         body="$GL(n)$: $e^{tA}$. $T^2$: $t\\mapsto(at,bt)$ mod $\\mathbb Z^2$: circle if $a/b\\in\\mathbb Q$, dense line if irrational, point if $(0,0)$. $\\mathbb R^n$: $t\\mapsto tv$. In physics: the unitary evolution $e^{-iHt/\\hbar}$.",
         used=[CH], related=["Exponential Map", "Integral Curve", "Left-Invariant Vector Field", "Lie Group Homomorphism"]),
    dict(title="Exponential Map", aliases=["exp", "exponential of a Lie algebra", "exp: g to G", "Proposition 20.8", "normal coordinates"], scope=[T, EB], by=BY,
         syl={T: f"slide DG26 via [[{MT}/2026-10-24-october-19-24|Oct 19–24 note]]; HW9 Q3–Q5.", EB: f"[[{LEE}#page=537|Lee Prop. 20.8, p. 519]], [[{LEE}#page=539|Lee Prop. 20.9, p. 521]]."},
         intuition="Follow the infinitesimal symmetry $X$ for one unit of time: the dictionary from the Lie algebra to the group.",
         key="$\\exp X=\\gamma_X(1)$; $\\exp sX=\\gamma_X(s)$. Smooth; $\\exp(s+t)X=\\exp sX\\exp tX$; $(\\exp X)^{-1}=\\exp(-X)$; $d\\exp_0=\\mathrm{id}$ so $\\exp$ is a **local diffeomorphism** near $0$; natural: $\\Phi\\circ\\exp=\\exp\\circ\\Phi_*$; flow of $\\tilde X$ is $R_{\\exp tX}$. $\\mathrm{Lie}(H)=\\{X:\\exp tX\\in H\\ \\forall t\\}$.",
         body="**Not** additive ($\\exp(X+Y)=\\exp X\\exp Y$ for all $X,Y$ iff $G_0$ abelian), not injective ($\\mathbb R\\to S^1$), not onto ($\\mathfrak{sl}(2,\\mathbb R)\\to SL(2,\\mathbb R)$: $\\operatorname{tr}e^A\\ge-2$). $[X,Y]=0\\iff$ exps commute. $\\exp X\\exp Y$ as coordinates (HW9 Q3).",
         used=[CH, "DM15 Closed Subgroups and the Lie Correspondence"], related=["One-Parameter Subgroup", "Matrix Exponential", "Lie Algebra of a Lie Group", "Trotter Product Formula"]),
    dict(title="Matrix Exponential", aliases=["e^A", "exp of a matrix", "Rodrigues formula", "Proposition 20.2"], scope=[T, EB], by=BY,
         syl={T: f"slide DG26 via [[{MT}/2026-10-24-october-19-24|Oct 19–24 note]].", EB: f"[[{LEE}#page=535|Lee Prop. 20.2, p. 517]]."},
         intuition="The power series of $e^x$ with a matrix plugged in; it solves $\\dot X=XA$.",
         key="$e^A=\\sum_kA^k/k!$ converges (M-test, $\\|A^k/k!\\|\\le\\|A\\|^k/k!$) to an invertible matrix; $t\\mapsto e^{tA}$ is the one-parameter subgroup of $GL(n,\\mathbb R)$ with velocity $A$; $\\exp A=e^A$ on $GL(n)$ and its subgroups; $\\det e^A=e^{\\operatorname{tr}A}$.",
         body="$e^{tJ}=R(t)$ for $J=\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$; nilpotent $A$: $e^{tA}=I+tA$. $SO(3)$: $e^{\\hat\\omega}=I+\\tfrac{\\sin|\\omega|}{|\\omega|}\\hat\\omega+\\tfrac{1-\\cos|\\omega|}{|\\omega|^2}\\hat\\omega^2$ (checked); $SU(2)$: $\\cos\\tfrac{|\\omega|}2I-i\\sin\\tfrac{|\\omega|}2\\hat\\omega\\!\\cdot\\!\\sigma$. Linear ODE solutions in [[PA14 ODE Existence Uniqueness and Smooth Dependence]].",
         used=[CH], related=["Exponential Map", "One-Parameter Subgroup", "Matrix Lie Algebras", "General Linear Group"]),
    dict(title="Trotter Product Formula", aliases=["Lie product formula", "Corollary 20.11", "Proposition 20.10", "sum from products"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=540|Lee Prop. 20.10, p. 522]], [[{LEE}#page=541|Lee Cor. 20.11, p. 523]]."},
         intuition="Alternating tiny steps along $X$ and $Y$ gives, in the limit, a step along $X+Y$.",
         key="$\\exp tX\\exp tY=\\exp\\big(t(X+Y)+t^2Z(t)\\big)$ with $Z$ smooth, hence $\\lim_n\\big(\\exp\\tfrac tnX\\exp\\tfrac tnY\\big)^n=\\exp t(X+Y)$. Proof: $\\varphi=\\exp^{-1}(\\exp tX\\exp tY)$ has $\\varphi'(0)=X+Y$ ($dm_{(e,e)}(X,Y)=X+Y$).",
         body="Numerically the error for random $3\\times3$ $X,Y$ is $2.46\\times10^{-1},\\dots,2.46\\times10^{-4}$ for $n=10,\\dots,10^4$ (rate $1/n$). It makes $\\{X:\\exp tX\\in H\\}$ a vector space for closed $H$: the Closed Subgroup Theorem ([[DM15 Closed Subgroups and the Lie Correspondence]]). Used in physics for operator splitting.",
         used=[CH, "DM15 Closed Subgroups and the Lie Correspondence"], related=["Exponential Map", "Lie Subgroup", "Matrix Exponential"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
