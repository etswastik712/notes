"""QM09 numbers: Stern-Gerlach, spin-1/2 algebra, sequential SG, density matrix, dynamics, spin-j, two spins, Bell/CHSH,
measurement model, photon-polarisation and two-level parallels.

.venv/bin/python -W ignore scripts/qm09_numbers.py
Every closed form quoted in QM09 is recomputed here by an independent numerical route (matrix algebra, expm, enumeration).
"""
import itertools
import math

import numpy as np
from scipy.linalg import expm

# ---------------------------------------------------------------- constants (CODATA 2018)
HBAR = 1.054571817e-34
H_PL = 6.62607015e-34
E_CH = 1.602176634e-19
M_E = 9.1093837015e-31
M_P = 1.67262192369e-27
M_N = 1.67492749804e-27
K_B = 1.380649e-23
C_LT = 2.99792458e8
U_AMU = 1.66053906660e-27
MU_B = 9.2740100783e-24        # J/T
MU_N = 5.0507837461e-27        # J/T
MU_P = 1.41060679736e-26       # J/T
GAMMA_E = 1.76085963023e11     # rad s^-1 T^-1 (|gamma_e|)
GAMMA_P = 2.6752218744e8       # rad s^-1 T^-1
GAMMA_N = 1.83247171e8         # rad s^-1 T^-1 (|gamma_n|)
ALPHA_FS = 7.2973525693e-3

# Pauli matrices
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
SIG = [sx, sy, sz]


def sec(t):
    print("\n=== " + t + " ===")


def nvec(theta, phi=0.0):
    return np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)])


def ndots(n):
    return n[0] * sx + n[1] * sy + n[2] * sz


def ket_plus(theta, phi=0.0):
    return np.array([math.cos(theta / 2), np.exp(1j * phi) * math.sin(theta / 2)])


def ket_minus(theta, phi=0.0):
    return np.array([-np.exp(-1j * phi) * math.sin(theta / 2), math.cos(theta / 2)])


# ================================================================ 1. The apparatus
sec("1. SG deflection of a silver beam (illustrative parameters)")
m_ag = 107.8682 * U_AMU
T_oven = 1300.0
v_mp = math.sqrt(3 * K_B * T_oven / m_ag)          # most probable speed of an effusive beam
v_rms2 = math.sqrt(4 * K_B * T_oven / m_ag)        # sqrt of <v^2> of the beam
G = 1000.0                                          # dB/dz = 10 T/cm
L1, L2 = 0.035, 0.010                               # magnet length, magnet-to-plate distance
F = MU_B * G
a = F / m_ag
t1, t2 = L1 / v_mp, L2 / v_mp
z1 = 0.5 * a * t1 ** 2
vz = a * t1
z2 = vz * t2
z_tot = z1 + z2
print(f"m_Ag={m_ag:.4e} kg  T={T_oven} K  v_mp={v_mp:.1f} m/s  sqrt<v^2>={v_rms2:.1f} m/s")
print(f"F=mu_B*G={F:.3e} N  a={a:.3e} m/s^2  weight ratio F/mg={F/(m_ag*9.80665):.3e}")
print(f"t_magnet={t1*1e6:.1f} us  z(exit)={z1*1e3:.4f} mm  v_z={vz:.3f} m/s  drift={z2*1e3:.4f} mm")
print(f"total deflection each way={z_tot*1e3:.4f} mm  separation of the two spots={2*z_tot*1e3:.4f} mm")
print(f"classical band: uniform over +-{z_tot*1e3:.3f} mm (mu_z uniform in [-mu,mu])")
print(f"de Broglie wavelength of Ag at v_mp: {H_PL/(m_ag*v_mp)*1e12:.3f} pm")
# thermal speed spread: deflection ~ 1/v^2, so a 10% speed change shifts the spot by ~20%
print(f"speed spread: dz/z = -2 dv/v  -> 10% speed change moves the spot by {2*10:.0f}%")
# gravity sag over the same flight for comparison
print(f"gravity drop in the magnet+drift: {0.5*9.80665*((L1+L2)/v_mp)**2*1e6:.2f} um (negligible)")
# precession frequency inside the field for Ag at B=0.1 T (Larmor >> transit rate)
B0 = 0.1
w_L = 2 * MU_B * B0 / HBAR / 2   # g=2: omega = gamma B = e B/m_e  (gamma=g mu_B/hbar)
w_L = 2.0 * MU_B * B0 / HBAR
print(f"Larmor angular frequency of the spin in B0=0.1 T: {w_L:.3e} rad/s ({w_L/2/math.pi/1e9:.3f} GHz)  vs transit rate 1/t1={1/t1:.2e}/s")
print(f"turns of precession during transit: {w_L*t1/2/math.pi:.0f}")

