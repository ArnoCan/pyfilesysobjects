from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

from filesysobjects.paths import escapepathx, unescapepathx

#
#######################
#

class CallUnits(unittest.TestCase):
# 
#     def testCase000_printInput(self):
# 
# 
#         import re
#         x = '\a'
#         xl = len(x)
#         xr = re.escape(x)
#         xrl = len(xr)
#         
#         a0 = '\a'
#         a1 = '\\' + '\a'
#         a2 = '\\a'
#         l0 = len(a0)
#         l1 = len(a1)
#         l2 = len(a2)
#         print(a0)
#         print(a1)
#         print(a2)
# 
#         
# #         raw0 = '\abc"\n"'
# #         esc0 = '\\' + '\abc"\n"'
# #         _esc0 = escapepathx(raw0)
# #         _unesc0 = unescapepathx(_esc0)
# #         
# #         raw1 = '\abc"\a\n"'
# #         esc1 = '\\abc"\a\n"'
# #         _esc1 = escapepathx(raw1)
# #         _unesc1 = unescapepathx(_esc1)
#         pass

    def testCase010_printInput(self):

        raw = '\abc"\n"'
        esc = '\\abc"\\n"'
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)
        pass
        
    def testCase011_printInput(self):

        raw = '\abc"""x\ny\n"""'
        esc = '\\abc"""x\ny\n"""'
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)
        pass
        
    def testCase020_printInput(self):

        raw = "\abc'''x\ny\n'''"
        esc = "\\abc'''x\ny\n'''"
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

