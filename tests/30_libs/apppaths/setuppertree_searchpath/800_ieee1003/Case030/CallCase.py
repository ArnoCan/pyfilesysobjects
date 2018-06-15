# -*- coding: utf-8 -*-
"""Check defaults.
"""
from __future__ import absolute_import

import os,sys
import unittest
from unittest import SkipTest

import platform

from pysourceinfo.helper import getpythonpath_rel
from filesysobjects.apppaths import set_uppertree_searchpath,splitapppathx_getlocalpath,gettop_from_pathstring
from filesysobjects.paths import escapepathx

from testdata.filesysobjects import mypath

#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase002(self):
        self.maxDiff = None

        #for now windows only
        if platform.system() != 'Windows':
            unittest.SkipTest("Requires Windows - skipped!")
            return True
        if not os.path.exists('\\\\localhost\\C$'):
            unittest.SkipTest("Requires share for this test - skipped!")
            return True

        _sys = sys.path[:]

        _rtype = 'share'
        _host = 'localhost'
        _share_host, sp = os.path.splitdrive(mypath + os.path.normpath('/a/b///c/d///'))
        _s = _share_host.split(os.sep)
        try:
            start = splitapppathx_getlocalpath((_rtype, _s[0], _s[1], sp,))
        except IndexError:
            start = splitapppathx_getlocalpath((_rtype, '', _s[0], sp,))

        s = os.sep
        s4 = 4*s
        top = 'filesysobjects'+s4
        _res = []
        ret = set_uppertree_searchpath(start,top,_res,**{'reverse':True}) #@UnusedVariable

        resx = [
            mypath,
            mypath + '\\a',
            mypath + '\\a\\b',
            mypath + '\\a\\b\\c',
            mypath + '\\a\\b\\c\\d'
        ]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)

        self.assertEqual(resx, _res)
        pass

if __name__ == '__main__':
    unittest.main()
