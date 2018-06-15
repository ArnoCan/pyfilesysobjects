""" [RFC8089]_ - Appendix D.2. DOS- and Windows-Like Systems

.. seealso:

   When mapping a DOS- or Windows-like file path to a file URI, the
   drive letter (e.g., "c:") is typically mapped into the first path
   segment.

   Appendix E lists some nonstandard techniques for interacting with
   DOS- or Windows-like file paths and URIs.

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

    def testCase040(self):
        """
        rfc8089 - see also Appendix A
        """

        arg = "file:c:/home1/user"

        if RTE & RTE_WIN32:
            resX = "file:///c:/home1/user"
        else:
            resX = "file:///c:/home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

