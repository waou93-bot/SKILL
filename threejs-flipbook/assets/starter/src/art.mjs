export const PALETTE = { paper:'#f5f0e5', ink:'#24231f', red:'#ed4932' };
export const CHAPTERS = [
  { title:'Couverture', subtitle:'L’art de tourner la page.' },
  { title:'Interférences', subtitle:'Quand les lignes prennent vie.', text:'Deux rythmes se rencontrent. Une ligne en croise une autre et, entre les deux, une troisième forme apparaît. Elle ne tient qu’à notre regard.', detail:'La trame est une matière vivante : rapprocher, décaler, superposer. Le mouvement naît parfois de ce qui ne bouge pas.', note:'TRAME / SUPERPOSITION / PERCEPTION' },
  { title:'Tension', subtitle:'Le calme avant le mouvement.', text:'Une surface s’étire. Le centre résiste, les bords s’échappent. La tension donne une direction à ce qui semblait immobile.', detail:'Le papier connaît cette sensation. Avant de se retourner, il plie, retient son souffle, puis suit la main.', note:'COURBE / ÉQUILIBRE / ÉLASTICITÉ' },
  { title:'Cadence', subtitle:'Trouver un rythme dans la répétition.', text:'Une unité, puis une autre. Un intervalle se répète jusqu’à devenir un rythme. Un seul écart suffit pour faire entendre quelque chose de nouveau.', detail:'Ce qui se répète n’est jamais tout à fait identique. L’œil cherche la règle, puis s’attarde sur l’exception.', note:'MODULE / INTERVALLE / VARIATION' },
  { title:'Contreforme', subtitle:'Dessiner aussi ce qui manque.', text:'La forme s’arrête là où le vide commence. Pourtant, le vide n’est pas une absence. Il tient les caractères debout, sépare les signes et donne à la page son souffle.', detail:'Regarder autour plutôt qu’au centre. Voir l’espace entre les choses comme une matière à part entière.', note:'PLEIN / VIDE / TYPOGRAPHIE' },
  { title:'Horizon', subtitle:'Là où une ligne devient un paysage.', text:'Une ligne suffit à partager l’espace. Au-dessus, une promesse. En dessous, une profondeur. Tout paysage commence par cette décision simple.', detail:'Les bandes se resserrent au loin. Le plan devient volume, le noir devient distance. Une perspective sans point de fuite.', note:'LIGNE / PROFONDEUR / DISTANCE' },
  { title:'Recommencer', subtitle:'La dernière page est un début.', text:'On arrive au bout d’une revue comme au bord d’une idée. Rien n’est vraiment terminé : une forme aperçue ici peut devenir autre chose ailleurs.', detail:'FOLIO est une étude de papier, d’encre et de mouvement. Six compositions originales, réunies dans un objet que l’on peut parcourir à son rythme.', note:'ÉTUDE / EXPLORATION / SUITE' }
];

const W=900,H=1260;
function text(c,str,x,y,size=22,weight=400,color=PALETTE.ink,family='Arial') {
  c.fillStyle=color;c.font=`${weight} ${size}px ${family}`;c.fillText(str,x,y);
}
function wrapped(c,str,x,y,width,size=30,lineHeight=44,color=PALETTE.ink) {
  c.font=`400 ${size}px Arial`;c.fillStyle=color;
  let line='';
  for(const word of str.split(' ')) {
    const next=line?`${line} ${word}`:word;
    if(c.measureText(next).width>width && line){c.fillText(line,x,y);y+=lineHeight;line=word;}else line=next;
  }
  if(line)c.fillText(line,x,y);
  return y+lineHeight;
}
function rule(c,y,color=PALETTE.ink){c.fillStyle=color;c.fillRect(65,y,770,1.5);}
function label(c,left,right,color=PALETTE.ink){text(c,left,65,65,18,400,color,'monospace');c.textAlign='right';text(c,right,835,65,18,400,color,'monospace');c.textAlign='left';}
function foot(c,n,color=PALETTE.ink){rule(c,1187,color);text(c,'FOLIO — ÉTUDES DE MOUVEMENT',65,1220,16,400,color,'monospace');c.textAlign='right';text(c,String(n).padStart(2,'0'),835,1220,18,400,color,'monospace');c.textAlign='left';}

