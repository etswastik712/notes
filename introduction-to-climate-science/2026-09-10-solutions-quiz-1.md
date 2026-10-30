---
id: introduction-to-climate-science/2026-09-10-solutions-quiz-1
aliases: [Solutions to Quiz 1, Quiz 1 Solutions]
tags: [climate, introduction-to-climate-science, quiz, solutions, hydrostatic-balance, pressure-gradient, radiation]
trust_tier: agent_written
---

# Solutions to Quiz 1

## Covered
Source: Classroom Quiz 1 solutions document, `Solutions_Quiz1.pdf` (Classroom: announcement 2026-09-10), and numerical demo (Classroom: announcement 2026-09-11).

### Question 1: Pressure Gradients and Air Density

#### A. Horizontal Pressure Gradient in a Cyclone
- **Given parameters:**
  - Radial distance from cyclone center: $r = 1000\text{ km} = 10^6\text{ m}$
  - Eye pressure: $P_{\text{eye}} = 930\text{ hPa}$
  - Environmental sea-level pressure: $P_{\text{env}} = 1013\text{ hPa}$
- **Derivation & Calculation:**
  The radial pressure difference across the cyclone is:
  $$\Delta P = P_{\text{env}} - P_{\text{eye}} = 1013\text{ hPa} - 930\text{ hPa} = 83\text{ hPa} = 8.3 \times 10^3\text{ Pa}$$
  The horizontal pressure gradient magnitude is approximated by finite difference:
  $$\left| \frac{\partial P}{\partial r} \right| \approx \frac{\Delta P}{\Delta r} = \frac{8300\text{ Pa}}{10^6\text{ m}} = 8.3 \times 10^{-3}\text{ Pa m}^{-1}$$
  (Marking scheme: $1/2$ mark for correct formula, $1/2$ mark for correct units).

#### B. Vertical Pressure Gradient at Sea Level
- **Given parameters:**
  - Sea-level air density: $\rho \approx 1.225\text{ kg m}^{-3}$
  - Gravitational acceleration: $g = 9.81\text{ m s}^{-2}$
- **Derivation & Calculation:**
  By the hydrostatic equation:
  $$\frac{\partial P}{\partial z} = -\rho g$$
  The magnitude of the vertical pressure gradient is:
  $$\left| \frac{\partial P}{\partial z} \right| = \rho g = (1.225\text{ kg m}^{-3})(9.81\text{ m s}^{-2}) \approx 12.0\text{ Pa m}^{-1} \approx 12\text{ Pa m}^{-1}$$
  Ratio of vertical to horizontal pressure gradient magnitudes:
  $$\frac{|\partial P / \partial z|}{|\partial P / \partial r|} = \frac{12\text{ Pa m}^{-1}}{8.3 \times 10^{-3}\text{ Pa m}^{-1}} \approx 1.4 \times 10^3$$
  (Marking scheme: $1/2$ mark for calculating vertical pressure gradient, $1/2$ mark for comparison ratio).

#### C. Dynamical Implication
- The vertical pressure gradient is $\sim 1400$ times larger than the horizontal pressure gradient ($|\partial P/\partial z| \gg |\partial P/\partial r|$).
- **Physical consequence:** The vertical acceleration $dw/dt$ is negligible compared to individual vertical force terms ($-\frac{1}{\rho}\frac{\partial P}{\partial z}$ and $g$), validating the assumption of hydrostatic balance for large-scale synoptic atmospheric motion.

#### D. Density of Air at 5 km Below Mean Sea Level
- **Given parameters:**
  - Sea-level pressure: $P_0 = 101325\text{ Pa}$
  - Depth below mean sea level: $z = -5\text{ km} = -5000\text{ m}$
  - Atmospheric scale height: $H = 8400\text{ m}$ (given in question paper)
  - Dry air gas constant: $R_d = 287\text{ J K}^{-1}\text{ kg}^{-1}$
  - Reference temperature: $T = 288\text{ K}$
