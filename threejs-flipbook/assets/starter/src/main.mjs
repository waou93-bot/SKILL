import * as THREE from 'three';
import {paperProfile,boundedPage,spreadFaces,PAGE_WIDTH as W,PAGE_HEIGHT as H,SHEETS,THICKNESS} from './paper.mjs';
import {CHAPTERS,makePage,PALETTE} from './art.mjs';

const $=id=>document.getElementById(id);
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const stage=$('stage'),host=$('canvas-host'),flat=$('flat-view');
const pages=Array.from({length:SHEETS},(_,sheet)=>({front:makePage(sheet,'front'),back:makePage(sheet,'back')}));
const state={page:0,target:0,reading:false,sound:false,webgl:false,drag:null,hover:new THREE.Vector2(),dirty:true,visible:true};
let renderer,scene,camera,book,sheets=[],floorShadow,frame=0,lastTime=0,settledTime=0,audioContext;
const SEGMENTS=64, ROWS=1;
const progress=Array(SHEETS).fill(0);
const destination=Array(SHEETS).fill(0);
const curlDirection=Array(SHEETS).fill(1);
const curlTarget=Array(SHEETS).fill(1);
let lastTurnAt=-Infinity,turnSpeed=10;

function updateFlat(){
  flat.replaceChildren();
  const faces=spreadFaces(state.page);
  flat.classList.toggle('single',faces.length===1);
  for(const face of faces){
    const source=pages[face.sheet][face.side];
    const copy=document.createElement('canvas');copy.width=source.width;copy.height=source.height;
    copy.getContext('2d').drawImage(source,0,0);
    copy.setAttribute('role','img');copy.setAttribute('aria-label',face.side==='front'?`Planche : ${CHAPTERS[face.sheet].title}`:`Texte : ${CHAPTERS[face.sheet+1]?.title||'Colophon'}`);
    copy.addEventListener('click',()=>goTo(state.page+(face.side==='back'?-1:1)));
    flat.append(copy);
  }
  flat.scrollLeft=0;
}
function updateUI(){
  const p=state.page;
  document.body.classList.toggle('open',p>0);
  $('prev').disabled=p===0;$('next').disabled=p===SHEETS-1;
  $('page-number').textContent=p===0?'COUVERTURE':`${String(p*2).padStart(2,'0')} — ${String(p*2+1).padStart(2,'0')}`;
  $('chapter').textContent=`${String(p).padStart(2,'0')} / ${CHAPTERS[p].title.toUpperCase()}`;
  for(const b of $('chapter-links').children)b.setAttribute('aria-current',String(Number(b.dataset.page)===p));
  const copy=$('accessible-copy');copy.replaceChildren();
  const h=document.createElement('h2');h.textContent=CHAPTERS[p].title;copy.append(h);
  if(p>0){const paragraph=document.createElement('p');paragraph.textContent=[CHAPTERS[p].subtitle,CHAPTERS[p].text,CHAPTERS[p].detail].join(' ');copy.append(paragraph);}
  if(state.reading||!state.webgl)updateFlat();
}

function rustle(){
  if(!state.sound)return;
  try{
    audioContext ||= new (window.AudioContext||window.webkitAudioContext)();
    if(audioContext.state==='suspended')audioContext.resume();
    const length=Math.floor(audioContext.sampleRate*.38),buffer=audioContext.createBuffer(1,length,audioContext.sampleRate);
    const values=buffer.getChannelData(0);
    for(let i=0;i<length;i++)values[i]=(Math.random()*2-1)*Math.sin(Math.PI*i/length)**2;
    const source=audioContext.createBufferSource();source.buffer=buffer;
    const filter=audioContext.createBiquadFilter();filter.type='bandpass';filter.frequency.value=1400;filter.Q.value=.6;
    const gain=audioContext.createGain();gain.gain.value=.055;
    source.connect(filter).connect(gain).connect(audioContext.destination);source.start();
  }catch{state.sound=false;$('sound-toggle').setAttribute('aria-pressed','false');$('sound-state').textContent='indisponible';}
}

