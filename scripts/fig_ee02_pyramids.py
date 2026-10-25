"""EE02 - age pyramids as model output: stable age distributions of a 16-class (5-year) Leslie model of a human-like
population, for three net reproductive rates.  SCHEMATIC (my construction, not data): survival per 5 years is a smooth
human-like schedule; fertility is spread over ages 15-44 and scaled to the chosen R0.  Both sexes are shown as halves.
"""
from figlib import *

ages = [f"{5 * i}-{5 * i + 4}" for i in range(15)] + ["75+"]
# five-year survival probabilities from class i to i+1 (human-like, high-income)
Pr = np.array([0.994, 0.998, 0.998, 0.997, 0.996, 0.996, 0.994, 0.992, 0.989, 0.984, 0.975, 0.96, 0.93, 0.88, 0.80])
shape = np.zeros(16); shape[3:9] = [0.25, 0.9, 1.0, 0.75, 0.35, 0.08]       # ages 15-44 (classes 3..8)
l = np.concatenate([[1.0], np.cumprod(Pr)])
# half of the births are daughters: fertility row F_x = c*shape_x*(survival of the mother's class midpoint) ; R0 = sum l_x F_x
def leslie(R0):
    F = shape.copy()
    F = F * R0 / np.sum(l * F)
    L = np.zeros((16, 16)); L[0, :] = F
    for i in range(15):
        L[i + 1, i] = Pr[i]
    L[15, 15] = 0.0
    return L

def stable(L):
    ev, V = np.linalg.eig(L); k = np.argmax(ev.real)
    w = np.abs(V[:, k].real); return ev[k].real, w / w.sum()

cases = [("expanding: R0 = 2.0", 2.0, BLUE), ("stable: R0 = 1.0", 1.0, AQUA), ("shrinking: R0 = 0.6", 0.6, ORANGE)]
fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.2), sharey=True)
y = np.arange(16)
for ax, (nm, R0, col) in zip(axes, cases):
    lam, w = stable(leslie(R0))
    pct = 100 * w / 2
    ax.barh(y, -pct, color=col, alpha=0.9, height=0.86); ax.barh(y, pct, color=col, alpha=0.9, height=0.86)
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_title(f"{nm}\nλ = {lam:.3f} per 5 yr", fontsize=10)
    ax.set_xlim(-8, 8)
    ax.set_xticks([-6, -3, 0, 3, 6]); ax.set_xticklabels(["6", "3", "0", "3", "6"])
    ax.set_xlabel("% of population (each sex)")
    ax.grid(axis="y", visible=False)
    print(nm, "lambda per 5yr", round(lam, 4), "per yr", round(lam ** 0.2, 4), "base share", round(100 * w[:3].sum(), 1), "% under 15; 65+:", round(100 * w[13:].sum(), 1), "%")
axes[0].set_yticks(y); axes[0].set_yticklabels(ages, fontsize=7.6); axes[0].set_ylabel("age class (years)")
fig.tight_layout()
fig.text(0.5, -0.04, "Schematic (my construction): the stable age distribution of one Leslie model with fertility scaled to three values of R0. A broad base goes with λ > 1, "
         "a narrow base with λ < 1.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_ee02_pyramids")
