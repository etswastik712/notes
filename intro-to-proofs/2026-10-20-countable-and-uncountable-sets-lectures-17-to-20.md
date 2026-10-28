---
id: intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20
aliases: [Countable and Uncountable sets: Lectures 17 to 20, Countable and Uncountable sets]
tags: [intro-to-proofs, lecture, cardinality, countable-sets, uncountable-sets]
trust_tier: agent_written
---
# Countable and Uncountable sets: Lectures 17 to 20

## Covered
Lectures 17 to 20 by Supriya Pisolkar (Classroom file: Countable-Uncountable-sets.pdf).

### Lecture 17: Finite and Countable Sets, Countability of $\mathbb{Q}$

**Definitions:**
- **Finite set:** A set $A$ is finite if $A = \emptyset$ or there exists a bijection $A \to N_k = \{1, 2, \dots, k\}$ for some $k \in \mathbb{N}$. Cardinality $|A| = 0$ if $A = \emptyset$, and $|A| = k$ if $A \sim N_k$.
- **Equicardinality:** Sets $A$ and $B$ have the same cardinality, written $|A| = |B|$ or $A \sim B$, if and only if there exists a bijection $A \to B$. (E.g. $|\{a, b\}| = |\{1, 2\}|$; $|\mathbb{N}| = |E|$ where $E = \{2n : n \in \mathbb{N}\}$ is the set of even natural numbers via $n \mapsto 2n$).
- **Countable set:** A set is countable if it is finite or in bijection with $\mathbb{N}$ (i.e. countably infinite). Examples: $\mathbb{N}$, $\mathbb{Z}$, $E$, and the odd natural numbers are countable.
- **Cardinality of $\mathbb{N}$:** Denoted $|\mathbb{N}| = \aleph_0$ (aleph-naught).

**Theorem: $\mathbb{Q}$ is countable.**
- **Proof:**
  - **Step 1: $\mathbb{Q}_{>0}$ is countable.**
    Write $\mathbb{Q}_{>0} = \{m/n : m, n \in \mathbb{N}\}$. Arrange all positive rational fractions in a 2D grid:
    Row $m$, Column $n$ contains $m/n$.
    Traverse the grid diagonally along diagonals of constant sum $m+n$:
    - Diagonal $m+n=2$: $1/1$ (1st diagonal)
    - Diagonal $m+n=3$: $1/2, 2/1$ (2nd diagonal)
    - Diagonal $m+n=4$: $3/1, 2/2, 1/3$ (3rd diagonal), etc.
    Every positive rational $m/n$ is reached on the $(m+n-1)$-th diagonal.
    Omit any fraction already visited (e.g. $2/2, 3/3, 2/4$). This yields a sequence of distinct reduced fractions:
    $$\{a_1, a_2, a_3, \dots\} = \left\{ \frac{1}{1}, \frac{1}{2}, \frac{2}{1}, \frac{3}{1}, \frac{1}{3}, \dots \right\}$$
    Define $f: \mathbb{N} \to \mathbb{Q}_{>0}$ by $f(m) = a_m$.
    - Injective: $f(m_1) = f(m_2) \implies a_{m_1} = a_{m_2} \implies m_1 = m_2$, since all $a_i$ are distinct.
    - Surjective: Any $r \in \mathbb{Q}_{>0}$ can be written in lowest terms $p/q$, which appears on diagonal $p+q-1$ and is retained, so $r = a_m = f(m)$ for some $m \in \mathbb{N}$.
    Thus $\mathbb{Q}_{>0} \sim \mathbb{N}$, so $\mathbb{Q}_{>0}$ is countable.
  - **Step 2: $\mathbb{Q}_{<0}$ is countable.**
    Define $f: \mathbb{Q}_{>0} \to \mathbb{Q}_{<0}$ by $x \mapsto -x$.
    - Injective: $-x_1 = -x_2 \implies x_1 = x_2$.
    - Surjective: For any $r \in \mathbb{Q}_{<0}$, $-r \in \mathbb{Q}_{>0}$ and $f(-r) = -(-r) = r$.
    Since composition of bijections is a bijection, $\mathbb{N} \sim \mathbb{Q}_{>0} \sim \mathbb{Q}_{<0}$, so $\mathbb{Q}_{<0}$ is countable.
  - **Step 3: $\mathbb{Q} = \mathbb{Q}_{<0} \cup \{0\} \cup \mathbb{Q}_{>0}$ is countable.**
    Let $\mathbb{Q}_{>0} = \{a_1, a_2, \dots\}$ and $\mathbb{Q}_{<0} = \{-a_1, -a_2, \dots\}$. Construct the sequence:
    $$\{0, a_1, -a_1, a_2, -a_2, \dots\}$$
    Explicitly define $f: \mathbb{N} \to \mathbb{Q}$ by:
    $$f(n) = \begin{cases} 0, & n = 1 \\ a_{n/2}, & n \text{ is even} \\ -a_{(n-1)/2}, & n \text{ is odd, } n \ne 1 \end{cases}$$
    - Injective: 0 appears only at $n=1$. Positive rationals appear at even indices and negative rationals at odd indices ($n \ge 3$). Since all $a_k$ are distinct and positive, no two terms in the sequence are equal.
    - Surjective: Let $r \in \mathbb{Q}$. If $r=0$, $f(1)=0$. If $r>0$, $r=a_k$ for some $k \in \mathbb{N}$, so $f(2k) = a_k = r$. If $r<0$, $r = -a_t$ for some $t \in \mathbb{N}$, so $f(1+2t) = -a_t = r$.
    Hence $f$ is a bijection, and $\mathbb{Q}$ is countably infinite. $\square$

