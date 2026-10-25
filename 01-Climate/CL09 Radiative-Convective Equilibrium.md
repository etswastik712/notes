---
title: CL09 Radiative-Convective Equilibrium
aliases: [CL09, RCE, Radiative-convective equilibrium, Convection and the lapse rate]
subject: climate
type: chapter
chapter: 9
part: III
scope: [taught, extra-book, extra-beyond]
by: [suhas-pre]
status: draft
prereq: ["[[CL08 Greenhouse Models]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/suhas-pre, src/book, status/draft]
---
# CL09 · Radiative-Convective Equilibrium

◀ [[CL08 Greenhouse Models]] · [[Climate - Course Map|Course Map]] · [[CL10 Global Energy Balance and Meridional Structure]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - **§1** radiative equilibrium puts the ground warmer than the air above it (the temperature discontinuity)
> - **§2.1** the static-stability criterion: environment lapse rate vs $\Gamma_d$ (stated, not derived)
> - **§3** convective adjustment and the RCE structure (convective below $z_T$, radiative above)
> - **§4.1** the tropical troposphere is close to neutral for *moist* convection
> - **§5** OLR as a convection diagnostic, $(300/220)^4\approx3.5$
> - **§6** when does convection happen: two routes, tropics vs mid-latitudes
>
> 🟡 **Extra · book** (assigned books, not shown in class)
> - **§2.2–2.4** first law → $\Gamma_d=g/c_p$, potential temperature, buoyancy frequency $N^2$ (Wallace & Hobbs §3.4, §3.6; M&P Problem 1)
> - **§4.2** moist adiabat, latent heat, Clausius–Clapeyron (W&H §3.5)
> - **§7** buoyancy-oscillation numbers (M&P Problem 2)
> - **§8** the convection tank experiment, GFD Lab II (M&P Fig. 4.28, Problem 3)
> - **§9.1–9.4** why 6.5 K/km, the tropopause, the greenhouse "paradox", RCE and climate sensitivity (W&H §10.1, §10.3)
>
> 🔵 **Extra · beyond** (added from outside the course)
> - **§1 box** grey-gas radiative equilibrium derived: skin temperature, surface jump $\approx15$ K, lapse rate ≈ 23 K/km
> - **§3 box** a numerical column model (RE vs two RCEs)
> - **§3 intuition** greenhouse effect = lapse rate × emission height
> - **§8 box** daytime boundary-layer growth
> - **§9.5** Manabe–Strickler history and limits of 1-D models

> [!verify] Evidence level for "taught"
> None of the dated photo slides (7–22 Oct) contains convection or RCE theory (checked all six sets; the ITCZ slide [[22nd Oct.pdf#page=6|22 Oct p6]] only shows a convective tower with low-level convergence). §1–§6 are labelled *taught* because they are in Suhas's pre-midsem notes ([[suhas notes.pdf#page=20|suhas notes pp.20–21]], consolidated by AI: secondary source) **and** in the assigned excerpt of Marshall & Plumb §4.7 ([[climate-suhas merged.pdf#page=1|pp.56–57]]), which say the same thing, and which are in the quiz scope ([[climate_book_notes.pdf#page=3|quiz notes]]). Figures cited by the book (Fig. 3.4, Fig. 4.9, Eq. 4-22) are **not** in your pages; I rebuild the content they carry.

> [!key] After this chapter you can
> - explain **why** a purely radiative atmosphere is unstable at the ground, and put numbers on it (jump, lapse rate),
> - derive $\Gamma_d=g/c_p$, the potential temperature $\theta$ and the buoyancy frequency $N^2=(g/T)(\Gamma_d-\Gamma)$, and use them to classify any profile as stable / neutral / unstable,
> - define **radiative–convective equilibrium** and say what controls the profile below and above the tropopause,
> - explain why tropical lapse rates follow the **moist** adiabat and why cloud tops show up as **low OLR**,
> - solve the three Marshall & Plumb problems of §4.9 from scratch.

---

## 1. The problem: radiation alone makes the ground too hot
<span class="scope-taught">taught</span> *Suhas notes pp.16–21 (multilayer model → discontinuity); M&P §4.7, p.56* · <span class="scope-extra-beyond">extra · beyond</span> *the box derives the numbers*

In [[CL08 Greenhouse Models]] the atmosphere was stacked layer by layer. In the idealisation used here, all sunlight passes straight through and is absorbed **at the ground** (in reality about two-thirds of the absorbed solar energy; [[CL07 Optical Properties of the Atmosphere]]); the ground can only get rid of that energy by emitting infrared, which the air absorbs and re-emits layer after layer on its way to space. Imagine the atmosphere *never moves*: only radiation moves energy. The temperature structure that results is called **radiative equilibrium** (RE). It has a striking feature: the ground is radiatively **much warmer than the air immediately above it**, a *temperature discontinuity at the surface* (M&P Fig. 3.4: "the radiative equilibrium temperature of the ground is considerably warmer than that of the air above"). That profile cools with height far faster than a rising parcel would, so it is **unstable** and convection must occur.

> [!intuition] A hot plate under a blanket
> Think of a CPU under a heat-sink, or a sunlit tarmac road under still air: the surface is heated *directly* by absorbed sunlight but can lose that heat only through a poor, slow channel (here: the bucket-brigade of absorption and re-emission through the atmosphere). To push 240 W m⁻² through a poor channel the source must sit at a much higher temperature than the stuff next to it. A fluid cannot hold that situation: hot, light air sits *under* cooler, heavier air. It overturns (shimmering air over a road is exactly this). The atmosphere's answer is convection.

> [!extra-beyond]+ 🔵 Extra (beyond): radiative equilibrium of a grey atmosphere, derived
> **Set-up.** Shortwave all absorbed at the ground, flux $F=\sigma T_e^4=S(1-\alpha)/4=238$ W m⁻² ($T_e=254.6$ K). Longwave: a **grey** absorber with vertical optical depth $\tau$ measured *downward from the top of the atmosphere*, and the two-stream equations with diffusivity factor $D\approx1.66$ (a slanted beam sees optical depth $D\tau$):
> $$\frac{\mathrm dF_\uparrow}{\mathrm d\tau}=D\,(F_\uparrow-\sigma T^4),\qquad\frac{\mathrm dF_\downarrow}{\mathrm d\tau}=D\,(\sigma T^4-F_\downarrow).$$
> **Radiative equilibrium** means no net heating of any layer, so the net upward flux is constant, $F_\uparrow-F_\downarrow=F$. Subtracting the two equations gives $0=D(F_\uparrow+F_\downarrow-2\sigma T^4)$, i.e. $\sigma T^4=\tfrac12(F_\uparrow+F_\downarrow)$. Adding them gives $\mathrm d(F_\uparrow+F_\downarrow)/\mathrm d\tau=DF$. With $F_\downarrow(0)=0$ at the top, $F_\uparrow+F_\downarrow=F(1+D\tau)$, hence
> $$\boxed{T^4(\tau)=\tfrac12\,T_e^4\,(1+D\tau)}\tag{CL9.1}$$
> - **Top** ($\tau\to0$): $T=2^{-1/4}T_e=214$ K, the **skin temperature** (there $F_\downarrow=0$ and $F_\uparrow=F$, so $\sigma T^4=F/2$).
> - **Just above the ground** ($\tau=\tau_s$): $T_a^4=\tfrac12T_e^4(1+D\tau_s)$.
> - **The ground** absorbs $F$ of sunlight plus the downward flux and emits $\sigma T_g^4=F_\uparrow(\tau_s)=\sigma T_a^4+F/2$ (since $F_\uparrow=\sigma T^4+F/2$). Therefore
> $$\sigma\,(T_g^4-T_a^4)=\tfrac12\sigma T_e^4\ \ \text{whatever }\tau_s,\qquad T_g^4=T_e^4\,(1+\tfrac12D\tau_s).\tag{CL9.2}$$
> **Numbers** for $\tau_s=2.5$: $T_g=254.6\,(1+2.075)^{1/4}=337.1$ K, $T_a=322.5$ K: a **jump of 14.6 K** at the ground, even though the air has no discontinuity of its own. (For $\tau_s=1$: $T_g=296.1$ K.)
> **Lapse rate near the ground.** From (CL9.1), $\mathrm dT/\mathrm d\tau=DT_e^4/(8T^3)$ and $\mathrm d\tau/\mathrm dz=-\rho g\,\mathrm d\tau/\mathrm dp$. For an absorber that is partly well mixed and partly water-vapour-like, $\tau(p)=\tau_s[0.2p_*+0.8p_*^4]$ with $p_*=p/p_s$, so $|\mathrm d\tau/\mathrm dz|=3.4\,\tau_s/H$ at the ground ($H=RT/g\approx9.4$ km):
> $$\Gamma_{RE}\approx\frac{1.66\,(254.6)^4}{8\,(322)^3}\cdot\frac{3.4\times2.5}{9.4\ \mathrm{km}}\approx24\ \mathrm{K\,km^{-1}}\ \ \Big(\gg\Gamma_d=9.8\Big).$$
> I checked this with a numerical column (see §3): it reproduces $T_g=337.1$ K exactly and gives a ground lapse rate of **23.0 K km⁻¹**. Wallace & Hobbs' radiative-equilibrium curve (Fig. 10.4) has its ground at roughly 330–340 K (read off the figure), in line with this.

---

## 2. Static stability: when does a layer overturn?
<span class="scope-taught">taught</span> *the criterion: Suhas notes p.20 ("used, not derived"); M&P p.56* · <span class="scope-extra-book">extra · book</span> *derivations: W&H §3.4, §3.6; M&P Problem 1*

### 2.1 The criterion (what was taught)
<span class="scope-taught">taught</span> *Suhas notes p.20*

Define the **lapse rate** $\Gamma\equiv-\mathrm dT/\mathrm dz$ (positive when temperature falls with height; see [[Lapse Rate]]). A rising unsaturated parcel cools by expansion at the **dry adiabatic lapse rate**

$$\Gamma_d=\frac{g}{c_p}=\frac{9.81}{1004}\approx9.8\ \mathrm{K\,km^{-1}}$$
(the [[Dry Adiabatic Lapse Rate]]).

| environment lapse rate | verdict | what a parcel pushed up does |
|---|---|---|
| $\Gamma<\Gamma_d$ | **stable** | arrives colder (denser) than its surroundings and sinks back |
| $\Gamma=\Gamma_d$ | neutral | arrives with the same temperature, stays put |
| $\Gamma>\Gamma_d$ | **unstable** | arrives warmer (lighter), keeps rising: **convection** |

The radiative-equilibrium profile of §1 has $\Gamma\approx23\gg9.8$ at the ground: **unstable** ([[Atmospheric Stability]]).

> [!intuition] A ball on a landscape
> Static stability is a ball on a surface. Stable = ball in a bowl (push it, it rolls back); neutral = ball on a flat table (stays wherever you leave it); unstable = ball on top of a hill (any push and it accelerates away). The parcel is the ball; the environment's lapse rate is the shape of the landscape. In the language of [[Fixed Points and Linear Stability]] the three cases are a *centre*, a *marginal* case and a *saddle*; §2.4 shows this literally.

### 2.2 Where $\Gamma_d=g/c_p$ comes from
<span class="scope-extra-book">extra · book</span> *W&H §3.4.2, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=94|p.77]]*

> [!extra-book]+ 🟡 Extra (book): derivation from the first law
> Apply the [[First Law of Thermodynamics]] to a unit mass of air: $\mathrm dq=c_p\,\mathrm dT-\alpha\,\mathrm dp$ ($\alpha=1/\rho$). A parcel that exchanges no heat with its surroundings is **adiabatic**, $\mathrm dq=0$ ([[Adiabatic Process and Potential Temperature]]). Its pressure always equals that of the environment, which is in hydrostatic balance, $\mathrm dp=-\rho g\,\mathrm dz$ ([[CL06 Hydrostatic Balance and Vertical Structure]]). Then
> $$c_p\,\mathrm dT=\alpha\,\mathrm dp=-g\,\mathrm dz\ \Rightarrow\ \Big(\frac{\mathrm dT}{\mathrm dz}\Big)_{\rm parcel}=-\frac{g}{c_p}=-\Gamma_d .\tag{CL9.3}$$
> Equivalently $\mathrm d(c_pT+gz)=0$: the **dry static energy** $c_pT+gz$ is conserved. With $c_p=1004$ J kg⁻¹ K⁻¹, $\Gamma_d=9.77$ K km⁻¹. The *observed* mean lapse rate of the troposphere is 6–7 K km⁻¹ (W&H p.77); the parcel value is a property of the parcel, the observed one a property of the environment.

> [!intuition] An energy ledger
> Lifting 1 kg of air by $\mathrm dz$ costs $g\,\mathrm dz$ of potential energy. A parcel that exchanges no heat must pay from its own internal (thermal) energy, $c_p\,\mathrm dT$. So **rising air spends its warmth to climb**, at the exchange rate $g/c_p\approx10$ K per kilometre. Everyday versions: a bicycle pump gets hot when you compress air (the work you do becomes heat), and the nozzle of a spray can gets cold as the gas expands. Same physics, run backwards for a parcel that rises into thinner air.

### 2.3 Potential temperature: a label that rising parcels keep
<span class="scope-extra-book">extra · book</span> *W&H §3.4.3, p.77–78*

> [!extra-book]+ 🟡 Extra (book): potential temperature $\theta$
> The **potential temperature** is the temperature a parcel would have if brought adiabatically to the reference pressure $p_0=1000$ hPa. Along an adiabat, from (CL9.3) and the ideal gas law ($\alpha\,\mathrm dp=RT\,\mathrm dp/p$): $c_p\,\mathrm dT=RT\,\mathrm dp/p\Rightarrow\mathrm d\ln T=\kappa\,\mathrm d\ln p$ with $\kappa=R/c_p=0.286$. Integrating,
> $$\theta=T\Big(\frac{p_0}{p}\Big)^{\kappa},\qquad\theta\ \text{conserved in adiabatic motion}.\tag{CL9.4}$$
> *Example.* $T=280$ K at 800 hPa: $\theta=280\,(1000/800)^{0.286}=298.4$ K. A parcel with $T=255$ K at 500 hPa has $\theta=310.9$ K.
> **Stability in terms of $\theta$.** Taking $\ln$ and differentiating, $\dfrac{\partial\ln\theta}{\partial z}=\dfrac1T\dfrac{\partial T}{\partial z}-\kappa\,\dfrac{\partial\ln p}{\partial z}$. Hydrostatic balance with the ideal gas law gives $\partial\ln p/\partial z=-g/RT$, so $-\kappa\,\partial\ln p/\partial z=g/(c_pT)=\Gamma_d/T$:
> $$\boxed{\frac{\partial\ln\theta}{\partial z}=\frac1T\Big(\frac{\partial T}{\partial z}+\Gamma_d\Big)=\frac{\Gamma_d-\Gamma}{T}}\tag{CL9.5}$$
> So the layer is stable ⇔ $\Gamma<\Gamma_d$ ⇔ $\theta$ **increases with height**; a neutral (well-mixed, convective) layer has constant $\theta$.

> [!intuition] $\theta$ is a pressure-corrected temperature
> Weather maps correct station pressure to sea level so that places at different heights can be compared. $\theta$ is the same trick for temperature: it removes the cooling that comes merely from rising to lower pressure. A parcel moving adiabatically never changes its $\theta$ label; its real temperature changes only because pressure does. Mixing a layer thoroughly sets *one* $\theta$ for all of it, which is what "neutral" means.

### 2.4 The buoyancy frequency
<span class="scope-extra-book">extra · book</span> *M&P Problem 1 ([[climate-suhas merged.pdf#page=2|p.57]]); W&H §3.6.1, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=106|p.89]], Eqs. 3.73–3.75*

> [!extra-book]+ 🟡 Extra (book): displace a parcel and watch
> Push a parcel up by $\delta z$ from its equilibrium level. It keeps its own $\theta_p$ (the displacement is adiabatic), while the environment there has $\theta_E+(\mathrm d\theta_E/\mathrm dz)\,\delta z$. A parcel hotter than its surroundings by $\delta\theta$ has relative density deficit $\delta\theta/\theta_E$ and feels the buoyancy acceleration $g\,\delta\theta/\theta_E$. Here $\delta\theta=\theta_p-\theta_E(z+\delta z)=-(\mathrm d\theta_E/\mathrm dz)\,\delta z$, so
> $$\frac{\mathrm d^2\,\delta z}{\mathrm dt^2}=-N^2\,\delta z,\qquad N^2=\frac g{\theta_E}\frac{\mathrm d\theta_E}{\mathrm dz}=g\frac{\mathrm d\ln\theta_E}{\mathrm dz}=\boxed{\frac{g}{T_E}\Big(\frac{\mathrm dT_E}{\mathrm dz}+\Gamma_d\Big)}\tag{CL9.6}$$
> using (CL9.5). With $\Gamma=-\mathrm dT_E/\mathrm dz$: $N^2=(g/T_E)(\Gamma_d-\Gamma)$ (W&H Eq. 3.75).
> - $N^2>0$ (stable): $\delta z=\delta z_0\cos Nt$, a **buoyancy oscillation** of period $2\pi/N$.
> - $N^2=0$ (neutral): no restoring force; the parcel stays where it is pushed.
> - $N^2<0$ (unstable): $\delta z=\delta z_0\cosh(st)$, $s=\sqrt{-N^2}$, exponential growth.
> This is the same mathematics as a linear fixed point: write $\dot w=-N^2\delta z$, $\dot{\delta z}=w$, with eigenvalues $\pm iN$ (centre, stable) or $\pm s$ (saddle, unstable): [[Fixed Points and Linear Stability]].

![[fig_cl09_stability.png|760]]
*Figure CL9.1. Left: a parcel lifted 0.5 km along its dry adiabat (dashed) arrives colder than the stable environment (blue), equal in the neutral one, warmer in the unstable one (orange). Right: the resulting motion for 100 m initial displacement at $T=280$ K. Script `fig_cl09_stability.py`.*

> [!intuition] A spring made of stratification
> A stably stratified atmosphere is a spring. Lift a parcel, it is heavier than its surroundings and is pulled back; it overshoots, becomes lighter than its new surroundings, rises again: it **oscillates**. The frequency $N$ is the stiffness of the spring: steeper $\theta$ increase = stiffer spring. In the stratosphere ($\theta$ rises steeply) the oscillation is fast, in a neutral convective layer the spring has zero stiffness. The same $N$ sets the speed of internal gravity waves ([[Waves - Course Map]]).

> [!example] Worked example: how fast does the troposphere "ring"?
> Take $T=260$ K and the typical tropospheric $\Gamma=6.5$ K km⁻¹. Then $N^2=\dfrac{9.81}{260}\,(9.77-6.5)\times10^{-3}=1.25\times10^{-4}\ \mathrm{s^{-2}}$, $N=0.0111$ s⁻¹ and the period is $2\pi/N=563$ s $\approx9.4$ min. A parcel in the mid-troposphere pushed up a little oscillates with a period of about ten minutes. For the radiative-equilibrium layer of §1 ($\Gamma=23$, $T=322$): $N^2=(9.81/322)(9.77-23)\times10^{-3}=-4.0\times10^{-4}$, an overturning e-folding time $1/\sqrt{4.0\times10^{-4}}=50$ s.

> [!pitfall] Which lapse rate? Dry vs saturated
> Eq. (CL9.6) with $\Gamma_d$ holds for **unsaturated** parcels. Once a parcel condenses (§4.2) replace $\Gamma_d$ by the smaller $\Gamma_s$. A profile with $\Gamma_s<\Gamma<\Gamma_d$ is stable to dry but **unstable to saturated** displacements: *conditional instability* (W&H §3.6.3, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=108|p.91]], Fig. 3.16). This is why a moist tropical atmosphere convects even though its lapse rate is well below 9.8 K km⁻¹. Also: stability tells you a parcel *can* rise, not that it *will*; a trigger (heating, lifting, cooling aloft: §6) is still needed.

---

## 3. Convective adjustment and radiative–convective equilibrium
<span class="scope-taught">taught</span> *Suhas notes p.20–21; M&P p.56* · <span class="scope-extra-beyond">extra · beyond</span> *numerical column and the "pinning" argument*

**What convection does.** Unstable parcels rise, carrying heat upward (the ground's warmth is moved by bulk motion, not by radiation). Rising parcels mix with their surroundings; this *warms the environment aloft and cools the ground-level air* until the environment itself approaches **neutrality**, i.e. $\Gamma\to\Gamma_d$ for dry air or constant *moist* potential temperature in the moist tropics. This process, imposing a *maximum* lapse rate, is called **convective adjustment** ([[Convective Adjustment]], [[Convection]]).

**Radiative–convective equilibrium (RCE).** Combine the two controls: where convection reaches, it fixes the profile (near-neutral, a lapse rate $\Gamma_c$); above it, radiation alone sets the profile. The join is the **tropopause**, $z_T$ (in the tropics, the height reached by deep convection):

> [!key] Definition
> **RCE** = convectively determined state below $z_T$ + radiative-equilibrium state above $z_T$ (M&P Fig. 3.4: the blue curve versus the dashed pure-radiative curve).

> [!intuition] A speed limiter, a roof and a floor
> Radiation *wants* a profile that is far too steep near the ground. Convection acts as a **speed limiter** on the lapse rate: whenever radiation pushes $\Gamma$ above $\Gamma_c$, overturning clips it back (like a governor on an engine). The profile then has three anchors: a **roof** (the skin temperature 214 K, set by radiation in the thin air at the top), a **slope** below (set by convection) and a **floor**, the ground temperature, which is *whatever the slope delivers when the emission level sits where the planet's OLR must be 238 W m⁻²*. Next, the quantitative version.

> [!extra-beyond]+ 🔵 Extra (beyond): the pinning argument — greenhouse effect = lapse rate × emission height
> Outgoing radiation leaves from a level $z_e$ where, loosely, the atmosphere becomes transparent (the level of roughly unit optical depth, which W&H identify with the tropopause region, p.421). OLR must equal absorbed sunlight, so $T(z_e)\approx T_e=255$ K. **Below** $z_e$ convection fixes the slope $\Gamma$, therefore
> $$T_s\approx T_e+\Gamma\,z_e\qquad(255+6.5\times5\approx288\ \mathrm K).$$
> Read backwards: $z_e\approx(288-255)/6.5=5.1$ km, and **the 33 K greenhouse effect is the lapse rate times the emission height**. More greenhouse gas lifts $z_e$ (the layers that can still radiate to space are higher up, and colder), the roof stays at $T_e$, so the whole column below warms. To warm the surface by $0.99$ K (the no-feedback doubling of CO₂, $3.7/4\sigma T_e^3$, see [[Planck Sensitivity]]) the emission level must rise by $0.99/6.5\approx150$ m. This is how [[Greenhouse Effect]] and [[Zero-Dimensional Energy Balance Model]] connect to the vertical structure.

### A numerical RCE column
<span class="scope-extra-beyond">extra · beyond</span> *model in `scripts/cl09_rce.py` (my own code); compare W&H Fig. 10.4, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=439|p.422]]*

> [!extra-beyond]- 🔵 Extra (beyond): how the model works
> 80 layers equal in pressure; shortwave 238.2 W m⁻² absorbed at a ground slab ($C=10^6$ J m⁻² K⁻¹); grey two-stream longwave with $D=1.66$ and $\tau(p)=2.5\,[0.2p_*+0.8p_*^4]$; time-stepped to equilibrium (4-hour steps). **Convective adjustment (Manabe-style):** any two adjacent layers (or the ground and the lowest layer) steeper than $\Gamma_c$ are mixed to *exactly* $\Gamma_c$ conserving enthalpy $\sum\Delta p\,T$; I tested the flux solver against a direct recursion (agreement to $10^{-13}$) and the RE ground temperature against (CL9.2) (337.1 K, exact).

![[fig_cl09_re_vs_rce.png|820]]
*Figure CL9.2. Same sunlight, same infrared optical depth ($\tau_s=2.5$); only the vertical heat transport differs. Orange: pure radiative equilibrium (ground 337 K, 14.6 K jump, 23 K/km near the ground). Green dashed: convection limits the lapse rate to $\Gamma_d$ = 9.8 K/km. Blue: limited to the observed 6.5 K/km: ground 290 K, convection reaching 9.2 km, radiative equilibrium above. Right: lapse rates. Script `fig_cl09_re_vs_rce.py`.*

| case | ground $T_g$ | lowest air | convective top | OLR |
|---|---|---|---|---|
| pure radiative equilibrium | **337.1 K** | 321 K (jump 16 K) | none: super-adiabatic below 4.2 km ($>9.8$), unstable below 5.5 km ($>6.5$) | 238.2 W m⁻² |
| RCE, $\Gamma_c=9.8$ K/km | **301.3 K** | 300.7 K | 6.4 km | 238.2 W m⁻² |
| RCE, $\Gamma_c=6.5$ K/km | **289.9 K** | 289.5 K | 9.2 km | 238.2 W m⁻² |

Three lessons:
1. **Convection cools the surface** (337 → 290 K, −47 K) **and warms the free troposphere** (blue lies right of orange above ≈2.6 km, by 8 K at 4 km). Total energy is unchanged (OLR = 238 W m⁻² in all three): convection merely *moves* it from the ground into the air.
2. **The ground–air jump vanishes** (0.4 K left, from the finite layer thickness).
3. **Above the convective top the three profiles coincide**, approaching the skin temperature of 214 K: radiation controls the stratosphere.
The surface temperature of the 6.5 K/km run (290 K) is close to the observed 288 K. This is a toy (grey gas, no clouds, no humidity feedback, absorbed sunlight fixed), so the closeness is partly luck, but the *structure* is the one in Wallace & Hobbs Fig. 10.4.

> [!pitfall] "RCE means convection everywhere"
> No. Above $z_T$ the state is radiative; below it is convective. The tropopause marks the join, and in the real tropics it is where deep convection stops.

---

## 4. The tropical troposphere
<span class="scope-taught">taught</span> *§4.1: Suhas notes p.21; M&P p.56* · <span class="scope-extra-book">extra · book</span> *§4.2: W&H §3.5, §3.7.3*

### 4.1 Neutral for *moist* convection (what was taught)
<span class="scope-taught">taught</span> *M&P p.56: "constant moist potential temperature"*

Observations show that the **tropical troposphere is close to neutral for moist convection** all the way up to the tropopause (M&P cite their Fig. 4.9). Convection is frequent and deep enough in the tropics to keep the whole column near the **moist adiabat**. Hence: *below $z_T$ the state is convectively determined, above $z_T$ radiative*; the profile is the RCE structure of §3, and is a good first-order description of the mean tropical temperature profile.

How the tropical structure reaches **mid-latitudes** is "less certain": local convection is unlikely to be the main control there; **large-scale (synoptic) systems** transport heat both vertically and horizontally ([[CL10 Global Energy Balance and Meridional Structure]], [[CL11 Mean Meridional Circulation and Angular Momentum]]).

### 4.2 Why moist? Latent heat and the saturated lapse rate
<span class="scope-extra-book">extra · book</span> *W&H §3.5.2–3.5.4, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=101|p.84]]; §3.7.3, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=114|p.97]]*

