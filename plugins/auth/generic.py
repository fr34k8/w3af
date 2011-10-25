'''
generic.py

Copyright 2011 Andres Riancho

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
from urllib import urlencode

from core.data.options.option import option
from core.data.options.optionList import optionList
from core.controllers.basePlugin.baseAuthPlugin import baseAuthPlugin
from core.controllers.w3afException import w3afException

class generic(baseAuthPlugin):
    '''Generic auth plugin.'''

    def __init__(self):
        baseAuthPlugin.__init__(self)
        self.username = None
        self.password = None
        self.username_field = None
        self.password_field = None
        self.auth_url = None
        self.check_url = None
        
    def login(self):
        '''User login.'''
        try:
            # TODO Why we don't use httpPostDataRequest here?
            self._urlOpener.POST(self.auth_url, urlencode({
                self.username_field: self.username,
                self.password_field: self.password,
            }))
            return self.is_logged()
        except Exception, e:
            return False

    def logout(self):
        '''User login.'''
        return None

    def is_logged(self):
        '''Check user session.'''
        try:
            body = self._urlOpener.GET(self.check_url).body
            return self.username in body
        except Exception:
            return False
   
    def getOptions(self):
        '''
        @return: A list of option objects for this plugin.
        '''

        d1 = 'Username'
        o1 = option('username', self.username, d1, 'string')
        
        d2 = 'Password'
        o2 = option('password', self.password, d2, 'string')
 
        d3 = 'Username field'
        o3 = option('username_field', self.username_field, d3, 'string')
        
        d4 = 'Password field'
        o4 = option('password_field', self.password_field, d4, 'string')
               
        d5 = 'Auth URL - URL for POSTing auth information'
        o5 = option('auth_url', self.auth_url, d5, 'url')

        d6 = 'Check session URL - URL in which response body username will be searched'
        o6 = option('check_url', self.check_url, d6, 'url')

        ol = optionList()
        ol.add(o1)
        ol.add(o2)
        ol.add(o3)
        ol.add(o4)
        ol.add(o5)
        ol.add(o6)
        return ol

    def setOptions(self, optionsMap):
        '''
        This method sets all the options that are configured using 
        the user interface generated by the framework using 
        the result of getOptions().
        
        @parameter optionsMap: A dict with the options for the plugin.
        @return: No value is returned.
        ''' 
        self.username = optionsMap['username'].getValue()
        self.password = optionsMap['password'].getValue()
        self.username_field = optionsMap['username_field'].getValue()
        self.password_field = optionsMap['password_field'].getValue()
        self.auth_url = optionsMap['auth_url'].getValue()
        self.check_url = optionsMap['check_url'].getValue()

    def getPluginDeps(self):
        '''
        @return: A list with the names of the plugins that should be runned 
        before the current one.
        '''
        return []

    def getLongDesc(self):
        '''
        @return: A DETAILED description of the plugin functions and features.
        '''
        return '''
        This auth plugin can logging in to generic-passport
        
        Three configurable parameters exist:
            - username
            - password
            - username_field
            - password_field
            - auth_url
            - check_url
        '''