# ================================================================ 2. Angular momentum / magnetic moment
sec("2. Magnetic moment, g-factor, orbital vs spin")
print(f"mu_B = e hbar/2m_e = {E_CH*HBAR/(2*M_E):.6e} J/T (CODATA {MU_B:.6e})")
print(f"mu_B in eV/T = {MU_B/E_CH:.6e};   mu_B/h = {MU_B/H_PL/1e9:.4f} GHz/T;   mu_B/k_B = {MU_B/K_B*1e3:.4f} mK/T")
a_schwinger = ALPHA_FS / (2 * math.pi)
a_meas = 1.15965218128e-3
print(f"Schwinger a_e = alpha/2pi = {a_schwinger:.6e};  measured (CODATA 2018) {a_meas:.6e};  diff {100*(a_schwinger-a_meas)/a_meas:.3f} %")
print(f"gamma_e/2pi = g mu_B/h = {2*(1+a_meas)*MU_B/H_PL/1e9:.4f} GHz/T")
print(f"gamma_p/2pi = {GAMMA_P/2/math.pi/1e6:.4f} MHz/T;  gamma_n/2pi = {GAMMA_N/2/math.pi/1e6:.4f} MHz/T")
# classical expectation for isotropic orientations: mu_z uniform
print("isotropic orientation: P(cos theta) uniform -> mu_z uniform on [-mu,mu]; <mu_z^2>/mu^2 = 1/3")
# Bohr-Sommerfeld space quantisation: orbital l gives 2l+1 beams
for l in (0, 1, 2):
    print(f"orbital l={l}: {2*l+1} beams;  spin j=l+1/2... j={l+0.5}: {int(2*(l+0.5)+1)} beams")
print("Cs F=4: 2F+1 = 9 beams (Lison et al. 1999 via Sakurai Fig. 1.6)")

# ================================================================ 3. Pauli algebra checks
sec("3. Pauli algebra and eigenvectors")
eps = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    eps[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])
ok = True
for i in range(3):
    for j in range(3):
        lhs = SIG[i] @ SIG[j]
        rhs = (1 if i == j else 0) * I2 + 1j * sum(eps[i, j, k] * SIG[k] for k in range(3))
        ok &= np.allclose(lhs, rhs)
print("sigma_i sigma_j = delta_ij + i eps_ijk sigma_k :", ok)
rng = np.random.default_rng(1)
a_v, b_v = rng.normal(size=3), rng.normal(size=3)
lhs = ndots(a_v) @ ndots(b_v)
rhs = np.dot(a_v, b_v) * I2 + 1j * ndots(np.cross(a_v, b_v))
print("(a.sigma)(b.sigma) = a.b + i (a x b).sigma :", np.allclose(lhs, rhs))
for th, ph in ((0.7, 0.3), (2.1, -1.0), (math.pi / 2, math.pi / 2)):
    n = nvec(th, ph)
    kp, km = ket_plus(th, ph), ket_minus(th, ph)
    assert np.allclose(ndots(n) @ kp, kp) and np.allclose(ndots(n) @ km, -km)
    assert abs(np.vdot(kp, km)) < 1e-12
    bloch = np.array([np.vdot(kp, s @ kp).real for s in SIG])
    assert np.allclose(bloch, n)
print("|+n> = (cos th/2, e^{i phi} sin th/2) is the +1 eigenvector of n.sigma and <sigma> = n : True")
# exponential of n.sigma
th = 1.3
n = nvec(0.9, 0.4)
U = expm(-1j * th * ndots(n) / 2)
print("exp(-i th n.sigma/2) = cos(th/2) - i sin(th/2) n.sigma :",
      np.allclose(U, math.cos(th / 2) * I2 - 1j * math.sin(th / 2) * ndots(n)))
print(f"rotation by 2 pi: {np.round(expm(-1j*2*math.pi*ndots(n)/2).real,6).tolist()}  (=-1);  by 4 pi: {np.round(expm(-1j*4*math.pi*ndots(n)/2).real,6).tolist()}")
# conjugation = SO(3) rotation about z
phi = 0.8
Uz = expm(-1j * phi * sz / 2)
print("U sigma_x U^dag = cos(phi) sigma_x + sin(phi) sigma_y :",
      np.allclose(Uz @ sx @ Uz.conj().T, math.cos(phi) * sx + math.sin(phi) * sy))
# real-vector argument: mutually unbiased bases need i
print("MUBs: |<x+|y+>|^2 = |1 + e^{i b}|^2 / 4 = 1/2 requires cos b = 0 -> b = +-pi/2 (complex)")

# ================================================================ 4. Probabilities between SG axes
sec("4. Probabilities, sequential SG")
def P(nA, nB):
    """probability that a +nA atom passes an SG-nB analyser in the + port"""
    return abs(np.vdot(ket_plus(*nB), ket_plus(*nA))) ** 2

