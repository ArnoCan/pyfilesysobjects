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

from filesysobjects.pathtools import findpattern
from filesysobjects.pathtools import L_TDOWN_WALK,M_ALL,M_FILTPAR,T_ALL

#
#######################
#

class UseCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        unittest.TestCase.setUp(self)
        self.curd = os.getcwd()
        os.chdir(os.path.abspath(os.path.dirname(__file__)))

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        os.chdir(self.curd)
        
    def testCase000(self):
        ret = findpattern(level=0, topcutlist=[os.getcwd() + os.sep])
        resx = os.listdir('.')
        self.assertEqual(sorted(ret), sorted(resx))
        pass

    def testCase010(self):
        ret = findpattern(topcutlist=[os.getcwd() + os.sep])
        resx = []
        for a,b,c in os.walk('.'):
            if a and b:
                resx.extend([a + os.sep + x for x in b])
            if a and c:
                resx.extend([a + os.sep + x for x in c])

        for r in resx:
            if r[:2] == '.' + os.sep:
                resx[resx.index(r)] = r[2:]

        
        self.assertEqual(sorted(ret), sorted(resx))
        pass

#
#######################
#
if __name__ == '__main__':
    unittest.main()

