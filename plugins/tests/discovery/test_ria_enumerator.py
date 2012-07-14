'''
test_ria_enumerator.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

from ..helper import PluginTest, PluginConfig

class TestRIAEnumerator(PluginTest):
    
    base_url = 'http://moth/'
    
    _run_config = {
            'target': base_url,
            'plugins': {'discovery': (PluginConfig('ria_enumerator'),)}
        }
    
    def test_ria_enumerator(self):
        self._scan( self._run_config['target'], self._run_config['plugins'] )
        
        infos = self.kb.getData('ria_enumerator', 'info')
        self.assertEqual( len(infos) , 2)
        
        urls = [i.getURL().url_string for i in infos]
        self.assertTrue( self.base_url + 'crossdomain.xml' in urls )
        
        vulns = self.kb.getData('ria_enumerator', 'vuln')
        self.assertEqual( len(vulns) , 1)

