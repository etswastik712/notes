//META {"title": "Depth sets the timescale, not the size of the slow swings: weather-kicked slabs", "desc": "A slab with heat capacity C and restoring strength λ obeys C dT′/dt = F′ − λT′. For a white random push F′ the temperature power at angular frequency ω is ∝ 1/(ω²C² + λ²): for fast swings it falls as 1/C² (more depth, much less power), for slow swings C drops out and the power is the same for any depth. The bend is at period 2πτ with τ = C/λ. Add a deep ocean (heat capacity C_d exchanging γ W m⁻² K⁻¹ with the mixed layer) and the slowest swings are calmed by about a third.", "vault": "CL", "chapters": ["CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia", "CL27 Tutorials I - Daisyworld with Land and Ocean"], "tryit": "Defaults (mixed layer 75 m, b = 2.09, land 10⁷ J m⁻² K⁻¹): the mixed layer has ≈ 470× less power than land at 1 year and the same power (0.99) at 300 years. Change the depth: the fast end moves, the slow plateau does not. Tick the deep ocean: the plateau falls to ≈ 0.55 of land's at the slowest periods."}
ui.gridOf(2);
const P1=ui.canvas(380,{xmin:-1.3,xmax:3.3,ymin:-5,ymax:0.5,xlabel:'log₁₀ period (yr)',ylabel:'log₁₀ power / slow-limit power of land',title:'temperature power of weather-kicked slabs'});
const P2=ui.canvas(380,{xmin:0,xmax:3,ymin:0,ymax:4,xlabel:'log₁₀ period (yr)',ylabel:'response relative to the push',title:'(C ω)/λ : where the slab stops following'});
const sh=ui.slider('mixed-layer depth H (m)',5,500,5,75,draw),sb=ui.slider('feedback λ = b (W m⁻² K⁻¹)',1,6,0.05,2.09,draw),sg=ui.slider('mixed–deep exchange γ (W m⁻² K⁻¹)',0.1,3,0.05,0.7,draw);
const sd=ui.check('add the deep ocean (C_d = 4.2×10⁹ J m⁻² K⁻¹)',false,draw);const out=ui.readout();
const YR=3.156e7,CL=1e7,CD=4.2e9,rc=4.2e6;
function mag2(re,im){return re*re+im*im}
function draw(){const H=sh.value,b=sb.value,g=sg.value,deep=sd.value,Cm=rc*H;const ps=M.linspace(-1.3,3.3,240);
 const pl=[],pm=[],pd=[];for(const lp of ps){const w=2*Math.PI/(Math.pow(10,lp)*YR);
  const L=mag2(b,w*CL),Mx=mag2(b,w*Cm);let D=NaN;if(deep){// Z = i w Cm + b + g * i w Cd/(i w Cd + g)
   const den=mag2(g,w*CD),re=g*(w*CD)*(w*CD)/den,im=g*g*(w*CD)/den;D=mag2(b+re,w*Cm+im)}
  const ref=b*b;pl.push(Math.log10(ref/L));pm.push(Math.log10(ref/Mx));pd.push(deep?Math.log10(ref/D):NaN)}
 P1.clear();P1.line(ps,pl,C.orange,3);P1.line(ps,pm,C.blue,3);if(deep)P1.line(ps,pd,C.aqua,3);
 const tl=CL/b/YR,tm=Cm/b/YR;P1.vline(Math.log10(2*Math.PI*tl),C.orange);P1.vline(Math.log10(2*Math.PI*tm),C.blue);
 P1.legend([['land (C = 10⁷)',C.orange],['mixed layer',C.blue],['+ deep ocean',C.aqua]],P1.o.ml+8,P1.o.mt+14);
 const lp=M.linspace(0,3,200);P2.clear();P2.line(lp,lp.map(l=>Cm*2*Math.PI/(Math.pow(10,l)*YR)/b),C.blue,3);P2.line(lp,lp.map(l=>CL*2*Math.PI/(Math.pow(10,l)*YR)/b),C.orange,3);P2.hline(1,C.red);P2.text('Cω/λ = 1: the slab just keeps up',1.6,1.15,C.red);
 const w1=2*Math.PI/YR,w3=2*Math.PI/(300*YR);const r1=mag2(b,w1*CL)/mag2(b,w1*Cm),r3=mag2(b,w3*CL)/mag2(b,w3*Cm);
 out.textContent=`τ_land = ${M.fmt(tl*365.25,3)} d, τ_mixed = ${M.fmt(tm,3)} yr (bend at period 2πτ = ${M.fmt(2*Math.PI*tm,3)} yr);  P_mixed/P_land = 1/${M.fmt(1/r1,3)} at 1 yr and ${M.fmt(r3,3)} at 300 yr;  fast limit (C_land/C_mixed)² = 1/${M.fmt((Cm/CL)**2,3)}.`}
draw();
ui.note('CL23 §7 (Hasselmann). White push, Welch-free analytic spectra: Verified against scripts/joy_inertia_numbers.py: 1/473 at 1 yr, 1/184 at 2 yr, 0.99 at 300 yr for the app numbers.');
