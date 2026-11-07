"""ED11 numbers (relativistic electrodynamics). .venv/bin/python -W ignore scripts/ed11_numbers.py
G = Griffiths Ch.12 (SI), J = Jackson Ch.11 (Gaussian)."""
import numpy as np, sympy as sp
from scipy.integrate import quad
np.set_printoptions(precision=6,suppress=True)
rng=np.random.default_rng(11)
mu0=4e-7*np.pi;c=2.99792458e8;eps0=1/(mu0*c*c)
gam=lambda b:1/np.sqrt(1-b*b)

print("== 1. G 12.3.1: magnetism from electrostatics + length contraction (wire with +-lambda moving at +-v, charge q at speed u)")
lam,v,u,s,q=2e-6,0.6*c,0.3*c,0.05,1e-9   # lambda in the frame S where the positive line moves at v
vp=(v-u)/(1-v*u/c**2); vm=(v+u)/(1+v*u/c**2)       # (12.77): v_+ and v_- ; v_pm = (v -+ u)/(1 -+ vu/c^2)
g=gam(v/c);gp=gam(vp/c);gm=gam(vm/c);lam0=lam/g
lamp=gp*lam0;lamm=-gm*lam0;lamtot=lamp+lamm
closed=-2*lam*u*v/(c**2*np.sqrt(1-u*u/c**2))
print("   lambda_tot (direct from gamma_pm) = %.6e C/m ; closed form (12.83) = %.6e C/m"%(lamtot,closed))
Fbar=q*lamtot/(2*np.pi*eps0*s);F=np.sqrt(1-u*u/c**2)*Fbar          # (12.84),(12.85)
I=2*lam*v;Fmag=-q*u*mu0*I/(2*np.pi*s)
print("   force in S: sqrt(1-u^2/c^2) * F_bar = %.6e N ; magnetic -q u mu0 I/(2 pi s) = %.6e N ; ratio = %.12f"%(F,Fmag,F/Fmag))
print("   gamma_pm check: gamma_pm = gamma_v gamma_u (1 -+ uv/c^2): %.9f vs %.9f ; %.9f vs %.9f"%(gp,g*gam(u/c)*(1-u*v/c**2),gm,g*gam(u/c)*(1+u*v/c**2)))

def Fmat(E,B):  # G (12.119), SI, with E/c
    E=np.asarray(E,float)/c;B=np.asarray(B,float)
    return np.array([[0,E[0],E[1],E[2]],[-E[0],0,B[2],-B[1]],[-E[1],-B[2],0,B[0]],[-E[2],B[1],-B[0],0]])
def boost(vec):
    vec=np.asarray(vec,float);b=np.linalg.norm(vec)/c;n=vec/np.linalg.norm(vec);g=gam(b);L=np.eye(4)
    L[0,0]=g;L[0,1:]=-g*b*n;L[1:,0]=-g*b*n;L[1:,1:]=np.eye(3)+(g-1)*np.outer(n,n);return L
def EB(F):
    return c*np.array([F[0,1],F[0,2],F[0,3]]),np.array([F[2,3],F[3,1],F[1,2]])
