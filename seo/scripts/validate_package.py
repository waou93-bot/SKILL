#!/usr/bin/env python3
"""Structural SEO skill checks. No network, changes, or third-party dependencies."""
from __future__ import annotations
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['SKILL.md','agents/openai.yaml','references/recherche-benchmark.md',
 'references/audit-technique.md','references/contenu-autorite.md','references/mesure-economie.md',
 'references/ia-verticales.md','references/gates-experiences.md','references/sources.md',
 'references/sources.json','scripts/check_handoff.py','scripts/validate_package.py',
 'tests/test_handoff.py','tests/functional-cases.md']

def validate(root: Path=ROOT) -> tuple[list[str],dict[str,int]]:
    errors=[]; counts={'files':0,'json':0,'templates':0,'local_links':0,'sources':0}
    for rel in REQUIRED:
        if not (root/rel).is_file(): errors.append(f'Fichier requis absent : {rel}')
    files=[p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc']
    counts['files']=len(files)
    for p in root.rglob('*'):
        if p.is_symlink(): errors.append(f'Lien symbolique non attendu : {p}')
    skill=(root/'SKILL.md').read_text(encoding='utf-8') if (root/'SKILL.md').is_file() else ''
    match=re.match(r'^---\n(.*?)\n---\n',skill,re.S)
    if not match or not re.search(r'^name:\s*seo\s*$',match.group(1),re.M) or not re.search(r'^description:\s*',match.group(1),re.M):
        errors.append('Frontmatter SKILL.md incomplet.')
    interface=(root/'agents/openai.yaml').read_text(encoding='utf-8') if (root/'agents/openai.yaml').is_file() else ''
    for key in ('interface:','display_name:','short_description:','default_prompt:','policy:','allow_implicit_invocation:'):
        if key not in interface: errors.append(f'Métadonnée interface absente : {key}')
    for p in files:
        if p.suffix=='.json':
            counts['json']+=1
            try: data=json.loads(p.read_text(encoding='utf-8'))
            except (ValueError,OSError) as exc: errors.append(f'{p.name}: {exc}'); continue
            if 'assets' in p.parts:
                counts['templates']+=1
                if not isinstance(data,dict) or data.get('kind')!='TEMPLATE':
                    errors.append(f'{p.name}: modèle non identifié TEMPLATE.')
        if p.suffix=='.md':
            content=p.read_text(encoding='utf-8')
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',content):
                target=target.strip().split(' "')[0]
                if urlparse(target).scheme or target.startswith('#'): continue
                target=unquote(target.split('#')[0])
                q=(p.parent/target).resolve()
                counts['local_links']+=1
                if not q.is_relative_to(root.resolve()): errors.append(f'{p.name}: lien sortant du skill : {target}')
                elif not q.exists(): errors.append(f'{p.name}: lien local absent : {target}')
    try:
        source_data=json.loads((root/'references/sources.json').read_text(encoding='utf-8'))
        ids=set()
        for row in source_data['sources']:
            counts['sources']+=1
            if row['id'] in ids: errors.append('Source dupliquée : '+row['id'])
            ids.add(row['id'])
            if not row['url'].startswith('https://'): errors.append('URL source non HTTPS.')
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',row['accessed_at']): errors.append('Date source invalide.')
    except (OSError,ValueError,KeyError,TypeError) as exc:
        errors.append(f'Catalogue de sources invalide : {exc}')
    if len(list((root/'assets').glob('*'))) != 12: errors.append('12 modèles assets attendus.')
    return errors,counts

def main() -> int:
    errors,counts=validate()
    print(json.dumps(counts,ensure_ascii=False,indent=2))
    if errors:
        print('\n'.join('ERREUR — '+e for e in errors)); return 1
    print('Structure OK. YAML : présence lexicale des clés, pas analyseur YAML complet.')
    print('Aucune intégration hôte ni performance SEO évaluée.')
    return 0
if __name__=='__main__':
    raise SystemExit(main())
