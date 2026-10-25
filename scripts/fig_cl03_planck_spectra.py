"""CL03 - Planck spectra of the Sun (5772 K) and Earth (255 K, 288 K), area-normalised, on a log wavelength axis."""
from figlib import *

lam = np.logspace(-7.3, -3.9, 1500)          # m


def planck(l, T):
    return 2 * H_PL * C_LT**2 / (l**5 * np.expm1(H_PL * C_LT / (l * K_B * T)))


def pi_B(l, T):                               # hemispheric emittance per unit wavelength, W m-2 m-1
    return np.pi * planck(l, T)


fig, ax = plt.subplots(figsize=(7.2, 4.1))
Ts = {"Sun, 5772 K": (5772, BLUE), "Earth surface, 288 K": (288, ORANGE), "Earth emission level, 255 K": (255, AQUA)}
for name, (T, c) in Ts.items():
    y = pi_B(lam, T)                          # spectral emittance per unit wavelength (peaks sit at Wien's lambda_m)
    y = y / y.max()
    ax.plot(lam * 1e6, y, color=c, label=name)
    lm = 2.897771955e-3 / T
    ax.plot([lm * 1e6], [1.0], "o", color=c, ms=5)
ax.annotate("$\\lambda_m$ = 0.50 µm", (0.50, 1.0), xytext=(-8, 8), textcoords="offset points", ha="center", fontsize=8.5)
ax.annotate("$\\lambda_m$ = 10.1 µm (288 K)\nand 11.4 µm (255 K)", (10.8, 1.0), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=8.5)
ax.axvspan(0.4, 0.7, color="#eda100", alpha=0.18, lw=0)
ax.annotate("visible", (0.53, 0.03), ha="center", fontsize=8.5, color=MUTED)
ax.axvline(4, color=MUTED, lw=0.8, ls=":")
ax.annotate("shortwave", (3.5, 0.62), ha="right", fontsize=9, color=MUTED)
ax.annotate("longwave", (4.6, 0.62), ha="left", fontsize=9, color=MUTED)
ax.set_xscale("log")
ax.set_xlim(0.1, 100)
ax.set_ylim(0, 1.3)
ax.set_xlabel("wavelength λ  (µm)")
ax.set_ylabel(r"spectral emittance $\pi B_\lambda$  (each curve scaled to its peak)")
ax.set_title("Sunlight and Earth's glow barely overlap", pad=26)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3, fontsize=8.5, columnspacing=1.2, handlelength=1.6)
save(fig, "fig_cl03_planck_spectra")