**Historical milestones:**
- 1638 (Galileo): Bijection between $\mathbb{N}$ and the perfect squares $\{n^2 : n \in \mathbb{N}\}$.
- 1851 (Bolzano): First use of the mathematical term "set"; constructed bijections between intervals of different lengths.
- 1888 (Dedekind): Defined an infinite set as one in bijection with a proper subset of itself.
- 1874 (Cantor): Proved $\mathbb{N}$ and $\mathbb{R}$ are not in bijection; formulated the Continuum Hypothesis; introduced "countable" and "uncountable".

---

### Lecture 18: Cardinality Equivalence and Subsets

**Relation $\sim$:**
For sets $A, B$, write $A \sim B$ if there is a bijection $A \to B$.
$\sim$ is an equivalence relation on the power set of any universe:
1. Reflexive: $\operatorname{id}_A: A \to A$ is a bijection, so $A \sim A$.
2. Symmetric: If $f: A \to B$ is a bijection, $f^{-1}: B \to A$ is a bijection, so $B \sim A$.
3. Transitive: If $f: A \to B$ and $g: B \to C$ are bijections, $g \circ f: A \to C$ is a bijection, so $A \sim C$.

**Assumed blackbox principles:**
1. There is no injection $N_{n+1} \to N_n$ for any $n \ge 1$ (hence $N_m \sim N_n \implies m = n$).
2. Any subset of $N_k$ is finite: $A \subseteq N_k \implies A \sim N_j$ for some $j \le k$.
3. Every subset of $\mathbb{N}$ is countable (Well-Ordering Principle of $\mathbb{N}$).

**Consequences:**
- **Proposition 1:** If $A \subseteq B$ and $B$ is finite, then $A$ is finite ($|A| \le |B|$).
  *Proof:* If $B = \emptyset$, $A = \emptyset$. Else let $f: B \to N_k$ be a bijection. The restriction $f|_A: A \to f(A) \subseteq N_k$ is an injection, hence $f(A) \sim N_j$ for some $j \le k$, so $A \sim N_j$. $\square$
- **Proposition 2:** If $B \sim N_k$ with $k \ge 1$ and $x \in B$, then $B \setminus \{x\} \sim N_{k-1}$.
  *Proof:* Let $f: B \to N_k$ be a bijection with $i = f(x)$. Let $\sigma: N_k \to N_k$ swap $i$ and $k$ and fix all other elements. $\sigma$ is a bijection, so $g = \sigma \circ f: B \to N_k$ is a bijection with $g(x) = k$. Restricting $g$ to $B \setminus \{x\}$ yields a bijection onto $N_k \setminus \{k\} = N_{k-1}$. $\square$
