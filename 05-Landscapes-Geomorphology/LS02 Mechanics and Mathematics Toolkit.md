---
title: LS02 Mechanics and Mathematics Toolkit
aliases: [LS02, Mechanics and Mathematics Toolkit]
subject: landscapes
type: chapter
chapter: 2
part: I
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS02 · Mechanics and Mathematics Toolkit

◀ [[LS01 Landscapes as Physical Systems]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS03 Digital Elevation Models and Terrain Analysis]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides 35–38, 45–50 of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 5 sections, 8 derivation boxes, 6 redrawn figures and 10 slide images.

> [!key] After this chapter you can
> - expand a function in a Taylor series and use order-of-magnitude reasoning,
> - write mass conservation $\partial_t\rho+\partial_xq=S$ and derive the diffusion equation,
> - balance forces on a slab and use stress, pressure and viscosity,
> - solve the Newtonian viscous flow down an incline.

> [!intuition] The one-sentence story
> Almost every landscape equation is one of four things: a Taylor expansion, mass conservation with a flux, a force balance with a stress, or a viscous flow; this chapter derives each once so the rest can use them.

```mermaid
flowchart LR
  A["orders of magnitude,<br/>dimensions"] --> B["Taylor series,<br/>Newton laws"]
  B --> C["mass conservation,<br/>flux, diffusion"]
  C --> D["force balance, stress"]
  D --> E["viscous flow"]
```
*Concept map: every box is a section of this chapter.*

*[Slides 35–50]*

This chapter reviews (slides 35–50) the physics used throughout: Newton's laws and stability, hydrostatics, stress, viscous flow and mass conservation. Wherever the argument needs mathematics beyond 12th grade, a blue box derives it first.


## Orders of magnitude and dimensional consistency

A **scaling argument** finds how a quantity depends on the parameters by balancing the dominant terms and discarding $\mathcal{O}\!\left(1\right)$ constants; it gives $\sim$, not $=$. Its logic is *dimensional homogeneity*: an equation is valid only if every term has the same units.


> [!example] 🧮 Worked example: Speed of a viscous film from dimensions alone
> A viscous layer of thickness $H$ on a slope $\theta$ has parameters $\rho g\sin\theta [\mathrm{kg m^{-2}s^{-2}}]$, $H [\mathrm m]$, $\mu [\mathrm{kg m^{-1}s^{-1}}]$. A speed $[\mathrm{m s^{-1}}]$ can be formed in only one way: $v\sim(\rho g\sin\theta)^aH^b\mu^c$. Matching kg: $a+c=0$; s: $-2a-c=-1$ gives $a=1, c=-1$; m: $-2a+b-c=1\Rightarrow b=2$. So $v\sim\rho g\sin\theta H^2/\mu$, exactly the result of slide 48 obtained there by force balance. The exact solution (§2.6) differs only by the factor $1/2$.


## Taylor series and Newton's laws (slides 35–36)

> [!figure]- 🖼 Slides 35–36: open to see the slides this section explains
> ![[pre_035.jpg|300]] ![[pre_036.jpg|300]]


> [!key] 🛠 Tool: The Taylor series, from the fundamental theorem of calculus
> Let $f$ be smooth. By the fundamental theorem, $f(t)=f(0)+\int_0^t f'(s) \mathrm{d} s$. Apply the same theorem to $f'$: $f'(s)=f'(0)+\int_0^sf”(r) \mathrm{d} r$. Then
>
>
> $$
> f(t)=f(0)+t f'(0)+\int_0^t\!\!\int_0^s f”(r) \mathrm{d} r \mathrm{d} s .
> $$
>
>
> Repeating with $f”$, $f”'$, \dots, and using $\int_0^t\!\int_0^s\mathrm{d} r \mathrm{d} s=t^2/2$, $\int_0^t\!\int_0^s\!\int_0^r\mathrm{d} q\mathrm{d} r\mathrm{d} s=t^3/6$, etc., gives
>
>
> $$
> f(t)=f(0)+t f'(0)+\tfrac12t^2f''(0)+\tfrac16t^3f'''(0)+\cdots=\sum_{k\ge0}\frac{t^k}{k!}f^{(k)}(0). \tag{2}
> $$
>
>
> If $t$ is small the terms shrink rapidly and truncation after the first neglected term gives an error of the size of that term. **Partial derivatives**: for $f(x,y)$, $\partial_xf$ is the derivative with $y$ held fixed. Applying (2) first along $x$ and then along $y$, $f(x+\mathrm{d} x,y+\mathrm{d} y)\approx f+\partial_xf \mathrm{d} x+\partial_yf \mathrm{d} y$ (to first order). This is the only multivariable calculus needed in this text.


