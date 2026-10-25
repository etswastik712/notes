---
id: introduction-to-climate-science/2026-09-02-study-material-moist-and-dry-air
aliases: [Study material: Moist and dry air, Moist and dry air (Wallace & Hobbs)]
tags: [climate, introduction-to-climate-science, atmospheric-thermodynamics, virtual-temperature, gas-laws, wallace-and-hobbs]
trust_tier: agent_written
---

# Study material: Moist and dry air - Chapter 3 Wallace and Hobbs

## Covered
Source: Wallace, J. M. and Hobbs, P. V., *Atmospheric Science: An Introductory Survey* (2nd ed), Chapter 3: Atmospheric Thermodynamics, Sections 3.1 & 3.1.1, pp. 63–67 (Classroom: Study material, 2026-09-02).

### 1. The Ideal Gas Equation
Laboratory observations confirm atmospheric gases obey the ideal gas equation of state across meteorological conditions:
$$pV = m R T$$
$$p = \rho R T$$
$$p \alpha = R T \quad \left(\alpha \equiv \frac{1}{\rho}\right)$$
where $p$ is pressure ($\text{Pa}$), $V$ is volume ($\text{m}^3$), $m$ is mass ($\text{kg}$), $T$ is absolute temperature ($\text{K} = {}^\circ\text{C} + 273.15$), $\rho$ is density ($\text{kg m}^{-3}$), $\alpha$ is specific volume ($\text{m}^3\text{ kg}^{-1}$), and $R$ is the gas constant for $1\text{ kg}$ of the specific gas.

**Kinetic theory foundations:**
- Boyle's law: Isothermal process ($T = \text{const}$) $\implies p \propto 1/V$.
- Charles's first law: Isobaric process ($p = \text{const}$) $\implies V \propto T$.
- Charles's second law: Isochoric process ($V = \text{const}$) $\implies p \propto T$.
- Avogadro's hypothesis: Equal volumes of gases at identical temperature and pressure contain the same number of molecules $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$.
- Universal gas constant: For $1\text{ mol}$, $R^* = 8.3145\text{ J K}^{-1}\text{ mol}^{-1}$. For $n$ moles, $pV = n R^* T$.
- Boltzmann's constant: $k = \frac{R^*}{N_A} = 1.381 \times 10^{-23}\text{ J K}^{-1}$; microscopic equation of state: $p = n_0 k T$ (where $n_0 = N/V$ is number density).

### 2. Gas Constants for Dry Air and Water Vapor
- **Dry air:**
  Apparent molecular weight of dry air:
  $$M_d \equiv \frac{\sum_i m_i}{\sum_i (m_i / M_i)} = 28.97\text{ g mol}^{-1}$$
  Gas constant for $1\text{ kg}$ of dry air:
  $$R_d = 1000 \frac{R^*}{M_d} = 1000 \times \frac{8.3145}{28.97} = 287.0\text{ J K}^{-1}\text{ kg}^{-1}$$
  Ideal gas equation for dry air:
  $$p_d \alpha_d = R_d T \quad \iff \quad p_d = \rho_d R_d T$$
- **Water vapor:**
  Molecular weight of water vapor: $M_w = 18.016\text{ g mol}^{-1}$.
  Gas constant for $1\text{ kg}$ of water vapor:
  $$R_v = 1000 \frac{R^*}{M_w} = 1000 \times \frac{8.3145}{18.016} = 461.51\text{ J K}^{-1}\text{ kg}^{-1}$$
  Ideal gas equation for water vapor:
  $$e \alpha_v = R_v T \quad \iff \quad e = \rho_v R_v T$$
  where $e$ is the partial pressure exerted by water vapor (vapor pressure).
- **Dimensionless ratio $\epsilon$:**
  $$\epsilon \equiv \frac{R_d}{R_v} = \frac{M_w}{M_d} = \frac{18.016}{28.97} \approx 0.622$$

