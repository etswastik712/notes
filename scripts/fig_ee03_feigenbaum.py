"""EE03 - Feigenbaum ratio computed numerically for the logistic map and the Ricker map (superstable parameters)."""
from figlib import *
from scipy.optimize import brentq

K = 100.0
ricker = lambda n, r: n * np.exp(r * (1 - n / K))
logistic = lambda x, a: a * x * (1 - x)

def itv(f, x, par, p):
    for _ in range(p):
        x = f(x, par)
    return x

def superstable(f, xc, lo, hi, nmax):
    roots, prev = [], lo
    for n in range(nmax + 1):
        p = 2 ** n
        grid = np.linspace(prev + 1e-5, hi, 400001)
        v = itv(f, xc(grid), grid, p) - xc(grid)
        root = None
        for i in np.where(v[:-1] * v[1:] < 0)[0]:
            g = lambda a: itv(f, xc(a), a, p) - xc(a)
            a0 = brentq(g, grid[i], grid[i + 1], xtol=1e-14)
            if n == 0 or abs(itv(f, xc(a0), a0, p // 2) - xc(a0)) > 1e-5:
                root = a0; break
        if root is None: break
        roots.append(root); prev = root
    return np.array(roots)

Rl = superstable(logistic, lambda a: 0.5 + 0 * a, 1.5, 3.5699, 7)
Rr = superstable(ricker, lambda r: K / r, 1.0 - 1e-4, 2.6924, 7)
dl = (Rl[1:-1] - Rl[:-2]) / (Rl[2:] - Rl[1:-1])
dr = (Rr[1:-1] - Rr[:-2]) / (Rr[2:] - Rr[1:-1])
fig, (p, q) = plt.subplots(1, 2, figsize=(10.0, 3.8))
p.plot(range(1, len(dl) + 1), dl, "-o", color=BLUE, ms=5, label="logistic map")
p.plot(range(1, len(dr) + 1), dr, "-s", color=ORANGE, ms=5, label="Ricker map")
p.axhline(4.6692, color=INK, ls="--", lw=1)
p.annotate("δ = 4.6692…", (5.0, 4.6692), xytext=(0, -16), textcoords="offset points", fontsize=9)
p.set_ylim(3.4, 5.0); p.set_xlabel("n"); p.set_ylabel(r"$\delta_n=(a_n-a_{n-1})/(a_{n+1}-a_n)$")
p.set_title("Ratios of successive gaps converge to the same number", fontsize=10); p.legend(loc="lower right", fontsize=8.5)
gl = np.diff(Rl); gr = np.diff(Rr)
q.semilogy(range(1, len(gl) + 1), gl, "-o", color=BLUE, ms=5, label="logistic")
q.semilogy(range(1, len(gr) + 1), gr, "-s", color=ORANGE, ms=5, label="Ricker")
q.set_xlabel("n"); q.set_ylabel(r"gap  $a_{n+1}-a_n$ (log scale)")
q.set_title("Gaps shrink geometrically: a straight line on a log axis", fontsize=10); q.legend(fontsize=8.5)
fig.tight_layout(); save(fig, "fig_ee03_feigenbaum")
print("logistic a_n", np.round(Rl, 6)); print("logistic delta", np.round(dl, 4))
print("Ricker r_n", np.round(Rr, 6)); print("Ricker delta", np.round(dr, 4))
