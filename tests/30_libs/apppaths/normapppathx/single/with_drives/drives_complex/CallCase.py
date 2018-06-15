from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

import filesysobjects.apppaths

#
#######################
#

class CallUnits(unittest.TestCase):
    
    def testCase010(self):
        _in = 'd://hostname/tests//////a/b/hostname//c////////d/tests/b///c'
        resX = 'd://hostname/tests/a/b/hostname/c/d/tests/b/c'
        res = filesysobjects.apppaths.normapppathx(_in, spf='posix', tpf='posix')
        self.assertEqual(resX, res)

    def testCase011(self):
        _in = 'd://hostname/tests//////a/b/hostname//c////////d/tests/b///c'
        resX = 'd:/hostname/tests/a/b/hostname/c/d/tests/b/c'
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(resX, res)

    def testCase012(self):
        _in = 'd://hostname/tests//////a/b/hostname//c////////d/tests/b///c'
        resX = r'd:\hostname\tests\a\b\hostname\c\d\tests\b\c'
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(resX, res)

    def testCase020(self):
        _in = 'hostname/'
        resX = 'hostname'
        res = filesysobjects.apppaths.normapppathx(_in, spf='posix', tpf='posix')
        self.assertEqual(resX, res)

    def testCase021(self):
        _in = 'hostname/'
        resX = 'hostname'
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(resX, res)

    def testCase030(self):
        _in = 'd:/hostname/'
        resX = 'd:/hostname'
        res = filesysobjects.apppaths.normapppathx(_in, spf='posix', tpf='posix')
        self.assertEqual(resX, res)

    def testCase031(self):
        _in = 'd:/hostname/'
        resX = 'd:\\hostname'
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(resX, res)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

