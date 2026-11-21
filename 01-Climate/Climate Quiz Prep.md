---
title: Climate Quiz Prep
aliases: [Quiz prep, Climate quiz]
subject: climate
type: moc
scope: [taught, extra-book]
by: [suhas-pre, suhas-post]
status: draft
tags: [subject/climate, type/moc, taught, extra/book, src/suhas-pre, src/suhas-post, src/book, status/draft]
---
# Climate Quiz Prep

◀ [[Climate - Course Map|Course Map]] · chapters [[CL09 Radiative-Convective Equilibrium|CL09]] · [[CL10 Global Energy Balance and Meridional Structure|CL10]] · [[CL11 Mean Meridional Circulation and Angular Momentum|CL11]] · [[CL12 Rotating Frames and the Coriolis Force|CL12]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] Quiz scope and what is taught vs extra
> **Quiz (Fri 23 Oct 2026), from `climate_book_notes.pdf`:** Marshall & Plumb Ch. 4.7, 5, 6.6, 8 and Hartmann 2.8–2.9. Each of the four chapters has a **Quiz checklist** at its end, checked against the book text, and a syllabus map saying what was shown in class.
>
> **M&P §4.7** (convection, RCE) → [[CL09 Radiative-Convective Equilibrium]]
> - 🟢 Suhas pre-midsem notes; no photographed slide covers it
> - 🟡 derivations and problems from the book
>
> **M&P §5.1, Hartmann §2.8–2.9** → [[CL10 Global Energy Balance and Meridional Structure]]
> - 🟢 almost entirely taught (7 Oct slides + handwritten notes pp.1–2)
>
> **M&P §5.4, Ch. 8** → [[CL11 Mean Meridional Circulation and Angular Momentum]]
> - 🟢 8 Oct slides + notes pp.2–3
> - 🟡 angular-momentum budget, eddies, Fig. 6.17
>
> **M&P §6.6** → [[CL12 Rotating Frames and the Coriolis Force]]
> - 🟢 14–15 Oct slides + notes pp.4–5
> - 🟡 radial-inflow lab, parabolic free surface

> [!key] How to use this page
> 1. **Formulas** (below): can you state each and say where it applies?
> 2. **Traps**: the 25 items the checklists flag most.
> 3. **Derivations** you may be asked to reproduce, with the chapter section to revise.
> 4. **Self-test**: cover the answers.

## 1. Formula sheet
| Topic | Relation | Numbers |
|---|---|---|
| Dry adiabat | $\Gamma_d=g/c_p$ ([[Dry Adiabatic Lapse Rate]]) | 9.8 K km⁻¹; real mean 6.5; moist $\Gamma_s$ 4–9 |
| Stability | $N^2=\dfrac gT\Big(\dfrac{\mathrm dT_E}{\mathrm dz}+\Gamma_d\Big)$, $N^2>0$ stable ([[Atmospheric Stability]]) | $N\approx0.01$ s⁻¹, period ≈ 10 min |
| Convective OLR contrast | $(T_s/T_c)^4$ ([[Outgoing Longwave Radiation]]) | $(300/220)^4\approx3.5$ |
| No-tilt maximum insolation | $S_0/\pi$ ([[Insolation]]) | 435 W m⁻² (1367), 433 (1361) |
| TOA balance | $R_{TOA}=S(1-\alpha)-\mathrm{OLR}$ ([[Top-of-Atmosphere Radiation Budget]]) | global $\alpha\approx0.29$–0.30 |
| Column budget | $\partial E/\partial t=R_{TOA}-\Delta F$; annual mean $R_{TOA}=\Delta F$ | |
| Poleward flux | $F(\varphi)=2\pi a^2\!\int_{-\pi/2}^{\varphi}R_{TOA}\cos\varphi'\,\mathrm d\varphi'$ ([[Poleward Energy Transport]]) | peak 5.8–6 PW near 40° |
| Mass stream function | $\psi=\dfrac{2\pi a\cos\varphi}{g}\int_0^p[v]\,\mathrm dp$ ([[Mass Stream Function]]) | |
| Absolute angular momentum | $A=\Omega a^2\cos^2\varphi+ua\cos\varphi$ ([[Absolute Angular Momentum of Air]]) | |
| Ring of air | $u=\Omega a\,\sin^2\varphi/\cos\varphi$ | 14, 58, 134 m s⁻¹ at 10°, 20°, 30° |
| Frame rule | $(\mathrm d\mathbf A/\mathrm dt)_I=(\mathrm d\mathbf A/\mathrm dt)_r+\boldsymbol\Omega\times\mathbf A$ ([[Rotating Reference Frames]]) | |
| Rotating equation | $\mathrm D\mathbf u/\mathrm Dt=\dots-2\boldsymbol\Omega\times\mathbf u+\Omega^2\mathbf R_\perp$ | |
| Modified potential | $\phi=gz-\Omega^2r^2/2$; free surface $z=h_0+\Omega^2r^2/2g$ ([[Centrifugal Force and Effective Gravity]]) | |
| Coriolis parameter | $f=2\Omega\sin\varphi$ ([[Coriolis Parameter]]) | $1.03\times10^{-4}$ s⁻¹ at 45° |

