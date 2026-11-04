"""CM05 numbers. .venv/bin/python -W ignore scripts/cm05_numbers.py"""
import numpy as np
from scipy.integrate import solve_ivp, quad
rng=np.random.default_rng(1)
print("== disintegration (LL 16): m=1, v0=1 in C, parent speed V=2 (V>v0): sin th_max = v0/V")
v0=1.;V=2.; print("th_max=%.3f deg"%np.degrees(np.arcsin(v0/V)))
c=rng.uniform(-1,1,2_000_000); s=np.sqrt(1-c**2)  # isotropic in C: cos th0 uniform
vx=v0*c+V; vy=v0*s; T=0.5*(vx**2+vy**2); th=np.degrees(np.arctan2(vy,vx))
print("T range [%.4f,%.4f] expected [%.4f,%.4f]; max lab angle %.3f deg"%(T.min(),T.max(),0.5*(v0-V)**2,0.5*(v0+V)**2,th.max()))
h,_=np.histogram(T,bins=10,range=(0.5,4.5)); print("histogram of T (10 bins) rel. spread: %.4f"%(h.std()/h.mean()))
print("== elastic collision, target at rest: tan th1 = m2 sin chi/(m1 + m2 cos chi), th2=(pi-chi)/2")
m1,m2=1.,4.; chi=np.radians(90); th1=np.degrees(np.arctan2(m2*np.sin(chi),m1+m2*np.cos(chi))); th2=np.degrees((np.pi-chi)/2)
v1=np.sqrt(m1**2+m2**2+2*m1*m2*np.cos(chi))/(m1+m2); v2=2*m1/(m1+m2)*np.sin(chi/2)
print("th1=%.3f th2=%.3f v1/v=%.4f v2/v=%.4f ; m1 v1^2 + m2 v2^2 = %.6f (should be m1=1)"%(th1,th2,v1,v2,m1*v1**2+m2*v2**2))
print("energy transfer fraction 4 m1 m2/(m1+m2)^2 sin^2(chi/2) = %.4f"%(4*m1*m2/(m1+m2)**2*np.sin(chi/2)**2))
print("m1=4,m2=1: max lab deflection sin th = m2/m1 -> %.3f deg ; equal masses th1+th2 = %.1f deg"%(np.degrees(np.arcsin(1/4)),90))
print("== hard sphere, equal masses: dsigma1 = a^2 |cos th1| dOmega1 ; integrate over forward hemisphere")
print("integral = %.6f (pi = %.6f)"%(2*np.pi*quad(lambda t:np.cos(t)*np.sin(t),0,np.pi/2)[0],np.pi))
print("== Rutherford deflection by trajectory integration: U=alpha/r, alpha/(m v^2)=0.5, p=1: chi = 2 arctan(alpha/(m v^2 p))")
a_mv2=0.5; p=1.0
f=lambda t,y:[y[2],y[3],a_mv2*y[0]/np.hypot(y[0],y[1])**3,a_mv2*y[1]/np.hypot(y[0],y[1])**3]  # m=1, v=1 -> alpha=0.5, F = alpha r/r^3
R0=2000.; s=solve_ivp(f,[0,4000],[-R0,p,1.0,0.0],rtol=1e-12,atol=1e-12,max_step=1.0)
vxf,vyf=s.y[2,-1],s.y[3,-1]; chi_num=np.degrees(np.arctan2(vyf,vxf)); print("chi_numeric=%.4f deg ; formula=%.4f deg"%(abs(chi_num),np.degrees(2*np.arctan(a_mv2/p))))
print("== Rutherford, 5 MeV alpha on gold: alpha=Z1 Z2 e^2/(4 pi eps0) = 2*79*1.43996 MeV fm")
al=2*79*1.439964; E=5.0
print("alpha=%.2f MeV fm ; closest approach head-on d = alpha/E = %.2f fm"%(al,al/E))
for thd in (30,60,90,120,150):
    th=np.radians(thd); ds=(al/(4*E))**2/np.sin(th/2)**4
    print("theta=%3d deg  dsigma/dOmega = %9.2f fm^2/sr = %8.3f b/sr"%(thd,ds,ds/100))
print("ratio (30deg)/(150deg) = %.1f ; recoil correction mass ratio m1/m2=%.4f"%(1/np.sin(np.radians(15))**4*np.sin(np.radians(75))**4,4/197))
print("== small-angle formula: p = 2 alpha/(m v^2 theta) vs exact (alpha/mv^2) cot(theta/2), alpha/mv^2=1")
for th in (0.05,0.1,0.5,1.0):
    print("theta=%.2f: exact p=%.4f  small-angle p=%.4f ratio=%.4f"%(th,1/np.tan(th/2),2/th,(2/th)/(1/np.tan(th/2))))
print("== spherical well (LL P2): n^2=1+2U0/mv^2; U0=0.5 mv^2: n=%.4f chi_max: cos(chi/2)=1/n -> %.3f deg ; check integral of dsigma = pi a^2"%(np.sqrt(2),np.degrees(2*np.arccos(1/np.sqrt(2)))))
n=np.sqrt(2.0); 
def dsdw(chi):
    c=np.cos(chi/2); return n**2/(4*c)*(n*c-1)*(n-c)/(n**2+1-2*n*c)**2
chimax=2*np.arccos(1/n)
print("total = %.6f"%(2*np.pi*quad(lambda x:dsdw(x)*np.sin(x),0,chimax)[0]))
# via geometry: sin alpha = p/a ; sin beta = sin alpha / n ; chi = 2 (alpha - beta)
al_=np.linspace(0,np.pi/2,100001); be_=np.arcsin(np.sin(al_)/n); chi_=2*(al_-be_); p_=np.sin(al_)
i=np.argmin(abs(chi_-np.radians(40))); dpdchi=np.gradient(p_,chi_); print("check dsigma/dOmega at chi=40deg: geometry p/sin chi |dp/dchi| = %.6f, formula = %.6f"%(p_[i]/np.sin(chi_[i])*abs(dpdchi[i]),dsdw(chi_[i])))
print("== gravitational focusing: sigma = pi R^2 (1+ v_esc^2/v_inf^2); Earth v_esc=11.186 km/s")
for vinf in (5,11.186,20,40): print("v_inf=%.3f km/s: enhancement %.4f"%(vinf,1+(11.186/vinf)**2))
print("== fall to centre U=-alpha/r^2: sigma=2 pi alpha/(m v^2); alpha/(m v^2)=1 -> sigma=%.4f"%(2*np.pi))
