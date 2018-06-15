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

from filesysobjects.paths import normpathx
from filesysobjects.pathtools import findpattern
from filesysobjects import T_ALL, T_DIR, RTE, RTE_WIN32

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
#
#######################
#

class UseCase(unittest.TestCase):

    def testCase010(self):
        self.maxDiff = None

        arg = tdata + os.path.sep + 'b' + os.path.sep + 'c' + os.path.sep
        arg_cut = tdata + os.path.sep

        if RTE & RTE_WIN32:
            retX = [
                'b\\c\\c.pl',
                'b\\c\\c.pm',
                'b\\c\\c.pod',
                'b\\c\\d\\d.pl',
                'b\\c\\d\\d.pm',
                'b\\c\\d\\d.pod'
            ]
        else:
            retX = [
                'b/c/c.pl',
                'b/c/c.pm',
                'b/c/c.pod',
                'b/c/d/d.pl',
                'b/c/d/d.pm',
                'b/c/d/d.pod',
            ]
        retX = sorted(retX)
        #retX = [normpathx(x) for x in retX]

        ret = findpattern(
            arg,
            topcutlist=[arg_cut],
            types=T_ALL^T_DIR,
            whitelist='.*[.](pl|pm|pod)'
            )
        ret = sorted(ret)

#         print('4TEST:')
#         for i in ret:
#             print("            '" + str(i) + "',")

        # print('4TEST:' + str(ret))
        # print('4TEST:' + str(retX))

        self.assertEqual(ret, retX)


#
#######################
#
if __name__ == '__main__':
    unittest.main()