## 2. The 25 traps
**Signs and conventions**
1. With $\Omega>0$ Coriolis turns motion to the **right** (NH), **left** in the SH. Poleward flow in the NH picks up a **westerly** component. ([[CL12 Rotating Frames and the Coriolis Force|CL12]], [[CL11 Mean Meridional Circulation and Angular Momentum|CL11]])
2. The factor is **$2\boldsymbol\Omega\times\mathbf u$**, and centrifugal is $\Omega^2\times$ the **perpendicular** distance $a\cos\varphi$.
3. Coriolis does **no work**; centrifugal acts on a parcel **at rest**, Coriolis does not.
4. Positive $R_{TOA}$ = **gain**; $R_{TOA}=Q_{abs}-\mathrm{OLR}$ with $Q_{abs}=S(1-\alpha)$.
5. $N^2$ uses $\mathrm dT_E/\mathrm dz$ (negative in the troposphere): check the sign of $\Gamma$.

**Radiative-convective equilibrium**
6. RCE is **two regimes**: convective below the tropopause height $z_T$, radiative above.
7. The discontinuity in radiative equilibrium is **at the ground**; it is unstable because the lapse rate exceeds the adiabatic one.
8. The neutral state in the moist tropics is constant **moist** potential temperature, not the dry one; do not use $\Gamma_d$ in saturated air.
9. Convection needs a warm surface or cool air aloft; mid-latitude convection is **intermittent** (cold fronts, thunderstorms).
10. Fig. 3.4, Fig. 4.9 and Eq. 4-22 are **not in your pages**: Problem 2 uses "typical" numbers.

**Energy balance**
11. $S_0/\pi=435$ W m⁻² uses 1367 (433 with 1361) and is the **no-tilt** maximum.
12. "Maximum insolation at the summer pole" is the **solstice daily mean**; the annual-mean poles are the minimum.
13. Orbital-distance variation is $<\pm2\%$ in distance (≈ ±3.4 % in flux): real, but $\ll$ the tilt effect; perihelion is in early January.
14. Albedo is highest at the poles (and over thick cloud and the Sahara). OLR is **low** under high tropical cloud and at the poles, **high** over deserts.
15. Net radiation changes sign near 40° (Hartmann; slides ≈ 33–37°). Deserts have a net annual **loss**, supplied by atmospheric transport.
16. The **flux** peaks where $R_{TOA}$ changes sign, is **zero at the poles**; the energy equation uses the **divergence**, the transport is its **integral**; $R_{TOA}=\Delta F$ only in the annual mean.
17. "The negative area looks bigger" is a plotting effect: with the $\cos\varphi$ weight the areas are equal.
18. Ocean transport peaks near 20°, atmosphere near 40°; the ocean flux is the **residual**.

**Circulation**
19. Hadley ascent follows the **summer** hemisphere; the Ferrel cell is thermally **indirect**.
20. A single pole-to-pole cell is forbidden by **angular momentum**, not by energy.
21. The ring-of-air formula is for the **frictionless upper branch**, not the surface; the book's 130 m s⁻¹ is a rounding of 134.
22. $\psi=0$ at the ground means **no net mass flux**, not no wind.
23. The subtropical jet is strongest in **winter** (~30 m s⁻¹ mean, ~50 instantaneous); surface westerlies peak near 50°, not at the jet.
24. $\theta$ **always increases with height** in the troposphere; isentropes slope up toward the pole; the tropopause is higher in the tropics.
25. The 6× absorbed-solar ratio (tropics/poles, M&P p.63–64) exceeds the insolation ratio (2.4) because of **albedo**.

