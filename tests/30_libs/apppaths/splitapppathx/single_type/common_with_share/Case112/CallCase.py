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

import filesysobjects.apppaths

#
#######################
#


class CallUnits(unittest.TestCase):
    """Network resources IEEE.1003.1/CIFS/SMB/UNC - respect hostname
    """

    def testCase000(self):
        """Respect 'hostname', which is actual hostname, and a node name.
        """
        
        start = r'\\hostname\tests\\\\\\a\b\hostname\\c\\\\\\\\d\tests\b\\\c'
        startRef = [('share', 'hostname', 'tests', '\\a\\b\\hostname\\c\\d\\tests\\b\\c')]
        ret = filesysobjects.apppaths.splitapppathx(start,appsplit=True)
        self.assertEqual(startRef, ret) 


        top = 'hostname////////////'
        topRef = [('lfsys', '', '', 'hostname')]
        ret = filesysobjects.apppaths.splitapppathx(top,appsplit=True)
        self.assertEqual(topRef, ret) 


        top0ref=r'\\hostname\tests\a\b\hostname'
        topRef = [('share', 'hostname', 'tests', '\\a\\b\\hostname')]
        top = filesysobjects.apppaths.gettop_from_pathstring(top, [start], tpf='win')
        ret = filesysobjects.apppaths.splitapppathx(top,appsplit=True)

        self.assertEqual(top0ref, top) 
        self.assertEqual(topRef, ret) 
        pass



#
#######################
#

if __name__ == '__main__':
    unittest.main()

