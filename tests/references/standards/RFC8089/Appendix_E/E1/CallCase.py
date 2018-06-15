""" [RFC8089]_ - Appendix E.1. User Information

.. seealso:


   It might be necessary to include user information such as a user name
   in a file URI, for example, when mapping a VMS file path with a node
   reference that includes an access control string.

   To allow user information to be included in a file URI, the "file-
   auth" rule in Section 2 can be replaced with the following: ::

      file-auth   = "localhost"
                  / [ userinfo "@" ] host

   This uses the "userinfo" rule from [RFC3986].

   As discussed in the HP OpenVMS Systems Documentation
   <http://h71000.www7.hp.com/doc/84final/ba554_90015/ch03s09.html>,
   "access control strings include sufficient information to allow
   someone to break in to the remote account, [therefore] they create
   serious security exposure." In a similar vein, the presence of a
   password in a "user:password" userinfo field is deprecated by
   [RFC3986]. Take care when dealing with information that can be used
   to identify a user or grant access to a system.

"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

from filesysobjects import RTE, RTE_WIN32
import filesysobjects.apppaths

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase010(self):

        arg = "http://user:password@hostname/path/to/file?query#fragment"
        resX = "http://user:password@hostname/path/to/file?query#fragment"
        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase011(self):

        arg = "http://user:password@hostname/path/to/file?query#fragment"
        resX = [('http', 'user:password@hostname', '', '/path/to/file', '?query#fragment')]

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=True, apppre=True)
        self.assertEqual(res, resX)

    def testCase020(self):

        arg = "http://localhost/path/to/file?query#fragment"
        resX = "http://localhost/path/to/file?query#fragment"
        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase021(self):
        arg = "http://localhost/path/to/file?query#fragment"
        resX = [('http', 'localhost', '', '/path/to/file', '?query#fragment')]
        res = filesysobjects.apppaths.normapppathx(arg, appsplit=True, apppre=True)
        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