- **Corollary:** A finite set is never equivalent to any of its proper subsets.
  *Proof:* Let $|B| < \infty$ and $A \subsetneq B$. Pick $x \in B \setminus A$. Then $A \subseteq B \setminus \{x\}$. By Proposition 2, $B \setminus \{x\} \sim N_{k-1}$, so $A \sim N_j$ for some $j \le k-1$. If $A \sim B$, then $N_j \sim A \sim B \sim N_k$ with $j < k$, contradicting blackbox 1. $\square$
- **Proposition 3:** $\mathbb{N}$ is infinite.
  *Proof:* The map $f: \mathbb{N} \to O$ given by $n \mapsto 2n-1$ is a bijection onto the set $O$ of odd natural numbers. But $O \subsetneq \mathbb{N}$ (since $2 \notin O$). If $\mathbb{N}$ were finite, this would contradict the Corollary. $\square$
- **Proposition 4:**
  1. If $A \sim B$ and $A$ is infinite, then $B$ is infinite.
  2. If $A$ is infinite and $A \subseteq B$, then $B$ is infinite.
- **Corollary:** If $A \subseteq B$ and $B$ is countable, then $A$ is countable.
  *Proof:* If $B$ is finite, $A$ is finite (Proposition 1). If $B$ is countably infinite, let $f: B \to \mathbb{N}$ be a bijection; restricting $f$ to $A$ gives $A \sim f(A) \subseteq \mathbb{N}$, which is countable by blackbox 3. $\square$
- **Contrapositive:** If $A \subseteq B$ and $A$ is uncountable, then $B$ is uncountable.
- **Definition of Uncountable Set:** An infinite set that is not countable is called uncountable.

---

### Lecture 19: Uncountability of $(0, 1)$ and Cantor's Diagonal Argument

**Decimal representation of reals:**
Every $x \in (0, 1)$ can be written as $x = 0.a_1 a_2 a_3 \dots = \sum_{k=1}^\infty a_k 10^{-k}$ with $a_k \in \{0, 1, \dots, 9\}$. The series converges because $a_k 10^{-k} \le 9 \cdot 10^{-k}$ and $\sum_{k=1}^\infty 9 \cdot 10^{-k} = 1$.
- **Non-uniqueness of decimal expansions:** $0.4999\dots = 0.5000\dots = 1/2$.
- **Normalized form:** A decimal representation $0.a_1 a_2 \dots$ is normalized if it does not end in an infinite string of 9s (i.e. there is no $k$ such that $a_n = 9$ for all $n > k$). If a number ends in all 9s, replace it with the terminating expression ending in 0s.
- **Uniqueness Theorem:** Every $x \in (0, 1)$ has exactly one normalized decimal expression.
- **Equality Theorem:** Two decimal numbers in normalized form are equal if and only if they have identical digits in every decimal position.

