"""Synthetic unit tests only; these fixtures are not real project observations."""
from __future__ import annotations
import copy
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_handoff import validate_handoff

def fixture():
    return {
      'kind':'HANDOFF','schema_version':'1.0','run_id':'SYNTHETIC-TEST',
      'project_id':'fixture-only','as_of':'2026-09-16','entrypoint':'standalone',
      'mode':'CADRAGE','channel_decision':'PILOTE','technical_readiness':'NON_AUDITE',
      'evidence_basis':'DOCUMENTAIRE','decision_rationale':'Test unitaire fictif.',
      'objective':'Valider le contrôleur, pas un projet.',
      'observation_scope':{'inspected_urls':[],'known_url_population':None,
                           'environments':[],'limitations':['Pas de site réel.']},
      'critical_checks':[],'blocking_issues':[],'project_outcome_evidence':[],
      'unknowns':[],'artifacts':[],'limitations':['Fixture synthétique.'],
      'permissions':{'granted_actions':[],'evidence':[],'max_cash_eur':None},
      'tasks':[],'next_action_ids':[],'next_review':{'automated':False},
    }
def task(action='analysis',cost=0):
    return {'id':'T1','action':action,'cash_cost':cost,
            'required_permissions':[action],'dependencies':[],'status':'PROPOSE'}
def ready(d):
    d['technical_readiness']='PRET_POUR_TEST'
    d['observation_scope']['inspected_urls']=['https://example.invalid/test']
    d['critical_checks']=[{'id':'C1','status':'PASS','evidence':'Fixture synthétique.'}]

def permit(d,*actions,cap=None):
    d['permissions']={'granted_actions':list(actions),
                      'evidence':['Autorisation fictive du test unitaire.'],'max_cash_eur':cap}

class HandoffTests(unittest.TestCase):
    def test_empty_pilot_can_be_proposed(self): self.assertEqual([],validate_handoff(fixture()))
    def test_template_rejected(self):
        d=fixture(); d['kind']='TEMPLATE'; self.assertTrue(validate_handoff(d))
    def test_priority_from_desk_rejected(self):
        d=fixture(); d['channel_decision']='PRIORITAIRE'; self.assertTrue(validate_handoff(d))
    def test_priority_with_project_evidence(self):
        d=fixture(); d.update(channel_decision='PRIORITAIRE',evidence_basis='MIXTE')
        d['project_outcome_evidence']=[{'source':'fixture','observed_at':'2026-09-16','finding':'Fictif.'}]
        self.assertEqual([],validate_handoff(d))
    def test_ready_without_inspection_rejected(self):
        d=fixture(); d['technical_readiness']='PRET_POUR_TEST'; self.assertTrue(validate_handoff(d))
    def test_ready_with_checks(self):
        d=fixture(); ready(d); self.assertEqual([],validate_handoff(d))
    def test_ready_with_failed_check_rejected(self):
        d=fixture(); ready(d); d['critical_checks'][0]['status']='FAIL'; self.assertTrue(validate_handoff(d))
    def test_blocker_overrides_ready(self):
        d=fixture(); ready(d); d['blocking_issues']=['blocked']; self.assertTrue(validate_handoff(d))
    def test_proposal_is_not_permission(self):
        d=fixture(); d['tasks']=[task('publish')]; self.assertEqual([],validate_handoff(d))
        d['next_action_ids']=['T1']; self.assertTrue(validate_handoff(d))
    def test_permitted_ready_publish(self):
        d=fixture(); ready(d); permit(d,'publish'); d['tasks']=[task('publish')]; d['next_action_ids']=['T1']
        self.assertEqual([],validate_handoff(d))
    def test_permission_requires_trace(self):
        d=fixture(); permit(d,'edit_code'); d['permissions']['evidence']=[]; self.assertTrue(validate_handoff(d))
    def test_empty_required_permissions_cannot_bypass(self):
        d=fixture(); d['tasks']=[task('delete_content')]; d['tasks'][0]['required_permissions']=[]
        d['next_action_ids']=['T1']; self.assertTrue(validate_handoff(d))
    def test_known_spend_within_cap(self):
        d=fixture(); permit(d,'spend',cap=50); d['tasks']=[task('spend',40)]; d['next_action_ids']=['T1']
        self.assertEqual([],validate_handoff(d))
    def test_overspend_rejected(self):
        d=fixture(); permit(d,'spend',cap=50); d['tasks']=[task('spend',51)]; d['next_action_ids']=['T1']
        self.assertTrue(validate_handoff(d))
    def test_unknown_spend_rejected(self):
        d=fixture(); permit(d,'spend',cap=50); d['tasks']=[task('spend',None)]; d['next_action_ids']=['T1']
        self.assertTrue(validate_handoff(d))
    def test_automation_not_provided(self):
        d=fixture(); d['next_review']['automated']=True; self.assertTrue(validate_handoff(d))
    def test_partial_scope_disclosed(self):
        d=fixture(); d['observation_scope'].update(known_url_population=100,limitations=[])
        self.assertTrue(validate_handoff(d))
    def test_dependency_before_action(self):
        d=fixture(); permit(d,'analysis'); a=task(); b=copy.deepcopy(a); b['id']='T2'; b['dependencies']=['T1']
        d['tasks']=[a,b]; d['next_action_ids']=['T2','T1']; self.assertTrue(validate_handoff(d))
        d['next_action_ids']=['T1','T2']; self.assertEqual([],validate_handoff(d))
    def test_invalid_shapes_do_not_crash(self):
        for d in [None,[],{}, {'kind':'HANDOFF','tasks':[None,{'id':'T1','action':[]}], 'next_action_ids':['T1']}]:
            with self.subTest(d=d): self.assertTrue(validate_handoff(d))
    def test_nan_cost_rejected(self):
        d=fixture(); d['tasks']=[task('spend',float('nan'))]; self.assertTrue(validate_handoff(d))
    def test_duplicate_task_rejected(self):
        d=fixture(); d['tasks']=[task(),task()]; self.assertTrue(validate_handoff(d))

if __name__=='__main__': unittest.main()