> [!derivation] 🟢 In the slides: Slide 35–36: a particle's whole trajectory from a force law
> Slide 35 writes $x(t)=x(0)+t\dot x(0)+\tfrac12t^2\ddot x(0)+\tfrac16t^3\dddot x(0)+\dots$, i.e. (2). To use it we must know all derivatives at $t=0$. Newton's second law supplies them:
>
>
> $$
> m\ddot x=\sum_if_i(x,\dot x,t)\quad\Longrightarrow\quad \ddot x(0)=\tfrac1m\sum_if_i\big(x(0),\dot x(0),0\big).
> $$
>
>
> Differentiating the law once more gives $\dddot x(0)=\frac1m\frac{\mathrm{d}}{\mathrm{d} t}\sum f_i$ evaluated at $t=0$, again in terms of $x(0),\dot x(0)$; and so on. Hence *the initial position, initial velocity and the force law determine the entire trajectory*. This is the “time-dependent motion” of slide 36: $\{x(0),\dot x(0),\ddot x(t)\}$ with $m\ddot x=\sum f_i$.
>
> *Time-independent case, a particle at rest.* If $\dot x(0)=0$ and $\sum_if_i=0$ at $x(0)$ then $\ddot x(0)=0$ and all higher derivatives vanish too (if the forces do not depend on time), so $x(t)=x(0)$ for all $t$. For a landscape one accepts $\sum f_i\approx0$ with error small compared with the individual forces, as the slide's “$\sum f_i\approx0$” indicates.


> [!derivation] 🟢 In the slides: Slide 36: a steady state may or may not be stable
> Let the net force depend on position only, $F(x)$, with $F(x_*)=0$ (equilibrium). For a small displacement $\delta=x-x_*$, expand by (2): $F\approx F'(x_*)\delta$. Then $m\ddot\delta=F'(x_*)\delta$.
>
>
> - If $F'(x_*)=-k<0$ (restoring force), $\delta=\delta_0\cos(\sqrt{k/m} t)$: the displacement stays bounded — **stable**.
> - If $F'(x_*)=+k>0$, $\delta=\tfrac12\delta_0(\mathrm{e}^{\sqrt{k/m} t}+\mathrm{e}^{-\sqrt{k/m} t})$ grows exponentially — **unstable**: the equilibrium exists but is never observed for long because perturbations are always present.
> - If $F'(x_*)=0$, neutral (marginal).
>
>
> In terms of a potential energy $V$ with $F=-V'$: stable at a minimum of $V$, unstable at a maximum.


![[ls_fig02.png]]
*Figure LS02.1. Equilibria of a ball in a potential well (potential energy shown as height). Slide 36: “steady state may/may not be stable”.*


> [!intuition] Why unstable equilibria matter to geology
> An unstable equilibrium is a perfectly balanced state that any noise destroys. A pile of loose sand at a slope above the angle of repose, a heavy fluid resting on a light one (Rayleigh–Taylor, §2.5) and a mountain whose rock is loaded to its strength (Chapter 6) are all close to such edges; landslides, overturn and failure are the way the system leaves them.


## Mass conservation, flux and diffusion (slide 50)

> [!figure]- 🖼 Slide 50: open to see the slides this section explains
> ![[pre_050.jpg|300]]


![[ls_fig03.png]]
*Figure LS02.2. The control element of slide 50: quantity $n$ per unit length, flux $Q$ across any point, source $s$ per unit length.*


