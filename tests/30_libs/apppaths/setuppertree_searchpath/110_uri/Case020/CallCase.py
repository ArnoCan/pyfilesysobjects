"""Check IEEE1003.1-Chap. 4.2.
"""
from __future__ import absolute_import

import unittest
import os,sys

from pysourceinfo.helper import getpythonpath_rel
from filesysobjects.apppaths import set_uppertree_searchpath
import filesysobjects


#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase000(self):
        _s = sys.path[:]
        #FIXME: Check and fix start = 'file://'+os.path.abspath(os.path.dirname(__file__))
        start = 'file://'+os.path.abspath(os.path.dirname(__file__))
        top = 'tests'
        _res = []
        ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable
        
        forDebugOnly = sys.path #@UnusedVariable
        
        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../../"))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx = [
            '110_uri/Case020', 
            '110_uri', 
        ]                
        resx = [filesysobjects.paths.normpathx(i) for i in resx]
        
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        self.assertEqual(resx ,res)
        pass

    def testCase001(self):
        _s = sys.path[:]
        start = 'file://'+os.path.abspath(os.path.dirname(__file__))
        top = 'tests'
        _res = []
        ret = set_uppertree_searchpath(start,top,_res,**{'reverse':True}) #@UnusedVariable
        
        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../../"))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx = ['110_uri', '110_uri\\Case020']
        resx = [filesysobjects.paths.normpathx(i) for i in resx]
        
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        
        self.assertEqual(resx, res)

    def testCase010(self):
        _s = sys.path[:]
        start = 'file://'+os.path.abspath(os.path.dirname(__file__))
        top = 'tests'
        _res = []
        ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable
        
        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../../"))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx = ['110_uri\\Case020', '110_uri',]
        resx = [filesysobjects.paths.normpathx(i) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        assert resx == res

    def testCase011(self):
        _s = sys.path[:]
        start = 'file://'+os.path.abspath(os.path.dirname(__file__))
        top = 'tests'
        _res = []
        ret = set_uppertree_searchpath(start,top,_res,**{'reverse':True}) #@UnusedVariable
        
        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../../"))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx =  ['110_uri', '110_uri\\Case020']
        resx = [filesysobjects.paths.normpathx(i) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)        

        assert resx == res


if __name__ == '__main__':
    unittest.main()
