# -*- coding: utf-8 -*-
from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import os,sys
import unittest
from unittest import SkipTest

import filesysobjects.apppaths

#
#######################
#

class CallUnits(unittest.TestCase):
    
    def testCase070(self):
        _in    = 'd:/'
        resX = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase071(self):
        _in    = 'd:\\'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)
        
    def testCase072(self):
        _in    = 'd:\\\\'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase073(self):
        _in    = 'd:\\\\\\\\'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase074(self):
        _in    = 'd:///'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase075(self):
        _in    = 'd:\\\\\\'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase076(self):
        _in    = 'd:///'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase077(self):
        _in    = 'd:\\\\\\'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase080(self):
        _in    = 'd:\\/'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase081(self):
        _in    = 'd:\\///////'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase082(self):
        _in    = 'd:\\\\\\///////'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase090(self):
        _in    = 'd:\\\\/\\\\/'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase091(self):
        _in    = 'd:\\\\/\\\\///\\\\/'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)


    def testCase092(self):
        _in    = 'd:\\\\/\\\\///\\\\/\\\\/\\\\////////'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase100(self):
        _in    = 'd:\\/\\/'
        resX  = 'd:/'

        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

