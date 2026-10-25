---
id: introduction-to-climate-science/2026-09-10-reading-manabe-and-strickler-1964
aliases: [Reading: Manabe and Strickler (1964), Thermal Equilibrium with Convective Adjustment]
tags: [climate, introduction-to-climate-science, reading, radiative-equilibrium, radiative-convective-equilibrium, convective-adjustment, manabe-strickler]
trust_tier: agent_written
---

# Reading: Manabe and Strickler (1964) Thermal Equilibrium with Convective Adjustment

## Covered
Source: Research paper `MS64.pdf` (S. Manabe and R. F. Strickler, *Journal of the Atmospheric Sciences*, 21(4), 361–385, 1964; Classroom: announcement 2026-09-10). Non-mandatory reading material for conceptual depth on radiative and radiative-convective equilibrium.

### 1. Terminology Key
- **Pure Radiative Equilibrium (RE):** A theoretical state where the vertical temperature profile is governed solely by the balance between absorbed solar flux and emitted/absorbed longwave infrared flux, without any fluid motion or turbulent heat exchange.
- **Radiative-Convective Equilibrium (RCE):** A thermodynamic steady state where vertical convective overturning neutralizes superadiabatic layers in the troposphere up to the tropopause, while pure radiative balance governs the stratosphere above.
- **Convective Adjustment:** A parameterization technique that resets the vertical lapse rate $-\partial T/\partial z$ to a critical neutral lapse rate $\Gamma_c$ whenever the radiative lapse rate exceeds $\Gamma_c$, while strictly conserving column internal energy.
- **Critical Lapse Rate ($\Gamma_c$):** The threshold lapse rate above which atmospheric parcels become buoyant; taken as the observed mean tropospheric lapse rate ($\Gamma_c = 6.5\text{ K km}^{-1}$), reflecting moist convective neutrality, or the dry adiabatic lapse rate ($\Gamma_d = 9.8\text{ or }10.0\text{ K km}^{-1}$).

---

### 2. Failure of Pure Radiative Equilibrium
When the 1D atmospheric column is integrated numerically to an asymptotic steady state with radiative transfer alone:
1. **Surface Overheating:** Solar radiation penetrates the relatively transparent atmosphere and is absorbed primarily at the surface, driving the radiative surface equilibrium temperature to an unrealistically high value ($T_s \approx 332.3\text{ K} \approx 59.3^\circ\text{C}$ for clear sky).
2. **Cold Upper Troposphere:** The upper troposphere cools intensely by IR divergence, causing extreme vertical thermal gradients ($-\partial T/\partial z > 20\text{ K km}^{-1}$ near the ground).
3. **Surface Temperature Discontinuity:** A sharp finite temperature jump develops between the ground and the air immediately adjacent to it:
   $$T_s - T_{\text{air}}(0^+) > 10\text{ K}$$
4. **Dynamical Instability:** Because $-\partial T/\partial z \gg \Gamma_d$, this profile is dynamically unstable to vertical buoyant acceleration, triggering vigorous convective overturning.

---

### 3. Formulation of Convective Adjustment
The time-stepping integration of layer temperatures is formulated as:
$$T^{\tau+1} = T^\tau + \left(\frac{\partial T}{\partial t}\right) \Delta t$$
In non-convective layers, temperature changes solely by net radiative flux divergence:
$$\left(\frac{\partial T}{\partial t}\right)_{\text{NET}} = \left(\frac{\partial T}{\partial t}\right)_{\text{RAD}} = -\frac{1}{\rho c_p} \frac{\partial F_{\text{net}}}{\partial z}$$
Whenever the lapse rate exceeds the critical lapse rate:
$$\left( -\frac{\partial T}{\partial z} \right) > \Gamma_c$$
the temperatures of the unstable layers are adjusted such that:
$$-\frac{\partial T}{\partial z} = \Gamma_c$$
subject to the exact conservation of total thermal energy across the convective layer bounded by pressure $p_{cT}$ (top) and $p_{cB}$ (bottom):
$$\frac{c_p}{g} \int_{p_{cT}}^{p_{cB}} \left(\frac{\partial T}{\partial t}\right)_{\text{NET}} dp = \frac{c_p}{g} \int_{p_{cT}}^{p_{cB}} \left(\frac{\partial T}{\partial t}\right)_{\text{RAD}} dp + (-F_0^\uparrow + S_0)$$
where $-F_0^\uparrow + S_0$ represents the net heat flux exchanged at the Earth's surface interface.

---

