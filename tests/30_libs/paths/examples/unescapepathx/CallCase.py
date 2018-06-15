from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

import filesysobjects.paths

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        arg = '/my/odd/searchpath/"""[\\\\/xyz].*"""/myfile.z'
        resx = r'/my/odd/searchpath/"""[\\/xyz].*"""/myfile.z'

        res = filesysobjects.paths.unescapepathx(arg, tpf='posix')

        self.assertEqual(res, resx)

    def testCase010(self):
        arg = '\my\odd\searchpath\\a\\b\\n\\r\\t"""[\\/xyz].*"""\myfile.z'
        resx = '\my\odd\searchpath\a\b\n\r\t"""[\\/xyz].*"""\myfile.z'

        res = filesysobjects.paths.unescapepathx(arg, tpf='posix')

        self.assertEqual(res, resx)

    def testCase020(self):
        arg = '\\\\my\\\\odd\\\\searchpath\\a\\b\\n\\r\\t"""[\\/xyz].*"""\\\\myfile.z'
        resx = '\my\odd\searchpath\a\b\n\r\t"""[\\/xyz].*"""\myfile.z'

        res = filesysobjects.paths.unescapepathx(
            arg, tpf='posix',
            force=True
            )

        self.assertEqual(res, resx)

    def testCase030(self):
        arg = r'\\my\\odd\\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\\myfile.z'
#        resx = '\\\\my\\\\odd\\\\searchpath\\' + '\a\\' + '\b\\' + '\n\\' + '\r\\' + '\t"""[\/xyz].*"""\\\\myfile.z'
        resx = '\\\\my\\\\odd\\\\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\\\\myfile.z'

        res = filesysobjects.paths.unescapepathx(
            arg, 
            tpf='posix',
            force=False
            )

#         argHex  = ' '.join(hex(ord(x)) for x in arg)
#         argChar = '    '.join(x for x in arg)
#         resxHex  = ' '.join(hex(ord(x)) for x in resx)
#         resxChar = '    '.join(x for x in resx)
#         resHex   = ' '.join(hex(ord(x)) for x in res)
#         resChar  = '    '.join(x for x in res)
#         
#         print("4TEST:arg     = " + str(arg))
#         print("4TEST:resx    = " + str(resx))
#         print("4TEST:res     = " + str(res))
#         print()
#         print("4TEST:argHex  = " + str(argHex))
#         print("4TEST:argChar = " + str(argChar))
#         print("4TEST:resHex  = " + str(resxHex))
#         print("4TEST:resChar = " + str(resxChar))
#         self.assertEqual(resHex, resxHex)

        self.assertEqual(res, resx)

    def testCase040(self):
        arg = r'\\my\\odd\\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\\myfile.z'
#        resx = '\\\\my\\odd\\searchpath\\' + '\a\\' + '\b\\' + '\n\\' + '\r\\' + '\t"""[\/xyz].*"""\\myfile.z'
        resx = '\\\\my\\odd\\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\\myfile.z'

        res = filesysobjects.paths.unescapepathx(
            arg, 
            tpf='posix',
            netpath=True,
            force=True
            )

#         argHex  = ' '.join(hex(ord(x)) for x in arg)
#         argChar = '    '.join(x for x in arg)
#         resxHex  = ' '.join(hex(ord(x)) for x in resx)
#         resxChar = '    '.join(x for x in resx)
#         resHex   = ' '.join(hex(ord(x)) for x in res)
#         resChar  = '    '.join(x for x in res)
#          
#         print("4TEST:arg     = " + str(arg))
#         print("4TEST:resx    = " + str(resx))
#         print("4TEST:res     = " + str(res))
#         print()
#         print("4TEST:argHex  = " + str(argHex))
#         print("4TEST:argChar = " + str(argChar))
#         print("4TEST:resHex  = " + str(resxHex))
#         print("4TEST:resChar = " + str(resxChar))
#         self.assertEqual(resHex, resxHex)

        self.assertEqual(res, resx)

    def testCase050(self):
        arg = r'\\my\\odd\\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\\myfile.z'
#        resx = '\my\odd\searchpath\\' + '\a\\' + '\b\\' + '\n\\' + '\r\\' + '\t"""[\/xyz].*"""\myfile.z'
        resx = '\my\odd\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\myfile.z'

        res = filesysobjects.paths.unescapepathx(
            arg, 
            tpf='posix',
            netpath=False,
            force=True
            )

#         argHex  = ' '.join(hex(ord(x)) for x in arg)
#         argChar = '    '.join(x for x in arg)
#         resxHex  = ' '.join(hex(ord(x)) for x in resx)
#         resxChar = '    '.join(x for x in resx)
#         resHex   = ' '.join(hex(ord(x)) for x in res)
#         resChar  = '    '.join(x for x in res)
#          
#         print("4TEST:arg     = " + str(arg))
#         print("4TEST:resx    = " + str(resx))
#         print("4TEST:res     = " + str(res))
#         print()
#         print("4TEST:argHex  = " + str(argHex))
#         print("4TEST:argChar = " + str(argChar))
#         print("4TEST:resHex  = " + str(resxHex))
#         print("4TEST:resChar = " + str(resxChar))
#         self.assertEqual(resHex, resxHex)

        self.assertEqual(res, resx)

    def testCase060(self):
        arg = r'\\my\\odd\\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\\myfile.z'
#        resx = '\my\odd\searchpath\\' + '\a\\' + '\b\\' + '\n\\' + '\r\\' + '\t' + '"""[\/xyz].*"""\myfile.z'
        resx = '\my\odd\searchpath\\a\\b\\n\\r\\t"""[\/xyz].*"""\myfile.z'

        res = filesysobjects.paths.unescapepathx(
            arg, 
            tpf='posix',
            force=True
            )

#         argHex  = ' '.join(hex(ord(x)) for x in arg)
#         argChar = '    '.join(x for x in arg)
#         resxHex  = ' '.join(hex(ord(x)) for x in resx)
#         resxChar = '    '.join(x for x in resx)
#         resHex   = ' '.join(hex(ord(x)) for x in res)
#         resChar  = '    '.join(x for x in res)
#           
#         print("4TEST:arg     = " + str(arg))
#         print("4TEST:resx    = " + str(resx))
#         print("4TEST:res     = " + str(res))
#         print()
#         print("4TEST:argHex  = " + str(argHex))
#         print("4TEST:argChar = " + str(argChar))
#         print("4TEST:resHex  = " + str(resxHex))
#         print("4TEST:resChar = " + str(resxChar))
#         self.assertEqual(resHex, resxHex)

        self.assertEqual(res, resx)

if __name__ == '__main__':
    unittest.main()

