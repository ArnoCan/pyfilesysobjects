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

    def testCase000(self):
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

        self.assertEqual(self.top0ref, self.top0)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

