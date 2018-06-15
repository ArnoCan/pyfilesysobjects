from __future__ import absolute_import
from filesysobjects import W_LITERAL

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

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase010(self):
        
        arg = tdata + '/b/c/c.py'
        resX = arg

        resX = filesysobjects.apppaths.splitapppathx(resX)
        arg = filesysobjects.apppaths.normapppathx(arg)

        res = filesysobjects.pathtools.expandpath(arg, wildcards=W_LITERAL)
        self.assertEqual(res, resX)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

