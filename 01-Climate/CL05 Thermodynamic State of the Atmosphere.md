---
title: CL05 Thermodynamic State of the Atmosphere
aliases: [CL05, Equation of state of air, Ideal gas law for the atmosphere]
subject: climate
type: chapter
chapter: 5
part: II
scope: [taught, extra-book, extra-beyond]
by: [suhas-pre, argha]
status: draft
prereq: ["[[CL04 Feedback and Multiple Steady States]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/suhas-pre, src/argha, status/draft]
---
# CL05 · Thermodynamic State of the Atmosphere

◀ [[CL04 Feedback and Multiple Steady States]] · [[Climate - Course Map|Course Map]] · [[CL06 Hydrostatic Balance and Vertical Structure]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 the state variables and their laws (Argha L3 sl. 30)
> - §2 the ideal gas law in its mass, mole and molecule forms, $R^*$, $k_B$ (Suhas pre-midsem; Argha L5 sl. 51 for $p=\rho k_BT/m$)
> - §3 Dalton's law, mean molar mass, $R_d=287$ J kg⁻¹ K⁻¹ (Suhas pre-midsem)
> - §4 water vapour, $R_v$, $\varepsilon=0.622$, virtual temperature (Suhas pre-midsem)
> - §5 composition of dry air, measures of abundance, well-mixed vs short-lived gases (Suhas pre-midsem; Argha L5 sl. 55)
>
> 🟡 **Extra · book**
> - Wallace & Hobbs Table 1.1, the mean-molecular-weight formula, "water is 0.25 % of the mass" (Ch. 1, p.8)
> - moisture variables: saturation vapour pressure, relative humidity, dew point (W&H §3.5.1) — §6
>
> 🔵 **Extra · beyond**
> - kinetic derivation of $p=nk_BT$, molecular speeds and mean free path (§2)
> - the *exact* form $T_v=T(1+0.608\,q)$ and buoyancy (§4)
> - modern CO₂/CH₄/N₂O values (§5)
> - Bolton's formula and the dew-point example (§6)
> - how ideal is air? (§7)

> [!key] After this chapter you can
> - list the seven fields that describe the atmosphere and say which law closes each,
> - write the ideal gas law as $p=\rho R T$, $pV=nR^*T$ and $p=nk_BT$, and convert between them,
> - **derive** the mean molar mass $M_d=28.97$ g mol⁻¹ and the gas constant $R_d=287$ J kg⁻¹ K⁻¹ of dry air from its composition,
> - use Dalton's law, and **derive virtual temperature** $T_v=T(1+0.608\,q)$ to explain why humid air is *lighter*,
> - convert between mole fraction, mass mixing ratio, specific humidity and vapour pressure, and say why mixing ratios are the right "currency" for tracers.

## 1. What has to be described
<span class="scope-taught">taught</span> *Argha L3, slide 30*

Chapters 3–4 treated the planet as a single number. To go further we need the state of the *gas* itself. Argha's slide 30 lists the basic variables and what fixes each [[climate_intro_L1_L6.pdf#page=30|(slide 30)]]:

| field | symbol | fixed by | note |
|---|---|---|---|
| wind (3 components) | $u,v,w$ | **momentum** conservation (Newton's 2nd law) | CL12–CL14 |
| density | $\rho$ | **mass** conservation (continuity) | |
| humidity | $q$ | **water** conservation (evaporation, condensation) | §4, §6 |
| temperature | $T$ | **energy** conservation (first law) | $c_P\,\partial T/\partial t=$ heat supply | 
| pressure | $p$ | the **ideal gas law** (this chapter) | closes the system |

Seven unknowns $(u,v,w,\rho,q,T,p)$, seven equations (three momentum, one each for mass, water and energy, plus the equation of state). The equation of state is the *closure*: it is what ties the pressure that pushes the air around to the density and temperature that the other laws control. Water is a bit-player by mass (about 0.25 % of the atmosphere, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=25|W&H p.8]]) but carries ~2.5 % of its enthalpy and drives clouds, rain and much of the poleward heat transport, which is why $q$ gets its own equation ([[CL03 Radiation and Planetary Energy Balance]], [[CL10 Global Energy Balance and Meridional Structure]]).

> [!intuition] Seven unknowns need seven equations
> Think of a spreadsheet in which every column is a field. Five of the columns have their own "rule" (a conservation law) that says how they change; the pressure column has *no* rule of its own: it is simply computed, cell by cell, from density and temperature. That "compute pressure from the other two" rule is the ideal gas law. Without it you could not tell how a warmed parcel will push on its neighbours.

## 2. The ideal gas law: three forms of one statement
<span class="scope-taught">taught</span> *Suhas pre-midsem (consolidated notes pp.4–5); Argha L5, slide 51*

For $m$ kg of gas in volume $V$ at pressure $p$ and absolute temperature $T$ ([[suhas notes.pdf#page=4|suhas notes, p.4]]):

$$p=\rho R T,\qquad pV=mRT,\qquad p\alpha=RT\quad(\alpha=1/\rho).\tag{CL5.1}$$

$R$ is the *specific* gas constant of that gas [J kg⁻¹ K⁻¹]. Holding one variable fixed gives the old laws: $T$ fixed ⇒ $pV$ const (**Boyle**); $p$ fixed ⇒ $V\propto T$ (**Charles**); $V$ fixed ⇒ $p\propto T$. See [[Ideal Gas Law]].

> [!intuition] Pressure is a handball court
> Picture $N$ elastic balls flying about a court. Pressure is the *rate at which the walls are hit, times how hard*. Shrink the court (smaller $V$) and the balls hit a given wall more often ⇒ $p\propto1/V$ (Boyle). Make the balls faster (higher $T$) and each hit is harder *and* more frequent, both $\propto v$, so $p\propto v^2\propto T$ (Charles). The Argha slide is exactly this picture: $pV=Nk_BT$ so $p=\rho k_BT/m$ ([[climate_intro_L1_L6.pdf#page=51|slide 51]]).

**Three equivalent forms.** With the mole ($n=m/M$, $N_A=6.022\times10^{23}$ mol⁻¹) and the molecule:

| form | equation | constant | value |
|---|---|---|---|
| per unit **mass** | $p=\rho RT$ | $R=R^*/M$ | gas-specific |
| per **mole** | $pV=nR^*T$ | $R^*$ (universal) | 8.3145 J mol⁻¹ K⁻¹ |
| per **molecule** | $p=n_0k_BT$ | $k_B=R^*/N_A$ | $1.381\times10^{-23}$ J K⁻¹ |

($n_0$ is the number density, molecules per m³; $M$ in kg mol⁻¹.) The molecular form is the most fundamental; multiply by $N_A$ to get moles, by the mass of a molecule to get mass. The link to Argha's slide: $\rho=n_0m$, so $p=n_0k_BT=\rho k_BT/m$ and the specific constant is $R=k_B/m$.

> [!extra-beyond]- 🔵 Extra (beyond): why $p=n_0k_BT$ (kinetic derivation)
> The slides and notes take the gas law as an empirical input. Here is the molecular argument. Take molecules of mass $m$, number density $n_0$, velocities $\mathbf v$. In time $\mathrm dt$ the molecules that hit a wall patch of area $A$ with $v_x>0$ are those in a slab of volume $Av_x\mathrm dt$ (half of them have $v_x>0$). Each rebounds with momentum change $2mv_x$:
> $$p=\frac{F}{A}=\frac{1}{A\,\mathrm dt}\sum 2mv_x=2m\cdot\tfrac12n_0\langle v_x^2\rangle=n_0m\langle v_x^2\rangle=\tfrac13n_0m\langle v^2\rangle.$$
> (isotropy: $\langle v_x^2\rangle=\tfrac13\langle v^2\rangle$.) Temperature is *defined* through the mean kinetic energy per degree of freedom, $\tfrac12m\langle v_x^2\rangle=\tfrac12k_BT$, so $p=n_0k_BT$. ∎
> Numbers for N₂ at 288 K: $m=4.65\times10^{-26}$ kg, rms speed $\sqrt{3k_BT/m}=507$ m s⁻¹ (close to the 340 m s⁻¹ speed of sound, which is a molecular speed), number density $n_0=p/k_BT=2.55\times10^{25}$ m⁻³, mean free path ≈ 65 nm, ~$7\times10^{9}$ collisions per second per molecule.

> [!example] Worked examples
> **(a) Sea-level density.** $p=1013.25$ hPa, $T=288.15$ K, $R_d=287.05$: $\rho=\dfrac{101325}{287.05\times288.15}=\mathbf{1.225}$ kg m⁻³.
> **(b) Density at 5 km** in the standard atmosphere ($p=540.2$ hPa, $T=255.65$ K): $\rho=54020/(287.05\times255.65)=0.736$ kg m⁻³, 60 % of the sea-level value.
> **(c) A litre of air** holds $n_0\times10^{-3}\,\mathrm{m^3}=2.5\times10^{22}$ molecules, i.e. 0.042 mol and 1.2 g.
> **(d) Heating a closed box** from 288 to 300 K at constant $V$ raises $p$ by $300/288-1=4.2\,\%$.

> [!pitfall] Units, always units
> $T$ must be in kelvin, $p$ in pascal (1 hPa = 100 Pa), and *which* $R$? Per kg of dry air ($287$ J kg⁻¹ K⁻¹) is not per mole ($8.31$). A factor 1000 appears when the molar mass is quoted in g mol⁻¹: $R_d=1000R^*/M_d$ with $M_d=28.97$ g mol⁻¹.

## 3. Mixtures of gases: Dalton's law, mean molar mass and $R_d$
<span class="scope-taught">taught</span> *Suhas pre-midsem (pp.5–6)*

Air is a mixture. **Dalton's law**: the total pressure is the sum of the **partial pressures**, each being the pressure that species would exert if it alone filled the volume at the same $T$:

$$p=\sum_ip_i,\qquad p_i=x_ip,\qquad x_i=\frac{n_i}{n}\ \ (\text{mole fraction}).\tag{CL5.2}$$

(Ideal gases do not feel each other, so each obeys $p_i=n_{0,i}k_BT$ independently; $x_i=p_i/p$ follows by dividing.) For moist air $p=p_d+e$, with $e$ the vapour pressure.

> [!intuition] A crowd pushing on a wall
> A mixed crowd of runners pushes on a wall; the total push is the sum of each group's push. A group's push depends only on how many of its members there are and how fast they run, not on who else is in the room. That is why the mole fraction (the *head count*) is the natural weight for partial pressure.

**Mean molar mass.** For a mixture of total mass $m=\sum n_iM_i$ and total moles $n=\sum n_i$ define $\overline M=m/n=\sum x_iM_i$. Then $pV=nR^*T=m\,(R^*/\overline M)\,T$, so the mixture behaves as a single gas with

$$\boxed{R_{\rm mix}=\frac{R^*}{\overline M},\qquad\overline M=\sum_ix_iM_i}\tag{CL5.3}$$

(this is the "apparent molecular weight" $M_d=\sum m_i/\sum(m_i/M_i)$ of the Suhas notes, in the same words as W&H eq. 1.7, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=25|W&H p.8]]).

![[fig_cl05_composition.png|760]]
*Figure CL5.1. (a) Dry air by volume (log scale): three gases make 99.96 %; the infrared-active gases (orange) are all trace amounts. (b) Summing $x_iM_i$ gives $M_d=28.97$ g mol⁻¹. See: nitrogen alone supplies three quarters of the molar mass, and trace gases contribute 0.02 g mol⁻¹ in total.*

> [!example] Worked example: $M_d$ and $R_d$ from the composition
> $M_d=0.7808(28.013)+0.2095(32.000)+0.0093(39.95)+420{\times}10^{-6}(44.01)+\dots=21.87+6.70+0.37+0.02=\mathbf{28.97}$ g mol⁻¹ (script `fig_cl05_composition.py`: 28.966). Then
> $$R_d=\frac{1000\,R^*}{M_d}=\frac{1000\times8.3145}{28.97}=\mathbf{287.0}\ \mathrm{J\,kg^{-1}K^{-1}}.$$
> Partial pressures at 1013.25 hPa: N₂ 791 hPa, O₂ 212 hPa, Ar 9.4 hPa, CO₂ 0.43 hPa. **Mass** fractions differ from mole fractions: N₂ 75.5 %, O₂ 23.1 %, Ar 1.28 % (heavier molecules weigh more per head).

> [!example] Worked example (from the notes): a dry-air/vapour mixture
> At $T=273.2$ K let the partial densities be $\rho_d=1.275$ kg m⁻³ and $\rho_v=4.770\times10^{-3}$ kg m⁻³. Then $p_d=\rho_dR_dT=1.275\times287.0\times273.2=99\,970$ Pa $=999.7$ hPa and $e=\rho_vR_vT=4.77\times10^{-3}\times461.5\times273.2=601$ Pa $=6.01$ hPa. By Dalton $p=999.7+6.0=1005.7$ hPa. (This is also the worked example in W&H p.65–66, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=82|PDF p.82]].)

> [!pitfall] Mole fraction ≠ mass fraction
> "78 % nitrogen" is by **volume** (= by number of molecules = by partial pressure). By mass it is 75.5 %. Mixing up the two is the commonest error in this topic. Rule: *volume/number/pressure fractions go together; mass fractions are weighted by molar mass.*

## 4. Water vapour is light: moist air and virtual temperature
<span class="scope-taught">taught</span> *Suhas pre-midsem (pp.5–6); details also in W&H §3.1.1* · <span class="scope-extra-beyond">extra · beyond</span> *exact q-form and buoyancy*

Water vapour has $M_w=18.016$ g mol⁻¹, lighter than dry air (28.97). Therefore its gas constant is larger,

$$R_v=\frac{1000R^*}{M_w}=461.5\ \mathrm{J\,kg^{-1}K^{-1}},\qquad\varepsilon\equiv\frac{R_d}{R_v}=\frac{M_w}{M_d}=0.622,\qquad e\,\alpha_v=R_vT.\tag{CL5.4}$$

> [!intuition] Swapping bowling balls for tennis balls
> At the same pressure and temperature a gas always contains the **same number of molecules per cubic metre** (Avogadro). Replace a few nitrogen molecules (mass 28) by water molecules (mass 18) and the *number* of molecules is unchanged, but the total *mass* in the volume falls. Humid air is lighter than dry air at the same $p$ and $T$. This is counter-intuitive ("muggy air feels heavy") but it is a fact, and it is why a humid air mass rises more easily.

**Derivation of $T_v$** (following Suhas notes p.6). Take volume $V$ of moist air with $m_d$ of dry air and $m_v$ of vapour. Each fills all of $V$ at the common temperature $T$, with partial densities $\rho_d'=m_d/V$ and $\rho_v'=m_v/V$, so $p-e=\rho_d'R_dT$ and $e=\rho_v'R_vT$, and the density is

$$\rho=\rho_d'+\rho_v'=\frac{p-e}{R_dT}+\frac{e}{R_vT}=\frac{p}{R_dT}\Big[1-\frac ep(1-\varepsilon)\Big].$$

Write this as $p=\rho R_dT_v$ with

$$\boxed{T_v\equiv\frac{T}{1-\dfrac ep(1-\varepsilon)}}\tag{CL5.5}$$

Since $0<\varepsilon<1$: $T_v\ge T$, with equality only for dry air. **$T_v$ is the temperature that dry air would need in order to have the density of the actual moist air at the same pressure**; we keep the constant $R_d$ and absorb the humidity into the temperature. See [[Virtual Temperature]].

> [!derivation]- 🔵 The exact form in terms of specific humidity $q$
> Specific humidity is $q=\rho_v'/\rho$ (mass of vapour per mass of moist air). Using $\rho_v'=e/(R_vT)$ and the density above,
> $$q=\frac{\varepsilon e}{p-(1-\varepsilon)e}\quad\Longleftrightarrow\quad\frac ep=\frac{q}{\varepsilon+(1-\varepsilon)q}.$$
> Substituting in (CL5.5): $1-\dfrac ep(1-\varepsilon)=\dfrac{\varepsilon}{\varepsilon+(1-\varepsilon)q}$, hence
> $$\boxed{T_v=T\Big[1+\frac{1-\varepsilon}{\varepsilon}\,q\Big]=T\,(1+0.608\,q)}\qquad(\text{exact; }(1-\varepsilon)/\varepsilon=0.608).$$
> The moist gas constant is $R_m=R_d(1+0.608\,q)$, which exceeds $R_d$ because the mixture is lighter. Numerical check at 25 °C, RH 60 %, 1000 hPa: $e=19.0$ hPa ⇒ (CL5.5) gives $T_v=300.31$ K, and $q=11.9$ g kg⁻¹ in the $q$-form gives 300.31 K ✓.

![[fig_cl05_virtual_temperature.png|760]]
*Figure CL5.2. (a) Molar masses: water vapour is the lightest of the common molecules, so moist air (28.5 g mol⁻¹ at 4 % vapour) is lighter than dry air. (b) The virtual-temperature excess at 1000 hPa grows steeply with temperature because the saturation vapour pressure does (Clausius–Clapeyron). See: it is negligible in the cold (0.1 K at −20 °C) and 5 K for saturated 30 °C air.*

> [!example] Worked examples
> **(a) Saturated tropical boundary layer** ($T=30$ °C, 1000 hPa): $e_s=42.5$ hPa, $q=26.8$ g kg⁻¹, $T_v-T=0.608\times0.0268\times303.15=\mathbf{4.95}$ K, and the density is lower than that of dry air by 1.6 %.
> **(b) Typical humid day** (25 °C, RH 60 %): $q=11.9$ g kg⁻¹, $T_v-T=2.2$ K.
> **(c) Why it matters:** a parcel with $T_v'$ warmer than its surroundings by 1 K has buoyancy $g\,T_v'/T_v\approx9.81/300=0.033$ m s⁻². A 3 K virtual-temperature excess is as buoyant as a 3 K *real* excess, even if the thermometer reads the same. Convection and static stability must therefore use $T_v$, not $T$ ([[Atmospheric Stability]], [[Convection]], [[CL09 Radiative-Convective Equilibrium]]).

> [!pitfall] $T_v$ is a bookkeeping device, not a thermometer reading
> A thermometer measures $T$. $T_v$ is *computed* so that we can keep using the dry-air constant. In the same spirit, clouds add the weight of liquid water, which can be included in a "density temperature". When a question says "temperature" and humidity is not mentioned, use $T$; when it asks about *density* or *buoyancy*, think $T_v$.

## 5. What the air is made of, and how to count it
<span class="scope-taught">taught</span> *Suhas pre-midsem (p.7); Argha L5, slide 55* · <span class="scope-extra-book">extra · book</span> *W&H Table 1.1 values and molecular weights*

Dry air is 78.08 % N₂, 20.95 % O₂ and 0.93 % Ar by volume; everything else is a trace ([[Atmospheric Composition]], Fig. CL5.1). W&H Table 1.1 ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=25|p.8]]) gives the molecular weights and fractions used above. Water vapour is listed separately because it varies by more than three orders of magnitude (from ~10 ppmv in the coldest air to ~5 % in hot, humid air), which is why abundances are customarily quoted *relative to dry air*.

