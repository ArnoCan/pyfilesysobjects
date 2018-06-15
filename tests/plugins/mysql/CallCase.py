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


class UseCase(unittest.TestCase):

    def testCase010(self):
        """
        .. code-block:: python
           :linenos:

           path = 'mysql://glance:$GLANCE_MYSQL_PASSWORD@controller/glance'
            
        """
#         arg = 'mysql://glance:$GLANCE_MYSQL_PASSWORD@controller/glance'
#         res = splitapppathx(arg, appsplit=True, tpf='posix')
# 
#         resX =  [('mysql', 'glance:$GLANCE_MYSQL_PASSWORD@controller', '/glance', '')]
#         self.assertEqual(res, resX)
        self.skipTest("not implemented")


if __name__ == '__main__':
    unittest.main()

