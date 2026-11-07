"""ED01 numbers (electrostatics review). .venv/bin/python -W ignore scripts/ed01_numbers.py
G = Griffiths (SI), J = Jackson Ch.1-4 (SI)."""
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_legendre
np.set_printoptions(precision=6,suppress=True)
eps0=8.8541878128e-12;k=1/(4*np.pi*eps0);rng=np.random.default_rng(1)

print("== 1. Gauss + curl on a uniformly charged ball (G Ex. 2.3): E_out = q/(4 pi eps0 r^2), E_in = q r/(4 pi eps0 R^3)")
R=0.1;q=1e-9;rho=q/(4/3*np.pi*R**3)
def E(x):
    r=np.linalg.norm(x);return k*q*x/R**3 if r<R else k*q*x/r**3
def div(x,h=1e-6): return sum((E(x+h*np.eye(3)[i])[i]-E(x-h*np.eye(3)[i])[i])/(2*h) for i in range(3))
def curl(x,h=1e-6):
    J=np.array([[(E(x+h*np.eye(3)[j])[i]-E(x-h*np.eye(3)[j])[i])/(2*h) for j in range(3)] for i in range(3)])
    return np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]])
for xx in (np.array([0.03,0.02,-0.01]),np.array([0.2,-0.1,0.15])):
    print("   at r=%.3f m: div E = %.6e V/m^2 ; rho/eps0 inside / 0 outside = %.6e ; |curl E| = %.2e"%(np.linalg.norm(xx),div(xx),(rho/eps0 if np.linalg.norm(xx)<R else 0.0),np.linalg.norm(curl(xx))))
print("   flux through spheres: r=0.05: %.6e ; r=0.2: %.6e ; q/eps0 = %.6e ; (r/R)^3 q/eps0 at 0.05 = %.6e"%(4*np.pi*0.05**2*np.linalg.norm(E(np.array([0.05,0,0]))),4*np.pi*0.2**2*np.linalg.norm(E(np.array([0.2,0,0]))),q/eps0,(0.05/R)**3*q/eps0))

print("\n== 2. electrostatic energy (G 2.42, 2.43, 2.45, Example 2.9, Problem 2.34 as asked; J 1.47-1.53)")
Wshell=q**2/(8*np.pi*eps0*R)
Wfield_shell=eps0/2*(quad(lambda r:(k*q/r**2)**2*4*np.pi*r*r,R,np.inf)[0])
Wsurf=0.5*(q/(4*np.pi*R**2))*(k*q/R)*4*np.pi*R**2
print("   shell: (1/2) sigma V A = %.6e J ; (eps0/2) int E^2 = %.6e J ; q^2/(8 pi eps0 R) = %.6e J"%(Wsurf,Wfield_shell,Wshell))
Vball=lambda r:k*q/(2*R)*(3-(r/R)**2)
Wrho=0.5*quad(lambda r:rho*Vball(r)*4*np.pi*r*r,0,R)[0]
Wfield=eps0/2*(quad(lambda r:(k*q*r/R**3)**2*4*np.pi*r*r,0,R)[0]+quad(lambda r:(k*q/r**2)**2*4*np.pi*r*r,R,np.inf)[0])
Wsnow=quad(lambda r:k*(rho*4/3*np.pi*r**3)*(rho*4*np.pi*r*r)/r,0,R)[0]
print("   uniform ball: (1/2)int rho V = %.6e ; (eps0/2) int E^2 = %.6e ; snowball = %.6e ; 3 q^2/(20 pi eps0 R) = %.6e J"%(Wrho,Wfield,Wsnow,3*q**2/(20*np.pi*eps0*R)))
a=0.2;Ws=eps0/2*quad(lambda r:(k*q*r/R**3)**2*4*np.pi*r*r,0,R)[0]+eps0/2*quad(lambda r:(k*q/r**2)**2*4*np.pi*r*r,R,a)[0]
Ssurf=0.5*eps0*(k*q/a**2*4*np.pi*a**2*0+0)
print("   energy inside the ball = %.4f of the total ; outside r > R = %.4f of the total"%(eps0/2*quad(lambda r:(k*q*r/R**3)**2*4*np.pi*r*r,0,R)[0]/Wfield,1-eps0/2*quad(lambda r:(k*q*r/R**3)**2*4*np.pi*r*r,0,R)[0]/Wfield))
print("   two opposite point charges at distance d=1 cm: pair energy (2.42) = %.6e J (negative); field energy of the pair excludes self-energies"%(-k*q*q/0.01))
print("   a pressure check, G 2.52: P = eps0 E^2/2 at the surface of a conducting sphere with sigma=q/(4 pi R^2): P = %.6e Pa ; sigma^2/(2 eps0) = %.6e Pa"%(eps0/2*(k*q/R**2)**2,(q/(4*np.pi*R**2))**2/(2*eps0)))