function goTo(requested){
  const target=boundedPage(requested);
  if(target===state.page && !state.drag)return;
  state.target=target;state.page=target;
  const now=performance.now();
  // Repeated clicks accelerate pages already in flight, without resetting them.
  turnSpeed=now-lastTurnAt<260?Math.min(24,turnSpeed+4):10;
  lastTurnAt=now;
  for(let i=0;i<SHEETS;i++){
    const next=i<target?1:0;
    if(Math.abs(next-progress[i])>.0002){
      curlTarget[i]=next>progress[i]?1:-1;
      if(progress[i]<.001||progress[i]>.999)curlDirection[i]=curlTarget[i];
    }
    destination[i]=next;
  }
  if(reduced.matches)for(let i=0;i<SHEETS;i++){progress[i]=destination[i];if(sheets[i])updatePaper(i);}
  updateUI();rustle();wake();
}
function setReading(on){
  state.reading=on;document.body.classList.toggle('reading',on);
  $('read-toggle').setAttribute('aria-pressed',String(on));
  $('read-toggle').textContent=on?'Vue 3D':'Vue lecture';
  flat.hidden=!(on||!state.webgl);
  if(on)updateFlat();wake();
}
function setIndex(open){
  $('index-panel').hidden=!open;$('scrim').hidden=!open;
  $('index-toggle').setAttribute('aria-expanded',String(open));
  if(open)$('chapter-links').querySelector('[aria-current="true"]').focus();
  else $('index-toggle').focus();
}

for(let i=0;i<CHAPTERS.length;i++){
  const b=document.createElement('button');b.dataset.page=i;
  const n=document.createElement('span');n.textContent=String(i).padStart(2,'0');b.append(n,document.createTextNode(CHAPTERS[i].title));
  b.addEventListener('click',()=>{goTo(i);setIndex(false);});$('chapter-links').append(b);
}
$('next').addEventListener('click',()=>goTo(state.page+1));
$('prev').addEventListener('click',()=>goTo(state.page-1));
$('open-book').addEventListener('click',()=>goTo(1));
$('home').addEventListener('click',event=>{event.preventDefault();goTo(0);});
$('read-toggle').addEventListener('click',()=>setReading(!state.reading));
$('sound-toggle').addEventListener('click',()=>{state.sound=!state.sound;$('sound-toggle').setAttribute('aria-pressed',String(state.sound));$('sound-state').textContent=state.sound?'on':'off';if(state.sound)rustle();});
$('index-toggle').addEventListener('click',()=>setIndex($('index-panel').hidden));
$('scrim').addEventListener('click',()=>setIndex(false));
document.addEventListener('keydown',event=>{
  if(! $('index-panel').hidden){
    if(event.key==='Escape'){setIndex(false);event.preventDefault();}
    if(event.key==='Tab'){
      const focusables=[$('index-toggle'),...$('chapter-links').children];
      const first=focusables[0],last=focusables.at(-1);
      if(event.shiftKey&&document.activeElement===first){last.focus();event.preventDefault();}
      else if(!event.shiftKey&&document.activeElement===last){first.focus();event.preventDefault();}
    }
    return;
  }
  if(event.altKey||event.ctrlKey||event.metaKey)return;
  if(event.key==='ArrowRight'){goTo(state.page+1);event.preventDefault();}
  if(event.key==='ArrowLeft'){goTo(state.page-1);event.preventDefault();}
  if(event.key==='Home'){goTo(0);event.preventDefault();}
  if(event.key==='End'){goTo(SHEETS-1);event.preventDefault();}
  if(event.key==='Escape'&&state.reading)setReading(false);
});

