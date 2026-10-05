"""Check completion declarations, not website quality or authenticity of evidence."""
import json
import sys
from pathlib import Path

REQUIRED = {'contexte','skills','recherche','toolbox','architecture','design','donnees','contenu','realisation','seo','recette','livraison'}

def check(data):
    errors = []
    steps = data.get('steps', [])
    ids = [s.get('id') for s in steps]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate step IDs')
    for missing in sorted(REQUIRED - set(ids)):
        errors.append('Missing step: ' + missing)
    for s in steps + data.get('pages', []):
        label = s.get('id') or s.get('url') or '?'
        state = s.get('state')
        if state == 'VERIFIE':
            if not s.get('evidence') or not s.get('verification'):
                errors.append(str(label) + ': missing evidence or verification')
        elif state == 'NON_APPLICABLE':
            if not s.get('reason'):
                errors.append(str(label) + ': missing exclusion reason')
        else:
            errors.append(str(label) + ': unfinished (' + str(state) + ')')
    if not data.get('pages'):
        errors.append('Missing page inventory')
    return errors

if __name__ == '__main__':
    data = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8-sig'))
    errors = check(data)
    print(json.dumps({'scope':'completion_declarations','passed':not errors,'errors':errors}, ensure_ascii=False))
    sys.exit(bool(errors))
