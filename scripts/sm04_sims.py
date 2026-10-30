"""SM04 (kinetic theory) - the two irreversibility toy models used in the chapter.

  * Kac ring (1956): N sites on a ring, k of the edges marked; a ball changes colour whenever it crosses a marked edge.
    Exactly reversible and periodic (period N if k is even, 2N if k is odd), yet under the 'molecular chaos' assumption
    the colour imbalance m_t decays as (1 - 2 mu)^t, mu = k/N.
  * Kac velocity model: random pairs rotate their velocities by a random angle (v1,v2 -> v1 c + v2 s, -v1 s + v2 c),
    conserving v1^2 + v2^2.  The fourth moment relaxes as exp(-t/4) (t in units of one collision per particle).
"""
import numpy as np


def kac_ring(N, k, steps, seed=0):
    rng = np.random.default_rng(seed)
    marked = np.zeros(N, dtype=bool)
    marked[rng.choice(N, k, replace=False)] = True
    colour = np.where(rng.random(N) < 0.5, 1, -1).astype(np.int8)
    colour[:] = 1                      # start fully ordered: all white (+1)
    m = np.empty(steps + 1)
    m[0] = colour.mean()
    flip = np.where(marked, -1, 1).astype(np.int8)          # flip[i] applies to the edge between site i and i+1
    for t in range(1, steps + 1):
        colour = np.roll(colour * flip, 1)                   # ball at i crosses edge i (flips if marked), moves to i+1
        m[t] = colour.mean()
    return m


def kac_model(N=100000, t_max=20.0, snapshots=(0, 2, 6, 15), seed=1, bin_w=0.1):
    """Start from the uniform law on [-sqrt3, sqrt3] (variance 1).  Time unit: N/2 pair collisions."""
    rng = np.random.default_rng(seed)
    v = rng.uniform(-np.sqrt(3), np.sqrt(3), N)
    out = {"t": [], "kurt": [], "H": [], "snap": {}}
    n_coll_per_unit = N // 2
    edges = np.arange(-6, 6 + bin_w, bin_w)

    def record(t):
        sig2 = v.var()
        out["t"].append(t); out["kurt"].append(((v - v.mean()) ** 4).mean() / sig2 ** 2 - 3)
        h, _ = np.histogram(v, bins=edges, density=True)
        pos = h > 0
        out["H"].append((h[pos] * np.log(h[pos])).sum() * bin_w)
        if t in snapshots: out["snap"][t] = v.copy()

    record(0)
    for t in range(1, int(t_max) + 1):
        for _ in range(2):                      # 2 half-steps so that each unit has N/2 collisions in two batches of N/4 pairs
            idx = rng.permutation(N)[: 2 * (n_coll_per_unit // 2)]
            a, b = idx[: len(idx) // 2], idx[len(idx) // 2:]
            th = rng.uniform(0, 2 * np.pi, len(a))
            c, s = np.cos(th), np.sin(th)
            va, vb = v[a].copy(), v[b].copy()
            v[a] = va * c + vb * s
            v[b] = -va * s + vb * c
        record(t)
    return out
