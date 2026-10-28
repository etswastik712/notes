---
title: Dirac Algebra
aliases: ["bra-ket algebra", "abstract Hilbert space", "Dirac formalism", "ket space", "quantum state space"]
subject: foundations
type: chapter
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
prereq: ["[[Dirac Notation]]", "[[Hilbert Space]]", "[[Hermitian Operator]]", "[[Canonical Commutation Relation]]"]
tags: [subject/foundations, type/chapter, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---

# Dirac Algebra

[[Quantum Mechanics - Course Map|QM Map]] · [[09-Foundations|Foundations]]

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is from Sakurai and what is extra in this chapter
> 🟡 **Extra · book** (Sakurai & Napolitano *Modern Quantum Mechanics* 3rd ed., Ch. 1 and §2.1 [[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF]]; Griffiths Ch. 3 [[Griffiths - Introduction to quantum mechanics.pdf|PDF pp.95–140]]; Shankar Ch. 1; Cohen-Tannoudji Vol. 1 Ch. II; Dirac Ch. 1–2):
> - §1 Ket space: physical motivation, vector space axioms, null ket, superposition, observables as operators, eigenket equation $\hat A|a'\rangle = a'|a'\rangle$, completeness (Sakurai §1.1–1.2)
> - §2 Dual space, bra vectors, the "DC machine", inner product axioms, Schwarz inequality, discrete and continuous orthonormality, phase conventions (Sakurai §1.2)
> - §3 Linear operators, outer product dyads $|\beta\rangle\langle\alpha|$, completeness relation as resolution of identity $\hat 1 = \sum |a'\rangle\langle a'|$, commutator algebra and Leibniz rules, harmonic oscillator matrix elements, projection operators (Sakurai §1.2–1.3)
> - §4 The adjoint (Hermitian conjugate), algebraic properties, Hermitian observables, full proofs of real eigenvalues and mutual orthogonality of distinct eigenstates, ladder operators as non-Hermitian examples (Sakurai §1.3)
> - §5 Completeness, state expansion amplitudes $c_{a'} = \langle a'|\alpha\rangle$, operator matrix elements, matrix multiplication as operator composition, unitary change of basis $U_{b'a'} = \langle b'|a'\rangle$, transformation of operators $X^{(b)} = U X^{(a)} U^\dagger$ (Sakurai §1.3–1.4)
> - §6 Position and momentum representations: continuous spectrum, wave function as inner product $\psi(x') = \langle x'|\alpha\rangle$, rigorous translation-operator derivation of $\hat p \leftrightarrow -i\hbar\partial_x$, plane wave eigenkets $\langle x'|p'\rangle$, Fourier transforms, Gaussian wave packet minimum-uncertainty demonstration (Sakurai §1.6–1.7)
> - §7 Unitary operators, spatial translation operator $\mathcal{T}(\ell) = e^{-i\hat p\ell/\hbar}$, canonical commutation relation $[\hat x,\hat p]=i\hbar$ from translation symmetry, Hadamard lemma / Baker–Campbell–Hausdorff translation of coordinate operator $e^{i\hat p a/\hbar}\hat x e^{-i\hat p a/\hbar} = \hat x + a\hat 1$, qubit Hadamard basis rotation (Sakurai §1.6)
> - §8 Measurement postulate in projector form, expectation values, dispersions, compatible observables and simultaneous eigenbases, CSCOs, complete derivation of the Robertson uncertainty relation $\Delta A\,\Delta B \ge \frac{1}{2}|\langle[\hat A,\hat B]\rangle|$, minimum-uncertainty saturation conditions, qubit and harmonic oscillator examples (Sakurai §1.4–1.5)
> - §9 Time evolution: unitary propagator $\hat U(t,t_0)$, infinitesimal generator, derivation of the Schrödinger equation $i\hbar\partial_t|\alpha,t\rangle = \hat H|\alpha,t\rangle$, stationary states, quantum beat frequency in 2-level superposition, harmonic oscillator coherent dynamics (Sakurai §2.1)
>
> 🔵 **Extra · beyond** (my additions and rigorous derivations):
> - §10 The Heisenberg picture: operator dynamics $\hat A_H(t) = \hat U^\dagger \hat A_S \hat U$, Heisenberg equation of motion, derivation of Ehrenfest's theorem, quantum Hamilton's equations, picture comparison table; all matrix and oscillator numerical examples computed and cross-checked with [[QM03 States Operators and Measurement]], [[QM05 The Harmonic Oscillator]], and [[QM06 The Oscillator Toolbox]].

> [!key] After this chapter you can
> - describe a physical quantum state as an abstract ket $|\alpha\rangle$ in a complex Hilbert space, independent of any coordinate representation,
> - construct the dual bra space $\langle\alpha|$ via the conjugate-linear dual correspondence ("DC machine") and apply the inner product axioms,
> - **prove** the Cauchy–Schwarz inequality in bra-ket notation and identify the geometric condition for saturation,
> - define linear operators, outer product dyads $|\beta\rangle\langle\alpha|$, and project states using projection operators $\hat P_n = |n\rangle\langle n|$,
> - **prove** from first principles that Hermitian operators possess strictly real eigenvalues and mutually orthogonal eigenstates for distinct eigenvalues,
> - insert the resolution of the identity $\hat 1 = \sum |a'\rangle\langle a'|$ or $\int dx'|x'\rangle\langle x'|$ to evaluate matrix elements, transform bases unitarily via $U X U^\dagger$, and switch between representations,
> - **derive** the position representation of momentum $\langle x'|\hat p|\alpha\rangle = -i\hbar\frac{\partial}{\partial x'}\psi(x')$ directly from the infinitesimal spatial translation operator,
> - **prove** the Robertson uncertainty relation $\Delta A\,\Delta B \ge \frac{1}{2}|\langle[\hat A,\hat B]\rangle|$ using the Schwarz inequality and operator decomposition into Hermitian and anti-Hermitian parts,
> - formulate quantum dynamics via the unitary time-evolution operator $\hat U(t,t_0) = e^{-i\hat H(t-t_0)/\hbar}$, derive the time-dependent Schrödinger equation, and translate between the Schrödinger, Heisenberg, and Interaction pictures.

> [!intuition] The one-sentence story
> Quantum mechanics is linear algebra on an infinite-dimensional complex vector space: physical states are unit-norm kets, physical questions are Hermitian operators whose eigenvalues are the possible measurement outcomes, inner products provide the probability amplitudes, and Dirac's bra-ket notation unifies wave mechanics, matrix mechanics, and momentum space into a single coordinate-free geometric framework.

<!-- da-patch-v1 -->
![[Dirac Algebra Map.svg]]
*Diagram DA.0. The chapter in one page: kets and bras, operators, adjoints, completeness, the two continuous representations, unitary translation, measurement and dynamics. Editable source: [[Dirac Algebra Map.excalidraw]].*

> [!intuition] How to read this chapter: five pictures to keep in your head
> 1. **A ket is an arrow, a wave function is its shadow.** The arrow $|\alpha\rangle$ is the state; $\psi(x)=\langle x|\alpha\rangle$ is its shadow on the "position ruler", $\tilde\psi(p)=\langle p|\alpha\rangle$ its shadow on the "momentum ruler", $c_n=\langle n|\alpha\rangle$ its shadow on the "energy ruler". Same arrow, three rulers (Figure DA.1).
> 2. **A bra is a measuring device.** $\langle\alpha|$ eats a ket and returns a number: how much of it lies along $\alpha$. Probabilities are $|\text{that number}|^2$.
> 3. **Inserting $\mathbf{1}=\sum|a\rangle\langle a|$ is free.** It multiplies by 1, so it changes nothing, but it gives you a basis to stand in. Nearly every proof below is "insert 1, then use what you know about the basis".
> 4. **Hermitian = a ruler that does not lie**: real readings, perpendicular axes. Unitary = a rigid rotation of Hilbert space: lengths and overlaps preserved. Translation and time evolution are unitary; position, momentum and energy are Hermitian.
> 5. **Non-commuting = different rulers.** If $[A,B]\neq0$ no single set of axes is sharp for both; sharpening the state along $A$ smears it along $B$, and Robertson's inequality is the exchange rate.

> [!pitfall] Six slips that recur in every Dirac-notation calculation
> 1. $c|\alpha\rangle\leftrightarrow c^*\langle\alpha|$ (the bra is *conjugate*-linear): $\langle\alpha|\,c\,|\beta\rangle=c\langle\alpha|\beta\rangle$ but $(c|\alpha\rangle)^\dagger=c^*\langle\alpha|$.
> 2. $(AB)^\dagger=B^\dagger A^\dagger$: **reverse the order**.
> 3. A continuous basis needs $\int dx'\,|x'\rangle\langle x'|$ and $\delta$-normalisation, not a sum and a Kronecker delta.
> 4. $\langle x'|p'\rangle=e^{ip'x'/\hbar}/\sqrt{2\pi\hbar}$ — the $\sqrt{2\pi\hbar}$ is what makes $\langle p|p'\rangle=\delta(p-p')$.
> 5. Hermitian is not the same as having real *matrix* entries: only the conjugate-transpose condition counts.
> 6. A global phase $e^{i\gamma}|\alpha\rangle$ is the same physical state; a *relative* phase between components is physical (it is what makes the beats of §9).

---

## 1. Ket space: the abstract state

<span class="scope-extra-book">extra · book</span> *Sakurai §1.2 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF Ch. 1]]); Griffiths §3.1–3.2 ([[Griffiths - Introduction to quantum mechanics.pdf|PDF pp.95–115]]); Shankar §1.1–1.3*

> [!intuition] Why abstract at all?
> Because the same physical state can be handed to you as a function of $x$, a function of $p$, or a list of numbers $c_n$, and no one of these is *the* state. The ket is what they have in common. It is like speaking of a vector in the plane rather than of its coordinates: coordinates change when you rotate the axes, the vector does not.

### Physical motivation: why abstract Hilbert space?

In wave mechanics (Schrödinger), a physical state is described by a complex spatial wave function $\psi(x)$. In matrix mechanics (Heisenberg), the same state is described by an infinite column vector of energy or number-basis amplitudes $(c_0, c_1, c_2, \dots)^{\mathsf T}$. In momentum space, it is represented by a Fourier profile $\tilde\psi(p)$. 

These three descriptions appear mathematically distinct:
1. **Position space:** continuous functions $\psi(x) \in L^2(\mathbb{R})$, with differential operators $\hat p = -i\hbar\frac{\partial}{\partial x}$.
2. **Momentum space:** continuous functions $\tilde\psi(p) \in L^2(\mathbb{R})$, with multiplication operators $\hat p = p$ and differential position $\hat x = i\hbar\frac{\partial}{\partial p}$.
3. **Energy/Number space:** discrete square-summable sequences $(c_0, c_1, \dots) \in \ell^2(\mathbb{C})$, with infinite matrices for $\hat x$ and $\hat p$.

Yet every physical prediction — energy levels, transition probabilities, measurement expectations — is identical across all three formulations. Paul Dirac realised that $\psi(x)$, $\tilde\psi(p)$, and $c_n$ are merely **coordinate representations** of a single underlying geometric entity, in precisely the same sense that the triplets $(v_x, v_y, v_z)$ and $(v_r, v_\theta, v_\phi)$ are coordinate representations of an intrinsic geometric arrow $\mathbf{v}$ in Euclidean 3-space. 

Dirac introduced the **ket vector**, denoted $|\alpha\rangle$, to represent the physical state itself, independent of any choice of coordinates or basis. The state space is a complex vector space $\mathcal{V}$, known when equipped with an inner product and completeness as a [[Hilbert Space]] $\mathcal{H}$.

```
                 Abstract State Vector: |α⟩ ∈ ℋ
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
  Position Basis        Momentum Basis           Number Basis
  {|x'⟩}                {|p'⟩}                  {|n⟩}
       │                       │                       │
       ▼                       ▼                       ▼
  ψ(x') = ⟨x'|α⟩        ψ̃(p') = ⟨p'|α⟩           c_n = ⟨n|α⟩
  Wavefunction          Fourier Transform       Discrete Sequence
  L²(ℝ) space           L²(ℝ) space             ℓ²(ℂ) space
```

### The vector space axioms and the null ket

The set of all state kets forms a vector space over the field of complex numbers $\mathbb{C}$. It satisfies eight basic axioms:
1. **Commutativity of addition:** $|\alpha\rangle + |\beta\rangle = |\beta\rangle + |\alpha\rangle$.
2. **Associativity of addition:** $(|\alpha\rangle + |\beta\rangle) + |\gamma\rangle = |\alpha\rangle + (|\beta\rangle + |\gamma\rangle)$.
3. **Existence of the null ket:** There exists a unique zero vector, the **null ket** $|{\rm null}\rangle \equiv 0$, such that $|\alpha\rangle + 0 = |\alpha\rangle$ for all $|\alpha\rangle$.
4. **Existence of additive inverse:** For every $|\alpha\rangle$, there exists a ket $-|\alpha\rangle$ such that $|\alpha\rangle + (-|\alpha\rangle) = 0$.
5. **Distributivity over ket addition:** $c(|\alpha\rangle + |\beta\rangle) = c|\alpha\rangle + c|\beta\rangle$ for any $c \in \mathbb{C}$.
6. **Distributivity over scalar addition:** $(c_1 + c_2)|\alpha\rangle = c_1|\alpha\rangle + c_2|\alpha\rangle$.
7. **Associativity of scalar multiplication:** $c_1(c_2|\alpha\rangle) = (c_1 c_2)|\alpha\rangle$.
8. **Unitary scalar:** $1|\alpha\rangle = |\alpha\rangle$.

> [!pitfall] The null ket is not a physical state
> The null ket $0$ represents the absence of a system; its norm is $\langle 0|0\rangle = 0$. Because the Born probability rule requires states to be normalised to unity ($\langle\alpha|\alpha\rangle = 1$), the null ket does not represent any physically realisable state. When we write an eigenvalue equation $\hat A|a'\rangle - a'|a'\rangle = 0$, the right-hand side is the null ket $0 \in \mathcal{H}$, meaning the equation is satisfied non-trivially.

### The superposition principle

The linearity of ket space encodes the **superposition principle**: if $|\alpha\rangle$ and $|\beta\rangle$ are physically realisable states of a system, any linear combination
$$|\psi\rangle = c_\alpha |\alpha\rangle + c_\beta |\beta\rangle \qquad (c_\alpha, c_\beta \in \mathbb{C})$$
is also a physically realisable state of the system, provided it is normalised.

### Observables and the eigenket equation

Physical quantities that can be measured (energy, position, linear momentum, angular momentum) are called **observables**. In the Dirac formalism, every observable $A$ is represented by a linear operator $\hat A$ acting on kets. 