> [!intuition] A heater inside the parcel
> A parcel that rises keeps cooling by expansion. When it cools enough that the water vapour it carries **condenses** (cloud forms), condensation releases latent heat, a small heater switched on *inside* the parcel. The parcel still cools as it rises, but more slowly than a dry one. The warmer and more humid the air, the more vapour there is to condense (the [[Clausius-Clapeyron Relation]]: saturation vapour pressure rises ~7 % per kelvin), so the heater is stronger in the warm tropics than in cold air near the tropopause.

> [!extra-book]+ 🟡 Extra (book): the saturated adiabatic lapse rate
> With condensation the first law reads $c_p\,\mathrm dT+g\,\mathrm dz=-L\,\mathrm dr_s$ ($r_s$ the saturation mixing ratio, $L$ the latent heat of vaporisation, $2.5\times10^6$ J kg⁻¹). Take $r_s\simeq\varepsilon e_s/p$ with $\varepsilon=0.622$ and use Clausius–Clapeyron, $\mathrm d\ln e_s/\mathrm dT=L/(R_vT^2)$, and hydrostatics, $\mathrm d\ln p=-g\,\mathrm dz/(R_dT)$:
> $$\mathrm dr_s=r_s\Big[\frac{L}{R_vT^2}\mathrm dT+\frac{g\,\mathrm dz}{R_dT}\Big].$$
> Substituting and collecting $\mathrm dT$ and $\mathrm dz$ terms:
> $$\boxed{\Gamma_s=\frac{g\,\big(1+\dfrac{L\,r_s}{R_dT}\big)}{c_p+\dfrac{L^2r_s\,\varepsilon}{R_dT^2}}}\qquad(\Gamma_s<\Gamma_d).\tag{CL9.7}$$
> Evaluated with the Bolton (1980) saturation formula: $\Gamma_s=4.3$ K km⁻¹ at 20 °C, 1000 hPa; 6.0 at 0 °C, 800 hPa; 7.7 at −20 °C, 500 hPa; 9.0 at −40 °C, 300 hPa. W&H quote 4 K km⁻¹ near the ground in warm humid air to 6–7 K km⁻¹ in the middle troposphere, "only slightly less than $\Gamma_d$" near the tropopause. A saturated parcel that leaves a 300 K, 1000 hPa surface follows the blue curve below; it reaches 220 K at **13.8 km** (168 hPa), where a dry parcel would have reached 220 K at only 8.2 km.