> [!extra-beyond]+ 🔵 Extra (beyond): updated values
> The 2006 textbook table gives CO₂ = 380 ppm. At the time of writing (NOAA Global Monitoring Laboratory, annual means ≈ 2023, `[verify]` the exact numbers): CO₂ ≈ 420 ppm, CH₄ ≈ 1.9 ppm, N₂O ≈ 0.34 ppm. These grow every year, N₂ and O₂ do not.

**Measures of abundance.** Let subscript $d$ denote the dry air in the same parcel.

| measure | definition | conserved when the parcel expands? |
|---|---|---|
| mole fraction $x_i=n_i/n$ ("ppmv") | = $p_i/p$ = $V_i/V$ | yes (for the dry mixture) |
| **mass mixing ratio** $r_i=m_i/m_d$ | mass of $i$ per mass of dry air | **yes** |
| number density $n_{0,i}$, concentration $\rho_i$ | per unit volume | **no** (changes when the volume does) |
| specific humidity $q=m_v/(m_d+m_v)$; mixing ratio $w=m_v/m_d$ | water vapour only | yes (until condensation) |

Conversion between mole fraction and mass mixing ratio: $x_i=\dfrac{n_i}{n_d}=\dfrac{m_i/M_i}{m_d/M_d}=r_i\,\dfrac{M_d}{M_i}$, i.e. $r_i=x_i\,M_i/M_d$.

