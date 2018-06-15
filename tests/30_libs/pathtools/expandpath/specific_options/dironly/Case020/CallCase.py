from __future__ import absolute_import
import filesysobjects

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

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normpathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        resX = [
            tdata + '/b2/c',
            tdata + '/b2/c0',
            tdata + '/b2/c1'
        ]
        arg = tdata + '/b2/c;' + tdata + '/b2/c0;' + tdata + '/b2/c1/'
        resX = [filesysobjects.apppaths.normapppathx(x, tpf='posix') for x in resX]
        arg = filesysobjects.apppaths.normapppathx(arg, tpf='win', spf='win')

        res = filesysobjects.pathtools.expandpath(arg, dironly=True, wildcards=W_RE, spf='win', tpf='posix')
        self.assertEqual(res, resX)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

