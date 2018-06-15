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

    def testCase010(self):
        self.maxDiff = None

        arg = '[\[]'
        argEscX = '[\[]'
        resX = '[\[]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase020(self):
        self.maxDiff = None

        arg = '[\a\[]'
        argEscX = '[\a\[]'
        resX = '[\a\[]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase030(self):
        self.maxDiff = None

        arg = '\a[\a\[]'
        argEscX = '\\a[\a\[]'
        resX = '\a[\a\[]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase040(self):
        self.maxDiff = None

        arg = '[\n\r\t\[\]]'
        argEscX = '[\n\r\t\[\]]'
        resX = '[\n\r\t\[\]]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase050(self):
        self.maxDiff = None

        arg = 'Z:[\n\r\t\[\]]'
        argEscX = 'Z:[\n\r\t\[\]]'
        resX = 'Z:[\n\r\t\[\]]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase060(self):
        self.maxDiff = None

        arg = '\b[\[]'
        argEscX = '\\b[\[]'
        resX = '\b[\[]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase070(self):
        self.maxDiff = None

        arg = '\b[\n\r\t\[\]]'
        argEscX = '\\b[\n\r\t\[\]]'
        resX = '\b[\n\r\t\[\]]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)


    def testCase080(self):
        self.maxDiff = None

        arg = '\a\b[\n\r\t\[\]]'
        argEscX = '\\a\\b[\n\r\t\[\]]'
        resX = '\a\b[\n\r\t\[\]]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)

    def testCase100(self):
        self.maxDiff = None

        arg = 'Z:\a\b[\n\r\t\[\]]'
        argEscX = 'Z:\\a\\b[\n\r\t\[\]]'
        resX = 'Z:\a\b[\n\r\t\[\]]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

        self.assertEqual(argEsc, argEscX)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

