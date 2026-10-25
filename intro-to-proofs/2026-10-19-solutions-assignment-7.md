---
id: intro-to-proofs/2026-10-19-solutions-assignment-7
aliases: [Solutions Assignment 7, Assignment 7 Solutions]
tags: [intro-to-proofs, solutions, assignment, countability]
trust_tier: agent_written
---
# Solutions: Assignment 7

## Covered
Instructor's solutions for Assignment 7, Questions 4 and 5 (Classroom file: Solutions_Assignment_7.pdf).

**Question 4. Subsets of countable sets are countable.**
- **Statement:** Let $A$ be a countable set and let $S \subseteq A$ be non-empty. Show that $S$ is countable.
- **Proof:**
  - **Case (a): $A$ is finite.**
    By definition, there exists $k \in \mathbb{N}$ and a bijection $f: \{1, 2, \dots, k\} \to A$.
    We first prove by induction on $k$ that every non-empty subset of $\{1, 2, \dots, k\}$ is finite:
    1. Base case ($k=1$): The only non-empty subset of $\{1\}$ is $\{1\}$ itself, which is finite.
    2. Inductive step: Assume that every non-empty subset of $\{1, 2, \dots, k\}$ is finite ($k \ge 1$). Let $T \subseteq \{1, 2, \dots, k+1\}$ be non-empty.
       - If $k+1 \notin T$, then $T \subseteq \{1, 2, \dots, k\}$, so $T$ is finite by the inductive hypothesis.
       - If $k+1 \in T$: if $T = \{k+1\}$, then $T$ is finite. Otherwise, let $T' = T \setminus \{k+1\} \subseteq \{1, 2, \dots, k\}$. By the inductive hypothesis, there exists $r \in \mathbb{N}$ and a bijection $h: \{1, 2, \dots, r\} \to T'$. Define $\tilde{h}: \{1, 2, \dots, r+1\} \to T$ by $\tilde{h}(i) = h(i)$ for $1 \le i \le r$, and $\tilde{h}(r+1) = k+1$. Then $\tilde{h}$ is a bijection, so $T$ is finite.
       - By PMI, every non-empty subset of $\{1, 2, \dots, k\}$ is finite.
    Now let $S \subseteq A$ be non-empty. Consider $T = f^{-1}(S) = \{i \in \{1, \dots, k\} : f(i) \in S\}$. Since $f$ is a bijection and $S \ne \emptyset$, $T$ is a non-empty subset of $\{1, \dots, k\}$. Thus there exists $r \in \mathbb{N}$ and a bijection $h: \{1, \dots, r\} \to T$. The restriction $f|_T: T \to S$ is a bijection. Therefore, the composition $f|_T \circ h: \{1, \dots, r\} \to S$ is a bijection, proving $S$ is finite.
  - **Case (b): $A$ is countably infinite and $S$ is infinite.**
    There exists a bijection $f: \mathbb{N} \to A$, so $A = \{f(1), f(2), f(3), \dots\}$.
    Since $S \ne \emptyset$, the index set $\{n \in \mathbb{N} : f(n) \in S\}$ is a non-empty subset of $\mathbb{N}$.
    By the Well-Ordering Principle of $\mathbb{N}$, every non-empty subset of $\mathbb{N}$ has a least element. Define:
    $$n_1 = \min\{n \in \mathbb{N} : f(n) \in S\}$$
    Inductively, define:
    $$n_{k+1} = \min\{n \in \mathbb{N} : n > n_k \text{ and } f(n) \in S\}$$
    Each $n_{k+1}$ exists because $S$ is infinite (otherwise $S \subseteq \{f(1), \dots, f(n_k)\}$ would be finite).
    Define $g: \mathbb{N} \to S$ by $g(k) = f(n_k)$.
    - Injectivity: If $g(i) = g(j)$, then $f(n_i) = f(n_j)$. Since $f$ is injective, $n_i = n_j$. Since the sequence $(n_k)_{k \in \mathbb{N}}$ is strictly increasing, $n_i = n_j \iff i = j$. Hence $g$ is injective.
    - Surjectivity: Let $s \in S$. Since $f: \mathbb{N} \to A$ is surjective and $S \subseteq A$, there exists $n \in \mathbb{N}$ such that $f(n) = s$. The index $n$ must appear in the sequence $(n_k)$: if there were no $k$ with $n_k = n$, then for some $m$ we would have $n < n_m$, implying all remaining elements of $S$ have indices bounded, which contradicts $S$ being infinite. Hence $n = n_k$ for some $k$, so $g(k) = f(n_k) = f(n) = s$. Hence $g$ is surjective.
    Therefore, $g$ is a bijection, and $S$ is countably infinite. $\square$

