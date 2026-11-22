"""Numbers for the EC2113 (climate) Sem-3 archive papers 2020-2025. Run: python scripts/cl_qp_archive_numbers.py"""
import math
sig=5.67e-8; Om=7.29e-5; S=1368
d=math.radians
def daily_insol(lat,dec,S0=S):
    phi,de=d(lat),d(dec); x=-math.tan(phi)*math.tan(de)
    h0=math.pi if x<-1 else (0 if x>1 else math.acos(x))
    return S0/math.pi*(h0*math.sin(phi)*math.sin(de)+math.cos(phi)*math.cos(de)*math.sin(h0)), 24*h0/math.pi
print("== 2020 key check ==")
f=2*7.292e-5*math.sin(d(50)); a=f*1000; print("f50=",f,"a=",a,"disp=",0.5*a*1000**2/1e3,"km")
print("== 2021 ==")
for nm,al,T in (("1",0.2,220),("2",0.4,250),("3",0.6,280)):
    cool=al*342; warm=sig*288**4-sig*T**4; print(f"type{nm}: albedo cooling {cool:.1f}, greenhouse {warm:.1f}, net {warm-cool:+.1f} W/m2")
print("emission height (288-255)/6.5 =",(288-255)/6.5,"km; pole flux S sin23.5 =",S*math.sin(d(23.5)))
print("== 2022 mid ==")
for lat in (15,25):
    for nm,dec in (("Mar eq",0),("Jun sol",23.44)):
        Q,L=daily_insol(lat,dec); print(f"A2 {lat}N {nm}: daily mean {Q:.0f} W/m2, day {L:.1f} h, noon alt {90-abs(lat-dec):.1f}")
print("B1a dS for 1K:",S*4/255,"; forcing",S*4/255*0.7/4)
A=0.71*4*math.pi*6371e3**2; print("B1b ocean area",A,"rise",2.55e18/1000/A,"m")
e1,e2=0.005,0.0607; r=math.sqrt(1-e1**2)/math.sqrt(1-e2**2); print("B4a annual mean diff %",(r-1)*100)
rp=((1+e2)/(1-e2))**2; print("B4b peri/aph ratio",rp,"diff rel aph %",(rp-1)*100,"rel peri %",(1-1/rp)*100)
print("== 2022 end ==")
print("A1b p_top",7e7/1000,"p_bot",7e7/1000+1.2*9.8*500)
f40=2*Om*math.sin(d(40)); u=100/3.6; print("A5 f",f40,"PGF/m",f40*u,"dp/dy",0.37*f40*u,"Pa/m")
for lat in (90,30):
    Q,L=daily_insol(lat,23.44); print(f"B4b June {lat}N: {Q:.0f} W/m2 (day {L:.1f} h)")
print("B4e sigma*205^4 =",sig*205**4)
print("== 2023 mid ==")
print("A1 Venus",S/0.72**2,"Mars",S/1.52**2)
R=6.38e6; print("A2 u30",Om*R*math.sin(d(30))**2/math.cos(d(30)))
Te=(S*0.7/(4*sig))**0.25; eps=2-2*(Te/300)**4; print("B2 Te",Te,"eps",eps)
print("== 2024 ==")
Te=(S*0.7/(4*sig))**0.25; print("mid B2 Te",Te,"Ts(eps=0.5)",Te*(2/1.5)**0.25)
print("mid A1e T=2900/10 =",290)
print("quiz1 Q2 S cos35",S*math.cos(d(35)))
print("quiz1 Q8 Te faint sun",((0.7*S)*0.7/(4*sig))**0.25, "(albedo 0:",(0.7*S/(4*sig))**0.25,")")
R=6.36e6; v40=Om*R*math.cos(d(40)); print("quiz2 Q2 earth speed 40S",v40,"relative",336-v40)
print("quiz2 Q3",20*50/4)
Qp=S/math.pi*math.sin(d(23.44)); print("quiz2 Q7 annual mean pole",Qp*0+0,"(approx S sin(eps)/pi)",Qp,"equator approx",S/math.pi)
f45=2*Om*math.sin(d(45)); f10=2*Om*math.sin(d(10)); print("end B2 f45",f45,"PGF",f45*10,"u_g at 10N",f45*10/f10)
print("end B3a u30 (R=6.36e6)",Om*R*math.sin(d(30))**2/math.cos(d(30)))
f50=2*Om*math.sin(d(50)); print("end B3b a",f50*1000,"disp km",0.5*f50*1000*1e6/1e3)
print("== 2025 ==")
for dec in (0,23.44,-23.44):
    alt=90-abs(45-dec); print(f"mid B4b dec {dec}: alt {alt:.1f}, noon flux {S*math.sin(d(alt)):.0f}")
print("mid B1: Ts=3^0.25*203",3**0.25*203,"Tb",2**0.25*203,"Tb-Ta",2**0.25*203-203)
for lat in (46.5,0.5):
    f=2*Om*math.sin(d(lat)); a=f*50/3.6; print(f"end 5b lat {lat}: a={a:.2e}, d(20min)={0.5*a*1200**2:.0f} m")
