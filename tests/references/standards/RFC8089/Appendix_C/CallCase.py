# -*- coding: utf-8 -*-
""" [RFC8089]_ - Appendix C. sSimilar Technologies

.. seealso:


   * The WHATWG URL specification [WHATWG-URL] defines browser behavior
     for a variety of inputs, including file URIs. As a living
     document, it changes to reflect updates in browser behavior. As a
     result, its algorithms and syntax definitions may or may not be
     consistent with this specification. Implementors should be aware
     of this possible discrepancy if they expect to share file URIs
     with browsers that follow the WHATWG specification.

   * The Universal Naming Convention (UNC) [MS-DTYP] defines a string
     format that can perform a similar role to the file URI scheme in
     describing the location of files, except that files located by UNC
     filespace selector strings are typically stored on a remote
     machine and accessed using a network protocol. Appendix E.3 lists
     some ways in which UNC filespace selector strings are currently
     made to interoperate with the file URI scheme.

   * The Microsoft Windows API defines Win32 Namespaces
     [Win32-Namespaces] for interacting with files and devices using
     Windows API functions. These namespaced paths are prefixed by
     "\\\\\\\\?\\\\" for Win32 File Namespaces and "\\\\\\\\.\\\\" for Win32 Device
     Namespaces. There is also a special case for UNC file paths in
     Win32 File Namespaces, referred to as "Long UNC", using the prefix
     "\\\\\\\\?\\\\UNC\". This specification does not define a mechanism for
    translating namespaced paths to or from file URIs.

.. warning::

   Not yet implemented.

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

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase001(self):

        self.skipTest("Not yet implemented: Windows Name Spaces")

if __name__ == '__main__':
    unittest.main()

