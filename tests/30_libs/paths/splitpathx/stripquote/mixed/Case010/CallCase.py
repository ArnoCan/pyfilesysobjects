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
        
        path = '''/"\""b"""'''
        resX = ('', 'b',)
        resXpath = '/b'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        
    def testCase001(self):
        
        path = "/""""b"""
        resX = ('', 'b',)
        resXpath = '/b'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase002(self):
        
        path = "/""""'''b"""
        resX = ('', "'''b",)
        resXpath = "/'''b"
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase003(self):
        
        path = "/""""b'''"""
        resX = ('', "b'''",)
        resXpath = "/b'''"
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase004(self):
        
        path = "/""""''b'''"""
        resX = ('', "''b'''",)
        resXpath = "/''b'''"
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase005(self):
        
        path = "/""""'''b'''"""
        resX = ('', "'''b'''",)
        resXpath = "/'''b'''"
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertNotEqual(res, resX)
        self.assertNotEqual(respath, resXpath)

    def testCase006(self):
        
        path = "/"'''"""b"""'''
        resX = ('', '"""b"""',)
        resXpath = '/"""b"""'
        
        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertNotEqual(res, resX)
        self.assertNotEqual(respath, resXpath)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

