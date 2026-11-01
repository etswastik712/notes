"""Differential Geometry vault (14-Differential-Geometry): numbers quoted in the DM chapters, recomputed.

    .venv/bin/python -W ignore scripts/dm_numbers.py            # all chapters
    .venv/bin/python -W ignore scripts/dm_numbers.py DM01 DM03  # selected chapters
"""
import sys

import numpy as np
import sympy as sp

rng = np.random.default_rng(11)


def jac_fd(f, x, h=1e-6):
    """Central-difference Jacobian of f: R^n -> R^m at x."""
    x = np.asarray(x, float)
    cols = []
    for i in range(len(x)):
        e = np.zeros_like(x)
        e[i] = h
        cols.append((np.asarray(f(x + e)) - np.asarray(f(x - e))) / (2 * h))
    return np.array(cols).T


# ------------------------------------------------------------------------------------------------------------------ DM01
def dm01():
    print("== DM01 Smooth Manifolds")
    # 1. the graph charts of S^2 (MT3184 HW1 Q2): phi_1^+(x,y,z) = (y,z) on {x>0},  phi_3^+(x,y,z) = (x,y) on {z>0}
    # transition phi_3^+ o (phi_1^+)^{-1}(y, z) = (sqrt(1 - y^2 - z^2), y) on {y^2 + z^2 < 1, z > 0}
    trans = lambda p: np.array([np.sqrt(1 - p[0] ** 2 - p[1] ** 2), p[0]])
    p = np.array([0.3, 0.5])
    J = jac_fd(trans, p)
    x = np.sqrt(1 - p @ p)
    print("graph atlas: transition (y,z) -> (sqrt(1-y^2-z^2), y) at (0.3, 0.5): det J = %.6f, formula z/x = %.6f" % (np.linalg.det(J), p[1] / x))
    print("  J (finite difference) =", np.round(J, 6).tolist(), "; formula [[-y/x, -z/x],[1, 0]] =", np.round([[-p[0] / x, -p[1] / x], [1, 0]], 6).tolist())
    # inverse transition is smooth too: (x, y) -> (y, sqrt(1-x^2-y^2))
    # 2. stereographic charts: psi_N(x,y,z) = (x,y)/(1-z), psi_S(x,y,z) = (x,y)/(1+z); transition = inversion w -> w/|w|^2
    sinv = lambda w: np.array([2 * w[0], 2 * w[1], w @ w - 1]) / (w @ w + 1)        # (psi_N)^{-1}
    psi_S = lambda q: q[:2] / (1 + q[2])
    worst = 0.0
    for _ in range(1000):
        w = rng.normal(size=2) * rng.uniform(0.1, 5)
        worst = max(worst, np.abs(psi_S(sinv(w)) - w / (w @ w)).max())
    print("stereographic: max |psi_S(psi_N^-1(w)) - w/|w|^2| over 1000 random w = %.1e" % worst)
    w = np.array([0.7, -1.3])
    Jinv = jac_fd(lambda v: v / (v @ v), w)
    print("  inversion Jacobian det at w = (0.7, -1.3): %.6f; formula -1/|w|^4 = %.6f" % (np.linalg.det(Jinv), -1 / (w @ w) ** 2))
    # 3. the chart x -> x^3 on R: transition with the identity chart is x^{1/3} (not smooth at 0)
    print("chart x^3 vs identity: transition y -> y^{1/3}; derivative (1/3) y^{-2/3} at y = 1e-3, 1e-6, 1e-9: %s" % ", ".join("%.4g" % (y ** (-2 / 3) / 3) for y in (1e-3, 1e-6, 1e-9)))
    # 4. projective plane charts: [x0:x1:x2], U_0 = {x0 != 0}, phi_0 = (x1/x0, x2/x0); U_1: phi_1 = (x0/x1, x2/x1)
    # transition phi_1 o phi_0^{-1}(a, b) = (1/a, b/a) on a != 0; Jacobian det = -1/a^3
    a_, b_ = 1.7, -0.4
    tr = lambda v: np.array([1 / v[0], v[1] / v[0]])
    print("RP^2: transition (a,b) -> (1/a, b/a) at (1.7, -0.4): det J = %.6f; formula -1/a^3 = %.6f" % (np.linalg.det(jac_fd(tr, [a_, b_])), -1 / a_ ** 3))
    # 5. gluing two copies of R^n by inversion: the unit balls B_1 (chart N) and B_1 (chart S) are disjoint
    ok = True
    for _ in range(20000):
        w = rng.normal(size=2) * rng.uniform(0.01, 3)
        n = np.linalg.norm(w)
        if n < 1 and 1 / n < 1:        # w in B_1 of chart N and its S-coordinate w/|w|^2 in B_1 of chart S
            ok = False
    print("two copies of R^2 glued by inversion: no point lies in both unit balls (20000 samples):", ok)


# ------------------------------------------------------------------------------------------------------------------ DM02
def f_bump(t):
    """f(t) = exp(-1/t) for t > 0, 0 otherwise: smooth, flat at 0."""
    t = np.asarray(t, float)
    out = np.zeros_like(t)
    m = t > 0
    out[m] = np.exp(-1.0 / t[m])
    return out


def h_step(t):
    """Smooth step: 0 for t <= 0, 1 for t >= 1."""
    return f_bump(t) / (f_bump(t) + f_bump(1 - np.asarray(t, float)))


def dm02():
    print("== DM02 Smooth Maps and Partitions of Unity")
    print("f(t) = e^{-1/t} is flat at 0: f(t)/t^k at t = 0.01 for k = 5, 10, 20: %s" % ", ".join("%.1e" % (f_bump(0.01) / 0.01 ** k) for k in (5, 10, 20)))
    print("   (f(0.01) = %.2e: smaller than every power of t)" % f_bump(0.01))
    print("smooth step h(t) = f(t)/(f(t)+f(1-t)): h(0.25) = %.4f, h(0.5) = %.4f, h(0.75) = %.4f" % tuple(h_step(np.array([0.25, 0.5, 0.75]))))
    # bump on R^n equal to 1 on B_1 and supported in B_2: b(x) = h(2 - |x|)
    b = lambda r: h_step(2 - np.asarray(r, float))
    print("bump b(x) = h(2 - |x|): b(0.5) = %.1f, b(1) = %.1f, b(1.5) = %.4f, b(1.9) = %.6f, b(2) = %.1f, b(3) = %.1f" % (b(0.5), b(1.0), b(1.5), b(1.9), b(2.0), b(3.0)))
    # partition of unity of R subordinate to U1 = (-inf, 1), U2 = (0, inf): psi2(x) = h(3x - 1), psi1 = 1 - psi2
    psi2 = lambda x: h_step(3 * np.asarray(x, float) - 1)
    xs = np.array([-1.0, 0.0, 0.2, 1 / 3, 0.4, 0.5, 0.6, 2 / 3, 0.9, 2.0])
    print("partition of unity on R (psi2 = h(3x - 1), psi1 = 1 - psi2); sum = 1 by construction:")
    for x in xs:
        print("   x = %6.3f  psi1 = %.6f  psi2 = %.6f" % (x, 1 - psi2(x), psi2(x)))
    print("   supp psi2 = [1/3, inf) inside U2 = (0, inf); supp psi1 = (-inf, 2/3] inside U1 = (-inf, 1)")
    # partition of unity on S^1 subordinate to V1 = S^1 minus N, V2 = S^1 minus S:  psi1 = h(0.5 - y)
    th = np.linspace(0, 2 * np.pi, 2001)
    y = np.sin(th)
    p1 = h_step(0.5 - y)
    p2 = 1 - p1
    print("S^1: psi1 = h(0.5 - y) vanishes for y >= 0.5 (near N): max over y >= 0.5 = %.1e; psi2 vanishes for y <= -0.5: max = %.1e" % (p1[y >= 0.5].max(), p2[y <= -0.5].max()))
    # antipodal map F(p) = -p on S^2 in charts psi_2 (near N) and psi_1 (near S): psi_1 o F o psi_2^{-1}(u) = -u
    sinv2 = lambda u: np.array([2 * u[0], 2 * u[1], 1 - u @ u]) / (1 + u @ u)          # psi_2^{-1}
    psi1 = lambda q: q[:2] / (1 - q[2])
    err = 0.0
    for _ in range(2000):
        u = rng.normal(size=2) * rng.uniform(0.05, 4)
        err = max(err, np.abs(psi1(-sinv2(u)) + u).max())
    print("antipodal map in stereographic charts: max |psi_1(F(psi_2^-1(u))) + u| over 2000 random u = %.1e (so F(u) = -u, dF = -I)" % err)
    print("   at p = (0,0,1): psi_2(p) = (0,0); F(p) = (0,0,-1) has psi_1 = (0,0)")

