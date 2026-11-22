---
title: TD2213 Past Papers 2022 - Solved
aliases: [TD2213 2022, thermodynamics endsem 2022]
subject: thermo
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/thermo, type/practice, taught, extra/beyond, src/exam-paper, status/draft, quiz/thermo]
---
# TD2213 Past Papers 2022 (January Semester): End-sem, Solved

[[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · [[Thermodynamics Quiz Prep]] · other years: [[TD2213 End-Semester 2021 - Solved|2021]] · [[TD2213 Past Papers 2023 - Solved|2023]] · [[TD2213 Past Papers 2024 - Solved|2024]] · [[TD2213 Past Papers 2025 - Solved|2025]] · [[TD2213 End-Semester 2026 January Semester - Solved|2026]]

<span class="scope-taught">taught · past paper (Srabanti Chaudhury, Muhammed Musthafa)</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The paper
> **End-sem**, 07 May 2022, 40 marks. Source: [[Thermodynamics Endsems 2022.pdf]] (2 pp., a low-resolution scan), from the Drive **Question Paper Archive → Sem-3 → Thermodynamics (sem 4)**, downloaded 2026-11-22 to `physics/thermodynamics-stat-mech/lecture-notes-slides/past-papers/qp-archive/Thermodynamics (sem 4)/`.
>
> TD2213 is taught in the January (4th) semester; the archive files it under Sem-3. The archive has no other paper for 2022.
>
> Numbers: `scripts/td_qp_archive_numbers.py`. Questions repeated from 2021 link to [[TD2213 End-Semester 2021 - Solved]].

> [!example]- Q1 (5) · 4N coin flips: $p(N)/p(2N)$ shrinks as N grows ([[SM01 Probability Large Numbers and Information]], [[TH09 Microstates Macrostates and Multiplicity]])
> The ratio is
> $$\frac{p(N)}{p(2N)}=\frac{\binom{4N}{N}}{\binom{4N}{2N}}=\frac{[(2N)!]^2}{N!\,(3N)!}.$$
> Apply Stirling's approximation, $\ln n!\approx n\ln n-n$:
> $$\ln\frac{p(N)}{p(2N)}\approx4N\ln2N-N\ln N-3N\ln3N=N\ln\frac{16}{27}.$$
> So the ratio is $\approx(16/27)^N$, which falls **exponentially** with N.
>
> Exact values: 0.667 at N = 1, 0.084 at N = 5, 3.3 × 10⁻⁵ at N = 20. The Stirling form gives 0.59, 0.073 and 2.9 × 10⁻⁵, the right trend with an O(√N) prefactor missing.

> [!example]- Q2 (5) · Birthday problem, 25 students
> $$P=1-\prod_{k=0}^{24}\frac{365-k}{365}=\mathbf{0.569}.$$

> [!example]- Q3 (5) · Show $\kappa_S=\dfrac{C_V}{C_P}\kappa_T$ with Jacobians ([[TH05 Potentials Maxwell Relations Stability and the Third Law]])
> $$\frac{\kappa_S}{\kappa_T}=\frac{(\partial V/\partial P)_S}{(\partial V/\partial P)_T}=\frac{\partial(V,S)/\partial(P,S)}{\partial(V,T)/\partial(P,T)}.$$
> Swap the denominators:
> $$\frac{\kappa_S}{\kappa_T}=\frac{\partial(V,S)}{\partial(V,T)}\cdot\frac{\partial(P,T)}{\partial(P,S)}=\Big(\frac{\partial S}{\partial T}\Big)_V\Big(\frac{\partial T}{\partial S}\Big)_P=\frac{C_V/T}{C_P/T}=\frac{C_V}{C_P}.$$

> [!example]- Q4 (3) · Entropy against volume at constant P, sign set by α
> $$\Big(\frac{\partial S}{\partial V}\Big)_P=\Big(\frac{\partial S}{\partial T}\Big)_P\Big(\frac{\partial T}{\partial V}\Big)_P=\frac{C_P}{T}\cdot\frac1{V\alpha}.$$
> Since $C_P>0$, S **increases** with V when α > 0 and **decreases** when α < 0 (e.g. water between 0 and 4 °C).

> [!example]- Q5 (4) · A body ($C_P$, $T_i$) reaches equilibrium with a reservoir at $T_f>T_i$ ([[TH04 The Second Law Carnot Engines and Entropy]])
> - Body: $\Delta S=C_P\ln(T_f/T_i)$.
> - Reservoir: $\Delta S=-C_P(T_f-T_i)/T_f$.
> - Universe:
> $$\Delta S_{univ}=C_P\Big[\ln x-1+\frac1x\Big],\qquad x=\frac{T_f}{T_i}.$$
> This is > 0 for every x ≠ 1, since $\ln x>1-1/x$.

> [!example]- Q6 (3) · 2.00 mol He, isothermal at 22 °C, 22.8 → 31.7 dm³ ([[TH02 Work Heat and the First Law]], [[TH03 The Ideal Gas and Adiabatic Processes]])
> In every case ΔU = ΔH = 0, because U and H of an ideal gas depend on T only.
> - (a) Reversible: $w=-nRT\ln(V_2/V_1)=$ **−1.62 kJ**, so q = +1.62 kJ.
> - (b) Against $P_{ext}=P_f=nRT/V_2=154.8$ kPa: $w=-P_{ext}\Delta V=$ **−1.38 kJ**, so q = +1.38 kJ.
> - (c) Free expansion: **q = w = 0**.

> [!example]- Q7 (3) · Fifteen boys: 5 lost, 8 sunburned, 6 fine ([[SM01 Probability Large Numbers and Information]])
> 15 − 6 = 9 boys had at least one problem. So lost ∩ sunburned = 5 + 8 − 9 = 4.
> - (a) P(lost | sunburned) = 4/8 = **1/2**.
> - (b) P(sunburned | lost) = 4/5 = **0.8**.

> [!example]- Q8 (2) · 14 identical dodgeballs into 5 bins
> - (a) No restriction (stars and bars): $\binom{18}{4}=$ **3060**.
> - (b) At least one per bin: $\binom{13}{4}=$ **715**.

> [!example]- Q9 (2) · Ice → water with ΔS = 22.1 J/K and q = 6.00 kJ ([[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]])
> $\Delta S_{univ}=22.1-6000/T$.
> - At −10 °C: −0.70 J/K, **not spontaneous**.
> - At +10 °C: +0.91 J/K, **spontaneous**.

> [!example]- Q10 (2) · van der Waals gas: U depends on V ([[TH05 Potentials Maxwell Relations Stability and the Third Law]])
> $$\Big(\frac{\partial U}{\partial V}\Big)_T=T\Big(\frac{\partial P}{\partial T}\Big)_V-P=\frac{RT}{V-b}-P=\frac a{V^2}>0.$$

> [!example]- Q11 (2) · Adiabatic expansion into vacuum, V → 2V
> T is constant. Compute ΔS along a reversible isotherm: **ΔS = nR ln 2** (5.76 J/K per mol), with $\Delta S_{surr}=0$. So $\Delta S_{univ}>0$: **spontaneous** and irreversible. See also [[TD2213 End-Semester 2021 - Solved|2021]] §3 Q3.

> [!example]- Q12 (2) · Isothermal work exceeds adiabatic work for the same start ([[TH03 The Ideal Gas and Adiabatic Processes]])
> On a P–V diagram the adiabat through the starting point is steeper ($PV^\gamma$ = const), so it lies **below** the isotherm.
> - (i) Same final V: the area under the isotherm is larger, so $W_{iso}>W_{adi}$.
> - (ii) Same final P: the isotherm ends at a larger volume, $V_{iso}=V_1(P_1/P_2)$ against $V_1(P_1/P_2)^{1/\gamma}$, and it also lies higher throughout. So again $W_{iso}>W_{adi}$.
>
> Physically, the isothermal gas draws heat from the surroundings while the adiabatic gas pays for its work from U and cools.

> [!example]- Q13 (2) · Dipoles with and without a field
> Without the field $S=k\ln4=1.386k$; with it, $1.228k$. **The field-free distribution has the higher entropy.** Details in [[TD2213 End-Semester 2021 - Solved|2021]] Q1.

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | questions | [[Thermodynamics Endsems 2022.pdf]] (Drive QP archive, 2026-11-22; low-resolution scan) | taught (past paper) |
> | numbers | `scripts/td_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] The scan is low resolution. Q6's temperature (22 °C) and volumes, and Q7's counts, were read carefully but may contain misreadings.
