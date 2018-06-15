from __future__ import absolute_import
import filesysobjects

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

import filesysobjects.userdata

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        user = filesysobjects.userdata.getcurrent_username()
        userappconfig = filesysobjects.userdata.getdir_userappdata()
        if userappconfig not in (
                '/home/' + user + '/.local/share/tests',
                r'C:\Users' + os.sep + user + os.sep + 'AppData' + os.sep + 'Roaming',
                r'C:\Users' + os.sep + user + os.sep + 'AppData' + os.sep + 'Roaming' + os.sep + 'tests',
                ):
            self.skipTest("Current tests by author only.")


#
#######################
#

if __name__ == '__main__':
    unittest.main()

