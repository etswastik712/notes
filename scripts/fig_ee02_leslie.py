"""EE02 - the slide-16 Leslie simulation reproduced: 200 newborns, P = (0.5, 0.2, 0.1), F = (0, 2, 1, 1).
A total population (log axis) with the asymptote lambda^t; B age proportions converging to the stable age distribution;
C N(t+1)/N(t) -> lambda with the damping envelope (|lambda_2|/lambda_1)^t.
"""
from figlib import *

L = np.zeros((4, 4)); L[0, :] = [0, 2, 1, 1]
for i, p in enumerate([0.5, 0.2, 0.1]):
    L[i + 1, i] = p
ev, V = np.linalg.eig(L); k = np.argmax(ev.real)
lam = ev[k].real
sad = np.abs(V[:, k].real); sad /= sad.sum()
lam2 = sorted(np.abs(np.delete(ev, k)))[-1]
T = 90
n = np.array([200., 0, 0, 0]); traj = [n.copy()]
for _ in range(T):
    n = L @ n; traj.append(n.copy())
traj = np.array(traj); N = traj.sum(1); t = np.arange(T + 1)
prop = traj / N[:, None]
ratio = N[1:] / N[:-1]

fig, axes = plt.subplots(1, 3, figsize=(11.6, 3.7))
a = axes[0]
a.plot(t, N, color=BLUE, label="$N_t$")
c = N[-1] / lam ** T
a.plot(t, c * lam ** t, color=ORANGE, ls="--", lw=1.4, label=r"$c\,\lambda^t$, $\lambda=1.0508$")
a.set_yscale("log"); a.set_xlabel("time step t"); a.set_ylabel("total population $N_t$ (log scale)")
a.set_title("A  zigzag, then a straight line", fontsize=10); a.legend(loc="upper left", fontsize=8.5)
a.grid(which="minor", visible=False)

b = axes[1]
cols = [BLUE, ORANGE, AQUA, VIOLET]
for j in range(4):
    b.plot(t, prop[:, j], color=cols[j], lw=1.5)
    b.plot([0, T], [sad[j], sad[j]], color=cols[j], lw=0.9, ls=":")
    b.text(T + 1.5, sad[j], f"class {j}: {sad[j]:.3f}", color=INK, fontsize=8, va="center")
b.set_xlim(0, T + 28); b.set_xlabel("time step t"); b.set_ylabel("share of population")
b.set_title("B  age shares settle (SAD, dotted)", fontsize=10)

c3 = axes[2]
c3.plot(t[:-1], ratio, color=BLUE, lw=1.5)
c3.axhline(lam, color=ORANGE, ls="--", lw=1.4)
env = 1.0 * (lam2 / lam) ** t[:-1]
c3.plot(t[:-1], lam + 1.2 * env, color=MUTED, lw=0.9, ls=":")
c3.plot(t[:-1], lam - 1.2 * env, color=MUTED, lw=0.9, ls=":")
c3.text(30, 1.75, r"dotted: envelope $\propto(|\lambda_2|/\lambda_1)^t$" "\n" "with ratio 0.906 per step", color=MUTED, fontsize=8.2)
c3.set_ylim(0, 2.6); c3.set_xlabel("time step t"); c3.set_ylabel("$N_{t+1}/N_t$")
c3.set_title(r"C  growth ratio $\to\lambda=1.05082$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.04, "Reproduced from the slide-16 matrix (200 newborns). The transient is the sum of the other eigenvalue terms; the slowest, |λ₂| = 0.952, "
         "dies out relative to λ₁ by a factor 0.906 per step.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_ee02_leslie")
print("lambda", lam, "lambda2", lam2, "ratio", lam2 / lam)
