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
        raw += "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999"
        raw += os.pathsep
        raw += "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999"
        raw += os.pathsep
        raw += "/aaaaaaaaaa/bbbbbbbbbb"
        raw += os.pathsep
        raw += "/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999"

        raw = normapppathx(raw)
        res = str(
            filesysobjects.pprint.PPPathVar(
                raw,
                format='xml',
                )
            )


        resx = '''<PATH>
    <entry idx=0>/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/ffffffffff/gggggggggg/hhhhhhhhhh/iiiiiiiiii/jjjjjjjjjj/kkkkkkkkkk/llllllllll/mmmmmmmmmm/nnnnnnnnnn/oooooooooo/pppppppppp/qqqqqqqqq/rrrrrrrrrr/ssssssssss/tttttttttt/uuuuuuuuuu/vvvvvvvvvv/wwwwwwwwww/xxxxxxxxxx/yyyyyyyyyy/zzzzzzzzzz</entry>
    <entry idx=1>/aaaaaaaaaa/bbbbbbbbbb/cccccccccc/dddddddddd/eeeeeeeeee/ffffffffff/gggggggggg/hhhhhhhhhh/iiiiiiiiii</entry>
    <entry idx=2>/aaaaaaaaaa/bbbbbbbbbb/cccccccccc</entry>
    <entry idx=3>/aaaaaaaaaa/bbbbbbbbbb</entry>
    <entry idx=4>/aaaaaaaaaa</entry>
    <entry idx=5>/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999</entry>
    <entry idx=6>/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999</entry>
    <entry idx=7>/aaaaaaaaaa/bbbbbbbbbb</entry>
    <entry idx=8>/00000000000/1111111111/22222222222/3333333333/4444444444/5555555555/6666666666/7777777777/8888888888/9999999999</entry>
</PATH>
'''

        #
#         print("4TEST:<\n" + str(res) + ">")
#         print("4TEST:<" + str(resx) + ">")

        self.assertEqual(res, resx)
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

