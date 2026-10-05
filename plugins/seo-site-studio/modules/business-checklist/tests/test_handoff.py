"""Synthetic fixtures only. These are not real market tests or customer observations."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))
from check_handoff import validate_handoff, validate_checklist, validate_bundle

TEMPLATE = json.loads((SKILL / "assets/05-decision-handoff.json").read_text(encoding="utf-8"))
CHECKLIST = json.loads((SKILL / "assets/08-checklist.json").read_text(encoding="utf-8"))

def assessment(decision="TESTER"):
    d = deepcopy(TEMPLATE)
    d.update(kind="ASSESSMENT", run_id="synthetic-run", project_id="synthetic-project",
             as_of="2026-09-16", decision=decision, decision_rationale="Synthetic rationale for a unit test, not a business assessment.",
             checklist_ref="10_CHECKLIST.json")
    return d

def go_fixture():
    d = assessment("GO_PILOTE")
    d["evidence_basis"] = "MIXTE"
    d["evidence"] = [{"id":"E1", "type":"OBSERVATION_TERRAIN", "verified":True,
                       "claim":"Synthetic field observation for testing the validator only.",
                       "source_ref":"fixtures/fictional-pilot.md", "observed_at":"2026-09-15", "relevance":"PROJET"}]
    for g in d["gates"]:
        g.update(result="FAVORABLE", rationale="Synthetic test fixture.", evidence_ids=["E1"])
    d["next_step"].update(scope="Synthetic pilot", max_cash_eur=100, max_hours=2,
                           owner="Synthetic owner", review_date="2026-09-30", budget_evidence_ref="fixtures/budget.md")
    d["finance"]["without_unsecured_funding_reviewed"] = True
    d["next_actions"] = [{"id":"P0-1", "action":"Synthetic action, do not execute."}]
    return d

class HandoffTests(unittest.TestCase):
    def assert_invalid(self, d):
        self.assertTrue(validate_handoff(d)[0])
    def test_template_valid_but_warns(self):
        errors, warnings = validate_handoff(TEMPLATE)
        self.assertEqual(errors, [])
        self.assertTrue(warnings)
    def test_template_cannot_carry_decision(self):
        d=deepcopy(TEMPLATE); d["decision"]="TESTER"; self.assert_invalid(d)
    def test_template_cannot_grant_permissions(self):
        d=deepcopy(TEMPLATE); d["permissions"].update(granted_actions=["spend"],approval_ref="fake"); self.assert_invalid(d)
    def test_documentary_testing_is_allowed(self):
        self.assertEqual(validate_handoff(assessment())[0], [])
    def test_bounded_go_with_synthetic_field_data_consistent(self):
        self.assertEqual(validate_handoff(go_fixture())[0], [])
    def test_documentary_go_rejected(self):
        d=go_fixture(); d["evidence_basis"]="DOCUMENTAIRE"; self.assert_invalid(d)
    def test_unverified_field_data_rejected(self):
        d=go_fixture(); d["evidence"][0]["verified"]=False; self.assert_invalid(d)
    def test_competitor_field_data_is_not_project_evidence(self):
        d=go_fixture(); d["evidence"][0]["relevance"]="EXTERNE"; self.assert_invalid(d)
    def test_field_evidence_must_be_used_by_gate(self):
        d=go_fixture(); d["evidence"].append(dict(d["evidence"][0], id="E2", type="FAIT_SOURCE"))
        for g in d["gates"]: g["evidence_ids"]=["E2"]
        self.assert_invalid(d)
    def test_unresolved_critical_gate_rejected(self):
        d=go_fixture(); d["gates"][0]["result"]="NON_CONCLUANT"; self.assert_invalid(d)
    def test_blocker_prevents_go(self):
        d=go_fixture(); d["blocking_issues"]=["Unresolved blocker"]; self.assert_invalid(d)
    def test_missing_budget_rejected(self):
        d=go_fixture(); d["next_step"]["max_cash_eur"]=None; self.assert_invalid(d)
    def test_negative_budget_rejected(self):
        d=go_fixture(); d["next_step"]["max_cash_eur"]=-1; self.assert_invalid(d)
    def test_boolean_budget_rejected(self):
        d=go_fixture(); d["next_step"]["max_cash_eur"]=True; self.assert_invalid(d)
    def test_infinite_budget_rejected(self):
        d=go_fixture(); d["next_step"]["max_cash_eur"]=float("inf"); self.assert_invalid(d)
    def test_zero_budget_is_valid(self):
        d=go_fixture(); d["next_step"]["max_cash_eur"]=0; self.assertEqual(validate_handoff(d)[0], [])
    def test_missing_time_cap_rejected(self):
        d=go_fixture(); d["next_step"]["max_hours"]=None; self.assert_invalid(d)
    def test_missing_review_rejected(self):
        d=go_fixture(); d["next_step"]["review_date"]=None; self.assert_invalid(d)
    def test_trigger_instead_of_date_allowed(self):
        d=go_fixture(); d["next_step"].update(review_date=None,review_trigger="After synthetic observation"); self.assertEqual(validate_handoff(d)[0], [])
    def test_without_funding_stress_required_for_go(self):
        d=go_fixture(); d["finance"]["without_unsecured_funding_reviewed"]=False; self.assert_invalid(d)
    def test_unknown_evidence_ref_rejected(self):
        d=go_fixture(); d["gates"][0]["evidence_ids"]=["MISSING"]; self.assert_invalid(d)
    def test_duplicate_evidence_rejected(self):
        d=go_fixture(); d["evidence"].append(deepcopy(d["evidence"][0])); self.assert_invalid(d)
    def test_duplicate_gate_rejected(self):
        d=assessment(); d["gates"][0]["id"]="G2"; self.assert_invalid(d)
    def test_permission_requires_trace(self):
        d=assessment(); d["permissions"]["granted_actions"]=["spend"]; self.assert_invalid(d)
    def test_missing_permission_does_not_forge_authorization(self):
        errors,warnings=validate_handoff(go_fixture()); self.assertEqual(errors,[])
        self.assertTrue(any("No execution permission" in x for x in warnings))
    def test_reconciled_model_requires_checks(self):
        d=assessment(); d["finance"].update(status="RECONCILIE", model_ref="model.xlsx"); self.assert_invalid(d)
    def test_absent_seo_allowed(self):
        d=assessment(); d["seo"]["status"]="ABSENT"; self.assertEqual(validate_handoff(d)[0], [])
    def test_fake_seo_execution_rejected(self):
        d=assessment(); d["seo"]["status"]="EXECUTE_AVEC_TRACE"; self.assert_invalid(d)
    def test_seo_double_count_check_required(self):
        d=assessment(); d["seo"].update(status="EXECUTE_AVEC_TRACE",source_ref="SEO/handoff.json"); self.assert_invalid(d)
    def test_stop_needs_documented_blocker(self):
        self.assert_invalid(assessment("STOP_VERSION_ACTUELLE"))
    def test_information_block_names_missing_information(self):
        self.assert_invalid(assessment("BLOQUE_INFORMATION"))
        d=assessment("BLOQUE_INFORMATION"); d["unknowns"]=["Authorized project budget not supplied."]
        self.assertEqual(validate_handoff(d)[0], [])
    def test_unknown_success_score_rejected(self):
        d=assessment(); d["success_score"]=99; self.assert_invalid(d)
    def test_false_verified_hypothesis_rejected(self):
        d=go_fixture(); d["evidence"][0]["type"]="HYPOTHESE"; self.assert_invalid(d)
    def test_bad_date_rejected(self):
        d=assessment(); d["as_of"]="2026-02-30"; self.assert_invalid(d)
    def test_non_object_fails_cleanly(self):
        self.assert_invalid([])

class ChecklistTests(unittest.TestCase):
    def test_template_has_sixty_controls(self):
        self.assertEqual(len(CHECKLIST["checks"]),60)
        self.assertEqual(validate_checklist(CHECKLIST),[])
    def assessed(self):
        d=deepcopy(CHECKLIST); d["kind"]="ASSESSMENT"
        for c in d["checks"]: c["critical_for_next_scope"]=False
        return d
    def test_etaye_requires_evidence(self):
        d=self.assessed(); d["checks"][0].update(status="ETAYE",rationale="Enough for current scope.")
        self.assertTrue(validate_checklist(d))
    def test_non_applicable_requires_reason(self):
        d=self.assessed(); d["checks"][0]["status"]="NON_APPLICABLE"
        self.assertTrue(validate_checklist(d))
    def test_duplicate_ids_rejected(self):
        d=deepcopy(CHECKLIST); d["checks"][1]["id"]=d["checks"][0]["id"]
        self.assertTrue(validate_checklist(d))
    def test_test_status_requires_next_action(self):
        d=self.assessed(); d["checks"][0].update(status="A_TESTER",rationale="Not measured.")
        self.assertTrue(validate_checklist(d))
    def test_cross_file_evidence_references_checked(self):
        d=self.assessed(); d["checks"][0].update(status="ETAYE",rationale="Synthetic example.",evidence_ids=["E1"])
        self.assertTrue(validate_checklist(d,set()))
        self.assertEqual(validate_checklist(d,{"E1"}),[])
    def test_template_cannot_claim_evidence(self):
        d=deepcopy(CHECKLIST); d["checks"][0].update(status="ETAYE",rationale="Synthetic example.",evidence_ids=["E1"])
        self.assertTrue(validate_checklist(d))

class BundleTests(unittest.TestCase):
    def test_templates_are_compatible(self):
        self.assertEqual(validate_bundle(TEMPLATE,CHECKLIST)[0],[])
    def test_assessment_cannot_reference_template(self):
        self.assertTrue(validate_bundle(assessment(),CHECKLIST)[0])
    def test_different_project_rejected(self):
        d=assessment(); c=deepcopy(CHECKLIST)
        c.update(kind="ASSESSMENT",project_id="other",run_id=d["run_id"],as_of=d["as_of"])
        for check in c["checks"]: check["critical_for_next_scope"]=False
        self.assertTrue(validate_bundle(d,c)[0])
    def test_launch_requires_quantified_financial_model(self):
        d=go_fixture(); d["decision"]="LANCER_PROGRESSIVEMENT"
        self.assertTrue(validate_handoff(d)[0])
        d["finance"].update(status="CHIFFRE",model_ref="fixtures/synthetic-finance.json")
        self.assertEqual(validate_handoff(d)[0],[])
    def test_unresolved_critical_check_blocks_go(self):
        d=go_fixture(); c=deepcopy(CHECKLIST)
        c.update(kind="ASSESSMENT",project_id=d["project_id"],run_id=d["run_id"],as_of=d["as_of"])
        for check in c["checks"]: check["critical_for_next_scope"]=False
        c["checks"][0].update(critical_for_next_scope=True,status="A_TESTER",rationale="Unresolved.",next_action="Test.")
        self.assertTrue(validate_bundle(d,c)[0])
        c["checks"][0].update(status="ETAYE",evidence_ids=["E1"])
        self.assertEqual(validate_bundle(d,c)[0],[])

if __name__ == "__main__":
    unittest.main()