> [!intuition] Why mixing ratio and not concentration? The sugar in the coffee
> If you pour half a cup of sweet coffee into a bigger mug, the *concentration of sugar per cm³* is unchanged in the cup but changes if the coffee is stretched into a different volume. The **grams of sugar per gram of coffee** is unchanged by pouring. A rising air parcel expands (its density falls), so its CO₂ *concentration* falls even though nothing happened to the CO₂. The mixing ratio $r_i=m_i/m_d$ counts the dry-air mass that travels with the parcel, so it changes only through real sources, sinks or mixing. A quantity that a parcel keeps is a **conserved tracer**: that is why mixing ratios are the currency of atmospheric chemistry.

> [!example] Worked example: a unit conversion
> CO₂ at 420 ppmv: $r=420\times10^{-6}\times\dfrac{44.01}{28.965}=638\times10^{-6}$ kg/kg, i.e. **638 ppm by mass**. Doubling CO₂ changes $M_d$ by only $420{\times}10^{-6}(44.01-28.97)=0.006$ g mol⁻¹ (0.02 %): $R_d$ is unaffected for all practical purposes.

**Well-mixed or not?** Argha's slide 55 [[climate_intro_L1_L6.pdf#page=55|(slide 55)]]: *long-lived* gases are well mixed, *short-lived* ones sit near their sources. The reason is a race between two time scales: winds stir the troposphere in about a year (a few weeks within a hemisphere), whereas chemistry removes each gas in its own lifetime $\tau_{\rm chem}$. If $\tau_{\rm chem}\gg$ the mixing time (N₂, O₂, Ar, CO₂, CH₄), the gas is spread evenly, its mixing ratio is nearly constant with height up to ~100 km (the *turbopause*, see [[CL06 Hydrostatic Balance and Vertical Structure]]). If $\tau_{\rm chem}\ll$ the mixing time (water vapour, which rains out in about 9 days; ozone near the ground; NO₂), the gas is concentrated where it is produced.