# ------------------------------------------------------------------------------------------------------------------ DM03
def dm03():
    print("== DM03 Tangent Vectors and the Differential")
    r3 = np.sqrt(3.0)
    # stereographic charts: phi = psi_1 (from N, domain S^2 minus N), psi = psi_2 (from S)
    phi = lambda q: q[:2] / (1 - q[2])
    phi_inv = lambda u: np.array([2 * u[0], 2 * u[1], u @ u - 1]) / (u @ u + 1)
    psi = lambda q: q[:2] / (1 + q[2])
    # HW2 Q3: p = (sqrt3/2, 1/2, 0), X = (1, 2) in the phi-basis, f(u1, u2) = u1 + 2 u2^2
    u = np.array([r3 / 2, 0.5])
    X = np.array([1.0, 2.0])
    grad_f = np.array([1.0, 4 * u[1]])
    print("HW2 Q3: p = (sqrt3/2, 1/2, 0), phi(p) = (%.6f, %.6f); X f = 1*1 + 2*4*u2 = %.6f" % (*phi(np.array([r3 / 2, 0.5, 0.0])), X @ grad_f))
    # independent check: push X to R^3 through phi^{-1}, differentiate f o phi along the curve
    eps = 1e-6
    q = lambda t: phi_inv(u + t * X)
    fval = lambda t: (lambda w: w[0] + 2 * w[1] ** 2)(phi(q(t)))
    print("   finite difference of f along the curve phi^-1(u + tX): %.6f" % ((fval(eps) - fval(-eps)) / (2 * eps)))
    J = jac_fd(lambda w: w / (w @ w), u)
    Xt = J @ X
    print("   transition J = D(w/|w|^2)(u) = %s ; X in the psi-basis = J X = (%.6f, %.6f); exact (-1/2 - sqrt3, 1 - sqrt3/2) = (%.6f, %.6f)"
          % (np.round(J, 6).tolist(), *Xt, -0.5 - r3, 1 - r3 / 2))
    print("   check by pushing the curve: d/dt psi(phi^-1(u + tX)) at 0 = %s" % np.round((psi(phi_inv(u + eps * X)) - psi(phi_inv(u - eps * X))) / (2 * eps), 6).tolist())
    # Test 1 Q4: X = (1, 2) at p = (0,0,1) in the psi-chart (psi(N) = (0,0)); the graph chart phi_3^+(x,y,z) = (x,y)
    g3 = lambda w: 2 * w / (1 + w @ w)                       # phi_3^+ o psi^{-1}(w) = (x, y) = 2w/(1+|w|^2)
    J0 = jac_fd(g3, np.zeros(2))
    print("Test 1 Q4: Jacobian of phi_3^+ o psi^-1 at 0 = %s, so X = (1,2) becomes %s in the graph chart" % (np.round(J0, 6).tolist(), np.round(J0 @ X, 6).tolist()))
    # HW3 Q1: alpha(t) = (t, 2t, sqrt(1 - 5t^2)), p = alpha(1/4); charts phi_3^+ = (x, y), phi_2^+ = (x, z)
    alpha = lambda t: np.array([t, 2 * t, np.sqrt(1 - 5 * t * t)])
    t0 = 0.25
    print("HW3 Q1: p = alpha(1/4) = %s ; |p| = %.12f" % (np.round(alpha(t0), 6).tolist(), np.linalg.norm(alpha(t0))))
    d3 = (alpha(t0 + eps)[[0, 1]] - alpha(t0 - eps)[[0, 1]]) / (2 * eps)
    d2 = (alpha(t0 + eps)[[0, 2]] - alpha(t0 - eps)[[0, 2]]) / (2 * eps)
    print("   (a) alpha'(1/4) in the phi_3^+ basis = (%.6f, %.6f)" % tuple(d3))
    print("   (c) alpha'(1/4) in the phi_2^+ basis = (%.6f, %.6f); formula (1, -5/sqrt11) = (1, %.6f)" % (*d2, -5 / np.sqrt(11)))
    Fr = lambda w: np.array([0.5 * (w[0] - r3 * w[1]), 0.5 * (r3 * w[0] + w[1])])     # F in the phi_3^+ charts: rotation by 60 degrees
    DF = jac_fd(Fr, u)
    print("   (b) DF(p) alpha'(1/4) in the phi_3^+ bases = %s; formula (1/2)(1 - 2 sqrt3, sqrt3 + 2) = (%.6f, %.6f)" % (np.round(DF @ d3, 6).tolist(), 0.5 * (1 - 2 * r3), 0.5 * (r3 + 2)))
    # derivation property of a tangent vector (directional derivative): v(fg) = f(p) v(g) + g(p) v(f)
    f = lambda x: np.sin(x[0]) * x[1] ** 2 + x[2]
    g = lambda x: np.exp(x[0] - x[1]) + x[2] ** 3
    a = np.array([0.3, -0.7, 1.1])
    v = np.array([0.4, 1.3, -0.8])
    D = lambda h: (h(a + eps * v) - h(a - eps * v)) / (2 * eps)
    print("Leibniz rule for the directional derivative: v(fg) = %.8f, f(a) v(g) + g(a) v(f) = %.8f" % (D(lambda x: f(x) * g(x)), f(a) * D(g) + g(a) * D(f)))
    # change of basis: components transform with the Jacobian of the transition; the coordinate vectors with its inverse transpose-free form
    Jinv = np.linalg.inv(J)
    print("coordinate vectors: d/du^j = sum_i (dpsi^i/du^j) d/dpsi^i (columns of J); check J^-1 J = I: %.1e" % np.abs(Jinv @ J - np.eye(2)).max())

# ------------------------------------------------------------------------------------------------------------------ DM04
def dm04():
    print("== DM04 The Tangent Bundle and the Rank Theorem")
    # 1. TS^1 in the stereographic charts: transition (w, v) -> (1/w, -v/w^2); check with the actual circle
    sinv = lambda w: np.array([2 * w, w * w - 1]) / (w * w + 1)           # psi_N^{-1} on S^1 (projection from N = (0, 1))
    psi_S = lambda q: q[0] / (1 + q[1])
    w0, v0, e = 1.7, 0.9, 1e-6
    curve = lambda t: sinv(w0 + t * v0)                                   # curve with velocity v0 d/dw in chart N
    w_new = psi_S(curve(0.0))
    v_new = (psi_S(curve(e)) - psi_S(curve(-e))) / (2 * e)
    print("TS^1: (w, v) = (%.2f, %.2f) -> (1/w, -v/w^2) = (%.6f, %.6f); computed (%.6f, %.6f)" % (w0, v0, 1 / w0, -v0 / w0 ** 2, w_new, v_new))
    # 2. HW3 Q3: Y = (phi^-1)_* (d/du^1) on S^2, written in the psi-chart: (u2^2 - u1^2, -2 u1 u2)
    phi_inv = lambda u: np.array([2 * u[0], 2 * u[1], u @ u - 1]) / (u @ u + 1)
    psi = lambda q: q[:2] / (1 + q[2])
    worst, zeros = 0.0, 0
    for _ in range(500):
        ut = rng.normal(size=2) * rng.uniform(0.1, 3)                      # psi-coordinates
        u = ut / (ut @ ut)                                                # phi-coordinates of the same point
        push = (psi(phi_inv(u + e * np.array([1.0, 0.0]))) - psi(phi_inv(u - e * np.array([1.0, 0.0])))) / (2 * e)
        Yt = np.array([ut[1] ** 2 - ut[0] ** 2, -2 * ut[0] * ut[1]])
        worst = max(worst, np.abs(push - Yt).max() / max(1.0, np.abs(Yt).max()))
        assert abs(np.linalg.norm(Yt) - (ut @ ut)) < 1e-9
    print("HW3 Q3: Y = (phi^-1)_* d/du^1 in psi coordinates = (u2^2 - u1^2, -2 u1 u2): max relative error over 500 random points %.1e; |Y| = |u|^2 (zero only at u = 0 = the north pole)" % worst)
    # 3. rank of dF for F(u, v) = (u + v, (u + v)^2) (constant rank 1) and of F: S^2 -> R, F = z (rank 1 except at the poles)
    ranks = set()
    for _ in range(200):
        a, b = rng.normal(size=2) * 3
        ranks.add(np.linalg.matrix_rank(np.array([[1.0, 1.0], [2 * (a + b), 2 * (a + b)]])))
    print("F(u,v) = (u+v, (u+v)^2): rank of DF at 200 random points: %s (constant)" % sorted(ranks))
    # F = z on S^2 in the chart psi_N: z = (|w|^2 - 1)/(|w|^2 + 1); gradient magnitude 4|w| /(|w|^2+1)^2 ; rank drops to 0 at w = 0 (south pole) and as |w| -> infinity (north pole)
    zf = lambda w: (w @ w - 1) / (w @ w + 1)
    for w in ([0.0, 0.0], [1e-3, 0.0], [1.0, 0.0], [1e3, 0.0]):
        w = np.array(w)
        g = jac_fd(zf, w)
        print("   F = z on S^2 at |w| = %-8g: |grad| = %.3e  (rank %d)" % (np.linalg.norm(w), np.linalg.norm(g), np.linalg.matrix_rank(g, tol=1e-9)))
    # 4. rank theorem example from PA13: psi o F o phi^-1 (s, t) = (s, 0) with phi(u,v) = (u+v, v), psi(a,b) = (a, b - a^2)
    Fm = lambda p: np.array([p[0] + p[1], (p[0] + p[1]) ** 2])
    phi_ = lambda p: np.array([p[0] + p[1], p[1]])
    phi_i = lambda q: np.array([q[0] - q[1], q[1]])
    psi_ = lambda q: np.array([q[0], q[1] - q[0] ** 2])
    err = max(np.abs(psi_(Fm(phi_i(q))) - np.array([q[0], 0.0])).max() for q in rng.normal(size=(200, 2)) * 2)
    print("rank theorem normal form psi F phi^-1 = (s, 0): max error over 200 points = %.1e" % err)

# ------------------------------------------------------------------------------------------------------------------ DM05
def dm05():
    print("== DM05 Immersions, Embeddings, Submersions and Coverings")
    # 1. the dense line on the torus: F(t) = (e^{it}, e^{i alpha t}), alpha = sqrt 2: injective immersion, not an embedding
    alpha = np.sqrt(2.0)
    def torus_dist(t):
        a = np.abs((t + np.pi) % (2 * np.pi) - np.pi)
        b = np.abs((alpha * t + np.pi) % (2 * np.pi) - np.pi)
        return np.hypot(a, b)
    print("dense line on T^2 (alpha = sqrt2): smallest distance |F(t) - F(0)| for t in [1, T] (step 1e-3):")
    best, tbest = 9.0, 0.0
    for T in (10, 100, 1000, 10000):
        t = np.arange(1.0, T, 1e-3)
        d = torus_dist(t)
        i = d.argmin()
        print("   T = %-6d min distance = %.5f at t = %.3f" % (T, d[i], t[i]))
    # return times along the continued-fraction denominators: t_n = 2 pi q_n with q_n/p_n ~ alpha  (Dirichlet's approximation)
    qs = [1, 2, 5, 12, 29, 70, 169, 408, 985]
    print("   returns at t = 2 pi q for q in the Pell denominators: distance from F(0) = %s" % ", ".join("%.1e" % torus_dist(2 * np.pi * q) for q in qs))
    # 2. the cusp (t^2, t^3) is not an immersion at t = 0
    print("cusp F(t) = (t^2, t^3): F'(t) = (2t, 3t^2): at t = -1, -0.5, 0, 0.5, 1: %s" % [tuple(np.round([2 * x, 3 * x * x], 3)) for x in (-1, -0.5, 0, 0.5, 1)])
    # 3. det: GL(n,R) -> R^x is a submersion: d(det)_X(B) = det X tr(X^-1 B); B = X gives n det X != 0
    X = rng.normal(size=(3, 3)) + 3 * np.eye(3)
    eps = 1e-6
    fd = (np.linalg.det(X + eps * X) - np.linalg.det(X - eps * X)) / (2 * eps)
    print("det: d(det)_X(X) = %.6f finite difference, n det X = %.6f (so d(det)_X is onto R: rank 1 at every X)" % (fd, 3 * np.linalg.det(X)))
    # 4. z -> z^3 on S^1: 3 sheets, derivative 3
    th = 0.7
    roots = [np.exp(1j * (th + 2 * np.pi * k) / 3) for k in range(3)]
    print("z -> z^3: fibre over e^{0.7i} = %s; each cubes back to e^{0.7i}: max error %.1e; d/dtheta (3 theta) = 3" % (np.round(np.angle(roots), 4).tolist(), max(abs(r ** 3 - np.exp(1j * th)) for r in roots)))
    # 5. a proper injective immersion: t -> (t^3, t) has closed image (graph) and is an embedding: inverse is the projection
    t = rng.normal(size=1000)
    img = np.stack([t ** 3, t], 1)
    print("t -> (t^3, t): inverse = second coordinate; max |inverse(F(t)) - t| = %.1e (a global left inverse: embedding)" % np.abs(img[:, 1] - t).max())

