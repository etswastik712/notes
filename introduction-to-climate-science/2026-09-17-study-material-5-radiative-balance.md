---
id: introduction-to-climate-science/2026-09-17-study-material-5-radiative-balance
aliases: [Study material 5: Radiative balance, Marshall & Plumb Ch 2: The global energy balance]
tags: [climate, introduction-to-climate-science, radiative-balance, greenhouse-effect, blackbody, solar-constant, climate-feedbacks]
trust_tier: agent_written
---

# Study material 5: Radiative balance

## Covered
Source: Marshall and Plumb, *Atmosphere, Ocean, and Climate Dynamics*, Chapter 2: "The global energy balance" (Classroom: study material 2026-09-17).

### 1. Terminology Key
- **Solar Constant ($S_0$):** The total incident solar radiative flux density per unit area normal to the solar beam at Earth's mean orbital distance ($S_0 \approx 1367\text{ W m}^{-2}$).
- **Planetary Albedo ($\alpha_p$):** The fraction of total incident solar irradiance reflected back to space by the planet's surface, atmosphere, and cloud systems (global average $\alpha_p \approx 0.30$).
- **Effective Planetary Emission Temperature ($T_e$):** The equivalent blackbody temperature of a planet required to balance absorbed solar irradiance ($T_e = 255\text{ K}$ for Earth).
- **Greenhouse Effect:** The warming of the planetary surface above its effective emission temperature ($T_s > T_e$) caused by atmospheric trace gases that are transparent to incoming solar shortwave radiation but absorb and re-emit outgoing terrestrial longwave infrared radiation.
- **Leaky Greenhouse:** An idealized atmospheric slab model possessing a non-zero longwave transmissivity ($1 - \epsilon$), where emissivity/absorptivity $\epsilon < 1$.
- **Climate Sensitivity ($\partial T_s / \partial Q$):** The equilibrium change in global-mean surface temperature resulting from an external perturbation $\delta Q$ in radiative forcing.

---

### 2. Planetary Emission Temperature and Global Energy Balance

#### A. Geometric Formulation
The Sun emits total luminosity $Q = 3.87 \times 10^{26}\text{ W}$. At mean Sun–Earth orbital radius $r = 150 \times 10^9\text{ m}$:
$$S_0 = \frac{Q}{4\pi r^2} \approx 1367\text{ W m}^{-2}$$
Because Earth is a sphere of radius $a$, it intercepts solar rays over its cross-sectional disk area $\pi a^2$:
$$\text{Total incident solar power} = S_0 \pi a^2 \approx 1.74 \times 10^{17}\text{ W}$$
Accounting for planetary reflection fraction $\alpha_p$:
$$\text{Total solar power absorbed} = (1 - \alpha_p) S_0 \pi a^2 \approx (1 - 0.30)(1.74 \times 10^{17}\text{ W}) = 1.22 \times 10^{17}\text{ W}$$
The globally averaged incident solar flux per unit surface area of the sphere ($4\pi a^2$) is:
$$\bar{F}_{\text{solar}} = \frac{S_0 \pi a^2}{4\pi a^2} = \frac{S_0}{4} \approx 342\text{ W m}^{-2}$$

#### B. Stefan–Boltzmann Balance and Derivation of $T_e$
Assuming the Earth radiates isotropically from its entire spherical surface area $4\pi a^2$ as an equivalent blackbody at effective emission temperature $T_e$:
$$\text{Total emitted terrestrial radiation} = 4\pi a^2 \sigma T_e^4$$
where $\sigma = 5.67 \times 10^{-8}\text{ W m}^{-2}\text{ K}^{-4}$.
In global radiative equilibrium:
$$\text{Absorbed Solar Power} = \text{Emitted Terrestrial Power}$$
$$(1 - \alpha_p) S_0 \pi a^2 = 4\pi a^2 \sigma T_e^4$$
Dividing by $\pi a^2$ yields the fundamental emission temperature equation:
$$T_e = \left[ \frac{S_0 (1 - \alpha_p)}{4\sigma} \right]^{1/4}$$
For Earth:
$$T_e = \left[ \frac{1367 \times (1 - 0.30)}{4 \times 5.67 \times 10^{-8}} \right]^{1/4} = [4.219 \times 10^9]^{1/4} \approx 255\text{ K} \quad (-18^\circ\text{C})$$
The radius $a$ cancels identically; $T_e$ depends strictly on orbital distance $r$ (via $S_0$) and albedo $\alpha_p$.

