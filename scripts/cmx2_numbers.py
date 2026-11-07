"""CMX2 numbers (EM Lagrangian and gauge symmetry). .venv/bin/python -W ignore scripts/cmx2_numbers.py
G = Goldstein-Poole-Safko (SI in Sect. 1.5), LL2 = Landau-Lifshitz Vol. 2 (Gaussian), J = Jackson Ch. 12 (Gaussian). Here SI."""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
np.set_printoptions(precision=6,suppress=True)
qe=1.602176634e-19;mp=1.67262192e-27;c=2.99792458e8

print("== 1. symbolic: Euler-Lagrange of L = m v^2/2 - q phi + q A.v is the Lorentz force (G 1.63-1.66, LL2 17.2); random polynomial phi(x,y,z,t), A(x,y,z,t) with mixed terms")
import random
random.seed(5)
t,m,q=sp.symbols('t m q');X=sp.Function('x')(t);Y=sp.Function('y')(t);Z=sp.Function('z')(t)
xs,ys,zs,ts=sp.symbols('xs ys zs ts')
def randpoly():
    mons=[xs*ys,ys*zs,zs*xs,xs*ts,ys*ts,zs*ts,xs**2,ys**2,zs**2*ts,xs*ys*zs,ts**2,xs,ys,zs,ts,xs**2*ys]
    return sum(sp.Rational(random.randint(-5,5),random.randint(1,4))*mo for mo in mons)
phi=randpoly();A=[randpoly() for _ in range(3)]
sub=lambda e:e.subs({xs:X,ys:Y,zs:Z,ts:t},simultaneous=True)
v=[X.diff(t),Y.diff(t),Z.diff(t)]
def lagr(phi,A): return m*(v[0]**2+v[1]**2+v[2]**2)/2-q*sub(phi)+q*sum(sub(A[i])*v[i] for i in range(3))
L=lagr(phi,A)
def EL(L,Xq): return sp.diff(sp.diff(L,Xq.diff(t)),t)-sp.diff(L,Xq)
gradphi=[sub(sp.diff(phi,s_)) for s_ in (xs,ys,zs)];dAdt=[sub(sp.diff(a,ts)) for a in A]
E=[-gradphi[i]-dAdt[i] for i in range(3)]
Bv=[sub(sp.diff(A[2],ys)-sp.diff(A[1],zs)),sub(sp.diff(A[0],zs)-sp.diff(A[2],xs)),sub(sp.diff(A[1],xs)-sp.diff(A[0],ys))]
vxB=[v[1]*Bv[2]-v[2]*Bv[1],v[2]*Bv[0]-v[0]*Bv[2],v[0]*Bv[1]-v[1]*Bv[0]]
for i,Xq in enumerate((X,Y,Z)):
    print("   component %s: EL(L) - (m a - q(E + v x B)) = %s"%('xyz'[i],sp.simplify(sp.expand(EL(L,Xq)-(Xq.diff(t,2)*m-q*(E[i]+vxB[i]))))))

print("\n== 2. gauge: A -> A + grad Lambda, phi -> phi - d Lambda/dt changes L by q dLambda/dt (a total derivative) and leaves the equations of motion alone (G Ex.1.9, LL1 sec.2, LL2 18.1-18.3, J 12.1)")
Lam=randpoly()
Ap=[A[i]+sp.diff(Lam,s_) for i,s_ in enumerate((xs,ys,zs))];phip=phi-sp.diff(Lam,ts)
Lp=lagr(phip,Ap)
print("   L' - L - q dLambda/dt = %s"%sp.simplify(sp.expand(Lp-L-q*sub(Lam).diff(t))))
print("   Euler-Lagrange expressions of L' and L differ by:",[sp.simplify(sp.expand(EL(Lp,Xq)-EL(L,Xq))) for Xq in (X,Y,Z)])
Pold=[sp.diff(L,v_) for v_ in v];Pnew=[sp.diff(Lp,v_) for v_ in v]
print("   canonical momentum P' - P - q grad Lambda =",[sp.simplify(sp.expand(Pnew[i]-Pold[i]-q*sub(sp.diff(Lam,s_)))) for i,s_ in enumerate((xs,ys,zs))])
H_old=sum(Pold[i]*v[i] for i in range(3))-L;H_new=sum(Pnew[i]*v[i] for i in range(3))-Lp
print("   energy function h = P.v - L: h' - h = %s ; -q (partial Lambda / partial t) = %s  (only the explicit time dependence of Lambda changes it)"%(sp.simplify(sp.expand(H_new-H_old)),sp.simplify(sp.expand(-q*sub(sp.diff(Lam,ts))))))

