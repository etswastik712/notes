---
id: introduction-to-climate-science/2026-10-08-study-material-9-mean-meridional-circulation-part-2-observation
aliases: [Study material 9: Mean meridional circulation: Part 2 observation, Marshall & Plumb Ch 5: Atmospheric Winds and Overturning Circulation]
tags: [climate, introduction-to-climate-science, meridional-circulation, hadley-cell, ferrel-cell, streamfunction, trade-winds, subtropical-jet, eddies]
trust_tier: agent_written
---

# Study material 9: Mean meridional circulation: Part 2 observation

## Covered
Source: Marshall and Plumb, *Atmosphere, Ocean and Climate Dynamics*, Chapter 5: "The meridional structure of the atmosphere", Section 5.4.1 ("Distribution of winds") (Classroom: study material 2026-10-08).

### 1. Terminology Key
- **Velocity Vector ($\mathbf{u}$):** Atmospheric motion vector resolved into eastward ($u$, zonal), northward ($v$, meridional), and upward ($w$, vertical) components: $\mathbf{u} = (u, v, w)$.
- **Subtropical Jet Stream:** A narrow, high-velocity core of upper-tropospheric zonal westerly winds ($u > 30\text{ m s}^{-1}$) located near $30^\circ$ latitude at $\sim 200\text{ mbar}$ ($\sim 10–12\text{ km}$ altitude), driven by the poleward advection of angular momentum in the Hadley cell.
- **Trade Winds:** Persistent low-level tropical easterly surface winds equatorward of $\sim 30^\circ$, directed northeasterly in the Northern Hemisphere and southeasterly in the Southern Hemisphere due to Coriolis deflection of the returning branch of the Hadley cell.
- **Meridional Overturning Streamfunction ($\chi$):** A scalar field describing mass transport in the latitude–height plane, satisfying mass conservation for zonally averaged flow.
- **Hadley Cell:** A thermally direct tropical overturning circulation with ascent near the equator, poleward flow in the upper troposphere, subsidence in the subtropics ($\sim 30^\circ$), and equatorward return flow near the surface.
- **Ferrel Cell:** A weak, thermally indirect midlatitude overturning circulation ($30^\circ–60^\circ$) with sinking motion in the subtropics and rising motion in subpolar latitudes, driven by extratropical eddy momentum and heat fluxes.
- **Trade Inversion:** A persistent temperature inversion located in the subtropics between subsiding dry air aloft and cool, moist marine boundary layer air below.
- **Baroclinic Eddies:** Large-scale synoptic transient wave disturbances (cyclones and anticyclones) that dominate mid- and high-latitude circulation, executing the bulk of extratropical heat and moisture transport.

---

### 2. Large-Scale Wind Distribution

#### A. Aspect Ratio and Vertical Velocity Magnitude
The atmospheric velocity components satisfy a severe geometric scale asymmetry:
- Horizontal scales of synoptic motion: $L \sim 1000\text{ km} = 10^6\text{ m}$.
- Vertical scale (tropospheric scale height): $H \sim 10\text{ km} = 10^4\text{ m}$.
- Aspect ratio:
  $$\frac{H}{L} \sim 10^{-2} \ll 1$$
From the continuity equation $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} \approx 0$, it follows that:
$$w \sim \frac{H}{L} U \sim 10^{-2} \times 10\text{ m s}^{-1} \sim 10^{-1}–10^{-2}\text{ m s}^{-1} \quad (\sim 1–10\text{ cm s}^{-1})$$
Except in violent convective cores, vertical velocity $w$ is two to three orders of magnitude smaller than horizontal velocities ($u, v$). It cannot usually be measured directly by anemometers and must be deduced from mass continuity or thermodynamic equations.

