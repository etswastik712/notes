"""EE02 - every number quoted in the chapter (Phlox life table, survivorship, Leslie example, loggerhead matrix,
sensitivity/elasticity, TED scenarios, age-structure examples).

    .venv/bin/python -W ignore scripts/ee02_numbers.py
"""
import numpy as np
from scipy.optimize import brentq

np.set_printoptions(precision=4, suppress=True)

# ------------------------------------------------------------------ 1. Phlox drummondii cohort table (slide 10)
n_x = np.array([996, 158, 154, 151, 147, 136, 105, 74, 22, 0], float)
l_x = np.array([1.0, .1586, .1546, .1516, .1476, .1365, .1054, .0743, .0221, 0.0])
m_x = np.array([0.0, .3352, .7963, 2.3995, 3.1094, 2.5411, 3.1589, 8.6625, 4.3072, 0.0])
print("== Phlox")
print("l_x from counts:", np.round(n_x / n_x[0], 4))
print("R0 = sum l_x m_x (slide columns):", round(float(np.sum(l_x * m_x)), 4), "(slide prints 2.4177; Molles ch.10-11 use lambda = 2.4177)")
start = np.array([0, 299, 306, 313, 320, 327, 334, 341, 348, 355], float)   # class starts (days)
mid = start + np.array([299, 7, 7, 7, 7, 7, 7, 7, 7, 7]) / 2                 # midpoints (first class 0-299)
T = float(np.sum(mid * l_x * m_x) / np.sum(l_x * m_x))
print("generation time T = sum x l_x m_x / R0 (class midpoints, days):", round(T, 1))
print("r ~ ln R0 / T per day:", round(np.log(2.4177) / T, 5))
r_el = brentq(lambda r: np.sum(np.exp(-r * mid) * l_x * m_x) - 1, 1e-5, 0.1)
print("Euler-Lotka root r (per day):", round(r_el, 5), " -> per generation-year lambda_365 =", round(np.exp(r_el * 365), 3))
q = 1 - l_x[1:-1] / l_x[:-2]
print("interval death probabilities q (classes 2..9):", np.round(q, 3))
print("fraction dead before day 299:", round(1 - l_x[1], 4))
N0, lam = 996, 2.4177
for t in (1, 2, 3, 8, 16, 24, 32):
    print(f"  geometric growth N_{t} = 996*2.4177^{t} = {N0 * lam ** t:.3e}")
print("  density at t=32 on 24e6 km2 (per m2):", round(N0 * lam ** 32 / 24e6 / 1e6, 1))

# ------------------------------------------------------------------ 2. survivorship on linear vs log axes (slide 12)
print("\n== survivorship")
n = 1000 * 0.4 ** np.arange(4)
print("1000 -> ", n, "  losses:", -np.diff(n), " proportion lost each step:", 1 - n[1:] / n[:-1], "  ln slope:", round(np.log(0.4), 4))

# ------------------------------------------------------------------ 3. Leslie matrix of slides 15-21
print("\n== Leslie example (slides 16-21)")
P = [0.5, 0.2, 0.1]
F = [0, 2, 1, 1]
L = np.zeros((4, 4)); L[0, :] = F
for i, p in enumerate(P):
    L[i + 1, i] = p
w, V = np.linalg.eig(L)
k = np.argmax(w.real)
lam = w[k].real
sad = np.abs(V[:, k].real); sad /= sad.sum()
wl, Vl = np.linalg.eig(L.T)
v = np.abs(Vl[:, np.argmax(wl.real)].real); v /= v[0]
print("lambda =", round(lam, 5), " (slide 1.05082)")
print("SAD    =", np.round(sad, 6), " (slide 0.634921 0.302108 0.057499 0.005472)")
print("moduli of other eigenvalues:", np.round(sorted(np.abs(np.delete(w, k)), reverse=True), 4), " damping ratio |l2|/l1 =", round(sorted(np.abs(np.delete(w, k)))[-1] / lam, 4))
print("characteristic equation l^4 = l^2 + 0.1 l + 0.01 residual at lambda:", round(lam ** 4 - lam ** 2 - 0.1 * lam - 0.01, 8))
l_age = np.array([1, 0.5, 0.1, 0.01])
print("l_x =", l_age, " R0 = sum l_x F_x =", round(float(np.sum(l_age * np.array(F))), 4))
print("SAD ratios w_{x+1}/w_x = P_x/lambda:", np.round(sad[1:] / sad[:-1], 4), " vs", np.round(np.array(P) / lam, 4))
print("reproductive values (left eigenvector, v1=1):", np.round(v, 3))
nt = np.array([200., 0, 0, 0])
print("hand iteration from (200,0,0,0):")
traj = [nt.copy()]
for t in range(200):
    nt = L @ nt
    traj.append(nt.copy())
    if t < 4:
        print(f"  t={t + 1}: n={nt}  N={nt.sum():.1f}")
