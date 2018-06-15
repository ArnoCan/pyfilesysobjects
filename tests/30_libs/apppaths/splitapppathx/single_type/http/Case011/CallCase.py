from __future__ import absolute_import

import unittest
import os

import filesysobjects.apppaths
from filesysobjects import RTE, RTE_WIN32


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase000(self):
        apstr = 'http://hostname/a/b/c'
        retRef = [('http','hostname', '', '/a/b/c', '')]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True)
        self.assertEqual(retRef, ret)

    def testCase010(self):
        apstr = filesysobjects.apppaths.normapppathx('http://hostname/a/b/c?query#fragment')
        retRef = [('http','hostname', '', '/a/b/c', '?query#fragment')]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True)
        self.assertEqual(retRef, ret)

    def testCase020(self):
        apstr = 'http://'+filesysobjects.paths.normpathx('hostname/a/b/c')
        retRef = [('http','hostname', '', '/a/b/c', '')]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True)
        self.assertEqual(retRef, ret)

    def testCase030(self):
        apstr = 'http://'+filesysobjects.paths.normpathx('hostname/a/b/c')
        retRef = [('http','hostname', '', '/a/b/c', '')]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True)
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

