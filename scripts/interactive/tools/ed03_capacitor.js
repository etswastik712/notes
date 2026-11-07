//META {"title":"Displacement current: charging a capacitor","desc":"A circular parallel-plate capacitor (plate radius R) is charged by a steady current I. Ampère's law needs both the conduction current through a loop and the displacement current ε₀ dΦ_E/dt: with the flat disc surface the whole answer comes from the displacement term, with the balloon surface through the wire from the conduction current. Move the Amperian loop and compare B(r) with and without the displacement term.","vault":"ED","chapters":["ED03 Maxwell's Equations and Boundary Conditions"],"tryit":"Drag r across the plate radius R: B grows linearly inside the gap (only the part of the displacement current enclosed counts) and falls as 1/r outside, joining the wire's field. Untick 'include displacement current' to see Ampère's law fail (B = 0 in the gap)."}
ui.gridOf(2);const P1=ui.canvas(320,{xmin:-1.7,xmax:1.7,ymin:-1.5,ymax:1.5,axes:false,equal:true});
const P2=ui.canvas(320,{xmin:0,xmax:15,ymin:0,ymax:9,xlabel:'loop radius r (cm)',ylabel:'B (µT)',title:'B(r) around the axis'});
const sr=ui.slider('Amperian loop radius r (cm)',0.2,15,0.1,2,draw),sI=ui.slider('charging current I (A)',0.5,5,0.1,2,draw),cb=ui.check('include displacement current',true,draw);
const out=ui.readout();const R=5,mu0=4e-7*Math.PI,e0=8.854e-12;
function Bof(r,I,disp){const rm=r/100,Rm=R/100;const enc=disp?(r<=R?I*(r/R)**2:I):0;return mu0*enc/(2*Math.PI*rm)*1e6}
function draw(){const r=sr.value,I=sI.value,d=cb.value;P1.clear();
 // side view schematic: plates, wire, loop circle shown face-on
 P1.ptext('face-on view of the gap: plates (grey disc), loop (blue)',P1.w/2,12,C.muted,'center');
 P1.circle(0,0,P1.X(1)-P1.X(0),C.panel,C.muted,2);P1.circle(0,0,(P1.X(1)-P1.X(0))*Math.min(r/R,1.55*1.0),null,C.blue,3);
 const rr=Math.min(r/R,1.55);for(let k=0;k<8;k++){const a=k*Math.PI/4;P1.arrow(rr*Math.cos(a)-0.0,rr*Math.sin(a),rr*Math.cos(a)-0.28*Math.sin(a),rr*Math.sin(a)+0.28*Math.cos(a),C.orange,2,6)}
 P1.ptext('E (out of page) grows as charge builds up',P1.w/2,P1.h-10,C.muted,'center');
 for(let i=0;i<16;i++)P1.ptext('⊙',P1.X(((i%4)-1.5)*0.4),P1.Y((Math.floor(i/4)-1.5)*0.4),C.muted,'center','14px system-ui');
 P2.clear();const rs=M.linspace(0.05,15,300);P2.set({ymax:Math.max(9,Bof(R,I,true)*1.15)});P2.clear();
 P2.line(rs,rs.map(x=>Bof(x,I,true)),C.blue,3);P2.line(rs,rs.map(x=>Bof(x,I,false)),C.red,2,[5,4]);P2.vline(R,C.muted);P2.text('R',R+0.2,P2.o.ymax*0.93,C.muted);P2.dot(r,Bof(r,I,d),C.orange,6);
 P2.legend([['with displacement current',C.blue],['conduction current only (wrong)',C.red,[5,4]]],P2.w*0.45,P2.o.mt+14);
 const Id=r<=R?I*(r/R)**2:I;out.textContent=`r = ${M.fmt(r,3)} cm   enclosed displacement current I_d = I(r/R)² = ${M.fmt(Id,4)} A (r<R) ; = I (r>R)\nB(r) = μ₀ I_enc/(2πr) = ${M.fmt(Bof(r,I,d),4)} µT   ${d?'':'(without ε₀dΦ_E/dt Ampère gives 0 in the gap: inconsistent)'}\nflat disc surface: I_conduction = 0, ε₀ dΦ_E/dt = ${M.fmt(Id,4)} A;  balloon through the wire: I_conduction = ${M.fmt(I,3)} A, displacement = 0  → same B`}
draw();ui.note('Checks vs ED03 Worked example 1: R = 5 cm, I = 2 A: B(2 cm) = 3.20 µT, B(5 cm) = 8.0 µT, B(10 cm) = 4.0 µT, dE/dt = 2.876×10¹³ V m⁻¹ s⁻¹.');