print("\n== 2. field transformation: tensor law F' = L F L^T vs G (12.109) [x boost] and J (11.149) [general boost]")
E=rng.normal(size=3)*1e5;B=rng.normal(size=3)*0.3;vx=0.55*c
L=boost([vx,0,0]);F2=L@Fmat(E,B)@L.T;E2,B2=EB(F2);b=vx/c;g=gam(b)
Eg=np.array([E[0],g*(E[1]-vx*B[2]),g*(E[2]+vx*B[1])]);Bg=np.array([B[0],g*(B[1]+vx/c**2*E[2]),g*(B[2]-vx/c**2*E[1])])
print("   x-boost: max|tensor - (12.109)| : E %.2e (relative), B %.2e (relative)"%(np.abs(E2-Eg).max()/np.abs(E).max(),np.abs(B2-Bg).max()/np.abs(B).max()))
vv=np.array([0.2,-0.3,0.4])*c;bb=vv/c;g=gam(np.linalg.norm(bb));L=boost(vv);F3=L@Fmat(E,B)@L.T;E3,B3=EB(F3)
# Jackson (11.149) in Gaussian with c=1: E' = g(E + b x B) - g^2/(g+1) b (b.E);  here SI: E' = g(E + v x B) - g^2/(g+1) b (b.E)
Ej=g*(E+np.cross(vv,B))-g*g/(g+1)*bb*np.dot(bb,E);Bj=g*(B-np.cross(vv,E)/c**2)-g*g/(g+1)*bb*np.dot(bb,B)
print("   general boost: max|tensor - (11.149)| : E %.2e, B %.2e (relative)"%(np.abs(E3-Ej).max()/np.abs(E).max(),np.abs(B3-Bj).max()/np.abs(B).max()))

print("\n== 3. invariants (G 12.47, 12.51; J 11.14)")
eta=np.diag([-1,1,1,1.0]);lower=lambda T:eta@T@eta
def dual(E,B):  # G (12.120)
    E=np.asarray(E)/c;return np.array([[0,B[0],B[1],B[2]],[-B[0],0,-E[2],E[1]],[-B[1],E[2],0,-E[0]],[-B[2],-E[1],E[0],0]])
for (Ea,Ba,lab) in ((E,B,'original'),(E3,B3,'boosted')):
    F=Fmat(Ea,Ba);Gd=dual(Ea,Ba);Fl=lower(F);Gl=lower(Gd)
    print("   %-9s F^{mu nu}F_{mu nu} = %.6e ; 2(B^2 - E^2/c^2) = %.6e ; G^{mu nu}G_{mu nu} = %.6e ; F^{mu nu}G_{mu nu} = %.6e ; -4 E.B/c = %.6e ; E.B = %.6e ; E^2-c^2B^2 = %.6e"%(lab,np.sum(F*Fl),2*(Ba@Ba-Ea@Ea/c**2),np.sum(Gd*Gl),np.sum(F*Gl),-4*Ea@Ba/c,Ea@Ba,Ea@Ea-c*c*Ba@Ba))

