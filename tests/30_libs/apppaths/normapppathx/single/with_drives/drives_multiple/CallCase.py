from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import filesysobjects.paths

#
#######################
#

class CallUnits(unittest.TestCase):
    
    def testCase000(self):
        s = os.sep
        s10 = 10*os.sep
        _in = 'd:'+s+'a'+s10+'b'+s+'c'
        _norm   = os.path.normpath('d:/a/b/c')
        _in += os.pathsep + _in
        _norm  += os.pathsep + _norm
        res = filesysobjects.paths.normpathx(_in)
        self.assertEqual(res, _norm)
        
    def testCase010(self):
        s = os.sep
        s10 = 10*os.sep
        _in = 'd:'+s+'a'+s10+'b'+s+'c'
        _norm   = os.path.normpath('d:/a/b/c')
        _in += os.pathsep + _in
        _norm  += os.pathsep + _norm
        res = filesysobjects.paths.normpathx(_in)
        self.assertEqual(res, _norm)

    def testCase020(self):
        s = os.sep
        s7 = 7*os.sep
        _in = 'd:'+s+'a'+s7+'b'+s+'c'
        _norm   = os.path.normpath('d:/a/b/c')
        _in += os.pathsep + _in
        _norm  += os.pathsep + _norm
        res = filesysobjects.paths.normpathx(_in)
        self.assertEqual(res, _norm)

    def testCase030(self):
        s = os.sep
        s7 = 7*os.sep
        _in = 'd:'+s+'a'+s+'b'+s7+'c'
        _norm   = os.path.normpath('d:/a/b/c')
        _in += os.pathsep + _in
        _norm  += os.pathsep + _norm
        res = filesysobjects.paths.normpathx(_in)
        self.assertEqual(res, _norm)

    def testCase050(self):
        s = os.sep
        _in = 'd:'+s
        _norm  = 'd:'+s
        _in += os.pathsep + _in
        _norm  += os.pathsep + _norm
        res = filesysobjects.paths.normpathx(_in)
        self.assertEqual(res, _norm)

    def testCase060(self):
        s = os.sep
        s7 = 7*os.sep #@UnusedVariable
        s10 = 10*os.sep #@UnusedVariable
        _in = 'd:'+s
        _norm  = 'd:'+os.sep
        _in += os.pathsep + _in
        _norm  += os.pathsep + _norm
        res = filesysobjects.paths.normpathx(_in)
        self.assertEqual(res, _norm)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

