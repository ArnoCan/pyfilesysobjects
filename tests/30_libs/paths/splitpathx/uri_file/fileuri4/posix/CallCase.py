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
from filesysobjects import PathError
#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase000(self):

        path = 'a/b/c'

        try:
            filesysobjects.paths.splitpathx(path, spf='posix', apppre=True, tpf='fileuri4')
        except PathError:
            pass

    def testCase010(self):

        path = '/a/b/c'
        resX = ('file://', 'a', 'b', 'c')
        resXpath = 'file:///a/b/c'

        res = filesysobjects.paths.splitpathx(path, spf='posix', apppre=True, tpf='fileuri4')
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

    def testCase020(self):

        path = '//a/b/c'
        resX = ('file:///', 'a', 'b', 'c')
        resXpath = 'file:////a/b/c'

        res = filesysobjects.paths.splitpathx(path, spf='posix', apppre=True, tpf='fileuri4')
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)

if __name__ == '__main__':
    unittest.main()