print("\n== 4. fields of a uniformly moving charge: boost the Coulomb field, compare G (12.93), J (11.152)-(11.154), and the retarded (Lienard-Wiechert) result of ED09")
q=1e-9;beta=0.8;v=beta*c;g=gam(beta);k=1/(4*np.pi*eps0)
b_,t=0.3,0.17e-9            # impact parameter (m) and lab time with the charge at x = v t at time t (J's geometry: observer at (0,b,0), charge passes x=0 at t=0)
xq=v*t
# observer at P=(0,b,0): R = P - charge position
R=np.array([-xq,b_,0.0]);Rm=np.linalg.norm(R);psi=np.arccos(np.dot(R,[1,0,0])/Rm)
# method A (G 12.93)
EA=k*q*(1-beta**2)/(1-beta**2*np.sin(psi)**2)**1.5/Rm**2*R/Rm
# method B (J 11.152): E1 = -q g v t/(b^2+g^2 v^2 t^2)^{3/2}, E2 = g q b/(...)^{3/2} (Gaussian -> times k for SI)
den=(b_**2+g**2*v**2*t**2)**1.5;EB_=k*q*np.array([-g*v*t/den,g*b_/den,0])
# method C: boost the rest-frame Coulomb field with the tensor, evaluated at the point (t', x') in the charge frame
tp=g*(t-v*0/c**2);xp=g*(0-v*t);rp=np.array([xp,b_,0]);Ep=k*q*rp/np.linalg.norm(rp)**3
L=boost([-v,0,0]);Fc=L@Fmat(Ep,np.zeros(3))@L.T;EC,BC=EB(Fc)   # lab frame sees the charge moving at +v => the boost from rest frame uses -v... test sign via B below
# method D: retarded LW velocity field: E = q/(4 pi eps0) (1-beta^2)/(R_ret^2 (1-n.beta)^3) (n - beta)  where n from retarded position
from scipy.optimize import brentq
P=np.array([0,b_,0.0]);tt=t
f=lambda tr:np.linalg.norm(P-np.array([v*tr,0,0]))-c*(tt-tr);tr=brentq(f,tt-1e-6,tt,xtol=1e-30,rtol=1e-15,maxiter=500)
Rr=P-np.array([v*tr,0,0]);Rrm=np.linalg.norm(Rr);n=Rr/Rrm;bv=np.array([beta,0,0])
ED=k*q*(1-beta**2)*(n-bv)/(Rrm**2*(1-n@bv)**3)
print("   E at P: (12.93) %s ; (11.152) %s ; boosted Coulomb field %s ; retarded LW %s  [V/m]"%(EA,EB_,EC,ED))
print("   max relative differences: A-B %.2e ; A-C %.2e ; A-D %.2e"%(np.abs(EA-EB_).max()/np.abs(EA).max(),np.abs(EA-EC).max()/np.abs(EA).max(),np.abs(EA-ED).max()/np.abs(EA).max()))
# B field: v x E / c^2 (G 12.112 first form) vs J B3 = beta E2 (Gaussian) -> SI: B3 = beta E2 / c
Bvec=np.cross([v,0,0],EA)/c**2;print("   B_z = (v x E)/c^2 = %.6e T ; beta E_2/c = %.6e T"%(Bvec[2],beta*EA[1]/c))
print("   pancake: E_parallel / E_Coulomb = 1/g^2 = %.6f ; E_perp / E_Coulomb = g = %.6f (g=%.4f)"%(1/g**2,g,g))
# check formula at psi=0 and pi/2
for ps in (0,np.pi/2):
    print("      psi=%.2f: (1-b^2)/(1-b^2 sin^2 psi)^{3/2} = %.6f"%(ps,(1-beta**2)/(1-beta**2*np.sin(ps)**2)**1.5))
# time integral invariance (J 11.153): integral of E_2 dt = 2 q/(b v) (Gaussian) for any gamma
for bt in (0.1,0.5,0.9,0.99,0.999):
    gg=gam(bt);vv_=bt*c;sc=b_/(gg*vv_)                           # integrate the literal E_2(t) with t = sc * x (sc = duration scale)
    I2=quad(lambda X_:gg*b_/(b_**2+gg**2*vv_**2*(sc*X_)**2)**1.5*sc,-np.inf,np.inf)[0]
    print("      beta=%.3f: gamma=%8.3f  peak E_2/E_2(beta=0) = %.3f (=gamma)  duration b/(g v)=%.3e s  b v int E_2 dt /q-units = %.9f (should be 2 for every beta)"%(bt,gg,gg,b_/(gg*vv_),I2*b_*vv_))

print("\n== 5. plane wave seen from a frame moving along the propagation direction (G Problem 12.48 asked; derived here)")
E0=100.0;w=2*np.pi*5e14
for bt in (0.1,0.5,0.9,0.99):
    g=gam(bt);Ebar=g*(E0-bt*c*E0/c);Bbar=g*(E0/c-bt*c/c**2*E0)  # E_y, B_z = E0/c
    fact=np.sqrt((1-bt)/(1+bt))
    print("   beta=%.2f: E_bar/E0 = %.6f ; sqrt((1-b)/(1+b)) = %.6f ; omega_bar/omega = %.6f ; intensity ratio = %.6f ; (1-b)/(1+b) = %.6f ; E_bar/(c B_bar) = %.6f"%(bt,Ebar/E0,fact,g*(1-bt),(Ebar/E0)**2,(1-bt)/(1+bt),Ebar/(c*Bbar)))

