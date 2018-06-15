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
        res = filesysobjects.pathtools.findrelpath_in_searchpath('myfile.*', [os.path.dirname(__file__)])

        # FIXME: 
        # for now ok, the actual order, though the first is defined by 
        # standard lib 'glob', so have a look on platform dependency 
        resx = 'myfile.json'

        self.assertEqual(os.path.basename(res), resx) 


if __name__ == '__main__':
    unittest.main()

