---
title: PH2113 Past Papers 2023 - Solved
aliases: [PH2113 2023, quantum midsem 2023, quantum endsem 2023]
subject: qm
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/qm, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# PH2113 Past Papers 2023: Mid-sem and End-sem, Solved

[[Quantum Mechanics - Course Map|Course Map]] · [[Quantum Mechanics Quiz Prep]] · other years: [[PH2113 Past Papers 2021 - Solved|2021]] · [[PH2113 Past Papers 2022 - Solved|2022]] · [[PH2113 Past Papers 2024 - Solved|2024]] · [[PH2113 Past Papers 2025 - Solved|2025]]

<span class="scope-taught">taught · past papers (Rejish Nath, Prasenjit Ghosh)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> From the Drive **Question Paper Archive → Sem-3 → PH2113**, downloaded 2026-11-22 to `physics/quantum-mechanics/lecture-notes-slides/past-papers/qp-archive/PH2113/`. Both are phone scans:
> - [[quantum_physics_midsem_2023_rejish_compressed.pdf]]: **mid-term**, Fall 2023, 20 marks, 12 questions (1–6 one mark each, closed book);
> - [[quantum_endsem_2023_prasenjit_compressed.pdf]]: **end-sem**, 22 Nov 2023, 30 marks.
>
> No keys: solutions mine. Numbers: `scripts/qm_qp_archive_numbers.py`.

## Mid-term (Fall 2023)
> [!example]- Q1–Q6 (1 mark each)
> 1. "The peak of a blackbody spectrum occurs at a frequency inversely proportional to $T$": **False**. $\nu_{max}\propto T$ (Wien: $h\nu_{max}=2.82kT$); it is the *wavelength* peak that goes as $1/T$.
> 2. Compton shift $\Delta\lambda=\lambda_C(1-\cos\theta)$ is **independent of λ**, so at θ = 45° the ratio of the changes is **1**.
> 3. $v_\phi=\sqrt{g/k}$ ⇒ $\omega=\sqrt{gk}$ ⇒ $v_g=\tfrac12\sqrt{g/k}=v_\phi/2$.
> 4. Well-defined momentum $k_0$: $g(k)=\delta(k-k_0)$ (then $\psi=e^{ik_0x}/\sqrt{2\pi}$).
> 5. $\psi(x)=\delta(x-x_0)$ ⇒ $g(k)=\frac1{\sqrt{2\pi}}\int\delta(x-x_0)e^{-ikx}dx=\dfrac{e^{-ikx_0}}{\sqrt{2\pi}}$: all momenta equally likely.
> 6. Free particle: **(a) only Δx changes with time**; $|g(k)|^2$ is time-independent, so Δp is constant.

