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

    def testCase010_printInput(self):

        raw = '\w1\w1\w2'
        esc = '\\w1\\w1\\w2'
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)
        pass
        

if __name__ == '__main__':
    unittest.main()

