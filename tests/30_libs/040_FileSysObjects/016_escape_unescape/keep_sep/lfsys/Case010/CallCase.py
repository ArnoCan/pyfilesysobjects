from __future__ import absolute_import
from linecache import getline


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

    def testCase000(self):
        apstr = r'hostname\a\b\c'
        retRef = ('LFSYS','', '', r'hostname\a\b\c') 
        ret = filesysobjects.FileSysObjects.splitAppPrefix(apstr,**{'tpf':'win'})
        self.assertEqual(retRef, ret) 
        
    def testCase001(self):
        apstr = os.path.normpath('hostname/a/b/c')
        retRef = ('LFSYS','', '', 'hostname/a/b/c') 
        ret = filesysobjects.FileSysObjects.escapeFilePath(apstr,'k')
        ret = filesysobjects.FileSysObjects.splitAppPrefix(ret,**{'tpf':'posix'})
        self.assertEqual(retRef, ret) 
        
    def testCase002(self):
        apstr = os.path.normpath('hostname/a/b/c')
        retRef = ('LFSYS','', '', os.path.normpath('hostname/a/b/c')) 
 
        ret = filesysobjects.FileSysObjects.splitAppPrefix(apstr)
        self.assertEqual(retRef, ret) 
 
#
#######################
#

if __name__ == '__main__':
    unittest.main()

