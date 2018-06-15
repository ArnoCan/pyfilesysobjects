"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os,sys

from pysourceinfo.helper import getpythonpath_rel
from filesysobjects.apppaths import set_uppertree_searchpath
from filesysobjects.paths import normpathx

#
#######################
#
class CallUnits(unittest.TestCase):
    
    def testCase000(self):
        """Check defaults.
        """
        _s = sys.path[:]

        start = os.path.abspath(os.path.dirname(__file__)+os.sep+'a'+os.sep+'b'+os.sep+'c'+os.sep+'d'+os.sep+'b'+os.sep+'c'+os.sep)
        top = 'tests'
        _res = []
        ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable
        
        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../"))
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx =  [
            'Case030\\a\\b\\c\\d\\b\\c',
            'Case030\\a\\b\\c\\d\\b',
            'Case030\\a\\b\\c\\d',
            'Case030\\a\\b\\c',
            'Case030\\a\\b',
            'Case030\\a',
            'Case030',
        ]
        res = [ normpathx(i) for i in res]
        resx = [normpathx(i) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()