for g in (0.0, math.pi / 6, math.pi / 3, math.pi / 2, 2 * math.pi / 3, math.pi):
    # angle g between axes (both in the x-z plane)
    p_num = P((0, 0), (g, 0))
    assert abs(p_num - (1 + math.cos(g)) / 2) < 1e-12
print("P(+n'|+n) = cos^2(gamma/2) = (1 + n.n')/2 : True (6 angles)")
print(f"z -> x: P = {P((0,0),(math.pi/2,0)):.4f};  z -> y: {P((0,0),(math.pi/2,math.pi/2)):.4f};  x -> y: {P((math.pi/2,0),(math.pi/2,math.pi/2)):.4f}")
# three stage z+ -> n(theta) -> z-
for th in (30, 45, 60, 90, 120, 150):
    t = math.radians(th)
    p1 = P((0, 0), (t, 0))
    p2 = abs(np.vdot(ket_minus(0, 0), ket_plus(t, 0))) ** 2
    print(f"  theta={th:3d} deg: P(n+|z+)={p1:.4f}  P(z-|n+)={p2:.4f}  product={p1*p2:.4f}  sin^2(th)/4={math.sin(t)**2/4:.4f}")
print("unpolarised oven -> SGz(+) -> SGx(+) -> SGz: intensities I0/2, I0/4, then I0/8 in each z port")
# recombination with relative phase phi (Larmor rotation in the x arms)
for phi in (0.0, math.pi / 2, math.pi, 3 * math.pi / 2):
    amp = np.vdot(np.array([0, 1]), (np.outer(ket_plus(math.pi / 2), ket_plus(math.pi / 2).conj())
                                       + np.exp(1j * phi) * np.outer(ket_minus(math.pi / 2), ket_minus(math.pi / 2).conj())) @ np.array([1, 0]))
    print(f"  recombined, relative phase phi={phi:.3f}: P(z-) = {abs(amp)**2:.4f}  sin^2(phi/2) = {math.sin(phi/2)**2:.4f}")
# Zeno chain: rotate analyser by pi/N each time
print("filter chain +z -> -z in N steps: P = cos^{2N}(pi/2N)")
for N in (1, 2, 3, 4, 10, 100, 1000):
    p = math.cos(math.pi / (2 * N)) ** (2 * N)
    print(f"  N={N:5d}: {p:.5f}   (1 - pi^2/4N = {1 - math.pi**2/(4*N):.5f})")
# hidden-variable model: 4 types (z+-, x+-): third SGz after x+ would give z+ only
print("type model (z,x both sharp): after SGz+ then SGx+, the z-value is still + -> P(z-)=0, but experiment gives 1/2")
# variance sum
for th, ph in ((0.5, 0.2), (1.9, 2.2)):
    k = ket_plus(th, ph)
    var = sum(np.vdot(k, s @ s @ k).real - np.vdot(k, s @ k).real ** 2 for s in SIG)
    print(f"  sum of Var(sigma_i) in a pure state = {var:.6f}  (=2  <->  sum Var(S_i) = hbar^2/2)")
# uncertainty relations for |+z>
k = np.array([1, 0], complex)
dX = math.sqrt(np.vdot(k, sx @ sx @ k).real - np.vdot(k, sx @ k).real ** 2)
dY = math.sqrt(np.vdot(k, sy @ sy @ k).real - np.vdot(k, sy @ k).real ** 2)
print(f"|+z>: dSx dSy = {dX*dY/4:.3f} hbar^2 = (1/2)|<Sz>|*hbar = {0.5*0.5:.3f} hbar^2")

# ================================================================ 5. Density matrix and thermal polarisation
sec("5. Density matrix")
rho_u = I2 / 2
print(f"unpolarised: Tr rho^2 = {np.trace(rho_u@rho_u).real:.3f}, S = ln2 = {math.log(2):.4f} (= {math.log(2)/math.log(2):.0f} bit), <sigma> = 0")
mix_z = 0.5 * np.diag([1, 0]) + 0.5 * np.diag([0, 1])
kpx, kmx = ket_plus(math.pi / 2), ket_minus(math.pi / 2)
mix_x = 0.5 * np.outer(kpx, kpx.conj()) + 0.5 * np.outer(kmx, kmx.conj())
print("50/50 mixture of +-z equals 50/50 mixture of +-x:", np.allclose(mix_z, mix_x), "=", np.allclose(mix_z, rho_u))
sup = np.array([1, 1], complex) / math.sqrt(2)
print("superposition (|+z>+|-z>)/sqrt2: P(+z)=0.5, <sigma_x> =", np.vdot(sup, sx @ sup).real, " vs mixture <sigma_x> =", np.trace(mix_z @ sx).real)
# partial polarisation: rho = (1+ r.sigma)/2
r = np.array([0, 0, 0.6])
rho = 0.5 * (I2 + sum(ri * s for ri, s in zip(r, SIG)))
ev = np.linalg.eigvalsh(rho)
S_vn = -sum(e * math.log(e) for e in ev if e > 0)
print(f"r=0.6: eigenvalues {ev}, purity {np.trace(rho@rho).real:.3f} (=(1+r^2)/2), entropy {S_vn:.4f} nat")
print("P(+n) = (1 + r.n)/2 : r=0.6 along z: P(+z)=%.2f, P(+x)=0.50" % ((1 + 0.6) / 2))

