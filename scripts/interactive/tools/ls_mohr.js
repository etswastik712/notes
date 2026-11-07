//META {"title":"Mohr's circle and Coulomb failure: why faults dip at about 60°","desc":"Principal stresses σ₁ > σ₃ define a circle of all possible (normal stress, shear stress) pairs on planes through a point. Pore-fluid pressure P shifts the circle toward lower effective normal stress. The rock fails on a plane when the circle touches the Coulomb envelope τ = C + f σ_n (f = tan φ) and the first plane to fail has its normal at 45° + φ/2 from σ₁, i.e. the plane itself is 45° − φ/2 from σ₁ (≈ 30° for f = 0.6). Left: the circle and the envelope; right: the sample with the failure plane.","vault":"LS","chapters":["LS09 Faults and Earthquakes","LS02 Mechanics and Mathematics Toolkit","LS13 Landslides"],"tryit":"C = 0.3, f = 0.6 and σ₃ = 1: increase σ₁ until the circle touches the line; the failure plane is 29.5° from σ₁ (φ = 31°). Increase the pore pressure and the circle slides left into failure without changing σ₁ − σ₃: the mechanism of injection-induced earthquakes. C = 0: σ₁/σ₃ at failure = 3.1."}
ui.gridOf(2);const P1=ui.canvas(350,{xmin:-0.5,xmax:8,ymin:-0.2,ymax:4.2,xlabel:'normal stress σ_n (effective)',ylabel:'shear stress τ',title:'Mohr circle and Coulomb envelope',equal:true});const P2=ui.canvas(350,{xmin:-2,xmax:2,ymin:-2,ymax:2,axes:false,equal:true,title:'the sample: σ₁ vertical, a plane at angle β from σ₁'});
const s1=ui.slider('σ₁ (stress units)',1,12,0.05,4,draw),s3=ui.slider('σ₃',0.1,6,0.05,1,draw),sp=ui.slider('pore pressure P',0,5,0.05,0,draw),sc=ui.slider('cohesion C',0,1,0.01,0.3,draw),sf=ui.slider('friction coefficient f = tan φ',0.2,1,0.01,0.6,draw),sth=ui.slider('plane normal angle θ from σ₁ (deg)',0,90,0.5,60.5,draw);
const out=ui.readout();
function draw(){const S1=s1.value,S3=Math.min(s3.value,S1-0.01),P=sp.value,C=sc.value,f=sf.value,th=sth.value*Math.PI/180;const e1=S1-P,e3=S3-P;const cen=(e1+e3)/2,R=(e1-e3)/2;const phi=Math.atan(f),cosphi=Math.cos(phi),sinphi=Math.sin(phi);
 P1.set({xmin:-1,xmax:Math.max(8,e1+1),ymin:-0.2,ymax:Math.max(4.2,R*1.3,C+f*8)});P1.clear();P1.line([-1,P1.o.xmax],[C+f*-1,C+f*P1.o.xmax],C_env(),3);function C_env(){return C0()}function C0(){return '#d6453d'}
 P1.hline(0,C.ink0||'#888');
 const th_=M.linspace(0,Math.PI,200);P1.line(th_.map(a=>cen+R*Math.cos(a)),th_.map(a=>R*Math.sin(a)),C_blue(),3);function C_blue(){return '#2a78d6'}
 // plane point: sigma_n = cen + R cos(2θ'), where 2θ is measured from sigma_1 axis (angle between normal and sigma1 is θ): sigma_n = cen + R cos 2θ ; tau = R sin 2θ
 const sn=cen+R*Math.cos(2*th),ta=R*Math.sin(2*th);P1.dot(sn,ta,'#e08a1e',8);P1.line([cen,sn],[0,ta],'#999',1.5,[3,3]);
 // failure margin: distance from centre to envelope line
 const dist=(C+f*cen)*cosphi;// perpendicular distance from (cen,0) to line tau = C + f sigma_n
 const touching=R>=dist-1e-3;const thF=(Math.PI/4+phi/2);
 P1.vline(0,'#bbb');
 P2.clear();const G=P2.g;
 // sample drawn as rectangle with plane at angle beta=90-theta from sigma1 (vertical)
 const beta=Math.PI/2-th;G.save();P2.poly([[-1,-1.5],[1,-1.5],[1,1.5],[-1,1.5]],'rgba(150,110,70,0.30)',C_ink());function C_ink(){return '#444'}
 // plane through centre making angle beta with vertical (sigma1)
 const dx=Math.sin(beta),dy=Math.cos(beta);P2.line([-1.4*dx,1.4*dx],[-1.4*dy,1.4*dy],touching?'#d6453d':'#e08a1e',4);
 P2.arrow(0,1.9,0,1.55,'#2a78d6',3,9);P2.arrow(0,-1.9,0,-1.55,'#2a78d6',3,9);P2.arrow(-1.9,0,-1.15,0,'#1baf7a',3,9);P2.arrow(1.9,0,1.15,0,'#1baf7a',3,9);P2.text('σ₁',0.12,1.85,'#2a78d6');P2.text('σ₃',1.55,0.15,'#1baf7a');P2.text('β = '+M.fmt(beta*180/Math.PI,3)+'° from σ₁',-1.7,-1.8,C_ink());
 G.restore();
 const ratio=C===0?(1+sinphi)/(1-sinphi):NaN;
 out.textContent=`effective principal stresses σ₁ − P = ${M.fmt(e1,3)}, σ₃ − P = ${M.fmt(e3,3)}: circle centre ${M.fmt(cen,3)}, radius ${M.fmt(R,3)}   φ = arctan f = ${M.fmt(phi*180/Math.PI,4)}°   envelope distance from the centre = ${M.fmt(dist,3)}\n${touching?'THE CIRCLE TOUCHES THE ENVELOPE → failure':'stable: circle below the envelope, margin = '+M.fmt(dist-R,3)}   plane at θ = ${M.fmt(sth.value,3)}°: σ_n = ${M.fmt(sn,3)}, τ = ${M.fmt(ta,3)}, τ/σ_n = ${M.fmt(ta/Math.max(sn,1e-9),3)}   most-likely failure plane: θ = 45° + φ/2 = ${M.fmt(thF*180/Math.PI,4)}° from σ₁ (plane ${M.fmt(45-phi*90/Math.PI,4)}° from σ₁)${C===0?'   σ₁/σ₃ at failure = (1+sinφ)/(1−sinφ) = '+M.fmt(ratio,3):''}`}
draw();ui.note('LS09/LS02: σ_n = ½(σ₁+σ₃) + ½(σ₁−σ₃)cos2θ, τ = ½(σ₁−σ₃) sin2θ (θ from σ₁ to the plane normal); Coulomb: τ = C + f σ_n, f = tanφ; failure plane β = 45° − φ/2 from σ₁ (≈ 30° for f = 0.6, φ = 31°); C = 0: σ₁/σ₃ = 3.1 (f = 0.6), 4.7 for Byerlee f = 0.85. Effective stress: σ − P (Terzaghi).');
