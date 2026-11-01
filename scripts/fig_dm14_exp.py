"""DM14 - exp: sl(2,R) -> SL(2,R) is not onto, the Trotter product formula, and the one-parameter subgroups of T^2."""
from figlib import *
from scipy.linalg import expm

fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.4), gridspec_kw=dict(width_ratios=[1.05, 1.0, 1.0]))
r = np.random.default_rng(14)

# A: traces of exp(A), A in sl(2,R) ---------------------------------------------------------------------------------------------------------------------
a = axes[0]
N = 60000
x_, y_, z_ = r.normal(size=(3, N)) * r.uniform(0.2, 4, size=N)
mu2 = x_ ** 2 + y_ * z_
tr = np.where(mu2 > 0, 2 * np.cosh(np.sqrt(np.abs(mu2))), 2 * np.cos(np.sqrt(np.abs(mu2))))
a.hist(tr[tr <= 14], bins=np.linspace(-4, 14, 120), color=BLUE, alpha=0.85)
a.axvspan(-4, -2, color=RED, alpha=0.16)
a.axvline(-2, color=RED, lw=1.4)
a.scatter([-2.5], [0], color=RED, s=60, zorder=5, clip_on=False)
a.text(-3.9, a.get_ylim()[1] * 0.55, "tr < −2:\nno A with\ne^A of this trace", fontsize=8.6, color=RED)
a.text(-3.9, a.get_ylim()[1] * 0.2, "diag(−2, −½) ∈ SL(2,ℝ)\nhas trace −2.5", fontsize=8.2, color=RED)
a.set_xlabel("tr e^A,  A ∈ sl(2,ℝ) random"); a.set_ylabel("count")
a.set_title("A  exp: sl(2,ℝ) → SL(2,ℝ) is not onto", fontsize=9.8)

# B: Trotter product formula ---------------------------------------------------------------------------------------------------------------------------
b = axes[1]
X, Y = r.normal(size=(3, 3)), r.normal(size=(3, 3))
ns = np.array([10, 30, 100, 300, 1000, 3000, 10000])
err = [np.abs(np.linalg.matrix_power(expm(X / n) @ expm(Y / n), n) - expm(X + Y)).max() for n in ns]
b.loglog(ns, err, "o-", color=ORANGE, lw=2.0, label=r"$\|(e^{X/n}e^{Y/n})^n-e^{X+Y}\|$")
b.loglog(ns, err[0] * ns[0] / ns, "--", color=MUTED, lw=1.2, label="slope −1")
e1 = np.abs(expm(X) @ expm(Y) - expm(X + Y)).max()
b.axhline(e1, color=RED, lw=1.2, ls=":")
b.text(12, e1 * 0.55, r"$n=1$: $\|e^Xe^Y-e^{X+Y}\|=%.1f$" % e1, fontsize=8.2, color=RED)
b.set_xlabel("n"); b.set_ylabel("error")
b.legend(fontsize=8, loc="lower left")
b.set_title("B  (exp(X/n) exp(Y/n))ⁿ → exp(X+Y)", fontsize=9.8)

# C: one-parameter subgroups of T^2 = R^2 / Z^2 ----------------------------------------------------------------------------------------------------------
c = axes[2]
def torus_line(a_, b_, T, n=4000):
    t = np.linspace(0, T, n)
    x = (a_ * t) % 1; y = (b_ * t) % 1
    brk = np.where((np.abs(np.diff(x)) > 0.5) | (np.abs(np.diff(y)) > 0.5))[0] + 1
    xs, ys = np.insert(x, brk, np.nan), np.insert(y, brk, np.nan)
    return xs, ys
xs, ys = torus_line(2, 3, 1.0, 2000)
c.plot(xs, ys, color=BLUE, lw=2.2, label="(a,b) = (2,3): closed, period 1 (S¹)")
xs, ys = torus_line(1, np.sqrt(2), 14.0, 20000)
c.plot(xs, ys, color=ORANGE, lw=0.8, alpha=0.85, label="(a,b) = (1,√2): injective, dense (ℝ)")
c.scatter([0.0], [0.0], color=INK, s=34, zorder=5)
c.text(0.03, 0.03, "e  (a,b) = (0,0): constant", fontsize=8.0)
c.set_xlim(0, 1); c.set_ylim(0, 1); c.set_aspect("equal")
c.legend(fontsize=7.4, loc="upper center", bbox_to_anchor=(0.5, -0.08))
c.set_title("C  one-parameter subgroups of T²", fontsize=9.8)

fig.tight_layout()
fig.text(0.5, -0.04, "A: trace of e^A for 60000 random A ∈ sl(2,ℝ) (values above 14 not shown): it never falls below −2 (closed form 2cosh μ or 2cos ω). B: Lee Cor. 20.11, error decays like 1/n. "
         "C: HW9 Q1: the image is a circle, a dense line or a point. Numbers: dm_numbers.py (DM14).", ha="center", fontsize=7.8, color=MUTED)
save(fig, "fig_dm14_exp")
