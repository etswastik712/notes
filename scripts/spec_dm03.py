"""Concept notes for DM03 (Tangent Vectors and the Differential).  .venv/bin/python -W ignore scripts/spec_dm03.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM03 Tangent Vectors and the Differential"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Tangent Vector", aliases=["derivation at a point", "tangent vector at p", "derivation"], scope=[T, EB], by=BY,
         syl={T: f"[[{MT}/2026-08-14-hw2|HW2]] Q1, [[{MT}/2026-09-03-test-i|Test 1]] Q1 (locality via bump functions); week 2 (slides unreadable).", EB: f"[[{LEE}#page=71|Lee Lemma 3.1, Prop. 3.2, pp. 53–54]]; Tu §2."},
         intuition="A rule for differentiating functions at a point: 'rate of change of $f$ in a direction'. Linearity and the product rule are all it must obey.",
         key="A **derivation at $p$** is a linear $v:C^\\infty(M)\\to\\mathbb R$ with $v(fg)=f(p)v(g)+g(p)v(f)$. Constants are killed; $v$ is **local** ($f=g$ near $p\\Rightarrow vf=vg$, by a bump function).",
         body="On $\\mathbb R^n$: $v=\\sum v(x^i)\\,\\partial/\\partial x^i|_a$ (Hadamard's lemma). Equivalent definitions: velocity of curves, or $n$-tuples with a transformation law ([[Velocity of a Curve]], [[Transformation Law for Tangent Vectors]]).",
         used=[CH], related=["Tangent Space", "Coordinate Basis", "Bump Function"]),
    dict(title="Tangent Space", aliases=["T_pM", "tangent space at a point"], scope=[T], by=BY,
         syl={T: f"week 2 ({MT}/2026-08-14-august-10-14); HW2; Test 1."},
         intuition="All the directions in which one can move from $p$, collected in a vector space the same size as the manifold.",
         key="$T_pM$ = the real vector space of derivations at $p$; $\\dim T_pM=\\dim M=n$ (a chart gives $d\\varphi_p:T_pM\\cong T_{\\varphi(p)}\\mathbb R^n$). $T_pU=T_pM$ for $U$ open; $T_aV\\cong V$ for a vector space; $T_{(p,q)}(M\\times N)\\cong T_pM\\oplus T_qN$.",
         body="For a sphere $T_pS^2\\cong p^\\perp\\subset\\mathbb R^3$. All tangent spaces assemble into the tangent bundle ([[DM04 The Tangent Bundle and the Rank Theorem]]). Tangent space of a Lie group at the identity is its Lie algebra ([[DM11 The Lie Algebra of a Lie Group]]).",
         used=[CH], related=["Tangent Vector", "Differential of a Smooth Map", "Tangent Space of a Product"]),
    dict(title="Differential of a Smooth Map", aliases=["pushforward", "dF_p", "tangent map", "derivative of a smooth map"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-14-hw2|HW2]] Q4, [[{MT}/2026-08-20-hw3|HW3]] Q1; Test 1 Q2."},
         intuition="How a map stretches and rotates directions at a point: the best linear approximation of $F$ near $p$, as a map between tangent spaces.",
         key="$dF_p:T_pM\\to T_{F(p)}N$, $dF_p(v)f=v(f\\circ F)$. Linear; chain rule $d(G\\circ F)=dG\\circ dF$; $d\\,\\mathrm{id}=\\mathrm{id}$; diffeomorphism $\\Rightarrow$ isomorphism. In coordinate bases its matrix is the Jacobian of $\\psi\\circ F\\circ\\varphi^{-1}$.",
         body="Computed along curves: $dF_p(v)=(F\\circ\\gamma)'(0)$ when $\\gamma'(0)=v$. Example: rotation by $60^\\circ$ about the $z$-axis in the graph chart is a rotation matrix; $dF\\alpha'(\\tfrac14)=(-1.232,1.866)$. Extended to $dF:TM\\to TN$ in [[DM04 The Tangent Bundle and the Rank Theorem]]. Euclidean case: [[Total Derivative]].",
         used=[CH], related=["Tangent Space", "Coordinate Basis", "Velocity of a Curve", "Total Derivative"]),
    dict(title="Coordinate Basis", aliases=["coordinate vectors", "partial derivative vectors", "d/dx^i"], scope=[T], by=BY,
         syl={T: f"week 2 post: tangent spaces 'calculated in local coordinates'; HW2 Q3; HW3 Q1."},
         intuition="The $n$ rules 'differentiate along the $i$-th coordinate line', one for each coordinate of the chart.",
         key="For a chart $(U,\\varphi=(x^i))$: $\\dfrac{\\partial}{\\partial x^i}\\Big|_pf=\\dfrac{\\partial(f\\circ\\varphi^{-1})}{\\partial x^i}(\\varphi(p))$. They form a basis of $T_pM$; the components of $v$ are $v^i=v(x^i)$.",
         body="A different chart gives a different basis, related by the Jacobian of the transition ([[Transformation Law for Tangent Vectors]]). Coordinate vector fields $\\partial/\\partial x^i$ commute: $[\\partial_i,\\partial_j]=0$ ([[DM10 Vector Fields and Lie Brackets]]).",
         used=[CH], related=["Tangent Vector", "Differential of a Smooth Map", "Transformation Law for Tangent Vectors"]),
    dict(title="Transformation Law for Tangent Vectors", aliases=["change of coordinates for tangent vectors", "change of basis between charts", "contravariant transformation"], scope=[T], by=BY,
         syl={T: f"week 2 post ('how these change when the coordinates change'); [[{MT}/2026-08-14-hw2|HW2]] Q3; Test 1 Q4; [[{LEE}#page=79|Lee Prop. 3.15, p. 61]]."},
         intuition="The same arrow is described by different numbers in different coordinate systems; the Jacobian of the coordinate change converts them.",
         key="If $\\tilde x=\\tilde\\varphi\\circ\\varphi^{-1}(x)$ is the transition, components transform by $\\tilde v^j=\\sum_i\\dfrac{\\partial\\tilde x^j}{\\partial x^i}v^i$ and basis vectors by $\\partial/\\partial x^i=\\sum_j\\dfrac{\\partial\\tilde x^j}{\\partial x^i}\\partial/\\partial\\tilde x^j$.",
         body="HW2 Q3: $X=(1,2)$ becomes $(-\\tfrac12-\\sqrt3,1-\\tfrac{\\sqrt3}2)=(-2.2320,0.1340)$ via the Jacobian of $w\\mapsto w/|w|^2$. Test 1 Q4: $(1,2)\\mapsto(2,4)$ via $2I$.",
         used=[CH], related=["Coordinate Basis", "Transition Map", "Stereographic Projection"]),
    dict(title="Velocity of a Curve", aliases=["velocity vector", "tangent vector to a curve", "gamma'(t)"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-14-hw2|HW2]] Q5; [[{MT}/2026-08-20-hw3|HW3]] Q1(a),(c); [[{LEE}#page=88|Lee Props. 3.23–3.24, Cor. 3.25, p. 70]]."},
         intuition="The instantaneous direction of motion along a path, as a rule for differentiating functions along the path.",
         key="For a smooth curve $\\gamma:J\\to M$: $\\gamma'(t_0)=d\\gamma_{t_0}(d/dt)$, i.e. $\\gamma'(t_0)f=(f\\circ\\gamma)'(t_0)$; in a chart its components are $(x^i\\circ\\gamma)'(t_0)$. Every $v\\in T_pM$ is $\\gamma'(0)$ for some curve; $dF_p(\\gamma'(0))=(F\\circ\\gamma)'(0)$.",
         body="HW3 Q1: $\\alpha(t)=(t,2t,\\sqrt{1-5t^2})$: $\\alpha'(\\tfrac14)=(1,2)$ in the $\\varphi_3^+$ basis and $(1,-5/\\sqrt{11})$ in the $\\varphi_2^+$ basis. Velocities of curves on $S^2\\subset\\mathbb R^3$ are orthogonal to the position. Integral curves of vector fields ([[Integral Curve]]) are curves whose velocity is prescribed.",
         used=[CH], related=["Tangent Vector", "Differential of a Smooth Map", "Integral Curve"]),
    dict(title="Tangent Space of a Product", aliases=["T(M x N)", "tangent space of product manifold"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-14-hw2|HW2]] Q2(b); [[{LEE}#page=77|Lee Prop. 3.14, p. 59]]."},
         intuition="A direction in $M\\times N$ is a direction in $M$ together with a direction in $N$.",
         key="$\\alpha:T_{(p,q)}(M\\times N)\\to T_pM\\oplus T_qN$, $\\alpha(v)=(d(\\pi_1)v,d(\\pi_2)v)$, is an isomorphism (coordinate vectors go to coordinate vectors in the product chart).",
         body="Used for the Lie group multiplication $m:G\\times G\\to G$: $dm_{(e,e)}(X,Y)=X+Y$ (HW4 Q6, [[DM08 Lie Groups]]).",
         used=[CH], related=["Product Manifold", "Tangent Space", "Differential of a Smooth Map"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
