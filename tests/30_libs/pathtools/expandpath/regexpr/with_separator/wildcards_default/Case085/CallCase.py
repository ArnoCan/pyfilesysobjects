from __future__ import absolute_import

import unittest
import os
import re

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"


#
#######################
#

import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'


class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase100(self):

        resX = tdata + '/b/c/c.pod' + os.pathsep \
            + tdata + '/b/c/c.py'  + os.pathsep \
            + tdata + '/b/c/c.pl'  + os.pathsep \
            + tdata + '/b/c/c.pm'

        from filesysobjects import V3K
        # import os
        if os.path.exists(tdata + '/b/c/c.pyc'):  # not V3K:
            resX += os.pathsep + tdata + '/b/c/c.pyc'

        resX = filesysobjects.apppaths.splitapppathx(resX)

        arg = tdata + '\\b\\\\"""[^\\\\]*\\"""[c][.][p][^"""\\\\"""]*'
        arg = filesysobjects.pathtools.stripquotes(arg)

        res = filesysobjects.pathtools.expandpath(arg, stripquotes=True)
        self.assertEqual(sorted(res), sorted(resX))


if __name__ == '__main__':
    unittest.main()

