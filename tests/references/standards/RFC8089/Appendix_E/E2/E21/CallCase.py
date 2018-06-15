""" [RFC8089]_ - Appendix E.2. Relative Resolution

.. seealso:


   To mimic the behavior of DOS- or Windows-like file systems, relative
   references beginning with a slash "/" can be resolved relative to the
   drive letter when present; resolution of ".." dot segments (per
   Section 5.2.4 of [RFC3986]) can be modified to not ever overwrite the
   drive letter.

   For example: ::

      base URI: file:///c:/path/to/file.txt
      base URI: /some/other/thing.bmp
      resolved: file:///c:/some/other/thing.bmp

      base URI: file:///c:/foo.txt
      rel. ref.: ../bar.txt
      resolved: file:///c:/bar.txt

   A relative reference starting with a drive letter would be
   interpreted by a generic URI parser as a URI with the drive letter as
   its scheme. Instead, such a reference ought to be constructed with a
   leading slash "/" character (e.g., "/c:/foo.txt").

   Relative references with a drive letter followed by a character other
   than a slash (e.g., "/c:bar/baz.txt" or "/c:../foo.txt") might not be
   accepted as dereferenceable URIs in DOS- or Windows-like systems.

"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import os
import re
import posixpath
import unittest


from filesysobjects import RTE, RTE_WIN32,PathError
import filesysobjects.apppaths

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase010(self):
        """D.2. DOS- and Windows-Like Systems
        """

        arg = "file:///c:/path/to/file.txt"

        if RTE & RTE_WIN32:
            resX = "file:///c:/path/to/file.txt"
        else:
            resX = "file:///c:/path/to/file.txt"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase020(self):
        """Appendix B. Example URIs
        """

        arg = "/some/other/thing.bmp"

        if RTE & RTE_WIN32:
            resX = "file:///some/other/thing.bmp"
        else:
            resX = "file:///some/other/thing.bmp"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase030(self):
        """D.2. DOS- and Windows-Like Systems
        """

        arg = "file:///c:/foo.txt"

        resX = "file:///c:/foo.txt"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase040(self):
        """Appendix B. Example URIs
        """
        arg = "../bar.txt"

        try:
            res = filesysobjects.apppaths.normpathx(arg, appsplit=False, apppre=True)
        except PathError:
            pass

    def testCase041(self):
        """Appendix B. Example URIs
        """
        arg = "file:///../bar.txt"

        try:
            res = filesysobjects.apppaths.normpathx(arg, appsplit=False, apppre=True)
        except PathError:
            pass

    def testCase050(self):
        """Appendix B. Example URIs
        """
        arg = "../bar.txt"

        try:
            res = filesysobjects.apppaths.normpathx(arg, appsplit=False, apppre=True)
        except PathError:
            pass


if __name__ == '__main__':
    unittest.main()

