from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

#
#######################
#

import filesysobjects.apppaths

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        arg = '/my/odd/searchpath/"""[/xyz].*"""/myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='posix',     # source platform POSIX, default is local platform
            tpf='fileuri',   # target platform FILEURI, default is local platform
            strip=True,      # strip null-entries
            )
 

        resx = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

        
        self.assertEqual(res, resx)

    def testCase001(self):
        arg = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=False,     # activate application prefix
            spf='fileuri',   # target platform FILEURI, default is local platform
            tpf='posix',     # source platform POSIX, default is local platform
            strip=True,      # strip null-entries
            )
 
        resx = '/my/odd/searchpath/"""[/xyz].*"""/myfile.z'

        self.assertEqual(res, resx)

    def testCase010(self):
        arg = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='win',       # source platform Windows, default is local platform
            tpf='fileuri',   # target platform FILEURI, default is local platform
            strip=True,      # strip null-entries
            )
 
        resx = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'
        
        self.assertEqual(res, resx)

    def testCase011(self):
        arg = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=False,    # activate application prefix
            spf='fileuri',   # target platform FILEURI, default is local platform
            tpf='win',       # source platform Windows, default is local platform
            strip=True,      # strip null-entries
            )
 
        resx = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

        self.assertEqual(res, resx)

    def testCase020(self):
        arg = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='win',       # source platform Windows, default is local platform
            tpf='http',      # target platform FILEURI, default is local platform
            strip=True,      # strip null-entries
            )
 
        resx = 'http:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'
        
        self.assertEqual(res, resx)

    def testCase021(self):
        arg = 'http:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=False,    # activate application prefix
            spf='http',      # target platform FILEURI, default is local platform
            tpf='win',       # source platform Windows, default is local platform
            strip=True,      # strip null-entries
            )
 
        resx = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

        self.assertEqual(res, resx)

    def testCase030(self):
        arg = r'\\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='win',       # source platform Windows, default is local platform
            tpf='posix',     # target platform FILEURI, default is local platform
            strip=True,      # strip null-entries
            )
 
        resx = 'file://my/odd/searchpath/"""[/xyz].*"""/myfile.z'
        
        self.assertEqual(res, resx)

    def testCase031(self):
        arg = '//my/odd/searchpath/"""[/xyz].*"""/myfile.z'

        res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=False,    # activate application prefix
            spf='posix',     # target platform FILEURI, default is local platform
            tpf='win',       # source platform Windows, default is local platform
            strip=True,      # strip null-entries
            )
 
        resx = r'\\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()