> [!derivation] 🟢 In the slides: Slide 50: the one-dimensional continuity equation
> Let $n(x,t)$ be the amount of a conserved quantity (mass, ice, sediment, \dots) per unit length and $Q$ the amount crossing a point per unit time; for material moving with velocity $v_x$, $Q=n v_x$ (slide: $Q_x=n(x)v_x(x)$). For the element $[x,x+\mathrm{d} x]$:
>
>
> $$
> \underbrace{\partial_tn \mathrm{d} x}_{\text{rate of change of content}}=\underbrace{Q(x)}_{\text{in}}-\underbrace{Q(x+\mathrm{d} x)}_{\text{out}}+\underbrace{s(x) \mathrm{d} x}_{\text{source}} .
> $$
>
>
> Taylor: $Q(x+\mathrm{d} x)=Q(x)+\partial_xQ \mathrm{d} x$. Dividing by $\mathrm{d} x$:
>
>
> $$
> \boxed{\ \partial_tn=-\partial_xQ+s(x)\ } \tag{3}
> $$
>
>
> Nothing else is assumed except that the quantity is neither created nor destroyed except through $s$. In steady state, $\partial_xQ=s$: flux changes only where there is a source.
>
>
> *Closure by gradients.* Many transport mechanisms move material *down a gradient*, from high to low $n$, at a rate proportional to the steepness of the gradient: $Q\propto-\partial_xn$ (the slide writes $Q_x\propto\partial_xn$, the minus sign is implied by direction). Writing $Q=-D \partial_xn$ with $D>0$,
>
>
> $$
> \boxed{\ \partial_tn=D\,\partial_x^2n+s(x)\ }\qquad\text{(diffusion equation).} \tag{4}
> $$
>
>
> The value of $D$ has units $\mathrm{m^2 s^{-1}}$. Slide 122 states that this same equation governs hillslope evolution (Chapter 12).


> [!intuition] What $\partial_x^2n$ means
> By the Taylor series, $n(x+\mathrm{d} x)+n(x-\mathrm{d} x)-2n(x)\approx\partial_x^2n \mathrm{d} x^2$. So $\partial_x^2n>0$ means $n(x)$ is *below* the average of its neighbours: diffusion fills that local dip. Diffusion therefore smooths: it removes curvature, flattens hills, warms the cold neighbour.


> [!key] 🛠 Tool: Three solutions of the diffusion equation used later
> **(a) Steady, uniform source.** $\partial_tn=0$: $Dn”=-s$, so $n=n_0-\tfrac{s}{2D}x^2$: a parabola (used for hillslopes, §12.4).
>
> **(b) Similarity solution: spreading from a step or a fixed boundary value.** Suppose $n(x,0)=0$ for $x>0$ and $n(0,t)=n_s$, $n(\infty,t)=0$, with $s=0$. The problem contains no length except through $\sqrt{Dt}$ (dimensions: $D t$ is a length squared), so $n=f(\eta)$ with $\eta=x/(2\sqrt{Dt})$. Then $\partial_tn=f' \partial_t\eta=-\tfrac{\eta}{2t}f'$ and $\partial_x^2n=f”/(4Dt)$. Insert in (4): $f”=-2\eta f'$. Write $g=f'$: $g'/g=-2\eta$, so $g=A\mathrm{e}^{-\eta^2}$ and $f=B+A\int_0^\eta\mathrm{e}^{-s^2}\mathrm{d} s$. Define $\mathrm{erf}(\eta)=\frac2{\sqrt\pi}\int_0^\eta\mathrm{e}^{-s^2}\mathrm{d} s$. (Its limit $\mathrm{erf}(\infty)=1$ follows from $I^2=\iint\mathrm{e}^{-(x^2+y^2)}\mathrm{d} x\mathrm{d} y=\int_0^{2\pi}\!\!\int_0^\infty\mathrm{e}^{-r^2}r \mathrm{d} r\mathrm{d}\theta=\pi$, so $I=\int_0^\infty\mathrm{e}^{-s^2}\mathrm{d} s=\sqrt\pi/2$.) The boundary conditions $f(0)=n_s$, $f(\infty)=0$ fix $B=n_s$, $A=-n_s\frac{2}{\sqrt\pi}$:
>
>
> $$
> n(x,t)=n_s\,\mathrm{erfc}\!\left(\frac{x}{2\sqrt{Dt}}\right),\qquad\mathrm{erfc}=1-\mathrm{erf}. \tag{5}
> $$
>
>
> The profile spreads with the *diffusion length* $\ell\sim2\sqrt{Dt}$ (Fig. (erfc)): time to diffuse a distance $\ell$ is $t\sim\ell^2/4D$. A step initially at $x=0$ (high on the left, $n_0$; zero on the right) similarly gives $n=\frac{n_0}2\mathrm{erfc}(x/2\sqrt{Dt})$.
>
> **(c) Periodic forcing.** If $n(0,t)=a\cos\omega t$, try $n=a \mathrm{e}^{-x/\delta}\cos(\omega t-x/\delta)$. Put $\psi=\omega t-x/\delta$. Then $\partial_tn=-a\omega\mathrm{e}^{-x/\delta}\sin\psi$, and differentiating twice in $x$ gives $\partial_x^2n=-\tfrac{2a}{\delta^2}\mathrm{e}^{-x/\delta}\sin\psi$. The equation $\partial_tn=D\partial_x^2n$ holds if and only if $\omega=2D/\delta^2$, i.e.
>
>
> $$
> \delta=\sqrt{2D/\omega}=\sqrt{DP/\pi}\quad(P=2\pi/\omega),\qquad n=a\,\mathrm{e}^{-x/\delta}\cos(\omega t-x/\delta). \tag{6}
> $$
>
>
> The wave is damped by $\mathrm{e}^{-1}$ per $\delta$ and lags in phase by one radian per $\delta$. (Derivation by trial: complex $n=\mathrm{Re}[a\mathrm{e}^{\mathrm{i}\omega t-\lambda x}]$ gives $\mathrm{i}\omega=D\lambda^2$, $\lambda=(1+\mathrm{i})/\delta$; the check above avoids complex numbers.)


