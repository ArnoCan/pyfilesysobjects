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

from filesysobjects import W_RE, RTE, RTE_WIN32

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase311(self):

        if RTE & RTE_WIN32:
            arg = tdata + '/b/(.+?)//([cd][.]s.*|[cd][.]p.*|d)/d.*'
            resX = [
                # not matched, because 'expandpath' looks for the longest, else use 'findpattern'
                tdata + '/b/c/d/d.pm',
                tdata + '/b/c/d/d.smod',
                tdata + '/b/c/d/d.py',
                tdata + '/b/c/d/d.sh',
                tdata + '/b/c/d/d.pl',
                tdata + '/b/c/d/d.pod',
            ]
            from filesysobjects import V3K
            # import os
            if os.path.exists(tdata + '/b/c/d/d.pyc'):  # not V3K:
                resX.append(tdata + '/b/c/d/d.pyc')
        else:
            arg = tdata + '/b/(.+?)/([cd][.]s.*|[cd][.]p.*|d)/d.*'
            resX = [
                # not matched, because 'expandpath' looks for the longest, else use 'findpattern'
                tdata + '/b/c/d/d.pm',
                tdata + '/b/c/d/d.smod',
                tdata + '/b/c/d/d.py',
                tdata + '/b/c/d/d.sh',
                tdata + '/b/c/d/d.pl',
                tdata + '/b/c/d/d.pod',
            ]
            from filesysobjects import V3K
            # import os
            if os.path.exists(tdata + '/b/c/d/d.pyc'):  # not V3K:
                resX.append(tdata + '/b/c/d/d.pyc')


        arg = filesysobjects.apppaths.normapppathx(arg, tpf='posix')
        res = filesysobjects.pathtools.expandpath(arg, wildcards=W_RE, isFile=True, isDir=False)
        res = [filesysobjects.apppaths.normapppathx(x, tpf='posix') for x in res]

        # print("4TEST")
        # for r in res:
        #     print(r)

        self.assertEqual(sorted(res), sorted(resX))


#
#######################
#

if __name__ == '__main__':
    unittest.main()

