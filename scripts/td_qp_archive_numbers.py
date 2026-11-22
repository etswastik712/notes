"""Numbers for TD2213 Sem-3/4 archive papers 2022-2025. Run: python scripts/td_qp_archive_numbers.py"""
import math
from math import comb, log
R=8.314
p=1.0
for k in range(25): p*=(365-k)/365
print("birthday 25:",1-p)
for N in (1,5,20,100): print("2022 Q1 N",N,"ratio",comb(4*N,N)/comb(4*N,2*N),"(16/27)^N",(16/27)**N)
T=295.15; w=-2*R*T*log(31.7/22.8); Pf=2*R*T/31.7e-3; print("2022 Q6 rev w",w,"Pf",Pf,"irrev w",-Pf*(31.7-22.8)*1e-3)
print("2022 Q8",comb(18,4),comb(13,4))
for TC in (-10,10): Ts=TC+273.15; print("2022 Q9",TC,22.1-6000/Ts)
print("2022 Q11 dS",R*log(2))
print("2023 q1/2024 quiz KE A",1.5*1.3*5.750*101.325,"B",1.5*1.0*7.475*101.325,"J")
dT=0.140*(2-6)-2.533e-2/2*(2**2-6**2); print("2023 mid Q6 dT",dT,"Tf",573+dT)
def cp_int(a,b,T1,T2): return a*(T2-T1)+b/2*(T2**2-T1**2)
dH=cp_int(20.17,0.3665,298.15,473.15); print("2023 mid Q11 dH",dH,"dU",dH-R*175,"w(constP)",-R*175)
dH=cp_int(20.17,0.4001,273.15,373.15); print("2025 quiz1 Q3 dH",dH,"dU",dH-R*100)
print("2023 end Q1 dS",2*R*log(3),"dG",-2*R*300*log(3),"; cal:",2*1.98*log(3),-2*1.98*300*log(3))
N=1000; n=300; print("2023 end Q7 ln(WB/WA) N=1000,n=300:",log(comb(2*N,2*n))-2*log(comb(N,n)))
T1=300.15; T2=T1*0.5**(2/3); dU=1.5*R*(T2-T1); print("2024 mid Q5 T2",T2,"dU=w",dU,"dH",2.5*R*(T2-T1))
Rb=0.08314; P=Rb*300/(1.42-0.032)-1.355/1.42**2; print("2024 mid Q6 P",P,"ideal",Rb*300/1.42)
print("2024 mid Q9",30*log(510/500)-R*log(0.1))
c=4185; Tf=(343.15+3*303.15)/4; print("2024 mid Q10 Tf",Tf,"dS",c*(log(Tf/343.15)+3*log(Tf/303.15)))
dSi=50*336/273.15+50*4.19*log(293.15/273.15); q=50*336+50*4.19*20; print("2024 end Q6 dSice",dSi,"dSuniv",dSi-q/293.15)
print("2025 quiz2 Q1 phase only dSuniv",50*336/273.15-50*336/293.15)
print("2024 end Q7a",3*(1/6)**2*(5/6),"b",2/27)
print("2025 quiz1 Q4 P",math.exp(-12000/R*(1/373.15-1/338.15)),"atm")
print("2025 mid Q1",334/273.15+4.18*log(323.15/273.15))
qw=45*4.18*55; Tg=225-qw/(90*1.045); print("2025 mid Q2 gas out",Tg,"dS/min",45*4.18*log(388.15/333.15)+90*1.045*log((Tg+273.15)/498.15))
W=750*(1-300.15/1273.15); QL=W*263.15/37; print("2025 mid Q3 W",W,"QL",QL,"to air",750-W+QL+W)
Pc,Tc,w=4.0e6,250,0.248; P7=Pc*10**(-(w+1)); B=log(Pc/P7)/(1/175-1/250); Tb=1/(1/175+log(P7/101325)/B); print("2025 mid Q7 P(0.7Tc)",P7,"dH/R",B,"Tb",Tb)
Tf=(10*90+2.5*20)/12.5; print("2025 end Q2 Tf",Tf,"dS kJ/K",4.187*(10*log((Tf+273.15)/363.15)+2.5*log((Tf+273.15)/293.15)))
print("2025 end Q4 q",R*300.15*log(10),"dS",R*log(10))
Ra=0.08206; T=473.15; V=4.0
print("2025 end Q8 ideal",Ra*T/V,"vdW",Ra*T/(V-0.03039)-5.464/V**2)
Rb=0.08314; Tc=647.1; Pc=220.64; a=0.42748*Rb**2*Tc**2.5/Pc; b=0.08664*Rb*Tc/Pc
print("   RK a",a,"b",b,"P bar",Rb*T/(V-b)-a/(T**0.5*V*(V+b)),"(ideal bar",Rb*T/V,")")
