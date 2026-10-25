"""PR05 - continuous random variables: Rayleigh (quartiles), the normal curve, and E[Y] = integral of P(Y>y)."""
from figlib import *
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.9))
a = axes[0]
x = np.linspace(0, 4, 500)
a.plot(x, x * np.exp(-x ** 2 / 2), color=BLUE, label=r"pdf $f=xe^{-x^2/2}$")
a.plot(x, 1 - np.exp(-x ** 2 / 2), color=ORANGE, label=r"cdf $F=1-e^{-x^2/2}$")
for q, lab in zip((0.25, 0.5, 0.75), ("$q_1$", "median", "$q_3$")):
    xq = np.sqrt(-2 * np.log(1 - q)); a.plot([xq, xq], [0, q], color=MUTED, lw=0.8, ls=":"); a.plot([0, xq], [q, q], color=MUTED, lw=0.8, ls=":"); a.text(xq + 0.04, {0.25: 0.03, 0.5: 0.10, 0.75: 0.17}[q], f"{xq:.3f}", fontsize=8.0)
a.fill_between(x, 0, x * np.exp(-x ** 2 / 2), where=(x > 1) & (x < 3), color=BLUE, alpha=0.18)
a.text(2.05, 0.30, "$P(1<X<3)=0.595$", fontsize=8.4); a.set_xlabel("$x$"); a.legend(fontsize=8.2, loc="upper right", bbox_to_anchor=(1.0, 0.8)); a.set_title("A  Rayleigh: cdf first, pdf by differentiation", fontsize=10)
b = axes[1]
z = np.linspace(-4, 4, 600)
b.plot(z, stats.norm.pdf(z), color=INK)
for k, c, al in ((3, VIOLET, 0.12), (2, AQUA, 0.18), (1, BLUE, 0.25)):
    m = abs(z) <= k; b.fill_between(z[m], 0, stats.norm.pdf(z[m]), color=c, alpha=al)
for xi in (-1, 1): b.plot([xi], [stats.norm.pdf(1)], "o", color=ORANGE, ms=6)
b.annotate("inflection\nat $\\pm1$", (1, stats.norm.pdf(1)), xytext=(1.7, 0.31), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.text(0, 0.14, "68.3 %", ha="center", fontsize=8.4, color="white"); b.text(0, 0.03, "", fontsize=8)
b.text(-3.9, 0.36, "95.4 % within $\\pm2$,\n99.7 % within $\\pm3$", fontsize=8.2)
b.set_xlabel("$z$"); b.set_title("B  standard normal, $\\int e^{-x^2/2}\\mathrm{d}x=\\sqrt{2\\pi}$", fontsize=10)
c = axes[2]
y = np.linspace(0, 1, 400)
c.plot(y, 1 - np.sqrt(y), color=BLUE, label=r"$P(Y>y)=1-\sqrt{y}$, $Y=X^2$, $X\sim U(0,1)$")
c.fill_between(y, 0, 1 - np.sqrt(y), color=BLUE, alpha=0.18); c.text(0.18, 0.12, r"area $=\int P(Y>y)\,\mathrm{d}y=\frac{1}{3}=E[Y]$", fontsize=8.6)
c.set_xlabel("$y$"); c.set_ylim(0, 1.05); c.legend(fontsize=8.0, loc="upper right"); c.set_title(r"C  $E[Y]=\int_0^\infty P(Y>y)\,\mathrm{d}y$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: quartiles $0.7585,\\ 1.1774,\\ 1.6651$. B: $\\Phi(1)-\\Phi(-1)=0.6827$, $0.9545$, $0.9973$. C: the layer-cake identity used to prove LOTUS for $g\\geq0$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pr05_continuous")