When a physical measurement of $A$ on a state yields a single, sharp, reproducible value $a'$ with zero statistical uncertainty, the state is called an **eigenket** of $\hat A$, and $a'$ is its **eigenvalue**:
$$\boxed{\ \hat A|a'\rangle = a'|a'\rangle\ }$$
The set of all eigenvalues $\{a'\}$ is the **spectrum** of $\hat A$. The spectrum may be discrete (e.g. bound energy levels $E_n = (n+\frac{1}{2})\hbar\omega$ in [[QM05 The Harmonic Oscillator]]), continuous (e.g. position eigenvalues $x' \in (-\infty,\infty)$), or a combination of both (e.g. the hydrogen atom).

- **Position eigenket:** $\hat x|x'\rangle = x'|x'\rangle$. A state in which the particle is located definitively at $x=x'$.
- **Energy eigenket:** $\hat H|E_n\rangle = E_n|E_n\rangle$. A state with definite energy $E_n$ (a stationary state).
- **Momentum eigenket:** $\hat p|p'\rangle = p'|p'\rangle$. A state with definite linear momentum $p'$.

### Completeness as the bridge to measurement

The set of all eigenkets $\{|a'\rangle\}$ of a physical observable forms a complete set: any arbitrary physical state $|\alpha\rangle$ can be written as a linear superposition:
$$|\alpha\rangle = \sum_{a'} c_{a'} |a'\rangle \quad \text{(discrete)}, \qquad |\alpha\rangle = \int da'\, c(a')|a'\rangle \quad \text{(continuous)}.$$
This expansion is the foundation of quantum measurement: the complex coefficient $c_{a'}$ is the **probability amplitude** that a measurement of $A$ will yield the outcome $a'$.

![[fig_da_ket.png]]
*Figure DA.1. A: The abstract Hilbert space $\mathcal{H}$ viewed as a complex geometric space, showing the invariant state ket $|\alpha\rangle$ and three representative orthonormal coordinate bases: the discrete number basis $\{|n\rangle\}$, the continuous position basis $\{|x'\rangle\}$, and the continuous momentum basis $\{|p'\rangle\}$. B: The concrete realisations of $|\alpha\rangle$ across representations: in position space as a spatial wave function $\psi(x') = \langle x'|\alpha\rangle$, in momentum space as the Fourier transform $\tilde\psi(p') = \langle p'|\alpha\rangle$, and in number space as a sequence of discrete amplitudes $c_n = \langle n|\alpha\rangle$. C: The dual correspondence ("DC machine") mapping ket space $\mathcal{H}$ to bra space $\mathcal{H}^*$ through conjugate linearity.*

### Comparison: Dirac vs Wavefunction vs Matrix notation

| Concept | Dirac Notation | Wavefunction Representation | Matrix Mechanics (Discrete Basis) |
|---|---|---|---|
| **State** | Abstract ket $|\psi\rangle$ | Spatial wave function $\psi(x)$ | Column vector $\mathbf{c} = (c_1, c_2, \dots)^{\mathsf T}$ |
| **Dual State** | Abstract bra $\langle\psi|$ | Complex conjugate $\psi^*(x)$ | Conjugate transpose row $\mathbf{c}^\dagger = (c_1^*, c_2^*, \dots)$ |
| **Inner Product** | $\langle\phi|\psi\rangle$ | $\displaystyle\int_{-\infty}^\infty \phi^*(x)\psi(x)\,\mathrm dx$ | $\mathbf{b}^\dagger\mathbf{c} = \sum_n b_n^* c_n$ |
| **Observable** | Operator $\hat A$ | Differential operator (e.g. $-i\hbar\partial_x$) | Matrix $A_{mn} = \langle m|\hat A|n\rangle$ |
| **Eigenvalue Eq.** | $\hat A\|a'\rangle = a'\|a'\rangle$ | $\hat A(x)\psi_{a'}(x) = a'\psi_{a'}(x)$ | $\mathbf{A}\mathbf{v}_{a'} = a'\mathbf{v}_{a'}$ |
| **Completeness** | $\sum_n \|n\rangle\langle n\| = \hat 1$ | $\sum_n \psi_n(x)\psi_n^*(x') = \delta(x-x')$ | $\sum_n \mathbf{v}_n \mathbf{v}_n^\dagger = \mathbf{I}$ |
| **Expectation** | $\langle\hat A\rangle = \langle\psi\|\hat A\|\psi\rangle$ | $\displaystyle\int \psi^*(x)\hat A\psi(x)\,\mathrm dx$ | $\mathbf{c}^\dagger\mathbf{A}\mathbf{c}$ |

> [!example] Worked numerical example: Superposition in a two-level system
> Consider an orthonormal two-level basis $\{|1\rangle, |2\rangle\}$ with $\langle 1|1\rangle = \langle 2|2\rangle = 1$ and $\langle 1|2\rangle = 0$. Let a state be
> $$|\alpha\rangle = \frac{1}{\sqrt{3}}|1\rangle + \sqrt{\frac{2}{3}}e^{i\pi/4}|2\rangle.$$
> We verify normalisation:
> $$\langle\alpha|\alpha\rangle = \left(\frac{1}{\sqrt{3}}\langle 1| + \sqrt{\frac{2}{3}}e^{-i\pi/4}\langle 2|\right)\left(\frac{1}{\sqrt{3}}|1\rangle + \sqrt{\frac{2}{3}}e^{i\pi/4}|2\rangle\right) = \frac{1}{3}\langle 1|1\rangle + \frac{2}{3}e^{-i\pi/4}e^{i\pi/4}\langle 2|2\rangle = \frac{1}{3} + \frac{2}{3} = 1.000.$$
> If observable $\hat A$ has eigenkets $|1\rangle$ and $|2\rangle$ with eigenvalues $a_1 = +2.0$ and $a_2 = -1.0$:
> - The probability of measuring $a_1 = +2.0$ is $P(a_1) = |\langle 1|\alpha\rangle|^2 = |1/\sqrt{3}|^2 = 1/3 \approx 0.3333$.
> - The probability of measuring $a_2 = -1.0$ is $P(a_2) = |\langle 2|\alpha\rangle|^2 = |\sqrt{2/3}e^{i\pi/4}|^2 = 2/3 \approx 0.6667$.
> - The expectation value is $\langle\hat A\rangle = P(a_1)a_1 + P(a_2)a_2 = \frac{1}{3}(2.0) + \frac{2}{3}(-1.0) = 0.000$.

> [!extra-beyond]- Rigged Hilbert Spaces (Gel'fand Triplet)
> Strict Hilbert space $\mathcal{H} = L^2(\mathbb{R})$ contains only square-integrable functions: $\int |\psi|^2 dx < \infty$. Continuous eigenkets like position $|x'\rangle$ and momentum $|p'\rangle$ are normalised to Dirac delta functions ($\langle x'|x''\rangle = \delta(x'-x'')$), which have infinite $L^2$-norm and therefore do not strictly belong to $\mathcal{H}$. 
> Rigorous mathematical physics resolves this using a **Gel'fand triplet** (Rigged Hilbert Space):
> $$\Phi \subset \mathcal{H} \subset \Phi^*$$
> where $\Phi$ is the space of smooth, rapidly decreasing test functions (Schwartz space), $\mathcal{H}$ is the physical Hilbert space $L^2$, and $\Phi^*$ is the dual space of tempered distributions. Physical wave packets live in $\mathcal{H}$, while idealised eigenkets $|x'\rangle$ and $|p'\rangle$ live in the distribution space $\Phi^*$. Dirac algebra operates seamlessly across this triplet.

---

## 2. Bras, inner products, and the dual space

<span class="scope-extra-book">extra · book</span> *Sakurai §1.2–1.3 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.12–19]]); Shankar §1.2–1.4; Griffiths §3.2*

> [!intuition] The inner product as a shadow
> $\langle\alpha|\beta\rangle$ is the (complex) length of the shadow of $|\beta\rangle$ on $|\alpha\rangle$. The Schwarz inequality says a shadow cannot be longer than the arrow, with equality only when the two arrows are parallel: that is the *whole* content of $|\langle\alpha|\beta\rangle|^2\le\langle\alpha|\alpha\rangle\langle\beta|\beta\rangle$ and, later, of the uncertainty principle.

### The "DC Machine": Dual Correspondence

To every ket space $\mathcal{V}$, mathematicians associate a **dual space** $\mathcal{V}^*$, consisting of all continuous linear functionals that map kets to complex numbers: $f: \mathcal{V} \to \mathbb{C}$. Dirac denoted elements of the dual space as **bras**, written $\langle\alpha|$.

The relationship between kets and bras is established by a one-to-one mapping that Sakurai terms the **dual correspondence (DC)**:
$$|\alpha\rangle \quad\overset{\text{DC}}{\longleftrightarrow}\quad \langle\alpha|.$$

The fundamental property of the DC machine is that it is **conjugate-linear** (antilinear):
$$\boxed{\ c_1|\alpha\rangle + c_2|\beta\rangle \quad\overset{\text{DC}}{\longleftrightarrow}\quad c_1^*\langle\alpha| + c_2^*\langle\beta|\ }$$
In matrix mechanics, if a ket is represented by a column vector $\mathbf{v}$, the dual bra is represented by the conjugate-transpose (Hermitian conjugate) row vector $\mathbf{v}^\dagger$:
$$|\alpha\rangle \doteq \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} \quad\implies\quad \langle\alpha| \doteq \begin{pmatrix} c_1^* & c_2^* \end{pmatrix}.$$

### Axioms of the inner product

When a bra $\langle\beta|$ meets a ket $|\alpha\rangle$, they form a closed "bra-c-ket", or **inner product**, denoted $\langle\beta|\alpha\rangle \in \mathbb{C}$. The inner product satisfies:

> [!key] Inner-product axioms
> 1. **Conjugate symmetry:** $\langle\beta|\alpha\rangle = \langle\alpha|\beta\rangle^*$.
> 2. **Linearity in the ket:** $\langle\gamma|\big(c_1|\alpha\rangle + c_2|\beta\rangle\big) = c_1\langle\gamma|\alpha\rangle + c_2\langle\gamma|\beta\rangle$.
> 3. **Conjugate-linearity in the bra:** $\big(c_1\langle\alpha| + c_2\langle\beta|\big)|\gamma\rangle = c_1^*\langle\alpha|\gamma\rangle + c_2^*\langle\beta|\gamma\rangle$.
> 4. **Positive definiteness:** $\langle\alpha|\alpha\rangle \ge 0$ for all $|\alpha\rangle$, with $\langle\alpha|\alpha\rangle = 0$ if and only if $|\alpha\rangle = 0$ (the null ket).

The norm of a ket is defined as the non-negative real root:
$$\||\alpha\rangle\| \equiv \sqrt{\langle\alpha|\alpha\rangle}.$$
A state is **normalised** when $\||\alpha\rangle\| = 1$, i.e. $\langle\alpha|\alpha\rangle = 1$.

### The Cauchy–Schwarz inequality

The Cauchy–Schwarz inequality is the single most important inequality in quantum foundations; it governs all quantum uncertainty relations.

> [!derivation] Full proof of the Schwarz inequality
> For any two kets $|\alpha\rangle$ and $|\beta\rangle$, consider the auxiliary ket $|\gamma\rangle$ constructed by subtracting from $|\alpha\rangle$ its projection along $|\beta\rangle$:
> $$|\gamma\rangle \equiv |\alpha\rangle - \frac{\langle\beta|\alpha\rangle}{\langle\beta|\beta\rangle}|\beta\rangle \qquad (\text{assuming } |\beta\rangle \ne 0).$$
> By Axiom 4 (positive definiteness), the norm of $|\gamma\rangle$ must be non-negative: $\langle\gamma|\gamma\rangle \ge 0$.
> 
> Let us write down the dual bra $\langle\gamma|$ using the conjugate-linear rules of the DC machine:
> $$\langle\gamma| = \langle\alpha| - \left(\frac{\langle\beta|\alpha\rangle}{\langle\beta|\beta\rangle}\right)^*\langle\beta| = \langle\alpha| - \frac{\langle\alpha|\beta\rangle}{\langle\beta|\beta\rangle}\langle\beta|.$$
> Now we expand the inner product $\langle\gamma|\gamma\rangle$:
> $$\begin{aligned}
> \langle\gamma|\gamma\rangle &= \left(\langle\alpha| - \frac{\langle\alpha|\beta\rangle}{\langle\beta|\beta\rangle}\langle\beta|\right)\left(|\alpha\rangle - \frac{\langle\beta|\alpha\rangle}{\langle\beta|\beta\rangle}|\beta\rangle\right) \\
> &= \langle\alpha|\alpha\rangle - \frac{\langle\beta|\alpha\rangle}{\langle\beta|\beta\rangle}\langle\alpha|\beta\rangle - \frac{\langle\alpha|\beta\rangle}{\langle\beta|\beta\rangle}\langle\beta|\alpha\rangle + \frac{\langle\alpha|\beta\rangle\langle\beta|\alpha\rangle}{\langle\beta|\beta\rangle^2}\langle\beta|\beta\rangle \\
> &= \langle\alpha|\alpha\rangle - \frac{|\langle\alpha|\beta\rangle|^2}{\langle\beta|\beta\rangle} - \frac{|\langle\alpha|\beta\rangle|^2}{\langle\beta|\beta\rangle} + \frac{|\langle\alpha|\beta\rangle|^2}{\langle\beta|\beta\rangle} \\
> &= \langle\alpha|\alpha\rangle - \frac{|\langle\alpha|\beta\rangle|^2}{\langle\beta|\beta\rangle} \ge 0.
> \end{aligned}$$
> Multiplying both sides by the positive scalar $\langle\beta|\beta\rangle > 0$:
> $$\langle\alpha|\alpha\rangle\langle\beta|\beta\rangle - |\langle\alpha|\beta\rangle|^2 \ge 0 \implies \boxed{\ |\langle\alpha|\beta\rangle|^2 \le \langle\alpha|\alpha\rangle\langle\beta|\beta\rangle\ }$$
> Equality holds if and only if $\langle\gamma|\gamma\rangle = 0$, which by Axiom 4 implies $|\gamma\rangle = 0$. From our definition of $|\gamma\rangle$, this requires $|\alpha\rangle = c|\beta\rangle$ for some complex constant $c$. That is, **equality holds if and only if $|\alpha\rangle$ and $|\beta\rangle$ are linearly dependent**. $\square$

### Orthonormality: discrete vs continuous

Two kets $|\alpha\rangle$ and $|\beta\rangle$ are **orthogonal** if their inner product vanishes: $\langle\alpha|\beta\rangle = 0$. A set of kets $\{|a_n\rangle\}$ is **orthonormal** if every ket is normalised and all pairs are mutually orthogonal:

1. **Discrete basis:**
   $$\langle a_m|a_n\rangle = \delta_{mn} = \begin{cases} 1 & \text{if } m = n, \\ 0 & \text{if } m \ne n. \end{cases}$$
   For the harmonic oscillator number basis $|n\rangle$ ([[QM05 The Harmonic Oscillator]], [[QM06 The Oscillator Toolbox]]):
   $$\langle m|n\rangle = \delta_{mn}.$$

2. **Continuous basis:**
   Eigenkets of continuous observables cannot be unit-normalised; they are **delta-function normalised**:
   $$\langle x'|x''\rangle = \delta(x'-x''), \qquad \langle p'|p''\rangle = \delta(p'-p'').$$

### Normalisation and phase: global vs relative

Let $|\psi\rangle$ be a physical state. Multiplying $|\psi\rangle$ by an overall complex phase factor $e^{i\theta}$ ($\theta \in \mathbb{R}$) produces a new ket $|\psi'\rangle = e^{i\theta}|\psi\rangle$.
The inner product with any state $|\phi\rangle$ transforms as:
$$|\langle\phi|\psi'\rangle|^2 = |\langle\phi|e^{i\theta}|\psi\rangle|^2 = |e^{i\theta}\langle\phi|\psi\rangle|^2 = |\langle\phi|\psi\rangle|^2.$$
Because all physical observables and probabilities depend solely on absolute squares of inner products, **the global phase $e^{i\theta}$ is physically unobservable**: $|\psi\rangle$ and $e^{i\theta}|\psi\rangle$ represent the identical physical state.

> [!pitfall] Relative phase produces real physical interference
> While global phase is unobservable, **relative phase between components in a superposition is directly measurable**. 
> Consider two states $|\psi_A\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle)$ and $|\psi_B\rangle = \frac{1}{\sqrt{2}}(|1\rangle + e^{i\pi}|2\rangle) = \frac{1}{\sqrt{2}}(|1\rangle - |2\rangle)$.
> Their overlap with an interrogation state $|+\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle)$ yields:
> - For $|\psi_A\rangle$: $|\langle +|\psi_A\rangle|^2 = |1|^2 = 1.000$ (constructive interference).
> - For $|\psi_B\rangle$: $|\langle +|\psi_B\rangle|^2 = |\frac{1}{2}(1 - 1)|^2 = 0.000$ (destructive interference).
> Changing the relative phase shifts physical interference fringes!

> [!example] Worked numerical example: Checking the Schwarz inequality
> Let $|\alpha\rangle = \begin{pmatrix} 2 \\ 1+i \end{pmatrix}$ and $|\beta\rangle = \begin{pmatrix} 3i \\ 4 \end{pmatrix}$.
> 1. $\langle\alpha|\alpha\rangle = |2|^2 + |1+i|^2 = 4 + (1^2 + 1^2) = 6.000$.
> 2. $\langle\beta|\beta\rangle = |3i|^2 + |4|^2 = 9 + 16 = 25.000$.
> 3. Product of norms: $\langle\alpha|\alpha\rangle\langle\beta|\beta\rangle = 6 \times 25 = 150.000$.
> 4. Overlap inner product:
>    $$\langle\alpha|\beta\rangle = (2)^*(3i) + (1+i)^*(4) = 2(3i) + (1-i)(4) = 6i + 4 - 4i = 4 + 2i.$$
> 5. Absolute square: $|\langle\alpha|\beta\rangle|^2 = |4+2i|^2 = 4^2 + 2^2 = 16 + 4 = 20.000$.
> 
> We test the inequality:
> $$|\langle\alpha|\beta\rangle|^2 = 20.000 \le 150.000 = \langle\alpha|\alpha\rangle\langle\beta|\beta\rangle \quad \checkmark$$
> The ratio is $\frac{20}{150} = \frac{2}{15} \approx 0.1333 \ll 1$, showing that $|\alpha\rangle$ and $|\beta\rangle$ are far from parallel.

---

## 3. Operators, outer products, and the identity

<span class="scope-extra-book">extra · book</span> *Sakurai §1.3 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.19–26]]); Griffiths §3.2–3.3; Shankar §1.3; Dirac Ch. 1*

> [!intuition] $|\beta\rangle\langle\alpha|$ is the atom of all operators
> It reads out the $\alpha$-component of whatever you feed it and re-emits that amount along $|\beta\rangle$. Every operator is a sum of such atoms, $X=\sum_{a'',a'}|a''\rangle X_{a''a'}\langle a'|$, which is exactly what a matrix is. The projector $P_n=|n\rangle\langle n|$ is the atom with $\beta=\alpha$: *keep only the $n$-th component*.

### Linear operators

A **linear operator** $\hat X$ is a mapping from ket space to ket space, $|\alpha\rangle \mapsto \hat X|\alpha\rangle$, preserving linear combinations:
$$\hat X\big(c_1|\alpha\rangle + c_2|\beta\rangle\big) = c_1 \hat X|\alpha\rangle + c_2 \hat X|\beta\rangle.$$
Operators act on bras from the right: $\langle\alpha|\hat X$. In general, $\hat A\hat B \ne \hat B\hat A$: quantum operators form a non-commutative algebra.

