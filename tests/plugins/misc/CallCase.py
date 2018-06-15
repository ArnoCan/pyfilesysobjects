"""Examples from documents for 'normapppathx()'.
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

from filesysobjects.apppaths import splitapppathx

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase020(self):
        """
        RFC 3689

        .. code-block:: python
           :linenos:

           path = 'http://www.ics.uci.edu/pub/ietf/uri/#Related'
            
        """
        arg = 'http://www.ics.uci.edu/pub/ietf/uri/#Related'
        resX = [('http', 'www.ics.uci.edu', '', '/pub/ietf/uri/#Related', '')]
        res = splitapppathx(arg, appsplit=True, tpf='posix')
        self.assertEqual(res, resX)

    def testCase040(self):
        """
        .. code-block:: python
           :linenos:

           path = 'http://www.ietf.org/rfc/rfc2396.txt'
            
        """
        arg = 'http://www.ietf.org/rfc/rfc2396.txt'
        resX = [('http', 'www.ietf.org', '', '/rfc/rfc2396.txt', '')]
        res = splitapppathx(arg, appsplit=True, tpf='posix')
        self.assertEqual(res, resX)

    def testCase090(self):
        """
        .. code-block:: python
           :linenos:

           path = 'tel:+1-816-555-1212'
            
        """

        self.skipTest("Not supported")

#         arg = 'tel:+1-816-555-1212'
#         resX = [('tel', '', '', '+1-816-555-1212')]
#         res = normapppathx(arg, appsplit=True, tpf='posix')
#         self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

