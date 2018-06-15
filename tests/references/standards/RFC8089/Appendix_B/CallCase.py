""" [RFC8089]_ - Appendix B. Example URIs

.. seealso:


   The syntax in Section 2 is intended to support file URIs that take
   the following forms:

   Local files:

   * A traditional file URI for a local file with an empty authority.
     This is the most common format in use today. For example:

     * "file:///path/to/file"

   * The minimal representation of a local file with no authority field
     and an absolute path that begins with a slash "/". For example:

     * "file:/path/to/file"

   Non-local files:

   * A non-local file with an explicit authority. For example:

     * "file://host.example.com/path/to/file"

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

from filesysobjects import RTE, RTE_WIN32
import filesysobjects.apppaths

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase010(self):
        """
        rfc8089
        """

        arg = "file:///path/to/file"

        if RTE & RTE_WIN32:
            resX = "\\path\\to\\file"
        else:
            resX = "/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)
        pass

    def testCase020(self):
        """
        rfc8089
        """

        arg = "file:/path/to/file"

        if RTE & RTE_WIN32:
            resX = "\\path\\to\\file"
        else:
            resX = "/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)
        pass

    def testCase030(self):
        """
        rfc8089
        """
        arg = "file://host.example.com/path/to/file"
        resX = "file://host.example.com/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase031(self):
        """
        rfc8089
        """
        arg = "file://host.example.com/path/to/file"
        resX = "//host.example.com/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=False)
        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

