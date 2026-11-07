"""ED02 numbers (magnetostatics review). .venv/bin/python -W ignore scripts/ed02_numbers.py
G = Griffiths Ch.5-6 (SI), J = Jackson Ch.5 (SI)."""
import numpy as np
from scipy.special import ellipk,ellipe
from scipy.integrate import quad,solve_ivp
np.set_printoptions(precision=6,suppress=True)
mu0=4e-7*np.pi;qe=1.602176634e-19;mp=1.67262192e-27

def biot_loop(P,a=1.0,z0=0.0,I=1.0,n=4000,sign=1):
    """numerical Biot-Savart of a circular loop radius a at height z0 in the xy plane, at point P (3,)."""
    t=(np.arange(n)+0.5)*2*np.pi/n;dt=2*np.pi/n
    src=np.stack([a*np.cos(t),a*np.sin(t),np.full(n,z0)],1);dl=np.stack([-a*np.sin(t),a*np.cos(t),np.zeros(n)],1)*dt*sign
    R=P-src;r=np.linalg.norm(R,axis=1)
    return mu0*I/(4*np.pi)*np.sum(np.cross(dl,R)/r[:,None]**3,axis=0)
def loop_exact(rho,z,a=1.0,I=1.0):
    """B_rho,B_z of a loop via elliptic integrals (the formula used by the interactive tool)."""
    k2=4*a*rho/((a+rho)**2+z**2);K=ellipk(k2);E=ellipe(k2);s=np.sqrt((a+rho)**2+z**2);d=(a-rho)**2+z**2
    Bz=mu0*I/(2*np.pi)/s*(K+(a*a-rho*rho-z*z)/d*E)
    Br=mu0*I/(2*np.pi)*z/(rho*s)*(-K+(a*a+rho*rho+z*z)/d*E) if rho>1e-9 else 0.0
    return Br,Bz

print("== 1. circular loop: numerical Biot-Savart (G 5.34, J 5.4) vs axis formula (G 5.41) and the elliptic-integral form used by the tool")
for z in (0.0,0.5,1.0,2.0):
    B=biot_loop(np.array([0,0,z]));ax=mu0*1/(2)*1/(1+z*z)**1.5;print("   on axis z=%.1f a: numerical Bz = %.8e T ; mu0 I a^2/(2(a^2+z^2)^{3/2}) = %.8e T"%(z,B[2],ax))
P=np.array([0.6,0,0.4]);Bn=biot_loop(P);Br,Bz=loop_exact(0.6,0.4);print("   off axis (rho=0.6 a, z=0.4 a): numerical (Bx,Bz) = (%.8e, %.8e) ; elliptic formula (B_rho,B_z) = (%.8e, %.8e)"%(Bn[0],Bn[2],Br,Bz))
print("   centre: B = mu0 I/(2a) = %.6e T (J: 'for r << a ... mu0 I/2a in the z direction')"%(mu0/2))

print("\n== 2. straight wire and force between wires (G 5.37-5.40, J 5.11)")
s=0.05;I=10.0
for L in (1.0,10.0,100.0,1000.0):
    th=np.arctan(L/2/s);B=mu0*I/(4*np.pi*s)*(np.sin(th)+np.sin(th));print("   finite wire of length %6.0f m at s=5 cm: B = mu0 I/(4 pi s)(sin th1 + sin th2) = %.6e T ; infinite wire mu0 I/(2 pi s) = %.6e T"%(L,B,mu0*I/(2*np.pi*s)))
print("   force per unit length between two 1 A wires 1 m apart: mu0 I1 I2/(2 pi d) = %.6e N/m (J 5.11, G 5.40)"%(mu0/(2*np.pi)))

print("\n== 3. div B = 0 and curl B = mu0 J for a cylinder with uniform current (G 5.46, 5.50, 5.56; J 5.17, 5.22)")
Rc=0.02;I=5.0;Jz=I/(np.pi*Rc**2)
def Bcyl(x):
    s_=np.hypot(x[0],x[1]);ph=np.array([-x[1],x[0],0])/s_
    return (mu0*I*s_/(2*np.pi*Rc**2) if s_<Rc else mu0*I/(2*np.pi*s_))*ph
