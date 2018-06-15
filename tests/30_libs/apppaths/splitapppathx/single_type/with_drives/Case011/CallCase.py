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

    def testCase000(self):
        apstr = 'd:/a/b/c'
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/a/b/c'))]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

    def testCase010(self):
        apstr = filesysobjects.paths.normpathx('d:a/b/c')
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('a/b/c'))]
        ret0 = filesysobjects.apppaths.splitapppathx(apstr, apppre=False, appsplit=False, tpf='posix', spf='win32')
        ret1 = os.pathsep.join(ret0)
        if ret1[0] == os.pathsep: # if a platform requires it for join of single !?
            ret1 = ret1[1:]
        ret2 = filesysobjects.paths.escapepathx(ret1)
        ret3 = filesysobjects.apppaths.splitapppathx(ret2,appsplit=True,spf='win')
        self.assertEqual(retRef, ret3)

    def testCase020(self):
        apstr = 'd:'
        retRef = [('ldsys','', 'd:', '')]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

    def testCase030(self):
        apstr = 'd:'+filesysobjects.paths.normpathx('/')
        retRef = [('ldsys','', 'd:', filesysobjects.paths.normpathx('/'))]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win')
        self.assertEqual(retRef, ret)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

