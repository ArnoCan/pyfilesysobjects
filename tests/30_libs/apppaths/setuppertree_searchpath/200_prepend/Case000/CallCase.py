from __future__ import absolute_import

import unittest
import os,sys

from filesysobjects.apppaths import set_uppertree_searchpath,addpath_to_searchpath
from filesysobjects.paths import unescapepathx

#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase000(self):
        self.maxDiff = None
        _s = sys.path[:]

        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        start = os.path.abspath(os.path.dirname(__file__))
        top = os.path.abspath(os.path.dirname(__file__))
        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable

        sp = os.path.dirname(os.path.dirname(__file__)+os.sep+C)
        addpath_to_searchpath(sp, res,**{'prepend':True})

        resx = [
            os.path.dirname(os.path.dirname(__file__)+os.sep+C),
            os.path.abspath(os.path.dirname(__file__)),
        ]
        resx = map(os.path.normpath,resx)

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        res = [unescapepathx(i) for i in res]
        resx = [unescapepathx(i) for i in resx]

        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()
