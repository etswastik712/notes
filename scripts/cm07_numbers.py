"""CM07 numbers (rigid bodies). .venv/bin/python -W ignore scripts/cm07_numbers.py
Every number quoted in CM07 is printed here; LL = Landau-Lifshitz Vol. 1."""
import numpy as np
from scipy.integrate import solve_ivp, dblquad, quad
from scipy.special import ellipk
np.set_printoptions(precision=6,suppress=True)

print("== 1. rolling wheel (LL 31.2): speed of a rim point at angle a from the contact point = 2V sin(a/2)")
for a in (0,90,180): print("   a=%3d deg: v/V = %.4f"%(a,2*np.sin(np.radians(a)/2)))

print("\n== 2. principal moments of inertia, uniform density, recomputed by quadrature (units mu=1)")
# rod: I = L^2/12 (thin), sphere 2/5 R^2, cylinder, cone, ellipsoid, box
R=1.0;h=1.0
# cylinder about axis: 1/2 R^2 ; about a diameter through centre: R^2/4 + h^2/12
Iz=dblquad(lambda r,z:r**2*2*np.pi*r,-h/2,h/2,0,R)[0]/(np.pi*R**2*h)
Ix=dblquad(lambda r,z:(r**2/2+z**2)*2*np.pi*r,-h/2,h/2,0,R)[0]/(np.pi*R**2*h)
print("   cylinder R=1,h=1: I3=%.6f (R^2/2=0.5), I1=I2=%.6f (R^2/4+h^2/12=%.6f)"%(Iz,Ix,0.25+1/12))
# cone apex at z=0, base z=h, radius r=R z/h ; centre of mass at 3h/4
V=np.pi*R**2*h/3
zc=dblquad(lambda r,z:z*2*np.pi*r,0,h,0,lambda z:R*z/h)[0]/V
I3c=dblquad(lambda r,z:r**2*2*np.pi*r,0,h,0,lambda z:R*z/h)[0]/V
I1apex=dblquad(lambda r,z:(r**2/2+z**2)*2*np.pi*r,0,h,0,lambda z:R*z/h)[0]/V
I1c=I1apex-zc**2
print("   cone R=1,h=1: z_cm=%.6f (3h/4), I3=%.6f (3R^2/10=0.3), I1 about apex %.6f (3/5 (R^2/4+h^2)=%.6f), I1 about cm (parallel axis 32.12) %.6f (3/20 (R^2+h^2/4)=%.6f)"%(zc,I3c,I1apex,0.6*(0.25+1),I1c,0.15*(1+0.25)))
# ellipsoid by MC
rng=np.random.default_rng(1);a,b,c=3.0,2.0,1.0
P=rng.uniform(-1,1,(4000000,3));P=P[(P**2).sum(1)<1];X=P*np.array([a,b,c])
I1e=((X[:,1]**2+X[:,2]**2).mean());I2e=((X[:,0]**2+X[:,2]**2).mean());I3e=((X[:,0]**2+X[:,1]**2).mean())
print("   ellipsoid (3,2,1) by Monte Carlo: I1,I2,I3 = %.3f %.3f %.3f  vs (b^2+c^2)/5,(a^2+c^2)/5,(a^2+b^2)/5 = %.3f %.3f %.3f"%(I1e,I2e,I3e,(b*b+c*c)/5,(a*a+c*c)/5,(a*a+b*b)/5))
print("   triangle inequality (32.9): I3=%.3f <= I1+I2=%.3f ; thin disc (planar, 32.10): I3 = 2 I1 exactly"%(I3e,I1e+I2e))
print("   sphere: I = 2/5 R^2 = 0.4; thin rod L=1: I = 1/12 = %.6f; box a,b,c: (b^2+c^2)/12 etc."%(1/12))

