"""Check recorded consistency only; never probes a site or grants permission."""
import json,sys,os,posixpath
STATES=['CONCEPTION','LOCAL_VERIFIE','PREPROD_PRIVEE_VERIFIEE','PRET_PRODUCTION','PRODUCTION_VERIFIEE']
def check(s):
 errors=[]
 if s.get('state') not in STATES:return ['unknown state']
 if not s.get('version'):errors.append('artifact version missing')
 git=s.get('git')
 if git:
  if git.get('applicable') is False:
   if not git.get('reason'):errors.append('Git exclusion requires reason')
  elif git.get('applicable') is True:
   for field in ['root','branch','base_sha','head','preservation_record']:
    if not git.get(field):errors.append('Git record missing: '+field)
   owners=git.get('file_owners',[])
   paths=[posixpath.normpath(o.get('path','').replace('\\','/')) for o in owners]
   if not git.get('case_sensitive_paths',os.name!='nt'):paths=[p.casefold() for p in paths]
   if len(paths)!=len(set(paths)):errors.append('multiple Git file owners')
   if git.get('integration_status')=='verified':
    if git.get('conflicts_remaining'):errors.append('verified integration with conflicts')
    if git.get('tested_revision')!=git.get('head'):errors.append('Git tests cover old revision')
    if git.get('tested_base_sha')!=git.get('base_sha'):errors.append('Git base moved after tests')
    if not git.get('diff_review_source') or not git.get('test_source'):errors.append('Git integration proof missing')
    if git.get('test_result')!='pass':errors.append('Git final tests not successful')
    if git.get('ci_required') and (git.get('ci_revision')!=git.get('head') or git.get('ci_result')!='pass'):errors.append('required CI not verified on final revision')
   for action in git.get('external_actions',[]):
    if action.get('status')=='done' and (not action.get('action') or not action.get('target') or not any(a.get('action')==action.get('action') and a.get('target')==action.get('target') and a.get('human_source') for a in s.get('authorizations',[]))):errors.append('Git external action lacks recorded authorization')
  else:errors.append('Git scope missing')
 def evidence(kind):
  remote=kind in ['served_version','access_control','noindex','https','production_indexability']
  environment='production' if s['state']=='PRODUCTION_VERIFIEE' else 'preproduction'
  return any(e.get('kind')==kind and e.get('version')==s.get('version') and e.get('result')=='pass' and e.get('source') and e.get('date') and not e.get('invalidated',False) and (not remote or (e.get('target')==s.get('url') and e.get('environment')==environment)) for e in s.get('evidence',[]))
 def authorized(action):
  return any(a.get('action')==action and a.get('target')==s.get('url') and a.get('human_source') for a in s.get('authorizations',[]))
 idx=STATES.index(s['state'])
 if idx>=1:
  for kind in ['technical','visual','seo','user_journey']:
   if not evidence(kind):errors.append('current evidence missing: '+kind)
  architecture=s.get('seo_architecture',{})
  if architecture.get('applicable') is False:
   if not architecture.get('reason'):errors.append('SEO scope exclusion requires reason')
  elif architecture.get('applicable') is True:
   families=architecture.get('families',{})
   for family in ['accueil','categories','selections','marques_modeles','comparatifs','questions','catalogue','destination']:
    record=families.get(family,{})
    if record.get('status')=='not_applicable':
     if not record.get('reason'):errors.append('SEO family exclusion requires reason: '+family)
    elif record.get('status')!='verified' or not record.get('artifact'):errors.append('SEO family unverified: '+family)
   for kind in ['seo_intentions','seo_catalogue','seo_link_graph','seo_family_coverage']:
    if not evidence(kind):errors.append('SEO architecture evidence missing: '+kind)
  else:errors.append('SEO architecture scope missing')
 if s['state']=='PREPROD_PRIVEE_VERIFIEE':
  if not s.get('url'):errors.append('preprod URL missing')
  if not authorized('deploy_preprod'):errors.append('preprod authorization missing')
  for kind in ['served_version','access_control','noindex']:
   if not evidence(kind):errors.append('preprod evidence missing: '+kind)
 if idx>=3:
  if not s.get('domain'):errors.append('domain missing')
  if not s.get('facts_confirmed'):errors.append('essential facts unconfirmed')
  for kind in ['domain_access','release_rollback_plan']:
   if not evidence(kind):errors.append('readiness evidence missing: '+kind)
 if idx==4:
  if not s.get('url'):errors.append('production URL missing')
  if not authorized('deploy_production'):errors.append('production authorization missing')
  for kind in ['served_version','https','production_indexability']:
   if not evidence(kind):errors.append('production evidence missing: '+kind)
 if s.get('status')=='COMPLET' and s.get('blockers'):errors.append('complete with blockers')
 return errors
if __name__=='__main__':
 errors=check(json.load(open(sys.argv[1],encoding='utf-8')))
 print(json.dumps({'valid_record':not errors,'errors':errors,'scope':'record consistency only'},ensure_ascii=False))
 sys.exit(bool(errors))