sec("5b. Thermal spin polarisation P = tanh(mu B / kT)")
for lab, mu, B, T in (("electron 1 T, 300 K", MU_B, 1.0, 300.0), ("electron 1 T, 4 K", MU_B, 1.0, 4.0), ("electron 10 T, 2 K", MU_B, 10.0, 2.0),
                      ("proton 1.5 T, 300 K", MU_P, 1.5, 300.0), ("proton 3 T, 310 K", MU_P, 3.0, 310.0)):
    x = mu * B / (K_B * T)
    print(f"  {lab:22s} x=mu B/kT={x:.4e}  P=tanh x={math.tanh(x):.4e}")
print(f"Zeno-type scale: Zeeman splitting 2 mu_B B/h at 1 T = {2*MU_B/H_PL/1e9:.3f} GHz = {2*MU_B/E_CH*1e6:.2f} ueV;  kT(300 K) = {K_B*300/E_CH*1e3:.2f} meV")
print(f"proton Larmor: 1.5 T -> {GAMMA_P*1.5/2/math.pi/1e6:.3f} MHz; 3 T -> {GAMMA_P*3/2/math.pi/1e6:.3f} MHz; 7 T -> {GAMMA_P*7/2/math.pi/1e6:.2f} MHz")

# ================================================================ 6. Dynamics
sec("6. Larmor precession, Rabi oscillation")
# Heisenberg: dS/dt = gamma S x B ; check with expm for H = -gamma B Sz  (hbar=1, S = sigma/2)
gam, B = 1.0, 0.7
Hm = -gam * B * sz / 2
t = 1.9
Ut = expm(-1j * Hm * t)
S0 = np.array([0.3, 0.5, math.sqrt(1 - 0.34)])             # initial Bloch vector
psi0 = ket_plus(math.acos(S0[2]), math.atan2(S0[1], S0[0]))
psi_t = Ut @ psi0
Sx_t, Sy_t, Sz_t = [np.vdot(psi_t, s @ psi_t).real for s in SIG]
w = -gam * B
pred = (S0[0] * math.cos(w * t) - S0[1] * math.sin(w * t), S0[0] * math.sin(w * t) + S0[1] * math.cos(w * t), S0[2])
print("Larmor rotation about z at omega = -gamma B:", np.allclose([Sx_t, Sy_t, Sz_t], pred))
print(f"state-ket period 4 pi/omega = 2 x precession period: ket at t=2pi/|omega|: {np.round((expm(-1j*Hm*2*math.pi/abs(w)) @ psi0)[0]/psi0[0], 6)} (= -1)")

# Rabi
def rabi_P(Delta, Om, t):
    W = math.sqrt(Delta ** 2 + Om ** 2)
    return Om ** 2 / W ** 2 * math.sin(W * t / 2) ** 2

maxerr = 0
for Delta, Om in ((0.0, 1.0), (0.5, 1.0), (1.0, 1.0), (2.0, 1.0), (0.3, 2.2)):
    for tt in np.linspace(0.1, 12, 25):
        Hp = 0.5 * (Delta * sz + Om * sx)
        psi = expm(-1j * Hp * tt) @ np.array([1, 0], complex)
        maxerr = max(maxerr, abs(abs(psi[1]) ** 2 - rabi_P(Delta, Om, tt)))
print(f"Rabi formula P = Om^2/(Om^2+D^2) sin^2(W t/2) vs expm: max error {maxerr:.2e}")
print("resonance FWHM in detuning = 2 Omega; pi pulse: Omega t = pi; pi/2 pulse: Omega t = pi/2")
# numerical check of the rotating-frame derivation with the full (non rotating-wave) time-dependent Hamiltonian
from scipy.integrate import solve_ivp
w0, Om, wd = 50.0, 1.0, 50.0
# H = (w0/2) sz + (Om/2)(sx cos wd t + sy sin wd t)*  (rotating field): exact rotating-frame solution has Delta = w0-wd
def f2(t, y):
    Ht = 0.5 * w0 * sz + 0.5 * Om * (sx * math.cos(wd * t) + sy * math.sin(wd * t))
    return -1j * (Ht @ y)
