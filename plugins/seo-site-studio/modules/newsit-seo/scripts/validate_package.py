"""Validate package integrity only; no claim about agent or website behavior."""
import json
import re
import sys
from pathlib import Path


def validate(root):
    errors = []
    required = [
        'SKILL.md', 'README.md', 'agents/openai.yaml', 'evals/evals.json',
        'references/integrations.md', 'references/vitrine.md',
        'references/marchand.md', 'references/affiliation.md',
        'references/seo-et-recette.md',
        'references/evaluation.md', 'assets/brief.md', 'assets/pages.csv',
        'scripts/install.ps1', 'references/deux-stacks.md',
        'references/google-bing-seo.md', 'assets/seo-obligatoire.csv',
    ]
    for name in required:
        if not (root / name).is_file():
            errors.append(f'Missing: {name}')
    for path in root.rglob('*'):
        if not path.is_file() or path.suffix not in {'.md', '.json', '.yaml', '.py', '.ps1', '.csv'}:
            continue
        try:
            body = path.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError:
            errors.append(f'Not UTF-8: {path.relative_to(root)}')
            continue
        if '\ufffd' in body or '\x00' in body:
            errors.append(f'Encoding artifact: {path.relative_to(root)}')
        if path.suffix == '.md':
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                    continue
                candidate = (path.parent / target.split('#', 1)[0]).resolve()
                if not candidate.is_relative_to(root):
                    errors.append(f'Link outside package: {target}')
                elif not candidate.is_file():
                    errors.append(f'Broken link: {path.name} -> {target}')
    skill_path = root / 'SKILL.md'
    if skill_path.is_file():
        skill = skill_path.read_text(encoding='utf-8-sig')
        if not re.match(r'^---\nname: newsit-seo\n', skill):
            errors.append('Unexpected skill name/frontmatter')
        front = re.match(r'^---\n(.*?)\n---(?:\n|$)', skill, re.S)
        if not front:
            errors.append('Invalid frontmatter boundaries')
        else:
            for field, limit in [('description', 1024), ('compatibility', 500)]:
                value = re.search(r'^' + field + r': (.+)$', front.group(1), re.M)
                try:
                    parsed = json.loads(value.group(1)) if value else None
                    if not isinstance(parsed, str) or not parsed.strip() or len(parsed) > limit:
                        errors.append(f'Invalid or too long frontmatter scalar: {field}')
                except (ValueError, AttributeError):
                    errors.append(f'Invalid quoted frontmatter scalar: {field}')
        if len(skill.splitlines()) >= 500:
            errors.append('SKILL.md should stay under 500 lines')
    eval_path = root / 'evals/evals.json'
    if eval_path.is_file():
        try:
            evals = json.loads(eval_path.read_text(encoding='utf-8-sig'))
            if evals.get('skill_name') != 'newsit-seo':
                errors.append('Mismatched eval skill_name')
            ids = []
            for item in evals.get('evals', []):
                ids.append(item.get('id'))
                for field in ('id', 'prompt', 'expected_output', 'files', 'expectations'):
                    if field not in item:
                        errors.append(f'Eval {item.get("id")}: missing {field}')
                for name in item.get('files', []):
                    if not (root / name).is_file():
                        errors.append(f'Eval input missing: {name}')
            if len(ids) != len(set(ids)) or not ids:
                errors.append('Empty or duplicate eval IDs')
        except (ValueError, TypeError) as exc:
            errors.append(f'Invalid eval JSON: {exc}')
    return errors


if __name__ == '__main__':
    package_root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parents[1]).resolve()
    problems = validate(package_root)
    print(json.dumps({'scope': 'package_integrity', 'passed': not problems, 'errors': problems}, ensure_ascii=True))
    sys.exit(1 if problems else 0)
