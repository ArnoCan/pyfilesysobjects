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

        _tlst = []

        _start = testdata.filesysobjects.mypath + '/findnodes/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h/a/b/c/d/e/f/g/h'
        _start = normpathx(_start)
        
        # 0. get top node by regular expression
        _top = "a/b/[a-z]+/.*/data"
        _top = normpathx(_top)
        topX = gettop_from_pathstring(_top, [_start],**{'pattern':'regexpr',})
        topx = gettop_from_pathstring(_top, [_start],**{'pattern':'regexpr',})
        
        _top = "a/b/[^/]*/[def]{1}/data"
        _top = normpathx(_top)
        topY = gettop_from_pathstring(_top, [_start],**{'pattern':'regexpr',})
        topy = gettop_from_pathstring(_top, [_start],**{'pattern':'regexpr',})

        # *** restore sys.path ***
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        # ************************
        
        assert topX == topY
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

