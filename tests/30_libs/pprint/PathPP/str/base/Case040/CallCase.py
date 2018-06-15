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

import filesysobjects.pprint

#
#######################
#


class CallUnits(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        raw  = (
            "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/ffffffffff/gggggggggg/hhhhhhhhh/iiiiiiiiii",
            "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc",
            "/aaaaaaaaaa/bbbbbbbbbb",
            "/aaaaaaaaaa",
            "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999",
            "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999",
            "/aaaaaaaaaa/bbbbbbbbbb" ,
            "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999",
        )
        res = str(filesysobjects.pprint.PPPathVar(raw, linesep='\n'))


        resx = """PATH = [
    "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/ffffffffff/gggggggggg/hhhhhhhhh/iiiiiiiiii",
    "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc",
    "/aaaaaaaaaa/bbbbbbbbbb",
    "/aaaaaaaaaa",
    "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999",
    "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999",
    "/aaaaaaaaaa/bbbbbbbbbb",
    "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999"
]
"""

        #
#         print("4TEST:" + str(res))

        self.assertEqual(res, resx)
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