> [!example]- Q7–Q12 (2 marks each; Q12 4 × 1)
> 7. $\lambda=h/\sqrt{2meV}=1.226/\sqrt{100}$ nm $=$ **0.123 nm**. ([[QM01 From Waves to Probabilities]])
> 8. Photon wavelength = $h/mc$ ⇒ $E_\gamma=hc/\lambda=mc^2$: **the photon energy equals the particle's rest energy**.
> 9. $h\nu=6.626\times10^{-34}\times1.5\times10^{15}/e=6.20$ eV ⇒ $K_{max}=1.20$ eV ⇒ stopping potential **1.2 V**.
> 10. Plancherel: substitute $\psi(x)=\frac1{\sqrt{2\pi}}\int\phi(k)e^{ikx}dk$: $\int|\psi|^2dx=\frac1{2\pi}\iiint\phi^*(k')\phi(k)e^{i(k-k')x}dk\,dk'\,dx$. Then $\int e^{i(k-k')x}dx=2\pi\delta(k-k')$ gives $\int|\phi(k)|^2dk$.
> 11. $g(k)=C$ on $|k|\le k_0$: $\psi(x)=\frac C{\sqrt{2\pi}}\int_{-k_0}^{k_0}e^{ikx}dk=C\sqrt{\tfrac2\pi}\,\dfrac{\sin k_0x}x$. $|\psi|^2\propto\sin^2(k_0x)/x^2$: a central peak of width ~$2\pi/k_0$ (zeros at $x=n\pi/k_0$) with side lobes ∝ $1/x^2$. Normalisation: $C=1/\sqrt{2k_0}$.
> 12. $\psi=2\alpha^{3/2}xe^{-\alpha x}$ ($x\ge0$). (a) $4\alpha^3\int_0^\infty x^2e^{-2\alpha x}dx=4\alpha^3\cdot\frac2{(2\alpha)^3}=1$ ✓. (b) $\frac d{dx}(x^2e^{-2\alpha x})=0$ ⇒ $x=1/\alpha$. (c) The density rises as $x^2$, peaks at $1/\alpha$ (value $4\alpha e^{-2}$), and decays exponentially. (d) $P(0<x<1/\alpha)=1-5e^{-2}=$ **0.323**.

## End-semester (22 Nov 2023)

> [!question] Q1 (5 + 2 + 2 + 2 + 2 + 2) · $V=0$ for $|x|<a/2$, ∞ otherwise. (a) Normalised stationary states and energies. (b) Sketch $V$, the levels, and the ground and first excited states. (c) In the first excited state, $P(-a/4<x<a/4)$. (d) $\langle p\rangle$ there. (e) If the walls are finite ($V_0$) and $E<V_0$, how do the states change? (f) Are the energies lower than for the infinite well?

> [!example]- Solution ([[QM04 The Particle in a Box]], [[QM07 The Finite Square Well]])
> (a) $E_n=\dfrac{n^2\pi^2\hbar^2}{2ma^2}$; $\psi_n=\sqrt{\tfrac2a}\cos\frac{n\pi x}a$ for odd $n$ (even parity) and $\sqrt{\tfrac2a}\sin\frac{n\pi x}a$ for even $n$ (odd parity), zero outside.
> (b) Levels in the ratio 1 : 4 : 9 …; $\psi_1$ is a single cos hump, zero at the walls; $\psi_2$ is a full sine with one node at the centre.
> (c) $\frac2a\int_{-a/4}^{a/4}\sin^2\frac{2\pi x}a\,dx=\frac2a\cdot\frac a4=$ **1/2**.
> (d) **0** (real standing wave).
> (e) The wavefunctions **leak into the walls** as decaying exponentials $e^{-\kappa|x|}$, with $\kappa=\sqrt{2m(V_0-E)}/\hbar$. They are no longer zero at $\pm a/2$; ψ and ψ′ are continuous there. The shapes are similar but slightly wider, and there are only finitely many bound states.
> (f) **Yes, lower.** Spreading into the walls lengthens the effective wavelength, so the kinetic energy falls. Equivalently, the finite well's potential is everywhere ≤ the infinite well's, so by the variational principle (applied level by level) every bound energy is lower.

> [!question] Q2 (2 + 3 + 1 + 3 + 2 + 2 + 2) · (i) An electron and a proton of the same energy $E<U$ approach a barrier: which tunnels more? (ii) Half-oscillator: $\frac12m\omega^2x^2$ for $x>0$, ∞ for $x\le0$; sketch the two lowest states. (iii) The dimension of $\psi(\vec r)$ in 3-D. (iv) Three sketched ψ(x), which can be physical? (a) a slowly rising straight line extending indefinitely; (b) a curve with *two* branches over the same $x$; (c) a hump with a sharp corner at its peak. (v) Sketch the H ground-state radial function and radial probability. (vi) How much more likely is a 1s electron at $a_0$ than at $a_0/2$? (vii) $\Phi(\phi)=Ae^{im\phi}$: find $A$ and show orthogonality.

> [!example]- Solution ([[QM08 Quantum Tunnelling]], [[QM05 The Harmonic Oscillator]], [[QM12 The Hydrogen Atom]], [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]])
> (i) $T\approx e^{-2\kappa L}$ with $\kappa=\sqrt{2m(U-E)}/\hbar$: the proton's κ is $\sqrt{1836}\approx43$ times larger, so **the electron** tunnels far more.
> (ii) ψ must vanish at $x=0$, so only the full oscillator's **odd** states survive: $\psi_1$ and $\psi_3$ restricted to $x>0$ (renormalised), with $E=\tfrac32\hbar\omega$ (one hump) and $\tfrac72\hbar\omega$ (two humps, one node).
> (iii) $\int|\psi|^2d^3r=1$ ⇒ $[\psi]=$ **L^{−3/2}**.
> (iv)
> - (a) **Not physical**: it does not decay, so it cannot be normalised (at best an idealised scattering state).
> - (b) **Not physical**: two values at the same $x$, not a function.
> - (c) **Physical only if** the potential has a δ-function spike at the corner. Otherwise ψ′ must be continuous, so a kink is forbidden.
>
> (v) $R_{10}=2a_0^{-3/2}e^{-r/a_0}$ is maximal at $r=0$ and decays. $P(r)=r^2R^2$ starts at 0 and **peaks at $r=a_0$**.
> (vi) Radial probability ratio: $\dfrac{a_0^2e^{-2}}{(a_0/2)^2e^{-1}}=4/e=$ **1.47 times** more likely. (Per unit volume, i.e. $|\psi|^2$, it is $e^{-1}=0.37$: *less* likely. The radial reading is intended.)
> (vii) $\int_0^{2\pi}|A|^2d\phi=1$ ⇒ $A=1/\sqrt{2\pi}$. $\int\Phi_{m'}^*\Phi_md\phi=\frac1{2\pi}\int_0^{2\pi}e^{i(m-m')\phi}d\phi=\delta_{mm'}$ ($m$ integer, by single-valuedness).

## Topic map
| question | topic | vault |
|---|---|---|
| MS 1–3, 7–9 | blackbody, Compton, photoelectric, de Broglie | [[QM01 From Waves to Probabilities]] |
| MS 4–6, 10–11 | wave packets, Fourier, spreading | [[QM02 The Schrodinger Equation and Stationary States]] |
| MS 12; ES 2(iii)–(iv) | normalisation, admissible ψ | [[QM03 States Operators and Measurement]] |
| ES 1 | infinite and finite wells | [[QM04 The Particle in a Box]], [[QM07 The Finite Square Well]] |
| ES 2(i)–(ii) | tunnelling, half-oscillator | [[QM08 Quantum Tunnelling]], [[QM05 The Harmonic Oscillator]] |
| ES 2(v)–(vii) | hydrogen, azimuthal functions | [[QM12 The Hydrogen Atom]], [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | [[quantum_physics_midsem_2023_rejish_compressed.pdf]], [[quantum_endsem_2023_prasenjit_compressed.pdf]] (Drive QP archive, 2026-11-22; scans; ES 2(iv) sketches at 220 dpi) | taught (past papers) |
> | numbers | `scripts/qm_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The ES 2(iv) sketch descriptions are my reading of the scan. ES 2(vi) has two readings.
