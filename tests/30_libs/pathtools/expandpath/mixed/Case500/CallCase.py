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

from filesysobjects.pathtools import W_RE

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase010(self):
        self.maxDiff = None


        resX = [
            tdata + '/b/c/c.pl',
            tdata + '/b/c/c.pm',
            tdata + '/b/c/c.pod',
            tdata + '/b/c/c.py',
        ]

        from filesysobjects import V3K
        # import os
        if os.path.exists(tdata + '/b/c/c.pyc'):  # not V3K:
            resX.append(tdata + '/b/c/c.pyc')


        arg = os.path.dirname(tdata) + '/*/[!ac]/[^abd-z]/[cd][^"""\\\\"""]*[.][p][^"""\\\\"""]*'

        resX = sorted(resX)

        arg = filesysobjects.apppaths.normapppathx(arg)

        res = filesysobjects.pathtools.expandpath(arg, wildcards=W_RE)
        res = sorted(res)

        # print('4TEST:')
        # for i in res:
        #     print(i)

        res = [filesysobjects.apppaths.normapppathx(x) for x in res]
        resX = [filesysobjects.apppaths.normapppathx(x) for x in resX]
        self.assertEqual(sorted(res), sorted(resX))

#
#######################
#

if __name__ == '__main__':
    unittest.main()

