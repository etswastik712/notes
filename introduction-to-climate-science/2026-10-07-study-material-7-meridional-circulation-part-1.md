---
id: introduction-to-climate-science/2026-10-07-study-material-7-meridional-circulation-part-1
aliases: [Study material 7: Meridional circulation part1, Marshall & Plumb Ch 5: Meridional structure of the atmosphere]
tags: [climate, introduction-to-climate-science, meridional-circulation, insolation, milankovitch-cycles, energy-balance, potential-temperature]
trust_tier: agent_written
---

# Study material 7: Meridional circulation part1

## Covered
Source: Marshall and Plumb, *Atmosphere, Ocean and Climate Dynamics*, Chapter 5: "The meridional structure of the atmosphere", Sections 5.1.1–5.1.4 (Classroom: study material 2026-10-07).

### 1. Terminology Key
- **Climatology:** Long-term temporal average (annual mean, seasonal mean, or monthly climatology) of atmospheric and oceanic state variables over a specified multi-year reference epoch, frequently zonally averaged across longitude.
- **Zonal Average ($\bar{X}$):** Longitudinal mean of a field $X(\lambda, \phi, z)$ around a circle of latitude $\phi$:
  $$\bar{X}(\phi, z) = \frac{1}{2\pi} \int_0^{2\pi} X(\lambda, \phi, z) \, d\lambda$$
- **Insolation:** Instantaneous or time-integrated incident solar radiative flux density arriving at the top of the atmosphere (TOA) normal to a horizontal terrestrial surface ($\text{W m}^{-2}$).
- **Axial Obliquity ($\delta$):** The tilt angle of Earth's rotational spin axis relative to the normal of its orbital revolution plane around the Sun, currently $\delta \approx 23.45^\circ \approx 23.5^\circ$.
- **Isentropic Surface:** A continuous surface of constant potential temperature ($\theta = \text{constant}$), equivalent to a surface of constant specific dry entropy $s = c_p \ln\theta + \text{constant}$.
- **Tropopause:** The dynamic and thermodynamic boundary separating the turbulently mixed, convectively conditioned troposphere below from the stably stratified, radiatively conditioned stratosphere above.
- **Milankovitch Cycles:** Quasi-periodic perturbations in Earth's orbital geometry—eccentricity ($100\text{ kyr}, 400\text{ kyr}$), obliquity/tilt ($41\text{ kyr}$), and precession ($21\text{ kyr}$)—modulating the latitudinal and seasonal distribution of insolation.

---

### 2. Radiative Forcing and Incoming Solar Radiation

#### A. Spherical Geometry and the Non-Tilted Baseline
Earth intercepts an essentially parallel beam of solar irradiance with flux density $S_0 \approx 1367\text{ W m}^{-2}$. Because the planet is spherical, the local angle of incidence $\theta_z$ (solar zenith angle) varies with latitude.
- In the hypothetical case where Earth's spin axis has zero tilt ($\delta = 0$):
  - At the equator ($\phi = 0$), incoming rays arrive normal to the surface at solar noon. The diurnal average incident flux maximizes at:
    $$S_{\max} = \frac{S_0}{\pi} \approx \frac{1367}{\pi} \approx 435\text{ W m}^{-2}$$
  - Away from the equator, the 24-hour mean incident flux decreases strictly monotonically with latitude as $\bar{S}(\phi) = \frac{S_0}{\pi} \cos\phi$, falling identically to zero at the poles ($\phi = \pm 90^\circ$).

#### B. Impact of Axial Obliquity ($\delta = 23.5^\circ$)
Because Earth's rotational axis tilts by $23.5^\circ$ toward the North Star, the subsolar latitude oscillates between the Tropic of Cancer ($23.5^\circ\text{N}$) at northern summer solstice and the Tropic of Capricorn ($23.5^\circ\text{S}$) at northern winter solstice.
- **Summer Pole Insolation Paradox:** At the summer solstice, polar day provides 24 hours of continuous daylight poleward of the Arctic/Antarctic circles ($66.5^\circ$). Although the solar zenith angle is oblique ($\cos\theta_z \le \sin 23.5^\circ \approx 0.399$), the continuous duration of illumination causes the daily averaged TOA insolation to exhibit a slight maximum at the summer pole (exceeding $500\text{ W m}^{-2}$, higher than at the equator).
- **Surface Absorption vs. Albedo:** Despite this peak in incident TOA irradiance, net absorbed solar radiation at the summer pole remains very low because high-albedo sea ice and snow ($\alpha \approx 0.60–0.90$) reflect most incoming photons back to space.
- **Annual Equator-to-Pole Insolation Gradient:** Axial tilt permits polar latitudes to receive solar radiation during their respective summer half-years, substantially reducing the annual-mean equator-to-pole insolation gradient relative to a non-tilted planet.

