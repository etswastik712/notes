"""CM09 numbers (Hamilton's equations, Routhian, Poisson brackets). .venv/bin/python -W ignore scripts/cm09_numbers.py
LL = Landau-Lifshitz Vol. 1 §40-§42; LL's bracket: [f,g] = sum_k (df/dp_k dg/dq_k - df/dq_k dg/dp_k)  (42.5)"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
np.set_printoptions(precision=6,suppress=True)

print("== 1. Poisson-bracket algebra in LL's convention (symbolic)")
x,y,z,px,py,pz=sp.symbols("x y z p_x p_y p_z",real=True)
Q=[x,y,z];Pm=[px,py,pz]
def PB(f,g): return sp.simplify(sum(sp.diff(f,Pm[k])*sp.diff(g,Q[k])-sp.diff(f,Q[k])*sp.diff(g,Pm[k]) for k in range(3)))
Mx=y*pz-z*py;My=z*px-x*pz;Mz=x*py-y*px
print("   [q_i,p_k] = -delta, [p_i,q_k] = +delta (42.13):",PB(x,px),PB(px,x))
print("   [Mx,py] =",PB(Mx,py)," [Mx,pz] =",PB(Mx,pz)," [Mx,px] =",PB(Mx,px),"   (LL Problem 1: -pz, +py, 0)")
print("   [Mx,My]+Mz =",sp.simplify(PB(Mx,My)+Mz)," [My,Mz]+Mx =",sp.simplify(PB(My,Mz)+Mx)," [Mz,Mx]+My =",sp.simplify(PB(Mz,Mx)+My),"   (all 0: LL Problem 2, [Mx,My] = -Mz etc.)")
r2=x**2+y**2+z**2;p2=px**2+py**2+pz**2;rp=x*px+y*py+z*pz
phi=sp.Function("F")(r2,p2,rp)
print("   [F(r^2,p^2,r.p), Mz] =",sp.simplify(PB(phi,Mz)),"  (LL Problem 3: 0)")
print("   [r_vec, Mz] =",[PB(c,Mz) for c in Q]," = r x n with n=z:",[y,-x,0],"  (LL Problem 4: f x n)")
f=x**2*py+sp.sin(px);g=y*pz*x+px**3;h=z*py**2+x*y
J=sp.simplify(PB(f,PB(g,h))+PB(g,PB(h,f))+PB(h,PB(f,g)));print("   Jacobi identity for three test functions:",J)
H=(p2)/2+sp.Function("U")(sp.sqrt(r2))
print("   central force: [H,Mz] =",sp.simplify(PB(H,Mz)),"  => Mz conserved; Poisson's theorem: [Mx,My] = -Mz gives Mz from Mx,My")

print("\n== 2. integrators on H = (p^2+q^2)/2: one-step Jacobian determinant (phase-space area) and energy drift")
def step_rk4(q,p,h):
    f=lambda s:np.array([s[1],-s[0]]);s=np.array([q,p]);k1=f(s);k2=f(s+h/2*k1);k3=f(s+h/2*k2);k4=f(s+h*k3);return s+h/6*(k1+2*k2+2*k3+k4)
def step_leap(q,p,h): p=p-h/2*q;q=q+h*p;p=p-h/2*q;return np.array([q,p])
def step_euler(q,p,h): return np.array([q+h*p,p-h*q])
def jac(step,h):
    e=1e-6;J=np.zeros((2,2))
    for j,d in enumerate(((1,0),(0,1))):
        a=step(0.3+e*d[0],0.4+e*d[1],h);b=step(0.3-e*d[0],0.4-e*d[1],h);J[:,j]=(a-b)/(2*e)
    return np.linalg.det(J)
h=0.1
print("   h=0.1: det J: RK4 = %.8f ; leapfrog = %.8f ; explicit Euler = %.8f (exact: 1+h^2 = %.4f)"%(jac(step_rk4,h),jac(step_leap,h),jac(step_euler,h),1+h*h))
def matrix(st,h): return np.array([st(1,0,h),st(0,1,h)]).T
for name,st in (("RK4",step_rk4),("leapfrog",step_leap),("explicit Euler",step_euler)):
    A=matrix(st,h);steps_per=2*np.pi/h
    out=[]
    for Np in (10,1000,100000):
        N=int(round(Np*steps_per));S=np.linalg.matrix_power(A,N) if name!="explicit Euler" else None
        if S is None: out.append("Np=%d: H/H0 = (1+h^2)^(N) -> 10^%.0f"%(Np,N*np.log10(1+h*h)));continue
        s0=S@np.array([1.0,0.0]);dev=[];sc=s0.copy()
        for i in range(70): dev.append(abs(0.5*sc@sc-0.5));sc=st(sc[0],sc[1],h)
        out.append("Np=%d: H = %.6f, |dH| over the next period <= %.2e"%(Np,0.5*s0@s0,max(dev)))
    print("   %-14s"%name+" | ".join(out))

print("\n== 3. heavy symmetric top in canonical variables (Legendre transform of LL §35 Problem 1's Lagrangian)")
I1p=1.0;I3=0.4;mgl=1.0;pps=3.2;pph=3.475;th0=np.radians(60)
# L = I1'/2 (thd^2 + phd^2 sin^2) + I3/2 (psid + phd cos)^2 - mgl cos ; p_th=I1' thd ; p_ph=(I1' sin^2 + I3 cos^2) phd + I3 psid cos ; p_ps = I3(psid + phd cos)
# H = p_th^2/(2 I1') + (p_ph - p_ps cos)^2/(2 I1' sin^2) + p_ps^2/(2 I3) + mgl cos
Hf=lambda th,pth: pth**2/(2*I1p)+(pph-pps*np.cos(th))**2/(2*I1p*np.sin(th)**2)+pps**2/(2*I3)+mgl*np.cos(th)
def f(t,s):
    th,pth=s;h=1e-6;dH=(Hf(th+h,pth)-Hf(th-h,pth))/(2*h);return [pth/I1p,-dH]
sol=solve_ivp(f,[0,20],[th0,0.0],rtol=1e-11,atol=1e-13,dense_output=True,max_step=0.002);t=np.linspace(0,20,40001);th=sol.sol(t)[0]
print("   theta range from Hamilton's equations: %.4f deg .. %.4f deg ; H drift %.2e (CM07 gave 9.53 deg and 60 deg)"%(np.degrees(th.min()),np.degrees(th.max()),np.ptp(Hf(th,sol.sol(t)[1]))))
Ep=Hf(th0,0.0)-pps**2/(2*I3)-mgl;print("   E' = H - M3^2/(2 I3) - mgl = %.5f (CM07: 1.84375)"%Ep)

print("\n== 4. Hamiltonian in a uniformly rotating frame (LL §40 Problem 2): H = p^2/2m - Omega.(r x p) + U  vs CM08's example")
m=1.3;Om=np.array([0,0,0.7]);r0=np.array([1,0.3,0.2]);v0=np.array([-0.2,0.5,0.1]);t=2.0
r_in=r0+v0*t;p_in=m*v0
c,s=np.cos(Om[2]*t),np.sin(Om[2]*t);R=np.array([[c,s,0],[-s,c,0],[0,0,1]])
r_rot=R@r_in;p_rot=R@p_in   # canonical momentum p = m v0 (components in the rotating frame)
H_rot=p_rot@p_rot/(2*m)-Om@np.cross(r_rot,p_rot)
print("   H = %.6f ; E0 - M.Omega = %.6f (CM08: -0.314600)"%(H_rot,0.5*m*v0@v0-Om@(m*np.cross(r_in,v0))))

print("\n== 5. Routhian for a particle in a central field (eliminate the cyclic angle phi)")
print("   R = p_phi^2/(2mr^2)... : R(r,rdot) = (1/2) m rdot^2 - [ p_phi^2/(2 m r^2) + U(r) ]  -> the effective potential of CM04")
mm=1.0;pphi=1.2;U=lambda r:-1/r   # Kepler
rs=np.linspace(0.3,5,2000);Ueff=pphi**2/(2*mm*rs**2)+U(rs);i=Ueff.argmin();print("   Kepler m=1, p_phi=1.2, U=-1/r: minimum of U_eff at r=%.4f (p_phi^2/m = %.4f), U_eff = %.4f (-m/(2 p_phi^2) = %.4f)"%(rs[i],pphi**2/mm,Ueff[i],-mm/(2*pphi**2)))

print("\n== 6. Poisson's theorem on the Kepler problem: Mz and the Runge-Lenz component A_x are integrals; [Mz,Ax] is another integral")
mk=1.0;kk=1.0;rr=sp.sqrt(r2)
Ax=(py*Mz-pz*My)-mk*kk*x/rr
Ay=(pz*Mx-px*Mz)-mk*kk*y/rr
print("   [Mz,Ax] + Ay =",sp.simplify(PB(Mz,Ax)+Ay),"  (0: [Mz,Ax] = -Ay: Poisson's theorem yields the next Runge-Lenz component)")
