from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

import filesysobjects.paths

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        arg = r'/my/odd/searchpath/"""[\\/xyz].*"""/myfile.z'
        resx = '/my/odd/searchpath/"""[\\\\/xyz].*"""/myfile.z'

        res = filesysobjects.paths.escapepathx(arg, tpf='posix')

        self.assertEqual(res, resx)

    def testCase010(self):
        arg = '\my\odd\searchpath\a\b\n\r\t"""[\\/xyz].*"""\myfile.z'
        resx = '\my\odd\searchpath\\a\\b\\n\\r\\t"""[\\/xyz].*"""\myfile.z'

        res = filesysobjects.paths.escapepathx(arg, tpf='posix')

        self.assertEqual(res, resx)

    def testCase020(self):
        arg = '\my\odd\searchpath\a\b\n\r\t"""[\\/xyz].*"""\myfile.z'
        resx = '\\\\my\\\\odd\\\\searchpath\\a\\b\\n\\r\\t"""[\\/xyz].*"""\\\\myfile.z'

        res = filesysobjects.paths.escapepathx(
            arg, tpf='posix',
            force=True
            )

        self.assertEqual(res, resx)

    def testCase030(self):
        arg = r'\my\odd\searchpath\a\b\n\r\t"""[\/xyz].*"""\myfile.z'
        resx = r'\\my\\odd\\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\\myfile.z'

        res = filesysobjects.paths.escapepathx(
            arg, tpf='posix',
            force=True
            )

        self.assertEqual(res, resx)

if __name__ == '__main__':
    unittest.main()