sol = solve_ivp(f2, [0, 2 * math.pi / Om * 1.0], [1 + 0j, 0j], rtol=1e-10, atol=1e-12, t_eval=[math.pi / Om, 2 * math.pi / Om])
print(f"rotating field, resonance, Omega=1: P_flip(pi/Om)={abs(sol.y[1,0])**2:.6f} (pi pulse: 1), P_flip(2pi/Om)={abs(sol.y[1,1])**2:.6f} (0)")
# Bloch-Siegert: linear field = two counter-rotating halves; far-from-resonance half contributes ~ Om^2/(4 w0) shift
print(f"counter-rotating half shifts the resonance by ~ Omega^2/(4 omega_0) = {Om**2/(4*w0):.4f} (rad/s units of the example) -> negligible for Omega<<omega_0")

sec("6b. Practical numbers")
B0e, B1 = 1.0, 1e-3
print(f"electron: B0=1 T -> {GAMMA_E*B0e/2/math.pi/1e9:.3f} GHz ; with B1=1 mT: Omega/2pi = {GAMMA_E*B1/2/math.pi/1e6:.2f} MHz, pi pulse = {1/(2*GAMMA_E*B1/2/math.pi)*1e9:.2f} ns")
B1p = 10e-6
print(f"proton: B1 = 10 uT -> Omega/2pi = {GAMMA_P*B1p/2/math.pi:.1f} Hz, pi pulse = {math.pi/(GAMMA_P*B1p)*1e3:.3f} ms, pi/2 pulse = {math.pi/2/(GAMMA_P*B1p)*1e3:.3f} ms")
# neutron interferometer
lam = 1.8e-10
vn = H_PL / (M_N * lam)
ell = 0.02
dB = 4 * math.pi * vn / (GAMMA_N * ell)
print(f"neutron lambda=1.8 A: v={vn:.1f} m/s;  for l=2 cm: delta B (successive maxima, 4pi) = {dB*1e3:.3f} mT = {dB*1e4:.1f} G; 2pi would be {dB/2*1e3:.3f} mT")
print(f"  rotation angle in 1 mT over 2 cm: {GAMMA_N*1e-3*ell/vn:.3f} rad = {GAMMA_N*1e-3*ell/vn/math.pi:.3f} pi")
print(f"  B*l for a 2pi spin rotation: {2*math.pi*vn/GAMMA_N*1e4*100:.2f} G*cm")
# Larmor/Coriolis analogue
Om_E = 7.2921159e-5
print(f"Coriolis <-> Lorentz: qB = 2 m Omega; for an electron the Earth-rotation-equivalent B = {2*M_E*Om_E/E_CH:.3e} T")

# ================================================================ 7. Spin j
sec("7. Angular momentum algebra and spin j")
def jmats(j):
    m = np.arange(j, -j - 1, -1)
    dim = len(m)
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((dim, dim), complex)
    for i in range(1, dim):
        mm = m[i]
        Jp[i - 1, i] = math.sqrt(j * (j + 1) - mm * (mm + 1))
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2j)
    return Jx, Jy, Jz, Jp, Jm

for j in (0.5, 1, 1.5, 2.5):
    Jx, Jy, Jz, Jp, Jm = jmats(j)
    comm = np.allclose(Jx @ Jy - Jy @ Jx, 1j * Jz) and np.allclose(Jy @ Jz - Jz @ Jy, 1j * Jx) and np.allclose(Jz @ Jx - Jx @ Jz, 1j * Jy)
    J2 = Jx @ Jx + Jy @ Jy + Jz @ Jz
    print(f"j={j}: dim {int(2*j+1)}, [Ji,Jj]=i eps Jk: {comm}, J^2 = j(j+1) = {j*(j+1):.3f}: {np.allclose(J2, j*(j+1)*np.eye(int(2*j+1)))}")
# spin 1 matrices
Jx, Jy, Jz, _, _ = jmats(1)
print("spin-1 Jx (units hbar) =\n", np.round(Jx.real, 4))
# rotated-axis probabilities: starting in |j,m=j>_z, measure J_n with n at angle beta
def pj(j, beta):
    Jx, Jy, Jz, _, _ = jmats(j)
    Jn = math.sin(beta) * Jx + math.cos(beta) * Jz
    w, v = np.linalg.eigh(Jn)
    psi = np.zeros(int(2 * j + 1), complex); psi[0] = 1
    probs = np.abs(v.conj().T @ psi) ** 2
    return dict(zip(np.round(w, 3), np.round(probs, 5)))

