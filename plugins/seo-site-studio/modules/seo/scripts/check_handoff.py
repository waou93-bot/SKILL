#!/usr/bin/env python3
"""Check a SEO handoff's internal consistency. Does not execute or authorize tasks.

Python 3.10+, standard library only. Evidence authenticity and user permissions
must also be verified by the host. A valid JSON document is not an approval.
"""
from __future__ import annotations
import argparse
from datetime import date
import json
import math
from pathlib import Path
from typing import Any

MODES = {'CADRAGE','AUDIT','PREFLIGHT','MIGRATION','SUIVI','CORRECTION_CIBLEE'}
CHANNELS = {'A_EVALUER','PILOTE','PRIORITAIRE','SECONDAIRE','NON_PRIORITAIRE','BLOQUE_DONNEES'}
READINESS = {'NON_AUDITE','PARTIEL','BLOQUANT','PRET_POUR_TEST'}
BASES = {'DOCUMENTAIRE','OBSERVATIONS_PROJET','MIXTE'}
ACTIONS = {'analysis','write_report','edit_code','publish','deploy','edit_robots',
           'delete_content','spend','outreach','install_tracking'}

def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def money(value: Any) -> bool:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(value) and value >= 0
    except OverflowError:
        return False

def validate_handoff(data: Any) -> list[str]:
    """Return deterministic errors, without network access or side effects."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return ['Le document doit être un objet JSON.']
    if data.get('kind') != 'HANDOFF':
        errors.append('kind doit être HANDOFF : un TEMPLATE n’est pas un résultat exécutable.')
    if data.get('schema_version') != '1.0':
        errors.append('schema_version doit être 1.0.')
    for key in ('run_id','project_id','as_of','decision_rationale','objective'):
        if not nonempty(data.get(key)):
            errors.append(f'{key} doit être renseigné.')
    try:
        date.fromisoformat(data.get('as_of', ''))
    except (ValueError, TypeError):
        errors.append('as_of doit être une date ISO YYYY-MM-DD.')
    for key, allowed in [('mode',MODES),('channel_decision',CHANNELS),
                         ('technical_readiness',READINESS),('evidence_basis',BASES)]:
        if not isinstance(data.get(key),str) or data[key] not in allowed:
            errors.append(f'{key} invalide.')

    def obj(key: str) -> dict:
        result = data.get(key)
        if not isinstance(result,dict):
            errors.append(f'{key} doit être un objet.'); return {}
        return result
    def arr(parent: dict, key: str, prefix: str='') -> list:
        result = parent.get(key)
        if not isinstance(result,list):
            errors.append(f'{prefix}{key} doit être une liste.'); return []
        return result

    scope = obj('observation_scope')
    urls = arr(scope,'inspected_urls','observation_scope.')
    if any(not nonempty(x) for x in urls):
        errors.append('Les URL inspectées doivent être des chaînes non vides.')
    if len([x for x in urls if isinstance(x,str)]) != len(set(x for x in urls if isinstance(x,str))):
        errors.append('URL inspectées dupliquées.')
    limits = arr(scope,'limitations','observation_scope.')
    arr(scope,'environments','observation_scope.')
    population = scope.get('known_url_population')
    if population is not None:
        if not isinstance(population,int) or isinstance(population,bool) or population < 0:
            errors.append('known_url_population doit être null ou un entier positif/nul.')
        elif population < len(urls):
            errors.append('Plus d’URL inspectées que la population déclarée.')
        elif population > len(urls) and not limits:
            errors.append('Un échantillon partiel doit déclarer ses limites.')
    checks = arr(data,'critical_checks')
    blockers = arr(data,'blocking_issues')
    outcomes = arr(data,'project_outcome_evidence')
    arr(data,'unknowns'); arr(data,'artifacts'); arr(data,'limitations')
    if data.get('channel_decision') == 'PRIORITAIRE':
        if data.get('evidence_basis') == 'DOCUMENTAIRE' or not outcomes:
            errors.append('PRIORITAIRE requiert des observations de résultat propres au projet.')
        for row in outcomes:
            if not isinstance(row,dict) or any(not nonempty(row.get(k)) for k in ('source','observed_at','finding')):
                errors.append('Chaque preuve de résultat doit avoir source, observed_at et finding.')
    if data.get('technical_readiness') == 'PRET_POUR_TEST':
        if not urls or not checks:
            errors.append('PRET_POUR_TEST requiert un périmètre inspecté et des contrôles critiques.')
        if any(not isinstance(c,dict) or c.get('status') != 'PASS'
               or not nonempty(c.get('id')) or not nonempty(c.get('evidence')) for c in checks):
            errors.append('Tous les contrôles critiques du périmètre doivent être PASS et sourcés.')
        if blockers:
            errors.append('PRET_POUR_TEST incompatible avec des blocages non résolus.')
    if data.get('technical_readiness') == 'BLOQUANT' and not blockers:
        errors.append('BLOQUANT doit préciser les blocages.')

    permissions = obj('permissions')
    grants_raw = arr(permissions,'granted_actions','permissions.')
    permission_evidence = arr(permissions,'evidence','permissions.')
    grants = {x for x in grants_raw if isinstance(x,str)}
    if len(grants_raw) != len(grants) or not grants.issubset(ACTIONS):
        errors.append('Permissions inconnues, non textuelles ou dupliquées.')
    if grants and (not permission_evidence or any(not nonempty(x) for x in permission_evidence)):
        errors.append('Les permissions accordées doivent référencer une autorisation réelle.')
    cap = permissions.get('max_cash_eur')
    if cap is not None and not money(cap):
        errors.append('max_cash_eur doit être null ou un montant fini non négatif.')

    tasks = arr(data,'tasks')
    by_id: dict[str,dict] = {}
    for task in tasks:
        if not isinstance(task,dict) or not nonempty(task.get('id')):
            errors.append('Chaque tâche doit avoir un id.'); continue
        tid = task['id']
        if tid in by_id:
            errors.append(f'Identifiant de tâche dupliqué : {tid}.')
        by_id[tid] = task
        action = task.get('action')
        if not isinstance(action,str) or action not in ACTIONS:
            errors.append(f'{tid}: action invalide.')
        req = task.get('required_permissions')
        if not isinstance(req,list) or any(not isinstance(p,str) or p not in ACTIONS for p in req):
            errors.append(f'{tid}: required_permissions invalide.')
        elif action not in req:
            errors.append(f'{tid}: required_permissions doit inclure son action.')
        cost = task.get('cash_cost')
        if cost is not None and not money(cost):
            errors.append(f'{tid}: cash_cost doit être null ou un montant fini non négatif.')
        deps = task.get('dependencies')
        if not isinstance(deps,list) or any(not nonempty(p) for p in deps):
            errors.append(f'{tid}: dependencies doit être une liste d’identifiants.')
    for tid,task in by_id.items():
        deps=task.get('dependencies',[])
        if isinstance(deps,list):
            for dep in deps:
                if not isinstance(dep,str) or dep not in by_id or dep == tid:
                    errors.append(f'{tid}: dépendance absente ou invalide.')

    selected = arr(data,'next_action_ids')
    selected_ids = [x for x in selected if isinstance(x,str)]
    if len(selected_ids) != len(selected) or len(selected_ids) != len(set(selected_ids)):
        errors.append('next_action_ids doit contenir des identifiants uniques.')
    spend_total = 0.0
    for index,tid in enumerate(selected_ids):
        if tid not in by_id:
            errors.append(f'Action sélectionnée inexistante : {tid}.'); continue
        task = by_id[tid]; action = task.get('action'); req = task.get('required_permissions')
        if isinstance(action,str) and action not in grants:
            errors.append(f'{tid}: action non autorisée.')
        if isinstance(req,list) and any(not isinstance(p,str) or p not in grants for p in req):
            errors.append(f'{tid}: permission requise non accordée.')
        if isinstance(action,str) and action in {'publish','deploy'} and data.get('technical_readiness') != 'PRET_POUR_TEST':
            errors.append(f'{tid}: publication/déploiement sans état technique prêt sur le périmètre.')
        cost = task.get('cash_cost')
        if action == 'spend' and not money(cost):
            errors.append(f'{tid}: dépense sélectionnée sans montant connu.')
        if money(cost) and cost > 0:
            spend_total += cost
            if 'spend' not in grants:
                errors.append(f'{tid}: coût sélectionné sans permission spend.')
        deps=task.get('dependencies',[])
        if isinstance(deps,list):
            for dep in deps:
                if isinstance(dep,str) and dep in by_id and by_id[dep].get('status') != 'DONE' and dep not in selected_ids[:index]:
                    errors.append(f'{tid}: dépendance non terminée ni planifiée avant cette action.')
    if spend_total > 0 and (not money(cap) or spend_total > cap):
        errors.append('Dépenses sélectionnées supérieures au plafond approuvé ou plafond absent.')
    review = obj('next_review')
    if review.get('automated') is not False:
        errors.append('Aucune automatisation récurrente n’est fournie par ce package.')
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file',type=Path)
    args=parser.parse_args()
    try:
        data=json.loads(args.file.read_text(encoding='utf-8-sig'))
    except (OSError,ValueError) as exc:
        print(f'Lecture impossible : {exc}'); return 2
    errors=validate_handoff(data)
    if errors:
        print('\n'.join(f'ERREUR — {x}' for x in errors)); return 1
    print('Cohérence contrôlée. Ni autorisation utilisateur ni vérité des preuves certifiées.')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
