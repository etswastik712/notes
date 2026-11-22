"""Numbers for the eco-evo (BI2113) Sem-3 archive papers 2021-2025.
Run: python scripts/ee_qp_archive_numbers.py"""
import numpy as np, math
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
print("== 2021 mid (online) ==")
print("Q1 dN/dt", 1.5*30*(1-30/50))
print("Q4 N", 27*80/10)
F = 1360/(17/3); print("Q13 F, M", F, 2*F/3)
print("D-Q7 max dN/dt rK/4", 0.1*500/4)
print("D-Q4 coexistence: alpha12*K2 < K1 < K2/alpha21:", 1.5*100, 100/0.5)
print("== 2022 mid ==")
L = np.array([[0,2,2,1],[1,0,0,0],[0,.4,0,0],[0,0,.4,0]])
n0 = np.array([10,5,3,0]); print("Q9 n1 =", L@n0, "lambda =", max(abs(np.linalg.eigvals(L))))
L5 = np.array([[0,2,2,1,0],[1,0,0,0,0],[0,.4,0,0,0],[0,0,.4,0,0],[0,0,0,.3,0]])
print("   5-class n1 =", L5@np.array([10,5,3,0,0]))
a12,a21,K1,K2 = 4,.15,100,20
print("Q11 N1*,N2* =", (K1-a12*K2)/(1-a12*a21), (K2-a21*K1)/(1-a12*a21), "; K2/a21 =", K2/a21, "K1/a12 =", K1/a12)
print("== 2022 end ==")
print("Q6 q =", 0.8)
q = math.sqrt(0.4); p = 1-q; print("Q10 q,p", q, p, "AA among tolerant", p*p/0.6)
def eq(w11,w12,w22): return (w12-w22)/(2*w12-w11-w22)
for name,w,num in (("Nublar",(0.2,0.8,0.4),(200,100,400)),("Sorna",(0.7,0.3,0.6),(300,200,100))):
    pst = eq(*w); p0 = (2*num[0]+num[1])/(2*sum(num))
    p = p0
    for _ in range(5000):
        wb = p*p*w[0]+2*p*(1-p)*w[1]+(1-p)**2*w[2]
        p = (p*p*w[0]+p*(1-p)*w[1])/wb
    wb = p*p*w[0]+2*p*(1-p)*w[1]+(1-p)**2*w[2]
    grey = (1-p)**2*w[2]/wb
    print(f"Q13 {name}: p*={pst:.4f} p0={p0:.4f} -> p_eq={p:.4f}; grey newborn {(1-p)**2:.4f}, grey mature {grey:.4f}")
print("== 2023 mid ==")
r = math.log(415/377)/8; t = math.log(1660/377)/r
print(f"Q7 r={r:.5f}/min, t={t:.1f} min after 10:00 -> {int(10*60+t)//60}:{int(10*60+t)%60:02d}")
n = math.log(100000/20000)/math.log(1.25); print("Q9 n =", n, [20000*1.25**k for k in (7,8)])
print("Q12", 0.1*500/4)
print("== 2023 end ==")
print("Q3 doubling years", math.log(2)/math.log(1.15))
p = (1+math.sqrt(1-2*0.3432))/2; print("Q10 p_red =", p)
p = 0.25; w=(0.8,0.2,0.5); print("Q13 p*=", eq(*w))
for _ in range(2000):
    wb = p*p*w[0]+2*p*(1-p)*w[1]+(1-p)**2*w[2]; p=(p*p*w[0]+p*(1-p)*w[1])/wb
