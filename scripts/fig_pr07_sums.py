"""PR07 - convolution of two normals, the parabola Var(X+tY), and E|X-Y| for iid standard normals."""
from figlib import *
from scipy import stats

rng = np.random.default_rng(7)
fig, axes = plt.subplots(1, 3, figsize=(12.2, 3.8))

a = axes[0]
x = np.linspace(-6, 7, 600)
m1, s1, m2, s2, z = 1.0, 2.0, -0.5, 1.5, 2.0
fx = stats.norm.pdf(x, m1, s1); fy = stats.norm.pdf(z - x, m2, s2)
a.plot(x, fx, color=BLUE, lw=1.4, label=r"$f_X(x)$")
a.plot(x, fy, color=ORANGE, lw=1.4, label=r"$f_Y(z-x)$, $z=2$")
a.fill_between(x, fx * fy, color=AQUA, alpha=0.55, label=r"product $f_X(x)f_Y(z-x)$")
a.set_xlabel("$x$"); a.set_yticks([]); a.legend(fontsize=8.2, loc="upper left")
a.text(0.97, 0.55, "shaded area" + "\n" + r"$=f_{X+Y}(2)=0.1333$", transform=a.transAxes, ha="right", fontsize=8.2, color=INK)
a.set_title("A  the convolution integrand", fontsize=10)

b = axes[1]
t = np.linspace(-3.2, 3.2, 400)
for rho, c in ((0.0, BLUE), (0.6, AQUA), (-0.9, ORANGE), (1.0, RED)):
    b.plot(t, 1 + 2 * rho * t + t ** 2, color=c, lw=1.6, label=fr"$\rho={rho:+.1f}$")
b.axhline(0, color=INK, lw=0.8)
b.set_ylim(-0.5, 9); b.set_xlabel("$t$"); b.set_ylabel(r"$\mathrm{Var}(X+tY)$ (unit variances)")
b.legend(fontsize=8.2, loc="upper center")
b.set_title(r"B  $\mathrm{Var}(X+tY)\geq0$ forces $|\rho|\leq1$", fontsize=10)

c = axes[2]
d = np.abs(rng.standard_normal(200000) - rng.standard_normal(200000))
c.hist(d, bins=60, density=True, color=BLUE, alpha=0.55, label=r"$|X-Y|$, simulated")
u = np.linspace(0, 6, 300)
c.plot(u, 2 * stats.norm.pdf(u, 0, np.sqrt(2)), color=ORANGE, lw=2, label=r"$2\,\varphi_{N(0,2)}$: the folded $N(0,2)$")
c.axvline(2 / np.sqrt(np.pi), color=INK, lw=0.9, ls="--"); c.text(1.2, 0.02, r"mean $2/\sqrt{\pi}=1.128$", fontsize=8.2)
c.set_xlim(0, 5); c.set_xlabel("$|X-Y|$"); c.set_ylabel("density"); c.legend(fontsize=8.2, loc="upper right")
c.set_title(r"C  $X-Y\sim N(0,2)$, so $E|X-Y|=2/\sqrt{\pi}$", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: $X\\sim N(1,4)$, $Y\\sim N(-0.5,2.25)$; B: parabola $1+2\\rho t+t^2$ touches zero only at $\\rho=\\pm1$. C: 200,000 seeded draws; numbers in scripts/pr_numbers2.py.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pr07_sums")
