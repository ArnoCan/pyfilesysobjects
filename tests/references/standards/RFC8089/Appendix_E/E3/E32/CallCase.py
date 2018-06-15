""" [RFC8089]_ - Appendix E.3.2. <file> URI with UNC Path

.. seealso:

   It is common to encounter file URIs that encode entire UNC strings in
   the path, usually with all backslash "\" characters replaced with
   slashes "/".

   To interpret such URIs, the "auth-path" rule in Section 2 can be
   replaced with the following: ::

      auth-path = [ file-auth ] path-absolute
                / unc-authority path-absolute

      unc-authority = 2*3"/" file-host

      file-host = inline-IP / IPv4address / reg-name

      inline-IP = "%5B" ( IPv6address / IPvFuture ) "%5D"

   This syntax uses the "IPv4address", "IPv6address", "IPvFuture", and
   "reg-name" rules from [RFC3986].

      Note that the "file-host" rule is the same as "host" but with
      percent-encoding applied to "[" and "]" characters.

   This extended syntax is intended to support URIs that take the
   following forms, in addition to those in Appendix B:

   Non-local files:

   * The representation of a non-local file with an empty authority and
     a complete (transformed) UNC string in the path. For example:

     * "file:////host.example.com/path/to/file"

   * As above, with an extra slash between the empty authority and the
     transformed UNC string, as per the syntax defined in [RFC1738].
     For example:

     * "file://///host.example.com/path/to/file"

     This representation is notably used by the Firefox web browser.
     See Bugzilla#107540 [Bug107540].

   It also further limits the definition of a "local file URI" by
   excluding any file URI with a path that encodes a UNC string.

.. note::

   Transforms to common usage 'as canonical': '////' => '/////'

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
        rfc1738 - rfc8089-F
        """

        arg = "file:////host.example.com/path/to/file"

        if RTE & RTE_WIN32:
            resX = "file://///host.example.com/path/to/file"
        else:
            resX = "file://///host.example.com/path/to/file"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        self.assertEqual(res, resX)

    def testCase020(self):
        """
        rfc1738 - rfc8089-F
        """

        arg = "file://///host.example.com/path/to/file"

        if RTE & RTE_WIN32:
            resX = "file://///host.example.com/path/to/file"
        else:
            resX = "file://///host.example.com/path/to/file"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