print("\n== 3. method of images")
qq=1e-9;d=0.05
sig=lambda rr:-qq*d/(2*np.pi*(rr*rr+d*d)**1.5)
Qind=quad(lambda rr:sig(rr)*2*np.pi*rr,0,np.inf)[0];print("   plane: induced charge (G 3.11) = %.6e (= -q = %.6e) ; sigma(0) = %.6e C/m^2 ; force = -q^2/(16 pi eps0 d^2) = %.6e N"%(Qind,-qq,sig(0.0),-k*qq*qq/(2*d)**2))
Vplane=lambda x,y,z:k*qq*(1/np.sqrt(x*x+y*y+(z-d)**2)-1/np.sqrt(x*x+y*y+(z+d)**2))
print("   max |V| on z=0 for 5 random points: %.2e ; field normal at (0,0,0): E_z = %.6e V/m = sigma/eps0 = %.6e V/m (sign: field points into the conductor)"%(max(abs(Vplane(*(rng.normal(size=2)*0.1),0.0)) for _ in range(5)) if False else max(abs(Vplane(rng.normal()*0.1,rng.normal()*0.1,0.0)) for _ in range(5)),-2*k*qq*d/d**3*0+(-2*k*qq/d**2),sig(0.0)/eps0))
# sphere: J (2.4): q' = -a q / y, y' = a^2/y
asph=0.1;y=0.25;qimg=-asph/y*qq;yimg=asph**2/y
def Vs(x):
    return k*qq/np.linalg.norm(x-np.array([0,0,y]))+k*qimg/np.linalg.norm(x-np.array([0,0,yimg]))
pts=[asph*v/np.linalg.norm(v) for v in rng.normal(size=(6,3))]
print("   grounded sphere a=0.1, charge at y=0.25: q' = %.4e C, y' = %.5f m ; max |V| on 6 random surface points = %.2e V (scale k q/a = %.1f V)"%(qimg,yimg,max(abs(Vs(p)) for p in pts),k*qq/asph))
Fs=k*qq*qimg/(y-yimg)**2;print("   force on q = %.6e N (attractive) ; induced total charge = q' = %.4e ; as y -> infinity q' -> 0 like a/y"%(Fs,qimg))
def Er_out(t):
    p=asph*np.array([np.sin(t),0,np.cos(t)]);h=1e-7;n=p/asph
    return -(Vs(p+h*n)-Vs(p-h*n))/(2*h)
sig_s=lambda t:eps0*Er_out(t)
Qs=quad(lambda t:sig_s(t)*2*np.pi*asph**2*np.sin(t),0,np.pi,limit=200)[0];print("   integral of eps0 E_r over the sphere surface = %.6e C ; q' = %.6e C"%(Qs,qimg))

print("\n== 4. multipole expansion (G 3.94-3.101, J 4.1-4.13)")
print("   generating function: sum_{n<=N} (r'/r)^n P_n(cos alpha) vs 1/sqrt(1 + s^2 - 2 s cos alpha), s = 0.3, alpha = 40 deg")
s_=0.3;al=np.radians(40);ex=1/np.sqrt(1+s_*s_-2*s_*np.cos(al))
for N in (0,1,2,4,8):
    ser=sum(s_**n*eval_legendre(n,np.cos(al)) for n in range(N+1));print("      N=%d: series %.8f exact %.8f  error %.2e  (s^{N+1} = %.2e)"%(N,ser,ex,abs(ser-ex),s_**(N+1)))
print("   physical dipole +-q at z = +-d/2, d = 1 cm: relative error of the pure-dipole potential on the axis and at 60 degrees (G Ex 3.10):")
dd=0.01
def Vphys(r,t):
    p=np.array([r*np.sin(t),0,r*np.cos(t)]);return k*qq*(1/np.linalg.norm(p-np.array([0,0,dd/2]))-1/np.linalg.norm(p+np.array([0,0,dd/2])))
