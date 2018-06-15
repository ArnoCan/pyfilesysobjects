from __future__ import absolute_import
import filesysobjects

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

#
#######################
#

import filesysobjects.paths

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        """UNC
        """
        res = filesysobjects.paths.normpathx(
            r'file://///host/share/a/b/c',
            tpf='posix',
            strip=True,
            apppre=False)
        resX = '//host/share/a/b/c'

        self.assertEqual(res, resX)

    def testCase010(self):
        """non-local
        """
        res = filesysobjects.paths.normpathx(
            'file://host/a/b/c',
            tpf='posix',
            strip=True,
            apppre=False)
        resX = '//host/a/b/c'

        self.assertEqual(res, resX)

    def testCase020(self):
        """absolute
        """
        res = filesysobjects.paths.normpathx(
            r'file:///a/b/c',
            tpf='posix',
            strip=True,
            apppre=False)
        resX = '/a/b/c'

        self.assertEqual(res, resX)


    def testCase030(self):
        """min
        """
        res = filesysobjects.paths.normpathx(
            r'file:/a/b/c',
            tpf='posix',
            strip=True,
            apppre=False)
        resX = '/a/b/c'

        self.assertEqual(res, resX)

    def testCase040(self):
        """short
        """
        res = filesysobjects.paths.normpathx(
            r'file:d:/a/b/c',
            tpf='posix',
            strip=True,
            apppre=False)
        resX = 'd:/a/b/c'

        self.assertEqual(res, resX)

    def testCase050(self):
        """absolute drive
        """
        res = filesysobjects.paths.normpathx(
            r'file:///d:/a/b/c',
            tpf='posix',
            strip=True,
            apppre=False)
        resX = '/d:/a/b/c'

        self.assertEqual(res, resX)

    def testCase060(self):
        """absolute DOS drive
        """
        res = filesysobjects.paths.normpathx(
            r'file:///d:/a/b/c',
            tpf='win',
            strip=True,
            apppre=False)
        resX = r'd:\a\b\c'

        self.assertEqual(res, resX)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