![[ls_fig04.png]]
*Figure LS02.3. Diffusion from a boundary held at $n_s$, eq. (5). Quadrupling the time only doubles the penetration depth (curves at $Dt=1,4,16$).*


## Force balance and stress (slides 37–38, 45–46)


### Hydrostatic equilibrium


![[ls_fig05.png]]
*Figure LS02.4. Slide 37: a fluid element of face area $\mathrm{d} a$ and height $\mathrm{d} z$ at rest. Pressure forces on the faces (purple) balance the weight (blue).*


> [!derivation] 🟢 In the slides: Slide 38: hydrostatic equilibrium
> For an element of area $\mathrm{d} a$ and height $\mathrm{d} z$, the upward force from below is $P(z)\mathrm{d} a$, the downward force from above is $P(z+\mathrm{d} z)\mathrm{d} a$, and the weight is $\rho g \mathrm{d} a \mathrm{d} z$ (mass $\rho \mathrm{d} a \mathrm{d} z$). Zero net force:
>
>
> $$
> P(z) \mathrm{d} a-P(z+\mathrm{d} z) \mathrm{d} a-\rho g \mathrm{d} a \mathrm{d} z=0.
> $$
>
>
> With $P(z+\mathrm{d} z)=P(z)+\partial_zP \mathrm{d} z$ and dividing by $\mathrm{d} a \mathrm{d} z$:
>
>
> $$
> \boxed{\ \partial_zP+\rho g=0\ } \tag{7}
> $$
>
>
> Solve with the boundary condition $P(z=0)=0$ at the top surface $z=0$ ($z$ upward here means depth $d=-z$ increases downward, so $P(d)=\int_0^d\rho g \mathrm{d} d'$). For uniform $\rho$: $P=\rho g d$. Examples: $4$ km of ocean: $P=1000\cdot9.8\cdot4000=39 \mathrm{MPa}$; $35$ km of crust ($\rho=2800$): $P\approx0.96 \mathrm{GPa}$; the $100$ MPa at $3$ km depth quoted on slide 53 is $2800\cdot9.8\cdot3000\approx82 \mathrm{MPa}\approx10^8$ Pa.


> [!example] ❓ Question on the slides: Slide 38: show that this gives a buoyant force equal to the weight of the displaced liquid
> Immerse a body occupying volume $V$ with its boundary $\partial V$ in a fluid at rest with pressure $P(z)$. The force on the body from the fluid is $\vect F_P=-\oint_{\partial V}P \hat{\vect n} \mathrm{d} A$, where the pressure pushes *into* the surface. The $z$-component is $F_{P,z}=-\oint P n_z \mathrm{d} A$. Choose a thin vertical column of horizontal cross-section $\mathrm{d} a$ that cuts the body at a top point $z_t$ and a bottom point $z_b$ (for a body convex in $z$). On its top face $n_z \mathrm{d} A=+\mathrm{d} a$ (upward normal) and on its bottom face $n_z \mathrm{d} A=-\mathrm{d} a$. The column contributes
>
>
> $$
> -P(z_t) \mathrm{d} a+P(z_b) \mathrm{d} a=\mathrm{d} a [P(z_b)-P(z_t)]=\mathrm{d} a\int_{z_b}^{z_t}(-\partial_zP) \mathrm{d} z=\mathrm{d} a\int_{z_b}^{z_t}\rho_fg \mathrm{d} z,
> $$
>
>
> using (7). Summing over columns, $F_{P,z}=\rho_fgV$ (for uniform fluid density $\rho_f$): **the upward force equals the weight of the displaced fluid**. This is Archimedes' principle. The key point: the pressure field that balances the fluid's own weight is *independent of what occupies the region*; replacing the displaced fluid by the body leaves the pressure forces unchanged. Isostasy (Chapter 7) is exactly this with mantle as fluid.


> [!derivation] 🔵 Extra (not derived in the slides): Stability of a stratified fluid (energy argument) and Rayleigh–Taylor growth rate
> **Energy argument.** Take two small equal volumes $V$ of density $\rho_1$ at height $z_1$ and $\rho_2$ at $z_2>z_1$. Interchanging them changes the potential energy by
>
>
> $$
> \Delta E=Vg(\rho_1z_2+\rho_2z_1)-Vg(\rho_1z_1+\rho_2z_2)=Vg(\rho_1-\rho_2)(z_2-z_1).
> $$
>
>
> If the heavier fluid is below ($\rho_1>\rho_2$) then $\Delta E>0$: any overturn raises the energy, so hydrostatic equilibrium is **stable**. If the heavier fluid is on top, $\Delta E<0$: overturn releases energy and the equilibrium is **unstable** (slide 39: unstable density stratification is “in equilibrium, but unstable to perturbation”).
>
> **Growth rate (inviscid, small amplitude).** Let fluid 1 (density $\rho_1$) occupy $z>0$ above fluid 2 ($\rho_2$) at $z<0$; interface $z=\eta=\eta_0\mathrm{e}^{\sigma t}\cos kx$. Describe each fluid by a velocity potential $\varphi$ ($\vect v=\nabla\varphi$, $\nabla^2\varphi=0$, decaying away from the interface): $\varphi_1=B_1\mathrm{e}^{-kz}\cos kx \mathrm{e}^{\sigma t}$, $\varphi_2=B_2\mathrm{e}^{kz}\cos kx \mathrm{e}^{\sigma t}$. *Kinematic condition* (interface moves with the fluid): $\partial_t\eta=\partial_z\varphi$ at $z=0$, so $\sigma\eta_0=-kB_1=kB_2$. *Dynamic condition*: pressure is continuous; from the linearised Bernoulli law $P=-\rho(\partial_t\varphi+g\eta)$ at $z=0$, $\rho_1(\sigma B_1+g\eta_0)=\rho_2(\sigma B_2+g\eta_0)$. Substituting $B_1=-\sigma\eta_0/k$, $B_2=\sigma\eta_0/k$:
>
>
> $$
> \sigma^2=A g k,\qquad A=\frac{\rho_1-\rho_2}{\rho_1+\rho_2}  (\text{Atwood number}).
> $$
>
>
> If $\rho_1>\rho_2$ (heavy over light) $\sigma$ is real and positive: exponential growth with rate $\sqrt{Agk}$, fastest at the *shortest* wavelengths (viscosity and surface tension cut this off in reality). If $\rho_1<\rho_2$, $\sigma$ is imaginary: interfacial gravity waves. For a salt layer under sediment or a dense lithospheric root above mantle the same physics governs sinking (salt domes, slide 13).


![[pre_038.jpg|460]] ![[pre_039.jpg|460]]


> [!example] 🖼 Reading the diagram: Slides 38–39: Rayleigh–Taylor images
> Slide 38 shows a still from a laboratory video of green fluid structures growing from a boundary layer while the growth “decelerates due to the effect of the stable stratification”: the ambient is stable, so as the plumes rise they do work against buoyancy and slow down. Slide 39 (left) shows four snapshots of a numerical Rayleigh–Taylor simulation (yellow = heavy fluid below? blue = fluid above): a sinusoidal perturbation of the interface grows into a downgoing finger of one fluid and rising bubbles of the other, whose heads roll up into mushroom shapes (secondary Kelvin–Helmholtz instability) until the region mixes. Slide 39 (right) is a glass of water with a layer of dyed fluid: the coloured layer breaks into finger-like drips. In all cases the initial exponential growth $\mathrm{e}^{\sigma t}$ is followed by nonlinear, mixing behaviour.


### Stress in a solid at rest (slides 45–46)

> [!figure]- 🖼 Slides 45–46: open to see the slides this section explains
> ![[pre_045.jpg|300]] ![[pre_046.jpg|300]]


> [!key] 🛠 Tool: Stress and traction; equilibrium of a 2-D element
> Inside a material, the force per unit area exerted across an imaginary surface is the *traction*. Cutting a small square element with edges $\mathrm{d} x,\mathrm{d} y$ (unit depth $\mathrm{d} z$) produces four faces. Let $\sigma_{xx}$ denote the traction component normal to a face perpendicular to $x$ (compressive positive) and $\sigma_{xy}$ the component along $x$ acting on a face perpendicular to $y$ (and $\sigma_{yx}$ the component along $y$ on a face perpendicular to $x$). These four numbers $\sigma_{xx},\sigma_{xy},\sigma_{yx},\sigma_{yy}$ (the *stress tensor*) determine the traction on any face.


![[ls_fig06.png]]
*Figure LS02.5. Slides 45–46: forces on a solid element at rest with compressive-positive stress. Normal stresses (blue) push into the element; shear tractions (red) act along faces; weight (green) acts along $-y$.*


> [!derivation] 🟢 In the slides: Slides 45–46: Stokes' (equilibrium) equations for a solid at rest
> *Along $x$* (panel a). The left face at $x$ is pushed in $+x$ by $\sigma_{xx}(x) \mathrm{d} y \mathrm{d} z$, the right face in $-x$ by $\sigma_{xx}(x+\mathrm{d} x) \mathrm{d} y \mathrm{d} z$; the bottom face is dragged in $+x$ by $\sigma_{xy}(y)\mathrm{d} x \mathrm{d} z$ and the top face in $-x$ by $\sigma_{xy}(y+\mathrm{d} y)\mathrm{d} x \mathrm{d} z$. Sum $=0$ (the slide's equation):
>
>
> $$
> \sigma_{xy}(y)\mathrm{d} x\mathrm{d} z-\sigma_{xy}(y+\mathrm{d} y)\mathrm{d} x\mathrm{d} z+\sigma_{xx}(x)\mathrm{d} y\mathrm{d} z-\sigma_{xx}(x+\mathrm{d} x)\mathrm{d} y\mathrm{d} z=0 .
> $$
>
>
> Divide by $\mathrm{d} x \mathrm{d} y \mathrm{d} z$ and use Taylor ($f(y+\mathrm{d} y)-f(y)=\partial_yf \mathrm{d} y$):
>
>
> $$
> -\partial_y\sigma_{xy}-\partial_x\sigma_{xx}=0 . \tag{8}
> $$
>
>
> *Along $y$* (panel b), including the weight $-\rho g \mathrm{d} x\mathrm{d} y\mathrm{d} z$:
>
>
> $$
> -\partial_x\sigma_{xy}-\partial_y\sigma_{yy}-\rho g=0 . \tag{9}
> $$
>
>
> These are the slide's two equations. Check: for a fluid at rest, $\sigma_{xx}=\sigma_{yy}=P$, $\sigma_{xy}=0$, and (9) becomes (7) (with $y$ vertical) — hydrostatics is the special case.


> [!example] ❓ Question on the slides: Slide 46: solid at rest with zero net *torque*?
> Take moments about the centre of the element. The vertical shear tractions on the two $x$-faces (each of size $\sigma_{yx}\mathrm{d} y\mathrm{d} z$, lever arm $\mathrm{d} x/2$, both turning the element the same way) give a moment $\sigma_{yx} \mathrm{d} x \mathrm{d} y \mathrm{d} z$ in one sense; the horizontal shear tractions on the two $y$-faces give $\sigma_{xy} \mathrm{d} x \mathrm{d} y \mathrm{d} z$ in the opposite sense. The normal tractions and the weight act through (or symmetrically about) the centre and give no moment to leading order; the rotational inertia of the element is of size $\mathrm{d} V (\mathrm{d} x^2+\mathrm{d} y^2)$, negligible compared with $\mathrm{d} V$ as the element shrinks. Hence $\sigma_{xy}=\sigma_{yx}$: **the stress tensor is symmetric**, which is why the slide can use a single shear stress $\sigma_{xy}$ throughout.


> [!derivation] 🔵 Extra (not derived in the slides): The “one missing equation”: statical indeterminacy and the Airy stress function
> The slide notes: “one missing equation! Add a compatibility condition”. Count: three unknown fields $\sigma_{xx},\sigma_{xy},\sigma_{yy}$ but only two equations ((8)–(9)). Force balance alone cannot determine stress: many stress fields balance the same loads. Extra information about *how the material deforms* must be added. A neat way to see the structure: define a scalar $\Phi(x,y)$ (Airy stress function) with $\sigma_{xx}=\partial_y^2\Phi$, $\sigma_{xy}=-\partial_x\partial_y\Phi$, $\sigma_{yy}=\partial_x^2\Phi-\rho gy$. Direct substitution shows both (8) and (9) are satisfied identically ($\partial_x\partial_y^2\Phi-\partial_x\partial_y^2\Phi=0$ and $\rho g-\rho g=0$). Equilibrium therefore fixes nothing about $\Phi$. The missing condition is that the strains derived from the stresses (through Hooke's law for an elastic solid) come from a single-valued displacement field — the *compatibility condition*, which for plane strain reads $\nabla^4\Phi=\partial_x^4\Phi+2\partial_x^2\partial_y^2\Phi+\partial_y^4\Phi=0$ (T&S Ch. 3, 8). For a viscous fluid the missing information is Newton's law of viscosity (next section) with velocity as extra unknown.


## Viscous flow (slides 47–49)

> [!figure]- 🖼 Slides 47–49: open to see the slides this section explains
> ![[pre_047.jpg|300]] ![[pre_048.jpg|300]] ![[pre_049.jpg|300]]


> [!key] Definition: Newtonian viscosity
> Shear a fluid layer between a fixed plate and a plate moving at speed $V$, gap $H$. The velocity varies linearly, $v_x=Vy/H$. A fluid is *Newtonian* if the shear stress needed is proportional to the velocity gradient: $\tau=\mu \mathrm{d} v_x/\mathrm{d} y$, the constant $\mu$ being the *dynamic viscosity* (Pa s). Other viscosities ($\eta$ in some books) are the same $\mu$. In the slides' sign convention (compression positive), $\sigma_{xy}=-\mu \partial_yv_x$.


| Material | $\mu$ (Pa s) | Material | $\mu$ (Pa s) |
|---|---|---|---|
| water | $10^{-3}$ | pitch (slide 59) | $\sim10^{8}$ |
| honey | $\sim10$ | glacier ice (effective, §14.4) | $\sim10^{13}$–$10^{14}$ |
| basalt lava | $10^{2}$–$10^{5}$ | Earth's upper mantle | $\sim10^{20}$–$10^{21}$ |
| mud/debris flow | $10^{1}$–$10^{3}$ | lower mantle | $\sim10^{21}$–$10^{23}$ |

*Viscosities spanning 26 orders of magnitude. The mantle is a fluid on geological time scales (Chapter 7).*


![[ls_fig07.png]]
*Figure LS02.6. Slides 47–49: steady flow of a viscous layer on an infinite slab inclined at $\theta$. Velocity is zero at the bed (no slip), maximal at the free surface, where the shear traction vanishes.*


> [!derivation] 🟢 In the slides: Slides 47–49: exact solution for steady Newtonian flow down a slope
> Axes: $x$ down-slope, $y$ normal to the bed; the layer has thickness $H$ and nothing varies with $x$ (“infinite slab”). Gravity has components $+g\sin\theta$ along $x$ and $-g\cos\theta$ along $y$. Equilibrium of an element (with weight components, (8)–(9) and $\partial_x=0$):
>
>
> $$
> \begin{aligned}
> -\partial_y\sigma_{xy}+\rho g\sin\theta&=0,\\
> -\partial_y\sigma_{yy}-\rho g\cos\theta&=0.
> \end{aligned} \tag{10}
> $$
>
>
> (The slide divides by $\rho$.) Constitutive law with $v_y=0$: $\sigma_{xy}=-\mu \partial_yv_x$. Substituting into (10):
>
>
> $$
> \mu \partial_y^2v_x+\rho g\sin\theta=0\quad\Longrightarrow\quad v_x=-\frac{\rho g\sin\theta}{2\mu}y^2+c_1y+c_0 .
> $$
>
>
> *Boundary conditions*: no slip at the bed, $v_x(0)=0\Rightarrow c_0=0$; at the free surface the shear traction of the air is zero, $\sigma_{xy}(H)=0\Rightarrow\partial_yv_x(H)=0\Rightarrow c_1=\rho g\sin\theta H/\mu$. Hence
>
>
> $$
> \boxed{\,v_x(y)=\frac{\rho g\sin\theta}{\mu}\Big(Hy-\frac{y^2}{2}\Big)\,}\qquad U_s=v_x(H)=\frac{\rho g\sin\theta\,H^2}{2\mu},\quad q=\int_0^Hv_x\,\mathrm{d} y=\frac{\rho g\sin\theta\,H^3}{3\mu}. \tag{11}
> $$
>
>
> The shear stress $-\sigma_{xy}=\rho g\sin\theta (H-y)$ increases linearly to the bed value $\tau_b=\rho g H\sin\theta$ — simply the down-slope weight of the overlying column per unit area, as it must be. The normal stress from (10) with $\sigma_{yy}(H)=0$ is $\sigma_{yy}=\rho g\cos\theta (H-y)$ (the lithostatic pressure with $g\to g\cos\theta$).
>
>
> *Slide 48's scaling argument.* The viscous shear stress is $\sim\mu v/H$ and its gradient (force per volume) $\sim(\mu v/H)/H$; setting this equal to the gravitational driving $\rho g\sin\theta$ gives $v\sim\rho g\sin\theta H^2/\mu$, agreeing with (11) up to the factor $\tfrac12$. *Sign remark*: the slide prints $-\mu\partial_y^2v_x+g\sin\theta=0$ and $v_x\propto(y^2/2-Hy)$, which describes flow *up* the slope for the axes drawn; the sign in front of $\mu\partial_y^2v_x$ must be $+$ once $\sigma_{xy}=-\mu\partial_yv_x$, as above; slide 144 gives the correct positive form.


> [!example] 🧮 Worked example: A Newtonian “glacier”
> Ice with $\mu=10^{13}$ Pa s, $H=100$ m, $\theta=3^\circ$ ($\sin\theta=0.0523$), $\rho=917$: $U_s=917\cdot9.8\cdot0.0523\cdot10^4/(2\cdot10^{13})=2.3\times10^{-7} \mathrm{m s^{-1}}\approx7 \mathrm{m yr^{-1}}$: the right order of magnitude for a temperate glacier. Chapter 14 shows the real, nonlinear rheology changes the $H$-dependence.


> [!intuition] Why inertia can be dropped
> The ratio of inertial to viscous forces is the Reynolds number $\mathrm{Re}=\rho UL/\mu$. For the slab above $\mathrm{Re}\sim917\cdot10^{-7}\cdot100/10^{13}\sim10^{-15}$; for mantle flow $\mathrm{Re}\sim10^{-20}$. Acceleration terms $\rho \mathrm{d}\vect v/\mathrm{d} t$ are then utterly negligible, which is why the force balance of slides 45–49 has no acceleration: the flow is always in instantaneous equilibrium with its driving forces (Stokes flow).

## Further slides explained one by one
<span class="scope-taught">taught</span> *the slides of this chapter's range that carry no derivation of their own; each image is followed by what it shows*

![[pre_037.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 37: Hydrostatic force balance (steady case)
> A small rectangular element of fluid (orange) between heights $z$ and $z+dz$ with the pressure $P(z)$ pushing up on its bottom face, $P(z+dz)$ pushing down on its top face and gravity $g$ acting down. With zero net force (fluid at rest) $P(z)-P(z+dz)-\rho g\,dz=0$, i.e. $dP/dz=-\rho g$, the hydrostatic equation derived in this chapter and used throughout (isostasy, lithostatic pressure).


## Map of this chapter
> [!connection] How LS02 connects
> **Previous:** [[LS01 Landscapes as Physical Systems]] · **Next:** [[LS03 Digital Elevation Models and Terrain Analysis]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 35–38, 45–50 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].
