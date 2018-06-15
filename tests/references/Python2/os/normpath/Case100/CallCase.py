"""Examples of 'os.path.normpath()'.
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

from filesysobjects import RTE, RTE_WIN32
import filesysobjects.paths
#
#######################
#


class UseCase(unittest.TestCase):

    def testCase010(self):

        arg = r'/a\/b'
        # ( unesc => /a\/b )

        if RTE & RTE_WIN32:
            resX = '\\a\\b'
        else:
            resX = '/a\/b'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase020(self):

        arg = r'\a\b'
        # ( unesc => /a\\/b )

        if RTE & RTE_WIN32:
            resX = r'\a\b'
        else:
            resX = r'\a\b'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase030(self):

        arg = r'/a\\\/b'
        # ( unesc => /a/b   )

        if RTE & RTE_WIN32:
            resX = r'\a\b'
        else:
            resX = '/a\\\\\/b'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase040(self):

        arg = r'/a\\\\/b'
        # ( unesc => /a\\/b )

        if RTE & RTE_WIN32:
            resX = r'\a\b'
        else:
            resX = '/a\\\\\\\\/b'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase050(self):

        arg = r'/a\\\\/b'
        # ( unesc => /a/b   )

        if RTE & RTE_WIN32:
            resX = r'\a\b'
        else:
            resX = '/a\\\\\\\\/b'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase060(self):

        arg = r'/w////w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = r'\w\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase070(self):

        arg = r'/w////w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase080(self):

        arg = r'/w/w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase090(self):

        arg = r'/w///w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase100(self):

        arg = r'/w//w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase110(self):

        arg = r'/w//w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase120(self):

        arg = r'/w/w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase130(self):

        arg = r'/w/w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase140(self):

        arg = r'/w\\\/w'
        # ( unesc => /w\\/w )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w\\\\\\/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase150(self):

        arg = r'/w\\\/w'
        # ( unesc => /w\\/w )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w\\\\\\/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase160(self):

        arg = r'/w\\\w'
        # ( unesc => /w\\w  )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w\\\\\\w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase170(self):

        arg = r'/w\\\w'
        # ( unesc => /w\\w  )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '/w\\\\\\w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase180(self):

        arg = r'\w\\\/w'
        # ( unesc => \w\\/w )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '\\w\\\\\\/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase190(self):

        arg = r'\w\\\/w'
        # ( unesc => \w\\/w )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '\\w\\\\\\/w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase200(self):

        arg = r'\w\\\\w'
        # ( unesc => \w\\w  )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '\\w\\\\\\\\w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase210(self):

        arg = r'\w\\\\w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '\\w\\\\\\\\w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase220(self):

        arg = r'\w\\\w'
        # ( unesc => \w\\w  )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '\\w\\\\\\w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)

    def testCase230(self):

        arg = r'\w\\\w'
        # ( unesc => /w/w   )

        if RTE & RTE_WIN32:
            resX = '\\w\\w'
        else:
            resX = '\\w\\\\\\w'

        res = os.path.normpath(arg)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

