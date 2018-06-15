# -*- coding: utf-8 -*-
""" [RFC1738]_ - 3.13 HTTP

* "../../../g"

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

import filesysobjects.paths
import filesysobjects.apppaths
from filesysobjects import RTE, RTE_WIN32


class UseCase(unittest.TestCase):

    def setUp(self):
        self.arg = "../../../g"
        self.arg1 = "/../../../g"

    def testCase010_normpathx(self):
        if RTE & RTE_WIN32:
            resX = "..\\..\\..\\g"
        else:
            resX = "../../../g"
        res = filesysobjects.paths.normpathx(self.arg)
        self.assertEqual(res, resX)

    def testCase012_normpathx(self):
        if RTE & RTE_WIN32:
            resX = "\\g"
        else:
            resX = "/g"
        res = filesysobjects.paths.normpathx(self.arg1)
        self.assertEqual(res, resX)

    def testCase020_splitpathx(self):
        resX = ('..', '..', '..', 'g',)
        res = filesysobjects.paths.splitpathx(self.arg)
        self.assertEqual(res, resX)

    def testCase021_splitpathx(self):
        resX = ('', 'g',)
        res = filesysobjects.paths.splitpathx(self.arg1)
        self.assertEqual(res, resX)

    def testCase030_escapepathx(self):
        if RTE & RTE_WIN32:
            resX = '../../../g'
        else:
            resX = '../../../g'
        res = filesysobjects.paths.escapepathx(self.arg)
        self.assertEqual(res, resX)

    def testCase040_unescapepathx(self):
        if RTE & RTE_WIN32:
            resX = '../../../g'
        else:
            resX = '../../../g'
        res = filesysobjects.paths.unescapepathx(self.arg)
        self.assertEqual(res, resX)

    def testCase110_normapppathx(self):
        if RTE & RTE_WIN32:
            resX = '..\\..\\..\\g'
        else:
            resX = "../../../g"
        res = filesysobjects.apppaths.normapppathx(self.arg)
        self.assertEqual(res, resX)

    def testCase111_normapppathx(self):
        if RTE & RTE_WIN32:
            resX = '\\g'
        else:
            resX = "/g"
        res = filesysobjects.apppaths.normapppathx(self.arg1)
        self.assertEqual(res, resX)

    def testCase120_splitapppathx(self):
        if RTE & RTE_WIN32:
            resX = ['..\\..\\..\\g']
        else:
            resX = ['../../../g']
        res = filesysobjects.apppaths.splitapppathx(self.arg)
        self.assertEqual(res, resX)

    def testCase121_splitapppathx(self):
        if RTE & RTE_WIN32:
            resX = ['\\g']
        else:
            resX = ['/g']
        res = filesysobjects.apppaths.splitapppathx(self.arg1)
        self.assertEqual(res, resX)

    def testCase122_splitapppathx(self):
        if RTE & RTE_WIN32:
            resX =  [('lfsys', '', '', '..\\..\\..\\g')]
        else:
            resX =  [('lfsys', '', '', '../../../g')]
        res = filesysobjects.apppaths.splitapppathx(self.arg, appsplit=True)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

