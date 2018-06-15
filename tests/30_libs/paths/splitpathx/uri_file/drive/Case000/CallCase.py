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
import string
import filesysobjects.paths

#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase000(self):
        
        path = 'x:/a/b/c'
        resX = ('x:', 'a', 'b', 'c')
        resXpath = 'x:/a/b/c'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, spf='win')
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase010(self):
        
        path = 'file:x:/a/b/c'
        resX = ('x:', 'a', 'b', 'c')
        resXpath = 'x:/a/b/c'
        
#        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, spf='win')
#        res = filesysobjects.paths.splitpathx(path, spf='win')
        res = filesysobjects.paths.splitpathx(path, spf='win', apppre=False)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

