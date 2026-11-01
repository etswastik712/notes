"""Concept notes for DM10 (Vector Fields and Lie Brackets).  .venv/bin/python -W ignore scripts/spec_dm10.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM10 Vector Fields and Lie Brackets"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Vector Field", aliases=["smooth vector field", "vector fields", "derivation of C^infty(M)", "derivation of the algebra of smooth functions", "X(M)", "rough vector field"], scope=[T, EB], by=BY,
         syl={T: f"slides DG8–DG10 via [[{MT}/2026-08-20-august-17-21|Aug 17–21]] and [[{MT}/2026-08-27-august-24-28|Aug 24–28]] notes; HW3 Q3, HW4 Q2.", EB: f"[[{LEE}#page=198|Lee Prop. 8.14, p. 180]], [[{LEE}#page=199|Lee Prop. 8.15, p. 181]]."},
         intuition="An arrow attached to every point of the manifold, varying smoothly: equivalently, a rule $f\\mapsto Xf$ that differentiates functions.",
         key="A smooth section $X:M\\to TM$ of $\\pi:TM\\to M$; in a chart $X=\\sum X^i\\partial/\\partial x^i$ with $X^i$ smooth. A rough field is smooth iff $Xf\\in C^\\infty(M)$ for all $f\\in C^\\infty(M)$ (Prop 8.14). **Vector fields = derivations of $C^\\infty(M)$** ($\\mathbb R$-linear, $D(fg)=fDg+gDf$; Prop 8.15). $\\mathfrak X(M)$ is a $C^\\infty(M)$-module and, with the bracket, a Lie algebra.",
         body="Examples: coordinate fields, Euler field $\\sum x^i\\partial_i$, rotation fields $x\\partial_y-y\\partial_x$, $\\partial_\\theta$ on $S^1$ and $T^n$; a vector $v\\in T_pM$ extends to a global field (bump function, HW4 Q2). $|x|\\partial_x$ is not smooth. The Hairy Ball Theorem forbids a non-vanishing field on $S^{2k}$ ([[Hairy Ball Theorem]]); Lie groups have global frames ([[DM11 The Lie Algebra of a Lie Group]]).",
         used=[CH, "DM04 The Tangent Bundle and the Rank Theorem"], related=["Tangent Bundle", "Local Frame", "Lie Bracket of Vector Fields", "F-Related Vector Fields", "Tangent Vector"]),
    dict(title="F-Related Vector Fields", aliases=["F-related", "pushforward of a vector field", "F_*X", "related vector fields"], scope=[T, EB], by=BY,
         syl={T: f"slide DG10 (Prop 8.19) via [[{MT}/2026-08-27-august-24-28|Aug 24–28 note]]; HW4 Q3.", EB: f"[[{LEE}#page=200|Lee Prop. 8.16, p. 182]], [[{LEE}#page=201|Lee Prop. 8.19, p. 183]]."},
         intuition="Two fields that the map $F$ carries into each other: following $X$ in $M$ and then applying $F$ equals following $Y$ in $N$.",
         key="$X\\in\\mathfrak X(M)$ and $Y\\in\\mathfrak X(N)$ are $F$-related if $dF_p(X_p)=Y_{F(p)}$ for all $p$, iff $X(f\\circ F)=(Yf)\\circ F$ for all $f$ (Prop 8.16). If $F$ is a **diffeomorphism**, $F_*X=dF\\circ X\\circ F^{-1}$ is the unique related field (Prop 8.19). Brackets of related pairs are related ([[Naturality of the Lie Bracket]]).",
         body="HW4 Q3: $F(x,y)=(xy,y/x)$ on the open quadrant sends $x\\partial_x+y\\partial_y$ to $2u\\partial_u$. $\\partial_t$ on $\\mathbb R$ is related to $-y\\partial_x+x\\partial_y$ under $t\\mapsto(\\cos t,\\sin t)$. In general no related field exists for a non-injective or non-surjective $F$; for a Lie group homomorphism, left-invariant fields are related ([[DM11 The Lie Algebra of a Lie Group]]).",
         used=[CH], related=["Vector Field", "Differential of a Smooth Map", "Diffeomorphism", "Naturality of the Lie Bracket"]),
    dict(title="Lie Bracket of Vector Fields", aliases=["Lie bracket", "commutator of vector fields", "[X,Y]", "bracket of vector fields"], scope=[T, EB], by=BY,
         syl={T: f"slides DG16–DG17 via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]]; HW6 Q4–Q5.", EB: f"[[{LEE}#page=204|Lee Lemma 8.25, Prop. 8.26, p. 186]], [[{LEE}#page=205|Lee Prop. 8.28, p. 187]]."},
         intuition="The part of the second derivatives $XY$ and $YX$ that does not cancel: the first-order measure of how far the flows of $X$ and $Y$ are from commuting.",
         key="$[X,Y]f=X(Yf)-Y(Xf)$ is again a vector field (the second-order terms cancel: Leibniz rule, HW6 Q4). Coordinates: $[X,Y]=(XY^j-YX^j)\\partial_j$; $[\\partial_i,\\partial_j]=0$. Properties: bilinear, antisymmetric, Jacobi, $[fX,gY]=fg[X,Y]+f(Xg)Y-g(Yf)X$.",
         body="HW6 Q5: $[x\\partial_y-y\\partial_x,\\,y\\partial_z-z\\partial_y]=x\\partial_z-z\\partial_x$; $[\\partial_x,x\\partial_y]=\\partial_y$; $[x\\partial_x,\\partial_x]=-\\partial_x$; $[r\\partial_r,\\partial_\\theta]=0$. The rotation fields satisfy $[L_x,L_y]=-L_z$. The flow quadrilateral closes up to $\\varepsilon^2[X,Y]$ ([[DM13 Lie Derivatives and Commuting Vector Fields]]). Quantum-mechanical analogue: $[\\hat x,\\hat p]=i\\hbar$.",
         used=[CH, "DM11 The Lie Algebra of a Lie Group"], related=["Jacobi Identity", "Naturality of the Lie Bracket", "Vector Field", "Lie Group"]),
    dict(title="Jacobi Identity", aliases=["Jacobi", "Lie algebra axioms"], scope=[T], by=BY,
         syl={T: f"slide DG17 via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]]."},
         intuition="The consistency law of a commutator: it says $\\operatorname{ad}_X=[X,\\cdot]$ is a derivation of the bracket.",
         key="$[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$. Together with bilinearity and antisymmetry it defines a **Lie algebra**. For vector fields it is verified by expanding the twelve terms $XYZ,XZY,\\dots$ which cancel in pairs; for matrices $[A,B]=AB-BA$ it is the same computation.",
         body="Examples: $\\mathfrak X(M)$ with the Lie bracket, $\\mathfrak{gl}(n,\\mathbb R)$ with the matrix commutator, $\\mathbb R^3$ with the cross product. Checked exactly on three fields of $\\mathbb R^3$ with polynomial and trigonometric components. The cross-product case is [[DM11 The Lie Algebra of a Lie Group]].",
         used=[CH, "DM11 The Lie Algebra of a Lie Group"], related=["Lie Bracket of Vector Fields", "Lie Group"]),
    dict(title="Naturality of the Lie Bracket", aliases=["Proposition 8.30", "pushforward of brackets", "brackets and diffeomorphisms"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=206|Lee Prop. 8.30, p. 188]], [[{LEE}#page=207|Lee Cor. 8.31, p. 189]]."},
         intuition="The bracket is defined by derivatives alone, so any smooth change of variables carries brackets to brackets.",
         key="If $X_i$ is $F$-related to $Y_i$ ($i=1,2$) then $[X_1,X_2]$ is $F$-related to $[Y_1,Y_2]$ (Prop 8.30). For a diffeomorphism: $F_*[X_1,X_2]=[F_*X_1,F_*X_2]$ (Cor 8.31). For an immersed submanifold: brackets of fields tangent to $S$ are tangent to $S$ (Cor 8.32).",
         body="Checked for $F(x,y)=(xy,y/x)$, $X_1=x\\partial_x+y\\partial_y$, $X_2=y\\partial_x+x^2\\partial_y$ ($[X_1,X_2]=x^2\\partial_y$ pushes to $((u/v)^{3/2},(u/v)^{1/2})$ on both sides). It is the reason left-invariant fields are closed under brackets and why $F_*:\\mathrm{Lie}(G)\\to\\mathrm{Lie}(H)$ is a Lie algebra homomorphism ([[DM11 The Lie Algebra of a Lie Group]]); the Frobenius-necessity half is in [[DM15 Closed Subgroups and the Lie Correspondence]].",
         used=[CH, "DM11 The Lie Algebra of a Lie Group"], related=["F-Related Vector Fields", "Lie Bracket of Vector Fields", "Lie Group Homomorphism"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