> [!intuition] Perfume in a room
> Spray perfume in one corner. If it lingers for hours it ends up everywhere (well mixed); if it decomposes within seconds you smell it only near the spray. Gases are the same, with "seconds vs hours" replaced by "chemical lifetime vs the year it takes the winds to stir the troposphere". (The slide carries a note to itself, "N₂O & NO₂ to be flipped", presumably two entries to be swapped in its figure: N₂O is the long-lived gas, with a lifetime of ~100 years, NO₂ the short-lived one, lifetime of hours to days. `[verify]` which entries were meant.)

> [!connection] Radiative importance is *anti*-correlated with abundance
> The three gases that make up 99.96 % of the air do nothing to infrared radiation; the greenhouse gases are 0.04 % of the air. Diatomic molecules (N₂, O₂) have one vibrational mode, which does not change the molecule's electric dipole, so they neither absorb nor emit in the thermal infrared; triatomic and polar molecules (H₂O, CO₂, O₃, N₂O) have bending modes that do change the dipole, so a few hundred ppm are enough to matter. This is previewed in [[CL07 Optical Properties of the Atmosphere]] and used in [[CL08 Greenhouse Models]] and the [[Greenhouse Effect]]. The underlying selection rules are quantum-mechanical and symmetry-based: [[Quantum Mechanics - Course Map]], [[Group Theory - Course Map]].

