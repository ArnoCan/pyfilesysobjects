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
        apstr = filesysobjects.paths.normpathx('d:/')
        apstr += os.pathsep + "d:/"
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/')
        apstr += os.pathsep + "d:/"
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/')
        apstr += os.pathsep + "d:/"
        apstr += ';abc;x:/we'

        if RTE & RTE_WIN32:
            retRef = [
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('lfsys', '', '', 'abc'),
                ('ldsys', '', 'x:', '\\we')
            ]
            ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True, spf="win")
        else:
            retRef = [
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/;abc;x'),
                ('lfsys', '', '', '/we')
            ]
            ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='posix',strict=True)
        self.assertEqual(retRef, ret)

    def testCase010(self):
        apstr = filesysobjects.paths.normpathx('d:/')
        apstr += os.pathsep + "d:/"
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/')
        apstr += os.pathsep + "d:/"
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/')
        apstr += os.pathsep + "d:/"
        apstr += ';abc;x:/we'

        if RTE & RTE_WIN32:
            retRef = [
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('lfsys', '', '', 'abc'),
                ('ldsys', '', 'x:', '\\we')
            ]
            ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True, spf="win")
        else:
            retRef = ['d', '/', 'd', '/', 'd', '/', 'd', '/', 'd', '/', 'd', '/;abc;x', '/we']
            ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False,spf='posix',strict=True)
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

