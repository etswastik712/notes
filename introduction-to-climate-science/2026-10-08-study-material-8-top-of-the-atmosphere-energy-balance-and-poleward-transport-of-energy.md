---
id: introduction-to-climate-science/2026-10-08-study-material-8-top-of-the-atmosphere-energy-balance-and-poleward-transport-of-energy
aliases: [Study material 8: Top of the atmosphere energy balance and poleward transport of energy, Hartmann Ch 2: The global energy balance]
tags: [climate, introduction-to-climate-science, energy-balance, toa-radiation, albedo, olr, poleward-energy-flux, ocean-heat-transport, atmospheric-heat-transport]
trust_tier: agent_written
---

# Study material 8: Top of the atmosphere energy balance and poleward transport of energy

## Covered
Source: D. L. Hartmann, *Global Physical Climatology*, Chapter 2: "The Global Energy Balance", Sections 2.8 ("The energy balance at the top of the atmosphere") and 2.9 ("Poleward energy flux") (Classroom: study material 2026-10-08).

### 1. Terminology Key
- **Top of the Atmosphere (TOA) Net Radiation ($R_{\text{TOA}}$):** The net radiative energy flux entering the climate system per unit horizontal surface area ($\text{W m}^{-2}$), representing the difference between absorbed solar irradiance and outgoing longwave emission.
- **Absorbed Solar Radiation ($Q_{\text{abs}}$):** Incident solar flux density minus the reflected component: $Q_{\text{abs}} = S_{\text{TOA}}(1 - \alpha)$.
- **Planetary Albedo ($\alpha_p$):** The fraction of incident solar radiation reflected by Earth's surface, clouds, and atmospheric constituents back to space; global mean $\alpha_p \approx 0.29$ ($29\%$).
- **Outgoing Longwave Radiation ($\text{OLR}$):** Upwelling terrestrial thermal infrared radiation escaping to space at the top of the atmosphere ($\text{W m}^{-2}$).
- **Horizontal Flux Divergence ($\Delta F_{ao}$):** The net horizontal rate of energy export per unit surface area by atmospheric winds and oceanic currents out of a vertical atmospheric-ocean column.
- **Petawatt ($\text{PW}$):** Standard unit of large-scale global power transport: $1\text{ PW} \equiv 10^{15}\text{ W}$.

---

### 2. Top of the Atmosphere (TOA) Radiative Balance

#### A. Governing Radiative Formulation
At the top of the atmosphere, energy exchange occurs solely via electromagnetic radiation. Satellite radiometry (CERES, ERBE) resolves the local energy balance:
$$R_{\text{TOA}} = Q_{\text{abs}} - \text{OLR}$$
$$Q_{\text{abs}} = S_{\text{TOA}}(1 - \alpha)$$
where $S_{\text{TOA}}$ is incident solar irradiance and $\alpha$ is regional albedo.

#### B. Spatial Distribution of Planetary Albedo ($\alpha$)
The annual mean planetary albedo shows marked geographical structure (CERES 2000–2013):
1. **Polar Caps ($\alpha > 0.60$):** Highest albedos occur over polar regions where extensive snow cover, sea ice, and persistent low cloudiness coincide with large solar zenith angles. High zenith angles lengthen the atmospheric path and enhance surface reflection.
2. **Bright Deserts ($\alpha \approx 0.35–0.45$):** Secondary albedo maxima occur over subtropical arid regions, notably the Sahara and Arabian deserts, due to quartz-rich sand mineralogy.
3. **Deep Convective Clouds ($\alpha \approx 0.30–0.45$):** Distinct tropical maxima occur along the Intertropical Convergence Zone (ITCZ) and the Western Pacific Warm Pool due to thick cirrus and cumulonimbus anvils.
4. **Cloud-Free Oceans ($\alpha \approx 0.08–0.10$):** Clear open water possesses the lowest albedo on Earth ($8–10\%$), absorbing over $90\%$ of incident insolation.

