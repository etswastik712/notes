"""QM02 - which functions can be states? Six candidates from Lecture 8 / Tutorial problem 1: |psi|^2 and the verdict."""
from figlib import *

x = np.linspace(-6, 6, 1201)
cases = [
    (r"$e^{-ax^2}$", np.exp(-2 * x ** 2 / 2), "allowed", AQUA, "$\\int|\\psi|^2$ finite"),
    (r"$e^{-a|x|}$", np.exp(-2 * abs(x)), "allowed as a state", AQUA, "cusp: needs a delta-type $V$"),
    (r"$e^{ax^2}$ (growing)", np.exp(0.3 * x ** 2) / np.exp(0.3 * 36), "not allowed", RED, "$\\int|\\psi|^2=\\infty$"),
    (r"$1/\sqrt{1+|x|}$", 1 / (1 + abs(x)), "not allowed", RED, "$|\\psi|^2\\sim1/|x|$: log divergence"),
    (r"$1/(1+|x|)$", 1 / (1 + abs(x)) ** 2, "allowed", AQUA, "$|\\psi|^2\\sim1/x^2$ converges"),
    (r"$1/x$ through $x=0$", np.minimum(1 / np.where(abs(x) < 1e-6, 1e-6, x) ** 2, 30), "not allowed", RED, "$|\\psi|^2\\sim1/x^2$ at the origin"),
]
fig, axes = plt.subplots(2, 3, figsize=(10.6, 5.4))
for ax, (name, f, verdict, col, why) in zip(axes.ravel(), cases):
    ax.fill_between(x, f, color=col, alpha=0.18); ax.plot(x, f, color=col, lw=1.8)
    ax.set_title(name + "  ($|\\psi|^2$)", fontsize=9.5); ax.set_yticks([]); ax.set_xticks([])
    ax.text(0.5, -0.12, verdict + ": " + why, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=INK)
    ax.set_ylim(0, max(f.max() * 1.1, 1e-3)); ax.set_xlim(-6, 6); ax.grid(False)
fig.tight_layout(h_pad=3.2)
fig.text(0.5, -0.02, "Square-integrability is the probability requirement; extra smoothness depends on the Hamiltonian. The growing and $1/x$ curves are clipped at the plot edge.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm02_admissible")
