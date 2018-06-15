from __future__ import absolute_import
from linecache import getline
from filesysobjects import RTE_WIN32


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os
import ntpath
import posixpath

from filesysobjects import RTE, RTE_WIN32
import filesysobjects.paths

#
#######################
#

class CallUnits(unittest.TestCase):

    def testCase000(self):
        _in    = '\\a'
        if RTE & RTE_WIN32:
            resX  = ntpath.normpath('\\a')
        else:
            resX  = posixpath.normpath('\\a')
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase001(self):
        _in    = '\a'
        if RTE & RTE_WIN32:
            resX  = ntpath.normpath('\a')
        else:
            resX  = posixpath.normpath('\a')

        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase002(self):
        _in    = r'\a'
        if RTE & RTE_WIN32:
            resX  = ntpath.normpath(r'\a')
        else:
            resX  = posixpath.normpath(r'\a')
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase010(self):
        _in    = 'd:\\a'
        if RTE & RTE_WIN32:
            resX  = ntpath.normpath('d:\\a')
        else:
            resX  = posixpath.normpath('d:\\a')
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase011(self):
        _in    = 'd:\a'
        if RTE & RTE_WIN32:
            resX  = ntpath.normpath('d:\a')
        else:
            resX  = posixpath.normpath('d:\a')
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase012(self):
        _in    = 'd:/a'
        if RTE & RTE_WIN32:
            resX  = ntpath.normpath('d:\\a')
        else:
            resX  = posixpath.normpath('d:/a')
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase020(self):
        _in    = 'd:\\'
        if RTE & RTE_WIN32:
            resX  = 'd:\\'
        else:
            resX  = 'd:\\'
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase021(self):
        _in    = 'd:/'
        if RTE & RTE_WIN32:
            resX  = 'd:\\'
        else:
            resX  = 'd:'
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)

    def testCase030(self):
        _in    = '/a/b/c'
        if RTE & RTE_WIN32:
            resX  = ntpath.normpath('/a/b/c')
        else:
            resX  = posixpath.normpath('/a/b/c')
        res = filesysobjects.paths.normpathx(_in, spf='win', tpf='local')
        self.assertEqual(res, resX)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

