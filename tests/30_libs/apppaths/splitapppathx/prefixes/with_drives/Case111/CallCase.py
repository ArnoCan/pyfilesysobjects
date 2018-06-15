from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.paths

#
#######################
#


class CallUnits(unittest.TestCase):
    """Network resources IEEE.1003.1/CIFS/SMB/UNC - respect hostname
    """

    def setUp(self):
        self.start = os.path.normpath('d://hostname/tests//////a/b/hostname//c////////d/tests/b///c')
        self.top = os.path.normpath('hostname/')


    def testCase000(self):
        """Respect 'hostname', which is actual hostname, and a node name.
        """
        startRef = ('ldsys', '', 'd:', os.path.normpath('/hostname/tests/a/b/hostname/c/d/tests/b/c'))
        ret = filesysobjects.apppaths.splitapppathx(self.start, appsplit=True, spf='win')[0]
        self.assertEqual(startRef, ret) 

    def testCase010(self):
        """Respect 'hostname', which is actual hostname, and a node name.
        """
        topRef = ('lfsys', '', '', 'hostname')
        ret = filesysobjects.apppaths.splitapppathx(self.top, appsplit=True)[0]
        self.assertEqual(topRef, ret) 

    def testCase020(self):
        """Respect 'hostname', which is actual hostname, and a node name.
        """
        top0ref=os.path.normpath('d:/hostname')
        topRef = ('ldsys', '', 'd:', os.path.normpath('/hostname'))
        top = filesysobjects.apppaths.gettop_from_pathstring(self.top, [self.start], spf='win')
        ret = filesysobjects.apppaths.splitapppathx(top, appsplit=True, spf='win')[0]

        self.assertEqual(top0ref, top) 
        self.assertEqual(topRef, ret) 
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

