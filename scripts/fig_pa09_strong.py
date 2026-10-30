"""PA09 - postage with stamps of 4 and 5, Fibonacci growth, the Josephus sawtooth."""
from figlib import *
from collections import deque

fig, axes = plt.subplots(1, 3, figsize=(12.4, 3.8))
a = axes[0]
rep = lambda m: any((m - 4 * x) >= 0 and (m - 4 * x) % 5 == 0 for x in range(m // 4 + 1))
for m in range(1, 41):
    r, c = (m - 1) // 10, (m - 1) % 10
    ok = rep(m)
    base = 12 <= m <= 15
    a.add_patch(plt.Rectangle((c, -r), 0.92, 0.82, color=(ORANGE if base else (AQUA if ok else "#e8e8e8")), alpha=0.9 if base else 0.55))
    a.text(c + 0.46, -r + 0.41, str(m), ha="center", va="center", fontsize=8.4, color=INK if ok else MUTED)
a.text(5.0, -3.2, "orange: base cases 12-15. Any later $n$ is a base case\nplus 4-stamps: $n\\to n-4$, so $P(n-4)\\Rightarrow P(n)$", ha="center", va="top", fontsize=8.2)
a.set_xlim(-0.1, 10); a.set_ylim(-4.3, 1.0); a.axis("off")
a.set_title("A  every $n\\geq12$ is $4x+5y$: four base cases", fontsize=10)

b = axes[1]
F = [0, 1, 1]
for i in range(3, 41): F.append(F[-1] + F[-2])
n = np.arange(1, 41); phi = (1 + 5 ** 0.5) / 2
b.semilogy(n, [F[i] for i in n], color=BLUE, lw=2, label=r"$F_n$")
b.semilogy(n, 2.0 ** n, color=ORANGE, lw=1.4, ls="--", label=r"$2^n$ (upper bound)")
b.semilogy(n, phi ** (n - 2.0), color=AQUA, lw=1.4, ls="--", label=r"$\varphi^{\,n-2}$ (lower bound)")
b.set_xlabel("$n$"); b.legend(fontsize=8.2, loc="lower right")
b.set_title("B  $\\varphi^{n-2}\\leq F_n<2^n$ by strong induction", fontsize=10)

c = axes[2]
def jos(m):
    dq = deque(range(1, m + 1))
    while len(dq) > 1:
        dq.rotate(-1); dq.popleft()
    return dq[0]
m = np.arange(1, 65)
c.step(m, [jos(int(x)) for x in m], where="mid", color=BLUE, lw=1.6)
for p in (1, 2, 4, 8, 16, 32, 64):
    c.axvline(p, color=MUTED, lw=0.7, ls=":")
c.set_xlabel("$n$ (number of people)"); c.set_ylabel("$J(n)$ (survivor)")
c.text(9, 49, r"$J(2^m+\ell)=2\ell+1$" + "\n" + r"dotted lines: $n=2^m$, $J=1$", fontsize=8.4)
c.set_title("C  Josephus: a sawtooth, by induction on $n$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: unattainable amounts are 1, 2, 3, 6, 7, 11 (grey). B: exact values. C: simulation of 'every second person leaves'. Numbers in scripts/pa_numbers2.py.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa09_strong")
