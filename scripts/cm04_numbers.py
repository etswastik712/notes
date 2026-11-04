"""CM04 numbers. .venv/bin/python -W ignore scripts/cm04_numbers.py"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
print("== Earth-Moon: reduced mass and centre of mass")
m1=5.972e24; m2=7.348e22; d=3.844e8
print("mu=%.4e kg ; r1=m2 d/(m1+m2)=%.4e m (Earth radius 6.371e6)"%(m1*m2/(m1+m2),m2*d/(m1+m2)))
print("== Earth orbit about the Sun (GM=1.32712440e20, a=1.495978707e11, e=0.0167)")
GM=1.32712440e20;a=1.495978707e11;e=0.0167
T=2*np.pi*np.sqrt(a**3/GM); rp=a*(1-e); ra=a*(1+e); vp=np.sqrt(GM/a*(1+e)/(1-e)); va=np.sqrt(GM/a*(1-e)/(1+e))
print("T=%.4e s = %.3f d ; r_peri=%.4e r_aph=%.4e ; v_p=%.3f km/s v_a=%.3f km/s ; v_circ=%.3f km/s"%(T,T/86400,rp,ra,vp/1e3,va/1e3,np.sqrt(GM/a)/1e3))
print("check L conservation: r_p v_p=%.6e r_a v_a=%.6e"%(rp*vp,ra*va))
print("== Mars a=1.524 AU: T=a^1.5 yr = %.4f yr"%(1.524**1.5))
print("== Kepler orbit m=alpha=1, p=1, e=0.5")
p=1.;e=0.5; a_=p/(1-e**2); E=-1/(2*a_); Tp=2*np.pi*a_**1.5
print("a=%.5f b=%.5f E=%.5f rmin=%.5f rmax=%.5f T=%.5f"%(a_,p/np.sqrt(1-e**2),E,p/(1+e),p/(1-e),Tp))
rp_=p/(1+e); vp_=np.sqrt(2*(E+1/rp_))
f=lambda t,y:[y[2],y[3],-y[0]/np.hypot(y[0],y[1])**3,-y[1]/np.hypot(y[0],y[1])**3]
s=solve_ivp(f,[0,Tp],[rp_,0,0,vp_],rtol=1e-12,atol=1e-13,dense_output=True)
y=s.sol(np.linspace(0,Tp,5)); print("position after one period:",y[:2,-1].round(8)," start:",y[:2,0])
t=np.linspace(0,Tp,2001); x,yy,vx,vy=s.sol(t); Lz=x*vy-yy*vx; En=0.5*(vx**2+vy**2)-1/np.hypot(x,yy)
Ax=vy*Lz-x/np.hypot(x,yy); Ay=-vx*Lz-yy/np.hypot(x,yy)
print("Lz=%.6f(ptp %.1e) E=%.6f(ptp %.1e) |A|=%.6f (ptp %.1e) direction=(%.4f,%.4f)"%(Lz[0],np.ptp(Lz),En[0],np.ptp(En),np.hypot(Ax[0],Ay[0]),np.ptp(np.hypot(Ax,Ay)),Ax[0],Ay[0]))
print("== Kepler's equation xi - e sin xi = 2 pi t/T at t=T/4")
Mn=np.pi/2; xi=brentq(lambda z:z-e*np.sin(z)-Mn,0,np.pi); X=a_*(np.cos(xi)-e); Y=a_*np.sqrt(1-e**2)*np.sin(xi)
# LL's x,y: x measured from centre of ellipse along major axis; focus at x=ae. Convert to focus-origin coords:
Xf=X+a_*e  # origin at focus (perihelion at +x) -- LL: x from centre with focus at distance ae -> perihelion on +x side?
Xn,Yn=s.sol(Tp/4)[:2]
print("xi=%.6f  r=a(1-e cos xi)=%.6f  numerical r(T/4)=%.6f"%(xi,a_*(1-e*np.cos(xi)),np.hypot(Xn,Yn)))
print("== precession for central force F=-r^n, n=-2.1 (m=k=1): beta^2=3+n, apsidal advance per orbit 2pi(1/beta-1)")
n=-2.1; beta=np.sqrt(3+n)
fr=lambda t,y:[y[2],y[3],-y[0]/np.hypot(y[0],y[1])*np.hypot(y[0],y[1])**n,-y[1]/np.hypot(y[0],y[1])*np.hypot(y[0],y[1])**n]
s=solve_ivp(fr,[0,80],[1,0,0,1.02],rtol=1e-12,atol=1e-13,dense_output=True,max_step=0.01)
t=np.linspace(0,80,160001); x,y,vx,vy=s.sol(t); r=np.hypot(x,y); ph=np.unwrap(np.arctan2(y,x))
im=[i for i in range(1,len(t)-1) if r[i]<r[i-1] and r[i]<=r[i+1]]
print("successive pericentre angles:",ph[im][:4].round(5)," spacing=",np.diff(ph[im])[:3].round(5)," predicted 2pi/beta=%.5f, advance 2pi(1/beta-1)=%.5f (%.2f deg)"%(2*np.pi/beta,2*np.pi*(1/beta-1),np.degrees(2*np.pi*(1/beta-1))))
print("== fall to the centre: U=-alpha/r^2, m=1, M=1: threshold alpha=M^2/2m=0.5")
for al in (0.4,0.6):
    g=lambda t,y:[y[1],1/y[0]**3-2*al/y[0]**3]  # r'' = M^2/(m^2 r^3) - dU/dr/m, U=-al/r^2 -> -dU/dr=-2 al/r^3
    ev=lambda t,y:y[0]-1e-3; ev.terminal=True
    s=solve_ivp(g,[0,50],[1.5,0.0],events=ev,rtol=1e-10,atol=1e-12)
    print("alpha=%.1f reaches r=1e-3 at t=%s ; min r=%.4f"%(al,"%.3f"%s.t_events[0][0] if len(s.t_events[0]) else "never",s.y[0].min()))