print("\n== 3. compound pendulum (LL §32 Problem 3), uniform rod length L pivoted at one end, axis along a principal axis (cos a=1)")
L=1.0;l=L/2;I1=L**2/12
w2=9.81*l/(l**2+I1); print("   omega^2 = g l/(l^2+I1/mu) = %.6f s^-2 ; 3g/(2L) = %.6f -> equivalent simple pendulum length 2L/3 = %.6f"%(w2,3*9.81/(2*L),2*L/3))

def rot_integrate(I,Om0,T,K=None,R0=None,rtol=1e-11):
    """Euler equations in the body frame + rotation matrix R (columns = body axes in space)."""
    I=np.array(I,float)
    def f(t,y):
        Om=y[:3];Rm=y[3:].reshape(3,3)
        M=I*Om; Kb=np.zeros(3) if K is None else K(t,Rm)
        dOm=(np.cross(M,Om)+Kb)/I
        S=np.array([[0,-Om[2],Om[1]],[Om[2],0,-Om[0]],[-Om[1],Om[0],0]])
        return np.concatenate([dOm,(Rm@S).ravel()])
    R0=np.eye(3) if R0 is None else R0
    return solve_ivp(f,[0,T],np.concatenate([Om0,R0.ravel()]),rtol=rtol,atol=1e-13,dense_output=True,max_step=0.01)

print("\n== 4. free symmetric top, I1=I2=1, I3=1.5, spin Omega3=1, small tilt")
I=(1,1,1.5);Om0=np.array([0.3,0,1.0]);s=rot_integrate(I,Om0,60)
t=np.linspace(0,60,60001);Y=s.sol(t);Om=Y[:3]
M0=np.array(I)*Om0;Mn=np.linalg.norm(M0)
Mspace=np.einsum('tij,jt->it',Y[3:].reshape(3,3,-1).transpose(2,0,1),(np.array(I)[:,None]*Om))
print("   |M| conserved: %.3e relative drift ; E conserved: %.3e"%(np.abs(np.linalg.norm(Mspace,axis=0)/Mn-1).max(),np.abs((0.5*(np.array(I)[:,None]*Om**2).sum(0))/(0.5*(np.array(I)*Om0**2).sum())-1).max()))
w_pred=Om0[2]*(I[2]-I[0])/I[0]
zc=t[1:][(Om[0][:-1]>0)&(Om[0][1:]<=0)];Tbody=np.mean(np.diff(zc))
print("   body-frame frequency omega = Omega3 (I3-I1)/I1 (36.6) = %.4f ; measured 2pi/T = %.4f"%(w_pred,2*np.pi/Tbody))
# precession of the symmetry axis about M in space
x3=Y[3:].reshape(3,3,-1)[:,2,:]   # third column of R (axis x3 in space)
Mh=M0/Mn
e1=np.cross(Mh,[0,0,1.0]); e1/=np.linalg.norm(e1); e2=np.cross(Mh,e1)
ph=np.unwrap(np.arctan2(x3.T@e2,x3.T@e1)); Opr=np.polyfit(t,ph,1)[0]
theta=np.degrees(np.arccos(np.clip(x3.T@Mh,-1,1)))
print("   angle between x3 and M: min %.4f max %.4f deg (constant, LL 35.4) ; precession rate measured %.4f ; M/I1 = %.4f (33.5)"%(theta.min(),theta.max(),Opr,Mn/I[0]))
print("   axis spin rate (33.4): Omega3 = (M/I3) cos(theta) = %.4f (Omega3 = %.4f)"%(Mn/I[2]*np.cos(np.radians(theta.mean())),Om0[2]))

print("\n== 5. asymmetrical top I=(1,2,3)  (LL §37)")
I=np.array([1.,2.,3.])
def kinds(Om0):
    M=I*Om0;E=0.5*(I*Om0**2).sum();M2=(M**2).sum()
    return E,M2
for Om0 in (np.array([0.5,0.9,0.4]),np.array([0.4,0.9,0.5]),np.array([0.15,1,0.15])):
    E,M2=kinds(Om0)
    print("   Omega0=%s: E=%.5f M^2=%.5f ; 2E I1=%.4f 2E I2=%.4f 2E I3=%.4f -> M^2 %s 2EI2"%(Om0,E,M2,2*E*I[0],2*E*I[1],2*E*I[2],">" if M2>2*E*I[1] else "<"))
