---
id: ph2113/2026-10-26-tutorial-iv-finite-well-practice
aliases: [Tutorial IV finite well practice question]
tags: [ph2113, tutorial, finite-well]
trust_tier: agent_written
---

# Tutorial IV: exact shape of $k/k_0$ for the finite well (2026-10-26)

## Covered
Single practice question on the finite square well $-a\le x\le a$, depth/height $V_0$ (Classroom: tutorial4.pdf).
- Even bound states satisfy $\tan(k_0a)=\dfrac{k}{k_0}$ (eq. 1), with $k_0=\sqrt{2mE}/\hbar$ (inside) and $k=\sqrt{2m(V_0-E)}/\hbar$ (outside, decay constant).
- In class this was solved graphically with an approximate shape for $k/k_0$. The task: plot the exact shape of $k/k_0$ against $k_0a$ by examining its values and derivatives at various points.

Worked outline (mine, not in the post; check before relying on it). Put $z=k_0a$ and $z_0^2=2mV_0a^2/\hbar^2$. Since $k^2+k_0^2=2mV_0/\hbar^2$,
$$f(z)=\frac{k}{k_0}=\frac{\sqrt{z_0^2-z^2}}{z},\qquad 0<z\le z_0 .$$
- $f\to\infty$ as $z\to0^+$ (like $z_0/z$); $f(z_0)=0$.
- $f'(z)=-\dfrac{z_0^2}{z^2\sqrt{z_0^2-z^2}}<0$: strictly decreasing; $f'\to-\infty$ at $z=z_0$ (vertical tangent), $f'\to-\infty$ as $z\to0^+$ too.
- $f''(z)=\dfrac{z_0^2\,(2z_0^2-3z^2)}{z^3(z_0^2-z^2)^{3/2}}$: convex for $z<z_0\sqrt{2/3}$, concave after, inflection at $z=z_0\sqrt{2/3}$.
- Even levels are the intersections of $\tan z$ with $f(z)$ on $(0,z_0]$.

## From the post
Even though we will have the quiz in this week's tutorial slot, I am attaching a practice question on this week's material.

## Files
- [tutorial4.pdf](https://drive.google.com/file/d/1cjhTnmrljivVryb2fbmp3ZwvMZ5eH5Z4/view?usp=drive_web) (read in full); post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODk1NzYzNzM1NTg1

## Related
- [[ph2113/2026-10-27-finite-well-notes]]: the lecture notes this question comes from
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: infinite-well limit ($z_0\to\infty$)
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: matching conditions at a finite jump in $V$