#### C. Orbital Eccentricity vs. Axial Tilt
- Earth's orbit is slightly elliptical ($e \approx 0.0167$). Perihelion occurs in early January (Earth closest to the Sun; incident flux $\sim +3.4\%$ above annual mean), while aphelion occurs in early July (flux $\sim -3.4\%$).
- Although non-negligible, this $\sim \pm 3.4\%$ flux modulation is minor compared to the dominant seasonal insolation shifts induced by axial obliquity.

---

### 3. Outgoing Longwave Radiation and Net Energy Balance

#### A. TOA Absorbed Solar vs. Emitted Terrestrial Radiation
Averaged over the annual cycle, satellite observations (ERBE, CERES) reveal the global radiative budget:
1. **Absorbed Solar Radiation ($Q_{\text{abs}}$):** Strongly concentrated in the tropics, where high solar elevation and low oceanic albedo produce values exceeding $300\text{ W m}^{-2}$. Tropical absorption is approximately six times larger than polar absorption ($Q_{\text{abs, pole}} \sim 50\text{ W m}^{-2}$).
2. **Outgoing Longwave Radiation ($\text{OLR}$):** Emitted terrestrial radiation exhibits a much weaker latitudinal gradient than absorbed solar radiation, decreasing only moderately from $\sim 250–270\text{ W m}^{-2}$ in the subtropics to $\sim 150–180\text{ W m}^{-2}$ at high latitudes.
   - *Equatorial OLR Dip:* A distinct local minimum in annual-mean OLR occurs over the equatorial belt ($\sim 5^\circ\text{N}–5^\circ\text{S}$). This is caused by cold, high cloud tops associated with deep convective towers along the Intertropical Convergence Zone (ITCZ), which emit at low temperatures ($T \sim 200–220\text{ K}$).

#### B. Latitudinal Imbalance and Required Poleward Energy Transport
- **Surplus and Deficit Zones:**
  - Equatorward of $\sim 35^\circ–40^\circ$ latitude, absorbed solar radiation exceeds OLR, creating a net radiative surplus ($R_{\text{TOA}} > 0$).
  - Poleward of $\sim 35^\circ–40^\circ$ latitude, emitted longwave radiation exceeds absorbed solar radiation, creating a persistent net radiative deficit ($R_{\text{TOA}} < 0$).
- **Poleward Transport:** Because local heat content does not experience secular runaway heating in the tropics or runaway cooling at the poles, steady-state thermodynamic balance requires a continuous poleward transport of energy across each latitude circle.
- **Magnitude:** Satellite radiation budget integration demonstrates that the required poleward energy transport reaches an annual-mean peak of approximately:
  $$\mathcal{F}_{\text{total}} \approx 5.8–6.0\text{ PW} \quad (1\text{ PW} \equiv 10^{15}\text{ W})$$
  in each hemisphere near $35^\circ–40^\circ$ latitude, accomplished jointly by atmospheric winds and oceanic currents.

---

### 4. Observed Meridional Thermal Structure of the Troposphere

#### A. Zonal-Mean Temperature Distribution ($\bar{T}$)
- **Vertical Gradient:** In the troposphere, $\partial \bar{T}/\partial z < 0$ everywhere due to radiative-convective adjustment, maintaining an average tropospheric lapse rate of $\Gamma \sim 6.5\text{ K km}^{-1}$.
- **Horizontal Gradient:** Temperature decreases poleward ($\partial \bar{T}/\partial \phi < 0$).
  - Annual-mean surface temperature reaches a maximum of $\sim 27^\circ\text{C}$ ($300\text{ K}$) just north of the equator (the thermal equator at $\sim 5^\circ\text{N}$).
  - Surface temperatures drop below $0^\circ\text{C}$ poleward of $\sim 60^\circ$ latitude.
  - The annual-mean surface equator-to-pole temperature difference across the troposphere is $\Delta T \approx 40^\circ\text{C}$.

