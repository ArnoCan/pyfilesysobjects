"""Check default values, and with defaults as passed parameters.
"""
from __future__ import absolute_import
from __future__ import print_function

_author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.6'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import testdata.filesysobjects

from filesysobjects.pathtools import findpattern
from filesysobjects.paths import normpathx

#
#######################
#

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = normpathx(tdata, tpf='posix')

class UseCase(unittest.TestCase):

    def testCase012_confirm_basics(self):
        kargs = {}
        kargs['whitelist'] = [
            tdata + normpathx('/"""[^/]+"""/.*/[c]+.sh'),
            tdata + normpathx('/"""[^\a]+"""/.*/[c]+.sh'),
        ]

        retX = [
            tdata + normpathx('/b/c/c.sh'),
            tdata + normpathx('/b2/c/c.sh'),
            tdata + normpathx('/b0/c/c.sh'),
        ]
        retX = [normpathx(x) for x in retX]

        ret = findpattern(tdata,**kargs)

        ret = sorted(ret)
        retX.sort()

        self.maxDiff = None
        self.assertEqual(sorted(ret), sorted(retX))
        pass


if __name__ == '__main__':
    unittest.main()