print("\n== 6. E x B drift: boost to the frame with E' = 0 (E perpendicular to B, E < cB); G (12.111)")
Ev=np.array([0,1e5,0]);Bv=np.array([0,0,1.0]);vd=np.cross(Ev,Bv)/(Bv@Bv)
L=boost(vd);F4=L@Fmat(Ev,Bv)@L.T;E4,B4=EB(F4)
print("   E=1e5 V/m, B=1 T: drift v = E x B / B^2 = %s m/s (beta = %.4e) ; E' = %s V/m ; |B'| = %.9f T ; sqrt(B^2 - E^2/c^2) = %.9f T"%(vd,np.linalg.norm(vd)/c,E4,np.linalg.norm(B4),np.sqrt(Bv@Bv-Ev@Ev/c**2)))
print("   a deterministic check of the guiding-centre claim: proton in these fields, RK integration of the Lorentz force, average velocity")
qm=1.602176634e-19/1.67262192e-27
def rhs(tt,y):
    vel=y[3:];return np.concatenate([vel,qm*(Ev+np.cross(vel,Bv))])
from scipy.integrate import solve_ivp
T=2*np.pi/(qm*1.0);sol=solve_ivp(rhs,[0,50*T],np.zeros(6),rtol=1e-11,atol=1e-9,dense_output=True)
print("   average velocity over 50 gyro-periods: %s m/s (nonrelativistic; E x B/B^2 = %s)"%((sol.y[:3,-1])/(50*T),vd))

print("\n== 7. covariant Lorentz force (G 12.128): K^mu = q F^{mu nu} eta_nu equals gamma q (E.u/c, E + u x B)")
E=rng.normal(size=3)*1e4;B=rng.normal(size=3)*0.2;uvec=rng.uniform(-0.4,0.4,3)*c;g=gam(np.linalg.norm(uvec)/c);qq=1.6e-19
eta_up=g*np.array([c,*uvec]);eta_dn=eta@eta_up;K=qq*Fmat(E,B)@eta_dn
Kexp=g*qq*np.array([E@uvec/c,*(E+np.cross(uvec,B))])
print("   K^mu/(gamma q) = %s ; expected (E.u/c, E+u x B) = %s ; max rel diff %.2e"%(K/(g*qq),Kexp/(g*qq),np.abs(K-Kexp).max()/np.abs(Kexp).max()))
print("   eta^mu eta_mu = %.6e (= -c^2 = %.6e)"%(eta_up@eta_dn,-c*c))

print("\n== 8. potentials and tensor Maxwell equations (G 12.131-12.137): symbolic check (units c = 1, mu0 = 1)")
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3');X=[x0,x1,x2,x3]
V=sp.Function('V')(*X);Ax,Ay,Az=[sp.Function(n)(*X) for n in ('Ax','Ay','Az')]
A_up=[V,Ax,Ay,Az]                # A^mu = (V/c, A)
Fm=sp.Matrix(4,4,lambda m,n:sp.diff(A_up[n],X[m] if m==0 else X[m])*(1 if m==0 else 1)) if False else None
# F^{mu nu} = d^mu A^nu - d^nu A^mu with d^0 = -d/dx0 (Griffiths F^{mu nu} = dA^nu/dx_mu - dA^mu/dx_nu, x_0 = -x^0)
d_up=lambda m,f:(-sp.diff(f,x0) if m==0 else sp.diff(f,X[m]))
Fsym=sp.Matrix(4,4,lambda m,n:d_up(m,A_up[n])-d_up(n,A_up[m]))
Ex=-sp.diff(V,x1)-sp.diff(Ax,x0);By=sp.diff(Ax,x3)-sp.diff(Az,x1)
print("   F^{01} == E_x/c  ->",sp.simplify(Fsym[0,1]-Ex)==0,"; F^{31} == B_y ->",sp.simplify(Fsym[3,1]-By)==0)
# homogeneous equations: d_mu F_{nu lam}+cyc = 0 -> check d_lam F_{mu nu} cyclic identity for lowered F
Fl=Fsym.copy()
for i in range(4):
    for j in range(4):
        Fl[i,j]=Fsym[i,j]*(-1 if (i==0)!=(j==0) else 1)