## 3. Derivations to practise
| Derive | Where to revise |
|---|---|
| radiative-equilibrium profile of a grey atmosphere and why it fails near the ground | [[CL09 Radiative-Convective Equilibrium]] §§2–3 |
| $\Gamma_d=g/c_p$, $\theta$, $N^2$ | CL09 (first law + hydrostatic): [[First Law of Thermodynamics]], [[Adiabatic Process and Potential Temperature]] |
| daily-mean insolation $Q$ and $S_0/\pi$ | [[CL10 Global Energy Balance and Meridional Structure]], [[Insolation]] |
| poleward flux from $R_{TOA}(\varphi)$ | CL10, [[Poleward Energy Transport]] |
| ring-of-air $u(\varphi)$ and why the Hadley cell stops | [[CL11 Mean Meridional Circulation and Angular Momentum]] §4, [[Hadley Cell]] |
| $\mathbf u_I=\mathbf u_r+\boldsymbol\Omega\times\mathbf r$, Coriolis and centrifugal terms | [[CL12 Rotating Frames and the Coriolis Force]] §§2–3 |
| parabolic free surface $z=h_0+\Omega^2r^2/2g$ | CL12 (extra · book box) |

## 4. Self-test (cover the answers)
1. **Why does the radiative-equilibrium profile have a discontinuity at the ground, and what removes it?** Sunlight heats the ground but infrared escapes slowly, so the ground is warmer than the air just above it; the profile is convectively unstable, and convection mixes heat upward.
2. **Why $S_0/\pi$ at the equator but $S_0/4$ globally?** Daily mean of $\cos h$ over a day for the equator at no tilt is $1/\pi$; the sphere average of $S\cos\theta$ is $1/4$.
3. **Where is the poleward flux maximum, and why?** Near 40°, where $R_{TOA}$ changes sign: $\mathrm dF/\mathrm d\varphi\propto R_{TOA}\cos\varphi$.
4. **Why are deserts net energy losers?** High albedo and high OLR; supplied by sinking air and horizontal transport.
5. **Derive $u(\varphi)$.** Conserve $\Omega a^2\cos^2\varphi+ua\cos\varphi=\Omega a^2$ ⇒ $u=\Omega a\sin^2\varphi/\cos\varphi$.
6. **Why can't one Hadley cell reach the pole?** $u\to\infty$ as $\varphi\to90^\circ$ (130+ m s⁻¹ already at 30°).
7. **What does Coriolis do to a parcel's energy?** Nothing: workless; it only turns the velocity.
8. **Why does the free surface of a rotating tank of water form a paraboloid?** In solid-body rotation $p/\rho+\phi$ is constant; at the surface $p=0$ ⇒ $gz-\Omega^2r^2/2=$ const.
9. **Why is the tropical atmosphere nearly on a moist adiabat?** Deep convection keeps the profile close to neutral for ascent of saturated parcels.
10. **Why does the Earth bulge at the equator?** The effective gravity (gravity + centrifugal) is tilted; a deformable Earth flows until the surface is perpendicular to it.

## 5. Part VI: Joy's ocean module (CL22–CL30), added 2026-11-21
<span class="scope-taught">taught</span> *Joy's O1–O7 lectures, notes and tutorials; the Classroom post of 19 Nov: "the syllabus will be everything. However, the exam will likely test your grasp of the post mid-sem material in greater depth."* Figures below are copied from the chapters' cheat-sheets (each verified there).

