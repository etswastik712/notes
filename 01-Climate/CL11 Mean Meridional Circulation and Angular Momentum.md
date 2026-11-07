---
title: CL11 Mean Meridional Circulation and Angular Momentum
aliases: [CL11, Hadley circulation chapter, Tropical overturning circulation]
subject: climate
type: chapter
chapter: 11
part: IV
scope: [taught, extra-book, extra-beyond]
by: [suhas-post]
status: draft
prereq: ["[[CL10 Global Energy Balance and Meridional Structure]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/suhas-post, src/own-notes, status/draft]
---
# CL11 · Mean Meridional Circulation and Angular Momentum

◀ [[CL10 Global Energy Balance and Meridional Structure]] · [[Climate - Course Map|Course Map]] · [[CL12 Rotating Frames and the Coriolis Force]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 the single-cell picture and why energetics allows it
> - §2 the mass stream function (definition, meaning, sign)
> - §3 the observed three-cell circulation, seasons, ITCZ, climate impacts
> - §4 why one cell cannot reach the pole: absolute angular momentum, the ring of air, the subtropical jet, the trades
> - §5 the angular-momentum budget and surface friction
> - §6 anatomy of the Hadley cell
> - §7 eddies and the mid-latitudes (overview)
>
> 🟡 **Extra · book** (M&P Ch. 5, 8; Hartmann Ch. 6)
> - magnitudes and units of Fig. 5.21
> - the numerical values 14 / 58 / 130 m s⁻¹ of Eq. 8-2
> - footnote: cell width depends on rotation rate
> - footnote: length-of-day changes (1 ms, 0.1 ms)
> - Hartmann Fig. 6.17 (angular-momentum cycle with eddy transport)
> - Hartmann §6.5.2 (why deserts occur)
> - GFD Lab VIII (rotating annulus)
> - naming of Ferrel, trade-wind etymology
>
> 🔵 **Extra · beyond**
> - derivation of ψ and its properties
> - numbers for the thickness argument
> - absolute vorticity as $-\partial A/\partial\varphi$ and $\mathrm{Ro}=1$
> - why sinking air dries (numbers)
> - the atmosphere's angular momentum and the length-of-day estimate
> - the Ferrel cell as an eddy artefact
> - **the Held–Hou model of the Hadley-cell edge**
>
> **Quiz note.** [[climate_book_notes.pdf#page=1|climate_book_notes.pdf]] scopes the quiz to the *assigned excerpts* (Marshall & Plumb Ch. 4.7, 5, 6.6, 8; Hartmann 2.8–2.9). So 🟡 items taken from those excerpts are "read for the quiz" even though they were not shown in class; 🔵 items are not examinable.

> [!key] After this chapter you can
> - explain why a temperature contrast produces poleward flow aloft, and why that gives a **single-cell hypothesis** for the tropics,
> - define the **mass stream function** $\psi$, read a $\psi$ contour plot (direction, strength, ascent and descent) and say what $\psi=0$ at the ground means,
> - describe the observed **Hadley, Ferrel and Polar cells**, their seasonal behaviour, the ITCZ and the desert belts,
> - **derive** $A=\Omega a^2\cos^2\varphi+ua\cos\varphi$ and the ring-of-air wind $u=\Omega a\sin^2\varphi/\cos\varphi$, and use them to show that no cell can extend from equator to pole,
> - explain the **subtropical jet**, the **trade winds** and the surface westerlies from angular momentum, and describe the **angular-momentum budget** of the whole atmosphere.

## 1. A temperature contrast calls for a circulation
<span class="scope-taught">taught</span> *Suhas 7 Oct p20, 8 Oct p4–6 and p13–14, 14 Oct p1; handwritten notes p.3*

[[CL10 Global Energy Balance and Meridional Structure|Chapter 10]] showed that the tropics absorb more sunlight than they emit and the poles the opposite, so *something* must carry energy poleward. The slide's first guess ([[8th Oct.pdf#page=4|8 Oct, p4]]): **a single meridional circulation** from the tropics to the poles. Its upper branch carries warm air poleward and its lower branch returns cold air equatorward, which cools the tropics and warms the poles ([[8th Oct.pdf#page=5|p5]]).

![[8th Oct.pdf#page=5&height=330]]
*8 Oct, p5: the single-cell picture. W/E mark the zonal winds this circulation would produce on a rotating Earth (we test this in §4).*

> [!intuition] The room-heater picture
> A radiator in a cold room: warm air rises along the heater, spreads out under the ceiling, sinks at the far cold wall and creeps back along the floor. The tropics are the radiator, the poles the cold wall, the tropopause the ceiling. If the Earth did not rotate, this is exactly what we would see: **one cell in each hemisphere, thermally direct** (warm air rises, cold air sinks).

**Does energetics allow it?** The slide answers yes ([[8th Oct.pdf#page=14|p13–14]]): "because tropical regions are much warmer than polar regions, the **thickness** of the air column between any two pressure levels is greater in the tropics. This creates a height gradient on constant-pressure surfaces that can drive an upper-level meridional circulation from the equator toward the poles."

> [!derivation]- Why warm columns are thick (hypsometric equation)
> Hydrostatic balance $\mathrm dp=-\rho g\,\mathrm dz$ and the ideal gas law $p=\rho R_dT$ ([[Ideal Gas Law]]) give $\mathrm dz=-\dfrac{R_dT}{g}\,\dfrac{\mathrm dp}{p}$. Integrating between two pressure levels,
> $$z_2-z_1=\frac{R_d\bar T}{g}\ln\frac{p_1}{p_2},$$
> where $\bar T$ is the layer-mean temperature (see [[CL06 Hydrostatic Balance and Vertical Structure]]). The same pressure drop needs a *taller* layer when the air is warmer, because warm air is less dense.

> [!intuition] Stacks of pancakes
> A pressure level is a particular weight of air above you. A stack with a fixed weight is **taller if the pancakes are fluffy (warm) and shorter if they are dense (cold)**. At the same ground pressure, the 500 hPa surface therefore sits higher over the tropics than over the poles: the upper-level pressure surfaces slope *down toward the pole*, and air starts to slide downhill, i.e. poleward.

> [!extra-beyond]- 🔵 Extra (beyond): the numbers
> For the 1000–500 hPa layer, $T=300$ K gives $z_2-z_1=6.09$ km and $T=250$ K gives 5.07 km: **about 1 km higher** over the tropics. Spread over an equator-to-pole distance of $10^4$ km, and ignoring rotation, the poleward pressure-gradient force on a unit mass aloft is $g\,\Delta z/\Delta y\approx10^{-3}$ m s⁻². An unbalanced force of that size would accelerate air to 10 m s⁻¹ in about three hours, so the response is fast: the real question is what *balances* the force, which is the subject of [[CL12 Rotating Frames and the Coriolis Force|the next two chapters]].

So energetics *allows* a single cell. The slide then asks "how do we verify the hypothesis?" ([[8th Oct.pdf#page=6|p6]]) and, on 14 Oct, adds the test: *does the hypothesised motion follow the principle of angular-momentum conservation?* ([[14th Oct.pdf#page=1|14 Oct, p1]]). The plan of this chapter: first describe what the atmosphere actually does (§2–3), then run the angular-momentum test (§4).

## 2. Measuring a circulation: the mass stream function
<span class="scope-taught">taught</span> *Suhas 7 Oct p20, 8 Oct p7–8; handwritten notes p.3 (χ and its winds)*

Averaged around a latitude circle, the 3-D wind becomes a 2-D flow in the latitude–height plane: $([v],[\omega])$, with $\omega=\mathrm Dp/\mathrm Dt$ the vertical velocity in pressure coordinates. Two numbers per point is awkward. The **mass stream function** packs both into one scalar ([[8th Oct.pdf#page=8|8 Oct, p8]]):

$$\boxed{\psi(\varphi,p)=\frac{2\pi a\cos\varphi}{g}\int_0^{p}[v]\,\mathrm dp'}\qquad[\mathrm{kg\,s^{-1}}]\tag{CL11.1}$$

$a$ is the Earth's radius, $g$ gravity, $[v]$ the zonal-mean northward wind. The slide says it "captures the **northward mass flux above a particular pressure $p$**" ([[8th Oct.pdf#page=7|p7]]). See [[Mass Stream Function]].

> [!intuition] A contour map of the flow
> $\psi$ works like the **contour lines on a map of a hill**, except that air moves *along* the contours instead of up them. Where contours bunch together, the flow is fast (like a river narrowing); a closed set of contours is a circulation cell; the number on a contour is how much mass is carried **between that contour and the top (equivalently the ground)**. The *difference* between two contours is the mass flux in the channel between them.

**Building $\psi$ by hand.** Take one latitude, 15° N, and an idealised profile of $[v]$: poleward aloft, equatorward below, and **no net mass flux** (otherwise the latitude circle would pile up air). Then (CL11.1) is just a running total from the top down.

![[fig_cl11_streamfunction_build.png|780]]
*Figure CL11.1. (a) An illustrative $[v](p)=V\cos(\pi p/p_s)$ with $V=1.5$ m s⁻¹. (b) Its running total $\psi(p)$: zero at the top (nothing above), zero at the ground (the total over the whole column is zero), and maximal at 500 hPa where $[v]$ changes sign. Illustrative profile, not data; script `fig_cl11_streamfunction_build.py`.*

> [!example] Worked example: mass flux of the upper branch
> At 15° N, $2\pi a\cos\varphi/g=3.94\times10^{6}$ kg m⁻¹ s⁻¹ per m s⁻¹ per Pa⁻¹... precisely: $2\pi(6.371\times10^6)\cos15^\circ/9.81=3.94\times10^{6}$ (units m s² kg⁻¹... i.e. kg per pascal-metre). A poleward wind of 2 m s⁻¹ through 200 hPa ($=2\times10^4$ Pa) carries
> $$\psi=3.94\times10^6\times2\times2\times10^4=1.58\times10^{11}\ \mathrm{kg\,s^{-1}}=158\times10^9\ \mathrm{kg\,s^{-1}}.$$
> The same mass must come back equatorward below. If the return flow occupies the lowest 100 hPa it needs 4 m s⁻¹; spread over 700 hPa it needs only **0.6 m s⁻¹**. That is why the return flow is "weaker" but thick (§3.3). For comparison the Hadley cells in Marshall & Plumb's Fig. 5.21 peak at order $10^2\times10^9$ kg s⁻¹ (colour bar to ±200).

**Sign convention.** Positive $\psi$ = northward flux above, southward below = a **clockwise** loop when latitude increases to the right. So the Northern-Hemisphere Hadley cell has $\psi>0$, the Southern one $\psi<0$ (Marshall & Plumb: "flow circulates around positive (negative) centres in a clockwise (anticlockwise) sense").

> [!extra-beyond]- 🔵 Extra (beyond): why this works (continuity)
> Zonal-mean mass continuity in pressure coordinates is $\dfrac{1}{a\cos\varphi}\dfrac{\partial([v]\cos\varphi)}{\partial\varphi}+\dfrac{\partial[\omega]}{\partial p}=0$. Because of it, defining $[v]=\dfrac{g}{2\pi a\cos\varphi}\dfrac{\partial\psi}{\partial p}$ and $[\omega]=-\dfrac{g}{2\pi a^2\cos\varphi}\dfrac{\partial\psi}{\partial\varphi}$ satisfies continuity identically (the mixed second derivatives cancel). Then $\mathrm D\psi/\mathrm Dt=[v]\partial_\varphi\psi/a+[\omega]\partial_p\psi=0$: **a parcel keeps its value of $\psi$**, i.e. it moves along a contour. Ascent ($[\omega]<0$) sits where $\psi$ increases poleward; descent where it decreases poleward. Marshall & Plumb's $\chi$ is the height-coordinate version, $v=-(\rho a\cos\varphi)^{-1}\partial\chi/\partial z$, $w=(\rho a^2\cos\varphi)^{-1}\partial\chi/\partial\varphi$, plotted in units of $10^9$ kg s⁻¹ (Sverdrups, §11.5.2).

> [!pitfall] Common slips
> - $\psi$ is a **mass flux** (kg s⁻¹), not a velocity and not a mass.
> - $\psi$ is a *zonal* mean: it hides the eddies, which dominate mid-latitudes (§7).
> - $\psi=0$ at the ground does **not** mean no flow there: it means the *net* northward flux of the column is zero, with northward and southward parts cancelling.

## 3. What the atmosphere actually does
<span class="scope-taught">taught</span> *Suhas 8 Oct p9–12, 14 Oct p2–3; handwritten notes p.2 (M&P §5.4)*

### 3.1 Three cells per hemisphere
Instead of one cell, the observed overturning has **three per hemisphere** ([[8th Oct.pdf#page=9|8 Oct, p9–12]]):

![[8th Oct.pdf#page=9&height=360]]
*8 Oct, p9: observed mean meridional circulation, DJF (top), JJA, annual mean (bottom).*

| cell | latitudes | rising | sinking | surface wind | thermal character |
|---|---|---|---|---|---|
| **Hadley** | 0–30° | near the equator ([[Intertropical Convergence Zone]]) | subtropics ~30° | trades, easterly ([[Trade Winds and Westerlies]]) | **thermally direct** |
| **Ferrel** | 30–60° | ~60° | ~30° | westerlies | **thermally indirect** |
| **Polar** | 60–90° | ~60° | pole | polar easterlies | thermally direct (weak) |

See [[Hadley Cell]] and [[Ferrel Cell and Polar Cell]]. "Thermally direct" means the sense of the circulation is warm air rising and cold air sinking; "indirect" is the reverse.

![[fig_cl11_three_cells.png|840]]
*Figure CL11.2. A **schematic** three-cell structure built from a simple analytic $\psi$ (relative strengths only, not a fit to data; script `fig_cl11_three_cells.py`). Streamlines follow from $\psi$ via the formulas of §2. Blue = clockwise, red = anticlockwise. Compare 8 Oct p9 and Marshall & Plumb Fig. 5.21.*

> [!intuition] Engines and refrigerators
> A **direct** cell is a heat engine: it turns the heat contrast into the kinetic energy of the wind (like a convection cell in a pot). An **indirect** cell has the opposite sign: it moves air against the buoyancy, like a refrigerator, and needs a motor. The motor is the **mid-latitude eddies** (§7). So the Ferrel cell is not "driven by the tropics' heat" the way the Hadley cell is.

### 3.2 It follows the Sun
In **DJF** air rises just *south* of the equator and sinks at ~30° N; in **JJA** it rises just north and sinks at ~30° S. The ascent is on the **summer side**, where the warm surface triggers convection; the descent is strong on the winter side. The annual mean therefore shows two weaker, roughly symmetric cells, with ascent a little north of the equator (caption of M&P Fig. 5.21).

> [!intuition] A see-saw that tilts with the Sun
> The Hadley circulation is not two fixed cells but one big overturning that **leans toward the summer hemisphere**: in winter the winter-hemisphere cell grows, crosses the equator, and dominates, with the strongest jet at its edge. The two cells you see in the annual mean are the *average* of this see-saw.

> [!pitfall] Quiz trap: "Hadley ascent is at the equator"
> The ascent follows the **summer hemisphere**; at the equator only in the annual mean (roughly) and at the equinoxes.

### 3.3 Winds that go with it
Zonal-mean meridional winds are weak, $<1$ m s⁻¹, **except in the tropics**: in the upper troposphere (≈200 hPa, 20° N–20° S) they blow toward the winter hemisphere at up to ~3 m s⁻¹; the **return flow** in the lower troposphere is weaker and directed mostly toward the summer hemisphere (handwritten notes p.2; M&P p.77). Weaker because it is spread over a deeper layer (worked example in §2). Vertical motion is much smaller than horizontal ($w\ll u,v$, a consequence of the thinness of the atmosphere), so it is *inferred* rather than measured, which is exactly why $\psi$ is computed from $[v]$.

> [!extra-book]+ 🟡 Extra (book): magnitudes and units
> In M&P Fig. 5.21 the overturning is drawn in units of $10^9$ kg s⁻¹ (Sverdrups); the solstice Hadley cells reach about 100–200 on that scale. The first part of the excerpt (p.74) describes Hadley's picture of *rings* of air that sink and "expand outward" at low levels, producing the near-equatorial easterlies: "as attractive as this simple circulation may seem, ... it is not in accord with observations."

### 3.4 Where it rains and where it does not
Mean **ascent** coincides with the wet tropics (cold cloud tops in the outgoing longwave radiation); **descent** is dry and cloud-free: the **desert belt** and the **trade inversion** ([[CL09 Radiative-Convective Equilibrium]] gives the cloud-top picture). The slide "Impact of Hadley circulation on the climate" ([[14th Oct.pdf#page=2|14 Oct, p2]]) maps hot arid and semi-arid climates (Sonoran, Sahara, Rub' al Khali, Namib, Kalahari, Great Australian...) on the ~30° belts, with rising warm moist air at the equator and descending cold dry air near the poles.

![[14th Oct.pdf#page=2&height=330]]
*14 Oct, p2. The ITCZ is introduced on p3 as the signature of "tropics defined by the dynamics of air".*

> [!intuition] Why sinking air is dry (the bicycle pump)
> Pump a bicycle tyre and the pump heats up: compressing air warms it. Sinking air is compressed by the increasing pressure, so it **warms** and its relative humidity **drops**; any cloud evaporates. In addition, the air aloft has already lost most of its water as rain in the ITCZ. Together: warm, dry, clear.

> [!extra-beyond]- 🔵 Extra (beyond): a number
> Dry-adiabatic compression (Poisson's law, $T\propto p^{0.286}$): air at 255 K and 500 hPa sinking to 900 hPa arrives at $255\times(900/500)^{0.286}=302$ K (29 °C). Radiative cooling on the way down lowers this, but the sign and size of the warming explain why the descent zones are hot and dry.

> [!pitfall] Not every desert belongs to the Hadley cell
> The map also shows the Takla Makan and Gobi, which lie far from the ocean behind mountains. Hartmann (§6.5.2, [[Large-scale_patterns_Hartmann.pdf#page=5|pp.184–186]]) lists several causes of aridity: subtropical **subsidence**, **rain shadows** (Patagonia, the Great Basin), and **distance from moisture** (inland Asia), plus cold-coastal-current deserts (Atacama, Namib). The poleward cells give the *polar* deserts (cold, dry descent). 🟡 *extra · book*.

### 3.5 The ITCZ
<span class="scope-taught">taught</span> *Suhas 14 Oct p3*

Where the trade winds of the two hemispheres meet, the air has nowhere to go but up: this is the **Inter-Tropical Convergence Zone** ([[14th Oct.pdf#page=3|14 Oct, p3]]), the bright band of cloud across the tropical oceans and the ascending branch of the Hadley cells. It migrates with the Sun and, over Asia, becomes the monsoon trough ([[CL15 Monsoons]]).

> [!extra-beyond]- 🔵 Extra (beyond): why the Ferrel cell is "reverse"
> The Ferrel cell exists in the **Eulerian zonal mean** (average at fixed height or pressure) but is largely driven by eddy fluxes of heat and momentum. In the transformed Eulerian mean, or averaged on surfaces of constant potential temperature, the mid-latitude overturning is a single **thermally direct** cell; the "indirect" Ferrel cell is partly a bookkeeping artefact of where you average (Vallis, *Atmospheric and Oceanic Fluid Dynamics*, Ch. 11 treats "Hadley and Ferrel cells").

## 4. Why one cell cannot reach the pole: angular momentum
<span class="scope-taught">taught</span> *Suhas 8 Oct p15–18, 14 Oct p1, 21 Oct p2; handwritten notes p.3 (M&P §8.2.1)*

Energetics allowed a single cell. The next test is **angular momentum**, and it fails ([[21st Oct.pdf#page=2|21 Oct, p2]]: "angular momentum conservation does not permit a single meridional cell").

### 4.1 Absolute angular momentum
The angular momentum **per unit mass** about the Earth's axis of a parcel at latitude $\varphi$ with eastward wind $u$ relative to the ground is ([[8th Oct.pdf#page=15|8 Oct, p15–16]])

$$\boxed{A=\Omega a^2\cos^2\varphi+u\,a\cos\varphi}\tag{CL11.2}$$

> [!derivation]- Derivation
> $A=L_z/m=(\mathbf r\times\mathbf v)_z$. A parcel at distance $r=a\cos\varphi$ from the axis, seen from the **inertial** frame, moves eastward at the sum of the ground's speed $\Omega r$ and its own wind $u$: $v_{\rm in}=\Omega r+u$. The lever arm is $r$, so $A=r(\Omega r+u)=\Omega a^2\cos^2\varphi+ua\cos\varphi$. The first term is the angular momentum the parcel carries just by being on the rotating Earth; the second is due to the wind. (The slides first write $A=\Omega a^2+ua$ with $a$ the perpendicular distance from the axis, then substitute $a\to R\cos\varphi$.) Called "absolute" because it is measured in the inertial frame: [[Absolute Angular Momentum of Air]], [[Rotating Reference Frames]].

> [!intuition] The ice skater
> A skater spins slowly with arms out. Pulling the arms in shrinks the circle the mass moves on; angular momentum $mvr$ cannot change, so $v$ must go **up**. A ring of air drifting poleward is exactly this: its circle around the axis shrinks, so unless something takes angular momentum away it must **spin faster**.

Reference speeds ($\Omega a=464.6$ m s⁻¹): the **ground** moves east at $\Omega a\cos\varphi=$ 464.6, 402.3, 328.5 and 232.3 m s⁻¹ at 0°, 30°, 45°, 60°. The slide quotes ≈ 460 and ≈ 330 m s⁻¹ for the equator and 45° N ([[15th Oct.pdf#page=20|15 Oct p20]], see [[CL12 Rotating Frames and the Coriolis Force]]).

### 4.2 The ring of air
Take a ring of air that is **at rest at the equator**: $u=0$, $\varphi=0$, so $A_0=\Omega a^2$ ([[8th Oct.pdf#page=17|p17]]). Let the upper branch of the Hadley cell carry it poleward. Above the boundary layer there is no friction, and for an axisymmetric flow there are no east–west pressure forces to give a torque, so $A$ is **conserved**. At latitude $\varphi$:

$$\Omega a^2\cos^2\varphi+ua\cos\varphi=\Omega a^2\ \Longrightarrow\ \boxed{u(\varphi)=\Omega a\,\frac{1-\cos^2\varphi}{\cos\varphi}=\Omega a\,\frac{\sin^2\varphi}{\cos\varphi}}\tag{CL11.3}$$

([[8th Oct.pdf#page=18|p18]]; Marshall & Plumb Eq. 8-2). Plugging in numbers ($\Omega a=464.6$ m s⁻¹):

| latitude | 10° | 20° | 30° | 45° | 60° | 90° |
|---|---|---|---|---|---|---|
| $u$ (m s⁻¹) | 14.2 | 57.8 | **134** | 329 | 697 | $\infty$ |

![[fig_cl11_am_curves.png|860]]
*Figure CL11.3. (a) Winds needed to conserve $A$ for rings starting at rest at the equator and at 5°, 10°, 15°; the band is the observed subtropical-jet speed. (b) In the inertial frame the ground slows as it nears the axis (blue) while the ring speeds up (orange); the gap is the wind $u$.*

> [!intuition] Why infinity at the pole?
> Figure CL11.3b: the ring's speed in space is $\Omega a/\cos\varphi$. As $\varphi\to90^\circ$ the circle shrinks to a point; to keep its angular momentum a parcel would have to whirl round a vanishingly small circle at infinite speed. Nature will not allow that, so the cell **must end**.

> [!verify] 130 or 134 m s⁻¹ at 30°?
> Marshall & Plumb print $u(10^\circ,20^\circ,30^\circ)=(14,58,130)$ m s⁻¹. Recomputing Eq. 8-2 with $\Omega=7.292\times10^{-5}$ s⁻¹ and $a=6371$ km gives **(14.2, 57.8, 134.1)**; the book's 130 is a rounded (or approximate) value, and a table of exact numbers is in the AI book-notes. This chapter uses **134**. (It does not change the argument: both are far above the observed ~30–50 m s⁻¹.)

> [!pitfall] Quiz trap: what the formula applies to
> Eq. (CL11.3) is for the **upper branch**: frictionless, axisymmetric, starting from $u=0$ at the equator. It does **not** apply near the surface, where friction dominates, nor to the return flow.

**Why the conclusion is robust.** The assumptions — axisymmetry, no friction, start from rest at the equator, thin atmosphere ($r\approx a\cos\varphi$) — each fail a little, but not by a factor of 5. Even a ring that starts at 10° would need 118 m s⁻¹ at 30°.

### 4.3 Coriolis turns the flow east: the subtropical jet
Near the equator $f=2\Omega\sin\varphi$ is small, so the Coriolis force hardly constrains the flow: the equatorial atmosphere acts as if the Earth rotated slowly. Moving poleward, $f$ grows and turns the northward flow to its **right** (east), giving a westerly component. At the poleward edge of the cell we therefore expect strong westerlies, and there they are: the **[[Subtropical Jet]]**, "driven in large part by the advection from the equator of large values of absolute angular momentum by the Hadley circulation" (M&P p.143; handwritten notes p.3). Two descriptions of the same fact: [[Coriolis Force|Coriolis]] force turning the flow, or angular-momentum conservation (CL12 §4.3 shows they are equivalent: $\mathrm Du/\mathrm Dt=2\Omega\sin\varphi\,v+uv\tan\varphi/a$).

**The observed jet** is ~30 m s⁻¹ in the zonal mean (~50 m s⁻¹ instantaneous) at ~200 hPa near 30° in the winter hemisphere, much weaker than the 134 m s⁻¹ of Eq. (CL11.3). The ring-of-air number is an *upper bound*: the real cell terminates earlier, and eddies, friction and horizontal mixing remove westerly momentum (§5, §7, and the Held–Hou estimate of 59 m s⁻¹ in §8).

### 4.4 The trade winds
Near the surface the equatorward return flow is also turned right in the NH: equatorward + westward = **north-easterly** (south-easterly in the SH): the **[[Trade Winds and Westerlies|trade winds]]**. They are much weaker than the winds aloft because friction acts on the near-surface flow. In angular-momentum language: air that comes from higher latitudes, where the ground moves slowly, arrives at the equator where the ground moves fast, so it **lags** the ground (easterly) — and the ground drags it forward, giving the air angular momentum (§5).

### 4.5 Where the Hadley cell stops
M&P: "such an axisymmetric circulation cannot extend all the way to the pole in the way envisaged by Hadley; it must terminate somewhere before it reaches the pole. Just how far ... depends on many factors." The handwritten notes record the same. How far it goes *can* be estimated: §8 derives the Held–Hou result $\varphi_H=(5R/3)^{1/2}\approx20^\circ$.

> [!extra-beyond]- 🔵 Extra (beyond): absolute vorticity and the Rossby number of the ring
> The absolute vorticity of a zonal flow is $\zeta_a=f+\zeta=2\Omega\sin\varphi-\dfrac{1}{a\cos\varphi}\dfrac{\partial(u\cos\varphi)}{\partial\varphi}$. Differentiating (CL11.2) gives the identity $\zeta_a=-\dfrac{1}{a^2\cos\varphi}\dfrac{\partial A}{\partial\varphi}$. For a motionless atmosphere $A=\Omega a^2\cos^2\varphi$ and $\zeta_a=f$. For the angular-momentum-conserving wind $A$ is *uniform* in latitude, so $\zeta_a=0$: **the relative vorticity exactly cancels the planetary one**, $\zeta=-f$, i.e. a local Rossby number $\mathrm{Ro}=-\zeta/f=1$. Geostrophic balance requires $\mathrm{Ro}\ll1$ ([[CL13 Horizontal Motion - Geostrophic Balance and Friction]]), so in the Hadley-cell upper branch the flow is *not* in geostrophic balance: another way to say that the tropics are a different dynamical regime from mid-latitudes.

## 5. The angular-momentum budget of the whole atmosphere
<span class="scope-taught">taught</span> *handwritten notes p.3 (M&P §8.1: diagram of friction signs); Suhas 21 Oct p2*
<span class="scope-extra-book">extra · book</span> *M&P pp.140–143 (Fig. 8.1, footnote 3); Hartmann Fig. 6.17*

At the surface the zonal-mean wind is **easterly in the tropics and westerly in mid-latitudes**. The atmosphere sits on a rotating, rough planet, so friction couples the two ([[Suhas post midsem.pdf#page=3|handwritten notes p.3]]):

- **Tropics, $u<0$:** the ground moves east faster than the air; friction drags the air eastward, so the air **gains** westerly angular momentum from the Earth.
- **Mid-latitudes, $u>0$:** the air moves east faster than the ground; friction slows it, so the air **loses** angular momentum to the Earth.

In steady state the **net frictional torque on the whole atmosphere must be zero** (handwritten notes; M&P p.143): otherwise the total angular momentum would drift. Gain in the tropics equals loss in mid-latitudes, so there must be a **poleward transport of westerly angular momentum** from the tropics to the mid-latitudes. A zonal wind cannot do this (it moves nothing north–south): it needs meridional flow. In the tropics the mean meridional circulation does it (the Hadley cell advects angular momentum up and poleward); in mid-latitudes the mean flow is weak and **eddies** do it (M&P p.141; Hartmann Fig. 6.17).

![[CL11 Angular Momentum Cycle.svg|720]]
*Figure CL11.4. The cycle: picked up where the surface wind is easterly, carried up and poleward by the Hadley cell and by eddies, and returned to the solid Earth where the surface wind is westerly. Editable source: [[CL11 Angular Momentum Cycle.excalidraw]].*

> [!intuition] A relay race, with the Earth as the baton store
> Imagine the Earth as a giant flywheel with a pipeline of air wrapped around it. In the tropics the spinning ground feeds momentum into the air; the circulation relays it poleward; in mid-latitudes the air hands it back by rubbing against the ground. If the hand-in at one end were not equal to the hand-out at the other, the flywheel (the whole planet) would speed up or slow down, and the day would lengthen or shorten.

> [!extra-book]+ 🟡 Extra (book): the length of the day
> M&P footnote 3 (p.143): the length of the day does vary through exchange of angular momentum between the atmosphere and the solid Earth: by about **1 ms** on seasonal timescales and by about **0.1 ms from day to day**. Hartmann's Fig. 6.17 ([[Large-scale_patterns_Hartmann.pdf#page=1|p.180]]) draws the same cycle for January: "westerly angular momentum to atmosphere in easterlies" and "to Earth in westerlies", with wavy arrows for the poleward *and downward* transport by eddies.

> [!extra-beyond]- 🔵 Extra (beyond): how big is the atmosphere's angular momentum?
> Let the atmosphere (mass $5.3\times10^{18}$ kg) rotate rigidly with the Earth: $L_{\rm atm}\approx\tfrac23Ma^2\Omega\approx1.0\times10^{28}$ kg m² s⁻¹. The solid Earth has $I\Omega=8.0\times10^{37}\times7.29\times10^{-5}=5.8\times10^{33}$. A length-of-day change of 1 ms ($\Delta\Omega/\Omega\approx1.2\times10^{-8}$) therefore needs the atmosphere to swap $\Delta L\approx6.8\times10^{25}$ kg m² s⁻¹, only 0.7 % of the first number. In wind terms: changing the mass-weighted zonal-mean wind by $\Delta\bar u$ changes the angular momentum by $M\,a\langle\cos\varphi\rangle\Delta\bar u=2.6\times10^{25}\,\Delta\bar u$ (with $\langle\cos\varphi\rangle=\pi/4$ for mass-weighting), so **1 m s⁻¹ ≈ 0.4 ms** of length of day: a seasonal swing of ~2.6 m s⁻¹ in the global zonal-mean wind accounts for the 1 ms. (Besides friction, mountains exert a *pressure torque* on the atmosphere: Peixoto & Oort, *Physics of Climate*.)

## 6. Anatomy of the Hadley cell
<span class="scope-taught">taught</span> *handwritten notes p.3 (M&P §8.2.1, Figs. 8.4–8.5); 8 Oct p10; 14 Oct p2*
<span class="scope-extra-book">extra · book</span> *M&P p.144 (GFD Lab VIII), footnote 2*

Following one parcel round the loop (Figs. CL11.2 and 8.4):

| stage | where | what happens | winds |
|---|---|---|---|
| 1 | surface, near the equator | warm moist air converges ([[Intertropical Convergence Zone|ITCZ]]) and picks up heat and moisture from the warm ocean | trades weak at the convergence |
| 2 | rising branch | deep convection releases latent heat; air rises to ~15 km | little horizontal motion |
| 3 | upper troposphere, poleward | flow poleward; **angular momentum conserved**; Coriolis turns it east | westerlies strengthen with latitude |
| 4 | subtropical edge, ~30° | strongest westerlies: the **jet**; air cools radiatively and **sinks** | jet ~30–50 m s⁻¹ |
| 5 | subtropical subsidence | sinking air is warm (adiabatic compression) and dry (air aloft is drier than surface air) | calm subtropical highs |
| 6 | surface, equatorward | return flow turned right: **north-easterly trades**; friction adds angular momentum | trades a few m s⁻¹ |

- **Trade inversion.** The boundary between the warm, dry, subsiding air above and the cooler, moister near-surface air is the trade inversion, within which the trades blow ([[CL09 Radiative-Convective Equilibrium]]).
- **Weak horizontal temperature gradients** exist aloft within the cell (M&P Figs. 5.7–5.8): a consequence of very efficient meridional heat transport. Since air moving at ~1–3 m s⁻¹ crosses 3300 km (0° to 30°) in about 20–40 days, one circuit takes of order 2 months (my estimate).
- **In the axisymmetric model** the surface winds are westerly at the poleward edge of the cell and easterly near the equator, similar to observations but not identical: **observed surface westerlies maximise near 50° N/S, well poleward of the subtropical jet** (handwritten notes; M&P p.144), a hint that something other than the Hadley cell is at work (§7).

> [!extra-book]+ 🟡 Extra (book): GFD Lab VIII, the rotating annulus
> A cylindrical tank with a metal can of ice at the centre produces a temperature gradient decreasing "poleward". At slow rotation (about 1 rpm) a strong eastward ("super-rotating") flow develops in the upper fluid, maintained by **angular-momentum advection by the meridional circulation**: water rises at the outer wall, moves inward aloft conserving angular momentum (strong "westerly" flow), meets the cold inner wall, cools and sinks; dye and potassium-permanganate crystals show the flow outward along the bottom. A laboratory analogue of the Hadley cell and subtropical jet.
> Footnote 2 (p.143): for a faster (slower) rotating Earth, other things equal, the cell would extend less (more) far poleward. §8 makes this quantitative.

## 7. Beyond the tropics: eddies and the mid-latitudes
<span class="scope-taught">taught</span> *handwritten notes p.2–3 (M&P §5.4 "eddies and waves", §8.2 assumptions)*
<span class="scope-extra-book">extra · book</span> *M&P p.77–78, Fig. 5.22*

The theory so far assumed an **axisymmetric** atmosphere responding to an axisymmetric heating. It "works for the tropics, fails in the extratropics (symmetry broken by hydrodynamical instability)" (handwritten notes p.3; M&P p.142). On any weather map (M&P Fig. 5.22) the mid-latitude flow is full of localised highs and lows, instantaneous structure that the zonal average hides. These **eddies** are "the key agency of meridional heat and moisture transport in the middle to high latitudes" (M&P p.77), and of the poleward angular-momentum transport of §5. They arise from an instability of the thermal-wind shear produced by the pole-to-equator temperature gradient (**baroclinic instability**, M&P §8.2.2, not covered in the excerpt).

> [!intuition] Stirring versus overturning
> Heat a pan of water on one side and cool it on the other. Near the heater a neat convection cell forms (the Hadley cell). Further out the flow breaks into swirls that stir hot into cold. The swirls move more heat than the tidy overturning does. Mid-latitudes are the swirly part, and the "Ferrel cell" is just what the *average* of the swirls looks like.

**Reynolds split.** Write $v=[v]+v'$ and $T=[T]+T'$. The zonal-mean poleward heat flux is $[vT]=[v][T]+[v'T']$: the first term is the mean overturning (strong in the tropics), the second the **eddy covariance** (strong in mid-latitudes; see [[Probability - Course Map]] for covariance). The same split applies to angular momentum, $[vA]=[v][A]+[v'A']$.

## 8. How far does the Hadley cell reach? The Held–Hou model
<span class="scope-extra-beyond">extra · beyond</span> *Held & Hou (1980), J. Atmos. Sci. 37, 515–533; derivation re-done here and checked against Vallis, AOFD §11.2*

> [!extra-beyond]- 🔵 Extra (beyond): derivation of the edge, $\varphi_H=(5R/3)^{1/2}$
> **Assumptions.** Axisymmetric and steady; the poleward upper branch conserves angular momentum; the lower branch has $u\approx0$ (friction); thermal-wind balance; the heating is a Newtonian relaxation to a radiative-equilibrium potential temperature $\theta_E$; dry, small-angle ($\sin\varphi\approx\varphi$, $\cos\varphi\approx1$, $y=a\varphi$).
> **1. Wind.** From (CL11.3): $u_M=\Omega y^2/a$ in the upper branch.
> **2. Temperature slaved to the wind.** Thermal-wind balance, integrated from the ground ($u=0$) to the outflow height $H$, reads $2\Omega\sin\varphi\,u_M(H)=-\dfrac{g H}{a\theta_0}\dfrac{\partial\bar\theta}{\partial\varphi}$, where $\bar\theta$ is the vertically-averaged potential temperature. With $u_M=\Omega a\sin^2\varphi/\cos\varphi$ this gives, in the small-angle limit, $$\bar\theta_M(y)=\theta(0)-\frac{\theta_0\,\Omega^2\,y^4}{2gHa^2}.$$ So the temperature *drops steeply* poleward, flat near the equator.
> **3. The radiative-equilibrium profile.** $\theta_E(y)=\theta_{E0}-\Delta\theta\,(y/a)^2$.
> **4. Two conditions fix the unknowns** ($\theta(0)$ and the edge $Y_H=a\varphi_H$). (i) **Continuity** of temperature at the edge, $\bar\theta_M(Y_H)=\theta_E(Y_H)$ (otherwise the thermal wind would be infinite). (ii) **No net heating inside the cell**: the circulation only redistributes heat, so $\int_0^{Y_H}\bar\theta_M\,\mathrm dy=\int_0^{Y_H}\theta_E\,\mathrm dy$ (the "equal-area construction").
> **5. Algebra.** Write $\kappa=\Omega^2a^2\theta_0/(2gH)$ so that $\bar\theta_M=\theta(0)-\kappa\varphi^4$. Condition (i): $\theta(0)=\theta_{E0}-\Delta\theta\varphi_H^2+\kappa\varphi_H^4$. Condition (ii): $\int_0^{\varphi_H}[\theta(0)-\kappa\varphi^4-\theta_{E0}+\Delta\theta\varphi^2]\mathrm d\varphi=0$, i.e. $(\kappa\varphi_H^4-\Delta\theta\varphi_H^2)\varphi_H-\kappa\varphi_H^5/5+\Delta\theta\varphi_H^3/3=0$. Divide by $\varphi_H^3$: $\tfrac45\kappa\varphi_H^2=\tfrac23\Delta\theta$, so $$\boxed{\varphi_H=\Big(\frac{5}{3}R\Big)^{1/2},\qquad R=\frac{gH\,\Delta\theta}{\theta_0\,\Omega^2a^2}}$$ and $\theta(0)=\theta_{E0}-\tfrac{5}{18}R\,\Delta\theta$. $R$ is the **thermal Rossby number**: (speed of shallow-water waves / rotation speed)$^2$ times the fractional equator–pole temperature contrast.
> **6. Numbers.** Vallis's example ($\theta_0=300$ K, $\Delta\theta=50$ K, $H=10$ km, $\Omega=7.272\times10^{-5}$ s⁻¹) gives $R=0.076$ and $\varphi_H=0.356$ rad $=\mathbf{20.4^\circ}$ (reproduced by solving the two conditions numerically: 20.41°). The wind at the edge is $u_M(\varphi_H)=\Omega a\varphi_H^2=59$ m s⁻¹, closer to the observed ~50 m s⁻¹ jet maxima than 134 m s⁻¹. With $H=15$ km the edge is 25.0°.
> **7. Scaling and its checks.** $\varphi_H\propto\Omega^{-1}H^{1/2}\Delta\theta^{1/2}$, i.e. by logarithmic differentiation ([[Linearisation and Sensitivity]]) $\Delta\varphi_H/\varphi_H=\tfrac12\Delta H/H+\tfrac12\Delta(\Delta\theta)/\Delta\theta-\Delta\Omega/\Omega$. Doubling $\Omega$ halves the cell (10°); halving it gives 41°; a very slowly rotating planet such as Venus gets $\varphi_H>90^\circ$, i.e. a cell that spans the globe. Real Earth: observed edges are 25–30°, wider than 20° (moisture, eddies, seasonality neglected here).
> **8. Caveats.** Dry Boussinesq model, Newtonian cooling, symmetric heating, no eddies: the model gives a *finite* cell for a perfectly symmetric atmosphere, which is the point, but not a quantitative forecast.

![[fig_cl11_held_hou.png|860]]
*Figure CL11.5. (a) Equal-area construction for Vallis's parameters (the two shaded areas are equal). (b) The cell edge against rotation rate. Script `fig_cl11_held_hou.py`.*

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Why the Hadley cell stops: angular momentum and the ring of air
> A ring of air conserves its absolute angular momentum per unit mass A = Ωa² cos²φ + u a cos φ as it drifts poleward.
>
> ![[cl_angular_momentum.png|720]]
>
> **Try:** Slide φ to 30°: u = 134 m/s (the observed subtropical jet is weaker, because eddies and friction break the conservation); at 60°: 697 m/s, at 80° more than 2500 m/s. Start the ring at 10° instead of the equator to see the wind it picks up. Switch to 'surface (friction)' to see the trade-wind sign.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_angular_momentum.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_angular_momentum.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL11 connects
> **Builds on:** [[CL10 Global Energy Balance and Meridional Structure]] (why energy must move) · [[CL03 Radiation and Planetary Energy Balance]] (the tropical surplus) · [[CL06 Hydrostatic Balance and Vertical Structure]] (thickness) · [[CL09 Radiative-Convective Equilibrium]] (convection and the trade inversion).
> **Leads to:** [[CL12 Rotating Frames and the Coriolis Force]] (why the Coriolis force exists) · [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (jets, geostrophy, Rossby number) · [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (the observed winds in detail) · [[CL15 Monsoons]] (the seasonal ITCZ).
> **Concepts:** [[Hadley Cell]] · [[Mass Stream Function]] · [[Ferrel Cell and Polar Cell]] · [[Subtropical Jet]] · [[Trade Winds and Westerlies]] · [[Intertropical Convergence Zone]] · [[Absolute Angular Momentum of Air]] · [[Coriolis Force]] · [[Rotating Reference Frames]].

> [!connection] Mechanics and quantum mechanics
> The conservation of angular momentum that rules the Hadley cell is the same law as the figure skater's spin and, in quantum mechanics, the reason why electrons in atoms have conserved angular momentum: [[Quantum Mechanics - Course Map]]. In a rotating frame it becomes the Coriolis force: [[Rotating Reference Frames]].

> [!connection] Thermodynamics and waves
> The Hadley cell is a heat engine (heat in at the warm surface, out by radiation aloft): [[Thermodynamics and Statistical Mechanics - Course Map]]; sinking air warms by compression ([[Ideal Gas Law]]). Mid-latitude eddies are baroclinic waves; Rossby waves and the thermal wind belong to [[Waves - Course Map]].

> [!connection] Landscapes, deep time, ecology
> Desert belts at ±30°, rain shadows and dust sources shape landscapes: [[Landscapes and Geomorphology - Course Map]]. The position of the ITCZ and the deserts shifts with climate in deep time: [[Evolution of Earth and Life - Course Map]]. In a globally frozen [[Snowball Earth]], the small thermal inertia of the surface is argued to reverse the annual-mean tropical circulation and produce an equatorial desert (Hoffman et al. 2017). Rainforest under the ITCZ, savanna and desert under the sinking branch are the template for the world's biomes: [[Ecology and Evolution - Course Map]].

> [!connection] Foundations
> Conservation laws and symmetry (axisymmetry removes the pressure torque): [[Rotating Reference Frames]]; log-derivative scaling of $\varphi_H$: [[Linearisation and Sensitivity]]; eddy flux as a covariance: [[Probability - Course Map]].

## Summary
> [!summary] Cheat-sheet
> - **Single cell**: temperature contrast ⇒ thick warm columns ⇒ upper-level pressure surfaces slope down poleward ⇒ poleward aloft, equatorward below (*thermally direct*).
> - **Mass stream function** $\psi=\dfrac{2\pi a\cos\varphi}{g}\int_0^p[v]\,\mathrm dp$; $\psi=0$ at top and ground; positive = clockwise; contours = streamlines; $[v]=\dfrac{g}{2\pi a\cos\varphi}\partial_p\psi$.
> - **Observed**: Hadley (0–30°, direct), Ferrel (30–60°, indirect), Polar (60–90°, direct); ascent follows the summer hemisphere; ascent ↔ wet (ITCZ), descent ↔ dry (deserts, trade inversion); upper meridional wind ≲ 3 m s⁻¹, return flow weaker.
> - **Angular momentum** $A=\Omega a^2\cos^2\varphi+ua\cos\varphi$; ring from rest at the equator: $u=\Omega a\sin^2\varphi/\cos\varphi$ = 14, 58, **134** m s⁻¹ at 10°, 20°, 30° (M&P print 130); $\to\infty$ at the pole ⇒ the cell **must end**.
> - **Consequences**: poleward flow turned right ⇒ westerlies ⇒ **subtropical jet** (~30°, 200 hPa, ~30 m s⁻¹ mean); equatorward return flow ⇒ **trades** (NE in NH); surface westerlies peak near 50°.
> - **Budget**: tropics gain westerly AM from the ground (easterlies), mid-latitudes lose it (westerlies); net torque zero; transport by Hadley cell (tropics) and eddies (mid-latitudes).
> - 🔵 **Held–Hou**: $\varphi_H=(5R/3)^{1/2}$, $R=gH\Delta\theta/(\theta_0\Omega^2a^2)$; 20° for Earth-like parameters, $\propto1/\Omega$.

> [!summary] Quiz checklist (checked against M&P and the AI book-notes)
> 1. **Signs**: with $\Omega>0$, Coriolis deflects to the **right**; poleward flow in the NH becomes **westerly** (eastward). ✓ *(M&P p.143; notes §7.2)*
> 2. **Where (CL11.3) applies**: upper branch only (frictionless, axisymmetric, $u=0$ at the equator); **not** at the surface. ✓
> 3. **Hadley ascent** follows the **summer hemisphere**, it is not fixed at the equator. ✓ *(M&P p.74)*
> 4. **Ferrel cell** is thermally **indirect** (rising at 60°, sinking at 30°); Hadley and Polar are direct. ✓
> 5. The **book's 130 m s⁻¹** at 30° is a rounding of 134. (Quote 134, mention 130.)
> 6. $\psi=0$ at the ground means **no net mass flux** in the column, not "no wind".
> 7. The **subtropical jet** is strongest in the **winter** hemisphere (~30 m s⁻¹ mean, ~50 instantaneous); surface westerlies peak at ~50°, **not** at the jet latitude.
> 8. A single equator-to-pole cell is not forbidden by energy, it is forbidden by **angular momentum**.

## Practice
1. **Ground speed.** Find the eastward speed of the ground and the angular momentum per unit mass of air at rest relative to the ground at 30°. Express the latter as a fraction of $\Omega a^2$.
2. **Ring winds.** Use (CL11.3) to find the wind of a ring that left the equator at rest when it reaches 25° and 40°.
3. **Ring from 10°.** What wind does a ring that is at rest at 10° have at 30°?
4. **Equatorward return.** Air at rest relative to the ground at 30° N moves to the equator conserving angular momentum. What is its zonal wind there? Repeat for the move 30° → 10°. Why are real trade winds only a few m s⁻¹?
5. **Mass flux.** At 15° N the zonal-mean meridional wind is 2 m s⁻¹ through 200 hPa aloft. (a) Find the northward mass flux. (b) If the return flow is uniform over 700 hPa, how fast is it?
6. **Signs.** Sketch $\psi(\varphi,p)$ for NH Hadley, Ferrel and Polar cells and label the sign of each, the direction of the flow aloft and at the surface, and the surface wind direction in each cell.
7. **Held–Hou.** For $H=12$ km, $\Delta\theta=40$ K, $\theta_0=300$ K find $R$ and $\varphi_H$. What rotation rate would give a cell reaching 30°? What happens to the answer if $\Delta\theta$ increases?
8. **Day length.** By how much does the length of day change if the mass-weighted zonal-mean wind rises by 1 m s⁻¹? Which direction?
9. **Conceptual.** (a) Why is the surface friction torque *positive* in the tropics and *negative* in mid-latitudes? (b) Why can't the zonal flow itself carry angular momentum poleward? (c) Explain "thermally indirect" in one sentence.

> [!example]- Solutions
> 1. $\Omega a\cos30^\circ=402.3$ m s⁻¹; $A=\Omega a^2\cos^2\varphi=0.75\,\Omega a^2=2.22\times10^9$ m² s⁻¹ ($\Omega a^2=2.96\times10^9$).
> 2. $u=\Omega a\sin^2\varphi/\cos\varphi$: 25° → 91.6 m s⁻¹; 40° → 250.6 m s⁻¹.
> 3. $u=\Omega a(\cos^210^\circ-\cos^230^\circ)/\cos30^\circ=117.9$ m s⁻¹.
> 4. $u=\Omega a(\cos^2\varphi_0-\cos^2\varphi)/\cos\varphi$: 30° → 0: $-116$ m s⁻¹ (westward); 30° → 10°: $-103.7$ m s⁻¹. Real trades are a few m s⁻¹ because friction continually restores angular momentum (the ground drags the air eastward), so $A$ is not conserved in the lower branch.
> 5. (a) $\dfrac{2\pi a\cos\varphi}{g}=3.94\times10^6$ kg Pa⁻¹ m⁻¹·... so flux $=3.94\times10^6\times2\times2\times10^4=1.58\times10^{11}$ kg s⁻¹. (b) Return: $v=1.58\times10^{11}/(3.94\times10^6\times7\times10^4)=0.57$ m s⁻¹.
> 6. NH Hadley $\psi>0$ (clockwise): poleward aloft, equatorward at the surface (easterly trades). Ferrel $\psi<0$ (anticlockwise): equatorward aloft, poleward at the surface (westerlies). Polar $\psi>0$: poleward aloft, equatorward at the surface (polar easterlies). Ascent is where $\psi$ increases poleward (equator, 60°), descent where it decreases (30°, pole).
> 7. $R=gH\Delta\theta/(\theta_0\Omega^2a^2)=9.81\times1.2\times10^4\times40/(300\times2.159\times10^5)=0.0727$; $\varphi_H=(5R/3)^{1/2}=0.348$ rad $=19.9^\circ$. For 30° $R=3\varphi^2/5=0.164$, so $\Omega=\Omega_E\sqrt{0.0727/0.164}=0.66\,\Omega_E$ (day ≈ 36 h). $\varphi_H\propto\Delta\theta^{1/2}$: a larger equator-to-pole contrast widens the cell.
> 8. $\Delta L=M\,a\,\tfrac\pi4\,\Delta\bar u=2.6\times10^{25}$ kg m² s⁻¹ and $\Delta\mathrm{LOD}=\mathrm{LOD}\,\Delta L/(I\Omega)=0.39$ ms; westerlies increase ⇒ the solid Earth slows ⇒ **longer** day.
> 9. (a) Tropical surface wind is easterly, so the ground moves east *faster* than the air and friction speeds the air up (gain, positive); in mid-latitudes the air is faster than the ground and friction slows it (loss). (b) A zonal wind moves air east–west; transporting angular momentum *north–south* needs a meridional velocity $v$ correlated with $A$. (c) A thermally indirect cell has the *colder* air rising and the *warmer* air sinking, so it turns kinetic energy into potential energy; it needs the eddies to drive it.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (3): the other tool's concept notes from the lectures, unreviewed
> [[zettel/atmospheric-angular-momentum-balance|Atmospheric Angular Momentum Balance]] · [[zettel/atmospheric-convection-cell|Atmospheric Convection Cell]] · [[zettel/zonal-average|Zonal Average]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | need for transport; single-cell figure (W/E labels); upper branch warm poleward, lower cold equatorward | [[7th Oct.pdf#page=20\|7 Oct p20]]; [[8th Oct.pdf#page=4\|8 Oct p4–6]] | taught |
> | energetics allows one cell; thickness / height-gradient argument | [[8th Oct.pdf#page=13\|8 Oct p13–14]]; handwritten notes p.3 | taught |
> | test with angular momentum | [[14th Oct.pdf#page=1\|14 Oct p1]]; [[21st Oct.pdf#page=2\|21 Oct p2]] | taught |
> | mass stream function (definition, "northward mass flux above $p$") | [[7th Oct.pdf#page=20\|7 Oct p20]]; [[8th Oct.pdf#page=7\|8 Oct p7–8]]; handwritten p.3 ($\chi$ and its winds) | taught |
> | observed three cells; direct/indirect labels | [[8th Oct.pdf#page=9\|8 Oct p9–12]]; handwritten p.2 | taught |
> | seasonal behaviour, meridional winds < 3 m s⁻¹, return flow, ascent ↔ wet / descent ↔ dry, trade inversion, eddies | handwritten p.2 (M&P §5.4); [[climate-suhas merged.pdf#page=14\|M&P pp.73–77]] | taught |
> | climate impacts (deserts), ITCZ | [[14th Oct.pdf#page=2\|14 Oct p2–3]] | taught |
> | $A$, ring of air, $u(\varphi)$, jet, trades, termination of the cell, trade inversion, weak temperature gradients, surface westerlies at 50° | [[8th Oct.pdf#page=15\|8 Oct p15–18]]; handwritten p.3 (M&P §8.2.1); [[climate-suhas merged.pdf#page=22\|M&P pp.142–144]] | taught |
> | angular-momentum budget, friction signs, zero net torque | handwritten p.3 (M&P §8.1); [[climate-suhas merged.pdf#page=20\|M&P pp.140–141]] | taught |
> | axisymmetric assumption fails; eddies | handwritten p.2–3; M&P pp.77, 142 | taught |
> | magnitudes/units of Fig. 5.21; Hadley's ring picture | [[climate-suhas merged.pdf#page=16\|M&P pp.74, 76]] | extra/book |
> | numerical values 14/58/130; footnote 2 (rotation rate); footnote 3 (length of day) | [[climate-suhas merged.pdf#page=23\|M&P p.143]] | extra/book |
> | GFD Lab VIII | [[climate-suhas merged.pdf#page=24\|M&P p.144]] | extra/book |
> | Fig. 6.17 AM cycle with eddy transport; deserts (§6.5.2) | [[Large-scale_patterns_Hartmann.pdf#page=1\|Hartmann pp.180, 184–186]] | extra/book |
> | derivation of $\psi$ properties; thickness numbers; dry adiabat number; $\zeta_a=-\partial A/\partial\varphi/(a^2\cos\varphi)$, Ro=1; atmosphere AM and day length; circuit time; Ferrel as eddy artefact | derived here / Vallis | extra/beyond |
> | Held–Hou derivation, numbers, scaling | derived here; checked against Vallis AOFD §11.2 (Held & Hou 1980) | extra/beyond |
>
> **Dropped as redundant:** the repeat of the "ring of air" argument in the handwritten notes and in M&P §8.2.1 (merged with the 8 Oct slides in §4.2); the second statement of the angular-momentum formula on 8 Oct p15 and p16 (merged in §4.1); the summary slides of 21 Oct p1–2 (folded into §1 and §4).

> [!provenance]- Slide evidence (click to expand pages)
> ![[8th Oct.pdf#page=18&height=300]]
> ![[8th Oct.pdf#page=14&height=300]]
> ![[14th Oct.pdf#page=3&height=300]]
> ![[21st Oct.pdf#page=2&height=300]]

**References.** Marshall, J. & Plumb, R. A. (2008) *Atmosphere, Ocean and Climate Dynamics*, §5.4, Ch. 8 · Hartmann, D. L. (2016) *Global Physical Climatology*, 2nd ed., §6.5 · Held, I. M. & Hou, A. Y. (1980) *J. Atmos. Sci.* 37, 515–533 · Vallis, G. K. *Atmospheric and Oceanic Fluid Dynamics*, Ch. 11 · Peixoto, J. P. & Oort, A. H. (1992) *Physics of Climate* · Hoffman, P. F. et al. (2017) *Sci. Adv.* 3, e1600983.
