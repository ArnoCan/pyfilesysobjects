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

from filesysobjects.apppaths import normapppathx

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
        arg = 'd:/'
        resX = 'd:/'
        
        res = normapppathx(arg, tpf='posix', spf='win', apppre=False)

        self.assertEqual(res, resX)
        
    def testCase002(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:/:e:'
            
        """
        arg = 'd:/:e:'
        resX = 'd:/:e:'
        
        res = normapppathx(arg, spf='win', tpf='posix', apppre=False)

        self.assertEqual(res, resX)

    def testCase003(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:/:e:/'
            
        """
        arg = 'd:/:e:/'
        resX = 'd:/:e:/'
        
        res = normapppathx(arg, spf='win', tpf='posix', apppre=False)

        self.assertEqual(res, resX)

    def testCase004(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\'
            
        """
        arg = 'd:\\'
        resX = 'd:/'
        
        res = normapppathx(arg, spf='win', tpf='posix', apppre=False)

        self.assertEqual(res, resX)

    def testCase005(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\:e:\\'
            
        """
        arg = 'd:\\:e:\\'
        resX = 'd:/:e:/'
        
        res = normapppathx(arg, spf='win', tpf='posix', apppre=False)

        self.assertEqual(res, resX)

    def testCase006(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\;e:'
            
        """
        arg = 'd:\\;e:'
        resX = 'd:/:e:'
        
        res = normapppathx(arg, spf='win', tpf='posix', apppre=False)

        self.assertEqual(res, resX)

    def testCase007(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\:e:\\'
            
        """
        arg = 'd:\\:e:\\'
        resX = 'd:/:e:/'
        
        res = normapppathx(arg, spf='win', tpf='posix', apppre=False)

        self.assertEqual(res, resX)

    def testCase008(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\;e:\\'
            
        """
        arg = 'd:\\;e:\\'
        resX = 'd:/:e:/'
        
        res = normapppathx(arg, spf='win', tpf='posix', apppre=False)

        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