for rd in (3,10,30,100):
    r=rd*dd;t=np.radians(60);Vd=k*qq*dd*np.cos(t)/r**2;print("      r/d = %3d: V_phys = %.6e, V_dip = %.6e, rel. error = %.3e (octopole/dipole ~ (d/r)^2 *1/4 = %.3e)"%(rd,Vphys(r,t),Vd,abs(Vphys(r,t)-Vd)/abs(Vphys(r,t)),0.25/rd**2))
print("   linear quadrupole +q at z=+-a, -2q at 0: V on the z axis vs the l = 2 term k q a^2 *2 / z^3 [G 3.96 with cos^2 -> P2]:")
aa=0.02
for zr in (4,10,30):
    z=zr*aa;Vex=k*qq*(1/(z-aa)+1/(z+aa)-2/z);Vq=k*qq*2*aa**2/z**3;print("      z/a = %2d: exact %.6e  quadrupole term %.6e  rel err %.2e"%(zr,Vex,Vq,abs(Vex-Vq)/abs(Vex)))
print("   traceless Q_ij of the linear quadrupole (J 4.9): Q_zz = %.3e, Q_xx = Q_yy = %.3e (sum = %.1e)"%(sum(qi*(3*zi*zi-zi*zi) for qi,zi in ((qq,aa),(qq,-aa),(-2*qq,0))),-0.5*sum(qi*(3*zi*zi-zi*zi) for qi,zi in ((qq,aa),(qq,-aa),(-2*qq,0))),0.0))

print("\n== 5. dielectrics")
print("   dielectric sphere in a uniform field: solve J(4.48)-(4.55)/G(4.43)-(4.49) boundary conditions by a truncated Legendre series")
def sphere_field(er,L=6,Rr=1.0,E0=1.0):
    # unknowns A_l (inside, r^l), B_l (outside, r^-(l+1)); V_out = -E0 r cos + sum B_l r^-(l+1) P_l
    # conditions at r=R: continuity of V and of eps dV/dr for each l: build the linear system for l = 0..L
    sol={}
    for l in range(L+1):
        # unknowns (A,B): A R^l - B R^-(l+1) = -E0 R delta_{l1} ; er l A R^{l-1} + (l+1) B R^-(l+2) = -E0 delta_{l1}
        M=np.array([[Rr**l,-Rr**(-(l+1))],[er*l*Rr**(l-1) if l>0 else 0.0,(l+1)*Rr**(-(l+2))]]);b=np.array([-E0*Rr*(l==1),-E0*(l==1)])
        sol[l]=np.linalg.solve(M,b)
    return sol
for er in (2.0,5.0,80.0):
    A1=sphere_field(er)[1][0];Ein=-A1;print("      eps_r=%5.1f: E_in/E0 = %.8f ; 3/(eps_r+2) = %.8f ; all l != 1 coefficients zero: %s"%(er,Ein,3/(er+2),all(np.allclose(sphere_field(er)[l],0) for l in (0,2,3,4,5,6))))
print("   half-space dielectric (G 4.8, J 4.4): z>0 vacuum with charge q at (0,0,d), z<0 dielectric eps_r; image q' = -(eps_r-1)/(eps_r+1) q = -chi/(chi+2) q (G 4.51)")
for er in (2.0,5.0):
    chi=er-1;qi=-(er-1)/(er+1)*qq;qb=-chi/(chi+2)*qq
    # check continuity of V and D_z at random interface points (rho,0)
    errV=0;errD=0
    for _ in range(5):
        rr=rng.uniform(0.01,0.2);R1=np.hypot(rr,d)
        V_above=k*qq/R1+k*qi/R1;V_below=k*(qq+qi)/(er*R1) if False else k*(2*er/(er+1)*qq/er)/R1 if False else None
        qpp=2*er/(er+1)*qq
        Vb=k*qpp/(er*R1)         # potential below = q''/(4 pi eps R) with eps = er eps0
        Va=k*(qq+qi)/R1
        # D_z above: eps0 E_z, E_z = k[q (-(d))/(R^3)... evaluated at z=0: field of q at (0,0,d): E_z = -k q d / R^3 ... plus image at (0,0,-d): +k q' d / R^3 wait for z=0, image at -d: E_z from image = k q' (0-(-d))/R^3 = k q' d/R^3
        Dz_above=eps0*(-k*qq*d/R1**3+k*qi*d/R1**3)
        Dz_below=er*eps0*(-k*qpp/er*d/R1**3*(1)) if False else er*eps0*(k*(qpp/er)*(-d)/R1**3)
        errV=max(errV,abs(Va-Vb)/abs(Va));errD=max(errD,abs(Dz_above-Dz_below)/abs(Dz_above))
    sb=lambda rr:-1/(2*np.pi)*chi/(chi+2)*qq*d/(rr*rr+d*d)**1.5
    Qb=quad(lambda rr:sb(rr)*2*np.pi*rr,0,np.inf)[0]
    F=-k*chi/(chi+2)*qq*qq/(2*d)**2
    print("      eps_r=%.0f: q' = %.4e (G 4.51: -chi/(chi+2) q); surface bound charge integral = %.4e ; max rel mismatch of V and D_z at the interface: %.1e, %.1e ; force on q = %.4e N"%(er,qi,Qb,errV,errD,F))