#### C. Spatial Distribution of Outgoing Longwave Radiation ($\text{OLR}$)
Because thermal emission is governed by the Stefan–Boltzmann law ($\propto \sigma T^4$), $\text{OLR}$ is controlled by the temperature of the emitting layer:
- **Deserts and Subtropical Oceans ($>280\text{ W m}^{-2}$):** The highest $\text{OLR}$ values are observed over warm subtropical deserts and cloud-free oceans, where hot surface temperatures emit directly through a dry, transparent atmospheric window.
- **Deep Convection and Polar Caps ($<180\text{ W m}^{-2}$):** The lowest $\text{OLR}$ values occur over polar ice sheets (due to cold surface temperatures) and over the ITCZ/monsoon convergence zones, where high cloud tops emit at upper tropospheric temperatures ($T \sim 200–220\text{ K}$).

#### D. Net Radiation ($R_{\text{TOA}}$) and the Desert Radiative Deficit
- **Tropical Surplus:** Net radiation is strongly positive across tropical and summer subtropical oceans, reaching peaks of $\sim 140\text{ W m}^{-2}$ where insolation is intense and ocean albedo is small.
- **Polar Deficit:** Net radiation is strongly negative poleward of $\sim 40^\circ$ latitude in both hemispheres, with severe energy losses during winter polar darkness where $\text{OLR}$ operates with zero compensating insolation.
- **The Subtropical Desert Energy Paradox:** Despite located in subtropical latitudes with plentiful insolation, arid regions like the Sahara experience a **negative net annual radiation balance** ($R_{\text{TOA}} < 0$). This occurs because high surface albedo reduces $Q_{\text{abs}}$, while high surface temperature and low atmospheric humidity permit huge $\text{OLR}$ loss to space.
  - *Dynamical Compensation:* Because land cannot transport heat horizontally, this TOA radiative deficit is balanced by lateral atmospheric heat convergence: upper-level air subsides over the desert, warming adiabatically during compression and maintaining desert aridity.

---

### 3. Poleward Energy Flux

#### A. Energy Balance Equation for the Fluid Column
For a vertical atmospheric-ocean column extending from the ocean bottom to TOA, neglecting energy exchange with the solid Earth:
$$\frac{\partial E_{ao}}{\partial t} = R_{\text{TOA}} - \Delta F_{ao}$$
where:
- $\partial E_{ao}/\partial t$ is the rate of change of internal, potential, and latent energy storage.
- $\Delta F_{ao}$ is the horizontal divergence of the combined atmospheric and oceanic heat flux.

Averaged over a full annual cycle, the storage rate vanishes ($\partial E_{ao}/\partial t \approx 0$):
$$R_{\text{TOA}} = \Delta F_{ao}$$
The local net radiative imbalance at TOA is identically balanced by the divergence of horizontal fluid heat transport.

