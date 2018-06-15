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
from filesysobjects import T_ALL, T_DIR
#
#######################
#

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = normpathx(tdata, tpf='posix')

class UseCase(unittest.TestCase):

    def testCase090(self):
        self.maxDiff = None

        kargs = {}
        kargs['whitelist'] = [
            tdata + normpathx('/.+/c/c.sh'),
            tdata + normpathx('//[a].smod'),
            tdata + normpathx('/.+/smods/a.smod'),
            tdata + normpathx('/b3/sm[o]ds/.+/a.smod'),
            tdata + normpathx('/b3/s[m]ods/.+/.+/a.smod'),
            tdata + normpathx('/b3//[smo]*[smo]+[smo]+ds/.+/.+/.+/a.smod'),
            tdata + normpathx('/b3//[smo]*.[smo]ds/.+/.+/.+/.+/a.smod'),
        ]

        kargs['types'] = T_ALL ^ T_DIR

        retX = [
            tdata + normpathx('/b/c/c.sh'),
            tdata + normpathx('/b2/c/c.sh'),
            tdata + normpathx('/b0/c/c.sh'),

            tdata + normpathx('/a.smod'),
            tdata + normpathx('/b3/smods/a.smod'),
            tdata + normpathx('/b3/smods/b/c/a.smod'),
            tdata + normpathx('/b3/smods/c/c/a.smod'),
            tdata + normpathx('/b3/smods/c/c/d/a.smod'),
            tdata + normpathx('/b3/smods/c/c/d/e/a.smod'),
            tdata + normpathx('/b3/smods/c/d/a.smod'),
            tdata + normpathx('/b3/smods/a/a.smod'),
            tdata + normpathx('/b3/smods/a/c/a.smod'),
        ]
        retX = [normpathx(x) for x in retX]

        ret = findpattern(normpathx(tdata, spf='posix'),**kargs)

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None

#         print('4TEST:')
#         for i in ret:
#             print("            '" + str(i) + "',")

        self.assertEqual(ret, retX)
        pass


if __name__ == '__main__':
    unittest.main()

