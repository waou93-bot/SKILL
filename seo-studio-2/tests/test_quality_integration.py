"""Régressions du contrat de dépendances ; aucune recette navigateur simulée."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_studio import fixture, write
import studio


class QualityIntegrationTests(unittest.TestCase):
    def test_inventory_includes_quality_without_seo_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in studio.QUALITY:
                write(root/name/'SKILL.md', f'---\nname: {name}\ndescription: Functional testing\n---\nInstructions\n')
            names = {e['name'] for e in studio.inventory([root])['entries']}
            self.assertEqual(names, studio.QUALITY)

    def test_missing_quality_blocks_handoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            state = fixture(project)
            for name in studio.QUALITY:
                with self.subTest(name=name):
                    saved = state['dependencies']
                    state['dependencies'] = [d for d in saved if d['name'] != name]
                    write(project/'state.json', studio.json_text(state))
                    result = studio.validate_project(project, 'handoff')
                    self.assertIn('Socle de dépendances incomplet', result['errors'])
                    state['dependencies'] = saved

    def test_quality_cannot_bypass_reading_as_later_phase(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            state = fixture(project)
            dep = next(d for d in state['dependencies'] if d['name'] == 'webapp-testing')
            dep.update(status='PREPARE_PHASE_ULTERIEURE', reason='Pas encore de site')
            write(project/'state.json', studio.json_text(state))
            self.assertTrue(any('obligatoire : webapp-testing' in e for e in studio.validate_project(project, 'handoff')['errors']))


if __name__ == '__main__':
    unittest.main()
