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

#
#######################
#

class UseCase(unittest.TestCase):

    def testCase010(self):
        self.maxDiff = None

        arg = [
            tdata + os.path.sep + 'b' + os.path.sep + 'c' + os.path.sep,
            tdata + os.path.sep + 'b0' + os.path.sep + 'c' + os.path.sep,
            tdata + os.path.sep + 'b1' + os.path.sep + 'c' + os.path.sep,
        ]
        arg_cut = [
            tdata + os.path.sep
        ]

        retX = [
            r'b0\c\C.txt',
            r'b0\c\c.pl',
            r'b0\c\c.pod',
            r'b0\c\c.py',
            r'b0\c\c.smod',
            r'b0\c\d',
            r'b0\c\d\D.txt',
            r'b0\c\d\d.pl',
            r'b0\c\d\d.pod',
            r'b0\c\d\d.py',
            r'b0\c\d\d.smod',
            r'b\c\...c3.txt',
            r'b\c\..c2.txt',
            r'b\c\.c.txt',
            r'b\c\C.txt',
            r'b\c\c.pl',
            r'b\c\c.pod',
            r'b\c\c.py',
            r'b\c\c.smod',
            r'b\c\d',
            r'b\c\d\.d.txt',
            r'b\c\d\D.txt',
            r'b\c\d\d.pl',
            r'b\c\d\d.pod',
            r'b\c\d\d.py',
            r'b\c\d\d.smod',
        ]

        retX = [normpathx(x) for x in retX]
        retX = sorted(retX)

        ret = findpattern(
            *arg,
            topcutlist=arg_cut,
            blacklist=['.*__pycache__.*', '.*.pyc', '.*__init__.py', '.*[.]sh', '.*[.]pm']
            )
        ret = sorted(ret)

#         print('4TEST:')
#         for i in ret:
#             print("            r'" + str(i) + "',")


        self.assertEqual(sorted(ret), sorted(retX))


#
#######################
#
if __name__ == '__main__':
    unittest.main()

