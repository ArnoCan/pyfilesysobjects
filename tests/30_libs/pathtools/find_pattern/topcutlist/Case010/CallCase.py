"""Check default values, and with defaults as passed parameters.
"""
from __future__ import absolute_import
from __future__ import print_function

_author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.4'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import filesysobjects.apppaths
import testdata.filesysobjects

from filesysobjects.pathtools import findpattern
from filesysobjects.paths import normpathx

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normpathx(tdata)

#
#######################
#

class UseCase(unittest.TestCase):

    def testCase010(self):
        self.maxDiff = None

        arg = tdata + os.path.sep + 'b' + os.path.sep + 'c' + os.path.sep
        arg_cut = tdata + os.path.sep

        retX = [
            'b/c/...c3.txt',
            'b/c/..c2.txt',
            'b/c/.c.txt',
            'b/c/C.txt',
            'b/c/c.pl',
            'b/c/c.pm',
            'b/c/c.pod',
            'b/c/c.py',
            'b/c/c.sh',
            'b/c/c.smod',
            'b/c/d',
            'b/c/d/.d.txt',
            'b/c/d/D.txt',
            'b/c/d/d.pl',
            'b/c/d/d.pm',
            'b/c/d/d.pod',
            'b/c/d/d.py',
            'b/c/d/d.sh',
            'b/c/d/d.smod',
        ]

        retX = sorted(retX)
        retX = [normpathx(x) for x in retX]

        ret = findpattern(
            arg,
            topcutlist=[arg_cut],
            blacklist='.*/__init__.py|.*__pycache__.*|.*[.]pyc'
            )
        ret = sorted(ret)

#         print('4TEST:')
#         for i in ret:
#             print("            '" + str(i) + "',")

        self.assertEqual(ret, retX)


#
#######################
#
if __name__ == '__main__':
    unittest.main()

