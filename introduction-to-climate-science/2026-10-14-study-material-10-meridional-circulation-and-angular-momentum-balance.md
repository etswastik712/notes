---
id: introduction-to-climate-science/2026-10-14-study-material-10-meridional-circulation-and-angular-momentum-balance
aliases: [Study material 10: Meridional circulation and Angular momentum balance, Marshall & Plumb Ch 8: General circulation of the atmosphere]
tags: [climate, introduction-to-climate-science, general-circulation, angular-momentum, hadley-cell, subtropical-jet, trade-winds, gfd-lab]
trust_tier: agent_written
---

# Study material 10: Meridional circulation and Angular momentum balance

## Covered
Source: Marshall and Plumb, *Atmosphere, Ocean and Climate Dynamics*, Chapter 8: "The general circulation of the atmosphere", Sections 8.1 ("Understanding the observed circulation") and 8.2 ("A mechanistic view of the circulation") (Classroom: study material 2026-10-14).

### 1. Terminology Key
- **Absolute Angular Momentum ($A$):** The total angular momentum of an atmospheric parcel per unit mass about Earth's rotation axis, comprising planetary rotation and relative eastward motion: $A = \Omega r^2 + u r$.
- **Planetary Angular Momentum:** Angular momentum per unit mass contributed by Earth's solid-body rotation rate $\Omega$: $A_p = \Omega (a \cos\phi)^2$.
- **Relative Angular Momentum:** Angular momentum per unit mass contributed by the zonal wind $u$ relative to the rotating surface: $A_r = u (a \cos\phi)$.
- **Global Surface Torque Balance:** The requirement that in a statistically steady state, the net frictional torque exerted by the Earth's surface on the atmosphere must integrate to zero over the globe.
- **Axisymmetric Circulation:** A hypothetical atmospheric flow field invariant with longitude ($\partial / \partial \lambda = 0$).
- **Thermal Wind Balance:** The geostrophic and hydrostatic relation linking vertical shear of the horizontal wind to horizontal temperature gradients: $\frac{\partial u}{\partial z} \approx -\frac{g}{f T_0} \frac{\partial T}{\partial y}$.
- **Length of Day ($\text{LOD}$):** The astronomical duration of one terrestrial rotation, varying by $\sim 0.1–1\text{ ms}$ seasonally due to angular momentum exchange between the fluid atmosphere and the solid Earth.

---

### 2. Demands of the Global Budgets

#### A. Global Energy vs. Angular Momentum Budgets
The general circulation is fundamentally constrained by two simultaneous global conservation requirements:
1. **Energy Budget:** The tropics experience net radiative surplus ($R_{\text{TOA}} > 0$) while high latitudes experience net radiative deficit ($R_{\text{TOA}} < 0$). To prevent runaway tropical heating and polar freezing, the fluid general circulation must transport $\approx 5.8–6.0\text{ PW}$ of energy poleward across each hemisphere.
2. **Angular Momentum Budget:**
   - In the tropics ($0^\circ–30^\circ$), surface winds are easterly ($u < 0$). Because the underlying solid Earth moves eastward faster than the atmosphere, surface friction exerts an eastward torque on the air: **the atmosphere gains westerly angular momentum from the Earth in the tropics**.
   - In midlatitudes ($30^\circ–60^\circ$), surface winds are westerly ($u > 0$). The atmosphere moves eastward faster than the Earth, so friction exerts a westward drag: **the atmosphere loses westerly angular momentum to the Earth in midlatitudes**.
   - **Net Global Steady-State Requirement:** To maintain constant global atmospheric angular momentum, the net frictional torque over the planetary surface must vanish:
     $$\int_{\text{surface}} \tau_x \, dA = 0$$
   - Therefore, the atmospheric circulation must continually transport **westerly angular momentum poleward** from the tropical source regions to the midlatitude sink regions.

#### B. Why Upper Zonal Winds Cannot Carry the Flux Alone
Although strong westerly winds dominate the upper troposphere, pure zonal flow cannot transport properties meridionally ($\int_0^{2\pi} u \, d\lambda$ has zero cross-latitude velocity). North–south transport requires a meridional overturning circulation ($v, w$) in the tropics and asymmetric eddies ($u'v'$) in the extratropics.

---

### 3. Axisymmetric Hadley Circulation and Angular Momentum Conservation

