# -*- coding: utf-8 -*-
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

from filesysobjects.paths import normpathx
from filesysobjects import RTE, RTE_WIN32
#
#######################
#

class CallUnits(unittest.TestCase):

    def testCase010_printInput(self):

        raw = u'/Français/złoty/Österreich'
        if RTE & RTE_WIN32:
            resX = u'\\Français\\złoty\\Österreich'
        else:
            resX = u'/Français/złoty/Österreich'

        res = normpathx(raw)
        self.assertEqual(res, resX)

    def testCase020_printInput(self):

        raw =  u'/Fran\açais/złoty/Öste\ar-\nreich'
        if RTE & RTE_WIN32:
            resX = u'\\Fran\açais\\złoty\\Öste\ar-\nreich'
        else:
            resX = u'/Fran\açais/złoty/Öste\ar-\nreich'

        res = normpathx(raw)
        self.assertEqual(res, resX)

    def testCase030_printInput(self):

        raw =  u'/FrǞan\açaǣis/złoty/Öste\ar-\nreich'

        if RTE & RTE_WIN32:
            resX = u'\\FrǞan\açaǣis\\złoty\\Öste\ar-\nreich'
        else:
            resX = u'/FrǞan\açaǣis/złoty/Öste\ar-\nreich'

        res = normpathx(raw)
        self.assertEqual(res, resX)

    def testCase040_printInput(self):

        raw =  u'/Fr\u01dean\aça\u01e3is/złoty/Öste\ar-\nreich'

        if RTE & RTE_WIN32:
            resX = u'\\FrǞan\açaǣis\\złoty\\Öste\ar-\nreich'
        else:
            resX = u'/FrǞan\açaǣis/złoty/Öste\ar-\nreich'

        res = normpathx(raw)
        self.assertEqual(res, resX)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

