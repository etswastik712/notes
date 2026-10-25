"""QM01 - double slit: amplitudes add, probabilities do not; and the pattern builds up one electron at a time (my simulation)."""
from figlib import *

rng = np.random.default_rng(7)
y = np.linspace(-3, 3, 2001)
w, lam = 1.4, 0.55                      # envelope width, fringe spacing (arbitrary screen units)
g = np.exp(-y ** 2 / (2 * w ** 2))
delta = 2 * np.pi * y / lam
psiA = g * np.exp(1j * delta / 2); psiB = g * np.exp(-1j * delta / 2)
P_wave = np.abs(psiA + psiB) ** 2
P_cl = np.abs(psiA) ** 2 + np.abs(psiB) ** 2
Z = np.trapezoid(P_wave, y)

fig = plt.figure(figsize=(11.2, 4.4))
gs = fig.add_gridspec(2, 3, width_ratios=[1.35, 1, 1], hspace=0.55, wspace=0.38)
a = fig.add_subplot(gs[:, 0])
a.plot(y, P_cl / Z, color=ORANGE, label=r"$|\psi_A|^2+|\psi_B|^2$ (add probabilities)")
a.plot(y, P_wave / Z, color=BLUE, label=r"$|\psi_A+\psi_B|^2$ (add amplitudes)")
a.set_xlabel("position on the screen (arbitrary units)"); a.set_ylabel("probability density")
a.legend(fontsize=8.4, loc="upper right", bbox_to_anchor=(1.0, 1.02))
a.set_title("A  dark fringes: where $\\psi_A+\\psi_B=0$", fontsize=10)
a.set_ylim(0, 1.22 * (P_wave / Z).max())
zeros = lam * (np.arange(-5, 5) + 0.5)
zeros = zeros[abs(zeros) < 2.9]
a.plot(zeros, np.zeros_like(zeros), "o", mfc=SURFACE, mec=INK, ms=5, zorder=6)
a.text(1.25, 0.56, "circles: dark fringes,\nprobability exactly 0\n(each slit alone would\nsend electrons there)", fontsize=8.0, color=MUTED, va="center")
cdf = np.cumsum(P_wave); cdf /= cdf[-1]
for k, (N, pos) in enumerate(((30, (0, 1)), (300, (1, 1)), (5000, (0, 2)))):
    pass
panels = [(30, gs[0, 1]), (300, gs[1, 1]), (6000, gs[0, 2]), (60000, gs[1, 2])]
for N, spec in panels:
    ax = fig.add_subplot(spec)
    hits = np.interp(rng.random(N), cdf, y)
    if N <= 300:
        ax.plot(hits, rng.random(N) * 0.8, ".", color=BLUE, ms=3.2, alpha=0.8); ax.set_yticks([]); ax.set_ylim(0, 1)
    else:
        ax.hist(hits, bins=60, color=BLUE, alpha=0.85, density=True); ax.set_yticks([])
        ax.plot(y, P_wave / Z, color=INK, lw=0.9)
    ax.set_title(f"{N:,} electrons", fontsize=9)
    ax.set_xlim(-3, 3); ax.grid(False)
    if spec in (gs[1, 1], gs[1, 2]):
        ax.set_xlabel("screen position", fontsize=8.5)
fig.suptitle("B  single flashes, wave statistics", x=0.745, y=1.0, fontsize=10, fontweight="semibold")
fig.text(0.5, -0.04, "Left: two-slit model with equal slit amplitudes (Gaussian envelope, fringe spacing 0.55); both curves normalised alike. "
         "Right: electrons drawn at random from $|\\psi_A+\\psi_B|^2$, my simulation, not an experiment.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm01_double_slit")