function cover(c) {
  c.fillStyle=PALETTE.red;c.fillRect(0,0,W,H);
  label(c,'REVUE D’EXPLORATIONS VISUELLES','VOL. 001');
  text(c,'FOLIO',43,307,229,900);
  text(c,'ÉTUDES DE',65,382,33,700);text(c,'MOUVEMENT',65,423,33,700);
  c.save();c.beginPath();c.rect(0,472,W,583);c.clip();
  c.strokeStyle=PALETTE.ink;c.lineWidth=6;
  for(let j=0;j<47;j++) {
    c.beginPath();
    for(let x=-80;x<=980;x+=5){const y=575+j*10+Math.sin(x/125+j*.065)*90+Math.cos(x/230-j*.08)*72;if(x===-80)c.moveTo(x,y);else c.lineTo(x,y);}
    c.stroke();
  }
  c.restore();
  text(c,'PAPIER. ENCRE. UNE AUTRE DIMENSION.',65,1112,19,400,PALETTE.ink,'monospace');
  foot(c,'01');
}
function interference(c) {
  c.save();c.beginPath();c.rect(40,135,820,965);c.clip();
  c.strokeStyle=PALETTE.ink;c.lineWidth=4;
  for(let n=-28;n<100;n++) {
    c.beginPath();
    for(let y=135;y<=1100;y+=5) {
      const x=n*15+Math.sin(y/175)*105;
      if(y===135)c.moveTo(x,y);else c.lineTo(x,y);
    }c.stroke();
  }
  c.strokeStyle=PALETTE.red;c.lineWidth=4;
  for(let n=-28;n<100;n++) {
    c.beginPath();
    for(let y=135;y<=1100;y+=5) {
      const x=n*15+Math.sin(y/230+1.2)*150;
      if(y===135)c.moveTo(x,y);else c.lineTo(x,y);
    }c.stroke();
  }c.restore();
}
function tension(c) {
  c.fillStyle=PALETTE.red;c.fillRect(65,160,770,910);
  c.save();c.beginPath();c.rect(65,160,770,910);c.clip();c.strokeStyle=PALETTE.ink;c.lineWidth=4;
  for(let n=0;n<=40;n++){
    const y=110+n*26;
    c.beginPath();c.moveTo(20,y);c.bezierCurveTo(200,y,350,700-n*4,470,645+n*2);c.bezierCurveTo(585,615+n*8,675,y,900,y);c.stroke();
  }
  c.restore();
}
function cadence(c) {
  c.save();c.translate(450,620);c.rotate(-Math.PI/12);
  const size=93;
  for(let y=-4;y<=4;y++)for(let x=-3;x<=3;x++){
    c.fillStyle=(x+y)%2===0?PALETTE.ink:PALETTE.red;
    c.save();c.translate(x*size,y*size);c.rotate((x===0&&y===0)?Math.PI/4:0);
    c.fillRect(-size*.39,-size*.39,size*.78,size*.78);c.restore();
  }c.restore();
  text(c,'1 : 1 : 1 : 1 : 1 : 1 : ?',125,1110,26,400,PALETTE.ink,'monospace');
}
function counterform(c) {
  c.fillStyle=PALETTE.ink;c.fillRect(65,145,770,952);
  c.save();c.beginPath();c.rect(65,145,770,952);c.clip();
  text(c,'a',-45,910,1220,900,PALETTE.paper);
  c.fillStyle=PALETTE.red;c.beginPath();c.arc(530,682,92,0,Math.PI*2);c.fill();
  c.restore();
}
function horizon(c) {
  c.save();c.beginPath();c.rect(65,145,770,952);c.clip();
  c.fillStyle=PALETTE.red;c.fillRect(65,145,770,440);
  c.fillStyle=PALETTE.ink;c.fillRect(65,585,770,512);
  for(let i=0;i<27;i++) {
    const u=i/27;const y=587+Math.pow(u,2.25)*512;
    const h=1+Math.pow(u,2)*20;c.fillStyle=PALETTE.paper;c.fillRect(65,y,770,h);
  }
  c.fillStyle=PALETTE.paper;c.beginPath();c.arc(450,429,79,0,Math.PI*2);c.fill();c.restore();
}
function again(c) {
  c.fillStyle=PALETTE.red;c.fillRect(0,0,W,H);
  text(c,'ENCORE.',65,292,155,900);
  c.strokeStyle=PALETTE.ink;c.lineWidth=5;
  c.save();c.translate(450,700);
  for(let i=0;i<30;i++){
    c.save();c.rotate(i*.1);const s=405-i*10;c.strokeRect(-s/2,-s/2,s,s);c.restore();
  }c.restore();
  text(c,'TOUTE FIN EST UNE NOUVELLE FORME.',65,1110,20,400,PALETTE.ink,'monospace');
}

export function makePage(sheet, side) {
  const canvas=document.createElement('canvas');canvas.width=W;canvas.height=H;
  const c=canvas.getContext('2d',{alpha:false});
  if(!c)throw new Error('Canvas 2D indisponible');
  c.fillStyle=PALETTE.paper;c.fillRect(0,0,W,H);
  if(side==='front') {
    if(sheet===0)cover(c);
    else {
      const data=CHAPTERS[sheet];
      if(sheet===6){again(c);label(c,'FOLIO / COLLECTED STUDIES','06');}
      else {label(c,`ÉTUDE ${String(sheet).padStart(2,'0')}`,data.title.toUpperCase());[null,interference,tension,cadence,counterform,horizon][sheet](c);}
      foot(c,sheet*2+1);
    }
  }else{
    const ch=Math.min(sheet+1,6),data=CHAPTERS[ch];
    label(c,'FOLIO / ÉTUDES DE MOUVEMENT',`ÉTUDE ${String(ch).padStart(2,'0')}`);
    text(c,String(ch).padStart(2,'0'),57,317,220,900,PALETTE.red);
    const titleSize=data.title.length>12?60:76;
    text(c,data.title,65,430,titleSize,900);
    const next=wrapped(c,data.subtitle,65,499,735,32,43);
    rule(c,next+37);
    const bodyEnd=wrapped(c,data.text,65,next+115,710,30,45);
    wrapped(c,data.detail,65,bodyEnd+38,710,24,37,'#646159');
    text(c,data.note,65,1108,17,400,PALETTE.red,'monospace');foot(c,ch*2);
  }
  return canvas;
}