- **Calculation:**
  Using the isothermal barometric relationship $P(z) = P_0 e^{-z/H}$:
  $$P(-5000\text{ m}) = 101325 \exp\left(-\frac{-5000}{8400}\right) = 101325 e^{5000/8400} \approx 101325 e^{0.5952} \approx 1.84 \times 10^5\text{ Pa}$$
  Using the ideal gas equation of state $P = \rho R_d T$:
  $$\rho = \frac{P}{R_d T} = \frac{1.84 \times 10^5\text{ Pa}}{(287\text{ J kg}^{-1}\text{ K}^{-1})(288\text{ K})} \approx 2.23\text{ kg m}^{-3}$$

---

### Question 2: Solar Radiation and Mass-Energy Conversion

#### A. Total Radiative Power Emitted by the Sun
- **Model:** Approximating the Sun as a spherical blackbody of radius $R_{\odot}$ and effective temperature $T_{\odot}$.
- **Formulation via Stefan–Boltzmann law:**
  The radiative flux per unit area emitted at the solar photosphere is:
  $$F_\odot = \sigma T_\odot^4$$
  Integrating over the total surface area of the solar sphere ($A = 4\pi R_{\text{sun}}^2$):
  $$P_{\text{sun}} = 4\pi R_{\text{sun}}^2 \sigma T_{\text{sun}}^4 \approx 3.8 \times 10^{26}\text{ W} = 3.8 \times 10^{26}\text{ J s}^{-1}$$
- **Alternative formulation via Solar Constant ($S_\odot$):**
  At mean Sun–Earth distance $R_{\text{sun-earth}}$:
  $$S_\odot = \frac{4\pi R_{\text{sun}}^2}{4\pi R_{\text{sun-earth}}^2} \sigma T_{\text{sun}}^4 = \frac{P_{\text{sun}}}{4\pi R_{\text{sun-earth}}^2}$$
  $$P_{\text{sun}} = S_\odot \cdot 4\pi R_{\text{sun-earth}}^2$$

#### B. Rate of Solar Mass Conversion into Energy via Nuclear Fusion
- **Einstein mass–energy equivalence:**
  $$E = m c^2$$
  Differentiating with respect to time $t$:
  $$\frac{dE}{dt} = c^2 \frac{dm}{dt} \implies \frac{dm}{dt} = \frac{1}{c^2}\frac{dE}{dt}$$
  Substituting the total solar radiant luminosity $\frac{dE}{dt} = P_\odot \approx 3.8 \times 10^{26}\text{ W}$ and speed of light $c \approx 3.0 \times 10^8\text{ m s}^{-1}$:
  $$\frac{dm}{dt} = \frac{3.8 \times 10^{26}\text{ J s}^{-1}}{(3.0 \times 10^8\text{ m s}^{-1})^2} = \frac{3.8 \times 10^{26}}{9.0 \times 10^{16}}\text{ kg s}^{-1} \approx 4.2 \times 10^9\text{ kg s}^{-1}$$
  The Sun converts approximately $4.2 \times 10^9\text{ kg}$ of mass into radiant energy every second.

#### C. Neglect of Solar Longwave Radiation in Earth's Energy Balance
- **Physical principle:**
  - Stefan–Boltzmann flux at the Sun's surface is $F_\odot = \sigma T_\odot^4$. While the solar blackbody curve at $T_\odot \approx 6000\text{ K}$ emits higher intensity per unit area across all wavelengths (including the infrared) than Earth does at $T_e \approx 255\text{ K}$ (Figure 1 in solutions), the geometric dilution factor between the Sun and Earth is immense:
    $$\frac{F_{\text{Earth}}}{F_\odot} = \frac{R_{\odot}^2}{R_{\text{sun-earth}}^2} \approx \left(\frac{6.96 \times 10^8\text{ m}}{1.496 \times 10^{11}\text{ m}}\right)^2 \approx 2.16 \times 10^{-5}$$
  - The flux reaching the Earth's orbit is:
    $$F_{\text{Earth}} = \frac{P_\odot}{4\pi R_{\text{sun-earth}}^2}$$
  - At Earth's orbit, the incident solar spectrum is concentrated almost entirely in short wavelengths ($\sim 95\%$ between $0.25$ and $2.5\,\mu\text{m}$, peaking in visible at $\sim 0.5\,\mu\text{m}$). The longwave tail of solar radiation incident on Earth is negligible compared to the total incoming shortwave flux ($S_0 \approx 1367\text{ W m}^{-2}$).
  - Concurrently, Earth's own emission is purely longwave thermal infrared ($4–100\,\mu\text{m}$, peaking near $14\,\mu\text{m}$). Therefore, Earth's energy balance can be decoupled into incoming solar shortwave radiation versus outgoing terrestrial longwave radiation without introducing significant error.

