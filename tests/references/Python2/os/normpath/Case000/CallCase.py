"""Examples of 'os.path.normpath()'.
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
import os

from filesysobjects import RTE, RTE_WIN32

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase001(self):

        arg = 'd:/'

        if RTE & RTE_WIN32:
            resX = 'd:\\'
        else:
            resX = 'd:'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase002(self):

        arg = 'd:/:d:'

        if RTE & RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:/:d:'

        res = os.path.normpath(arg)

        self.assertEqual(res, resX)

    def testCase003(self):

        arg = 'd:/:d:/'

        if RTE & RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:/:d:'

        res = os.path.normpath(arg)

        self.assertEqual(res, resX)

    def testCase004(self):

        arg = 'd:\\'

        if RTE & RTE_WIN32:
            resX = 'd:\\'
        else:
            resX = 'd:\\'

        res = os.path.normpath(arg)

        self.assertEqual(res, resX)

    def testCase005(self):

        arg = 'd:\\:d:\\'

        if RTE & RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:\\:d:\\'

        res = os.path.normpath(arg)

        self.assertEqual(res, resX)

    def testCase006(self):

        arg = 'd:\;d:'

        if RTE & RTE_WIN32:
            resX = 'd:\\;d:'
        else:
            resX = 'd:\\;d:'

        res = os.path.normpath(arg)

        self.assertEqual(res, resX)

    def testCase007(self):

        arg = 'd:\\:d:\\'

        if RTE & RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:\\:d:\\'

        res = os.path.normpath(arg)

        self.assertEqual(res, resX)

    def testCase008(self):

        arg = 'd:\\;d:\\'

        if RTE & RTE_WIN32:
            resX = 'd:\\;d:'
        else:
            resX = 'd:\\;d:\\'

        res = os.path.normpath(arg)

        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