#### C. Planetary Comparative Data

| Planet | Distance $r$ ($10^9\text{ m}$) | Solar Constant $S_0$ ($\text{W m}^{-2}$) | Planetary Albedo $\alpha_p$ | Computed $T_e$ ($\text{K}$) | Measured $T_m$ ($\text{K}$) | Surface Temp $T_s$ ($\text{K}$) | Rotation Period $\tau$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Venus** | 108 | 2632 | 0.77 | 227 | 230 | 760 | 243 days |
| **Earth** | 150 | 1367 | 0.30 | 255 | 250 | 288 | 1.00 day |
| **Mars** | 228 | 589 | 0.24 | 211 | 220 | 230 | 1.03 days |
| **Jupiter** | 780 | 51 | 0.51 | 103 | 130 | 134 | 0.41 days |

> *Note on Jupiter:* Measured emission temperature ($T_m = 130\text{ K}$) exceeds computed solar radiative equilibrium ($T_e = 103\text{ K}$) because approximately half of Jupiter's emitted energy originates from internal gravitational contraction (Kelvin–Helmholtz mechanism).

---

### 3. Atmospheric Absorption Spectrum and Wien's Law
- **Wien's Displacement Law:** The wavelength of maximum blackbody spectral radiance satisfies:
  $$\lambda_{\max} T = 2898\,\mu\text{m K} \approx \text{constant}$$
  - For the Sun ($T_\odot \approx 6000\text{ K}$): $\lambda_{\max} \approx 0.5–0.6\,\mu\text{m}$ (visible spectrum; $95\%$ of energy between $0.25$ and $2.5\,\mu\text{m}$).
  - For Earth ($T_e \approx 255\text{ K}$): $\lambda_{\max} \approx \frac{6000}{255} \times 0.6\,\mu\text{m} \approx 14\,\mu\text{m}$ (thermal infrared).
- **Spectral Separation:** The solar shortwave and terrestrial longwave spectra have negligible spectral overlap, allowing shortwave insolation and longwave thermal emission to be analyzed independently.
- **Atmospheric Gaseous Opacity:**
  - Diatomic gases ($\text{N}_2, \text{O}_2$) comprising $>99\%$ of dry air are transparent across the infrared because symmetric nonpolar homonuclear diatomics lack permanent or transient dipole moments for IR vibration-rotation transitions.
  - Triatomic greenhouse gases ($\text{H}_2\text{O}, \text{CO}_2, \text{O}_3$) possess bending and asymmetric stretching vibrational modes with transient dipoles, producing strong IR absorption bands:
    - $\text{H}_2\text{O}$: Strong absorption below $8\,\mu\text{m}$ ($6.3\,\mu\text{m}$ vibrational band) and above $12\,\mu\text{m}$ (pure rotational band).
    - $\text{CO}_2$: Powerful $15\,\mu\text{m}$ bending vibrational band.
    - $\text{O}_3$: $9.6\,\mu\text{m}$ band in the atmospheric window, plus UV absorption bands.
  - **Atmospheric Window:** $8–12\,\mu\text{m}$ spectral region where the clear atmosphere is relatively transparent to outgoing terrestrial radiation.

---

### 4. Idealized Greenhouse Models

#### A. Single-Layer Completely Opaque Greenhouse ($\epsilon = 1$)
Assume a single isothermal atmospheric layer at temperature $T_a$, completely transparent to shortwave solar radiation and completely opaque to longwave infrared radiation.
- **Top of the Atmosphere (TOA) Energy Balance:**
  $$\frac{1}{4}(1 - \alpha_p) S_0 = A^\uparrow = \sigma T_a^4$$
  Since $\frac{1}{4}(1 - \alpha_p)S_0 = \sigma T_e^4$:
  $$\sigma T_a^4 = \sigma T_e^4 \implies T_a = T_e = 255\text{ K}$$