print("   p_eq", round(p,6))
KP,KS,aPS,aSP = 70,11,5.5,.12
print("Q14a intercepts P-isocline (70,0),(0,", KP/aPS, ") S-isocline (", KS/aSP, ",0),(0,11)")
print("   N_P*,N_S* =", (KP-aPS*KS)/(1-aPS*aSP), (KS-aSP*KP)/(1-aPS*aSP))
print("Q14b S-isocline (", 20/.2, ",0),(0,20)")
print("== 2024 mid ==")
print("Q4 n =", math.log(.5)/math.log(.98))
A = np.array([[.28,5],[.12,.8]]); ev = np.linalg.eigvals(A); print("Q5 matrix", A.tolist(), "lambda", max(ev.real))
r = math.log(1e4)/30; print("Q8 r=", r, "2 plants at 15 d:", 2*math.exp(15*r), "N0 needed:", 1e4/math.exp(15*r))
print("Q10 a12 =", (250-125)/250, "a21 =", (300-250)/125)
print("== 2024 end ==")
print("Q3 p = 6/7 =", 6/7)
print("Q10", 0.01/0.19)
qe, qw = math.sqrt(1/6000), math.sqrt(1/500000); qs = (qe+qw)/2
print(f"Q13 qe={qe:.4f} qw={qw:.4f} q={qs:.4f} q^2={qs**2:.6f} (1 in {1/qs**2:.0f}); rounded q=0.0072 -> {0.0072**2:.6f}")
print("Q14 q=0.2 -> females horned p^2 =", 0.8**2)
print("== 2024 assignment ==")
A = np.array([[.4,3],[.32,.7]]); w,v = np.linalg.eig(A); i = np.argmax(w.real); v = v[:,i].real; v/=v.sum()
print("A1 lambda =", w[i].real, "juvenile fraction =", v[0])
r1,K1,a12,r2,K2,a21 = 1,200,.8,.5,300,2
f = lambda t,x: [r1*x[0]*(K1-x[0]-a12*x[1])/K1, r2*x[1]*(K2-x[1]-a21*x[0])/K2]
print("A2 interior saddle:", (K1-a12*K2)/(1-a12*a21), (K2-a21*K1)/(1-a12*a21))
for s in ((70,175),(70,75),(30,120),(30,100)):
    sol = solve_ivp(f,(0,400),s,rtol=1e-9,atol=1e-9); print("   start",s,"->",np.round(sol.y[:,-1],2))
lx = np.array([250,239,210,156,129,109,76,43,32,19,9,0])/250
mx = np.array([0,0,0,.551,.412,.251,.99,.95,.71,.49,.135,0])
lb = np.array([250,239,210,156,129,109,76,43,32,19,9,9,9,0])/250
mb = np.array([0,0,0,0,.412,.251,.99,.95,.71,.49,.27,.27,.27,0])
def rr(l,m):
    x = np.arange(len(l)); g = lambda r: np.sum(np.exp(-r*x)*l*m)-1
    return brentq(g,-2,2)
for nm,l,m in (("a",lx,mx),("b",lb,mb)):
    R0 = np.sum(l*m); x = np.arange(len(l)); T = np.sum(x*l*m)/R0
    print(f"A3{nm} R0={R0:.4f} T={T:.2f} r(Euler-Lotka)={rr(l,m):.4f}/day")
rP,C,d2,g = 1.05,.1,.6,.45
fp = lambda t,x: [rP*x[0]-C*x[0]*x[1], -d2*x[1]+g*C*x[0]*x[1]]
V = lambda N,P: g*C*N - d2*math.log(N) + C*P - rP*math.log(P)
print("A4 eq N*,P* =", d2/(g*C), rP/C, "V(30,10) =", V(30,10), "V(18,15) =", V(18,15))
sol = solve_ivp(fp,(0,30),[30,10],dense_output=True,rtol=1e-10,atol=1e-10,max_step=0.001)
ts = sol.t; N,P = sol.y
d = np.hypot(N-18,P-15); i = np.argmin(d[:len(d)//1])
print(f"   closest approach to (18,15): t={ts[i]:.3f} yr, N={N[i]:.2f}, P={P[i]:.2f}")
from scipy.signal import argrelmin
for j in argrelmin(d)[0][:4]: print(f"   local min t={ts[j]:.3f}: N={N[j]:.2f} P={P[j]:.2f} dist={d[j]:.3f}")
print("== 2025 ==")
print("mid Q3 Lincoln", 46*37/27)
print("mid Q11 sp1 isocline (250,0)-(0,", 250/1.4, "); sp2 (", 1500/.9, ",0)-(0,1500)")
print("end Q5 max het 4 alleles", 1-4*.25**2, "; Q8 P(same genotype)", .25**2+.5**2+.25**2)
