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

import filesysobjects.paths

#
#######################
#

class CallUnits(unittest.TestCase):

    def testCase000(self):
        apstr = filesysobjects.apppaths.normapppathx('hostname/a/b/c')
        retRef = ('lfsys', '', '', 'hostname/a/b/c')
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)

    def testCase010(self):
        apstr = 'file://'+filesysobjects.apppaths.normapppathx('hostname/a/b/c', apppre=False)
        retRef = [('rfsys','hostname', '', '/a/b/c')]
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')
        self.assertEqual(retRef, ret)

    def testCase020(self):
        apstr = filesysobjects.apppaths.normapppathx('/hostname/a/b/c', apppre=False)
        retRef = ('lfsys','', '', '/hostname/a/b/c')
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)

    def testCase030(self):
        apstr = 'file://'+filesysobjects.apppaths.normapppathx('/hostname/a/b/c', apppre=False)
        retRef = ('lfsys','', '', '/hostname/a/b/c')
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)

    def testCase040(self):
        apstr = 'file://'+filesysobjects.apppaths.normapppathx('/hostname/a/b/c', apppre=False,**{'tpf':'local'})
        retRef = ('lfsys','', '', '/hostname/a/b/c')
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)

    def testCase041(self):
        apstr = 'file://'+filesysobjects.apppaths.normapppathx('hostname/a/b/c', apppre=False,**{'tpf':'local'})
        retRef = ('rfsys','hostname', '', '/a/b/c')
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

