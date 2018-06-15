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

import filesysobjects.pprint
# import pysourceinfo.helper


class CallUnits(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None
    
    def testCase010(self):
        raw  = "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/ffffffffff/gggggggggg/hhhhhhhhhh/iiiiiiiiii/jjjjjjjjjj/kkkkkkkkkk/llllllllll/mmmmmmmmmm/nnnnnnnnnn/oooooooooo/pppppppppp/qqqqqqqqq/rrrrrrrrrr/ssssssssss/tttttttttt/uuuuuuuuuu/vvvvvvvvvv/wwwwwwwwww/xxxxxxxxxx/yyyyyyyyyy/zzzzzzzzzz"
        raw += os.pathsep
        raw += "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/ffffffffff/gggggggggg/hhhhhhhhhh/iiiiiiiiii" 
        raw += os.pathsep
        raw += "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc" 
        raw += os.pathsep
        raw += "/aaaaaaaaaa/bbbbbbbbbb" 
        raw += os.pathsep
        raw += "/aaaaaaaaaa" 
        raw += os.pathsep
        raw += "/0000000000/1111111111/2222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999"
        raw += os.pathsep
        raw += "/0000000000/1111111111/2222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999"
        raw += os.pathsep
        raw += "/aaaaaaaaaa/bbbbbbbbbb" 
        raw += os.pathsep
        raw += "/0000000000/1111111111/2222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999"
        res = str(
            filesysobjects.pprint.PPPathVar(
                raw,
                overflow='clipmerge',
                keepentry=False,
                offset=4,
                offsetchar='.',
                indentchar='*',
                indentclipchar='x',
                )
            )
        
        # print("4TEST:<\n" + str(res) + ">")
        
        resx = '''....PATH = "/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/ffffffffff/"
....****"gggggggggg/hhhhhhhhhh/iiiiiiiiii/jjjjjjjjjj/kkkkkkkkkk/llllllllll/mmmm"
....****"mmmmmm/nnnnnnnnnn/oooooooooo/pppppppppp/qqqqqqqqq/rrrrrrrrrr/sssssssss"
....****"s/tttttttttt/uuuuuuuuuu/vvvvvvvvvv/wwwwwwwwww/xxxxxxxxxx/yyyyyyyyyy/zz"
....****"zzzzzzzz:/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/fffff"
....****"fffff/gggggggggg/hhhhhhhhhh/iiiiiiiiii:/aaaaaaaaaa/bbbbbbbbbb/cccccccc"
....****"cc:/aaaaaaaaaa/bbbbbbbbbb:/aaaaaaaaaa:/0000000000/1111111111/222222222"
....****"2/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/99"
....****"99999999:/0000000000/1111111111/2222222222/3333333333/4444444444/55555"
....****"55555/6666666666/7777777777/8888888888/9999999999:/aaaaaaaaaa/bbbbbbbb"
....****"bb:/0000000000/1111111111/2222222222/3333333333/4444444444/5555555555/"
....****"6666666666/7777777777/8888888888/9999999999"
'''

        self.assertEqual(res, resx)
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

