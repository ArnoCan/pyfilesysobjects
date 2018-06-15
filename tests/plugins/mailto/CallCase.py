"""Examples from documents for 'normapppathx()'.
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

from filesysobjects.apppaths import splitapppathx

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase060(self):
        """
        .. code-block:: python
           :linenos:

           path = 'mailto:John.Doe@example.com'
            
        """
        self.skipTest("Not supported")

#         arg = 'mailto:John.Doe@example.com'
#         resX =  [('mailto', '', '', 'John.Doe@example.com')]
#         res = normapppathx(arg, appsplit=True, tpf='posix')
#         self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

