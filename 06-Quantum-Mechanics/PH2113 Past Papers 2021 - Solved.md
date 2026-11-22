---
title: PH2113 Past Papers 2021 - Solved
aliases: [PH2113 2021, quantum midsem 2021, QM online test 2021]
subject: qm
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/qm, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# PH2113 Past Papers 2021 (online mid-sem), Solved

[[Quantum Mechanics - Course Map|Course Map]] · [[Quantum Mechanics Quiz Prep]] · other years: [[PH2113 Past Papers 2020 - Question Map|2020]] · [[PH2113 Past Papers 2022 - Solved|2022]] · [[PH2113 Past Papers 2023 - Solved|2023]] · [[PH2113 Past Papers 2024 - Solved|2024]] · [[PH2113 Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · past paper</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The paper
> [[QM_2020_batch_midsems_ogale.pdf]] (9 pp.): a student's result sheet from the online (CodeTantra) **mid-sem of the 2020-batch run of PH2113**, autumn 2021. The file name gives the instructor as Ogale. From the Drive **Question Paper Archive → Sem-3 → PH2113**, downloaded 2026-11-22 to `physics/quantum-mechanics/lecture-notes-slides/past-papers/qp-archive/PH2113/`. **Section 1**: 6 descriptive questions (uploads, blank in the export; one evaluator comment). **Section 2**: 10 MCQs (2 marks each; ticks and crosses show the student's marks). Read from page images. Numbers: `scripts/qm_qp_archive_numbers.py`.

## Section 1: descriptive
> [!question] D1 · $\psi=Nx(L-x)$ for $0<x<L$, else 0. (a) Normalise. (b) $\langle x\rangle$, $\langle x^2\rangle$. (c) $\langle p_x\rangle$, $\langle p_x^2\rangle$.

> [!example]- Solution ([[QM03 States Operators and Measurement]], [[QM04 The Particle in a Box]])
> (a) $\int_0^Lx^2(L-x)^2dx=L^5/30$ ⇒ $N=\sqrt{30/L^5}$.
> (b) The density is symmetric about $L/2$, so $\langle x\rangle=L/2$; $\langle x^2\rangle=\tfrac27L^2$, hence $\Delta x=L/\sqrt{28}$.
> (c) $\psi$ is real, so $\langle p\rangle=0$. $\langle p^2\rangle=-\hbar^2\int\psi\psi''=2\hbar^2N^2\int_0^Lx(L-x)dx=\mathbf{10\hbar^2/L^2}$ (just above the box ground state's $\pi^2\hbar^2/L^2=9.87\hbar^2/L^2$: the parabola is close to $\sin(\pi x/L)$).

> [!question] D2 · $\rho_\nu(\nu,T)=\dfrac{8\pi\nu^2}{c^3}\dfrac{h\nu}{e^{h\nu/kT}-1}$. (a) Convert to $\rho(\lambda,T)$. (b) $\lambda_{max}$ for 5500 °C. (c) Photon energies at $\lambda_{max}$ and $\lambda_{max}/2$. (d) $\lambda_{max}$ for stars at 5000 °C and 6000 °C.

> [!example]- Solution ([[QM01 From Waves to Probabilities]])
> (a) $\rho_\lambda d\lambda=\rho_\nu|d\nu|$ with $\nu=c/\lambda$, $|d\nu/d\lambda|=c/\lambda^2$: $\rho(\lambda,T)=\dfrac{8\pi hc}{\lambda^5}\dfrac1{e^{hc/\lambda kT}-1}$.
> (b) $d\rho/d\lambda=0$ ⇒ $5(1-e^{-x})=x$ with $x=hc/\lambda kT$ ⇒ $x=4.965$: Wien's law $\lambda_{max}T=2.898\times10^{-3}$ m K. At 5773 K: **502 nm**.
> (c) $hc/\lambda$: **2.47 eV** at $\lambda_{max}$, **4.94 eV** at $\lambda_{max}/2$.
> (d) 5273 K: **550 nm** (48 nm longer, redder); 6273 K: **462 nm** (40 nm shorter, bluer).

> [!question] D3 (5) · Hydrogen absorbs a photon $n=1\to4$. Frequency? Electron speeds in $n=1$ and $n=4$? Possible emitted frequencies on the way back?

> [!example]- Solution ([[QM12 The Hydrogen Atom]])
> $\Delta E=13.6(1-\tfrac1{16})=12.75$ eV ⇒ $\nu=$ **3.08 × 10¹⁵ Hz** (97.3 nm). Bohr speeds $v_n=\alpha c/n$: $v_1=$ **2.19 × 10⁶ m/s**, $v_4=$ **5.5 × 10⁵ m/s**. Downward routes give **six** lines:
> | transition | frequency | wavelength |
> |---|---|---|
> | 4→3 | 1.60 × 10¹⁴ Hz | 1877 nm |
> | 4→2 | 6.17 × 10¹⁴ Hz | 487 nm |
> | 4→1 | 3.08 × 10¹⁵ Hz | 97.3 nm |
> | 3→2 | 4.57 × 10¹⁴ Hz | 657 nm |
> | 3→1 | 2.92 × 10¹⁵ Hz | 103 nm |
> | 2→1 | 2.47 × 10¹⁵ Hz | 122 nm |

> [!question] D4 (17) · (a) Photons from a 2000 °C blackbody fall on a material of work function 4 eV: which wavelengths eject photoelectrons? What changes at 2500 °C? (b) 248 nm UV on a work function of 2.3 eV: the fastest photoelectrons' kinetic energy and de Broglie wavelength.

> [!example]- Solution ([[QM01 From Waves to Probabilities]])
> (a) Only photons with $h\nu>4$ eV, i.e. **λ < 310 nm**, whatever the source temperature. At 2500 °C **the range does not change**, because it is set by the work function alone. What changes is the *number* of such photons: the Wien tail at short λ grows steeply with $T$, so the photocurrent rises. The electrons' maximum energy stays fixed by the shortest wavelengths present.
> (b) $hc/\lambda=5.00$ eV ⇒ $K_{max}=$ **2.70 eV**; $\lambda_{dB}=h/\sqrt{2mK}=$ **0.75 nm**.

> [!question] D5 (19) · X-ray diffraction uses λ ~ 1 Å. If electrons or neutrons are used instead, is either relativistic?

> [!example]- Solution
> $p=h/\lambda$: electron $K=p^2/2m=$ **150 eV** ≪ 511 keV; neutron $K=$ **0.082 eV** ≪ 940 MeV. **Neither is relativistic** (the evaluator's comment: "Both are non relativistic").

> [!question] D6 · (a) If $v_{ph}=E/p=\sqrt{g\lambda/2\pi}$, show $v_g=v_{ph}/2$. (b) For a relativistic particle, show the group velocity equals the particle velocity and $v_gv_{ph}=c^2$; so $v_{ph}>c$ for $m_0\neq0$. Is that a problem?

> [!example]- Solution ([[QM01 From Waves to Probabilities]])
> (a) $v_{ph}=\omega/k=\sqrt{g/k}$ ⇒ $\omega=\sqrt{gk}$ ⇒ $v_g=d\omega/dk=\tfrac12\sqrt{g/k}=v_{ph}/2$ (deep-water waves).
> (b) $v_g=dE/dp=pc^2/E=\gamma mvc^2/\gamma mc^2=v$. $v_{ph}=E/p=c^2/v$, so $v_gv_{ph}=c^2$ and $v_{ph}>c$. **No problem**: the phase of an infinite monochromatic wave carries no energy or information; signals travel with the envelope at $v_g=v<c$.

## Section 2: MCQs (2 marks each)
> [!example]- Answers
> 1. $\langle\phi_1|\phi_2\rangle=1+2+3\alpha=0$ ⇒ **α = −1 (c)** ✓.
> 2. The time-independent SE expresses **conservation of total energy (a)** ✓.
> 3. Free Gaussian packet: **Δp stays fixed, Δx grows without limit (d)**: momentum is conserved for a free particle, and the packet spreads ($\Delta x\propto t$ at late times). (Student's answer marked wrong.)
> 4. $\lambda\ll hc/\phi_0$ ⇒ $K\approx hc/\lambda$ ⇒ $\lambda_D=h/\sqrt{2mhc/\lambda}\propto\lambda^{1/2}$ ⇒ $d\lambda_D/d\lambda=\lambda_D/2\lambda$: **∝ λ_D/λ (d)**. (The student's (c) was marked wrong.)
> 5. $|a|^2+\tfrac{11}{16}+\tfrac1{16}=1$ ⇒ **a = 1/2 (b)** (the key option shown in green; $i\sqrt3/4$ has modulus $\sqrt3/4$).
> 6. $\psi=e^{-x^2/a^2+ikx}$: **⟨p⟩ = ħk (a)** ✓.
> 7. $(x+d/dx)\psi=\alpha\psi$ ⇒ $\psi'=(\alpha-x)\psi$ ⇒ **ψ = ψ₀e^{αx−x²/2} (b)** ✓.
> 8. Two blackbodies, $T_1<T_2$: **(c)**: the hotter curve is above the cooler one at *every* λ and peaks at shorter λ ✓. ((a) and (d) cross; (b) has the hotter curve lower.)
> 9. A valid solution of the SE: **(a)**, a smooth decaying curve ✓. (b) has a kink (allowed only at a δ-potential), and (c) is double-valued.
> 10. Superposed waves: **add amplitudes (a)** ✓.

## Topic map
| question | topic | vault |
|---|---|---|
| D2, D4, D5, D6, MCQ 4, 8 | blackbody, photoelectric effect, de Broglie, phase and group velocity | [[QM01 From Waves to Probabilities]] |
| D1, MCQ 1, 5, 6, 7 | normalisation, expectation values, operators | [[QM03 States Operators and Measurement]] |
| MCQ 2, 3, 9, 10 | Schrödinger equation, wave packets | [[QM02 The Schrodinger Equation and Stationary States]] |
| D3 | Bohr levels | [[QM12 The Hydrogen Atom]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions, MCQ marks | [[QM_2020_batch_midsems_ogale.pdf]] (Drive QP archive, 2026-11-22; page images, 200 dpi crops for D6 and MCQ 8) | taught (past paper) |
> | numbers | `scripts/qm_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The instructor and date come from the file name and the sheet's style (no header page in the export).