## 6. Moisture variables
<span class="scope-extra-book">extra · book</span> *W&H §3.5.1 (PDF p.97)* · <span class="scope-extra-beyond">extra · beyond</span> *Bolton's formula, dew-point example*

Water is the one species that changes phase in the atmosphere, so it has several measures ([[Mixing Ratio and Humidity]]):

- **vapour pressure** $e$ (partial pressure of vapour) and **saturation vapour pressure** $e_s(T)$ (the largest $e$ that can exist in equilibrium with liquid water),
- **mixing ratio** $w=\dfrac{m_v}{m_d}=\dfrac{\varepsilon e}{p-e}$ and **specific humidity** $q=\dfrac{w}{1+w}$ (almost equal: they differ by $w\sim0.01$),
- **relative humidity** $\mathrm{RH}=e/e_s\approx w/w_s$,
- **dew point** $T_d$: the temperature at which $e_s(T_d)=e$.

$e_s$ rises about **7 % per kelvin**, a consequence of the Clausius–Clapeyron relation ([[Clausius-Clapeyron Relation]]); an empirical fit (Bolton 1980) is $e_s(T)=6.112\exp\!\big[17.67\,T_c/(T_c+243.5)\big]$ hPa with $T_c$ in °C.

| $T$ (°C) | −20 | 0 | 10 | 20 | 30 |
|---|---|---|---|---|---|
| $e_s$ (hPa) | 1.26 | 6.11 | 12.27 | 23.37 | 42.46 |
| $q_s$ at 1000 hPa (g kg⁻¹) | 0.8 | 3.8 | 7.7 | 14.7 | 26.8 |

