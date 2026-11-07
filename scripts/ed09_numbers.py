"""ED09 numbers (retarded potentials, Lienard-Wiechert). .venv/bin/python -W ignore scripts/ed09_numbers.py
SI with c = 1 and q/(4 pi eps0) = 1 unless stated.  G = Griffiths (equation numbers 10.x), J = Jackson."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
np.set_printoptions(precision=6,suppress=True)

print("== 1. G Example 10.2: infinite wire, current I0 switched on at t=0 (mu0 = c = 1, I0 = 1)")
def A_ret(s,t):   # A_z = (1/4pi) int I(t_r)/r dz with r = sqrt(s^2+z^2), t_r = t - r ; only |z| <= sqrt(t^2-s^2)
    if t<=s: return 0.0
    zm=np.sqrt(t*t-s*s);return 1/(4*np.pi)*2*quad(lambda z:1/np.sqrt(s*s+z*z),0,zm)[0]
def A_closed(s,t): return 0.0 if t<=s else (1/(2*np.pi))*np.log((t+np.sqrt(t*t-s*s))/s)
s0,t0=1.0,2.0
print("   A at s=1,t=2: quadrature %.8f ; closed form (mu0 I0/2pi) ln[(ct+sqrt((ct)^2-s^2))/s] = %.8f"%(A_ret(s0,t0),A_closed(s0,t0)))
h=1e-5
E_num=-(A_closed(s0,t0+h)-A_closed(s0,t0-h))/(2*h);E_formula=-(1/(2*np.pi))*1/np.sqrt(t0*t0-s0*s0)
B_num=-(A_closed(s0+h,t0)-A_closed(s0-h,t0))/(2*h);B_formula=(1/(2*np.pi*s0))*t0/np.sqrt(t0*t0-s0*s0)
print("   E_z = -dA/dt: numeric %.8f ; formula -(mu0 I0 c/2pi)/sqrt((ct)^2-s^2) = %.8f"%(E_num,E_formula))
print("   B_phi = -dA_z/ds: numeric %.8f ; formula (mu0 I0/2 pi s) ct/sqrt((ct)^2-s^2) = %.8f ; static value %.8f"%(B_num,B_formula,1/(2*np.pi*s0)))
for t in (1.01,1.5,3,10,100): print("     t=%6.2f: B/B_static = %.6f , |E|/(mu0 I0 c/2pi s) = %.6f"%(t,t/np.sqrt(t*t-1),1/np.sqrt(t*t-1)))

print("\n== 2. LW potentials of a charge in uniform motion w(t) = v t x_hat  (G 10.46, 10.49, 10.51)")
v=0.6;rpt=np.array([0.7,1.1,0.4]);t=2.0
w=lambda tt:np.array([v*tt,0,0]);vel=lambda tt:np.array([v,0,0])
tr=brentq(lambda x:np.linalg.norm(rpt-w(x))-(t-x),-50,t-1e-9)
r_vec=rpt-w(tr);r=np.linalg.norm(r_vec);Vlw=1/(r-r_vec@vel(tr))
root=np.sqrt((t-rpt@vel(0))**2+(1-v*v)*(rpt@rpt-t*t))
V1049=1/root
R=rpt-w(t);cosθ=(R@np.array([1,0,0]))/np.linalg.norm(R);sin2=1-cosθ**2
V1051=1/(np.linalg.norm(R)*np.sqrt(1-v*v*sin2))
print("   t_r = %.8f ; V (10.46) = %.8f ; V (10.49) = %.8f ; V (10.51) = %.8f"%(tr,Vlw,V1049,V1051))
Eq=lambda r_,t_:None

print("\n== 3. field of a uniformly moving charge: (10.72) at the retarded point vs (10.75) from the present position")
u=r_vec/r-vel(tr);Efield=(1-v*v)*u*r/(r_vec@u*0+ (r_vec@u))**1   # placeholder replaced below
def E_G(r_vec,u,v_,a_):
    r=np.linalg.norm(r_vec);return r/ (r_vec@u)**3*((1-v_@v_)*u+np.cross(r_vec,np.cross(u,a_))/1.0)
uvec=(r_vec/r)-vel(tr)   # u = c r_hat - v with c=1
E1072=(r/(r_vec@uvec)**3)*(((1-v*v))*uvec+np.cross(r_vec,np.cross(uvec,np.zeros(3))))
Rn=np.linalg.norm(R);E1075=(1-v*v)/(1-v*v*sin2)**1.5*R/Rn**3
print("   E (10.72, a=0) = %s ; E (10.75) = %s ; difference %.2e"%(E1072,E1075,np.linalg.norm(E1072-E1075)))
print("   direction check: E parallel to R (present position -> field point): |E x R|/|E||R| = %.2e"%(np.linalg.norm(np.cross(E1072,R))/np.linalg.norm(E1072)/Rn))
for b in (0.5,0.9,0.99):
    g=1/np.sqrt(1-b*b);print("   v/c=%.2f: E(theta=0)/E_static = %.4f (1-v^2/c^2) ; E(theta=90)/E_static = %.4f (1/sqrt(1-v^2/c^2)) ; gamma = %.4f"%(b,1-b*b,g,g))

print("\n== 4. accelerated charge: circular motion radius a=1, omega=0.4 (v=0.4 c): check (10.72),(10.73) against -grad V - dA/dt, curl A (LW potentials, finite differences)")
om=0.4;a_=1.0
wc=lambda tt:a_*np.array([np.cos(om*tt),np.sin(om*tt),0.0]);vc=lambda tt:a_*om*np.array([-np.sin(om*tt),np.cos(om*tt),0.0]);ac=lambda tt:-a_*om*om*np.array([np.cos(om*tt),np.sin(om*tt),0.0])
def retarded(rpt,t): return brentq(lambda x:np.linalg.norm(rpt-wc(x))-(t-x),t-200,t-1e-12)
def VA(rpt,t):
    x=retarded(rpt,t);rv=rpt-wc(x);r=np.linalg.norm(rv);den=r-rv@vc(x);return 1/den,vc(x)/den
def fields(rpt,t):
    x=retarded(rpt,t);rv=rpt-wc(x);r=np.linalg.norm(rv);uu=rv/r-vc(x)
    E=(r/(rv@uu)**3)*((1-vc(x)@vc(x))*uu+np.cross(rv,np.cross(uu,ac(x))));B=np.cross(rv/r,E);return E,B
rpt=np.array([3.0,2.0,1.5]);t=5.0;h=1e-5
Vp=lambda p,tt:VA(p,tt)[0];Ap=lambda p,tt:VA(p,tt)[1]
gradV=np.array([(Vp(rpt+h*e,t)-Vp(rpt-h*e,t))/(2*h) for e in np.eye(3)]);dAdt=(Ap(rpt,t+h)-Ap(rpt,t-h))/(2*h)
E_num=-gradV-dAdt
J=np.array([(Ap(rpt+h*e,t)-Ap(rpt-h*e,t))/(2*h) for e in np.eye(3)])   # J[i,j] = d_i A_j
B_num=np.array([J[1,2]-J[2,1],J[2,0]-J[0,2],J[0,1]-J[1,0]])
E_f,B_f=fields(rpt,t)
print("   E numerical = %s ; E (10.72) = %s ; |diff| = %.2e"%(E_num,E_f,np.linalg.norm(E_num-E_f)))
print("   B numerical = %s ; B (10.73) = %s ; |diff| = %.2e"%(B_num,B_f,np.linalg.norm(B_num-B_f)))
divA=sum(J[i,i] for i in range(3));dVdt=(Vp(rpt,t+h)-Vp(rpt,t-h))/(2*h)
print("   Lorenz condition: div A + dV/dt = %.2e (should be 0, c=1)"%(divA+dVdt))
print("   B perpendicular to E: E.B = %.2e ; B = n x E magnitude check |B|/|E| = %.5f"%(E_f@B_f,np.linalg.norm(B_f)/np.linalg.norm(E_f)))

print("\n== 5. velocity field ~ 1/r^2 vs radiation field ~ 1/r: fixed retarded time t_r = 10 and direction n, distance r varied (field point = w(t_r) + r n, observed at t = t_r + r)")
def split(tr_,nvec,r):
    rv=r*nvec;uu=nvec-vc(tr_)
    Ev=(r/(rv@uu)**3)*((1-vc(tr_)@vc(tr_))*uu);Ea=(r/(rv@uu)**3)*np.cross(rv,np.cross(uu,ac(tr_)));return np.linalg.norm(Ev),np.linalg.norm(Ea)
d=np.array([0.3,0.9,0.3]);d/=np.linalg.norm(d)
for r in (1,2,5,10,20,50,100,1000):
    Ev,Ea=split(10.0,d,r);print("   r=%6g: |E_velocity|=%.4e  |E_accel|=%.4e  accel/velocity = %.4f  (|E_v| r^2 = %.5f, |E_a| r = %.5f)"%(r,Ev,Ea,Ea/Ev,Ev*r*r,Ea*r))
Ev1,Ea1=split(10.0,d,1.0);print("   crossover r* where the two are equal: r* = |E_v| r^2/(|E_a| r) = %.4f (in units a = 1, c = 1)"%(Ev1/Ea1))

print("\n== 6. long wire with I(t) = k t (t>0): exact retarded B vs quasi-static Biot-Savart mu0 I(t)/(2 pi s)  (mu0 = c = k = 1)")
def A_lin(s,t):
    if t<=s: return 0.0
    zm=np.sqrt(t*t-s*s);return 1/(4*np.pi)*2*quad(lambda z:(t-np.sqrt(s*s+z*z))/np.sqrt(s*s+z*z),0,zm)[0]
for ct in (1.2,2.0,5.0,20.0):
    s=1.0;h=1e-5;B_ex=-(A_lin(s+h,ct)-A_lin(s-h,ct))/(2*h);B_bs=ct/(2*np.pi*s)
    print("   ct/s = %5.1f: B_exact = %.7f ; B_BS = %.7f ; ratio = %.7f ; sqrt(1-(s/ct)^2) = %.7f"%(ct,B_ex,B_bs,B_ex/B_bs,np.sqrt(1-(s/ct)**2)))