function texture(canvas){const t=new THREE.CanvasTexture(canvas);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=Math.min(8,renderer.capabilities.getMaxAnisotropy());return t;}
function updatePaper(index){
  const sheet=sheets[index],profile=paperProfile(progress[index],SEGMENTS,index,curlDirection[index]);
  const geometry=sheet.front.geometry;
  const pos=geometry.attributes.position,normal=geometry.attributes.normal;
    for(let row=0;row<=ROWS;row++)for(let col=0;col<=SEGMENTS;col++){
      const k=row*(SEGMENTS+1)+col;
      pos.setXYZ(k,profile[col].x,H/2-row/ROWS*H,profile[col].z);
      const a=profile[Math.max(0,col-1)],b=profile[Math.min(SEGMENTS,col+1)];
      const dx=b.x-a.x,dz=b.z-a.z,length=Math.hypot(dx,dz);
      normal.setXYZ(k,-dz/length,0,dx/length);
    }
  pos.needsUpdate=true;normal.needsUpdate=true;
  if(renderer)renderer.shadowMap.needsUpdate=true;
}

function init3D(){
  renderer=new THREE.WebGLRenderer({antialias:true,alpha:true,powerPreference:'low-power'});
  renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setSize(stage.clientWidth,stage.clientHeight);
  renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.NoToneMapping;
  renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  renderer.shadowMap.autoUpdate=false;
  host.append(renderer.domElement);
  renderer.domElement.setAttribute('aria-hidden','true');
  scene=new THREE.Scene();
  camera=new THREE.PerspectiveCamera(34,stage.clientWidth/stage.clientHeight,.1,60);
  book=new THREE.Group();book.position.z=.09;scene.add(book);
  const ambient=new THREE.HemisphereLight(0xffffff,0xb6afa2,1.6);ambient.position.set(0,0,5);scene.add(ambient);
  const key=new THREE.DirectionalLight(0xfff4dd,1.9);key.position.set(-3,5,9);key.castShadow=true;
  key.shadow.mapSize.set(1024,1024);key.shadow.camera.left=-5;key.shadow.camera.right=5;key.shadow.camera.top=5;key.shadow.camera.bottom=-5;
  key.shadow.camera.near=.1;key.shadow.camera.far=25;key.shadow.normalBias=.025;key.shadow.bias=-.0005;key.shadow.radius=4;scene.add(key);
  const fill=new THREE.DirectionalLight(0xffffff,.35);fill.position.set(5,-4,5);scene.add(fill);
  const floor=new THREE.Mesh(new THREE.PlaneGeometry(200,200),new THREE.ShadowMaterial({opacity:.17}));floor.position.z=-.055;floor.receiveShadow=true;scene.add(floor);
  const shadowCanvas=document.createElement('canvas');shadowCanvas.width=256;shadowCanvas.height=256;
  const sc=shadowCanvas.getContext('2d');const gradient=sc.createRadialGradient(128,128,15,128,128,125);
  gradient.addColorStop(0,'rgba(45,38,28,.27)');gradient.addColorStop(.5,'rgba(45,38,28,.15)');gradient.addColorStop(1,'rgba(45,38,28,0)');sc.fillStyle=gradient;sc.fillRect(0,0,256,256);
  floorShadow=new THREE.Mesh(new THREE.PlaneGeometry(7,5),new THREE.MeshBasicMaterial({map:texture(shadowCanvas),transparent:true,depthWrite:false}));floorShadow.position.set(0,-.16,-.052);scene.add(floorShadow);
  const backing=new THREE.Mesh(new THREE.BoxGeometry(W+.025,H+.04,.043),new THREE.MeshStandardMaterial({color:0x8b2418,roughness:.94}));backing.position.set(W/2,0,-.028);backing.castShadow=true;book.add(backing);
  const edges=new THREE.Mesh(new THREE.BoxGeometry(W-.025,H-.025,THICKNESS*SHEETS),new THREE.MeshStandardMaterial({color:0xeee7da,roughness:1}));edges.castShadow=true;book.add(edges);
  const leftBacking=backing.clone();leftBacking.position.x=-W/2;leftBacking.visible=false;book.add(leftBacking);
  const leftEdges=edges.clone();leftEdges.position.x=-W/2;leftEdges.visible=false;book.add(leftEdges);
  book.userData={leftBacking,leftEdges,edges,backing};
  for(let i=0;i<SHEETS;i++){
    const geometry=new THREE.PlaneGeometry(W,H,SEGMENTS,ROWS);
    const backGeometry=geometry.clone();
    // Front and back share deformation buffers, while keeping distinct UVs.
    backGeometry.setAttribute('position',geometry.attributes.position);
    backGeometry.setAttribute('normal',geometry.attributes.normal);
    const bounds=new THREE.Sphere(new THREE.Vector3(0,0,.04),Math.hypot(W,H/2)+.2);
    geometry.boundingSphere=bounds;backGeometry.boundingSphere=bounds;
    geometry.attributes.position.setUsage(THREE.DynamicDrawUsage);
    geometry.attributes.normal.setUsage(THREE.DynamicDrawUsage);
    const uv=backGeometry.attributes.uv;for(let k=0;k<uv.count;k++)uv.setX(k,1-uv.getX(k));
    const common={roughness:.96,metalness:0,polygonOffset:true,polygonOffsetFactor:-1,polygonOffsetUnits:-1};
    const front=new THREE.Mesh(geometry,new THREE.MeshStandardMaterial({...common,map:texture(pages[i].front),side:THREE.FrontSide}));
    const back=new THREE.Mesh(backGeometry,new THREE.MeshStandardMaterial({...common,map:texture(pages[i].back),side:THREE.BackSide}));
    front.castShadow=back.castShadow=true;front.receiveShadow=back.receiveShadow=true;
    front.userData.sheet=back.userData.sheet=i;
    book.add(front,back);sheets.push({front,back});updatePaper(i);
  }
  state.webgl=true;
  renderer.domElement.addEventListener('webglcontextlost',event=>{event.preventDefault();fallback('La vue 3D a été interrompue. La revue reste disponible à plat.');});
  bindPointer(renderer.domElement);
  new ResizeObserver(()=>{renderer.setSize(stage.clientWidth,stage.clientHeight);camera.aspect=stage.clientWidth/stage.clientHeight;camera.updateProjectionMatrix();wake();}).observe(stage);
  wake();
}

