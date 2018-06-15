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


class CallUnits(unittest.TestCase):

    def testCase000(self):
        s = os.sep
        s10 = 10 * '\\'
        apstr = 'd:'+s+'a'+s10+'b'+s+'c'
        retRef = [
            ('ldsys', '', 'd:', filesysobjects.paths.normpathx(s+'a'+s10+'b'+s+'c', strip=False))
        ]
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='win', strip=False)
        self.assertEqual(retRef, ret)

    def testCase001(self):
        s = os.sep
        s10 = 10*'/'
        appathstr = s+'a'+s10+'b'+s+'c'
        apstr = 'd:'+appathstr
        if RTE & RTE_WIN32:
            retRef = [
                ('lfsys','', '', 'd'),
                ('lfsys','', '', '\\a\\b\\c')  # spf=posix
            ]
        else:
            retRef = [
                ('lfsys','', '', 'd'),
                ('lfsys','', '', '/a/b/c')  # spf=posix
            ]
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='posix')
        self.assertEqual(retRef, ret)

    def testCase002(self):
        s = os.sep
        s10 = 10 * os.sep
        apstr = 'd:'+s+'a'+s10+'b'+s+'c'
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/a/b/c'))]
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, spf='win')
        self.assertEqual(retRef, ret)

    def testCase010(self):
        s = os.sep
        s10 = 10*os.sep
        apstr = 'd:'+s+'a'+s10+'b'+s+'c'
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/a/b/c'))] #FIXME: for whatever reason...
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

    def testCase020(self):
        s = os.sep
        s7 = 7*os.sep
        s10 = 10*os.sep
        apstr = 'd:'+s+'a'+s7+'b'+s+'c'
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/a/b/c'))]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

    def testCase030(self):
        s = os.sep
        s7 = 7*os.sep
        s10 = 10*os.sep
        apstr = 'd:'+s+'a'+s+'b'+s7+'c'
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/a/b/c'))]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

    def testCase050(self):
        s = os.sep
        s7 = 7*os.sep
        s10 = 10*os.sep
        apstr = 'd:'+s
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/'))]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

    def testCase060(self):
        s = os.sep
        s7 = 7*os.sep
        s10 = 10*os.sep
        apstr = 'd:'+s
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/'))]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

