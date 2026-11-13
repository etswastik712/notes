//META {"title": "T–S diagram: what makes seawater heavy, and why mixing sinks", "desc": "Seawater density from the UNESCO EOS-80 equation of state at surface pressure, drawn as lines of equal σ = ρ − 1000 kg m⁻³ on a temperature–salinity diagram. Warm water: the lines lie flat, temperature does most of the work (ρα = 0.30 kg m⁻³ per K at 25 °C); near freezing the lines stand almost upright, salt decides (ρα = 0.054, ρβ = 0.80). Place two water samples and mix them: the mixture lies on the straight line between them but is denser than the average of the two (cabbeling), most strongly for a warm–cold pair of equal density.", "vault": "CL", "chapters": ["CL25 The Ocean's Ledger IV - Salt, Density and Water Masses", "CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch"], "tryit": "Sample A = 0 °C, S = 34.0 and B = 20 °C, S = 38.3 (σ = 27.30 for both): the 50 % mixture is 0.56 kg m⁻³ denser than either. Then put A at the AAIW point (3.3 °C, 34.15) and B at NADW (4 °C, 35.0): the excess is only 0.001. Set S = 32.8 and cool to the freezing line: σ stays near 26.4, never the 27.7 of the deep Pacific."}
ui.gridOf(2);
const P=ui.canvas(430,{xmin:32,xmax:38,ymin:-2.5,ymax:30,xlabel:'salinity (g/kg)',ylabel:'temperature (°C)',title:'lines of equal σ (EOS-80, surface pressure)'});
const P2=ui.canvas(430,{xmin:0,xmax:1,ymin:0,ymax:1,xlabel:'fraction of sample B in the mixture',ylabel:'σ (kg m⁻³)',title:'density of the mixture'});
function rho(S,T){const rw=999.842594+6.793952e-2*T-9.095290e-3*T**2+1.001685e-4*T**3-1.120083e-6*T**4+6.536332e-9*T**5;
 const A=8.24493e-1-4.0899e-3*T+7.6438e-5*T**2-8.2467e-7*T**3+5.3875e-9*T**4,B=-5.72466e-3+1.0227e-4*T-1.6546e-6*T**2;return rw+A*S+B*Math.pow(S,1.5)+4.8314e-4*S*S}
const tf=S=>-0.0575*S+1.710523e-3*Math.pow(S,1.5)-2.154996e-4*S*S;
const sTa=ui.slider('A: temperature (°C)',-2,30,0.1,0,draw),sSa=ui.slider('A: salinity',32,38,0.01,34.0,draw),sTb=ui.slider('B: temperature (°C)',-2,30,0.1,20,draw),sSb=ui.slider('B: salinity',32,38,0.01,38.3,draw),sm=ui.slider('mixing fraction of B',0,1,0.01,0.5,draw);
const out=ui.readout();
function Tof(S,sg){let lo=-2.5,hi=40;for(let i=0;i<50;i++){const m=(lo+hi)/2;if(rho(S,m)-1000>sg)lo=m;else hi=m}return(lo+hi)/2}
function draw(){const Ta=sTa.value,Sa=sSa.value,Tb=sTb.value,Sb=sSb.value,f=sm.value;P.clear();
 for(let sg=20;sg<=28.5;sg+=0.5){const Ss=M.linspace(32,38,60),Ts=Ss.map(S=>Tof(S,sg));const ok=Ts.every(t=>t>-2.4&&t<30);P.line(Ss,Ts.map(t=>t>30||t<-2.5?NaN:t),C.violet,sg%1===0?1.8:0.7);if(sg%1===0){const j=Ts.findIndex(t=>t<29.5&&t>-2.4);if(j>=0)P.text(String(sg),Ss[j],Ts[j]+0.6,C.violet,'left','11px system-ui')}}
 P.line([32,38],[tf(32),tf(38)],C.muted,2);P.text('freezing',32.1,-1.6,C.muted);
 const Sm=Sa*(1-f)+Sb*f,Tm=Ta*(1-f)+Tb*f;P.line([Sa,Sb],[Ta,Tb],C.muted,1.5,[5,4]);P.dot(Sa,Ta,C.blue,7);P.dot(Sb,Tb,C.orange,7);P.dot(Sm,Tm,C.red,7);P.text('A',Sa+0.06,Ta+1,C.blue);P.text('B',Sb+0.06,Tb+1,C.orange);P.text('mix',Sm+0.06,Tm+1,C.red);
 const fs=M.linspace(0,1,100),sg=fs.map(g=>rho(Sa*(1-g)+Sb*g,Ta*(1-g)+Tb*g)-1000),lin=fs.map(g=>(rho(Sa,Ta)*(1-g)+rho(Sb,Tb)*g)-1000);
 const lo=Math.min(...sg,...lin),hi=Math.max(...sg,...lin),pad=Math.max(0.05,(hi-lo)*0.15);P2.set({ymin:lo-pad,ymax:hi+pad});P2.clear();P2.line(fs,lin,C.muted,2,[5,4]);P2.line(fs,sg,C.red,3);P2.dot(f,rho(Sm,Tm)-1000,C.red,7);
 P2.legend([['linear average of the two σ',C.muted,[5,4]],['σ of the mixture',C.red]],P2.o.ml+8,P2.o.mt+14);
 const ra=rho(Sa,Ta)-1000,rb=rho(Sb,Tb)-1000,rm=rho(Sm,Tm)-1000,ex=rm-(ra*(1-f)+rb*f);
 out.textContent=`σ_A = ${M.fmt(ra,4)}, σ_B = ${M.fmt(rb,4)}, mixture (${M.fmt(Tm,3)} °C, S = ${M.fmt(Sm,4)}) σ = ${M.fmt(rm,4)}: ${M.fmt(ex,2)} kg m⁻³ denser than the linear average (cabbeling).  Freezing point at S_A: ${M.fmt(tf(Sa),3)} °C.`}
draw();
ui.note('CL25 §6 and §8. EOS-80 polynomial recalled, validated against Joy’s TEOS-10 values in scripts/fig_cl25.py (freezing point −1.92 °C at S = 35; ρα, ρβ at 25 and 0 °C; σ 26.4 for the N Pacific cooled to freezing).');