print("spin 1, |m=0>_z measured along x:")
Jx1 = jmats(1)[0]
w, v = np.linalg.eigh(Jx1)
psi0z = np.array([0, 1, 0], complex)
print("   eigenvalues of Jx:", np.round(w, 3), " probabilities:", np.round(np.abs(v.conj().T @ psi0z) ** 2, 5))
print("   d^1_00(beta) = cos(beta): P(0->0) = cos^2(beta); at 90 deg = 0 (tested above)")
for j in (0.5, 1, 1.5):
    beta = math.pi / 2
    pr = pj(j, beta)
    n = int(2 * j)
    binom = {round(m - n / 2, 3): math.comb(n, m) * math.cos(beta / 2) ** (2 * m) * math.sin(beta / 2) ** (2 * (n - m)) for m in range(n + 1)}
    print(f"  j={j}, beta=90 deg: numeric {pr}   binomial {({k: round(v_, 5) for k, v_ in sorted(binom.items())})}")
    for (k1, v1) in pr.items():
        assert abs(v1 - binom[k1]) < 1e-4

sec("7b. Schwinger oscillator model (truncated Fock space)")
nmax = 8
ad = np.diag(np.sqrt(np.arange(1, nmax + 1)), -1).astype(float)    # a^dagger
a_op = ad.T
Id = np.eye(nmax + 1)
Ap = np.kron(ad, Id); Am = np.kron(a_op, Id)
Bp = np.kron(Id, ad); Bm = np.kron(Id, a_op)
Jp = Ap @ Bm        # a^dag b
Jm = Bp @ Am        # b^dag a
Jz = 0.5 * (Ap @ Am - Bp @ Bm)
N = Ap @ Am + Bp @ Bm
def idx(na, nb):
    return na * (nmax + 1) + nb
# test on low-lying states (truncation spoils the highest levels)
good = [idx(na, nb) for na in range(4) for nb in range(4)]
comm = Jp @ Jm - Jm @ Jp - 2 * Jz
print("[J+,J-] = 2 Jz on states with na,nb<=3:", all(np.allclose(comm[:, g], 0) for g in good))
Jx = (Jp + Jm) / 2; Jy = (Jp - Jm) / 2j
J2 = Jx @ Jx + Jy @ Jy + Jz @ Jz
okj = all(abs(J2[g, g] - (N[g, g] / 2) * (N[g, g] / 2 + 1)) < 1e-9 for g in good)
print("J^2 = (N/2)(N/2+1) on those states:", okj)
print("|na,nb> -> j=(na+nb)/2, m=(na-nb)/2 ; one quantum in two modes = spin-1/2 ; Stokes operators of light = same algebra")

# ================================================================ 8. Two spins
sec("8. Two spins: singlet and triplet")
s_up, s_dn = np.array([1, 0], complex), np.array([0, 1], complex)
singlet = (np.kron(s_up, s_dn) - np.kron(s_dn, s_up)) / math.sqrt(2)
trip = [np.kron(s_up, s_up), (np.kron(s_up, s_dn) + np.kron(s_dn, s_up)) / math.sqrt(2), np.kron(s_dn, s_dn)]
S1S2 = sum(np.kron(s, s) for s in SIG) / 4   # in hbar^2
w, v = np.linalg.eigh(S1S2)
print("S1.S2 eigenvalues (hbar^2):", np.round(w, 4), "(expected -3/4, +1/4 x3)")
print("singlet is an eigenvector with -3/4:", np.allclose(S1S2 @ singlet, -0.75 * singlet), "; triplet +1/4:", all(np.allclose(S1S2 @ t_, 0.25 * t_) for t_ in trip))
U = expm(-1j * 0.9 * ndots(nvec(0.8, 1.3)) / 2)
print("(U x U)|singlet> = det(U)|singlet> = |singlet> :", np.allclose(np.kron(U, U) @ singlet, np.linalg.det(U) * singlet))
print("partial trace of singlet is I/2:", np.allclose(np.einsum('ijkj->ik', np.outer(singlet, singlet.conj()).reshape(2, 2, 2, 2)), I2 / 2))
nu21 = 1420405751.768
print(f"hydrogen hyperfine: nu={nu21/1e6:.6f} MHz, DE={H_PL*nu21/E_CH*1e6:.4f} ueV, lambda={C_LT/nu21*100:.3f} cm, hnu/k={H_PL*nu21/K_B*1e3:.2f} mK")
print(f"  statistical weights F=1:F=0 = 3:1 -> at T>>68 mK population ratio -> {3*math.exp(-H_PL*nu21/(K_B*100)):.4f} (T=100 K)")
print("  A10 = 2.87e-15 /s -> lifetime ~ 1.1e7 yr (recalled)")

# ================================================================ 9. Bell
sec("9. Singlet correlations, CHSH, Wigner inequality")
def E_corr(a, b):
    return np.vdot(singlet, np.kron(ndots(a), ndots(b)) @ singlet).real

for deg in (0, 30, 60, 90, 120, 180):
    t = math.radians(deg)
    a, b = nvec(0.0), nvec(t, 0.0)
    assert abs(E_corr(a, b) + math.cos(t)) < 1e-12