def curlz(x,h=1e-7):
    dBy_dx=(Bcyl(x+np.array([h,0,0]))[1]-Bcyl(x-np.array([h,0,0]))[1])/(2*h);dBx_dy=(Bcyl(x+np.array([0,h,0]))[0]-Bcyl(x-np.array([0,h,0]))[0])/(2*h);return dBy_dx-dBx_dy
def divB(x,h=1e-7): return sum((Bcyl(x+h*np.eye(3)[i])[i]-Bcyl(x-h*np.eye(3)[i])[i])/(2*h) for i in range(3))
for xx in (np.array([0.007,0.004,0.0]),np.array([0.03,0.02,0.0])):
    print("   r=%.4f m: (curl B)_z = %.6e A/m^2 ; mu0 J_z (inside) / 0 (outside) = %.6e ; div B = %.2e"%(np.hypot(xx[0],xx[1]),curlz(xx),mu0*Jz if np.hypot(xx[0],xx[1])<Rc else 0.0,divB(xx)))
print("   Ampere loop: B(s=3 cm)*2 pi s = %.6e = mu0 I = %.6e (T m)"%(mu0*I/(2*np.pi*0.03)*2*np.pi*0.03,mu0*I))

print("\n== 4. solenoid: finite solenoid on its axis by summing loops (G 5.59, J 5.5-5.6 spirit); infinite solenoid vector potential (G 5.72, 5.73)")
a=0.02;n=2000.0;I=1.0
for Lr in (1,5,20,100):
    L=Lr*a;N=4001;zs=np.linspace(-L/2,L/2,N);dz=zs[1]-zs[0]
    Bc=sum(mu0*(n*I*dz)*a*a/(2*(a*a+z*z)**1.5) for z in zs)
    print("   L/a = %3d: B(centre) = %.6e T ; mu0 n I L/(2 sqrt((L/2)^2+a^2)) = %.6e ; infinite limit mu0 n I = %.6e T"%(Lr,Bc,mu0*n*I*L/(2*np.sqrt((L/2)**2+a*a)),mu0*n*I))
Rs=0.03;nI=mu0*n*I
def Asol(x):
    s_=np.hypot(x[0],x[1]);ph=np.array([-x[1],x[0],0])/s_
    return (nI/2*s_ if s_<Rs else nI*Rs**2/(2*s_))*ph
def curlA(x,h=1e-7):
    f=lambda y:Asol(y);J=np.array([[(f(x+h*np.eye(3)[j])[i]-f(x-h*np.eye(3)[j])[i])/(2*h) for j in range(3)] for i in range(3)]);return np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]])
print("   B=curl A inside (s=1.5 cm): %s ; mu0 n I = %.6e T ; outside (s=5 cm): %s"%(curlA(np.array([0.015,0.0,0.0])),nI,curlA(np.array([0.05,0.0,0.0]))))
print("   oint A.dl around s=5 cm = %.6e T m^2 ; flux B pi R^2 = %.6e T m^2 (G 5.71)"%(2*np.pi*0.05*np.linalg.norm(Asol(np.array([0.05,0,0]))),nI*np.pi*Rs**2))

print("\n== 5. magnetic dipole: loop field vs dipole formula (G 5.85-5.89, J 5.55-5.56); loop a = 1, I = 1 so m = pi")
m=np.pi
for rr in (3,10,30):
    th=np.radians(60);P=rr*np.array([np.sin(th),0,np.cos(th)]);B=biot_loop(P);r=np.linalg.norm(P);nn=P/r;Bd=mu0/(4*np.pi*r**3)*(3*nn*(np.array([0,0,m])@nn)-np.array([0,0,m]))
    print("   r/a = %2d, theta = 60 deg: |B_loop| = %.6e T ; |B_dipole| = %.6e T ; relative difference of the vectors = %.3e  (compare (a/r)^2 = %.3e)"%(rr,np.linalg.norm(B),np.linalg.norm(Bd),np.linalg.norm(B-Bd)/np.linalg.norm(B),1/rr**2))
print("   m is independent of the origin (G 5.86): shifting the origin changes the loop's m = I a only through the vector area: 0 (a closed loop has zero net displacement)")

