"""Initial raw tests by SubprocessUnit with hard-coded defaults.

Due to the basic character of the test these are done a little more than less.
 
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import filesysobjects.configdata


class CallUnits(unittest.TestCase):

    def setUp(self):   
        self.oldwd = os.getcwd()
        self.pos = os.path.normpath(os.path.dirname(__file__))
        os.chdir(self.pos + os.sep + '..' + os.sep + '..')
        pass

    def tearDown(self):
        os.chdir(self.oldwd)

    def testCase010(self):
        fplist = [
            self.pos + os.sep + 'a',
            self.pos + os.sep + 'b',
            self.pos + os.sep + 'c',
        ]

        res = filesysobjects.configdata.ConfigPath(
            replace=self.pos + os.sep + 'b',
            append=self.pos + os.sep + 'c',
            prepend=self.pos + os.sep + 'a'
            )
        
        assert res.get_config_path_list() == fplist

if __name__ == '__main__':
    unittest.main()