traj = np.array(traj)
N = traj.sum(1)
ratio = N[1:] / N[:-1]
dev = np.abs(traj / traj.sum(1, keepdims=True) - sad).max(1)
first = int(np.argmax(dev < 0.01))
print("steps until every age proportion is within 0.01 of SAD:", first, "; ratio N_{t+1}/N_t at t=200:", round(ratio[-1], 5), "; N_200 =", f"{N[-1]:.0f}")
print("total N at steps 1..8:", np.round(N[1:9], 1))

# ------------------------------------------------------------------ 4. loggerhead (Crowder et al. 1994)
print("\n== loggerhead")
sigma = np.array([0.6747, 0.75, 0.6758, 0.7425, 0.8091])      # Table 1
dur = np.array([1, 7, 8, 6, 32.0])                            # stage durations (adults ">32": 32 used in the formula)
fec = np.array([0, 0, 0, 0, 76.5])
A_slide = np.array([[0, 0, 0, 4.665, 61.896], [.675, .703, 0, 0, 0], [0, .047, .657, 0, 0], [0, 0, .019, .682, 0], [0, 0, 0, .061, .8091]])


def build(sig, lam0, d=dur, f=fec):
    """Crouse/Caswell stage matrix: gamma_i = (s/lam)^(T-1)(1 - s/lam)/(1-(s/lam)^T); P = s(1-gamma); G = s*gamma."""
    n = len(sig)
    A = np.zeros((n, n))
    gam = np.zeros(n)
    for i in range(n - 1):
        x = sig[i] / lam0
        gam[i] = x ** (d[i] - 1) * (1 - x) / (1 - x ** d[i])
    P_ = sig * (1 - gam); G_ = sig * gam
    P_[-1], G_[-1] = sig[-1], 0.0
    for i in range(n):
        A[i, i] = P_[i]
        if i < n - 1:
            A[i + 1, i] = G_[i]
        A[0, i] += f[i] * P_[i] + (f[i + 1] * G_[i] if i < n - 1 else 0)
    return A


def dom(A):
    ev = np.linalg.eigvals(A)
    return ev[np.argmax(ev.real)].real


def solve(sig, d=dur, f=fec):
    lam0 = 0.95
    for _ in range(200):
        A = build(sig, lam0, d, f)
        new = dom(A)
        if abs(new - lam0) < 1e-10:
            break
        lam0 = new
    return A, lam0


A, lam_ = solve(sigma)
print("rebuilt matrix from Table 1 (lambda self-consistent):\n", np.round(A, 4))
print("slide/Table 2 matrix:\n", A_slide)
print("max abs difference:", round(float(np.abs(A - A_slide).max()), 4))
lam_s = dom(A_slide)
print("lambda (Table 2) =", round(lam_s, 5), " r = ln lambda =", round(np.log(lam_s), 5), " (paper: decline 4.96 %/yr; Fig. 4 baseline -0.050)")
ev, V = np.linalg.eig(A_slide); k = np.argmax(ev.real)
w5 = np.abs(V[:, k].real); w5 /= w5.sum()
evl, Vl = np.linalg.eig(A_slide.T); kl = np.argmax(evl.real)
v5 = np.abs(Vl[:, kl].real); v5 /= v5[0]
print("stable stage distribution w =", np.round(w5, 4), " (Table 3: 0.2385 0.6478 0.1033 0.0073 0.0031)")
print("reproductive values v (v1=1) =", np.round(v5, 2), " ratios:", np.round(v5[1:] / v5[:-1], 2), " (paper: x1.4, x4.4% ~5.4?, >14.3, 2.8)")
S = np.outer(v5, w5) / (v5 @ w5)
E = A_slide * S / lam_s
print("elasticity matrix sums to", round(float(E.sum()), 4))
print("elasticity of lambda to F:", round(float(E[0, :].sum() - E[0, 0] * 0), 4), "(row 1 includes F and P1 entries)")
sigma2 = np.array([0.6747, 0.75, 0.6758, 0.7425, 0.8091])


def lam_of(sig, d=dur):
    return solve(sig, d)[1]


base = lam_of(sigma2)
el_sig = []
for i in range(5):
    s2 = sigma2.copy(); s2[i] *= 1.001
    el_sig.append((lam_of(s2) - base) / base / 0.001)
