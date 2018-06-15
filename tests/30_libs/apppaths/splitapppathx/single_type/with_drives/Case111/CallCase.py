# -*- coding: utf-8 -*-
from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import os,sys

import unittest
from unittest import SkipTest

import filesysobjects.apppaths
from filesysobjects import RTE, RTE_WIN32

#
#######################
#


class CallUnits(unittest.TestCase):
    """Network resources IEEE.1003.1/CIFS/SMB/UNC - respect hostname
    Respect 'hostname', which is actual hostname, and a node name.
    """

    # not in 2.6.6
    # @classmethod
    # def setUpClass(self):
    #     self.top = filesysobjects.paths.normpathx('hostname/')
    #     self.start = filesysobjects.paths.normpathx('d://hostname/tests//////a/b/hostname//c////////d/tests/b///c')

    def setUp(self):
        self.top = filesysobjects.paths.normpathx('hostname/')
        self.start = filesysobjects.paths.normpathx('d://hostname/tests//////a/b/hostname//c////////d/tests/b///c')

        self.top0ref=filesysobjects.paths.normpathx('d:/hostname')
        self.top0 = filesysobjects.apppaths.gettop_from_pathstring(self.top, [self.start], spf='win')

        self.topRef0 = [
            ('lfsys', '', '', 'd'),
            ('lfsys', '', '', filesysobjects.paths.normpathx('/hostname'))
        ]
        self.topRef1 = [
            ('ldsys', '', 'd:', filesysobjects.paths.normpathx('/hostname'))
        ]


    def testCase000(self):
        ret = filesysobjects.apppaths.splitapppathx(self.start,appsplit=True)

        if RTE & RTE_WIN32:
            startRef = [
                ('ldsys', '', 'd:', filesysobjects.paths.normpathx('/hostname/tests/a/b/hostname/c/d/tests/b/c'))
            ]
            self.assertEqual(startRef, ret)
        else:
            startRef = [
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', filesysobjects.paths.normpathx('/hostname/tests/a/b/hostname/c/d/tests/b/c'))
            ]
            self.assertEqual(startRef, ret)

    def testCase001(self):
        startRef = [
            ('ldsys', '', 'd:', filesysobjects.paths.normpathx('/hostname/tests/a/b/hostname/c/d/tests/b/c'))
        ]
        ret = filesysobjects.apppaths.splitapppathx(self.start,spf='win',appsplit=True)
        self.assertEqual(startRef, ret)

    def testCase010(self):
        topRef = [('lfsys', '', '', 'hostname')]
        ret = filesysobjects.apppaths.splitapppathx(self.top,appsplit=True)
        self.assertEqual(topRef, ret)


    def testCase020(self):
        self.assertEqual(self.top0ref, self.top0)

    def testCase030(self):

        if RTE & RTE_WIN32:
            ret = filesysobjects.apppaths.splitapppathx(self.top0,appsplit=True)
            self.assertEqual(self.topRef1, ret)
        else:
            ret = filesysobjects.apppaths.splitapppathx(self.top0,appsplit=True)
            self.assertEqual(self.topRef0, ret)

    def testCase031(self):
        ret = filesysobjects.apppaths.splitapppathx(self.top0,appsplit=True,spf='win')
        self.assertEqual(self.topRef1, ret)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

