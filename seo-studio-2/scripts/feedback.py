"""Review supplied post-launch evidence. No API, scheduler or publication writes."""
import argparse
from datetime import date
import hashlib
import json
import math
from pathlib import Path


def check_feedback(project, state, data, *, load, safe_path, digest):
    if not isinstance(data, dict) or data.get('schema_version') != '1':
        raise ValueError('Monitoring : objet de format 1 attendu')
    if data.get('run_id') != state['run_id']:
        raise ValueError('Monitoring : projet différent')
    release = data.get('release_snapshot')
    if not isinstance(release, dict):
        raise ValueError('Monitoring : instantané de publication absent')
    snapshot = safe_path(project, release.get('path'), True)
    if digest(snapshot) != release.get('sha256'):
        raise ValueError('Monitoring : instantané de publication modifié')
    frozen = load(snapshot)
    if not isinstance(frozen, dict) or frozen.get('run_id') != state['run_id']:
        raise ValueError('Monitoring : instantané hors projet')
    pages = {p['id']: p for p in frozen['pages']}
    source = data.get('source')
    if not isinstance(source, dict) or not all(isinstance(source.get(k), str) and source[k].strip()
                                             for k in ('provider', 'exported_at', 'path', 'sha256', 'limitations')):
        raise ValueError('Monitoring : provenance et limites de données requises')
    date.fromisoformat(source['exported_at'])
    if digest(safe_path(project, source['path'], True)) != source['sha256']:
        raise ValueError('Monitoring : export source modifié')
    source_data = load(safe_path(project, source['path'], True))
    if not isinstance(source_data, dict) or source_data.get('rows') != data.get('rows'):
        raise ValueError('Monitoring : lignes différentes de l’export source normalisé')
    baseline, current = data.get('baseline'), data.get('current')
    windows = []
    for window in (baseline, current):
        if not isinstance(window, dict):
            raise ValueError('Monitoring : deux fenêtres de comparaison requises')
        start, end = date.fromisoformat(window['start']), date.fromisoformat(window['end'])
        if end < start:
            raise ValueError('Monitoring : fenêtre inversée')
        windows.append((start, end, (end-start).days+1))
    if windows[0][1] >= windows[1][0] or windows[0][2] != windows[1][2]:
        raise ValueError('Monitoring : fenêtres distinctes de même durée requises')
    thresholds = data.get('thresholds', {})
    if not isinstance(thresholds, dict):
        raise ValueError('Monitoring : seuils invalides')
    min_impressions = thresholds.get('min_impressions', 100)
    ctr_drop = thresholds.get('relative_ctr_drop', .2)
    if type(min_impressions) is not int or min_impressions < 1 or type(ctr_drop) not in (int,float) or not 0 < ctr_drop < 1:
        raise ValueError('Monitoring : seuils invalides')
    rows = data.get('rows')
    if not isinstance(rows, list) or not rows:
        raise ValueError('Monitoring : données absentes, aucune conclusion')
    actions, seen = [], set()
    for row in rows:
        if not isinstance(row, dict) or row.get('page_id') not in pages or row['page_id'] in seen:
            raise ValueError('Monitoring : page inconnue ou dupliquée')
        seen.add(row['page_id'])
        for period in ('baseline', 'current'):
            metrics = row.get(period)
            if not isinstance(metrics, dict):
                raise ValueError('Monitoring : métriques absentes')
            for key in ('impressions', 'clicks', 'conversions', 'position'):
                value = metrics.get(key)
                if value is not None and (type(value) not in (int,float) or not math.isfinite(value) or value < 0):
                    raise ValueError('Monitoring : métrique invalide')
            if any(metrics.get(k) is not None and type(metrics[k]) is not int for k in ('impressions','clicks','conversions')):
                raise ValueError('Monitoring : compte entier attendu')
            if metrics.get('clicks') is not None and metrics.get('impressions') is not None and metrics['clicks'] > metrics['impressions']:
                raise ValueError('Monitoring : clics supérieurs aux impressions')
        before, after = row['baseline'], row['current']
        recommendation, reason = 'OBSERVE', 'Données insuffisantes ou pas de signal dépassant les seuils'
        if all(x.get('impressions') is not None and x.get('clicks') is not None and x['impressions'] >= min_impressions
               for x in (before, after)):
            old_ctr, new_ctr = before['clicks']/before['impressions'], after['clicks']/after['impressions']
            if old_ctr > 0 and new_ctr <= old_ctr*(1-ctr_drop):
                recommendation, reason = 'REVIEW_SNIPPET_AND_INTENT', 'Baisse relative du CTR au-delà du seuil ; cause à examiner, aucune réécriture automatique'
        if row.get('indexation') == 'NOT_INDEXED':
            recommendation, reason = 'INVESTIGATE_INDEXATION', 'Non-indexation rapportée : vérifier accès, canonical et utilité ; aucune suppression automatique'
        elif row.get('indexation') not in ('INDEXED', 'UNKNOWN', None):
            raise ValueError('Monitoring : état d’indexation invalide')
        actions.append({'page_id': row['page_id'], 'recommendation': recommendation, 'reason': reason})
    impacted = {a['page_id'] for a in actions if a['recommendation'] != 'OBSERVE'}
    # Proposed work opens a new revision; the published snapshot stays immutable.
    return {'status': 'REVIEWED_SUPPLIED_DATA', 'actions': actions,
            'review_ids_to_reopen_if_changes_approved': [r['id'] for r in state['reviews']] if impacted else [],
            'published_snapshot_modified': False, 'external_actions_taken': False,
            'interpretation': 'Signals and proposed investigations only. Seasonality, position mix and causality require review. No ranking promise.'}


def main():
    from studio import load, safe_path, digest
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('--input', default='monitoring/state.json')
    args=parser.parse_args()
    try:
        state=load(safe_path(args.project,'state.json',True))
        result=check_feedback(args.project,state,load(safe_path(args.project,args.input,True)),load=load,safe_path=safe_path,digest=digest)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return 0
    except (ValueError,OSError,KeyError,TypeError) as exc:
        parser.exit(2,'BLOCKED: '+str(exc)+'\n')


if __name__=='__main__':
    raise SystemExit(main())