- **Surface Energy Balance:**
  $$S^\uparrow = \frac{1}{4}(1 - \alpha_p)S_0 + A^\downarrow$$
  $$\sigma T_s^4 = \sigma T_e^4 + \sigma T_a^4 = 2\sigma T_e^4$$
  $$T_s = 2^{1/4} T_e \approx 1.1892 \times 255\text{ K} \approx 303\text{ K}$$
  The opaque greenhouse warms the surface by $48\text{ K}$ above $T_e$, overestimating the observed mean ($288\text{ K}$) because the real atmosphere is partially transparent to IR ("leaky") and convectively cooled.

#### B. Single-Layer Leaky Greenhouse Model ($\epsilon < 1$)
Assume the atmospheric layer has infrared absorptivity/emissivity $\epsilon$ ($0 < \epsilon < 1$), where by Kirchhoff's law, emissivity equals absorptivity.
- Upwelling terrestrial emission from the surface is $S^\uparrow = \sigma T_s^4$.
- The atmosphere absorbs a fraction $\epsilon S^\uparrow$ and transmits $(1 - \epsilon) S^\uparrow$ directly to space.
- The atmospheric layer emits $A^\uparrow = A^\downarrow = \epsilon \sigma T_a^4$ upward and downward.
- **TOA Energy Balance:**
  $$\frac{1}{4}(1 - \alpha_p) S_0 = A^\uparrow + (1 - \epsilon) S^\uparrow$$
  $$\sigma T_e^4 = \epsilon \sigma T_a^4 + (1 - \epsilon)\sigma T_s^4$$
- **Surface Energy Balance:**
  $$S^\uparrow = \frac{1}{4}(1 - \alpha_p) S_0 + A^\downarrow$$
  $$\sigma T_s^4 = \sigma T_e^4 + \epsilon \sigma T_a^4$$
  $$\epsilon \sigma T_a^4 = \sigma T_s^4 - \sigma T_e^4$$
- **Combining TOA and Surface Equations:**
  $$\sigma T_e^4 = (\sigma T_s^4 - \sigma T_e^4) + (1 - \epsilon)\sigma T_s^4 = (2 - \epsilon)\sigma T_s^4 - \sigma T_e^4$$
  $$2\sigma T_e^4 = (2 - \epsilon)\sigma T_s^4$$
  $$\sigma T_s^4 = \frac{2}{2 - \epsilon} \sigma T_e^4 \implies T_s = \left(\frac{2}{2 - \epsilon}\right)^{1/4} T_e$$
- **Atmospheric Temperature:**
  $$\sigma T_a^4 = \frac{\sigma T_s^4 - \sigma T_e^4}{\epsilon} = \frac{\left( \frac{2}{2 - \epsilon} - 1 \right)\sigma T_e^4}{\epsilon} = \frac{1}{2 - \epsilon} \sigma T_e^4$$
  $$T_a = \left(\frac{1}{2 - \epsilon}\right)^{1/4} T_e = \left(\frac{1}{2}\right)^{1/4} T_s$$
- **Limiting Behaviors:**
  - $\epsilon \to 0$ (transparent atmosphere): $T_s \to T_e$, $T_a \to 2^{-1/4} T_e$.
  - $\epsilon \to 1$ (opaque atmosphere): $T_s \to 2^{1/4} T_e \approx 303\text{ K}$, $T_a \to T_e$.
  - For Earth ($T_s = 288\text{ K}, T_e = 255\text{ K}$):
    $$\left(\frac{2}{2 - \epsilon}\right)^{1/4} = \frac{288}{255} \approx 1.1294 \implies \frac{2}{2 - \epsilon} \approx 1.626 \implies \epsilon \approx 0.77$$
  - In all physical cases ($0 < \epsilon \le 1$), $T_a < T_s$: the atmosphere is always colder than the surface beneath it.

#### C. Multi-Layer Opaque Greenhouse and Surface Discontinuity
- For an atmosphere divided into $n$ opaque isothermal layers, surface temperature scales as $T_s = (n + 1)^{1/4} T_e$.
- In continuous multi-layer radiative transfer calculations, the downward IR emission from the lowest atmospheric layer is insufficient to warm the near-surface air to the ground temperature, producing an inescapable **temperature discontinuity** at the ground ($T_s \gg T_{\text{air}}(0^+)$).
- In the real atmosphere, this extreme vertical temperature gradient triggers immediate **buoyant convective overturning**, which transports sensible and latent heat vertically, eliminating the discontinuity.