#### A. Absolute Angular Momentum on a Sphere
Consider a thin ring of air encircling the globe at latitude $\phi$. The perpendicular distance from the ring to Earth's rotation axis is:
$$r = a \cos\phi$$
where $a = 6.371 \times 10^6\text{ m}$ is Earth's mean radius.
The absolute angular momentum per unit mass $A$ is:
$$A = \Omega r^2 + u r = \Omega a^2 \cos^2\phi + u a \cos\phi$$
where:
- $\Omega = 7.292 \times 10^{-5}\text{ rad s}^{-1}$ is Earth's angular rotation rate.
- $u$ is the eastward zonal wind speed.

#### B. Upper-Branch Parcel Trajectory and Derivation of $u(\phi)$
Assume the Hadley cell is axisymmetric and friction is negligible in the upper tropospheric branch ($z \sim 10–12\text{ km}$).
- Air ascends in deep convective towers at the equator ($\phi = 0$). By equatorial symmetry, the relative zonal wind is approximately zero at the equator: $u(\phi = 0) = 0$.
- The initial absolute angular momentum per unit mass of the parcel at the equator is:
  $$A_0 = \Omega a^2 \cos^2(0) + (0) a \cos(0) = \Omega a^2$$
- As the ring of air flows poleward in the upper branch, it conserves its absolute angular momentum ($DA/Dt = 0$):
  $$A(\phi) = \Omega a^2 \cos^2\phi + u(\phi) a \cos\phi = A_0 = \Omega a^2$$
- Subtracting $\Omega a^2 \cos^2\phi$ from both sides:
  $$u(\phi) a \cos\phi = \Omega a^2 \left( 1 - \cos^2\phi \right) = \Omega a^2 \sin^2\phi$$
- Dividing by $a \cos\phi$ yields the theoretical zonal wind of an angular-momentum-conserving Hadley cell:
  $$u(\phi) = \Omega a \frac{\sin^2\phi}{\cos\phi}$$

#### C. Breakdown of the Single Equator-to-Pole Hadley Cell
Evaluating $u(\phi)$ using $\Omega a = (7.292 \times 10^{-5})(6.371 \times 10^6) \approx 464.6\text{ m s}^{-1}$:
- At $\phi = 10^\circ$:
  $$u(10^\circ) = 464.6 \times \frac{\sin^2 10^\circ}{\cos 10^\circ} = 464.6 \times \frac{0.03015}{0.9848} \approx 14.2\text{ m s}^{-1}$$
- At $\phi = 20^\circ$:
  $$u(20^\circ) = 464.6 \times \frac{\sin^2 20^\circ}{\cos 20^\circ} = 464.6 \times \frac{0.1170}{0.9397} \approx 57.9\text{ m s}^{-1}$$
- At $\phi = 30^\circ$:
  $$u(30^\circ) = 464.6 \times \frac{\sin^2 30^\circ}{\cos 30^\circ} = 464.6 \times \frac{0.2500}{0.8660} \approx 134.1\text{ m s}^{-1}$$
- As $\phi \to 90^\circ$: $\cos\phi \to 0 \implies u(\phi) \to \infty$.

**Physical Conclusion:** On a rapidly rotating planet like Earth, an axisymmetric single meridional cell extending from equator to pole (as originally hypothesized by George Hadley in 1735) is dynamically impossible.
- Angular momentum conservation accelerates poleward-moving rings to enormous eastward speeds.
- By thermal wind balance, such immense vertical wind shear requires extreme horizontal temperature gradients that cannot be radiatively supported.
- The strong Coriolis force ($f = 2\Omega\sin\phi$) deflects poleward-moving air eastward, transforming meridional flow into purely zonal flow, forming the **subtropical jet** and forcing subsidence near $\phi \approx 30^\circ$.
- Beyond $30^\circ$, axisymmetry breaks down completely due to **baroclinic instability**, handing over heat and momentum transport to extratropical eddies.

---

### 4. Vertical Structure and Surface Circulation

#### A. Subtropical Subsidence and the Trade Inversion
- Air sinking on the poleward flank of the Hadley cell ($\sim 25^\circ–35^\circ$) experiences adiabatic compression, warming at the dry adiabatic lapse rate ($\Gamma_d \approx 9.8\text{ K km}^{-1}$).
- This warm, dry subsiding air caps the cool, moist marine boundary layer, creating the robust **trade wind inversion** and suppressing deep precipitating convection across the subtropical oceans and deserts.

#### B. Low-Level Return Branch and the Trade Winds
- As air returns equatorward in the lower troposphere, Coriolis acceleration deflects it to the right in the Northern Hemisphere and to the left in the Southern Hemisphere:
  $$\frac{Du}{Dt} \approx f v$$
  Since $v < 0$ in the Northern Hemisphere, $Du/Dt < 0$, accelerating the flow westward and sustaining the **northeastern trade winds** (and southeastern trade winds in the Southern Hemisphere).
