#!/usr/bin/env python3
"""Render Pages CMS JSON into the existing static site. No third-party packages."""
import argparse
import html
import json
import re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'\{\{([\w.]+)\}\}')

def safe_url(value):
    value = value.strip()
    if re.search(r'[\x00-\x20]', value) or urlsplit(value).scheme.lower() not in ('', 'http', 'https', 'mailto', 'tel'):
        raise ValueError('Links must use a normal web, email, phone, or relative address')
    return value

class RichText(HTMLParser):
    allowed = {'p','br','strong','b','em','i','u','s','a','ul','ol','li','blockquote','h2','h3','h4','img','hr','code','pre','table','thead','tbody','tr','th','td','span','small','sub','sup'}
    def handle_starttag(self, tag, attrs):
        if tag not in self.allowed:
            raise ValueError(f'Unsupported content element: {tag}')
        for name,value in attrs:
            if name.startswith('on') or name in ('srcdoc','style'):
                raise ValueError(f'Unsupported content attribute: {name}')
            if name in ('src','href'):safe_url(value or '')

def rich(value):
    RichText().feed(value)
    return value

def render(template, content, specs, site):
    def replace(match):
        key=match[1]
        if key.startswith('site.'):
            return html.escape(site[key[5:]], quote=True)
        spec=specs[key]
        value=content[key]
        if spec.get('site')=='email':value=site['email']
        elif spec.get('site')=='gmail':value='https://mail.google.com/mail/?view=cm&fs=1&to='+quote(site['email'],safe='')
        if not isinstance(value,str):raise ValueError(f'{key} must contain text')
        kind=spec['kind']
        if kind=='url':return html.escape(safe_url(value),quote=True)
        if kind=='text':return html.escape(value,quote=True)
        value=rich(value)
        single=re.fullmatch(r'\s*<p>(.*?)</p>\s*',value,re.S)
        if single and re.search(r'</?p\b',single[1]):single=None
        if kind=='inline':
            result=single[1] if single else value
            if re.search(r'<(?:p|ul|ol|div|h[1-6])\b',result):
                raise ValueError('List item text must remain a single paragraph')
            return result
        opening=spec['opening']
        if single:return opening+single[1]+'</p>'
        # Multiple paragraphs/images/lists need a block wrapper rather than nested <p> tags.
        opening=opening.replace('<p','<div',1)
        if 'class="' in opening:opening=opening.replace('class="','class="cms-rich-text ',1)
        else:opening=opening[:-1]+' class="cms-rich-text">'
        return opening+value+'</div>'
    return TOKEN.sub(replace,template)

def build(output):
    manifest=json.loads((ROOT/'scripts/content-manifest.json').read_text())
    site=json.loads((ROOT/'content/site.json').read_text())
    rendered={}
    for path,item in manifest.items():
        content=json.loads((ROOT/item['content']).read_text())
        rendered[path]=render((ROOT/'templates'/path).read_text(),content,item['fields'],site)
    # Validate all content before writing any output.
    for path,value in rendered.items():
        target=output/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(value)
    print(f'Rendered {len(rendered)} CMS pages')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    build(parser.parse_args().output.resolve())
