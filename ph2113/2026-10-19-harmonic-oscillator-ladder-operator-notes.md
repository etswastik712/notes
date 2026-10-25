---
id: ph2113/2026-10-19-harmonic-oscillator-ladder-operator-notes
aliases: ["Quantum harmonic oscillator: ladder-operator notes (19 October 2026)"]
tags: []
trust_tier: agent_written
---

# Quantum harmonic oscillator: ladder-operator notes (19 October 2026)

## Covered
Source: handwritten class notes (Classroom: Harmonic_oscillator.pdf). The scan text is badly garbled, so the points below are the ones that could be read reliably; check against the PDF.

**Setting.** Classical mechanics: pendulum, spring-mass system. The notes open with the question of where the classical probability distribution is peaked.

**Factorising the Hamiltonian.** $\hat H=\frac1{2m}\left[\hat p^2+(m\omega\hat x)^2\right]$. Using $a^2+b^2=(ia+b)(-ia+b)$ idea (as in the notes, $a^2-b^2=(a+b)(a-b)$ with $i$ inserted) the operators
$\hat a_\pm=\frac1{\sqrt{2\hbar m\omega}}(\mp i\hat p+m\omega\hat x)$
are defined; the notes also note that $\hat p$ and $\hat x$ do not commute, so the factorisation leaves a commutator term:
- $[\hat a_-,\hat a_+]=1$.
- $\hat H=\hbar\omega\left(\hat a_+\hat a_-+\tfrac12\right)=\hbar\omega\left(\hat a_-\hat a_+-\tfrac12\right)$.
- Inverse relations: $\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a_++\hat a_-)$, $\hat p=i\sqrt{\frac{\hbar m\omega}{2}}(\hat a_+-\hat a_-)$.

**Ladder property.** Let $\psi_n$ satisfy $\hat H\psi_n=E_n\psi_n$ (existence of eigenstates not yet shown at that point). Then
- $\hat H(\hat a_+\psi_n)=(E_n+\hbar\omega)(\hat a_+\psi_n)$,
- $\hat H(\hat a_-\psi_n)=(E_n-\hbar\omega)(\hat a_-\psi_n)$.
Proof pattern: write $\hat H\hat a_+=\hat a_+(\hat H+\hbar\omega)$ using $[\hat a_-,\hat a_+]=1$, and similarly for $\hat a_-$.
Consequences:
1. If $\psi_n$ is an eigenstate, so are $\hat a_+\psi_n$, $\hat a_-\psi_n$, and repeated applications $(\hat a_\pm)^k\psi_n$.
2. Eigenvalues are separated by $\hbar\omega$, the energy unit of the system. Knowing one eigenstate, all others follow by raising and lowering.

**Ground state.** Since $V(x)\ge0$ there is a minimum-energy state $\psi_0$; lowering cannot go below it, so $\hat a_-\psi_0=0$ (the alternative, a non-physical state, is excluded).
- $\hat a_-\psi_0=0\Rightarrow\left(\hbar\frac{d}{dx}+m\omega x\right)\psi_0=0$, a first-order differential equation, solved by $\psi_0(x)=Ae^{-m\omega x^2/2\hbar}$.
- Normalisation $\int\psi_0^*\psi_0\,dx=1$ (Gaussian integral): $A=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}$.
- Ground-state energy: $\hat H\psi_0=\hbar\omega(\hat a_+\hat a_-+\tfrac12)\psi_0=\tfrac12\hbar\omega\,\psi_0$, so $E_0=\tfrac12\hbar\omega$.

**Higher states.** $\psi_n=A_n(\hat a_+)^n\psi_0$, $E_n=\hbar\omega\left(n+\tfrac12\right)$.

**Useful identity** (moving $\hat a_\pm$ across an integral): $\int f^*(\hat a_\pm g)\,dx=\int(\hat a_\mp f)^*g\,dx$, i.e. $\hat a_+$ and $\hat a_-$ are Hermitian conjugates of each other. It follows from integration by parts (boundary terms vanish) and gives $\hat a_\pm^\dagger=\hat a_\mp$.

**Normalisation of $A_n$.** From $E_n=\hbar\omega(n+\frac12)$ and $\int\psi_n^*\hat H\psi_n=E_n$ one gets $\int|\hat a_-\psi_n|^2dx=n$ and $\int|\hat a_+\psi_n|^2dx=n+1$, hence
- $\hat a_+\psi_n=\sqrt{n+1}\,\psi_{n+1}$,
- $\hat a_-\psi_n=\sqrt n\,\psi_{n-1}$,
- $\psi_n=\frac1{\sqrt{n!}}(\hat a_+)^n\psi_0$.

**Expectation values.** With $\hat x$, $\hat p$ in terms of $\hat a_\pm$:
- $\langle\hat p\rangle=\int\psi_n^*\hat p\,\psi_n\,dx\propto\int\psi_n^*(\hat a_+-\hat a_-)\psi_n\,dx=0$ (orthogonality, $\psi_{n\pm1}\perp\psi_n$).
- $\langle\hat p^2\rangle$: expand $-(\hat a_+-\hat a_-)^2$; the $\hat a_\pm^2$ terms vanish and the cross terms give $\hat a_+\hat a_-$ and $\hat a_-\hat a_+$, i.e. a result $\propto(2n+1)$. The last lines of the scan are illegible; the closed form $\langle\hat p^2\rangle=\hbar m\omega(n+\tfrac12)$ is what this pattern gives, not read from the page.

## From the post
Notes from the Simple Harmonic Oscillator.

## Files
- [Harmonic_oscillator.pdf](https://drive.google.com/file/d/1Zlz_9283o-N01ENFNuArrjOh8W-Kr58x/view?usp=drive_web): handwritten scan; text extraction is partly garbled (several equations reconstructed from context).

## Related
- [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators]]: problem set on these results (lowering property, $\psi_1,\psi_2$, ground-state uniqueness)
- [[ph2113/2026-10-19-tutorial-iii-harmonic-oscillator-expectation-values]]: problem set using $\langle p^2\rangle$, $\langle x\rangle$ and orthogonality
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: the earlier bound-state spectrum
- [[06-quantum-mechanics/qm05-the-harmonic-oscillator]]: your own oscillator notes
- [[06-quantum-mechanics/concepts/ladder-operators]]: your concept note on $\hat a_\pm$
- [[06-quantum-mechanics/concepts/number-operator]]: $\hat a_+\hat a_-\psi_n=n\psi_n$
- [[06-quantum-mechanics/concepts/canonical-commutation-relation]]: source of $[\hat a_-,\hat a_+]=1$
