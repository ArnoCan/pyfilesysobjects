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
from filesysobjects import RTE, RTE_WIN32

#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase000(self):
        apstr = "d:"
        apstr += os.pathsep + "d:"
        if RTE & RTE_WIN32:
            retRef = [
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', ';d'),
            ]
        else:
            retRef = [
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', 'd'),
            ]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='posix')
        self.assertEqual(retRef, ret)



#
#######################
#

if __name__ == '__main__':
    unittest.main()

