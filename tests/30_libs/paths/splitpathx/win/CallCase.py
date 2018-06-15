"""Examples from documents for 'normpathx()'.
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import unittest

from filesysobjects import RTE, RTE_WIN32
from filesysobjects.paths import splitpathx

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"


class UseCase(unittest.TestCase):

#     def testCase001(self):
#         arg = '"""d"""'
#         resX = r'\\localhost\C$'
#
#         res = normpathx(arg, tpf='posix')
#
#         self.assertEqual(res, resX)


    def testCase010(self):

#         if RTE & RTE_WIN32:
#             tpf = 'win'
#         else:
#             tpf = 'cnw'

        tpf = 'win'

        kargs = {
            'apppre': False,
            'keepsep': False,
            'stripquote': False,
            'tpf': tpf,
            'psep': ';;',
            'sep': '\\',
            'strip': True
        }
        arg = '/.\\file_at_current_dir'

        res = splitpathx(arg, **kargs)

        resX = ('', r'file_at_current_dir')
        self.assertEqual(res, resX)

        resX = os.sep + r'file_at_current_dir'
        self.assertEqual(os.sep.join(res), resX)


if __name__ == '__main__':
    unittest.main()