**Theorem: The open interval $(0, 1)$ is uncountable.**
- **Proof:**
  - **Step 1: $(0, 1)$ is infinite.**
    The set $A = \{1/2, 1/3, 1/4, \dots\} \subseteq (0, 1)$ is infinite via the bijection $\mathbb{N} \to A, n \mapsto \frac{1}{n+1}$.
  - **Step 2: No function $f: \mathbb{N} \to (0, 1)$ is surjective.**
    Let $f: \mathbb{N} \to (0, 1)$ be an arbitrary function. Write each value $f(n)$ in its unique normalized decimal form:
    $$\begin{aligned}
    f(1) &= 0.a_{11} a_{12} a_{13} \dots \\
    f(2) &= 0.a_{21} a_{22} a_{23} \dots \\
    &\;\;\vdots \\
    f(n) &= 0.a_{n1} a_{n2} a_{n3} \dots
    \end{aligned}$$
    Define a real number $b = 0.b_1 b_2 b_3 \dots$ by modifying the diagonal digits:
    $$b_k = \begin{cases} 3, & \text{if } a_{kk} \ne 3 \\ 7, & \text{if } a_{kk} = 3 \end{cases} \quad \text{for all } k \in \mathbb{N}$$
    - Since every digit $b_k \in \{3, 7\}$, we have $0 < 0.333\dots \le b \le 0.777\dots < 1$, so $b \in (0, 1)$.
    - Since $b$ contains no 9s, it is in normalized form.
    - For each $n \in \mathbb{N}$, $b$ differs from $f(n)$ at the $n$-th decimal place ($b_n \ne a_{nn}$). By the Equality Theorem, $b \ne f(n)$ for all $n \in \mathbb{N}$.
    Thus $b \notin \operatorname{Im}(f)$, so $f$ cannot be surjective.
    Since no function $\mathbb{N} \to (0, 1)$ can be surjective, no bijection exists, so $(0, 1)$ is uncountable. $\square$

**Theorem: Every open interval $(a, b)$ with $a < b$ has $(a, b) \sim (0, 1)$, hence is uncountable.**
- **Proof:** Define $f: (0, 1) \to (a, b)$ by $f(x) = a + (b-a)x$.
  - Injective: $a + (b-a)x_1 = a + (b-a)x_2 \implies (b-a)x_1 = (b-a)x_2 \implies x_1 = x_2$ since $b-a \ne 0$.
  - Surjective: For any $y \in (a, b)$, $x = \frac{y-a}{b-a} \in (0, 1)$ satisfies $f(x) = y$.
  Thus $f$ is a bijection. $\square$

---

### Lecture 20: Uncountability of $\mathbb{R}$, Cantor's Theorem, and the Continuum Hypothesis

**Theorem: $\mathbb{R}$ is uncountable.**
- **Proof:** Construct an explicit bijection $f: (0, 1) \to \mathbb{R}$:
  $$f(x) = \begin{cases} 1 - \frac{1}{2x}, & 0 < x \le \frac{1}{2} \\ \frac{1}{2(1-x)} - 1, & \frac{1}{2} \le x < 1 \end{cases}$$
  - Note $f(1/2) = 1 - 1 = 0 = 1 - 1$.
  - For $0 < x \le 1/2$: $0 < 2x \le 1 \implies \frac{1}{2x} \ge 1 \implies f(x) = 1 - \frac{1}{2x} \le 0$, so $f((0, 1/2]) = (-\infty, 0]$.
  - For $1/2 \le x < 1$: $0 < 2(1-x) \le 1 \implies \frac{1}{2(1-x)} \ge 1 \implies f(x) \ge 0$, so $f([1/2, 1)) = [0, \infty)$.
  Construct the candidate inverse $g: \mathbb{R} \to (0, 1)$:
  $$g(y) = \begin{cases} \frac{1}{2(1-y)}, & y \le 0 \\ 1 - \frac{1}{2(1+y)}, & y \ge 0 \end{cases}$$
  Note $g(0) = 1/2$. For $y \le 0$, $1-y \ge 1 \implies 0 < g(y) \le 1/2$. For $y \ge 0$, $1+y \ge 1 \implies 1/2 \le g(y) < 1$.
  - Verification $g(f(x)) = x$:
    - If $x \in (0, 1/2]$, $f(x) \le 0$:
      $$g(f(x)) = \frac{1}{2(1 - f(x))} = \frac{1}{2\left(1 - \left(1 - \frac{1}{2x}\right)\right)} = \frac{1}{2 \cdot \frac{1}{2x}} = x$$
    - If $x \in [1/2, 1)$, $f(x) \ge 0$:
      $$g(f(x)) = 1 - \frac{1}{2(1 + f(x))} = 1 - \frac{1}{2\left(1 + \left(\frac{1}{2(1-x)} - 1\right)\right)} = 1 - (1-x) = x$$
  - Verification $f(g(y)) = y$:
    - If $y \le 0$, $g(y) \in (0, 1/2]$:
      $$f(g(y)) = 1 - \frac{1}{2 g(y)} = 1 - \frac{1}{2 \cdot \frac{1}{2(1-y)}} = 1 - (1-y) = y$$
    - If $y \ge 0$, $g(y) \in [1/2, 1)$:
      $$f(g(y)) = \frac{1}{2(1 - g(y))} - 1 = \frac{1}{2 \cdot \frac{1}{2(1+y)}} - 1 = (1+y) - 1 = y$$
  Hence $g = f^{-1}$, so $f$ is a bijection, establishing $(0, 1) \sim \mathbb{R}$.
  Since $(0, 1)$ is uncountable, $\mathbb{R}$ is uncountable (otherwise a bijection $\mathbb{N} \to \mathbb{R}$ composed with $g$ would give a bijection $\mathbb{N} \to (0, 1)$). $\square$

