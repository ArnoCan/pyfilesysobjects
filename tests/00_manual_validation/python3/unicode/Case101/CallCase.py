from __future__ import absolute_import
import filesysobjects

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

from filesysobjects.apppaths import normapppathx

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):

        arg = r'\u0041\u0042/'
        resX = '\\u0041\\u0042/'

        kwargs = {}
        kwargs['spf'] = 'posix'
        kwargs['tpf'] = 'posix'
        kwargs['strip'] = False
        kwargs['delnulpsep'] = True
        kwargs['apppre'] = False

        res = normapppathx(arg, **kwargs)

        # python2 - str: /u0041/u0042/
        # python3 - str: AB/
        self.assertEqual(res, resX)
#
#######################
#

if __name__ == '__main__':
    unittest.main()

