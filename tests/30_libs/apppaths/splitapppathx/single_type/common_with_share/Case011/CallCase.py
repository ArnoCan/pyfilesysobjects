from __future__ import absolute_import

import unittest
import os

import filesysobjects.apppaths
from filesysobjects import RTE, RTE_WIN32, PathError


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

from filesysobjects import RTE_FILEURI, RTE_FILEURI0, RTE_FILEURI4, RTE_FILEURI5, RTE_POSIX


class CallUnits(unittest.TestCase):

    def testCase000(self):
        apstr = '//hostname/share/a/b/c'
        retRef = [('share','hostname', 'share', '\\a\\b\\c')]
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True)
        self.assertEqual(retRef, ret)

    def testCase001(self):
        apslist = ('share','hostname', 'share', '/a/b/c')
        resx = '//hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, apppre=False, tpf=RTE_POSIX)
        self.assertEqual(resx, res)

    def testCase002(self):
        """RFC8089 - E.3.1 """
        apslist = ('share','hostname', 'share', '/a/b/c')
        resx = 'file://hostname/share/a/b/c'

#         x0 = filesysobjects.apppaths.join_apppathx_entry(apslist, apppre=False, tpf=RTE_POSIX)
#         x1 = filesysobjects.apppaths.normapppathx("//hostname/share/a/b/c", apppre=True, tpf=RTE_POSIX)

        res = filesysobjects.apppaths.join_apppathx_entry(apslist, apppre=True, tpf=RTE_POSIX)
        self.assertEqual(resx, res)

    def testCase003(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file://hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI)
        self.assertEqual(resx, res)

    def testCase004(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file://hostname/share/a/b/c'
        try:
            res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI0)
        except PathError:
            pass

    def testCase005(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file:////hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI4)
        self.assertEqual(resx, res)

    def testCase006(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file://///hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI5)
        self.assertEqual(resx, res)

    def testCase010(self):
        apstr = 'smb://hostname/share/a/b/c'
        retRef = [('smb','hostname', 'share', '/a/b/c')]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True)
        self.assertEqual(retRef, ret)

    def testCase020(self):
        apslist = ('share','hostname', 'share', '/a/b/c')
        resx = 'file://hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI)
        self.assertEqual(resx, res)

    def testCase021(self):
        apstr = 'file://///hostname/share/a/b/c'
        retRef = [('share','hostname', 'share', '\\a\\b\\c')]
        ret = filesysobjects.apppaths.splitapppathx(apstr, appsplit=True)
        self.assertEqual(retRef, ret)

    def testCase022(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file:////hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI4)
        self.assertEqual(resx, res)

    def testCase023(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file://///hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI5)
        self.assertEqual(resx, res)

    def testCase030(self):
        apstr = 'file:////hostname/share/a/b/c'
        retRef = [('share','hostname', 'share', '\\a\\b\\c')]
        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True)
        self.assertEqual(retRef, ret)

    def testCase031(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file://hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI)
        self.assertEqual(resx, res)

    def testCase032(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        try:
            res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI0)  # @UnusedVariable
        except PathError:
            pass

    def testCase033(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file:////hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI4)
        self.assertEqual(resx, res)

    def testCase034(self):
        apslist = ('share','hostname', 'share', '/a/b/c')

        resx = 'file://///hostname/share/a/b/c'
        res = filesysobjects.apppaths.join_apppathx_entry(apslist, tpf=RTE_FILEURI5)
        self.assertEqual(resx, res)

if __name__ == '__main__':
    unittest.main()

