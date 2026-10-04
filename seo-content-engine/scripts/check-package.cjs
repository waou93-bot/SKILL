const fs=require('node:fs');const {validate,load}=require('./validate.cjs');
function excluded(raw,domains){try{const host=new URL(raw).hostname.toLowerCase().replace(/\.$/,'');return domains.some(d=>{const n=(d.includes('://')?new URL(d).hostname:d).toLowerCase().replace(/\.$/,'');return host===n||host.endsWith('.'+n);});}catch{return true;}}
function check(a,c){const defects=[...validate(load('ArticlePackage'),a),...validate(load('Config'),c)];if(defects.length)return defects;
 for(const claim of a.claims)if(claim.state!=='verified'||!claim.sources.length)defects.push('Affirmation non vérifiée: '+claim.id);
 const urls=[...a.internal_links,...a.external_sources,a.cta.url,...a.claims.flatMap(x=>x.sources)];
 const markdown=a.content_markdown.matchAll(/https?:\/\/[^\s<>\)\]]+/g);for(const m of markdown)urls.push(m[0]);
 for(const u of urls)if(excluded(u,c.excluded_domains||[]))defects.push('URL invalide ou exclue: '+u);
 return [...new Set(defects)];}
module.exports={check,excluded};
if(require.main===module){try{const defects=check(JSON.parse(fs.readFileSync(process.argv[2],'utf8')),JSON.parse(fs.readFileSync(process.argv[3],'utf8')));console.log(JSON.stringify({blocking_defects:defects,remaining_review:['exactitude réelle','liens HTTP et redirections','originalité','données sensibles','intention','validation qualifiée si nécessaire']},null,2));process.exitCode=defects.length?1:0;}catch{console.error('Entrées illisibles');process.exitCode=2;}}
