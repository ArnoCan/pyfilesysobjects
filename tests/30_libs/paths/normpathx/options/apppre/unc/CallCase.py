from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import os
import re
import posixpath
import unittest


from filesysobjects import RTE, RTE_WIN32
import filesysobjects.apppaths

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase010(self):

        arg = "file:///c:/path/to/file.txt"

        if RTE & RTE_WIN32:
            resX = "file:///c:/path/to/file.txt"
        else:
            resX = "file:///c:/path/to/file.txt"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase020(self):

        arg = "/some/other/thing.bmp"

        if RTE & RTE_WIN32:
            resX = "file:///some/other/thing.bmp"
        else:
            resX = "file:///some/other/thing.bmp"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase030(self):

        arg = "file:///c:/foo.txt"

        resX = "file:///c:/foo.txt"

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase040(self):
        """This is NOT supported.
        """
        arg = "../bar.txt"

        if RTE & RTE_WIN32:
            resX = "file:///" + re.sub(r'\\', '/', os.path.abspath("..")) + "/bar.txt"
        else:
            resX = "file:///" + os.path.abspath("..") + "/bar.txt"

        # import sys
        # sys.tracebacklimit = 1000

        res = filesysobjects.apppaths.normpathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase041(self):
        """This is NOT supported.
        """
        arg = "file:///../bar.txt"

        if RTE & RTE_WIN32:
            resX = "file:///" + re.sub(r'\\', '/', os.path.abspath("..")) + "/bar.txt"
        else:
            resX = "file:///" + os.path.abspath("..") + "/bar.txt"

        # import sys
        # sys.tracebacklimit = 1000

        res = filesysobjects.apppaths.normpathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)

    def testCase050(self):
        """This is NOT supported.
        """
        arg = "../bar.txt"

        if RTE & RTE_WIN32:
            resX = "file:///" + re.sub(r'\\', '/', os.path.abspath("..")) + "/bar.txt"
        else:
            resX = "file:///" + os.path.abspath("..") + "/bar.txt"

        # import sys
        # sys.tracebacklimit = 1000

        res = filesysobjects.apppaths.normapppathx(arg, appsplit=False, apppre=True)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

