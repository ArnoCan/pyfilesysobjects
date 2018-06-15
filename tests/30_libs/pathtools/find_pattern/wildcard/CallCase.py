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
from filesysobjects.apppaths import  set_uppertree_searchpath
from filesysobjects.apppaths import gettop_from_pathstring

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


        _start = testdata.filesysobjects.mypath + '/findnodes/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h'
        _start = normpathx(_start)
        _top = os.sep + "a" + os.sep
        _top = normpathx(_top, keepsep=True)
        _tlst = []

        # set search for the call of 'myscript.sh'
        set_uppertree_searchpath(_start,'filesysobjects')

        topx = gettop_from_pathstring(_top, [_start],**{'pattern':'regexpr',})
        t = set_uppertree_searchpath(_start, topx, _tlst)
        if t:
            a0 = findrelpath_in_searchpath(
                "b/*/[def]/",
                _tlst,
                **{'reverse':True,'matchidx':0}
            )

        assert a0.endswith(normpathx(topx + "/b/c/d"))

        pass


if __name__ == '__main__':
    unittest.main()