> [!key] Formula and fact sheet (Part VI)
> - **Energy ledger (CL22):** CERES 2010–24 net **+1.26 W m⁻²** (ASR 241.95, OLR 240.69); poleward transport **5.8 PW (N), 5.7 PW (S)**; ASR = OLR at 37°S/36°N; $LE\approx550(1-\mathrm{RH})$; Gulf Stream 30 Sv ≈ 0.77 PW.
> - **Inertia (CL23):** $d=\sqrt{2\kappa/\omega}$ (soil ~10 cm/day, ~2 m/yr); $\tau=C/\lambda$, λ = 3.8: land 12 d, air 1 month, **mixed layer 1.7 yr**, full ocean 140 yr; fast swings ∝ $1/C^2$; "depth sets the timescale, not the size"; > 91 % of the imbalance goes into the ocean.
> - **Momentum (CL24):** Ekman transport $M=\tau/\rho f$, **90° right (N) / left (S)**; spiral 45° at the surface; pumping $w=\mathrm{curl}(\tau/\rho f)\approx20$ m/yr; geostrophic $u=(g/f)\,$slope; ACC 125 Sv.
> - **Salt (CL25):** S records E − P; mean 34.7; Arabian Sea 36.2 vs Bay of Bengal 32.9; warm water: T rules density, cold water: salt rules; NADW 4 °C/35.0, AAIW 3.3/34.15, AABW 0.4/34.67.
> - **Mass and the switch (CL26):** sinking only in the N. Atlantic (15–20 Sv) and around Antarctica (~10 Sv); Southern Ocean winds bring it back up; turnover **~1000 yr**, deep flow ~1 mm/s; **Joy's Stommel: $y|1-y|=E$, hump ¼ at $y=\tfrac12$; E = 0.15 → on 0.82, unstable, reversed −0.13**; AMOC carries heat north everywhere (0.9–1.2 PW) → ITCZ north; IPCC AR6 C.3.4: very likely to weaken, medium confidence no collapse before 2100.
> - **Slow swings (CL29):** anomaly; ocean = low-pass filter (std ∝ 1/√window) **or** coupled loop; equatorial Ekman divergence + pressure gradient ($f=0$) → tilted thermocline, cold tongue, warm pool; **Bjerknes feedback** (weaker trades → flatter thermocline → warmer east → weaker trades); **Kelvin wave east, Rossby waves west and reflected → delayed negative feedback**, ~6 months to reverse, period 2–7 yr (mean ~4); IOD, Atlantic Niño.
> - **Carbon (CL29–CL30):** 1750–2024: **752 GtC; air 41 %, ocean 28 %, land 25 %**; ocean holds ~50–60× the air's carbon as HCO₃⁻/CO₃²⁻; Revelle factor; BEAM boxes 595/714/35 680 GtC, $1/k_a$ = 5 yr, turnover 1000 yr; **1000 yr → 480 ppm in 2024 (measured 425); 200 yr → 422**; stop in 2025 → **334 ppm, 22 % stays** (independent of the rates); 24 % of 1000 GtC, 42 % of 5000 GtC; no chemistry 1.6 %; Archer: 2–20 centuries / 3000–7000 yr / 10⁵ yr.
> - **Tutorials (CL27–CL28):** Daisyworld with ocean (thermal inertia, hysteresis, lags); CERES: cloud radiative effect −19.6 = −45.0 (SW) + 25.4 (LW) W m⁻²; El Niño's OLR dipole.

> [!warning] Traps (Part VI)
> 26. Ekman transport is 90° to the wind, the **surface** current only 45°.
> 27. On the equator $f=0$: the wind is balanced by a **pressure gradient**, not Coriolis.
> 28. El Niño = **weaker** trades and a **flatter** thermocline, not stronger ones.
> 29. The Bjerknes feedback alone gives a switch; the **delayed** wave feedback gives the oscillation.
> 30. The settled CO₂ level does **not** depend on the exchange times; only how fast it gets there does.
> 31. A model that fits the past (200-yr turnover) is not automatically right about the future (too fast a drawdown).
> 32. "Thermohaline" is out of favour: the Southern Ocean **winds** do much of the upwelling.
> 33. The oldest water is at **mid-depth in the North Pacific**, not at the bottom.
> 34. Joy's Stommel (fixed T, hump at ¼) ≠ CL26 §7's version (fold 0.141): use Joy's in the exam.

> [!question]- Self-test (Part VI), answers in the chapters
> 1. Why is the ocean's net TOA imbalance +1.26 W m⁻² and where does the heat go (CL22, CL23)? 2. Derive $\tau=C/\lambda$ for a 50 m mixed layer (CL23). 3. Ekman transport for τ = 0.1 N m⁻² at 30°N (CL24). 4. Why is the Bay of Bengal fresher than the Arabian Sea (CL25)? 5. Solve $y|1-y|=0.2$ for the on state (CL26 §9.6: 0.72). 6. Draw the Bjerknes loop and say which two ledgers it joins (CL29 §5). 7. Why does El Niño turn around (CL29 §6)? 8. Why did the ocean take only 28 % of our carbon (CL29 Q6)? 9. Why doesn't CO₂ return to 280 ppm (CL30 Q8)? 10. What does the no-buffer run show (CL30 Run 6)?

## Study plan (about 2 hours)
1. 20 min: read the four **syllabus maps** and **summaries** (CL09 → CL12).
2. 30 min: derive three of §3 on paper.
3. 30 min: read the four **Quiz checklists**; tick each.
4. 30 min: practice problems with the **collapsed solutions** closed; compare.
5. 10 min: this page's self-test.

## Provenance
> [!provenance]- Source map
> Checklists come from the four chapters, each verified against the book excerpt `climate-suhas merged.pdf` and cross-checked with `climate_book_notes.pdf` (AI notes). Items that the AI notes got wrong or that the book contradicts are flagged inside the chapters with `[!verify]`.
