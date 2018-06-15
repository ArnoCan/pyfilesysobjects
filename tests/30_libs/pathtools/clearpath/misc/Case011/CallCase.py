from __future__ import absolute_import
from __future__ import print_function
from linecache import getline

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.pathtools
import pysourceinfo.helper

#
#######################
#


class CallUnits(unittest.TestCase):
    
    def testCase000(self):

        plistRaw = [
            "/a1/b/c"+os.pathsep+"/a1/b/c",
        ]        
        plist = [os.path.normpath(i) for i in plistRaw]
        
        filesysobjects.pathtools.clearpath(plist,**{'split':True,'redundant':True,'shrink':True,}) # here just a demo
        plistRef = [
            "/a1/b/c",
        ]
        plistRef = [os.path.normpath(i) for i in plistRef]

        assert plist == plistRef
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