print("\n== 3. three gauges for the same uniform B = B zhat plus E = E yhat (SI, proton): Hamilton's equations H = (P - qA)^2/2m + q phi, phi = -E y")
B0=1.0;E0=1.0e5;om=qe*B0/mp;Tc=2*np.pi/om
gauges={'Landau-x  A=(-By,0,0)':lambda x,y,l:np.array([-B0*y,0.0]),
        'Landau-y  A=(0,Bx,0)':lambda x,y,l:np.array([0.0,B0*x]),
        'symmetric A=(B/2)(-y,x,0)':lambda x,y,l:np.array([-B0*y/2,B0*x/2])}
# Jacobian dA_j/dx_i for the three gauges
dA={'Landau-x  A=(-By,0,0)':np.array([[0,0],[-B0,0]]),'Landau-y  A=(0,Bx,0)':np.array([[0,B0],[0,0]]),'symmetric A=(B/2)(-y,x,0)':np.array([[0,B0/2],[-B0/2,0]])}   # dA[i,j] = dA_j/dx_i
def run(name,lam=0.0,v0=(3e4,1e4),r0=(0.0,0.0),E=E0,N=20,gauge_extra=False):
    Af=gauges[name];J=dA[name].copy()
    def Aext(r):
        a=Af(r[0],r[1],0)
        if lam: a=a+lam*np.array([r[1],r[0]])                  # extra gauge term A += grad(lam x y) = lam (y, x)
        return a
    Jx=J.copy()
    if lam: Jx=J+lam*np.array([[0,1],[1,0]])
    def rhs(tt,s):
        r=s[:2];P=s[2:];kin=P-qe*Aext(r);vv=kin/mp
        dP=(qe/mp)*(Jx@kin)-np.array([0.0,qe*(-E)])             # dP_i/dt = (q/m) sum_j (P_j - q A_j) dA_j/dx_i - q dphi/dx_i, phi = -E y
        return np.concatenate([vv,dP])
    P0=mp*np.array(v0)+qe*Aext(np.array(r0))
    sol=solve_ivp(rhs,[0,N*Tc],np.concatenate([r0,P0]),rtol=1e-11,atol=1e-14,dense_output=True)
    return sol,Aext
ref,_=run('Landau-x  A=(-By,0,0)')
tt=np.linspace(0,20*Tc,4001);r_ref=ref.sol(tt)[:2]
for name in gauges:
    for lam in (0.0,0.7):
        sol,Aext=run(name,lam);r=sol.sol(tt)[:2]
        dev=np.max(np.linalg.norm(r-r_ref,axis=0))/np.max(np.linalg.norm(r_ref,axis=0))
        P=sol.sol(tt)[2:];print("   %-28s extra gauge lam=%.1f: max orbit deviation from the Landau-x orbit / orbit size = %.2e ; canonical P_x range %.3e kg m/s, kinetic m v_x range %.3e"%(name,lam,dev,np.ptp(P[0]),np.ptp(mp*np.gradient(r[0],tt))))
print("   drift speed E/B = %.4e m/s ; <dx/dt> over 20 periods = %.6e m/s (gauge-independent: orbits coincide)"%(E0/B0,ref.sol(20*Tc)[0]/(20*Tc)))

print("\n== 4. conserved canonical momenta (E = 0 for the rotation case): Noether in a gauge (CM03), and what they mean physically")
for name,idx in (('Landau-x  A=(-By,0,0)','P_x'),('Landau-y  A=(0,Bx,0)','P_y')):
    sol,Aext=run(name,E=0.0);P=sol.sol(tt)[2:];k=0 if idx=='P_x' else 1
    print("   %-24s %s: relative variation over 20 periods = %.2e ; the other component P_%s varies by %.2e kg m/s"%(name,idx,np.ptp(P[k])/np.max(np.abs(P[k])),'y' if k==0 else 'x',np.ptp(P[1-k])))
