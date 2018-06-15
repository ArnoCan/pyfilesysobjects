from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os
import ntpath
import posixpath

#
#######################
#

import filesysobjects.apppaths
import filesysobjects.paths
import filesysobjects.pathtools
import testdata.filesysobjects
from filesysobjects import RTE, RTE_WIN32
tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase010(self):

        if RTE & RTE_WIN32:
            resX = ntpath.normpath(tdata) + '\\b\\/[^//\\\\]*/\\\\[c][.][p][^/\\\\]*'
        else:
            resX = posixpath.normpath(tdata) + '/b//[^//\\\\]*/\\\\[c][.][p][^/\\\\]*'

        arg0 = filesysobjects.paths.normpathx(tdata, tpf='posix') + '/b/"""/[^//\\\\]*/""""""\\\\[c][.][p][^/\\\\]*"""'

        res0 = filesysobjects.paths.normpathx(arg0, spf='posix')
        res0 = filesysobjects.pathtools.stripquotes(res0)

        self.assertEqual(res0, resX)

    def testCase020(self):

        resX = filesysobjects.paths.normpathx(tdata, tpf='posix') + '/b//[^//\\\\]*/\\\\[c][.][p][^/\\\\]*'

        arg0 = filesysobjects.paths.normpathx(tdata, tpf='posix') + '/b/"""/[^//\\\\]*/""""""\\\\[c][.][p][^/\\\\]*"""'

        res0 = filesysobjects.paths.normpathx(arg0, spf='posix', tpf='posix')
        res0 = filesysobjects.pathtools.stripquotes(res0)

        self.assertEqual(res0, resX)

    def testCase030(self):

        resX = filesysobjects.paths.normpathx(tdata, tpf='win') + '\\b\\/[^//\\\\]*/\\\\[c][.][p][^/\\\\]*'

        arg0 = filesysobjects.paths.normpathx(tdata, tpf='posix') + '/b/"""/[^//\\\\]*/""""""\\\\[c][.][p][^/\\\\]*"""'

        res0 = filesysobjects.paths.normpathx(arg0, spf='posix', tpf='win')
        res0 = filesysobjects.pathtools.stripquotes(res0)

        self.assertEqual(res0, resX)


if __name__ == '__main__':
    unittest.main()