### The outer product dyad as an operator

Let $|\beta\rangle$ and $|\alpha\rangle$ be two arbitrary kets. The juxtaposition
$$\hat O \equiv |\beta\rangle\langle\alpha|$$
is an **outer product** (or dyad). It acts on any test ket $|\gamma\rangle$ via associativity of the inner product:
$$\hat O |\gamma\rangle = \big(|\beta\rangle\langle\alpha|\big)|\gamma\rangle = |\beta\rangle\big(\langle\alpha|\gamma\rangle\big) = \big(\langle\alpha|\gamma\rangle\big)|\beta\rangle.$$
Because $\langle\alpha|\gamma\rangle$ is a complex scalar, the outer product takes in a ket $|\gamma\rangle$, calculates its scalar projection onto $|\alpha\rangle$, and outputs a ket pointing along the direction of $|\beta\rangle$. In matrix notation, if $|\beta\rangle$ is an $N\times 1$ column and $\langle\alpha|$ is a $1\times N$ row, $|\beta\rangle\langle\alpha|$ is an $N\times N$ matrix of **rank 1**.

### The resolution of the identity

If $\{|a'\rangle\}$ is a complete orthonormal discrete basis, summing the diagonal dyads $|a'\rangle\langle a'|$ yields the **identity operator**:
$$\boxed{\ \hat 1 = \sum_{a'} |a'\rangle\langle a'|\ }$$
For a continuous basis, the sum becomes an integral:
$$\boxed{\ \hat 1 = \int dx'\, |x'\rangle\langle x'| = \int dp'\, |p'\rangle\langle p'|\ }$$
This relation, known as the **completeness relation** or **resolution of the identity**, is the single most powerful algebraic tool in quantum mechanics. Whenever an expression is difficult to evaluate, **insert $\hat 1$**:
$$\langle\beta|\alpha\rangle = \langle\beta|\hat 1|\alpha\rangle = \sum_{a'} \langle\beta|a'\rangle\langle a'|\alpha\rangle.$$
This expresses an inner product as a sum over intermediate transition amplitudes.

![[fig_da_representations.png]]
*Figure DA.2. A: The outer product dyad $|\beta\rangle\langle\alpha|$ acting as a directed mapping: it swallows an input ket $|\gamma\rangle$, projects it onto $\langle\alpha|$ to produce the scalar amplitude $\langle\alpha|\gamma\rangle$, and ejects a state proportional to $|\beta\rangle$. B: Matrix anatomy of the dyad $|\beta\rangle\langle\alpha|$ in a discrete basis, showing how a column vector multiplied by a row vector builds an $N\times N$ matrix of rank 1. C: The completeness relation $\hat 1 = \sum_n |n\rangle\langle n|$ as a decomposition of the identity operator into mutually orthogonal projection operators $\hat P_n$.*

### The commutator algebra

The **commutator** of two operators $\hat A$ and $\hat B$ is defined as
$$[\hat A, \hat B] \equiv \hat A\hat B - \hat B\hat A.$$
Key algebraic identities (readily verified by direct expansion):
1. **Antisymmetry:** $[\hat A, \hat B] = -[\hat B, \hat A]$.
2. **Linearity:** $[\hat A, c_1\hat B + c_2\hat C] = c_1[\hat A, \hat B] + c_2[\hat A, \hat C]$.
3. **Leibniz product rule (derivation property):**
   $$\boxed{\ [\hat A, \hat B\hat C] = [\hat A, \hat B]\hat C + \hat B[\hat A, \hat C]\ }$$
   $$\boxed{\ [\hat A\hat B, \hat C] = \hat A[\hat B, \hat C] + [\hat A, \hat C]\hat B\ }$$
4. **Jacobi identity:** $[\hat A, [\hat B, \hat C]] + [\hat B, [\hat C, \hat A]] + [\hat C, [\hat A, \hat B]] = 0$.

### Matrix elements and the harmonic oscillator

The matrix elements of an operator $\hat X$ in a discrete orthonormal basis $\{|n\rangle\}$ are defined by
$$X_{mn} \equiv \langle m|\hat X|n\rangle.$$
From [[QM05 The Harmonic Oscillator]] and [[QM06 The Oscillator Toolbox]], the ladder operators act as:
$$\hat a|n\rangle = \sqrt{n}|n-1\rangle, \qquad \hat a^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle.$$
In the number basis $\{|0\rangle, |1\rangle, |2\rangle, \dots\}$, their explicit matrix representations are:
$$\hat a \doteq \begin{pmatrix} 0 & \sqrt{1} & 0 & 0 & \dots \\ 0 & 0 & \sqrt{2} & 0 & \dots \\ 0 & 0 & 0 & \sqrt{3} & \dots \\ 0 & 0 & 0 & 0 & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}, \qquad \hat a^\dagger \doteq \begin{pmatrix} 0 & 0 & 0 & 0 & \dots \\ \sqrt{1} & 0 & 0 & 0 & \dots \\ 0 & \sqrt{2} & 0 & 0 & \dots \\ 0 & 0 & \sqrt{3} & 0 & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}.$$
Since $\hat x = \sqrt{\frac{\hbar}{2m\omega}}(\hat a + \hat a^\dagger)$ and $\hat p = i\sqrt{\frac{m\hbar\omega}{2}}(\hat a^\dagger - \hat a)$, position and momentum are tridiagonal matrices with zero diagonal entries:
$$\hat x \doteq \sqrt{\frac{\hbar}{2m\omega}}\begin{pmatrix} 0 & 1 & 0 & 0 & \dots \\ 1 & 0 & \sqrt{2} & 0 & \dots \\ 0 & \sqrt{2} & 0 & \sqrt{3} & \dots \\ 0 & 0 & \sqrt{3} & 0 & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}, \qquad \hat p \doteq i\sqrt{\frac{m\hbar\omega}{2}}\begin{pmatrix} 0 & -1 & 0 & 0 & \dots \\ 1 & 0 & -\sqrt{2} & 0 & \dots \\ 0 & \sqrt{2} & 0 & -\sqrt{3} & \dots \\ 0 & 0 & \sqrt{3} & 0 & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}.$$

### Projection operators

An operator $\hat P_n$ that projects onto a single basis ket $|n\rangle$ is defined by:
$$\hat P_n \equiv |n\rangle\langle n|.$$
Its fundamental properties:
1. **Idempotence:** $\hat P_n^2 = (|n\rangle\langle n|)(|n\rangle\langle n|) = |n\rangle(\langle n|n\rangle)\langle n| = |n\rangle(1)\langle n| = \hat P_n$.
2. **Mutual orthogonality:** $\hat P_m \hat P_n = |m\rangle\langle m|n\rangle\langle n| = |m\rangle(0)\langle n| = 0$ for $m \ne n$.
3. **Completeness:** $\sum_n \hat P_n = \hat 1$.
4. **Hermiticity:** $\hat P_n^\dagger = (|n\rangle\langle n|)^\dagger = |n\rangle\langle n| = \hat P_n$.

> [!example] Worked numerical example: Projecting a state
> Consider the state $|\alpha\rangle = \sqrt{0.36}|1\rangle + \sqrt{0.64}|2\rangle = 0.6|1\rangle + 0.8|2\rangle$.
> Let $\hat P_1 = |1\rangle\langle 1|$.
> Acting with $\hat P_1$ on $|\alpha\rangle$:
> $$\hat P_1|\alpha\rangle = |1\rangle\langle 1|(0.6|1\rangle + 0.8|2\rangle) = |1\rangle(0.6\langle 1|1\rangle + 0.8\langle 1|2\rangle) = 0.6|1\rangle.$$
> The probability of the state being in $|1\rangle$ is the norm squared of the projected ket:
> $$P(1) = \|\hat P_1|\alpha\rangle\|^2 = \langle\alpha|\hat P_1^\dagger\hat P_1|\alpha\rangle = \langle\alpha|\hat P_1|\alpha\rangle = (0.6)^2 = 0.360.$$
> The normalised post-measurement state is:
> $$|\alpha_{\text{after}}\rangle = \frac{\hat P_1|\alpha\rangle}{\|\hat P_1|\alpha\rangle\|} = \frac{0.6|1\rangle}{0.6} = |1\rangle.$$

---

## 4. The adjoint and Hermitian operators

<span class="scope-extra-book">extra · book</span> *Sakurai §1.3 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.26–32]]); Griffiths §3.2; Shankar §1.4; Dirac Ch. 2*

> [!intuition] Why observables must be Hermitian
> A measuring stick must give real numbers and its readings for different outcomes must not overlap. Both are exactly the two theorems proved here: real eigenvalues and orthogonal eigenkets. Geometrically a Hermitian operator stretches (or flips) a set of perpendicular axes by real factors, and nothing else. A non-Hermitian operator such as the ladder $\hat a$ also rotates and shears; that is why it can *move* between eigenstates and cannot be *measured*.

### Definition of the adjoint (Hermitian conjugate)

Let $\hat X$ be a linear operator. If $|\alpha\rangle \mapsto \hat X|\alpha\rangle$, what is the dual bra of $\hat X|\alpha\rangle$?
By the DC machine, the dual bra is denoted $\langle\alpha|\hat X^\dagger$, where $\hat X^\dagger$ is the **adjoint** (or **Hermitian conjugate**) of $\hat X$.

Formally, $\hat X^\dagger$ is defined by the requirement that for *all* kets $|\alpha\rangle$ and $|\gamma\rangle$:
$$\boxed{\ \langle\gamma|\hat X|\alpha\rangle^* = \langle\alpha|\hat X^\dagger|\gamma\rangle\ }$$
In terms of matrix elements, taking the adjoint corresponds to **transposing and complex conjugating**:
$$(X^\dagger)_{mn} = \langle m|\hat X^\dagger|n\rangle = \langle n|\hat X|m\rangle^* = X_{nm}^*.$$

### Computational rules for the adjoint

> [!derivation] Proof of algebraic properties of the adjoint
> 1. **Scalar multiplication:** $(c\hat X)^\dagger = c^*\hat X^\dagger$.
>    Proof: $\langle\gamma|c\hat X|\alpha\rangle^* = (c\langle\gamma|\hat X|\alpha\rangle)^* = c^*\langle\gamma|\hat X|\alpha\rangle^* = c^*\langle\alpha|\hat X^\dagger|\gamma\rangle = \langle\alpha|(c^*\hat X^\dagger)|\gamma\rangle$. $\square$
> 2. **Operator products reverse order:** $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger$.
>    Proof: Let $|\phi\rangle = \hat B|\alpha\rangle$. Then $\langle\gamma|\hat A\hat B|\alpha\rangle = \langle\gamma|\hat A|\phi\rangle$. Taking the complex conjugate:
>    $$\langle\gamma|\hat A|\phi\rangle^* = \langle\phi|\hat A^\dagger|\gamma\rangle.$$
>    Now let $\langle\psi| = \langle\gamma|\hat A$, so $|\psi\rangle = \hat A^\dagger|\gamma\rangle$. Then:
>    $$\langle\phi|\psi\rangle^* = \langle\psi|\phi\rangle = \langle\psi|\hat B|\alpha\rangle \implies \langle\phi|\psi\rangle = \langle\alpha|\hat B^\dagger|\psi\rangle = \langle\alpha|\hat B^\dagger\hat A^\dagger|\gamma\rangle.$$
>    Comparing with the definition $\langle\gamma|(\hat A\hat B)|\alpha\rangle^* = \langle\alpha|(\hat A\hat B)^\dagger|\gamma\rangle$, we conclude $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger$. $\square$
> 3. **Outer product:** $(|\beta\rangle\langle\alpha|)^\dagger = |\alpha\rangle\langle\beta|$.
>    Proof: For arbitrary $|\gamma\rangle, |\delta\rangle$:
>    $$\langle\gamma|(|\beta\rangle\langle\alpha|)|\delta\rangle^* = \big(\langle\gamma|\beta\rangle\langle\alpha|\delta\rangle\big)^* = \langle\beta|\gamma\rangle\langle\delta|\alpha\rangle = \langle\delta|\alpha\rangle\langle\beta|\gamma\rangle = \langle\delta|(|\alpha\rangle\langle\beta|)|\gamma\rangle.$$
>    Hence $(|\beta\rangle\langle\alpha|)^\dagger = |\alpha\rangle\langle\beta|$. $\square$

### Hermitian (self-adjoint) operators

An operator $\hat A$ is **Hermitian** (or self-adjoint) if it equals its own adjoint:
$$\boxed{\ \hat A^\dagger = \hat A\ }$$
Equivalently, for all states $|\alpha\rangle, |\beta\rangle$:
$$\langle\beta|\hat A|\alpha\rangle^* = \langle\alpha|\hat A|\beta\rangle.$$
Taking $|\beta\rangle = |\alpha\rangle$, we obtain $\langle\alpha|\hat A|\alpha\rangle^* = \langle\alpha|\hat A|\alpha\rangle$.
Therefore, **the expectation value of a Hermitian operator in any physical state is strictly real**:
$$\langle\hat A\rangle \in \mathbb{R}.$$
This is why all physical observables are required to be Hermitian operators.

### Proof 1: Eigenvalues of a Hermitian operator are real

> [!derivation] Proof: Real eigenvalues
> Let $\hat A$ be a Hermitian operator ($\hat A^\dagger = \hat A$), and let $|a'\rangle$ be an eigenket with eigenvalue $a'$:
> $$\hat A|a'\rangle = a'|a'\rangle.$$
> Take the inner product of both sides with the bra $\langle a'|$:
> $$\langle a'|\hat A|a'\rangle = a'\langle a'|a'\rangle. \tag{1}$$
> Now take the complex conjugate of equation (1):
> $$\langle a'|\hat A|a'\rangle^* = (a')^*\langle a'|a'\rangle^* = (a')^*\langle a'|a'\rangle. \tag{2}$$
> By the definition of the adjoint, the left-hand side of (2) is:
> $$\langle a'|\hat A|a'\rangle^* = \langle a'|\hat A^\dagger|a'\rangle.$$
> Because $\hat A$ is Hermitian ($\hat A^\dagger = \hat A$), this becomes:
> $$\langle a'|\hat A|a'\rangle = (a')^*\langle a'|a'\rangle. \tag{3}$$
> Subtracting equation (3) from equation (1):
> $$\big(a' - (a')^*\big)\langle a'|a'\rangle = 0.$$
> Since $|a'\rangle$ is an eigenket, it is not the null ket, so $\langle a'|a'\rangle > 0$. Therefore:
> $$a' - (a')^* = 0 \implies \boxed{\ a' = (a')^*\ }$$
> Every eigenvalue of a Hermitian operator is **strictly real**. $\square$

### Proof 2: Eigenstates with different eigenvalues are orthogonal