Om0=np.array([0.5,0.9,0.4]); E,M2=kinds(Om0)
I1,I2,I3=I
if M2>2*E*I2:
    k2=(I2-I1)*(2*E*I3-M2)/((I3-I2)*(M2-2*E*I1))
    Kk=ellipk(k2); T37=4*Kk*np.sqrt(I1*I2*I3/((I3-I2)*(M2-2*E*I1)))
    print("   case M^2>2EI2: k^2 = %.6f (37.9), K(k) = %.6f (37.11), T = 4K sqrt(I1I2I3/((I3-I2)(M^2-2EI1))) = %.6f (37.12)"%(k2,Kk,T37))
else:
    k2=(I2-I3)*(2*E*I1-M2)/((I1-I2)*(M2-2*E*I3)) if False else None
s=rot_integrate(I,Om0,60);t=np.linspace(0,60,120001);Om=s.sol(t)[:3]
zc=t[1:][(Om[1][:-1]<0.9*0+Om[1][:-1])&False]
# period of Omega1 via upward crossings of its mean
m=Om[0].mean();zc=t[1:][(Om[0][:-1]<m)&(Om[0][1:]>=m)];print("   numerical period of Omega1(t): %.6f"%np.mean(np.diff(zc)))
print("   (37.10) check: Omega2 max sqrt((2EI3-M^2)/(I2(I3-I2))) = %.5f ; numerical max %.5f"%(np.sqrt((2*E*I3-M2)/(I2*(I3-I2))),np.abs(Om[1]).max()))

print("   stability of the three axes: perturb each by 1e-4 and find growth")
for ax,name in ((0,"x1 (smallest I)"),(1,"x2 (intermediate I)"),(2,"x3 (largest I)")):
    Om0=np.zeros(3);Om0[ax]=1;Om0[(ax+1)%3]=1e-4;s=rot_integrate(I,Om0,40);t=np.linspace(0,40,40001);Om=s.sol(t)[:3]
    dev=np.sqrt((Om**2).sum(0)-Om[ax]**2)
    print("   rotation about %-20s: max transverse |Omega|/Omega = %.4g"%(name,dev.max()))
# growth rate near x2
Om2=1.0;lam_pred=Om2*np.sqrt((I2-I1)*(I3-I2)/(I1*I3))
Om0=np.array([1e-9,1,0.]);s=rot_integrate(I,Om0,16,rtol=1e-12);t=np.linspace(6,13,2000);Om=s.sol(t)[:3]
lam_meas=np.polyfit(t,np.log(np.abs(Om[0])),1)[0]
print("   growth rate about x2 (Omega2=1): predicted sqrt((I2-I1)(I3-I2)/(I1 I3)) Omega2 = %.5f ; measured slope (t = 6..13) %.5f"%(lam_pred,lam_meas))
# stable frequency near x3 (LL §37 Problem 1) : omega = Omega0 sqrt((I3/I2-1)(I3/I1-1)), Omega0 = M/I3 ~ Omega3
Om3=1.0;w3=Om3*np.sqrt((I3/I2-1)*(I3/I1-1));Om0=np.array([1e-4,0,1.]);s=rot_integrate(I,Om0,60);t=np.linspace(0,60,60001);Om=s.sol(t)[:3]
zc=t[1:][(Om[0][:-1]<0)&(Om[0][1:]>=0)]
print("   small oscillation near x3: predicted omega = Omega3 sqrt((I3/I2-1)(I3/I1-1)) = %.5f ; measured %.5f"%(w3,2*np.pi/np.mean(np.diff(zc))))
w1=np.sqrt((I1-I2)*(I1-I3)/(I2*I3));Om0=np.array([1.,1e-4,0]);s=rot_integrate(I,Om0,60);t=np.linspace(0,60,60001);Om=s.sol(t)[:3]
zc=t[1:][(Om[1][:-1]<0)&(Om[1][1:]>=0)]
print("   small oscillation near x1: predicted omega = Omega1 sqrt((I1-I2)(I1-I3)/(I2 I3)) = %.5f ; measured %.5f"%(w1,2*np.pi/np.mean(np.diff(zc))))

