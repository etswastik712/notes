---
title: PH2113 Past Papers 2022 - Solved
aliases: [PH2113 2022, quantum midsem 2022, quantum endsem 2022]
subject: qm
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/qm, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# PH2113 Past Papers 2022: Mid-sem and End-sem, Solved

[[Quantum Mechanics - Course Map|Course Map]] · [[Quantum Mechanics Quiz Prep]] · other years: [[PH2113 Past Papers 2021 - Solved|2021]] · [[PH2113 Past Papers 2023 - Solved|2023]] · [[PH2113 Past Papers 2024 - Solved|2024]] · [[PH2113 Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · past papers (Bhas Bapat, Sourabh Dube)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3 → PH2113**, downloaded 2026-11-22 to `physics/quantum-mechanics/lecture-notes-slides/past-papers/qp-archive/PH2113/`. Each paper is there twice, as two scans with different file names (checked to be identical in content):
> - **Mid-sem**, 29 Sep 2022, 30 marks: [[PH2113_midsem_22.pdf]] = [[QuantumPhys_Midsem_Aug22_Bhas-Sourabh.pdf]]. Part A: all 3 (4 marks each); Part B: any 2 of 4 (6 each); Part C: any 1 of 2 (6).
> - **End-sem**, 26 Nov 2022, 80 marks: [[PH2113_endsem_22.pdf]] = [[QuantumPhys_Endsem_Aug22_Bhas-Sourabh.pdf]], 5 questions, with constants given ($m_p$ rounded to 2 × 10⁻²⁷ kg).
>
> No keys: solutions mine. Numbers: `scripts/qm_qp_archive_numbers.py`.

## Mid-semester (29 Sep 2022)

> [!question] A1 (4) · From Planck's spectral radiance, show the total power radiated by a blackbody ∝ T⁴ (use $\int_0^\infty\frac{x^3}{e^x-1}dx=\frac{\pi^4}{15}$).

> [!example]- Solution ([[QM01 From Waves to Probabilities]])
> $u=\int_0^\infty\frac{8\pi h\nu^3}{c^3}\frac{d\nu}{e^{h\nu/kT}-1}$. Put $x=h\nu/kT$: $u=\frac{8\pi(kT)^4}{c^3h^3}\int\frac{x^3dx}{e^x-1}=\frac{8\pi^5k^4}{15c^3h^3}T^4$. The emitted power per area is $\frac c4u=\sigma T^4$, with $\sigma=\frac{2\pi^5k^4}{15c^2h^3}=5.67\times10^{-8}$ W m⁻² K⁻⁴. All the $T$ dependence comes out of the integral through the scaling $x=h\nu/kT$.

> [!question] A2 (4) · An electron has de Broglie wavelength 0.022 nm. The group velocity and the wave (phase) velocity of its matter wave?

> [!example]- Solution
> $p=h/\lambda=3.0\times10^{-23}$ kg m/s. **Group velocity = particle velocity** $v=p/m=$ **3.3 × 10⁷ m/s** (0.11 c: non-relativistic to ~1 %). The phase velocity depends on what is called $E$:
> - with the kinetic energy, $v_{ph}=E/p=v/2=$ **1.65 × 10⁷ m/s**;
> - with the total energy, $v_{ph}=c^2/v=$ **2.7 × 10⁹ m/s** (> c, harmless; see [[PH2113 Past Papers 2021 - Solved|2021]] D6).

> [!question] A3 (4) · In 1-D the wavefunction is real. Is it dimensionless? If not, its dimensions? What does it mean?

> [!example]- Solution ([[QM03 States Operators and Measurement]])
> **Not dimensionless.** $\int|\psi|^2dx=1$ is a pure number, so $[\psi]=$ **L^{−1/2}** (in 3-D, L^{−3/2}). $\psi$ is a probability *amplitude*; $|\psi(x)|^2dx$ is the probability of finding the particle in $[x,x+dx]$, so $|\psi|^2$ is a probability density per length. Being real does not change this (a real ψ just carries no probability current).

> [!question] B1 (6) · Davisson–Germer: show $n/\sin\theta\propto\sqrt V$.

> [!example]- Solution
> Bragg/grating condition for the surface rows (spacing $d$): $n\lambda=d\sin\theta$. Electrons accelerated through $V$: $\lambda=h/\sqrt{2meV}$. So $\dfrac n{\sin\theta}=\dfrac d\lambda=\dfrac{d\sqrt{2meV}}h\propto\sqrt V$.

> [!question] B2 (6) · From Bohr's postulate $L=n\hbar$, show $r=4\pi\epsilon_0\dfrac{n^2\hbar^2}{mZe^2}$.

> [!example]- Solution ([[QM12 The Hydrogen Atom]])
> Circular orbit: $\dfrac{mv^2}r=\dfrac{Ze^2}{4\pi\epsilon_0r^2}$; quantisation $mvr=n\hbar$ ⇒ $v=n\hbar/mr$. Substituting: $\dfrac{n^2\hbar^2}{mr^3}=\dfrac{Ze^2}{4\pi\epsilon_0r^2}$ ⇒ $r=\dfrac{4\pi\epsilon_0n^2\hbar^2}{mZe^2}=\dfrac{n^2a_0}Z$. (The sheet writes "$L=nh$"; it must be $n\hbar$ to give this formula.)

> [!question] B3 (6) · Using de Broglie and wave optics, argue that an orbiting electron in H cannot be treated by ordinary (classical) mechanics (energy ~10 eV, orbit ~10⁻¹⁰ m).

> [!example]- Solution ([[QM01 From Waves to Probabilities]])
> $\lambda=h/\sqrt{2mE}=$ **0.39 nm** for 10 eV, *larger* than the orbit (~0.1 nm) and comparable to its circumference. Ray (geometric) optics is the short-wavelength limit of wave optics; it fails when λ is comparable to the apertures or obstacles, where diffraction dominates. Likewise classical trajectories, the "rays" of matter waves, are meaningful only when λ ≪ the scale of the motion. Here λ ≳ the orbit, so the electron must be treated as a wave: standing-wave orbits, $n\lambda=2\pi r$.

> [!question] B4 (6) · $\psi_n=A\sin(n\pi x/l)$ in a box of length $l$: $\langle p\rangle$?

> [!example]- Solution ([[QM04 The Particle in a Box]])
> $\langle p\rangle=-i\hbar A^2\int_0^l\sin\frac{n\pi x}l\cdot\frac{n\pi}l\cos\frac{n\pi x}l\,dx=-i\hbar A^2\frac{n\pi}{2l}\int_0^l\sin\frac{2n\pi x}l\,dx=$ **0**. (A real bound state is a standing wave, equal parts $\pm n\pi\hbar/l$.)

> [!question] C1 (6) · With the uncertainty relation $p\sim h/r$ for an electron confined within $r$, minimise $E=$ kinetic + Coulomb energy. Find $r$.

> [!example]- Solution ([[QM12 The Hydrogen Atom]])
> $E(r)=\dfrac{p^2}{2m}-\dfrac{e^2}{4\pi\epsilon_0r}$ with $p=\hbar/r$: $dE/dr=0$ ⇒ $r=\dfrac{4\pi\epsilon_0\hbar^2}{me^2}=a_0=$ **0.053 nm**, $E_{min}=-13.6$ eV, the exact ground state. With $p=h/r$ as the sheet writes it, $r=(2\pi)^2a_0=2.1$ nm and $E=-0.34$ eV. The method is right, but the order-of-magnitude constant matters.

> [!question] C2 (6) · Sommerfeld's rule $\oint p\,dq=nh$. For a harmonic oscillator of frequency ν, show Planck's $E=nh\nu$ (ellipse area $\pi ab$).

> [!example]- Solution ([[QM05 The Harmonic Oscillator]])
> $E=\dfrac{p^2}{2m}+\tfrac12m\omega^2q^2$: in phase space an **ellipse** with semi-axes $p_0=\sqrt{2mE}$, $q_0=\sqrt{2E/m\omega^2}$. $\oint p\,dq=\pi p_0q_0=\dfrac{2\pi E}\omega=\dfrac E\nu=nh$ ⇒ $E=nh\nu$. (The exact quantum answer adds the zero-point $\tfrac12h\nu$.)

## End-semester (26 Nov 2022)

> [!question] 1 (15) · (a) Eigenvalues of a Hermitian operator are real. (b) Its eigenfunctions with different eigenvalues are orthogonal. (c) From the commutators of $L_x,L_y,L_z$, find $[L^2,L_z]$.

> [!example]- Solution ([[QM03 States Operators and Measurement]], [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]])
> (a) $A\psi=a\psi$: $\langle\psi|A\psi\rangle=a\langle\psi|\psi\rangle$ and $\langle A\psi|\psi\rangle=a^*\langle\psi|\psi\rangle$. Hermiticity makes them equal, so $a=a^*$.
> (b) $A\psi_1=a_1\psi_1$, $A\psi_2=a_2\psi_2$: $\langle\psi_1|A\psi_2\rangle=a_2\langle\psi_1|\psi_2\rangle=\langle A\psi_1|\psi_2\rangle=a_1\langle\psi_1|\psi_2\rangle$ (with $a_1$ real). So $(a_2-a_1)\langle\psi_1|\psi_2\rangle=0$, and $\langle\psi_1|\psi_2\rangle=0$.
> (c) $[L^2,L_z]=[L_x^2,L_z]+[L_y^2,L_z]$. Using $[L_x,L_z]=-i\hbar L_y$ and $[L_y,L_z]=i\hbar L_x$: $[L_x^2,L_z]=-i\hbar(L_xL_y+L_yL_x)$ and $[L_y^2,L_z]=i\hbar(L_yL_x+L_xL_y)$. Sum: **0**.

> [!question] 2 (15) · (A) Two masses $m$ on a massless rod of length $a$, rotating in a plane about the fixed centre: the allowed energies. (B) A wavepacket of unit-amplitude cosine waves with $k$ uniform in $[k_0-\Delta k,k_0+\Delta k]$: the probability distribution, sketched and described.

> [!example]- Solution ([[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]], [[QM02 The Schrodinger Equation and Stationary States]])
> (A) $I=2m(a/2)^2=ma^2/2$; $H=L_z^2/2I$ with $L_z=\ell\hbar$, $\ell\in\mathbb Z$ (single-valued $e^{i\ell\phi}$): $E_\ell=\dfrac{\hbar^2\ell^2}{2I}=$ **$\dfrac{\hbar^2\ell^2}{ma^2}$**, $\ell=0,\pm1,\pm2,\dots$: doubly degenerate except $\ell=0$.
> (B) At $t=0$: $\psi(x)=\int_{k_0-\Delta k}^{k_0+\Delta k}\cos kx\,dk=\dfrac{2\cos(k_0x)\sin(\Delta k\,x)}x$, so $|\psi|^2=\dfrac{4\cos^2(k_0x)\sin^2(\Delta k\,x)}{x^2}$. Rapid carrier fringes $\cos^2k_0x$ under a **sinc² envelope** with:
> - its central maximum at $x=0$ (height $4\Delta k^2$);
> - zeros at $x=n\pi/\Delta k$;
> - side lobes falling as $1/x^2$;
> - width $\Delta x\sim\pi/\Delta k$, so $\Delta x\,\Delta k\sim$ const: the uncertainty relation.
>
> (Cosines contain $\pm k$, so this is a standing packet.)

> [!question] 3 (15) · (A) The $n=2$ state of H lives ~10⁻⁸ s before decaying to $n=1$: (a) the energy uncertainty (eV); (b) the transition energy; (c) the wavelength and its uncertainty (nm). (B) Can protons in a nucleus be at rest? If not, estimate their speed.

> [!example]- Solution ([[QM12 The Hydrogen Atom]], [[QM01 From Waves to Probabilities]])
> (A)
> (a) $\Delta E\sim\hbar/\tau=$ **6.6 × 10⁻⁸ eV** (or $\hbar/2\tau$, 3.3 × 10⁻⁸ eV).
> (b) $13.6(1-\tfrac14)=$ **10.2 eV**.
> (c) $\lambda=hc/E=$ **121.6 nm** (Lyman α); $\Delta\lambda=\lambda\Delta E/E=$ **7.9 × 10⁻⁷ nm**, the natural linewidth.
>
> (B) **No.** Confinement to $\Delta x\sim$ nuclear size (2–5 fm) forces $\Delta p\gtrsim\hbar/2\Delta x$, so $v\sim\Delta p/m_p\approx$ **(0.6–1.6) × 10⁷ m/s**, a few per cent of $c$ (kinetic energies of MeV, as observed).

> [!question] 4 (20) · $A$ (observable α) has eigenfunctions $\phi_{1,2}$ with eigenvalues $a_{1,2}$; $B$ (β) has $\chi_{1,2}$ with $b_{1,2}$. $\phi_1=(5\chi_1+12\chi_2)/13$, $\phi_2=(12\chi_1-5\chi_2)/13$. α is measured and gives $a_1$; then β; then α again. Probability of $a_2$?

> [!example]- Solution ([[QM03 States Operators and Measurement]])
> After the first measurement the state is $\phi_1$. β gives $b_1$ with probability $25/169$ (state $\chi_1$) or $b_2$ with $144/169$ (state $\chi_2$). Inverting: $\chi_1=(5\phi_1+12\phi_2)/13$ and $\chi_2=(12\phi_1-5\phi_2)/13$. So $P(a_2|\chi_1)=144/169$ and $P(a_2|\chi_2)=25/169$.
> $$P(a_2)=\frac{25}{169}\cdot\frac{144}{169}+\frac{144}{169}\cdot\frac{25}{169}=\frac{7200}{28561}=\mathbf{0.252}.$$
> Without the β measurement it would be 0: the intermediate measurement of an incompatible observable destroys the information.

> [!question] 5 (15) · Estimate the He ground-state energy by scaling the coordinate (as done in class for H), in eV. How much does it change if "corrected" for electron–electron repulsion?

> [!example]- Solution ([[QM12 The Hydrogen Atom]])
> **Without repulsion**: each electron is hydrogenic with $Z=2$. Scaling $r\to r/Z$ gives $E=-Z^2\times13.6$ eV each: $E=-2\times4\times13.6=$ **−108.8 eV**.
> **With repulsion**, the same scaling estimate: put both electrons at radius $r$ on opposite sides, so $r_{12}=2r$:
> - $E(r)=2\cdot\dfrac{\hbar^2}{2mr^2}-2\cdot\dfrac{2e^2}{4\pi\epsilon_0r}+\dfrac{e^2}{4\pi\epsilon_0\,2r}=\dfrac{\hbar^2}{mr^2}-\dfrac72\dfrac{e^2}{4\pi\epsilon_0r}$;
> - minimising gives $r=\tfrac47a_0$ and $E=-\tfrac{49}{16}\times27.2=$ **−83.3 eV**.
>
> The correction is **≈ +25 eV**. (The variational method with $Z_{eff}=27/16$ gives −77.5 eV; experiment −79.0 eV. The no-repulsion estimate is ~30 eV too low.)

## Topic map
| question | topic | vault |
|---|---|---|
| MS A1–A2, B1, B3 | blackbody, de Broglie, Davisson–Germer | [[QM01 From Waves to Probabilities]] |
| MS A3, ES 1, 4 | states, Hermitian operators, measurement | [[QM03 States Operators and Measurement]] |
| MS B4 | box | [[QM04 The Particle in a Box]] |
| MS C2 | oscillator, old quantum theory | [[QM05 The Harmonic Oscillator]] |
| ES 2 | rotor, angular momentum, wave packets | [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]], [[QM02 The Schrodinger Equation and Stationary States]] |
| MS B2, C1; ES 3, 5 | Bohr model, hydrogen, helium | [[QM12 The Hydrogen Atom]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | [[PH2113_midsem_22.pdf]], [[PH2113_endsem_22.pdf]] (and the Bhas-Sourabh copies); Drive QP archive, 2026-11-22; scans | taught (past papers) |
> | numbers | `scripts/qm_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The "class" method for He (ES 5) is reconstructed; the opposite-sides geometry is my assumption. MS B2's "$L=nh$" is read as $n\hbar$.
