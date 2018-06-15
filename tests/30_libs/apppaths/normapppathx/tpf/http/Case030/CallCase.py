"""Examples from documents for 'normpathx()'.
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

from filesysobjects.apppaths import normapppathx

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase010(self):
        arg = '\\\\localhost\\C$'
        resX = r'\\localhost\C$'
        
        res = normapppathx(arg, tpf='win')

        self.skipTest("TODO")
        self.assertEqual(res, resX)
        
    def testCase020(self):
        arg = '\\\\localhost\\C$'
        resX = r'//localhost/C$'
        
        res = normapppathx(arg, tpf='posix')

        self.skipTest("TODO")
        self.assertEqual(res, resX)

    def testCase030(self):
        arg = 'http://localhost:8000/a/b///'
        resX = r'//localhost:8000/a/b/'
        
        res = normapppathx(arg, tpf='posix')

        self.assertEqual(res, resX)

    def testCase040(self):
        arg = 'http://localhost:8000/a/b///'
        resX = r'\\localhost:8000\a\b'
        
        res = normapppathx(arg, tpf='win')

        self.assertEqual(res, resX)

    def testCase050(self):
        arg = 'http://localhost:8000/a/b///'
        resX = r'http://localhost:8000/a/b/'
        
        res = normapppathx(arg, tpf='http')

        self.assertEqual(res, resX)

    def testCase060(self):
        arg = 'http://localhost:8000/a/b///'
        resX = r'https://localhost:8000/a/b/'
        
        res = normapppathx(arg, tpf='https')

        self.assertEqual(res, resX)

#     def testCase040(self):
#         arg = '\\\\localhost\\C$'
#         resX = r'file:////localhost/C$'
#         
#         res = normapppathx(arg, tpf='win', apppre=True)
# 
#         self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

