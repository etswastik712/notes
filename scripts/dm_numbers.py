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

# ------------------------------------------------------------------------------------------------------------------ driver
CHAPTERS = {"DM01": dm01, "DM02": dm02, "DM03": dm03, "DM04": dm04, "DM05": dm05, "DM06": dm06, "DM07": dm07, "DM08": dm08, "DM09": dm09}

if __name__ == "__main__":
    which = sys.argv[1:] or sorted(CHAPTERS)
    for k in which:
        CHAPTERS[k]()
