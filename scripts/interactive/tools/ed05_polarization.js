//META {"title":"Polarization of light: from linear through elliptical to circular","desc":"E = (a₁ cos(ωt), a₂ cos(ωt + δ)) for a wave travelling along z. The tip of E traces a straight line, an ellipse or a circle. Change the two amplitudes and the phase lag δ; the Stokes parameters, the sense of rotation (helicity) and the ellipse axes are shown live. Right: the instantaneous wave along z as a spiral.","vault":"ED","chapters":["ED05 Electromagnetic Waves in Vacuum"],"tryit":"δ = 0: linear. δ = 90° with a₁ = a₂: circular. Keep δ = 90° and shrink a₂: elliptical with axes along x and y. Choose δ = 60°, a₁ = 3, a₂ = 4 for the Stokes numbers in ED05."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-1.3,xmax:1.3,ymin:-1.3,ymax:1.3,axes:false,equal:true});
const P2=ui.canvas(340,{xmin:0,xmax:2.2,ymin:-1.3,ymax:1.3,xlabel:'z / λ (wave moving to the right)',ylabel:'E_x, E_y',title:'E along z at the instant shown'});
const s1=ui.slider('a₁ (x amplitude)',0,1,0.01,0.75,draw),s2=ui.slider('a₂ (y amplitude)',0,1,0.01,1,draw),sd=ui.slider('phase lag δ (deg)',-180,180,1,90,draw);
ui.button('linear H',()=>{s1.value=1;s2.value=0;sd.value=0;draw()});ui.button('linear +45°',()=>{s1.value=.7;s2.value=.7;sd.value=0;draw()});ui.button('circular',()=>{s1.value=.8;s2.value=.8;sd.value=90;draw()});ui.button('elliptical',()=>{s1.value=.5;s2.value=1;sd.value=60;draw()});
const out=ui.readout();let t=0;
function draw(){const a1=s1.value,a2=s2.value,d=sd.value*Math.PI/180;P1.clear();P1.arrow(-1.2,0,1.2,0,C.grid,1);P1.arrow(0,-1.2,0,1.2,C.grid,1);
 const ph=M.linspace(0,2*Math.PI,200);P1.line(ph.map(p=>a1*Math.cos(p)),ph.map(p=>a2*Math.cos(p+d)),C.blue,2,[6,3]);
 const ex=a1*Math.cos(t),ey=a2*Math.cos(t+d);P1.arrow(0,0,ex,ey,C.orange,3,10);P1.circle(ex,ey,5,C.orange);
 P1.ptext('E_x',P1.X(1.25),P1.Y(0)-10,C.muted);P1.ptext('E_y',P1.X(0)+8,P1.Y(1.25),C.muted);
 const zs=M.linspace(0,2.2,300);P2.clear();const k=2*Math.PI;P2.line(zs,zs.map(z=>a1*Math.cos(t-k*z)),C.blue,2);P2.line(zs,zs.map(z=>a2*Math.cos(t-k*z+d)),C.orange,2);
 P2.legend([['E_x',C.blue],['E_y',C.orange]],P2.w-90,P2.o.mt+14);
 const s0=a1*a1+a2*a2,sA=a1*a1-a2*a2,sB=2*a1*a2*Math.cos(d),sC=2*a1*a2*Math.sin(d);
 const tilt=0.5*Math.atan2(sB,sA),chi=0.5*Math.asin(M.clamp(sC/(s0||1),-1,1));
 const hel=sC>1e-9?'counter-clockwise looking into the wave (positive helicity, "left" circular in optics)':sC<-1e-9?'clockwise looking into the wave (negative helicity)':'linear (no rotation)';
 out.textContent=`Stokes: s₀ = ${M.fmt(s0,4)}  s₁ = ${M.fmt(sA,4)}  s₂ = ${M.fmt(sB,4)}  s₃ = ${M.fmt(sC,4)}   s₀² − s₁² − s₂² − s₃² = ${M.fmt(s0*s0-sA*sA-sB*sB-sC*sC,2)} (0 for fully polarized)\nellipse tilt ψ = ${M.fmt(tilt*180/Math.PI,4)}°   ellipticity angle χ = ${M.fmt(chi*180/Math.PI,4)}°   axis ratio b/a = ${M.fmt(Math.abs(Math.tan(chi)),4)}\nsense: ${hel}`}
loop((dt)=>{t+=dt*2.2;draw()});draw();
ui.note('Sign convention: E = Re[(a₁, a₂e^{iδ})e^{-iωt}] would reverse the rotation sense, here the argument is ωt + δ with the wave travelling toward +z (phase kz − ωt → shown at fixed z as ωt). ED05 Worked example 7: a₁ = 3, a₂ = 4, δ = 60° → s = (25, −7, 12, 20.78).');