dd=lambda f,m:sp.diff(f,X[m])
ok=all(sp.simplify(dd(Fl[m,n],l)+dd(Fl[n,l],m)+dd(Fl[l,m],n))==0 for m in range(4) for n in range(4) for l in range(4))
print("   cyclic identity d_l F_{mn} + d_m F_{nl} + d_n F_{lm} = 0 holds identically:",ok)
# inhomogeneous: d F^{mu nu}/dx^nu = box A^mu - d^mu (d_nu A^nu) -> (G 12.134); verify the expression for mu = 1
box=lambda f:-sp.diff(f,x0,2)+sum(sp.diff(f,X[i],2) for i in (1,2,3))
lhs=sum(sp.diff(Fsym[1,n],X[n]) for n in range(4))
div=sp.diff(A_up[0],x0)+sum(sp.diff(A_up[i],X[i]) for i in (1,2,3))         # d_mu A^mu
rhs_=sp.diff(div,x1)-box(Ax)
print("   dF^{1 nu}/dx^nu == d^1(d_mu A^mu) - box A^1  (G 12.134):",sp.simplify(lhs-rhs_)==0)

print("\n== 9. numbers for the practice problems")
g=gam(0.6);print("   P1: E=3e5 V/m (y), B=0, observer at 0.6c: E_bar_y = %.4e V/m ; B_bar_z = %.4e T ; check B_bar = -v x E_bar / c^2 = %.4e T"%(g*3e5,-g*0.6*3e5/c,-0.6*c*g*3e5/c**2))
Ee=5e8;Bb=1.0;vb=c**2*Bb/Ee;gb=gam(vb/c);print("   P2: E_y=5e8 V/m, B_z=1 T: boost speed c^2 B/E = %.4e m/s = %.4f c ; E_bar = %.4e V/m ; sqrt(E^2-c^2B^2) = %.4e V/m ; B_bar = %.2e T"%(vb,vb/c,gb*(Ee-vb*Bb),np.sqrt(Ee**2-c*c*Bb**2),gb*(Bb-vb*Ee/c**2)))
I=100.0;uu=1e6;sw=0.01;lt=-I*uu*gam(uu/c)/c**2;Eb=lt/(2*np.pi*eps0*sw);Bw=mu0*I/(2*np.pi*sw)
print("   P3: I = 100 A, u = 1e6 m/s, s = 1 cm: lambda_tot = %.4e C/m ; E_bar = %.2f V/m ; u B = %.2f V/m ; B = %.3e T"%(lt,Eb,uu*Bw,Bw))
bt=0.8;ps=np.arcsin(np.sqrt((1-(1-bt**2)**(2/3))/bt**2));print("   P4: beta=0.8: E = E_Coulomb at psi = %.2f deg (sin^2 psi = %.4f)"%(np.degrees(ps),np.sin(ps)**2))
gg=7000;bb=np.sqrt(1-1/gg**2);qe=1.602176634e-19;bimp=1e-3;print("   P12: gamma=7000, b=1 mm: peak E_2 = gamma k q/b^2 = %.3f V/m ; duration b/(gamma v) = %.3e s ; k q/b^2 = %.3e V/m"%(gg*qe/(4*np.pi*eps0*bimp**2),bimp/(gg*bb*c),qe/(4*np.pi*eps0*bimp**2)))
lam0=1e-6;vv=0.6*c;gv=gam(0.6);print("   P13: rest line charge lambda0=1 uC/m, boosted 0.6c along the wire, s=1 cm: E = %.4e V/m (=gamma E0 = %.4e) ; B = %.4e T ; mu0 I/(2 pi s) with I = gamma lambda0 v: %.4e T"%(gv*lam0/(2*np.pi*eps0*0.01),gv*lam0/(2*np.pi*eps0*0.01),vv*gv*lam0/(2*np.pi*eps0*0.01)/c**2,mu0*gv*lam0*vv/(2*np.pi*0.01)))