#### B. Mean Zonal Wind Climatology ($\bar{u}$)
Cross-sections of zonally averaged zonal wind $\bar{u}(\phi, p)$ demonstrate that eastward (westerly, $u > 0$) flow dominates almost the entire troposphere outside the equatorial boundary layer:
1. **Upper-Tropospheric Subtropical Jet:**
   - Located at approximately $200\text{ mbar}$ ($z \approx 10–12\text{ km}$) near $30^\circ$ latitude.
   - Reaches maximum intensity in the winter hemisphere: climatological mean zonal speed $\sim 30\text{ m s}^{-1}$, with instantaneous local core speeds exceeding $50\text{ m s}^{-1}$.
   - Weaker jet core ($\sim 20\text{ m s}^{-1}$) is present in the summer hemisphere.
2. **Polar Front / Eddy-Driven Jet:**
   - A secondary westerly maximum is located in midlatitudes near $45^\circ–50^\circ$, exhibiting a more barotropic structure extending to the surface.
3. **Surface Zonal Winds:**
   - Constrained by turbulent ground friction to modest speeds ($\sim 2–8\text{ m s}^{-1}$).
   - **Midlatitude Surface Westerlies:** Poleward of $\sim 30^\circ$, surface winds are westerly ($u > 0$).
   - **Tropical Surface Easterlies (Trades):** Equatorward of $\sim 30^\circ$, surface winds are easterly ($u < 0$). These low-level winds turn toward the equator, creating the northeast trades in the Northern Hemisphere and southeast trades in the Southern Hemisphere.

---

### 3. Mean Meridional Overturning Circulation

#### A. Streamfunction Formulation ($\chi$)
In spherical coordinates with radius $a$, latitude $\phi$, and height $z$, the zonally averaged continuity equation is:
$$\frac{1}{a \cos\phi} \frac{\partial}{\partial \phi} \left( \bar{v} \cos\phi \right) + \frac{1}{\rho} \frac{\partial}{\partial z} \left( \rho \bar{w} \right) = 0$$
This is identically satisfied by defining the mass overturning streamfunction $\chi(\phi, z)$:
$$\bar{v} = -\frac{1}{\rho a \cos\phi} \frac{\partial \chi}{\partial z}, \quad \bar{w} = \frac{1}{\rho a^2 \cos\phi} \frac{\partial \chi}{\partial \phi}$$
In standard units, $\chi$ is expressed in Sverdrups ($1\text{ Sv} \equiv 10^9\text{ kg s}^{-1}$). Flow circulates clockwise around positive centers of $\chi$ and anticlockwise around negative centers.

#### B. Seasonal Migration and Cell Structure
The meridional overturning circulation exhibits pronounced seasonal asymmetry:
- **December–January–February (DJF; Boreal Winter):**
  - Solar heating maximizes in the Southern Hemisphere (summer hemisphere).
  - Strong convective ascent occurs just south of the equator ($\sim 5^\circ–10^\circ\text{S}$).
  - A massive cross-equatorial Hadley cell transports air across the equator into the Northern Hemisphere, descending vigorously in the northern subtropics ($\sim 30^\circ\text{N}$).
  - The winter Hadley cell dominates the global circulation; the summer cell is virtually suppressed.
- **June–July–August (JJA; Boreal Summer):**
  - Strong ascent shifts north of the equator ($\sim 10^\circ–15^\circ\text{N}$).
  - Cross-equatorial flow carries mass into the Southern Hemisphere, descending in the southern subtropics ($\sim 30^\circ\text{S}$).
- **Annual Mean:**
  - Symmetrically smooths into two classical Hadley cells branching northward and southward, with ascent near the equator and descent in the subtropics ($\pm 30^\circ$).
  - Overturning transport in the annual mean is $\sim 100 \times 10^9\text{ kg s}^{-1}$.

#### C. Climatic Zones Linked to the Vertical Branches
- **Ascending Branch (ITCZ):** Characterized by low surface pressure, convergent trade winds, intense convective cloudiness, high precipitation, and low outgoing longwave radiation (cold anvil tops).
- **Descending Branch (Subtropical Deserts):** Air subsiding from the upper troposphere warms adiabatically by compression ($dT/dz = -\Gamma_d$). The relative humidity plummets, cloud formation is suppressed, and high surface insolation combines with high OLR. This zone defines the planet's great desert belts (Sahara, Arabian, Kalahari, Australian) and maintains the sharp trade inversion at the top of the marine boundary layer.