print("elasticity of lambda to stage survival sigma_i:", np.round(el_sig, 3), " sum", round(sum(el_sig), 3), "(Fig. 2: large juvenile highest, then small juvenile)")
print("baseline lambda (rebuilt):", round(base, 5), "r:", round(np.log(base), 5))
# the paper's own method (Appendix 2): P and G are functions of sigma at FIXED lambda in gamma; the resulting
# survival elasticities then sum to more than 1
A0, lam0 = solve(sigma2)
ev0, V0 = np.linalg.eig(A0); k0 = np.argmax(ev0.real); w0 = np.abs(V0[:, k0].real)
evl0, Vl0 = np.linalg.eig(A0.T); v0 = np.abs(Vl0[:, np.argmax(evl0.real)].real)
S0 = np.outer(v0, w0) / (v0 @ w0)
el_paper = []
for i in range(5):
    s2 = sigma2.copy(); s2[i] += 1e-6
    dA = (build(s2, lam0) - build(sigma2, lam0)) / 1e-6
    el_paper.append(sigma2[i] / lam0 * np.sum(S0 * dA))
print("elasticity to sigma_i, paper's method (lambda held fixed inside gamma):", np.round(el_paper, 3), " sum", round(sum(el_paper), 3),
      "(Fig. 2 read-off ~ 0.06 0.41 0.46 0.32 0.28)")

print("\nFig. 4 reproduction: r after reducing annual mortality (1-sigma) in ONE stage by 10/50/90 %")
rows = {}
for i, nm in enumerate(["egg/hatchling", "small juvenile", "large juvenile", "subadult", "adult"]):
    out = []
    for red in (0.1, 0.5, 0.9):
        s2 = sigma2.copy(); s2[i] = 1 - (1 - s2[i]) * (1 - red)
        out.append(np.log(lam_of(s2)))
    rows[nm] = out
    print(f"  {nm:15s} r = {np.round(out, 4)}")
out = []
for inc in (0.1, 0.5, 0.9):
    f2 = fec.copy(); f2[4] *= 1 + inc
    out.append(np.log(solve(sigma2, dur, f2)[1]))
print(f"  {'fecundity':15s} r = {np.round(out, 4)}")
print("  (read off the slide-26 bars, approx.: egg -0.049/-0.042/-0.036; small -0.041/-0.010/+0.020; large -0.035/+0.015/+0.060; sub -0.041/-0.014/+0.011; adult -0.044/-0.020/+0.017; fecundity -0.046/-0.033/-0.025)")

print("\nTED scenario (paper: difference between Heron Island and Little Cumberland survivals x 0.67 or x 0.99)")
aus = {2: 0.83, 3: 0.885, 4: 0.91}
for nm, fr in (("seasonal offshore, x0.67", 0.67), ("all waters all seasons, x0.99", 0.99)):
    s2 = sigma2.copy()
    for idx, a in aus.items():
        s2[idx] += fr * (a - s2[idx])
    lam2 = lam_of(s2)
    print(f"  {nm}: new survivals {np.round(s2, 4)}  lambda={lam2:.4f}  r={np.log(lam2):+.4f}  growth {100 * (lam2 - 1):+.2f} %/yr  years for x10: {np.log(10) / np.log(lam2):.0f}")
print("uniform mortality reduction in large juv, subadult and adult (Fig. 5 lines):")
for red in (0.1, 0.2, 0.3, 0.4, 0.8):
    s2 = sigma2.copy()
    for idx in (2, 3, 4):
        s2[idx] = 1 - (1 - s2[idx]) * (1 - red)
    lam2 = lam_of(s2)
    print(f"  -{int(red * 100)} % mortality: lambda={lam2:.4f}  r={np.log(lam2):+.4f}  years for x10: {np.log(10) / np.log(lam2) if lam2 > 1 else float('nan'):.0f}")
print("mortality cut needed for lambda = 1 (large juv + subadult + adult):",
      round(brentq(lambda x: np.log(lam_of(np.array([sigma2[0], sigma2[1]] + [1 - (1 - s) * (1 - x) for s in sigma2[2:]]))), 0.0, 0.8), 3))
print("perfect egg survival (sigma_1 -> 1): lambda =", round(lam_of(np.array([1.0, *sigma2[1:]])), 4), "(still < 1)")
print("sigma_3 -> 1: lambda =", round(lam_of(np.array([sigma2[0], sigma2[1], 1.0, *sigma2[3:]])), 4))

# ------------------------------------------------------------------ 5. human age structure examples (Molles Fig. 11.24)
print("\n== human populations (Molles 2022, Fig 11.24; UN WPP 2020)")
for nm, b, d in (("Sweden", 0.010, 0.010), ("Hungary", 0.010, 0.013), ("Rwanda", 0.037, 0.010)):
    r = b - d
    msg = f"{nm}: b={b} d={d} r={r:+.3f}"
    if r > 0:
        msg += f"  doubling time {np.log(2) / r:.1f} yr"
    if r < 0:
        msg += f"  halving time {np.log(2) / -r:.0f} yr"
    print(msg)

# momentum toy: 4 age classes of 20 years (0-19, 20-39, 40-59, 60-79); fertility then cut to replacement
Lm = np.zeros((4, 4)); Lm[0, 1] = 1.3; Lm[0, 2] = 0.5
for i, p in enumerate([0.97, 0.96, 0.85]):
    Lm[i + 1, i] = p
