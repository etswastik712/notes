---
title: CL13 Horizontal Motion - Geostrophic Balance and Friction
aliases: [CL13, Geostrophic balance chapter, Horizontal momentum equations]
subject: climate
type: chapter
chapter: 13
part: IV
scope: [taught, extra-book, extra-beyond]
by: [suhas-pre, suhas-post]
status: draft
prereq: ["[[CL12 Rotating Frames and the Coriolis Force]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/suhas-pre, src/suhas-post, status/draft]
---
# CL13 · Horizontal Motion: Geostrophic Balance and Friction

◀ [[CL12 Rotating Frames and the Coriolis Force]] · [[Climate - Course Map|Course Map]] · [[CL14 Observed Winds - Jets, Trades and the ITCZ]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!note] Neena 2025 cross-reference (2026-11-13)
> The 2025 course (Neena) covered this ground too: Neena 2025 **L14–L17** (forces controlling atmospheric motion) (`earth-and-climate/climate/lecture-notes-slides/ec2113_neena`, PDFs listed in [[Climate - Course Map]]). This chapter is built from **this year's** Argha/Suhas material, which stays primary here. In the earlier new-source comparison (PROGRESS, 2026-11-07) those lectures were judged to **repeat** this chapter's content; **no Neena-specific content has been added to this chapter** beyond this pointer, and it has **not been re-read line by line** for differences (L14-L17). Where a Neena lecture was found to add material, it is added and labelled in the chapter that needed it (for example CL10 §7).

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 forces on a parcel: pressure-gradient force, gravity (Suhas pre-midsem)
> - horizontal momentum equations with Coriolis and friction, $f=2\Omega\sin\varphi$ (22 Oct p9–12)
> - §3 friction and the planetary boundary layer, free atmosphere vs near surface (22 Oct p8, 13–15)
> - §4 geostrophic balance (22 Oct p16–18)
> - §5 flow around highs and lows (22 Oct p19–22)
> - §6 cyclonic/anticyclonic flow, NH vs SH, cyclones (22 Oct p23–24)
>
> 🟡 **Extra · book**
> - Rossby number and the scale argument (M&P §7.1, p.110, in §2)
> - Buys-Ballot's law, "river banks" picture, isobar-spacing statement (M&P pp.111–112, in §4)
> - pressure-coordinate form, non-divergence, streamfunction $\psi_g=gz/f$ (M&P §7.1.1, in §4.5)
> - synoptic chart, 24 m/s check, Rossby-number map (M&P §7.1.2, in §4.3)
> - three-way friction balance and angle $\psi$, gradient wind (Wallace & Hobbs §7.2.5–7.2.6, in §3.3 and §6)
>
> 🔵 **Extra · beyond**
> - friction-induced convergence and vertical-velocity estimate (§5)
> - gradient-wind numbers, cyclostrophic limit, hurricane example (§6)
> - Ekman layer solution (§7)
> - geostrophy near the equator (§4.4)
> - Rossby-number chart (§2)

> [!key] After this chapter you can
> - derive the **pressure-gradient force** from a fluid box and write the horizontal equations of motion $\mathrm Du/\mathrm Dt=-\frac1\rho\partial_xp+fv+F_x$, $\mathrm Dv/\mathrm Dt=-\frac1\rho\partial_yp-fu+F_y$,
> - use the **Rossby number** to say when rotation controls the flow, and why the geostrophic wind is the right zeroth-order description of large-scale winds,
> - derive and use **geostrophic balance**, state Buys-Ballot's law, and compute wind speeds from isobar or height-contour spacing,
> - explain how **friction** turns and slows the surface wind, and hence why surface flow spirals into lows and out of highs, with the consequences for weather,
> - say which way the wind circulates round highs and lows in each hemisphere, and where geostrophy breaks down (equator, strong curvature, boundary layer).

## 1. Forces on an air parcel and the horizontal equations of motion
<span class="scope-taught">taught</span> *Suhas pre-midsem notes pp.12–13 (pressure-gradient force, gravity) · 22 Oct p9–12 (momentum equations with Coriolis and friction)*

[[CL12 Rotating Frames and the Coriolis Force|Chapter 12]] ended with Newton's law in the rotating frame, (CL12.4). To apply it we need the real forces acting on a parcel. They come in two families: **body forces**, proportional to the mass (gravity), and **surface forces**, acting across the parcel's boundary (pressure and friction).

### 1.1 The pressure-gradient force
<span class="scope-taught">taught</span> *Suhas pre-midsem notes p.12*

> [!intuition] Only differences push
> Stand at the bottom of a swimming pool. Water presses on you from every side with enormous force, yet you are not accelerated: the pushes cancel. If you stand in a river whose water is deeper upstream, the push on your upstream side is slightly bigger than on your downstream side and you feel a net shove. Air is the same: a uniform pressure of 1000 hPa moves nothing; it is the **spatial change** of pressure across a parcel that pushes it, from high toward low.

Take a box of air of size $\delta x\,\delta y\,\delta z$ centred at $(x_0,y_0,z_0)$ where the pressure is $p_0$. Expand $p$ to first order. On the face at $x_0+\delta x/2$ the pressure is $p_0+\tfrac12\frac{\partial p}{\partial x}\delta x$ and the force it exerts (area $\delta y\,\delta z$) points in $-x$; on the face at $x_0-\delta x/2$ the pressure is $p_0-\tfrac12\frac{\partial p}{\partial x}\delta x$ and the force points in $+x$:

$$F_x=-\Big(p_0+\tfrac12\tfrac{\partial p}{\partial x}\delta x\Big)\delta y\,\delta z+\Big(p_0-\tfrac12\tfrac{\partial p}{\partial x}\delta x\Big)\delta y\,\delta z=-\frac{\partial p}{\partial x}\,\delta x\,\delta y\,\delta z .$$

The $p_0$ terms cancel: **a uniform pressure exerts no net force**. Dividing by the mass $m=\rho\,\delta x\,\delta y\,\delta z$:

$$\boxed{\frac{\mathbf F_{\rm pg}}{m}=-\frac1\rho\nabla p}\tag{CL13.1}$$

The force per unit mass points from high to low pressure, its magnitude is the pressure *gradient* divided by density, and the absolute value of $p$ does not appear ([[Pressure Gradient Force]]). Its vertical component, combined with gravity, gives hydrostatic balance ([[CL06 Hydrostatic Balance and Vertical Structure]]).

> [!example] How big is it?
> Surface weather charts are drawn with isobars every 4 hPa. If they are 300 km apart at mid-latitude, $|\nabla p|=400\ \mathrm{Pa}/3\times10^5\ \mathrm m=1.33\times10^{-3}$ Pa m⁻¹ and, with $\rho=1.2$ kg m⁻³, the force per unit mass is $1.1\times10^{-3}$ m s⁻², about $10^{-4}\,g$. It is a tiny force, but it acts on the air for days over thousands of kilometres.

### 1.2 Gravity and the other forces
<span class="scope-taught">taught</span> *Suhas pre-midsem notes p.12*

True gravity per unit mass is $\mathbf g^*=-\dfrac{GM}{r^2}\hat{\mathbf r}$ (Newton). On the rotating Earth it merges with the centrifugal term into the effective gravity $\mathbf g$ of [[Centrifugal Force and Effective Gravity]]. Friction $\mathbf F$ is a surface force that depends on the shear and is concentrated near the ground (§3). Coriolis is the apparent force of the rotating frame ([[Coriolis Force]]).

### 1.3 The horizontal momentum equations
<span class="scope-taught">taught</span> *22 Oct p9–12*

Start from (CL12.4) and write $\boldsymbol\Omega=(0,\Omega\cos\varphi,\Omega\sin\varphi)$ in local $(x\ \text{east},y\ \text{north},z\ \text{up})$ coordinates. The slides compute $2\boldsymbol\Omega\times\mathbf V$ as a determinant with $\mathbf V=(u,v,0)$, i.e. they **drop the vertical velocity** ([[22nd Oct.pdf#page=10|22 Oct, p10]]):

$$2\boldsymbol\Omega\times\mathbf V=2\Omega\begin{vmatrix}\hat{\mathbf i}&\hat{\mathbf j}&\hat{\mathbf k}\\0&\cos\varphi&\sin\varphi\\u&v&0\end{vmatrix}=2\Omega\big(-v\sin\varphi,\ u\sin\varphi,\ -u\cos\varphi\big).$$

Its horizontal components are $-2\Omega v\sin\varphi$ and $+2\Omega u\sin\varphi$; moving $-2\boldsymbol\Omega\times\mathbf V$ to the right-hand side gives $+fv$ and $-fu$ with the **Coriolis parameter** $f=2\Omega\sin\varphi$ ([[Coriolis Parameter]], and (CL12.5a–b) of chapter 12). Adding the pressure-gradient force and a frictional force $(F_x,F_y)$ ([[22nd Oct.pdf#page=12|22 Oct, p12]]):

$$\boxed{\frac{\mathrm Du}{\mathrm Dt}=-\frac1\rho\frac{\partial p}{\partial x}+fv+F_x,\qquad\frac{\mathrm Dv}{\mathrm Dt}=-\frac1\rho\frac{\partial p}{\partial y}-fu+F_y}\tag{CL13.2}$$

> [!intuition] What $+fv$ and $-fu$ do
> Ignore the pressure force and friction: $\dot u=fv$, $\dot v=-fu$. Then the velocity vector $(u,v)$ simply **rotates clockwise at angular rate $f$** (in the NH) without changing its length: a Coriolis-only parcel moves in an "inertial circle" of period $2\pi/f\approx17$ h at 45° (see [[Foucault Pendulum]] and chapter 12). So Coriolis is a steering wheel, not an engine: it can only turn the wind, never speed it up. Everything interesting in this chapter is what happens when the pressure force tries to accelerate the wind while the steering wheel keeps turning it.

> [!example] Why is the vertical equation different?
> In the vertical, the pressure-gradient force $-\rho^{-1}\partial p/\partial z\approx g$ almost exactly cancels gravity (hydrostatic balance). Large-scale vertical velocities are $w\sim1$ cm s⁻¹ varying over a day, so $\mathrm Dw/\mathrm Dt\sim10^{-2}/10^{5}=10^{-7}$ m s⁻², roughly $10^{-8}\,g$: negligible. The vertical component of Coriolis, $2\Omega u\cos\varphi\sim10^{-3}$ m s⁻², is also $10^{-4}\,g$ and is absorbed into the hydrostatic balance ([[Eotvos Effect]]). That is why only the horizontal equations (CL13.2) carry the dynamics.

## 2. Scales of motion and the Rossby number
<span class="scope-taught">taught</span> *Suhas pre-midsem notes p.14 (table of scales)* · <span class="scope-extra-book">extra · book</span> *M&P §7.1, p.110 (Rossby number)* · <span class="scope-extra-beyond">extra · beyond</span> *chart and numbers*

Which terms of (CL13.2) matter depends on the size of the motion. The pre-midsem notes tabulate the typical **horizontal scales** ([[Scales of Atmospheric Motion]]): molecular mean free path $10^{-7}$ m · minute eddies $10^{-2}$–$10^{-1}$ · dust devils 1–10 · gusts 10–$10^2$ · tornadoes $10^2$ · cumulonimbus $10^3$ · fronts and squall lines $10^4$–$10^5$ · hurricanes $10^5$ · synoptic cyclones $10^6$ · planetary waves $10^7$ m. Rotation becomes important only for the largest of these.

> [!extra-book]+ 🟡 Extra (book): the Rossby number
> Marshall & Plumb quantify this by comparing the acceleration term with the Coriolis term ([[Geostrophic_motion_Marshall_and_Plumb.pdf#page=1|M&P §7.1, p.110]]). Let the horizontal velocity scale be $U$, the horizontal length scale $L$ and the time scale $\mathcal T\sim L/U$. Then $\partial\mathbf u/\partial t\sim\mathbf u\!\cdot\!\nabla\mathbf u\sim U^2/L$, while the Coriolis term is $fU$. Their ratio is the **Rossby number**
> $$Ro=\frac{U^2/L}{fU}=\frac{U}{fL}.\tag{CL13.3}$$
> For synoptic systems in mid-latitudes, $U\sim10$ m s⁻¹, $L\sim10^6$ m, $\mathcal T\sim10^5$ s, $f\simeq1.03\times10^{-4}$ s⁻¹ (45°): the acceleration is $\sim10^{-4}$ m s⁻² against $fU\simeq10^{-3}$ m s⁻², so $Ro\approx0.1$. For the large-scale ocean circulation, $Ro\approx10^{-3}$ (M&P §9.3). When $Ro\ll1$ the acceleration is negligible and the momentum equation reduces to the balance
> $$f\,\hat{\mathbf z}\times\mathbf u+\frac1\rho\nabla p=0\qquad(\text{M\&P Eq. 7-2}).$$
> The "Rossby number" is named for Carl-Gustaf Rossby (1898–1957), founder of modern dynamical meteorology. The footnote adds that near the equator, where $f\to0$, the assumption of small $Ro$ breaks down.

> [!intuition] Does the Earth have time to bend you?
> $Ro=(L/U)^{-1}/f$ compares two clocks: how long the motion takes to do its own business ($L/U$) and how long the Earth takes to turn it ($1/f$, about 3 hours at 45°). Small $Ro$ means the motion is *slow* compared with the Earth's clock, so rotation has time to act. A baseball flight lasts a second: the Earth hardly turns it. A bathtub drains in a minute, far shorter than 3 hours, so the Earth's rotation does not set the direction of the drain vortex (only in careful experiments, with water left to settle for a day, does it show). A weather system takes about a day to cross its own width ($10^6$ m at 10 m s⁻¹): longer than 3 hours, so the Earth bends it fully. A hurricane's winds go round its 100 km core in under an hour, shorter than the Earth's clock, so the curvature (centrifugal) term beats Coriolis ($Ro\approx5$).

![[fig_cl13_rossby_scales.png|660]]
*Figure CL13.1. Rossby number $U/fL$ against horizontal scale (45°, lines of constant $U$). See: synoptic and planetary scales sit well below the dashed $Ro=1$ line (rotation dominates), hurricanes and thunderstorms above it, tornadoes far above; the ocean gyre is deep in the rotating regime. Script `fig_cl13_rossby_scales.py`.*

| system | $U$ (m s⁻¹) | $L$ (m) | $Ro=U/fL$ | regime |
|---|---|---|---|---|
| planetary wave | 20 | $10^7$ | 0.02 | geostrophic |
| synoptic cyclone | 10 | $10^6$ | 0.1 | near-geostrophic |
| ocean gyre | 0.1 | $10^6$ | $10^{-3}$ | geostrophic |
| hurricane | 50 | $10^5$ | ≈ 5 | gradient/cyclostrophic |
| thunderstorm | 10 | $10^4$ | ≈ 10 | not rotation-controlled |
| tornado | 50 | $10^2$ | ≈ 5000 | cyclostrophic |

## 3. Friction and the planetary boundary layer
<span class="scope-taught">taught</span> *22 Oct p8, p13–15* · <span class="scope-extra-book">extra · book</span> *Wallace & Hobbs §7.2.5, §3.3*

### 3.1 Why a boundary layer
<span class="scope-taught">taught</span> *22 Oct p8 (CliSci p12)*

The slide's statement: **surface roughness and friction (wind drag) is strongest in the planetary boundary layer (PBL), which extends to about 1–2 km; above it the surface's influence declines** ([[22nd Oct.pdf#page=8|22 Oct, p8]]). The wind profile on the slide shows speed increasing with height from near zero at the ground to a steady value at the top of the layer.

> [!intuition] A rug on a rough floor
> Slide a thick rug across a rough floor. The bottom fibres cling to the floor, the ones above are dragged along less and less, and the top moves freely. Friction at the ground is passed upward by turbulence (swirling eddies mixing slow air up and fast air down). Above a kilometre or two the eddies fade and the air moves as if the ground did not exist: that is the **free atmosphere**.

### 3.2 Free atmosphere versus near surface: the equations
<span class="scope-taught">taught</span> *22 Oct p13–15*

Above the PBL the frictional term is negligible and the equations are ([[22nd Oct.pdf#page=13|22 Oct, p13]], the slide's figure (a): upper-level wind, no friction, with isobars at 688–700 mb, the pressure-gradient force toward low, and the Coriolis force toward high):

$$\frac{\mathrm Du}{\mathrm Dt}=-\frac1\rho\frac{\partial p}{\partial x}+fv,\qquad\frac{\mathrm Dv}{\mathrm Dt}=-\frac1\rho\frac{\partial p}{\partial y}-fu .$$

Near the surface the friction terms are retained ([[22nd Oct.pdf#page=15|22 Oct, p15]], figure (b): surface wind, effect of friction, with the wind arrow turned toward low pressure):

$$\frac{\mathrm Du}{\mathrm Dt}=-\frac1\rho\frac{\partial p}{\partial x}+fv+F_x,\qquad\frac{\mathrm Dv}{\mathrm Dt}=-\frac1\rho\frac{\partial p}{\partial y}-fu+F_y .$$

### 3.3 The three-way balance (what friction does to the wind)
<span class="scope-extra-book">extra · book</span> *Wallace & Hobbs §7.2.5 (book p.281–282, PDF p.298–299); the slide only draws the effect*

> [!extra-book]+ 🟡 Extra (book): the three-way balance, with full algebra
> The slides draw the surface wind turned toward low pressure but do not derive the angle. Take the Northern Hemisphere with low pressure to the north, so the pressure-gradient force $P=|\nabla p|/\rho$ points north. Friction opposes the wind, $\mathbf F=-\kappa\mathbf V_s$ (a simple linear drag with rate $\kappa$). Let the wind $\mathbf V_s$ make an angle $\psi$ toward the low with the isobars: $\mathbf V_s=V_s(\cos\psi,\sin\psi)$. Coriolis acts to the right: $\mathbf C=fV_s(\sin\psi,-\cos\psi)$. Steady state requires $P\hat{\mathbf y}+\mathbf C+\mathbf F=0$:
> $$x:\ fV_s\sin\psi-\kappa V_s\cos\psi=0\ \Rightarrow\ \tan\psi=\frac\kappa f,\qquad y:\ P-fV_s\cos\psi-\kappa V_s\sin\psi=0\ \Rightarrow\ V_s=\frac{P}{f}\cos\psi=V_g\cos\psi.$$
> Wallace & Hobbs' words: the angle is set by the requirement that the component of the pressure-gradient force along the wind equals the drag, and the speed by the requirement that Coriolis balance the pressure force normal to the wind: so $V_s<V_g$ (**sub-geostrophic**), and *the stronger the drag, the larger the angle and the slower the wind*. The cross-isobar flow toward low pressure is the **Ekman drift** seen on surface charts, strongest over rough land.

![[fig_cl13_force_triangles.png|700]]
*Figure CL13.2. Left: free atmosphere, two forces cancel and the wind runs along the isobars (Buys-Ballot: low on the left). Right: in the boundary layer friction opposes the wind; the three forces close a triangle (checked numerically in `fig_cl13_force_triangles.py`), the wind is turned about 30° toward low pressure and is 87 % of the geostrophic speed. See: the three arrows form a closed triangle.*

> [!example] Worked example: turning angle and speed
> Take the 4 hPa per 300 km case at 45° N: $P=1.11\times10^{-3}$ m s⁻², $f=1.03\times10^{-4}$ s⁻¹, so $V_g=P/f=10.8$ m s⁻¹. Choose $\psi=30^\circ$ (typical of land). Then $\kappa=f\tan\psi=5.95\times10^{-5}$ s⁻¹ (a drag time $1/\kappa=4.7$ h); $V_s=V_g\cos30^\circ=9.3$ m s⁻¹, of which $V_s\sin\psi=4.7$ m s⁻¹ blows **across** the isobars toward low pressure, and the frictional force is $\kappa V_s=5.6\times10^{-4}$ m s⁻², half of the pressure force. Over the sea, where roughness is less, $\psi\approx10$–$15^\circ$ and the wind is 96–98 % of $V_g$.

## 4. Geostrophic balance
<span class="scope-taught">taught</span> *22 Oct p16–18 (CliSci p19–21)* · <span class="scope-extra-book">extra · book</span> *M&P §7.1, pp.110–115*

### 4.1 The balance
<span class="scope-taught">taught</span> *22 Oct p16–17*

The slide: **steady-state (non-accelerating) flow results when the pressure gradient force exactly balances the Coriolis force; this is called geostrophic balance** ([[22nd Oct.pdf#page=17|22 Oct, p17]]). Put $\mathrm Du/\mathrm Dt=\mathrm Dv/\mathrm Dt=0$ and $F_x=F_y=0$ in (CL13.2):

$$0=-\frac1\rho\frac{\partial p}{\partial x}+fv_g,\quad0=-\frac1\rho\frac{\partial p}{\partial y}-fu_g\ \Longrightarrow\ \boxed{v_g=\frac{1}{\rho f}\frac{\partial p}{\partial x},\qquad u_g=-\frac{1}{\rho f}\frac{\partial p}{\partial y}}\tag{CL13.4}$$

These are exactly the two equations on the slide. In vector form $\mathbf u_g=\dfrac{1}{\rho f}\hat{\mathbf z}\times\nabla p$ (M&P Eq. 7-3). Two immediate consequences:

- $\mathbf u_g\cdot\nabla p=u_g\,\partial_xp+v_g\,\partial_yp=\frac{1}{\rho f}(-\partial_yp\,\partial_xp+\partial_xp\,\partial_yp)=0$: **the geostrophic wind blows parallel to the isobars** (slide: "Geostrophic winds blow parallel to isobars").
- $|\mathbf u_g|=\dfrac{|\nabla p|}{\rho|f|}$: the closer the isobars, the faster the wind.

> [!intuition] Why the wind does not just run downhill
> Picture the pressure field as a landscape and the air as a ball. Left alone, the ball would roll downhill (from high to low). But the instant it moves, Coriolis starts to turn it to the right. It keeps turning until the Coriolis force points exactly back against the pressure push; at that point the ball moves at right angles to the slope, i.e. along the **contour lines**, like a hiker who never wants to lose or gain height. The slope force is cancelled by the "steering" force, and what remains is motion along the contours at a speed that makes the two equal. A steep hillside (closely spaced isobars) needs a faster ball to cancel it.

> [!pitfall] Three traps
> 1. Geostrophic is **not** the same as "the wind blows from high to low". It blows *along* isobars; only friction gives a component toward low pressure (§3).
> 2. $f$ changes sign across the equator, so in the SH the low is on the **right**: the circulations reverse (§5).
> 3. Geostrophic balance is a *diagnostic balance*, not a mechanism: it does not say how the wind got there (adjustment) nor what changes it (friction, curvature, accelerations).

### 4.2 Buys-Ballot's law and the "river" picture
<span class="scope-extra-book">extra · book</span> *M&P pp.111–112*

> [!extra-book]+ 🟡 Extra (book): reading a map
> Marshall & Plumb note that the force balance requires $\mathbf u_g$ to be normal to the pressure gradient, giving **Buys-Ballot's law** (the 19th-century Dutch meteorologist): *in the Northern Hemisphere, if you stand with your back to the wind, low pressure is on your left* (left→right in the SH). The flow is clockwise around a high and anticlockwise around a low in the NH ([[Geostrophic_motion_Marshall_and_Plumb.pdf#page=2|M&P Fig. 7.1, p.111]]). Because the geostrophic flow does not cross isobars, the isobars act like the **banks of a river**: where they are close together the flow is fast, where they are far apart it is slow (p.112, Fig. 7.2). This is why meteorologists are traditionally preoccupied with pressure maps: *the pressure field determines the winds*.

### 4.3 Numbers and the synoptic chart
<span class="scope-taught">taught</span> *22 Oct p18 (the 500 mb chart 12Z 8 Nov 1999)* · <span class="scope-extra-book">extra · book</span> *M&P pp.114–115 (24 m/s example, Rossby-number map)*

The slides show a **500 mb chart** (contours of height every 60 m, isotherms in °C; [[22nd Oct.pdf#page=18|22 Oct, p18]]) as an example of observed flow along contours.

![[fig_cl13_geostrophic_speed.png|720]]
*Figure CL13.3. Left: geostrophic wind for 4 hPa isobars (surface, $\rho=1.2$) against their spacing at three latitudes. Right: the same gradient against latitude. See: $V_g\propto1/(\text{spacing})$ and $\propto1/\sin\varphi$; the shaded region ($Ro>0.3$ for a 1000 km, 10 m s⁻¹ system, i.e. equatorward of ~13°) is where the balance fails (§4.4). Script `fig_cl13_geostrophic_speed.py`.*

> [!example] Worked example 1: surface wind from a weather chart
> Isobars every 4 hPa, 300 km apart, at 45° N ($f=1.03\times10^{-4}$ s⁻¹, $\rho=1.2$): $V_g=\dfrac{1}{\rho f}\dfrac{\Delta p}{\Delta s}=\dfrac{1.33\times10^{-3}}{1.2\times1.03\times10^{-4}}=\mathbf{10.8\ m\,s^{-1}}$ (≈ 21 kn). At 30° N the same chart gives 15.2 m s⁻¹, at 60° N 8.8 m s⁻¹, at 20° N 22 m s⁻¹.

> [!extra-book]+ 🟡 Extra (book): the 500 mb example, with a check
> M&P look at the 500 mb height field (their Fig. 7.4) at 43° N, 133° W: the wind blows along the contours to the SSE at 25 m s⁻¹ and the height falls 60 m in 250 km. Then (Eq. 7-7 below, M&P p.115)
> $$V_g=\frac gf\frac{\Delta z}{L}=\frac{9.81}{9.7\times10^{-5}}\times\frac{60}{2.5\times10^{5}}=24\ \mathrm{m\,s^{-1}},\ \text{close to the observed 25}.$$
> Their Fig. 7.5 shows $Ro\sim0.1$ over most of the region, approaching 1 only in strong cyclones.

> [!verify] The value of $f$ in the M&P example
> At 43° N, $f=2\Omega\sin43^\circ=9.95\times10^{-5}$ s⁻¹, not $9.7\times10^{-5}$ (which corresponds to latitude 41.7°). The text's 24 m s⁻¹ becomes 23.7 m s⁻¹ with the exact $f$ (24.3 with theirs): the conclusion "close to the observed 25" holds either way. **This vault uses the exact $f$.**

### 4.4 Where geostrophy fails
<span class="scope-extra-beyond">extra · beyond</span> *derived here*

> [!extra-beyond]+ 🔵 Extra (beyond): the equator, curvature, and acceleration
> - **Near the equator** $f=2\Omega\sin\varphi\to0$, so (CL13.4) predicts unbounded winds: at 2° N the same 4 hPa/300 km chart would give 218 m s⁻¹, absurd. In terms of the Rossby number, a 1000 km, 10 m s⁻¹ system has $Ro=U/fL=2.0$ at 2°, 0.8 at 5°, and 0.1 only at 45°. Geostrophic balance is a mid- and high-latitude balance; in the tropics winds are driven by other terms ([[Intertropical Convergence Zone]], [[Trade Winds and Westerlies]]).
> - **Curved flow** (small radii) adds a centripetal term $V^2/R$, giving the gradient wind (§6).
> - **Accelerating flow** (growing or decaying systems, fronts) has $\mathrm Du/\mathrm Dt\neq0$: the small departure from geostrophy, the *ageostrophic wind*, is what changes the pressure pattern and makes weather. A geostrophic wind alone can never evolve, since it already balances the pressure gradient.

### 4.5 Geostrophy in pressure coordinates (height contours)
<span class="scope-extra-book">extra · book</span> *M&P §7.1.1, pp.112–113*

> [!extra-book]- 🟡 Extra (book): upper-air charts use height, not pressure
> Observations aloft are given on **constant-pressure surfaces**, and the natural quantity is the **height $z$** of the surface. For two nearby points A, B with the same pressure and a point C on the level of A (M&P Fig. 7.3), the hydrostatic relation $p_C-p_0=g\rho(z_B-z_0)$ gives
> $$\Big(\frac{\partial p}{\partial x}\Big)_{\!z}=g\rho\Big(\frac{\partial z}{\partial x}\Big)_{\!p}.$$
> Substituting in (CL13.4) the density cancels:
> $$\mathbf u_g=\frac gf\,\hat{\mathbf z}_p\times\nabla_pz,\qquad(u_g,v_g)=\Big(-\frac gf\frac{\partial z}{\partial y},\ \frac gf\frac{\partial z}{\partial x}\Big)\qquad(\text{M\&P Eq. 7-7, 7-8}).$$
> "The wonderful simplification is that $\rho$ does not appear explicitly, so we need not be concerned about its variation." Height contours are streamlines of the geostrophic flow on a pressure surface. For constant $f$ the geostrophic flow is **non-divergent** on pressure surfaces, $\partial_xu_g+\partial_yv_g=0$ (Eq. 7-9), so there is a streamfunction
> $$u_g=-\frac{\partial\psi_g}{\partial y},\quad v_g=\frac{\partial\psi_g}{\partial x},\qquad\psi_g=\frac gf\,z\qquad(7\text{-}10,\ 7\text{-}11).$$
> Example in the text: the 500 mbar surface falls 800 m over 5000 km, so $u_g=\frac{9.81}{10^{-4}}\times\frac{800}{5\times10^6}=15$ m s⁻¹. Non-divergence is only approximate: it fails where $f$ varies appreciably with latitude, which is why large-scale vertical motion exists ([[Mass Stream Function]]).

## 5. Flow around highs and lows
<span class="scope-taught">taught</span> *22 Oct p19–24 (CliSci p22–25)* · <span class="scope-extra-beyond">extra · beyond</span> *friction-induced vertical motion estimate*

### 5.1 Drawing the geostrophic flow
<span class="scope-taught">taught</span> *22 Oct p19–22*

The slides pose it as a drawing exercise. A **low** ("L") with isobars 995, 1000, 1005 hPa increasing outward ([[22nd Oct.pdf#page=19|p19]]) is annotated with dashed arrows at the four compass points ([[22nd Oct.pdf#page=20|p20]]): at the top the arrow points **west** (left), on the right **north** (up), at the bottom **east**, on the left **south**. That is **anticlockwise** flow around a low. A **high** ("H", isobars 1010, 1005, 1000 hPa decreasing outward, [[22nd Oct.pdf#page=22|p22]]) has arrows east at the top, south on the right, west at the bottom, north on the left: **clockwise**.

You can derive both with (CL13.4) or with Buys-Ballot: at the east side of a low, pressure rises to the east, so $\partial_xp>0$ and $v_g=\frac1{\rho f}\partial_xp>0$: the wind blows north; on the west side it blows south; and so on round the circle.

![[fig_cl13_flow_high_low.png|720]]
*Figure CL13.4. Geostrophic wind (arrows, speed ∝ gradient) around a 20 hPa low and a 20 hPa high at 45° N and 45° S (script `fig_cl13_flow_high_low.py`; the code asserts PGF + CF = 0 at the marked point). See: the pressure-gradient force (red) always points down the pressure gradient and the Coriolis force (violet) opposite; the circulation reverses with the sign of $f$. Max wind 10.8 m s⁻¹ in each panel.*

| | Low (L) | High (H) |
|---|---|---|
| Northern Hemisphere | anticlockwise (**cyclonic**) | clockwise (**anticyclonic**) |
| Southern Hemisphere | clockwise (**cyclonic**) | anticlockwise (**anticyclonic**) |

"Cyclonic" means *in the same sense as the planet's own rotation* seen from above the pole of that hemisphere (M&P p.93 footnote), so the word is the same in both hemispheres even though the direction on the page is not.

> [!intuition] Every low is a valley, every high a hill
> Think of the pressure map as a relief map. Winds circle hills and valleys along the contours, with the valley (low) always on the left in the NH. So the NH anticlockwise spin round a low and clockwise round a high is not a separate rule but Buys-Ballot applied round a closed contour. In the SH the Coriolis turn flips, so the whole picture is mirror-reversed.

### 5.2 Surface and free atmosphere
<span class="scope-taught">taught</span> *22 Oct p23 (CliSci p24)*

The slide shows eight panels ([[22nd Oct.pdf#page=23|22 Oct, p23]]): for **cyclonic flow around a low** and **anticyclonic flow around a high**, each at the **surface** and in the **free atmosphere**, for the NH (a, b) and the SH (c, d). In the free atmosphere the wind circles the centre (geostrophic). At the surface the arrows **spiral**: **inward** toward a low and **outward** from a high, in the same sense of rotation. This is exactly the effect of friction (§3.3): the wind is turned across the isobars toward low pressure, so near a low it has an inward component and near a high an outward component: air flows *out of* highs and *into* lows, down the pressure gradient, as one would naively expect.

> [!extra-beyond]+ 🔵 Extra (beyond): friction, convergence and rising air
> Take the worked example of §3.3 for the *cross-isobar speed*, $4.7$ m s⁻¹, as an inflow into a low of radius $r=500$ km, and suppose the inflow speed grows linearly with $r$ inside the low, $u_r\propto r$. The horizontal divergence is $\nabla\!\cdot\!\mathbf v=\frac1r\partial_r(ru_r)=2u_r/r=-1.9\times10^{-5}$ s⁻¹. Mass continuity over a boundary layer of depth $h=1$ km (air cannot pile up) forces a vertical velocity at its top $w=-h\,\nabla\!\cdot\!\mathbf v\approx1.9\times10^{-2}$ m s⁻¹ $=1.9$ cm s⁻¹ $\approx1.6$ km per day. So **friction makes a surface low a region of rising air**, with cloud and rain; the same argument with the sign reversed makes a high a region of subsiding, clear, dry air. This is why highs bring settled weather and lows bring storms.

> [!pitfall] Which direction is "cyclonic" in the south?
> Cyclonic means *with the Earth's rotation*: anticlockwise in the NH, **clockwise** in the SH. A SH low rotates clockwise, which looks "wrong" if you remember only the NH rule. Slide 24 shows both hemispheres' satellite pictures for this reason.

## 6. Cyclones: when curvature matters
<span class="scope-taught">taught</span> *22 Oct p24 (satellite images of a NH and a SH cyclone)* · <span class="scope-extra-book">extra · book</span> *Wallace & Hobbs §7.2.6* · <span class="scope-extra-beyond">extra · beyond</span> *numbers*

The slide closes the topic with satellite images of a Northern Hemisphere cyclone and a Southern Hemisphere cyclone: "look at the circulation" ([[22nd Oct.pdf#page=24|22 Oct, p24]]): the NH one spirals anticlockwise, the SH one clockwise ([[Cyclones and Anticyclones]]).

For a system with strongly curved flow, the Rossby number is not small and the parcel's centripetal acceleration $V^2/R$ cannot be ignored (§2). The result is the **gradient wind**.

> [!extra-book]+ 🟡 Extra (book): the gradient wind (W&H §7.2.6), with derivation and numbers
> Wallace & Hobbs introduce it in §7.2.6 (book p.282): centripetal accelerations in curved trajectories are much larger than those in straight flow. For circular flow of radius $R$ and speed $V$ the radial force balance is
> $$\text{low (cyclonic):}\quad\frac{V^2}{R}+fV=\frac{|\nabla p|}{\rho}\equiv P,\qquad\text{high (anticyclonic):}\quad\frac{V^2}{R}-fV+P=0 .$$
> (In a low the net *inward* force $P-fV$ supplies the centripetal acceleration; in a high Coriolis, which points inward, exceeds the outward pressure force.) Solutions:
> $$V_{\rm low}=-\frac{fR}{2}+\sqrt{\frac{f^2R^2}{4}+RP}\ <\ V_g,\qquad V_{\rm high}=\frac{fR}{2}-\sqrt{\frac{f^2R^2}{4}-RP}\ >\ V_g .$$
> With $R=500$ km, $P=1.11\times10^{-3}$ m s⁻² (the 4 hPa/300 km case) and $f=1.03\times10^{-4}$: $V_g=10.8$, $V_{\rm low}=9.2$ m s⁻¹ (**sub**-geostrophic), $V_{\rm high}=15.3$ m s⁻¹ (**super**-geostrophic). For a high the square root must be real, so $P\le f^2R/4=1.33\times10^{-3}$ m s⁻² ($\approx1.6$ hPa per 100 km): **the pressure gradient near the centre of a high cannot exceed this limit**, which is why high-pressure centres have flat, widely spaced isobars while lows can have very sharp ones.

> [!extra-beyond]- 🔵 Extra (beyond): the cyclostrophic limit (tornado, dust devil)
> When $V^2/R\gg fV$ (large $Ro$), Coriolis drops out: $V^2/R=P$, so $V=\sqrt{RP}$ in either sense of rotation. For a hurricane with $V=50$ m s⁻¹ at $R=50$ km and $f=5\times10^{-5}$ s⁻¹ (20° N): $V^2/R=5\times10^{-2}$ m s⁻² against $fV=2.5\times10^{-3}$: Coriolis is only 5 % of the balance, so the eyewall flow is nearly **cyclostrophic**, and the required pressure gradient is $\rho(V^2/R+fV)=63$ Pa km⁻¹ ≈ 0.63 hPa km⁻¹, i.e. over 50 km a pressure drop of about 31 hPa. Rotation matters only to *initiate* the vortex (Coriolis gives the sense of rotation) and in the far field.

## 7. The Ekman layer
<span class="scope-extra-beyond">extra · beyond</span> *simplest closed solution of the boundary-layer momentum equation (not in the course)*

> [!extra-beyond]+ 🔵 Extra (beyond): a boundary layer with eddy viscosity
> To see the friction angle emerge, model turbulence by an eddy viscosity $K$ (constant, a crude assumption): $F_x=K\,\partial_z^2u$, $F_y=K\,\partial_z^2v$, with pressure force fixed by the geostrophic wind $(u_g,0)$ (aloft). Writing the steady equations of (CL13.2) in terms of the departure $u-u_g$ from the geostrophic wind:
> $$f\,v+K\,u''=0,\qquad -f(u-u_g)+K\,v''=0 .$$
> With no-slip at the ground ($u=v=0$ at $z=0$) and $u\to u_g$, $v\to0$ aloft the solution is
> $$u=u_g\big[1-e^{-z/D}\cos(z/D)\big],\qquad v=u_g\,e^{-z/D}\sin(z/D),\qquad D=\sqrt{2K/f}.$$
> The wind turns **cyclonically (toward low pressure) as it nears the ground**: at $z=0^+$ it is $45^\circ$ to the left of the geostrophic wind, and the tip of the wind vector traces the **Ekman spiral**. The layer is $\sim\pi D$ deep (where the wind first points along the geostrophic wind again). With $K=5$ m² s⁻¹ and $f=1.03\times10^{-4}$: $D=311$ m, depth $\pi D\approx980$ m, matching the "1–2 km" of the slide.
>
> ![[fig_cl13_ekman_spiral.png|700]]
> *Figure CL13.5. Left: hodograph of the Ekman spiral (tip of the wind vector with height). Right: speed and components with height; the speed overshoots 10 m s⁻¹ near $\pi D$ (10.4 m s⁻¹) before settling. See: the wind starts at 45° left of the geostrophic wind at the ground. Real boundary layers have angles of 10–30° because a thin surface layer carries the stress. Script `fig_cl13_ekman_spiral.py`; $K=5$ m² s⁻¹ is illustrative.*
>
> The same balance in the *ocean* (wind stress dragging the surface water) gives the wind-driven **Ekman drift**, to the right of the wind in the NH (W&H Fig. 7.11, confined to the top ~50 m); its divergence causes coastal upwelling.

> [!intuition] Why the wind rotates with height
> The wind at each level feels the friction from the layer below (a drag backwards) and from above (a forward tug). Coriolis keeps turning whatever is moving to the right. Near the ground drag is large and the wind direction is pulled all the way round to the left of the geostrophic wind; higher up the drag shrinks and the Coriolis turning wins, spinning the wind back clockwise with height until it matches the geostrophic flow. The spiral is what you get when a "turn right" force fights a "slow down" force through a stack of layers.

## 8. Where this leads
<span class="scope-taught">taught</span> *synthesis*

- Geostrophic balance + the vertical structure of the atmosphere give the **thermal wind**: the change of the geostrophic wind with height is proportional to the horizontal temperature gradient, which explains why the strongest westerlies (the [[Subtropical Jet]]) sit above the strongest temperature gradient ([[CL14 Observed Winds - Jets, Trades and the ITCZ]]).
- Friction plus Coriolis explain the surface **trades and westerlies** ([[Trade Winds and Westerlies]]) and the inflow into the ITCZ ([[Intertropical Convergence Zone]]).
- Where $f$ is small and heating is strong, balance gives way to buoyancy and pressure forces: monsoon circulations, sea breezes ([[Land-Sea Thermal Circulation]], [[CL15 Monsoons]]).
- The tendency of geostrophic flow to be non-divergent is why vertical motion is a small residual, and why large-scale waves ([[Waves - Course Map]]) propagate as Rossby waves.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Rotation and the wind: Coriolis, inertial oscillations, geostrophic balance
> On a rotating planet a free particle in the horizontal plane moves in inertial circles of radius v/f with period 2π/f, f = 2Ω sin φ (left panel, in the rotating frame).
>
> ![[cl_coriolis.png|720]]
>
> **Try:** Move the latitude from 45° N to the equator: f → 0 and the inertial radius diverges (no rotation felt). Go to the Southern Hemisphere: the circles reverse and the geostrophic wind flips. Slide friction up: the wind crosses the isobars.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_coriolis.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_coriolis.html) · all tools and coverage: [[Interactive Tools]]

> [!interactive]+ Interactive: The Ekman spiral and Ekman transport
> A steady wind stress τ drags the surface water; friction (constant eddy viscosity A_z) and the Coriolis force turn the current with depth: the Ekman spiral.
>
> ![[cl_ekman_spiral.png|720]]
>
> **Try:** A_z = 0.1 m² s⁻¹ at f = 10⁻⁴ s⁻¹ (about 43° latitude): D_E = 44.7 m and the surface current is 3.1 cm/s for τ = 0.1 N m⁻². Change A_z: D_E and the surface speed change but the transport arrow does not. Move to the southern hemisphere: everything mirrors. Latitude 11°, τ = 0.063 N m⁻² gives the 8.8 Sv-type transport of the Chereskin–Roemmich section over ~4000 km.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_ekman_spiral.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_ekman_spiral.html) · all tools and coverage: [[Interactive Tools]]

> [!interactive]+ Interactive: Rotating frames: Coriolis and centrifugal forces, and the Foucault pendulum
> The same motion in two descriptions.
>
> ![[cm08_rotating_frame.png|720]]
>
> **Try:** Free particle: change Ω and watch the straight inertial path become a spiral-like curve in the rotating view, with the Coriolis force always perpendicular to the velocity. 'At rest in the inertial frame' appears as a clockwise circle for Ω > 0. Foucault: at latitude 45° the plane turns once in 23.93 h / sin 45° = 33.85 h; at the poles once per sidereal day, at the equator not at all.
>
> [▶ Open the tool in your browser](../Assets/interactive/cm08_rotating_frame.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cm08_rotating_frame.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL13 connects
> **Builds on:** [[CL12 Rotating Frames and the Coriolis Force]] (the Coriolis terms, $f=2\Omega\sin\varphi$) · [[CL06 Hydrostatic Balance and Vertical Structure]] (vertical balance) · [[CL11 Mean Meridional Circulation and Angular Momentum]] (why Coriolis matters at all).
> **Leads to:** [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (observed geostrophic winds, thermal wind, jets) → [[CL15 Monsoons]] (when balance fails).
> **Concepts:** [[Pressure Gradient Force]] · [[Geostrophic Balance]] · [[Rossby Number]] · [[Scales of Atmospheric Motion]] · [[Planetary Boundary Layer and Friction]] · [[Cyclones and Anticyclones]] · [[Coriolis Force]] · [[Coriolis Parameter]] · [[Centrifugal Force and Effective Gravity]] · [[Eotvos Effect]] · [[Foucault Pendulum]]
> **Other subjects:** [[Waves - Course Map]] (inertial and Rossby waves) · [[Fixed Points and Linear Stability]] (adjustment to balance) · [[Thermodynamics and Statistical Mechanics - Course Map]] (the Rossby number is a dimensionless ratio like the Reynolds and Mach numbers)

> [!connection] Fluid mechanics and oceanography
> Geostrophic balance is the same equation for the ocean (large-scale currents are geostrophic: $Ro\sim10^{-3}$, M&P §9.3), and the Ekman layer of §7 is the oceanic wind-driven surface current. The same "turn plus drag" balance appears in any rotating fluid, e.g. the tea-leaf paradox and the Taylor–Proudman effect in a rotating tank (M&P labs).

> [!connection] Dynamical systems
> A geostrophic state is a **slow manifold**: any initial imbalance excites fast inertia–gravity waves that radiate away, leaving the flow close to balance (geostrophic adjustment). The "slow" and "fast" separation is the same idea as time-scale separation in [[Relaxation Time]].

## Summary
> [!summary] Cheat-sheet
> - **PGF per unit mass** $=-\frac1\rho\nabla p$ (differences push, not absolute pressure). 4 hPa per 300 km ≈ $1.1\times10^{-3}$ m s⁻².
> - **Equations:** $\mathrm Du/\mathrm Dt=-\frac1\rho\partial_xp+fv+F_x$, $\mathrm Dv/\mathrm Dt=-\frac1\rho\partial_yp-fu+F_y$, $f=2\Omega\sin\varphi$ (7.3×10⁻⁵ at 30°, 1.03×10⁻⁴ at 45°, 1.26×10⁻⁴ at 60°).
> - $Ro=U/fL$: ≈ 0.1 synoptic, $10^{-3}$ ocean, ≈ 5 hurricane. Small $Ro$ ⇒ geostrophy; fails near the equator.
> - **Geostrophic wind:** $u_g=-\frac{1}{\rho f}\partial_yp$, $v_g=\frac1{\rho f}\partial_xp$; parallel to isobars; low on the left (NH); $|V_g|=|\nabla p|/\rho|f|$; on pressure surfaces $V_g=\frac gf|\nabla_pz|$, $\psi_g=gz/f$.
> - **PBL** 1–2 km; friction ⇒ $\tan\psi=\kappa/f$, $V_s=V_g\cos\psi$, wind crosses isobars toward low pressure (10–30°).
> - **Low:** NH anticlockwise, SH clockwise; **high:** reverse. Surface: spiral in at lows (rise), out at highs (sink); free atmosphere: circles.
> - **Gradient wind:** $V^2/R\pm fV=P$; low sub-, high super-geostrophic; $P_{\max,\rm high}=f^2R/4$. Cyclostrophic $V=\sqrt{RP}$.

## Practice
1. **Derive** the pressure-gradient force per unit mass from a box of air and show a uniform pressure produces no force.
2. **Coriolis parameter.** Compute $f$ at 30°, 45°, 60° N and at the equator. What is its sign in the SH?
3. **Geostrophic wind from a surface chart.** Isobars every 4 hPa, 300 km apart, at 30° N ($\rho=1.2$). Find $V_g$ and compare with 45° N.
4. **Upper-air chart.** On the 500 hPa surface heights fall 120 m over 500 km at 40° N. Find $V_g$.
5. **Buys-Ballot.** In the NH the wind blows **from the north**. Where is the low pressure? And in the SH?
6. **Rossby numbers.** Compute $Ro$ for (a) a dust devil $U=5$ m s⁻¹, $L=10$ m; (b) a jet stream meander $U=40$ m s⁻¹, $L=2000$ km at 45°; (c) a mid-latitude ocean eddy $U=0.2$, $L=50$ km. Which is geostrophic?
7. **Friction.** With $\psi=20^\circ$, find $V_s/V_g$ and $\kappa/f$. If the drag time $1/\kappa$ is 6 h, which latitude's $f$ gives this angle?
8. **Gradient wind.** For a high with $R=1000$ km at 45° N find the maximum pressure gradient and the speed at $P=0.8P_{\max}$.
9. **Convergence.** A low of radius 800 km has a cross-isobar inflow of 3 m s⁻¹ at its edge growing linearly with $r$. Estimate the vertical velocity at 1.2 km.
10. **Equator.** At what latitude does a 1000 km, 10 m s⁻¹ system reach $Ro=1$? Is geostrophy acceptable at 3° N?

> [!example]- Solutions
> 1. See §1.1: net force $=-\partial_xp\,\delta x\,\delta y\,\delta z$; if $p$ is uniform the two face forces are equal and opposite. Per unit mass divide by $\rho\,\delta x\,\delta y\,\delta z$.
> 2. $f=2\Omega\sin\varphi$: 7.29×10⁻⁵ (30°), 1.03×10⁻⁴ (45°), 1.26×10⁻⁴ (60°) s⁻¹; 0 at the equator; negative in the SH.
> 3. $f(30^\circ)=7.29\times10^{-5}$: $V_g=1.33\times10^{-3}/(1.2\times7.29\times10^{-5})=15.2$ m s⁻¹, vs 10.8 m s⁻¹ at 45°: weaker $f$ ⇒ faster wind for the same gradient.
> 4. $f(40^\circ)=9.37\times10^{-5}$: $V_g=\frac gf\frac{\Delta z}{L}=\frac{9.81}{9.37\times10^{-5}}\times\frac{120}{5\times10^5}=25.1$ m s⁻¹.
> 5. NH: back to the wind means facing south; low on the left = **east**. SH: low on the right: facing south, right = **west**.
> 6. (a) $Ro=5/(10^{-4}\times10)=5000$; (b) $40/(1.03\times10^{-4}\times2\times10^6)=0.19$; (c) $0.2/(10^{-4}\times5\times10^4)=0.04$. (b) and (c) are rotation-controlled; (a) is cyclostrophic/not rotating.
> 7. $V_s/V_g=\cos20^\circ=0.94$; $\kappa/f=\tan20^\circ=0.364$. $\kappa=1/(6\ \mathrm h)=4.63\times10^{-5}$ s⁻¹, so $f=\kappa/0.364=1.27\times10^{-4}$ s⁻¹, i.e. $\sin\varphi=0.87$, $\varphi\approx60^\circ$.
> 8. $P_{\max}=f^2R/4=(1.03\times10^{-4})^2\times10^6/4=2.66\times10^{-3}$ m s⁻² (≈ 3.2 hPa per 100 km). At $P=0.8P_{\max}=2.12\times10^{-3}$: $V=\frac{fR}{2}-\sqrt{(fR/2)^2-RP}=51.5-\sqrt{2653-2120}=51.5-23.1=28.4$ m s⁻¹ (the geostrophic value would be 20.6).
> 9. $\nabla\!\cdot\!\mathbf v=2u_r/r=2\times(-3)/(8\times10^5)=-7.5\times10^{-6}$ s⁻¹; $w=-h\nabla\!\cdot\!\mathbf v=1200\times7.5\times10^{-6}=9\times10^{-3}$ m s⁻¹ ≈ 0.9 cm s⁻¹ (0.8 km per day).
> 10. $Ro=U/(fL)=1\Rightarrow f=10^{-5}$ s⁻¹, $\sin\varphi=10^{-5}/1.46\times10^{-4}=0.0685$, $\varphi=3.9^\circ$. At 3° N $Ro\approx1.3$: **no**, geostrophy is unacceptable; use the full equations.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (1): the other tool's concept notes from the lectures, unreviewed
> [[zettel/pressure-gradient-force|Pressure Gradient Force]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | body/surface forces, PGF derivation, gravity | [[suhas notes.pdf#page=12\|Suhas pre-midsem notes p.12]] (AI-consolidated: secondary; derivation checked here) | taught |
> | table of horizontal scales | [[suhas notes.pdf#page=14\|Suhas pre-midsem notes p.14]] (after Holton) | taught |
> | friction, PBL 1–2 km | [[22nd Oct.pdf#page=8\|22 Oct p8]]; [[22nd Oct CliSci slides.pdf#page=12\|CliSci p12]] | taught |
> | momentum equations, $\boldsymbol\Omega$ components, $2\boldsymbol\Omega\times\mathbf V$, $f=2\Omega\sin\varphi$, $F_x,F_y$ | [[22nd Oct.pdf#page=9\|22 Oct p9–12]]; CliSci p13–16 | taught |
> | free atmosphere vs near surface equations and figure | [[22nd Oct.pdf#page=13\|22 Oct p13–15]]; CliSci p17–18 | taught |
> | geostrophic balance statement and equations; maps; 500 mb chart | [[22nd Oct.pdf#page=16\|22 Oct p16–18]]; CliSci p19–21 | taught |
> | flow around L (995/1000/1005) and H (1010/1005/1000): arrows | [[22nd Oct.pdf#page=19\|22 Oct p19–22]]; CliSci p22–23 | taught |
> | cyclonic/anticyclonic, surface vs free atmosphere, NH/SH; cyclone images | [[22nd Oct.pdf#page=23\|22 Oct p23–24]]; CliSci p24–25 | taught |
> | Rossby number, Eq. 7-1/7-2, ocean $Ro\sim10^{-3}$ | [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=1\|M&P §7.1 p.110]] | extra/book |
> | Eq. 7-3/7-4, Buys-Ballot, Fig. 7.1, river banks (Fig. 7.2), Eq. 7-5 non-divergence | [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=2\|M&P pp.111–112]] | extra/book |
> | pressure-coordinate form, Eq. 7-6…7-11, 800 m/5000 km → 15 m/s | [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=4\|M&P pp.112–113]] | extra/book |
> | Fig. 7.4 synoptic chart, 24 m/s check, Fig. 7.5 $Ro$ map | [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=6\|M&P pp.114–115]] | extra/book |
> | three-way balance, angle $\psi$, sub-geostrophic wind, Ekman drift (ocean) | [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=298\|W&H §7.2.5, p.281–282]] | extra/book |
> | gradient wind | [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=299\|W&H §7.2.6, p.282]] | extra/book |
> | friction algebra, gradient-wind numbers, cyclostrophic limit, convergence → vertical velocity, Ekman solution, equator and $Ro$ chart | derived here (all numbers recomputed) | extra/beyond |
>
> **Dropped as redundant:** the three repeats of the "modify the horizontal momentum equations" slide (22 Oct p9, 10, 12 are successive builds of one derivation); the faded duplicate of the low-pressure drawing (p21); and the pre-midsem notes' discussion of gravity which is superseded by [[CL12 Rotating Frames and the Coriolis Force]].

**References.** Marshall, J. & Plumb, R. A. (2008) *Atmosphere, Ocean and Climate Dynamics*, §7.1 · Wallace, J. M. & Hobbs, P. V. (2006) *Atmospheric Science*, §7.2 · Holton, J. R. *An Introduction to Dynamic Meteorology* (scales of motion table) · Ekman, V. W. (1905) *Ark. Mat. Astron. Fys.* 2(11) · Vallis, G. K. *Atmospheric and Oceanic Fluid Dynamics*, Ch. 2 and 5.

## Across subjects
- [[Law of the Wall]] (Landscapes): the atmospheric surface layer obeys the same logarithmic profile $U=(u_*/\kappa)\ln(z/z_0)$ with a friction velocity and a roughness length.