print("\n== 6. heavy symmetric top (LL §35 Problems 1-3), units mu g l = 1, I1' = I1 + mu l^2 = 1, I3 = 0.4 (spin about x3)")
I1p=1.0;I3=0.4;mgl=1.0
def top_sim(M3,tilt,T=80,l=1.0,mu=1.0,g=1.0):
    I1pp=1.0   # inertia about pivot, perpendicular to axis
    Ib=(I1pp,I1pp,I3)
    def K(t,Rm):
        x3=Rm[:,2]; # torque = r_cm x F, r_cm = l x3 (space), F = -mu g z
        Ts=np.cross(l*x3,np.array([0,0,-mu*g]))
        return Rm.T@Ts
    R0=np.array([[1,0,0],[0,np.cos(tilt),-np.sin(tilt)],[0,np.sin(tilt),np.cos(tilt)]])   # axis x3 tilted from vertical by 'tilt'
    Om0=np.array([0,0,M3/I3]);return rot_integrate(Ib,Om0,T,K=K,R0=R0,rtol=1e-10)
thr=2*np.sqrt(I1p*mgl)
print("   sleeping-top threshold (Problem 2): M3^2 > 4 I1' mu g l -> M3 > %.4f"%thr)
for M3 in (1.6,1.9,2.1,2.6):
    s=top_sim(M3,0.02);t=np.linspace(0,80,16001);x3=s.sol(t)[3:].reshape(3,3,-1)[:,2,:];th=np.degrees(np.arccos(np.clip(x3[2],-1,1)))
    print("   M3 = %.1f: initial tilt 0.02 rad (1.15 deg), max tilt over 80 time units = %.2f deg -> %s"%(M3,th.max(),"STABLE (stays small)" if th.max()<10 else "UNSTABLE (falls)"))
print("   fast top: M3=20 (Omega3=%.1f): tilt 40 deg, nutation and precession"%(20/I3))
s=top_sim(20,np.radians(40),T=40);t=np.linspace(0,40,80001);R=s.sol(t)[3:].reshape(3,3,-1);x3=R[:,2,:];th=np.degrees(np.arccos(np.clip(x3[2],-1,1)))
phi=np.unwrap(np.arctan2(x3[1],x3[0]));Opr=np.polyfit(t,phi,1)[0]
Mb=np.array([1,1,0.4])[:,None]*s.sol(t)[:3];Ms=np.einsum('ijt,jt->it',R,Mb);Mnorm=np.linalg.norm(Ms,axis=0)
print("   mean precession rate %.5f ; fast-top prediction (LL Problem 3) mu g l/M = %.5f (M ~ M3 cos(tilt)... see text: %.5f)"%(Opr,mgl/20,mgl/ (Mnorm.mean())))
zc=t[1:][(np.gradient(th)[:-1]<0)&(np.gradient(th)[1:]>=0)];print("   nutation period from simulation %.4f vs 2 pi I1'/M = %.4f"%(np.mean(np.diff(zc)),2*np.pi*I1p/Mnorm.mean()))
# effective potential roots example
Mz=15.0;M3=20.0;th0=np.radians(40.0)
Ueff=lambda th:(Mz-M3*np.cos(th))**2/(2*I1p*np.sin(th)**2)-mgl*(1-np.cos(th))
print("   U_eff has minimum at theta where dU/dtheta=0: scan")
ths=np.linspace(0.05,3.0,5000);u=Ueff(ths);i=u.argmin();print("   U_eff min %.4f at theta = %.2f deg"%(u[i],np.degrees(ths[i])))
