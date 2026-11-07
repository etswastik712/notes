//META {"title":"Rectangular waveguide: cutoff, modes and the bouncing wave","desc":"A hollow metal pipe of cross-section a × b. Each TE_mn mode has a cutoff frequency f_mn = (c/2)√((m/a)² + (n/b)²); below it the wave is evanescent. Choose the guide size, the mode and the frequency: left, the transverse electric field pattern; right, the cutoff ladder with your operating frequency, and the zig-zag path of the equivalent bouncing plane wave with phase velocity above c and group velocity below c.","vault":"ED","chapters":["ED07 Guided Waves"],"tryit":"With a = 2.28 cm, b = 1.01 cm sweep the frequency from 5 to 18 GHz and count the modes that switch on (TE10 at 6.57, TE20 at 13.15, TE01 at 14.84, TE11 at 16.23 GHz). At 10 GHz the bounce angle is 41.1°."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:0,xmax:1,ymin:0,ymax:1,axes:false});
const P2=ui.canvas(340,{xmin:0,xmax:1,ymin:0,ymax:30,axes:false});
ui.gridOf(1);const P3=ui.canvas(120,{xmin:0,xmax:1,ymin:0,ymax:1,axes:false});
const sa=ui.slider('width a (cm)',1.5,4,0.01,2.28,draw),sb=ui.slider('height b (cm)',0.5,3,0.01,1.01,draw),sm=ui.slider('mode index m',0,3,1,1,draw),sn=ui.slider('mode index n',0,3,1,0,draw),sf=ui.slider('frequency f (GHz)',3,30,0.05,10,draw);
const out=ui.readout();const c=29.9792458; // cm·GHz
function fc(m,n,a,b){return c/2*Math.hypot(m/a,n/b)}
function draw(){const a=sa.value,b=sb.value,m=sm.value,n=sn.value,f=sf.value;
 P1.clear();const W=P1.w,H=P1.h,px=40,py=26,bw=W-2*px,bh=H-2*py-34;
 const sc=Math.min(bw/a,bh/b),w=a*sc,h=b*sc,x0=(W-w)/2,y0=py+(bh-h)/2;
 if(m===0&&n===0){P1.ptext('TE₀₀ does not exist',W/2,H/2,C.red,'center','14px system-ui')}
 else{const g=P1.g,N=60,M2=Math.max(10,Math.round(N*b/a));for(let i=0;i<N;i++)for(let j=0;j<M2;j++){const x=(i+.5)/N*a,y=(j+.5)/M2*b;const Ex=(n/b)*Math.cos(m*Math.PI*x/a)*Math.sin(n*Math.PI*y/b),Ey=-(m/a)*Math.sin(m*Math.PI*x/a)*Math.cos(n*Math.PI*y/b);const mag=Math.hypot(Ex,Ey)/Math.hypot(m/a,n/b);g.fillStyle=`rgba(42,120,214,${0.12+0.8*mag})`;g.fillRect(x0+i*w/N,y0+(M2-1-j)*h/M2,w/N+1,h/M2+1)}
  for(let i=0;i<10;i++)for(let j=0;j<Math.max(4,Math.round(10*b/a));j++){const x=(i+.5)/10*a,y=(j+.5)/Math.max(4,Math.round(10*b/a))*b;const Ex=(n/b)*Math.cos(m*Math.PI*x/a)*Math.sin(n*Math.PI*y/b),Ey=-(m/a)*Math.sin(m*Math.PI*x/a)*Math.cos(n*Math.PI*y/b);const L=Math.hypot(Ex,Ey);if(L<1e-6)continue;const s=10/Math.hypot(m/a,n/b);const X=x0+x*sc,Y=y0+h-y*sc;g.strokeStyle=C.ink;g.lineWidth=1.5;g.beginPath();g.moveTo(X,Y);g.lineTo(X+Ex*s,Y-Ey*s);g.stroke()}}
 P1.g.strokeStyle=C.ink;P1.g.lineWidth=3;P1.g.strokeRect(x0,y0,w,h);P1.ptext(`TE${m}${n}: transverse E (arrows, shade = |E|)  walls: E_∥ = 0`,W/2,H-14,C.muted,'center','12px system-ui');
 P1.ptext('a = '+M.fmt(a,3)+' cm',W/2,y0-8,C.muted,'center');
 P2.clear();const modes=[];for(let i=0;i<=4;i++)for(let j=0;j<=4;j++)if(i||j)modes.push([fc(i,j,a,b),i,j]);modes.sort((p,q)=>p[0]-q[0]);
 const top=Math.max(30,f*1.1);P2.set({ymax:top});const g=P2.g;const x1=20,x2=P2.w*0.55;
 for(const [fcv,i,j] of modes.filter(q=>q[0]<=Math.max(f*1.3,18)).slice(0,10)){const y=P2.Y(fcv);g.strokeStyle=fcv<f?C.blue:C.muted;g.lineWidth=2.5;g.beginPath();g.moveTo(x1+30,y);g.lineTo(x2,y);g.stroke();P2.ptext(`TE${i}${j}  ${M.fmt(fcv,4)} GHz`,x2+6,y,fcv<f?C.blue:C.muted,'left','11px system-ui')}
 P2.g.strokeStyle=C.orange;P2.g.lineWidth=2;P2.g.setLineDash([6,4]);P2.g.beginPath();P2.g.moveTo(x1,P2.Y(f));P2.g.lineTo(P2.w-10,P2.Y(f));P2.g.stroke();P2.g.setLineDash([]);P2.ptext('operating f = '+M.fmt(f,4)+' GHz',x1,P2.Y(f)-9,C.orange);
 P2.ptext('GHz',14,14,C.muted);
const fcm=fc(m,n,a,b),r=f>fcm?Math.sqrt(1-((fcm/f)**2)):0;
 P3.clear();{const g=P3.g,zx=60,zw=P3.w-120,zy0=24,zh=64;g.strokeStyle=C.ink;g.lineWidth=3;g.beginPath();g.moveTo(zx,zy0);g.lineTo(zx+zw,zy0);g.moveTo(zx,zy0+zh);g.lineTo(zx+zw,zy0+zh);g.stroke();
  if(r>0){const th=Math.acos(r),L=zh/Math.tan(Math.max(th,0.06));g.strokeStyle=C.red;g.lineWidth=2;g.beginPath();let x=zx,y=zy0+zh,dir=-1;g.moveTo(x,y);while(x<zx+zw){const dx=Math.min(L,zx+zw-x);x+=dx;y+=dir*zh*dx/L;if(dx>=L*0.999)dir=-dir;g.lineTo(x,y)}g.stroke();P3.ptext('equivalent plane wave bounces at θ = '+M.fmt(th*180/Math.PI,3)+'° to the axis: net speed along the guide = c cos θ = v_g',zx,zy0-10,C.red)}
  else P3.ptext('below cutoff: the wave cannot propagate (evanescent)',zx,zy0-10,C.red)}
 const dBper10=f<fcm?20*Math.log10(Math.E)*(2*Math.PI/c*Math.sqrt(fcm*fcm-f*f))*10/ (1):0;
 out.textContent=f>fcm?`TE${m}${n}: f_c = ${M.fmt(fcm,5)} GHz  f/f_c = ${M.fmt(f/fcm,4)}   guide wavelength λ_g = λ₀/√(1−(f_c/f)²) = ${M.fmt(c/f/r,4)} cm (λ₀ = ${M.fmt(c/f,4)} cm)\nv_p = c/√(1−(f_c/f)²) = ${M.fmt(1/r,4)} c   v_g = c√(1−(f_c/f)²) = ${M.fmt(r,4)} c   v_p v_g = c²   propagating TE modes at this f: ${modes.filter(q=>q[0]<f).length}`:`TE${m}${n}: f_c = ${M.fmt(fcm,5)} GHz > f: evanescent with κ = (2π/c)√(f_c²−f²) = ${M.fmt(2*Math.PI/c*Math.sqrt(fcm*fcm-f*f),4)} cm⁻¹ → ${M.fmt(dBper10,4)} dB per 10 cm`}
draw();ui.note('ED07 Worked example 1: a = 2.28 cm, b = 1.01 cm → f_c(TE10) = 6.574 GHz, TE20 13.149, TE01 14.841, TE11 16.232; at 10 GHz: λ_g = 3.98 cm, v_p = 1.327c, v_g = 0.7535c.');