> [!example] Worked example: dew point
> Air at 25 °C, 1000 hPa, RH 60 %: $e=0.6\times31.67=19.0$ hPa; $w=0.622\times19.0/(1000-19.0)=12.0$ g kg⁻¹; $q=11.9$ g kg⁻¹. Dew point: invert Bolton: $T_d=243.5\ln(e/6.112)/[17.67-\ln(e/6.112)]=16.7$ °C. Cool the air to 16.7 °C and it is saturated: dew or cloud forms. (Indian monsoon air with dew point ≥ 24 °C holds ≥ 19 g kg⁻¹.)

> [!intuition] Air as a sponge that gets bigger when warm
> A cold sponge holds little water, a warm one much more: $e_s$ roughly doubles every 10 K. RH is "how full the sponge is". Cooling air with fixed water content fills the sponge (RH rises) until 100 %, then it must wring out the excess: clouds. This is the engine of every latent-heat process in the next chapters.

## 7. How ideal is air?
<span class="scope-extra-beyond">extra · beyond</span> *standard kinetic-theory estimate*

The ideal gas law assumes point molecules that do not attract each other. Two checks. (1) *Volume of the molecules*: with diameter ≈ 0.37 nm and $n_0=2.5\times10^{25}$ m⁻³ the fraction of space occupied by the molecules themselves is $n_0\tfrac\pi6d^3\approx7\times10^{-4}$ (0.07 %). (2) *Mean separation* ($n_0^{-1/3}\approx3.4$ nm, about 9 molecular diameters) is large compared with the range of the intermolecular force. Deviations from ideality are therefore of order 0.1 % at sea level and smaller aloft: an excellent approximation for everything in this course. It would fail for water vapour near saturation at very high pressure, in clouds' liquid phase, or on Venus's surface (92 bar).

## 8. Looking ahead
<span class="scope-taught">taught</span> *synthesis*

We now have $p=\rho R_dT_v$: pressure, density and (virtual) temperature are tied together. To find *how each varies with height* we need one more principle, the balance between gravity and the vertical pressure force: **hydrostatic balance**, the subject of [[CL06 Hydrostatic Balance and Vertical Structure]]. Combined with the gas law it gives the exponential fall-off of pressure with a scale height of about 8 km. After that, [[CL07 Optical Properties of the Atmosphere]] returns to radiation with the composition we have just established.

