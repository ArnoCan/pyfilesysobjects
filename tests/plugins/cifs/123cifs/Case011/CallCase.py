from __future__ import absolute_import


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
    pass

    def testCase000(self):
        apstr = filesysobjects.apppaths.normapppathx('//hostname/share/a/b/c',**{'tpf':'win'})
        retRef = ('share','hostname', 'share', filesysobjects.apppaths.normapppathx('/a/b/c', apppre=False,**{'tpf':'posix'}))
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)

    def testCase010(self):
        apstr = filesysobjects.apppaths.normapppathx('cifs://hostname/share/a/b/c', apppre=False,**{'tpf':'win'})
        retRef = ('share','hostname', 'share', filesysobjects.apppaths.normapppathx('/a/b/c', apppre=False,**{'tpf':'posix'}))
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)

    def testCase020(self):
        apstr = filesysobjects.apppaths.normapppathx('file://///hostname/share/a/b/c', apppre=False,**{'tpf':'win'})
        retRef = ('share','hostname', 'share', filesysobjects.apppaths.normapppathx('/a/b/c', apppre=False,**{'tpf':'posix'}))
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True, tpf='posix')[0]
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

