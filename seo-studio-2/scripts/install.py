#!/usr/bin/env python3
"""Copie explicite et non destructive du seul package SEO STUDIO 2. Hors ligne."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import sys
import tempfile
from studio import ROOT, check_package, file_signature, json_text, safe_path


def install(source: Path, target_root: Path, apply: bool = False) -> dict:
    source = source.absolute();target_root=target_root.absolute()
    verification = check_package(source)
    if verification['status']!='PACKAGE_INTEGRITY_OK':
        raise ValueError('Intégrité source refusée : '+str(verification['errors']))
    dest = safe_path(target_root,'seo-studio-2')
    if dest.resolve()==source.resolve():
        return {'status':'ALREADY_PRESENT','target':str(dest),'written':False,'host_discovery_verified':False}
    if dest.resolve().is_relative_to(source.resolve()) or source.resolve().is_relative_to(dest.resolve()):
        raise ValueError('Source et destination imbriquées')
    if dest.exists():
        if dest.is_dir() and file_signature(source)==file_signature(dest):
            return {'status':'ALREADY_IDENTICAL','target':str(dest),'written':False,'host_discovery_verified':False}
        raise ValueError('Installation différente existante : aucun écrasement. Sauvegarder, comparer et autoriser une migration séparée.')
    if not apply:
        return {'status':'DRY_RUN','target':str(dest),'written':False,'source_files':verification['files'],
                'warning':'Aucun fichier copié. Le contrôle des dépendances et la découverte hôte restent séparés.'}
    target_root.mkdir(parents=True,exist_ok=True)
    lock=target_root/'.seo-studio-2.install.lock'
    try:
        fh=lock.open('x',encoding='utf-8')
    except FileExistsError as exc:
        raise ValueError('Une installation est en cours ou un verrou reste à examiner') from exc
    stage_parent=None
    try:
        with fh: fh.write('SEO STUDIO 2 installation locale\n')
        if dest.exists():
            raise ValueError('La destination vient d’apparaître ; copie suspendue')
        stage_parent=Path(tempfile.mkdtemp(prefix='.seo-studio-2-stage-',dir=target_root))
        staged=stage_parent/'seo-studio-2'
        shutil.copytree(source,staged,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.git'))
        result=check_package(staged)
        if result['status']!='PACKAGE_INTEGRITY_OK':
            raise ValueError('Échec de vérification de la copie')
        if dest.exists():
            raise ValueError('Destination créée pendant la préparation ; aucun remplacement')
        staged.rename(dest)
        result=check_package(dest)
        if result['status']!='PACKAGE_INTEGRITY_OK':
            raise ValueError('Vérification finale en échec ; conserver le dossier et diagnostiquer')
    finally:
        if stage_parent and stage_parent.exists():
            shutil.rmtree(stage_parent)
        lock.unlink(missing_ok=True)
    return {'status':'FILES_INSTALLED','target':str(dest),'written':True,'host_discovery_verified':False,
            'dependencies_installed':False,'personna_training_executed':False,
            'warning':'La copie n’est pas la preuve de détection par Codex ni de fonctionnement multiagent.'}


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

if __name__=='__main__':
    sys.exit(main())