> [!derivation] Proof: Orthogonality of distinct eigenstates
> Let $|a'\rangle$ and $|a''\rangle$ be two eigenkets of the Hermitian operator $\hat A$, with eigenvalues $a'$ and $a''$:
> $$\hat A|a'\rangle = a'|a'\rangle, \qquad \hat A|a''\rangle = a''|a''\rangle.$$
> Multiply the first equation from the left by $\langle a''|$:
> $$\langle a''|\hat A|a'\rangle = a'\langle a''|a'\rangle. \tag{4}$$
> Now apply the DC machine to the second eigenvalue equation. Since $a''$ is real ($a''^* = a''$ by Proof 1) and $\hat A^\dagger = \hat A$:
> $$\langle a''|\hat A^\dagger = a''^*\langle a''| \implies \langle a''|\hat A = a''\langle a''|.$$
> Multiply this equation from the right by $|a'\rangle$:
> $$\langle a''|\hat A|a'\rangle = a''\langle a''|a'\rangle. \tag{5}$$
> Subtracting equation (5) from equation (4):
> $$\boxed{\ (a' - a'')\langle a''|a'\rangle = 0\ }$$
> If the eigenvalues are distinct ($a' \ne a''$), we can divide by $(a' - a'') \ne 0$, forcing:
> $$\boxed{\ \langle a''|a'\rangle = 0\ }$$
> Eigenstates corresponding to different eigenvalues of a Hermitian operator are **strictly orthogonal**. $\square$

### Examples of Hermitian and non-Hermitian operators

- **Hermitian observables:**
  - Position $\hat x$: $\langle\beta|\hat x|\alpha\rangle = \int \phi^* x \psi dx = (\int \psi^* x \phi dx)^* = \langle\alpha|\hat x|\beta\rangle^*$.
  - Momentum $\hat p$: Integration by parts transfers $-i\hbar\partial_x$ with a sign flip that cancels $(-i)^* = +i$.
  - Hamiltonian $\hat H = \frac{\hat p^2}{2m} + V(\hat x)$.
  - Parity $\hat\Pi$: $\langle\beta|\hat\Pi|\alpha\rangle = \int \phi^*(x)\psi(-x)dx = \int \phi^*(-u)\psi(u)du = \langle\alpha|\hat\Pi|\beta\rangle^*$.
  - Pauli spin matrices $\sigma_x = \begin{pmatrix} 0&1\\1&0 \end{pmatrix}, \sigma_y = \begin{pmatrix} 0&-i\\i&0 \end{pmatrix}, \sigma_z = \begin{pmatrix} 1&0\\0&-1 \end{pmatrix}$.

- **Non-Hermitian operators:**
  - Harmonic oscillator ladder lowering operator $\hat a$: $(\hat a)^\dagger = \hat a^\dagger \ne \hat a$.
  - Its expectation value can be complex: in a coherent state $|\alpha_{\text{coh}}\rangle$, $\langle\hat a\rangle = \alpha_{\text{coh}} \in \mathbb{C}$. Ladder operators are mathematical stepping tools, not physical observables!

> [!example] Worked numerical example: Diagonalising a $2\times 2$ Hermitian matrix
> Consider the Hermitian operator $\hat M$ represented in an orthonormal basis $\{|1\rangle, |2\rangle\}$ by:
> $$\hat M \doteq \begin{pmatrix} 2 & 1-i \\ 1+i & 3 \end{pmatrix}.$$
> Check Hermiticity: $\hat M^\dagger = \begin{pmatrix} 2^* & (1+i)^* \\ (1-i)^* & 3^* \end{pmatrix} = \begin{pmatrix} 2 & 1-i \\ 1+i & 3 \end{pmatrix} = \hat M$.
> 1. **Characteristic polynomial:**
>    $$\det(\hat M - \lambda\hat 1) = (2-\lambda)(3-\lambda) - (1-i)(1+i) = (\lambda^2 - 5\lambda + 6) - (1 - (-1)) = \lambda^2 - 5\lambda + 4 = 0.$$
> 2. **Eigenvalues:**
>    $$(\lambda - 1)(\lambda - 4) = 0 \implies \lambda_1 = 1.000, \quad \lambda_2 = 4.000.$$
>    Both eigenvalues are strictly real, verifying Proof 1.
> 3. **Eigenvectors:**
>    - For $\lambda_1 = 1$: $\begin{pmatrix} 2-1 & 1-i \\ 1+i & 3-1 \end{pmatrix}\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = \begin{pmatrix} 1 & 1-i \\ 1+i & 2 \end{pmatrix}\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = 0 \implies u_1 + (1-i)u_2 = 0$.
>      Choose $u_2 = 1 \implies u_1 = -(1-i) = -1+i$. Normalising: $\|u\|^2 = |-1+i|^2 + 1^2 = 2 + 1 = 3$.
>      $$|v_1\rangle = \frac{1}{\sqrt{3}}\begin{pmatrix} -1+i \\ 1 \end{pmatrix}.$$
>    - For $\lambda_2 = 4$: $\begin{pmatrix} 2-4 & 1-i \\ 1+i & 3-4 \end{pmatrix}\begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} -2 & 1-i \\ 1+i & -1 \end{pmatrix}\begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = 0 \implies (1+i)w_1 - w_2 = 0$.
>      Choose $w_1 = 1 \implies w_2 = 1+i$. Normalising: $\|w\|^2 = 1^2 + |1+i|^2 = 1 + 2 = 3$.
>      $$|v_2\rangle = \frac{1}{\sqrt{3}}\begin{pmatrix} 1 \\ 1+i \end{pmatrix}.$$
> 4. **Check orthogonality (Proof 2):**
>    $$\langle v_1|v_2\rangle = \frac{1}{3}\Big((-1+i)^*(1) + (1)^*(1+i)\Big) = \frac{1}{3}\Big((-1-i) + (1+i)\Big) = \frac{1}{3}(0) = 0.000 \quad \checkmark$$

---

## 5. Completeness, matrix representations, and change of basis

<span class="scope-extra-book">extra · book</span> *Sakurai §1.3–1.4 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.19–26, 33–42]]); Griffiths §3.3–3.4; Shankar §1.5–1.8*

> [!intuition] Change of basis = rotating your ruler
> A unitary $U_{b'a'}=\langle b'|a'\rangle$ is the table of the new axes' shadows on the old. The state does not change; its list of numbers does. Operators change as $X\to UXU^\dagger$ so that every physical number $\langle\beta|X|\alpha\rangle$ stays the same. Diagonalising an operator is just choosing the rotation in which it is a pure stretch.

### Expanding states in a complete basis

