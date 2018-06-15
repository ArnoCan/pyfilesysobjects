from __future__ import absolute_import
from __future__ import print_function
from linecache import getline

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

from filesysobjects.apppaths import normapppathx
import filesysobjects.pprint

#
#######################
#


class CallUnits(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase000(self):
        raw = "/path0" + os.pathsep + "/path1" + os.pathsep + "/path2"
        res = str(filesysobjects.pprint.PPPathVar(raw))
        resx = """PATH = [
    "/path0",
    "/path1",
    "/path2"
]
"""
        resx = normapppathx(res)

#         print("4TEST:" + str(res))

        self.assertEqual(res, resx)
        pass

if __name__ == '__main__':
    unittest.main()

