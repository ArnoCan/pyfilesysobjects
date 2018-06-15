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

from filesysobjects import RTE, RTE_WIN32
import filesysobjects.paths
import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        resX = ['', 'my', 'path', '[^/]*', '[c][.][p][^/]*', ]
        arg = '/my/path/"""[^/]*/"""[c][.][p][^"""/"""]*'
        arg = filesysobjects.apppaths.normpathx(arg, stripquote=True, tpf='posix', spf='posix')
        res = filesysobjects.pathtools.splitre_separator(arg)
        self.assertEqual(res, resX)

    def testCase010(self):
        resX = ['', 'my', 'path', '[^/]*', '[c][.][p][^/]*', ]
        arg = '/my/path/"""[^/]*/"""[c][.][p][^"""/"""]*'
        arg = filesysobjects.apppaths.normpathx(arg, stripquote=True, tpf='posix', spf='posix')
        res = filesysobjects.pathtools.splitre_separator(arg)
        self.assertEqual(res, resX)

    def testCase020(self):
        resX = ['', 'my', 'path', '[^/]*', '[c][.][p][^/]*']
        arg = '/my/path/"""[^/]*/"""[c][.][p][^"""/"""]*'
        arg = filesysobjects.apppaths.normpathx(arg, stripquote=True, tpf='win', spf='posix')
        res = filesysobjects.pathtools.splitre_separator(arg)
        self.assertEqual(res, resX)

    def testCase030(self):
        resX = ['', 'my', 'path', '[^/]*', '[c][.][p][^/]*']
        arg = '/my/path/"""[^/]*/"""[c][.][p][^"""/"""]*'
        arg = filesysobjects.apppaths.normpathx(arg, stripquote=True, tpf='win', spf='win')
        res = filesysobjects.pathtools.splitre_separator(arg)
        self.assertEqual(res, resX)

    def testCase040(self):
        resX = ['', 'my', 'path', '[^/]*', '[c][.][p][^/]*']
        arg = '/my/path/"""[^/]*/"""[c][.][p][^"""/"""]*'
        arg = filesysobjects.apppaths.normpathx(arg, stripquote=True, tpf='posix', spf='win')
        res = filesysobjects.pathtools.splitre_separator(arg)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

