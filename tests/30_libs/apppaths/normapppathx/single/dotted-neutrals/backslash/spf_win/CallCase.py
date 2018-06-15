from __future__ import absolute_import
from linecache import getline

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os,platform
from filesysobjects import RTE, RTE_WIN32

import filesysobjects.apppaths
#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase110(self):
        arg = r'file:///.\\file_at_current_dir'  # needs to be exact

        if RTE & RTE_WIN32:
            resX = r'\file_at_current_dir'
        else:
            resX = r'/file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win')
        self.assertEqual(res, resX )

    def testCase120(self):
        arg = r'file:////\\\\\\.\\\\/file_at_current_dir'  # needs to be exact
        resX = r'file:///file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase121(self):
        arg = r'file://////////.\\\\/file_at_current_dir'  # needs to be exact
        resX = r'file:///file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase122(self):
        arg = r'file:////\\\\a\\\\..\\\/file_at_current_dir'  # needs to be exact
        resX = r'file:///file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase123(self):
        arg = r'file://////a///..///\\\\/file_at_current_dir'  # needs to be exact
        resX = r'file:///file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase124(self):
        arg = r'file://///a///..///\\\\/file_at_current_dir'  # needs to be exact
        resX = r'file:///file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase125(self):
        arg = r'file:////posixapp///..///\\\\/file_at_current_dir'  # needs to be exact
        resX = r'file:////posixapp/file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase150(self):
        arg = r'file:////\\\.\/file_at_current_dir/./a/b/./..//..'  # needs to be exact
        resX = r'file:///file_at_current_dir'

#         res0 = filesysobjects.paths.normpathx(arg, spf='posix', apppre=True)
#         res1 = filesysobjects.paths.normpathx(arg, spf='win', apppre=True)
#         res2 = filesysobjects.apppaths.normapppathx(arg, spf='posix', apppre=True)

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase160(self):
        arg = r'file:////\\\\\\.\\\\/file_at_current_dir//./a/b/./..///..'  # needs to be exact
        resX = r'file:///file_at_current_dir'

#         res0 = filesysobjects.paths.normpathx(arg, spf='posix', apppre=True)
#         res1 = filesysobjects.paths.normpathx(arg, spf='win', apppre=True)
#         res2 = filesysobjects.apppaths.normapppathx(arg, spf='posix', apppre=True)

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )



    def testCase200(self):
        arg = r'file:////.\\/file_at_current_dir'  # meets pattern for posix app
        resX = r'file:////file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase201(self):
        arg = r'file:////.///file_at_current_dir'  # meets pattern for posix app
        resX = r'file:////file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase202(self):
        arg = r'file:////a\\/file_at_current_dir'  # meets pattern for posix app
        resX = r'file:////a/file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )

    def testCase203(self):
        arg = r'file:////a///file_at_current_dir'  # needs to be exact
        resX = r'file:////a/file_at_current_dir'

        res = filesysobjects.apppaths.normapppathx(arg, spf='win', apppre=True)
        self.assertEqual(res, resX )


#
#######################
#

if __name__ == '__main__':
    unittest.main()

