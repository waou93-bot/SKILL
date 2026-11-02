"""Offline HTML inventory; lexical overlap is a candidate signal, not semantic judgment."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack=[]; self.title=[]; self.headings=[]; self.links=[]; self.main=[]; self.body=[]; self.h=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.stack.append(tag)
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag in ('h1','h2'): self.h=[tag,[]]
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs); self.handle_endtag(tag)
    def handle_endtag(self, tag):
        if self.h and self.h[0]==tag:
            self.headings.append({'level':tag,'text':' '.join(' '.join(self.h[1]).split())}); self.h=None
        if tag in self.stack:
            idx=len(self.stack)-1-self.stack[::-1].index(tag); del self.stack[idx:]
    def handle_data(self, data):
        if 'title' in self.stack: self.title.append(data)
        if self.h: self.h[1].append(data)
        if any(x in self.stack for x in ('script','style','nav','header','footer','noscript')): return
        if any(x in self.stack for x in ('main','article')): self.main.append(data)
        elif 'body' in self.stack: self.body.append(data)

VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
_original=Page.handle_starttag
def start(self,tag,attrs):
    _original(self,tag,attrs)
    if tag in VOID: self.handle_endtag(tag)
Page.handle_starttag=start

def analyze(root,max_files=2000,max_bytes=2_000_000):
    root=Path(root)
    if root.is_symlink() or not root.is_dir(): raise ValueError('Root must be a real directory')
    if max_files<1 or max_bytes<1: raise ValueError('Limits must be positive')
    root=root.resolve(); pages=[]; errors=[]; skipped=0; seen=0
    for path in sorted(root.rglob('*')):
        if path.suffix.lower() not in ('.html','.htm'): continue
        seen+=1
        if seen>max_files: skipped+=1; continue
        rel=path.relative_to(root).as_posix()
        try:
            if any(p.is_symlink() for p in (path,*list(path.parents)[:len(path.relative_to(root).parts)-1])) or not path.resolve().is_relative_to(root): raise ValueError('symbolic or outside root')
            if path.stat().st_size>max_bytes: raise ValueError('size limit exceeded')
            parser=Page(); parser.feed(path.read_text(encoding='utf-8-sig'))
            text=' '.join(' '.join(parser.main or parser.body).split())
            tokens=set(re.findall(r'[^\W\d_]{3,}',text.casefold(),flags=re.UNICODE))
            pages.append({'file':rel,'title':' '.join(' '.join(parser.title).split()),'headings':parser.headings,'links':parser.links,'word_count':len(re.findall(r'\b\w+\b',text,flags=re.UNICODE)),'content_excerpt':text[:500], 'text_empty':not bool(text),'_tokens':tokens})
        except (OSError,UnicodeError,ValueError) as exc: errors.append({'file':rel,'error':str(exc)})
    pairs=[]
    for i,a in enumerate(pages):
        for b in pages[i+1:]:
            if len(a['_tokens'])<10 or len(b['_tokens'])<10: continue
            union=a['_tokens']|b['_tokens']; score=len(a['_tokens']&b['_tokens'])/len(union)
            if score>=0.4: pairs.append({'a':a['file'],'b':b['file'],'jaccard':round(score,3)})
    pairs.sort(key=lambda p:(-p['jaccard'],p['a'],p['b']))
    for p in pages: del p['_tokens']
    return {'scope':'local HTML; no rendering, no crawl; lexical candidates only','root':str(root),'coverage':{'discovered':seen,'analyzed':len(pages),'failed':len(errors),'skipped_limit':skipped,'complete':bool(pages) and not errors and not skipped},'pages':pages,'lexical_candidates':pairs[:100], 'candidate_limit':100,'errors':errors}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root');p.add_argument('--max-files',type=int,default=2000);p.add_argument('--max-bytes',type=int,default=2000000);a=p.parse_args()
    try: result=analyze(a.root,a.max_files,a.max_bytes)
    except (ValueError,OSError) as exc: print(json.dumps({'status':'NOT_RUN','error':str(exc)},ensure_ascii=False),file=sys.stderr);return 2
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['coverage']['complete'] else 1
if __name__=='__main__':raise SystemExit(main())

