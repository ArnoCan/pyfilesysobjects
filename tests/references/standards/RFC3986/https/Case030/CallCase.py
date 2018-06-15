""" [RFC4516]_ - 4. Examples
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
        https://my.domain.com/my/path/?myarg0:myarg1
        """

        arg = 'https://my.domain.com/my/path/?myarg0""":"""myarg1'

        resX = [('https', 'my.domain.com', '', '/my/path/', '?myarg0""":"""myarg1')]
        
        res = filesysobjects.apppaths.normapppathx(arg, appsplit=True, apppre=False)
        self.assertEqual(res, resX)

    def testCase020(self):
        """
        https://my.domain.com/my/path/?myarg0:myarg1
        """

        arg = "https://my.domain.com/my/path/?myarg0:myarg1"

        resX = "https://my.domain.com/my/path/?myarg0:myarg1"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

