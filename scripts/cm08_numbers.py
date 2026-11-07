"""CM08 numbers (non-inertial frames). .venv/bin/python -W ignore scripts/cm08_numbers.py
LL = Landau-Lifshitz Vol. 1 §39."""
import numpy as np
from scipy.integrate import solve_ivp
np.set_printoptions(precision=6,suppress=True)
g=9.81;Om_E=7.2921e-5

print("== 1. pendulum in a uniformly accelerated frame (LL 39.5): uniform field -mW added to gravity")
a=2.0;l=1.0
geff=np.hypot(g,a);th0=np.degrees(np.arctan2(a,g))
print("   a=%.1f m/s^2: equilibrium angle atan(a/g) = %.4f deg ; g_eff = %.4f ; period 2 pi sqrt(l/g_eff) = %.5f s (vs %.5f s at rest)"%(a,th0,geff,2*np.pi*np.sqrt(l/geff),2*np.pi*np.sqrt(l/g)))
# check by integrating pendulum on a cart
def f(t,y):
    th,w=y; return [w,-(g*np.sin(th)+a*np.cos(th))/l]   # cart accelerating to the right, theta from vertical; fictitious force -a to the left
th_eq=-np.radians(th0)   # cart accelerates to the right: the bob hangs back (to the left)
s=solve_ivp(f,[0,20],[th_eq+0.01,0],rtol=1e-11,atol=1e-12,dense_output=True,max_step=0.002);t=np.linspace(0,20,400001);y=s.sol(t)[0]
zc=t[1:][((y[:-1]-th_eq)>0)&((y[1:]-th_eq)<=0)];print("   integrated equilibrium at theta = %.4f deg (hangs back); small-oscillation period about it: %.5f s"%(np.degrees(th_eq),np.mean(np.diff(zc))))

print("\n== 2. rotating frame: transform a free particle and check (39.9) with U=0:  a' = -2 Om x v' - Om x (Om x r')")
Om=np.array([0,0,0.7])
r0=np.array([1.0,0.3,0.0]);v0=np.array([-0.2,0.5,0.0])   # inertial straight line
def Rz(a): c,s_=np.cos(a),np.sin(a);return np.array([[c,s_,0],[-s_,c,0],[0,0,1]])  # inertial -> rotating (frame rotates by +Om t)
def rot_path(t):
    r_in=r0+v0*t; return Rz(Om[2]*t)@r_in
t=np.linspace(0,6,6001);rp=np.array([rot_path(x) for x in t]);h=t[1]-t[0]
vp=np.gradient(rp,h,axis=0);ap=np.gradient(vp,h,axis=0)
pred=-2*np.cross(Om,vp)-np.cross(Om,np.cross(Om,rp))
print("   max |a' - (Coriolis+centrifugal)| over the path (finite differences): %.2e ; typical |a'| = %.3f"%(np.abs(ap[5:-5]-pred[5:-5]).max(),np.linalg.norm(ap[5:-5],axis=1).mean()))
print("   a particle at rest at radius r in the inertial frame appears to circle clockwise at Omega: radial net force = centrifugal + Coriolis = m Om^2 r (1 - 2) = -m Om^2 r (centripetal) -> OK")

print("\n== 3. energy in the rotating frame (LL 39.13): E = E0 - M.Om")
m=1.3;r0=np.array([1.0,0.3,0.2]);v0=np.array([-0.2,0.5,0.1]);tt=2.0
r_in=r0+v0*tt;v_in=v0
R=Rz(Om[2]*tt)
r_rot=R@r_in;v_rot=R@v_in-np.cross(Om,r_rot)   # v = v0 - Om x r in the rotating components
E0=0.5*m*v_in@v_in
E=0.5*m*v_rot@v_rot-0.5*m*np.cross(Om,r_rot)@np.cross(Om,r_rot)   # (39.11) with U=0
M=m*np.cross(r_in,v_in)
print("   E (39.11) = %.6f ; E0 - M.Om = %.6f ; E0 = %.6f"%(E,E0-M@Om,E0))