**Cardinalities and Cantor's Theorem:**
- $|\mathbb{R}| = \mathfrak{c}$ (continuum) $= 2^{\aleph_0} = \aleph_1$ (under CH notation).
- Strictly increasing hierarchy: $\aleph_0 = |\mathbb{N}| < \mathfrak{c} = |\mathbb{R}|$.
- **Cantor's Theorem:** For every set $A$, $|A| < |\mathcal{P}(A)|$:
  $$|\mathbb{N}| < |\mathcal{P}(\mathbb{N})| < |\mathcal{P}(\mathcal{P}(\mathbb{N}))| < \dots, \quad \text{with } |\mathcal{P}(\mathbb{N})| = |\mathbb{R}| = 2^{\aleph_0}$$

**Continuum Hypothesis (CH):**
- Question (Cantor): Does there exist any set $X$ such that $\aleph_0 < |X| < \mathfrak{c}$?
- **Continuum Hypothesis:** There is no set $X$ with $\aleph_0 < \operatorname{card}(X) < \mathfrak{c}$.
- Resolution: CH is independent of ZFC (Zermelo-Fraenkel set theory with Choice):
  - Kurt Gödel (1940): Proved CH cannot be disproved from ZFC.
  - Paul Cohen (1963): Proved CH cannot be proved from ZFC (using forcing, awarded Fields Medal).

## From the post
(no text)

## Files
- [Countable-Uncountable-sets.pdf](https://drive.google.com/file/d/1v6bK-dMcnb-cPsJaJkBICrsTWeakbTI3/view?usp=drive_web)
- Classroom post: [Countable and Uncountable sets: Lectures 17 to 20](https://classroom.google.com/c/ODcxNTUyOTc2ODA3/m/ODc0MTM2NTIxMzQz/details)

## Related
- [[11-proofs-analysis-topology/concepts/countable-set]]: definitions and foundational properties of countable sets
- [[11-proofs-analysis-topology/concepts/uncountable-set]]: Cantor diagonal argument and continuum cardinality $\mathfrak{c}$
- [[11-proofs-analysis-topology/pa04-functions-and-cardinality]]: lecture chapter on bijections and equicardinality
- [[intro-to-proofs/2026-10-19-solutions-assignment-7]]: subset of countable set is countable, and product of countably infinite sets is countably infinite
- [[intro-to-proofs/2026-10-22-assignment-8]]: assignment sheet practising uncountability proofs and interval bijections

<!-- kurooto:material6cdf64b0 -->
## Concepts in Countable-Uncountable-sets
[[zettel/cardinality-equivalence]], [[zettel/uncountable-set]], [[zettel/countability-of-the-rationals]], [[zettel/diagonal-traversal-enumeration]], [[zettel/finite-set-proper-subset-non-equivalence]], [[zettel/infinitude-of-the-natural-numbers]], [[zettel/normalized-decimal-expansion]], [[zettel/cantor-diagonal-argument]], [[zettel/uncountability-of-the-unit-interval]], [[zettel/uncountability-of-the-real-numbers]]
<!-- /kurooto:material6cdf64b0 -->
