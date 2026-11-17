---
id: ph2113/2026-11-16-circular-well-2d-and-density-notebook
aliases: [Circular infinite well, 2-d Schrödinger example]
tags: [ph2113, lecture-notes]
trust_tier: agent_written
---

# Schrödinger equation in two dimensions: the circular infinite well (notes and Python notebook)

## Covered
**Setup** (Classroom: Angular_momentum.pdf, "Schrodinger Equation in Two Dimensions: An Example"). Potential $V=0$ for $x^2+y^2<a^2$, $V=\infty$ otherwise; it depends only on $r=\sqrt{x^2+y^2}$ (circular symmetry). In polar coordinates
$$-\frac{\hbar^2}{2m}\left[\partial_r^2\psi+\frac1r\partial_r\psi+\frac1{r^2}\partial_\theta^2\psi\right]+V(r)\psi=E\psi,$$
and inside the well the $V$ term drops.

**Separation.** $\psi=R(r)\Theta(\theta)$. The angular momentum operator commutes with $\hat H$ here, so $\Theta$ is an eigenfunction of it: $\Theta(\theta)=e^{il\theta}$, $l$ an integer, eigenvalue $\hbar l$. The radial equation becomes
$$\frac1R\frac{d^2R}{dr^2}+\frac1{rR}\frac{dR}{dr}-\frac{l^2}{r^2}=-k^2,\qquad E=\frac{\hbar^2k^2}{2m}.$$

**Solution.** Bessel functions (they appear in problems with cylindrical symmetry; the sheet says you will meet them again in Math Methods II and Optics): $R(r)=AJ_l(kr)+BY_l(kr)$. Finite at $r=0$ gives $B=0$; vanishing at $r=a$ gives $J_l(ka)=0$, so $k_{n,l}=j_{l,n}/a$ with $j_{l,n}$ the $n$-th root of $J_l$, and
$$E_{n,l}=\frac{\hbar^2k_{n,l}^2}{2m},\qquad \psi(r,\theta)=J_l(k_{n,l}r)\,e^{il\theta}.$$
The sheet also points to the Wolfram demonstration "Particle in an infinite circular well" and plots the first Bessel functions and their roots.

**Notebook** (Classroom: circular_well_density.ipynb; its text, not outputs, was read):
- Normalised states $\psi_{n,l}=N_{n,l}J_l(k_{n,l}r)e^{il\theta}$, with $\int_0^aJ_l^2(kr)\,r\,dr=\tfrac{a^2}2J_{l+1}^2(ka)$ when $J_l(ka)=0$, giving $|N_{n,l}|^2=\dfrac1{\pi a^2J_{l+1}^2(j_{l,n})}$.
- Since $|e^{il\theta}|^2=1$, an $L_z$ eigenstate has a circularly symmetric density (rings, not lobes). The states $\pm l$ are degenerate, so $\cos l\theta$ and $\sin l\theta$ combinations are also energy eigenstates (not $L_z$ eigenstates) and show $2l$ angular lobes; the code uses $\sqrt2\cos l\theta$ for $l\neq0$ to keep the norm.
- Energies in units of $\hbar^2/2ma^2$ are $E=j_{l,n}^2$; number of radial nodes is $n-1$ (not counting the wall); every level with $l\neq0$ is doubly degenerate ($\pm l$).
- Code (numpy, scipy `jv`, `jn_zeros`, matplotlib, Plotly): a normalisation check (should print about 1), a 3-d plus top-view density plot, a Plotly slider explorer over states $(n,l)$ ordered by energy for both the $e^{il\theta}$ and $\cos l\theta$ forms, a gallery for $n=1..3$, $l=0..3$, and an energy-level diagram. The notebook needs Plotly (`conda install -c conda-forge plotly`).

## From the post
Notes and python notebook for this week and last.

## Files
- [Angular_momentum.pdf](https://drive.google.com/file/d/1WovsR8KEycnh38UBnb1e02fauQeZ4W-r/view?usp=drive_web) (the circular-well example; read in full)
- [circular_well_density.ipynb](https://drive.google.com/file/d/1L5RzSfTMME_bXaJVCyVwv2kLWzsVuezz/view?usp=drive_web) (notebook; read as text)

## Related
- [[ph2113/2026-11-16-angular-momentum-2d-handwritten-notes]]: the lecture derivation of $e^{il\theta}$ and the radial equation
- [[ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator]]: same polar equation and radial equation for the 2-d oscillator
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: the 1-d infinite well this generalises
- [[ph2113/2026-08-25-lecture-9-free-particle-ring-general-properties]]: single-valuedness giving integer $l$ on a ring
- [[06-quantum-mechanics/concepts/angular-momentum-algebra]]: their own concept note on angular momentum

<!-- kurooto:material02cb5e79 -->
## Concepts in circular_well_density
[[zettel/circular-infinite-well-potential-in-two-dimensions]], [[zettel/circular-well-normalization-constant]], [[zettel/angular-wavefunction-representations-in-circular-wells]]
<!-- /kurooto:material02cb5e79 -->
