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
        https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head:/frameworks/python/

        Current version requires %-encoding in the path part of URIs only due implementation detail.

        https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head%3A/frameworks/python/

        """
        arg = 'https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head%3A/frameworks/python/'

        resX = [('https', 'bazaar.launchpad.net', '', '/~jakob-simon-gaarde/ladon/trunk/files/head%3A/frameworks/python/', '')]

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=True, apppre=False)
        self.assertEqual(res, resX)

    def testCase020(self):
        """
        https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head:/frameworks/python/
        """

        self.skipTest("available next release")

        arg = "https://'''bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head:/frameworks/python/'''"

        resX = "https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head:/frameworks/python/"

        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

    def testCase030(self):
        """
        https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head:/frameworks/python/
        """

        self.skipTest("available next release")

        arg = "https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head[:]/frameworks/python/"

        resX = "https://bazaar.launchpad.net/~jakob-simon-gaarde/ladon/trunk/files/head:/frameworks/python/"

        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