Let $\{|a'\rangle\}$ be the complete orthonormal eigenbasis of an observable $\hat A$. Inserting the identity operator $\hat 1 = \sum_{a'}|a'\rangle\langle a'|$ decomposes any state $|\alpha\rangle$:
$$|\alpha\rangle = \hat 1|\alpha\rangle = \sum_{a'} |a'\rangle\langle a'|\alpha\rangle = \sum_{a'} c_{a'} |a'\rangle,$$
where the complex coefficient
$$\boxed{\ c_{a'} = \langle a'|\alpha\rangle\ }$$
is the projection of $|\alpha\rangle$ onto basis ket $|a'\rangle$.
The inner product of two states $|\alpha\rangle$ and $|\beta\rangle$ becomes:
$$\langle\beta|\alpha\rangle = \langle\beta|\hat 1|\alpha\rangle = \sum_{a'} \langle\beta|a'\rangle\langle a'|\alpha\rangle = \sum_{a'} b_{a'}^* c_{a'}.$$
For $|\beta\rangle = |\alpha\rangle$, the normalisation requirement $\langle\alpha|\alpha\rangle = 1$ gives:
$$\sum_{a'} |c_{a'}|^2 = 1.$$
By the Born rule, $|c_{a'}|^2$ is the probability $P(a')$ of obtaining eigenvalue $a'$ upon measuring $A$.

### Matrix representation of operators

Inserting the resolution of the identity twice, on the left and right of an operator $\hat X$:
$$\hat X = \hat 1 \hat X \hat 1 = \left(\sum_{a''}|a''\rangle\langle a''|\right) \hat X \left(\sum_{a'}|a'\rangle\langle a'|\right) = \sum_{a''}\sum_{a'} |a''\rangle \langle a''|\hat X|a'\rangle \langle a'|.$$
The numbers
$$\boxed{\ X_{a''a'} \equiv \langle a''|\hat X|a'\rangle\ }$$
are the **matrix elements** of $\hat X$ in the $\{|a'\rangle\}$ basis. Here $a''$ indexes the **row** and $a'$ indexes the **column**.

Operator multiplication becomes standard matrix multiplication:
$$\langle a''|\hat X\hat Y|a'\rangle = \langle a''|\hat X \hat 1 \hat Y|a'\rangle = \sum_{a'''} \langle a''|\hat X|a'''\rangle\langle a'''|\hat Y|a'\rangle = \sum_{a'''} X_{a''a'''} Y_{a'''a'}.$$

### Change of basis and unitary transformations

Suppose we have two complete orthonormal bases: the old basis $\{|a'\rangle\}$ and a new basis $\{|b'\rangle\}$.
How do state coefficients and operator matrices transform between them?

Define the **transformation operator** $\hat U$:
$$\hat U \equiv \sum_k |b_k\rangle\langle a_k|.$$
Its matrix elements are $U_{ba} \equiv \langle b|a\rangle$.
Let us check the unitarity of $\hat U$:
$$\hat U^\dagger \hat U = \left(\sum_k |a_k\rangle\langle b_k|\right)\left(\sum_j |b_j\rangle\langle a_j|\right) = \sum_{k,j} |a_k\rangle \underbrace{\langle b_k|b_j\rangle}_{\delta_{kj}} \langle a_j| = \sum_k |a_k\rangle\langle a_k| = \hat 1.$$
Similarly $\hat U\hat U^\dagger = \hat 1$. Thus, **the transformation matrix connecting any two orthonormal bases is strictly unitary**:
$$\hat U^\dagger = \hat U^{-1}.$$

> [!derivation] Transformation of operator matrix elements
> Let an operator have matrix elements $X^{(a)}_{a''a'} = \langle a''|\hat X|a'\rangle$ in the $\{|a'\rangle\}$ basis.
> In the new $\{|b'\rangle\}$ basis, its matrix elements are:
> $$X^{(b)}_{b''b'} = \langle b''|\hat X|b'\rangle.$$
> Insert the completeness relation for the $\{|a'\rangle\}$ basis twice:
> $$\begin{aligned}
> X^{(b)}_{b''b'} &= \langle b''|\left(\sum_{a''}|a''\rangle\langle a''|\right)\hat X\left(\sum_{a'}|a'\rangle\langle a'|\right)|b'\rangle \\
> &= \sum_{a'',a'} \langle b''|a''\rangle \langle a''|\hat X|a'\rangle \langle a'|b'\rangle \\
> &= \sum_{a'',a'} U_{b''a''} X^{(a)}_{a''a'} (U^\dagger)_{a'b'}.
> \end{aligned}$$
> In compact matrix notation:
> $$\boxed{\ \mathbf{X}^{(b)} = \mathbf{U} \mathbf{X}^{(a)} \mathbf{U}^\dagger\ }$$
> This is a **unitary similarity transformation**. $\square$

### Big comparison: A state across three bases

Consider the 1D harmonic oscillator in an equal superposition of its ground and first excited states:
$$|\alpha\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle.$$

| Basis | Mathematical Nature | State Representation $|\alpha\rangle$ | Action of Operator $\hat x$ |
|---|---|---|---|
| **Energy/Number Basis** $\{|n\rangle\}$ | Discrete orthonormal sequence ($\ell^2$) | Column vector: $\mathbf{c} = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \\ \vdots \end{pmatrix}$ | Matrix multiplication by tridiagonal $\hat x$ matrix: $(\hat x\mathbf{c})_0 = \sqrt{\frac{\hbar}{2m\omega}}\frac{1}{\sqrt{2}}$ |
| **Position Basis** $\{|x'\rangle\}$ | Continuous coordinate basis ($L^2$) | Wave function: $\psi(x') = \langle x'\|\alpha\rangle = \frac{1}{\sqrt{2}}\psi_0(x') + \frac{1}{\sqrt{2}}\psi_1(x')$ | Multiplication by $x'$: $\hat x\psi(x') = x'\psi(x')$ |
| **Momentum Basis** $\{|p'\rangle\}$ | Continuous Fourier dual basis ($L^2$) | Fourier transform: $\tilde\psi(p') = \langle p'\|\alpha\rangle = \frac{1}{\sqrt{2}}\tilde\psi_0(p') + \frac{1}{\sqrt{2}}\tilde\psi_1(p')$ | Differentiation: $\hat x\tilde\psi(p') = i\hbar\frac{\partial}{\partial p'}\tilde\psi(p')$ |

> [!example] Worked numerical example: Qubit basis change from $Z$ to $X$
> Let $\{|+z\rangle, |-z\rangle\}$ be the eigenbasis of $\sigma_z = \begin{pmatrix} 1&0\\0&-1 \end{pmatrix}$.
> The eigenstates of $\sigma_x = \begin{pmatrix} 0&1\\1&0 \end{pmatrix}$ are:
> $$|+x\rangle = \frac{1}{\sqrt{2}}|+z\rangle + \frac{1}{\sqrt{2}}|-z\rangle, \qquad |-x\rangle = \frac{1}{\sqrt{2}}|+z\rangle - \frac{1}{\sqrt{2}}|-z\rangle.$$
> The unitary change-of-basis matrix $U$ (the Hadamard matrix) has elements $U_{ji} = \langle x_j|z_i\rangle$:
> $$U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$
> Check unitarity:
> $$U^\dagger U = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1+1 & 1-1 \\ 1-1 & 1+1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \hat 1 \quad \checkmark$$
> We transform $\sigma_z$ into the $X$-basis:
> $$\sigma_z^{(x)} = U \sigma_z^{(z)} U^\dagger = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \sigma_x.$$
> The $Z$-operator becomes off-diagonal in the $X$-basis, as required!

---

## 6. Position and momentum representations

<span class="scope-extra-book">extra · book</span> *Sakurai §1.6–1.7 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.47–60]]); Griffiths §3.4; Shankar §1.10*

> [!intuition] $p=-i\hbar\,d/dx$ is not a definition, it is a consequence
> Momentum is *what moves the wave sideways*. If shifting by $\ell$ is $e^{-ip\ell/\hbar}$, then for small $\ell$ the change of $\psi(x)$ is $-\ell\,\psi'(x)$, so $p\leftrightarrow-i\hbar\,d/dx$. A plane wave $e^{ipx/\hbar}$ is the one shape a shift leaves unchanged except for a phase: it is the eigenfunction. The Fourier transform is the change of ruler from $x$ to $p$ (Figure DA.1 B).

### Continuous spectrum and position eigenkets

The position observable $\hat x$ satisfies the continuous eigenvalue equation:
$$\hat x|x'\rangle = x'|x'\rangle, \qquad x' \in (-\infty, \infty).$$
Orthonormality and completeness take the form:
$$\langle x'|x''\rangle = \delta(x'-x''), \qquad \int_{-\infty}^\infty dx'\, |x'\rangle\langle x'| = \hat 1.$$

### The wave function as an inner product

The spatial wave function $\psi(x')$ is not an abstract entity; it is the **inner product** of the position eigenbra $\langle x'|$ with the state ket $|\alpha\rangle$:
$$\boxed{\ \psi(x') \equiv \langle x'|\alpha\rangle\ }$$
Expanding $|\alpha\rangle$ in the position basis:
$$|\alpha\rangle = \hat 1|\alpha\rangle = \int_{-\infty}^\infty dx'\, |x'\rangle\langle x'|\alpha\rangle = \int_{-\infty}^\infty dx'\,\psi(x')|x'\rangle.$$
The overlap between two physical states $|\alpha\rangle$ and $|\beta\rangle$ is recovered immediately:
$$\langle\beta|\alpha\rangle = \langle\beta|\hat 1|\alpha\rangle = \int_{-\infty}^\infty dx'\, \langle\beta|x'\rangle\langle x'|\alpha\rangle = \int_{-\infty}^\infty dx'\,\phi^*(x')\psi(x').$$

### Derivation: Momentum operator in position space

Why is momentum represented by $-i\hbar\frac{\partial}{\partial x'}$ in position space? Sakurai derives this profoundly from the **spatial translation operator** $\mathcal{T}(dx')$.

> [!derivation] Rigorous derivation of $\langle x'|\hat p|\alpha\rangle = -i\hbar\partial_{x'}\psi(x')$
> Let $\mathcal{T}(dx')$ be the operator that translates a physical system by an infinitesimal displacement $dx'$:
> $$\mathcal{T}(dx')|x'\rangle = |x'+dx'\rangle.$$
> 1. **Bra translation:**
>    Consider the inner product $\langle x'|\mathcal{T}(dx')|x''\rangle = \langle x'|x''+dx'\rangle = \delta\big(x' - (x''+dx')\big) = \delta\big((x'-dx') - x''\big) = \langle x'-dx'|x''\rangle$.
>    Since this holds for all basis kets $|x''\rangle$:
>    $$\langle x'|\mathcal{T}(dx') = \langle x' - dx'|.$$
> 2. **Infinitesimal generator:**
>    Because translations preserve probabilities, $\mathcal{T}(dx')$ must be unitary. For infinitesimal $dx'$, it must deviate from identity linearly with a Hermitian generator $\hat G$:
>    $$\mathcal{T}(dx') = \hat 1 - \frac{i}{\hbar}\hat p\,dx', \qquad (\hat p^\dagger = \hat p).$$
> 3. **Action on an arbitrary ket $|\alpha\rangle$:**
>    Contract $\langle x'|\mathcal{T}(dx')$ with $|\alpha\rangle$:
>    $$\langle x'|\mathcal{T}(dx')|\alpha\rangle = \langle x' - dx'|\alpha\rangle = \psi(x' - dx').$$
> 4. **Taylor expansion:**
>    Expanding both sides to first order in $dx'$:
>    $$\text{LHS} = \langle x'|\left(\hat 1 - \frac{i}{\hbar}\hat p\,dx'\right)|\alpha\rangle = \langle x'|\alpha\rangle - \frac{i}{\hbar}dx'\,\langle x'|\hat p|\alpha\rangle = \psi(x') - \frac{i}{\hbar}dx'\,\langle x'|\hat p|\alpha\rangle.$$
>    $$\text{RHS} = \psi(x' - dx') = \psi(x') - dx'\,\frac{\partial\psi}{\partial x'} + \mathcal{O}(dx'^2).$$
> 5. **Equating terms:**
>    $$\psi(x') - \frac{i}{\hbar}dx'\,\langle x'|\hat p|\alpha\rangle = \psi(x') - dx'\,\frac{\partial\psi}{\partial x'}.$$
>    Cancelling $\psi(x')$ and dividing by $-dx'$:
>    $$\frac{i}{\hbar}\langle x'|\hat p|\alpha\rangle = \frac{\partial\psi}{\partial x'} \implies \boxed{\ \langle x'|\hat p|\alpha\rangle = -i\hbar\frac{\partial}{\partial x'}\langle x'|\alpha\rangle = -i\hbar\frac{\partial\psi}{\partial x'}\ }$$
> Thus, the differential operator $-i\hbar\frac{\partial}{\partial x'}$ is the coordinate representation of the abstract momentum observable $\hat p$. $\square$

### Momentum eigenkets and plane waves

Let $|p'\rangle$ be an eigenket of momentum: $\hat p|p'\rangle = p'|p'\rangle$.
In the position representation, this eigenvalue equation reads:
$$\langle x'|\hat p|p'\rangle = p'\langle x'|p'\rangle \implies -i\hbar\frac{\partial}{\partial x'}\langle x'|p'\rangle = p'\langle x'|p'\rangle.$$
This is an elementary first-order differential equation for the transformation function $\langle x'|p'\rangle$:
$$\frac{\partial}{\partial x'}\langle x'|p'\rangle = \frac{ip'}{\hbar}\langle x'|p'\rangle \implies \langle x'|p'\rangle = N e^{ip'x'/\hbar}.$$
To fix the normalisation constant $N$, we impose delta-normalisation $\langle p'|p''\rangle = \delta(p'-p'')$:
$$\langle p'|p''\rangle = \int_{-\infty}^\infty dx'\, \langle p'|x'\rangle\langle x'|p''\rangle = |N|^2 \int_{-\infty}^\infty dx'\, e^{i(p''-p')x'/\hbar} = |N|^2 (2\pi\hbar)\,\delta(p''-p').$$
Hence $|N|^2 (2\pi\hbar) = 1 \implies N = \frac{1}{\sqrt{2\pi\hbar}}$, yielding the famous **plane wave**:
$$\boxed{\ \langle x'|p'\rangle = \frac{1}{\sqrt{2\pi\hbar}}e^{ip'x'/\hbar}\ }$$

### Momentum-space wave function and the Fourier transform

The momentum wave function $\tilde\psi(p') \equiv \langle p'|\alpha\rangle$ is the Fourier transform of $\psi(x')$:
$$\tilde\psi(p') = \langle p'|\hat 1|\alpha\rangle = \int_{-\infty}^\infty dx'\, \langle p'|x'\rangle\langle x'|\alpha\rangle = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty dx'\, e^{-ip'x'/\hbar}\psi(x').$$
The inverse transform is obtained symmetrically:
$$\psi(x') = \langle x'|\hat 1|\alpha\rangle = \int_{-\infty}^\infty dp'\, \langle x'|p'\rangle\langle p'|\alpha\rangle = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty dp'\, e^{ip'x'/\hbar}\tilde\psi(p').$$

> [!example] Worked numerical example: Minimum-uncertainty Gaussian wave packet
> Consider a normalised Gaussian wave packet centred at $x_0 = 0$ with initial momentum $p_0$ and spatial width $\sigma$:
> $$\psi(x) = \left(2\pi\sigma^2\right)^{-1/4}\exp\!\left(-\frac{x^2}{4\sigma^2} + \frac{ip_0 x}{\hbar}\right).$$
> 1. **Compute momentum representation $\tilde\psi(p)$:**
>    $$\tilde\psi(p) = \frac{1}{\sqrt{2\pi\hbar}}\frac{1}{(2\pi\sigma^2)^{1/4}}\int_{-\infty}^\infty dx\,\exp\!\left(-\frac{x^2}{4\sigma^2} + \frac{i(p_0-p)x}{\hbar}\right).$$
>    Using the standard Gaussian integral $\int_{-\infty}^\infty e^{-ax^2+bx}dx = \sqrt{\frac{\pi}{a}}e^{b^2/4a}$ with $a = \frac{1}{4\sigma^2}$ and $b = \frac{i(p_0-p)}{\hbar}$:
>    $$\sqrt{\frac{\pi}{a}} = \sqrt{4\pi\sigma^2} = 2\sqrt{\pi}\sigma, \qquad \frac{b^2}{4a} = \frac{-(p-p_0)^2/\hbar^2}{1/\sigma^2} = -\frac{(p-p_0)^2\sigma^2}{\hbar^2}.$$
>    Multiplying prefactors:
>    $$\tilde\psi(p) = \frac{2\sqrt{\pi}\sigma}{\sqrt{2\pi\hbar}(2\pi\sigma^2)^{1/4}}\exp\!\left(-\frac{(p-p_0)^2\sigma^2}{\hbar^2}\right) = \left(\frac{2\sigma^2}{\pi\hbar^2}\right)^{1/4}\exp\!\left(-\frac{(p-p_0)^2\sigma^2}{\hbar^2}\right).$$
> 2. **Compute dispersions:**
>    - Probability density $|\psi(x)|^2 = \frac{1}{\sqrt{2\pi}\sigma}e^{-x^2/2\sigma^2} \implies \langle x\rangle = 0, \quad \langle x^2\rangle = \sigma^2 \implies \Delta x = \sigma$.
>    - Probability density $|\tilde\psi(p)|^2 = \sqrt{\frac{2\sigma^2}{\pi\hbar^2}}\exp\!\left(-\frac{2\sigma^2(p-p_0)^2}{\hbar^2}\right)$.
>      This is a normal distribution in $p$ with variance:
>      $$\text{Var}(p) = \frac{1}{2\big(2\sigma^2/\hbar^2\big)} = \frac{\hbar^2}{4\sigma^2} \implies \Delta p = \frac{\hbar}{2\sigma}.$$
> 3. **Uncertainty product:**
>    $$\Delta x\,\Delta p = \sigma \cdot \left(\frac{\hbar}{2\sigma}\right) = \frac{\hbar}{2}.$$
>    The Gaussian wave packet achieves the absolute theoretical minimum of quantum uncertainty!

---

## 7. Unitary operators and the translation operator

<span class="scope-extra-book">extra · book</span> *Sakurai §1.6 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.47–54]]); Griffiths §3.2; Shankar §1.6*

> [!intuition] Why $[\hat x,\hat p]=i\hbar$ is a statement about geometry
> Slide a particle by $\ell$ and then read its position: you find $x+\ell$. Read its position and then slide: you find $x$ and then move the *answer*. The two orders differ by $\ell$, and $\ell$ is exactly what the generator $\hat p$ multiplies. The canonical commutator is the statement that **space has translation symmetry** written in the language of operators.

### Unitary operators preserve geometry

An operator $\hat U$ is **unitary** if its adjoint equals its inverse:
$$\boxed{\ \hat U^\dagger \hat U = \hat U \hat U^\dagger = \hat 1\ }$$
Unitary operators are the quantum analogues of rotations in Euclidean space: they preserve all inner products and norms:
$$\langle\alpha_{\text{new}}|\beta_{\text{new}}\rangle = \big(\langle\alpha|\hat U^\dagger\big)\big(\hat U|\beta\rangle\big) = \langle\alpha|\hat U^\dagger \hat U|\beta\rangle = \langle\alpha|\hat 1|\beta\rangle = \langle\alpha|\beta\rangle.$$
Because measurement probabilities and expectation values are built from inner products, **unitary operators represent the physical symmetries of nature** (translations, rotations, time evolution).

### The finite translation operator

To translate a state by a finite distance $\ell$, we apply $N$ successive infinitesimal steps of length $\ell/N$ and take the continuum limit $N \to \infty$:
$$\mathcal{T}(\ell) = \lim_{N\to\infty} \left[\mathcal{T}\left(\frac{\ell}{N}\right)\right]^N = \lim_{N\to\infty} \left(\hat 1 - \frac{i}{\hbar}\hat p\frac{\ell}{N}\right)^N = \exp\!\left(-\frac{i\hat p\ell}{\hbar}\right).$$
The finite translation operator is:
$$\boxed{\ \mathcal{T}(\ell) = \exp\!\left(-\frac{i\hat p\ell}{\hbar}\right)\ }$$

### Canonical commutation relation from translation symmetry

> [!derivation] Proof of CCR $[\hat x,\hat p]=i\hbar$ from translation
> Consider the action of $\hat x$ and $\mathcal{T}(dx')$ on a position eigenket $|x'\rangle$:
> 1. $\hat x \mathcal{T}(dx')|x'\rangle = \hat x|x'+dx'\rangle = (x'+dx')|x'+dx'\rangle = (x'+dx')\mathcal{T}(dx')|x'\rangle$.
> 2. $\mathcal{T}(dx')\hat x|x'\rangle = \mathcal{T}(dx')(x'|x'\rangle) = x'\mathcal{T}(dx')|x'\rangle$.
> Subtracting:
> $$[\hat x, \mathcal{T}(dx')] |x'\rangle = dx'\,\mathcal{T}(dx')|x'\rangle = dx'|x'\rangle + \mathcal{O}(dx'^2).$$
> Since this holds for all basis kets $|x'\rangle$, the operator identity is:
> $$[\hat x, \mathcal{T}(dx')] = dx'\,\hat 1.$$
> Now substitute the infinitesimal expansion $\mathcal{T}(dx') = \hat 1 - \frac{i}{\hbar}\hat p\,dx'$:
> $$[\hat x, \hat 1 - \frac{i}{\hbar}\hat p\,dx'] = -\frac{i}{\hbar}[\hat x, \hat p]\,dx' = dx'\,\hat 1.$$
> Dividing by $dx'$ and multiplying by $i\hbar$:
> $$\boxed{\ [\hat x, \hat p] = i\hbar\hat 1\ }$$
> The canonical commutation relation is a direct mathematical consequence of the homogeneity and translation symmetry of space! $\square$

### The Hadamard lemma and shift of position

How does the finite translation operator transform the position operator?
We use the **Hadamard lemma** (the operator identity derived from the Baker–Campbell–Hausdorff formula):
$$e^{\hat A}\hat B e^{-\hat A} = \hat B + [\hat A, \hat B] + \frac{1}{2!}[\hat A, [\hat A, \hat B]] + \frac{1}{3!}[\hat A, [\hat A, [\hat A, \hat B]]] + \dots$$
Let $\hat A = \frac{i\hat p a}{\hbar}$ and $\hat B = \hat x$. Then:
$$[\hat A, \hat B] = \left[\frac{i\hat p a}{\hbar}, \hat x\right] = \frac{ia}{\hbar}[\hat p, \hat x] = \frac{ia}{\hbar}(-i\hbar\hat 1) = a\hat 1.$$
Since $a\hat 1$ is a scalar multiple of the identity, all higher nested commutators vanish identically:
$$[\hat A, [\hat A, \hat B]] = \left[\frac{i\hat p a}{\hbar}, a\hat 1\right] = 0.$$
Therefore, the series terminates after the first commutator term:
$$\boxed{\ \mathcal{T}^\dagger(a)\hat x\mathcal{T}(a) = e^{i\hat p a/\hbar}\hat x e^{-i\hat p a/\hbar} = \hat x + a\hat 1\ }$$
Conjugating position by the translation operator shifts the position operator by precisely the displacement $a$.

---

## 8. Measurement, compatible observables, and the Robertson uncertainty relation

<span class="scope-extra-book">extra · book</span> *Sakurai §1.4–1.5 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.33–47]]); Griffiths §3.4–3.5; Shankar §1.9–1.10*

> [!intuition] Commuting observables share a ruler; non-commuting ones do not
> If $[A,B]=0$ there is a basis in which both are diagonal: read both at once. If not, the best you can do is trade: a state sharp in $A$ (an eigenket of $A$) is a superposition of $B$-eigenkets, so $B$ is spread. Robertson gives the exact exchange rate, $\Delta A\,\Delta B\ge\frac12|\langle[A,B]\rangle|$, and Figure DA.3 shows the Gaussian that pays no extra.

### The measurement postulate in Dirac language

Let observable $A$ have a complete discrete spectral decomposition:
$$\hat A = \sum_{a'} a' |a'\rangle\langle a'| = \sum_{a'} a' \hat P_{a'}, \qquad \hat P_{a'} \equiv |a'\rangle\langle a'|.$$
When a measurement of $A$ is performed on a system in state $|\alpha\rangle$:
1. **Possible outcomes:** The only possible result is one of the eigenvalues $a'$ of $\hat A$.
2. **Born probability rule:** The probability $P(a')$ of obtaining eigenvalue $a'$ is the expectation of the projection operator $\hat P_{a'}$:
   $$P(a') = \langle\alpha|\hat P_{a'}|\alpha\rangle = \langle\alpha|a'\rangle\langle a'|\alpha\rangle = |\langle a'|\alpha\rangle|^2.$$
3. **State reduction (wave-function collapse):** Immediately following the measurement returning outcome $a'$, the state collapses to:
   $$|\alpha_{\text{post}}\rangle = \frac{\hat P_{a'}|\alpha\rangle}{\sqrt{\langle\alpha|\hat P_{a'}|\alpha\rangle}} = \frac{\langle a'|\alpha\rangle}{|\langle a'|\alpha\rangle|}|a'\rangle = e^{i\theta}|a'\rangle \doteq |a'\rangle.$$

The **expectation value** is the statistical average:
$$\langle A\rangle \equiv \langle\alpha|\hat A|\alpha\rangle = \sum_{a'} a' |\langle a'|\alpha\rangle|^2 = \sum_{a'} a' P(a').$$
The **uncertainty** (standard deviation or dispersion) is:
$$\Delta A \equiv \sqrt{\langle(\hat A - \langle A\rangle)^2\rangle} = \sqrt{\langle A^2\rangle - \langle A\rangle^2}.$$

### Compatible observables and simultaneous eigenkets

Two observables $A$ and $B$ are **compatible** if their operators commute: $[\hat A, \hat B] = 0$.

> [!derivation] Proof: Commuting observables share a simultaneous eigenbasis
> Let $[\hat A, \hat B] = 0$ and let $|a'\rangle$ be an eigenket of $\hat A$: $\hat A|a'\rangle = a'|a'\rangle$.
> Act with $\hat A$ on the ket $\hat B|a'\rangle$:
> $$\hat A(\hat B|a'\rangle) = (\hat A\hat B)|a'\rangle = (\hat B\hat A)|a'\rangle = \hat B(\hat A|a'\rangle) = \hat B(a'|a'\rangle) = a'(\hat B|a'\rangle).$$
> This proves that $\hat B|a'\rangle$ is *also* an eigenket of $\hat A$ with the same eigenvalue $a'$.
> 1. **Non-degenerate case:** If $a'$ is non-degenerate, the eigenspace is one-dimensional, so any vector in that space must be a scalar multiple of $|a'\rangle$. Hence:
>    $$\hat B|a'\rangle = b'|a'\rangle.$$
>    Thus, $|a'\rangle$ is simultaneously an eigenket of both $\hat A$ and $\hat B$.
> 2. **Degenerate case:** If $a'$ has an $m$-fold degeneracy, $\hat B$ leaves the $m$-dimensional eigenspace invariant. Because $\hat B$ is Hermitian, it can be diagonalised within this subspace (by the spectral theorem), yielding $m$ mutually orthogonal simultaneous eigenkets $|a', b^{(1)}\rangle, \dots, |a', b^{(m)}\rangle$. $\square$

### Complete Set of Commuting Observables (CSCO)

If an eigenvalue $a'$ of $\hat A$ is degenerate, the label $a'$ alone does not uniquely specify a physical state. We search for a second observable $\hat B$ commuting with $\hat A$ ($[\hat A, \hat B] = 0$). If degeneracies still remain, we find a third observable $\hat C$ commuting with both $\hat A$ and $\hat B$.
A set of mutually commuting observables $\{\hat A, \hat B, \hat C, \dots\}$ is called a **Complete Set of Commuting Observables (CSCO)** if their simultaneous eigenvalues $(a', b', c', \dots)$ uniquely specify a single physical state ket:
$$|a', b', c', \dots\rangle.$$
Examples:
- 1D Harmonic oscillator: $\{\hat H\}$ is a CSCO (no degeneracy, [[QM05 The Harmonic Oscillator]]).
- 3D Central force / Hydrogen atom: $\{\hat H, \hat L^2, \hat L_z\}$ is the standard CSCO, uniquely labeling states as $|n, \ell, m_\ell\rangle$.

### Full derivation of the Robertson uncertainty relation

> [!derivation] Complete derivation of the Robertson relation
> Let $\hat A$ and $\hat B$ be two arbitrary Hermitian operators. For any state $|\alpha\rangle$, define the shifted operators:
> $$\Delta\hat A \equiv \hat A - \langle A\rangle\hat 1, \qquad \Delta\hat B \equiv \hat B - \langle B\rangle\hat 1.$$
> Note that $\Delta\hat A$ and $\Delta\hat B$ are Hermitian, and their commutator is identical to $[\hat A, \hat B]$:
> $$[\Delta\hat A, \Delta\hat B] = [\hat A - \langle A\rangle, \hat B - \langle B\rangle] = [\hat A, \hat B].$$
> Now construct two auxiliary kets:
> $$|f\rangle \equiv \Delta\hat A|\alpha\rangle, \qquad |g\rangle \equiv \Delta\hat B|\alpha\rangle.$$
> Their norms squared are the variances:
> $$\langle f|f\rangle = \langle\alpha|\Delta\hat A^\dagger\Delta\hat A|\alpha\rangle = \langle\alpha|(\Delta\hat A)^2|\alpha\rangle = (\Delta A)^2,$$
> $$\langle g|g\rangle = \langle\alpha|\Delta\hat B^\dagger\Delta\hat B|\alpha\rangle = \langle\alpha|(\Delta\hat B)^2|\alpha\rangle = (\Delta B)^2.$$
> By the Cauchy–Schwarz inequality (§2):
> $$(\Delta A)^2 (\Delta B)^2 = \langle f|f\rangle\langle g|g\rangle \ge |\langle f|g\rangle|^2. \tag{1}$$
> Next, evaluate the inner product $\langle f|g\rangle$:
> $$\langle f|g\rangle = \langle\alpha|\Delta\hat A\Delta\hat B|\alpha\rangle.$$
> We decompose the operator product $\Delta\hat A\Delta\hat B$ into its Hermitian and anti-Hermitian parts:
> $$\Delta\hat A\Delta\hat B = \frac{1}{2}\{\Delta\hat A, \Delta\hat B\} + \frac{1}{2}[\Delta\hat A, \Delta\hat B],$$
> where $\{\hat X, \hat Y\} \equiv \hat X\hat Y + \hat Y\hat X$ is the **anticommutator**.
> - The anticommutator $\{\Delta\hat A, \Delta\hat B\}$ is Hermitian: $\{\Delta\hat A, \Delta\hat B\}^\dagger = \Delta\hat B\Delta\hat A + \Delta\hat A\Delta\hat B = \{\Delta\hat A, \Delta\hat B\}$. Therefore, its expectation value is **purely real**.
> - The commutator $[\Delta\hat A, \Delta\hat B] = [\hat A, \hat B]$ is anti-Hermitian: $[\hat A, \hat B]^\dagger = \hat B\hat A - \hat A\hat B = -[\hat A, \hat B]$. Therefore, its expectation value is **purely imaginary**.
> 
> Taking the expectation value:
> $$\langle f|g\rangle = \frac{1}{2}\langle\{\Delta\hat A, \Delta\hat B\}\rangle + \frac{1}{2}\langle[\hat A, \hat B]\rangle.$$
> For any complex number $z = x + iy$ with $x, y \in \mathbb{R}$, $|z|^2 = x^2 + y^2 \ge y^2 = (\text{Im}\,z)^2$. Here:
> $$|\langle f|g\rangle|^2 = \frac{1}{4}\big|\langle\{\Delta\hat A, \Delta\hat B\}\rangle\big|^2 + \frac{1}{4}\big|\langle[\hat A, \hat B]\rangle\big|^2 \ge \frac{1}{4}\big|\langle[\hat A, \hat B]\rangle\big|^2. \tag{2}$$
> Combining inequalities (1) and (2):
> $$(\Delta A)^2(\Delta B)^2 \ge \frac{1}{4}\big|\langle[\hat A, \hat B]\rangle\big|^2.$$
> Taking the square root of both sides:
> $$\boxed{\ \Delta A\,\Delta B \ge \frac{1}{2}\big|\langle[\hat A, \hat B]\rangle\big|\ }$$
> This is the **generalised Robertson uncertainty relation**. $\square$

### Conditions for saturation (minimum uncertainty)

The uncertainty inequality becomes an exact equality ($\Delta A\,\Delta B = \frac{1}{2}|\langle[\hat A, \hat B]\rangle|$) if and only if **both** inequalities (1) and (2) are saturated simultaneously:
1. **Schwarz saturation:** $|f\rangle = c|g\rangle$ for some complex constant $c$.
2. **Vanishing anticommutator expectation:** $\langle\{\Delta\hat A, \Delta\hat B\}\rangle = 0$.
Condition 2 requires $\langle f|g\rangle$ to be purely imaginary, meaning $c = i\lambda$ with $\lambda \in \mathbb{R}$.
Thus, the minimum-uncertainty condition is:
$$\big(\hat A - \langle A\rangle\big)|\alpha\rangle = i\lambda\big(\hat B - \langle B\rangle\big)|\alpha\rangle \qquad (\lambda \in \mathbb{R}).$$
In position space for $\hat A = \hat x$ and $\hat B = \hat p$, this differential equation yields the Gaussian wave packet!

![[fig_da_uncertainty.png]]
*Figure DA.3 (contours in the figure are the $1/e$ Wigner contours, radius 1 in units of $\sqrt{\hbar/m\omega}$, i.e. $\sqrt2$ times the one-standard-deviation radius $\sqrt{\hbar/2}$ used in the caption; the dashed curves in A are the *momentum* densities, of width $\hbar/2\sigma$). A: The Heisenberg uncertainty trade-off for a family of Gaussian wave packets: squeezing $\Delta x = \sigma$ unavoidably broadens the momentum profile $\Delta p = \hbar/2\sigma$ such that the product remains fixed at $\hbar/2$. B: Phase-space uncertainty ellipses in the dimensionless $(x, p)$ plane: a coherent state is a symmetric circle of radius $\sqrt{\hbar/2}$, while squeezed states are rotated ellipses maintaining constant phase-space area $\pi\hbar$. C: The Robertson uncertainty product $\Delta x\Delta p = (n+\frac{1}{2})\hbar$ for the harmonic oscillator as a function of quantum number $n$, saturating the fundamental quantum bound $\hbar/2$ exclusively at the ground state $n=0$.*

> [!example] Worked numerical example: Qubit spin uncertainty
> For a spin-1/2 particle, $\hat S_x = \frac{\hbar}{2}\sigma_x, \hat S_y = \frac{\hbar}{2}\sigma_y, \hat S_z = \frac{\hbar}{2}\sigma_z$.
> Commutator: $[\hat S_x, \hat S_y] = \frac{\hbar^2}{4}[\sigma_x, \sigma_y] = \frac{\hbar^2}{4}(2i\sigma_z) = i\hbar\hat S_z$.
> The Robertson relation predicts:
> $$\Delta S_x\,\Delta S_y \ge \frac{1}{2}|\langle[\hat S_x, \hat S_y]\rangle| = \frac{\hbar}{2}|\langle S_z\rangle|.$$
> Let the system be in the eigenstate $|+z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
> 1. $\langle S_z\rangle = \frac{\hbar}{2}(1) = \frac{\hbar}{2} \implies \text{Lower bound} = \frac{\hbar}{2}\left(\frac{\hbar}{2}\right) = \frac{\hbar^2}{4}$.
> 2. Expectation values:
>    $$\langle S_x\rangle = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = 0, \qquad \langle S_y\rangle = 0.$$
> 3. Squares: $\hat S_x^2 = \frac{\hbar^2}{4}\sigma_x^2 = \frac{\hbar^2}{4}\hat 1 \implies \langle S_x^2\rangle = \frac{\hbar^2}{4} \implies \Delta S_x = \frac{\hbar}{2}$.
>    Similarly, $\hat S_y^2 = \frac{\hbar^2}{4}\hat 1 \implies \langle S_y^2\rangle = \frac{\hbar^2}{4} \implies \Delta S_y = \frac{\hbar}{2}$.
> 4. Uncertainty product:
>    $$\Delta S_x\,\Delta S_y = \left(\frac{\hbar}{2}\right)\left(\frac{\hbar}{2}\right) = \frac{\hbar^2}{4}.$$
> The Robertson bound is **exactly saturated** for the state $|+z\rangle$!

---

## 9. Time evolution: the Schrödinger picture

<span class="scope-extra-book">extra · book</span> *Sakurai §2.1 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.71–86]]); Griffiths §2.1; Shankar §4.1*

> [!intuition] Time evolution is a spinning of the energy axes
> In the energy basis $e^{-iHt/\hbar}$ multiplies the $n$-th component by $e^{-iE_nt/\hbar}$: each axis spins at its own rate $\omega_n=E_n/\hbar$. A state with one energy only changes phase (nothing observable moves: *stationary*). With two energies the components drift in relative phase and the probability sloshes at $\omega_{21}=(E_2-E_1)/\hbar$ — the quantum beat of Figure DA.4 C. Dynamics is interference between energy components.

### The time-evolution operator

In the Schrödinger picture, physical state kets change with time: $|\alpha\rangle \to |\alpha, t\rangle$.
The connection between the initial state at $t_0$ and the state at time $t$ is mediated by the **time-evolution operator** (or propagator) $\hat U(t, t_0)$:
$$|\alpha, t\rangle = \hat U(t, t_0)|\alpha, t_0\rangle.$$
Axioms satisfied by $\hat U(t, t_0)$:
1. **Unitarity:** $\hat U^\dagger(t, t_0)\hat U(t, t_0) = \hat 1$ (conservation of total probability $\langle\alpha, t|\alpha, t\rangle = 1$).
2. **Composition:** $\hat U(t_2, t_0) = \hat U(t_2, t_1)\hat U(t_1, t_0)$ for $t_0 \le t_1 \le t_2$.
3. **Identity at zero elapsed time:** $\hat U(t_0, t_0) = \hat 1$.

### Derivation of the Schrödinger equation from infinitesimal evolution

> [!derivation] Infinitesimal time translation generates Schrödinger's equation
> Consider an infinitesimal time step $dt$. By Axiom 3, $\hat U(t_0+dt, t_0)$ must differ from $\hat 1$ by terms of order $dt$.
> Unitarity requires the generator to be Hermitian:
> $$\hat U(t_0+dt, t_0) = \hat 1 - \frac{i}{\hbar}\hat H\,dt, \qquad (\hat H^\dagger = \hat H).$$
> Here $\hat H$ is the Hamiltonian (the generator of time translations).
> Apply this operator to the state $|\alpha, t\rangle$:
> $$|\alpha, t+dt\rangle = \hat U(t+dt, t)|\alpha, t\rangle = \left(\hat 1 - \frac{i}{\hbar}\hat H\,dt\right)|\alpha, t\rangle = |\alpha, t\rangle - \frac{i}{\hbar}\hat H\,dt|\alpha, t\rangle.$$
> Subtracting $|\alpha, t\rangle$ and dividing by $dt$:
> $$\frac{|\alpha, t+dt\rangle - |\alpha, t\rangle}{dt} = -\frac{i}{\hbar}\hat H|\alpha, t\rangle.$$
> Taking the limit $dt \to 0$:
> $$\frac{\partial}{\partial t}|\alpha, t\rangle = -\frac{i}{\hbar}\hat H|\alpha, t\rangle \implies \boxed{\ i\hbar\frac{\partial}{\partial t}|\alpha, t\rangle = \hat H|\alpha, t\rangle\ }$$
> This is the **time-dependent Schrödinger equation** for the abstract state ket. $\square$

For a time-independent Hamiltonian $\hat H$, integrating the differential equation $\frac{d\hat U}{dt} = -\frac{i}{\hbar}\hat H\hat U$ with initial condition $\hat U(0) = \hat 1$ yields:
$$\boxed{\ \hat U(t, 0) = \exp\!\left(-\frac{i\hat H t}{\hbar}\right)\ }$$

### Stationary states and quantum beats

Let $|E_n\rangle$ be an eigenket of the Hamiltonian: $\hat H|E_n\rangle = E_n|E_n\rangle$.
Its time evolution is:
$$|E_n, t\rangle = e^{-i\hat H t/\hbar}|E_n\rangle = e^{-iE_n t/\hbar}|E_n\rangle.$$
This is a **stationary state**: the ket merely acquires an overall phase factor. For any observable $\hat A$:
$$\langle A\rangle(t) = \langle E_n, t|\hat A|E_n, t\rangle = \big(e^{iE_n t/\hbar}\langle E_n|\big)\hat A\big(e^{-iE_n t/\hbar}|E_n\rangle\big) = \langle E_n|\hat A|E_n\rangle = \text{constant}.$$

For an arbitrary superposition $|\alpha, 0\rangle = \sum_n c_n |E_n\rangle$:
$$|\alpha, t\rangle = \sum_n c_n e^{-iE_n t/\hbar}|E_n\rangle.$$
The probabilities of obtaining energy $E_n$ remain constant: $P(E_n) = |c_n e^{-iE_n t/\hbar}|^2 = |c_n|^2$.
However, expectation values of operators that do not commute with $\hat H$ will oscillate at the Bohr transition frequencies:
$$\omega_{mn} = \frac{E_m - E_n}{\hbar}.$$

![[fig_da_evolution.png]]
*Figure DA.4. A: Time evolution in the Schrödinger picture: the state vector $|\psi(t)\rangle$ rotates continuously through Hilbert space while operator coordinate axes remain static. B: Time evolution in the Heisenberg picture: the state vector $|\psi(0)\rangle$ is permanently frozen at its $t=0$ position while the observable operator axes $\hat A_H(t)$ rotate in the opposite sense. C: Quantum beat interference: in a superposition of two stationary states, the probability densities exhibit sinusoidal beating at the Bohr difference frequency $\omega_{21} = (E_2 - E_1)/\hbar$.*

> [!example] Worked numerical example: Quantum beat frequency in a 2-level atom
> Consider a 2-level atom with Hamiltonian $\hat H|E_1\rangle = E_1|E_1\rangle$ and $\hat H|E_2\rangle = E_2|E_2\rangle$, where $E_2 - E_1 = \hbar\omega_{21}$.
> At $t=0$, the system is in an equal superposition:
> $$|\psi, 0\rangle = \frac{1}{\sqrt{2}}|E_1\rangle + \frac{1}{\sqrt{2}}|E_2\rangle.$$
> At time $t$:
> $$|\psi, t\rangle = \frac{1}{\sqrt{2}}e^{-iE_1 t/\hbar}|E_1\rangle + \frac{1}{\sqrt{2}}e^{-iE_2 t/\hbar}|E_2\rangle = \frac{e^{-iE_1 t/\hbar}}{\sqrt{2}}\Big(|E_1\rangle + e^{-i\omega_{21}t}|E_2\rangle\Big).$$
> Let $\hat x$ be an electric dipole operator with $\langle E_1|\hat x|E_1\rangle = \langle E_2|\hat x|E_2\rangle = 0$ (due to parity) and transition matrix element $\langle E_1|\hat x|E_2\rangle = d \in \mathbb{R}$.
> We compute $\langle x\rangle(t)$:
> $$\begin{aligned}
> \langle x\rangle(t) &= \langle\psi, t|\hat x|\psi, t\rangle \\
> &= \frac{1}{2}\Big(e^{iE_1 t/\hbar}\langle E_1| + e^{iE_2 t/\hbar}\langle E_2|\Big)\hat x\Big(e^{-iE_1 t/\hbar}|E_1\rangle + e^{-iE_2 t/\hbar}|E_2\rangle\Big) \\
> &= \frac{1}{2}\Big(0 + e^{i(E_1-E_2)t/\hbar}\langle E_1|\hat x|E_2\rangle + e^{i(E_2-E_1)t/\hbar}\langle E_2|\hat x|E_1\rangle + 0\Big) \\
> &= \frac{1}{2}\Big(d e^{-i\omega_{21}t} + d e^{i\omega_{21}t}\Big) = d\cos(\omega_{21}t).
> \end{aligned}$$
> The dipole moment oscillates sinusoidally at the transition frequency $\omega_{21}$ with amplitude $d$. This oscillating dipole radiates electromagnetic waves at frequency $\omega_{21}$ — the physical origin of atomic emission spectra!

---

## 10. 🔵 The Schrödinger vs Heisenberg pictures

<span class="scope-extra-beyond">extra · beyond</span> *Sakurai §2.2 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF pp.86–98]]); Shankar §4.3; Cohen-Tannoudji Ch. III*

> [!intuition] Moving the camera or moving the scene
> Schrödinger: the state moves, the measuring axes stay. Heisenberg: the state stays, the axes counter-rotate. Every prediction is a *relative* orientation of state and axes, so they agree on all of them (Figure DA.4 A,B). The Heisenberg form is the one that makes the classical limit obvious: $\dot x=p/m$, $\dot p=-V'(x)$ as *operator* equations.

### Defining the Heisenberg picture

In the **Schrödinger picture** (subscript $S$), state kets evolve in time while operators are static:
$$|\alpha, t\rangle_S = \hat U(t)|\alpha, 0\rangle_S, \qquad \hat A_S = \text{static}.$$
The expectation value of an observable is:
$$\langle A\rangle(t) = {}_S\langle\alpha, t|\hat A_S|\alpha, t\rangle_S = {}_S\langle\alpha, 0|\hat U^\dagger(t)\hat A_S\hat U(t)|\alpha, 0\rangle_S.$$
This motivates the **Heisenberg picture** (subscript $H$): define the state kets to be permanently frozen at $t=0$, and transfer all dynamical time dependence into the operators:
$$\boxed{\ |\alpha\rangle_H \equiv |\alpha, 0\rangle_S\ }$$
$$\boxed{\ \hat A_H(t) \equiv \hat U^\dagger(t)\hat A_S\hat U(t) = e^{i\hat H t/\hbar}\hat A_S e^{-i\hat H t/\hbar}\ }$$
By construction, all physical predictions are identical:
$$\langle A\rangle(t) = {}_H\langle\alpha|\hat A_H(t)|\alpha\rangle_H = {}_S\langle\alpha, t|\hat A_S|\alpha, t\rangle_S.$$

### The Heisenberg equation of motion

> [!derivation] Deriving the Heisenberg equation of motion
> Differentiate $\hat A_H(t) = \hat U^\dagger(t)\hat A_S\hat U(t)$ with respect to time using the product rule:
> $$\frac{d\hat A_H}{dt} = \frac{\partial\hat U^\dagger}{\partial t}\hat A_S\hat U + \hat U^\dagger\left(\frac{\partial\hat A_S}{\partial t}\right)\hat U + \hat U^\dagger\hat A_S\frac{\partial\hat U}{\partial t}.$$
> From the Schrödinger equation for $\hat U(t) = e^{-i\hat H t/\hbar}$:
> $$\frac{\partial\hat U}{\partial t} = -\frac{i}{\hbar}\hat H\hat U = -\frac{i}{\hbar}\hat U\hat H, \qquad \frac{\partial\hat U^\dagger}{\partial t} = \frac{i}{\hbar}\hat U^\dagger\hat H = \frac{i}{\hbar}\hat H\hat U^\dagger.$$
> Substituting these derivatives:
> $$\begin{aligned}
> \frac{d\hat A_H}{dt} &= \frac{i}{\hbar}\hat U^\dagger\hat H\hat A_S\hat U - \frac{i}{\hbar}\hat U^\dagger\hat A_S\hat H\hat U + \left(\frac{\partial\hat A_S}{\partial t}\right)_H \\
> &= \frac{i}{\hbar}\left(\hat U^\dagger\hat H\hat U\hat U^\dagger\hat A_S\hat U - \hat U^\dagger\hat A_S\hat U\hat U^\dagger\hat H\hat U\right) + \left(\frac{\partial\hat A}{\partial t}\right)_H.
> \end{aligned}$$
> Since $\hat H_H(t) = \hat U^\dagger\hat H\hat U = \hat H$ (the Hamiltonian commutes with functions of itself):
> $$\frac{d\hat A_H}{dt} = \frac{i}{\hbar}\big(\hat H\hat A_H(t) - \hat A_H(t)\hat H\big) + \left(\frac{\partial\hat A}{\partial t}\right)_H.$$
> Recognizing the commutator:
> $$\boxed{\ \frac{d\hat A_H}{dt} = \frac{i}{\hbar}[\hat H, \hat A_H] + \left(\frac{\partial\hat A}{\partial t}\right)_H = \frac{1}{i\hbar}[\hat A_H, \hat H] + \left(\frac{\partial\hat A}{\partial t}\right)_H\ }$$
> This is the **Heisenberg equation of motion**. $\square$

### Quantum Hamilton's equations and Ehrenfest's theorem

Consider a particle moving in a 1D potential: $\hat H = \frac{\hat p^2}{2m} + V(\hat x)$.
Let us evaluate the Heisenberg equations of motion for position and momentum:
1. **Position equation:**
   $$\frac{d\hat x_H}{dt} = \frac{i}{\hbar}[\hat H, \hat x_H] = \frac{i}{\hbar}\left[\frac{\hat p_H^2}{2m}, \hat x_H\right] = \frac{i}{2m\hbar}(-2i\hbar\hat p_H) = \frac{\hat p_H}{m}.$$
2. **Momentum equation:**
   $$\frac{d\hat p_H}{dt} = \frac{i}{\hbar}[\hat H, \hat p_H] = \frac{i}{\hbar}[V(\hat x_H), \hat p_H] = \frac{i}{\hbar}\left(i\hbar\frac{\partial V}{\partial\hat x_H}\right) = -\frac{\partial V(\hat x_H)}{\partial\hat x_H}.$$

These operator equations are the exact quantum mechanical analogues of **Hamilton's canonical equations of classical mechanics**:
$$\frac{dx}{dt} = \frac{p}{m}, \qquad \frac{dp}{dt} = -\frac{\partial V}{\partial x}.$$
Taking expectation values on both sides yields **Ehrenfest's theorem**:
$$\boxed{\ \frac{d\langle x\rangle}{dt} = \frac{\langle p\rangle}{m}, \qquad \frac{d\langle p\rangle}{dt} = -\left\langle\frac{\partial V}{\partial x}\right\rangle\ }$$
Quantum mechanical wave packets follow classical trajectories to the extent that $\langle\nabla V(x)\rangle \approx \nabla V(\langle x\rangle)$ (valid when the wave packet width is small compared to the scale of spatial variation of the force).

### Comparison: Schrödinger vs Heisenberg vs Interaction pictures

| Feature | Schrödinger Picture | Heisenberg Picture | Interaction (Dirac) Picture |
|---|---|---|---|
| **State Vector** | Moves: $i\hbar\partial_t\|\psi\rangle_S = \hat H\|\psi\rangle_S$ | Static: $\|\psi\rangle_H = \|\psi(0)\rangle_S$ | Moves via $V$: $i\hbar\partial_t\|\psi\rangle_I = \hat V_I\|\psi\rangle_I$ |
| **Operators** | Static: $\hat A_S$ | Moves: $\frac{d\hat A_H}{dt} = \frac{i}{\hbar}[\hat H, \hat A_H]$ | Moves via $H_0$: $\frac{d\hat A_I}{dt} = \frac{i}{\hbar}[\hat H_0, \hat A_I]$ |
| **Expectation** | ${}_S\langle\psi(t)\|\hat A_S\|\psi(t)\rangle_S$ | ${}_H\langle\psi\|\hat A_H(t)\|\psi\rangle_H$ | ${}_I\langle\psi(t)\|\hat A_I(t)\|\psi(t)\rangle_I$ |
| **Best Used For** | Wave mechanics, bound states | Operator algebra, QFT, classical limit | Time-dependent perturbation theory |

> [!example] Worked numerical example: The harmonic oscillator in the Heisenberg picture
> For the harmonic oscillator, $\hat H = \hbar\omega(\hat a^\dagger\hat a + \frac{1}{2})$.
> 1. **Equation of motion for lowering operator $\hat a_H(t)$:**
>    $$[\hat H, \hat a_H] = \hbar\omega[\hat a^\dagger\hat a, \hat a_H] = \hbar\omega[\hat a^\dagger, \hat a]\hat a = \hbar\omega(-1)\hat a = -\hbar\omega\hat a_H.$$
>    $$\frac{d\hat a_H}{dt} = \frac{i}{\hbar}(-\hbar\omega\hat a_H) = -i\omega\hat a_H(t).$$
>    Integrating with initial condition $\hat a_H(0) = \hat a$:
>    $$\hat a_H(t) = \hat a e^{-i\omega t}, \qquad \hat a_H^\dagger(t) = \hat a^\dagger e^{i\omega t}.$$
> 2. **Heisenberg position operator $\hat x_H(t)$:**
>    $$\begin{aligned}
>    \hat x_H(t) &= \sqrt{\frac{\hbar}{2m\omega}}\Big(\hat a_H(t) + \hat a_H^\dagger(t)\Big) = \sqrt{\frac{\hbar}{2m\omega}}\Big(\hat a e^{-i\omega t} + \hat a^\dagger e^{i\omega t}\Big) \\
>    &= \sqrt{\frac{\hbar}{2m\omega}}\Big((\hat a+\hat a^\dagger)\cos\omega t - i(\hat a - \hat a^\dagger)\sin\omega t\Big) \\
>    &= \hat x(0)\cos\omega t + \frac{\hat p(0)}{m\omega}\sin\omega t.
>    \end{aligned}$$
> This is the **exact classical equation of motion** for a harmonic oscillator, preserved identically at the operator level!

---

> [!connection] Group theory used here
> The translation operator is a unitary representation of $(\mathbb R,+)$ and $[\hat x,\hat p]=i\hbar$ defines the Heisenberg group: [[GT07 p-Groups and Nilpotent Groups]] §5, [[GT10 Symmetry Representations and Characters]] §6; see [[Where Groups Appear in the Vault]].

## Map of this chapter

> [!connection] How Dirac Algebra connects to the quantum mechanics vault
> **Builds on:**
> - [[Dirac Notation]] — introduces the fundamental symbols $|\psi\rangle$ and $\langle\phi|$
> - [[Hilbert Space]] — the abstract topological and algebraic framework
> - [[Hermitian Operator]] — self-adjoint operators in linear algebra
> - [[Canonical Commutation Relation]] — the foundational commutation algebra
>
> **Provides the rigorous mathematical foundation for:**
> - [[QM03 States Operators and Measurement]] — measurement probabilities, 2-level systems, compatible operators
> - [[QM04 The Particle in a Box]] — spatial boundary conditions, parity, superposition dynamics
> - [[QM05 The Harmonic Oscillator]] — ladder operators $\hat a, \hat a^\dagger$, number basis $|n\rangle$
> - [[QM06 The Oscillator Toolbox]] — Fock space matrix representations, coherent states, virial and Ehrenfest theorems
>
> **Core concepts consolidated here:**
> [[Dirac Notation]] · [[Hilbert Space]] · [[Hermitian Operator]] · [[Hermitian Conjugate]] · [[Eigenstate and Eigenvalue]] · [[Commutator]] · [[Canonical Commutation Relation]] · [[Completeness Relation]] · [[Measurement Postulate]] · [[Generalised Uncertainty Principle]] · [[Heisenberg Uncertainty Principle]] · [[Unitary Operator]] · [[Time Evolution Operator]] · [[Schrodinger Equation]] · [[Stationary State]] · [[Plane Wave]] · [[Gaussian Wave Packet]] · [[Number Basis]] · [[Number Operator]] · [[Dirac Delta Function]] · [[Gaussian Integral]]

---

## Summary

> [!summary] Dirac Algebra cheat-sheet
> - **Ket and Dual Bra:** Physical states are kets $|\alpha\rangle \in \mathcal{H}$; dual bras $\langle\alpha| \in \mathcal{H}^*$ are constructed via the conjugate-linear DC machine: $c|\alpha\rangle \leftrightarrow c^*\langle\alpha|$.
> - **Inner Product:** $\langle\beta|\alpha\rangle = \langle\alpha|\beta\rangle^*$; norm $\|\alpha\|^2 = \langle\alpha|\alpha\rangle \ge 0$.
> - **Schwarz Inequality:** $|\langle\alpha|\beta\rangle|^2 \le \langle\alpha|\alpha\rangle\langle\beta|\beta\rangle$, equality iff $|\alpha\rangle \propto |\beta\rangle$.
> - **Orthonormality:** Discrete $\langle a_m|a_n\rangle = \delta_{mn}$; continuous $\langle x'|x''\rangle = \delta(x'-x'')$, $\langle p'|p''\rangle = \delta(p'-p'')$.
> - **Outer Product Dyad:** $|\beta\rangle\langle\alpha|$ is a rank-1 operator mapping $|\gamma\rangle \mapsto \langle\alpha|\gamma\rangle|\beta\rangle$.
> - **Resolution of Identity:** $\hat 1 = \sum |a'\rangle\langle a'| = \int dx'|x'\rangle\langle x'|$; insert everywhere to expand amplitudes.
> - **Adjoint Rules:** $(c\hat A)^\dagger = c^*\hat A^\dagger$, $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger$, $(|\beta\rangle\langle\alpha|)^\dagger = |\alpha\rangle\langle\beta|$.
> - **Hermitian Observables:** $\hat A^\dagger = \hat A \implies$ eigenvalues are strictly real, eigenstates with distinct eigenvalues are strictly orthogonal.
> - **Change of Basis:** Unitary transformation $U_{ba} = \langle b|a\rangle$, with operator matrix transforming as $\mathbf{X}^{(b)} = \mathbf{U}\mathbf{X}^{(a)}\mathbf{U}^\dagger$.
> - **Coordinate Representations:** $\psi(x') = \langle x'|\alpha\rangle$, $\langle x'|\hat p|\alpha\rangle = -i\hbar\partial_{x'}\psi(x')$, $\langle x'|p'\rangle = \frac{1}{\sqrt{2\pi\hbar}}e^{ip'x'/\hbar}$.
> - **Spatial Translation:** $\mathcal{T}(a) = e^{-i\hat p a/\hbar}$; generates spatial shifts $\mathcal{T}^\dagger(a)\hat x\mathcal{T}(a) = \hat x + a\hat 1$; implies $[\hat x, \hat p] = i\hbar$.
> - **Robertson Uncertainty:** $\Delta A\,\Delta B \ge \frac{1}{2}|\langle[\hat A, \hat B]\rangle|$; saturated when $(\Delta\hat A)|\alpha\rangle = i\lambda(\Delta\hat B)|\alpha\rangle$ with $\lambda \in \mathbb{R}$.
> - **Time Evolution:** Schrödinger equation $i\hbar\partial_t|\alpha, t\rangle = \hat H|\alpha, t\rangle$; propagator $\hat U(t) = e^{-i\hat H t/\hbar}$.
> - **Heisenberg Picture:** States are frozen $|\alpha\rangle_H = |\alpha, 0\rangle_S$; operators evolve via $\frac{d\hat A_H}{dt} = \frac{i}{\hbar}[\hat H, \hat A_H] + (\frac{\partial\hat A}{\partial t})_H$; implies Ehrenfest's theorem.

---

## Practice

1. **Inner product axioms and conjugate linearity.**
   Using strictly the inner product axioms, prove that $\langle c_1\alpha + c_2\beta|\gamma\rangle = c_1^*\langle\alpha|\gamma\rangle + c_2^*\langle\beta|\gamma\rangle$. Show that for any state $|\psi\rangle$, $\langle\psi|\psi\rangle$ is real.

2. **The Schwarz inequality.**
   Two normalised states $|\alpha\rangle$ and $|\beta\rangle$ have an inner product $\langle\alpha|\beta\rangle = \frac{1}{2} + \frac{i}{2}$.
   (a) Calculate $|\langle\alpha|\beta\rangle|^2$ and verify that it satisfies the Schwarz inequality.
   (b) What is the norm of the state $|\gamma\rangle = |\alpha\rangle - \langle\beta|\alpha\rangle|\beta\rangle$?

3. **Adjoint properties.**
   Let $\hat A$ and $\hat B$ be Hermitian operators.
   (a) Prove that the product $\hat A\hat B$ is Hermitian if and only if $[\hat A, \hat B] = 0$.
   (b) Prove that $i[\hat A, \hat B]$ is always Hermitian.
   (c) Prove that the anticommutator $\{\hat A, \hat B\} = \hat A\hat B + \hat B\hat A$ is always Hermitian.

4. **Projector algebra.**
   Let $\hat P_1 = |1\rangle\langle 1|$ and $\hat P_2 = |2\rangle\langle 2|$ where $\langle 1|2\rangle = 0$ and $\langle 1|1\rangle = \langle 2|2\rangle = 1$.
   (a) Show that $\hat P_{1+2} = \hat P_1 + \hat P_2$ is an orthogonal projector (i.e. Hermitian and idempotent).
   (b) For an arbitrary state $|\psi\rangle = c_1|1\rangle + c_2|2\rangle + c_3|3\rangle$, compute $\hat P_{1+2}|\psi\rangle$ and its norm.

5. **Completeness and expectation values in a 3-level system.**
   An observable $\hat A$ on a three-dimensional Hilbert space has an orthonormal eigenbasis $\{|1\rangle, |2\rangle, |3\rangle\}$ with eigenvalues $a_1 = 1$, $a_2 = 0$, $a_3 = -1$.
   A system is prepared in the state $|\psi\rangle = \frac{1}{2}|1\rangle + \frac{i}{\sqrt{2}}|2\rangle + \frac{1}{2}|3\rangle$.
   (a) Verify that $|\psi\rangle$ is normalised.
   (b) Calculate the probabilities $P(a_1)$, $P(a_2)$, and $P(a_3)$.
   (c) Compute the expectation value $\langle\hat A\rangle$ and the variance $(\Delta A)^2$.

6. **Plane wave delta-normalisation.**
   Starting from the coordinate definition of momentum eigenkets $\langle x'|p'\rangle = \frac{1}{\sqrt{2\pi\hbar}}e^{ip'x'/\hbar}$, prove directly by inserting completeness that:
   $$\langle p'|p''\rangle = \delta(p'-p'').$$

7. **Translation operator on wavefunctions.**
   Let $\mathcal{T}(a) = \exp(-ia\hat p/\hbar)$ be the spatial translation operator.
   Prove by Taylor series expansion that for any spatial wave function $\psi(x) = \langle x|\psi\rangle$:
   $$\langle x|\mathcal{T}(a)|\psi\rangle = \psi(x-a).$$

8. **Compatible observables in degenerate spaces.**
   A two-dimensional subspace has degenerate eigenvalues $a_1 = a_2 = 3$ for operator $\hat A$.
   In an orthonormal basis $\{|e_1\rangle, |e_2\rangle\}$ spanning this subspace, a commuting operator $\hat B$ has matrix representation:
   $$\hat B \doteq \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}.$$
   Find the simultaneous eigenstates of $\hat A$ and $\hat B$ and their corresponding $\hat B$-eigenvalues.

9. **Robertson uncertainty for angular momentum.**
   The components of orbital angular momentum satisfy $[\hat L_x, \hat L_y] = i\hbar\hat L_z$.
   (a) Write down the Robertson uncertainty relation for $\Delta L_x\,\Delta L_y$.
   (b) Evaluate this relation for an eigenstate $|l, m\rangle$ of $\hat L^2$ and $\hat L_z$. Show that for $m = l$, $\Delta L_x\,\Delta L_y = \frac{\hbar^2 l}{2}$, and verify that the Robertson bound is satisfied.

10. **Schrödinger vs Heisenberg picture dynamics.**
    A particle of mass $m$ moves in a constant gravitational field $V(x) = mgx$.
    (a) In the Heisenberg picture, write down the equations of motion for $\hat x_H(t)$ and $\hat p_H(t)$.
    (b) Integrate these operator differential equations directly to find $\hat x_H(t)$ and $\hat p_H(t)$ in terms of $\hat x(0)$ and $\hat p(0)$.
    (c) Verify that taking expectation values reproduces classical parabolic trajectory kinematics.

> [!example]- Solutions
> 1. **Inner product axioms.**
>    From conjugate symmetry (Axiom 1): $\langle c_1\alpha + c_2\beta|\gamma\rangle = \langle\gamma|c_1\alpha + c_2\beta\rangle^*$.
>    By linearity in the ket (Axiom 2): $\langle\gamma|c_1\alpha + c_2\beta\rangle = c_1\langle\gamma|\alpha\rangle + c_2\langle\gamma|\beta\rangle$.
>    Taking the complex conjugate: $(c_1\langle\gamma|\alpha\rangle + c_2\langle\gamma|\beta\rangle)^* = c_1^*\langle\gamma|\alpha\rangle^* + c_2^*\langle\gamma|\beta\rangle^*$.
>    Applying conjugate symmetry again: $c_1^*\langle\alpha|\gamma\rangle + c_2^*\langle\beta|\gamma\rangle$. $\square$
>    For $|\psi\rangle$: $\langle\psi|\psi\rangle = \langle\psi|\psi\rangle^*$, which directly implies $\text{Im}(\langle\psi|\psi\rangle) = 0$, so $\langle\psi|\psi\rangle \in \mathbb{R}$.
>
> 2. **Schwarz inequality.**
>    (a) $|\langle\alpha|\beta\rangle|^2 = |\frac{1}{2} + \frac{i}{2}|^2 = (\frac{1}{2})^2 + (\frac{1}{2})^2 = \frac{1}{4} + \frac{1}{4} = \frac{1}{2} = 0.500$.
>    Since $\langle\alpha|\alpha\rangle = 1$ and $\langle\beta|\beta\rangle = 1$, the upper bound is $\langle\alpha|\alpha\rangle\langle\beta|\beta\rangle = 1.000$.
>    $0.500 \le 1.000$, which satisfies the Schwarz inequality.
>    (b) The norm squared is $\langle\gamma|\gamma\rangle = \langle\alpha|\alpha\rangle - \frac{|\langle\alpha|\beta\rangle|^2}{\langle\beta|\beta\rangle} = 1 - \frac{0.5}{1} = 0.500$.
>    Thus, $\||\gamma\rangle\| = \sqrt{0.5} = \frac{1}{\sqrt{2}} \approx 0.7071$.
>
> 3. **Adjoint properties.**
>    (a) $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger = \hat B\hat A$. For $\hat A\hat B$ to be Hermitian, we require $(\hat A\hat B)^\dagger = \hat A\hat B \iff \hat B\hat A = \hat A\hat B \iff [\hat A, \hat B] = 0$. $\square$
>    (b) $(i[\hat A, \hat B])^\dagger = -i[\hat A, \hat B]^\dagger = -i(\hat A\hat B - \hat B\hat A)^\dagger = -i(\hat B^\dagger\hat A^\dagger - \hat A^\dagger\hat B^\dagger) = -i(\hat B\hat A - \hat A\hat B) = i(\hat A\hat B - \hat B\hat A) = i[\hat A, \hat B]$. $\square$
>    (c) $(\{\hat A, \hat B\})^\dagger = (\hat A\hat B + \hat B\hat A)^\dagger = \hat B^\dagger\hat A^\dagger + \hat A^\dagger\hat B^\dagger = \hat B\hat A + \hat A\hat B = \{\hat A, \hat B\}$. $\square$
>
> 4. **Projector algebra.**
>    (a) Hermiticity: $\hat P_{1+2}^\dagger = (\hat P_1 + \hat P_2)^\dagger = \hat P_1^\dagger + \hat P_2^\dagger = \hat P_1 + \hat P_2 = \hat P_{1+2}$.
>    Idempotence: $\hat P_{1+2}^2 = (\hat P_1 + \hat P_2)(\hat P_1 + \hat P_2) = \hat P_1^2 + \hat P_1\hat P_2 + \hat P_2\hat P_1 + \hat P_2^2$.
>    Using $\hat P_1^2 = \hat P_1$, $\hat P_2^2 = \hat P_2$, and $\hat P_1\hat P_2 = |1\rangle\langle 1|2\rangle\langle 2| = 0 = \hat P_2\hat P_1$:
>    $\hat P_{1+2}^2 = \hat P_1 + 0 + 0 + \hat P_2 = \hat P_{1+2}$. Thus it is an orthogonal projector. $\square$
>    (b) $\hat P_{1+2}|\psi\rangle = (|1\rangle\langle 1| + |2\rangle\langle 2|)(c_1|1\rangle + c_2|2\rangle + c_3|3\rangle) = c_1|1\rangle + c_2|2\rangle$.
>    Norm: $\|\hat P_{1+2}|\psi\rangle\| = \sqrt{|c_1|^2 + |c_2|^2}$.
>
> 5. **Completeness in a 3-level system.**
>    (a) $\langle\psi|\psi\rangle = |1/2|^2 + |i/\sqrt{2}|^2 + |1/2|^2 = 1/4 + 1/2 + 1/4 = 1.000$. Normalised.
>    (b) $P(a_1) = |\langle 1|\psi\rangle|^2 = |1/2|^2 = 1/4 = 0.250$.
>    $P(a_2) = |\langle 2|\psi\rangle|^2 = |i/\sqrt{2}|^2 = 1/2 = 0.500$.
>    $P(a_3) = |\langle 3|\psi\rangle|^2 = |1/2|^2 = 1/4 = 0.250$. (Sum $= 0.25 + 0.50 + 0.25 = 1.000$).
>    (c) $\langle\hat A\rangle = P(a_1)(1) + P(a_2)(0) + P(a_3)(-1) = \frac{1}{4}(1) + 0 + \frac{1}{4}(-1) = 0.000$.
>    $\langle\hat A^2\rangle = P(a_1)(1)^2 + P(a_2)(0)^2 + P(a_3)(-1)^2 = \frac{1}{4}(1) + 0 + \frac{1}{4}(1) = \frac{1}{2} = 0.500$.
>    $(\Delta A)^2 = \langle A^2\rangle - \langle A\rangle^2 = 0.500 - 0.000 = 0.500 \implies \Delta A = 1/\sqrt{2} \approx 0.7071$.
>
> 6. **Plane wave normalisation.**
>    Insert the continuous position identity $\hat 1 = \int_{-\infty}^\infty dx'|x'\rangle\langle x'|$:
>    $$\langle p'|p''\rangle = \langle p'|\hat 1|p''\rangle = \int_{-\infty}^\infty dx'\, \langle p'|x'\rangle\langle x'|p''\rangle = \int_{-\infty}^\infty dx'\, \left(\frac{1}{\sqrt{2\pi\hbar}}e^{-ip'x'/\hbar}\right)\left(\frac{1}{\sqrt{2\pi\hbar}}e^{ip''x'/\hbar}\right) = \frac{1}{2\pi\hbar}\int_{-\infty}^\infty dx'\, e^{i(p''-p')x'/\hbar}.$$
>    Let $u = x'/\hbar \implies dx' = \hbar du$:
>    $$\langle p'|p''\rangle = \frac{\hbar}{2\pi\hbar}\int_{-\infty}^\infty du\, e^{i(p''-p')u} = \frac{1}{2\pi}\int_{-\infty}^\infty du\, e^{i(p''-p')u} = \delta(p''-p') = \delta(p'-p''). \quad \square$$
>
> 7. **Translation operator on wavefunctions.**
>    Expand the exponential operator: $\mathcal{T}(a) = \exp(-ia\hat p/\hbar) = \sum_{n=0}^\infty \frac{1}{n!}\left(-\frac{ia}{\hbar}\right)^n \hat p^n$.
>    In position space, $\langle x|\hat p^n|\psi\rangle = (-i\hbar)^n \frac{\partial^n}{\partial x^n}\psi(x)$.
>    $$\langle x|\mathcal{T}(a)|\psi\rangle = \sum_{n=0}^\infty \frac{1}{n!}\left(-\frac{ia}{\hbar}\right)^n (-i\hbar)^n \frac{\partial^n\psi}{\partial x^n} = \sum_{n=0}^\infty \frac{(-a)^n}{n!}\frac{\partial^n\psi}{\partial x^n}.$$
>    By Taylor's theorem, this power series is precisely $\psi(x - a)$. $\square$
>
> 8. **Compatible observables in degenerate spaces.**
>    Since $\hat A$ is proportional to identity on this subspace ($\hat A = 3\hat 1$), any linear combination of $|e_1\rangle$ and $|e_2\rangle$ is an eigenstate of $\hat A$ with eigenvalue 3. To find simultaneous eigenstates, we diagonalise $\hat B$:
>    $\det\begin{pmatrix} 1-\lambda & 2 \\ 2 & 1-\lambda \end{pmatrix} = (1-\lambda)^2 - 4 = 0 \implies 1-\lambda = \pm 2 \implies \lambda_+ = 3, \quad \lambda_- = -1$.
>    - For $\lambda_+ = 3$: $\begin{pmatrix} -2 & 2 \\ 2 & -2 \end{pmatrix}\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = 0 \implies u_1 = u_2$. Normalised: $|v_+\rangle = \frac{1}{\sqrt{2}}(|e_1\rangle + |e_2\rangle)$.
>    - For $\lambda_- = -1$: $\begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}\begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = 0 \implies w_1 = -w_2$. Normalised: $|v_-\rangle = \frac{1}{\sqrt{2}}(|e_1\rangle - |e_2\rangle)$.
>    The simultaneous eigenstates are $|v_+\rangle$ (eigenvalues $a=3, b=3$) and $|v_-\rangle$ (eigenvalues $a=3, b=-1$).
>
> 9. **Robertson uncertainty for angular momentum.**
>    (a) $\Delta L_x\,\Delta L_y \ge \frac{1}{2}|\langle[\hat L_x, \hat L_y]\rangle| = \frac{\hbar}{2}|\langle L_z\rangle|$.
>    (b) For state $|l, m\rangle$, $\langle L_z\rangle = m\hbar$. The lower bound is $\frac{\hbar^2 |m|}{2}$.
>    By symmetry, $\langle L_x\rangle = \langle L_y\rangle = 0$ and $\langle L_x^2\rangle = \langle L_y^2\rangle = \frac{1}{2}\langle L_x^2 + L_y^2\rangle = \frac{1}{2}\langle \hat L^2 - \hat L_z^2\rangle = \frac{\hbar^2}{2}[l(l+1) - m^2]$.
>    Therefore, $\Delta L_x = \Delta L_y = \hbar\sqrt{\frac{l(l+1)-m^2}{2}}$.
>    Product: $\Delta L_x\,\Delta L_y = \frac{\hbar^2}{2}[l(l+1) - m^2]$.
>    For $m = l$: $\Delta L_x\,\Delta L_y = \frac{\hbar^2}{2}[l^2+l - l^2] = \frac{\hbar^2 l}{2}$.
>    Comparing with the lower bound $\frac{\hbar^2 |m|}{2} = \frac{\hbar^2 l}{2}$: the bound is **exactly saturated**!
>
> 10. **Schrödinger vs Heisenberg picture dynamics.**
>     (a) $\hat H = \frac{\hat p_H^2}{2m} + mg\hat x_H$.
>     $\frac{d\hat x_H}{dt} = \frac{i}{\hbar}[\hat H, \hat x_H] = \frac{\hat p_H}{m}$.
>     $\frac{d\hat p_H}{dt} = \frac{i}{\hbar}[\hat H, \hat p_H] = \frac{i}{\hbar}[mg\hat x_H, \hat p_H] = -mg\hat 1$.
>     (b) Integrating the momentum equation: $\hat p_H(t) = \hat p(0) - mg t\hat 1$.
>     Substituting into the position equation:
>     $\frac{d\hat x_H}{dt} = \frac{\hat p(0)}{m} - gt\hat 1 \implies \hat x_H(t) = \hat x(0) + \frac{\hat p(0)}{m}t - \frac{1}{2}gt^2\hat 1$.
>     (c) Taking expectation values in any state $|\psi\rangle$:
>     $\langle x\rangle(t) = \langle x\rangle_0 + \frac{\langle p\rangle_0}{m}t - \frac{1}{2}gt^2$.
>     This is the exact classical kinematic formula for projectile motion under gravity.

---

## Provenance

> [!provenance]- Source map for this chapter
> | Section & Topic | Primary Book Source | Syllabus / Chapter Connections | Scope |
> |---|---|---|---|
> | §1 Physical motivation, ket space axioms, superposition, observables | Sakurai & Napolitano §1.1–1.2 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf\|Sakurai PDF]]); Shankar §1.1–1.3 | [[QM03 States Operators and Measurement]] §1–2 | extra/book |
> | §2 Dual space, bra vectors, DC machine, inner product axioms, Schwarz proof | Sakurai §1.2–1.3; Griffiths §3.2 ([[Griffiths - Introduction to quantum mechanics.pdf\|PDF pp.95–115]]) | [[QM03 States Operators and Measurement]] §4 | extra/book |
> | §3 Linear operators, outer product dyad, completeness relation, commutator algebra | Sakurai §1.2–1.3; Dirac *Principles* Ch. 1 | [[QM05 The Harmonic Oscillator]] §2–3; [[QM06 The Oscillator Toolbox]] §2 | extra/book |
> | §4 Adjoint properties, Hermitian observables, full proofs of real eigenvalues & orthogonality | Sakurai §1.3; Griffiths §3.2 | [[QM05 The Harmonic Oscillator]] §10 (Tutorial III Q3) | extra/book |
> | §5 Basis expansion, matrix representations, unitary change of basis $U X U^\dagger$ | Sakurai §1.3–1.4; Shankar §1.5–1.8 | [[QM03 States Operators and Measurement]] §6; [[QM06 The Oscillator Toolbox]] §2 | extra/book |
> | §6 Continuous position/momentum eigenkets, translation derivation of $\hat p$, plane wave, Gaussian packet | Sakurai §1.6–1.7; Griffiths §3.4; Shankar §1.10 | [[QM05 The Harmonic Oscillator]] §8; [[Gaussian Integral]] | extra/book |
> | §7 Unitary operators, translation operator $\mathcal{T}(a) = e^{-i\hat p a/\hbar}$, CCR $[\hat x,\hat p]=i\hbar$ | Sakurai §1.6; Shankar §1.6 | [[Canonical Commutation Relation]]; [[QM03 States Operators and Measurement]] §5 | extra/book |
> | §8 Measurement postulate, compatible observables, CSCO, full Robertson derivation | Sakurai §1.4–1.5; Griffiths §3.4–3.5 | [[QM03 States Operators and Measurement]] §4–5 | extra/book |
> | §9 Time-evolution operator, Schrödinger equation derivation, stationary states, beats | Sakurai §2.1; Griffiths §2.1; Shankar §4.1 | [[QM02 The Schrodinger Equation and Stationary States]]; [[QM05 The Harmonic Oscillator]] §6 | extra/book |
> | §10 Heisenberg picture, Heisenberg equation of motion, quantum Hamilton's equations, Ehrenfest | Sakurai §2.2; Shankar §4.3; Cohen-Tannoudji Ch. III | [[QM06 The Oscillator Toolbox]] §6 | extra/beyond |
> | Full algebraic proofs, 2×2 numerical matrices, qubit spin examples, 10 practice problems with solutions | Written and computed explicitly for this foundations treatise | Cross-vault integration | extra/beyond |
>
> **Methodology and notes:**
> - The chapter follows the structural backbone of J. J. Sakurai and J. Napolitano (*Modern Quantum Mechanics*, 3rd ed., Cambridge University Press, 2020), Chapters 1 and 2.1–2.2.
> - Supplemental treatments and pedagogical proofs were adapted from D. J. Griffiths (*Introduction to Quantum Mechanics*, 1st/2nd eds., Prentice Hall), R. Shankar (*Principles of Quantum Mechanics*, 2nd ed., Plenum Press), and C. Cohen-Tannoudji, B. Diu, and F. Laloë (*Quantum Mechanics*, Vol. 1, Wiley-Interscience).
> - Every proof has been carried out step-by-step with zero skipped algebra: the Cauchy–Schwarz inequality, the reality of Hermitian eigenvalues, the mutual orthogonality of distinct eigenstates, the translation operator derivation of momentum $\hat p \leftrightarrow -i\hbar\partial_x$, the canonical commutation relation $[\hat x, \hat p] = i\hbar$, the Robertson uncertainty inequality, the infinitesimal generator derivation of Schrödinger's equation, and the Heisenberg equation of motion.
> - All numerical examples (qubits, two-level matrices, Gaussian wave packets, harmonic oscillator ladders) were calculated and verified for internal consistency.

**References.** Sakurai, J. J. and Napolitano, J. *Modern Quantum Mechanics* (3rd ed.), Ch. 1 and §2.1 · Griffiths, D. J. *Introduction to Quantum Mechanics* (1st ed.), Ch. 3 · Shankar, R. *Principles of Quantum Mechanics* (2nd ed.), Ch. 1 · Cohen-Tannoudji, C., Diu, B. and Laloë, F. *Quantum Mechanics* Vol. 1, Ch. II · Dirac, P. A. M. *The Principles of Quantum Mechanics* (4th ed.), Ch. 1.
