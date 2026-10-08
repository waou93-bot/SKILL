import assert from 'node:assert/strict';
import {paperProfile,boundedPage,spreadFaces,PAGE_WIDTH,SHEETS} from './src/paper.mjs';
for(let s=0;s<SHEETS;s++)for(let i=0;i<=100;i++){
  const profile=paperProfile(i/100,32,s);
  assert.ok(profile.every(p=>Number.isFinite(p.x)&&Number.isFinite(p.z)));
  for(let n=1;n<profile.length;n++)assert.ok(Math.abs(Math.hypot(profile[n].x-profile[n-1].x,profile[n].z-profile[n-1].z)-PAGE_WIDTH/32)<1e-9);
  if(i===0)assert.ok(Math.abs(profile.at(-1).x-PAGE_WIDTH)<1e-9);
  if(i===100)assert.ok(Math.abs(profile.at(-1).x+PAGE_WIDTH)<1e-9);
}
assert.ok(paperProfile(.5).at(-1).x>0,'Le bord libre doit suivre le pli');
const forward=paperProfile(.5),reverse=paperProfile(.5,64,0,-1);
assert.ok(reverse.at(-1).x<0,'La courbure inverse doit suivre le mouvement vers la droite');
for(let i=0;i<forward.length;i++)assert.ok(Math.abs(forward[i].x+reverse[i].x)<1e-9&&Math.abs(forward[i].z-reverse[i].z)<1e-9,'Les courbures opposées doivent être miroirs');
assert.equal(boundedPage(-10),0);assert.equal(boundedPage(999),SHEETS-1);
for(let i=0;i<SHEETS;i++)assert.ok(spreadFaces(i).every(f=>f.sheet>=0&&f.sheet<SHEETS));
console.log('Profil, longueur du papier, courbure, bornes et faces validés. Le GPU et les interactions navigateur ne sont pas couverts.');