sol,Aext=run('symmetric A=(B/2)(-y,x,0)',E=0.0,r0=(2e-3,1e-3),v0=(3e4,1e4));S=sol.sol(tt);r=S[:2];P=S[2:]
Lz=r[0]*P[1]-r[1]*P[0];Lkin=mp*(r[0]*np.gradient(r[1],tt)-r[1]*np.gradient(r[0],tt))
print("   symmetric gauge: canonical L_z = x P_y - y P_x relative variation = %.2e ; kinetic L_z = m(x vy - y vx) varies by %.2e relative (not conserved)"%(np.ptp(Lz)/np.max(np.abs(Lz)),np.ptp(Lkin)/np.max(np.abs(Lkin))))
# guiding centre and radius (q > 0, B along +z: clockwise gyration); centre = r + (m/qB)(v_y, -v_x)
vx0,vy0=3e4,1e4;rho=mp*np.hypot(vx0,vy0)/(qe*B0)
cn=np.array([2e-3,1e-3])+(mp/(qe*B0))*np.array([vy0,-vx0]);d=np.linalg.norm(r-cn[:,None],axis=0)
print("   orbit centre r + (m/qB)(v_y,-v_x) = (%.4e, %.4e) m: distance to it stays between %.6e and %.6e m (rho = m v/(qB) = %.6e m)"%(cn[0],cn[1],d.min(),d.max(),rho))
Rc2=np.linalg.norm(cn)
print("   L_z = (qB/2)(R_c^2 - rho^2): measured %.6e ; formula %.6e (R_c = %.4e m from the origin, rho = %.4e m): the conserved canonical angular momentum combines guiding-centre distance and gyroradius"%(Lz[0],qe*B0/2*(Rc2**2-rho**2),Rc2,rho))
solL,_=run('Landau-x  A=(-By,0,0)',E=0.0);yy=solL.sol(tt)[1];Px0=solL.sol(0)[2]
print("   Landau gauge (E = 0): guiding-centre y_c = -P_x/(qB) = %.6e m ; centre of the simulated orbit (y_min + y_max)/2 = %.6e m"%(-Px0/(qe*B0),(yy.min()+yy.max())/2))

print("\n== 5. relativistic Hamiltonian (J 12.12-12.17, G 7.141-7.142, 8.56, LL2 16.4-16.8): proton in B = 1 T with gamma = 3")
g=3.0;v=c*np.sqrt(1-1/g**2);p=g*mp*v;B0=1.0
# Hamilton: H = c sqrt((P - qA)^2 + m^2c^2) + q phi ; symmetric gauge, particle starts at origin moving along +x, B along z
Bz=B0
def rhs_rel(tt,s):
    x,y,Px,Py=s;Ax,Ay=-Bz*y/2,Bz*x/2;kx,ky=Px-qe*Ax,Py-qe*Ay;en=np.sqrt(kx*kx+ky*ky+(mp*c)**2)
    vx,vy=c*kx/en,c*ky/en
    # dP_i/dt = q v_j dA_j/dx_i ; dA/dx: Ax=-By/2 -> dAx/dx=0,dAx/dy=-B/2 ; Ay=Bx/2 -> dAy/dx=B/2, dAy/dy=0
    dPx=qe*(vy*Bz/2);dPy=qe*(vx*(-Bz/2))
    return [vx,vy,dPx,dPy]
Tg=2*np.pi*g*mp/(qe*B0)
sol=solve_ivp(rhs_rel,[0,5*Tg],[0,0,p,0],rtol=1e-12,atol=1e-20,dense_output=True)
tt2=np.linspace(0,5*Tg,2001);S=sol.sol(tt2);x,y,Px,Py=S;Ax,Ay=-Bz*y/2,Bz*x/2;kx,ky=Px-qe*Ax,Py-qe*Ay;gam=np.sqrt(1+(kx**2+ky**2)/(mp*c)**2)
print("   gamma along the orbit: min %.10f max %.10f (H = gamma m c^2 conserved; no E field) ; radius of the circle R = gamma m v/(qB) = %.6e m (formula) vs fitted radius %.6e m"%(gam.min(),gam.max(),p/(qe*B0),0.5*(np.ptp(x)) ))
print("   energy check: H = c sqrt((P-qA)^2 + m^2c^2) = %.9e J constant to %.1e ; gamma m c^2 = %.9e J"%(np.mean(c*np.sqrt(kx**2+ky**2+(mp*c)**2)),np.ptp(c*np.sqrt(kx**2+ky**2+(mp*c)**2))/np.mean(c*np.sqrt(kx**2+ky**2+(mp*c)**2)),g*mp*c*c))
print("   period T = 2 pi gamma m/(qB) = %.6e s (non-relativistic would be %.6e s)"%(Tg,2*np.pi*mp/(qe*B0)))

print("\n== 6. E x B drift from the Landau-gauge reduction: H = p_y^2/2m + (P_x + qBy)^2/2m - qEy with P_x conserved -> a 1D oscillator; centre shift and drift")
Pxv=0.0;E0=1e5;B0=1.0
# minimum of V(y) = (Px + qBy)^2/2m - qEy : V' = qB (Px+qBy)/m - qE = 0 -> y0 = (mE/B - Px)/(qB)... check
y0=(mp*E0/B0-Pxv)/(qe*B0)
print("   V(y) = (P_x + qB y)^2/2m - qE y has its minimum at y0 = (mE/B - P_x)/(qB) = %.6e m; there dx/dt = (P_x + qB y0)/m = E/B = %.6e m/s (kinetic velocity, independent of P_x and q, m)"%(y0,(Pxv+qe*B0*y0)/mp))
print("   so the 2D problem reduces to a 1D oscillator of frequency omega = qB/m = %.6e rad/s about y0 (P_x conserved because of the translation symmetry of A in x)"%om)
