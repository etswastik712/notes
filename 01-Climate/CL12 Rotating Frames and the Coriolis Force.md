---
title: CL12 Rotating Frames and the Coriolis Force
aliases: [CL12, Coriolis and centrifugal forces, Equations of motion in a rotating frame]
subject: climate
type: chapter
chapter: 12
part: IV
scope: [taught, extra-book, extra-beyond]
by: [suhas-post]
status: draft
prereq: ["[[CL11 Mean Meridional Circulation and Angular Momentum]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/suhas-post, src/book, src/own-notes, status/draft]
---
# CL12 · Rotating Frames and the Coriolis Force

◀ [[CL11 Mean Meridional Circulation and Angular Momentum]] · [[Climate - Course Map|Course Map]] · [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 why a rotating frame (14 Oct p1–8)
> - §2.1–2.2 two frames and the velocity relation (14 Oct p9–12)
> - §2.3 the rule for *any* vector (slide 13)
> - §2.4 the acceleration relation, Coriolis + centrifugal (slides 14–17)
> - §3 Newton's law in the rotating frame, Coriolis does no work (handwritten notes p.4, M&P Eq. 6-28)
> - §4 physical interpretation: 4.1 object at rest, 4.2 east–west motion, 4.3 north–south motion (15 Oct p1–22; the equatorward case is on notes p.5)
> - §4.4 right in the NH, left in the SH
> - §5 components and $f=2\Omega\sin\varphi$ (22 Oct p9–12, repeated in CL13)
>
> 🟡 **Extra · book** (Marshall & Plumb §6.6 and §7.1, the assigned excerpts)
> - §2.3 box: unit-vector proof
> - §3 box: modified potential $\phi=gz-\Omega^2r^2/2$
> - §5 box: Rossby number and scale analysis (M&P §7.1)
> - §6: radial-inflow experiment, parabolic free surface, sign conventions
>
> 🔵 **Extra · beyond** (added from outside the course)
> - §4.1 box: how oblate really, WGS84 gravity
> - §4.2 box: quantifying the eastward case
> - §4.3 box: Coriolis from angular momentum with the curvature term
> - §5 box: the β-plane
> - §7: Eötvös effect, Foucault pendulum, inertial oscillations, Larmor analogy
>
> *Intuition, example, pitfall and derivation boxes are study aids for the syllabus content of their section and carry its scope.*

> [!key] After this chapter you can
> - derive $\dfrac{\mathrm D\mathbf u}{\mathrm Dt}=-\dfrac1\rho\nabla p+\mathbf g^*+\mathbf F-2\boldsymbol\Omega\times\mathbf u+\Omega^2\mathbf R_\perp$ from Newton's law in an inertial frame, and say which terms are *real* and which are *apparent*;
> - explain the **centrifugal force** (and why it makes the Earth oblate and defines "down") and the **Coriolis force** (why it bends motion to the *right* in the Northern Hemisphere and to the *left* in the Southern) in three independent ways: vectors, force balance and angular momentum;
> - write the Coriolis acceleration in components, give $f=2\Omega\sin\varphi$, and justify which terms can be dropped for large-scale flow;
> - do the numbers: speeds, accelerations, tilts, deflections.

> [!intuition] The whole chapter in 60 seconds
> Newton's $\mathbf F=m\mathbf a$ holds in a frame that is not accelerating. The Earth turns once every 23 h 56 min, so the grid we paint on the ground ("east, north, up") is *accelerating*: every point on it goes round in a circle. If we insist on using that grid, Newton's law gives wrong trajectories unless we add two fake accelerations: one that depends on **where** you are (centrifugal: always straight out from the axis) and one that depends on **how fast you move** (Coriolis: always sideways to your motion). The first is absorbed into "down" and moulded the planet into an oblate shape; the second is what bends winds and ocean currents. Everything else in this chapter is making those two sentences precise and checking they are right.

## 1. Why a rotating frame?
<span class="scope-taught">taught</span> *Suhas 14 Oct p1–8 · continues [[CL11 Mean Meridional Circulation and Angular Momentum|CL11]]*

[[CL11 Mean Meridional Circulation and Angular Momentum|Chapter 11]] showed that a single pole-to-pole cell would carry a ring of air from the equator to latitude $\varphi$ with the impossible eastward speed $u=\Omega a\sin^2\varphi/\cos\varphi$. That argument *assumed* we may use angular-momentum conservation on a rotating planet. The 14 Oct lecture states the problem and then systematises it:

- "If the Earth were not rotating, we would see a single meridional circulation. We need to consider whether the hypothesised motion follows the principle of angular momentum conservation or not" ([[14th Oct.pdf#page=1|p1]]).
- "What actually causes zonal (east–west) winds?" Land–ocean contrast, topography and vegetation can; **but even if the Earth were zonally homogeneous, zonal winds would be found**, and observed zonal winds show a clear structure ([[14th Oct.pdf#page=5|p4–5]]). So there is a *dynamical* origin of zonal wind that is not about geography.
- "Previous discussions based on the movement of a ring of air suggest that conservation of angular momentum must be included when discussing winds in the atmosphere. We now explore how to ensure conservation of momentum when discussing air motion in Earth's atmosphere" ([[14th Oct.pdf#page=7|p6–7]]).
- "To describe motion of an air parcel it is more sensible to choose a coordinate system fixed with respect to Earth. That is a **non-inertial** frame of reference. Although solutions to many problems can be obtained to the desired accuracy by ignoring the rotation of the Earth, **many important effects result from the non-inertial nature of the Earth coordinate system**" ([[14th Oct.pdf#page=8|p8]]).

> [!intuition] The merry-go-round
> Stand on a merry-go-round and throw a ball straight at a friend on the rim. To someone watching from the ground the ball flies in a **straight line**, as Newton says. But the friend moved while the ball was in the air, and *to you and your friend* the ball curves away to the side. You could explain this curve by a sideways force, but no one is pushing the ball. The "force" is your frame turning underneath it. The Earth is a gigantic merry-go-round whose riders are the oceans and the atmosphere, and we measure everything (wind, pressure, currents) from the rider's seat, so we need the fake force.

> [!example] Worked example 1: how fast does the ground move?
> A point at latitude $\varphi$ is a distance $R=a\cos\varphi$ from the axis and travels once round it per sidereal day, at speed $\Omega a\cos\varphi$. With $\Omega=2\pi/86164\ \mathrm s=7.292\times10^{-5}\ \mathrm{s^{-1}}$ and $a=6371$ km:
>
> | latitude | ground speed $\Omega a\cos\varphi$ | centrifugal $\Omega^2a\cos\varphi$ | $f=2\Omega\sin\varphi$ |
> |---|---|---|---|
> | 0° | 464.6 m s⁻¹ | 0.0339 m s⁻² | 0 |
> | 30° | 402.3 | 0.0293 | $0.73\times10^{-4}$ s⁻¹ |
> | 45° | 328.5 | 0.0240 | $1.03\times10^{-4}$ |
> | 60° | 232.3 | 0.0169 | $1.26\times10^{-4}$ |
> | 90° | 0 | 0 | $1.46\times10^{-4}$ |
>
> The ground at the equator moves at 1670 km h⁻¹ (faster than sound), yet we feel nothing: we move with it. Only *departures* from this motion (winds) and *changes of latitude* reveal the rotation.

> [!pitfall] Sidereal vs solar day
> $\Omega$ is the rotation rate relative to the **stars**: one rotation in 86 164 s (23 h 56 min 4 s), not $2\pi/86400$ s. Using the solar day would give $7.272\times10^{-5}$, a 0.3 % error; irrelevant for most estimates but wrong in principle (the extra 4 min per day is the Earth's orbital motion).

## 2. Transformation between frames
<span class="scope-taught">taught</span> *Suhas 14 Oct p9–17 · handwritten notes p.4 · M&P §6.6.2 (Eqs. 6-24 to 6-27)*

### 2.1 Two coordinate systems
<span class="scope-taught">taught</span> *14 Oct p9–10*

Take two coordinate systems with **common origin and common $z$-axis** ([[14th Oct.pdf#page=9|p9–10]]): an inertial one $(X,Y,Z)$, subscript $I$, and one rotating about $Z$ with angular velocity $\boldsymbol\Omega=\Omega\hat{\mathbf z}$ (constant), subscript $r$. The parcel $P$ has position vector $\mathbf R$, with components $(x,y,z)$ in the first and $(x_r,y_r,z_r)$ in the second system; the vector itself is the same arrow, only its description differs.

![[14th Oct.pdf#page=10&height=330]]
*14 Oct, p10: the rotating observer sees a parcel that is stationary in the inertial frame moving **opposite** to the rotation with linear velocity $\boldsymbol\Omega\times\mathbf R$.*

### 2.2 Position and velocity
<span class="scope-taught">taught</span> *14 Oct p11–12 · notes p.4*

If $P$ is stationary in the inertial frame, the rotating observer sees it move with $-\boldsymbol\Omega\times\mathbf R$. More generally the two observers' rates of change of $\mathbf R$ differ by exactly that amount:

$$\Big(\frac{\mathrm d\mathbf R}{\mathrm dt}\Big)_{\!r}=\Big(\frac{\mathrm d\mathbf R}{\mathrm dt}\Big)_{\!I}-\boldsymbol\Omega\times\mathbf R\quad\Longleftrightarrow\quad\boxed{\mathbf u_I=\mathbf u_r+\boldsymbol\Omega\times\mathbf R}\tag{CL12.1}$$

("if we allow point $P$ to have a velocity with respect to the rotating coordinate system, that velocity must be added to $\boldsymbol\Omega\times\mathbf R$ to obtain the time rate of change of $\mathbf R$ in the inertial system", slide 11.)

> [!intuition] Read it as "ground velocity plus wind"
> $\boldsymbol\Omega\times\mathbf R$ is the velocity of the *ground* under the parcel as seen from space. $\mathbf u_r$ is the *wind* (velocity relative to the ground). Their sum is the velocity relative to the stars. A parcel of air at rest relative to the ground ($\mathbf u_r=0$) is *not* at rest in space: it is carried round at $\Omega a\cos\varphi$.

> [!example] Worked example 2: velocity of a westerly jet in space
> A westerly jet of 40 m s⁻¹ at 45° N has $\mathbf u_r=(40,0,0)$ (east, north, up) and the ground velocity is $\boldsymbol\Omega\times\mathbf R=(328.5,0,0)$ m s⁻¹, so $u_I=368.5$ m s⁻¹ eastward relative to the stars: the wind adds 12 % to the parcel's speed in space. An easterly 40 m s⁻¹ gives $288.5$ m s⁻¹. Both are huge compared with the wind; the *difference* between them, $2\times40$ m s⁻¹, is what the atmosphere's pressure field has to account for. *(Check: the angular momentum per unit mass is $u_Ia\cos\varphi$; the wind part $ua\cos\varphi$ is only 12 % of the total, but it is the part that changes.)*

### 2.3 The same rule works for any vector
<span class="scope-taught">taught</span> *14 Oct p13 · M&P Eq. 6-26*

The relation does not care that $\mathbf R$ is a position. "Validity of the above expression is not limited to the vector $\mathbf R$. In fact it satisfies any arbitrary vector" (slide 13):

$$\boxed{\Big(\frac{\mathrm d\mathbf A}{\mathrm dt}\Big)_{\!I}=\Big(\frac{\mathrm d\mathbf A}{\mathrm dt}\Big)_{\!r}+\boldsymbol\Omega\times\mathbf A}\tag{CL12.2}$$

> [!intuition] Why a cross product appears
> Imagine an arrow $\mathbf A$ **glued to the carousel**. The rider sees it frozen: $(\mathrm d\mathbf A/\mathrm dt)_r=0$. The person on the ground sees the tip go in a circle: in a time $\mathrm dt$ the arrow turns by the angle $\Omega\,\mathrm dt$ about the axis, so its tip moves by $\mathrm d\mathbf A=(\boldsymbol\Omega\,\mathrm dt)\times\mathbf A$, perpendicular to both the axis and the arrow. That is $(\mathrm d\mathbf A/\mathrm dt)_I=\boldsymbol\Omega\times\mathbf A$. If the arrow also changes as seen by the rider, the two effects simply add. Equation (CL12.2) is exactly that sentence.

> [!extra-book]- 🟡 Extra (book): the unit-vector proof, and why scalars are unchanged
> Marshall & Plumb prove (CL12.2) with unit vectors ([[climate-suhas merged.pdf#page=26|M&P pp.93–94, Eqs. 6-25, 6-26]]). In the rotating frame write $\mathbf A=\hat{\mathbf x}A_x+\hat{\mathbf y}A_y+\hat{\mathbf z}A_z$ with unit vectors fixed *in that frame*. The rider sees only the components change: $(\mathrm d\mathbf A/\mathrm dt)_r=\hat{\mathbf x}\dot A_x+\hat{\mathbf y}\dot A_y+\hat{\mathbf z}\dot A_z$. The outsider also sees the unit vectors turn, $(\mathrm d\hat{\mathbf x}/\mathrm dt)_I=\boldsymbol\Omega\times\hat{\mathbf x}$ and similarly for $\hat{\mathbf y},\hat{\mathbf z}$. By the product rule
> $$\Big(\frac{\mathrm d\mathbf A}{\mathrm dt}\Big)_{\!I}=\Big(\frac{\mathrm d\mathbf A}{\mathrm dt}\Big)_{\!r}+\boldsymbol\Omega\times(\hat{\mathbf x}A_x+\hat{\mathbf y}A_y+\hat{\mathbf z}A_z).$$
> *Scalars* (temperature, pressure) have $(\mathrm D/\mathrm Dt)_I=(\mathrm D/\mathrm Dt)_r$: both observers follow the same parcel and read the same thermometer, so scalar equations (thermodynamic, continuity) are *unchanged* by rotation; only vector (momentum) equations get extra terms (M&P p.93). This was not discussed on the slides.

### 2.4 Accelerations: where Coriolis and centrifugal come from
<span class="scope-taught">taught</span> *14 Oct p14–17 · notes p.4 · M&P Eq. 6-27*

Apply (CL12.2) to the inertial velocity $\mathbf u_I=\mathbf u_r+\boldsymbol\Omega\times\mathbf R$ ([[14th Oct.pdf#page=14|slides 14–16]]), step by step:

$$\begin{aligned}
\Big(\frac{\mathrm d\mathbf u_I}{\mathrm dt}\Big)_{\!I}&=\Big[\frac{\mathrm d}{\mathrm dt}(\mathbf u_r+\boldsymbol\Omega\times\mathbf R)\Big]_r+\boldsymbol\Omega\times(\mathbf u_r+\boldsymbol\Omega\times\mathbf R)\\
&=\underbrace{\frac{\mathrm d\mathbf u_r}{\mathrm dt}}_{\text{(1) wind acceleration}}+\underbrace{\frac{\mathrm d\boldsymbol\Omega}{\mathrm dt}\times\mathbf R}_{\text{(2) } =0}+\underbrace{\boldsymbol\Omega\times\Big(\frac{\mathrm d\mathbf R}{\mathrm dt}\Big)_r}_{\text{(3) }=\boldsymbol\Omega\times\mathbf u_r}+\underbrace{\boldsymbol\Omega\times\mathbf u_r}_{\text{(4)}}+\underbrace{\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf R)}_{\text{(5) centrifugal}} .
\end{aligned}$$

Terms (3) and (4) are equal, which gives the factor 2. For a vector $\mathbf R$ with $\mathbf R_\perp$ its part perpendicular to $\boldsymbol\Omega$, $\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf R)=\boldsymbol\Omega(\boldsymbol\Omega\!\cdot\!\mathbf R)-\Omega^2\mathbf R=-\Omega^2\mathbf R_\perp$ (the slides' "$\mathbf R_r$" in $-\Omega^2\mathbf R_r$ is this perpendicular distance vector, $R=a\cos\varphi$ on the Earth). Hence

$$\boxed{\frac{\mathrm d\mathbf u_I}{\mathrm dt}=\frac{\mathrm d\mathbf u_r}{\mathrm dt}+\underbrace{2\boldsymbol\Omega\times\mathbf u_r}_{\text{Coriolis}}\ \underbrace{-\,\Omega^{2}\mathbf R_\perp}_{\text{centrifugal}}\ +\ \frac{\mathrm d\boldsymbol\Omega}{\mathrm dt}\times\mathbf R}\tag{CL12.3}$$

The labelled slide ([[14th Oct.pdf#page=17|p17]]) calls the three right-hand extras "the sum of the correction terms": $-\Omega^2\mathbf R_r$ centrifugal acceleration, $2\boldsymbol\Omega\times\mathbf u_r$ Coriolis acceleration, $(\mathrm d\boldsymbol\Omega/\mathrm dt)\times\mathbf R_r$ "time rate of change of rotation $\approx0$", leaving $\mathrm d\mathbf u_I/\mathrm dt\approx\mathrm d\mathbf u_r/\mathrm dt+2\boldsymbol\Omega\times\mathbf u_r-\Omega^2\mathbf R_r$.

> [!intuition] Why is it a *2*?
> Two separate things happen when a parcel moves relative to the ground. **(3)** Its *velocity vector* $\mathbf u_r$ is described in a frame that rotates, so it seems to turn at rate $\Omega$: that contributes $\boldsymbol\Omega\times\mathbf u_r$. **(4)** The parcel arrives at a *new place* on the carousel, where the ground velocity $\boldsymbol\Omega\times\mathbf R$ is different (a point nearer the axis moves more slowly): that contributes another $\boldsymbol\Omega\times\mathbf u_r$. The two effects are equal, so the Coriolis acceleration is **twice** $\boldsymbol\Omega\times\mathbf u_r$. (A neat check: walk radially outward on a carousel at speed $v$; your tangential speed in space must increase at rate $\Omega v$ because the ground you reach moves faster, which is half of the $2\Omega v$ you must be pushed with, the other half being the turning of your radial velocity.)

> [!example] Worked example 3: size of the neglected term
> The rotation rate of the Earth is not exactly constant: the day length changes by about a millisecond over a season (M&P p.143, footnote). Then $\Delta\Omega/\Omega\approx10^{-3}/86400=1.2\times10^{-8}$ in a quarter-year ($8\times10^{6}$ s), so $\mathrm d\Omega/\mathrm dt\approx1\times10^{-19}\ \mathrm{s^{-2}}$ and $|\mathrm d\Omega/\mathrm dt\times\mathbf R|\approx6\times10^{-13}$ m s⁻² at 45°. The Coriolis term for a 10 m s⁻¹ wind is $\sim10^{-3}$ m s⁻², $10^{9}$ times larger. Dropping the third term is justified.

## 3. Newton's law in the rotating frame
<span class="scope-taught">taught</span> *handwritten notes p.4 ("Newton's law is valid only for inertial acceleration"; "Coriolis does no work") · M&P Eqs. 6-6, 6-28, 6-31*

Newton's second law holds only for the *inertial* acceleration. For a fluid parcel the real forces per unit mass are the pressure gradient, true (Newtonian) gravity $\mathbf g^*=-g^*\hat{\mathbf z}$ and friction $\mathbf F$ ([[Suhas post midsem.pdf#page=4|notes p.4]]):

$$\frac{\mathrm d\mathbf u_I}{\mathrm dt}=-\frac1\rho\nabla p+\mathbf g^{*}+\mathbf F.$$

Substitute (CL12.3) and move the apparent accelerations to the right, as in the handwritten notes:

$$\boxed{\frac{\mathrm D\mathbf u}{\mathrm Dt}=-\frac1\rho\nabla p+\mathbf g^{*}+\mathbf F\ \underbrace{-\,2\boldsymbol\Omega\times\mathbf u}_{\text{Coriolis}}\ +\ \underbrace{\Omega^2\mathbf R_\perp}_{\text{centrifugal}}}\tag{CL12.4}$$

where $\mathbf u=\mathbf u_r$ now means velocity relative to the Earth. This is M&P's Eq. 6-28. The first three terms on the right are *real forces*; the last two are **apparent** accelerations that exist because we use rotating coordinates ([[Coriolis Force]], [[Centrifugal Force and Effective Gravity]]).

| | Coriolis $-2\boldsymbol\Omega\times\mathbf u$ | Centrifugal $+\Omega^2\mathbf R_\perp$ |
|---|---|---|
| depends on | the **velocity** relative to the frame | the **position** (distance from the axis) |
| direction | perpendicular to $\mathbf u$ (right of motion for $\Omega$ anticlockwise) | away from the axis |
| work | **none** | can do work; derives from a potential |
| acts on a parcel at rest? | no | yes |
| lives in | horizontal flow: sets the large-scale balance | absorbed into $\mathbf g_{\rm eff}$ |

> [!derivation]+ The Coriolis acceleration does no work
> Take the dot product of the Coriolis term with the velocity: $\mathbf u\cdot(-2\boldsymbol\Omega\times\mathbf u)=0$, because $\boldsymbol\Omega\times\mathbf u$ is perpendicular to $\mathbf u$ (a triple product with a repeated vector). So the kinetic-energy equation $\dfrac{\mathrm D}{\mathrm Dt}\tfrac12|\mathbf u|^2=\mathbf u\cdot(\text{other forces})$ has no Coriolis term: it **changes the direction of the velocity, never its magnitude** ("coriolis does no work by definition as $(\boldsymbol\Omega\times\mathbf u_r)\cdot\mathbf u_r=0$", notes p.4; M&P p.96).

> [!intuition] "Felt" force vs apparent force
> *Centrifugal.* In a car taking a bend you feel pushed outward against the door. In the road's inertial frame nothing pushes you outward: your body is trying to go straight and the door pushes you *inward* ("centripetal"). In the car's frame this inward push must be balanced by an invented outward force: the centrifugal force. On the Earth the "door" is the ground, and the outward force is what makes your weight at the equator 0.35 % lower than it would be if the Earth did not spin. *Coriolis.* A person standing still on the ground feels no Coriolis force at all (it needs velocity). It is more like the **magnetic force on a moving charge**: perpendicular to the motion, proportional to speed, and unable to speed anything up. This analogy is exact in form (see §7).

> [!extra-book]+ 🟡 Extra (book): the centrifugal term is a gradient; the "modified potential"
> Because $\Omega^2\mathbf R_\perp=\nabla(\tfrac12\Omega^2R_\perp^2)$ the centrifugal acceleration can be combined with gravity into a single potential. Writing $\mathbf g^*=-\nabla\Phi^*$ (with $\Phi^*=gz$ near the surface), (CL12.4) becomes
> $$\frac{\mathrm D\mathbf u}{\mathrm Dt}+\frac1\rho\nabla p+\nabla\phi=-2\boldsymbol\Omega\times\mathbf u+\mathbf F,\qquad\phi=gz-\tfrac12\Omega^2R_\perp^2$$
> (M&P Eqs. 6-29, 6-30, [[climate-suhas merged.pdf#page=27|p.95]]). The handwritten notes stop one step earlier: $\mathrm d\mathbf u_r/\mathrm dt+\rho^{-1}\nabla p+\nabla(gz)=-2\boldsymbol\Omega\times\mathbf u_r+\Omega^2\mathbf R_r+\mathbf F$ (p.4). Surfaces of constant $\phi$ are the **level surfaces** that define the shape of the Earth; "gravity" in everyday life and in atmospheric models means $\nabla\phi$.

> [!example] Worked example 4: how big are the terms?
> At the equator the centrifugal acceleration is $\Omega^2a=0.0339$ m s⁻², i.e. $1/290$ of $g$ ($0.35$ %), at 45° it is $0.0240$ m s⁻². The Coriolis acceleration of a 40 m s⁻¹ jet at 45° is $2\Omega u\sin\varphi=4.1\times10^{-3}$ m s⁻² (horizontal, towards the south for an eastward jet), about 6 times smaller than the centrifugal term and $4\times10^{-4}g$. It cannot be hidden in $g$ because it depends on the motion, and it is comparable to the other horizontal forces (pressure gradient $\sim10^{-3}$ m s⁻²), so it controls the large-scale flow ([[CL13 Horizontal Motion - Geostrophic Balance and Friction]]).

## 4. Physical interpretation
<span class="scope-taught">taught</span> *Suhas 15 Oct p1–22 · handwritten notes p.4–5*

[[15th Oct.pdf#page=1|15 Oct]] re-derives the same results physically, one situation at a time. Notation: $a$ Earth's radius, $\varphi$ latitude, $R=a\cos\varphi$ distance from the axis; east $=\hat{\mathbf x}$, north $=\hat{\mathbf y}$, up $=\hat{\mathbf z}$.

### 4.1 An object at rest on the rotating Earth
<span class="scope-taught">taught</span> *15 Oct p2–11 · notes p.4*

**Assumptions** (slide 2): a spherical Earth with uniform mass distribution and homogeneous constituents, "made up of plastic materials" (it can flow).

Two forces act on an object at rest: **true gravity** $\mathbf g^*$, towards the centre (slide 4), and the **centrifugal force** $\Omega^2R$, outward and perpendicular to the axis. Start with the local vertical along $\mathbf g^*$ (slide 5). Resolve the centrifugal force into local components (slides 5–7; notes p.4):

$$\text{vertical (outward)}:\ \Omega^2R\cos\varphi=\Omega^2a\cos^2\varphi,\qquad\text{horizontal (equatorward)}:\ \Omega^2R\sin\varphi=\Omega^2a\sin\varphi\cos\varphi .$$

The vertical part opposes gravity; the horizontal part pushes an object at rest *towards the equator* ("the object will experience a net equatorward forcing", slide 7). It is hard to separate gravity and centrifugal force physically, so one *measures* their sum, the **effective gravity** ([[15th Oct.pdf#page=8|slides 8–9]])

$$\mathbf g_{\rm eff}=\mathbf g^*+\Omega^2\mathbf R_\perp .$$

![[fig_cl12_effective_gravity.png|520]]
*Figure CL12.1. Force balance at latitude 42° on a sphere, centrifugal exaggerated ~120×. Effective gravity (black) is tilted away from the direction of the centre (blue); a level surface (red) is perpendicular to it, i.e. tilted off the sphere. The tilt is equatorward of the radial direction.*

> [!intuition] Pizza dough and the Earth as its own "parabolic table"
> Spin a ball of pizza dough on your finger: it flows outward and flattens into a disc until each bit of dough sits in equilibrium on a surface *perpendicular to the net force*. The Earth did the same over geological time. The plastic Earth flowed equatorward and piled up there until the surface became an equipotential of $\phi=gz-\tfrac12\Omega^2R^2$. Once that happened, an object at rest feels **no horizontal force at all**. This is the best thing about the Earth for meteorology: the centrifugal force has been *used up* in shaping the planet, so the only inertial force left to worry about when things move is the Coriolis force. (Marshall & Plumb build a rotating table with a *parabolic* surface in the laboratory for exactly the same reason: §6.)

Mass flows until "the equatorward component of centrifugal force balances the poleward component of effective gravity" ([[15th Oct.pdf#page=10|slide 10]]). After this, the Earth has "acquired the oblate spheroid shape", gravity has a horizontal component along the surface and "the poleward component of gravity is balanced by the equatorial component of centrifugal force" ([[15th Oct.pdf#page=11|slide 11]]).

> [!verify] The word "poleward" in slides 9–11 and the notes: two readings, one balance
> Slide 9 says of the effective gravity "horizontal component acts **poleward**, vertical component acts downward"; slide 10 says mass flows until the equatorward centrifugal part "balances the **poleward component of effective gravity**"; slide 11 labels $\vec g_{\rm hor}$ poleward and $(\Omega^2R)_{\rm hor}$ equatorward on the *bulged* Earth; the handwritten notes write "horizontal: $g_{\rm hor}-\Omega^2R\sin\varphi$ = poleward" and "balances poleward $g$". The statements are reconcilable once you notice **what each is measured against**:
>
> | Reading | reference surface | horizontal part of … | direction |
> |---|---|---|---|
> | **A** (slides 5–8, Fig. CL12.1) | the *sphere* | $\mathbf g^*+\Omega^2\mathbf R_\perp$ ($\mathbf g^*$ purely radial) | **equatorward** (all of it is the centrifugal part) |
> | **B** (slides 10–11, notes) | the *bulged* surface | true gravity $\mathbf g^*$ of the oblate planet, taken along the new surface | **poleward**, "downhill" because the surface rises towards the equator |
>
> At equilibrium B's poleward gravity component equals A's equatorward centrifugal component, the net horizontal force on a resting object is zero, and $\mathbf g_{\rm eff}$ is exactly perpendicular to the surface. The slides use the phrase "effective gravity" loosely on slides 10, 14 and 16 (where "centrifugal force > effective gravity" really means *centrifugal > the poleward pull of gravity along the surface*). **Physically correct version, used in this vault:** on a sphere the horizontal part of $\mathbf g^*+\Omega^2\mathbf R_\perp$ points equatorward; the plastic Earth flows until the poleward along-surface component of gravity cancels it. Worth checking with Suhas if the wording matters for an answer; the *final balance* is unambiguous.

> [!example] Worked example 5: how tilted is the effective gravity?
> Relative to the spherical radial direction the angle of $\mathbf g_{\rm eff}$ is $\delta\approx\Omega^2a\sin\varphi\cos\varphi/g$:
>
> | latitude | horizontal centrifugal (m s⁻²) | tilt $\delta$ |
> |---|---|---|
> | 10° | 0.0058 | 0.034° |
> | 30° | 0.0147 | 0.086° |
> | **45°** | **0.0169** | **0.099°** (maximum) |
> | 60° | 0.0147 | 0.086° |
>
> So the Earth's surface differs from a sphere by a tiny tilt of 1.7 mrad at most, yet integrated over a quarter-circle of 10 000 km it adds up to the 21 km difference between the equatorial and polar radii. The vertical part reduces $g$ at the equator by $\Omega^2a=0.0339$ m s⁻².

> [!extra-beyond]- 🔵 Extra (beyond): how oblate, really? Measured gravity at the pole and equator
> A **homogeneous** rotating fluid planet has flattening $f\approx\tfrac54q$ with $q=\Omega^2a/g_{\rm eq}\approx1/288$, i.e. $f\approx1/231$ and $a_{\rm eq}-a_{\rm pole}\approx27.6$ km (Maclaurin). The real Earth has $f=1/298.26$ (21.4 km) because the density increases towards the core (Clairaut), so "uniform mass distribution" on slide 2 over-predicts the bulge by ~30 %; the *mechanism* is the same. Measured (WGS84) normal gravity is 9.7803 m s⁻² at the equator and 9.8322 m s⁻² at the poles, a difference of 0.0519 m s⁻²: the centrifugal term accounts for $0.0339$, i.e. **65 %**; the rest is the equatorial bulge itself, which puts the equator farther from the centre (weaker attraction).

### 4.2 An object moving east–west
<span class="scope-taught">taught</span> *15 Oct p12–17 · notes p.4*

The Earth rotates **west to east** (anticlockwise seen from above the North Pole).

> [!intuition] Walking on a carousel
> Walk with the carousel's rotation and you whirl round faster than the platform, so you feel flung outward harder; walk against it and your whirl is slower, so you feel a weaker outward push. The Earth is the carousel: **moving east you are spinning faster about the axis than the ground, so the centrifugal force on you is larger than at rest; moving west it is smaller.**

- **Moving east** ([[15th Oct.pdf#page=13|slides 13–14]]): the parcel's total rotation rate about the axis exceeds $\Omega$, so the **centrifugal force is stronger** than for the object at rest. The balance between gravity's poleward component and centrifugal is disrupted in favour of centrifugal ("centrifugal force > effective gravity; it causes equatorward motion"). Facing east in the Northern Hemisphere, the equator is to your **right**.
- **Moving west** ([[15th Oct.pdf#page=15|slides 15–16]]): total rotation is slower, centrifugal force is **weaker**, gravity wins and the parcel drifts *poleward*. Facing west, the pole (north) is to your **right**.

"In both cases the object deflects to the right of its path" ([[15th Oct.pdf#page=17|slide 17]]) in the Northern Hemisphere (to the left in the Southern).

| motion | total angular velocity | centrifugal compared with rest | drift | relative to the path (NH) |
|---|---|---|---|---|
| eastward | $\Omega+u/R>\Omega$ | stronger | equatorward (south) | **right** |
| westward | $\Omega-\lvert u\rvert/R<\Omega$ | weaker | poleward (north) | **right** |

> [!extra-beyond]- 🔵 Extra (beyond): quantifying the eastward case
> Let the parcel move east with speed $u$ relative to the ground. Its angular velocity about the axis is $\Omega+u/R$, so its centrifugal acceleration is
> $$\Big(\Omega+\frac uR\Big)^{\!2}R=\Omega^2R+2\Omega u+\frac{u^2}{R}.$$
> The extra $2\Omega u$ points away from the axis; resolved along the local vertical and meridian it is $2\Omega u\cos\varphi$ **upward** and $2\Omega u\sin\varphi$ **equatorward**. These are exactly the components of $-2\boldsymbol\Omega\times\mathbf u$ for $\mathbf u=(u,0,0)$, as the determinant in §5 shows: $(0,-2\Omega u\sin\varphi,+2\Omega u\cos\varphi)$. The $u^2/R$ term is the curvature correction, small for atmospheric speeds ($u^2/R\sim10^{-5}$ m s⁻² for 20 m s⁻¹ at 45°). Its *vertical* part is the [[Eotvos Effect]] (§7).

### 4.3 An object moving north–south
<span class="scope-taught">taught</span> *15 Oct p18–22 (poleward case) · notes p.4–5 (both cases)*

Force balance between $\mathbf g_{\rm eff}$ and the centrifugal force predicts **no** east–west deflection for north–south motion: neither force has an east or west component. The slide leaves this "as an exercise" ([[15th Oct.pdf#page=18|slide 18]]) and uses **angular momentum conservation** instead ([[15th Oct.pdf#page=19|slides 19–22]]; notes p.4–5):

> [!intuition] The ice skater
> A skater spinning with arms out spins slowly; pull the arms in and she spins faster, because her angular momentum $m\,r^2\,\omega$ is conserved when $r$ shrinks. A parcel of air moving **poleward** is like arms pulled in: its distance from the axis $a\cos\varphi$ shrinks, so its eastward speed (relative to the stars) must grow to keep $\Omega a^2\cos^2\varphi+ua\cos\varphi$ constant, while the ground under it moves east *more slowly* the higher the latitude. The parcel *outruns* the ground: it drifts east relative to the ground, which is to the **right** of its poleward motion. Moving equatorward is the skater extending her arms: the parcel lags and drifts west, again to the **right** of its motion in the NH.

- The distance from the axis is largest at the equator and decreases poleward, so the eastward ground speed $\Omega a\cos\varphi$ is largest at the equator: ~**460 m s⁻¹** there, ~**330 m s⁻¹** at 45° N (slide 20).
- **Poleward-moving air** (slides 21–22): "the parcel has high eastward momentum and it conserves it as it moves poleward"; the ground north of the equator moves east with lesser speed, "as a result the air parcel outpaces the earth surface toward east. It appears as deflection to the right of its path."
- **Equatorward-moving air** (handwritten notes p.5, not on the photographed slides): "as it moves closer to the equator the ground moves faster; the parcel will move west"; in both hemispheres "deflection = right (NH), left (SH)". Facing south in the NH, west is on your right.

![[fig_cl12_angular_momentum.png|760]]
*Figure CL12.2. Left: the eastward speed of the ground. Right: the eastward wind a ring of air would need if it left the equator at rest and conserved absolute angular momentum ($14,\,58,\,134$ m s⁻¹ at 10°, 20°, 30°). This is the argument of [[CL11 Mean Meridional Circulation and Angular Momentum]].*

> [!example] Worked example 6: ring-of-air numbers, poleward and equatorward
> The absolute angular momentum per unit mass is $A=\Omega a^2\cos^2\varphi+ua\cos\varphi$ ([[Absolute Angular Momentum of Air]]).
> - **Equator → 30° N, starting at rest relative to the ground** ($A_0=\Omega a^2$): $u=\Omega a\sin^2\varphi/\cos\varphi=464.6\times0.2887=\mathbf{+134}$ m s⁻¹ (westerly). To 45°: $+328.5$ m s⁻¹; to 60°: $+697$ m s⁻¹.
> - **30° N → equator, starting at rest:** $A_0=\Omega a^2\cos^2 30^\circ=0.75\,\Omega a^2$ and at the equator $A=\Omega a^2+ua$, so $u=\Omega a(0.75-1)=\mathbf{-116}$ m s⁻¹ (easterly). From 45° N: $-232$ m s⁻¹.
>
> These are unrealistic as *winds* because friction, pressure forces and eddies intervene, but the **sign** is right: poleward flow aloft turns into westerlies (the subtropical jet) and equatorward flow near the surface into easterlies (the trades).

> [!extra-beyond]- 🔵 Extra (beyond): Coriolis from angular momentum, with the curvature term
> Conserve $A=\Omega a^2\cos^2\varphi+ua\cos\varphi$ following a parcel and write $v=a\dot\varphi$:
> $$0=\frac{\mathrm dA}{\mathrm dt}=a\cos\varphi\,\dot u-2\Omega a^2\cos\varphi\sin\varphi\,\dot\varphi-ua\sin\varphi\,\dot\varphi\ \Rightarrow\ \frac{\mathrm Du}{\mathrm Dt}=\underbrace{2\Omega\sin\varphi\,v}_{\text{Coriolis}}+\underbrace{\frac{uv\tan\varphi}{a}}_{\text{curvature}}.$$
> The first term is the Coriolis term $+fv$ of (CL12.5b) with $f=2\Omega\sin\varphi$; the second is a geometric ("metric") term from the curvature of latitude circles, dropped on the tangent-plane approximation. It ties the vector argument of §2–3, the force-balance argument of §4.2 and the angular-momentum argument of §4.3 together: **they are the same effect.**

### 4.4 Why right in the Northern Hemisphere and left in the Southern?
<span class="scope-taught">taught</span> *the rule: 15 Oct p17, notes p.4–5 · explanation: M&P p.96*

The Coriolis force turns a parcel to the right of its motion in the NH ($\Omega$ anticlockwise seen from above the north pole), to the left in the SH. The reason is geometric: horizontal motion is only turned by the component of $\boldsymbol\Omega$ along the **local vertical**, $\Omega\sin\varphi$, and that component changes sign across the equator.

> [!intuition] Stand at a pole, then at the other
> At the North Pole the ground under you turns anticlockwise (seen from above) once a day: your local "rotation" is $+\Omega$. At the South Pole, looking *down* on the ground from above (the local "up" direction), the Earth turns **clockwise**: $-\Omega$. At latitude $\varphi$ only the share $\Omega\sin\varphi$ of the Earth's spin lies along local "up" (like tilting a turntable: only the vertical component of the spin turns objects lying on it), so the local rotation rate is $\Omega\sin\varphi$: positive in the north, zero at the equator, negative in the south. Anticlockwise rotation deflects to the right; clockwise to the left. M&P put it as: "for the southern hemisphere, the effective sign of rotation is reversed" ([[climate-suhas merged.pdf#page=28|p.96]]; their Fig. 6.17, which is not in the excerpt).

![[fig_cl12_omega_components.png|760]]
*Figure CL12.3. At latitude $\varphi$ the rotation vector splits into a vertical part $\Omega\sin\varphi$ (which turns horizontal motion: this defines $f$) and a northward part $\Omega\cos\varphi$ (which only matters for vertical and east–west motion).*

![[fig_cl12_hemispheres.png|820]]
*Figure CL12.4. A parcel with no pressure force launched northward at 45° in each hemisphere, 10 m s⁻¹: a circle bending right (NH) or left (SH), radius $U/|f|=97$ km, period $2\pi/|f|=16.9$ h. Right: $f$ against latitude; at 30° $f=\Omega$ and the period is one sidereal day. (Script `fig_cl12_hemispheres.py`.)*

## 5. The Coriolis acceleration in components, and the Coriolis parameter
<span class="scope-taught">taught</span> *22 Oct p9–12 (repeated in [[CL13 Horizontal Motion - Geostrophic Balance and Friction|CL13]]) · M&P Eq. 6-28 and §7.1*

Take local Cartesian axes $(x,y,z)$ = (east, north, up). At latitude $\varphi$ the rotation vector points parallel to the Earth's axis, which in the local frame is $\boldsymbol\Omega=(0,\ \Omega\cos\varphi,\ \Omega\sin\varphi)$ (22 Oct slides 9–10: "Earth angular velocity in component form"). With $\mathbf u=(u,v,w)$:

> [!derivation]+ Cross product, step by step
> $$\boldsymbol\Omega\times\mathbf u=\begin{vmatrix}\hat{\mathbf x}&\hat{\mathbf y}&\hat{\mathbf z}\\0&\Omega\cos\varphi&\Omega\sin\varphi\\u&v&w\end{vmatrix}
> =\hat{\mathbf x}\big(\Omega\cos\varphi\,w-\Omega\sin\varphi\,v\big)-\hat{\mathbf y}\big(0\cdot w-\Omega\sin\varphi\,u\big)+\hat{\mathbf z}\big(0\cdot v-\Omega\cos\varphi\,u\big).$$
> Hence $\boldsymbol\Omega\times\mathbf u=(\Omega\cos\varphi\,w-\Omega\sin\varphi\,v,\ \ \Omega\sin\varphi\,u,\ \ -\Omega\cos\varphi\,u)$ and
> $$-2\boldsymbol\Omega\times\mathbf u=\big(2\Omega\sin\varphi\,v-2\Omega\cos\varphi\,w,\ \ -2\Omega\sin\varphi\,u,\ \ 2\Omega\cos\varphi\,u\big).\tag{CL12.5a}$$
> Check against §4: eastward $u$ gives $(0,-2\Omega u\sin\varphi,+2\Omega u\cos\varphi)$: equatorward in the NH and upward, as found from the centrifugal argument. Northward $v$ gives $+2\Omega v\sin\varphi$ eastward: right of the motion ✓. Westward $u<0$ gives a northward and *downward* push ✓.

For large-scale atmospheric flow the vertical velocity is tiny compared with the horizontal ($|w|\ll|v|$) and the vertical component $2\Omega\cos\varphi\,u$ is small compared with $g$ and the vertical pressure gradient, so only the horizontal parts survive:

$$\boxed{\frac{\mathrm Du}{\mathrm Dt}=\dots+fv,\qquad\frac{\mathrm Dv}{\mathrm Dt}=\dots-fu,\qquad f=2\Omega\sin\varphi}\tag{CL12.5b}$$

(the form on 22 Oct, [[22nd Oct.pdf#page=12|slide 12]]: $\mathrm du/\mathrm dt=-\rho^{-1}\partial p/\partial x+2\Omega\sin\varphi\,v$ and $\mathrm dv/\mathrm dt=-\rho^{-1}\partial p/\partial y-2\Omega\sin\varphi\,u$). $f$ is the **Coriolis parameter** ([[Coriolis Parameter]]): $\approx0$ at the equator, $1.03\times10^{-4}$ s⁻¹ at 45°, $1.46\times10^{-4}$ s⁻¹ at the poles, odd across the equator.

> [!intuition] The turntable on its side
> At the **pole** the Earth is a turntable lying flat: it spins horizontal motion fully. At the **equator** the same turntable is standing on its edge, spinning about a *horizontal* north–south axis: a horizontal puck on it is *not* turned sideways, but anything moving up/down or east/west is pushed vertically (the term $2\Omega\cos\varphi$, i.e. §7's Eötvös effect). Between the two, the horizontal part of the effect scales as $\sin\varphi$. This is why the Coriolis force is "weak at the equator" in the horizontal and why large-scale tropical flow behaves differently from mid-latitude flow ([[CL11 Mean Meridional Circulation and Angular Momentum]]).

> [!extra-book]+ 🟡 Extra (book): scale analysis and the Rossby number (M&P §7.1)
> The assigned excerpt for the next chapter ([[Geostrophic_motion_Marshall_and_Plumb.pdf#page=1|M&P §7.1, p.110]]) asks which terms matter for a free-atmosphere flow with typical speed $U\sim10$ m s⁻¹, length scale $L\sim10^6$ m, time scale $L/U\sim10^5$ s. The acceleration terms are of order $U^2/L\sim10^{-4}$ m s⁻² and the Coriolis term $fU\sim10^{-3}$ m s⁻². Their ratio is the **Rossby number**
> $$\mathrm{Ro}=\frac{U}{fL}\sim\frac{10}{10^{-4}\cdot10^{6}}=0.1,$$
> so the Coriolis term dominates over the acceleration of the flow. Developed in [[CL13 Horizontal Motion - Geostrophic Balance and Friction]]. Some orders of magnitude: a bathtub vortex ($U\sim0.1$ m s⁻¹, $L\sim0.3$ m) has $\mathrm{Ro}\sim3000\gg1$ (the Earth's rotation is irrelevant for the drain); a hurricane ($U\sim50$ m s⁻¹, $L\sim10^5$ m) $\mathrm{Ro}\sim5$–10 depending on latitude; a tornado ($L\sim100$ m) $\mathrm{Ro}\sim5000$.

> [!example] Worked example 7: Coriolis on a meridional wind and a projectile
> A **10 m s⁻¹ southerly or northerly wind at 30° N**: $f=2\Omega\sin30^\circ=7.29\times10^{-5}$ s⁻¹, so $\mathrm Du/\mathrm Dt=fv=7.3\times10^{-4}$ m s⁻² and an unopposed parcel gains $2.6$ m s⁻¹ of eastward speed per hour. At $30^\circ$ the inertial period $2\pi/f$ equals one sidereal day (23.9 h): $f=\Omega$ exactly. **A 100 m s⁻¹ shell over 100 km at 45° N**: flight time 1000 s, sideways displacement $\tfrac12(2\Omega\sin\varphi\,u)t^2=\tfrac12\times1.03\times10^{-2}\times10^6=$ **3.6 km** to the right; the same shell fired at the equator is not deflected horizontally.

> [!extra-beyond]- 🔵 Extra (beyond): the β-plane preview
> $f$ varies with latitude: $\beta\equiv\mathrm df/\mathrm dy=2\Omega\cos\varphi/a$, which is $2.3\times10^{-11}$ m⁻¹ s⁻¹ at the equator and $1.6\times10^{-11}$ at 45°. Expanding $f\approx f_0+\beta y$ around a latitude (the **β-plane**) keeps the dominant effect of the sphericity. It is the restoring mechanism of **Rossby waves**, the planetary-scale waves that organise mid-latitude weather ([[Waves - Course Map]]). On an $f$-plane ($\beta=0$) there are no Rossby waves, only inertial oscillations (§7).

## 6. What the assigned book adds: experiments on a rotating table
<span class="scope-extra-book">extra · book</span> *Marshall & Plumb §6.6.1 and §6.6.4 (pp.93–96), not shown on the slides*

Everything above is in the lectures; the book surrounds it with two laboratory experiments that make the physics tangible. They are labelled *extra* because the 14–15 Oct slides do not contain them.

> [!extra-book]+ 🟡 Extra (book): radial inflow experiment (GFD Lab III, §6.6.1, [[climate-suhas merged.pdf#page=25|p.93]])
> Water flows inward through a ring diffuser at $r_1$ in a tank rotating at $\Omega$. Each ring of fluid conserves its absolute angular momentum, $V_\theta r=\Omega r_1^2$ (Eq. 6-22) because it enters with the table's own speed $\Omega r_1$. The azimuthal velocity *relative to the table* is $v_\theta=V_\theta-\Omega r$:
> $$v_\theta=\Omega\,\frac{r_1^2-r^2}{r}\qquad(\text{Eq. 6-23}),$$
> anticlockwise (**cyclonic**) for $\Omega>0$, greatly magnified at small $r$. Example: $r_1=0.5$ m, $\Omega=2$ rad s⁻¹, at $r=0.25$ m: $v_\theta=2\times0.1875/0.25=1.5$ m s⁻¹, three times the table's own speed there ($\Omega r=0.5$ m s⁻¹). Writing the force balance in *relative* velocities automatically produces the extra term $-2\Omega v_\theta$, "the Coriolis acceleration... because we have chosen to express our force balance in terms of relative, rather than absolute, velocities" (Eq. 6-21). This is the same conclusion as §2.4 reached with a particular geometry, and the same mathematics as the ring of air in [[CL11 Mean Meridional Circulation and Angular Momentum]] ($r=a\cos\varphi$).

> [!extra-book]+ 🟡 Extra (book): the parabolic free surface (GFD Lab IV, §6.6.4, [[climate-suhas merged.pdf#page=28|p.96]])
> Let a tank of water come into **solid-body rotation**: the fluid is at rest relative to the tank ($\mathbf u=0$, $\mathbf F=0$). Then (CL12.4) with the modified potential reduces to $\rho^{-1}\nabla p+\nabla\phi=0$, a generalisation of hydrostatic balance to the rotating frame, so $p/\rho+\phi=$ const: surfaces of constant $p$ coincide with surfaces of constant $\phi$. At the free surface $p=0$, so $gz-\tfrac12\Omega^2r^2=$ const, and fixing the constant by $z=h(0)$ on the axis:
> $$\boxed{z(r)=h(0)+\frac{\Omega^2r^2}{2g}}\tag{CL12.6}$$
> a **paraboloid**: depressed on the axis, highest at the rim (Fig. 6.11: a tank 1 m square at 20 rpm). *Example:* $\Omega=20\ \mathrm{rpm}=2.09$ rad s⁻¹; at $r=0.5$ m the rise is $\Omega^2r^2/2g=4.39\times0.25/19.6=\mathbf{5.6}$ cm and the slope is $\Omega^2r/g=0.22$. The surface is perpendicular to the effective gravity, exactly like the oblate Earth (§4.1), which is why the rotating table models the planet in the laboratory.
>
> The book then uses a table of this shape (a solid paraboloid) so the fluid *feels no centrifugal force* and only Coriolis acts: GFD Labs IV–V. The sign convention for the Southern Hemisphere and the experiments on the table are in the same pages (Fig. 6.17 is cited but not in the excerpt).

> [!verify] Two small checks of the AI book notes against the book
> The AI-generated `climate_book_notes.pdf` (pp.9–10) reproduces Eqs. 6-24, 6-26, 6-27, 6-28, 6-29, 6-30 and the parabola correctly ([[climate_book_notes.pdf#page=10|p.10]]). It describes the tank in Fig. 6.11b as "1 m wide"; the caption in the book says "a tank of 1 m square". Its "quiz trap" items concern the Hadley chapter (CL11); the ones relevant here are collected in the quiz checklist below.

## 7. Beyond the course: consequences and cousins of the Coriolis force
<span class="scope-extra-beyond">extra · beyond</span> *standard results; verified numerically*

> [!extra-beyond]- 🔵 Extra (beyond): the Eötvös effect, your weight depends on your eastward speed
> From the vertical component of (CL12.5a) and the $u^2/R$ term of §4.2, the extra upward acceleration of a body moving east at $u$ at latitude $\varphi$ is $2\Omega u\cos\varphi+u^2/a$. A train moving east at 30 m s⁻¹ at the equator becomes lighter by $2\Omega u=4.4\times10^{-3}$ m s⁻² (+$1.4\times10^{-4}$ from $u^2/a$), i.e. **0.046 %** of its weight; a jet at 250 m s⁻¹ loses 0.37 %. Used in gravimetry at sea, where ship speed must be corrected for. See [[Eotvos Effect]].

> [!extra-beyond]- 🔵 Extra (beyond): the Foucault pendulum
> A pendulum swinging in a vertical plane has no horizontal force to turn that plane except Coriolis: the plane rotates (clockwise in the NH) at the rate of the local vertical component of the rotation, $\Omega\sin\varphi$. Period of one full turn $2\pi/(\Omega\sin\varphi)=23.93\ \mathrm h/\sin\varphi$: Paris (48.85° N) 31.8 h, Delhi (28.6° N) 50.0 h, Pune (18.5° N) 75.4 h, at the pole 23.93 h, at the equator no rotation. A direct, laboratory demonstration of the rotation of the Earth ([[Foucault Pendulum]]).

> [!extra-beyond]- 🔵 Extra (beyond): inertial oscillations
> With no pressure force the horizontal equations are $\dot u=fv$, $\dot v=-fu$. Then $\ddot u=-f^2u$: a parcel moves in a circle of radius $U/|f|$ with period $2\pi/|f|=12\ \mathrm h/\sin\varphi$ (16.9 h and 97 km for 10 m s⁻¹ at 45°, Fig. CL12.4; 13.8 h and 158 km for 20 m s⁻¹ at 60°). These **inertial oscillations** are observed in the ocean mixed layer after storms. Mathematically the equilibrium is a centre (neutral stability, [[Fixed Points and Linear Stability]]): no restoring force, only turning.

> [!extra-beyond]- 🔵 Extra (beyond): the Coriolis–magnetic analogy (Larmor)
> $-2m\boldsymbol\Omega\times\mathbf u=2m\,\mathbf u\times\boldsymbol\Omega$ has exactly the form of the Lorentz force $q\,\mathbf u\times\mathbf B$ with $q\mathbf B\leftrightarrow2m\boldsymbol\Omega$. Both are perpendicular to $\mathbf u$ and do no work. **Larmor's theorem**: a weak magnetic field acts on charges like a rotation of the frame at $\omega_L=qB/2m$; the quantum-mechanical consequence is the Zeeman splitting. See [[Rotating Reference Frames]] and [[Quantum Mechanics - Course Map]].

## Map of this chapter
> [!connection] How CL12 connects
> **Builds on:** [[CL11 Mean Meridional Circulation and Angular Momentum]] (ring-of-air argument, why a single cell fails) · [[CL10 Global Energy Balance and Meridional Structure]] (why circulation exists at all) · [[CL06 Hydrostatic Balance and Vertical Structure]] (hydrostatic balance now with $\mathbf g_{\rm eff}$ and the geopotential $\phi$).
> **Leads to:** [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (pressure gradient vs Coriolis = geostrophic wind) · [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (trades and westerlies from the sign of the turning) · [[CL15 Monsoons]] (non-rotating vs rotating cross-equatorial flow).
> **Concepts:** [[Coriolis Force]] · [[Coriolis Parameter]] · [[Centrifugal Force and Effective Gravity]] · [[Absolute Angular Momentum of Air]] · [[Rotating Reference Frames]] · [[Eotvos Effect]] · [[Foucault Pendulum]] · [[Linearisation and Sensitivity]] (scale analysis).
> **Other subjects:** [[Waves - Course Map]] (Rossby and inertia–gravity waves) · [[Quantum Mechanics - Course Map]] (Larmor) · [[Landscapes and Geomorphology - Course Map]] (rotation, geoid and isostasy) · [[Thermodynamics and Statistical Mechanics - Course Map]] (a rotating fluid in equilibrium: the same geopotential idea).

> [!connection] Classical mechanics
> The rotating-frame relation (CL12.2) is the **transport theorem** of classical mechanics; Coriolis, centrifugal and Euler forces are what any Lagrangian written in rotating coordinates produces automatically. A *generalised* treatment (rotating frames in Lagrangian mechanics, gyroscopes, tides) belongs to the classical-mechanics notes; here it is specialised to the geophysical case where $\Omega$ is constant. See [[Rotating Reference Frames]].

> [!connection] Landscapes and the solid Earth
> The same potential $\phi=\Phi^*-\tfrac12\Omega^2R^2$ defines the **geoid**, the reference level for sea level and for the topography studied in [[Landscapes and Geomorphology - Course Map]]; the 21 km equatorial bulge is the Earth's rotating-frame equilibrium. On the other hand rotation does *not* measurably deflect rivers: their Rossby number is enormous.

## Summary
> [!summary] Cheat-sheet: Rotating frames and Coriolis
> - Frame rule: $(\mathrm d\mathbf A/\mathrm dt)_I=(\mathrm d\mathbf A/\mathrm dt)_r+\boldsymbol\Omega\times\mathbf A$; so $\mathbf u_I=\mathbf u_r+\boldsymbol\Omega\times\mathbf R$.
> - Acceleration: $\mathrm d\mathbf u_I/\mathrm dt=\mathrm d\mathbf u_r/\mathrm dt+2\boldsymbol\Omega\times\mathbf u_r-\Omega^2\mathbf R_\perp$ (the $\mathrm d\boldsymbol\Omega/\mathrm dt$ term $\approx0$).
> - Rotating-frame momentum equation: $\mathrm D\mathbf u/\mathrm Dt=-\rho^{-1}\nabla p+\mathbf g^*+\mathbf F-2\boldsymbol\Omega\times\mathbf u+\Omega^2\mathbf R_\perp$.
> - Coriolis: $\perp\mathbf u$, workless, right (NH)/left (SH); centrifugal: outward, conservative.
> - Effective gravity $\mathbf g_{\rm eff}=\mathbf g^*+\Omega^2\mathbf R_\perp$; $\phi=gz-\tfrac12\Omega^2R^2$; Earth is oblate because it flowed until $\mathbf g_{\rm eff}\perp$ surface.
> - Components: $-2\boldsymbol\Omega\times\mathbf u=(2\Omega\sin\varphi\,v-2\Omega\cos\varphi\,w,\ -2\Omega\sin\varphi\,u,\ 2\Omega\cos\varphi\,u)$; large scale: $+fv$, $-fu$, $f=2\Omega\sin\varphi$.
> - Numbers: $\Omega=7.292\times10^{-5}$ s⁻¹; $\Omega a=464.6$ m s⁻¹; $\Omega^2a=0.034$ m s⁻²; $f_{45}=1.03\times10^{-4}$ s⁻¹; tilt $\le0.1^\circ$ at 45°; $z=h_0+\Omega^2r^2/2g$.

> [!summary] Quiz checklist (Marshall & Plumb §6.6)
> - [ ] State and justify $\mathbf u_I=\mathbf u_r+\boldsymbol\Omega\times\mathbf r$ and the any-vector rule (CL12.2); say why $\mathrm D/\mathrm Dt$ of a **scalar** is the same in both frames.
> - [ ] Derive (CL12.3) and (CL12.4) from Newton's law in the inertial frame, naming each term and its direction.
> - [ ] Coriolis: perpendicular to the velocity, **no work** ($(\boldsymbol\Omega\times\mathbf u)\cdot\mathbf u=0$), changes direction not speed. Centrifugal: outward, equals $\nabla(\Omega^2r^2/2)$.
> - [ ] Combine gravity and centrifugal into $\phi=gz-\Omega^2r^2/2$; explain the parabolic free surface $z=h_0+\Omega^2r^2/2g$ and the oblate Earth.
> - [ ] **Sign traps:** with $\Omega>0$ (anticlockwise seen from above the pole) the deflection is to the **right**; in the SH the effective rotation $\Omega\sin\varphi$ is negative so deflection is to the **left**; poleward flow in the NH acquires an *eastward* (westerly) component; equatorward flow a *westward* one.
> - [ ] The factor is **2Ω×u** (not Ω×u); centrifugal is $\Omega^2$ times the *perpendicular* distance $R=a\cos\varphi$ (not $a$).
> - [ ] The ring-of-air formula $u=\Omega a\sin^2\varphi/\cos\varphi$ is for the **frictionless upper branch** starting from $u=0$ at the equator (do not apply it at the surface); values $14,58,134$ m s⁻¹ (the book rounds the last to 130).
> - [ ] Know why $f=2\Omega\sin\varphi$ and why the $2\Omega\cos\varphi$ terms are dropped at large scale.
> - [ ] Which of Coriolis/centrifugal acts on a parcel at rest? (only centrifugal.) Which depends on velocity? (only Coriolis.)

## Practice
1. **Derivation.** Starting from (CL12.1) and (CL12.2), obtain (CL12.3). Show that $\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf R)=-\Omega^2\mathbf R_\perp$ and that the Coriolis term does no work.
2. **Numbers.** (a) Centrifugal acceleration at 45° N. (b) Coriolis acceleration (horizontal) for a 10 m s⁻¹ meridional wind at 30° N. (c) How much eastward speed does an unopposed northward-moving parcel gain per hour there?
3. **Angular momentum.** Air leaves 30° N at rest relative to the ground, moves to the equator conserving absolute angular momentum. Find its zonal wind there. Repeat from 45° N, and for a parcel going equator → 45° N.
4. **Eötvös.** A train moves east at 30 m s⁻¹ at the equator. By what fraction does its apparent weight change? Repeat for a jet at 250 m s⁻¹.
5. **Oblateness.** (a) Maximum tilt of $\mathbf g_{\rm eff}$ from the vertical of a sphere. (b) Predict $a_{\rm eq}-a_{\rm pole}$ for a homogeneous body using $f\approx\tfrac54q$ and compare with 21.4 km.
6. **Parabolic table.** The water surface in a tank rises 5 cm between the axis and $r=0.5$ m. Find $\Omega$ in rad s⁻¹ and rpm.
7. **Foucault.** After how long does the swing plane complete one turn in Pune (18.5° N)? At what latitude does it take exactly 36 h?
8. **Inertial oscillation.** Period and radius for a 20 m s⁻¹ current at 60° N. At what latitude does the inertial period equal 24 h?
9. **Conceptual.** Why does the *force-balance* argument of §4.2 give east–west deflection but not north–south, while the angular-momentum argument gives both? Why does $f$ vanish at the equator although the Coriolis force does not?
10. **Rossby number.** Compute $\mathrm{Ro}=U/fL$ for (i) the synoptic scale ($U=10$ m s⁻¹, $L=10^6$ m, 45° N), (ii) a hurricane ($50$ m s⁻¹, $10^5$ m, 20° N), (iii) a tornado ($50$ m s⁻¹, $100$ m). For which is rotation of the Earth unimportant?

> [!example]- Solutions
> 1. From (CL12.2) with $\mathbf A=\mathbf u_I$: five terms, see §2.4; terms (3) and (4) equal. For the triple product use $\mathbf a\times(\mathbf b\times\mathbf c)=\mathbf b(\mathbf a\!\cdot\!\mathbf c)-\mathbf c(\mathbf a\!\cdot\!\mathbf b)$ with $\mathbf a=\mathbf b=\boldsymbol\Omega$: $\boldsymbol\Omega(\boldsymbol\Omega\!\cdot\!\mathbf R)-\Omega^2\mathbf R=-\Omega^2\mathbf R_\perp$. Work: $\mathbf u\cdot(\boldsymbol\Omega\times\mathbf u)=0$.
> 2. (a) $\Omega^2a\cos45^\circ=0.0240$ m s⁻². (b) $2\Omega\sin30^\circ\times10=7.3\times10^{-4}$ m s⁻². (c) $7.3\times10^{-4}\times3600=2.6$ m s⁻¹ per hour.
> 3. $u=\Omega a(\cos^2\varphi_0-\cos^2\varphi)/\cos\varphi$. 30° → 0°: $464.6\times(0.75-1)=-116$ m s⁻¹ (westward, an easterly). 45° → 0°: $464.6\times(0.5-1)=-232$ m s⁻¹. 0° → 45° N: $+328.5$ m s⁻¹ (westerly).
> 4. $2\Omega u=4.4\times10^{-3}$ m s⁻² (+$u^2/a=1.4\times10^{-4}$) $\Rightarrow4.6\times10^{-4}g=0.046$ %; jet: $2\Omega u=0.0365$ m s⁻² $=0.37$ % (lighter when moving east, heavier when moving west).
> 5. (a) $\delta_{\max}=\Omega^2a/(2g)=1.73\times10^{-3}$ rad $=0.099^\circ$ at 45°. (b) $q=1/288$, $f=\tfrac54q=1/231$, $a/231=27.6$ km vs 21.4 km (the dense core reduces the bulge).
> 6. $\Delta z=\Omega^2r^2/2g\Rightarrow\Omega=\sqrt{2g\Delta z}/r=\sqrt{0.981}/0.5=1.98$ rad s⁻¹ $=18.9$ rpm.
> 7. $T=2\pi/(\Omega\sin\varphi)=23.93\ \mathrm h/\sin18.5^\circ=75.4$ h. For 36 h: $\sin\varphi=23.93/36=0.665\Rightarrow\varphi=41.7^\circ$.
> 8. $f(60^\circ)=1.263\times10^{-4}$ s⁻¹: $T=2\pi/f=13.8$ h, $r=U/f=158$ km. For $T=24$ h (sidereal day 23.93 h): $f=\Omega\Rightarrow\sin\varphi=1/2$, $\varphi=30^\circ$.
> 9. East–west: moving along a latitude circle changes the centrifugal term, which has a *meridional* horizontal component; moving north–south changes $R$ but neither $\mathbf g_{\rm eff}$ nor the (zonally symmetric) centrifugal force has an east–west component, so the balance of forces says nothing: the deflection arises from conservation of angular momentum (equivalently the $\boldsymbol\Omega\times\mathbf u$ term). The *horizontal* deflecting component $2\Omega\sin\varphi$ vanishes at the equator because $\boldsymbol\Omega$ is horizontal there; the Coriolis force is $2\Omega\cos\varphi$ times $u$ *vertically*, so it still exists.
> 10. (i) $10/(1.03\times10^{-4}\cdot10^6)=0.1$. (ii) $f(20^\circ)=5.0\times10^{-5}$: $\mathrm{Ro}=50/(5.0\times10^{-5}\cdot10^5)=10$. (iii) $50/(1.03\times10^{-4}\cdot100)\approx4800$ (with $f$ at 45°). Rotation is unimportant when $\mathrm{Ro}\gg1$: tornado (and bathtub); important for synoptic systems; hurricanes are intermediate.

## PDF handout
The derivation chain, effective-gravity diagram (TikZ), component table and rules as a printable two-page LaTeX sheet: [[climate-rotating-frames-handout.pdf]].

![[climate-rotating-frames-handout.pdf#page=1&height=460]]

> [!connection] Group theory used here
> Rotations of the plane and the sphere form the groups $SO(2)$ and $SO(3)$: [[GT10 Symmetry Representations and Characters]] §6; see [[Where Groups Appear in the Vault]].

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (1): the other tool's concept notes from the lectures, unreviewed
> [[zettel/coriolis-deflection-on-planetary-circulation|Coriolis Deflection on Planetary Circulation]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | motivation: non-rotating Earth, angular momentum, non-inertial frame | [[14th Oct.pdf#page=1\|14 Oct p1–8]] | taught |
> | two coordinate systems, $\mathbf u_I=\mathbf u_r+\boldsymbol\Omega\times\mathbf R$, rule for any vector | [[14th Oct.pdf#page=9\|14 Oct p9–13]]; handwritten notes p.4; M&P Eqs. 6-24, 6-26 | taught |
> | acceleration transformation, Coriolis + centrifugal, $\mathrm d\Omega/\mathrm dt\approx0$ | [[14th Oct.pdf#page=14\|14 Oct p14–17]]; [[Suhas post midsem.pdf#page=4\|notes p.4]]; M&P Eq. 6-27 | taught |
> | Newton's law valid for inertial acceleration; (CL12.4); Coriolis does no work | [[Suhas post midsem.pdf#page=4\|notes p.4]]; M&P Eqs. 6-28, p.96 | taught |
> | object at rest, effective gravity, oblate Earth | [[15th Oct.pdf#page=2\|15 Oct p2–11]]; notes p.4 | taught |
> | eastward / westward motion | [[15th Oct.pdf#page=12\|15 Oct p12–17]]; notes p.4 | taught |
> | north–south: poleward case | [[15th Oct.pdf#page=18\|15 Oct p18–22]]; notes p.4–5 | taught |
> | north–south: equatorward case | handwritten notes p.5 (not in the photographed slides) | taught (per notes) |
> | right in the NH, left in the SH; local-vertical explanation | slide 17 / notes; M&P p.96 | taught |
> | $f=2\Omega\sin\varphi$ and component form | [[22nd Oct.pdf#page=9\|22 Oct p9–12]] (belongs to CL13) | taught |
> | unit-vector proof; scalar invariance; modified potential $\phi$ | M&P §6.6.2–6.6.3 (Eqs. 6-25, 6-29, 6-30) | extra/book |
> | radial-inflow experiment; parabolic free surface; SH sign convention (Fig. 6.17 not in excerpt) | M&P §6.6.1, §6.6.4 | extra/book |
> | Rossby number and scale analysis | M&P §7.1 (excerpt GEO p.1), developed in CL13 | extra/book |
> | eastward-case quantification; angular momentum → Coriolis + curvature; β-plane; Eötvös; Foucault; inertial oscillation; Larmor; WGS84 and Maclaurin | derived or standard results (numbers recomputed here) | extra/beyond |
>
> **Not in this chapter (other lectures of the same dates):** 14 Oct p2–3 (impact of the Hadley circulation, ITCZ) → [[CL11 Mean Meridional Circulation and Angular Momentum]] / [[CL14 Observed Winds - Jets, Trades and the ITCZ]].
> **Dropped as redundant:** the slides' separate statements of the transformation for $\mathbf R$ and then for $\mathbf u$ (slides 11–13) are merged into (CL12.1)–(CL12.2); the handwritten notes' repeat of the three-case argument is merged into §4.
> **Corrections to the pilot version of this chapter:** the Coriolis acceleration of a 40 m s⁻¹ jet is ~6 times (not 100 times) smaller than the centrifugal term at 45°; the equatorward case is now attributed to the handwritten notes, not the slides; the "poleward effective gravity" wording is resolved in §4.1.

> [!provenance]- Slide evidence (click to expand pages)
> ![[14th Oct.pdf#page=17&height=300]]
> ![[15th Oct.pdf#page=11&height=300]]
> ![[15th Oct.pdf#page=20&height=300]]
> ![[Suhas post midsem.pdf#page=4&height=420]]

**References.** Marshall, J. & Plumb, R. A. (2008) *Atmosphere, Ocean and Climate Dynamics*, Ch. 6 §6.6, Ch. 7 §7.1 · Wallace & Hobbs (2006) §7.2 ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=294|PDF p.294 ff.]]) · WGS84 normal gravity (NIMA TR8350.2) for the equator/pole values.

## Across subjects
- [[LS05 Shape of Planets]] (Landscapes): the same rotating-frame mechanics that gives the Coriolis force in the atmosphere gives the flattening of the planet (centrifugal term) and the tilt of the geoid.
- [[Storm Surge]] (Landscapes): the Coriolis force deflects the wind-driven surge, making it stronger on the right of a northern-hemisphere hurricane track where wind and forward motion add.
