import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path
from html.parser import HTMLParser

spec=importlib.util.spec_from_file_location('build_content',Path(__file__).with_name('build-content.py'))
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)

class ContentTests(unittest.TestCase):
    def test_all_pages_build_and_configuration_fields_exist(self):
        config=json.loads((build.ROOT/'.pages.yml').read_text())
        for entry in config['content']:
            data=json.loads((build.ROOT/entry['path']).read_text())
            for field in entry['fields']:self.assertIn(field['name'],data)
        with tempfile.TemporaryDirectory() as temp:
            build.build(Path(temp))
            self.assertEqual(len(list(Path(temp).rglob('*.html'))),13)
            for path in Path(temp).rglob('*.html'):
                self.assertNotRegex(path.read_text(),r'\{\{(?:field_|site\.)')

    def test_multi_paragraph_edits_keep_valid_wrapper(self):
        result=build.render('{{body}}',{'body':'<p>Hello <strong>world</strong>.</p><ul><li>New item</li></ul>'},{'body':{'kind':'paragraph','opening':'<p class="lead">'}},{})
        self.assertTrue(result.startswith('<div class="cms-rich-text lead">'))
        self.assertTrue(result.endswith('</div>'))

    def test_text_is_escaped_and_link_queries_survive(self):
        result=build.render('{{title}} {{url}}',{'title':'A & B < C','url':'https://example.com/?a=1&b=2'},{'title':{'kind':'text'},'url':{'kind':'url'}},{})
        self.assertEqual(result,'A &amp; B &lt; C https://example.com/?a=1&amp;b=2')

    def test_unsafe_content_fails_before_publication(self):
        for value in ['<script>alert(1)</script>','<img src="x" onerror="alert(1)">','<a href="javascript:alert(1)">x</a>']:
            with self.assertRaises(ValueError):build.rich(value)

    def test_contact_email_updates_gmail_and_visible_address(self):
        result=build.render('{{email}} {{gmail}}',{'email':'old','gmail':'old'},{'email':{'kind':'text','site':'email'},'gmail':{'kind':'url','site':'gmail'}},{'email':'new@example.com'})
        self.assertIn('new@example.com',result)
        self.assertIn('to=new%40example.com',result)

if __name__=='__main__':unittest.main()
