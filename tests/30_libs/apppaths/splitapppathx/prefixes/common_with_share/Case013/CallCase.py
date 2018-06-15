from __future__ import absolute_import

import unittest
import os

import filesysobjects.apppaths
from filesysobjects import RTE, RTE_WIN32


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"


#
#######################
#


class CallUnits(unittest.TestCase):
    """Split network resources IEEE.1003.1/CIFS/SMB/UNC/URI
    """

    def setUp(self):
        self.kargs = {}
        self.kargs['raw'] = False
        self.kargs['rtype'] = False

    def testCase000(self):

        apstr = 'file://///hostname///////////share/a///b//c////////////////////////'

        if RTE & RTE_WIN32:
            retRef = ('lfsys', '', '', '\\hostname\\share\\a\\b\\c')
        else:
            retRef = ('lfsys', '', '', '/hostname/share/a/b/c')

        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, **self.kargs)[0]
        self.assertEqual(retRef, ret)

    def testCase010(self):

        apstr = 'file://///hostname///////////share/a///b//c////////////////////////'

        if RTE & RTE_WIN32:
            retRef = ('lfsys', '', '', '\\\\\\hostname\\\\\\\\\\\\\\\\\\\\\\share\\a\\\\\\b\\\\c\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
        else:
            retRef = ('lfsys', '', '', '///hostname///////////share/a///b//c////////////////////////')

        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, strip=False, **self.kargs)[0]
        self.assertEqual(retRef, ret)



#
#######################
#

if __name__ == '__main__':
    unittest.main()