print("\n== 4. eastward deflection of a falling body (LL §39 Problem 1): y = (1/3) g Om cos(lat) t^3, t=sqrt(2h/g)")
def fall(h,lat_deg,full=True):
    lat=np.radians(lat_deg);O=Om_E*np.array([np.cos(lat),0,np.sin(lat)])   # x north, y west, z up (LL axes)
    def f(t,s_):
        r=s_[:3];v=s_[3:];acc=np.array([0,0,-g])+2*np.cross(v,O)+(np.cross(O,np.cross(r,O)) if full else 0)
        return np.concatenate([v,acc])
    ev=lambda t,s_:s_[2]; ev.terminal=True;ev.direction=-1
    sol=solve_ivp(f,[0,60],[0,0,h,0,0,0],events=ev,rtol=1e-12,atol=1e-14);return sol.y_events[0][0][:3],sol.t_events[0][0]
for h,lat in ((100,45),(100,18.5),(100,0),(100,89),(500,45)):
    pos,tf=fall(h,lat);T=np.sqrt(2*h/g);pred=-(1/3)*g*Om_E*np.cos(np.radians(lat))*T**3
    print("   h=%4d m lat=%5.1f: y_pred = %.5f m (=%.3f cm east) ; integrated y = %.5f m ; x (towards pole) = %.2e m"%(h,lat,pred,-100*pred,pos[1],pos[0]))

print("\n== 5. projectile deviation (LL §39 Problem 2): y = (4/3)(vz^3/g^2) Om_x - 4 (vz^2 vx/g^2) Om_z, thrown in the x-z plane")
vx,vz=30.0,40.0;lat=np.radians(45);O=Om_E*np.array([np.cos(lat),0,np.sin(lat)])
def f(t,s_):
    v=s_[3:];return np.concatenate([v,np.array([0,0,-g])+2*np.cross(v,O)])
ev=lambda t,s_:s_[2];ev.terminal=True;ev.direction=-1
sol=solve_ivp(f,[0.001,60],[0,0,0,vx,0,vz],events=ev,rtol=1e-12,atol=1e-14)
yp=(4/3)*vz**3/g**2*O[0]-4*vz**2*vx/g**2*O[2]
print("   v=(%d,%d) m/s at 45N: landing y integrated = %.5f m ; formula = %.5f m ; flight time %.4f (2vz/g = %.4f)"%(vx,vz,sol.y_events[0][0][1],yp,sol.t_events[0][0],2*vz/g))

print("\n== 6. Foucault pendulum (LL §39 Problem 3): path rotates with angular velocity -Om_z, Om_z = Om sin(lat)")
for lat in (45,18.5,90,10):
    Oz=Om_E*np.sin(np.radians(lat));w=2*np.pi/10.0   # 10 s pendulum
    f=lambda t,s_:[s_[2],s_[3],-w*w*s_[0]+2*Oz*s_[3],-w*w*s_[1]-2*Oz*s_[2]]
    T=3*3600*4;  # integrate 12 h? use shorter with scaled Om for speed
    # use scaled rotation to keep integration short: Om_z*K with K=2000, then rescale the rate
    K=2000.0;Ozs=Oz*K
    f=lambda t,s_:[s_[2],s_[3],-w*w*s_[0]+2*Ozs*s_[3],-w*w*s_[1]-2*Ozs*s_[2]]
    Tend=2*np.pi/Ozs*0.5;sol=solve_ivp(f,[0,Tend],[1,0,0,0],rtol=1e-11,atol=1e-13,dense_output=True,max_step=0.05)
    tt=np.linspace(Tend*0.8,Tend,20)  # fit angle of the oscillation plane (at times of max |x+iy|)
    z=sol.sol(np.linspace(0,Tend,200001));xy=z[0]+1j*z[1];ang=np.unwrap(np.angle(xy))
    # the slow rotation of the plane: angle of x+iy at positive extrema
    idx=np.where((np.abs(xy)[1:-1]>np.abs(xy)[:-2])&(np.abs(xy)[1:-1]>=np.abs(xy)[2:]))[0]+1
    a_=np.unwrap(2*np.angle(xy[idx]))/2;tp=np.linspace(0,Tend,200001)[idx];slope=np.polyfit(tp,a_,1)[0]/K
    P=2*np.pi/Oz/3600 if Oz>0 else np.inf
    print("   lat %5.1f: Om_z = %.4e rad/s ; measured plane rotation rate %.4e rad/s (rescaled) ; full turn takes %.2f h (= 23.934 h / sin lat = %.2f h)"%(lat,Oz,slope,P,23.9345/np.sin(np.radians(lat))))
