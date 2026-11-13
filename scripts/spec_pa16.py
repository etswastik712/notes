"""Concept notes for PA16 (Peano's axioms).   .venv/bin/python -W ignore scripts/spec_pa16.py"""
from mkconcept import write

CH = "PA16 Peano's Axioms and the Natural Numbers"
T, EBY = "taught", "extra-beyond"
BY = ["lecture-notes"]
L25 = "[[L-25.pdf#page=1|Lecture 25]]"

ITEMS = [
    dict(title="Peano System", aliases=["Peano axioms", "Peano's axioms", "Dedekind-Peano axioms", "successor function", "(P1)-(P3)", "predecessor lemma"], scope=[T, EBY], by=BY,
         syl={T: f"{L25}: the three axioms, the example, the three non-examples, Lemma 1 (predecessor), isomorphism of Peano systems, the ZFC model.", EBY: "no finite Peano system; the explicit finite checks (mine)."},
         intuition="A start (1) and a step ($s$) that never goes back to the start and never merges two numbers, with the rule that *nothing exists except what you reach from the start by steps*. That last rule is induction.",
         key="A **Peano system** is $(N,1,s)$ with $s:N\\to N$ and **(P1)** $s(n)\\ne1$ for all $n$; **(P2)** $s$ injective; **(P3)** if $S\\subseteq N$, $1\\in S$ and $s(S)\\subseteq S$ then $S=N$. **Lemma 1:** every $n\\ne1$ is $s(m)$ for exactly one $m$ (apply (P3) to $\\{1\\}\\cup\\mathrm{Im}\\,s$, then (P2)).",
         body="**Each axiom is needed:** $\\{1\\}$ with $s(1)=1$ breaks (P1); $\\{1,2\\}$ with $s(1)=s(2)=2$ breaks (P2); $\\mathbb N\\cup\\mathbb N'$ (a disjoint second copy) breaks (P3). No finite set works: an injective $s$ on a finite set is onto, contradicting (P1). Any two Peano systems are isomorphic; ZFC gives $0=\\varnothing$, $s(x)=x\\cup\\{x\\}$ as a model.",
         used=[CH, "PA05 Induction and the Number Systems"], related=["Natural Numbers", "Principle of Mathematical Induction", "Recursion Theorem", "Arithmetic on the Natural Numbers from the Successor", "Well-Ordering Principle"]),
    dict(title="Arithmetic on the Natural Numbers from the Successor", aliases=["recursive definition of addition", "recursive definition of multiplication", "n+s(m)=s(n+m)", "associativity of addition", "commutativity of addition", "cancellation law for addition", "1+n=n+1"], scope=[T, EBY], by=BY,
         syl={T: f"{L25}: the definitions of $+$ and $\\cdot$, Theorem 3 ($1+n=n+1$), Theorem 4 (associativity), the list of further results.", EBY: "full proofs of commutativity, cancellation and $a+z\\ne a$ (mine), and a machine check on $1\\le n\\le40$."},
         intuition="Adding $m$ means *taking the successor $m$ times*; multiplying by $m$ means *adding $n$ to itself $m$ times*. Every law about them is proved by induction on one variable, with the others held fixed.",
         key="$n+1:=s(n)$, $n+s(m):=s(n+m)$ (so $n+(m+1)=(n+m)+1$ by definition); $n\\cdot1:=n$, $n\\cdot(m+1):=n\\cdot m+n$. That these rules define functions on $N\\times N$ is the **Recursion Theorem**. Proved by induction: $1+n=n+1$; $(a+b)+c=a+(b+c)$; $a+b=b+a$; $a+c=b+c\\Rightarrow a=b$ (uses (P2)); multiplication commutative, associative, distributive.",
         body="Worked: $2+2=2+s(1)=s(2+1)=s(s(2))=s(3)=4$. The usual trap: the rule $n+(m+1)=(n+m)+1$ is the *definition* of $+$ and the **base case** of associativity, not associativity itself.",
         used=[CH], related=["Peano System", "Order on the Natural Numbers", "Recursion Theorem", "Principle of Mathematical Induction", "Group"]),
    dict(title="Order on the Natural Numbers", aliases=["a<b iff b=a+x", "discrete order", "no natural number between a and a+1", "trichotomy for natural numbers"], scope=[T, EBY], by=BY,
         syl={T: f"{L25}: the definition $a<b\\iff b=a+x$, Theorem 5, the link to PMI $\\Leftrightarrow$ WOP, trichotomy in the list of further results.", EBY: "proofs of exercises (d), (e) and of $a+z\\ne a$ (mine)."},
         intuition="$a<b$ means you can walk from $a$ to $b$ by taking at least one step. There is no room between $a$ and its successor, which is exactly why a least element always exists.",
         key="$a<b:\\iff b=a+x$ for some $x\\in N$; $a\\le b:\\iff a<b$ or $a=b$. **Theorem 5:** $a<b\\Rightarrow a+1\\le b$ (write $x=y+1$ by Lemma 1, then $b=(a+1)+y$). Also: no $n<1$; $a<b$ and $b<a$ cannot both hold (since $a+z\\ne a$); exactly one of $a<b$, $a=b$, $b<a$; $<$ is transitive and preserved by adding $c$.",
         body="Lemma 1 and Theorem 5 are exactly the two facts used to prove the **well-ordering principle from induction**, so PMI $\\Leftrightarrow$ WOP rests only on (P1)–(P3) and the definitions of $+$ and $<$.",
         used=[CH, "PA10 Well-Ordering and Well-Ordered Pairs"], related=["Peano System", "Arithmetic on the Natural Numbers from the Successor", "Well-Ordering Principle", "Principle of Mathematical Induction", "Partially Ordered Set"]),
]

if __name__ == "__main__":
    write("11-Proofs-Analysis-Topology", "analysis", ITEMS)
