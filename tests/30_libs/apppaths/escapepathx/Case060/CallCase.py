from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

#
#######################
#

import filesysobjects.paths
import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase020(self):
        self.maxDiff = None

        arg = 'Z:\a\b[\n\r\t\[\]]'
        argEscX = 'Z:\\a\\b[\n\r\t\[\]]'
        resX = 'Z:\a\b[\n\r\t\[\]]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

#         resXHex  = ' '.join(hex(ord(x)) for x in resX)
#         resXChar = '    '.join(x for x in resX)
#         resHex   = ' '.join(hex(ord(x)) for x in res)
#         resChar  = '    '.join(x for x in res)
#
#         print("4TEST:arg     = " + str(arg))
#         print("4TEST:argEsc  = " + str(argEsc))
#         print("4TEST:resX    = " + str(resX))
#         print("4TEST:res     = " + str(res))
#         print()
#         print("4TEST:resHex  = " + str(resXHex))
#         print("4TEST:resChar = " + str(resXChar))
#         print("4TEST:resHex  = " + str(resHex))
#         print("4TEST:resChar = " + str(resChar))

        self.assertEqual(argEsc, argEscX)
#        self.assertEqual(resHex, resXHex)
        self.assertEqual(res, resX)

    def testCase030(self):
        self.maxDiff = None

        arg = 'Z:\a\b[\[\n\r\t\]]'
        argEscX = 'Z:\\a\\b[\[\n\r\t\]]'
        resX = 'Z:\a\b[\[\n\r\t\]]'
        
        argEsc = filesysobjects.paths.escapepathx(arg)
        res = filesysobjects.paths.unescapepathx(argEsc)

#         resXHex  = ' '.join(hex(ord(x)) for x in resX)
#         resXChar = '    '.join(x for x in resX)
#         resHex   = ' '.join(hex(ord(x)) for x in res)
#         resChar  = '    '.join(x for x in res)
#
#         print("4TEST:arg     = " + str(arg))
#         print("4TEST:argEsc  = " + str(argEsc))
#         print("4TEST:resX    = " + str(resX))
#         print("4TEST:res     = " + str(res))
#         print()
#         print("4TEST:resHex  = " + str(resXHex))
#         print("4TEST:resChar = " + str(resXChar))
#         print("4TEST:resHex  = " + str(resHex))
#         print("4TEST:resChar = " + str(resChar))

        self.assertEqual(argEsc, argEscX)
#        self.assertEqual(resHex, resXHex)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

