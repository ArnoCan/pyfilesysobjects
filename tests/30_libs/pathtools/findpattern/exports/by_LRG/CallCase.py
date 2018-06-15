from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.4'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import sys,os

import testdata.filesysobjects

from filesysobjects.pathtools import findrelpath_in_searchpath
from filesysobjects.paths import normpathx
from filesysobjects.apppaths import set_uppertree_searchpath

#
#######################
#

class UseCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self._s = sys.path[:]

    def tearDown(self):
        unittest.TestCase.tearDown(self)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(self._s)

    def testCase000(self):
        self.maxDiff = None

        start = testdata.filesysobjects.mypath + '/findnodes/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h'
        start = normpathx(start)

        topnode = testdata.filesysobjects.mypath + '/findnodes'

        #
        # set the search list
        pathlist = []
        t = set_uppertree_searchpath(start, topnode, pathlist)

        self.assertTrue(t)

        # search side branches
        sidebranches  = findrelpath_in_searchpath(
            'a/*/*/d',
            pathlist,
            reverse=True,
            matchidx=1,
        )

        resx = normpathx(testdata.filesysobjects.mypath + '/findnodes/a/b/c/d/e/f/g/a/b/c/d')
        self.assertEqual(sidebranches, resx)
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

