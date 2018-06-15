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
from filesysobjects.apppaths import splitapppathx, splitapppathx_getlocalpath


#
#######################
#
class CallUnits(unittest.TestCase):

    def testCase100(self):
        
        _in = "file:c:\\a\\b\\c"
        resX = [
            "c:\\a\\b\\c",
        ]

        _r = splitapppathx(_in, appsplit=True, tpf='win')
        for i in range(len(_r)): 
            res = splitapppathx_getlocalpath(_r[i])
            self.assertEqual(res, resX[i])


    def testCase200(self):
        
        _in = "file:c:\\a\\b\\c"
        resX = [
            "c:/a/b/c",
        ]

        _r = splitapppathx(_in, appsplit=True, tpf='posix')
        for i in range(len(_r)): 
            res = splitapppathx_getlocalpath(_r[i])
            self.assertEqual(res, resX[i])

if __name__ == '__main__':
    unittest.main()
