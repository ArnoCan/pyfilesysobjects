from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.4'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import sys

import testdata.filesysobjects

from filesysobjects.pathtools import findrelpath_in_searchpath
from filesysobjects.paths import normpathx
from filesysobjects.apppaths import  set_uppertree_searchpath
from filesysobjects.apppaths import gettop_from_pathstring

#
#######################
#

class UseCase(unittest.TestCase):
    def testCase000(self):

        # *** save sys.path ***
        _s = sys.path[:]
        # *********************

        _start = testdata.filesysobjects.mypath + '/findnodes/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h'
        _start = normpathx(_start)
        _top = "a/b/c/d/"
        _top = normpathx(_top)
        _tlst = []

        # set search for the call of 'myscript.sh'
        set_uppertree_searchpath(_start,'filesysobjects')

        # 0. get top node within-start/path, this is eventually base on a part of the
        #    search path, gets the topmost hook by default.
        topX = gettop_from_pathstring(_top, [_start])

        # 1. set the search list
        t = set_uppertree_searchpath(_start, topX, _tlst)
        if t:
            # 2. search side branch
            a0 = findrelpath_in_searchpath(
                "a/*/data",
                _tlst,
                **{'reverse':True,'matchidx':1}
            )

            b0 = findrelpath_in_searchpath(
                "a/*/data",
                _tlst,
                **{'matchidx':0}
            )

            a1 = findrelpath_in_searchpath(
                "a/*/*/data",
                _tlst,
                **{'reverse':True,'matchidx':1}
            )

            b1 = findrelpath_in_searchpath(
                "a/*/*/data",
                _tlst,
                **{'matchidx':0}
            )

        # *** restore sys.path ***
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        # ************************

        assert a0 == b0
        assert a1 == b1

        assert a0 != a1

        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

