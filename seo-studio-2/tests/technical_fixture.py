"""Explicitly synthetic release protocol records; no browser/site execution."""
import studio
from technical_audit import site_context_digest

def complete_technical(project,state):
    base=project/'TECHNICAL';base.mkdir(exist_ok=True)
    source=base/'source.html';source.write_text('SYNTHETIC HTML snapshot, no actual site',encoding='utf-8')
    routes=[p['path'] for p in state['pages'] if p['public'] and p['wave']=='V1']
    state['technical_audit']={'report_path':'TECHNICAL/report.json','evidence_id':'technical-report',
                              'target_url':'http://127.0.0.1/','browser_routes':routes,'performance_routes':routes,
                              'scope_reason':'SYNTHETIC fixture covers each current route, not an actual audit'}
    page={'url':'http://127.0.0.1/','status':200,'html':True,'h1':['Synthetic'],'title':'Synthetic',
          'description':'Synthetic','canonicals':['http://127.0.0.1/'],'noindex':False,
          'robots_allowed':True,'jsonld':[]}
    meta={'tool':'SYNTHETIC_FIXTURE','version':'1','route':'/','profile':'synthetic mobile','observed_at':'2026-10-14'}
    report={'schema_version':'1.0.0','run_id':state['run_id'],'site_context_sha256':site_context_digest(state),
            'target':'http://127.0.0.1/',
            'site_snapshots':[{'path':'TECHNICAL/source.html','sha256':studio.digest(source)}],
            'status':'PASS','errors':[],'warnings':['Entirely synthetic fixture, no actual HTTP/browser/performance measured'],
            'http':{'status':'PASS','complete':True,'pages':[page],'robots':{'status':200},
                    'sitemap':{'status':200},'sitemap_urls':['http://127.0.0.1/'],'evidence_id':'technical-http'},
            'browser':{'status':'PASS','evidence_id':'technical-browser','runs':[{**meta,'checks':{'rendered_dom':True,'navigation':True,'console_errors':False,'raw_content_present':True,'raw_links_present':True}}]},
            'performance':{'status':'PASS','evidence_id':'technical-performance','runs':[{**meta,'measurement':'laboratory','mobile':True,'metrics':{'lcp_ms':100,'cls':0,'tbt_ms':0},'budgets':{'lcp_ms':2500,'cls':.1,'tbt_ms':200}}]}}
    report['http']['pages']=[{**page,'url':'http://127.0.0.1'+route,'requested_url':'http://127.0.0.1'+route,
                             'canonicals':['http://127.0.0.1'+route]} for route in routes]
    report['http']['sitemap_urls']=['http://127.0.0.1'+route for route in routes]
    for kind in ('browser','performance'):
        original=report[kind]['runs'][0]
        report[kind]['target']='http://127.0.0.1/'
        report[kind]['runs']=[{**original,'route':route,'requested_url':'http://127.0.0.1'+route,
                              'final_url':'http://127.0.0.1'+route} for route in routes]
    for kind in ('http','browser','performance'):
        path='TECHNICAL/'+kind+'.json'
        (project/path).write_text(studio.json_text({k:v for k,v in report[kind].items() if k!='evidence_id'}),encoding='utf-8')
        state['evidence'].append({'id':'technical-'+kind,'kind':'http' if kind=='http' else 'test_report','path':path,'sha256':studio.digest(project/path),'origin':'SYNTHETIC protocol only'})
    (project/'TECHNICAL/report.json').write_text(studio.json_text(report),encoding='utf-8')
    state['evidence'].append({'id':'technical-report','kind':'test_report','path':'TECHNICAL/report.json','sha256':studio.digest(project/'TECHNICAL/report.json'),'origin':'SYNTHETIC protocol only'})
    return report
