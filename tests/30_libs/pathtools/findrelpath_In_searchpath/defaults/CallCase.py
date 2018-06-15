# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
import unittest
from unittest import SkipTest

import filesysobjects.pathtools

#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase000(self):
        try:
            px = filesysobjects.pathtools.findrelpath_in_searchpath() #@UnusedVariable
        except Exception as e:
            if type(e) is TypeError:
                return
            raise
        pass

    def testCase001(self):
        px = filesysobjects.pathtools.findrelpath_in_searchpath('')
        self.assertIsNone(px) 
        pass

    def testCase002(self):
        px = filesysobjects.pathtools.findrelpath_in_searchpath(None)
        self.assertIsNone(px) 
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