const raycaster=new THREE.Raycaster(),ndc=new THREE.Vector2();
const localRay=new THREE.Ray(),inverseBook=new THREE.Matrix4(),pagePoint=new THREE.Vector3();
const navigationPlane=new THREE.Plane(new THREE.Vector3(0,0,1),-.08);
function hitPage(event){
  if(!renderer)return null;
  const r=renderer.domElement.getBoundingClientRect();ndc.set((event.clientX-r.left)/r.width*2-1,-(event.clientY-r.top)/r.height*2+1);
  raycaster.setFromCamera(ndc,camera);
  book.updateWorldMatrix(true,false);
  inverseBook.copy(book.matrixWorld).invert();
  localRay.copy(raycaster.ray).applyMatrix4(inverseBook);
  if(!localRay.intersectPlane(navigationPlane,pagePoint))return null;
  if(Math.abs(pagePoint.y)>H/2+.12||Math.abs(pagePoint.x)>W+.12)return null;
  const direction=pagePoint.x>=0?1:-1;
  if(direction===1&&state.page>=SHEETS-1||direction===-1&&state.page===0)return null;
  return {direction,index:direction===1?state.page:state.page-1,edge:Math.abs(pagePoint.x)>W*.70};
}
function dragTravel(){
  const right=book.localToWorld(new THREE.Vector3(W,0,.08)).project(camera);
  const left=book.localToWorld(new THREE.Vector3(-W,0,.08)).project(camera);
  return Math.max(120,Math.abs(right.x-left.x)*renderer.domElement.getBoundingClientRect().width/2);
}
function bindPointer(canvas){
  canvas.addEventListener('pointerdown',event=>{
    if(event.button!==0||state.reading||!$('index-panel').hidden)return;
    const hit=hitPage(event);if(!hit)return;
    if((hit.direction===1&&state.page===SHEETS-1)||(hit.direction===-1&&state.page===0))return;
    state.drag={...hit,startX:event.clientX,startY:event.clientY,start:progress[hit.index],travel:dragTravel(),moved:false,canDrag:hit.edge||!progress.some((p,i)=>Math.abs(p-destination[i])>.035),pointerId:event.pointerId};
    canvas.setPointerCapture(event.pointerId);canvas.style.cursor='grabbing';wake();
  });
  canvas.addEventListener('pointermove',event=>{
    const r=canvas.getBoundingClientRect();
    if(!reduced.matches)state.hover.set((event.clientX-r.left)/r.width-.5,(event.clientY-r.top)/r.height-.5);
    if(state.drag){
      const d=state.drag,dx=event.clientX-d.startX,dy=event.clientY-d.startY;
      if(d.canDrag&&Math.abs(dx)>7 && Math.abs(dx)>Math.abs(dy)*.7)d.moved=true;
      if(d.moved){
        // Use the projected width of the actual book, not the viewport width.
        // A full stroke from one outer edge to the other turns one complete page.
        const next=THREE.MathUtils.clamp(d.start-dx/d.travel,0,1);
        if(Math.abs(next-progress[d.index])>.0005)curlTarget[d.index]=next>progress[d.index]?1:-1;
        progress[d.index]=next;
        updatePaper(d.index);
      }
    }else {const hit=hitPage(event);canvas.style.cursor=hit?(hit.edge?'grab':'pointer'):'default';}
    wake();
  });
  function finish(event,cancelled=false){
    const d=state.drag;if(!d)return;
    state.drag=null;canvas.style.cursor='grab';
    if(canvas.hasPointerCapture(d.pointerId))canvas.releasePointerCapture(d.pointerId);
    if(cancelled){curlTarget[d.index]=destination[d.index]>progress[d.index]?1:-1;wake();return;}
    const completed=d.direction===1?progress[d.index]>.5:progress[d.index]<.5;
    if(!d.moved||completed)goTo(state.page+d.direction);
    else {curlTarget[d.index]=destination[d.index]>progress[d.index]?1:-1;wake();}
  }
  canvas.addEventListener('pointerup',event=>finish(event));
  canvas.addEventListener('pointercancel',event=>finish(event,true));
  canvas.addEventListener('pointerleave',()=>{state.hover.set(0,0);wake();});
}

