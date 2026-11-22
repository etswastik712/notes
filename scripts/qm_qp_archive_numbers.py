"""Numbers for the PH2113 Sem-3 archive papers 2021-2025. Run: python scripts/qm_qp_archive_numbers.py"""
import numpy as np, math
from scipy.integrate import quad
h=6.626e-34; hb=h/(2*math.pi); c=3e8; me=9.109e-31; e=1.602e-19; kB=1.381e-23; b=2.898e-3
print("== 2021 (online mid-sem) ==")
L=1.0
N2=1/quad(lambda x:(x*(L-x))**2,0,L)[0]; print("D1 N^2 L^5 =",N2,"(30)")
print("   <x^2>/L^2 =",N2*quad(lambda x:x**2*(x*(L-x))**2,0,L)[0], "(2/7=",2/7,")")
print("   <p^2> L^2/hbar^2 =",N2*quad(lambda x:(x*(L-x))*2,0,L)[0])
for TC in (5500,5000,6000):
    T=TC+273.15; lm=b/T; print(f"D2 T={TC}C: lam_max={lm*1e9:.0f} nm, E(lam_max)={h*c/lm/e:.2f} eV, E(lam/2)={2*h*c/lm/e:.2f} eV")
E=13.6*(1-1/16); print("D3 E=",E,"eV nu=",E*e/h,"Hz; v1=",2.188e6,"v4=",2.188e6/4)
for (n1,n2) in ((4,3),(4,2),(4,1),(3,2),(3,1),(2,1)):
    print(f"   {n1}->{n2}: {13.6*(1/n2**2-1/n1**2)*e/h:.3e} Hz, {h*c/(13.6*(1/n2**2-1/n1**2)*e)*1e9:.1f} nm")
print("D4a threshold lambda =",h*c/(4*e)*1e9,"nm")
K=h*c/(248e-9)/e-2.3; print("D4b KE=",K,"eV lambda_dB=",h/math.sqrt(2*me*K*e)*1e9,"nm")
for m,nm in ((me,'e'),(1.675e-27,'n')):
    p=h/1e-10; print(f"D5 {nm}: KE={p**2/(2*m)/e:.3g} eV, rest={m*c**2/e:.3g} eV")
print("MCQ5 |a|^2 =",1-11/16-1/16)
print("== 2022 mid ==")
p=h/0.022e-9; v=p/me; print("A2 p=",p,"v_g=",v,"v/c=",v/c,"v_ph(KE)=",v/2,"v_ph(total E)=",c**2/v)
lam=h/math.sqrt(2*me*10*e); print("B3 lambda_dB(10 eV)=",lam*1e9,"nm")
eps0=8.854e-12; k=e**2/(4*math.pi*eps0)
a0=hb**2/(me*k); print("C1 (hbar) r=a0=",a0,"E=",-k/(2*a0)/e,"eV; (h) r=",h**2/(me*k),"E=",-me*k**2/(2*h**2)/e)
print("== 2022 end ==")
dE=hb/1e-8/e; print("3A dE(hbar/dt)=",dE,"eV; hbar/2dt=",dE/2)
E=10.2; lam=h*c/(E*e); print("   lambda=",lam*1e9,"nm dlam=",lam*dE/E*1e9,"nm")
mp=1.67e-27
for dx in (2e-15,5e-15):
    dp=hb/(2*dx); print(f"3B dx={dx}: v~{dp/mp:.2e} m/s ({dp/mp/c:.3f} c)")
P=(25*144+144*25)/169**2; print("4 P(a2)=",P, "=7200/28561")
Ry=13.6
print("5 no repulsion:", -2*4*Ry, "; opposite-sides scaling: E=", -(3.5**2)/4*2*Ry, "r/a0=",4/7)
lam_=2-5/16; print("   variational Zeff=",lam_,"E=",-2*Ry*lam_**2, "(expt -79.0)")
print("== 2023 mid ==")
print("Q7 lambda=",h/math.sqrt(2*me*100*e)*1e9,"nm")
print("Q9 hnu=",h*1.5e15/e,"eV stop=",h*1.5e15/e-5,"V")
print("Q12d P=",1-5*math.exp(-2))
print("== 2023 end ==")
a=1.0; print("1c P=",quad(lambda x:(2/a)*math.sin(2*math.pi*x/a)**2,-a/4,a/4)[0])
print("2vi radial ratio=",4*math.exp(-1),"density ratio=",math.exp(-1))
print("== 2024 end ==")
a=5e-9; Ef=math.pi**2*hb**2/(2*me*a**2)/e; print("A7 E1(free mass)=",Ef,"eV; m*/me for 0.6 eV:",Ef/0.6,"for 600 eV:",Ef/600)
print("B2 <H'>=hbar w ; only w->2w: 5/4 hbar w")
print("== 2025 mid ==")
I=1/(4*math.pi); A=math.pi*1e-20; t=3.4e-19/(I*A); print("Q1 t=",t,"s")
print("Q2 N2=",12e16*630/420)
for n in (1,2,3):
    s=math.sqrt(n**2*math.pi**2/3-2)/2; print(f"Q6 n={n}: sx sp/hbar={s:.3f}")
L=1.0
f=lambda x: math.sqrt(2/L)*math.cos(math.pi*x/L)*math.sqrt(1/L)*math.cos(math.pi*x/(2*L))
ov=quad(f,-L/2,L/2)[0]; print("Q7 symmetric overlap^2=",ov**2,"(8/3pi)^2=",(8/(3*math.pi))**2)
g=lambda x: math.sqrt(2/L)*math.sin(math.pi*x/L)*math.sqrt(1/L)*math.sin(math.pi*x/(2*L))
print("   one-sided overlap^2=",quad(g,0,L)[0]**2,"32/9pi^2=",32/(9*math.pi**2))
print("== 2025 end ==")
print("A1 A=",1/math.sqrt(5)); print("A4 T=1/cosh^2(1)=",1/math.cosh(1)**2)
print("B1 <E>/E1=",1/4+4/2+9/8+16/8)
