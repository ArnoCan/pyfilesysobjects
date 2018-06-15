"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os,sys

from filesysobjects.apppaths import set_uppertree_searchpath
from filesysobjects.paths import unescapepathx


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
        self.maxDiff = None
        _s = sys.path[:]

        start = os.path.abspath(os.path.dirname(__file__))
        top = None
        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable

        resx = [
            os.path.abspath(os.path.dirname(__file__)),
        ]
        resx = [os.path.normpath(i) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        res = [unescapepathx(i) for i in res]
        resx = [unescapepathx(i) for i in resx]

        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()
