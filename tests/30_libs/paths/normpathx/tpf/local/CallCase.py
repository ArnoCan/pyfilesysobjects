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

import os
import sys
import unittest

from filesysobjects import RTE, RTE_POSIX, RTE_WIN32, V3K

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
        arg = 'd:/'
        if RTE is RTE_WIN32:
            resX = 'd:\\'
        else:
            resX = 'd:'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase002(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:/:d:'

        """
        arg = 'd:/:d:'
        if RTE is RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:/:d:'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase003(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:/:d:/'

        """
        arg = 'd:/:d:/'
        if RTE is RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:/:d:'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase004(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\'

        """
        arg = 'd:\\'
        if RTE is RTE_WIN32:
            resX = 'd:\\'
        else:
            resX = 'd:\\'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase005(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\:d\\'

        """
        arg = 'd:\\:d:\\'
        if RTE is RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:\\:d:\\'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase006(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\;d\\'

        """
        arg = 'd:\\;d:'
        if RTE is RTE_WIN32:
            resX = 'd:\\;d:'
        else:
            resX = 'd:\\;d:'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase007(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\:d\\'

        """
        arg = 'd:\\:d:\\'
        if RTE is RTE_WIN32:
            resX = 'd:\\:d:'
        else:
            resX = 'd:\\:d:\\'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase008(self):
        """
        .. code-block:: python
           :linenos:

           path = 'd:\\;d\\'

        """
        arg = 'd:\\;d:\\'
        if RTE is RTE_WIN32:
            resX = 'd:\\;d:'
        else:
            resX = 'd:\\;d:\\'

        res = normpathx(arg, tpf='local')

        self.assertEqual(res, resX)

    def testCase_009(self):
        """local:

           os.path.normpath() == filesysobjects.paths.normpathx(tpf='local')

        """
        if RTE is RTE_WIN32:
            import ntpath
            x0 = ntpath.normpath('\/')
        else:
            import posixpath
            x0 = posixpath.normpath('\/')

        self.assertEqual(x0, os.path.normpath('\/'))

        x1 = normpathx('\/',tpf='local', strip=False)

        if RTE is RTE_WIN32:
            if V3K:
                self.assertEqual(x0, '\\')
            else:
                try:
                    self.assertEqual(x0, '\\')
                except AssertionError as e:
                    sys.stderr.write(
                        str(e)
                        + "\nERROR:Python: Bug of Python2.7 for win32: '\\\\' instead of '\\'"
                        + '\n'
                        )

        else:
            self.assertEqual(x0, '\\')
        self.assertEqual(x0, x1)


if __name__ == '__main__':
    unittest.main()

