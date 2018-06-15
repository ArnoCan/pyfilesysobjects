# -*- coding: utf-8 -*-
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

        raw = u'/Français/złoty/Österreich'
        esc = u'/Français/złoty/Österreich'
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)

    def testCase020_printInput(self):

        raw =  u'/Fran\açais/złoty/Öste\ar-\nreich'
        esc = u'/Fran\\açais/złoty/Öste\\ar-\\nreich'
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)

    def testCase030_printInput(self):

        raw =  u'/FrǞan\açaǣis/złoty/Öste\ar-\nreich'
        esc = u'/FrǞan\\açaǣis/złoty/Öste\\ar-\\nreich'
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)

    def testCase040_printInput(self):

        raw =  u'/Fr\u01dean\aça\u01e3is/złoty/Öste\ar-\nreich'
        esc = u'/Fr\u01dean\\a\xe7a\u01e3is/z\u0142oty/\xd6ste\\ar-\\nreich'
        
        _esc = escapepathx(raw)
        _unesc = unescapepathx(_esc)

        self.assertEqual(esc, _esc)
        self.assertEqual(raw, _unesc)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