print("\n== 6. uniformly magnetized sphere (G 6.16, J 5.105-5.107): bound surface current K_b = M x n = M sin(theta) phi-hat")
M=1.0e5;Rs2=0.05
# B at centre from rings: each ring at polar angle t: radius R sin t, height R cos t, current dI = M sin t * R dt
ts=np.linspace(0,np.pi,20001);dts=ts[1]-ts[0]
Bc=sum(mu0*(M*np.sin(t)*Rs2*dts)*(Rs2*np.sin(t))**2/(2*(Rs2**3)) for t in ts)   # axis field at the centre of a ring: mu0 I rho^2/(2 R^3) with R the distance to the ring = Rs2
print("   B(centre) = %.8e T ; (2/3) mu0 M = %.8e T ; H(centre) = B/mu0 - M = %.6e A/m ; -M/3 = %.6e A/m"%(Bc,2/3*mu0*M,Bc/mu0-M,-M/3))
mm=4/3*np.pi*Rs2**3*M;z=0.2
Bring=0.0
for t in np.linspace(0,np.pi,4001)[:-1]+np.pi/8002:
    Bring+=biot_loop(np.array([0,0,z]),a=Rs2*np.sin(t),z0=Rs2*np.cos(t),I=M*np.sin(t)*Rs2*(np.pi/4000),n=400)[2]
print("   on the axis at z = 0.2 m: summed rings %.8e T ; dipole mu0 m/(2 pi z^3) with m = (4/3) pi R^3 M: %.8e T (the field outside is exactly a dipole: no higher multipoles)"%(Bring,mu0*mm/(2*np.pi*z**3)))

print("\n== 7. magnetic matter (G 6.13, 6.14, 6.19, 6.29-6.33, J 5.79-5.84): solenoid filled with a linear medium")
for chi in (-1e-5,2e-4,1000.0):
    mur=1+chi;H=n*I;Bm=mu0*mur*H;Mm=chi*H;print("   chi_m = %9.1e: H = n I = %.1f A/m ; M = chi H = %.4e A/m ; B = mu0(1+chi)H = %.6e T ; K_b = M = %.4e A/m ; bound/free surface current = chi = %.1e"%(chi,H,Mm,Bm,Mm,chi))

print("\n== 8. Lorentz force: no work, cycloid and E x B drift (G 5.1-5.11); proton with E = 1e5 V/m, B = 1 T")
E=1e5;B=1.0;om=qe*B/mp
f=lambda t,y:[y[3],y[4],y[5],(qe/mp)*(0+y[4]*B-y[5]*0),(qe/mp)*(E-y[3]*B),0.0]
# fields: E along y, B along z?  use G: B along x, E along z, motion in the yz plane: z'' = om (E/B - y'), y'' = om z'
def rhs(t,y):
    yy,zz,vy,vz=y;return [vy,vz,om*vz,om*(E/B-vy)]
T=2*np.pi/om;sol=solve_ivp(rhs,[0,20*T],[0,0,0,0],rtol=1e-11,atol=1e-12)
yy,zz,vy,vz=sol.y
print("   omega = %.5e rad/s, period %.4e s, R = E/(omega B) = %.4e m ; drift speed E/B = %.4e m/s ; y(20T)/(20T) = %.6e m/s"%(om,T,E/(om*B),E/B,yy[-1]/(20*T)))
KE=0.5*mp*(sol.y[2]**2+sol.y[3]**2);W=qe*E*sol.y[1]
print("   energy balance over the whole run: max |KE - q E z| / max KE = %.2e (the magnetic force does no work: G 5.11)"%(np.max(np.abs(KE-W))/np.max(KE)))

print("\n== 9. Helmholtz and anti-Helmholtz pairs (tool configurations): d = a gives zero second derivative at the centre")
def Bz_pair(z,d,sign=1,a=1.0): return mu0*(a*a/(2*(a*a+(z-d/2)**2)**1.5)+sign*a*a/(2*(a*a+(z+d/2)**2)**1.5))
h=1e-3
for d in (0.5,1.0,1.5):
    d2=(Bz_pair(h,d)-2*Bz_pair(0,d)+Bz_pair(-h,d))/h**2;print("   d/a = %.1f: B(0) = %.6e T (mu0 I/a units %.5f) ; d2B/dz2 at the centre = %.3e"%(d,Bz_pair(0,d),Bz_pair(0,d)/mu0,d2))
print("   Helmholtz centre field (4/5)^{3/2} mu0 I / a = %.6e T"%((4/5)**1.5*mu0))
