//META {"title":"Ideal gas processes and the Carnot cycle on a P–V diagram","desc":"One mole of ideal gas (choose monatomic γ = 5/3 or diatomic γ = 7/5) goes around a Carnot cycle: isothermal expansion at T_h, adiabatic expansion, isothermal compression at T_c, adiabatic compression. The enclosed area is the net work; the efficiency is 1 − T_c/T_h whatever the gas or the volumes. Watch the state point travel and the heat and work tally.","vault":"TH","chapters":["TH03 The Ideal Gas and Adiabatic Processes","TH04 The Second Law Carnot Engines and Entropy"],"tryit":"Increase T_h: the cycle widens and η rises. Change the volume ratio: Q_h and W change but η does not. Compare γ = 5/3 and 7/5: different adiabat steepness, same efficiency."}
ui.gridOf(2);const P1=ui.canvas(360,{xmin:0,xmax:10,ymin:0,ymax:10,xlabel:'V (L)',ylabel:'P (atm)',title:'P–V diagram'});const P2=ui.canvas(360,{xmin:0,xmax:1,ymin:0,ymax:1,axes:false});
const sTh=ui.slider('T_hot (K)',350,900,5,600,draw),sTc=ui.slider('T_cold (K)',150,340,5,300,draw),sV=ui.slider('V₁ (L), start of isothermal expansion',2,6,0.1,3,draw),sr=ui.slider('isothermal expansion ratio V₂/V₁',1.2,4,0.05,2,draw),gm=ui.select('gas',[['1.6667','monatomic γ = 5/3'],['1.4','diatomic γ = 7/5']],draw,'1.6667');
const out=ui.readout();const R=0.082057,Rj=8.314;let phase=0;
function states(){const Th=sTh.value,Tc=sTc.value,V1=sV.value,r=sr.value,g=parseFloat(gm.value);const V2=V1*r;const V3=V2*Math.pow(Th/Tc,1/(g-1)),V4=V1*Math.pow(Th/Tc,1/(g-1));return{Th,Tc,V1,V2,V3,V4,g,r}}
function draw(){const s=states();const P=(V,T)=>R*T/V;const seg=[];const n=80;
 const A=M.linspace(s.V1,s.V2,n).map(V=>[V,P(V,s.Th)]);const B=M.linspace(s.V2,s.V3,n).map(V=>[V,P(s.V2,s.Th)*Math.pow(s.V2/V,s.g)]);const Cc=M.linspace(s.V3,s.V4,n).map(V=>[V,P(V,s.Tc)]);const D=M.linspace(s.V4,s.V1,n).map(V=>[V,P(s.V4,s.Tc)*Math.pow(s.V4/V,s.g)]);
 const pts=[...A,...B,...Cc,...D];P1.set({xmax:Math.max(...pts.map(p=>p[0]))*1.1,ymax:Math.max(...pts.map(p=>p[1]))*1.15,xmin:0,ymin:0});P1.clear();
 P1.poly(pts,'rgba(42,120,214,0.15)',null);P1.line(A.map(p=>p[0]),A.map(p=>p[1]),C.red,3);P1.line(B.map(p=>p[0]),B.map(p=>p[1]),C.violet,3);P1.line(Cc.map(p=>p[0]),Cc.map(p=>p[1]),C.blue,3);P1.line(D.map(p=>p[0]),D.map(p=>p[1]),C.aqua,3);
 [['1',A[0]],['2',B[0]],['3',Cc[0]],['4',D[0]]].forEach(([n,p])=>P1.dot(p[0],p[1],C.ink,5));
 P1.legend([['1→2 isothermal at T_h (Q in)',C.red],['2→3 adiabatic',C.violet],['3→4 isothermal at T_c (Q out)',C.blue],['4→1 adiabatic',C.aqua]],P1.o.ml+P1.w*0.38,P1.o.mt+14);
 const idx=Math.floor(phase)%(4*n),q=pts[idx];P1.dot(q[0],q[1],C.orange,8);
 const Qh=Rj*s.Th*Math.log(s.r),Qc=Rj*s.Tc*Math.log(s.r),W=Qh-Qc,eta=W/Qh;
 // 2nd panel: bar chart of Q_h, Q_c, W and entropy changes
 P2.clear();const g=P2.g,W2=P2.w,H2=P2.h;const mx=Math.max(Qh,1);const bars=[['Q_h',Qh,C.red],['Q_c',Qc,C.blue],['W',W,C.orange]];bars.forEach(([nm,v,c],i)=>{const h=(H2*0.5)*v/mx,x=40+i*(W2-80)/3;g.fillStyle=c;g.fillRect(x,H2*0.62-h,(W2-80)/3-14,h);P2.ptext(nm+' = '+M.fmt(v,4)+' J',x,H2*0.62+14,C.ink,'left')});
 P2.ptext('entropy: ΔS (1→2) = Q_h/T_h = '+M.fmt(Qh/s.Th,4)+' J/K,  ΔS (3→4) = −Q_c/T_c = '+M.fmt(-Qc/s.Tc,4)+' J/K,  total over cycle = 0',W2/2,H2*0.80,C.ink,'center','12px system-ui');
 P2.ptext('η = W/Q_h = 1 − T_c/T_h = '+M.fmt(eta,4),W2/2,H2*0.90,C.orange,'center','15px system-ui');
 out.textContent=`V₂ = ${M.fmt(s.V2,4)} L   V₃ = ${M.fmt(s.V3,4)} L   V₄ = ${M.fmt(s.V4,4)} L   (V₃/V₂ = V₄/V₁ = (T_h/T_c)^{1/(γ−1)} = ${M.fmt(Math.pow(s.Th/s.Tc,1/(s.g-1)),4)}, so V₂/V₁ = V₃/V₄)\nQ_h = nRT_h ln(V₂/V₁) = ${M.fmt(Qh,5)} J   Q_c = nRT_c ln(V₃/V₄) = ${M.fmt(Qc,5)} J   W = ${M.fmt(W,5)} J   Q_h/T_h − Q_c/T_c = ${M.fmt(Qh/s.Th-Qc/s.Tc,2)}  (Clausius equality)`}
loop((dt)=>{phase+=dt*60;draw()});draw();
ui.note('Adiabats: PVᵞ = const and TVᵞ⁻¹ = const. The cycle area ∮P dV = W. For γ = 5/3, T_h = 600 K, T_c = 300 K: V₃/V₂ = 2^{1.5} = 2.83.');
