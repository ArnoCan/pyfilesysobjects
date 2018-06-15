"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os,sys

from pysourceinfo.helper import getpythonpath_rel
from filesysobjects.apppaths import set_uppertree_searchpath


#
#######################
#
class CallUnits(unittest.TestCase):
    

    
    

    #
    # Create by object
    #
    def testCase000(self):
        """Check defaults.
        """
        _s = sys.path[:]

        start = os.path.dirname(__file__)+os.sep+'a'+os.sep+'b'+os.sep+'c'+os.sep+'d'+os.sep+'b'+os.sep+'c'+os.sep
        start = os.path.abspath(start)
        top = 'tests'
        _res = []
        ret = set_uppertree_searchpath(start,top,_res,**{'reverse':True}) #@UnusedVariable
        
        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__) + "/.." * 2))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx = [
            '300_reverse', 
            '300_reverse/Case030', 
            '300_reverse/Case030/a', 
            '300_reverse/Case030/a/b', 
            '300_reverse/Case030/a/b/c', 
            '300_reverse/Case030/a/b/c/d', 
            '300_reverse/Case030/a/b/c/d/b', 
            '300_reverse/Case030/a/b/c/d/b/c'
        ]
        resx = [os.path.normpath(i) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        # print("4TEST:")
        # print("#---")
        # for i in resx:
        #     print(i)
        # print("#---")
        # for i in res:
        #     print(i)

        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()
