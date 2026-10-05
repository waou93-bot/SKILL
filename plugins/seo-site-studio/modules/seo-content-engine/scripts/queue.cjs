const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {validate,load}=require('./validate.cjs');
function stable(v){return JSON.stringify(v,(_,x)=>x&&typeof x==='object'&&!Array.isArray(x)?Object.fromEntries(Object.entries(x).sort(([a],[b])=>a.localeCompare(b))):x);}
function hash(v){return crypto.createHash('sha256').update(stable(v)).digest('hex');}
function ensure(schema,data){const e=validate(load(schema),data);if(e.length)throw Error(e.join('; '));}
function init(config){ensure('ScaleConfig',config);if(new Set(config.sites.map(s=>s.site_id)).size!==config.sites.length)throw Error('Sites dupliqués');return {config,jobs:[],ledger:{},events:[],paused:false};}
function event(state,action,id,now){state.events.push({action,id,at:new Date(now).toISOString()});}
function enqueue(state,jobs,now=Date.now()){
 if(!Array.isArray(jobs))throw Error('Liste attendue');
 const draft=structuredClone(state);
 for(const job of jobs){ensure('QueueJob',job);if(!draft.config.sites.some(s=>s.site_id===job.site_id))throw Error('Site inconnu');
  const id=hash([job.site_id,job.action,job.article_id,job.version]),fingerprint=hash(job),existing=draft.jobs.find(j=>j.id===id);
  if(existing){if(existing.fingerprint!==fingerprint)throw Error('Identité déjà utilisée avec un contenu différent');continue;}
  draft.jobs.push({...job,id,fingerprint,state:'queued',attempts:0,lease:null});event(draft,'enqueue',id,now);
 }
 Object.assign(state,draft);return state.jobs.map(j=>({id:j.id,state:j.state}));
}
function expire(state,now){for(const j of state.jobs)if(j.state==='running'&&j.lease.until<=now){j.state='needs_reconciliation';event(state,'lease_expired',j.id,now);}}
function gate(job,site){if(job.action!=='publish')return true;return site.publishing_mode!=='draft'&&!!job.authorization_reference&&job.validation_passed&&job.validated_version===job.version&&(!job.sensitive_topic||!!job.qualified_approval);}
function claim(state,worker,now=Date.now()){
 if(!/^[A-Za-z0-9_-]{1,64}$/.test(worker))throw Error('Identifiant worker invalide');expire(state,now);if(state.paused)return null;
 if(state.jobs.filter(j=>j.state==='running').length>=state.config.global_concurrency)return null;
 for(const job of state.jobs){if(job.state!=='queued')continue;const site=state.config.sites.find(s=>s.site_id===job.site_id);
  if(site.paused||state.jobs.filter(j=>j.state==='running'&&j.site_id===site.site_id).length>=site.concurrency)continue;
  if(job.attempts>=state.config.max_attempts||!gate(job,site)){job.state='blocked';event(state,'blocked',job.id,now);continue;}
  const month=new Date(now).toISOString().slice(0,7),key=site.site_id+':'+month;
  if(job.reserved_month!==month){const spent=state.ledger[key]||0;if(spent+job.estimated_cost>site.monthly_budget)continue;state.ledger[key]=spent+job.estimated_cost;job.reserved_month=month;}
  job.attempts++;job.state='running';job.lease={token:crypto.randomUUID(),worker,until:now+state.config.lease_seconds*1000};event(state,'claim',job.id,now);return structuredClone(job);
 }return null;
}
function finish(state,id,token,result,now=Date.now()){expire(state,now);const j=state.jobs.find(x=>x.id===id);if(!j||j.state!=='running'||j.lease.token!==token)throw Error('Bail invalide ou expiré');if(!['done','blocked','needs_reconciliation'].includes(result))throw Error('État interdit');j.state=result;if(result!=='needs_reconciliation')j.lease=null;event(state,'finish_'+result,id,now);}
function reconcile(state,id,result,confirmation,now=Date.now()){expire(state,now);const j=state.jobs.find(x=>x.id===id);if(!j||j.state!=='needs_reconciliation'||!['done','queued','blocked'].includes(result)||!confirmation)throw Error('Réconciliation explicite requise');j.state=result;j.lease=null;event(state,'reconcile_'+result,id,now);}
function mutate(file,fn){file=path.resolve(file);const lock=file+'.lock';let fd;try{fd=fs.openSync(lock,'wx',0o600);}catch{throw Error('File verrouillée; vérifier le processus avant toute intervention');}
 let tmp;try{const state=JSON.parse(fs.readFileSync(file,'utf8'));const result=fn(state);tmp=file+'.'+crypto.randomUUID()+'.tmp';fs.writeFileSync(tmp,JSON.stringify(state,null,2),{mode:0o600});const tf=fs.openSync(tmp,'r+');try{fs.fsyncSync(tf);}finally{fs.closeSync(tf);}fs.renameSync(tmp,file);return result;}finally{if(tmp&&fs.existsSync(tmp))fs.unlinkSync(tmp);fs.closeSync(fd);fs.unlinkSync(lock);}}
module.exports={init,enqueue,claim,finish,reconcile,gate,mutate};
if(require.main===module){const [cmd,file,...a]=process.argv.slice(2);try{if(!file)throw Error('Usage: queue.cjs init|enqueue|claim|finish|reconcile|pause|resume|status fichier ...');let result;
 if(cmd==='init'){const state=init(JSON.parse(fs.readFileSync(a[0],'utf8')));fs.mkdirSync(path.dirname(path.resolve(file)),{recursive:true});fs.writeFileSync(file,JSON.stringify(state,null,2),{flag:'wx',mode:0o600});result={initialized:true};}
 else result=mutate(file,state=>{switch(cmd){case 'enqueue':return enqueue(state,JSON.parse(fs.readFileSync(a[0],'utf8')));case 'claim':return claim(state,a[0]);case 'finish':finish(state,a[0],a[1],a[2]);return {updated:true};case 'reconcile':reconcile(state,a[0],a[1],a[2]);return {updated:true};case 'pause':case 'resume':if(a[0]==='all')state.paused=cmd==='pause';else{const s=state.config.sites.find(s=>s.site_id===a[0]);if(!s)throw Error('Site inconnu');s.paused=cmd==='pause';}event(state,cmd,a[0],Date.now());return {updated:true};case 'status':expire(state,Date.now());return {paused:state.paused,ledger:state.ledger,jobs:state.jobs.map(j=>({id:j.id,site:j.site_id,state:j.state,attempts:j.attempts}))};default:throw Error('Commande inconnue');}});
 console.log(JSON.stringify(result,null,2));}catch(e){console.error(['ENOENT','EACCES','EEXIST'].includes(e.code)?'Fichier absent, inaccessible ou déjà présent':e.message);process.exitCode=1;}}