---

### 5. Climate Feedbacks and Sensitivity

#### A. Blackbody (Planck) Negative Feedback
Perturbation $\delta Q$ applied to the global balance $\sigma T_e^4$:
$$\delta Q = \delta(\sigma T_e^4) = 4\sigma T_e^3 \delta T_s$$
Assuming $T_s - T_e \approx \text{const}$, the reference Stefan–Boltzmann climate sensitivity is:
$$\left( \frac{\partial T_s}{\partial Q} \right)_{\text{BB}} = \frac{1}{4\sigma T_e^3} = \frac{1}{4(5.67 \times 10^{-8})(255)^3} \approx 0.26\text{ K}/(\text{W m}^{-2})$$
A surface forcing increase of $1\text{ W m}^{-2}$ produces an unamplified blackbody warming of $\approx 0.26^\circ\text{C}$.

#### B. Water Vapor Positive Feedback
- Saturation vapor pressure obeys the Clausius–Clapeyron equation:
  $$\frac{d e_s}{e_s} = \beta dT, \quad \beta \approx 0.067^\circ\text{C}^{-1}$$
  Each $1^\circ\text{C}$ temperature rise increases saturation specific humidity by $\sim 7\%$.
- Because relative humidity remains approximately invariant under warming, actual atmospheric water vapor mass increases exponentially with temperature.
- Water vapor is Earth's primary greenhouse gas; enhanced IR absorption reduces outgoing IR, amplifying the initial warming.
- Combined blackbody and water vapor sensitivity:
  $$\left( \frac{\partial T_s}{\partial Q} \right)_{\text{BB} + \text{H}_2\text{O}} \approx 0.5\text{ K}/(\text{W m}^{-2})$$
  (Doubles the climate response of the Stefan–Boltzmann baseline).

#### C. Ice-Albedo and Cloud Feedbacks
- **Ice-Albedo Feedback (Positive):** Decreased temperature expands snow and sea-ice cover ($\alpha_{\text{ice}} \approx 0.20–0.70$, $\alpha_{\text{fresh snow}} \approx 0.75–0.95$ vs. $\alpha_{\text{ocean}} \approx 0.02–0.10$). Enhanced surface reflection lowers absorbed solar power $(1 - \alpha_p)S_0/4$, inducing further cooling.
- **Cloud Feedbacks:** Clouds double Earth's albedo from $\sim 0.15$ to $0.30$ (cooling), while absorbing upwelling terrestrial IR (warming). The net effect depends sensitively on cloud height, optical thickness, and cloud-top temperature.

## From the post
Reference:  Atmosphere, Ocean, Climate Dynamics by J. Marshall and A. Plumb.

## Files
- [Radiative_balance_Marshall_and_Plumb.pdf](https://drive.google.com/file/d/1R2b-3FY9wQjVNF3eKtQ3hDorI8iGm5Sv/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-radiative-balance-marshall-and-plumb-1R2b-3.pdf)

## Related
- [[introduction-to-climate-science/2026-09-17-study-material-6-radiative-convective-equilibrium]]: convection resolving the surface temperature discontinuity of radiative equilibrium
- [[01-climate/cl03-radiation-and-planetary-energy-balance]]: zero-dimensional energy balance, solar constant, and emission temperature
- [[01-climate/cl08-greenhouse-models]]: detailed mathematical derivations of single-layer, leaky, and two-layer greenhouse models
- [[01-climate/concepts/effective-emission-temperature]]: formal definition and calculation of $T_e$ across planetary bodies
- [[01-climate/concepts/greenhouse-effect]]: greenhouse trapping by triatomic trace gases
- [[03-thermodynamics/concepts/blackbody-radiation]]: Planck distribution, Stefan–Boltzmann law, and Wien displacement law

<!-- kurooto:material0ba276fb -->
## Concepts in Radiative_balance_Marshall_and_Plumb
[[zettel/planetary-emission-temperature]], [[zettel/stefan-boltzmann-law]], [[zettel/simple-greenhouse-model]]
<!-- /kurooto:material0ba276fb -->
