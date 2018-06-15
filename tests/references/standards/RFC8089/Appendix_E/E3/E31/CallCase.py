""" [RFC8089]_ - Appendix E.3.1. <file> URI with Authority

.. seealso:


   The following is an algorithmic description of the process of
   translating a UNC filespace selector string to a file URI by mapping
   the equivalent segments of the two schemes:

   1. Initialize the URI with the "file:" scheme identifier.

   2. Append the authority:

      1. Append the "//" authority sigil to the URI.

      2. Append the host-name field of the UNC string to the URI.

   3. Append the share-name:

      1. Transform the share-name to a path segment (see Section 3.3
         of [RFC3986]) to conform to the encoding rules of Section 2
         of [RFC3986].

      2. Append a delimiting slash character "/" and the transformed
         segment to the URI.

   4. For each object-name:

      1. Transform the objectname to a path segment as above.

         The colon character ":" is allowed as a delimiter before
         stream-name and stream-type in the file-name, if present.

      2. Append a delimiting slash character "/" and the transformed
         segment to the URI.

   For example, the UNC String: ::

      UNC String:   \\host.example.com\Share\path\to\file.txt

   would be transformed into the URI: ::

      URI:          file://host.example.com/Share/path/to/file.txt

   The inverse algorithm for translating a file URI to a UNC filespace
   selector string is left as an exercise for the reader.

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

        arg = r"\\host.example.com\Share\path\to\file.txt"
        resX = "file://///host.example.com/Share/path/to/file.txt"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=True, appsplit=False)
        self.assertEqual(res, resX)

    def testCase020(self):
        """
        rfc1738 - rfc8089-F
        """
        arg = "file://host.example.com/Share/path/to/file.txt"
        resX = "file://host.example.com/Share/path/to/file.txt"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

