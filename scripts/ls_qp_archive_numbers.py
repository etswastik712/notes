"""Numbers for the Sem-3 archive landscapes papers (EC2123: 2021, Sep/Nov 2022, Sep/Nov 2024).
Run: python scripts/ls_qp_archive_numbers.py"""
import math
yr = 3.156e7
print("== 2021 ==")
# Q1a: h_max ~ sigma/(rho g), g ~ (4/3) pi G rho R  => h ~ sigma/rho^2 at fixed R
for rr in (2700, 3000, 5500):
    print(f"Q1a rock rho={rr}: h_rock/h_ice = 10*(920/{rr})^2 = {10*(920/rr)**2:.2f}")
# Q5 flexure w0 e^{-u}(cos u + sin u)
u0 = 3*math.pi/4; ub = math.pi
f = lambda u: math.exp(-u)*(math.cos(u)+math.sin(u))
print(f"Q5 zero at u={u0:.3f} ({u0*100:.0f} km), bulge at u=pi ({ub*100:.0f} km), w/w0={f(ub):.4f}; w(5)/w0={f(5):.4f}")
# Q6 viscosity
rho, g, lam, tau = 3300, 10, 3e6, 5000*yr
P = rho*g*lam
print(f"Q6 P = rho g lambda = {P:.2e} Pa; mu = P tau = {P*tau:.2e} Pa s; with 4pi: {P*tau/4/math.pi:.2e}")
print("== 2022 mid ==")
# Q1 volumes (order of magnitude)
igp = 2500e3*300e3*2.5e3  # m^3 wedge average 2.5 km
him = 2500e3*250e3*15e3
print(f"Q1 IGP ~ {igp/1e9:.2e} km3 ; Himalayan denudation ~ {him/1e9:.2e} km3")
lt = him*2700/1e3/50e6
print(f"Q1d long-term flux over 50 Myr ~ {lt:.2e} t/yr")
# Q2 regolith
n = 1.0/0.1
print(f"Q2 top size = 1 m / 2^{n:.0f} = {1/2**n*1e3:.2f} mm; S/V top = {6*2**n:.0f} m^-1, base 6 m^-1")
# Q3 isostasy
H, rc, rm = 35, 2700, 3300
fb = H*(1-rc/rm)
print(f"Q3a freeboard above free-mantle level = {fb:.2f} km; minus 4 km ocean depth = {fb-4:.2f} km")
e = 24-(rc*35-1000*4-2900*7)/rm
print(f"   with 4 km water + 7 km oceanic crust (2900) loads: e = {e:.2f} km")
s = 1/(1-2000/3300)
print(f"Q3b sediment thickness to fill 1 km = {s:.2f} km -> {s*1e6/1e6:.2f} Myr at 1 mm/yr")
# Q4 Be-10
P0, zs, e_ = 10, 1.0, 1e-3
lam10 = math.log(2)/1.39e6
print(f"Q4 N = P z*/e = {P0*zs/e_:.0f} at/g; with decay: {P0/(lam10+e_/zs):.0f}")
# Q6 tree throw
q = (1/(10*30))*1*0.3
print(f"Q6 q = {q:.1e} m^2/yr = {q*1e4:.0f} cm^2/yr")
# Q7 fill oceans
land = 1.49e8; flux = land*50  # t/yr
V = 1.335e18  # m3
for rb in (2000, 2700):
    t = V*rb/1e3/flux
    print(f"Q7 flux {flux:.2e} t/yr, bulk {rb}: fill time {t/1e6:.0f} Myr")
den = 50e3/1e6/2700
print(f"Q7 denudation = {den*1e6:.1f} m/Myr -> 840 m flattened in {840/den/1e6:.0f} Myr")
print("== 2022 end ==")
L1, A2, L2 = 1.4, 1e5, 1e3
h = math.log10(L2/L1)/math.log10(A2)
print(f"Q1b Hack fit L = {L1} A^{h:.2f};  A = {(1/L1)**(1/h):.3f} x^{1/h:.2f}")
th = 0.5
print(f"Q1c S ~ x^-{th/h:.3f}; z = zL + B(L^p - x^p), p = {1-th/h:.3f}")
print("== 2024 mid ==")
for v, T in ((0.02, 500), (0.045, 300)):
    d = v*T; strain = d/100e3; tau_ = 70e9*strain; sn = 3e3*10*10e3
    print(f"Q1f v={v*1e3:.0f} mm/yr T={T}: slip {d:.1f} m, strain {strain:.1e}, tau {tau_/1e6:.1f} MPa, sigma_n {sn/1e6:.0f} MPa, mu {tau_/sn:.3f}")
print(f"Q1e crust 35->70 km: extra elevation 35*(1-2800/3300) = {35*(1-2800/3300):.1f} km")
print("== 2024 end ==")
for S in (0.02, 0.1, 0.3, 0.4):
    E = 15+123*S
    print(f"Q1f slope {S}: E = {E:.1f} m/Myr, horizontal retreat E/S = {E/S:.0f} m/Myr")
u = 3*math.pi/4; g2 = lambda u: -math.exp(-u)*math.cos(u)
print(f"Q3b w=-c e^-u cos u: zero at u=pi/2 ({math.pi/2:.2f}), bulge at u=3pi/4={u:.2f}, w/c={g2(u):.4f}")
print(f"Q3c bulge at 3pi/4*alpha: alpha=100 km -> {u*100:.0f} km")
print("Q5 300 C at 25-30 C/km ->", 300/30, "-", 300/25, "km")
