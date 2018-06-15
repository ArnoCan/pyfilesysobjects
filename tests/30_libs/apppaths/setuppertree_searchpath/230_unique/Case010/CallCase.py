from __future__ import absolute_import

import unittest
import os,sys

from filesysobjects.apppaths import set_uppertree_searchpath

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

        start = os.path.dirname(os.path.dirname(__file__)+os.sep+D)
        start = os.path.abspath(start)
        top = os.path.dirname(__file__)
        top = os.path.abspath(top)
        res_ = [
            os.path.dirname(__file__),
            os.path.dirname(os.path.dirname(__file__)+os.sep+C),
            os.path.dirname(os.path.dirname(__file__)+os.sep+A),
        ]
        res = [os.path.normpath(os.path.abspath(i)) for i in res_]
        ret = set_uppertree_searchpath(start,top,res,**{'unique':True, 'append':True }) #@UnusedVariable

        resx_ = [
            os.path.dirname(__file__),
            os.path.dirname(os.path.dirname(__file__)+os.sep+C),
            os.path.dirname(os.path.dirname(__file__)+os.sep+A),
            os.path.dirname(os.path.dirname(__file__)+os.sep+D),
            os.path.dirname(os.path.dirname(__file__)+os.sep+B),
        ]
        resx = [os.path.normpath(os.path.abspath(i)) for i in resx_]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
                
        assert resx == res
        pass

if __name__ == '__main__':
    unittest.main()
