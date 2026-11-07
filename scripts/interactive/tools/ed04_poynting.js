//META {"title":"Where does the energy flow? The Poynting vector","desc":"S = E × B/μ₀ shows the path of electromagnetic energy. In a current-carrying resistive wire the energy enters through the side, radially inward; in a charging capacitor it enters through the rim of the gap; in a plane wave it travels along k. Pick a scenario and adjust the numbers: the integral of S through the surface always equals the power delivered (VI, or dU/dt).","vault":"ED","chapters":["ED04 Conservation Laws - Energy, Momentum, Angular Momentum"],"tryit":"Wire: raise the current I and watch the inward flux keep equalling I²R. Capacitor: let the plates charge and compare the Poynting flux through the rim with dU/dt. Wave: check that S = c u for any polarisation."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-1.5,xmax:1.5,ymin:-1.2,ymax:1.2,axes:false,equal:true});
const P2=ui.canvas(340,{xmin:0,xmax:5,ymin:0,ymax:600,xlabel:'t (ns)',ylabel:'power (W)',title:'flux through the surface vs rate of energy change'});
const sc=ui.select('scenario',[['w','current-carrying resistive wire'],['c','charging capacitor gap'],['p','plane wave']],draw,'c'),sI=ui.slider('current I (A)',0.5,5,0.1,2,draw);
const out=ui.readout();const mu0=4e-7*Math.PI,e0=8.854e-12,c0=2.998e8;let t=0;
function draw(){const k=sc.value,I=sI.value;P1.clear();P2.clear();
 if(k==='w'){// wire along z, viewed in cross-section with S arrows inward; side view
  const a=1e-3,Lw=1,rho=1.68e-8,R=rho*Lw/(Math.PI*a*a),V=I*R,S=V*I/(2*Math.PI*a*Lw);P1.ptext('wire cross-section: E along the wire (out of page), B circles it, S = E×B/μ₀ points INWARD',P1.w/2,12,C.muted,'center','11px system-ui');
  P1.circle(0,0,(P1.X(1)-P1.X(0))*0.55,C.panel,C.ink,2);for(let i=0;i<12;i++){const a_=i*Math.PI/6;P1.arrow(1.35*Math.cos(a_),1.05*Math.sin(a_),0.7*Math.cos(a_),0.55*Math.sin(a_),C.orange,2.5,9)}
  P1.ptext('⊙ I',P1.X(0),P1.Y(0),C.ink,'center','16px system-ui');
  P2.set({ymax:Math.max(1,I*I*R*1.4)});P2.clear();P2.hline(I*I*R,C.blue);P2.text('flux through side = VI = I²R',0.2,I*I*R*1.1,C.blue);
  out.textContent=`copper wire a = 1 mm, L = 1 m: R = ${M.fmt(R*1e3,4)} mΩ  V = ${M.fmt(V*1e3,4)} mV   |S| at the surface = VI/(2πaL) = ${M.fmt(S,4)} W/m²   inward flux = ${M.fmt(S*2*Math.PI*a*Lw,4)} W = I²R = ${M.fmt(I*I*R,4)} W ✓`}
 else if(k==='c'){const Rc=0.05,d=2e-3,tt=t,ts=M.linspace(0,5e-9,50);const Et=x=>I*x/(e0*Math.PI*Rc*Rc);
  P1.ptext('capacitor gap seen from above: E (out of page) grows, B circles, S points inward at the rim',P1.w/2,12,C.muted,'center','11px system-ui');
  P1.circle(0,0,(P1.X(1)-P1.X(0))*0.7,C.panel,C.ink,2);for(let i=0;i<12;i++){const a_=i*Math.PI/6;P1.arrow(1.3*Math.cos(a_),1.0*Math.sin(a_),0.78*Math.cos(a_),0.55*Math.sin(a_),C.orange,2.5,9)}
  const pw=x=>Et(x)*I*d;const Utot=x=>0.5*e0*Et(x)**2*Math.PI*Rc*Rc*d;P2.set({xmax:5,ymax:pw(5e-9)*1.15});P2.clear();
  P2.line(ts.map(x=>x*1e9),ts.map(pw),C.blue,4);P2.line(ts.map(x=>x*1e9),ts.map(x=>(Utot(x+1e-12)-Utot(x-1e-12))/2e-12),C.orange,2,[6,3]);P2.legend([['Poynting flux through the rim',C.blue],['dU_E/dt',C.orange,[6,3]]],P2.o.ml+8,P2.o.mt+14);
  out.textContent=`R = 5 cm, d = 2 mm, I = ${M.fmt(I,3)} A:  at t = 1 ns  E = ${M.fmt(Et(1e-9),4)} V/m  V = Ed = ${M.fmt(Et(1e-9)*d,4)} V  P = E I d = ${M.fmt(pw(1e-9),5)} W = VI = dU/dt ✓ (B is constant in time here)`}
 else{const E0=100,u=e0*E0*E0;P1.ptext('plane wave: S = c u along k',P1.w/2,12,C.muted,'center');for(let i=0;i<14;i++){const x=-1.3+i*0.2;const ph=Math.cos(6*(x)-4*t);P1.arrow(x,0,x,0.9*ph,C.blue,2,6);P1.arrow(x,0,x-0.0,0,C.orange,0);P1.dot(x,0.0,C.muted,0)}
  P1.arrow(-1.3,-0.9,1.3,-0.9,C.red,3,12);P1.ptext('k, S',P1.X(1.0),P1.Y(-1.05),C.red);P2.set({ymax:300});P2.clear();const ts=M.linspace(0,5,200);P2.line(ts,ts.map(x=>c0*u*Math.cos(2*Math.PI*0.5*x)**2*0.001),C.blue,3);P2.hline(0.5*c0*u*0.001,C.orange);P2.ptext('S(t) ∝ cos²  (orange: average)',P2.o.ml+8,P2.o.mt+14,C.ink);
  out.textContent=`E₀ = 100 V/m: u = ε₀E₀² cos² (peak ${M.fmt(u,4)} J/m³),  S = c u,  ⟨S⟩ = ½cε₀E₀² = ${M.fmt(0.5*c0*u,4)} W/m²,  momentum density g = S/c² = ${M.fmt(0.5*u/c0,4)} kg m⁻² s⁻¹ (avg)`}}
loop((dt)=>{t+=dt;draw()});draw();
ui.note('ED04 Worked examples 1–3: wire power 0.535 W for I = 10 A (a = 1 mm); capacitor gap P = 115.04 W at t = 1 ns for I = 2 A; cable power IV.');
