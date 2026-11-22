---
title: PH2113 Past Papers 2025 - Solved
aliases: [PH2113 2025, quantum midsem 2025, quantum endsem 2025]
subject: qm
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/qm, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# PH2113 Past Papers 2025: Mid-sem and End-sem, Solved

[[Quantum Mechanics - Course Map|Course Map]] · [[Quantum Mechanics Quiz Prep]] · other years: [[PH2113 Past Papers 2021 - Solved|2021]] · [[PH2113 Past Papers 2022 - Solved|2022]] · [[PH2113 Past Papers 2023 - Solved|2023]] · [[PH2113 Past Papers 2024 - Solved|2024]]

<span class="scope-taught">taught · past papers (last year's run)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3 → Sem-3 Papers (Aug 2025)**, downloaded 2026-11-22 to `physics/quantum-mechanics/lecture-notes-slides/past-papers/qp-archive/`:
> - **Mid-sem**, 24 Sep 2025, 75 marks, Diptimoy Ghosh, closed book: [[Introductory Quantum __Physics.pdf]] (`Mid Sem/`, scan).
> - **End-sem**: [[Introductory Quantum Mechanics.pdf]] (`End Sem/`, scan). It has 3 pages: Section A (short, 28) and Section B (long, 72). The cover page with date and instructors is not in the file. The layout matches the 2024 end-sem.
>
> No keys: solutions mine. Numbers: `scripts/qm_qp_archive_numbers.py`.

## Mid-semester (24 Sep 2025)

> [!question] Q1 (5) · A potassium plate 1 m from a 1 W isotropic source; an electron collects energy from a circle of radius $10^{-10}$ m; work function 2.1 eV. Classically, how long until it can escape?

> [!example]- Solution ([[QM01 From Waves to Probabilities]])
> Intensity $I=P/4\pi r^2=0.080$ W m⁻²; collecting area $\pi(10^{-10})^2=3.1\times10^{-20}$ m²; power $2.5\times10^{-21}$ W. $t=3.4\times10^{-19}/2.5\times10^{-21}=$ **136 s ≈ 2 min**. Experiment shows **no measurable delay** (< 10⁻⁹ s), which is evidence for photons: the energy arrives in lumps $h\nu$.

> [!question] Q2 (5) · 420 nm and 630 nm beams of equal intensity; the first delivers 12 × 10¹⁶ photons s⁻¹ cm⁻². The second?

> [!example]- Solution
> Equal intensity = equal $N\,hc/\lambda$ ⇒ $N\propto\lambda$: $N_2=12\times10^{16}\times\frac{630}{420}=$ **1.8 × 10¹⁷ photons s⁻¹ cm⁻²**.

> [!question] Q3 (3) · $\psi=Ae^{ikx}+Be^{-ikx}$ for $x<0$, $Ce^{-ikx}$ for $x>0$. Show $A+B=C$.

> [!example]- Solution ([[QM02 The Schrodinger Equation and Stationary States]])
> ψ must be **continuous** at $x=0$ (finite potential; otherwise $\psi''$ would contain δ′ and the kinetic energy would diverge): $\psi(0^-)=A+B=\psi(0^+)=C$.

> [!question] Q4 (4) · $|\psi(0)\rangle=\frac1{\sqrt6}|\phi_1\rangle+\frac1{\sqrt3}|\phi_2\rangle+\sqrt{\tfrac12}|\phi_3\rangle$ (stationary states, energies $E_i$). $|\psi(t)\rangle$?

> [!example]- Solution
> $|\psi(t)\rangle=\frac1{\sqrt6}e^{-iE_1t/\hbar}|\phi_1\rangle+\frac1{\sqrt3}e^{-iE_2t/\hbar}|\phi_2\rangle+\frac1{\sqrt2}e^{-iE_3t/\hbar}|\phi_3\rangle$ (already normalised: $\tfrac16+\tfrac13+\tfrac12=1$).

> [!question] Q5 (10) · Show $\frac d{dt}\int\Psi_1^*\Psi_2\,dx=0$ for any two normalisable solutions with the same $V$.

> [!example]- Solution ([[QM03 States Operators and Measurement]])
> $\partial_t\Psi=\frac1{i\hbar}H\Psi$ and $\partial_t\Psi^*=-\frac1{i\hbar}(H\Psi)^*$ ($V$ real). So $\frac d{dt}\int\Psi_1^*\Psi_2=\frac1{i\hbar}\big[\int\Psi_1^*H\Psi_2-\int(H\Psi_1)^*\Psi_2\big]=0$, because $H$ is **Hermitian**. To show the Hermiticity of the kinetic term, integrate by parts twice; the boundary terms vanish for normalisable states. The $V$ terms cancel directly. Inner products, hence probabilities, are preserved: unitary evolution.

> [!question] Q6 (28) · Infinite well, $n$-th state: $\langle x\rangle$, $\langle x^2\rangle$, $\langle p\rangle$, $\langle p^2\rangle$, $\sigma_x$, $\sigma_p$. Check the uncertainty principle; which state is closest to the limit?

> [!example]- Solution ([[QM04 The Particle in a Box]])
> Box $[0,a]$, $\psi_n=\sqrt{2/a}\sin(n\pi x/a)$.
> - $\langle x\rangle=a/2$, $\langle x^2\rangle=a^2\Big(\dfrac13-\dfrac1{2n^2\pi^2}\Big)$.
> - $\langle p\rangle=0$, $\langle p^2\rangle=\dfrac{n^2\pi^2\hbar^2}{a^2}$.
> - $\sigma_x=a\sqrt{\dfrac1{12}-\dfrac1{2n^2\pi^2}}$, $\sigma_p=\dfrac{n\pi\hbar}a$.
> - $\sigma_x\sigma_p=\dfrac\hbar2\sqrt{\dfrac{n^2\pi^2}3-2}$: **0.568ħ** ($n=1$), 1.67ħ, 2.63ħ, …, always > ħ/2.
>
> **The ground state comes closest.**

> [!question] Q7 (10) · Ground state of a box of length $L$; the box suddenly expands symmetrically to $2L$, ψ unchanged. Show $P(\text{new ground state})=(8/3\pi)^2$.

> [!example]- Solution ([[QM04 The Particle in a Box]], [[QM03 States Operators and Measurement]])
> Centre the boxes at 0. Old state $\psi=\sqrt{2/L}\cos(\pi x/L)$ on $|x|<L/2$; new ground state $\phi_1=\sqrt{1/L}\cos(\pi x/2L)$ on $|x|<L$.
> $$c_1=\frac{\sqrt2}L\int_{-L/2}^{L/2}\cos\frac{\pi x}L\cos\frac{\pi x}{2L}dx=\frac{\sqrt2}L\cdot\frac{4\sqrt2L}{3\pi}=\frac8{3\pi}.$$
> (Product-to-sum: $\tfrac12[\cos\frac{3\pi x}{2L}+\cos\frac{\pi x}{2L}]$, which integrates to $\frac{L}{3\pi}2\sqrt2+\frac L\pi2\sqrt2$, halved.) So $P=(8/3\pi)^2=$ **0.72** ✓ (checked numerically). For a one-sided expansion ($[0,L]\to[0,2L]$) it would be $32/9\pi^2=0.36$, which is why "symmetrically" matters.

> [!question] Q8 (10) · $\psi_p=(2\pi\hbar)^{-3/2}e^{i\mathbf p\cdot\mathbf r/\hbar}$: find $\mathbf j$ and the density, and compare with $\mathbf j=\rho\mathbf v$.

> [!example]- Solution ([[QM08 Quantum Tunnelling]])
> $\mathbf j=\frac\hbar{2mi}(\psi^*\nabla\psi-\psi\nabla\psi^*)=|\psi|^2\frac{\mathbf p}m=\dfrac1{(2\pi\hbar)^3}\dfrac{\mathbf p}m$, and $\rho=|\psi|^2=(2\pi\hbar)^{-3}$. So $\mathbf j=\rho\mathbf v$ with $\mathbf v=\mathbf p/m$, exactly the form of a classical (or EM charge) current: a density moving with the classical velocity. The momentum density $\rho\mathbf p=m\mathbf j$.

## End-semester (Nov 2025)

### Section A (short)
> [!example]- A1–A7
> - **A1** $\psi=A(\psi_1+2\psi_2)$ with orthonormal eigenstates: $A=$ **1/√5**. Unchanged for box states, which are also orthonormal.
> - **A2** Finite well, half-width $a$: $z_0=a\sqrt{2mV_0}/\hbar=3\pi$. Even states need $z_0>0,\pi,2\pi$: **3 even**; odd states need $z_0>\pi/2,3\pi/2,5\pi/2$: **3 odd**. **6 bound states** (a 7th appears only for $z_0>3\pi$; at exactly $3\pi$ it sits at threshold, unbound). ([[QM07 The Finite Square Well]])
> - **A3** $\psi=A\sin\theta$: $-i\hbar\,\partial_\theta\sin\theta=-i\hbar\cos\theta$, not ∝ $\sin\theta$. **Not an eigenstate**: $\sin\theta$ is a superposition of $m=+1$ and $-1$. ([[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]])
> - **A4** $E=V_0/2$: $\frac{V_0^2}{4E(V_0-E)}=1$, so $T=\dfrac1{1+\sinh^2(2a\sqrt{mV_0}/\hbar)}=\dfrac1{\cosh^2(2a\sqrt{mV_0}/\hbar)}$. With the argument equal to 1: $T=1/\cosh^21=$ **0.42**. ([[QM10 The Finite Barrier and Tutorial V]])
> - **A5** Double harmonic well meeting at a cusp at $x=0$. **Case 1** ($E_0$ deep in the wells): two Gaussian-like humps centred at $\pm a$; small but positive at $x=0$ (tunnelling region); even and nodeless. **Case 2** ($E_0'$ far above the barrier): one broad single hump, like an oscillator ground state; the cusp hardly matters (only a slight flattening near 0).
> - **A6** $\langle E\rangle=\tfrac12(E_n+E_m)=\frac{(n^2+m^2)\pi^2\hbar^2}{4ma^2}$. Setting this equal to $10\pi^2\hbar^2/2ma^2$ gives $n^2+m^2=20$: **$\{n,m\}=\{2,4\}$**.
> - **A7** **Yes, the same period**, $T=2\pi\hbar/\Delta E_1$: in a two-level superposition, ⟨x⟩ oscillates at the Bohr frequency $(E_2-E_1)/\hbar$, whatever the absolute energies. Caveat: if the two box states have the same parity, $\langle1|x|2\rangle$ vanishes and ⟨x⟩ does not oscillate.

### Section B (long)
> [!question] B1 (8 + 4 + 2 + 4) · Box, $\psi(x,0)=\tfrac12\psi_1+\tfrac1{\sqrt2}\psi_2+\tfrac1{2\sqrt2}\psi_3+\tfrac1{2\sqrt2}\psi_4$. (a) Outcomes and probabilities. (b) $\langle E\rangle$. (c) At later $t$? (d) If $E_2$ is found at $t=0$, what does a later measurement give?

> [!example]- Solution ([[QM04 The Particle in a Box]], [[QM03 States Operators and Measurement]])
> (a) $E_1,E_2,E_3,E_4$ with probabilities **1/4, 1/2, 1/8, 1/8** (sum 1).
> (b) $\langle E\rangle=E_1(\tfrac14+4\cdot\tfrac12+9\cdot\tfrac18+16\cdot\tfrac18)=$ **43/8 E₁ = 5.375 E₁**.
> (c) The same outcomes and probabilities: stationary components only acquire phases.
> (d) The state collapses to $\psi_2$, a stationary state, so a later measurement gives **E₂ with certainty**.

> [!question] B2 (5 + 2 + 7 + 4) · Oscillator, $\psi(x,0)=\frac1{\sqrt2}(\psi_0+\psi_1)$. (a) $\langle x\rangle$, $\langle p\rangle$ at $t=0$ with ladder operators. (b) $\psi(x,t)$. (c) $\langle x\rangle(t)$, $\langle p\rangle(t)$. (d) Check Ehrenfest $d\langle x\rangle/dt=\langle p\rangle/m$.

> [!example]- Solution ([[QM06 The Oscillator Toolbox]])
> $x=\sqrt{\hbar/2m\omega}(a_++a_-)$, $p=i\sqrt{m\hbar\omega/2}(a_+-a_-)$.
> (a) $\langle x\rangle=\sqrt{\dfrac\hbar{2m\omega}}$, $\langle p\rangle=0$.
> (b) $\psi(x,t)=\frac1{\sqrt2}\big(\psi_0e^{-i\omega t/2}+\psi_1e^{-3i\omega t/2}\big)$.
> (c) $\langle x\rangle=\sqrt{\dfrac\hbar{2m\omega}}\cos\omega t$, $\langle p\rangle=-\sqrt{\dfrac{m\hbar\omega}2}\sin\omega t$.
> (d) $\dfrac{d\langle x\rangle}{dt}=-\omega\sqrt{\dfrac\hbar{2m\omega}}\sin\omega t=-\sqrt{\dfrac{\hbar\omega}{2m}}\sin\omega t=\langle p\rangle/m$ ✓.

> [!question] B3 (8 + 10) · Fixed energy $E<V_0$. (A) A single barrier of width $a$. (B) Two barriers of width $a/2$ separated by a well. (a) Sketch the wavefunctions. (b) Explain resonant transmission in B, and sketch $T$ against barrier separation from zero (= A) to infinity.

> [!example]- Solution ([[QM10 The Finite Barrier and Tutorial V]], [[QM08 Quantum Tunnelling]])
> (a)
> - **A**: on the left, incident plus reflected waves (a partial standing wave, amplitude modulated); inside, an exponential decay (plus a small growing part); on the right, a small transmitted plane wave with constant $|\psi|$.
> - **B**: the same pattern, plus an oscillating piece in the well between the barriers, followed by a second decay.
>
> (b) The well between the barriers has **quasi-bound levels** $E_n(d)$, which fall as the separation $d$ grows (more levels, more closely spaced).
> - Off resonance, the two barriers act in series: $T\sim T_1T_2$, small, *smaller* than for the single barrier A.
> - When a level crosses the incident energy ($E_n(d)=E$), waves bouncing in the well interfere constructively. Transmission is strongly enhanced, up to **T = 1 for identical barriers** (resonant tunnelling).
>
> Plot of $T$ against $d$: at $d=0$ the single-barrier value $T_A$; then a low baseline punctuated by **sharp peaks** (each reaching ~1) whenever $E_n(d)=E$. The peaks become more frequent at large $d$ (roughly when the well holds a whole number of half-wavelengths, $kd\approx n\pi$) and narrower as the barriers confine the levels better.

> [!question] B4 (3 + 6 + 2 + 7) · $\psi(x,0)=(\pi\sigma^2)^{-1/4}e^{-x^2/2\sigma^2}$. (a) Sketch $|\psi|^2$. (b) $\tilde\psi(p,0)$. (c) $\tilde\psi(p,t)$ for a free particle. (d) $\psi(x,t)$ by inverse transform; interpret.

> [!example]- Solution ([[QM02 The Schrodinger Equation and Stationary States]])
> (a) A Gaussian $|\psi|^2=\frac1{\sqrt\pi\sigma}e^{-x^2/\sigma^2}$, centred at 0, with standard deviation $\sigma/\sqrt2$.
> (b) $\tilde\psi(p,0)=\Big(\dfrac{\sigma^2}{\pi\hbar^2}\Big)^{1/4}e^{-p^2\sigma^2/2\hbar^2}$.
> (c) $E=p^2/2m$: $\tilde\psi(p,t)=\tilde\psi(p,0)\,e^{-ip^2t/2m\hbar}$; $|\tilde\psi|^2$ does not change.
> (d) $\psi(x,t)=\dfrac{(\pi\sigma^2)^{-1/4}}{\sqrt{1+i\hbar t/m\sigma^2}}\exp\Big[-\dfrac{x^2}{2\sigma^2(1+i\hbar t/m\sigma^2)}\Big]$. Hence $|\psi|^2$ is a Gaussian of width $\sigma(t)=\sigma\sqrt{1+(\hbar t/m\sigma^2)^2}$: the packet **spreads**, faster for narrow packets and light particles; Δp stays constant. The complex width produces a position-dependent phase (a "chirp": faster components ahead).

## Topic map
| question | topic | vault |
|---|---|---|
| MS 1–2 | photoelectric delay, photon counting | [[QM01 From Waves to Probabilities]] |
| MS 3–5; ES B4 | continuity, time evolution, unitarity, wave packets | [[QM02 The Schrodinger Equation and Stationary States]], [[QM03 States Operators and Measurement]] |
| MS 6–7; ES A6, B1 | box | [[QM04 The Particle in a Box]] |
| ES A2, A5 | finite and double wells | [[QM07 The Finite Square Well]] |
| ES A4, B3; MS 8 | barriers, resonance, current | [[QM08 Quantum Tunnelling]], [[QM10 The Finite Barrier and Tutorial V]] |
| ES A1, A7, B2 | oscillator, ladder operators | [[QM05 The Harmonic Oscillator]], [[QM06 The Oscillator Toolbox]] |
| ES A3 | $L_z$ | [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | [[Introductory Quantum __Physics.pdf]], [[Introductory Quantum Mechanics.pdf]] (Drive QP archive, 2026-11-22; scans) | taught (past papers) |
> | numbers (MS 1, 2, 6, 7; ES A1, A4, B1) | `scripts/qm_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The end-sem's date and instructors (no cover page). ES A2's counting at exactly $z_0=3\pi$.
