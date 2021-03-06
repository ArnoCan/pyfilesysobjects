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
        apstr += os.pathsep + "b:/"
        apstr += os.pathsep + filesysobjects.paths.normpathx('c:/')
        apstr += os.pathsep + "d:/"
        apstr += os.pathsep + filesysobjects.paths.normpathx('e:/')
        apstr += os.pathsep + "f:/"
        apstr += ';abc;x:/we'

        if RTE & RTE_WIN32:
            retRef = ['a:\\', 'b:\\', 'c:\\', 'd:\\', 'e:\\', 'f:\\', 'abc', 'x:\\we']
        else:
            retRef =  ['a:/:b:/:c:/:d:/:e:/:f:/', 'abc', 'x:/we']

        ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=False,spf='win')
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

