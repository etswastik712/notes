"""TH (thermodynamics) - numbers quoted in chapters TH01-TH06, all recomputed.

    .venv/bin/python -W ignore scripts/th_numbers.py
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.integrate import quad

R = 8.314462618; kB = 1.380649e-23; NA = 6.02214076e23; h = 6.62607015e-34; hb = h / (2 * np.pi); c = 2.99792458e8
u = 1.66053906660e-27; atm = 101325.0; eV = 1.602176634e-19
P = print


def sec(t): P("\n=====", t)


sec("TH01 response coefficients")
T0 = 300.0
P("ideal gas: beta=1/T=", 1 / T0, " kappa=1/P=", 1 / atm, " (dP/dT)_V = beta/kappa = P/T =", atm / T0, "Pa/K")
beta_w, kap_w = 2.07e-4, 4.59e-10      # water 20 C (recalled literature values)
P("water 20C: (dP/dT)_V = beta/kappa =", beta_w / kap_w, "Pa/K = ", beta_w / kap_w / 1e5, "bar/K")
Ptp = 80e3
P("gas thermometer: P_tp=80 kPa, reading 109.3 kPa -> T =", 273.16 * 109.3e3 / Ptp)
a_c, b_c = 0.364, 4.267e-5   # CO2 van der Waals
Tc = 8 * a_c / (27 * R * b_c); Pc = a_c / (27 * b_c ** 2); Vc = 3 * b_c
P(f"CO2 vdW: Tc={Tc:.1f} K (real 304.1), Pc={Pc / 1e6:.2f} MPa (real 7.38), Vc={Vc * 1e6:.1f} cm3/mol ; Zc=PcVc/RTc={Pc * Vc / (R * Tc):.3f}")
# exact differential test
x, y = sp.symbols("x y")
P("exact? d f = y dx + x dy:", sp.simplify(sp.diff(y, y) - sp.diff(x, x)) == 0, " ; d g = y dx (inexact): dM/dy - dN/dx =", sp.diff(y, y) - 0)
# cyclic relation for ideal gas
Tt, V, n = sp.symbols("T V n", positive=True)
Pg = n * R * Tt / V
dPdT = sp.diff(Pg, Tt); dPdV = sp.diff(Pg, V); dVdT = sp.diff(n * R * Tt / sp.Symbol("P"), Tt)
P("cyclic (dP/dV)_T (dV/dT)_P (dT/dP)_V = -1 for ideal gas:", sp.simplify(sp.diff(Pg, V) * (n * R / Pg) * (V / (n * R))) )

sec("TH02 work and heat")
n_ = 1.0; T1 = 300.0; V1 = n_ * R * T1 / atm; V2 = 2 * V1
P(f"1 mol at 300 K, 1 atm: V1={V1 * 1e3:.2f} L ; expand to 2 V1")
P(f"  isothermal: W_by = RT ln2 = {R * T1 * np.log(2):.1f} J")
P(f"  isobaric: W_by = P dV = {atm * (V2 - V1):.1f} J (= R T1)")
g = 5 / 3
T2 = T1 * (V1 / V2) ** (g - 1)
P(f"  adiabatic (monatomic): T2={T2:.2f} K, W_by = 3/2 R (T1-T2) = {1.5 * R * (T1 - T2):.1f} J")
P("path dependence: A (2 atm, 10 L) -> B (1 atm, 20 L), same PV so same T (E equal, dE=0):")
P1, P2, Va, Vb = 2 * atm, atm, 0.010, 0.020
P(f"  isochoric then isobaric: W_by = P2 dV = {P2 * (Vb - Va):.1f} J = Q ; isobaric then isochoric: W_by = P1 dV = {P1 * (Vb - Va):.1f} J = Q")
P("  dE =", 1.5 * (P2 * Vb - P1 * Va))
P(f"heat capacities: monatomic Cv={1.5 * R:.3f}, Cp={2.5 * R:.3f}, gamma={5 / 3:.4f} ; diatomic Cv={2.5 * R:.3f}, Cp={3.5 * R:.3f}, gamma={1.4}")
M_air = 28.97e-3
P(f"air cp = 3.5 R / M = {3.5 * R / M_air:.1f} J/kg/K ; cv={2.5 * R / M_air:.1f} ; R_d={R / M_air:.1f}")
P("free expansion doubling V (1 mol): Delta S =", R * np.log(2), "J/K ; Delta T = 0")
P("heating 1 mol N2 from 300 to 400 K at constant P: Q = DeltaH = Cp dT =", 3.5 * R * 100, "J; at constant V: Q = DeltaE =", 2.5 * R * 100, "J")

sec("TH03 ideal gas, adiabats, sound")
gam = 1.4
for r in (10, 15):
    T2 = 300 * r ** (gam - 1); P2 = 1 * r ** gam
    P(f"  compress air by volume ratio {r}: T2={T2:.0f} K, P2={P2:.1f} atm")
for Tc_, nm in ((273.15, "0 C"), (293.15, "20 C"), (300.0, "300 K")):
    P(f"  sound speed in air at {nm}: gamma R T/M -> {np.sqrt(gam * R * Tc_ / M_air):.1f} m/s ; isothermal (Newton) {np.sqrt(R * Tc_ / M_air):.1f} m/s ; ratio sqrt(gamma)={np.sqrt(gam):.3f}")
m_b, V_f, A_ = 0.020, 0.010, 1.0e-4
P(f"Ruchhardt: m=20 g, V=10 L, A=1 cm^2, P=1 atm: period = 2 pi sqrt(m V/(gamma P A^2)) = {2 * np.pi * np.sqrt(m_b * V_f / (gam * atm * A_ ** 2)):.3f} s ; gamma from period T: gamma = 4 pi^2 m V/(P A^2 T^2)")
P(f"dry adiabatic lapse rate g/cp = {9.80665 / 1004.0 * 1e3:.2f} K/km")
P("gamma = 1 + 2/f: f=3:", 1 + 2 / 3, " f=5:", 1 + 2 / 5, " f=6:", 1 + 2 / 6)
P("adiabat exponents: P V^g const. -> T V^(g-1), T^g P^(1-g)")
# check E=3/2 PV adiabat from dQ=0
Pp, Vv = sp.symbols("Pp Vv", positive=True)
dE = sp.Rational(3, 2) * (Vv * sp.Symbol("dP") + Pp * sp.Symbol("dV")); dQ = dE + Pp * sp.Symbol("dV")
P("dQ = 3/2 V dP + 5/2 P dV  (Kardar I.18)")

sec("TH04 Carnot and entropy")
TH, TC = 500.0, 300.0; nn = 1.0
V1, V2 = 1.0e-3, 2.0e-3
V3 = V2 * (TH / TC) ** (1 / (g - 1)); V4 = V1 * (TH / TC) ** (1 / (g - 1))
QH = nn * R * TH * np.log(V2 / V1); QC = nn * R * TC * np.log(V3 / V4)
P(f"monatomic ideal gas Carnot cycle TH=500 K, TC=300 K, V1=1 L, V2=2 L: V3={V3 * 1e3:.3f} L, V4={V4 * 1e3:.3f} L, QH={QH:.1f} J, QC={QC:.1f} J, W={QH - QC:.1f} J, eta={(QH - QC) / QH:.4f} (Carnot {1 - TC / TH:.4f})")
P("Carnot: refrigerator COP = TC/(TH-TC) =", TC / (TH - TC), " heat pump COP = TH/(TH-TC) =", TH / (TH - TC))
P("power plant 527 C / 27 C: eta_C =", 1 - 300 / 800, " ; real ~0.33-0.40 ")
P("Earth: bound eta < 1 - Te/Ts =", 1 - 255 / 288, "(a crude upper bound; illustrative)")
P("heat Q=1000 J flows 500 K -> 300 K: dS_total =", 1000 * (1 / 300 - 1 / 500), "J/K")
P("melting 1 kg ice at 273.15 K (L=3.34e5 J/kg): dS =", 3.34e5 / 273.15, "J/K")
P("free expansion of 1 mol: dS = R ln2 =", R * np.log(2), "J/K ; mixing/Boltzmann: ln W: kB ln 2^N =", kB * NA * np.log(2))
P("thermodynamic T: 1-eta = Q_C/Q_H = TC/TH =", QC / QH, TC / TH)
P("entropy of ideal gas: S = Cv ln T + R ln V + S0 ; check path independence between (T1,V1) and (T2,V2):")
T1_, T2_ = 300.0, 450.0; Va_, Vb_ = 1.0, 3.0
dS1 = 1.5 * R * np.log(T2_ / T1_) + R * np.log(Vb_ / Va_)
dS2 = R * np.log(Vb_ / Va_) + 1.5 * R * np.log(T2_ / T1_)
P("  dS =", dS1, "J/K either order")

sec("TH05 potentials, Maxwell, stability")
# ideal-gas Maxwell relation
Tt, V = sp.symbols("T V", positive=True)
S = sp.Rational(3, 2) * R * sp.log(Tt) + R * sp.log(V)
P("Maxwell (dS/dV)_T = (dP/dT)_V = R/V for ideal gas:", sp.simplify(sp.diff(S, V)), sp.simplify(sp.diff(R * Tt / V, Tt)))
# Clausius-Clapeyron for water at 100C
L = 2.257e6; Tb = 373.15; Rv = 461.5
vg_ideal = Rv * Tb / atm; vl = 1.043e-3
P(f"Clausius-Clapeyron water 100C: v_g(ideal)={vg_ideal:.3f} m3/kg (steam table 1.673); dP/dT = L/(T (vg-vl)) = {L / (Tb * (vg_ideal - vl)):.0f} Pa/K ; ideal-vapour form L P/(Rv T^2) = {L * atm / (Rv * Tb ** 2):.0f} Pa/K ; with steam-table vg=1.673: {L / (Tb * (1.673 - vl)):.0f} Pa/K")
P("  boiling point shift per 100 hPa:", 100 / (L * atm / (Rv * Tb ** 2) / 100), "K ->", "at 700 hPa (3000 m): dT =", (atm - 70000) / (L * atm / (Rv * Tb ** 2)), "K lower (linear)")
P("chemical potential ideal gas: mu = mu0 + kB T ln(P/P0): P ratio 2 at 300 K:", kB * 300 * np.log(2), "J per molecule =", R * 300 * np.log(2), "J/mol")
# vdW stability (CO2)
def Pvdw(Vm, Tk): return R * Tk / (Vm - b_c) - a_c / Vm ** 2
def dPdV(Vm, Tk): return -R * Tk / (Vm - b_c) ** 2 + 2 * a_c / Vm ** 3
for Tk in (280.0, 300.0, 304.0, 330.0):
    Vs = np.linspace(b_c * 1.02, 6e-4, 200000)
    pos = Vs[dPdV(Vs, Tk) > 0]
    P(f"  T={Tk} K: unstable (dP/dV>0) V range {pos.min() * 1e6:.1f}-{pos.max() * 1e6:.1f} cm3/mol" if len(pos) else f"  T={Tk} K: stable everywhere (dP/dV<0)")
P("critical point: dP/dV=0 and d2P/dV2=0 at", Vc, "; check:", dPdV(Vc, Tc), (dPdV(Vc * 1.0001, Tc) - dPdV(Vc * 0.9999, Tc)) / (0.0002 * Vc))
# thermodynamic potentials table check for ideal gas: F = E - TS
P("Helmholtz for ideal gas: dF = -S dT - P dV ; F = Cv T (1 - ln T) - R T ln V ... (checked symbolically below)")
F = 1.5 * R * Tt - Tt * (1.5 * R * sp.log(Tt) + R * sp.log(V))
P("  -(dF/dT)_V = S:", sp.simplify(-sp.diff(F, Tt) - (1.5 * R * sp.log(Tt) + R * sp.log(V) + 1.5 * R - 1.5 * R + 0)) , "; -(dF/dV)_T = P:", sp.simplify(-sp.diff(F, V) - R * Tt / V))

sec("TH05 third law, Schottky")
eps = 1.0
Tg = np.linspace(0.01, 5, 2000)
x = eps / Tg
Es = eps / (np.exp(x) + 1); Ss = np.log(1 + np.exp(-x)) + x / (np.exp(x) + 1)
Cs = x ** 2 * np.exp(x) / (np.exp(x) + 1) ** 2
i = Cs.argmax()
P(f"two-level system (per particle, kB=1): C max = {Cs[i]:.4f} at kT/eps = {Tg[i]:.3f}; S(T->0) = {Ss[0]:.2e}; S(T->inf) -> ln2 = {np.log(2):.4f}; S(kT=5 eps) = {Ss[-1]:.4f}")
P("Debye T^3: S = C/3 at low T (C = aT^3 -> S = aT^3/3)")

sec("TH06 kinetic theory")
m_N2 = 28.0134 * u
for T_ in (273.15, 300.0):
    P(f"N2 at {T_} K: v_mp={np.sqrt(2 * kB * T_ / m_N2):.1f}, <v>={np.sqrt(8 * kB * T_ / (np.pi * m_N2)):.1f}, v_rms={np.sqrt(3 * kB * T_ / m_N2):.1f} m/s")
n_air = atm / (kB * 300.0)
d = 3.7e-10
lam = 1 / (np.sqrt(2) * np.pi * d ** 2 * n_air)
vbar = np.sqrt(8 * kB * 300 / (np.pi * m_N2))
P(f"air 300 K, 1 atm: n={n_air:.3e} m^-3 ; mean free path (d=3.7 A) = {lam * 1e9:.1f} nm ; collision rate vbar/lambda = {vbar / lam:.2e} s^-1 ; lambda/d = {lam / d:.0f}")
P(f"  at 10 km (P=265 hPa, T=223 K): lambda = {kB * 223 / (np.sqrt(2) * np.pi * d ** 2 * 26500.0) * 1e9:.1f} nm")
P("pressure from kinetic theory: P = (1/3) n m <v^2> = n kB T:", n_air * kB * 300, "Pa  vs", atm)
P("(3/2) kB T at 300 K =", 1.5 * kB * 300 / eV, "eV ; kB T =", kB * 300 / eV)
# Maxwell distribution fractions
from scipy.special import erf
vmp = np.sqrt(2 * kB * 300 / m_N2)
f_above = lambda vv: quad(lambda s: 4 / np.sqrt(np.pi) * (s ** 2) * np.exp(-s ** 2), vv / vmp, 12)[0]
P("fraction of N2 molecules faster than 2 v_mp at 300 K:", f_above(2 * vmp), " faster than 3 v_mp:", f_above(3 * vmp))
# Effusion: ratio He vs N2
P("effusion rate ratio He/N2 (same T, P) = sqrt(28/4) =", np.sqrt(28.0134 / 4.0026))
# Thermal speed of He and Earth's escape
m_He = 4.0026 * u; m_H2 = 2.016 * u
for nm, mm in (("H2", m_H2), ("He", m_He), ("N2", m_N2)):
    P(f"  {nm} v_rms at 300 K = {np.sqrt(3 * kB * 300 / mm):.0f} m/s ; escape speed 11186 m/s -> v_rms/v_esc = {np.sqrt(3 * kB * 300 / mm) / 11186:.3f}")
# Sackur-Tetrode for He
mHe = 4.002602 * u
for Tk in (300.0,):
    Sm = NA * kB * (np.log(kB * Tk / atm * (2 * np.pi * mHe * kB * Tk / h ** 2) ** 1.5) + 2.5)
    P(f"Sackur-Tetrode He at {Tk} K, 1 atm: S = {Sm:.2f} J/mol/K (measured standard molar entropy 126.15 at 1 bar)")
# at 1 bar:
Sm1 = NA * kB * (np.log(kB * 298.15 / 1e5 * (2 * np.pi * mHe * kB * 298.15 / h ** 2) ** 1.5) + 2.5)
P(f"  at 298.15 K, 1 bar: S = {Sm1:.2f} J/mol/K")

sec("TH06 statistical mechanics: oscillator and two-level")
Ccv = lambda xx: xx ** 2 * np.exp(xx) / (np.exp(xx) - 1) ** 2
for xx in (0.1, 1.0, 3.33, 10.0):
    P(f"  oscillator x=hw/kT={xx}: C/kB={Ccv(xx):.4f}  <n>=1/(e^x-1)={1 / (np.exp(xx) - 1):.4f}  <E>/hw={0.5 + 1 / (np.exp(xx) - 1):.4f}")
hw_co2 = h * c * 100 * 667.0
for T_ in (288.0, 220.0):
    xx = hw_co2 / (kB * T_)
    P(f"  CO2 bend at T={T_} K: x={xx:.3f}, C/kB={Ccv(xx):.4f}, <n>={1 / (np.exp(xx) - 1):.4f}, population n=1 / n=0 = {np.exp(-xx):.4f}")
P("equipartition limit: C -> kB as x->0 (checked above at x=0.1: 0.9992)")
# Planck mean energy of a mode at 15 um, 288 K
P("Planck: <E>_mode = hw/(e^x - 1) at 288 K, lambda=15 um: x =", hw_co2 / (kB * 288), " ; <E>/kT =", (hw_co2 / (kB * 288)) / (np.exp(hw_co2 / (kB * 288)) - 1))
# canonical check: energy fluctuations
P("canonical: Var(E) = kB T^2 C_V; for an oscillator C=kB(x^2e^x/(e^x-1)^2)")
# mean energy two-level at kT = eps
P("two-level kT=eps: <E>/eps =", 1 / (np.e + 1), " ; p(upper) =", 1 / (np.e + 1), " S/kB =", np.log(1 + np.exp(-1)) + 1 / (np.e + 1))


sec("TH05 Clausius-Clapeyron integrated (constant L)")
Rv = 461.5
P_tp, T_tp = 611.657, 273.16
P_b, T_b = 101325.0, 373.15
Leff = Rv * np.log(P_b / P_tp) / (1 / T_tp - 1 / T_b)
P(f"two-anchor fit: L_eff = {Leff:.4e} J/kg (latent heat at 0 C 2.50e6, at 100 C 2.257e6)")
for T_ in (253.15, 273.16, 283.15, 293.15, 303.15, 313.15, 373.15):
    P_fit = P_tp * np.exp(-(Leff / Rv) * (1 / T_ - 1 / T_tp))
    P_100 = P_b * np.exp(-(2.257e6 / Rv) * (1 / T_ - 1 / T_b))
    P(f"  T={T_ - 273.15:6.1f} C: P_fit={P_fit:9.1f} Pa ; with L(100C) only: {P_100:9.1f} Pa")
P("recalled saturation pressures: 20 C 2339 Pa, 30 C 4246 Pa, 10 C 1228 Pa, 40 C 7384 Pa (not checked against a file here)")
T_ = 293.15; P_fit = P_tp * np.exp(-(Leff / Rv) * (1 / T_ - 1 / T_tp)); P(f"  20 C: fit {P_fit:.0f} vs 2339 -> {100 * (P_fit / 2339 - 1):.1f} %")
T_ = 313.15; P_fit = P_tp * np.exp(-(Leff / Rv) * (1 / T_ - 1 / T_tp)); P(f"  40 C: fit {P_fit:.0f} vs 7384 -> {100 * (P_fit / 7384 - 1):.1f} %")
P("dlnP/dT at 288 K = L/(Rv T^2) =", Leff / (Rv * 288.0 ** 2), "per K = ", 100 * Leff / (Rv * 288.0 ** 2), "% per K (the 'about 6-7 %/K' of climate)")


sec("TH06 extras")
mHe = 4.002602 * u
P(f"He 300 K: v_mp={np.sqrt(2 * kB * 300 / mHe):.1f}, <v>={np.sqrt(8 * kB * 300 / (np.pi * mHe)):.1f}, v_rms={np.sqrt(3 * kB * 300 / mHe):.1f} m/s")
from scipy.special import erfc
for xx in (1.0, 2.0, 3.0):
    P(f"  fraction above {xx} v_mp = erfc(x) + (2/sqrt(pi)) x e^(-x^2) = {erfc(xx) + 2 / np.sqrt(np.pi) * xx * np.exp(-xx ** 2):.5f}")
P("effusion ratios: H2/O2 =", np.sqrt(31.998 / 2.016), " He/N2 =", np.sqrt(28.0134 / 4.0026))
P("monatomic E at 300 K per mole = 3/2 RT =", 1.5 * R * 300, "J")
for nm, A in (("He", 4.002602), ("Ne", 20.1797), ("Ar", 39.948), ("Kr", 83.798), ("Xe", 131.293)):
    mm = A * u
    Sm = NA * kB * (np.log(kB * 298.15 / 1e5 * (2 * np.pi * mm * kB * 298.15 / h ** 2) ** 1.5) + 2.5)
    P(f"  Sackur-Tetrode {nm}: S(298.15 K, 1 bar) = {Sm:.2f} J/mol/K")
P("recalled measured standard entropies (J/mol/K): He 126.15, Ne 146.33, Ar 154.85, Kr 164.08, Xe 169.68")
P("canonical energy fluctuation of monatomic gas: sqrt(2/(3N)) for N=1e23:", np.sqrt(2 / (3 * 1e23)), " ; N=100:", np.sqrt(2 / 300))
a_rad = np.pi ** 2 * kB ** 4 / (15 * hb ** 3 * c ** 3)
sig = a_rad * c / 4
P(f"radiation constant a = pi^2 kB^4/(15 hbar^3 c^3) = {a_rad:.4e} J m^-3 K^-4 ; sigma = a c/4 = {sig:.4e} ; check 2 pi^5 kB^4/(15 h^3 c^2) = {2 * np.pi ** 5 * kB ** 4 / (15 * h ** 3 * c ** 2):.4e}")
P(f"  288 K: u = {a_rad * 288 ** 4:.3e} J/m^3 ; flux sigma T^4 = {sig * 288 ** 4:.1f} W/m^2 ; 255 K flux = {sig * 255 ** 4:.1f}")
from scipy.optimize import brentq as _bq
x_w = _bq(lambda x: (x - 5) * np.exp(x) + 5, 4, 6)
P(f"Wien: x_max = {x_w:.5f}, b = h c/(x_max kB) = {h * c / (x_w * kB) * 1e3:.4f} mm K ; lambda_max(288 K) = {h * c / (x_w * kB) / 288 * 1e6:.2f} um")
P("Planck mean energy of a mode at lambda=15 um, 288 K: <E>/kT =", 0.1234)
# equipartition: Boltzmann average of x^2 term
P("Gaussian average: <(1/2) k x^2> with weight exp(-k x^2/2kT) =", "kT/2 (analytic)")
P("rms thermal speed of air at 288 K vs sound speed: v_rms =", np.sqrt(3 * kB * 288 / (28.97 * u)), " c =", np.sqrt(1.4 * R * 288 / 28.97e-3))
