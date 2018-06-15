""" [RFC8089]_ - Appendix E.2.2. Vertical Line Character

.. seealso:


   Historically, some usages of file URIs have included a vertical line
   character "|" instead of a colon ":" in the drive letter construct.
   [RFC3986] forbids the use of the vertical line; however, it may be
   necessary to interpret or update old URIs.

   For interpreting such URIs, the "auth-path" and "local-path" rules in
   Section 2 and the "drive-letter" rule above can be replaced with the
   following: ::

      auth-path   = [ file-auth ] path-absolute
                  / [ file-auth ] file-absolute

      local-path  = [ drive-letter ] path-absolute
                  / file-absolute

      file-absolute = "/" drive-letter path-absolute

      drive-letter = ALPHA ":"
                   / ALPHA "|"

   This is intended to support regular DOS or Windows file URIs with
   vertical line characters in the drive letter construct. For example:

   * "file:///c|/path/to/file"
   * "file:/c|/path/to/file"
   * "file:c|/path/to/file"

   To update such an old URI, replace the vertical line "|" with a colon
   ":".

.. warning::

   This is not supported:
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

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase020(self):

        pass


if __name__ == '__main__':
    unittest.main()

