"""PR05 - Week 2: geometric -> exponential, the maximum of exponentials -> Gumbel, the folded normal."""
from figlib import *
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(12.4, 3.9))

# A: geometric survival function -> exponential survival function
a = axes[0]
lam = 1.0
x = np.linspace(0, 5, 400)
a.plot(x, np.exp(-lam * x), color=INK, lw=2.2, label=r"$e^{-\lambda x}$ (limit)")
for h, c in zip((0.5, 0.2, 0.05), (ORANGE, AQUA, VIOLET)):
    q = 1 - lam * h                      # per-step failure probability, success p = lam h
    k = np.arange(0, int(5 / h) + 1)
    a.step(k * h, q ** k, where="post", color=c, lw=1.6, label=rf"$P(G\geq k)=q^k$, $h={h}$")
a.set_xlabel(r"$x=kh$"); a.set_ylabel(r"$P(X\geq x)$"); a.set_xlim(0, 5)
a.legend(fontsize=8, loc="upper right")
a.set_title(r"A  geometric steps $\to$ exponential", fontsize=10)

# B: maximum of n exponentials, shifted by ln n, against Gumbel
b = axes[1]
y = np.linspace(-2.5, 6, 500)
for n, c in zip((1, 2, 5, 20), (ORANGE, AQUA, VIOLET, BLUE)):
    F = np.where(y + np.log(n) > 0, (1 - np.exp(-(y + np.log(n)))) ** n, 0.0)
    b.plot(y, F, color=c, lw=1.5, label=f"$n={n}$")
b.plot(y, np.exp(-np.exp(-y)), color=INK, lw=2.2, ls="--", label=r"Gumbel $e^{-e^{-y}}$")
b.set_xlabel(r"$y$"); b.set_ylabel(r"$P(M_n-\ln n\leq y)$")
b.legend(fontsize=8, loc="lower right")
b.set_title(r"B  $\max-\ln n\to$ Gumbel", fontsize=10)

# C: folded normal
c_ = axes[2]
z = np.linspace(-4, 4, 800)
c_.plot(z, stats.norm.pdf(z), color=MUTED, lw=1.4, ls=":", label="$Z\\sim N(0,1)$")
yy = np.linspace(0, 4, 400)
c_.plot(yy, 2 * stats.norm.pdf(yy), color=BLUE, lw=2.2, label=r"$|Z|$: $f(y)=\frac{2}{\sqrt{2\pi}}e^{-y^2/2}$")
m = np.sqrt(2 / np.pi)
c_.axvline(m, color=ORANGE, lw=1.4)
c_.text(m + 0.08, 0.72, rf"$E|Z|=\sqrt{{2/\pi}}={m:.4f}$", color=INK, fontsize=8.6)
c_.text(1.4, 0.55, rf"$\mathrm{{Var}}=1-2/\pi={1 - 2 / np.pi:.4f}$", fontsize=8.6)
c_.set_xlim(-4, 4); c_.set_ylim(0, 0.9); c_.set_xlabel("$y$")
c_.legend(fontsize=8, loc="upper left")
c_.set_title("C  the folded normal doubles the right half", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: $p=\\lambda h$, $q=1-\\lambda h$, $k=x/h$: $(1-\\lambda h)^{x/h}\\to e^{-\\lambda x}$ (at $\\lambda=1/2$, $x=2$: $0.3164,\\ 0.3585,\\ 0.3670,\\ 0.3678$ for $h=0.5,0.1,0.01,0.001$; limit $0.3679$). "
         "B: $(1-e^{-y}/n)^n$ at $y=0.5$: $0.393,\\ 0.485,\\ 0.524,\\ 0.540$ for $n=1,2,5,20$; Gumbel $0.5452$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pr05_exp_gumbel")