print("   capacitor: C = eps_r C0, and (1/2) int D.E = Q^2/2C (G 4.37, 4.55-4.58): A = 1 cm^2, d = 1 mm, eps_r = 4, Q = 1 nC")
A=1e-4;dc=1e-3;er=4.0;Q=1e-9;C0=eps0*A/dc;C=er*C0;Dfield=Q/A;Efield=Dfield/(er*eps0);W=0.5*Dfield*Efield*A*dc
print("      C0 = %.4e F, C = %.4e F ; W = (1/2) int D.E = %.6e J ; Q^2/2C = %.6e J ; vacuum Q^2/2C0 = %.6e J"%(C0,C,W,Q*Q/(2*C),Q*Q/(2*C0)))

print("\n== 6. uniqueness: Jacobi relaxation of Laplace's equation on a square, three different starting guesses, V0 on the top side")
def relax(init,N=41,iters=6000):
    V=init.copy();V[0,:]=0;V[-1,:]=0;V[:,0]=0;V[:,-1]=0;V[-1,:]=1.0;V[0,:]=0   # top row index -1 is y = a
    V[-1,0]=V[-1,-1]=0.5
    hist=[]
    for it in range(iters):
        W=V.copy();W[1:-1,1:-1]=0.25*(V[2:,1:-1]+V[:-2,1:-1]+V[1:-1,2:]+V[1:-1,:-2]);V=W
        if it in (10,100,1000,5999): hist.append((it,V[N//2,N//2]))
    return V,hist
N=41
res=[relax(np.zeros((N,N))),relax(rng.uniform(-5,5,(N,N))),relax(np.full((N,N),3.0))]
for i,(V,h) in enumerate(res):print("   start %d: V(center) at iterations 10/100/1000/6000 = %s"%(i,[round(float(v),5) for _,v in h]))
print("   max difference between the three converged solutions: %.2e ; exact V(center)=V0/4 (symmetry) = 0.25"%max(np.abs(res[0][0]-res[1][0]).max(),np.abs(res[0][0]-res[2][0]).max()))
ser=lambda x,y,n=801:sum(4/(m*np.pi)*np.sin(m*np.pi*x)*np.exp(m*np.pi*(y-1))*(1-np.exp(-2*m*np.pi*y))/(1-np.exp(-2*m*np.pi)) for m in range(1,n,2))   # = sinh(m pi y)/sinh(m pi), overflow-safe
print("   Fourier series (separation of variables, G 3.3.1) V(0.5,0.5) = %.8f ; at (0.5,0.25) = %.6f vs relaxation %.6f"%(ser(0.5,0.5),ser(0.5,0.25),res[0][0][N//4,N//2]))

print("\n== 7. numbers for the problems")
print("   P: field of a ball at its surface for q=1 nC, R=10 cm: E = %.1f V/m ; potential at the surface %.1f V ; at the centre %.1f V (= 3/2 of the surface value)"%(k*q/R**2,k*q/R,1.5*k*q/R))
print("   P: capacitor energy E=Q^2/2C, A=1 cm^2,d=1 mm: C0=%.4e F"%(eps0*1e-4/1e-3))
print("   P: Debye-like: potential energy of hydrogen-like pair in eV: k e^2/a0 = %.3f eV"%(k*(1.602176634e-19)**2/5.29177e-11/1.602176634e-19))
print("   P: water sphere eps_r=80 in field E0=1e5 V/m: inside field %.4e V/m (fraction %.4f); bound surface charge density at the pole sigma_b = 3 eps0 (eps_r-1)/(eps_r+2) E0 = %.4e C/m^2"%(3*1e5/82,3/82,3*eps0*79/82*1e5))
print("   P: dielectric slab image force, eps_r=4: F/F_conductor-plane = %.4f (= (eps_r-1)/(eps_r+1))"%(3/5))
