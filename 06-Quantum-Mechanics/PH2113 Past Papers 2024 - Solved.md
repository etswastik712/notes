---
title: PH2113 Past Papers 2024 - Solved
aliases: [PH2113 2024, quantum midsem 2024, quantum endsem 2024, quantum quizzes 2024]
subject: qm
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/qm, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# PH2113 Past Papers 2024: Quizzes, Mid-sem and End-sem, Solved

[[Quantum Mechanics - Course Map|Course Map]] · [[Quantum Mechanics Quiz Prep]] · other years: [[PH2113 Past Papers 2021 - Solved|2021]] · [[PH2113 Past Papers 2022 - Solved|2022]] · [[PH2113 Past Papers 2023 - Solved|2023]] · [[PH2113 Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · past papers (Arka Banerjee, Sunil Mukhi)</span> <span class="scope-extra-beyond">extra · beyond (end-sem solutions and checks mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3**, downloaded 2026-11-22 to `physics/quantum-mechanics/lecture-notes-slides/past-papers/qp-archive/`:
> - **Quiz 1** (30 Aug 2024, 50 marks): question image `Sem - 3 Papers (Aug 2024)/Quiz/Quantum Mechanics/Quiz - 1`, and **the instructors' solutions** [[Quiz 1 -solved.pdf]].
> - **Mid-sem** (21 Sep 2024, 100 marks: Section A 72, Section B MCQs 28): [[Quantum Mechanics.pdf]] and **solutions** [[Quantum Mechanics - solved.pdf]] (`Mid Sem/`).
> - **Quiz 2** (25 Oct 2024, 40 marks): [[Quiz - 2.pdf]] and **solutions** [[Quiz - 2 _ solutions.pdf]].
> - **End-sem** (29 Nov 2024, 100 marks): `End Sem/Quantum Mechanics/Pg 1`–`Pg 4` (photos). **No solutions.**
> - [[Intro QM-All Papers 2024-Mukhi_Arka.pdf]] (`PH2113/`): a 9-page scan of all four papers (checked: the same papers).
>
> Where official solutions exist, the answers below **check** them (✓ or a flag) rather than re-derive. The end-sem is solved here. Numbers: `scripts/qm_qp_archive_numbers.py`.

## Quiz 1 (30 Aug 2024): official solutions checked
> [!example]- Q1–Q3
> 1. A neutron's momentum uncertainty kept to 0.0001 % of its thermal momentum $\sqrt{2m_nk_BT}$: $\Delta x\ge\dfrac{\hbar}{2\Delta p}=\dfrac{10^6h}{4\pi\sqrt{2m_nk_BT}}\approx$ **2 × 10⁻⁴/√T m** ✓ (I get 2.4 × 10⁻⁴; the solution's "10¹⁶" is a typo for 10⁻⁶).
> 2. Particles through a biprism (width $d_1$, screen at $d_2$, fringe width $W$): $\lambda=Wd_1/d_2$, $p=h/\lambda$, $\nu=E/h=\dfrac{mc^2}h+\dfrac{hd_2^2}{2d_1^2W^2m}$ ✓ (the official answer keeps the rest-energy term).
> 3. Triangle $\psi=A(a-|x|)$ on $|x|\le a$: $A=\sqrt{3/2a^3}$, $\langle x\rangle=0$, $\langle x^2\rangle=a^2/10$, **Δx = a/√10** ✓.

## Mid-semester (21 Sep 2024): official solutions checked
> [!example]- Section A (72)
> - **A.1** $\psi=\tfrac1{\sqrt2}\psi_1+\tfrac1{\sqrt3}\psi_2$: norm² = 5/6, so $\psi=\sqrt{\tfrac35}\psi_1+\sqrt{\tfrac25}\psi_2$. $\Delta H=\sqrt{\tfrac35\cdot\tfrac25}\,(E_2-E_1)=$ **$\frac{\sqrt6}5(E_2-E_1)$** ✓ (for two levels with weights $p,1-p$, $\Delta H=\sqrt{p(1-p)}\,|E_2-E_1|$).
> - **A.2** The oscillator ground state in momentum space: $\tilde\psi(p)=(\pi m\hbar\omega)^{-1/4}e^{-p^2/2m\hbar\omega}$. $P(0<p<\sqrt{m\hbar\omega})=\frac1{\sqrt\pi}\int_0^1e^{-u^2}du=$ **0.42** ✓. ([[QM05 The Harmonic Oscillator]])
> - **A.3** $\psi=e^{ax-bx^2}$: $V=\dfrac{\hbar^2}{2m}(a-2bx)^2$ (up to a constant), $E=\hbar^2b/m$ above the minimum ✓. It is an oscillator with $m\omega/2\hbar=b$, i.e. $E=\hbar\omega/2$, consistent.
> - **A.4** Two free momentum states: $|\psi|^2$ oscillates at $\omega=|p_2^2-p_1^2|/2m\hbar$, period **$4\pi m\hbar/|p_2^2-p_1^2|$** ✓.
>
> **Section B** (MCQs, +4/−1), answers as in the official sheet:
> - B.1: the time-independent SE is a special case of the time-dependent one ✓;
> - B.2: $v_g=\sqrt{g/4k}$ for $\omega=\sqrt{gk}$ ✓;
> - B.3: Rayleigh–Jeans works for $h\nu\ll k_BT$ ✓;
> - B.4: false for a free stationary state: "energies quantised" ✓;
> - B.5: the product of two stationary states is not a valid state ✓;
> - B.6: Δx in an oscillator eigenstate is constant in time ✓;
> - B.7: each click's energy grows when the wavelength decreases ✓.

## Quiz 2 (25 Oct 2024): official solutions checked
> [!example]- Q1–Q3
> 1. $\psi=\tfrac12\psi_1+\tfrac12\psi_2+\tfrac1{\sqrt2}\psi_3$: $P(E_3=9\pi^2\hbar^2/2ma^2)=$ **1/2**, at $t=0$ and at all later times (stationary amplitudes only change phase) ✓.
> 2. $\psi_a=Ax(a-x)$ is symmetric about $a/2$, so only $n$ = 1, 3, 5, … occur; $\psi_b=Bx(a-x)(a/2-x)$ is antisymmetric, so only $n$ = 2, 4, … ✓. **[!verify] Slip in the solution**: it writes the energies as $(2n+1)\pi^2\hbar^2/2ma^2$ and $(2n)\pi^2\hbar^2/2ma^2$. Box energies go as $n^2$: it should be $(2n+1)^2\pi^2\hbar^2/2ma^2$ and $(2n)^2\pi^2\hbar^2/2ma^2$.
> 3. Coherent state $a_-\psi_\alpha=\alpha\psi_\alpha$ ($m=\omega=1$): $\langle x\rangle=\sqrt{\hbar/2}(\alpha+\alpha^*)$, $\langle p\rangle=i\sqrt{\hbar/2}(\alpha^*-\alpha)$, $\langle x^2\rangle=\tfrac\hbar2[(\alpha+\alpha^*)^2+1]$, $\langle p^2\rangle=\tfrac\hbar2[1-(\alpha^*-\alpha)^2]$. Hence $\Delta x\Delta p=$ **ħ/2 for every α**: minimum-uncertainty states ✓. ([[QM06 The Oscillator Toolbox]])

## End-semester (29 Nov 2024): solved

### Section A (short, 4 marks each)
> [!example]- A1–A7
> - **A1** $a_+a_-\psi_n=a_+\sqrt n\psi_{n-1}=\sqrt n\sqrt n\psi_n$: eigenvalue **n** (the number operator; $H=\hbar\omega(a_+a_-+\tfrac12)$). ([[QM06 The Oscillator Toolbox]])
> - **A2** $\psi_{100}\propto e^{-r/a_0}$ is maximal at $r=0$ and decays with scale $a_0$. $r^2|\psi_{100}|^2\propto r^2e^{-2r/a_0}$ is zero at the origin and **peaks at $r=a_0$**. ([[QM12 The Hydrogen Atom]])
> - **A3** **No.** $\cos2\phi=\tfrac12(e^{2i\phi}+e^{-2i\phi})$ is a superposition of $L=+2\hbar$ and $-2\hbar$. ($-i\hbar\partial_\phi\cos2\phi=2i\hbar\sin2\phi$, not ∝ $\cos2\phi$.) It *is* an eigenstate of $L^2_z$, with $4\hbar^2$. ([[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]])
> - **A4** $T=1$ when $\sin(2ka)=0$, i.e. $2ka=n\pi$: $E=\dfrac{n^2\pi^2\hbar^2}{8ma^2}$ ($n=1,2,\dots$, with $E>V_0$). This is **transmission resonance**: the well holds a whole number of half-wavelengths. [!verify] The sheet defines $k=\sqrt{2mE}/\hbar$; for a well of depth $V_0$ the wavenumber inside is normally $\sqrt{2m(E+V_0)}/\hbar$, and the prefactor $V_0^2/4E(E-V_0)$ is the barrier form. The condition $\sin(2k_{inside}a)=0$ is the general statement. ([[QM10 The Finite Barrier and Tutorial V]])
> - **A5** Ground state of the symmetric double well: **even, nodeless**. Two cos-like humps, one in each well; in the central barrier ($|x|<b$) it sags but stays positive as a cosh; outside $|x|>a$ it decays exponentially. ([[QM07 The Finite Square Well]])
> - **A6** **Zero**: box eigenfunctions are real (up to a constant phase), so $\psi^*\psi'-\psi\psi^{*\prime}=0$. They are standing waves with equal flow both ways. ([[QM08 Quantum Tunnelling]])
> - **A7** $E_1=\dfrac{\pi^2\hbar^2}{2m^*a^2}$ with $a=5$ nm. For the free mass, $E_1=0.0150$ eV, so $m^*/m_e=0.0150/E_1$. With **600 meV**: $m^*\approx$ **0.025 mₑ**. [!verify] The sheet says "600 eV", which would give an absurd $2.5\times10^{-5}m_e$; meV must be meant. ([[QM04 The Particle in a Box]])

### Section B (long)
> [!question] B1 (3 + 3 + 6 + 3 + 3) · Box: $\psi(x,0)=\frac1{\sqrt2}(\psi_1-\psi_2)$. (a) Sketch ψ and |ψ|². (b) $\psi(x,t)$. (c) Sketch at $t=\pi\hbar/E_1$ (the sheet's $\pi/\hbar E_1$ was corrected in class).

> [!example]- Solution ([[QM04 The Particle in a Box]], [[QM02 The Schrodinger Equation and Stationary States]])
> (a) $\psi_1-\psi_2$ is positive and large on the **left** half, where the sine of $\psi_2$ adds, and small on the right; $|\psi|^2$ is a lopsided hump concentrated at $x<a/2$.
> (b) $\psi(x,t)=\frac1{\sqrt2}\big(\psi_1e^{-iE_1t/\hbar}-\psi_2e^{-iE_2t/\hbar}\big)$, $E_2=4E_1$.
> (c) At $t=\pi\hbar/E_1$: $e^{-i\pi}=-1$ and $e^{-4i\pi}=1$, so $\psi=-\frac1{\sqrt2}(\psi_1+\psi_2)$. Up to a global sign this is the **mirror image**: the hump has moved to the **right** half. $|\psi|^2$ sloshes back and forth with period $2\pi\hbar/(E_2-E_1)=2\pi\hbar/3E_1$.

> [!question] B2 (2 + 4 + 4 + 8) · An oscillator in its ground state; at $t_0$ the parameters change suddenly, $\omega\to2\omega$ and $m\to m/2$, with ψ unchanged. (a) The new $H$. (b) $\langle E\rangle$ after $t_0$. (c) Stationary? (d) Same, but only $\omega\to2\omega$.

> [!example]- Solution ([[QM05 The Harmonic Oscillator]])
> Old ground state: $\langle p^2\rangle=m\hbar\omega/2$, $\langle x^2\rangle=\hbar/2m\omega$.
> (a) $H'=\dfrac{p^2}{2(m/2)}+\tfrac12\dfrac m2(2\omega)^2x^2=\dfrac{p^2}m+m\omega^2x^2$.
> (b) $\langle H'\rangle=\dfrac{m\hbar\omega/2}m+m\omega^2\dfrac\hbar{2m\omega}=$ **ħω**.
> (c) **Yes.** The ground-state Gaussian depends only on the product $m\omega$, and $m'\omega'=\tfrac m2\cdot2\omega=m\omega$. So the old ψ *is* the new ground state, with energy $\tfrac12\hbar\omega'=\hbar\omega$, consistent with (b).
> (d) $H''=\dfrac{p^2}{2m}+2m\omega^2x^2$: $\langle H''\rangle=\dfrac{\hbar\omega}4+2m\omega^2\dfrac\hbar{2m\omega}=$ **$\tfrac54\hbar\omega$**. That is above the new ground energy $\hbar\omega$. The state is too wide for the stiffer well, so it is not stationary: it "breathes".

> [!question] B3 (5 + 5 + 3 + 5) · $\psi(x,t)=(C/\pi)^{1/4}e^{iG(t)x/\hbar}e^{-\frac C2(x-F(t))^2}$, $C$ constant, $F$ and $G$ real. (a) $\langle x\rangle$, $\langle p\rangle$. (b) With Ehrenfest, find $G$ if $F=A_0\cos\Gamma t$. (c) The equation for $\langle x\rangle$, and the potential.

> [!example]- Solution ([[QM06 The Oscillator Toolbox]], [[QM03 States Operators and Measurement]])
> (a) $|\psi|^2$ is a normalised Gaussian centred at $F$: $\langle x\rangle=F(t)$. The phase $e^{iGx/\hbar}$ shifts momentum by $G$, and the real Gaussian has zero mean momentum: $\langle p\rangle=G(t)$.
> (b) $\langle p\rangle=m\,d\langle x\rangle/dt$ ⇒ $G(t)=-mA_0\Gamma\sin\Gamma t$.
> (c) $\dfrac{d^2\langle x\rangle}{dt^2}=-\Gamma^2\langle x\rangle$, and Ehrenfest's $m\ddot{\langle x\rangle}=-\langle V'\rangle$ ⇒ $V=\tfrac12m\Gamma^2x^2$: **a harmonic oscillator of frequency Γ**. (This is a coherent state: a rigidly oscillating Gaussian, as in Quiz 2 Q3.)

> [!question] B4 (3 + 7 + 3 + 5) · A particle on a ring of radius $R$ (2-D polar Schrödinger equation). (a) The simplified equation. (b) The general single-valued solution and the energies. (c) Normalised eigenfunctions. (d) Angular momentum eigenvalues; how many angular-momentum eigenstates per energy?

> [!example]- Solution ([[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]])
> (a) With $r=R$ fixed and $V$ constant (take 0): $-\dfrac{\hbar^2}{2mR^2}\dfrac{d^2\psi}{d\phi^2}=E\psi$.
> (b) $\psi=Ae^{i\ell\phi}+Be^{-i\ell\phi}$. Single-valuedness $\psi(\phi+2\pi)=\psi(\phi)$ ⇒ $\ell\in\mathbb Z$. $E_\ell=\dfrac{\hbar^2\ell^2}{2mR^2}$.
> (c) $\psi_\ell=\dfrac1{\sqrt{2\pi}}e^{i\ell\phi}$ (normalised over φ; per unit arc length, $1/\sqrt{2\pi R}$).
> (d) $L_z=\ell\hbar$, $\ell=0,\pm1,\pm2,\dots$. Each energy with $\ell\ne0$ has **two** angular-momentum eigenstates ($\pm\ell$, clockwise and anticlockwise); $E=0$ has one.

## Topic map
| paper | topic | vault |
|---|---|---|
| Quiz 1 | uncertainty, matter-wave interference, normalisation | [[QM01 From Waves to Probabilities]], [[QM03 States Operators and Measurement]] |
| Mid-sem | superpositions, ΔH, momentum space, inverse problems, free particles | [[QM02 The Schrodinger Equation and Stationary States]], [[QM05 The Harmonic Oscillator]] |
| Quiz 2 | box measurements, parity, coherent states | [[QM04 The Particle in a Box]], [[QM06 The Oscillator Toolbox]] |
| End-sem A | ladder operators, H atom, $L_z$, resonances, double well, current, quantum well | [[QM06 The Oscillator Toolbox]], [[QM07 The Finite Square Well]], [[QM10 The Finite Barrier and Tutorial V]], [[QM12 The Hydrogen Atom]] |
| End-sem B | box dynamics, sudden change, Ehrenfest, the ring | [[QM04 The Particle in a Box]], [[QM05 The Harmonic Oscillator]], [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | quiz 1, mid-sem and quiz 2 with official solutions | [[Quiz 1 -solved.pdf]], [[Quantum Mechanics - solved.pdf]], [[Quiz - 2.pdf]], [[Quiz - 2 _ solutions.pdf]] (text layer, read in full) | taught (instructors' solutions) |
> | end-sem | `End Sem/Quantum Mechanics/Pg 1–4` and [[Intro QM-All Papers 2024-Mukhi_Arka.pdf]] (images) | taught (past paper) |
> | checks and end-sem solutions | mine; `scripts/qm_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] Quiz 2 Q2 is missing the squares in the energies. End-sem A4's $k$ definition. End-sem A7's "600 eV" (meV meant).