## Map of this chapter
> [!connection] How CL05 connects
> **Builds on:** [[CL03 Radiation and Planetary Energy Balance]] (state variables, energy budget) · [[CL04 Feedback and Multiple Steady States]] (water-vapour feedback needs $e_s(T)$)
> **Leads to:** [[CL06 Hydrostatic Balance and Vertical Structure]] (gas law + gravity) · [[CL07 Optical Properties of the Atmosphere]] (absorbers from the composition) · [[CL09 Radiative-Convective Equilibrium]] ($T_v$ and moist convection) · [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (density in the pressure-gradient force)
> **Concepts:** [[Ideal Gas Law]] · [[Atmospheric Composition]] · [[Virtual Temperature]] · [[Mixing Ratio and Humidity]] · [[Clausius-Clapeyron Relation]] · [[Hydrostatic Balance]] · [[Standard Atmosphere]] · [[Atmospheric Stability]] · [[Convection]]
> **Other subjects:** [[Thermodynamics and Statistical Mechanics - Course Map]] (kinetic theory, equations of state) · [[Quantum Mechanics - Course Map]] and [[Group Theory - Course Map]] (why triatomics absorb) · [[Probability - Course Map]] (the Maxwell–Boltzmann speed distribution behind the kinetic derivation)

> [!connection] Statistical mechanics
> The kinetic derivation of $p=n_0k_BT$ is the simplest piece of statistical mechanics: macroscopic $p$ and $T$ as averages over a huge number of molecules. The distribution of molecular speeds (Maxwell–Boltzmann) and the equipartition theorem belong to [[Thermodynamics and Statistical Mechanics - Course Map]] and [[Probability - Course Map]].

## Summary
> [!summary] Cheat-sheet
> - Seven fields $(u,v,w,\rho,q,T,p)$; the ideal gas law closes the system.
> - $p=\rho RT=n_0k_BT$, $pV=nR^*T$; $R^*=8.3145$, $k_B=1.381\times10^{-23}$, $R=R^*/M$.
> - Dalton: $p=\sum p_i$, $p_i=x_ip$. Mean molar mass $\overline M=\sum x_iM_i$. **$M_d=28.97$ g mol⁻¹, $R_d=287.0$ J kg⁻¹ K⁻¹**; $R_v=461.5$; $\varepsilon=M_w/M_d=0.622$.
> - **Humid air is lighter.** $T_v=T/[1-(e/p)(1-\varepsilon)]=T(1+0.608\,q)$; $T_v-T\approx5$ K for saturated 30 °C air, ≈ 0.1 K at −20 °C.
> - Composition (by volume): N₂ 78.08 %, O₂ 20.95 %, Ar 0.93 %; CO₂ ≈ 420 ppm. Mole fraction $x_i=r_iM_d/M_i$; mixing ratios (not concentrations) are conserved for a parcel.
> - $e_s$ rises ~7 % K⁻¹; $w=\varepsilon e/(p-e)$; $q=w/(1+w)$; RH $=e/e_s$.

## Practice
1. **Density at altitude.** Find $\rho$ at 5 km if $p=540$ hPa and $T=255.7$ K. Compare with sea level.
2. **$R_d$.** Show from the composition that $R_d=287$ J kg⁻¹ K⁻¹ and compute the mass fractions of N₂, O₂ and Ar.
3. **Everest.** The summit pressure is ≈ 315 hPa. What is the partial pressure of O₂ and what fraction of the sea-level value is it?
4. **$T_v$.** Tropical air with $T=300$ K and $q=18$ g kg⁻¹ at 1000 hPa: find $T_v$, the density, and the density of dry air at the same $T$.
5. **Derive** $T_v=T(1+0.608\,q)$ from (CL5.5).
6. **Mixing ratio.** Show $q=w/(1+w)$ and $w=\varepsilon e/(p-e)$.
7. **Number density.** Molecules per m³ at 288 K and 1013 hPa, and at 10 km ($p=264$ hPa, $T=223$ K).
8. **Conversions.** A trace gas has $x=2$ ppbv and $M=48$ g mol⁻¹ (ozone). Its mass mixing ratio?
9. **Conceptual.** Why is a cloudy air parcel *heavier* than its water-vapour content alone suggests, even though vapour makes air lighter?
10. **Conceptual.** Why does the CO₂ *concentration* (molecules per m³) fall with height while its *mixing ratio* is constant?

> [!example]- Solutions
> 1. $\rho=54000/(287.05\times255.7)=0.736$ kg m⁻³ = 60 % of 1.225.
> 2. $\sum x_iM_i=28.97$ ⇒ $R_d=8314.5/28.97=287.0$. Mass fractions $x_iM_i/M_d$: N₂ 75.5 %, O₂ 23.1 %, Ar 1.28 %.
> 3. $p_{O_2}=0.2095\times315=66$ hPa, 31 % of the sea-level 212 hPa (the *fraction* of oxygen is unchanged, the pressure is not).
> 4. $T_v=300(1+0.608\times0.018)=303.3$ K; $\rho=10^5/(287.05\times303.3)=1.149$ kg m⁻³; dry air at 300 K: 1.161. Humid air is 1.1 % lighter.
> 5. See the derivation box: $e/p=q/[\varepsilon+(1-\varepsilon)q]$ ⇒ $1-(e/p)(1-\varepsilon)=\varepsilon/[\varepsilon+(1-\varepsilon)q]$ ⇒ $T_v=T[1+q(1-\varepsilon)/\varepsilon]$.
> 6. $w=m_v/m_d=\rho_v/\rho_d=(e/R_vT)/((p-e)/R_dT)=\varepsilon e/(p-e)$; $q=m_v/(m_d+m_v)=w/(1+w)$.
> 7. $n_0=p/k_BT$: sea level $1.013\times10^5/(1.381\times10^{-23}\times288)=2.55\times10^{25}$ m⁻³; 10 km: $2.64\times10^4/(1.381\times10^{-23}\times223)=8.6\times10^{24}$ m⁻³.
> 8. $r=x\,M/M_d=2\times10^{-9}\times48/28.97=3.3\times10^{-9}$, i.e. 3.3 ppbm.
> 9. Liquid droplets add mass without adding to the gas-phase pressure: the "density temperature" includes liquid-water loading, $T_\rho=T_v(1-q_l)$ roughly, so the droplets *reduce* buoyancy. A cloud is lighter than dry air only if the vapour effect wins; in the thick, droplet-laden part of a cumulonimbus the loading is what produces downdrafts.
> 10. A rising parcel expands, so its total density $\rho$ falls, and the number of CO₂ molecules per m³ falls in proportion. The ratio CO₂/dry air (mixing ratio) is unchanged because both the CO₂ and the dry air thin together.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | state variables and their laws, water 0.25 % mass / 2.5 % enthalpy | [[climate_intro_L1_L6.pdf#page=30\|Argha L3 sl. 30]]; W&H p.8 | taught (+ book) |
> | ideal gas law, moles, $R^*$, $k_B$, special cases | [[suhas notes.pdf#page=4\|Suhas notes pp.4–5]] | taught |
> | $p=\rho k_BT/m$ (kinetic form) | [[climate_intro_L1_L6.pdf#page=51\|Argha L5 sl. 51]] | taught |
> | Dalton, mean molar mass, $R_d$, worked vapour example | [[suhas notes.pdf#page=5\|Suhas notes pp.5–6]]; W&H §3.1 | taught |
> | $R_v$, $\varepsilon$, virtual temperature | [[suhas notes.pdf#page=6\|Suhas notes p.6]]; W&H §3.1.1 | taught |
> | composition and abundance measures, tracers | [[suhas notes.pdf#page=7\|Suhas notes p.7]] | taught |
> | well-mixed vs short-lived gases | [[climate_intro_L1_L6.pdf#page=55\|Argha L5 sl. 55]] | taught |
> | Table 1.1, mean-molecular-weight formula (1.7), mass of the atmosphere | W&H Ch. 1, p.8 (PDF 25) | extra/book |
> | moisture variables | W&H §3.5.1 (PDF 97) | extra/book |
> | kinetic derivation, molecular numbers, exact $T_v(q)$, buoyancy, dew-point example, modern abundances, non-ideality | derived here; NOAA GML (approx.) | extra/beyond |
>
> **Dropped as redundant:** Argha L3 slide 30's list of state variables and Suhas's introduction of the same quantities are merged in §1; Argha L5's kinetic $p=\rho k_BT/m$ and Suhas's three forms of the gas law are merged in §2; the composition slides (Argha L5 sl. 55) and Suhas's composition table are merged in §5.
>
> **Notes:** `suhas notes.pdf` is an AI-consolidated secondary source; every formula and number above was recomputed. Its worked examples are taken from W&H Ch. 3 (e.g., the 273 K dry-air/vapour mixture, W&H p.65–66).

**References.** Wallace & Hobbs (2006) *Atmospheric Science*, §1.3.3, §3.1, §3.5.1 · Bolton, D. (1980) *Mon. Weather Rev.* 108, 1046 · NOAA Global Monitoring Laboratory, annual mean greenhouse-gas indices (approximate values quoted).
