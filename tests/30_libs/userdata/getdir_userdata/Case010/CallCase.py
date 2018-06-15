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

        userhome = filesysobjects.userdata.getdir_userhome()
        userdata = filesysobjects.userdata.getdir_userdata()
        if userdata not in (userhome + '/home/acue/.config', userhome + os.sep + 'AppData' + os.sep + 'Local', ):
            self.skipTest("Current tests by author only.")


#
#######################
#

if __name__ == '__main__':
    unittest.main()

