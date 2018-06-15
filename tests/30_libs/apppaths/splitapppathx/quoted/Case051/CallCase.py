from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

#
#######################
#

import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects

from filesysobjects import W_RE, RTE, RTE_WIN32

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase010(self):

        arg = tdata + '/b/*/c.p"""[!:]*"""'
        if RTE & RTE_WIN32:
            resX = [tdata + '\\b\\*\\c.p[!:]*']
        else:
            resX = [tdata + '/b/*/c.p[!:]*']

        res = filesysobjects.apppaths.splitapppathx(arg, stripquote=True)

        self.assertEqual(res, resX)

    def testCase020(self):

        arg = tdata + '/b/*/c.p"""[!;]*"""'
        if RTE & RTE_WIN32:
            resX = [tdata + '\\b\\*\\c.p[!;]*']
        else:
            resX = [tdata + '/b/*/c.p[!;]*']

        res = filesysobjects.apppaths.splitapppathx(arg, stripquote=True)

        self.assertEqual(res, resX)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