ev, V = np.linalg.eig(Lm); k = np.argmax(ev.real)
lam_m = ev[k].real
sad_m = np.abs(V[:, k].real); sad_m /= sad_m.sum()
l_m = np.array([1, 0.97, 0.97 * 0.96, 0.97 * 0.96 * 0.85])
R0m = float(np.sum(l_m * Lm[0]))
print("toy growing country (20-year steps): lambda =", round(lam_m, 3), " R0 =", round(R0m, 3), " SAD =", np.round(sad_m, 3))
Lr = Lm.copy(); Lr[0] /= R0m                      # fertility cut so that R0 = 1 immediately
n_ = sad_m * 100.0
print("momentum after fertility falls to replacement (R0 = 1):")
hist = [n_.sum()]
for t in range(12):
    n_ = Lr @ n_
    hist.append(n_.sum())
print("  total (start=100):", np.round(hist, 1), "-> final/initial =", round(hist[-1] / hist[0], 3))

# ------------------------------------------------------------------ 6. worked examples and practice problems of the chapter
print("\n== chapter examples / practice")
lamT = 0.95158
for nm, s_, T_ in (("small juvenile", 0.75, 7), ("large juvenile", 0.6758, 8), ("subadult", 0.7425, 6)):
    x_ = s_ / lamT; g_ = x_ ** (T_ - 1) * (1 - x_) / (1 - x_ ** T_)
    print(f"  {nm}: x=sigma/lambda={x_:.4f} gamma={g_:.4f} G={s_ * g_:.4f} P={s_ * (1 - g_):.4f}")
ev_, V_ = np.linalg.eig(A_slide); k_ = np.argmax(ev_.real); lam_t = ev_[k_].real; w_t = np.abs(V_[:, k_].real)
evl_, Vl_ = np.linalg.eig(A_slide.T); v_t = np.abs(Vl_[:, np.argmax(evl_.real)].real)
S_t = np.outer(v_t, w_t) / (v_t @ w_t); E_t = A_slide * S_t / lam_t
for nm_, (i_, j_) in zip(["P2", "P3", "P4", "P5", "G1", "G2", "G3", "G4", "F4", "F5"],
                         [(1, 1), (2, 2), (3, 3), (4, 4), (1, 0), (2, 1), (3, 2), (4, 3), (0, 3), (0, 4)]):
    print(f"  {nm_}: a={A_slide[i_, j_]:.4f} sensitivity={S_t[i_, j_]:.4f} elasticity={E_t[i_, j_]:.4f}")
print("  elasticities grouped: P", round(float(E_t[1, 1] + E_t[2, 2] + E_t[3, 3] + E_t[4, 4]), 3), " G", round(float(E_t[1, 0] + E_t[2, 1] + E_t[3, 2] + E_t[4, 3]), 3),
      " F", round(float(E_t[0, 3] + E_t[0, 4]), 3))
Lp = np.array([[0, 1.2, 0.8], [0.5, 0, 0], [0, 0.4, 0]])
evp, Vp = np.linalg.eig(Lp); kp = np.argmax(evp.real)
print("  practice 3 (F=(0,1.2,0.8), P=(0.5,0.4)): lambda", round(evp[kp].real, 4), " SAD", np.round(np.abs(Vp[:, kp].real) / np.abs(Vp[:, kp].real).sum(), 4), " R0", 1.2 * 0.5 + 0.8 * 0.2)
Ls = np.array([[0, 0, 6], [0.5, 0, 0], [0, 0.4, 0]])
evs = np.linalg.eigvals(Ls)
print("  practice 4 (semelparous F3=6, P=(0.5,0.4)): eigenvalue moduli", np.round(np.abs(evs), 4), " (F3 P1 P2)^(1/3) =", round((6 * 0.5 * 0.4) ** (1 / 3), 4))
n_ = np.array([100., 0, 0]); seq = []
for _ in range(7):
    seq.append(n_.copy()); n_ = Ls @ n_
print("  from (100,0,0): totals", [float(s.sum()) for s in seq])
s_up = sigma2.copy(); s_up[2] *= 1.10
print("  practice 6: sigma_3 +10 % ->", round(float(s_up[2]), 4), " lambda", round(lam_of(s_up), 4), " relative change", round(lam_of(s_up) / lam_of(sigma2) - 1, 4))
s_half = sigma2.copy(); s_half[2] = 1 - (1 - s_half[2]) * 0.5
print("  large-juvenile mortality halved: sigma_3", round(float(s_half[2]), 4), " lambda", round(lam_of(s_half), 4))
print("  Rwanda doubling", round(np.log(2) / 0.027, 1), " Hungary halving", round(np.log(2) / 0.003))
