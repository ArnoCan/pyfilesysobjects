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

from filesysobjects import W_LITERAL_QUOTED

import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects
from filesysobjects.apppaths import normapppathx

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):

        resX = tdata + '/b/c/c.py'  + os.pathsep \
            + tdata + '/b/c/c.pl'  + os.pathsep \
            + tdata + '/b/c/c.pm'

        resX = normapppathx(resX)

        arg = tdata + '/b/"""c"""/c.py'  + os.pathsep \
            + tdata + '/b/c/c.pl'  + os.pathsep \
            + tdata + '/b/c/c.pm'

        res = filesysobjects.pathtools.expandpath(arg, wildcards=W_LITERAL_QUOTED)
        self.assertEqual(os.pathsep.join(res), resX)

    def testCase020(self):

        resX = tdata + '/b/c/c.py'  + os.pathsep \
            + tdata + '/b/c/c.pl'  + os.pathsep \
            + tdata + '/b/c/c.pm'
        resX = normapppathx(resX)

        arg = [
            tdata + '/b/"""c"""/c.py',
            tdata + '/b/c/c.pl',
            tdata + '/b/c/c.pm'
        ]

        res = filesysobjects.pathtools.expandpath(*arg, wildcards=W_LITERAL_QUOTED)
        self.assertEqual(os.pathsep.join(res), resX)

if __name__ == '__main__':
    unittest.main()

