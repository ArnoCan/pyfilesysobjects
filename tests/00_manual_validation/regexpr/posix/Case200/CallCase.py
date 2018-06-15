from __future__ import absolute_import


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
        
        path = '/a/"""[^/]+"""/""".*"""/"""[c]+.sh"""'
        resX = ('', 'a', '"""[^/]+"""', '""".*"""', '"""[c]+.sh"""')
        resXpath = '/a/"""[^/]+"""/""".*"""/"""[c]+.sh"""'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        self.assertEqual(path, respath)

    def testCase020(self):
        
        path = '/a/"""[^/]+"""/""".*"""/"""[c]+.sh"""'
        resX = ('', 'a', '"""[^/]+"""', '""".*"""', '"""[c]+.sh"""')
        resXpath = '/a/"""[^/]+"""/""".*"""/"""[c]+.sh"""'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=False)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        self.assertEqual(path, respath)

    def testCase100(self):
        
        path = '/a/"""[^/]+"""/""".*"""/"""[c]+.sh"""'
        resX = ('', 'a', '[^/]+', '.*', '[c]+.sh')
        resXpath = '/a/[^/]+/.*/[c]+.sh'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        pass

    def testCase101(self):
        
        path = '/a/"""[^/]+"""/.*/[c]+.sh'
        resX = ('', 'a', '[^/]+', '.*', '[c]+.sh')
        resXpath = '/a/[^/]+/.*/[c]+.sh'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        pass

    def testCase102(self):
        
        path = '/a/[^"""/"""]+/.*/[c]+.sh'
        resX = ('', 'a', '[^/]+', '.*', '[c]+.sh')
        resXpath = '/a/[^/]+/.*/[c]+.sh'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        pass

    def testCase103(self):
        
        path = '/a/[^"""/"""]+/.*/[c]+.sh'
        resX = ('', 'a', '[^"""/"""]+', '.*', '[c]+.sh')
        resXpath = '/a/[^"""/"""]+/.*/[c]+.sh'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=False)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)
        pass
#
#######################
#

if __name__ == '__main__':
    unittest.main()

