from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.paths

#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase000(self):
        apstr = 'd:/a/b/c'
        retRef = ('ldsys','', 'd:', os.path.normpath('/a/b/c')) 
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='win')[0]
        self.assertEqual(retRef, ret) 
        
    def testCase010(self):
        apstr = os.path.normpath('d:a/b/c')
        retRef = ('ldsys','', 'd:', filesysobjects.paths.escapepathx(os.path.normpath('a/b/c'))) 
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='win')[0]

        ret = (ret[0], ret[1], ret[2], filesysobjects.paths.escapepathx(ret[3]) ) 

        self.assertEqual(retRef, ret) 
        

    def testCase020(self):
        apstr = 'd:'
        retRef = ('ldsys','', 'd:', '') 
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='win')[0]
        self.assertEqual(retRef, ret) 

    def testCase030(self):
        apstr = 'd:'+os.path.normpath('/')
        retRef = ('ldsys','', 'd:', os.path.normpath('/')) 
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='win')[0]
        self.assertEqual(retRef, ret) 

#
#######################
#

if __name__ == '__main__':
    unittest.main()