---

### Question 3 Follow-up: Temperature Response to Emissivity ($\epsilon$) Oscillations
- **Problem context:** Numerical demo analyzing how equilibrium temperature varies when atmospheric emissivity $\epsilon$ periodically oscillates between $0.8$ and $0.4$ over a 100 Myr cycle (Figure 2 in solutions and Colab demonstration).
- **Physical relationship:**
  In a single-layer leaky greenhouse model:
  $$T_s = \left(\frac{2}{2 - \epsilon}\right)^{1/4} T_e$$
  As emissivity $\epsilon$ decreases from $0.8$ to $0.4$, the greenhouse trapping decreases, shifting $T_s$ from $[2/(1.2)]^{1/4} T_e \approx 1.136\, T_e$ down to $[2/(1.6)]^{1/4} T_e \approx 1.057\, T_e$, tracking the 100 Myr orbital/geological forcing cycle.

## From the post
**2026-09-10 post:**
Dear all

Please find the solutions to the Quiz1. If your method is different from this and is correct then also you been graded accordingly. 
Tomorrow we'll show you the quiz answer sheets. Please be in the designated classrooms.

**2026-09-11 post:**
Hi, 

For quiz 1 question 3, I have created a small demo to show how the temperature (equilibruim) changes with periodic change in epsilon i.e. emissivity. Imagine you are varying epsilon from 0.8 to 0.4 and again back to 0.8 in a span of 100 MA. How would the temperature vary is shown in the demo video. 
As some of you were trying to visualize that I am sending this to help you understand better.

## Files
- [Solutions_Quiz1.pdf](https://drive.google.com/file/d/1ko3f8YsFwZYQeb454NNRexKxBb8EEFIu/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-solutions-quiz1-1ko3f8.pdf)
- [screen-capture (2).mp4](https://drive.google.com/file/d/1t3s4xIitiogT5ISwfwFzDtcq2L2wVd98/view?usp=drive_web) (video demo)
- [Google Colab demo notebook](https://colab.research.google.com/drive/1P_dUSvg-z-tTk4GH9iuuS_i7AFPu1uFF?usp=sharing)

## Related
- [[introduction-to-climate-science/2026-09-09-study-material-4-pressure-gradient-force]]: formal derivation of horizontal pressure gradient force per unit mass and hydrostatic balance
- [[introduction-to-climate-science/2026-09-03-study-material-3-pressure-and-geopotential]]: scale height formula $H = R_d T / g_0$ and exponential pressure decay
- [[01-climate/cl03-radiation-and-planetary-energy-balance]]: blackbody radiation laws, solar constant $S_0$, and planetary emission temperature $T_e$
- [[01-climate/cl08-greenhouse-models]]: single-layer leaky greenhouse model and surface temperature dependence on emissivity $\epsilon$
- [[01-climate/concepts/hydrostatic-balance]]: hydrostatic equation $\partial p / \partial z = -\rho g$ condition and validity

<!-- kurooto:material34a6e136 -->
## Concepts in Solutions_Quiz1
[[zettel/atmospheric-scale-height]]
<!-- /kurooto:material34a6e136 -->

<!-- kurooto:material84c52cf5 -->
## Concepts in announcement
(none new)
<!-- /kurooto:material84c52cf5 -->