- Near-surface friction prevents the trade winds from reaching catastrophic speeds, maintaining steady velocities of $\sim 5–10\text{ m s}^{-1}$.

#### C. Midlatitude Surface Westerlies Discrepancy
- In an idealized axisymmetric model, surface westerlies would appear right at the subtropical edge ($\sim 30^\circ$).
- In the real atmosphere, surface westerlies maximize much further poleward, near $50^\circ\text{N/S}$. This poleward displacement occurs because synoptic-scale baroclinic eddies in the storm tracks converge westerly momentum into midlatitudes ($\frac{\partial}{\partial y}(\overline{u'v'}) < 0$), mechanically driving the surface westerlies.

---

### 5. Laboratory Demonstration: GFD Lab VIII (Rotating Annulus)
The dynamics of the Hadley circulation are directly reproduced in rotating laboratory tank experiments:
- **Experimental Apparatus:** A cylindrical tank containing water, with a cold cylinder at the center (representing the pole) and heated outer rim (representing the equator), placed on a rotating turntable.
- **Slow Rotation Regime ($\Omega \sim 1\text{ rpm}$):**
  - Fluid warms and rises at the outer perimeter, flows radially inward aloft, and rubs against the cold inner cylinder where it sinks.
  - Inward radial motion aloft conserves angular momentum ($V_\theta r = \text{const}$), spinning up a rapid cyclonic (eastward/westerly) jet stream in the upper fluid.
  - Near the bottom, radial outflow occurs in an Ekman boundary layer (visualized with sinking potassium permanganate crystals), deflected by Coriolis acceleration to form low-level easterlies.

---

### 6. Summary Comparison Table

| Feature / Domain | Upper Hadley Branch (Troposphere Aloft) | Lower Hadley Branch (Surface Layer) | Midlatitude Eddy Regime ($35^\circ–60^\circ$) |
| :--- | :--- | :--- | :--- |
| **Meridional Velocity ($v$)** | Poleward ($v > 0$ in NH, up to $3\text{ m s}^{-1}$) | Equatorward ($v < 0$ in NH, $\sim 2–5\text{ m s}^{-1}$) | Weak zonal-mean ($\bar{v} < 1\text{ m s}^{-1}$); strong eddy $v'$ |
| **Zonal Wind ($u$)** | Intense westerlies; subtropical jet ($>30–50\text{ m s}^{-1}$) | Steady easterlies; trade winds ($\sim 5–10\text{ m s}^{-1}$) | Deep westerlies peaking near $50^\circ$ at surface |
| **Angular Momentum Dynamic** | Advected poleward conserving $A = \Omega a^2\cos^2\phi + u a\cos\phi$ | Gained from Earth via frictional eastward torque | Transferred to Earth via surface frictional drag |
| **Dominant Physics** | Conservation of angular momentum + Coriolis deflection | Turbulent boundary layer drag + Coriolis deflection | Baroclinic instability + eddy momentum flux ($\overline{u'v'}$) |

---

## From the post
Reference: Atmosphere, Ocean and Climate Dynamics by J. Marshall and A. Plumb

## Files
- [Angular_momentum_balnce_and_meridional_circulation_Marshall_and_Plumb.pdf](https://drive.google.com/file/d/1YtfiW8GksmkA9A94GmfodxT6LbIv-GT0/view?usp=drive_web)

## Related
- [[01-climate/cl11-mean-meridional-circulation-and-angular-momentum]]: complete chapter note on angular momentum conservation and the Hadley cell.
- [[01-climate/concepts/hadley-cell]]: dedicated concept note for the tropical circulation cell.
- [[introduction-to-climate-science/2026-10-08-study-material-9-mean-meridional-circulation-part-2-observation]]: Part 2 covering observed winds, streamfunction $\chi$, and Ferrel cells.

<!-- kurooto:material45550f84 -->
## Concepts in Angular_momentum_balnce_and_meridional_circulation_Marshall_and_Plumb
[[zettel/atmospheric-energy-transport]], [[zettel/atmospheric-angular-momentum-balance]]
<!-- /kurooto:material45550f84 -->

<!-- kurooto:material92503a45 -->
## Concepts in Meridional_circulation_Marshall_and_Plumb
[[zettel/zonal-average]]
<!-- /kurooto:material92503a45 -->