#### D. Extratropical Overturning: The Ferrel Cell
- Located between $30^\circ$ and $60^\circ$ latitude in each hemisphere.
- Thermally indirect: cold air rises at high latitudes ($\sim 60^\circ$) while warm air sinks in the subtropics ($\sim 30^\circ$).
- The Ferrel cell is weak ($\chi \sim 20–30\text{ Sv}$) and cannot be explained by axisymmetric radiative driving; it is forced mechanically as a residual response to the divergence of momentum and heat fluxes by extratropical eddies.

---

### 4. Synoptic Eddies and Extratropical Transport

#### A. Departure from Axisymmetry
While zonal-mean climatological sections provide a concise baseline, instantaneous weather maps (such as the 500 mbar geopotential height analysis) reveal that the extratropical atmosphere is thoroughly non-axisymmetric:
- Dominated by localized cyclones (troughs, low geopotential height) and anticyclones (ridges, high geopotential height).
- Mean meridional winds in the extratropics are very weak ($\bar{v} < 1\text{ m s}^{-1}$). Mean overturning cannot accomplish the required poleward heat transport.

#### B. Eddy Flux Decomposition
Any atmospheric field $X$ can be decomposed into its zonal mean $\bar{X}$ and eddy perturbation $X'$:
$$X(\lambda, \phi, p, t) = \bar{X}(\phi, p, t) + X'(\lambda, \phi, p, t)$$
The total meridional transport of quantity $X$ per unit mass is:
$$\overline{v X} = \bar{v}\bar{X} + \overline{v' X'}$$
- In the tropics: $\bar{v}\bar{X}$ (the mean overturning Hadley circulation) dominates heat and momentum transport.
- In the extratropics: $\bar{v} \approx 0$, and the transient eddy covariance $\overline{v' X'}$ carries virtually $100\%$ of the poleward sensible heat ($\overline{v' T'} > 0$) and moisture ($\overline{v' q'} > 0$).
- Warm, moist parcels move poleward ($v' > 0, T' > 0, q' > 0$) while cold, dry parcels move equatorward ($v' < 0, T' < 0, q' < 0$), ensuring positive net poleward heat flux.

---

### 5. Summary Table: Global Circulation Regimes

| Regime / Cell | Latitude Domain | Overturning Sense | Zonal Wind Signature | Primary Transport Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **Hadley Cell** | $0^\circ–30^\circ\text{N/S}$ | Thermally direct (warm air rises, cool air sinks) | Low-level trades; upper-level subtropical westerly jet | Mean overturning circulation ($\bar{v}, \bar{w}$) |
| **Ferrel Cell** | $30^\circ–60^\circ\text{N/S}$ | Thermally indirect (forced by eddy drag) | Deep midlatitude westerlies from surface to tropopause | Synoptic baroclinic eddies ($\overline{v' T'}, \overline{v' u'}$) |
| **Polar Cell** | $60^\circ–90^\circ\text{N/S}$ | Thermally direct (weak polar descent) | Surface polar easterlies; weak westerlies aloft | Mixed: weak mean overturning and transient waves |

---

## From the post
Reference: Atmosphere, Ocean, Climate Dynamics by J. Marshall and A. Plumb

## Files
- [Mean_meridional_circulation_observation_Marshall_and_Plumb.pdf](https://drive.google.com/file/d/1Q6fmKneJpQdxnjuuAvOtleZrW47AAHdV/view?usp=drive_web)

## Related
- [[01-climate/cl11-mean-meridional-circulation-and-angular-momentum]]: comprehensive note on the Hadley and Ferrel cells and angular momentum constraints.
- [[01-climate/concepts/hadley-cell]]: concept card for the tropical Hadley circulation.
- [[introduction-to-climate-science/2026-10-07-study-material-7-meridional-circulation-part-1]]: Part 1 covering incoming insolation and tropospheric temperature profiles.

<!-- kurooto:materialc3c03163 -->
## Concepts in Mean_meridional_circulation_observation_Marshall_and_Plumb
(none new)
<!-- /kurooto:materialc3c03163 -->
