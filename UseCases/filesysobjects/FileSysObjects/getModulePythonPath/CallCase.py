"""Get the caller name.
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='af90cc0c-de54-4a32-becd-06f5ce5a3a75'

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.FileSysObjects


#
#######################
#

class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase002(self):
        f2 = filesysobjects.FileSysObjects.getCallerModuleFilePathName(2)

        p0 = filesysobjects.FileSysObjects.getPythonPathPrefixMatchFromSysPath(f2)
        p1 = filesysobjects.FileSysObjects.getCallerModulePythonPath(2)
        assert p0 == p1

    def testCase003(self):
        f3 = filesysobjects.FileSysObjects.getCallerModuleFilePathName(2)

        p0 = filesysobjects.FileSysObjects.getPythonPathPrefixMatchFromSysPath(f3)
        p1 = filesysobjects.FileSysObjects.getCallerModulePythonPath(3)
        assert p0 == p1


#
#######################
#

if __name__ == '__main__':
    unittest.main()

