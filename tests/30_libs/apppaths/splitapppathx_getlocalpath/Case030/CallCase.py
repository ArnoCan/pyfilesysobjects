# -*- coding: utf-8 -*-
"""Check defaults.
"""
from __future__ import absolute_import

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
import unittest
from unittest import SkipTest

import platform

from pysourceinfo.helper import getpythonpath_rel
from filesysobjects.apppaths import set_uppertree_searchpath,splitapppathx_getlocalpath,normapppathx, gettop_from_pathstring
from filesysobjects.paths import escapepathx

import testdata
import testdata.filesysobjects
tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = normapppathx(tdata, tpf='posix')

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

        _s = sys.path[:]

        _rtype = 'share'
        _host = 'localhost'
#        _host_share,sp = os.path.splitdrive(os.path.abspath(os.path.dirname(__file__))+os.path.normpath('/a/b///c/d/'))
        _host_share,sp = os.path.splitdrive(tdata + os.path.normpath('/b///c/d/'))

        #_share = 'C$'
        _hs = _host_share.split(os.sep)

        try:
            start = splitapppathx_getlocalpath(('share', _hs[0], _hs[1], sp,))
        except IndexError:
            start = splitapppathx_getlocalpath(('ldsys', '', _hs[0], sp,))

        s = os.sep
        s4 = 4*s
        top = 'pyfilesysobjects' + s4 + 'testdata'
        res = []
        ret = set_uppertree_searchpath(start, top, res,**{'reverse':True}) #@UnusedVariable

        resx = [
            os.path.dirname(testdata.__file__),
            os.path.dirname(testdata.__file__) + '\\filesysobjects',
            os.path.dirname(testdata.__file__) + '\\filesysobjects\\a',
            os.path.dirname(testdata.__file__) + '\\filesysobjects\\a\\b',
            os.path.dirname(testdata.__file__) + '\\filesysobjects\\a\\b\\c',
            os.path.dirname(testdata.__file__) + '\\filesysobjects\\a\\b\\c\\d'
        ]

        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()
