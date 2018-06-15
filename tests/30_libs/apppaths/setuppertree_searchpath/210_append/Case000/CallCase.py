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
        top = start
        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable

        addpath_to_searchpath(os.path.dirname(os.path.dirname(__file__)+os.sep+C), res,**{'append':True})

        resx = [
            os.path.abspath(os.path.dirname(__file__)),
            os.path.dirname(os.path.dirname(__file__)+os.sep+C),
        ]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

#         res = [unescapepathx(i) for i in res]
#         resx = [unescapepathx(i) for i in resx]

        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()
