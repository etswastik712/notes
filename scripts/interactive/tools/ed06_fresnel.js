//META {"title":"Reflection and refraction: Snell, Fresnel, Brewster, total internal reflection","desc":"A plane wave meets a flat interface between media of index n₁ and n₂. Set the angle of incidence: the rays show the reflected and transmitted directions (Snell), the curves show the reflected fraction for E parallel and perpendicular to the plane of incidence (Fresnel), with the Brewster and critical angles marked. Beyond the critical angle the transmitted wave becomes an evanescent field with the decay length shown.","vault":"ED","chapters":["ED06 Waves in Matter, Reflection and Dispersion"],"tryit":"n₁ = 1, n₂ = 1.5: the parallel curve touches zero at the Brewster angle 56.3°. Swap to n₁ = 1.5, n₂ = 1: total internal reflection beyond 41.8°, with an evanescent decay length ~λ/(2π√(sin²θ − sin²θ_c))."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-1.5,xmax:1.5,ymin:-1.2,ymax:1.2,axes:false,equal:true});
const P2=ui.canvas(340,{xmin:0,xmax:90,ymin:0,ymax:1,xlabel:'angle of incidence (deg)',ylabel:'reflected fraction R',title:'Fresnel reflectance'});
const sn1=ui.slider('n₁ (incident medium)',1,2.5,0.01,1,draw),sn2=ui.slider('n₂',1,2.5,0.01,1.5,draw),st=ui.slider('angle of incidence θ (deg)',0,89,0.5,40,draw);
const out=ui.readout();
function fres(th,n1,n2){const ti=th*Math.PI/180,st=n1/n2*Math.sin(ti);if(st>=1)return[1,1,true];const ct=Math.sqrt(1-st*st),ci=Math.cos(ti);const rs=(n1*ci-n2*ct)/(n1*ci+n2*ct),rp=(n2*ci-n1*ct)/(n2*ci+n1*ct);return[rs*rs,rp*rp,false]}
function draw(){const n1=sn1.value,n2=sn2.value,th=st.value,ti=th*Math.PI/180;P1.clear();
 P1.poly([[-1.5,0],[1.5,0],[1.5,-1.2],[-1.5,-1.2]],C.panel,null);P1.line([-1.5,1.5],[0,0],C.ink,2);P1.line([0,0],[-1.1,1.1],C.grid,1,[3,3]);
 P1.ptext('n₁ = '+M.fmt(n1,3),P1.X(-1.4),P1.Y(1.05),C.muted);P1.ptext('n₂ = '+M.fmt(n2,3),P1.X(-1.4),P1.Y(-1.05),C.muted);
 const[Rs,Rp,tir]=fres(th,n1,n2);
 P1.arrow(-Math.sin(ti)*1.1,Math.cos(ti)*1.1,0,0,C.blue,3,10);P1.arrow(0,0,Math.sin(ti)*1.1,Math.cos(ti)*1.1,C.orange,3,10);
 const sth=n1/n2*Math.sin(ti);if(sth<1){const tt=Math.asin(sth);P1.arrow(0,0,Math.sin(tt)*1.1,-Math.cos(tt)*1.1,C.aqua,3,10)}else{for(let i=0;i<7;i++){const len=0.55*Math.exp(-i/2);P1.line([0.08,0.08+len],[-0.12*(i+1),-0.12*(i+1)],C.aqua,3)}P1.ptext('evanescent field',P1.X(0.9),P1.Y(-0.4),C.aqua,'left')}
 P2.clear();const ths=M.linspace(0,89.9,400),Rv=ths.map(x=>fres(x,n1,n2));P2.line(ths,Rv.map(v=>v[0]),C.blue,2.5);P2.line(ths,Rv.map(v=>v[1]),C.orange,2.5);
 const tB=Math.atan(n2/n1)*180/Math.PI;P2.vline(tB,C.violet);P2.text('Brewster '+M.fmt(tB,4)+'°',tB+1,0.9,C.violet);
 if(n1>n2){const tc=Math.asin(n2/n1)*180/Math.PI;P2.vline(tc,C.red);P2.text('critical '+M.fmt(tc,4)+'°',tc-1,0.55,C.red,'right')}
 P2.dot(th,Rs,C.blue,5);P2.dot(th,Rp,C.orange,5);P2.legend([['E ⊥ plane of incidence',C.blue],['E ∥ plane of incidence',C.orange]],P2.o.ml+8,P2.o.mt+14);
 let s=`R_⊥ = ${M.fmt(Rs,4)}  R_∥ = ${M.fmt(Rp,4)}   (R+T = 1 for each polarization)\n`;
 if(tir){const sc=n2/n1,k=2*Math.PI/(600e-9/n1);const d=1/(k*Math.sqrt(Math.sin(ti)**2-sc*sc));s+=`TOTAL INTERNAL REFLECTION: transmitted wave is evanescent, decay length 1/(k√(sin²θ − sin²θ_c)) = ${M.fmt(d*1e9,4)} nm for λ₀ = 600 nm`}
 else s+=`refracted angle θ_t = ${M.fmt(Math.asin(sth)*180/Math.PI,4)}°  (n₁ sin θ = n₂ sin θ_t)   Brewster: tan θ_B = n₂/n₁ → ${M.fmt(tB,5)}°`;
 out.textContent=s}
draw();ui.note('Reflectances use r_⊥ = (n₁cosθ − n₂cosθ_t)/(n₁cosθ + n₂cosθ_t), r_∥ = (n₂cosθ − n₁cosθ_t)/(n₂cosθ + n₁cosθ_t) (equivalent to Griffiths (α−β)/(α+β) and Jackson (7.39)/(7.41) for μ = μ′). ED06 Worked example 2: n = 1 → 1.5 at 30°: R_⊥ = 0.0578, R_∥ = 0.0252.');
