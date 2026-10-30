"""Concept notes for DM07 (Sard, Whitney and Transversality).  .venv/bin/python -W ignore scripts/spec_dm07.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM07 Sard Whitney and Transversality"
EB = ["extra-book"]

ITEMS = [
    dict(title="Set of Measure Zero", aliases=["measure zero", "null set", "measure zero in a manifold"], scope=EB,
         syl=f"[[{LEE}#page=144|Lee Lemma 6.2, Props. 6.3–6.8, pp. 126–128]].",
         intuition="A set so thin it can be covered by countably many cubes of arbitrarily small total volume: curves in the plane, points on a line.",
         key="$A\\subseteq\\mathbb R^n$ has measure zero if for every $\\varepsilon>0$ countably many cubes of total volume $<\\varepsilon$ cover it. Countable unions are null; null sets have empty interior; $C^1$ maps preserve null sets (Lipschitz estimate), so the notion is chart independent on manifolds.",
         body="If $\\dim M<\\dim N$, $F(M)$ is null in $N$ (apply the previous fact to $F(x,y)=F(x)$ on $U\\times\\mathbb R^{n-m}$). The parabola arc $\\{(t,t^2)\\}$: $\\varepsilon$-neighbourhood area $\\approx2\\varepsilon L\\to0$.",
         used=[CH], related=["Sard's Theorem", "Whitney Embedding Theorem"]),
    dict(title="Sard's Theorem", aliases=["Sard", "Morse-Sard theorem", "regular values are dense"], scope=EB,
         syl=f"[[{LEE}#page=147|Lee Thm 6.10, p. 129]], [[{LEE}#page=149|Cor. 6.11, p. 131]]; Milnor §3 (stated, not proved in DM07).",
         intuition="Critical values are rare: almost every level of a smooth map is a regular level, hence a manifold.",
         key="For a smooth map $F:M\\to N$ the set of critical values has measure zero in $N$; so regular values are dense. Needs $C^\\infty$ (or $C^k$, $k\\ge\\max(m-n+1,1)$).",
         body="$f=x^3-3x$: critical values $\\pm2$ only (all $5000$ random levels regular). Critical *points* may be numerous even though critical *values* are null. Makes the [[Regular Level Set Theorem]] apply to almost every level.",
         used=[CH], related=["Regular Value", "Set of Measure Zero", "Regular Level Set Theorem"]),
    dict(title="Whitney Embedding Theorem", aliases=["Whitney embedding", "Whitney immersion theorem", "every manifold embeds in R^N"], scope=EB,
         syl=f"[[{LEE}#page=152|Lee Thm 6.15, p. 134]]; Thms 6.18–6.20 (immersion, strong forms).",
         intuition="Every abstract manifold can be realised as a surface in some Euclidean space; in fact $2n+1$ (even $2n$) dimensions always suffice.",
         key="Every smooth $n$-manifold embeds in $\\mathbb R^{2n+1}$ (Thm 6.15; proof: partition of unity gives an embedding in some $\\mathbb R^N$, then project along a direction avoiding the secant ($\\dim2n$) and tangent ($\\dim2n-1$) directions, possible when $N-1>2n$ by Sard-type measure arguments). Strong: $\\mathbb R^{2n}$; immersions: $\\mathbb R^{2n}$ ($\\mathbb R^{2n-1}$ for $n>1$).",
         body="Sharp: $\\mathbb{RP}^2$ embeds in $\\mathbb R^4$, not $\\mathbb R^3$. The trefoil's secant directions fill $S^2$ (648/648 bins), so projection to a plane always creates crossings.",
         used=[CH], related=["Smooth Embedding", "Partition of Unity", "Sard's Theorem"]),
    dict(title="Transversality", aliases=["transverse", "transverse intersection", "transversal maps"], scope=EB,
         syl=f"[[{LEE}#page=162|Lee Thm 6.30, p. 144]]; Thms 6.35–6.36; Guillemin–Pollack Ch. 2.",
         intuition="Two things meet 'cleanly' when their tangent spaces together span everything: no tangential grazing.",
         key="$f:N\\to M$ is **transverse** to an embedded $S\\subseteq M$ if $df_p(T_pN)+T_{f(p)}S=T_{f(p)}M$ for all $p\\in f^{-1}(S)$. Then $f^{-1}(S)$ is an embedded submanifold of codimension $\\operatorname{codim}S$. Case $S=\\{q\\}$: $q$ is a regular value.",
         body="$y=x^2-c$ is transverse to the $x$-axis iff $c\\ne0$ (slope angles $\\pm45^\\circ$ at $c=0.25$; tangent at $c=0$). The circle is tangent to $y=1$ at $(0,1)$. Transversality is generic and stable.",
         used=[CH], related=["Regular Level Set Theorem", "Regular Value", "Embedded Submanifold"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
