from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='af90cc0c-de54-4a32-becd-06f5ce5a3a75'

__docformat__ = "restructuredtext en"

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if version in ('2.6',): # pragma: no cover
    import unittest2 as unittest
    from unittest2 import SkipTest
elif version in ('2.7',): # pragma: no cover
    import unittest
    from unittest import SkipTest
else:
    print >>sys.stderr, "ERROR:Requires Python-2.6(.6+) or 2.7"
    sys.exit(1)

import testdata

import filesysobjects.FileSysObjects
import pysourceinfo.PySourceInfo

#
#######################
#


class CallUnits(unittest.TestCase):
    
    def __init__(self,*args,**kargs):
        """Creates search path list
        """
        super(CallUnits,self).__init__(*args,**kargs)    

    # not in 2.6.6
    # @classmethod
    # def setUpClass(cls):

    def setUp(self):
        super(CallUnits, self).setUpClass()
        self._s = sys.path[:]

        # data
        self.myBase = testdata.mypath+os.sep+"findnodes"

        #
        # prefix from unchanged sys.path
        self.mySysPathPrefixRaw = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(__file__) #@UnusedVariable
        
        self.myTestPath0Rel = os.path.normpath('a/b/c/d/e/f/g/h')
        self.myTestPath1Rel = self.myTestPath0Rel +os.sep+ self.myTestPath0Rel
        self.myTestPath2Rel = self.myTestPath1Rel +os.sep+ self.myTestPath0Rel
        
        
        self.myTestPath0 = self.myBase+os.sep+self.myTestPath0Rel #@UnusedVariable
        self.myTestPath1 = self.myBase+os.sep+self.myTestPath1Rel #@UnusedVariable
        self.myTestPath2 = self.myBase+os.sep+self.myTestPath2Rel #@UnusedVariable

    def reset_sys_path(self):
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(self._s)
    

    def testCase010(self):

        pxn = self.myTestPath1

        rpath = self.myTestPath1[-1:]
        plist = [self.myTestPath1[:-1]+os.pathsep+self.myTestPath2[:-1]]
        
        px = filesysobjects.FileSysObjects.findRelPathInSearchPath(rpath,plist,subsplit=True)

        self.reset_sys_path()

        self.assertEqual(px,pxn)
        pass

    def testCase020(self):

        pxn = self.myTestPath2

        rpath = self.myTestPath1[-1:]
        plist = [self.myTestPath2[:-1]+os.pathsep+self.myTestPath1[:-1]]
        
        px = filesysobjects.FileSysObjects.findRelPathInSearchPath(rpath,plist,subsplit=True)

        self.reset_sys_path()

        assert px == pxn 
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

