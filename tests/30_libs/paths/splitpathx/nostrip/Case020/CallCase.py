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
        
        path = r'\a/\b\c/'
        resX = ('', 'a', '', 'b', 'c', '')
        resXpath = '\\a\\\\b\\c\\'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        
    def testCase010(self):
        
        path = r'\//\a\b//\c'
        resX = ('', '', '', '', 'a', 'b', '', '', 'c')
        resXpath = '\\\\\\\\a\\b\\\\\\c'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        
        
    def testCase011(self):

        path = r'/\\/a/b\\/c'
        resX = ('', '', '', '', 'a', 'b', '', '', 'c')
        resXpath = '\\\\\\\\a\\b\\\\\\c'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        
    def testCase015(self):
        
        path = r'\a\//\b//\c'
        resX = ('', 'a', '', '', '', 'b', '', '', 'c')
        resXpath = '\\a\\\\\\\\b\\\\\\c'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        
    def testCase020(self):
        
        path = r'\//\a\//\b//\c'
        resX = ('', '', '', '', 'a', '', '', '', 'b', '', '', 'c')
        resXpath = '\\\\\\\\a\\\\\\\\b\\\\\\c'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        
    def testCase030(self):
        
        path = r'\a\/\b\//\c'
        resX = ('', 'a', '', '', 'b', '', '', '', 'c')
        resXpath = '\\a\\\\\\b\\\\\\\\c'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        
    def testCase040(self):
        
        path = r'\a\\\///b\c/\/'
        resX = ('', 'a', '', '', '', '', '', 'b', 'c', '', '', '')
        resXpath = '\\a\\\\\\\\\\\\b\\c\\\\\\'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase050(self):
        
        path = '\\a\\"""\\"""b/"""//"""c\\'
        resX = ('', 'a', '"""\\"""b', '"""//"""c', '')
        resXpath = '\\a\\"""\\"""b\\"""//"""c\\'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase060(self):
        
        path = '\\a\\"""\\"""b\\"""//"""c\\'
        resX = ('', 'a', '"""\\"""b', '"""//"""c', '')
        resXpath = '\\a\\"""\\"""b\\"""//"""c\\'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase070(self):
        
        path = '\\a\\"""\\"""b\"""//"""c\\'
        resX = ('', 'a', '"""\\"""b"""//"""c', '')
        resXpath = '\\a\\"""\\"""b\"""//"""c\\'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=';', strip=False)
        respath = '\\'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

