"""Examples from documents for 'normpathx()'.
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

from filesysobjects.paths import normpathx

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase001(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:/'
            
        """
        arg = '\\\:\\\:;'
        resX = '//:/:'
        
        larg = len(arg)
        lresX = len(resX)

        l0 = len(r'\\')
        assert l0 == 2  # OK
        l1 = len(r'\\\:')
        assert l1 == 4  # OK

        l0 = len('\\')
        assert l0 == 1  # OK
        l1 = len('\\\:')
        assert l1 == 3  # Why?

        l1 = len('\\:')
        assert l1 == 2  # Why?

        l1 = len('\:')
        assert l1 == 2  # Why?

        # res = normpathx(arg, tpf='cygwin')

        # self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

