from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

#
#######################
#

import filesysobjects.paths

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        arg = r'\\w3\\w1\\w2'

        res = filesysobjects.paths.splitpathx(
            arg,
            tpf='posix',
            strip=True,
            apppre=False)
        resX = ('', 'w3', 'w1', 'w2')

        self.assertEqual(res, resX)
        self.assertEqual('\\\\'.join(res), arg)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

