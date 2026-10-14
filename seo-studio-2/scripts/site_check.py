"""Contrôle hors réseau d'un export HTML. Ne certifie ni rendu ni indexation."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ''
        self.in_title = False
        self.description = ''
        self.ids = set()
        self.links = []
        self.assets = []
        self.image_alts = []
        self.search = False
        self.robots = ''
        self.canonical = ''

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'title':
            self.in_title = True
        if tag == 'meta':
            name = a.get('name', '').lower()
            if name == 'description':
                self.description = a.get('content', '')
            if name == 'robots':
                self.robots = a.get('content', '')
        if tag == 'link' and 'canonical' in a.get('rel', '').split():
            self.canonical = a.get('href', '')
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'input' and a.get('type', '').lower() == 'search':
            self.search = True
        if tag in {'img', 'script', 'source'} and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'link' and 'stylesheet' in a.get('rel', '').split() and a.get('href'):
            self.assets.append(a['href'])
        if tag == 'img':
            self.image_alts.append(a.get('alt'))

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def route(path, root):
    value = '/' + path.relative_to(root).as_posix()
    return value[:-10] if value.endswith('index.html') else value


def check(root: Path, landing_routes=(), public_base=None):
    root = root.resolve()
    if not root.is_dir():
        raise ValueError('Dossier HTML absent')
    docs, files, errors, warnings = {}, {}, [], []
    for file in sorted(root.rglob('*.html')):
        if file.is_symlink() or not file.resolve().is_relative_to(root):
            errors.append('Fichier symbolique ou sortant : ' + str(file))
            continue
        key = route(file, root)
        doc = Document()
        doc.feed(file.read_text(encoding='utf-8-sig'))
        docs[key], files[key] = doc, file
    if not docs:
        errors.append('Aucune page HTML à contrôler')
    base = urlsplit(public_base) if public_base else None
    if base and (base.scheme not in {'http', 'https'} or not base.hostname or base.username or base.password or base.path not in {'', '/'} or base.query or base.fragment):
        raise ValueError('public-base doit être une origine HTTP(S), sans secret ni sous-chemin')

    def resolve(owner, target):
        parsed = urlsplit(urljoin('https://local.invalid' + owner, target))
        internal = parsed.hostname == 'local.invalid' or (base and parsed.netloc == base.netloc and parsed.scheme == base.scheme)
        if not internal:
            return None
        dest = (root / unquote(parsed.path).lstrip('/')).resolve()
        if not dest.is_relative_to(root):
            raise ValueError('Destination hors export : ' + target)
        if dest.is_dir():
            dest /= 'index.html'
        elif not dest.suffix and not dest.is_file():
            dest = dest / 'index.html'
        return dest, unquote(parsed.fragment)

    graph = {key: set() for key in docs}
    for owner, doc in docs.items():
        if not doc.title.strip():
            errors.append(owner + ' : title absent/vide')
        if not doc.description.strip():
            errors.append(owner + ' : meta description absente/vide')
        if owner not in landing_routes and not doc.search:
            errors.append(owner + ' : recherche interne absente (hors landing)')
        if any(alt is None for alt in doc.image_alts):
            errors.append(owner + ' : image sans attribut alt')
        for target in doc.links + doc.assets:
            try:
                result = resolve(owner, target)
                if result is None:
                    continue
                dest, fragment = result
                if not dest.is_file():
                    errors.append(owner + ' : destination absente : ' + target)
                    continue
                if dest.suffix.lower() == '.html':
                    key = route(dest, root)
                    graph[owner].add(key)
                    if fragment and (key not in docs or fragment not in docs[key].ids):
                        errors.append(owner + ' : fragment absent : ' + target)
            except ValueError as exc:
                errors.append(owner + ' : ' + str(exc))
        if public_base and 'noindex' not in doc.robots.lower():
            if not doc.canonical:
                warnings.append(owner + ' : canonical à vérifier selon le contrat de page')
            elif doc.canonical != public_base.rstrip('/') + owner:
                errors.append(owner + ' : canonical incohérente avec la route')
    seen, queue = set(), ['/'] if '/' in docs else []
    while queue:
        key = queue.pop()
        if key in seen:
            continue
        seen.add(key)
        queue.extend(graph.get(key, set()) - seen)
    if '/' in docs:
        for key, doc in docs.items():
            if key not in seen and 'noindex' not in doc.robots.lower():
                errors.append(key + ' : page orpheline depuis accueil')
    else:
        warnings.append('Accueil / absent : accessibilité du graphe non contrôlée')
    warnings.append('Présence du champ uniquement : pertinence/corpus complet/clavier/mobile exigent une recette réelle. Liens externes, HTTP, Safari et indexation non testés.')
    return {'status': 'BLOQUE' if errors else 'LOCAL_HTML_OK', 'pages': len(docs), 'errors': sorted(set(errors)), 'warnings': warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('export', type=Path)
    parser.add_argument('--landing-route', action='append', default=[], help='Route réellement classée landing ; répétable. Aucune exception implicite.')
    parser.add_argument('--public-base')
    args = parser.parse_args()
    try:
        report = check(args.export, args.landing_route, args.public_base)
    except (ValueError, OSError, UnicodeError) as exc:
        report = {'status': 'BLOQUE', 'errors': [str(exc)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if report['status'] == 'BLOQUE' else 0


if __name__ == '__main__':
    raise SystemExit(main())