function fallback(message){
  state.webgl=false;state.reading=true;document.body.classList.add('reading');
  host.hidden=true;flat.hidden=false;updateFlat();
  $('read-toggle').hidden=true;$('loading').hidden=true;
  $('instructions').textContent=message||'Vue à plat · utilise les flèches pour feuilleter.';
}

function wake(){state.dirty=true;settledTime=0;if(!frame&&state.webgl&&state.visible&&!state.reading)frame=requestAnimationFrame(tick);}
function tick(time){
  frame=0;
  const dt=Math.min((time-(lastTime||time-16))/1000,.05);lastTime=time;
  let moving=false;
  for(let i=0;i<SHEETS;i++){
    let changed=false;
    const curlDelta=curlTarget[i]-curlDirection[i];
    if(Math.abs(curlDelta)>.0005){
      // Blend bending direction over time instead of flipping the mesh instantly.
      curlDirection[i]+=curlDelta*(1-Math.exp(-dt*18));
      if(Math.abs(curlTarget[i]-curlDirection[i])<.0005)curlDirection[i]=curlTarget[i];
      changed=true;
    }
    if(state.drag?.moved&&state.drag.index===i){if(changed)updatePaper(i);moving ||= changed;continue;}
    const delta=destination[i]-progress[i];
    if(Math.abs(delta)>.0002){
      progress[i]+=delta*(1-Math.exp(-dt*turnSpeed));
      if(Math.abs(destination[i]-progress[i])<.0005)progress[i]=destination[i];
      changed=true;
    }
    if(changed){updatePaper(i);moving=true;}
  }
  const open=THREE.MathUtils.clamp(progress.reduce((a,b)=>a+b,0),0,1);
  const mobile=stage.clientWidth<600;
  const closedCenter=mobile?0:stage.clientWidth<900?.75:1.6;
  const targetX=(closedCenter-W/2)*(1-open);
  book.position.x=reduced.matches?targetX:THREE.MathUtils.lerp(book.position.x,targetX,1-Math.exp(-dt*6));
  const tiltX=reduced.matches?0:state.hover.y*.045;
  const tiltY=reduced.matches?0:state.hover.x*.065;
  const targetRotation=-.105*(1-open)+tiltY*.3;
  const targetRX=-.025+tiltX;
  book.rotation.z=reduced.matches?targetRotation:THREE.MathUtils.lerp(book.rotation.z,targetRotation,.12);
  book.rotation.x=reduced.matches?targetRX:THREE.MathUtils.lerp(book.rotation.x,targetRX,.12);
  book.rotation.y=reduced.matches?tiltY:THREE.MathUtils.lerp(book.rotation.y,tiltY,.12);
  book.userData.leftBacking.visible=open>.015;book.userData.leftEdges.visible=open>.015;
  const turned=progress.reduce((a,b)=>a+b,0);
  const leftHeight=Math.max(.001,turned*THICKNESS-.01);
  const rightHeight=Math.max(.001,(SHEETS-turned)*THICKNESS-.01);
  book.userData.leftEdges.scale.z=leftHeight/(SHEETS*THICKNESS);
  book.userData.edges.scale.z=rightHeight/(SHEETS*THICKNESS);
  book.userData.leftEdges.position.z=leftHeight/2;
  book.userData.edges.position.z=rightHeight/2;
  // Fit the complete book in landscape. Portrait favours a larger closed cover.
  const aspect=camera.aspect;
  const visibleWidth=(mobile?W*2+1.0:W*2+2.4);
  const distance=Math.max(6.8,visibleWidth/(2*Math.tan(THREE.MathUtils.degToRad(camera.fov/2))*aspect));
  const closedZoom=mobile?(1-open)*.40:0;
  const z=distance*(1-closedZoom);
  camera.position.set(0,-z*.24,z);
  camera.lookAt(0,mobile?.12:0,0);
  floorShadow.position.x=book.position.x+W/2*(1-open);
  floorShadow.scale.x=.60+open*.4;
  const transformMoving=Math.abs(book.position.x-targetX)>.001||Math.abs(book.rotation.z-targetRotation)>.0003||Math.abs(book.rotation.x-targetRX)>.0003||Math.abs(book.rotation.y-tiltY)>.0003;
  // Refresh shadows only when the object changes, never during idle tail frames.
  if(transformMoving)renderer.shadowMap.needsUpdate=true;
  renderer.render(scene,camera);
  if(moving||transformMoving||state.drag||state.dirty){settledTime=0;state.dirty=false;}else settledTime+=dt;
  if(settledTime<.12&&state.visible&&!state.reading)frame=requestAnimationFrame(tick);
}
document.addEventListener('visibilitychange',()=>{state.visible=!document.hidden;if(state.visible){lastTime=0;wake();}else if(frame){cancelAnimationFrame(frame);frame=0;}});
reduced.addEventListener('change',()=>{if(reduced.matches){state.hover.set(0,0);for(let i=0;i<SHEETS;i++){progress[i]=destination[i];if(sheets[i])updatePaper(i);}}wake();});

try{init3D();}catch(error){console.warn('FOLIO : vue à plat activée.',error);fallback();}
updateUI();$('loading').hidden=true;
// Public diagnostic state for manual validation without exposing any user data.
window.folio={goTo,setReading,getState:()=>({page:state.page,reading:state.reading,webgl:state.webgl,reducedMotion:reduced.matches,turnSpeed,pageProgress:[...progress]})};
