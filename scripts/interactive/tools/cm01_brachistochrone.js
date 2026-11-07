//META {"title":"Brachistochrone: which path is fastest?","desc":"A bead slides from rest from the origin to the end point under gravity along four paths. Drag the end point or change the exponent of the trial path; the cycloid always wins. Press race to watch the beads.","vault":"CM","chapters":["CM01 Variational Calculus and Hamilton's Principle"],"tryit":"Drag the exponent p of the power-law path (p = 1 is the straight line) and watch its time exceed the cycloid's; then increase the depth Y beyond X to make the cycloid dip below the end point."}
const g=9.81;
const P=ui.canvas(380,{xmin:-0.05,xmax:1.45,ymin:-0.2,ymax:1.0,xlabel:'x (m)',ylabel:'depth y (m)'});
const sX=ui.slider('end point X (m)',0.4,1.4,0.01,1.0,draw),sY=ui.slider('end depth Y (m)',0.1,0.9,0.01,0.5,draw),sp=ui.slider('trial exponent p (y ∝ x^p)',0.3,1.6,0.01,0.7,draw);
const out=ui.readout(); let t=0,run=false;
function cyc(X,Y){ // find theta1 s.t. (1-cos)/(th-sin)=Y/X
  let lo=0.05,hi=6.2;const f=th=>(1-Math.cos(th))/(th-Math.sin(th))-Y/X;for(let i=0;i<80;i++){const m=(lo+hi)/2;if(f(lo)*f(m)<=0)hi=m;else lo=m}
  const th=(lo+hi)/2,a=X/(th-Math.sin(th));return{th,a,T:th*Math.sqrt(a/g)}}
function Tpow(X,Y,p){const m=8;let s=0,N=6000;for(let i=0;i<N;i++){const u=(i+.5)/N,x=X*Math.pow(u,m),dxdu=X*m*Math.pow(u,m-1),yy=Y*Math.pow(x/X,p),dy=Y*p*Math.pow(x/X,p-1)/X;s+=Math.sqrt((1+dy*dy)/(2*g*yy))*dxdu/N}return s}
function pos(kind,X,Y,p,s,c){ // position at fraction s of path-parameter progress chosen by time later
  return null}
function draw(){const X=sX.value,Y=sY.value,p=sp.value,c=cyc(X,Y);P.clear();
  const th=M.linspace(0,c.th,200);P.line(th.map(t=>c.a*(t-Math.sin(t))),th.map(t=>c.a*(1-Math.cos(t))),C.blue,3);
  P.line([0,X],[0,Y],C.orange,2);const xs=M.linspace(0,X,200);P.line(xs,xs.map(x=>Y*Math.sqrt(x/X)),C.aqua,2);P.line(xs,xs.map(x=>Y*Math.pow(x/X,p)),C.violet,2);
  P.dot(0,0,C.ink,4);P.dot(X,Y,C.red,6);
  P.legend([['cycloid (fastest)',C.blue],['straight line',C.orange],['parabola y∝√x',C.aqua],['y ∝ x^p, p='+p.toFixed(2),C.violet]],P.o.ml+P.w*0.55,P.o.mt+14);
  // note: y axis is depth (down); invert by plotting ymin..ymax downward
  const Tl=Math.hypot(X,Y)*Math.sqrt(2/(g*Y)),Tp=Tpow(X,Y,0.5),Tq=Tpow(X,Y,p);
  out.textContent=`times (s):  cycloid ${M.fmt(c.T,4)}   line ${M.fmt(Tl,4)}   y∝√x ${M.fmt(Tp,4)}   y∝x^p ${M.fmt(Tq,4)}\ncycloid: a = ${M.fmt(c.a,4)} m, θ₁ = ${M.fmt(c.th,4)} rad${c.th>Math.PI?'  (θ₁>π: the bead dips to depth 2a = '+M.fmt(2*c.a,3)+' m below the target)':''}`;
  if(run)drawBeads(X,Y,p,c)}
function drawBeads(X,Y,p,c){ // time-parameterised beads
  const pts={};
  { // cycloid
    const th=Math.min(c.th,t/Math.sqrt(c.a/g));P.dot(c.a*(th-Math.sin(th)),c.a*(1-Math.cos(th)),C.blue,7)}
  { const Tl=Math.hypot(X,Y)*Math.sqrt(2/(g*Y)),L=Math.hypot(X,Y),sn=Y/L;const s=Math.min(L,.5*g*sn*t*t);P.dot(s*X/L,s*Y/L,C.orange,7)}
  // power-law via integration of arclength vs energy
  for(const [pp,color] of [[0.5,C.aqua],[p,C.violet]]){ const m=8,N=3000;let tt=0,x=0;for(let i=0;i<N&&tt<t;i++){const u=(i+.5)/N,xm=X*Math.pow(u,m),dxdu=X*m*Math.pow(u,m-1),yy=Y*Math.pow(xm/X,pp),dy=Y*pp*Math.pow(xm/X,pp-1)/X;tt+=Math.sqrt((1+dy*dy)/(2*g*yy))*dxdu/N;x=X*Math.pow((i+1)/N,m)}P.dot(x,Y*Math.pow(x/X,pp),color,7)}}
P.o.ymin=1.0;P.o.ymax=-0.2; // depth increases downward
ui.button('▶ race',()=>{t=0;run=true;});
loop((dt)=>{if(run){t+=dt*0.5;draw();if(t>1.2)run=false}});
draw();
ui.note('Cycloid: x = a(θ − sin θ), y = a(1 − cos θ); time T = θ₁√(a/g). Checks against CM01 Worked example 3: X = 1, Y = 0.5 gives T = 0.5696 s (cycloid), 0.7139 s (line).');
