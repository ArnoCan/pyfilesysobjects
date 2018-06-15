from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os
# import sys

import filesysobjects.apppaths

#
#######################
#


class CallUnits(unittest.TestCase):
    """Split network resources IEEE.1003.1/CIFS/SMB/UNC/URI
    """

    def testCase110(self):
        kargs = {}
        kargs['raw'] = True
        kargs['rtype'] = True

        s5 = 5*os.sep
        s15 = 15*os.sep
        s20 = 20*os.sep
        apstr = 'file://///hostname'+s15+'share'+os.sep+'a'+os.sep+'b'+os.sep+'c'+s15
        retRef = ('raw', '', '', 'file://///hostname'+s15+'share'+os.sep+'a'+os.sep+'b'+os.sep+'c'+s15) 
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='win', **kargs)[0]
        
        self.assertEqual(retRef, ret) 


if __name__ == '__main__':
    unittest.main()

