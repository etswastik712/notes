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

## Study plan (about 2 hours)
1. 20 min: read the four **syllabus maps** and **summaries** (CL09 → CL12).
2. 30 min: derive three of §3 on paper.
3. 30 min: read the four **Quiz checklists**; tick each.
4. 30 min: practice problems with the **collapsed solutions** closed; compare.
5. 10 min: this page's self-test.

## Provenance
> [!provenance]- Source map
> Checklists come from the four chapters, each verified against the book excerpt `climate-suhas merged.pdf` and cross-checked with `climate_book_notes.pdf` (AI notes). Items that the AI notes got wrong or that the book contradicts are flagged inside the chapters with `[!verify]`.