# ------------------------------------------------------------------------------------------------------------------ DM06
def dm06():
    print("== DM06 Submanifolds")
    # 1. O(n) = Phi^{-1}(I), Phi(A) = A A^T: dPhi_A(B) = B A^T + A B^T is onto Sym(n) at every A in GL(n)
    def dPhi_matrix(A):
        n = A.shape[0]
        M = np.zeros((n * n, n * n))
        for k in range(n * n):
            E = np.zeros(n * n)
            E[k] = 1
            B = E.reshape(n, n)
            M[:, k] = (B @ A.T + A @ B.T).reshape(-1)
        return M
    for n in (2, 3, 4, 5):
        Q, _ = np.linalg.qr(rng.normal(size=(n, n)))                       # a random orthogonal matrix
        A = rng.normal(size=(n, n)) + 3 * np.eye(n)                        # a random invertible matrix
        r_o, r_a = np.linalg.matrix_rank(dPhi_matrix(Q)), np.linalg.matrix_rank(dPhi_matrix(A))
        print("  n=%d: rank dPhi_A = %d at a random orthogonal A and %d at a random invertible A; Sym(n) has dimension n(n+1)/2 = %d; dim O(n) = n^2 - rank = %d = n(n-1)/2 = %d"
              % (n, r_o, r_a, n * (n + 1) // 2, n * n - r_o, n * (n - 1) // 2))
    # T_I O(n) = ker dPhi_I = skew matrices; T_I SL(n) = ker tr
    n = 4
    K = dPhi_matrix(np.eye(n))
    u, sv, vt = np.linalg.svd(K)
    ker = vt[np.sum(sv > 1e-10):]
    skew_err = max(np.abs(b.reshape(n, n) + b.reshape(n, n).T).max() for b in ker)
    print("  n=4: kernel of dPhi_I has dimension %d and every kernel vector is skew: max |B + B^T| = %.1e" % (len(ker), skew_err))
    trmat = np.eye(n).reshape(1, -1)
    print("  T_I SL(4) = ker(tr): tr is a 1 x 16 matrix of rank %d, kernel dimension %d = n^2 - 1" % (np.linalg.matrix_rank(trmat), 16 - np.linalg.matrix_rank(trmat)))
    # 2. slice charts: circle near (0.6, 0.8): phi(x, y) = (x, y - sqrt(1 - x^2)); sphere: (x, y, z - sqrt(1 - x^2 - y^2))
    th = np.linspace(0.3, 1.2, 50)
    P = np.stack([np.cos(th), np.sin(th)], 1)
    phi = lambda q: np.array([q[0], q[1] - np.sqrt(1 - q[0] ** 2)])
    print("  slice chart of the circle near (0.6, 0.8): max |second coordinate of phi| on S1 = %.1e; det D phi = 1 at (0.6, 0.8): %.6f" % (max(abs(phi(q)[1]) for q in P), np.linalg.det(jac_fd(phi, [0.6, 0.8]))))
    # 3. T_p S^2 = ker dF_p, F = |x|^2: p = (1/4, 1/2, sqrt11/4); alpha'(1/4) = (1, 2, -5/sqrt11) lies in ker dF_p = p^perp
    p_ = np.array([0.25, 0.5, np.sqrt(11) / 4])
    v_ = np.array([1.0, 2.0, -5 / np.sqrt(11)])
    print("  F = |x|^2 on R^3, dF_p = 2 p^T: dF_p(alpha'(1/4)) = %.1e (= 0: alpha'(1/4) in T_pS^2 = ker dF_p)" % (2 * p_ @ v_))
    # 4. regular and critical levels of F = x^2 - y^2
    for c in (1.0, 0.25, 0.0):
        pts = []
        for x in np.linspace(-2, 2, 400001):
            y2 = x * x - c
            if y2 >= 0:
                pts.append((x, np.sqrt(y2)))
        mg = min(np.hypot(2 * x, 2 * y) for x, y in pts)
        print("  F = x^2 - y^2, level c = %-5g: smallest |grad F| on the level set = %.3e -> %s" % (c, mg, "regular value" if mg > 1e-3 else "critical value (the cross: not a submanifold)"))
    # 5. graph of a smooth function: slice chart (x, y) -> (x, y - f(x))
    f = lambda x: np.sin(3 * x)
    xs = rng.uniform(-2, 2, 100)
    print("  graph y = sin 3x: slice chart (x, y) -> (x, y - f(x)): max |second coord| on the graph = %.1e" % max(abs(f(x) - f(x)) for x in xs))

# ------------------------------------------------------------------------------------------------------------------ DM07
def trefoil(t):
    return np.stack([np.sin(t) + 2 * np.sin(2 * t), np.cos(t) - 2 * np.cos(2 * t), -np.sin(3 * t)], -1)


def dm07():
    print("== DM07 Sard, Whitney and Transversality")
    # 1. Sard in dimension 1: f(x) = x^3 - 3x has critical points +-1 and critical values -+2: a finite (measure zero) set
    f = lambda x: x ** 3 - 3 * x
    fp = lambda x: 3 * x ** 2 - 3
    xs = np.linspace(-3, 3, 600001)
    crit = xs[np.abs(fp(xs)) < 1e-5]
    print("f = x^3 - 3x: critical points near %s; critical values %s" % (np.unique(np.round(crit, 2)).tolist(), np.unique(np.round(f(crit), 3)).tolist()))
    cs = rng.uniform(-6, 6, 100000)
    frac_reg = np.mean([np.min(np.abs(fp(np.roots([1, 0, -3, -c]).real[np.abs(np.roots([1, 0, -3, -c]).imag) < 1e-9]))) > 1e-9 for c in cs[:5000]])
    print("   fraction of 5000 random values c in [-6, 6] that are regular values: %.4f (Sard: all but a null set)" % frac_reg)
    # 2. F: R -> R^2, F(t) = (t, t^2): dim M < dim N so the image has measure zero (a curve in the plane contains no open set): area of the epsilon-neighbourhood -> 0
    from scipy.spatial import cKDTree
    t = np.linspace(-1, 1, 20001)
    tree = cKDTree(np.stack([t, t * t], 1))
    L = np.sqrt(5) + 0.5 * np.arcsinh(2)
    for eps in (0.1, 0.03, 0.01):
        g = np.arange(-1.3, 1.3, eps / 4)
        gx, gy = np.meshgrid(g, g)
        d, _ = tree.query(np.stack([gx.ravel(), gy.ravel()], 1))
        area = np.mean(d < eps) * (g[-1] - g[0]) ** 2
        print("   epsilon = %-5g: area of the epsilon-neighbourhood of the parabola arc = %.4f  (2 eps L = %.4f, L = %.3f): -> 0 with eps" % (eps, area, 2 * eps * L, L))
    # 3. Whitney: directions of secants and tangents of a space curve cover (almost) all of S^2: dimension count 2n = 2 = dim S^2 when N = 2n + 1 = 3
    T = np.linspace(0, 2 * np.pi, 1500, endpoint=False)
    P = trefoil(T)
    i, j = np.triu_indices(len(T), 1)
    keep = (np.abs(i - j) > 3) & (np.abs(i - j) < len(T) - 3)
    d = P[j[keep]] - P[i[keep]]
    d /= np.linalg.norm(d, axis=1)[:, None]
    d = np.vstack([d, -d])
    lon, lat = np.degrees(np.arctan2(d[:, 1], d[:, 0])), np.degrees(np.arcsin(np.clip(d[:, 2], -1, 1)))
    H, _, _ = np.histogram2d(lon, np.sin(np.radians(lat)), bins=(36, 18), range=((-180, 180), (-1, 1)))
    print("trefoil curve in R^3: secant directions (unit vectors of x(t)-x(s)), equal-area bins of S^2 covered: %.1f%% of %d bins" % (100 * np.mean(H > 0), H.size))
    # 4. transversality: the parabola y = x^2 - c meets the x-axis transversally iff c != 0
    for c in (0.25, 0.0, -0.25):
        xs = np.roots([1, 0, -c]) if c != 0 else np.array([0.0])
        xs = xs[np.isreal(xs)].real
        angle = [np.degrees(np.arctan(2 * x)) for x in xs]
        print("   y = x^2 - %-5g meets y = 0 at x = %s with slope angle %s degrees -> %s" % (c, np.round(xs, 3).tolist(), np.round(angle, 2).tolist(), "transverse" if all(abs(a) > 1e-9 for a in angle) and len(xs) else ("tangent (not transverse)" if len(xs) else "no intersection")))

# ------------------------------------------------------------------------------------------------------------------ DM08
def quat_R(q):
    w, x, y, z = q
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def dm08():
    print("== DM08 Lie Groups")
    # 1. HW4 Q6: dm_(e,e)(X, Y) = X + Y and di_e(X) = -X for G = GL(3, R)
    n = 3
    X, Y = rng.normal(size=(n, n)), rng.normal(size=(n, n))
    eps = 1e-6
    I = np.eye(n)
    dm = ((I + eps * X) @ (I + eps * Y) - (I - eps * X) @ (I - eps * Y)) / (2 * eps)
    di = (np.linalg.inv(I + eps * X) - np.linalg.inv(I - eps * X)) / (2 * eps)
    print("GL(3): dm_(e,e)(X, Y) = X + Y: max error %.1e;  di_e(X) = -X: max error %.1e" % (np.abs(dm - (X + Y)).max(), np.abs(di + X).max()))
    # 2. HW5 Q2: F(g, h) = (g, gh) has invertible differential dF(X, Y) = (X, X h + g Y) (here for GL(2))
    g, h = rng.normal(size=(2, 2)) + 2 * np.eye(2), rng.normal(size=(2, 2)) + 2 * np.eye(2)
    def F(v):
        a, b = v[:4].reshape(2, 2), v[4:].reshape(2, 2)
        return np.concatenate([a.reshape(-1), (a @ b).reshape(-1)])
    J = jac_fd(F, np.concatenate([g.reshape(-1), h.reshape(-1)]))
    print("HW5 Q2: Jacobian of F(g,h) = (g, gh) on GL(2) x GL(2) is 8 x 8 with rank %d and |det| = %.4f (block triangular: det = det(g)^2 = %.4f)" % (np.linalg.matrix_rank(J, tol=1e-6), abs(np.linalg.det(J)), np.linalg.det(g) ** 2))
    # 3. homomorphisms have constant rank: det: GL(3) -> R^x (rank 1); eps: R -> T^2, t -> (e^{it}, e^{i sqrt2 t}) (rank 1); SU(2) -> SO(3) (rank 3)
    r_det = {np.linalg.matrix_rank(jac_fd(lambda v: np.array([np.linalg.det(v.reshape(3, 3))]), (rng.normal(size=(3, 3)) + 3 * np.eye(3)).reshape(-1), 1e-6), tol=1e-5) for _ in range(20)}
    print("homomorphism det: GL(3) -> R^x has rank %s at 20 random points (constant rank 1; kernel SL(3) of dimension 9 - 1 = 8)" % sorted(r_det))
    r_tor = {np.linalg.matrix_rank(jac_fd(lambda t: np.array([np.cos(t[0]), np.sin(t[0]), np.cos(np.sqrt(2) * t[0]), np.sin(np.sqrt(2) * t[0])]), rng.normal(size=1) * 20), tol=1e-6) for _ in range(20)}
    print("homomorphism R -> T^2 (t -> (e^{it}, e^{i sqrt2 t})) has rank %s at 20 random points (an injective immersion: kernel trivial)" % sorted(r_tor))
    ranks = set()
    for _ in range(40):
        q = rng.normal(size=4)
        q /= np.linalg.norm(q)
        # tangent space of S^3 at q: orthogonal complement; differential of q -> R(q) restricted to it
        Q, _ = np.linalg.qr(np.column_stack([q, rng.normal(size=(4, 3))]))
        T = Q[:, 1:]
        D = np.column_stack([(quat_R(q + 1e-6 * T[:, k]) - quat_R(q - 1e-6 * T[:, k])).reshape(-1) / 2e-6 for k in range(3)])
        ranks.add(np.linalg.matrix_rank(D, tol=1e-5))
    print("homomorphism SU(2) = S^3 -> SO(3) has rank %s at 40 random points (constant rank 3 = dim SU(2): a covering, kernel {+-1} is 0-dimensional)" % sorted(ranks))
    # 4. components: sign of det on random matrices; GL(n,R) has 2 components, det > 0 is the identity component
    M = rng.normal(size=(100000, 3, 3))
    d = np.linalg.det(M)
    print("GL(3,R): %.1f%% of random matrices have det > 0 (the identity component), %.1f%% have det < 0" % (100 * np.mean(d > 0), 100 * np.mean(d < 0)))
    def haar(n_):
        Q_, R_ = np.linalg.qr(rng.normal(size=(n_, n_)))
        return Q_ * np.sign(np.diag(R_))
    Qs = np.array([haar(3) for _ in range(2000)])
    ds = np.linalg.det(Qs)
    print("O(3): det = +1 for %.1f%% and -1 for %.1f%% of random orthogonal matrices (|det| = 1 always: %.1e); SO(3) is the identity component" % (100 * np.mean(ds > 0), 100 * np.mean(ds < 0), np.abs(np.abs(ds) - 1).max()))
    # 5. HW5 Q4 in the Lie group (R_{>0}, x): for U = (0.95, 1.05) find V = (1 - d, 1 + d) with g h^-1 in U for all g, h in V
    d = min((1.05 - 1) / (1.05 + 1), (1 - 0.95) / (1 + 0.95))
    lo, hi = (1 - d) / (1 + d), (1 + d) / (1 - d)
    print("HW5 Q4 in (R_{>0}, x), U = (0.95, 1.05): V = (1 - d, 1 + d) works iff (1+d)/(1-d) <= 1.05 and (1-d)/(1+d) >= 0.95; largest d = %.5f gives g/h in [%.5f, %.5f]" % (d, lo, hi))

# ------------------------------------------------------------------------------------------------------------------ DM09
def dm09():
    print("== DM09 Group Actions and Semidirect Products")
    # 1. orbit map of GL(n,R) acting on M(n,R) by A.X = A X A^T at X = I: d(theta^(I))_I(B) = B + B^T; stabiliser O(n)
    for n in (2, 3, 4):
        M = np.zeros((n * n, n * n))
        for k in range(n * n):
            E = np.zeros(n * n); E[k] = 1; B = E.reshape(n, n)
            M[:, k] = (B + B.T).reshape(-1)
        r = np.linalg.matrix_rank(M)
        print("  GL(%d,R) on M(%d) by congruence: rank of the orbit map at I = %d (= dim Sym = %d); dim stabiliser O(%d) = %d - %d = %d (= n(n-1)/2 = %d)" % (n, n, r, n * (n + 1) // 2, n, n * n, r, n * n - r, n * (n - 1) // 2))
    # 2. HW6 Q2: GL(n,C) on Hermitian matrices by A.X = A X A^*, stabiliser of I is U(n): orbit map B -> B + B^*, real rank n^2
    for n in (1, 2, 3):
        cols = []
        for k in range(2 * n * n):
            v = np.zeros(2 * n * n); v[k] = 1
            B = (v[:n * n] + 1j * v[n * n:]).reshape(n, n)
            C = B + B.conj().T
            cols.append(np.concatenate([C.real.reshape(-1), C.imag.reshape(-1)]))
        r = np.linalg.matrix_rank(np.array(cols).T)
        print("  GL(%d,C) on Hermitian matrices: real rank of B -> B + B^* is %d = n^2 = %d; dim U(%d) = 2n^2 - n^2 = %d" % (n, r, n * n, n, 2 * n * n - r))
    # 3. SO(3) acts on S^2: orbit map at N = (0,0,1): B -> B e3 for skew B has rank 2; stabiliser SO(2) of dimension 3 - 2 = 1
    skew = [np.array([[0, -c, b], [c, 0, -a], [-b, a, 0]]) for a, b, c in np.eye(3)]
    print("  SO(3) on S^2: rank of B -> B e_3 on skew B is %d = dim S^2, stabiliser of N has dimension 3 - %d = %d" % (np.linalg.matrix_rank(np.array([B @ np.array([0, 0, 1.0]) for B in skew])), 2, 1))
    print("  homogeneous spaces (dimension counts): S^n = O(n+1)/O(n): n(n+1)/2 - n(n-1)/2 = n; S^(2n+1) = U(n+1)/U(n): (n+1)^2 - n^2 = %d (n = 3: %d); S^2 = SU(2)/U(1): 3 - 1 = 2; RP^n = O(n+1)/(O(n) x O(1)): n" % (2 * 3 + 1, 2 * 3 + 1))
    # 4. HW6 Q3b: O(n) = SO(n) x| O(1): A = N psi(det A), N = A psi(det A)^-1 in SO(n), psi(s) = diag(s, 1, ..., 1); check on random orthogonal matrices
    def haar(n_):
        Q_, R_ = np.linalg.qr(rng.normal(size=(n_, n_)))
        return Q_ * np.sign(np.diag(R_))
    psi = lambda sgn, n_: np.diag([sgn] + [1.0] * (n_ - 1))
    errs = []
    for _ in range(500):
        A = haar(4)
        s_ = np.sign(np.linalg.det(A))
        N = A @ np.linalg.inv(psi(s_, 4))
        errs.append(max(abs(np.linalg.det(N) - 1), np.abs(N @ psi(s_, 4) - A).max()))
    print("  HW6 Q3b: O(4) = SO(4) x| O(1): 500 random A: A = N psi(det A) with det N = 1: max error %.1e" % max(errs))
    # semidirect law (n1,h1)(n2,h2) = (n1 theta_h1(n2), h1 h2) with theta_h(n) = psi(h) n psi(h)^-1 reproduces matrix multiplication
    A1, A2 = haar(4), haar(4)
    s1, s2 = np.sign(np.linalg.det(A1)), np.sign(np.linalg.det(A2))
    n1, n2 = A1 @ psi(s1, 4), A2 @ psi(s2, 4)       # not needed; use the real splitting below
    N1, N2 = A1 @ np.linalg.inv(psi(s1, 4)), A2 @ np.linalg.inv(psi(s2, 4))
    th = lambda s, N: psi(s, 4) @ N @ np.linalg.inv(psi(s, 4))
    lhs = A1 @ A2
    rhs = (N1 @ th(s1, N2)) @ psi(s1 * s2, 4)
    print("  semidirect law (N1, s1)(N2, s2) = (N1 theta_s1(N2), s1 s2) vs matrix product: max error %.1e" % np.abs(lhs - rhs).max())
    # 5. HW6 Q3c: GL(n,C) = SL(n,C) x| C^x with psi(lam) = diag(lam, 1, ..., 1)
    n = 3
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    lam = np.linalg.det(A)
    P = np.diag([lam] + [1.0] * (n - 1))
    S = A @ np.linalg.inv(P)
    print("  HW6 Q3c: A in GL(3,C): S = A psi(det A)^-1 has det S = %.6f%+.1ej (should be 1) and A = S psi(det A): error %.1e" % (np.linalg.det(S).real, np.linalg.det(S).imag, np.abs(S @ P - A).max()))
    # 6. affine group of the line, Aff(1) = R x| R^x with (b1, a1)(b2, a2) = (b1 + a1 b2, a1 a2) = composition of x -> a x + b
    b1, a1, b2, a2 = 0.7, 1.9, -1.3, 0.4
    f = lambda x, a, b: a * x + b
    x0 = 0.55
    print("  Aff(1): (f_{b1,a1} o f_{b2,a2})(x0) = %.6f; semidirect product (b1 + a1 b2, a1 a2) applied to x0 = %.6f" % (f(f(x0, a2, b2), a1, b1), f(x0, a1 * a2, b1 + a1 * b2)))
    # 7. Euclidean group E(2) = R^2 x| SO(2) as 3x3 matrices [[R, t], [0, 1]]
    def E(th_, t):
        c, s_ = np.cos(th_), np.sin(th_)
        return np.array([[c, -s_, t[0]], [s_, c, t[1]], [0, 0, 1.0]])
    th1, t1, th2, t2 = 0.8, np.array([1.0, 2.0]), -0.3, np.array([-0.5, 0.25])
    R = lambda a: np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    prod = E(th1, t1) @ E(th2, t2)
    law = E(th1 + th2, t1 + R(th1) @ t2)
    print("  E(2) = R^2 x| SO(2): matrix product vs (t1 + R(th1) t2, th1 + th2): max error %.1e" % np.abs(prod - law).max())


# ------------------------------------------------------------------------------------------------------------------ DM10
def dm10():
    print("== DM10 Vector Fields and Lie Brackets")
    x, y, z = sp.symbols("x y z", real=True)
    u, v = sp.symbols("u v", positive=True)

    def vf(comps, coords):
        return sp.Matrix(comps)

    def apply(X, f, coords):
        return sum(X[i] * sp.diff(f, coords[i]) for i in range(len(coords)))

    def bracket(X, Y, coords):
        return sp.Matrix([sp.simplify(apply(X, Y[i], coords) - apply(Y, X[i], coords)) for i in range(len(coords))])

    c3 = (x, y, z)
    # 1. HW4 Q3: F(x,y) = (xy, y/x) on the open quadrant; X = x d_x + y d_y; Y = dF(X) o F^-1
    c2 = (x, y)
    Fm = sp.Matrix([x * y, y / x])
    DF = Fm.jacobian(sp.Matrix(c2))
    Xe = sp.Matrix([x, y])
    Yxy = sp.simplify(DF * Xe)
    inv = {x: sp.sqrt(u / v), y: sp.sqrt(u * v)}
    Yuv = sp.simplify(Yxy.subs(inv, simultaneous=True))
    print("  HW4 Q3: det DF = %s (nonzero on the quadrant); F^-1(u,v) = (sqrt(u/v), sqrt(uv)); dF(X) in (x,y): %s -> Y(u,v) = %s" % (sp.simplify(DF.det()), list(Yxy), list(Yuv)))
    rr = np.random.default_rng(3)
    err = 0.0
    for _ in range(200):
        a, b = rr.uniform(0.2, 3, 2)
        q = np.array([a * b, b / a])
        step = 1e-6
        Fnum = lambda t: np.array([(a + t * a) * (b + t * b), (b + t * b) / (a + t * a)])     # curve through (a,b) with velocity X = (a, b)
        d = (Fnum(step) - Fnum(-step)) / (2 * step)
        err = max(err, np.abs(d - np.array([2 * q[0], 0.0])).max())
    print("      finite-difference check of Y = (2u, 0) along the flow lines of X at 200 random points: max error %.1e" % err)
    # 2. HW6 Q5
    X5 = sp.Matrix([-y, x, 0])
    Y5 = sp.Matrix([0, -z, y])
    print("  HW6 Q5: [x d_y - y d_x, y d_z - z d_y] = %s  (i.e. x d_z - z d_x)" % list(bracket(X5, Y5, c3)))
    # rotation generators and the sign
    Lx, Ly, Lz = sp.Matrix([0, -z, y]), sp.Matrix([z, 0, -x]), sp.Matrix([-y, x, 0])
    print("      [Lx, Ly] + Lz = %s ; [Ly, Lz] + Lx = %s ; [Lz, Lx] + Ly = %s  (vector-field bracket of rotation generators is MINUS the matrix commutator)"
          % (list(bracket(Lx, Ly, c3) + Lz), list(bracket(Ly, Lz, c3) + Lx), list(bracket(Lz, Lx, c3) + Ly)))
    # 3. Jacobi, product rule (Lee Prop 8.28)
    A = sp.Matrix([x * y, z, x ** 2 - y])
    B = sp.Matrix([sp.sin(x), y * z, 1 + x * z])
    C = sp.Matrix([y, x * z, x * y * z])
    jac = bracket(A, bracket(B, C, c3), c3) + bracket(B, bracket(C, A, c3), c3) + bracket(C, bracket(A, B, c3), c3)
    print("  Jacobi identity for three polynomial/trigonometric fields on R^3: [A,[B,C]] + [B,[C,A]] + [C,[A,B]] = %s" % [sp.simplify(t) for t in jac])
    f, g = x ** 2 * y + z, sp.exp(y) + x * z
    lhs = bracket(f * A, g * B, c3)
    rhs = f * g * bracket(A, B, c3) + apply(A, g, c3) * f * B - apply(B, f, c3) * g * A
    print("      [fA, gB] - (fg [A,B] + f (A g) B - g (B f) A) = %s" % [sp.simplify(t) for t in (lhs - rhs)])
    # 4. XY is not a derivation: X = d_x, Y = x d_y, f = x, g = y (Lee Ex. 8.24); [X,Y] = d_y
    Xa, Ya = sp.Matrix([1, 0]), sp.Matrix([0, x])
    fa, ga = x, y
    XY = lambda h: apply(Xa, apply(Ya, h, c2), c2)
    print("  X = d_x, Y = x d_y, f = x, g = y: XY(fg) = %s but f XY(g) + g XY(f) = %s (XY is not a derivation); [X,Y] = %s" % (sp.simplify(XY(fa * ga)), sp.simplify(fa * XY(ga) + ga * XY(fa)), list(bracket(Xa, Ya, c2))))
    # 5. naturality under the diffeomorphism F of HW4 Q3: F_*[X1,X2] = [F_*X1, F_*X2]
    X1 = sp.Matrix([x, y])
    X2 = sp.Matrix([y, x ** 2])
    br = bracket(X1, X2, c2)
    push = lambda W: sp.simplify((DF * W).subs(inv, simultaneous=True))
    lhs = push(br)
    rhs = bracket(push(X1), push(X2), (u, v))
    print("  naturality (Lee Cor 8.31), F = (xy, y/x): F_*[X1,X2] = %s ; [F_*X1, F_*X2] = %s ; difference %s" % (list(lhs), list(rhs), [sp.simplify(t) for t in (lhs - rhs)]))
    # 6. Euler and rotation fields on R^2: coordinate fields in polar coordinates commute
    E2, R2 = sp.Matrix([x, y]), sp.Matrix([-y, x])
    print("  Euler E = x d_x + y d_y, rotation R = -y d_x + x d_y: [E,R] = %s (E = r d_r, R = d_theta, [r d_r, d_theta] = 0); [E, d_x] = %s" % (list(bracket(E2, R2, c2)), list(bracket(E2, sp.Matrix([1, 0]), c2))))
    # 7. coordinate formula versus the definition on a random test function, finite-difference-free: apply to f
    ftest = sp.sin(x * y) + z ** 2
    lhs = apply(A, apply(B, ftest, c3), c3) - apply(B, apply(A, ftest, c3), c3)
    rhs = apply(bracket(A, B, c3), ftest, c3)
    print("  [A,B] f = A(Bf) - B(Af) agrees with the coordinate formula: %s" % sp.simplify(lhs - rhs))


# ------------------------------------------------------------------------------------------------------------------ DM11
def _apply(X, f, coords):
    return sum(X[i] * sp.diff(f, coords[i]) for i in range(len(coords)))


def _bracket(X, Y, coords):
    return sp.Matrix([sp.simplify(_apply(X, Y[i], coords) - _apply(Y, X[i], coords)) for i in range(len(coords))])


def dm11():
    print("== DM11 The Lie Algebra of a Lie Group")
    # 1. Lie(GL(n)): the left-invariant field with value A at I is X |-> XA; its bracket is the field of AB - BA
    for n in (2,):
        xs = sp.symbols("x1:%d" % (n * n + 1))
        X = sp.Matrix(n, n, xs)
        A = sp.Matrix(n, n, sp.symbols("a1:%d" % (n * n + 1)))
        B = sp.Matrix(n, n, sp.symbols("b1:%d" % (n * n + 1)))
        fA = list(X * A)
        fB = list(X * B)
        br = _bracket(sp.Matrix(fA), sp.Matrix(fB), xs)
        target = list(X * (A * B - B * A))
        print("  GL(%d): [A~, B~] - (X(AB-BA)) = %s  (A~_X = XA with symbolic entries a_ij, b_ij)" % (n, [sp.simplify(br[i] - target[i]) for i in range(n * n)]))
    # the same for n = 3 with fixed integer matrices
    n = 3
    xs = sp.symbols("y1:10")
    X = sp.Matrix(3, 3, xs)
    A = sp.Matrix([[1, 2, 0], [0, -1, 3], [2, 1, 1]])
    B = sp.Matrix([[0, 1, 1], [1, 0, -2], [3, 1, 0]])
    br = _bracket(sp.Matrix(list(X * A)), sp.Matrix(list(X * B)), xs)
    print("  GL(3): [A~, B~] - X(AB-BA) = zero field: %s" % (sp.simplify(br - sp.Matrix(list(X * (A * B - B * A)))) == sp.zeros(9, 1)))
    # 2. dimensions of the Lie algebras as kernels of the differentials at I
    def nulldim(rows_fn, n_unknown):
        M = np.array([rows_fn(e) for e in np.eye(n_unknown)]).T
        return n_unknown - np.linalg.matrix_rank(M, tol=1e-10)
    out = []
    for n in (2, 3, 4):
        # real matrices: so(n) = {A + A^T = 0}; sl(n) = {tr A = 0}
        so = nulldim(lambda e, n=n: (e.reshape(n, n) + e.reshape(n, n).T).ravel(), n * n)
        sl = nulldim(lambda e, n=n: [np.trace(e.reshape(n, n))], n * n)
        # complex matrices as 2 n^2 real unknowns (real, imag parts): u(n) = {A + A^* = 0}; su(n) adds tr A = 0
        def cplx(e, n=n):
            return (e[:n * n] + 1j * e[n * n:]).reshape(n, n)
        un = nulldim(lambda e, n=n: np.concatenate([(cplx(e) + cplx(e).conj().T).real.ravel(), (cplx(e) + cplx(e).conj().T).imag.ravel()]), 2 * n * n)
        su = nulldim(lambda e, n=n: np.concatenate([(cplx(e) + cplx(e).conj().T).real.ravel(), (cplx(e) + cplx(e).conj().T).imag.ravel(), [np.trace(cplx(e)).real, np.trace(cplx(e)).imag]]), 2 * n * n)
        out.append("n=%d: dim so=%d (n(n-1)/2=%d), sl=%d (n^2-1=%d), u=%d (n^2=%d), su=%d (n^2-1=%d)" % (n, so, n * (n - 1) // 2, sl, n * n - 1, un, n * n, su, n * n - 1))
    print("  dimensions of the Lie algebras as kernels (real dimension):\n    " + "\n    ".join(out))
    # 3. tr is the induced map of det (HW6 Q7) and tr[A,B] = 0
    r = np.random.default_rng(5)
    A4, B4 = r.normal(size=(4, 4)), r.normal(size=(4, 4))
    t = 1e-6
    print("  HW6 Q7: d/dt det(I + tA)|0 = %.6f (central difference) vs tr A = %.6f; tr[A,B] = %.1e" % ((np.linalg.det(np.eye(4) + t * A4) - np.linalg.det(np.eye(4) - t * A4)) / (2 * t), np.trace(A4), np.trace(A4 @ B4 - B4 @ A4)))
    # 4. so(3) = (R^3, x): the hat map
    hat = lambda w: np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
    e = np.eye(3)
    Ex, Ey, Ez = hat(e[0]), hat(e[1]), hat(e[2])
    comm = lambda P, Q: P @ Q - Q @ P
    print("  [E_x,E_y] - E_z = %.1e, [E_y,E_z] - E_x = %.1e, [E_z,E_x] - E_y = %.1e (matrix commutators of the skew generators: plus signs)"
          % (np.abs(comm(Ex, Ey) - Ez).max(), np.abs(comm(Ey, Ez) - Ex).max(), np.abs(comm(Ez, Ex) - Ey).max()))
    err = 0.0
    for _ in range(1000):
        w, v = r.normal(size=3), r.normal(size=3)
        err = max(err, np.abs(comm(hat(w), hat(v)) - hat(np.cross(w, v))).max())
        assert np.abs(comm(hat(w), hat(v)) + comm(hat(w), hat(v)).T).max() < 1e-12
    print("  hat map: [hat(w), hat(v)] = hat(w x v) at 1000 random pairs: max error %.1e; commutators of skew matrices are skew (checked)" % err)
    # 5. su(2) = so(3): tau_k = -i sigma_k / 2 and the differential of Ad: SU(2) -> SO(3) at the identity
    sg = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    tau = [-0.5j * s_ for s_ in sg]
    cc = lambda P, Q: P @ Q - Q @ P
    print("  su(2): [tau_1,tau_2] - tau_3 = %.1e, [tau_2,tau_3] - tau_1 = %.1e, [tau_3,tau_1] - tau_2 = %.1e" % (np.abs(cc(tau[0], tau[1]) - tau[2]).max(), np.abs(cc(tau[1], tau[2]) - tau[0]).max(), np.abs(cc(tau[2], tau[0]) - tau[1]).max()))
    from scipy.linalg import expm
    def Ad(U):
        return np.array([[0.5 * np.trace(sg[j] @ U @ sg[k] @ U.conj().T).real for k in range(3)] for j in range(3)])
    errs = []
    for k in range(3):
        dAd = (Ad(expm(1e-6 * tau[k])) - Ad(expm(-1e-6 * tau[k]))) / 2e-6
        errs.append(np.abs(dAd - [Ex, Ey, Ez][k]).max())
    print("      differential at I of Ad: SU(2) -> SO(3), R(U)_jk = (1/2) tr(sigma_j U sigma_k U*): d R(tau_k) = E_k with errors %s; so F_* is the isomorphism tau_k -> E_k (kernel {+-1} is discrete)" % ", ".join("%.1e" % q for q in errs))
    # 6. two-dimensional non-abelian Lie algebras: [e1,e2] = w, normal form [f1,f2] = f2
    ok = 0
    for _ in range(100):
        a, b = r.normal(size=2)
        w = np.array([a, b])                                        # [e1, e2] = a e1 + b e2
        f2 = w
        f1 = np.array([1.0, 0.0]) if abs(b) > 1e-3 else np.array([0.0, 1.0])
        c = f1[0] * f2[1] - f1[1] * f2[0]                          # f1 ^ f2 = c e1 ^ e2, so [f1, f2] = c w = c f2
        f1n = f1 / c                                               # [f1/c, f2] = f2
        ok += abs((f1n[0] * f2[1] - f1n[1] * f2[0]) - 1.0) < 1e-9
    E11 = np.array([[1, 0], [0, 0.0]]); E12 = np.array([[0, 1], [0, 0.0]])
    print("  HW7 Q1: normal form [f1,f2] = f2 reached for %d/100 random non-abelian structure constants; matrix realisation [E_11, E_12] = E_12: error %.1e (Lie algebra of Aff(1))" % (ok, np.abs(cc(E11, E12) - E12).max()))

    # 7. Aff(1) = {(b, a): a > 0} with (b1, a1)(b2, a2) = (b1 + a1 b2, a1 a2): left-invariant fields and their bracket
    b_, a_ = sp.symbols("b a", positive=True)
    b1, a1 = sp.symbols("b1 a1", positive=True)
    Lg = sp.Matrix([b1 + a1 * b_, a1 * a_])
    JL = Lg.jacobian(sp.Matrix([b_, a_]))
    e0 = {b_: 0, a_: 1}
    Xl1 = sp.simplify((JL * sp.Matrix([1, 0])).subs(e0)); Xl2 = sp.simplify((JL * sp.Matrix([0, 1])).subs(e0))
    X1 = sp.Matrix([a_, 0]); X2 = sp.Matrix([0, a_])
    brk = _bracket(X1, X2, (b_, a_))
    print("  Aff(1): d(L_g)_e e_b = %s and d(L_g)_e e_a = %s at g = (b1,a1), i.e. left-invariant fields X1 = a d_b, X2 = a d_a; [X1,X2] = %s = -X1; so [X2,X1] = X1 (normal form [f1,f2] = f2 with f1 = X2, f2 = X1)" % (list(Xl1), list(Xl2), list(brk)))


# ------------------------------------------------------------------------------------------------------------------ DM12
def dm12():
    from scipy.integrate import solve_ivp
    print("== DM12 Integral Curves, Flows and Flowouts")
    r = np.random.default_rng(12)
    # 1. HW7 Q5: V = y d_x + d_y: theta_t(x0, y0) = (x0 + y0 t + t^2/2, y0 + t)
    th = lambda t, p: np.array([p[0] + p[1] * t + t * t / 2, p[1] + t])
    err = 0.0
    gerr = 0.0
    for _ in range(50):
        p0 = r.normal(size=2) * 2
        T = r.uniform(-2, 2)
        sol = solve_ivp(lambda t, q: [q[1], 1.0], [0, T], p0, rtol=1e-11, atol=1e-12)
        err = max(err, np.abs(sol.y[:, -1] - th(T, p0)).max())
        s_, t_ = r.uniform(-2, 2, 2)
        gerr = max(gerr, np.abs(th(s_, th(t_, p0)) - th(s_ + t_, p0)).max())
    print("  HW7 Q5: V = y d_x + d_y has flow (x0 + y0 t + t^2/2, y0 + t): RK vs formula over 50 random (p, t): max error %.1e; group law theta_s theta_t = theta_{s+t}: max error %.1e" % (err, gerr))
    # 2. blow-up: W = x^2 d_x, x(t) = x0/(1 - x0 t); D^(p) = (-inf, 1/x0) for x0 > 0, (1/x0... ) for x0 < 0
    for x0 in (2.0, 0.5, -2.0):
        ev = lambda t, q: abs(q[0]) - 1e6
        ev.terminal = True
        sol = solve_ivp(lambda t, q: [q[0] ** 2], [0, 10], [x0], rtol=1e-12, atol=1e-12, events=ev)
        te = sol.t_events[0][0] if len(sol.t_events[0]) else None
        print("  W = x^2 d_x from x0 = %5.2f: |x| reaches 10^6 at t = %s; exact blow-up time 1/x0 = %s" % (x0, ("%.7f" % te) if te is not None else "never (t <= 10)", ("%.7f" % (1 / x0)) if x0 > 0 else "none for t > 0 (D = (-1/2, inf))"))
    # 3. rescaling lemma and periodicity for V = -y d_x + x d_y
    R = lambda t, p: np.array([p[0] * np.cos(t) - p[1] * np.sin(t), p[0] * np.sin(t) + p[1] * np.cos(t)])
    p0 = np.array([0.7, -1.3])
    a, t = 2.5, 0.37
    e = 1e-6
    d = (R(a * (t + e), p0) - R(a * (t - e), p0)) / (2 * e)
    Vf = lambda q: np.array([-q[1], q[0]])
    print("  rescaling lemma: d/dt gamma(a t) - a V(gamma(a t)) at a = 2.5: %.1e; period: |gamma(2 pi) - gamma(0)| = %.1e, |gamma(pi) - gamma(0)| = %.3f (so the minimal period is 2 pi)" % (np.abs(d - a * Vf(R(a * t, p0))).max(), np.abs(R(2 * np.pi, p0) - p0).max(), np.abs(R(np.pi, p0) - p0).max()))
    # 4. left-invariant fields are complete: the integral curve of A~ through X0 in GL(2) is X0 exp(tA), det = det X0 e^{t tr A} never 0
    from scipy.linalg import expm
    A = r.normal(size=(2, 2))
    X0 = r.normal(size=(2, 2))
    T = 3.0
    sol = solve_ivp(lambda t, y: (y.reshape(2, 2) @ A).ravel(), [0, T], X0.ravel(), rtol=1e-12, atol=1e-12)
    Xend = sol.y[:, -1].reshape(2, 2)
    print("  GL(2): integral curve of the left-invariant field A~ (A~_X = XA) through X0: RK at t = 3 vs X0 expm(3A): error %.1e; det X(3) = %.5f vs det X0 e^{3 tr A} = %.5f (never zero: the curve stays in GL(2))"
          % (np.abs(Xend - X0 @ expm(T * A)).max(), np.linalg.det(Xend), np.linalg.det(X0) * np.exp(T * np.trace(A))))
    # 5. flowout of S = {(s,0,0): s>0} along the helical field V = -y d_x + x d_y + d_z: Phi(t,s) = (s cos t, s sin t, t)
    Phi = lambda t, s: np.array([s * np.cos(t), s * np.sin(t), t])
    Vh = lambda q: np.array([-q[1], q[0], 1.0])
    mins = []
    err = 0.0
    for t_ in np.linspace(-12, 12, 97):
        for s_ in np.linspace(0.1, 3, 30):
            dPt = np.array([-s_ * np.sin(t_), s_ * np.cos(t_), 1.0])            # dPhi(d_t)
            dPs = np.array([np.cos(t_), np.sin(t_), 0.0])                       # dPhi(d_s)
            mins.append(np.linalg.svd(np.column_stack([dPt, dPs]), compute_uv=False).min())
            err = max(err, np.abs(dPt - Vh(Phi(t_, s_))).max())
    print("  flowout of the half-axis along the helical field: dPhi(d_t) = V o Phi (error %.1e), smallest singular value of dPhi over a grid = %.3f > 0 (Phi is an immersion; the image is a helicoid)" % (err, min(mins)))
    # 6. Example 9.23: S = positive x-axis, W = -y d_x + x d_y: Phi(t,s) = (s cos t, s sin t), det dPhi = s
    dets = [np.linalg.det(np.array([[-s_ * np.sin(t_), np.cos(t_)], [s_ * np.cos(t_), np.sin(t_)]])) for t_ in np.linspace(-3, 3, 13) for s_ in np.linspace(0.2, 4, 10)]
    print("  codimension 1: Phi(t,s) = (s cos t, s sin t) on (-pi,pi) x (0,inf) has det dPhi = -s: range %.2f .. %.2f (never 0); image = plane minus the closed negative x-axis; W = d_t in these polar coordinates" % (min(dets), max(dets)))
    # 7. HW7 Q6: minimal period on the torus T^2 for the field d_theta1 + d_theta2 (nowhere zero): theta_t has fixed points only for t in 2 pi Z
    print("  HW7 Q6: on T^2 the flow of d_1 + d_2 is theta_t(a, b) = (a + t, b + t) mod 2 pi; for 0 < t < 2 pi it has no fixed point (a + t = a mod 2 pi forces t in 2 pi Z): F = theta_t is homotopic to the identity (via theta_{st}) without fixed points")


# ------------------------------------------------------------------------------------------------------------------ DM13
def dm13():
    print("== DM13 Lie Derivatives and Commuting Vector Fields")
    r = np.random.default_rng(13)
    x, y, z = sp.symbols("x y z", real=True)
    c2 = (x, y)
    # 1. L_V W = [V, W] checked through the flow: V = y d_x + d_y (flow (x + y t + t^2/2, y + t)), W = x d_y
    th = lambda t, p: np.array([p[0] + p[1] * t + t * t / 2, p[1] + t])
    dth = lambda t: np.array([[1.0, t], [0.0, 1.0]])                              # d theta_t (constant in p for this shear)
    W = lambda q: np.array([0.0, q[0]])
    def LVW(p, h=1e-6):
        f = lambda t: np.linalg.inv(dth(t)) @ W(th(t, p))                          # d(theta_{-t})_{theta_t p} W_{theta_t p}
        return (f(h) - f(-h)) / (2 * h)
    br = _bracket(sp.Matrix([y, 1]), sp.Matrix([0, x]), c2)
    err = 0.0
    for _ in range(100):
        p0 = r.normal(size=2) * 2
        err = max(err, np.abs(LVW(p0) - np.array([float(br[0].subs({x: p0[0], y: p0[1]})), float(br[1].subs({x: p0[0], y: p0[1]}))])).max())
    print("  V = y d_x + d_y, W = x d_y: [V,W] = %s; (L_V W)_p from the definition (central difference) agrees at 100 random points: max error %.1e" % (list(br), err))
    # rotation field and d_x: L_V d_x = [V, d_x] = -d_y
    Rm = lambda t: np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    f = lambda t: Rm(-t) @ np.array([1.0, 0.0])
    h = 1e-6
    print("  V = -y d_x + x d_y, W = d_x: (L_V W) = d/dt R(-t) e_1 = %s (central difference); [V, d_x] = %s" % (np.round((f(h) - f(-h)) / (2 * h), 8).tolist(), list(_bracket(sp.Matrix([-y, x]), sp.Matrix([1, 0]), c2))))
    # 2. Exercise 9.37: constant field V = v: L_V W = D_v W
    Wf = lambda q: np.array([np.sin(q[0] * q[1]), q[0] ** 2 + q[1]])
    v = np.array([0.6, -1.1])
    p0 = np.array([0.4, 0.9])
    Dv = (Wf(p0 + h * v) - Wf(p0 - h * v)) / (2 * h)
    Ws = sp.Matrix([sp.sin(x * y), x ** 2 + y])
    brv = _bracket(sp.Matrix([0.6, -1.1]), Ws, c2)
    print("  Exercise 9.37: V = (0.6, -1.1) constant: D_v W = %s, [V,W] at p = %s" % (np.round(Dv, 6).tolist(), [round(float(t.subs({x: 0.4, y: 0.9})), 6) for t in brv]))
    # 3. Cor 9.39 identities on R^3 with symbolic fields
    c3 = (x, y, z)
    A = sp.Matrix([x * y, z, x ** 2 - y]); B = sp.Matrix([sp.sin(x), y * z, 1 + x * z]); C = sp.Matrix([y, x * z, x * y * z])
    g = x ** 2 * y + sp.cos(z)
    LV = lambda Vv, Ww: _bracket(Vv, Ww, c3)
    zero = lambda M: [sp.simplify(t) for t in M]
    print("  Cor 9.39: (a) L_V W + L_W V = %s; (b) L_V[W,X] - [L_V W, X] - [W, L_V X] = %s; (c) L_[V,W] X - (L_V L_W X - L_W L_V X) = %s; (d) L_V(gW) - ((Vg) W + g L_V W) = %s"
          % (zero(LV(A, B) + LV(B, A)), zero(LV(A, LV(B, C)) - LV(LV(A, B), C) - LV(B, LV(A, C))), zero(LV(LV(A, B), C) - (LV(A, LV(B, C)) - LV(B, LV(A, C)))),
             zero(LV(A, g * B) - (_apply(A, g, c3) * B + g * LV(A, B)))))
    # 4. flows of d_x and x d_y do not commute: theta_t psi_s vs psi_s theta_t differ by s t d_y
    TH = lambda t, p: np.array([p[0] + t, p[1]])                                  # flow of V = d_x
    PS = lambda s_, p: np.array([p[0], p[1] + s_ * p[0]])                         # flow of W = x d_y
    err = 0.0
    for _ in range(100):
        p0 = r.normal(size=2)
        t_, s_ = r.uniform(-2, 2, 2)
        d = TH(t_, PS(s_, p0)) - PS(s_, TH(t_, p0))
        err = max(err, np.abs(d - np.array([0.0, -s_ * t_])).max())
    print("  V = d_x, W = x d_y: theta_t(psi_s(p)) - psi_s(theta_t(p)) = (0, -s t) at 100 random (p, s, t): max deviation %.1e; [V,W] = d_y (the flows fail to commute by -st [V,W])" % err)
    # Euler and rotation: flows commute
    Dl = lambda t, p: np.exp(t) * p
    err = 0.0
    for _ in range(100):
        p0 = r.normal(size=2); t_, s_ = r.uniform(-1.5, 1.5, 2)
        err = max(err, np.abs(Dl(t_, Rm(s_) @ p0) - Rm(s_) @ Dl(t_, p0)).max())
    print("  Euler field (dilations e^t) and rotation field (R(s)): flows commute, max error %.1e; [E,R] = %s" % (err, list(_bracket(sp.Matrix([x, y]), sp.Matrix([-y, x]), c2))))
    # 5. HW8 Q6: V = d_x, V~ = d_x + y d_y agree on the x-axis, W = d_y
    Vv, Vt, Wv = sp.Matrix([1, 0]), sp.Matrix([1, y]), sp.Matrix([0, 1])
    print("  HW8 Q6: V = d_x and V~ = d_x + y d_y agree on {y = 0}, W = d_y: L_V W = %s, L_V~ W = %s (at the origin: %s)" % (list(_bracket(Vv, Wv, c2)), list(_bracket(Vt, Wv, c2)), list(_bracket(Vt, Wv, c2).subs({x: 0, y: 0}))))
    # 6. canonical form for the commuting pair E, R: Phi(s1, s2) = (e^{s1} cos s2, e^{s1} sin s2)
    err = 0.0
    for _ in range(100):
        s1, s2 = r.uniform(-2, 2), r.uniform(-3, 3)
        P = np.array([np.exp(s1) * np.cos(s2), np.exp(s1) * np.sin(s2)])
        d1 = np.array([np.exp(s1) * np.cos(s2), np.exp(s1) * np.sin(s2)])           # d Phi / d s1
        d2 = np.array([-np.exp(s1) * np.sin(s2), np.exp(s1) * np.cos(s2)])          # d Phi / d s2
        err = max(err, np.abs(d1 - P).max(), np.abs(d2 - np.array([-P[1], P[0]])).max())
    print("  commuting E = x d_x + y d_y, R = -y d_x + x d_y are coordinate fields d/ds1, d/ds2 for Phi(s1,s2) = (e^{s1} cos s2, e^{s1} sin s2): dPhi(d_s1) = E, dPhi(d_s2) = R, error %.1e (log-polar coordinates)" % err)


# ------------------------------------------------------------------------------------------------------------------ DM14
def dm14():
    from scipy.linalg import expm, logm
    print("== DM14 One-Parameter Subgroups and the Exponential Map")
    r = np.random.default_rng(14)
    # 1. matrix exponential: series, group law, det e^A = e^{tr A}
    A = r.normal(size=(4, 4))
    S = np.zeros((4, 4)); term = np.eye(4)
    for k in range(1, 60):
        S += term
        term = term @ A / k
    print("  e^A: partial sums of the series (60 terms) vs expm: %.1e; (e^{sA} e^{tA}) vs e^{(s+t)A}: %.1e; det e^A = %.8f, e^{tr A} = %.8f" % (np.abs(S - expm(A)).max(), np.abs(expm(0.3 * A) @ expm(0.9 * A) - expm(1.2 * A)).max(), np.linalg.det(expm(A)), np.exp(np.trace(A))))
    # 2. so(2): e^{tA} = R(t), kernel 2 pi Z
    J = np.array([[0.0, -1.0], [1.0, 0.0]])
    t = 0.83
    print("  A = [[0,-1],[1,0]]: e^{tA} - R(t) = %.1e; e^{2 pi A} - I = %.1e; e^{pi A} = -I: %.1e" % (np.abs(expm(t * J) - np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])).max(), np.abs(expm(2 * np.pi * J) - np.eye(2)).max(), np.abs(expm(np.pi * J) + np.eye(2)).max()))
    # 3. so(3): Rodrigues and surjectivity of exp
    hat = lambda w: np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
    err = 0.0
    for _ in range(500):
        w = r.normal(size=3) * 2
        n = np.linalg.norm(w); K = hat(w)
        rod = np.eye(3) + np.sin(n) / n * K + (1 - np.cos(n)) / n ** 2 * K @ K
        err = max(err, np.abs(expm(K) - rod).max())
    print("  so(3): expm(hat(w)) vs the Rodrigues formula I + sin|w|/|w| W + (1-cos|w|)/|w|^2 W^2 at 500 random w: max error %.1e" % err)
    err = 0.0; skew = 0.0; cnt = 0
    for _ in range(500):
        Q, Rr = np.linalg.qr(r.normal(size=(3, 3)))
        Q = Q * np.sign(np.diag(Rr))
        if np.linalg.det(Q) < 0:
            Q[:, 0] *= -1
        L = logm(Q)
        if np.abs(L.imag).max() > 1e-8:
            continue
        L = L.real
        cnt += 1
        err = max(err, np.abs(expm(L) - Q).max()); skew = max(skew, np.abs(L + L.T).max())
    print("      %d/500 random rotations have a real logarithm: expm(log R) = R to %.1e and log R is skew to %.1e (exp: so(3) -> SO(3) is onto; Euler: every rotation is a rotation about an axis)" % (cnt, err, skew))
    # 4. su(2) formula
    sg = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    err = 0.0
    for _ in range(200):
        w = r.normal(size=3) * 3
        n = np.linalg.norm(w)
        Aw = sum(-0.5j * w[k] * sg[k] for k in range(3))
        U = np.cos(n / 2) * np.eye(2) - 1j * np.sin(n / 2) * sum(w[k] / n * sg[k] for k in range(3))
        err = max(err, np.abs(expm(Aw) - U).max(), abs(np.linalg.det(U) - 1), np.abs(U @ U.conj().T - np.eye(2)).max())
    print("  su(2): expm(sum w_k tau_k) = cos(|w|/2) I - i sin(|w|/2) (w/|w|).sigma, unitary with det 1: max error %.1e at 200 random w" % err)
    # 5. exp: sl(2,R) -> SL(2,R) is not onto: tr e^A >= -2
    a_, b_, c_ = r.normal(size=(3, 200000)) * r.uniform(0.2, 4, size=200000)
    mu2 = a_ ** 2 + b_ * c_
    tr = np.where(mu2 > 0, 2 * np.cosh(np.sqrt(np.abs(mu2))), 2 * np.cos(np.sqrt(np.abs(mu2))))
    trs = np.array([np.trace(expm(np.array([[x_, y_], [z_, -x_]]))) for x_, y_, z_ in zip(a_[:300], b_[:300], c_[:300])])
    print("  sl(2,R): closed form tr e^A = 2 cosh(mu) or 2 cos(omega) matches expm at 300 random A (max error %.1e); over 200000 random A the smallest trace is %.5f >= -2; yet diag(-2,-1/2) in SL(2,R) has trace -2.5: not in the image of exp"
          % (np.abs(trs - tr[:300]).max(), tr.min()))
    # 6. Trotter product formula (Lee Cor 20.11)
    X, Y = r.normal(size=(3, 3)), r.normal(size=(3, 3))
    out = []
    for n in (10, 100, 1000, 10000):
        P = np.linalg.matrix_power(expm(X / n) @ expm(Y / n), n)
        out.append(np.abs(P - expm(X + Y)).max())
    print("  Trotter: |(e^{X/n} e^{Y/n})^n - e^{X+Y}| for n = 10, 100, 1000, 10000: %s (decays like 1/n); e^X e^Y - e^{X+Y} = %.3f for non-commuting X, Y but %.1e for diagonal X, Y"
          % (", ".join("%.2e" % q for q in out), np.abs(expm(X) @ expm(Y) - expm(X + Y)).max(), np.abs(expm(np.diag([0.3, -1.0, 0.5])) @ expm(np.diag([1.1, 0.2, -0.4])) - expm(np.diag([1.4, -0.8, 0.1]))).max()))
    # 7. HW9 Q3: Phi(X, Y) = e^X e^Y on gl(2) = so(2) + Sym(2): dPhi at 0 is (X, Y) -> X + Y
    basis_A = [np.array([[0, -1.0], [1.0, 0]])]
    basis_B = [np.array([[1.0, 0], [0, 0]]), np.array([[0, 0], [0, 1.0]]), np.array([[0, 1.0], [1.0, 0]])]
    allb = basis_A + basis_B
    h = 1e-6
    Jm = np.zeros((4, 4))
    for j, Bj in enumerate(allb):
        if j < 1:
            f = lambda e: (expm(e * Bj) @ np.eye(2)).ravel()
        else:
            f = lambda e: (np.eye(2) @ expm(e * Bj)).ravel()
        Jm[:, j] = (f(h) - f(-h)) / (2 * h)
    print("  HW9 Q3: gl(2) = so(2) + Sym(2): Jacobian of (X,Y) -> e^X e^Y at (0,0) in the basis (J) + (E11, E22, E12+E21): rank %d, |det| = %.4f (equals the matrix of X+Y, so Phi is a local diffeomorphism)" % (np.linalg.matrix_rank(Jm, tol=1e-6), abs(np.linalg.det(Jm))))
    # 8. HW9 Q1, Q2: one-parameter subgroups of T^2 = R^2/Z^2: t -> (a t, b t) mod 1
    dist = lambda t, a, b: np.hypot(*[min(abs(((q * t) + 0.5) % 1 - 0.5), 1) for q in (a, b)])
    ts = np.linspace(0.001, 2000, 4000001)
    out = []
    for (a, b) in ((2, 3), (1, np.sqrt(2)), (0, 0)):
        d = np.hypot(np.abs((a * ts + 0.5) % 1 - 0.5), np.abs((b * ts + 0.5) % 1 - 0.5))
        out.append("(a,b) = (%g, %.4f): min over 0.001 <= t <= 2000 of the distance to the identity = %.1e" % (a, b, d.min()))
    print("  HW9 Q1 on T^2 = R^2/Z^2, gamma(t) = (a t, b t) mod 1:\n    " + "\n    ".join(out) + "\n    (a,b) = (2,3): gamma(1) = gamma(0), minimal period 1 (circle); (1, sqrt2): never exactly returns but comes arbitrarily close (injective, dense); (0,0): constant")


# ------------------------------------------------------------------------------------------------------------------ DM15
def dm15():
    print("== DM15 Closed Subgroups and the Lie Correspondence")
    r = np.random.default_rng(15)
    # 1. the dense line H = {(t, sqrt2 t)} in T^2 = R^2/Z^2 is not closed: its closure is T^2 (HW9 Q6)
    targets = r.uniform(0, 1, size=(6, 2))
    out = []
    for T in (10, 100, 1000, 10000, 1000000):
        m = np.arange(0, T + 1, dtype=float)
        worst = 0.0
        for tg in targets:
            # at t = a + m the first coordinate equals the target's exactly; the second is sqrt2 (a + m) mod 1
            y = (np.sqrt(2) * (tg[0] + m)) % 1.0
            dy = np.abs(y - tg[1]); dy = np.minimum(dy, 1 - dy)
            worst = max(worst, dy.min())
        out.append("T = %7d: %.1e" % (T, worst))
    print("  H = {(t, sqrt2 t)} in T^2: for 6 random targets (a, b) the point of the arc 0 <= t <= T whose first coordinate is a (t = a + m) comes within  %s  of the target in the second coordinate (worst target); the distance -> 0 like 1/T, so the closure of H is all of T^2: H is a Lie subgroup that is not closed, hence not embedded, and its closure is the embedded subgroup T^2" % "; ".join(out))
    # 2. a distribution that is not involutive: D = span{d_x, d_y + x d_z} on R^3
    x, y, z = sp.symbols("x y z", real=True)
    c3 = (x, y, z)
    X1, X2 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, x])
    br = _bracket(X1, X2, c3)
    M = sp.Matrix.hstack(X1, X2, br)
    print("  Frobenius: D = span{d_x, d_y + x d_z}: [X1, X2] = %s; det[X1, X2, [X1,X2]] = %s (non-zero everywhere), so [X1,X2] is not in D: D is not involutive (a contact distribution; no surface has D as its tangent plane)" % (list(br), sp.simplify(M.det())))
    Y1, Y2 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])
    print("      D' = span{d_x, d_y}: [d_x, d_y] = %s in D': involutive; integral manifolds {z = const}. Left-invariant distribution of a subalgebra on Aff(1): span{X1} = span{a d_b} has integral curves a = const (the cosets of the subgroup {(b,1)})" % list(_bracket(Y1, Y2, c3)))
    # 3. graph of a Lie algebra homomorphism is a subalgebra of g x h: phi = (su(2) -> so(3), tau_k -> E_k)
    sg = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    tau = [-0.5j * s_ for s_ in sg]
    hat = lambda w: np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
    comm = lambda P, Q: P @ Q - Q @ P
    phi = lambda a: hat(a)                                                    # coordinates a in R^3 <-> sum a_k tau_k  ->  sum a_k E_k
    su = lambda a: sum(a[k] * tau[k] for k in range(3))
    err = 0.0
    for _ in range(500):
        a, b = r.normal(size=3), r.normal(size=3)
        c = comm(su(a), su(b))                                                # [X, Y] in su(2) = su(a x b)?  coordinates of [sum a tau, sum b tau] = a x b
        err = max(err, np.abs(c - su(np.cross(a, b))).max(), np.abs(comm(phi(a), phi(b)) - phi(np.cross(a, b))).max())
    print("  graph of phi: su(2) -> so(3), sum a_k tau_k -> sum a_k E_k: [(X, phi X), (Y, phi Y)] = ([X,Y], phi[X,Y]) at 500 random pairs: max error %.1e (so the graph is a Lie subalgebra of su(2) x so(3))" % err)
    # 4. Ad: SU(2) -> SO(3) has kernel {+-I} = the centre; SU(2) is simply connected, SO(3) = SU(2)/{+-I}
    from scipy.linalg import expm
    Ad = lambda U: np.array([[0.5 * np.trace(sg[j] @ U @ sg[k] @ U.conj().T).real for k in range(3)] for j in range(3)])
    err1 = err2 = err3 = 0.0
    for _ in range(300):
        U = expm(su(r.normal(size=3) * 2)); V = expm(su(r.normal(size=3) * 2))
        err1 = max(err1, np.abs(Ad(U) - Ad(-U)).max())
        err2 = max(err2, np.abs(U @ (-np.eye(2)) - (-np.eye(2)) @ U).max())
        err3 = max(err3, np.abs(Ad(U @ V) - Ad(U) @ Ad(V)).max())
    print("  Ad: SU(2) -> SO(3): Ad(U) = Ad(-U) (error %.1e), -I central (error %.1e), Ad(UV) = Ad(U)Ad(V) (error %.1e): the kernel {+-I} is the discrete centre, SO(3) = SU(2)/{+-I}" % (err1, err2, err3))

# ------------------------------------------------------------------------------------------------------------------ driver
CHAPTERS = {"DM01": dm01, "DM02": dm02, "DM03": dm03, "DM04": dm04, "DM05": dm05, "DM06": dm06, "DM07": dm07, "DM08": dm08, "DM09": dm09, "DM10": dm10, "DM11": dm11, "DM12": dm12, "DM13": dm13, "DM14": dm14, "DM15": dm15}

if __name__ == "__main__":
    which = sys.argv[1:] or sorted(CHAPTERS)
    for k in which:
        CHAPTERS[k]()
