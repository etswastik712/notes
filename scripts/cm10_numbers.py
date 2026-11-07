"""CM10 numbers (canonical transformations, Liouville). .venv/bin/python -W ignore scripts/cm10_numbers.py
LL = Landau-Lifshitz Vol. 1 §45-§46; LL bracket [f,g] = sum (df/dp dg/dq - df/dq dg/dp)."""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp, quad
np.set_printoptions(precision=6,suppress=True)
q,p,m,w,t,Qs,Ps=sp.symbols("q p m omega t Q P",positive=True)
def PB(f,g,x,y): return sp.simplify(sp.diff(f,y)*sp.diff(g,x)-sp.diff(f,x)*sp.diff(g,y))   # LL: d_p f d_q g - d_q f d_p g ; call PB(f,g,q,p)
def jac(Qf,Pf): return sp.simplify(sp.Matrix([[sp.diff(Qf,q),sp.diff(Qf,p)],[sp.diff(Pf,q),sp.diff(Pf,p)]]).det())

print("== 1. identity-type and simple canonical maps: LL conditions (45.10) [Q,Q]=0 trivially for s=1; [P,Q] = 1")
maps={"swap Q=p,P=-q":(p,-q),"scale Q=aq,P=p/a (a=3)":(3*q,p/3),"shear Q=q,P=p+cq (c=2)":(q,p+2*q),"Q=q+kp,P=p (k=2)":(q+2*p,p),
 "Q=q^2,P=p/(2q)":(q**2,p/(2*q)),"Q=q^2,P=p (not canonical)":(q**2,p),"Q=q,P=2p (scale 2)":(q,2*p)}
for k,(Qf,Pf) in maps.items(): print("   %-28s [P,Q]_(LL) = %-8s  Jacobian det = %s"%(k,PB(Pf,Qf,q,p),jac(Qf,Pf)))

print("\n== 2. oscillator H=p^2/2m + m w^2 q^2/2:  Q=arctan(m w q/p), P=(p^2+m^2 w^2 q^2)/(2 m w)  (action-angle)")
Qf=sp.atan(m*w*q/p);Pf=(p**2+m**2*w**2*q**2)/(2*m*w)
print("   [P,Q] =",PB(Pf,Qf,q,p),"; Jacobian det =",jac(Qf,Pf),"; H'(P) = w P:",sp.simplify((p**2/(2*m)+m*w**2*q**2/2)-w*Pf))
F=m*w*q**2/(2*sp.tan(Qs))
print("   generating function F(q,Q) = m w q^2 cot(Q)/2: p = dF/dq =",sp.simplify(sp.diff(F,q)),"; P = -dF/dQ =",sp.simplify(-sp.diff(F,Qs)))
print("   => p = m w q cot Q ; P = m w q^2/(2 sin^2 Q)  (consistent with the map above)")

print("\n== 3. the flow is a canonical transformation with generating function -S (LL end of §45): oscillator m=w=1")
def S(qt,q0,T): return (np.cos(T)*(qt**2+q0**2)-2*qt*q0)/(2*np.sin(T))
q0,p0,T=0.8,0.5,1.1
qt=q0*np.cos(T)+p0*np.sin(T);pt=-q0*np.sin(T)+p0*np.cos(T)
h=1e-6;pt_from_S=(S(qt+h,q0,T)-S(qt-h,q0,T))/(2*h);p0_from_S=-(S(qt,q0+h,T)-S(qt,q0-h,T))/(2*h)
print("   true path: q_t=%.6f p_t=%.6f ; dS/dq_t = %.6f ; -dS/dq_0 = %.6f (p_0 = %.6f)"%(qt,pt,pt_from_S,p0_from_S,p0))
s=solve_ivp(lambda t,y:[y[1],-y[0]],[0,T],[q0,p0],rtol=1e-12,atol=1e-14,dense_output=True)
Sint=quad(lambda tt:0.5*s.sol(tt)[1]**2-0.5*s.sol(tt)[0]**2,0,T)[0]
print("   action integral of L along the true path = %.6f ; closed form S(q_t,q_0,T) = %.6f"%(Sint,S(qt,q0,T)))

print("\n== 4. invariance of the Poisson bracket (45.9): f=q^2 p, g=p^2+q  under the oscillator map, m=w=1")
f=q**2*p;g=p**2+q
Qm=sp.atan(q/p);Pm=(p**2+q**2)/2
b_old=PB(f,g,q,p)
# express f,g through Q,P:  q = sqrt(2P) sin Q ; p = sqrt(2P) cos Q
fq=(Pm**0)*0
f_new=(2*Ps)**sp.Rational(3,2)*sp.sin(Qs)**2*sp.cos(Qs);g_new=2*Ps*sp.cos(Qs)**2+sp.sqrt(2*Ps)*sp.sin(Qs)
b_new=sp.simplify(sp.diff(f_new,Ps)*sp.diff(g_new,Qs)-sp.diff(f_new,Qs)*sp.diff(g_new,Ps))
pt={q:sp.Rational(8,10),p:sp.Rational(1,2)}
Qv=float(sp.atan(0.8/0.5));Pv=float((0.25+0.64)/2)
print("   [f,g]_(p,q) at (0.8,0.5) = %.6f ; [f,g]_(P,Q) at the image point (Q=%.4f, P=%.4f) = %.6f"%(float(b_old.subs(pt)),Qv,Pv,float(b_new.subs({Qs:Qv,Ps:Pv}))))

print("\n== 5. Liouville: area of a blob under the exact nonlinear pendulum flow (RK4, dt=1e-3) vs coarse-grained area")
def flow(pts,T):
    out=pts.copy()
    def f(t,y):
        n=len(y)//2;return np.concatenate([y[n:],-np.sin(y[:n])])
    y0=np.concatenate([pts[:,0],pts[:,1]]);sol=solve_ivp(f,[0,T],y0,rtol=1e-11,atol=1e-12,max_step=0.01)
    n=len(pts);return np.stack([sol.y[:n,-1],sol.y[n:,-1]],1)
def area(b): x,y=b[:,0],b[:,1];return 0.5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))
th=np.linspace(0,2*np.pi,4000,endpoint=False);b0=np.stack([1.5+0.4*np.cos(th),0.3+0.4*np.sin(th)],1);A0=area(b0)
rng=np.random.default_rng(3);rr=np.sqrt(rng.random(4000))*0.4;aa=rng.random(4000)*2*np.pi;in0=np.stack([1.5+rr*np.cos(aa),0.3+rr*np.sin(aa)],1)
for T in (0,2,5,10,15):
    b=flow(b0,T) if T>0 else b0;pts=flow(in0,T) if T>0 else in0
    cells=len({(int(np.floor((x+8)/0.12)),int(np.floor((y+8)/0.12))) for x,y in pts})*0.12**2
    print("   t=%4.1f: boundary area = %.6f (initial %.6f, ratio %.6f) ; coarse-grained (0.12 cells) area = %.4f"%(T,area(b),A0,area(b)/A0,cells))
