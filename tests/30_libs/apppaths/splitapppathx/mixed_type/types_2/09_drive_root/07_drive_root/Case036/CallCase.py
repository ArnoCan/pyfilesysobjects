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
        apstr = filesysobjects.paths.normpathx('a:/')

        if RTE & RTE_WIN32:
            retRef = ['a:\\']
        else:
            retRef = ['a:/']

        ret = filesysobjects.apppaths.splitapppathx(apstr, apppre=False, appsplit=False, spf='win', strict=True)
        self.assertEqual(retRef, ret)

    def testCase010(self):
        apstr = filesysobjects.paths.normpathx('c:/')

        if RTE & RTE_WIN32:
            retRef = ['c:\\']
        else:
            retRef = ['c:/']

        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False,spf='win',strict=True)
        self.assertEqual(retRef, ret)

    def testCase020(self):
        apstr = filesysobjects.paths.normpathx('e:/')

        if RTE & RTE_WIN32:
            retRef = ['e:\\']
        else:
            retRef = ['e:/']

        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False,spf='win',strict=True)
        self.assertEqual(retRef, ret)

    def testCase100(self):
        apstr = filesysobjects.paths.normpathx('c:/')
        apstr += ';' + filesysobjects.paths.normpathx('e:/')

        if RTE & RTE_WIN32:
            retRef = ['c:\\', 'e:\\']
        else:
            retRef = ['c:/', 'e:/']

        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False,spf='win',strict=True)
        self.assertEqual(retRef, ret)

    def testCase101(self):
        apstr = filesysobjects.paths.normpathx('c:/')
        apstr += ":" + filesysobjects.paths.normpathx('e:/')

        if RTE & RTE_WIN32:
            retRef = ['c', '\\', 'e', '\\']
        else:
            retRef = ['c', '/', 'e', '/']

        ret = filesysobjects.apppaths.splitapppathx(apstr, apppre=False, appsplit=False, spf='posix', strict=True)
        self.assertEqual(retRef, ret)

    def testCase102(self):
        apstr = filesysobjects.paths.normpathx('c:/')
        apstr += ";" + filesysobjects.paths.normpathx('e:/')

        if RTE & RTE_WIN32:
            retRef = ['c:\\', 'e:\\']
        else:
            retRef = ['c:/', 'e:/']

        ret = filesysobjects.apppaths.splitapppathx(apstr, apppre=False, appsplit=False, spf='win', strict=True)
        self.assertEqual(retRef, ret)

    def testCase200(self):
        apstr = filesysobjects.paths.normpathx('a:/')
        apstr += ';' + "b:/"
        apstr += ';' + filesysobjects.paths.normpathx('c:/')
        apstr += ';' + "d:/"
        apstr += ';' + filesysobjects.paths.normpathx('e:/')
        apstr += ';' + "f:/"
        apstr += ';abc;x:/we'

        if RTE & RTE_WIN32:
            retRef = ['a:\\', 'b:\\', 'c:\\', 'd:\\', 'e:\\', 'f:\\', 'abc', 'x:\\we']
        else:
            retRef = ['a:/', 'b:/', 'c:/', 'd:/', 'e:/', 'f:/', 'abc', 'x:/we']

        ret = filesysobjects.apppaths.splitapppathx(
            apstr,
            apppre=False,
            appsplit=False,
            spf='win',
            strict=True
            )
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