### 3. Dalton's Law and Moist Air Density
Dalton's law of partial pressures: The total pressure of a non-reacting mixture equals the sum of partial pressures:
$$p = p_d' + e$$
where $p_d'$ is the partial pressure of dry air and $e$ is vapor pressure.
The total density of moist air in volume $V$ is:
$$\rho = \frac{m_d + m_v}{V} = \rho_d' + \rho_v'$$
where $\rho_d' = \frac{p_d'}{R_d T} = \frac{p - e}{R_d T}$ and $\rho_v' = \frac{e}{R_v T}$.

**Why moist air is less dense than dry air:**
Because $M_w (18.016) < M_d (28.97)$, a given number of water vapor molecules has less mass than the same number of dry air molecules. By Avogadro's hypothesis, at equal temperature and pressure, substituting water vapor for dry air molecules reduces the mass per unit volume, making moist air lighter (less dense) than dry air.

### 4. Virtual Temperature ($T_v$)
Because the composition of moist air varies with water vapor content, the gas constant for moist air would vary spatially and temporally. Rather than using a variable gas constant, meteorology uses the dry air constant $R_d$ and defines a fictitious temperature called the **virtual temperature** $T_v$.

**Derivation:**
$$\rho = \rho_d' + \rho_v' = \frac{p - e}{R_d T} + \frac{e}{R_v T} = \frac{p}{R_d T} \left[ 1 - \frac{e}{p} + \frac{e}{p}\frac{R_d}{R_v} \right] = \frac{p}{R_d T} \left[ 1 - \frac{e}{p}(1 - \epsilon) \right]$$
Setting $p = \rho R_d T_v$ gives:
$$T_v = \frac{T}{1 - \frac{e}{p}(1 - \epsilon)}$$
Since $\epsilon \approx 0.622$, $1 - \epsilon \approx 0.378$:
$$T_v \approx T \left[ 1 + 0.378 \frac{e}{p} \right] \quad (\text{for } e \ll p)$$
Expressed in terms of the mixing ratio $w \equiv m_v / m_d \approx \epsilon \frac{e}{p}$:
$$T_v \approx T (1 + 0.61 w)$$

**Key Properties:**
- Virtual temperature is the temperature that dry air must have to attain the same density as moist air at the same pressure.
- Since moist air is less dense than dry air at the same $T$ and $p$, **$T_v$ is always greater than or equal to $T$** ($T_v \ge T$).
- For typical warm and humid conditions, $T_v$ exceeds $T$ by only a few degrees (e.g. $1\text{ to }3\text{ K}$).

### 5. Worked Example (Wallace & Hobbs Exercise 3.1)
- **Problem:** If at $0^\circ\text{C}$ ($T = 273.2\text{ K}$) the density of dry air alone is $\rho_d' = 1.275\text{ kg m}^{-3}$ and water vapor alone is $\rho_v' = 4.770 \times 10^{-3}\text{ kg m}^{-3}$, what is total pressure?
- **Solution:**
  - $p_d' = \rho_d' R_d T = (1.275)(287.0)(273.2) = 9.997 \times 10^4\text{ Pa} = 999.7\text{ hPa}$.
  - $e = \rho_v' R_v T = (4.770 \times 10^{-3})(461.5)(273.2) = 601.4\text{ Pa} = 6.014\text{ hPa}$.
  - $p = p_d' + e = 999.7 + 6.014 = 1005.7\text{ hPa} \approx 1006\text{ hPa}$.

## From the post
Reference: Atmospheric Science: An introductory survey by  J.M. Wallace and P.V. Hobbs

## Files
- [Circulation_Moist_and_dry_air_WH_lect1.pdf](https://drive.google.com/file/d/1ROEpQHIdNAmNr7dLTr_sHOWfxOfZUZeQ/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-circulation-moist-and-dry-air-wh-lect1-1ROEpQ.pdf)

## Related
- [[01-Climate/Concepts/Virtual Temperature]]: their concept note on virtual temperature and buoyancy
- [[01-Climate/CL05 Thermodynamic State of the Atmosphere]]: dry vs moist air, water vapor partial pressure, and gas constants
- [[01-Climate/Concepts/Ideal Gas Law]]: ideal gas formulation
- [[introduction-to-climate-science/2026-09-02-study-material-2-atmospheric-composition]]: Salby Ch 1 on atmospheric composition, Dalton's law, and gas mixtures