#### B. Potential Temperature ($\bar{\theta}$) and Isentropic Slopes
Potential temperature is defined by Poisson's relation:
$$\theta = T \left( \frac{p_0}{p} \right)^{R_d / c_p}, \quad p_0 = 1000\text{ mbar}, \quad \frac{R_d}{c_p} \approx \frac{287}{1004} \approx 0.286$$
- **Dry Static Stability:** Throughout the entire atmosphere, potential temperature strictly increases with height:
  $$\frac{\partial \bar{\theta}}{\partial z} > 0$$
  confirming that the atmosphere is stable to dry vertical convection on large scales ($N^2 > 0$).
- **Poleward Slope of Isentropes:** Surfaces of constant $\bar{\theta}$ (isentropes) slope upward from the tropics toward the poles throughout the troposphere. A fluid parcel displaced along an upward-sloping isentrope moves poleward and upward without experiencing dry buoyant resistance, a key geometric configuration for extratropical baroclinic eddies.
- **Troposphere vs. Stratosphere:**
  - In the troposphere, isentropic contours are widely spaced, reflecting moderate static stability.
  - In the stratosphere, isentropic contours become tightly packed, reflecting extreme static stability generated by ozone UV absorption.
- **Tropopause Height:** The tropopause slopes downward from an altitude of $\sim 16–17\text{ km}$ ($\sim 100\text{ mbar}$) in the tropics to $\sim 8–9\text{ km}$ ($\sim 300\text{ mbar}$) over the polar caps. Consequently, the tropical tropopause is much colder ($T \sim 190–200\text{ K}$) than the polar tropopause ($T \sim 220–230\text{ K}$).

---

### 5. Comparative Summary Table

| Parameter / Feature | Equatorial & Tropical Belt ($0^\circ–20^\circ$) | Subtropical Belt ($20^\circ–35^\circ$) | Polar Cap ($60^\circ–90^\circ$) |
| :--- | :--- | :--- | :--- |
| **Annual TOA Insolation** | Maximum ($\sim 380–420\text{ W m}^{-2}$) | High ($\sim 300–350\text{ W m}^{-2}$) | Minimum ($\sim 130–180\text{ W m}^{-2}$) |
| **Solstice Insolation** | Moderately steady year-round | Seasonal oscillation | 24-hr polar night (winter) / 24-hr polar day (summer) |
| **Planetary Albedo** | Moderate ($\sim 0.25$) except deep clouds | Minimum over clear oceans ($\sim 0.10$), high in Sahara | Maximum ($\sim 0.60–0.85$) due to snow/ice |
| **Net TOA Radiation** | Strongly positive (surplus) | Positive (except dry deserts) | Strongly negative (deficit) |
| **Tropospheric Depth** | Deep ($\sim 16–17\text{ km}$) | Intermediate ($\sim 12–14\text{ km}$) | Shallow ($\sim 8–9\text{ km}$) |
| **Tropopause Temperature** | Extremely cold ($T \sim 195\text{ K}$) | Intermediate ($T \sim 210\text{ K}$) | Relatively warmer ($T \sim 225\text{ K}$) |

---

## From the post
Reference: Atmosphere, Ocean and Climate Dynamics by J. Marshall and A. Plumb

## Files
- [Meridional_circulation_Marshall_and_Plumb.pdf](https://drive.google.com/file/d/19ybgMnexZ4nhQa85IhcCJOAMFkn3waS8/view?usp=drive_web)

## Related
- [[01-climate/cl10-global-energy-balance-and-meridional-structure]]: detailed chapter note covering planetary radiative balance and the observed meridional temperature distribution.
- [[01-climate/concepts/poleward-energy-transport]]: core concept note on the required atmospheric and oceanic heat flux.
- [[maps/courses/introduction-to-climate-science]]: course index and lecture syllabus map.
