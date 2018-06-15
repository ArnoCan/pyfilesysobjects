""" [RFC8089]_ - Appendix A. Differences from Previous Specifications

.. seealso:

   Differences from Previous Specifications
   The syntax definition in Section 2 inherits incremental differences
   from the general syntax of [RFC1738], as described by Appendix G of
   [RFC2396] and Appendix D of [RFC3986].
   According to the definition in [RFC1738], a file URL always started
   with the token "file://", followed by an (optionally blank) host name
   and a "/". The syntax given in Section 2 makes the entire authority
   component, including the double slashes "//", optional.

   .. note::

      The *filesysobjects* supports:
      
      * the long form resulting from RFC1738 for UNCs see RFC8089 Appendix F.
      
      * the short form resulting from RFC1738 for files, and drives.
      

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

        arg = "file:////home1/user"

        if RTE & RTE_WIN32:
            resX = "\\\\home1\\user"
        else:
            resX = "//home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

    def testCase011(self):
        """
        rfc1738 - rfc8089-F
        """

        arg = "file://///home1////.////user///.//a/b/../.."

        if RTE & RTE_WIN32:
            resX = "\\home1\\user"
        else:
            resX = "/home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

    def testCase012(self):
        """
        rfc1738 - rfc8089-F
        """

        arg = "file://////.//.//home1////.////user///.//a/b/../.."

        if RTE & RTE_WIN32:
            resX = "\\home1\\user"
        else:
            resX = "/home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

    def testCase020(self):
        """
        rfc1738
        """

        arg = "file:///home1/user"

        if RTE & RTE_WIN32:
            resX = "\\home1\\user"
        else:
            resX = "/home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

    def testCase030(self):
        """
        rfc8089
        """

        arg = "file:/home1/user"

        if RTE & RTE_WIN32:
            resX = "\\home1\\user"
        else:
            resX = "/home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

    def testCase040(self):
        """
        rfc8089
        """

        arg = "file:c:/home1/user"

        if RTE & RTE_WIN32:
            resX = "c:\\home1\\user"
        else:
            resX = "c:/home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

