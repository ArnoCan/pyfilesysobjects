from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

#
#######################
#

import filesysobjects.paths
import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """
    def testCase000(self):
        self.maxDiff = None

        arg = '\b[\[]'
        argEscX = '\\b[\[]'
        resX = '\b[\[]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase490(self):
        self.maxDiff = None

        arg = 'a\b[\[]'
        argEscX = 'a\\b[\[]'
        resX = 'a\b[\[]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase500(self):
        self.maxDiff = None

        arg = 'a[\[]'
        argEscX = 'a[\[]'
        resX = 'a[\[]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

