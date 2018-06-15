"""Local globs + regexpr.
"""
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

import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects

from filesysobjects import W_RE
from filesysobjects.pathtools import glob_to_re

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    
    def testCase010(self):
        res  = glob_to_re("\\a\\b[!123]*")
        resx = "\\a\\b[^123].*"
        self.assertEqual(res, resx)
    
    def testCase020(self):
        res  = glob_to_re("x.y")
        resx = "x[.]y"
        self.assertEqual(res, resx)
    
    def testCase030(self):
        res  = glob_to_re("\\a\\b[!123]*\\x.y\\")
        resx = "\\a\\b[^123].*\\x[.]y\\"
        self.assertEqual(res, resx)
    
    def testCase040(self):
        res  = glob_to_re("\\a\\b[!123]*\\?\\x.y\\")
        resx = "\\a\\b[^123].*\\.\\x[.]y\\"
        self.assertEqual(res, resx)

        
if __name__ == '__main__':
    unittest.main()

