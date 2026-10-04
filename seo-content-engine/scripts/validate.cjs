const fs=require('node:fs'),path=require('node:path');
function validate(s,v,p='$'){
 const e=[]; const types=Array.isArray(s.type)?s.type:[s.type];
 const actual=v===null?'null':Array.isArray(v)?'array':typeof v==='number'&&Number.isInteger(v)?'integer':typeof v;
 if(s.type&&!types.includes(actual)&&!(actual==='integer'&&types.includes('number')))return [p+': type invalide'];
 if(s.enum&&!s.enum.some(x=>JSON.stringify(x)===JSON.stringify(v)))e.push(p+': valeur hors enum');
 if(v&&actual==='object'){for(const k of s.required||[])if(!(k in v))e.push(p+'.'+k+': requis');for(const [k,x] of Object.entries(v)){if(s.properties?.[k])e.push(...validate(s.properties[k],x,p+'.'+k));else if(s.additionalProperties===false)e.push(p+'.'+k+': propriété inconnue');}}
 if(actual==='array')v.forEach((x,i)=>e.push(...validate(s.items,x,p+'['+i+']')));
 if(typeof v==='number'&&((s.minimum!==undefined&&v<s.minimum)||(s.maximum!==undefined&&v>s.maximum)))e.push(p+': hors limites');
 if(typeof v==='string'&&s.format){let ok=true;if(s.format==='uri'){try{const u=new URL(v);ok=['http:','https:'].includes(u.protocol);}catch{ok=false;}}if(s.format==='date')ok=/^\d{4}-\d{2}-\d{2}$/.test(v)&&!isNaN(Date.parse(v))&&new Date(v).toISOString().slice(0,10)===v;if(s.format==='date-time')ok=/^\d{4}-\d{2}-\d{2}T.*(?:Z|[+-]\d{2}:\d{2})$/.test(v)&&!isNaN(Date.parse(v));if(!ok)e.push(p+': format '+s.format);}
 return e;
}
function load(name){if(!/^[A-Za-z]+$/.test(name))throw Error('Nom de schéma invalide');return JSON.parse(fs.readFileSync(path.join(__dirname,'../schemas',name+'.schema.json'),'utf8'));}
module.exports={validate,load};
if(require.main===module){try{const e=validate(load(process.argv[2]),JSON.parse(fs.readFileSync(process.argv[3],'utf8')));console.log(JSON.stringify({valid:!e.length,errors:e},null,2));process.exitCode=e.length?1:0;}catch(e){console.error('Validation impossible: vérifier nom et fichier JSON');process.exitCode=2;}}
