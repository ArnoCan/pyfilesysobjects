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

import testdata.filesysobjects

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase010(self):

        path = '/*/[!ac]/[^abd-z]/[cd][^"""' + os.sep + '"""]*[.][p][^"""' + os.sep + '"""]*'
        resX = ('', '*', '[!ac]', '[^abd-z]', '[cd][^' + os.sep + ']*[.][p][^' + os.sep + ']*')
        resXpath = '/*/[!ac]/[^abd-z]/[cd][^' + os.sep + ']*[.][p][^' + os.sep + ']*'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = '/'.join(res)

        self.assertEqual(res, resX)
        self.assertEqual(respath, resXpath)


    def testCase100(self):

        path = os.path.dirname(tdata) + '/*/[!ac]/[^abd-z]/[cd][^"""' + os.sep + '"""]*[.][p][^"""' + os.sep + '"""]*'
        resX = (
            'testdata', 'filesysobjects', '*',
            '[!ac]', '[^abd-z]', '[cd][^' + os.sep + ']*[.][p][^' + os.sep + ']*'
            )
        resXpath = os.path.dirname(tdata) + os.sep + '*' + os.sep + '[!ac]' + os.sep + '[^abd-z]' + os.sep + '[cd][^' + os.sep + ']*[.][p][^' + os.sep + ']*'

        res = filesysobjects.paths.splitpathx(path, pathsep=':', strip=True, stripquote=True)
        respath = os.sep.join(res)

        self.assertEqual(res[-6:], resX)
        self.assertEqual(respath, resXpath)
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

