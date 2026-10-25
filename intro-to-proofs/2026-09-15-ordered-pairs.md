---
id: intro-to-proofs/2026-09-15-ordered-pairs
aliases: [Ordered pairs, Kuratowski ordered pair]
tags: [intro-to-proofs, set-theory, ZFC]
trust_tier: agent_written
---
# Ordered pairs

## Covered
Source: ordered pairs.pdf (Classroom: Ordered pairs). Question: which sets built by Pairing can represent $(A,B)$?

**Defining property (OP).** $(A,B)=(C,D)\iff A=C$ and $B=D$. The coordinates must be uniquely recoverable. Notes from the handout:
- Do not require $(A,B)\ne(B,A)$ for all $A,B$ (when $A=B$ they coincide); only for $A\ne B$ does it follow from (OP).
- $(A,A)\ne\{A\}$ is true for Kuratowski's definition but is not part of what makes something an ordered pair.

**Fails: $\{A,B\}$.** $\{A,B\}=\{B,A\}$, so it forgets order (e.g. $\{1,2\}=\{2,1\}$).

**Kuratowski.** $(A,B):=\{\{A\},\{A,B\}\}$. $A$ is in both inner sets, $B$ only in $\{A,B\}$.

Notation: for a nonempty family $\mathcal F$ of sets, $\bigcap\mathcal F=\{x: x\in E\ \forall E\in\mathcal F\}$, $\bigcup\mathcal F=\{x: x\in E\text{ for some }E\in\mathcal F\}$. With $\mathcal F=\{\{A\},\{A,B\}\}$: $\bigcap\mathcal F=\{A\}\cap\{A,B\}=\{A\}$ and $\bigcup\mathcal F=\{A,B\}$. If $A=B$ then $\mathcal F=\{\{A\}\}$ and the formulas still hold. If $\mathcal F=\mathcal G$ then $\bigcap\mathcal F=\bigcap\mathcal G$ and $\bigcup\mathcal F=\bigcup\mathcal G$ (same members).

**Proposition 1.** $\{\{A\},\{A,B\}\}=\{\{C\},\{C,D\}\}\iff A=C$ and $B=D$.
Proof ($\Rightarrow$): equal intersections give $\{A\}=\{C\}$, so $A=C$. Equal unions give $\{A,B\}=\{C,D\}=\{A,D\}$. Since $B\in\{A,D\}$, $B=A$ or $B=D$. If $B\ne A$, $B=D$. If $B=A$, then $\{A,D\}=\{A\}$, forcing $D=A=B$. So $B=D$ always. ($\Leftarrow$): substitution.

**$A=B$ case.** $(A,A)=\{\{A\},\{A,A\}\}=\{\{A\}\}$. If $\{\{A\}\}=\{A\}$ then $\{A\}=A$, so $A\in A$, excluded by the Axiom of Regularity. Hence $(A,A)\ne\{A\}$.

**Fails: $\{\{A\},\{B\}\}$.** Symmetric: $\{\{A\},\{B\}\}=\{\{B\},\{A\}\}$.

**Fails: $F(A,B)=\{A,\{B\}\}$.** Counterexample with $X=\varnothing$, $Y=\{\varnothing\}$, $Z=\{\{\varnothing\}\}$: $F(Z,X)=\{Z,\{X\}\}=\{Z,Y\}$ and $F(Y,Y)=\{Y,\{Y\}\}=\{Y,Z\}$, so $F(Z,X)=F(Y,Y)$ although $(Z,X)\ne(Y,Y)$.

**Works in ZFC: $\{A,\{A,B\}\}$ (Proposition 2).** Suppose $\{A,\{A,B\}\}=\{C,\{C,D\}\}$. Then $A=C$ or $A=\{C,D\}$, and $C=A$ or $C=\{A,B\}$. If $A\ne C$ then $A=\{C,D\}$ and $C=\{A,B\}$, so $C\in A\in C$, a membership cycle, ruled out by Regularity. So $A=C$. Regularity also gives $A\ne\{A,B\}$ and $A\ne\{A,D\}$ (else $A\in A$), so equality forces $\{A,B\}=\{A,D\}$, hence $B=D$. This proof needs Regularity; the Kuratowski proof does not.

**Why Kuratowski is preferred.** Simple; built from Pairing and elementary set operations; asymmetric coordinates; clean proof of (OP); no appeal to Regularity for (OP); $\bigcap(A,B)=\{A\}$ recovers the first coordinate; $\bigcup(A,B)=\{A,B\}$ recovers the unordered pair.

**Test for any proposal $F(A,B)$.** Is $F(A,B)=F(C,D)\iff A=C$ and $B=D$? If yes, legitimate; a single counterexample with $F(A,B)=F(C,D)$ but $A\ne C$ or $B\ne D$ kills it.

## From the post
(no text)

## Files
- [ordered pairs.pdf](https://drive.google.com/file/d/1BjdmQRMAiFqhQvV5EIfcSFQ0Tf9xcYma/view?usp=drive_web) (saved as intro-to-proofs/2026-10-25-ordered-pairs-1BjdmQ.pdf)

## Related
- [[11-Proofs-Analysis-Topology/Concepts/Ordered Pair]]: their concept note on the same definition
- [[11-Proofs-Analysis-Topology/PA02 Sets Families and the ZFC Foundations]]: ZFC axioms (Pairing, Regularity) and families
