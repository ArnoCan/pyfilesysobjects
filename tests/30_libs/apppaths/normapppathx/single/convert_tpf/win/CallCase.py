# -*- coding: utf-8 -*-
from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import os,sys
import unittest
from unittest import SkipTest

import filesysobjects.paths

#
#######################
#

class CallUnits(unittest.TestCase):
    
    def testCase000(self):
        _in    = '\a'
        resX  = '\a' 
        res = filesysobjects.apppaths.normapppathx(_in, spf='posix')
        self.assertEqual(res, resX)

    def testCase001(self):
        _in    = 'd:/a/b/c'
        resX  = os.path.normpath('d:\\'+'a\\'+'b\c')  # used as an unaltered reference, thus prep it
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase080(self):
        _in        = 'd:/'
        resX  = 'd:\\'
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)
        
    def testCase081(self):
        _in        = 'd:\\'
        resX  = os.path.normpath('d:\\' )
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)
        
    def testCase082(self):
        _in        = 'd:///'
        resX  = os.path.normpath('d:\\')
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase083(self):
        _in        = 'd:\\\\\\'
        resX  = os.path.normpath('d:\\')
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase084(self):
        _in        = 'd:///'
        resX  = os.path.normpath('d:\\')
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase085(self):
        _in        = 'd:\\\\\\'
        resX  = os.path.normpath('d:\\')
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase088(self):
        _in        = 'd:\\/'
        resX  = os.path.normpath('d:\\')
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase089(self):
        _in        = 'd:\\\\/\\\\///\\\\//////////'
        resX  = os.path.normpath('d:\\')
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase090(self):
        _in        = 'd:/a\b/c'
        resX  = 'd:\\a\b\\c'
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)

    def testCase091(self):
        _in        = 'd:a\b\c'
        resX  = 'd:a\b\\c'
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='win')
        self.assertEqual(res, resX)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