**Question 5. Cartesian product of countably infinite sets.**
- **Statement:** Let $A$ and $B$ be countably infinite sets, with bijections $f: \mathbb{N} \to A$ and $g: \mathbb{N} \to B$. Define $F: \mathbb{N} \times \mathbb{N} \to A \times B$ by $F(m, n) = (f(m), g(n))$. Show that $F$ is a bijection. Conclude that $A \times B$ is countably infinite.
- **Proof:**
  - Injectivity: Suppose $F(m_1, n_1) = F(m_2, n_2)$ for $(m_1, n_1), (m_2, n_2) \in \mathbb{N} \times \mathbb{N}$. Then $(f(m_1), g(n_1)) = (f(m_2), g(n_2))$, which means $f(m_1) = f(m_2)$ and $g(n_1) = g(n_2)$. Since $f$ and $g$ are injective, $m_1 = m_2$ and $n_1 = n_2$. Thus $(m_1, n_1) = (m_2, n_2)$, so $F$ is injective.
  - Surjectivity: Let $(a, b) \in A \times B$ be arbitrary. Since $f$ and $g$ are surjective, there exist $m, n \in \mathbb{N}$ such that $f(m) = a$ and $g(n) = b$. Then $(m, n) \in \mathbb{N} \times \mathbb{N}$ and $F(m, n) = (f(m), g(n)) = (a, b)$. Hence $F$ is surjective.
  - Conclusion: $F$ is a bijection. Since $\mathbb{N} \times \mathbb{N}$ is countably infinite (Assignment 7, Problem 3; diagonal traversal), composition of bijections implies $A \times B$ is countably infinite. $\square$

**Proof patterns:**
- Well-ordering extraction: to construct a bijection from $\mathbb{N}$ to an infinite subset $S \subseteq \mathbb{N}$, extract strictly increasing minimums $n_{k+1} = \min\{n > n_k : f(n) \in S\}$.
- Product bijections: given coordinate bijections $f, g$, the componentwise map $F(m,n) = (f(m), g(n))$ is automatically bijective, transferring countability from $\mathbb{N} \times \mathbb{N}$ to $A \times B$.

## From the post
Dear Batch 1,

As discussed in the last tutorial, please find the solutions of questions 4 and 5 of assignment 7, attached. We will discuss these briefly in the next tutorial. 

Please note that my tutorials hours are 4-5 PM, Tuesday (because Friday is not possible for most of the students). If you want to collect your quiz 3 answer sheets, you may do so only during office hours. I will inform when quiz 4 is graded.

Thanks,
Aakanksha

## Files
- [Solutions_Assignment_7.pdf](https://drive.google.com/file/d/1whqmxLNF2x3J722EusIBt9tBN3zv95Mb/view?usp=drive_web)
- Classroom post: [announcement](https://classroom.google.com/c/ODcxNTUyOTc2ODA3/p/ODc0MTIwMjYzMjM4)

## Related
- [[intro-to-proofs/2026-10-15-assignment-7]]: the problem sheet whose questions 4 and 5 are solved here
- [[11-proofs-analysis-topology/concepts/countable-set]]: definitions and foundational properties of countable sets
- [[11-proofs-analysis-topology/pa04-functions-and-cardinality]]: lecture chapter on bijections and equicardinality
