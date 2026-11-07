"""CM11 numbers (Hamilton-Jacobi, action-angle). .venv/bin/python -W ignore scripts/cm11_numbers.py
LL = Landau-Lifshitz Vol. 1 §43, §47-§50."""
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import ellipk
from scipy.optimize import brentq
np.set_printoptions(precision=6,suppress=True)

print("== 1. oscillator by Hamilton-Jacobi (LL 47.4): S = -Et + int sqrt(2mE - m^2 w^2 q^2) dq ; beta = dS/dE = int m dq/sqrt(...) - t")
m,w,E=1.0,2.0,3.0
A=np.sqrt(2*E/(m*w*w));print("   amplitude sqrt(2E/(m w^2)) = %.6f"%A)
# beta + t = int_0^q m dq'/sqrt(2mE-m^2 w^2 q'^2) = (1/w) arcsin(q/A)  -> q = A sin(w (t+beta))
for q_ in (0.4,0.9,1.2):
    I=quad(lambda x:m/np.sqrt(2*m*E-m*m*w*w*x*x),0,q_)[0];print("   q=%.2f: integral = %.6f ; (1/w) arcsin(q/A) = %.6f"%(q_,I,np.arcsin(q_/A)/w))
print("   -> t + beta = (1/w) arcsin(q/A): q(t) = A sin(w(t+beta)) = exact motion; area of the orbit = 2 pi E/w = %.6f ; I = E/w = %.6f (LL 49.12)"%(2*np.pi*E/w,E/w))

print("\n== 2. Kepler problem in spherical coordinates (LL 48.8-48.9) with b=0: radial integral and the conic orbit")
mk=1.0;k=1.0;Ek=-0.3;M=1.1
pp=M*M/(mk*k);e=np.sqrt(1+2*Ek*M*M/(mk*k*k));print("   m=k=1, E=%.2f, M=%.2f: p = M^2/mk = %.4f, e = %.6f, r_min = p/(1+e) = %.5f, r_max = p/(1-e) = %.5f"%(Ek,M,pp,e,pp/(1+e),pp/(1-e)))
rmin,rmax=pp/(1+e),pp/(1-e)
# phi(r) - phi0 = int_{rmin}^{r} M dr / (r^2 sqrt(2m(E+k/r) - M^2/r^2))   should equal arccos((p/r - 1)/e)
f=lambda r:M/(r*r*np.sqrt(2*mk*(Ek+k/r)-M*M/(r*r)))
for rr in (0.9,1.3,1.8,2.2):
    I=quad(f,rmin*(1+1e-9),rr,limit=200)[0];print("   r=%.2f: HJ integral = %.6f ; arccos((p/r-1)/e) = %.6f"%(rr,I,np.arccos((pp/rr-1)/e)))
print("   -> orbit  p/r = 1 + e cos(phi - phi0)")

print("\n== 3. pendulum H = p^2/2 - cos q: action I(E) = (1/2 pi) oint p dq, omega = dE/dI (LL 49.9) vs 2 pi/T(E) from elliptic K")
def I_of_E(E):
    q0=np.arccos(-E);return 2/(2*np.pi)*quad(lambda q:np.sqrt(2*(E+np.cos(q))),-q0,q0)[0]
for th0 in (20,60,90,120):
    E=-np.cos(np.radians(th0));kk=np.sin(np.radians(th0)/2);omega_K=np.pi/(2*ellipk(kk*kk))
    h=1e-5;omega_I=2*h/(I_of_E(E+h)-I_of_E(E-h))
    print("   amplitude %3d deg: E=%.5f I=%.6f (I small-amplitude = E+1 = %.6f) ; omega = dE/dI = %.6f ; pi/(2K(k)) = %.6f"%(th0,E,I_of_E(E),E+1,omega_I,omega_K))

print("\n== 4. adiabatic invariance (LL 49.6-49.7): H = p^2/2 + w(t)^2 q^2/2, w ramps linearly 1 -> 2 over time tau; I = E/w")
def run(tau,phase):
    w_=lambda t:1+min(t,tau)/tau
    f=lambda t,y:[y[1],-w_(t)**2*y[0]]
    y0=[np.sin(phase),np.cos(phase)]  # E0 = 1/2 (w=1), I0=0.5
    s=solve_ivp(f,[0,tau+40],y0,rtol=1e-10,atol=1e-12,dense_output=True,max_step=0.01)
    t=np.linspace(tau,tau+40,4000);q,p=s.sol(t);Et=0.5*p*p+0.5*4*q*q;return 0.5,Et/2.0
for tau in (2,10,50,300):
    ratios=[];Efs=[]
    for ph in np.linspace(0,np.pi,9)[:-1]:
        I0,I=run(tau,ph);ratios.append(I.mean()/I0);Efs.append(I.mean()*2)
    print("   tau=%4d: final I/I0 averaged over a period: mean %.5f, range [%.5f, %.5f] (E_f/E_0 = %.4f; w ratio is 2)"%(tau,np.mean(ratios),min(ratios),max(ratios),np.mean(Efs)/0.5))
