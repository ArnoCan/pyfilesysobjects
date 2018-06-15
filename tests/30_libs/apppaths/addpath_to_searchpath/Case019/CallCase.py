from __future__ import absolute_import

import os,sys
import unittest

from filesysobjects.apppaths import set_uppertree_searchpath,addpath_to_searchpath
import testdata.filesysobjects


#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase000(self):
        _s = sys.path[:]

        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable
 
        start = os.path.abspath(os.path.dirname(__file__))
        top = start
        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable
        dx = "file://"+os.path.abspath(testdata.filesysobjects.mypath+os.sep+D)
        addpath_to_searchpath( dx, res)
        res = [os.path.abspath(os.path.normpath(i)) for i in res]

        resx = [
            testdata.filesysobjects.mypath+os.sep+D,
            os.path.dirname(__file__),
        ]
        resx = [os.path.abspath(os.path.normpath(i)) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()
