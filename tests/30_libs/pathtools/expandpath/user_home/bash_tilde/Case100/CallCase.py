from __future__ import absolute_import
from __future__ import print_function

import unittest
import os,sys

from filesysobjects import RTE, RTE_WIN32
import filesysobjects.pathtools
import filesysobjects.userdata

import pysourceinfo.helper

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                "@Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"


class CallUnits(unittest.TestCase):
    
    def testCase000(self):

        if RTE & RTE_WIN32:
            self.skipTest("no tilde for home")
        else:
            mypath = "~" + os.sep + "."
        
        res = filesysobjects.pathtools.expandpath(mypath, abs=True)

        resx = filesysobjects.userdata.gethome()

        assert res[0] == resx

        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

