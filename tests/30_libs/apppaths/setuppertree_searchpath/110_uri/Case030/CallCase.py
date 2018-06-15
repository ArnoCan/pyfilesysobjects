"""Check IEEE1003.1-Chap. 4.2.
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
        _s = sys.path[:]
        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        start = 'file://'+os.path.abspath(os.path.dirname(__file__)+os.sep+D)
        top = 'a/b'
        _res = []
        ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable
        
        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../../"))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx = ['110_uri/Case030/a/b/c/d', '110_uri/Case030/a/b/c', '110_uri/Case030/a/b']
        res = [normpathx(i) for i in res]
        resx = [normpathx(i) for i in resx]
        
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        

        assert resx == res

    def testCase001(self):
        _s = sys.path[:]
        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        start = 'file://'+os.path.normpath(os.path.abspath(os.path.dirname(__file__)+os.sep+D))
        top = os.path.normpath('a/b')
        _res = []
        ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable

        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../../"))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx =  ['110_uri\\Case030\\a\\b\\c\\d', '110_uri\\Case030\\a\\b\\c', '110_uri\\Case030\\a\\b']
        res = [normpathx(i) for i in res]
        resx = [normpathx(i) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        
        self.assertEqual(resx, res)
        pass

    def testCase002(self):
        _s = sys.path[:]
        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        start = 'file://'+os.path.normpath(os.path.abspath(os.path.dirname(__file__)+os.sep+D))
        top = os.path.normpath('a/b')
        _res = []
        ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable

        mypos = os.path.abspath(os.path.normpath(os.path.dirname(__file__)+"/../../"))   
        res = []
        for i in range(len(_res)):
            pr = getpythonpath_rel(_res[i],[mypos])
            if pr:
                res.append(pr)
        resx =  ['110_uri\\Case030\\a\\b\\c\\d', '110_uri\\Case030\\a\\b\\c', '110_uri\\Case030\\a\\b']
        res = [normpathx(i) for i in res]
        resx = [normpathx(i) for i in resx]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        
        assert resx == res
        pass

#FIXME: seems to be not required for now
#     def testCase010(self):
#         _s = sys.path[:]
#         A = os.path.normpath('a/A.txt')         #@UnusedVariable
#         B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
#         C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
#         D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable
# 
#         start = 'file://'+os.path.normpath(os.path.abspath(os.path.dirname(__file__)+os.sep+D))
# #        top = 'file://'+os.path.normpath('a/b')
#         top = os.path.normpath('a/b')
#         _res = []
#         ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable
# 
#         forDebugOnly = sys.path #@UnusedVariable
#         
#         res = []
#         for i in range(len(_res)):
#             res.append(getpythonpath_rel(_res[i])) 
#         resx = [
#             '30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b/c/d', 
#             '30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b/c', 
#             '30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b'
# #             'tests/30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b/c/d', 
# #             'tests/30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b/c', 
# #             'tests/30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b'
#         ]
#         resx = map(os.path.normpath,resx)
# 
#         [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
#         sys.path.extend(_s)
#         
#         
#         print
#         print("-----")
#         print("4TEST:resx=  "+str(resx))
#         print("-----")
#         print("4TEST:res =   "+str(res))
# 
#         self.assertEqual(resx,res)
#         pass

    def testCase011(self):
#FIXME:
#         _s = sys.path[:]
#         A = os.path.normpath('a/A.txt')         #@UnusedVariable
#         B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
#         C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
#         D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable
# 
#         start = 'file://///'+os.path.normpath(os.path.abspath(os.path.dirname(__file__)+os.sep+D))
#         top = 'file://///'+os.path.normpath('a/b')
#         _res = []
#         ret = set_uppertree_searchpath(start,top,_res) #@UnusedVariable
# 
#         forDebugOnly = sys.path #@UnusedVariable
#         
#         res = []
#         for i in range(len(_res)):
#             res.append(getpythonpath_rel(_res[i])) 
#         resx = [
#             'tests/30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b/c/d', 
#             'tests/30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b/c', 
#             'tests/30_libs/040_filesysobjects/070_set_uppertree_searchpath/110_uri/Case030/a/b'
#         ]
#         resx = map(os.path.normpath, resx)
# 
#         [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
#         sys.path.extend(_s)
# 
#         assert resx == res
        pass


if __name__ == '__main__':
    unittest.main()
