""" [RFC8089]_ - Appendix F. Collected Nonstandard Rules

.. seealso:


   Here are the collected syntax rules for all optional appendices,
   presented for convenience. This collected syntax is not normative. ::

      file-URI = file-scheme ":" file-hier-part

      file-scheme = "file"

      file-hier-part = ( "//" auth-path )
                     / local-path

      auth-path  = [ file-auth ] path-absolute
                 / [ file-auth ] file-absolute
                 / unc-authority path-absolute

      local-path = [ drive-letter ] path-absolute
                 / file-absolute

      file-auth = "localhost"
                / [ userinfo "@" ] host

      unc-authority = 2*3"/" file-host

      file-host = inline-IP / IPv4address / reg-name

      inline-IP = "%5B" ( IPv6address / IPvFuture ) "%5D"

      file-absolute = "/" drive-letter path-absolute

      drive-letter = ALPHA ":"
                   / ALPHA "|"

   This collected syntax is intended to support file URIs that take the
   following forms:

   Local files:

   * A traditional file URI for a local file with an empty authority.
     For example:

     * "file:///path/to/file"

   * The minimal representation of a local file with no authority field
     and an absolute path that begins with a slash "/". For example:

     * "file:/path/to/file"

   * The minimal representation of a local file in a DOS- or Windows-
     based environment with no authority field and an absolute path
     that begins with a drive letter. For example:

     * "file:c:/path/to/file"

   * Regular DOS or Windows file URIs with vertical line characters in
     the drive letter construct. For example:

     * "file:///c|/path/to/file"
     * "file:/c|/path/to/file"
     * "file:c|/path/to/file"

   Non-local files:

   * The representation of a non-local file with an explicit authority.
     For example:

     * "file://host.example.com/path/to/file"

   * The "traditional" representation of a non-local file with an empty
     authority and a complete (transformed) UNC string in the path.
     For example:

     * "file:////host.example.com/path/to/file"

   * As above, with an extra slash between the empty authority and the
     transformed UNC string. For example:

     * "file://///host.example.com/path/to/file"

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
        arg = "file:///path/to/file"
        resX = "file:///path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase011(self):
        arg = "file:///path/to/file"
        if RTE & RTE_WIN32:
            resX = "\\path\\to\\file"
        else:
            resX = "/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=False)
        self.assertEqual(res, resX)

    def testCase020(self):
        arg = "file:/path/to/file"
        resX = "file:///path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase030(self):
        arg = "file:c:/path/to/file"
        resX = "file:///c:/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase040(self):
        arg = "file:c:/path/to/file"
        resX = "file:///c:/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase050(self):
        arg = "file://host.example.com/path/to/file"
        resX = "file://host.example.com/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase060(self):
        """Normallize to 5*'/'
        """
        arg = "file:////host.example.com/path/to/file"
        resX = "file://///host.example.com/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase070(self):
        """Normallize to 5*'/'
        """
        arg = "file://///host.example.com/path/to/file"
        resX = "file://///host.example.com/path/to/file"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)



if __name__ == '__main__':
    unittest.main()

