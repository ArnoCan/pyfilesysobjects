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
    
    def testCase002(self):
        _in    = 'd:a\\b\c'
        resX  = 'd:a/b/c' 
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)

    def testCase010(self):
        _in    = 'd:'
        resX  = os.path.normpath('d:' )
        res = filesysobjects.apppaths.normapppathx(_in, spf='win', tpf='posix')
        self.assertEqual(res, resX)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