### 4. Roles of Individual Gaseous Absorbers

| Absorber | Active Spectral Bands | Tropospheric Impact | Stratospheric Impact |
| :--- | :--- | :--- | :--- |
| **Water Vapor ($\text{H}_2\text{O}$)** | Rotation band ($>12\,\mu\text{m}$), $6.3\,\mu\text{m}$ vibration band, near-IR solar absorption | Dominant greenhouse gas; produces major surface warming and lower tropospheric opacity. | Weak impact on upper stratosphere due to extreme aridity ($q \sim 3 \times 10^{-6}\text{ g/g}$). |
| **Carbon Dioxide ($\text{CO}_2$)** | $15\,\mu\text{m}$ bending band, $4.3\,\mu\text{m}$, $2.7\,\mu\text{m}$ | Traps outgoing IR; provides $\approx 10\text{ K}$ baseline warming at surface. | Strong IR emitter to space; acts as the primary radiative cooling agent of the stratosphere. |
| **Ozone ($\text{O}_3$)** | UV Hartley ($0.2–0.3\,\mu\text{m}$), Huggins ($0.3–0.35\,\mu\text{m}$), Chappuis ($0.5–0.7\,\mu\text{m}$), and $9.6\,\mu\text{m}$ IR | Minor surface impact ($< 1\text{ K}$ change in surface temperature). | **Essential:** Solar UV absorption creates the stratospheric temperature inversion and stabilizes the tropopause. |

> **Key Result:** Without ozone, the model atmosphere exhibits a monotonic temperature decrease with height; no stratospheric temperature inversion or well-defined tropopause forms.

---

### 5. Influence of Clouds on Equilibrium Temperature
- **Low and Middle Clouds:**
  - High shortwave albedo ($\alpha_{\text{low}} \approx 0.69$, $\alpha_{\text{mid}} \approx 0.48$).
  - High longwave blackness.
  - Shortwave reflection strongly dominates over greenhouse trapping $\implies$ **net surface cooling**.
- **High Clouds (Cirrus):**
  - Low solar albedo ($\alpha_{\text{high}} \approx 0.21$).
  - High effective infrared emissivity ($\epsilon \approx 0.50$).
  - Because cirrus resides at cold altitudes ($> 9\text{ km}$, $T \sim 220\text{ K}$), it intercepts warm surface radiation while emitting weakly to space $\implies$ **net surface warming**.

---

### 6. Equilibrium State Summary

| Model Regime | Surface Temp $T_s$ | Tropopause Height | Stratospheric Structure |
| :--- | :--- | :--- | :--- |
| **Pure Radiative (Clear)** | $332.3\text{ K}$ ($59.3^\circ\text{C}$) | $\sim 10\text{ km}$ (diffuse) | Inversion present due to $\text{O}_3$ |
| **RCE ($\Gamma_c = 10\text{ K km}^{-1}$, Dry)** | $315.0\text{ K}$ | $\sim 11\text{ km}$ | Sharp tropopause boundary |
| **RCE ($\Gamma_c = 6.5\text{ K km}^{-1}$, Clear)** | $300.3\text{ K}$ ($27.3^\circ\text{C}$) | $\sim 13\text{ km}$ | Isothermal lower stratosphere |
| **RCE ($\Gamma_c = 6.5\text{ K km}^{-1}$, Average Clouds)** | $286.9\text{ K}$ ($13.9^\circ\text{C}$) | $\sim 13\text{ km}$ | Matches Standard Atmosphere ($288\text{ K}$) |

## From the post
For interested. students: Original research paper covering Radiative and radiative-convective equilibrium concept.

Non-Mandatory reading material. It will not be used for grading or setting exam/Quiz questions.

## Files
- [MS64.pdf](https://drive.google.com/file/d/1Ts32V8piHroPoOvWsC68EUAGzgB_P9RD/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-ms64-1Ts32V.pdf)

## Related
- [[introduction-to-climate-science/2026-09-17-study-material-6-radiative-convective-equilibrium]]: textbook analytical treatment of radiative-convective equilibrium
- [[01-climate/concepts/convective-adjustment]]: convective adjustment definition, lapse rate criteria, and numerical formulation
- [[01-climate/cl09-radiative-convective-equilibrium]]: detailed lecture notes on Manabe–Strickler 1D profiles and tropopause dynamics
- [[01-climate/concepts/greenhouse-effect]]: absorption and emission spectra of $\text{H}_2\text{O}, \text{CO}_2, \text{O}_3$
