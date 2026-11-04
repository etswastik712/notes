"""CM01 numbers: variational calculus examples. .venv/bin/python -W ignore scripts/cm01_numbers.py"""
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
g=9.81
print("== brachistochrone: (0,0) -> (1,-0.5) (y down positive: drop 0.5 m over 1 m)")
X,Y=1.0,0.5
# cycloid x=a(t-sin t), y=a(1-cos t); find t1
f=lambda t:(1-np.cos(t))/(t-np.sin(t))-Y/X
t1=brentq(f,0.1,6.2); a=X/(t1-np.sin(t1))
T_cyc=t1*np.sqrt(a/g)
T_line=np.sqrt(2*np.hypot(X,Y)/(g*Y/np.hypot(X,Y)))  # constant accel g sin(theta): s=1/2 g sinθ T²
# parabola-ish alternative: circular arc? use y=Y*(x/X)**p scan best power
def Tpow(p):
    h=lambda x:np.sqrt((1+(Y*p*x**(p-1)/X**p)**2)/(2*g*Y*(x/X)**p))
    return quad(h,0,X,limit=200)[0]
print("t1=%.5f a=%.5f T_cycloid=%.5f s T_line=%.5f s"%(t1,a,T_cyc,T_line))
print("T power-law y=Y(x/X)^p: p=0.5 %.5f, p=0.7 %.5f"%(Tpow(0.5),Tpow(0.7)))
print("== oscillator second variation, path x0(t)+eps sin(n pi t/T), m=1")
m=1.0;w=2.0
def action(T,n,eps):
    # true path with x(0)=0,x(T)=A : x0=A sin(wt)/sin(wT)
    A=1.0
    t=np.linspace(0,T,20001)
    x0=A*np.sin(w*t)/np.sin(w*T); v0=A*w*np.cos(w*t)/np.sin(w*T)
    x=x0+eps*np.sin(n*np.pi*t/T); v=v0+eps*(n*np.pi/T)*np.cos(n*np.pi*t/T)
    L=0.5*m*v**2-0.5*m*w**2*x**2
    return np.trapezoid(L,t)
for T in (1.0,1.4,2.0):
    pred=m*T/4*((np.pi/T)**2-w**2)
    d=(action(T,1,1e-2)-action(T,1,0))/1e-4
    print("T=%.2f wT=%.3f (pi=%.3f)  d2S/eps^2 numeric=%.5f predicted=%.5f"%(T,w*T,np.pi,d,pred))
print("== E-L check: L=1/2 m xdot^2 - U, U=1/2kx^2 -> m xddot=-kx (symbolic by hand); shift L->L+dF/dt F=x^2/2: same EOM numerically")
k=4.0
def rhs(t,y): return [y[1],-k*y[0]]
s=solve_ivp(rhs,[0,3],[1,0],rtol=1e-10,atol=1e-12)
print("x(3)=%.6f cos(2*3)=%.6f"%(s.y[0,-1],np.cos(2*3)))

print("\n== Thornton Ex 6.1: f=(dy/dx)^2, y=x+alpha sin x on [0,2pi]: J(alpha)=2pi+pi alpha^2")
for al in (-0.5,0.0,0.3,1.0):
    J=quad(lambda x:(1+al*np.cos(x))**2,0,2*np.pi)[0]; print("alpha=%.1f J=%.6f  2pi+pi a^2=%.6f"%(al,J,2*np.pi+np.pi*al**2))
print("\n== soap film between two coaxial rings radius 1, separation 2h: r(z)=c cosh(z/c), r(+-h)=1  =>  c cosh(h/c)=1")
from scipy.optimize import brentq as bq
cs=np.linspace(0.05,1.0,20000); 
hmax=max(c*np.arccosh(1/c) for c in cs if c<=1); print("h_max=%.5f (c at max ~%.4f)"%(hmax,[c for c in cs if abs(c*np.arccosh(1/c)-hmax)<1e-6][0]))
def area(c,h): # 2pi int r sqrt(1+r'^2) dz = 2pi int c cosh^2(z/c) dz = pi c (2h + c sinh(2h/c))... compute numerically
    return quad(lambda z:2*np.pi*c*np.cosh(z/c)**2,-h,h)[0]
h=0.5
roots=[]
for a,b in ((0.05,0.4),(0.4,1.0)):
    f=lambda c:c*np.cosh(h/c)-1
    try: roots.append(bq(f,a,b))
    except Exception as e: pass
print("h=0.5 roots c:",["%.5f"%r for r in roots]," areas:",["%.5f"%area(r,h) for r in roots]," two discs 2*pi*1^2 = %.5f"%(2*np.pi))
for hh in (0.6,0.7): print("h=%.1f: solvable? %s"%(hh, hh<=hmax))
print("\n== pendulum exact period T=4 sqrt(l/g) K(m=sin^2(th0/2)) vs 2pi sqrt(l/g)")
from scipy.special import ellipk
for th0 in (0.1,1.0,2.0,3.0):
    r=2/np.pi*ellipk(np.sin(th0/2)**2); print("theta0=%.1f rad  T/T_small=%.5f   (series 1+th0^2/16=%.5f)"%(th0,r,1+th0**2/16))
print("\n== great circle: two points alpha=170deg apart: short arc 170deg, long arc 190deg; conjugate (antipodal) point at 180deg")
print("\n== h where large catenoid area = two discs (Goldschmidt crossover)")
def big(h):
    f=lambda c:c*np.cosh(h/c)-1
    return bq(f,0.5518,1.0)
hh=bq(lambda h:area(big(h),h)-2*np.pi,0.4,0.65); print("h_cross=%.5f  c=%.5f"%(hh,big(hh)))