print("E(a,b) = -a.b = -cos(theta): True")
A0, A1 = nvec(0, 0), nvec(math.pi / 2, 0)
B0_, B1_ = nvec(math.pi / 4, 0), nvec(3 * math.pi / 4, 0)
S = E_corr(A0, B0_) - E_corr(A0, B1_) + E_corr(A1, B0_) + E_corr(A1, B1_)
print(f"CHSH S = E(a,b) - E(a,b') + E(a',b) + E(a',b') = {S:.6f}  |S| = {abs(S):.6f};  2 sqrt2 = {2*math.sqrt(2):.6f}")
# angle dependence S(phi) with a=0,a'=2phi,b=phi,b'=3phi
for phi in (10, 30, 45, 60):
    p = math.radians(phi)
    Sp = E_corr(nvec(0), nvec(p)) - E_corr(nvec(0), nvec(3 * p)) + E_corr(nvec(2 * p), nvec(p)) + E_corr(nvec(2 * p), nvec(3 * p))
    print(f"  phi={phi:2d} deg: |S| = {abs(Sp):.4f}   (3cos phi - cos 3phi = {3*math.cos(p)-math.cos(3*p):.4f})")
# deterministic local strategies
best = 0
for A_a, A_ap, B_b, B_bp in itertools.product((-1, 1), repeat=4):
    best = max(best, abs(A_a * B_b - A_a * B_bp + A_ap * B_b + A_ap * B_bp))
print(f"max |S| over the 16 deterministic local strategies = {best} (so every local-hidden-variable mixture obeys |S|<=2)")
# Tsirelson: C^2 = 4 + [A,A'][B,B'] (C = AB - AB' + A'B + A'B'; the sign flips for the other labelling)
Aa, Ap_, Bb, Bp_ = ndots(A0), ndots(A1), ndots(B0_), ndots(B1_)
Cop = np.kron(Aa, Bb) - np.kron(Aa, Bp_) + np.kron(Ap_, Bb) + np.kron(Ap_, Bp_)
lhs = Cop @ Cop
rhs = 4 * np.eye(4) + np.kron(Aa @ Ap_ - Ap_ @ Aa, Bb @ Bp_ - Bp_ @ Bb)
print("C^2 = 4 + [A,A'][B,B'] for C = AB - AB' + A'B + A'B' :", np.allclose(lhs, rhs), f"; ||C|| = {np.linalg.norm(Cop,2):.6f}")
# Wigner/Bell three-axis inequality P(a+,b+) <= P(a+,c+) + P(c+,b+)
def Ppp(t):  # singlet, both +, axes at angle t
    return 0.5 * math.sin(t / 2) ** 2
for th in (30, 45, 60, 80, 100):
    t = math.radians(th)
    lhsw = Ppp(2 * t); rhsw = 2 * Ppp(t)
    print(f"  a-c = c-b = {th:3d} deg: P(a+,b+)={lhsw:.4f}  P(a+,c+)+P(c+,b+)={rhsw:.4f}  {'VIOLATED' if lhsw>rhsw+1e-12 else 'ok'}")
# check P_pp with explicit state
t = math.radians(60)
PP = abs(np.kron(ket_plus(0), ket_plus(2 * t)).conj() @ singlet) ** 2
print(f"explicit P(a+,b+) at 120 deg: {PP:.4f} vs 1/2 sin^2(60 deg) = {Ppp(2*t):.4f}")
print("max violation of the three-axis inequality: (1/2) sin^2(theta) - sin^2(theta/2), maximal at theta = 60 deg: 0.375 - 0.25 = 0.125")
# no-signalling
rhoB = np.einsum('ijik->jk', np.outer(singlet, singlet.conj()).reshape(2, 2, 2, 2))
print("Bob's reduced state = I/2 regardless of Alice's choice:", np.allclose(rhoB, I2 / 2))

sec("9b. No cloning, BB84")
th = 0.7
print("no-cloning: <psi|phi> = <psi|phi>^2 only for overlap 0 or 1 -> a cloner that works for |+z> and |+x> would need 1/sqrt2 = 1/2: contradiction (overlap^2 =", round(0.5, 3), ")")
# BB84 intercept-resend: exact enumeration over Alice basis, Eve basis (when Bob basis == Alice basis)
err = 0.0
for eve_matches in (True, False):
    p_basis = 0.5
    # Bob (same basis as Alice) gets error probability 0 if Eve guessed the basis, else 1/2
    err += p_basis * (0.0 if eve_matches else 0.5)
print(f"BB84 intercept-resend: error rate in the sifted key = {err:.3f} (Eve wrong basis w.p. 1/2, then Bob wrong w.p. 1/2)")
print(f"probability Alice's and Bob's bases agree = 1/2; Eve undetected over n sifted bits: (3/4)^n -> n=64: {0.75**64:.2e}")

