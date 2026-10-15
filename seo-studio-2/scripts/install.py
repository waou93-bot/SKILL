#!/usr/bin/env python3
"""Copie explicite et non destructive des skills SEO Studio 2 et seo-site-preproduction."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import sys
import tempfile
from studio import (
    ROOT, COMPANION_DIR, check_companion, check_distribution, check_package,
    file_signature, json_text, safe_path,
)


def package_signature(path: Path) -> dict[str,str]:
    return {p:h for p,h in file_signature(path, {'MANIFEST.sha256.json'}).items()
            if not p.startswith(COMPANION_DIR)}


def install(source: Path, target_root: Path, apply: bool = False) -> dict:
    source = source.absolute();target_root=target_root.absolute()
    verification = check_distribution(source)
    if verification['status']!='PACKAGE_INTEGRITY_OK':
        raise ValueError('Intégrité de la distribution refusée : '+str(verification['errors']))
    source_companion = safe_path(source,'seo-site-preproduction')
    if not source_companion.is_dir():
        raise ValueError('Le bundle source doit inclure seo-site-preproduction')
    dest = safe_path(target_root,'seo-studio-2')
    companion_dest = safe_path(target_root,'seo-site-preproduction')
    if dest.resolve()==source.resolve():
        if companion_dest.resolve()==source_companion.resolve():
            return {'status':'ALREADY_PRESENT','targets':[str(dest),str(companion_dest)],
                    'written':False,'host_discovery_verified':False}
        raise ValueError('La source est déjà le dossier Studio ; installez depuis la racine du bundle.')
    if dest.resolve().is_relative_to(source.resolve()) or source.resolve().is_relative_to(dest.resolve()):
        raise ValueError('Source Studio et destination imbriquées')
    if companion_dest.resolve().is_relative_to(source.resolve()) or source_companion.resolve().is_relative_to(companion_dest.resolve()):
        raise ValueError('Source compagnon et destination imbriquées')

    package_present = dest.exists()
    companion_present = companion_dest.exists()
    if dest.is_symlink() or companion_dest.is_symlink():
        raise ValueError('Installation cible symbolique refusée')
    if package_present:
        if not dest.is_dir() or package_signature(dest)!=package_signature(source):
            raise ValueError('SEO Studio 2 existe avec un contenu différent : aucun écrasement. Sauvegarder, comparer et migrer explicitement.')
        if check_package(dest)['status']!='PACKAGE_INTEGRITY_OK':
            raise ValueError('Le package SEO Studio 2 présent échoue à son contrôle d’intégrité.')
    if companion_present:
        if not companion_dest.is_dir() or file_signature(companion_dest)!=file_signature(source_companion):
            raise ValueError('seo-site-preproduction existe avec un contenu différent : aucun écrasement. Sauvegarder, comparer et migrer explicitement.')
        if check_companion(companion_dest,standalone=True)['status']!='COMPANION_INTEGRITY_OK':
            raise ValueError('Le skill seo-site-preproduction présent échoue à son contrôle d’intégrité.')
    if package_present and companion_present:
        return {'status':'ALREADY_IDENTICAL','targets':[str(dest),str(companion_dest)],
                'written':False,'host_discovery_verified':False}
    if not apply:
        return {'status':'DRY_RUN','targets':[str(dest),str(companion_dest)],
                'written':False,'source_files':len(package_signature(source)),
                'companion_files':verification.get('companion_files',0),
                'warning':'Aucun fichier copié ; découverte hôte et dépendances restent à vérifier séparément.'}

    target_root.mkdir(parents=True,exist_ok=True)
    lock=target_root/'.seo-studio-2.install.lock'
    try:
        fh=lock.open('x',encoding='utf-8')
    except FileExistsError as exc:
        raise ValueError('Une installation est en cours ou un verrou reste à examiner') from exc
    stage_parent=None
    try:
        with fh: fh.write('SEO STUDIO 2 + seo-site-preproduction installation locale\n')
        if dest.exists() and not package_present:
            raise ValueError('Le dossier SEO Studio 2 vient d’apparaître ; copie suspendue')
        if companion_dest.exists() and not companion_present:
            raise ValueError('Le dossier seo-site-preproduction vient d’apparaître ; copie suspendue')
        stage_parent=Path(tempfile.mkdtemp(prefix='.seo-studio-2-stage-',dir=target_root))
        staged=None
        staged_companion=None
        if not package_present:
            staged=stage_parent/'seo-studio-2'
            shutil.copytree(source,staged,ignore=shutil.ignore_patterns(
                '__pycache__','*.pyc','.git','seo-site-preproduction'))
            result=check_package(staged)
            if result['status']!='PACKAGE_INTEGRITY_OK':
                raise ValueError('Échec de vérification du package SEO Studio 2 préparé : '+str(result['errors']))
        if not companion_present:
            staged_companion=stage_parent/'seo-site-preproduction'
            shutil.copytree(source_companion,staged_companion,
                            ignore=shutil.ignore_patterns('__pycache__','*.pyc','.git'))
            if file_signature(staged_companion)!=file_signature(source_companion):
                raise ValueError('Les empreintes du skill compagnon ont changé pendant la préparation')
            if check_companion(staged_companion,standalone=True)['status']!='COMPANION_INTEGRITY_OK':
                raise ValueError('Le skill compagnon préparé échoue à son contrôle d’intégrité')
        if dest.exists() and not package_present:
            raise ValueError('Destination SEO Studio 2 créée pendant la préparation ; aucun remplacement')
        if companion_dest.exists() and not companion_present:
            raise ValueError('Destination du skill compagnon créée pendant la préparation ; aucun remplacement')
        if staged is not None:
            staged.rename(dest)
        if staged_companion is not None:
            staged_companion.rename(companion_dest)
        if check_package(dest)['status']!='PACKAGE_INTEGRITY_OK':
            raise ValueError('Vérification finale de SEO Studio 2 en échec ; conserver le dossier et diagnostiquer')
        if check_companion(companion_dest,standalone=True)['status']!='COMPANION_INTEGRITY_OK':
            raise ValueError('Vérification finale du skill compagnon en échec ; conserver les dossiers et diagnostiquer')
    finally:
        if stage_parent and stage_parent.exists():
            shutil.rmtree(stage_parent)
        lock.unlink(missing_ok=True)
    installed=[]
    if not package_present: installed.append(str(dest))
    if not companion_present: installed.append(str(companion_dest))
    return {'status':'FILES_INSTALLED','targets':[str(dest),str(companion_dest)],
            'installed':installed,'written':bool(installed),'host_discovery_verified':False,
            'dependencies_installed':False,'personna_training_executed':False,
            'warning':'Les deux skills sont copiés séparément. La copie ne prouve pas leur détection par Codex ni un fonctionnement multiagent.'}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--target-root',type=Path,required=True)
    p.add_argument('--apply',action='store_true')
    args=p.parse_args()
    try:
        print(json_text(install(ROOT,args.target_root,args.apply)),end='')
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json_text({'status':'BLOQUE','error':str(exc)}),end='')
        return 2

if __name__ == '__main__':
    sys.exit(main())
