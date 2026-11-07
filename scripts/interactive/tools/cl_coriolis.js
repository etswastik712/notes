//META {"title":"Rotation and the wind: Coriolis, inertial oscillations, geostrophic balance","desc":"On a rotating planet a free particle in the horizontal plane moves in inertial circles of radius v/f with period 2π/f, f = 2Ω sin φ (left panel, in the rotating frame). Right: a steady wind in balance between the pressure-gradient force and the Coriolis force blows along the isobars (geostrophic), with low pressure on its left in the Northern Hemisphere; friction turns it across the isobars toward low pressure.","vault":"CL","chapters":["CL12 Rotating Frames and the Coriolis Force","CL13 Horizontal Motion - Geostrophic Balance and Friction"],"tryit":"Move the latitude from 45° N to the equator: f → 0 and the inertial radius diverges (no rotation felt). Go to the Southern Hemisphere: the circles reverse and the geostrophic wind flips. Slide friction up: the wind crosses the isobars."}
ui.gridOf(2);const P1=ui.canvas(360,{xmin:-1,xmax:1,ymin:-1,ymax:1,axes:false,equal:true});const P2=ui.canvas(360,{xmin:-1.3,xmax:1.3,ymin:-1.3,ymax:1.3,axes:false,equal:true});
const sl=ui.slider('latitude φ (deg, − = south)',-90,90,1,45,draw),sv=ui.slider('speed v (m/s)',5,60,1,20,draw),sf=ui.slider('friction angle toward low pressure (deg)',0,45,1,0,draw);
const out=ui.readout();const Om=7.2921e-5;let t=0,tr=[];
function draw(){const phi=sl.value*Math.PI/180,f=2*Om*Math.sin(phi),v=sv.value;P1.clear();const rr=Math.abs(f)>1e-9?v/Math.abs(f):Infinity;
 const sc=0.8/Math.max(1,Math.min(rr/1e5,1e9));// show in units of 100 km, auto-scaled
 const Rkm=rr/1000;const rd=Math.min(Rkm,2000);const S=0.45/(Math.min(Rkm,1000)||1);
 P1.ptext('inertial oscillation, rotating frame (anticyclonic: clockwise in N, counter-clockwise in S)',P1.w/2,12,C.muted,'center','11px system-ui');
 if(Math.abs(f)>1e-8){const ph=M.linspace(0,2*Math.PI,200),sgn=-Math.sign(f);const R=0.45;P1.line(ph.map(p=>R*Math.cos(p)),ph.map(p=>R*Math.sin(p)),C.blue,3);const a=t*Math.abs(f)*2000;const x=R*Math.cos(sgn*a-0.0)*1,y=R*Math.sin(sgn*a);P1.circle(x,y,8,C.orange,C.ink);P1.arrow(x,y,x-sgn*0.28*Math.sin(sgn*a),y+sgn*0.28*Math.cos(sgn*a)*1,C.red,3,9);P1.ptext('radius v/|f| = '+M.fmt(Rkm,4)+' km',P1.w/2,P1.h-12,C.ink,'center')}else P1.ptext('f ≈ 0 at the equator: straight lines (no inertial circle)',P1.w/2,P1.h/2,C.red,'center','14px system-ui');
 // geostrophic diagram
 P2.clear();const sg=Math.sign(f)||1;const fr=sf.value*Math.PI/180;
 // isobars horizontal lines, low pressure toward top (north) if NH wind flows east with low on left? set pressure gradient force pointing toward low = up
 for(let i=-4;i<=4;i++){P2.line([-1.25,1.25],[i*0.3,i*0.3],C.grid,2)}
 P2.ptext('LOW',P2.X(0),P2.Y(1.2),C.blue,'center','13px system-ui');P2.ptext('HIGH',P2.X(0),P2.Y(-1.2),C.red,'center','13px system-ui');
 // wind direction: in NH low pressure on left of wind: wind toward +x if low is up (left of east is north). In SH low on the right -> wind toward -x
 const wdir=sg>0?1:-1,ang=wdir>0?fr:Math.PI-fr*1;// friction rotates toward low (up)
 const wx=Math.cos(wdir>0?fr:Math.PI-fr),wy=Math.sin(wdir>0?fr:Math.PI-fr);
 P2.arrow(0,0,wx*0.9,wy*0.9,C.orange,4,12);P2.ptext('wind',P2.X(wx*0.9)+6,P2.Y(wy*0.9)-12,C.orange);
 P2.arrow(0,0,0,0.7,C.blue,3,11);P2.ptext('pressure-gradient force',P2.X(0.03),P2.Y(0.75),C.blue,'left');
 // Coriolis force perpendicular to wind (to the right in NH): -sg * (-wy, wx)... right of wind in NH
 const cx=sg*wy,cy=-sg*wx;P2.arrow(0,0,cx*0.7,cy*0.7,C.aqua,3,11);P2.ptext('Coriolis',P2.X(cx*0.7)+6,P2.Y(cy*0.7),C.aqua);
 if(fr>0.01){P2.arrow(0,0,-wx*0.5,-wy*0.5,C.violet,3,10);P2.ptext('friction',P2.X(-wx*0.5)-6,P2.Y(-wy*0.5),C.violet,'right')}
 const ug=Math.abs(f)>1e-8?'geostrophic wind V = |∇p|/(ρ|f|)':'no geostrophic balance at the equator';
 out.textContent=`φ = ${M.fmt(sl.value,3)}°   f = 2Ω sin φ = ${M.fmt(f,4)} s⁻¹   inertial period 2π/|f| = ${Math.abs(f)>1e-8?M.fmt(2*Math.PI/Math.abs(f)/3600,4)+' h':'∞'} (pendulum day = 12 h/sin φ)\n${ug}: in the ${f>=0?'Northern':'Southern'} Hemisphere the wind keeps low pressure on its ${f>=0?'left':'right'}; Coriolis acts to the ${f>=0?'right':'left'} of the motion.`}
loop((dt)=>{t+=dt;draw()});draw();
ui.note('Ω = 7.292×10⁻⁵ s⁻¹. At v = 20 m/s, φ = 45°: f = 1.03×10⁻⁴ s⁻¹ → inertial radius 194 km, period 16.9 h (CL12). Geostrophic balance: fk × V = −(1/ρ)∇p (CL13).');