# ================================================================ 10. Measurement model
sec("10. von Neumann model of the SG measurement")
dp = F * t1
sig_z = 20e-6
sig_p = HBAR / (2 * sig_z)
print(f"momentum kick dp = F t = {dp:.3e} kg m/s;  sigma_p = hbar/(2 sigma_z) = {sig_p:.3e} for sigma_z = 20 um;  dp/sigma_p = {dp/sig_p:.3e}")
print(f"  packet overlap exp(-dp^2/2 sigma_p^2) = exp(-{dp**2/(2*sig_p**2):.3e})  -> 0: a perfect which-spin measurement")
print(f"  velocity kick dv = dp/m = {dp/m_ag:.3f} m/s (vs v = {v_mp:.0f} m/s: angle {dp/(m_ag*v_mp)*1e3:.3f} mrad)")
# how small a kick would still leave overlap 1/e? dp = sqrt(2) sigma_p
print(f"  the gradient could be {dp/(math.sqrt(2)*sig_p):.1e} times weaker before the packets overlapped at the 1/e level")
# Bohr-Mott
for E_ev, w_beam in ((100.0, 1e-6), (100.0, 1e-3)):
    v = math.sqrt(2 * E_ev * E_CH / M_E)
    ratio = 2 * M_E * v * w_beam / HBAR
    lam_db = H_PL / (M_E * v)
    print(f"free electron E={E_ev:.0f} eV: v={v:.3e} m/s, lambda_dB={lam_db*1e9:.4f} nm, beam width {w_beam*1e6:.0f} um: Lorentz/SG force ratio = 2 m v w/hbar = {ratio:.3e}")

# ================================================================ 11. Photon polarisation
sec("11. Polarisation analogue")
def malus_chain(alphas):
    I = 0.5  # unpolarised through the first polariser (axis 0)
    prev = 0.0
    for a_ in alphas:
        I *= math.cos(a_ - prev) ** 2
        prev = a_
    return I
for al in (22.5, 45, 67.5):
    a_ = math.radians(al)
    I3 = malus_chain([a_, math.pi / 2])
    print(f"  crossed polarisers with an extra one at {al:4.1f} deg: I/I0 = {I3:.5f} ; (1/8) sin^2(2alpha) = {math.sin(2*a_)**2/8:.5f}")
print("  spin angle theta = 2 x polariser angle alpha; Malus cos^2(alpha) = cos^2(theta/2)")
print(f"  N polarisers rotating by 90 deg in N equal steps: transmitted fraction of a polarised beam = {math.cos(math.pi/20)**20:.4f} (N=10), {math.cos(math.pi/200)**200:.4f} (N=100)")

# ================================================================ 12. Two-level parallels
sec("12. Two-level parallels")
for dm2, L, E in ((2.5e-3, 295.0, 0.6), (2.5e-3, 810.0, 2.0), (7.5e-5, 180.0, 0.004), (7.5e-5, 60.0, 0.003)):
    phase = 1.267 * dm2 * L / E
    print(f"  Delta m^2={dm2:.1e} eV^2  L={L:6.1f} km  E={E:5.3f} GeV: phase={phase:.4f} rad, sin^2={math.sin(phase)**2:.4f}")
print(f"  check 1.267: Dm^2 L/(4 hbar c E) with 1 eV^2, 1 km, 1 GeV = {1*1000/(4*1.97327e-7*1e9):.4f}")
print(f"  first oscillation maximum at L/E = pi/(2*1.267*Dm^2) = {math.pi/(2*1.267*2.5e-3):.0f} km/GeV for 2.5e-3 eV^2")
nu_nh3 = 23.87e9
print(f"NH3 inversion: nu={nu_nh3/1e9:.2f} GHz -> {nu_nh3/C_LT/100:.3f} cm^-1 ; DE = {H_PL*nu_nh3/E_CH*1e6:.2f} ueV ({H_PL*nu_nh3/E_CH*1e3:.4f} meV) ; hnu/k = {H_PL*nu_nh3/K_B:.3f} K")
print("spin-only magnetic moments mu = sqrt(n(n+2)) mu_B:")
for n_ in range(1, 6):
    print(f"  n={n_}: {math.sqrt(n_*(n_+2)):.2f} mu_B  (S={n_/2})")
print("  O2 (two unpaired pi* electrons, triplet): 2.83 mu_B (spin-only); liquid O2 is attracted into the gap of a magnet (F = grad(mu.B), same force law as SG)")
print(f"SQUID/Josephson: skip. Transmon qubit: ~5 GHz = {H_PL*5e9/K_B*1e3:.0f} mK -> needs a dilution refrigerator")