#### B. Polar Cap Integration
To determine the total northward energy flux $F(\phi)$ across a given latitude circle $\phi$, we integrate the net radiation over a polar cap extending from the South Pole ($-\pi/2$) to latitude $\phi$:
$$F(\phi) = \int_{-\pi/2}^\phi \int_0^{2\pi} R_{\text{TOA}}(\lambda, \phi') \, a^2 \cos\phi' \, d\lambda \, d\phi'$$
where $a = 6.371 \times 10^6\text{ m}$ is Earth's mean radius.
Using the zonal-mean net radiation $\bar{R}_{\text{TOA}}(\phi') = \frac{1}{2\pi}\int_0^{2\pi} R_{\text{TOA}}\, d\lambda$:
$$F(\phi) = 2\pi a^2 \int_{-\pi/2}^\phi \bar{R}_{\text{TOA}}(\phi') \cos\phi' \, d\phi'$$

- **Global Conservation Boundary Condition:** Because a spherical planet cannot export heat laterally to outer space:
  $$F(\pi/2) = 2\pi a^2 \int_{-\pi/2}^{\pi/2} \bar{R}_{\text{TOA}}(\phi') \cos\phi' \, d\phi' = 0$$
  The global-mean net radiation must be zero for equilibrium. Any residual reflects planetary warming or cooling.

---

### 4. Atmospheric vs. Oceanic Heat Transport Partition

The total required poleward heat flux $F(\phi)$ peaks in mid-latitudes at approximately:
$$F_{\text{peak}} \approx 5.8\text{ PW} \quad (5.8 \times 10^{15}\text{ W}) \quad \text{near } 35^\circ–40^\circ\text{N/S}$$

#### A. Partitioning Methodology
- **Atmospheric Transport ($F_{\text{atmos}}$):** Directly integrated from atmospheric reanalysis data (ECMWF ERA-Interim, NCEP) by vertically integrating the fluxes of sensible heat, latent heat, and geopotential energy:
  $$F_{\text{atmos}}(\phi) = 2\pi a \cos\phi \int_0^{p_0} \overline{v \left(c_p T + gz + L_v q\right)} \frac{dp}{g}$$
- **Oceanic Transport ($F_{\text{ocean}}$):** Calculated as the residual by subtracting atmospheric flux from satellite-inferred total flux:
  $$F_{\text{ocean}}(\phi) = F_{\text{total}}(\phi) - F_{\text{atmos}}(\phi)$$

#### B. Latitudinal Partitioning Characteristics
1. **Subtropics ($20^\circ\text{N}$):**
   - The total flux is approximately $4.0\text{ PW}$.
   - Atmospheric and oceanic transports contribute equally: $F_{\text{ocean}} \approx 2.0\text{ PW}$ and $F_{\text{atmos}} \approx 2.0\text{ PW}$.
   - Oceanic transport achieves its global maximum near $20^\circ\text{N}$, driven by wind-driven subtropical gyres and western boundary currents (Gulf Stream, Kuroshio).
2. **Midlatitudes ($40^\circ–60^\circ$):**
   - Oceanic heat transport drops off rapidly poleward of $30^\circ–40^\circ$.
   - The broad global peak of $5.8\text{ PW}$ at $40^\circ$ is dominated by atmospheric transport ($F_{\text{atmos}} > 4.5\text{ PW}$), executed predominantly by synoptic-scale baroclinic eddies and transient cyclones.
3. **Hemispheric Asymmetry:**
   - Oceanic transport is somewhat stronger in the Northern Hemisphere than in the Southern Hemisphere due to the Atlantic Meridional Overturning Circulation (AMOC), which transports heat northward across the equator.

---

### 5. Summary Table: Energy Balance Components

| Latitude Zone | $Q_{\text{abs}}$ ($\text{W m}^{-2}$) | $\text{OLR}$ ($\text{W m}^{-2}$) | $R_{\text{TOA}}$ Balance | Dominant Transport Mechanism | Peak Heat Flux |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tropics ($0^\circ–20^\circ$)** | $>300$ | $230–260$ | Surplus ($+40$ to $+100$) | Hadley cell (atmosphere) + Ekman flow | Rises from $0$ to $4.0\text{ PW}$ |
| **Subtropics ($20^\circ–35^\circ$)** | $250–300$ | $>270$ | Surplus/Neutral | Ocean subtropical gyres + Hadley upper branch | Ocean peaks at $2.0\text{ PW}$ ($20^\circ\text{N}$) |
| **Midlatitudes ($35^\circ–60^\circ$)** | $150–220$ | $210–240$ | Deficit ($-20$ to $-60$) | Extratropical synoptic eddies (transient waves) | Total peaks at $5.8\text{ PW}$ ($40^\circ$) |
| **Polar Caps ($60^\circ–90^\circ$)** | $<100$ | $150–190$ | Severe Deficit ($<-80$) | Atmospheric eddy sensible heat transport | Declines to $0$ at the poles |

---

## From the post
Reference: Global physical climatology by D. L. Hartmann

## Files
- [TOA_energy_balance_and_poleward_energy_transport_Hartmann.pdf](https://drive.google.com/file/d/1WopmOttTxdHce-mlu7tuq7erm1iOU9v6/view?usp=drive_web)

## Related
- [[01-climate/cl10-global-energy-balance-and-meridional-structure]]: comprehensive chapter note on global energy balance and observed transport.
- [[01-climate/concepts/poleward-energy-transport]]: core concept note detailing the 5.8 PW midlatitude energy transport.
- [[introduction-to-climate-science/2026-10-07-study-material-7-meridional-circulation-part-1]]: Part 1 covering insolation geometry and tropospheric thermal structure.
