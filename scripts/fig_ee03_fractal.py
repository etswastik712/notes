"""EE03 - self-similarity of the bifurcation diagram (logistic map x -> a x (1-x)): the period-3 window repeats the whole diagram."""
from figlib import *

def diagram(lo, hi, n=1500, ylo=0.0, yhi=1.0):
    A, X = [], []
    for a in np.linspace(lo, hi, n):
        x = 0.4
        for _ in range(700):
            x = a * x * (1 - x)
        for _ in range(120):
            x = a * x * (1 - x)
            if ylo <= x <= yhi:
                A.append(a); X.append(x)
    return A, X

fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 4.1))
A, X = diagram(2.8, 4.0)
a.plot(A, X, ",", color=INK, alpha=0.6)
a.plot(A, X, ".", color=INK, ms=0.35, alpha=0.5)
a.axvspan(3.82, 3.87, color=ORANGE, alpha=0.2, lw=0)
a.set_xlabel("a"); a.set_ylabel("x"); a.set_title("Full diagram (logistic map)", fontsize=10)
A2, X2 = diagram(3.82, 3.87, n=1600, ylo=0.0, yhi=1.0)
b.plot(A2, X2, ",", color=INK, alpha=0.6)
b.plot(A2, X2, ".", color=INK, ms=0.35, alpha=0.5)
b.set_xlabel("a"); b.set_title("Zoom into the period-3 window: a smaller copy of the same tree", fontsize=10)
b.text(3.8315, 0.27, "3 branches → 6 → 12 …\n(period-3 window)", fontsize=8.5)
fig.tight_layout(); save(fig, "fig_ee03_fractal")
