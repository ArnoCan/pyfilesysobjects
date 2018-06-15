from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

#
#######################
#

import filesysobjects.apppaths
import filesysobjects.pathtools
import filesysobjects.paths
import testdata.filesysobjects

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase010(self):
        arg = '/"""[!x]*[/]"""'
        arg = filesysobjects.apppaths.normapppathx(arg)
        res = filesysobjects.paths.splitpathx(arg, stripquote=True)
        resX = ('', '[!x]*[/]')
        self.assertEqual(res, resX)
        pass

    def testCase011(self):
        arg = '/b/"""[!x]*[/]"""'
        arg = filesysobjects.apppaths.normapppathx(arg)
        res = filesysobjects.paths.splitpathx(arg, stripquote=True)
        resX = ('', 'b', '[!x]*[/]')
        self.assertEqual(res, resX)
        pass


    def testCase020(self):
        
        arg = '/b/"""[!x]*[/]"""[c][.][p]'
        arg = filesysobjects.apppaths.normapppathx(arg)
        res = filesysobjects.paths.splitpathx(arg, stripquote=True)
        resX = ('', 'b', '[!x]*[/][c][.][p]')
        self.assertEqual(res, resX)
        pass

    def testCase030(self):
        
        arg = '/b/"""[!x]*[/]"""[c][.][p][^"""/"""]*'
        arg = filesysobjects.apppaths.normapppathx(arg)
        res = filesysobjects.paths.splitpathx(arg, stripquote=True)
        resX = ('', 'b', '[!x]*[/][c][.][p][^/]*')
        self.assertEqual(res, resX)
        pass


    def testCase300(self):
        lx = len(filesysobjects.paths.splitpathx(tdata))        
        arg = tdata + '/b/"""[!x]*[/]"""[c][.][p][^"""/"""]*'
        resX = ('b', '[!x]*[/][c][.][p][^/]*')
        res = filesysobjects.paths.splitpathx(arg, stripquote=True)
        self.assertEqual(res[lx:], resX)
        pass



#
#######################
#

if __name__ == '__main__':
    unittest.main()