![[fig_cl09_moist_adiabat.png|760]]
*Figure CL9.3. Left: $\Gamma_s(T,p)$: small for warm moist air, approaching $\Gamma_d$ for cold air. Right: a saturated tropical parcel (blue) against the dry adiabat (orange) and the observed-mean 6.5 K/km (dashed). Script `fig_cl09_moist_adiabat.py`.*

The undiluted moist adiabat from a saturated 300 K surface is **warmer aloft** than the observed tropical mean (251.7 K vs the 6.5 K/km line's 235 K at 10 km): real parcels mix with drier environmental air (*entrainment*) and the surface air is not saturated, so real profiles lie between this curve and the dry adiabat; the *shape* (neutral to moist ascent, set by the warmest, most humid boundary-layer air) is what the book means.

> [!example] Worked example: latent heat is a big deal
> Lifting a 300 K parcel dry to 10 km would leave it at $300-9.8\times10=202$ K; the saturated parcel arrives at 252 K: **50 K warmer** because condensation returned latent heat. Convert it: the temperature difference times $c_p$ is $\approx50\,\text{K}\times1004=5\times10^4$ J kg⁻¹, about 20 g of condensed water per kg of air at $L=2.5\times10^6$ J kg⁻¹, close to the 23 g kg⁻¹ that a saturated 300 K, 1000 hPa parcel holds.

---

## 5. OLR as a convection diagnostic
<span class="scope-taught">taught</span> *Suhas notes p.21; M&P p.56, Fig. 4.27 ([[climate-suhas merged.pdf#page=1|p.56]])*

[[Outgoing Longwave Radiation]] (OLR) is the infrared flux a satellite sees leaving the planet. Two kinds of tropical scene differ enormously:

- **Low OLR:** deep convective towers whose **cold cloud tops** ($T_c\approx220$ K) emit to space;
- **High OLR:** *subtropical deserts and cooler oceans*, "relatively dry and cloud-free", where the radiation comes from the **warm surface** ($T_s\approx300$ K).

Since emission goes as $T^4$,

$$\frac{\sigma T_s^4}{\sigma T_c^4}=\Big(\frac{300}{220}\Big)^4=3.46,\qquad\sigma T_s^4=459\ \mathrm{W\,m^{-2}},\quad\sigma T_c^4=133\ \mathrm{W\,m^{-2}}.\tag{CL9.8}$$

![[Tropical OLR Contrast.svg|620]]
*Figure CL9.4 (after M&P Fig. 4.27). Editable version: [[Tropical OLR Contrast.excalidraw]].*

> [!intuition] Infrared goggles
> Look at the Earth through infrared goggles: cold things look dark, warm things bright. A thundercloud top is a cold lid over the warm ground: dark. The cloudless desert shows the hot ground directly: bright. That is why "OLR low" is used operationally to find the tropical convection (the ITCZ appears as a dark band: [[Intertropical Convergence Zone]]).

> [!pitfall] The ground does not radiate 459 W m⁻² to space even in clear sky
> The book's "radiation from the warm surface" is the idealisation $\varepsilon=1$. In reality water vapour and CO₂ absorb part of the surface emission even in a cloud-free sky: the global mean OLR is 240 W m⁻² against $\sigma(288)^4=390$ W m⁻², i.e. an **effective emissivity of $\approx0.62$**, the 0.6 used in the multiple-steady-state model of [[CL04 Feedback and Multiple Steady States]]. The *contrast* between cold cloud tops and the warm surface survives.

> [!example] Worked example: reading OLR as a temperature
> A pixel with OLR = 150 W m⁻² has brightness temperature $(150/\sigma)^{1/4}=226.8$ K: a deep cloud top, convection under way. A pixel with OLR = 280 W m⁻² has $T=265$ K: clear sky (or low warm cloud) over a hot surface whose emission is partly absorbed by water vapour. Using §4.2, 227 K on the moist adiabat of a 300 K surface corresponds to a height of ≈13 km.

---

## 6. When does convection happen?
<span class="scope-taught">taught</span> *Suhas notes p.21; M&P p.56*

Convection needs a **warm surface relative to the environmental air above**. Two routes:

1. **Warm the surface**, e.g. solar heating of the ground: *afternoon convection*, strongest in summer and above all in the tropics, where deep convection is very common. (This is the surface that, in the diurnal model of [[CL03 Radiation and Planetary Energy Balance]], peaks in the afternoon.)
2. **Cool the air aloft**: cold air advected over a warm surface, as when mid-latitude **thunderstorms** accompany the passage of a cold front.

In mid-latitudes *shallow* convection (cumulus) is frequent; *deep* convection (heavy rain, often thunderstorms) is **intermittent**. In the tropics deep convection is quasi-continuous, which is why the tropics are in RCE.

> [!intuition] Fire needs fuel, oxygen and a spark
> A convective storm needs: an *unstable profile* (fuel: $\Gamma$ steeper than the relevant adiabat), *moisture* (oxygen: latent heat release is the engine of deep convection, §4.2) and a *trigger* (spark: surface heating, fronts, convergence, mountains). The two routes above are two ways of getting the first ingredient.

> [!extra-book]+ 🟡 Extra (book): the trigger and the level of free convection
> A parcel lifted by a front or mountain cools dry-adiabatically until it saturates (the lifting condensation level), then along the moist adiabat; if it reaches a level warmer than its environment (the **level of free convection**, W&H Fig. 3.16, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=108|p.91]]) it rises on its own. Until then lifting must do the work; the energy "debt" before the LFC is why convection often waits for a trigger. See [[Atmospheric Stability]].

---

## 7. Putting numbers on the stability
<span class="scope-extra-book">extra · book</span> *M&P Problem 2 ([[climate-suhas merged.pdf#page=2|p.57]]); Fig. 4.9 is not in your pages*

The AI notes on the book ([[climate_book_notes.pdf#page=5|book-notes p.5]]) solve Problem 2 with **typical** numbers because Fig. 4.9 (the observed temperature profile) is not in your excerpt. Summary of the three quantities and how to compute each from *any* profile:

| quantity | method | typical value |
|---|---|---|
| tropospheric lapse rate $\Gamma$ | $\Delta T/\Delta z$ between ground and tropopause | 6.5 K km⁻¹ vs $\Gamma_d$ = 9.8 |
| pressure scale height | $H=RT_0/g$ with $T_0$ the mean over 700–300 hPa | $287\times255/9.81=7.5$ km |
| buoyancy period | $2\pi/N$, $N^2=(g/T)(\Gamma_d-\Gamma)$ | $N=0.011$ s⁻¹, ≈ 9–10 min |

Full worked solutions are in *Practice*.

---

## 8. Convection in a tank: the burrowing mixed layer
<span class="scope-extra-book">extra · book</span> *M&P §4.2.4 (GFD Lab II), Fig. 4.28, Eq. 4-31, Problem 3 ([[climate-suhas merged.pdf#page=2|p.57]])*

> [!extra-book]+ 🟡 Extra (book): the laboratory analogue of convective adjustment
> A tank of water, linearly stratified, $T_{\rm init}=T_0+T_z\,z$ ($T_z>0$: warmer above, stable), is heated from below by a pad delivering a flux $H$. Convection starts at the bottom and mixes a layer of depth $h$ to a **uniform** temperature that "joins on" to the stratification above (Fig. 4.28): the convective layer *burrows* upward, exactly as the radiative profile of §1 is "returned to the neutral state" by convection. The horizontally averaged heat equation is $\rho c_p\,\mathrm dT/\mathrm dt=H/h$ (Eq. 4-31).
> *Joins on* means the mixed layer has the initial temperature at its top: $T(t)=T_0+T_zh(t)$, so $\mathrm dT/\mathrm dt=T_z\,\mathrm dh/\mathrm dt$. Then
> $$\rho c_p\,T_z\,h\,\frac{\mathrm dh}{\mathrm dt}=H\ \Longleftrightarrow\ \boxed{\frac{\rho c_pT_z}{2}\frac{\mathrm d(h^2)}{\mathrm dt}=H}\ \Rightarrow\ h=\Big(\frac{2Ht}{\rho c_pT_z}\Big)^{1/2},\quad T-T_0=\Big(\frac{2HT_z\,t}{\rho c_p}\Big)^{1/2}.\tag{CL9.9}$$
> Both depth and temperature grow like $\sqrt t$: fast at first, then slower. **Energy check:** heat added per area is $Ht=\rho c_p\int_0^h[T-T_{\rm init}(z)]\,\mathrm dz=\rho c_pT_z\int_0^h(h-z)\,\mathrm dz=\tfrac12\rho c_pT_zh^2$, the same result.

![[fig_cl09_lab_convection.png|760]]
*Figure CL9.5. Illustrative numbers ($T_z=50$ K/m, $H=500$ W/m², water): after 10 min the mixed layer is 5.4 cm deep and 2.7 K warmer; four times as long gives only twice the depth. Script `fig_cl09_lab_convection.py`.*

> [!intuition] Why does it slow down? A bulldozer on a slope
> Each new layer the mixed region swallows is *colder* than the layer on top of the mixed region yet needs to be brought up to the new, warmer mixed temperature. As the mixed layer deepens, more water must be heated per unit of extra depth, so the same heating moves the boundary more slowly. Equivalent: the energy needed to mix to depth $h$ grows as $h^2$.

> [!extra-beyond]- 🔵 Extra (beyond): the same law runs the daytime boundary layer
> In the atmosphere, daytime heating of the ground by a sensible heat flux $H$ makes a convective boundary layer that burrows up into the stable *residual layer* left over from the previous night: $h\approx(2Ht/\rho c_pT_z)^{1/2}$ (the "encroachment" model). With $H=200$ W m⁻², $\rho=1.2$ kg m⁻³, $T_z=3$ K km⁻¹ (stable residual layer): $h=630$ m after 1 h, 1.1 km after 3 h, 1.5 km after 6 h: the observed order of magnitude of mid-day boundary-layer depths. (This idealisation ignores entrainment at the top, which adds ~20 % to the heat budget.)

---

## 9. What RCE explains, and what it leaves out
<span class="scope-extra-book">extra · book</span> *W&H §10.1, §10.3* · <span class="scope-extra-beyond">extra · beyond</span> *§9.5*

### 9.1 Why 6.5 K/km, and what the tropopause is
<span class="scope-extra-book">extra · book</span> *W&H §10.1, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=438|p.421]]*

> [!extra-book]+ 🟡 Extra (book): Wallace & Hobbs on the lapse rate and the tropopause
> - The tropopause (≈10 km, a temperature minimum) corresponds roughly to the level of **unit optical depth for outgoing longwave radiation**. Below it, repeated absorption and re-emission make radiative transfer an inefficient way to dispose of the energy absorbed at the ground, so **convection and large-scale motions** maintain the lapse rate near 6.5 K km⁻¹.
> - The observed lapse rate is stable even with respect to the *saturated* adiabat: most of the troposphere is slowly **subsiding clear air** that loses energy by radiation as it sinks (so its equivalent potential temperature falls), and only parcels that have recently been in the boundary layer rise rapidly in cloud updrafts ("hot towers", W&H Fig. 10.3).
> - RCE models mimic the large-scale effects by *artificially limiting the lapse rate*: Fig. 10.4 shows pure RE, dry-adiabatic adjustment and 6.5 K/km adjustment, the three curves of my Fig. CL9.2. The tropospheres of **Mars and Venus** and the **solar photosphere** (convective below, radiative above) can be modelled in a similar way.

### 9.2 The greenhouse "paradox"
> [!extra-book]+ 🟡 Extra (book): greenhouse gases cool the air yet warm the surface (W&H p.421)
> Greenhouse gases make the *atmosphere* lose energy radiatively (net longwave cooling of the troposphere), yet they make the *surface* warmer. RCE resolves this: in pure RE a transparent-to-sunlight atmosphere would neither gain nor lose energy radiatively; in RCE the troposphere is **warmer than radiative equilibrium** (Fig. CL9.2: blue to the right of orange above 2.6 km), kept warm by latent-heat release and sensible-heat transport. Because it is warm, it emits *more* infrared than it absorbs, so it cools radiatively, and the convective heat flux from the ground replaces what it loses.

### 9.3 RCE and climate sensitivity
> [!extra-book]+ 🟡 Extra (book): what RCE models give for doubled CO₂ (W&H §10.3, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=474|p.457]])
> One-dimensional RCE models give a forcing $F=3.7$ W m⁻² for doubling CO₂ and a surface warming of $0.96$ K without feedbacks ($=3.7\times0.266$, [[Planck Sensitivity]]); including the water-vapour feedback at fixed relative humidity roughly doubles it, and with ice-albedo feedback as well the feedback factor rises to ≈0.6, giving ≈2.5 K ([[Climate Feedback Factor]], [[CL04 Feedback and Multiple Steady States]]). The convective part of RCE is what makes the *lapse-rate feedback* negative: if the surface warms, the moist-adiabatic troposphere warms *more* aloft (because $\Gamma_s$ decreases with temperature, Fig. CL9.3), which radiates more to space (W&H state this in footnote 3 to Fig. 10.4, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=439|p.422]]: if $\Gamma$ stays close to $\Gamma_s$ as the surface warms, the upper troposphere warms faster than the surface). They also note that the **stratosphere** is close to radiative equilibrium: raising CO₂ *cools* it.

### 9.4 Back to CL08 and forward to CL10–11
In [[CL08 Greenhouse Models]] a layer model gave $T_s$ without any vertical transport; RCE shows that **a greenhouse atmosphere is a convecting one**. Forward: the tropics are in near-RCE, so the *vertical* structure here is the vertical branch of the tropical circulation: air rises in convective towers (low OLR), spreads poleward aloft and sinks in the subtropics ([[Hadley Cell]], [[CL11 Mean Meridional Circulation and Angular Momentum]]); the cold-cloud-top picture of §5 is the same picture as the ITCZ of [[Intertropical Convergence Zone]].

### 9.5 Limits and history of the idea
<span class="scope-extra-beyond">extra · beyond</span>

> [!extra-beyond]- 🔵 Extra (beyond): Manabe, Strickler and the limits of one dimension
> The radiative-convective model was introduced by Manabe & Strickler (1964) and used by Manabe & Wetherald (1967) to compute the response of surface temperature to CO₂ and water vapour: it was the first quantitative demonstration of the warming from rising CO₂ and of the water-vapour feedback. Its assumptions are exactly those of this chapter: radiation + a convective-adjustment lapse rate. **What it leaves out:** horizontal transport (the tropics export heat to the poles: [[Poleward Energy Transport]]); clouds; a lapse rate that is *prescribed* rather than computed from moist convection; a surface that is a single heat reservoir; the diurnal and seasonal cycles. A convecting planet with these missing pieces is the subject of the next chapters and of full climate models. Pure "radiative–convective equilibrium" with no large-scale circulation is also a standard idealised experiment in modern cloud-resolving simulations (Wing et al. 2018).

---

## Map of this chapter
> [!connection] How CL09 connects
> **Builds on:** [[CL08 Greenhouse Models]] (layer models and the discontinuity) · [[CL06 Hydrostatic Balance and Vertical Structure]] (hydrostatic balance, scale height) · [[CL05 Thermodynamic State of the Atmosphere]] (ideal gas law, $R_d$) · [[CL04 Feedback and Multiple Steady States]] (effective emissivity 0.6, feedback factors) · [[CL03 Radiation and Planetary Energy Balance]] ($T_e$, diurnal heating).
> **Leads to:** [[CL10 Global Energy Balance and Meridional Structure]] (OLR maps, net radiation) · [[CL11 Mean Meridional Circulation and Angular Momentum]] (the Hadley cell as the circulation of tropical RCE) · [[CL14 Observed Winds - Jets, Trades and the ITCZ]].
> **Concepts introduced:** [[Lapse Rate]] · [[Dry Adiabatic Lapse Rate]] · [[Atmospheric Stability]] · [[Convection]] · [[Convective Adjustment]] · [[First Law of Thermodynamics]] · [[Adiabatic Process and Potential Temperature]] · [[Clausius-Clapeyron Relation]].
> **Other subjects:** thermodynamics ([[Thermodynamics - Course Map]]), stability and oscillation maths ([[Fixed Points and Linear Stability]], [[Linearisation and Sensitivity]]), internal gravity waves ([[Waves - Course Map]]), Venus's runaway greenhouse and early-Earth climate ([[Evolution of Earth and Life - Course Map]]), regime shifts ([[Bistability and Tipping Points]]).

> [!connection] Thermodynamics
> Every step of §2 is a statement of the first law applied to a moving air parcel; §4.2 is the Clausius–Clapeyron relation made meteorological. These two notes are the climate-side halves of the [[Thermodynamics - Course Map]]: [[First Law of Thermodynamics]], [[Clausius-Clapeyron Relation]].

> [!connection] Dynamical systems
> The buoyancy equation $\ddot{\delta z}=-N^2\delta z$ *is* the linear stability analysis of [[Fixed Points and Linear Stability]]: $N^2>0$ gives oscillation (a centre), $N^2<0$ exponential escape (a saddle). The bistability of [[Bistability and Tipping Points]] arises when a *nonlinear* feedback makes the sign change with the state; the convective threshold $\Gamma=\Gamma_d$ is a bifurcation of the same kind (the onset of overturning).

---

## Summary
> [!summary] Cheat-sheet
> - **Pure radiative equilibrium** (grey): $T^4=\tfrac12T_e^4(1+D\tau)$; skin $T_e/2^{1/4}=214$ K; ground jump $\sigma(T_g^4-T_a^4)=F/2$; near-ground lapse rate ≫ $\Gamma_d$ ⇒ **unstable**.
> - $\Gamma_d=g/c_p=9.8$ K/km; $\theta=T(p_0/p)^\kappa$, $\kappa=0.286$; stable ⇔ $\partial\theta/\partial z>0$ ⇔ $\Gamma<\Gamma_d$.
> - $N^2=\dfrac g{T}(\Gamma_d-\Gamma)$; $N\approx0.011$ s⁻¹, period ≈ 9–10 min in the troposphere.
> - **RCE** = convective (near-neutral) below $z_T$ + radiative above. Convection *cools the surface, warms the free troposphere*, same OLR.
> - Tropics: neutral to **moist** convection (constant moist potential temperature); $\Gamma_s$: 4 (warm, moist) → 9 K/km (cold); observed mean ≈ 6.5 K/km.
> - OLR: $(300/220)^4=3.5$: cold deep-convective cloud tops ⇒ **low OLR**; clear dry subtropics ⇒ **high OLR**.
> - Convection needs a warm surface relative to the air above: heat the ground (afternoon, tropics) or cool the air aloft (cold fronts). Mid-latitudes: shallow common, deep intermittent; tropical structure reaches mid-latitudes through large-scale systems.
> - Lab: $h,\,T-T_0\propto\sqrt t$. Greenhouse effect ≈ lapse rate × emission height.

> [!summary] Quiz checklist (each item checked against the book text, not only the AI notes)
> 1. **RCE is two regimes**, not "convective everywhere": convective below $z_T$, radiative above. ✔ M&P p.56.
> 2. The **discontinuity is at the ground** (ground warmer than the air above), and the resulting profile is unstable because its lapse rate exceeds the adiabatic one. ✔
> 3. Neutral state in the *moist* tropics = constant **moist** potential temperature, not the dry one. ✔
> 4. Two routes to convection (warm surface; cool air aloft); **thunderstorms along cold fronts** are the mid-latitude example; deep convection is intermittent in mid-latitudes. ✔
> 5. Tropical structure reaches mid-latitudes via **large-scale systems** (Chapter 8), not local convection. ✔
> 6. OLR ratio: $(300/220)^4\approx3.5$; low OLR = cold cloud tops. ✔
> 7. $N^2=(g/T_E)(\mathrm dT_E/\mathrm dz+\Gamma_d)$: **sign:** $N^2>0$ stable. Check your sign of $\Gamma$ (the problem uses $\mathrm dT_E/\mathrm dz$, negative in the troposphere). ✔
> 8. Lab: the *convective layer* depth and its temperature rise grow as $\sqrt t$ (Problem 3). ✔
> 9. **Trap:** Fig. 3.4, Fig. 4.9 and Eq. 4-22 are not in your pages; numbers for Problem 2 are "typical" values (6.5 K/km, $H\approx7.5$ km, ~9–10 min), not read off a figure.
> 10. **Trap:** don't use $\Gamma_d$ for cloudy (saturated) air; use $\Gamma_s$ (4–9 K/km).

---

## Practice
<span class="scope-extra-book">extra · book</span> *Problems 1–3 are M&P §4.9 (p.57)* · <span class="scope-extra-beyond">extra · beyond</span> *Problems 4–10*

1. **(M&P 1)** Show that $N^2=\dfrac g{T_E}\Big(\dfrac{\mathrm dT_E}{\mathrm dz}+\Gamma_d\Big)$.
2. **(M&P 2)** From a tropospheric temperature profile (use $T=288$ K at the ground, 215 K at 11 km if Fig. 4.9 is not to hand): (a) estimate $\Gamma$ and compare with $\Gamma_d$; (b) estimate $H=RT_0/g$ for $T_0=$ the mean of the 700–300 hPa layer; (c) estimate the period of buoyancy oscillations in mid-troposphere.
3. **(M&P 3)** In the tank experiment $\rho c_p\,\mathrm dT/\mathrm dt=H/h$. Assuming the mixed layer is homogeneous and "joins on" to the initial stratification $T_z$, show $\dfrac{\rho c_pT_z}{2}\dfrac{\mathrm d}{\mathrm dt}h^2=H$. (a) Solve and show $h$ and $T-T_0$ grow as $\sqrt t$. (b) Is that consistent with the observed plot of temperature against time?
4. Compute $\theta$ for $T=300$ K at 900 hPa and for $T=260$ K at 600 hPa. Which parcel is stabler relative to the other? Is a layer between them stable?
5. Derive (CL9.1) and (CL9.2) and evaluate $T_g$, the air temperature just above the ground and the jump for $\tau_s=1$ (use $T_e=254.6$ K, $D=1.66$).
6. **Convective adjustment by hand.** Two layers of equal mass: lower at 900 hPa, 300 K; upper at 700 hPa, 275 K. Adjust to exactly neutral (dry adiabat) conserving $\sum T$ (equal masses).
7. **Greenhouse = $\Gamma z_e$.** With $\Gamma=6.5$ K km⁻¹ and $T_s=288$, $T_e=255$: find $z_e$. How much does $T_s$ change if the emission level rises by 150 m? Compare with $3.7/(4\sigma T_e^3)$.
8. **OLR.** Brightness temperatures for OLR = 150 and 280 W m⁻². What fraction of the 300 K surface emission reaches space in a clear sky with OLR = 280?
9. Compute $\Gamma_s$ at 15 °C, 900 hPa from (CL9.7) (use $e_s$ from Clausius–Clapeyron or Bolton's formula) and compare with $\Gamma_d$.
10. **Conceptual.** (a) Why does adding convection *cool* the surface and *warm* the free troposphere at unchanged OLR? (b) Why is the observed lapse rate stable to saturated displacement even though the tropics are convecting? (c) Why can $\Gamma_s<\Gamma<\Gamma_d$ still produce storms?

> [!example]- Solutions
> **1.** $\theta=T(p_0/p)^\kappa\Rightarrow\ln\theta=\ln T+\kappa\ln p_0-\kappa\ln p$. Differentiate in $z$: $\partial_z\ln\theta=\partial_z\ln T-\kappa\,\partial_z\ln p$. Hydrostatic + ideal gas: $\partial_zp=-\rho g=-pg/(RT)$ so $\partial_z\ln p=-g/(RT)$. Then $-\kappa\,\partial_z\ln p=(R/c_p)\,g/(RT)=g/(c_pT)=\Gamma_d/T$ and $\partial_z\ln\theta=(\partial_zT+\Gamma_d)/T$. The parcel keeps $\theta_p$, the environment's $\theta_E$ changes by $(\mathrm d\theta_E/\mathrm dz)\delta z$; the relative density deficit is $\delta\theta/\theta_E$ and the restoring acceleration $-g\,(\mathrm d\theta_E/\mathrm dz)\,\delta z/\theta_E=-N^2\delta z$ with $N^2=g\,\mathrm d\ln\theta_E/\mathrm dz=\frac g{T_E}\big(\frac{\mathrm dT_E}{\mathrm dz}+\Gamma_d\big)$. ∎
> **2.** (a) $\Gamma=(288-215)/11=6.6$ K km⁻¹ vs $\Gamma_d=9.8$: the troposphere is stable to dry displacements (smaller because of latent heating and large-scale subsidence, §9.1). (b) With $T_0\approx255$ K: $H=287\times255/9.81=7.46$ km. (c) $N^2=\frac{9.81}{260}\,(9.8-6.6)\times10^{-3}=1.2\times10^{-4}$ s⁻², $N=0.011$ s⁻¹, period $2\pi/N\approx570$ s $\approx9.5$ min. (The book's Fig. 4.9 would give slightly different numbers; the method is the point.)
> **3.** $T(t)=T_0+T_zh(t)$ since the mixed layer joins the stratification at its top; so $\mathrm dT/\mathrm dt=T_z\dot h$ and $\rho c_pT_zh\dot h=H$, i.e. $\frac{\rho c_pT_z}{2}\frac{\mathrm d}{\mathrm dt}h^2=H$. (a) $h(0)=0$: $h^2=2Ht/(\rho c_pT_z)$, so $h=(2Ht/\rho c_pT_z)^{1/2}$ and $T-T_0=T_zh=(2HT_zt/\rho c_p)^{1/2}$: both $\propto\sqrt t$ (a parabola on its side; steep at first, then flattening). (b) The expected observation is a straight line when plotted against $\sqrt t$; the observed-data plot is not in your pages. Energy check: $Ht=\rho c_p\int_0^h(T-T_{\rm init})\,\mathrm dz=\frac12\rho c_pT_zh^2$ ✓.
> **4.** $\theta_1=300\,(1000/900)^{0.286}=309.2$ K; $\theta_2=260\,(1000/600)^{0.286}=300.9$ K. $\theta$ *decreases* with height from 900 to 600 hPa, so the layer is **unstable**: the lower parcel, brought to 1000 hPa, would be warmer. Cross-check with lapse rates: the thickness is $\Delta z\approx(R\bar T/g)\ln(900/600)=8.2\ \mathrm{km}\times0.405=3.3$ km, so $\Gamma\approx40/3.3=12$ K km⁻¹ $>\Gamma_d$ ✓.
> **5.** Derivation in the §1 box. $\tau_s=1$: $T_g=254.6\,(1+0.83)^{1/4}=296.1$ K; $T_a=254.6\,(\tfrac12(1+1.66))^{1/4}=254.6\times1.0740=273.4$ K; jump $=296.1-273.4=22.7$ K (numerical column: 23.6 K at 60 m, lapse rate included). Note that $\sigma(T_g^4-T_a^4)=\tfrac12\sigma T_e^4$ in both cases.
> **6.** $r=(900/700)^{0.286}=1.0745$. Neutral: $T_{\rm low}=rT_{\rm up}$; $\sum T=575$ ⇒ $T_{\rm up}=575/(1+1.0745)=277.2$ K, $T_{\rm low}=297.8$ K. (Before: $300>1.0745\times275=295.5$, unstable.) The lower layer cools by 2.2 K, the upper warms by 2.2 K: convection moved heat upward.
> **7.** $z_e=(288-255)/6.5=5.1$ km. $\Delta T_s=6.5\times0.15=0.98$ K. $3.7/(4\sigma\,255^3)=0.99$ K: the two views agree: the no-feedback CO₂-doubling forcing is the same as raising the emission level by ~150 m.
> **8.** $T=(150/\sigma)^{1/4}=226.8$ K; $(280/\sigma)^{1/4}=265.1$ K. Fraction $280/459=0.61$ of the surface emission (the rest is absorbed and re-emitted by the atmosphere).
> **9.** $T=288.15$ K, $p=900$ hPa: $e_s=611.2\exp\!\big[17.67\times15/(288.15-29.65)\big]=1704$ Pa, $r_s=\varepsilon e_s/(p-e_s)=0.622\times1704/88296=0.0120$, $L=2.4655\times10^6$ J kg⁻¹. Numerator $g\,(1+Lr_s/R_dT)=9.81\,(1+0.358)=13.32$; denominator $c_p+L^2r_s\varepsilon/(R_dT^2)=1004+1904=2908$. So $\Gamma_s=13.32/2908=4.58\times10^{-3}$ K m⁻¹ $=\mathbf{4.6}$ K km⁻¹, less than half of $\Gamma_d$ (script check: 4.58).
> **10.** (a) Convection moves heat from the ground into the troposphere without changing the net flux: the ground loses energy by sensible and latent heat flux (so it cools), the air gains it (so it warms); the OLR is set by the energy balance, not by where the heat sits. (b) Because most of the troposphere is slowly subsiding, radiatively cooled clear air; only a small area of moist updrafts reaches saturation-adiabatic neutrality; the *mean* profile is then stabler than the moist adiabat (W&H p.421). (c) Conditional instability (§2.4 pitfall): unstable only for *saturated* parcels that are first lifted to the level of free convection.

---

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | radiative equilibrium has a ground discontinuity (statement) | [[suhas notes.pdf#page=16\|suhas notes pp.16–21]]; [[climate-suhas merged.pdf#page=1\|M&P §4.7 p.56]] | taught |
> | static-stability criterion vs $\Gamma_d$ (used, not derived) | [[suhas notes.pdf#page=20\|suhas notes p.20]] | taught |
> | convective adjustment; RCE (convective below, radiative above, $z_T$) | [[suhas notes.pdf#page=20\|suhas notes p.20–21]]; M&P p.56 | taught |
> | tropical troposphere neutral to moist convection; mid-latitudes | suhas notes p.21; M&P p.56 | taught |
> | OLR contrast $(300/220)^4$, Fig. 4.27 | suhas notes p.21; M&P p.56 | taught |
> | two routes to convection | suhas notes p.21; M&P p.56 | taught |
> | $\Gamma_d=g/c_p$ derivation, potential temperature | W&H §3.4.2–3.4.3, pp.77–78 | extra/book |
> | $N^2$ formula and derivation (Problem 1), parcel oscillation | M&P p.57; W&H §3.6.1 p.89 (Eq. 3.73–3.75) | extra/book |
> | moist adiabat, latent heat, Clausius–Clapeyron, conditional instability | W&H §3.5.2–3.5.4 p.84, §3.7.3 p.97, §3.6.3 p.91 | extra/book |
> | Problem 2 numbers | M&P p.57; [[climate_book_notes.pdf#page=5\|book-notes p.5]] (typical values) | extra/book |
> | GFD Lab II, Eq. 4-31, Problem 3 | M&P p.57 (Fig. 4.28, §4.2.4) | extra/book |
> | tropopause as unit optical depth; 6.5 K/km; paradox; Mars/Venus; RCE sensitivity | W&H §10.1 p.421–422 (Fig. 10.4), §10.3 p.457 | extra/book |
> | grey-gas radiative equilibrium: (CL9.1)–(CL9.2), skin temperature, jump, ground lapse rate | derived here; checked numerically (`cl09_rce.py`) | extra/beyond |
> | numerical RE/RCE column and table | `scripts/cl09_rce.py`, `fig_cl09_re_vs_rce.py` | extra/beyond |
> | greenhouse = $\Gamma z_e$ (pinning argument) | derived here (cf. W&H p.421) | extra/beyond |
> | boundary-layer encroachment; Manabe–Strickler history | standard results; Manabe & Strickler (1964); Manabe & Wetherald (1967) | extra/beyond |
>
> **Dropped as redundant:** the repetition of the radiative-discontinuity argument in Suhas notes §6.3 (multi-layer model) and §7.1 (RCE intro) is merged into §1; the book notes' separate restatement of "RCE" in §1.1 and the summary table is merged into §3.
> **Corrections / cautions:** (i) the AI notes call the tropical neutrality "moist-adiabatic", the book says "constant moist potential temperature" (equivalent). (ii) The book's "radiation from the warm surface" in clear sky ignores greenhouse absorption (§5 pitfall). (iii) Figures 3.4, 4.9 and Eq. 4-22 of M&P are outside your excerpt.

> [!provenance]- Slide evidence: the only convective picture in the photographed lectures
> ![[22nd Oct.pdf#page=6&height=300]]
> *22 Oct, p6: a convective tower with low-level convergence (the ITCZ), shown without convection theory; it returns in [[CL14 Observed Winds - Jets, Trades and the ITCZ]].*

**References.** Marshall, J. & Plumb, R. A. (2008) *Atmosphere, Ocean and Climate Dynamics*, §4.7–4.9 · Wallace, J. M. & Hobbs, P. V. (2006) *Atmospheric Science*, §3.4–3.7, §10.1, §10.3 · Manabe, S. & Strickler, R. F. (1964) *J. Atmos. Sci.* 21, 361 · Manabe, S. & Wetherald, R. T. (1967) *J. Atmos. Sci.* 24, 241 · Frierson, D. M. W., Held, I. M. & Zurita-Gotor, P. (2006) *J. Atmos. Sci.* 63, 2548 (grey-gas optical depth) · Wing, A. A. et al. (2018) *Geosci. Model Dev.* 11, 793 (RCE model intercomparison) `[verify]` · Bolton, D. (1980) *Mon. Wea. Rev.* 108, 1046 (saturation vapour pressure).
