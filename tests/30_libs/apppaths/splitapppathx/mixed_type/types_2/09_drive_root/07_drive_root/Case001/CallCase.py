from __future__ import absolute_import

import unittest
import os,sys

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

    def testCase000(self):
        apstr =  "d:"
        apstr += ':' + "e:"
        if RTE & RTE_WIN32:
            retRef = ['d::e:']
        else:
            retRef =  ['d', '', 'e', '']
        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False,delnulpsep=False,strip=False)
        self.assertEqual(retRef, ret)

    def testCase001(self):
        apstr =  "d:"
        apstr += ':' + "d:"
        if RTE & RTE_WIN32:
            retRef = ['d::d:']
        else:
            retRef =  ['d', 'd']
        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False,delnulpsep=True,strip=True)
        self.assertEqual(retRef, ret)

    def testCase002(self):
        apstr =  "d:"
        apstr += ':' + "d:"
        if RTE & RTE_WIN32:
            retRef = ['d::d:']
        else:
            retRef =  ['d', 'd']
        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False)
        self.assertEqual(retRef, ret)

    def testCase010(self):
        apstr =  "d:"
        apstr += os.pathsep + "d:"
        if RTE & RTE_WIN32:
            retRef = [('ldsys', '', 'd:', ''), ('ldsys', '', 'd:', '')]
        else:
            retRef = [
                ('lfsys','', '', 'd'),
                ('lfsys','', '', ''),
                ('lfsys','', '', 'd'),
                ('lfsys','', '', ''),
            ]
        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=True,delnulpsep=False)
        self.assertEqual(retRef, ret)

    def testCase011(self):
        apstr =  "d:"
        apstr += os.pathsep + "d:"
        if RTE & RTE_WIN32:
            retRef = [('ldsys', '', 'd:', ''), ('ldsys', '', 'd:', '')]
        else:
            retRef = [
                ('lfsys','', '', 'd'),
                ('lfsys','', '', 'd'),
            ]
        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=True,delnulpsep=True)
        self.assertEqual(retRef, ret)

    def testCase020(self):
        apstr =  "d:"
        apstr += os.pathsep + "d:"
        apstr += os.pathsep
        if RTE & RTE_WIN32:
            retRef = [('ldsys', '', 'd:', ''), ('ldsys', '', 'd:', ''), ('lfsys', '', '', '')]
        else:
            retRef = [
                ('lfsys','', '', 'd'),
                ('lfsys','', '', ''),
                ('lfsys','', '', 'd'),
                ('lfsys','', '', ''),
                ('lfsys','', '', ''),
            ]
        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=True,delnulpsep=False)
        self.assertEqual(retRef, ret)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

