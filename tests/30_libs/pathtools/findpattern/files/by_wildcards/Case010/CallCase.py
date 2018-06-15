"""Check default values, and with defaults as passed parameters.
"""
from __future__ import absolute_import
from __future__ import print_function

_author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.6'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import testdata.filesysobjects

from filesysobjects.pathtools import findpattern
from filesysobjects.paths import normpathx

#
#######################
#

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = normpathx(tdata, tpf='posix')

class UseCase(unittest.TestCase):

    def testCase006_normpath(self):
        """Check os.path.sep within normapth for regexpr.
        """
        np = tdata + normpathx('/[^/]+/*/[c]+.sh', tpf='posix')
        S = os.path.sep
        npX = tdata+S+'[^/]+'+S+'*'+S+'[c]+.sh'
        npX = normpathx(npX, tpf='posix')
        self.assertEqual(np, npX)


if __name__ == '__main__':
    unittest.main()

